"""Referenzfaelle RF-16 bis RF-20: Regeln und Randfaelle der Ueberarbeitung nach Pruefrunde 1.

RF-16 Sperre bei verletzter Probe und Fehlerbilder der Proben · RF-17 Steuerregeln · RF-18 Miete, Ertraege,
Verkauf · RF-19 Darlehen und Bankensicht · RF-20 Raender der Eingaben und der Suchen (Bericht "Grenzfaelle").
Sollwerte mit benanntem Rechenweg stehen im Code; die uebrigen sind in erwartete_werte.json festgeschrieben.
"""
import io
import os
import re
import tokenize
from decimal import Decimal as D
from dataclasses import replace
from zahlen import NULL, EINS, Rundung, de
from zeit import Raster
from steuer import (Steuer, KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST, GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN,
                    PRIVAT, BEFREIT)
from darlehen import Tranche
from finanzplan import PlanEingabe, Verkauf, rechne_plan, rechne_alternative, verdichte, ZEILEN
from proben import pruefe_plan, pruefe_alternative, pruefe_index
from kennzahlen import schuldendienstdeckung, renditemeldungen, meldung_izf
import grobkalkulation
from grobkalkulation import (rechne_grob, tragbarer_preis, zielwertsuche, suche_eingabe, haltedauer_tabelle, vergleiche,
                             Meldung, kalkuliere, darstellung, vorgaben_im_vorhaben)
import annahmen as A
from rf_rahmen import fall, pruefe, pruefe_fest, pruefe_gleich, pruefe_reihe, info, lehrbuch_steuer, izf
from rf_bausteine import lauf
from rf_grob import VG, KAT, KATN, GEBUNDEN, GEFOERDERT, proz_fest, kennungen
from rf_testfall import s1, s1_monat, REINERTRAG

CENT = Rundung("cent")


def meldung_von(f):
    try:
        f()
        return None
    except Meldung as m:
        return m.kennung


def proben_von(bef):
    return sorted({b[0] for b in bef})


def rf16_sperre():
    k = fall("RF-16", "Verletzte Probe sperrt das Ergebnis (R-13.1); Fehlerbilder der Proben")
    gut = rechne_grob(A.ANKAUF, VG, KAT)

    def stoerung(lokal):                 # Fehler im Mittelabruf: Einlage zum Stichtag um 100.000 Euro zu hoch
        lokal["einl"][0] += D(100000)
    grobkalkulation.STOERUNG[0] = stoerung
    try:
        e = rechne_grob(A.ANKAUF, VG, KAT)
        pruefe_gleich(k, "Einlage um 100.000 Euro zu hoch: Ergebnis gesperrt, keine Kennzahlen", (e.gesperrt, e.kennzahlen), (True, None))
        pruefe_gleich(k, "... verletzte Probe", proben_von(e.befunde), ["P-04"])
        pruefe(k, "... Abweichung der Probe P-04 (Eigenkapital als Ausgleichsposten)", e.befunde[0][2], "100000", "0")
        pruefe_gleich(k, "... Meldung", kennungen(e), ["M-10"])
        pruefe_gleich(k, "... Aufruf ohne Abbruch: Status", kalkuliere(A.ANKAUF, VG, KAT)["status"], "gesperrt")
        tp = tragbarer_preis(A.ANKAUF, VG, KAT)
        pruefe_gleich(k, "... Preissuche endet mit M-10 und ohne Preis", (tp["preis"], tp["meldung"]), (None, "M-10"))
        pruefe_gleich(k, "... Zielwertsuche endet mit M-10",
                      meldung_von(lambda: suche_eingabe(A.ANKAUF, VG, KAT, "verkaufsfaktor", D(8), D(40), D("0.01"))), "M-10")
        pruefe_gleich(k, "... Haltedauertabelle weist M-10 je Zeile aus", [x[3] for x in haltedauer_tabelle(A.ANKAUF, VG, KAT, 11, 12)], ["M-10", "M-10"])
        pruefe_gleich(k, "... Vergleich mit einer gesperrten Fassung ist nicht moeglich", meldung_von(lambda: vergleiche(gut, e)), "M-10")
    finally:
        grobkalkulation.STOERUNG[0] = None
    pruefe_gleich(k, "ohne Stoerung: Ergebnis nicht gesperrt", rechne_grob(A.ANKAUF, VG, KAT).gesperrt, False)
    # P-07 rechnet mit der Rechenfolge der Regel R-8.7 (Fall mit halbem Cent, Bericht Grenzfaelle GF-46)
    gf46 = replace(A.NEUBAU, bgf=D("2600.12"), kostenkennwert=D("2901.89"), bauzeit_monate=14, haltedauer=36,
                   foerderung=A.FOERDERUNG_B)
    e = rechne_grob(gf46, VG, KATN)
    pruefe_gleich(k, "Neubau mit 14 Monaten Bauzeit, Verkauf nach 36 Jahren: keine Probe verletzt", (e.gesperrt, proben_von(e.befunde)), (False, []))
    from proben import pruefe_zuschuss
    z, rueck = D("1709052.45"), D("8138.35")      # 1.709.052,45 x 2 / 420 = 8.138,345: halber Cent
    pruefe(k, "Rueckzahlung nach R-8.7 im Fall mit halbem Cent", grobkalkulation.restwert.zuschuss_rueckzahlung(z, 420, 2, CENT), "8138.35", "0")
    pruefe_gleich(k, "Zuschussprobe P-07 im Fall mit halbem Cent: keine Verletzung", pruefe_zuschuss(z, rueck, z, 420, 2, CENT), [])
    pruefe(k, "... die fruehere Probe mit vorgezogener Division haette gemeldet", z - rueck - (z - CENT.geld(z * (D(2) / D(420)))), "-0.01", "0")
    # Fehlerbilder: jede neue Probe schlaegt bei ihrem Fehler an
    plan, alt, _ = s1_monat(D("0.02"), D("0.08"), "cent")
    pruefe_gleich(k, "Testfall im Monatsraster: alle Proben bestanden", pruefe_plan(plan, alt), [])
    pe = plan.e
    pe.afa = [NULL] + [CENT.geld(D(17600) / 12)] * 60
    pe.tranchen = [Tranche("Bankdarlehen", 700000, "annuitaet_prozent", "0.04", tilgungssatz="0.02")]
    falsch = rechne_plan(pe)
    pruefe_gleich(k, "Fehlerbild Abschreibung je Monat statt je Planjahr: P-08 und P-19 melden", proben_von(pruefe_plan(falsch)), ["P-08", "P-15", "P-19"])
    pruefe(k, "... Endwert mit dem Fehler (frueherer Sollwert)", falsch.endwert, "585918.72", "0")
    e = rechne_grob(A.ANKAUF, VG, KAT)
    e.plan.zeilen[5]["tranchen"]["Bankdarlehen"]["zins"] += D("1.00")
    pruefe_gleich(k, "Fehlerbild Zins um einen Euro falsch: Zinsprobe P-17 meldet", "P-17" in proben_von(pruefe_plan(e.plan)), True)
    e = rechne_grob(A.ANKAUF, VG, KAT)
    e.plan.steuer.protokoll[3]["vv"] += D(1000)
    pruefe_gleich(k, "Fehlerbild Verlustvortrag falsch fortgeschrieben: Steuerprobe P-15 meldet", proben_von(pruefe_plan(e.plan)), ["P-15"])
    e = rechne_grob(A.ANKAUF, VG, KAT)
    e.plan.zeilen[30]["e_op"] += D(500)
    pruefe_gleich(k, "Fehlerbild Ergebnis ohne Zahlung: Bruecke der Steuerprobe P-15 meldet", proben_von(pruefe_plan(e.plan)), ["P-15"])
    e = rechne_grob(A.ANKAUF, VG, KAT)
    e.alt.zeilen[40]["kurz"] += D(100)
    pruefe_gleich(k, "Fehlerbild Unterlassensalternative falsch gebucht: P-16 meldet", proben_von(pruefe_alternative(e.alt, CENT)), ["P-16"])
    e = rechne_grob(A.ANKAUF, VG, KAT)
    e.plan.zeilen[24]["guthaben"] += D(10)
    pruefe_gleich(k, "Fehlerbild Bestand am Jahresende falsch: Jahresbestandsprobe P-09 meldet", "P-09" in proben_von(pruefe_plan(e.plan)), True)
    idx, steig = e.ertrag.indexreihen["Mieten"]
    pruefe_gleich(k, "Indexprobe P-18: richtige Reihe", pruefe_index({"Mieten": (idx, steig)}, CENT), [])
    pruefe_gleich(k, "Fehlerbild Index falsch: P-18 meldet", proben_von(pruefe_index({"Mieten": (idx[:3] + [idx[3] + D("0.01")] + idx[4:], steig)}, CENT)), ["P-18"])


