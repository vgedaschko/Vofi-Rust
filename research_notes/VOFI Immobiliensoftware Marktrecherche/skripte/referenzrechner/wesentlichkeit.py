"""Messskript zur Wesentlichkeitsschwelle (Spezifikation, Zeile "Wesentlichkeit und Eingabensparsamkeit").

Variiert je Gegenstand eine Groesse gegenueber dem Basisfall und gibt die Wirkung aus
  - auf den hoechsten tragbaren Preis (Ankauf: Kaufpreis, Neubau: Grundstueckspreis) in Euro und Prozent,
  - auf die VOFI-Rendite nach Steuern beim eingegebenen Preis in Prozentpunkten.
Stand: nach der Umsetzung der Durchsicht vom 2026-11-21 (docs/pruefung/2026-11-21-wesentlichkeit/durchsicht.md); die
dort entfallenen Eingaben, Vorgaben und Schalter sind nicht mehr Gegenstand. Die Zahlen der Durchsicht stammen aus
dem Stand davor.
Gegenstaende: Eingaben (E-..), Vorgaben des Hauses (H-..), Lesarten der Modellannahmen (MA-..), die Steuerregeln
des Kapitels 7 gegen die Lehrbuchform und Rechenregeln aus Sonderfaellen der Pruefrunden.

Das Skript misst nur. Es aendert kein Modul, keinen Sollwert und nicht erwartete_werte.json; es ist kein
Referenzfall und wird von referenzfaelle.py nicht aufgerufen.

    python3 wesentlichkeit.py [--ausgabe DATEI.json] [--nur GRUPPE[,GRUPPE]] [--ohne-preis]

Bezug der Preiswirkung: beim Ankauf der tragbare Kaufpreis. Beim Neubau ist der tragbare Grundstueckspreis ein
Residuum von rund einem Zwoelftel der Gesamtkosten; ein Prozent von ihm sind rund 0,08 % der Investition. Deshalb
gibt das Skript dort zwei Werte aus: Prozent des Grundstueckspreises und Prozent der Gesamtkosten beim tragbaren
Preis (Grundstueck, Erwerbsnebenkosten, Baukosten). "Ueber der Schwelle" heisst: Rendite ueber 0,1 Prozentpunkten
oder Preiswirkung ueber 1 % des Kaufpreises (Ankauf) oder der Gesamtkosten (Neubau); die engere Zaehlung nach dem
Grundstueckspreis steht im Feld ueber_schwelle_grundstueck.

Gruppen: eingabe, vorgabe, lesart, steuer, regel. Die Preissuche laeuft mit grobem Raster (10 Stuetzstellen,
Nachsuche 2 Euro); fuer die Messung in Prozent genuegt das. Im gefoerderten Neubau gibt es bei 5 % Zielrendite
keinen tragbaren Preis und die Suche ueber 38 Jahre ist teuer: dort wird nur die Rendite gemessen.
"""
import json
import sys
import time
from dataclasses import replace
from decimal import Decimal as D

import annahmen as A
from grobkalkulation import Meldung, rechne_grob, _tragbarer_preis
from rf_grob import VG, KAT, KATN, GEFOERDERT, MIT_KFW
from steuer import (KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST, GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN,
                    PRIVAT, BEFREIT)

SCHWELLE_PREIS = D("0.01")          # 1 % des tragbaren Preises
SCHWELLE_RENDITE = D("0.001")       # 0,1 Prozentpunkte
MESSRASTER = dict(suchraster=10, nachsuchfenster=2)

AN, NB, KFW, GEF = "Ankauf", "Neubau frei", "Neubau KfW", "Neubau gefoerdert"
FAELLE = {AN: (A.ANKAUF, VG, KAT, True), NB: (A.NEUBAU, VG, KATN, True), KFW: (MIT_KFW, VG, KATN, True),
          GEF: (GEFOERDERT, VG, KATN, False)}
ALLE, NEUBAU, FREI = (AN, NB, KFW, GEF), (NB, KFW, GEF), (AN, NB, KFW)


# ------------------------------------------------------------------ Bausteine der Variationen
def E(**kw):
    return lambda e, v, k: (replace(e, **kw), v, k)


def V(**kw):
    return lambda e, v, k: (e, replace(v, **kw), k)


def K(**kw):
    return lambda e, v, k: (e, v, replace(k, **kw))


def S(**kw):
    return lambda e, v, k: (replace(e, steuer=replace(e.steuer, **kw)), v, k)


def ST(**kw):
    return lambda e, v, k: (e, replace(v, stress=replace(v.stress, **kw)), k)


def F(**kw):
    return lambda e, v, k: (replace(e, foerderung=replace(e.foerderung, **kw)), v, k)


def KF(**kw):
    return lambda e, v, k: (e, v, replace(k, kfw=replace(k.kfw, **kw)))


def UE(**kw):
    return lambda e, v, k: (replace(e, uebernommen=dict(e.uebernommen, **kw)), v, k)


def status(st, **kw):
    return lambda e, v, k: (replace(e, steuer=A.steuer(st, **kw)), v, k)


def nach(*fs):
    def f(e, v, k):
        for g in fs:
            e, v, k = g(e, v, k)
        return e, v, k
    return f


GLEICH = lambda e, v, k: (e, v, k)
GEBUNDEN = E(gebunden_anteil=D("0.4"), bindung_jahre=6, gebundene_miete=D("6.80"))
UEBERNOMMEN = E(uebernommen=dict(restschuld=D(500000), nennbetrag=D(600000), zins=D("0.005"), tilgungssatz=D("0.02"),
                                 bindung_jahre=8, anschluss_zins=D("0.03"), beitrag_satz=D(0)))
STAFFEL_PLUS = [(0, D("10.80")), (22, D("13.80")), (32, D("16.80"))]
LUECKE = E(ist_miete=D("7.00"))                      # Ist-Miete 24 % unter der Vergleichsmiete
GROSS = E(wohnflaeche=D(13200), einheiten=200, kaufpreis=D(24000000), angebotspreis=D(26000000), stau_betrag=D(1200000))


