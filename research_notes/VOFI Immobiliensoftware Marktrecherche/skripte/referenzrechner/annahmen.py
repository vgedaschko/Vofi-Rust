"""Angenommener Katalog- und Vorgabenstand fuer die Referenzfaelle, getrennt nach Herkunft (R-3.1).

Kein Bestandteil des Rechenkerns: Die Werte stehen hier, weil der Rechenkern keinen Satz, keine Schwelle und
keine Frist als Festwert kennt. Drei Gruppen:
  KATALOG_*, steuer()   Katalogwerte (KAT-..) mit der Kennung des Quellenkatasters; Stand des Rechercheberichts
                        oder der am Original gelesenen Norm, sonst als Annahme gekennzeichnet
  VORGABEN*             Vorgaben des Hauses (H-..): Annahmen der Beispiele, die der Auftraggeber noch freigibt
  ANKAUF, NEUBAU        Eingaben des Anwenders (E-..) der beiden Referenzobjekte
Die vollstaendige Liste steht im Anhang A der Fachspezifikation.
"""
from decimal import Decimal as D
from dataclasses import replace
from steuer import (Steuerparameter, KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST, GEPRAEGTE_PG, GEWERBLICHE_PG,
                    EINZELUNTERNEHMEN, PRIVAT, BEFREIT, PERSONENUNTERNEHMEN)
import grobkalkulation
from grobkalkulation import Vorgaben, Stress, Grobeingabe, Foerderung, Katalog, KfwKonditionen

# ------------------------------------------------------------------ Katalogwerte: Steuer (KAT-03 bis KAT-06, KAT-16 bis KAT-18)


def kst_satz(jahr):
    """Koerperschaftsteuersatz je Kalenderjahr (KSTG-23), Stand Bericht B.3."""
    staffel = {2028: "0.14", 2029: "0.13", 2030: "0.12", 2031: "0.11"}
    if jahr <= 2027:
        return D("0.15")
    return D(staffel.get(jahr, "0.10"))


SOLI = D("0.055")                 # SOLZG-4
MESSZAHL = D("0.035")             # GEWSTG-11
ABRUNDUNG = D("100")              # GEWSTG-11: Abrundung des Gewerbeertrags auf volle 100 Euro
HEBESATZ = D("4.00")              # Annahme: 400 % (GEWSTG-16), Katalogwert der Gemeinde E-04
FREIBETRAG = D("24500")           # GEWSTG-11, natuerliche Personen und Personengesellschaften
ANRECHNUNGSFAKTOR = D("4")        # ESTG-35
FRIST_PRIVATVERKAUF = 10          # ESTG-23
HINZU_ANTEIL = D("0.25")          # GEWSTG-8: ein Viertel der Entgelte fuer Schulden
HINZU_FREIBETRAG = D("200000")    # GEWSTG-8
HINZU_PACHT = D("0.5")            # GEWSTG-8: die Haelfte der Pacht fuer Grundbesitz (Erbbauzins)
SOCKEL_VERLUST = D("1000000")     # ESTG-10D, GEWSTG-10A: Sockelbetrag der Mindestbesteuerung (nur Hinweis M-45)
ZINS_SATZ_PRIVAT = D("0.26375")   # ESTG-32D mit SOLZG-4: 25 % zuzueglich 5,5 % Zuschlag; ohne Kirchensteuer (Annahme)
EST_SATZ = D("0.42")              # Annahme: eingegebener Steuersatz E-42


def steuer(status, **kw):
    basis = dict(status=status, kst_satz=kst_satz, soli_satz=SOLI, messzahl=MESSZAHL, hebesatz=HEBESATZ,
                 abrundung=ABRUNDUNG, est_satz=EST_SATZ, anrechnungsfaktor=ANRECHNUNGSFAKTOR,
                 frist_privatverkauf=FRIST_PRIVATVERKAUF, hinzu_anteil=HINZU_ANTEIL,
                 hinzu_freibetrag=HINZU_FREIBETRAG, hinzu_pacht=HINZU_PACHT, sockel_verlust=SOCKEL_VERLUST)
    if status in PERSONENUNTERNEHMEN:
        basis["freibetrag"] = FREIBETRAG
    if status == PRIVAT:
        basis["zins_satz"] = ZINS_SATZ_PRIVAT
    basis.update(kw)
    return Steuerparameter(**basis)