def rf17_steuer():
    k = fall("RF-17", "Steuerregeln der Ueberarbeitung: Kuerzung, Hinzurechnung, Verluste, Zuschuss, Finanzierungskosten")
    r = Raster(1, 12, startjahr=2027)

    def st(status, alternative=False, **kw):
        return Steuer(A.steuer(status, **kw), r, CENT, alternative=alternative)

    # R-7.8 (GEWSTG-9, MA-030)
    pruefe(k, "Koerperschaft mit Kuerzung, 100.000 Ergebnis und 10.000 Zinsen: 17.407,50 + 14 % von 10.000",
           st(KOERPERSCHAFT, erweiterte_kuerzung=True).jahr(1, D(100000), D(10000)), "18807.50", "0")
    pruefe(k, "... dazu 500.000 Verkaufsgewinn, gewerbesteuerpflichtig (MA-030): 96.532,50 + 14 % von 510.000",
           st(KOERPERSCHAFT, erweiterte_kuerzung=True).jahr(1, D(100000), D(10000), D(500000)), "167932.50", "0")
    pruefe(k, "... andere Lesart MA-030: Verkaufsgewinn gekuerzt",
           st(KOERPERSCHAFT, erweiterte_kuerzung=True, kuerzung_verkauf=True).jahr(1, D(100000), D(10000), D(500000)), "97932.50", "0")
    pruefe(k, "Unterlassensalternative bei gesetztem Kennzeichen: 10.000 Zinsen zu 29,825 %",
           st(KOERPERSCHAFT, alternative=True, erweiterte_kuerzung=True).jahr(1, NULL, D(10000)), "2982.50", "0")
    s = st(KOERPERSCHAFT, erweiterte_kuerzung=True)
    pruefe_reihe(k, "Grenzsaetze mit Kuerzung 2027: s_op 15,825 %, s_Z 29,825 %", [s.grenzsatz_operativ(1), s.grenzsatz_zinsen(1)],
                 ["0.15825", "0.29825"], "0")
    # R-7.16 Hinzurechnung (GEWSTG-8)
    pruefe(k, "Hinzurechnung: 300.000 Entgelte, 40.000 Erbbauzins, Freibetrag 200.000: 15.825 + 14 % von 130.000",
           st(KOERPERSCHAFT).jahr(1, D(100000), NULL, NULL, D(300000), D(40000)), "34025.00", "0")
    pruefe(k, "Hinzurechnung bei sofortiger Verrechnung (Freibetrag verbraucht): 60.000 Entgelte",
           st(KOERPERSCHAFT, verlust="sofort").jahr(1, D(100000), NULL, NULL, D(60000)), "31925.00", "0")
    s = st(KOERPERSCHAFT, verlust="sofort")
    pruefe(k, "Entlastungssatz der Sollzinsen bei sofortiger Verrechnung: 29,825 % - 25 % x 14 %", s.grenzsatz_sollzinsen(1), "0.26325", "0")
    # R-7.6 (GEWSTG-10A): Personengesellschaft traegt den Gewerbeverlust vor
    s = st(GEWERBLICHE_PG, verlust="sofort")
    pruefe(k, "Personengesellschaft, sofort, Verlust 50.000: Erstattung nur der Einkommensteuer", s.jahr(1, D(-50000), NULL), "-21000.00", "0")
    pruefe(k, "... Folgejahr 80.000: Gewerbesteuer auf 30.000 nach Vortrag, voll angerechnet", s.jahr(2, D(80000), NULL), "33600.00", "0")
    pruefe(k, "... Gewerbesteuer des Folgejahres", s.protokoll[-1]["gewerbesteuer"], "770.00", "0")
    pruefe(k, "Einzelunternehmen, sofort, Verlust 50.000: Gewerbesteuer linear, Anrechnung gleicht aus",
           st(EINZELUNTERNEHMEN, verlust="sofort").jahr(1, D(-50000), NULL), "-21000.00", "0")
    # R-7.17, R-7.18
    pruefe(k, "Koerperschaft ohne Gewerbesteuer, 100.000 im Jahr 2027", st(KOERPERSCHAFT_OHNE_GEWST).jahr(1, D(100000), NULL), "15825.00", "0")
    pg = dict(hebesatz=D("4.40"), anteil_natuerliche=D("0.6"))
    pruefe(k, "gepraegte Personengesellschaft, 440 %, 60 %, Verkaufsgewinn 500.000 als laufender Gewinn (MA-036)",
           st(GEPRAEGTE_PG, **pg).jahr(1, NULL, NULL, D(500000)), "243285.00", "0")
    pruefe(k, "... als Aufgabegewinn (andere Lesart MA-036): Gewerbeertrag 40 %",
           st(GEPRAEGTE_PG, aufgabegewinn=True, **pg).jahr(1, NULL, NULL, D(500000)), "222285.00", "0")
    # R-7.11 Privatperson
    pruefe(k, "Privat, Verkauf nach 10 Jahren: Verlust 20.000, Gewinn 200.000, Vorfaelligkeit 30.000: 42 % von 150.000",
           st(PRIVAT, haltedauer=10).jahr(10, D(-20000), NULL, D(200000), NULL, NULL, D(30000)), "63000.00", "0")
    s = st(PRIVAT, haltedauer=11)
    pruefe(k, "Privat, Verkauf nach 11 Jahren: Gewinn steuerfrei, Vorfaelligkeit nicht abziehbar",
           s.jahr(11, D(-20000), NULL, D(200000), NULL, NULL, D(30000)), "0", "0")
    pruefe(k, "... Verlustvortrag aus Vermietung", s.vv, "20000", "0")
    # M-45
    s = st(KOERPERSCHAFT)
    s.jahr(1, D(-1500000), NULL)
    s.jahr(2, D(2000000), NULL)
    pruefe_gleich(k, "Verlustvortrag 1,5 Mio. Euro in einem Jahr verrechnet: Hinweis M-45", sorted(s.hinweise), ["M-45"])
    # R-7.1: Kennzeichen nur bei Koerperschaft und gewerblich gepraegter Personengesellschaft
    for name, status in (("Einzelunternehmen", EINZELUNTERNEHMEN), ("originaer gewerbliche Personengesellschaft", GEWERBLICHE_PG),
                         ("Privatperson", PRIVAT)):
        erg = kalkuliere(replace(A.ANKAUF, steuer=A.steuer(status, erweiterte_kuerzung=True)), VG, KAT)
        pruefe_gleich(k, f"Kennzeichen der Kuerzung bei {name}: Eingabemeldung", (erg["status"], erg["meldungen"][0]["kennung"]), ("eingabe", "M-20"))
    e = rechne_grob(replace(A.ANKAUF, steuer=A.steuer(BEFREIT)), VG, KAT)
    pruefe_gleich(k, "befreite Koerperschaft: Hinweis M-44 zum Verkaufsjahr", "M-44" in kennungen(e), True)
    # R-6.16 anschaffungsnahe Herstellungskosten (ESTG-6)
    for betrag in (320000, 400000):
        e = rechne_grob(replace(A.ANKAUF, stau_betrag=D(betrag)), VG, KAT)
        z = e.plan.zeilen[24]
        pruefe_fest(k, f"Erhaltung {betrag} im Jahr 2: Zahlung, davon aktiviert, Meldungen",
                    [str(z["erhaltung"] + z["investition"]), str(z["investition"]), kennungen(e)])
        pruefe_fest(k, f"Erhaltung {betrag} im Jahr 2: Abschreibung im Jahr 3, Endwert", [str(e.plan.zeilen[36]["afa"]), str(e.plan.endwert)])
    pruefe(k, "Schwelle: 15 % der Gebaeudeanschaffungskosten von 1.980.000", KAT.ahk_quote * D(1980000), "297000", "0")
    pruefe(k, "400.000 x 1,0609 ohne 19 % Umsatzsteuer", D(400000) * D("1.0609") / D("1.19"), "356605.04", "0.005")
    # R-7.3, R-7.19 Zuschuss nach MA-031
    werte = {}
    for lesart in ("sofort", "verteilt", "minderung"):
        for jahre in (38, 20):
            e = rechne_grob(replace(GEFOERDERT, haltedauer=jahre), replace(VG, ma031_zuschuss=lesart), KATN)
            werte[(lesart, jahre)] = (e.kennzahlen["endwertdifferenz"], e.kennzahlen["rendite"])
            pruefe_gleich(k, f"Zuschuss '{lesart}', {jahre} Jahre: Kontrollsummen", (e.gesperrt, e.befunde), (False, []))
            pruefe_fest(k, f"Zuschuss '{lesart}', {jahre} Jahre: Endwert, Endwertdifferenz, Summe der Steuern, Eigenkapital der Investitionsphase",
                        [str(e.plan.endwert), str(e.kennzahlen["endwertdifferenz"]), str(sum(e.plan.reihe("steuer"))), str(e.eigenkapital_investitionsphase)])
            proz_fest(k, f"Zuschuss '{lesart}', {jahre} Jahre: VOFI-Rendite", e.kennzahlen["rendite"])
    for jahre in (38, 20):
        pruefe_gleich(k, f"voreingestellte Lesart 'sofort' hat die niedrigste Endwertdifferenz und Rendite ({jahre} Jahre)",
                      werte[("sofort", jahre)] == min(werte[(l, jahre)] for l in ("sofort", "verteilt", "minderung")), True)
    pruefe_gleich(k, "Zuschuss ueber den Kosten, auf die er entfaellt: Meldung M-43",
                  kalkuliere(replace(GEFOERDERT, foerderung=replace(A.FOERDERUNG_B, zuschussquote=D("1.1"), darlehensquote=NULL, eigenmittelquote=NULL)),
                             VG, KATN)["meldungen"][0]["kennung"], "M-43")
    # R-7.15 einbehaltene Entgelte: verteilt (Betriebsvermoegen) gegen Jahr der Zahlung
    e_v = rechne_grob(GEFOERDERT, VG, KATN)
    e_s = rechne_grob(GEFOERDERT, replace(VG, ma032_entgelte_sofort=True), KATN)
    pruefe_fest(k, "einbehaltene Entgelte 65.393,64: abgezogen im Planjahr 1, 2 und 3 (verteilt ueber die zinslose Zeit)",
                [str(e_v.plan.jahressumme("einbehalt_steuer", j)) for j in (1, 2, 3)])
    pruefe(k, "... Summe der verteilten Betraege", sum(e_v.plan.reihe("einbehalt_steuer")), str(e_v.bemessung.einbehalt_darlehen + e_v.bemessung.einbehalt_zuschuss), "0")
    pruefe_fest(k, "... Endwert verteilt gegen Abzug im Jahr der Zahlung (andere Lesart MA-032)", [str(e_v.plan.endwert), str(e_s.plan.endwert)])
    # R-7.11 im Finanzplan: Privatperson, Vorfaelligkeit als Veraeusserungskosten
    for jahre, bindung in ((5, 10),):
        e = rechne_grob(replace(A.ANKAUF, steuer=A.steuer(PRIVAT), haltedauer=jahre, zinsbindung_jahre=bindung, stau_betrag=NULL), VG, KAT)
        t = e.plan.steuer.protokoll[-1]
        pruefe_fest(k, f"Privatperson, Verkauf nach {jahre} Jahren, Bindung {bindung}: Vorfaelligkeit, steuerlicher Verkaufsgewinn, Steuer des Jahres",
                    [str(e.plan.zeilen[jahre * 12]["vfe"]), str(t["verkaufsgewinn_steuerlich"]), str(t["steuer"])])