# ------------------------------------------------------------------ Gegenstaende
# (Kennung, Gruppe, worum es geht, Spanne der Variation, kostet, Faelle, Variation[, Basis[, Stressfall]])
GEGENSTAENDE = [
    # ---- a) Eingaben mit Voreinstellung oder freiwillig; Pflichteingaben stehen in PFLICHT
    ("E-02", "eingabe", "Stichtag (Katalogstand je Kalenderjahr)", "2027 -> 2029", "Eingabe", FREI, E(stichtag_jahr=2029)),
    ("E-05", "eingabe", "Lage im Gebiet: Kappungsgrenze", "im Gebiet (15 %) -> ausserhalb (20 %)", "Eingabe", (AN,), E(im_kappungsgebiet=False)),
    ("E-05", "eingabe", "Lage im Gebiet: Mietpreisbremse, 200 m2 leer", "im Gebiet -> ausserhalb", "Eingabe", (AN,),
     E(im_bremsgebiet=False), E(leere_flaeche=D(200))),
    ("E-11", "eingabe", "Erwerbsnebenkosten", "Voreinstellung -> 3 Prozentpunkte weniger", "Eingabe", (AN,), E(enk_satz=D("0.07"))),
    ("E-11", "eingabe", "Erwerbsnebenkosten", "8 % -> 6,5 %", "Eingabe", (NB,), E(enk_satz=D("0.065"))),
    ("H-39", "vorgabe", "Bodenanteil als Hauswert (Koerperschaft)", "25 % -> 35 %", "Hauswert", (AN,), V(bodenanteil=D("0.35"))),
    ("E-12", "eingabe", "Bodenanteil bei der Privatperson (kein Ausgleich beim steuerfreien Verkauf)", "25 % -> 35 %", "Eingabe", (AN,),
     E(bodenanteil=D("0.35")), status(PRIVAT)),
    ("E-16", "eingabe", "Marktmiete im Ankauf (wirkt nur bei leerer Flaeche und Fluktuation)", "10,50 -> 9,50 Euro", "Eingabe", (AN,), E(markt_miete=D("9.50"))),
    ("E-17", "eingabe", "Baujahr (Instandhaltungsstaffel nach Gebaeudealter)", "1990 -> 2008", "Eingabe", (AN,), E(baujahr=2008)),
    ("E-18", "eingabe", "Angebotspreis (nur Abstand zum Angebot)", "2,6 -> 2,8 Mio. Euro", "Eingabe", (AN,), E(angebotspreis=D(2800000))),
    ("E-23", "eingabe", "Vorlauf bis zum Baubeginn", "0 -> 12 Monate", "Eingabe", (NB,), E(vorlauf_monate=12)),
    ("E-24", "eingabe", "Festpreis des Bauvertrags", "nein -> ja", "Eingabe", (NB,), E(festpreis=True)),
    ("E-25", "eingabe", "Kennzeichen des Kostenkennwerts (200 bis 700 statt 300 und 400)", "2.320 mit Zuschlaegen -> 2.900 gesamt", "Eingabe", (NB,),
     E(kostenkennwert=D(2900), kennwert_gesamt=True)),
    ("E-26", "eingabe", "Bauzeit", "18 -> 24 Monate", "Eingabe", (NB,), E(bauzeit_monate=24)),
    ("E-27", "eingabe", "Stellplaetze", "0 -> 20 zu 60 Euro Miete", "Eingabe", (NB,), E(stellplaetze=20, stellplatz_miete=D(60))),
    ("E-31", "eingabe", "leerstehende Flaeche am Stichtag", "0 -> 200 m2", "Eingabe", (AN,), E(leere_flaeche=D(200))),
    ("E-31", "eingabe", "leerstehende Flaeche am Stichtag", "0 -> 600 m2 (45 %)", "Eingabe", (AN,), E(leere_flaeche=D(600))),
    ("E-32", "eingabe", "sonstige Ertraege", "0 -> 6.000 Euro im Jahr", "Eingabe", (AN,), E(sonstige_ertraege=D(6000))),
    ("E-33", "eingabe", "Mietenhistorie", "nicht angegeben -> letzte Erhoehung vor 6 Monaten, 7,50 Euro vor drei Jahren", "Eingabe", (AN,),
     E(mietenhistorie=(6, D("7.50")))),
    ("E-34", "eingabe", "CO2-Ausstoss (auch E-54, E-55 als Naeherung)", "30 -> 45 kg je m2", "Eingabe", (AN,), E(co2_ausstoss=D(45))),
    ("E-35", "eingabe", "KfW-Darlehen", "0 -> 3 Mio. Euro (35 Jahre, 1 Freijahr)", "Eingabe", (NB,),
     E(kfw_betrag=D(3000000), kfw_laufzeit=35, kfw_tilgungsfrei=1)),
    ("E-36", "eingabe", "KfW-Laufzeitvariante", "35/1 -> 10/2", "Eingabe", (KFW,), E(kfw_laufzeit=10, kfw_tilgungsfrei=2)),
    ("E-36", "eingabe", "KfW-Laufzeitvariante", "35/1 -> 25/3", "Eingabe", (KFW,), E(kfw_laufzeit=25, kfw_tilgungsfrei=3)),
    ("E-37", "eingabe", "KfW mit Qualitaetssiegel (hoeherer Hoechstbetrag)", "3,0 -> 4,5 Mio. Euro", "Eingabe", (KFW,),
     E(kfw_qng=True, kfw_betrag=D(4500000))),
    ("E-38", "eingabe", "Zins des KfW-Darlehens", "2,5 % -> 3,0 %", "Eingabe", (KFW,), E(kfw_zins=D("0.03"))),
    ("E-39", "eingabe", "Vorvermietung", "nein -> ja", "Eingabe", (NB,), E(vorvermietet=True)),
    ("E-41", "eingabe", "Kennzeichen erweiterte Kuerzung", "nein -> ja", "Eingabe", (AN, NB), S(erweiterte_kuerzung=True)),
    ("E-42", "eingabe", "Steuersatz der Personen (Personengesellschaft)", "42 % -> 35 %", "Eingabe", (AN,),
     status(GEWERBLICHE_PG, est_satz=D("0.35")), status(GEWERBLICHE_PG)),
    ("E-42", "eingabe", "Steuersatz der Personen (Privatperson)", "42 % -> 35 %", "Eingabe", (AN,),
     status(PRIVAT, est_satz=D("0.35")), status(PRIVAT)),
    ("E-43", "eingabe", "Anteil natuerlicher Personen", "100 % -> 60 %", "Eingabe", (AN,),
     status(GEWERBLICHE_PG, anteil_natuerliche=D("0.6")), status(GEWERBLICHE_PG)),
    ("H-38", "vorgabe", "Verlustverrechnung als Hauswert (MA-016)", "Vortrag -> sofort", "Hauswert", (AN, NB, GEF), S(verlust="sofort")),
    ("E-46", "eingabe", "Zinsbindung", "10 -> 5 Jahre", "Eingabe", (AN, NB), E(zinsbindung_jahre=5)),
    ("E-46", "eingabe", "Zinsbindung", "10 -> 15 Jahre", "Eingabe", (AN, NB), E(zinsbindung_jahre=15)),
    ("E-48", "eingabe", "Haltedauer", "12 -> 10 Jahre", "Eingabe", (AN,), E(haltedauer=10)),
    ("E-48", "eingabe", "Haltedauer", "12 -> 15 Jahre", "Eingabe", (AN,), E(haltedauer=15)),
    ("E-48", "eingabe", "Haltedauer", "15 -> 20 Jahre", "Eingabe", (NB,), E(haltedauer=20)),
    ("E-50", "eingabe", "Investitionsstau: Betrag", "120.000 -> 240.000 Euro", "Eingabe", (AN,), E(stau_betrag=D(240000))),
    ("E-51", "eingabe", "Investitionsstau: Jahr der Ausfuehrung", "Jahr 2 -> Jahr 5", "Eingabe", (AN,), E(stau_jahr=5)),
    ("H-23", "vorgabe", "Anpassungsdauer der Ist-Miete (Katalogwert)", "4 -> 1 Jahr", "Katalogwert", (AN,), V(anpassungsdauer=1)),
    ("E-56", "eingabe", "gebundener Bestand (E-56 bis E-58)", "0 -> 40 % bis Jahr 6 zu 6,80 Euro", "Eingabe", (AN,), GEBUNDEN),
    ("E-57", "eingabe", "Bindungsende", "Jahr 6 -> Jahr 10", "Eingabe", (AN,), E(bindung_jahre=10), GEBUNDEN),
    ("E-58", "eingabe", "gebundene Miete", "6,80 -> 7,50 Euro", "Eingabe", (AN,), E(gebundene_miete=D("7.50")), GEBUNDEN),
    ("E-59", "eingabe", "uebernommenes Darlehen", "keines -> 500.000 Euro zu 0,5 %", "Eingabe", (AN,), UEBERNOMMEN),
    ("E-59", "eingabe", "uebernommenes Darlehen: Anschlusszins", "3 % -> 5 %", "Eingabe", (AN,), UE(anschluss_zins=D("0.05")), UEBERNOMMEN),
    ("E-59", "eingabe", "uebernommenes Darlehen: Nennbetrag als Bezug der Rate", "600.000 -> Restschuld 500.000", "Eingabe", (AN,),
     UE(nennbetrag=D(500000)), UEBERNOMMEN),
    ("E-60", "eingabe", "verfuegbares Eigenkapital (zweite Preisgrenze)", "leer -> 1,2 Mio. Euro", "Eingabe", (AN,), E(verfuegbares_ek=D(1200000))),
    ("E-62", "eingabe", "Erbbauzins", "0 -> 12.000 Euro im Jahr", "Eingabe", (AN,), E(erbbauzins=D(12000))),
    ("E-64", "eingabe", "Tilgungssatz des Bankdarlehens", "2 % -> 3 %", "Eingabe", (AN, NB), E(tilgungssatz=D("0.03"))),
    ("E-65", "eingabe", "nachhaltige Miete der Bank im Neubau", "16,50 -> 15,00 Euro", "Eingabe", (NB,), E(nachhaltige_miete=D("15.00"))),
    ("E-69", "eingabe", "erweiterte Kuerzung bleibt im Verkaufsjahr", "nein -> ja", "Eingabe", (AN, NB),
     S(kuerzung_bleibt_verkaufsjahr=True), S(erweiterte_kuerzung=True)),
    ("E-70", "eingabe", "Verteilung des Zuschusses beantragt (Privatperson)", "nein -> ja", "Eingabe", (GEF,),
     E(zuschuss_verteilung=True), status(PRIVAT)),
    # ---- b) Vorgaben des Hauses
    ("H-01", "vorgabe", "Zielrendite", "5 % -> 4,5 %", "Vorgabe", FREI, V(zielrendite=D("0.045"))),
    ("H-02", "vorgabe", "Beleihungsquote", "65 % -> 60 %", "Vorgabe", FREI, V(beleihungsquote=D("0.60"))),
    ("H-02", "vorgabe", "Beleihungsquote", "65 % -> 50 %", "Vorgabe", FREI, V(beleihungsquote=D("0.50"))),
    ("H-03", "vorgabe", "Mindestdeckung", "1,2 -> 1,3", "Vorgabe", FREI, V(mindestdeckung=D("1.3"))),
    ("H-03", "vorgabe", "Mindestdeckung", "1,2 -> 1,1", "Vorgabe", FREI, V(mindestdeckung=D("1.1"))),
    ("H-04", "vorgabe", "Mindesttilgung", "2 % -> 1 %", "Vorgabe", (AN, NB), nach(V(mindesttilgung=D("0.01")), E(tilgungssatz=D("0.01")))),
    ("H-05", "vorgabe", "Anschlussaufschlag", "1 -> 2 Prozentpunkte", "Vorgabe", FREI, V(anschluss_aufschlag=D("0.02"))),
    ("H-08", "vorgabe", "kurzfristiger Habenzins", "2 % -> 1 %", "Vorgabe", ALLE, V(h_kurz=D("0.01"))),
    ("H-09", "vorgabe", "langfristiger Anlagezins der Alternative", "gleich Habenzins -> 3 %", "Vorgabe", (AN, NB), V(a_lang=D("0.03"))),
    ("H-10", "vorgabe", "Kontokorrentzins", "8 % -> 6 %", "Vorgabe", (GEF,), V(kk_zins=D("0.06"))),
    ("H-11", "vorgabe", "Kontokorrentlinie", "0 -> 250.000 Euro", "Vorgabe", (AN, NB), V(kk_linie=D(250000))),
    ("H-12", "vorgabe", "Mietsteigerung", "2 % -> 1,5 %", "Vorgabe", ALLE, V(mietsteigerung=D("0.015"))),
    ("H-13", "vorgabe", "Kostensteigerung", "2 % -> 3 %", "Vorgabe", ALLE, V(kostensteigerung=D("0.03"))),
    ("H-14", "vorgabe", "Baupreissteigerung", "3 % -> 2 %", "Vorgabe", (NB,), V(baupreissteigerung=D("0.02"))),
    ("H-14", "vorgabe", "Baupreissteigerung (Investitionsstau im Ankauf)", "3 % -> 2 %", "Vorgabe", (AN,), V(baupreissteigerung=D("0.02"))),
    ("H-15", "vorgabe", "struktureller Leerstand", "1,5 % -> 3 %", "Vorgabe", ALLE, V(leerstand=D("0.03"))),
    ("H-16", "vorgabe", "Verkaufskosten", "1,5 % -> 2,5 %", "Vorgabe", (AN, NB), V(verkaufskostensatz=D("0.025"))),
    ("H-17", "vorgabe", "Verwaltung je Einheit", "350 -> 420 Euro", "Vorgabe", (AN, NB), V(verwaltung_je_einheit=D(420))),
    ("H-17", "vorgabe", "Instandhaltung je m2", "Staffel + 20 %", "Vorgabe", (AN, NB), V(instandhaltung_staffel=STAFFEL_PLUS)),
    ("H-17", "vorgabe", "nicht umlagefaehige Betriebskosten je m2", "2 -> 3 Euro", "Vorgabe", (AN, NB), V(betriebskosten_je_qm=D(3))),
    ("H-18", "vorgabe", "Vorfaelligkeitssatz, Verkauf nach 8 Jahren", "1 % -> 2 %", "Vorgabe", (AN,), V(vfe_satz=D("0.02")), E(haltedauer=8)),
    ("H-23", "vorgabe", "Voreinstellung der Anpassungsdauer (Neubau: nach Bindungsende)", "4 -> 1 Jahr", "Vorgabe", (GEF,), V(anpassungsdauer=1)),
    ("H-25", "vorgabe", "kalkulatorischer Zins des Bankdarlehens", "Anschlusszins (5 %) -> fest 6 %", "Vorgabe", FREI, V(kalk_zins=D("0.06"))),
    ("H-25", "vorgabe", "kalkulatorischer Zins des Bankdarlehens", "Anschlusszins (5 %) -> fest 4 %", "Vorgabe", FREI, V(kalk_zins=D("0.04"))),
    ("H-26", "vorgabe", "Fluktuation", "0 % -> 5 % je Jahr", "Vorgabe", (AN,), V(fluktuation=D("0.05"))),
    ("H-27", "vorgabe", "Forderungsausfall", "0,5 % -> 1,5 %", "Vorgabe", ALLE, V(forderungsausfall=D("0.015"))),
    ("H-28", "vorgabe", "Anlaufleerstand leerer Flaechen im Ankauf, 200 m2 leer", "3 -> 6 Monate", "Vorgabe", (AN,),
     V(anlaufleerstand=6), E(leere_flaeche=D(200))),
    ("H-29", "vorgabe", "CO2-Preis", "50 -> 100 Euro je Tonne", "Vorgabe", (AN,), V(co2_preis=D(100))),
    ("H-29", "vorgabe", "Steigerung des CO2-Preises", "5 % -> 10 % je Jahr", "Vorgabe", (AN,), V(co2_steigerung=D("0.10"))),
    ("H-30", "vorgabe", "Zuschlag der Kostengruppe 700", "20 % -> 15 %", "Vorgabe", (NB,), V(zuschlag_kg700=D("0.15"))),
    ("H-30", "vorgabe", "Zuschlag der Kostengruppen 200, 500, 600", "5 % -> 8 %", "Vorgabe", (NB,), V(zuschlag_kg_uebrige=D("0.08"))),
    ("H-30", "vorgabe", "Herstellungskosten je Stellplatz, 20 Stellplaetze", "20.000 -> 30.000 Euro", "Vorgabe", (NB,),
     V(kosten_je_stellplatz=D(30000)), E(stellplaetze=20, stellplatz_miete=D(60))),
    ("H-31", "vorgabe", "Bereitstellungszins des Bankdarlehens", "0,25 % je Monat -> 0", "Vorgabe", (NB,), V(bereit_satz=D(0))),
    ("H-31", "vorgabe", "bereitstellungsfreie Zeit", "6 -> 12 Monate", "Vorgabe", (NB,), V(bereit_frei=12)),
    ("H-32", "vorgabe", "Bemessungszeitraum", "Zinsbindung (10) -> 15 Jahre", "Vorgabe", (KFW,), V(bemessungszeitraum=15)),
    ("H-32", "vorgabe", "Bemessungszeitraum, uebernommenes Darlehen", "Zinsbindung (10) -> 15 Jahre", "Vorgabe", (AN,), V(bemessungszeitraum=15), UEBERNOMMEN),
    ("H-33", "vorgabe", "Mindestansatz der Bewirtschaftung", "15 % -> 25 %", "Vorgabe", FREI, V(bewirtschaftung_mindest=D("0.25"))),
    ("H-34", "vorgabe", "Anlaufleerstand im Neubau", "3 -> 6 Monate", "Vorgabe", NEUBAU, V(anlaufleerstand_neubau=6)),
    ("H-37", "vorgabe", "Bauabschnitte der Foerderauszahlung", "50/75 % -> 40/70 %", "Vorgabe", (GEF,),
     V(bauabschnitt_rohbau=D("0.4"), bauabschnitt_innenputz=D("0.7"))),
    # ---- H-06: Stresshoehen, jede einzeln aus dem kombinierten Stressfall genommen (Preis und Rendite des Stressfalls)
    ("H-06", "vorgabe", "Stress: Anschlusszins", "+1 Prozentpunkt -> 0", "Vorgabe", (AN, NB), ST(anschlusszins_pp=D(0)), GLEICH, True),
    ("H-06", "vorgabe", "Stress: Zins bis zur Zusage mit Neubemessung", "+0,5 Prozentpunkte -> 0", "Vorgabe", (AN, NB), ST(zusage_pp=D(0)), GLEICH, True),
    ("H-06", "vorgabe", "Stress: Leerstand", "+2 Prozentpunkte -> 0", "Vorgabe", (AN, NB), ST(leerstand_pp=D(0)), GLEICH, True),
    ("H-06", "vorgabe", "Stress: Mietsteigerung", "-0,5 Prozentpunkte -> 0", "Vorgabe", (AN, NB), ST(mietsteigerung_pp=D(0)), GLEICH, True),
    ("H-06", "vorgabe", "Stress: Verkaufsfaktor", "-10 % -> 0", "Vorgabe", (AN, NB), ST(verkaufsfaktor_rel=D(0)), GLEICH, True),
    ("H-06", "vorgabe", "Stress: Investitionsstau", "+10 % -> 0", "Vorgabe", (AN,), ST(stau_rel=D(0)), GLEICH, True),
    ("H-06", "vorgabe", "Stress: Baukosten", "+5 % -> 0", "Vorgabe", (NB,), ST(baukosten_rel=D(0)), GLEICH, True),
    ("H-06", "vorgabe", "Stress: Bauzeit", "+3 Monate -> 0", "Vorgabe", (NB,), ST(bauzeit_monate=0), GLEICH, True),
    # ---- c) Lesarten der Modellannahmen, die als Schalter wirken
    ("MA-026/3", "lesart", "Bank setzt den Ertrag des Vorhabens an", "Voreinstellung -> Lesart 3", "Schalter", (AN,), V(ma026_ertrag_vorhaben=True)),
    ("MA-026/3", "lesart", "... bei Ist-Miete 11,00 Euro ueber der Vergleichsmiete", "Voreinstellung -> Lesart 3", "Schalter", (AN,),
     V(ma026_ertrag_vorhaben=True), E(ist_miete=D("11.00"))),
    ("MA-026/4", "lesart", "Bank rechnet fremde Tranchen durchgehend kalkulatorisch", "Bemessungszins -> Lesart 4", "Schalter", (KFW,), V(ma026_fremde_kalkulatorisch=True)),
    ("MA-026/4", "lesart", "... am uebernommenen Darlehen", "Bemessungszins -> Lesart 4", "Schalter", (AN,), V(ma026_fremde_kalkulatorisch=True), UEBERNOMMEN),
    ("MA-031", "lesart", "Zuschuss im Betriebsvermoegen: sofortige Einnahme", "verteilt -> sofort", "Schalter", (GEF,), V(ma031_zuschuss="sofort")),
    ("MA-036", "lesart", "Verkauf im Rahmen der Aufgabe des Betriebs (gepraegte KG, 440 %, 60 %)", "laufend -> Aufgabe", "Schalter", (AN,),
     S(aufgabegewinn=True), status(GEPRAEGTE_PG, hebesatz=D("4.40"), anteil_natuerliche=D("0.6"))),
    ("MA-038", "lesart", "Miete ueber der Vergleichsmiete bleibt stehen (Ist 11,00 Euro)", "Rueckfuehrung -> bleibt", "Schalter", (AN,),
     V(ma038_rueckfuehrung=False), E(ist_miete=D("11.00"))),
    # ---- d) Steuerregeln des Kapitels 7 gegen die Lehrbuchform (ein Satz auf eine Bemessungsgrundlage)
    ("R-7.8/7.16", "steuer", "Hinzurechnung der Entgelte fuer Schulden weglassen (Koerperschaft)", "Regel -> ohne", "nichts", (AN, NB), S(hinzu_anteil=D(0))),
    ("R-7.8/7.16", "steuer", "Hinzurechnung weglassen (gewerbliche Personengesellschaft)", "Regel -> ohne", "nichts", (AN,),
     S(hinzu_anteil=D(0)), status(GEWERBLICHE_PG)),
    ("R-7.8/7.16", "steuer", "Hinzurechnung weglassen (Neubau mit KfW: Entgelte ueber dem Freibetrag)", "Regel -> ohne", "nichts", (KFW,), S(hinzu_anteil=D(0))),
    ("R-7.8", "steuer", "Abrundung des Gewerbeertrags weglassen", "100 Euro -> 1 Cent", "nichts", (AN,), S(abrundung=D("0.01"))),
    ("R-7.7", "steuer", "Koerperschaftsteuersatz je Kalenderjahr -> ein Satz", "15 bis 10 % -> 15 %", "nichts", (AN, NB), S(kst_satz=lambda jahr: D("0.15"))),
    ("R-7.9", "steuer", "Gewerbesteuer mit Freibetrag und Anrechnung -> nur Steuersatz E-42 (Personengesellschaft, 400 %)", "Regel -> ein Satz", "Eingabe Hebesatz ueber Gemeinde",
     (AN,), S(hebesatz=D(0)), status(GEWERBLICHE_PG)),
    ("R-7.9", "steuer", "... bei Hebesatz 440 %", "Regel -> ein Satz", "nichts", (AN,), S(hebesatz=D(0)), status(GEWERBLICHE_PG, hebesatz=D("4.40"))),
    ("R-7.9", "steuer", "... bei 440 % und 60 % natuerlichen Personen", "Regel -> ein Satz", "Eingabe E-43", (AN,),
     S(hebesatz=D(0)), status(GEWERBLICHE_PG, hebesatz=D("4.40"), anteil_natuerliche=D("0.6"))),
    ("R-7.9", "steuer", "Freibetrag der Gewerbesteuer weglassen (Personengesellschaft)", "24.500 Euro -> 0", "nichts", (AN,), S(freibetrag=D(0)), status(GEWERBLICHE_PG)),
    ("R-7.9", "steuer", "Einzelunternehmen: Gewerbesteuer-Mechanik -> nur Steuersatz", "Regel -> ein Satz", "nichts", (AN,), S(hebesatz=D(0)), status(EINZELUNTERNEHMEN)),
    ("R-7.8", "steuer", "erweiterte Kuerzung -> Gewerbesteuer entfaellt ganz (Lehrbuchform mit Kennzeichen)", "Regel -> ein Satz", "nichts", (AN, NB),
     S(hebesatz=D(0)), S(erweiterte_kuerzung=True)),
    ("R-7.5/7.6", "steuer", "Verlustvortrag -> Soforterstattung (Privatperson)", "Vortrag -> sofort", "Hauswert H-38", (AN, GEF),
     S(verlust="sofort"), status(PRIVAT)),
    ("R-7.5/7.6", "steuer", "Verlustvortrag -> Soforterstattung (gewerbliche Personengesellschaft)", "Vortrag -> sofort", "Hauswert H-38", (AN,),
     S(verlust="sofort"), status(GEWERBLICHE_PG)),
    ("R-7.10", "steuer", "Privatperson: eigener Satz auf Zinsen -> ein Satz", "26,375 % -> 42 %", "nichts", (AN,), S(zins_satz=D("0.42")), status(PRIVAT)),
    ("R-7.11", "steuer", "Privatperson: steuerfreier Verkauf nach zehn Jahren -> immer steuerpflichtig", "frei -> pflichtig", "nichts", (AN,),
     S(frist_privatverkauf=99), status(PRIVAT)),
    ("R-7.17", "steuer", "Verein und Stiftung -> Koerperschaft ohne Gewerbesteuer in Lehrbuchform (Verkauf pflichtig, Abgrenzung)", "Regel -> ein Satz", "Steuerstatus",
     (AN,), status(KOERPERSCHAFT, hebesatz=D(0)), status(KOERPERSCHAFT_OHNE_GEWST)),
    ("R-7.12", "steuer", "befreite Koerperschaft gegen Koerperschaft (Bedeutung des Status)", "Koerperschaft -> befreit", "Steuerstatus", (AN,), status(BEFREIT)),
    ("R-7.1", "steuer", "Steuerstatus: Koerperschaft -> Privatperson", "Auswahl", "Steuerstatus", (AN,), status(PRIVAT)),
    ("R-7.1", "steuer", "Steuerstatus: Koerperschaft -> gewerbliche Personengesellschaft", "Auswahl", "Steuerstatus", (AN,), status(GEWERBLICHE_PG)),
    ("R-6.16", "steuer", "anschaffungsnahe Herstellungskosten weglassen (Erhaltung 400.000 Euro im Jahr 2)", "aktiviert -> sofort abziehbar", "nichts", (AN,),
     K(ahk_quote=D(10)), E(stau_betrag=D(400000))),
    ("R-7.19", "steuer", "Zuschuss der Privatperson: Einnahme im Zuflussjahr -> verteilt", "sofort -> verteilt", "Eingabe E-70", (GEF,),
     E(zuschuss_verteilung=True), status(PRIVAT)),
    # ---- umgekehrter Test: "einfache Steuer" = Steuersatz je Status + Verlustvortrag + steuerfreier Privatverkauf
    ("einfach", "steuer", "einfache Steuer statt Kapitel 7: Koerperschaft (ohne Hinzurechnung und Abrundung)", "Regel -> einfach", "-", (AN, NB),
     S(hinzu_anteil=D(0), abrundung=D("0.01"))),
    ("einfach", "steuer", "einfache Steuer: Koerperschaft mit Kennzeichen (Gewerbesteuer entfaellt)", "Regel -> einfach", "-", (AN,),
     S(hebesatz=D(0), hinzu_anteil=D(0)), S(erweiterte_kuerzung=True)),
    ("einfach", "steuer", "einfache Steuer: gewerbliche Personengesellschaft, 400 % (nur Steuersatz)", "Regel -> einfach", "-", (AN,),
     S(hebesatz=D(0), hinzu_anteil=D(0)), status(GEWERBLICHE_PG)),
    ("einfach", "steuer", "einfache Steuer: gepraegte Personengesellschaft, 440 %, 60 % natuerliche Personen", "Regel -> einfach", "-", (AN,),
     S(hebesatz=D(0), hinzu_anteil=D(0)), status(GEPRAEGTE_PG, hebesatz=D("4.40"), anteil_natuerliche=D("0.6"))),
    ("einfach", "steuer", "einfache Steuer: Privatperson (ein Satz auch auf Zinsen)", "Regel -> einfach", "-", (AN,), S(zins_satz=D("0.42")), status(PRIVAT)),
    # ---- e) Rechenregeln aus Sonderfaellen der Pruefrunden: Wirkung, wenn man sie weglaesst
    ("R-5.18", "regel", "Bereitstellungszins des Bankdarlehens weglassen", "0,25 % -> 0", "Vorgabe H-31", (NB, KFW), V(bereit_satz=D(0))),
    ("R-5.19", "regel", "Bereitstellungsprovision des KfW-Darlehens weglassen", "0,15 % -> 0", "nichts", (KFW,), KF(bereit_satz=D(0))),
    ("R-6.9", "regel", "CO2-Kostenanteil des Vermieters weglassen", "Regel -> 0", "Eingabe E-34, Vorgabe H-29", (AN,), V(co2_preis=D(0))),
    ("R-6.3", "regel", "Rueckfuehrung einer Uebermiete weglassen (Ist 11,00 Euro)", "Rueckfuehrung -> bleibt", "Schalter MA-038", (AN,),
     V(ma038_rueckfuehrung=False), E(ist_miete=D("11.00"))),
    ("R-6.3", "regel", "Wartefrist und Kappungsgrenze weglassen (Miete folgt der Anpassungsdauer)", "15 Monate, 15 % -> 12 Monate, keine Kappung", "nichts", (AN,),
     K(wartefrist=12, kappung=D(1), kappung_gesetzlich=D(1))),
    ("R-5.16", "regel", "Vorfaelligkeit weglassen (Verkauf nach 8 Jahren, Bindung 10)", "1 % -> 0", "Vorgabe H-18", (AN,), V(vfe_satz=D(0)), E(haltedauer=8)),
    ("R-5.16", "regel", "Vorfaelligkeit weglassen (KfW-Fall, Verkauf nach 8 Jahren)", "1 % -> 0", "Vorgabe H-18", (KFW,), V(vfe_satz=D(0)), E(haltedauer=8)),
    ("R-11.3", "regel", "Teilraten der Foerdermittel weglassen (Abruf nach Bedarf, keine Zwischenfinanzierung)", "30/30/30/10 -> 100 % ab Baubeginn", "Katalogwert H-37",
     (GEF,), F(teilraten=(D(1), D(0), D(0), D(0)))),
    ("R-6.8", "regel", "Instandhaltung nach Gebaeudealter -> ein Satz", "Staffel 9/11,50/14 -> 11,50", "nichts", (AN,), V(instandhaltung_staffel=[(0, D("11.50"))])),
    ("R-6.14", "regel", "Fluktuation (wie H-26)", "0 -> 5 %", "Vorgabe H-26", (AN,), V(fluktuation=D("0.05"))),
    ("R-5.12", "regel", "Mindestansatz der Bewirtschaftung weglassen", "15 % -> 0", "Vorgabe H-33", FREI, V(bewirtschaftung_mindest=D(0))),
    ("R-5.9", "regel", "Anschlussaufschlag weglassen (heutiger Zins gilt fort)", "+1 Prozentpunkt -> 0", "Vorgabe H-05", (AN, NB), V(anschluss_aufschlag=D(0))),
    # ---- f) Proben am Rand: Gegenstaende, die im Referenzfall wenig bewegen, in dem Fall, in dem sie am staerksten wirken
    ("H-39", "vorgabe", "Probe: Bodenanteil als Hauswert, weite Spanne", "25 % -> 50 %", "Hauswert", (AN,), V(bodenanteil=D("0.50"))),
    ("E-12", "eingabe", "Probe: Bodenanteil bei der Privatperson, weite Spanne", "25 % -> 50 %", "Eingabe", (AN,),
     E(bodenanteil=D("0.50")), status(PRIVAT)),
    ("H-23", "vorgabe", "Probe: Anpassungsdauer bei grosser Mietluecke (Ist 7,00 gegen 9,20 Euro)", "4 -> 1 Jahr", "Katalogwert", (AN,),
     V(anpassungsdauer=1), LUECKE),
    ("E-05", "eingabe", "Probe: Kappungsgrenze bei grosser Mietluecke", "im Gebiet (15 %) -> ausserhalb (20 %)", "Eingabe", (AN,),
     E(im_kappungsgebiet=False), LUECKE),
    ("E-33", "eingabe", "Probe: Mietenhistorie bei grosser Mietluecke", "nicht angegeben -> vor 6 Monaten, 6,50 Euro vor drei Jahren", "Eingabe", (AN,),
     E(mietenhistorie=(6, D("6.50"))), LUECKE),
    ("R-6.3", "regel", "Probe: Wartefrist und Kappungsgrenze weglassen bei grosser Mietluecke", "15 Monate, 15 % -> 12 Monate, keine Kappung", "nichts", (AN,),
     K(wartefrist=12, kappung=D(1), kappung_gesetzlich=D(1)), LUECKE),
    ("E-34", "eingabe", "Probe: CO2-Ausstoss, weite Spanne", "30 -> 60 kg je m2", "Eingabe", (AN,), E(co2_ausstoss=D(60))),
    ("R-6.9", "regel", "Probe: CO2-Kostenanteil des Vermieters weglassen bei 60 kg je m2", "Regel -> 0", "Eingabe E-34, Vorgabe H-29", (AN,),
     V(co2_preis=D(0)), E(co2_ausstoss=D(60))),
    ("H-28", "vorgabe", "Probe: Anlaufleerstand im Ankauf bei 600 m2 leer", "3 -> 12 Monate", "Vorgabe", (AN,),
     V(anlaufleerstand=12), E(leere_flaeche=D(600))),
    ("E-31", "eingabe", "Probe: leerstehende Flaeche bei 12 Monaten Anlaufleerstand", "0 -> 600 m2 (45 %)", "Eingabe", (AN,),
     E(leere_flaeche=D(600)), V(anlaufleerstand=12)),
    ("H-06", "vorgabe", "Probe: Stress Anschlusszins bei Zinsbindung 5 Jahre", "+1 Prozentpunkt -> 0", "Vorgabe", (AN,),
     ST(anschlusszins_pp=D(0)), E(zinsbindung_jahre=5), True),
    ("H-06", "vorgabe", "Probe: Stress Investitionsstau bei 500.000 Euro", "+10 % -> 0", "Vorgabe", (AN,),
     ST(stau_rel=D(0)), E(stau_betrag=D(500000)), True),
    ("R-7.8/7.16", "steuer", "Probe: Hinzurechnung weglassen beim zehnfachen Vorhaben (Darlehen ueber 10 Mio. Euro)", "Regel -> ohne", "nichts", (AN,),
     S(hinzu_anteil=D(0)), GROSS),
    ("E-59", "eingabe", "Probe: uebernommenes Darlehen, laufender Beitrag", "0 -> 0,5 %", "Eingabe", (AN,), UE(beitrag_satz=D("0.005")), UEBERNOMMEN),
    ("E-59", "eingabe", "Probe: uebernommenes Darlehen, Ende der Zinsbindung", "8 -> 3 Jahre", "Eingabe", (AN,), UE(bindung_jahre=3), UEBERNOMMEN),
    ("R-7.5/7.6", "steuer", "Probe: Verlustvortrag -> Soforterstattung (Privatperson, Neubau)", "Vortrag -> sofort", "Hauswert H-38", (NB,),
     S(verlust="sofort"), status(PRIVAT)),
    ("H-14", "vorgabe", "Probe: Baupreissteigerung, weite Spanne", "3 % -> 5 %", "Vorgabe", (NB,), V(baupreissteigerung=D("0.05"))),
    ("E-05", "eingabe", "Probe: Kappungsgrenze im Neubau", "im Gebiet (15 %) -> ausserhalb (20 %)", "Eingabe", (NB,), E(im_kappungsgebiet=False)),
    ("E-05", "eingabe", "Probe: Mietpreisbremse bei 600 m2 leer und Marktmiete 13,00 Euro", "im Gebiet -> ausserhalb", "Eingabe", (AN,),
     E(im_bremsgebiet=False), E(leere_flaeche=D(600), markt_miete=D("13.00"))),
    ("E-16", "eingabe", "Probe: Marktmiete im Ankauf bei 600 m2 leer", "10,50 -> 9,50 Euro", "Eingabe", (AN,),
     E(markt_miete=D("9.50")), E(leere_flaeche=D(600))),
    ("R-6.9", "regel", "Probe: CO2-Kostenanteil des Vermieters weglassen bei 60 kg je m2 und 100 Euro je Tonne", "Regel -> 0", "Eingabe E-34, Vorgabe H-29", (AN,),
     V(co2_preis=D(0)), nach(E(co2_ausstoss=D(60)), V(co2_preis=D(100)))),
    ("einfach", "steuer", "einfache Steuer: Koerperschaft, Neubau mit KfW (ohne Hinzurechnung und Abrundung)", "Regel -> einfach", "-", (KFW,),
     S(hinzu_anteil=D(0), abrundung=D("0.01"))),
]