# ------------------------------------------------------------------ Katalogwerte: uebrige
# KAT-15 nach KFW-297-298-MERKBLATT (am Original gelesen 2026-11-18, Pruefrunde 2): Hoechstbetraege je Wohneinheit ohne
# und mit Qualitaetssiegel, Laufzeitvarianten mit tilgungsfreien Anlaufjahren, Bereitstellungsprovision ab dem
# 13. Monat nach der Zusage, Abruffrist mit Verlaengerung. Zins und Zinsbindung sind Annahmen des Beispiels
# (KFW-KONDITIONENANZEIGER nicht gelesen). Die endfaellige Variante fuehrt 1a nicht.
KFW = KfwKonditionen(hoechstbetrag_je_einheit=D("100000"), hoechstbetrag_qng=D("150000"), zins=D("0.025"),
                     varianten=[(10, 1, 2), (25, 1, 3), (35, 1, 5)], zinsbindung_jahre=10,
                     bereit_satz=D("0.0015"), bereit_frei=12, abruffrist=12, abruf_verlaengerung=24)

KATALOG = Katalog(
    afa_satz=D("0.02"),                                 # KAT-07 (ESTG-7): Baujahr 1925 bis 2022
    wartefrist=15, kappung=D("0.15"), kappung_monate=36,    # KAT-08 (BGB-558); 15 % als Annahme zur Gemeinde
    mietpreisbremse=True, bremse_aufschlag=D("0.10"),   # KAT-08 (BGB-556D): Annahme zur Gemeinde und zum Aufschlag
    co2_vermieteranteil=D("0.40"),                      # KAT-09 (CO2KOSTAUFG-ANLAGE): Annahme zur Stufe bei 30 kg
    co2_5a_anteil=D("0.5"), co2_5a_ab_jahr=2028,        # KAT-09 (CO2KOSTAUFG-5A): haelftige Teilung ab dem genannten Jahr
    geb_steigerung=D("0.0615"), geb_fest_jahre=3, geb_schritt_jahre=3,      # KAT-11: Werte nach Bericht C.1 (Annahme)
    ahk_quote=D("0.15"), ahk_jahre=3,                   # KAT-12 (ESTG-6)
    ust_satz=D("0.19"),                                 # KAT-12 (USTG-12): Annahme zum Katalogstand
    kuendigung_sperre=120, kuendigung_frist=6,          # KAT-13 (BGB-489)
    bewirtschaftung_mindest=D("0.15"),                  # KAT-14 (BELWERTV-11)
    kfw=KFW,
    land="Niedersachsen", gemeinde="Beispielgemeinde (Annahme)",    # Land und Gemeinde, fuer die aufgeloest ist
    enk_satz=D("0.10"),                                 # KAT-01: Annahme der Beispiele (Voreinstellung von E-11)
    kappung_gesetzlich=D("0.20"),                       # KAT-08 (BGB-558): Kappungsgrenze ohne Gebietsverordnung
    kappung_ende_jahr=2029, bremse_ende_jahr=2029)      # KAT-08: Geltungsende der Verordnungen (BGB-556D; Annahme
                                                        # zur Gemeinde fuer die Kappungsverordnung)
KATALOG_NEUBAU = replace(KATALOG, afa_satz=D("0.03"),   # KAT-07 (ESTG-7): Fertigstellung nach 2022
                         enk_satz=D("0.08"))

# Grobfoerderung (KAT-10): Werte nach Bericht Anhang C.1 fuer Einkommensgruppe B und Mietenstufe IV bis VII
# (NBANK-RL-MIETWOHNRAUM-2026; MA-002, MA-003, MA-004); Annahme des Beispiels: Zins nach der zinslosen Zeit 5 %
FOERDERUNG_B = Foerderung(
    darlehensquote=D("0.60"), zuschussquote=D("0.20"), eigenmittelquote=D("0.20"),
    bemessungsgrenze_je_qm=D("5460"), eingangsmiete=D("8.20"), steigerung=D("0.0615"),
    fest_jahre=3, schritt_jahre=3, bindung_jahre=35, vkb_satz=D("0.005"), entgelt_darlehen=D("0.01"),
    entgelt_zuschuss=D("0.0075"), tilgung_jahre=42, zinslos_jahre=35, zins_danach=D("0.05"),
    teilraten=(D("0.30"), D("0.30"), D("0.30"), D("0.10")), bank_mindesttilgung=D("0.01"), tilgungsfrist_monate=24,
    aufschub_max_monate=60)

# Zulaessige Bereiche der Eingabepruefung (R-3.3, R-3.4, Spalte "zulaessig")
grobkalkulation.GRENZEN.update(
    enk_max=D("0.20"), zins_max=D("0.20"), bindung_max=40, haltedauer_max=42, steigerung_min=D("-0.05"),
    steigerung_max=D("0.15"), steuersatz_max=D("0.60"), bauzeit_max=60, anpassung_max=20, vorlauf_max=60)