def rf18_miete():
    k = fall("RF-18", "Miete im Bestand (BGB-558), Leerstand, Fluktuation, Kosten, Verkaufspreis")

    def erhoehungen(e, bis=157):
        return [[m, str(e.miete_je_qm[m].quantize(D("0.0001")))] for m in range(2, bis) if e.miete_je_qm[m] != e.miete_je_qm[m - 1]]

    basis = rechne_grob(A.ANKAUF, VG, KAT)
    # MA-037: vorsichtige Lesart gegen die andere Lesart und gegen eine bekannte Mietenhistorie
    andere = rechne_grob(A.ANKAUF, replace(VG, ma037_vorsicht=False), KAT)
    pruefe_fest(k, "MA-037 andere Lesart (drei Jahre unveraendert): Erhoehungen (Monat, Miete)", erhoehungen(andere))
    pruefe_fest(k, "MA-037: Endwert vorsichtig gegen andere Lesart", [str(basis.plan.endwert), str(andere.plan.endwert)])
    tp = tragbarer_preis(A.ANKAUF, replace(VG, ma037_vorsicht=False), KAT)
    pruefe_fest(k, "MA-037 andere Lesart: hoechster tragbarer Kaufpreis", tp["preis"], 0)
    hist = rechne_grob(replace(A.ANKAUF, mietenhistorie=(6, D("7.50"))), VG, KAT)
    pruefe_fest(k, "Mietenhistorie bekannt (letzte Erhoehung vor 6 Monaten von 7,50 Euro): Erhoehungen", erhoehungen(hist))
    pruefe(k, "... erste Erhoehung im Monat 13 bis zur Kappungsgrenze 7,50 x 1,15", hist.miete_je_qm[13], "8.625", "0")
    pruefe_gleich(k, "... MA-037 wirkt nicht", "MA-037" in hist.modellannahmen, False)
    # Anpassungsdauer null: im Jahr 1 gilt die Ist-Miete, danach das Ziel Vergleichsmiete mit Wartefrist und Kappung
    d0 = rechne_grob(replace(A.ANKAUF, anpassungsdauer=0), VG, KAT)
    pruefe(k, "Anpassungsdauer 0: Miete im Monat 12 ist die Ist-Miete", d0.miete_je_qm[12], "8.50", "0")
    pruefe_fest(k, "Anpassungsdauer 0: Erhoehungen", erhoehungen(d0))
    pruefe(k, "Anpassungsdauer 0: Reinertrag im ersten Jahr unveraendert", d0.bemessung.reinertrag_vj, str(basis.bemessung.reinertrag_vj), "0")
    # Ist-Miete ueber der Vergleichsmiete: Rueckfuehrung; die Bank setzt die Vergleichsmiete an
    hoch = rechne_grob(replace(A.ANKAUF, ist_miete=D("11.00")), VG, KAT)
    pruefe_fest(k, "Ist-Miete 11,00 ueber Vergleichsmiete 9,20: Miete im ersten Monat der Jahre 1 bis 7",
                [str(hoch.miete_je_qm[(j - 1) * 12 + 1].quantize(D("0.0001"))) for j in range(1, 8)])
    pruefe_fest(k, "... Reinertrag des Vorhabens, nachhaltiger Reinertrag der Bank, Bankdarlehen",
                [str(hoch.bemessung.reinertrag_vj), str(hoch.bemessung.ertrag_nachhaltig), str(hoch.darlehen)])
    hoch2 = rechne_grob(replace(A.ANKAUF, ist_miete=D("11.00")), replace(VG, ma026_ertrag_vorhaben=True), KAT)
    pruefe_fest(k, "... andere Lesart MA-026 (Ertrag des Vorhabens): Bankdarlehen", hoch2.darlehen)
    # leerstehendes Objekt und Teilleerstand (R-6.13)
    leer = replace(A.ANKAUF, leere_flaeche=D(1320), ist_miete=NULL)
    e = rechne_grob(leer, VG, KAT)
    pruefe_gleich(k, "leerstehendes Objekt: Kontrollsummen", (e.gesperrt, e.befunde), (False, []))
    pruefe_fest(k, "leerstehendes Objekt: Miete je m2 in den Monaten 3, 4 und 144", [str(e.miete_je_qm[m].quantize(D("0.0001"))) for m in (3, 4, 144)])
    pruefe(k, "... Neuvermietungsmiete: 9,20 x 1,10 nach der Mietpreisbremse, unter der Marktmiete 10,50", e.miete_je_qm[4], "10.12", "0")
    pruefe_fest(k, "leerstehendes Objekt: Bankdarlehen, Endwert, Verkaufspreis, Einstiegsfaktor",
                [str(e.darlehen), str(e.plan.endwert), str(e.verkauf.preis_brutto), str(e.einstiegsfaktor)])
    tp = tragbarer_preis(leer, VG, KAT)
    pruefe_fest(k, "leerstehendes Objekt: hoechster tragbarer Kaufpreis und Meldung", [str(tp["preis"]), tp["meldung"]])
    e = rechne_grob(leer, VG, replace(KAT, mietpreisbremse=False))
    pruefe(k, "leerstehendes Objekt ohne Mietpreisbremse: Marktmiete", e.miete_je_qm[4], "10.50", "0")
    pruefe_gleich(k, "Ist-Miete null bei vermieteter Flaeche: Eingabemeldung",
                  kalkuliere(replace(A.ANKAUF, ist_miete=NULL), VG, KAT)["meldungen"][0]["kennung"], "M-20")
    teil = rechne_grob(replace(A.ANKAUF, leere_flaeche=D(200)), VG, KAT)
    pruefe_fest(k, "200 m2 leer: Sollmiete im Monat 1 und 4, Einstiegsfaktor", [str(teil.ertrag.soll(1)), str(teil.ertrag.soll(4)), str(teil.einstiegsfaktor.quantize(D("0.01")))])
    # Fluktuation (R-6.14)
    fl = rechne_grob(A.ANKAUF, replace(VG, fluktuation=D("0.05")), KAT)
    pruefe_fest(k, "Fluktuation 5 % je Jahr: Miete je m2 im ersten Monat der Jahre 1 bis 6",
                [str(fl.miete_je_qm[(j - 1) * 12 + 1].quantize(D("0.0001"))) for j in range(1, 7)])
    pruefe(k, "... Jahr 2: 95 % zu 8,50 und 5 % zu 10,3224 (9,384 x 1,10)", fl.miete_je_qm[13], "8.59112", "0.000001", 5)
    pruefe_fest(k, "Fluktuation 5 %: Endwert", fl.plan.endwert)
    # sonstige Ertraege und Erbbauzins (R-6.15, R-6.11, R-8.1)
    so = rechne_grob(replace(A.ANKAUF, sonstige_ertraege=D(6000)), VG, KAT)
    pruefe(k, "sonstige Ertraege 6.000 Euro je Jahr: Sollmiete im Monat 1", so.ertrag.soll(1), "11720.00", "0")
    erb = rechne_grob(replace(A.ANKAUF, erbbauzins=D(12000), erbbauzins_steigerung=D("0.02")), VG, KAT)
    pruefe_fest(k, "Erbbauzins 12.000 Euro: massgebliche Jahresmiete am Verkaufsstichtag, Verkaufspreis, Einstiegsfaktor",
                [str(erb.ertrag.jahresmiete(144)), str(erb.verkauf.preis_brutto), str(erb.einstiegsfaktor.quantize(D("0.01")))])
    pruefe(k, "... Minderung des Verkaufspreises: 18 x 12 x Erbbauzins des Monats 144", basis.verkauf.preis_brutto - erb.verkauf.preis_brutto,
           str(18 * 12 * erb.ertrag.erbbau_monat(144)), "0.01")
    # CO2-Kosten (R-6.9) und Instandhaltung nach Baualter (R-6.8)
    pruefe(k, "CO2-Kosten des Vermieters im Jahr 1: 30 kg x 1.320 m2 x 40 % x 50 Euro je Tonne", D(30) * 1320 * D("0.4") * 50 / 1000, "792", "0")
    c5 = rechne_grob(A.ANKAUF, VG, replace(KAT, co2_kosten_5a_je_qm=D("0.10")))
    pruefe(k, "weitere Vermieterkosten 0,10 Euro je m2 (CO2KOSTAUFG-5A): Bewirtschaftung im Monat 1", c5.plan.zeilen[1]["kosten"], "2420.33", "0")
    alt = rechne_grob(replace(A.ANKAUF, baujahr=1996), VG, KAT)
    pruefe_reihe(k, "Baujahr 1996: Bewirtschaftung im Monat 1 (Stufe 11,50 Euro) und im Monat 13 (Stufe 14 Euro, Index 1,02)",
                 [alt.plan.zeilen[1]["kosten"], alt.plan.zeilen[13]["kosten"]], ["2134.33", "2459.50"], "0")
    # struktureller Leerstand im Verkaufspreis (R-8.1; Bericht Grenzfaelle GF-48)
    for quote in ("0.015", "0.295"):
        e = rechne_grob(A.ANKAUF, replace(VG, leerstand=D(quote)), KAT)
        pruefe_fest(k, f"Leerstand {quote}: Verkaufspreis, Endwertdifferenz", [str(e.verkauf.preis_brutto), str(e.kennzahlen["endwertdifferenz"])])
        proz_fest(k, f"Leerstand {quote}: VOFI-Rendite", e.kennzahlen["rendite"])
    # Darstellung in vollen Euro mit Rundungsdifferenz (R-12.7)
    mieten = [x["miete"] for x in verdichte(basis.plan)[1:]]
    dar = darstellung(mieten)
    pruefe_fest(k, "Darstellung der Jahresmieten in vollen Euro: Summe, Summe der gerundeten Zeilen, Rundungsdifferenz",
                [str(dar["summe"]), str(sum(dar["zeilen"])), str(dar["rundungsdifferenz"])])
    pruefe_gleich(k, "Zeilenkennungen des Finanzplans sind eindeutig", len({v[0] for v in ZEILEN.values()}), len(ZEILEN))