# Pflichteingaben ohne sinnvolle Voreinstellung: nicht gemessen
PFLICHT = [("E-01", "Vorhabensart"), ("E-03", "Land"), ("E-04", "Gemeinde"), ("E-10", "Kaufpreis"), ("E-13", "Wohnflaeche"),
           ("E-14", "Zahl der Einheiten"), ("E-15", "Ist-Miete"), ("E-19", "Vergleichsmiete"), ("E-17", "Baujahr"),
           ("E-20", "Grundstueckspreis"), ("E-21", "Grundstuecksflaeche"), ("E-22", "Brutto-Grundflaeche"),
           ("E-25", "Kostenkennwert"), ("E-26", "Bauzeit"), ("E-16", "Miete bei Bezug (Neubau)"),
           ("E-28", "Mietenstufe (gefoerdert)"), ("E-29", "Einkommensgruppe (gefoerdert)"), ("E-30", "Bodenrichtwert (gefoerdert)"),
           ("E-40", "Steuerstatus"), ("E-45", "Zins des Bankdarlehens"), ("E-47", "Verkaufsfaktor")]
# Zum Vergleich: so stark bewegen die Hauptannahmen das Ergebnis (nicht Teil der Zaehlung)
VERGLEICH = [
    ("E-15", "eingabe-pflicht", "Ist-Miete", "8,50 -> 8,00 Euro", "Pflicht", (AN,), E(ist_miete=D("8.00"))),
    ("E-19", "eingabe-pflicht", "Vergleichsmiete", "9,20 -> 8,70 Euro", "Pflicht", (AN,), E(vergleichsmiete=D("8.70"))),
    ("E-45", "eingabe-pflicht", "Zins des Bankdarlehens", "4 % -> 4,5 %", "Pflicht", (AN, NB), E(zins=D("0.045"))),
    ("E-47", "eingabe-pflicht", "Verkaufsfaktor", "18 -> 17", "Pflicht", (AN,), E(verkaufsfaktor=D(17))),
    ("E-47", "eingabe-pflicht", "Verkaufsfaktor", "24 -> 22", "Pflicht", (NB,), E(verkaufsfaktor=D(22))),
    ("E-16", "eingabe-pflicht", "Miete bei Bezug", "16,50 -> 15,50 Euro", "Pflicht", (NB,), E(markt_miete=D("15.50"))),
    ("E-25", "eingabe-pflicht", "Kostenkennwert", "2.320 -> 2.450 Euro je m2", "Pflicht", (NB,), E(kostenkennwert=D(2450))),
]