# ------------------------------------------------------------------ Vorgaben des Hauses (alle Werte Annahmen)
STRESS = Stress(anschlusszins_pp=D("0.01"), zusage_pp=D("0.005"), leerstand_pp=D("0.02"),
                verkaufsfaktor_rel=D("0.10"), mietsteigerung_pp=D("0.005"), instandhaltung_rel=D("0.10"),
                stau_rel=D("0.10"), baukosten_rel=D("0.05"), bauzeit_monate=3)

VORGABEN = Vorgaben(
    zielrendite=D("0.05"), beleihungsquote=D("0.65"), mindestdeckung=D("1.2"), mindesttilgung=D("0.02"),
    anschluss_aufschlag=D("0.01"), stress=STRESS, anschluss_regel="tilgungssatz", h_kurz=D("0.02"),
    kk_zins=D("0.08"), kk_linie=D(0), mietsteigerung=D("0.02"), kostensteigerung=D("0.02"),
    baupreissteigerung=D("0.03"), leerstand=D("0.015"), verkaufskostensatz=D("0.015"),
    verwaltung_je_einheit=D("350"),
    instandhaltung_staffel=[(0, D("9")), (22, D("11.50")), (32, D("14"))],   # Staffel nach Gebaeudealter (IIBV-28)
    betriebskosten_je_qm=D("2"), vfe_satz=D("0.01"),
    such_obergrenze_faktor=D(100), suchraster=40, nachsuchfenster=20, such_miete_max=D(100),
    izf_unten=D("-0.99"), izf_oben=D("10"), izf_raster=2000,
    kalk_zins=None, fluktuation=D(0), forderungsausfall=D("0.005"), anlaufleerstand=3,
    co2_preis=D("50"), co2_steigerung=D("0.05"),
    zuschlag_kg_uebrige=D("0.05"), zuschlag_kg700=D("0.20"), kosten_je_stellplatz=D("20000"),
    bereit_satz=D("0.0025"), bereit_frei=6,
    anpassungsdauer=4, vorlauf=0,                                           # H-23, H-35
    leerstandskosten_je_qm=D(0),                                            # H-36: in den bezeichneten Faellen 30 Euro
    warnschwelle_restwertanteil=D("0.95"), warnschwelle_faktorabstand=D(1),
    bauabschnitt_rohbau=D("0.5"), bauabschnitt_innenputz=D("0.75"))  # H-20

# ------------------------------------------------------------------ Eingaben der Referenzobjekte
# Referenzobjekt Ankauf: 20 Wohnungen, 1.320 m2, Baujahr 1990, Ist-Miete 8,50 Euro/m2 (Jahresmiete 134.640 Euro)
ANKAUF = Grobeingabe(
    art="ankauf", land="Niedersachsen", gemeinde="Beispielgemeinde (Annahme)", stichtag_jahr=2027, stichtag_monat=1,
    steuer=steuer(KOERPERSCHAFT), zins=D("0.04"), zinsbindung_jahre=10, verkaufsfaktor=D("18"), haltedauer=12,
    wohnflaeche=D("1320"), einheiten=20, enk_satz=D("0.10"), kaufpreis=D("2400000"), angebotspreis=D("2600000"),
    bodenanteil=D("0.25"), baujahr=1990, ist_miete=D("8.50"), vergleichsmiete=D("9.20"), markt_miete=D("10.50"),
    anpassungsdauer=4, stau_betrag=D("120000"), stau_jahr=2, stau_art="erhaltung", co2_ausstoss=D("30"))

# Referenzobjekt Neubau: 30 Wohnungen, 2.000 m2 Wohnflaeche, 2.600 m2 Brutto-Grundflaeche
NEUBAU = Grobeingabe(
    art="neubau", land="Niedersachsen", gemeinde="Beispielgemeinde (Annahme)", stichtag_jahr=2027, stichtag_monat=1,
    steuer=steuer(KOERPERSCHAFT), zins=D("0.04"), zinsbindung_jahre=10, verkaufsfaktor=D("24"), haltedauer=15,
    wohnflaeche=D("2000"), einheiten=30, enk_satz=D("0.08"), grundstueckspreis=D("1200000"),
    grundstuecksflaeche=D("2500"), bodenrichtwert=D("400"), bgf=D("2600"), kostenkennwert=D("2320"),
    bauzeit_monate=18, markt_miete=D("16.50"))