def rf19_bank():
    k = fall("RF-19", "Darlehen und Bankensicht: kalkulatorischer Kapitaldienst, Vorfaelligkeit, Eigenkapitalgrenze, Vorgaben")
    basis = rechne_grob(A.ANKAUF, VG, KAT)
    pruefe(k, "Bankdarlehen mit kalkulatorischem Zins 5 % (Gegenrechnung der Rolle Bank)", basis.darlehen, "1226609.99", "0")
    vz = replace(VG, ma026_vertragszins=True)
    e = rechne_grob(A.ANKAUF, vz, KAT)
    pruefe(k, "andere Lesart MA-026 (Vertragszins 4 %): Bankdarlehen wie im Entwurf", e.darlehen, "1431044.99", "0")
    tp = tragbarer_preis(A.ANKAUF, vz, KAT)
    pruefe_fest(k, "andere Lesart MA-026 (Vertragszins): hoechster tragbarer Kaufpreis", tp["preis"], 0)
    e = rechne_grob(A.ANKAUF, replace(VG, kalk_zins=D("0.06")), KAT)
    pruefe_fest(k, "fester kalkulatorischer Zins 6 % (H-25): Bankdarlehen", e.darlehen)
    # Mindestansatz der Bewirtschaftung (BELWERTV-11) im Neubau
    n = rechne_grob(A.NEUBAU, VG, KATN)
    pruefe(k, "Neubau: nachhaltiger Reinertrag = 85 % des Rohertrags von 396.000 Euro", n.bemessung.ertrag_nachhaltig, "336600.00", "0")
    pruefe_fest(k, "Neubau: Reinertrag des Vorhabens im ersten Jahr der Vollvermietung", n.bemessung.reinertrag_vj)
    # Vorfaelligkeit mit Kuendigungsrecht (BGB-489)
    for jahre, bindung in ((1, 40), (5, 20), (12, 15), (12, 12)):
        e = rechne_grob(replace(A.ANKAUF, haltedauer=jahre, zinsbindung_jahre=bindung, stau_betrag=NULL), VG, KAT)
        pruefe_fest(k, f"Haltedauer {jahre}, Zinsbindung {bindung}: Abloesung, Vorfaelligkeit, Meldung M-25",
                    [str(e.plan.zeilen[jahre * 12]["abloesung"]), str(e.plan.zeilen[jahre * 12]["vfe"]), "M-25" in kennungen(e)])
    e = rechne_grob(replace(A.ANKAUF, haltedauer=5, zinsbindung_jahre=20, stau_betrag=NULL), VG, KAT)
    pruefe(k, "... Haltedauer 5, Bindung 20: Restbindung 66 Monate bis zum fruehesten Kuendigungstermin",
           e.plan.zeilen[60]["vfe"], str(CENT.geld(e.plan.zeilen[60]["abloesung"] * D("0.01") * 66 / 12)), "0")
    for foerder in (True, False):
        g = replace(GEBUNDEN, haltedauer=5, uebernommen=dict(GEBUNDEN.uebernommen, foerderdarlehen=foerder))
        e = rechne_grob(g, VG, KAT)
        pruefe_fest(k, f"uebernommenes Darlehen, Kennzeichen Foerderdarlehen {foerder}, Verkauf nach 5 Jahren: Vorfaelligkeit aller Darlehen", e.plan.zeilen[60]["vfe"])
    # Eigenkapitalgrenze mit Nachschuessen (R-11.6): dieselbe Massnahme zum Stichtag und im Jahr 1
    for jahr in (0, 1):
        tp = tragbarer_preis(replace(A.ANKAUF, stau_betrag=D(420000), stau_jahr=jahr, verfuegbares_ek=D(1200000)), VG, KAT)
        pruefe_fest(k, f"Massnahme 420.000 im Jahr {jahr}, verfuegbares Eigenkapital 1,2 Mio.: Preis, bindende Grenze, Eigenkapitalbedarf",
                    [str(tp["preis"]), tp["bindend"], str(tp["ergebnis"].eigenkapitalbedarf)])
    tp = tragbarer_preis(replace(A.ANKAUF, stau_jahr=0, verfuegbares_ek=D(100)), replace(VG, beleihungsquote=NULL, zielrendite=D("0.01")), KAT)
    pruefe_gleich(k, "ohne Darlehen, Massnahme zum Stichtag, verfuegbares Eigenkapital 100 Euro: kein tragbarer Preis (M-46)",
                  (tp["preis"], tp["meldung"]), (None, "M-46"))
    # Deckung ueber die Haltedauer (R-10.14): Fall der Rolle Bank
    fall2 = replace(A.ANKAUF, zins=D("0.03"), ist_miete=D("8.50"), vergleichsmiete=D("8.50"), stau_betrag=NULL)
    vg2 = replace(VG, mietsteigerung=D("0.005"), ma026_vertragszins=True)
    for stress in (False, True):
        e = rechne_grob(fall2, vg2, KAT, stress=stress)
        name = "Stressfall" if stress else "Basisfall"
        pruefe_fest(k, f"Zins 3 %, Mietsteigerung 0,5 %, Vertragskonditionen, {name}: Deckung Jahr 1, kleinste Deckung, Jahr, Meldungen",
                    [str(e.dscr_vj.quantize(D("0.0001"))), str(e.deckung_min.quantize(D("0.0001"))), e.deckung_min_jahr, kennungen(e)])
    f = rechne_grob(GEFOERDERT, VG, KATN, stress=True)
    pruefe_fest(k, "gefoerderter Neubau im Stressfall: kleinste Deckung, Jahr, Meldungen",
                [str(f.deckung_min.quantize(D("0.0001"))), f.deckung_min_jahr, kennungen(f)])
    # Stressgroessen einzeln (R-11.8)
    einzeln = {}
    for name, st in (("Anschlusszins", dict(anschlusszins_pp=D("0.01"))), ("Zinsanstieg bis zur Zusage", dict(zusage_pp=D("0.005"))),
                     ("Leerstand", dict(leerstand_pp=D("0.02"))), ("Mietsteigerung", dict(mietsteigerung_pp=D("0.005"))),
                     ("Instandhaltung", dict(instandhaltung_rel=D("0.10"))), ("Verkaufsfaktor", dict(verkaufsfaktor_rel=D("0.10"))),
                     ("Investitionsstau", dict(stau_rel=D("0.10")))):
        e = rechne_grob(A.ANKAUF, replace(VG, stress=grobkalkulation.Stress(**st)), KAT, stress=True)
        einzeln[name] = str((e.kennzahlen["endwertdifferenz"] - basis.kennzahlen["endwertdifferenz"]).quantize(D("0.01")))
    pruefe_fest(k, "Stressgroessen einzeln: Aenderung der Endwertdifferenz gegen den Basisfall", einzeln)
    # Anschlussregeln (H-07, MA-034): Endwert und kleinste Deckung
    regeln = {}
    for regel in ("rate", "tilgungssatz", "restlaufzeit"):
        e = rechne_grob(A.ANKAUF, replace(VG, anschluss_regel=regel), KAT)
        regeln[regel] = [str(e.plan.endwert), str(e.deckung_nach_bindung["Bankdarlehen"][1].quantize(D("0.0001"))), str(e.kennzahlen["endwertdifferenz"])]
    pruefe_fest(k, "Anschlussregeln: Endwert, Deckung im Jahr 11, Endwertdifferenz", regeln)
    # Vorgaben im Vorhaben (R-3.2)
    e = rechne_grob(replace(A.ANKAUF, abweichungen={"mietsteigerung": (D("0.015"), None), "beleihungsquote": (D("0.60"), None)}), VG, KAT)
    pruefe_fest(k, "strengere Vorgaben im Vorhaben: Liste (Kennung, Art) und Meldungen",
                [[a["kennung"], a["art"]] for a in e.abweichungen] + kennungen(e))
    pruefe_gleich(k, "Lockerung ohne Begruendung: Eingabemeldung",
                  kalkuliere(replace(A.ANKAUF, abweichungen={"mietsteigerung": (D("0.025"), None)}), VG, KAT)["meldungen"][0]["kennung"], "M-20")
    e = rechne_grob(replace(A.ANKAUF, abweichungen={"mietsteigerung": (D("0.025"), "Mietspiegel 2026, Fortschreibung")}), VG, KAT)
    pruefe_fest(k, "Lockerung mit Begruendung: Liste und Meldungen", [[a["kennung"], a["art"], a["begruendung"]] for a in e.abweichungen] + kennungen(e))
    _, liste = vorgaben_im_vorhaben(VG, {"anschluss_regel": ("restlaufzeit", None)})
    pruefe_gleich(k, "H-07: 'Restlaufzeit bleibt' gilt als strenger als 'Tilgungssatz bleibt'", liste[0]["art"], "strenger")
    pruefe_gleich(k, "H-07: 'Rate bleibt' ohne Begruendung ist eine Lockerung",
                  meldung_von(lambda: vorgaben_im_vorhaben(VG, {"anschluss_regel": ("rate", None)})), "M-20")
    pruefe_gleich(k, "Wertansatz der Bank ueber dem Kaufpreis ohne Begruendung: Eingabemeldung",
                  kalkuliere(replace(A.ANKAUF, wertansatz_bank=D(2600000)), VG, KAT)["meldungen"][0]["kennung"], "M-20")
    e = rechne_grob(replace(A.ANKAUF, wertansatz_bank=D(2600000), wertansatz_begruendung="Gutachten vom Stichtag"), VG, KAT)
    pruefe_gleich(k, "Wertansatz ueber dem Kaufpreis mit Begruendung: M-35", "M-35" in kennungen(e), True)
    # Bereitstellungszinsen (R-5.18): Gegenrechnung der Rolle Bank am frueheren Abruf nicht moeglich; Formelprobe
    z = n.plan.zeilen
    pruefe(k, "Neubau: Bereitstellungszins im Monat 7 (erster Monat nach der bereitstellungsfreien Zeit)", z[7]["bereit"],
           str(CENT.geld(n.darlehen * D("0.0025"))), "0")