# ------------------------------------------------------------------ Messung
def messe(ein, vg, kat, mit_preis, stress=False):
    """Rendite beim eingegebenen Preis und tragbarer Preis; Meldungen statt Zahlen, wo es keine gibt."""
    erg = dict(rendite=None, preis=None, hinweis="", nebenkosten=None)
    try:
        e = rechne_grob(ein, vg, kat, stress=stress, mit_blatt=False, _begruendung=False)
        if e.gesperrt:
            erg["hinweis"] = "M-10"
        else:
            erg["rendite"] = e.kennzahlen["rendite"]
            erg["nebenkosten"] = (e.baukosten, ein.enk_satz)
    except Meldung as m:
        erg["hinweis"] = m.kennung
        return erg
    if mit_preis:
        tp = _tragbarer_preis(ein, replace(vg, **MESSRASTER), kat, stress=stress)
        erg["preis"] = tp["preis"]
        if tp["meldung"]:
            erg["hinweis"] = (erg["hinweis"] + " " + tp["meldung"]).strip()
    return erg


def laufe(gegenstaende, mit_preis=True, ausgabe=None):
    zeilen, basen = [], {}
    for g in gegenstaende:
        kennung, gruppe, text, spanne, kostet, faelle, var = g[:7]
        basis_f = g[7] if len(g) > 7 else GLEICH
        stress = g[8] if len(g) > 8 else False
        for fall in faelle:
            ein, vg, kat, preisfall = FAELLE[fall]
            preis_an = mit_preis and preisfall
            b_ein, b_vg, b_kat = basis_f(ein, vg, kat)
            schluessel = (fall, id(basis_f), stress, preis_an)
            if schluessel not in basen:
                basen[schluessel] = messe(b_ein, b_vg, b_kat, preis_an, stress)
            b = basen[schluessel]
            try:
                n = messe(*var(b_ein, b_vg, b_kat), preis_an, stress)
            except Exception as x:                       # eine unzulaessige Variation ist ein Befund der Messung
                n = dict(rendite=None, preis=None, hinweis=type(x).__name__ + ": " + str(x)[:80])
            z = dict(kennung=kennung, gruppe=gruppe, text=text, spanne=spanne, kostet=kostet, fall=fall,
                     basis_abweichend=basis_f is not GLEICH, stressfall=stress,
                     rendite_basis=b["rendite"], rendite_neu=n["rendite"], preis_basis=b["preis"], preis_neu=n["preis"],
                     hinweis=" / ".join(x for x in (b["hinweis"], n["hinweis"]) if x))
            z["d_rendite_pp"] = (None if None in (b["rendite"], n["rendite"]) else (n["rendite"] - b["rendite"]) * 100)
            if None in (b["preis"], n["preis"]):
                z["d_preis"] = z["d_preis_pct"] = z["d_preis_pct_bezug"] = None
            else:
                z["d_preis"] = n["preis"] - b["preis"]
                z["d_preis_pct"] = (D(z["d_preis"]) / D(b["preis"]) * 100) if b["preis"] else None
                # Bezug: Kaufpreis (Ankauf) oder Gesamtkosten beim tragbaren Preis (Neubau)
                bezug = D(b["preis"])
                if fall != AN and b["nebenkosten"]:
                    bezug = D(b["preis"]) * (1 + b["nebenkosten"][1]) + b["nebenkosten"][0]
                z["d_preis_pct_bezug"] = (D(z["d_preis"]) / bezug * 100) if bezug else None
            rendite_ueber = z["d_rendite_pp"] is not None and abs(z["d_rendite_pp"]) > SCHWELLE_RENDITE * 100
            z["ueber_schwelle"] = rendite_ueber or (z["d_preis_pct_bezug"] is not None
                                                    and abs(z["d_preis_pct_bezug"]) > SCHWELLE_PREIS * 100)
            z["ueber_schwelle_grundstueck"] = rendite_ueber or (z["d_preis_pct"] is not None
                                                                and abs(z["d_preis_pct"]) > SCHWELLE_PREIS * 100)
            zeilen.append(z)
            drucke(z)
            if ausgabe:
                json.dump(zeilen, open(ausgabe, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    return zeilen


def drucke(z):
    f = lambda x, n: "      -" if x is None else f"{x:+.{n}f}"
    print(f"{z['kennung']:11} {z['fall']:17} Preis {f(z['d_preis_pct'], 2):>8} % ({f(z['d_preis_pct_bezug'], 2):>6} % Bezug) {f(z['d_preis'], 0):>10} Euro  "
          f"Rendite {f(z['d_rendite_pp'], 3):>8} PP  {'UEBER' if z['ueber_schwelle'] else 'unter'}  "
          f"{z['text'][:70]} [{z['spanne'][:40]}] {z['hinweis']}", flush=True)


if __name__ == "__main__":
    arg = sys.argv[1:]
    ausgabe = arg[arg.index("--ausgabe") + 1] if "--ausgabe" in arg else None
    nur = arg[arg.index("--nur") + 1].split(",") if "--nur" in arg else None
    liste = GEGENSTAENDE + VERGLEICH
    if nur:
        liste = [g for g in liste if g[1] in nur]
    start = time.time()
    zeilen = laufe(liste, mit_preis="--ohne-preis" not in arg, ausgabe=ausgabe)
    ueber = sum(1 for z in zeilen if z["ueber_schwelle"])
    eng = sum(1 for z in zeilen if z["ueber_schwelle_grundstueck"])
    print(f"\n{len(zeilen)} Messungen an {len(liste)} Gegenstaenden; {ueber} ueber der Schwelle "
          f"(Preis > {SCHWELLE_PREIS * 100} % des Kaufpreises oder der Gesamtkosten oder Rendite > {SCHWELLE_RENDITE * 100} Prozentpunkte; "
          f"gemessen am Grundstueckspreis waeren es {eng}); "
          f"{len(PFLICHT)} Pflichteingaben nicht gemessen; Laufzeit {time.time() - start:.0f} Sekunden.")