def rf20_raender():
    k = fall("RF-20", "Raender der Eingaben und der Suchen (Bericht Grenzfaelle); der Aufruf endet nie mit einem Fehler")

    def status(ein, vg=VG, kat=KAT, **kw):
        erg = kalkuliere(ein, vg, kat, **kw)
        return [erg["status"]] + sorted(m["kennung"] for m in erg["meldungen"] if m["kennung"] not in ("M-37",))

    # GF-02, GF-31: Zins und Tilgung null
    null = replace(VG, mindesttilgung=NULL, anschluss_aufschlag=NULL)
    e = rechne_grob(replace(A.ANKAUF, zins=NULL, tilgungssatz=NULL), null, KAT)
    pruefe_gleich(k, "Zins und Tilgung null: gerechnet, (b) unbegrenzt, es bindet (a)", (e.gesperrt, e.bemessung.bank["b"], e.bemessung.bank["bindend"]), (False, None, ["a"]))
    pruefe_fest(k, "Zins und Tilgung null: Bankdarlehen, Endwert", [str(e.darlehen), str(e.plan.endwert)])
    e = rechne_grob(replace(A.ANKAUF, tilgungssatz=NULL), replace(VG, mindesttilgung=NULL, anschluss_regel="restlaufzeit"), KAT)
    pruefe_gleich(k, "Tilgung null mit 'Restlaufzeit bleibt': gerechnet mit Hinweis M-40", (e.gesperrt, "M-40" in kennungen(e)), (False, True))
    # Eingabepruefung (GF-03, GF-04, GF-06, GF-07, GF-21, GF-25, GF-41)
    for name, ein, vg, kat in (
            ("Bankzins -0,5 %", replace(A.ANKAUF, zins=D("-0.005")), VG, KAT),
            ("Bankzins -2 % bei 2 % Tilgung", replace(A.ANKAUF, zins=D("-0.02")), VG, KAT),
            ("Kaufpreis 0", replace(A.ANKAUF, kaufpreis=NULL), VG, KAT),
            ("Ist- und Vergleichsmiete 0", replace(A.ANKAUF, ist_miete=NULL, vergleichsmiete=NULL), VG, KAT),
            ("Verkaufsfaktor 0", replace(A.ANKAUF, verkaufsfaktor=NULL), VG, KAT),
            ("Steuersatz 100 %", replace(A.ANKAUF, steuer=A.steuer(PRIVAT, est_satz=EINS)), VG, KAT),
            ("Neubau, Bauzeit 0", replace(A.NEUBAU, bauzeit_monate=0), VG, KATN),
            ("Haltedauer 43 Jahre", replace(A.ANKAUF, haltedauer=43), VG, KAT),
            ("Land fehlt", replace(A.ANKAUF, land=""), VG, KAT),
            ("Mindestdeckung 0,9", A.ANKAUF, replace(VG, mindestdeckung=D("0.9")), KAT),
            ("KfW-Darlehen ueber dem Hoechstbetrag", replace(A.NEUBAU, kfw_betrag=D(3000001)), VG, KATN)):
        pruefe_gleich(k, f"{name}: Eingabemeldung M-20", status(ein, vg, kat), ["eingabe", "M-20"])
    # GF-40: Bauzeit 60, Haltedauer 6: im Stressfall endet die Haltedauer vor der Vollvermietung
    pruefe_gleich(k, "Neubau, Bauzeit 60 Monate, Haltedauer 6 Jahre: M-23 schon im Basisfall",
                  status(replace(A.NEUBAU, bauzeit_monate=60, haltedauer=6), VG, KATN), ["eingabe", "M-23"])
    # rueckwirkender Stichtag ist zulaessig (R-3.3, E-02)
    pruefe_gleich(k, "Stichtag Maerz 2019 (Nachkalkulation): gerechnet", status(replace(A.ANKAUF, stichtag_jahr=2019, stichtag_monat=3))[0], "ergebnis")
    # GF-19b: Zielrendite bei keinem zulaessigen Preis erreicht; kleinster zulaessiger Preis ueber einem Euro
    gf19 = replace(A.ANKAUF, verkaufsfaktor=D(4), uebernommen=dict(restschuld=D(2000000), zins=D("0.06"), tilgungssatz=D("0.02")))
    tp = tragbarer_preis(gf19, VG, KAT)
    pruefe_gleich(k, "uebernommenes Darlehen 2,0 Mio. Euro zu 6 %, Faktor 4: kein tragbarer Preis (M-32)", (tp["preis"], tp["meldung"]), (None, "M-32"))
    pruefe_fest(k, "... kleinster zulaessiger Preis (darunter M-22)", tp["unten"])
    # GF-44: Vollfinanzierung ohne Eigenkapital
    gf44 = replace(A.ANKAUF, enk_satz=NULL, verkaufsfaktor=D(5), stau_betrag=NULL)
    tp = tragbarer_preis(gf44, replace(VG, beleihungsquote=EINS, mindestdeckung=EINS, ma026_vertragszins=True), KAT)
    pruefe_gleich(k, "Vollfinanzierung ohne Eigenkapital: kein tragbarer Preis (M-41)", (tp["preis"], tp["meldung"]), (None, "M-41"))
    pruefe_fest(k, "... Preis, bis zu dem der Endwert ohne Eigenkapital nicht negativ ist (Nebenangabe)", tp["renditegrenze"])
    # GF-35: Preis genau an der Obergrenze des Suchbereichs
    tp0 = tragbarer_preis(A.ANKAUF, VG, KAT)
    bezug = max(tp0["ergebnis"].ertrag.jahresmiete(1), tp0["ergebnis"].ertrag.jahresmiete(144))
    tp = tragbarer_preis(A.ANKAUF, replace(VG, such_obergrenze_faktor=D(tp0["preis"]) / bezug), KAT)
    pruefe_gleich(k, "tragbarer Preis genau an der Obergrenze: Preis gefunden, keine Meldung M-33",
                  (tp["oben"], tp["preis"], tp["meldung"]), (tp0["preis"], tp0["preis"], None))
    # Nichtmonotonie durch die Abrundung des Gewerbeertrags (R-11.5): Zielrendite 5,000253 %
    tp = tragbarer_preis(A.ANKAUF, replace(VG, zielrendite=D("0.05000253")), KAT)
    vz = "".join("+" if rechne_grob(A.ANKAUF, replace(VG, zielrendite=D("0.05000253")), KAT, preis=x, mit_blatt=False).kennzahlen["endwertueberschuss"] >= 0 else "-"
                 for x in range(2317185, 2317200))
    pruefe_gleich(k, "Zielrendite 5,000253 %: Vorzeichen des Ziels fuer die Preise 2.317.185 bis 2.317.199", vz, "++++----++++---")
    pruefe_gleich(k, "... tragbarer Preis ist der groesste Preis, bis zu dem jeder kleinere das Ziel erreicht; Meldung M-34",
                  (tp["preis"], tp["meldung"]), (2317188, "M-34"))
    # GF-36: zwei Loesungen in einer Rasterzelle
    s = zielwertsuche(lambda x: (x - 3) * (x - D("3.2")), 0, 10, D("0.01"), VG.suchraster)
    pruefe_gleich(k, "zwei Loesungen in einer Rasterzelle: Status nennt die Rasterstellen", (s["status"], str(s["rasterweite"])),
                  ("keine Loesung: Ziel an allen Rasterstellen erreicht", "0.25"))
    # Verlust beim Verkauf (R-10.17, M-42)
    e = rechne_grob(replace(A.ANKAUF, verkaufsfaktor=D(4), haltedauer=2, stau_betrag=NULL), replace(VG, ma026_vertragszins=True), KAT)
    pruefe_fest(k, "Verkaufsfaktor 4, Verkauf nach zwei Jahren: Endwert, Fehlbetrag beim Verkauf, laufender Nachschussbedarf, Meldungen",
                [str(e.plan.endwert), str(e.fehlbetrag_verkauf), str(e.nachschuss_laufend), kennungen(e)])
    # GF-20 und weitere Statusfaelle: der Aufruf endet nie mit einem Programmfehler
    pruefe_gleich(k, "Zuschuss 80 % bei Grundstueck 5 Mio. Euro: gerechnet (Aufteilung auf Gebaeude und Boden)",
                  status(replace(GEFOERDERT, grundstueckspreis=D(5000000), bodenrichtwert=D(2500),
                                 foerderung=replace(A.FOERDERUNG_B, zuschussquote=D("0.8"), darlehensquote=NULL, eigenmittelquote=NULL)),
                         replace(VG, ma031_zuschuss="minderung"), KATN)[0], "ergebnis")
    # R-14.13: Meldungen, die kein anderer Fall ausloest
    tr = Tranche("D", 1000000, "annuitaet_prozent", "0.04", tilgungssatz="0.02", bindung=2)
    try:
        lauf(tr, 3, 1)
        m24 = None
    except ValueError as x:
        m24 = str(x)[:4]
    pruefe_gleich(k, "Darlehen ohne Anschlusszins, Laufzeit ueber die Zinsbindung: M-24", m24, "M-24")
    pruefe_gleich(k, "Grobfoerderung ohne Zins nach der zinslosen Zeit, Haltedauer 38 Jahre: Eingabemeldung M-24",
                  status(replace(GEFOERDERT, foerderung=replace(A.FOERDERUNG_B, zins_danach=None)), VG, KATN), ["eingabe", "M-24"])
    pruefe_gleich(k, "interner Zinsfuss mit zwei Loesungen: Hinweis M-26; mit einer Loesung kein Hinweis",
                  (meldung_izf(izf([D(-1000), D(5000), D(-6000)])[0])[0], meldung_izf(izf([D(-100), D(110)])[0])), ("M-26", None))
    for name, kw, soll in (("Nachschuss im Jahr 2 und Entnahme im Jahr 3: Hinweis M-27", dict(einlagen={2: 50000}, entnahmen={3: 50000}), ["M-27"]),
                           ("Nachschuss und Entnahme im selben Jahr (saldiert): kein Hinweis", dict(einlagen={2: 50000}, entnahmen={2: 50000}), []),
                           ("Testfall ohne Eigenkapital: Status M-28", dict(ek=0), ["M-28"]),
                           ("Testfall mit Verkauf zu 500.000 Euro: Status M-29", dict(verkauf=500000), ["M-29"])):
        p_, a_, kz_ = s1(**kw)
        pruefe_gleich(k, name, [m[0] for m in renditemeldungen(p_.einlagen_netto, p_.entnahmen_netto, kz_)], soll)
    tp = tragbarer_preis(A.ANKAUF, replace(VG, leerstand=EINS, forderungsausfall=NULL), KAT)
    pruefe_gleich(k, "struktureller Leerstand 100 %: Preissuche ohne Suchbereich (M-31)", (tp["preis"], tp["meldung"]), (None, "M-31"))
    try:
        zielwertsuche(lambda x: x, 5, 5, D("0.01"), VG.suchraster)
        m31 = None
    except Meldung as m:
        m31 = m.kennung
    pruefe_gleich(k, "Zielwertsuche mit Bereich 5 bis 5: M-31", m31, "M-31")
    e = rechne_grob(replace(A.ANKAUF, zins=D("0.03"), ist_miete=D("8.50"), vergleichsmiete=D("8.50"), stau_betrag=NULL),
                    replace(VG, mietsteigerung=D("0.005"), ma026_vertragszins=True, anschluss_aufschlag=D("0.04")), KAT)
    pruefe_gleich(k, "Anschlusszins 7 % nach Lesart 2 von MA-026: kleinste Deckung unter 1, Planjahr, Meldung M-39",
                  [str(e.deckung_min.quantize(D("0.0001"))), e.deckung_min_jahr, kennungen(e)], ["0.9522", 12, ["M-37", "M-39"]])
    # R-3.1: keine Zahlenliterale in den Kernmodulen ausser technischen Konstanten
    # erlaubt: 0, 1, 2 (Halbieren), 12 (Monate je Jahr), 3 (Nachkommastellen der Darstellung), 60 (Rechenstellen),
    # 80 (Bisektionsschritte), 1000 (Kilogramm je Tonne), Cent, zwoelf Rechenstellen, Rechentoleranz
    erlaubt = {"0", "1", "2", "3", "12", "60", "80", "1000", "0.01", "1E-12", "1E-30", "-1"}
    fund = set()
    ordner = os.path.dirname(os.path.abspath(__file__))
    for modul in ("zahlen", "zeit", "darlehen", "ertrag", "steuer", "restwert", "finanzplan", "kennzahlen", "proben", "grobkalkulation"):
        quelle = open(os.path.join(ordner, modul + ".py"), encoding="utf-8").read()
        for tok in tokenize.generate_tokens(io.StringIO(quelle).readline):
            if tok.type == tokenize.NUMBER and tok.string not in erlaubt:
                fund.add((modul, tok.string))
            if tok.type == tokenize.STRING and re.fullmatch(r"-?\d+(\.\d+)?(E-?\d+)?", tok.string.strip("\"'")) \
                    and tok.string.strip("\"'") not in erlaubt:
                fund.add((modul, tok.string))
    pruefe_gleich(k, "Kernmodule ohne Zahlenliterale ausser 0, 1, 2, 12 und technischen Konstanten", sorted(fund), [])


def alle():
    rf16_sperre()
    rf17_steuer()
    rf18_miete()
    rf19_bank()
    rf20_raender()
