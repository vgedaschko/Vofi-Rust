"""Referenzfaelle RF-11 bis RF-14: Grobkalkulation 1a (Ankauf, Neubau, Steuerstatus) und Randfaelle.

Eigene Faelle ohne veroeffentlichte Werte: Die Sollwerte sind in erwartete_werte.json festgeschrieben (R-15.2);
der Basisfall des Ankaufs ist zusaetzlich in gegenrechnung.py unabhaengig nachgebaut. Die Eingaben stehen in
annahmen.py und im Anhang A der Fachspezifikation.
"""
from decimal import Decimal as D
from dataclasses import replace
from zahlen import NULL, EINS, d, de, proz, Rundung
from steuer import (KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST, GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN, PRIVAT,
                    BEFREIT)
from kennzahlen import schuldendienstdeckung
from grobkalkulation import (rechne_grob, tragbarer_preis, zielwertsuche, suche_eingabe, haltedauer_tabelle,
                             vergleiche, Meldung, kalkuliere)
from finanzplan import verdichte
import annahmen as A
from rf_rahmen import (fall, pruefe, pruefe_fest, pruefe_proz, pruefe_reihe, pruefe_gleich, info, jahresplan,
                       lehrbuch_steuer, izf)
from rf_testfall import s1

VG, KAT, KATN = A.VORGABEN, A.KATALOG, A.KATALOG_NEUBAU

# Varianten der Referenzobjekte (Anhang A)
GEBUNDEN = replace(A.ANKAUF, gebunden_anteil=D("0.4"), bindung_jahre=6, gebundene_miete=D("6.80"),
                   uebernommen=dict(restschuld=D(500000), nennbetrag=D(600000), zins=D("0.005"), tilgungssatz=D("0.02"),
                                    bindung_jahre=8, anschluss_zins=D("0.03"), beitrag_satz=D(0)))
GEFOERDERT = replace(A.NEUBAU, foerderung=A.FOERDERUNG_B, haltedauer=38)
# Begruendung fuer Lesarten und Eingaben, die ein Referenzfall bewusst von der Voreinstellung abweichend setzt (R-3.2)
GRUND = {k: "Lesart des Referenzfalls" for k in ("zuschuss_verteilung", "steuer.kuerzung_bleibt_verkaufsjahr", "festpreis", "vorvermietet")}
MIT_KFW = replace(A.NEUBAU, kfw_betrag=D(3000000), kfw_laufzeit=35, kfw_tilgungsfrei=1)


def proz_fest(k, name, wert, stellen=3):
    pruefe_fest(k, name + " (%)", None if wert is None else wert * 100, stellen)


def kennungen(e):
    return sorted(m["kennung"] for m in e.meldungen)


def blatt(k, name, e, kurz=False):
    """Schreibt die Groessen des verkuerzten Kennzahlenblatts fest (R-11.12)."""
    kz = e.kennzahlen
    pruefe_gleich(k, f"{name}: alle Kontrollsummen bestanden", (e.gesperrt, len(e.befunde)), (False, 0))
    pruefe_fest(k, f"{name}: Bankdarlehen", e.darlehen)
    pruefe_fest(k, f"{name}: bindende Grenze des Darlehens", e.bemessung.bank["bindend"])
    pruefe_fest(k, f"{name}: Eigenkapital der Investitionsphase", e.eigenkapital_investitionsphase)
    pruefe_fest(k, f"{name}: Endwert", e.plan.endwert)
    pruefe_fest(k, f"{name}: Endwert der Unterlassensalternative", e.alt.endwert)
    pruefe_fest(k, f"{name}: Endwertdifferenz", kz["endwertdifferenz"])
    proz_fest(k, f"{name}: VOFI-Rendite", kz["rendite"])
    pruefe_fest(k, f"{name}: Meldungen", kennungen(e))
    if kurz:
        return
    proz_fest(k, f"{name}: Vergleichsrendite", kz["vergleichsrendite"])
    pruefe_fest(k, f"{name}: Abstand zur Zielrendite (Prozentpunkte)", kz["abstand_zielrendite"] * 100, 3)
    pruefe_fest(k, f"{name}: Endwertueberschuss", kz["endwertueberschuss"])
    pruefe_fest(k, f"{name}: laufender Nachschussbedarf nach der Investitionsphase", e.nachschuss_laufend)
    pruefe_fest(k, f"{name}: Fehlbetrag beim Verkauf", e.fehlbetrag_verkauf)
    pruefe_fest(k, f"{name}: Schuldendienstdeckung im ersten Jahr der Vollvermietung", e.dscr_vj, 4)
    pruefe_fest(k, f"{name}: kleinste Schuldendienstdeckung", e.deckung_min, 4)
    pruefe_fest(k, f"{name}: Planjahr der kleinsten Deckung", e.deckung_min_jahr)
    pruefe_fest(k, f"{name}: Zinsdeckung im ersten Jahr der Vollvermietung", e.zinsdeckung_vj, 4)
    pruefe_fest(k, f"{name}: Kapitaldienstreserve", e.kapitaldienstreserve)
    proz_fest(k, f"{name}: Darlehen zu Kaufpreis oder Gesamtkosten", e.darlehen_zu_wert, 2)
    proz_fest(k, f"{name}: Restschuld zum Wert am Ende der Zinsbindung", e.restschuld_zu_wert, 2)
    pruefe_fest(k, f"{name}: Einstiegsfaktor", e.einstiegsfaktor, 2)
    pruefe_fest(k, f"{name}: Ausstiegsfaktor", e.ausstiegsfaktor, 2)
    proz_fest(k, f"{name}: Nettoanfangsrendite", e.nettoanfangsrendite, 2)
    proz_fest(k, f"{name}: Restwertanteil am Endwert", e.restwertanteil, 2)
    pruefe_fest(k, f"{name}: Verkaufspreis", e.verkauf.preis_brutto)
    proz_fest(k, f"{name}: VOFI-Gesamtkapitalrendite", e.gesamtkapitalrendite)
    pruefe_fest(k, f"{name}: Modellannahmen, die gewirkt haben", e.modellannahmen)


def preis(k, name, tp):
    pruefe_fest(k, f"{name}: Preis", tp["preis"], 0)
    pruefe_fest(k, f"{name}: bindende Grenze und Meldung", [tp["bindend"], tp["meldung"]])
    if tp["preis"] is not None:
        e = tp["ergebnis"]
        pruefe_gleich(k, f"{name}: Preisprobe P-14", tp["p14"], True)
        pruefe_fest(k, f"{name}: Grenze, die das Darlehen bestimmt", e.bemessung.bank["bindend"])
        pruefe_fest(k, f"{name}: noetiges Eigenkapital", e.eigenkapital_investitionsphase)
        pruefe_fest(k, f"{name}: Preis je m2 Wohnflaeche", tp["preis_je_qm"])
        pruefe_fest(k, f"{name}: Abstand zum Angebotspreis", tp["abstand_angebot"])


def rf11_ankauf():
    k = fall("RF-11", "Grobkalkulation Ankauf (Monatsraster, Koerperschaft; Vorgaben und Katalog als Annahme)")
    e = rechne_grob(A.ANKAUF, VG, KAT)
    blatt(k, "Basisfall", e)
    bm = e.bemessung
    pruefe_fest(k, "Basisfall: Reinertrag im ersten Jahr", bm.reinertrag_vj)
    pruefe_fest(k, "Basisfall: nachhaltiger Reinertrag der Bank", bm.ertrag_nachhaltig)
    pruefe_fest(k, "Basisfall: Grenzen (a), (b), (c)", [str(bm.bank[x]) for x in "abc"])
    pruefe_fest(k, "Basisfall: Miete je m2 im ersten Monat der Jahre 1 bis 13",
                [str(e.miete_je_qm[(j - 1) * 12 + 1].quantize(D("0.0001"))) for j in range(1, 14)])
    wechsel = [m for m in range(2, 157) if e.miete_je_qm[m] != e.miete_je_qm[m - 1]]
    pruefe_fest(k, "Basisfall: Monate, ab denen eine Mieterhoehung wirkt", wechsel)
    pruefe_fest(k, "Basisfall: Miete je m2 nach jeder Erhoehung", [str(e.miete_je_qm[m].quantize(D("0.0001"))) for m in wechsel])
    j = verdichte(e.plan)
    pruefe_fest(k, "Basisfall: Jahresmiete Jahr 1 (Einzahlung nach Mietausfall)", j[1]["miete"])
    pruefe_fest(k, "Basisfall: Bewirtschaftung Jahr 1", j[1]["kosten"])
    pruefe_fest(k, "Basisfall: Investitionsstau, Zahlung in Jahr 2 (Preisstand 1,03^2)", j[2]["erhaltung"])
    pruefe_fest(k, "Basisfall: Steuer Jahre 1 bis 4", [str(x["steuer"]) for x in j[1:5]])
    pruefe_fest(k, "Basisfall: Rate ab Jahr 11 nach Anschlusszins (Jahressumme)", j[11]["zins"] + j[11]["tilgung"])
    pruefe_fest(k, "Basisfall: Restschuld am Ende der Zinsbindung", e.plan.zeilen[120]["restschuld"])
    pruefe_fest(k, "Basisfall: Abloesung beim Verkauf", e.plan.zeilen[144]["abloesung"])
    pruefe_fest(k, "Basisfall: massgebliche Jahresmiete am Verkaufsstichtag", e.ertrag.jahresmiete(144))
    pruefe_fest(k, "Basisfall: Verkaufsgewinn", e.plan.zeilen[144]["g_v"])
    pruefe_fest(k, "Basisfall: Steuer auf den Verkaufsgewinn", e.steuer_verkaufsgewinn)
    pruefe_fest(k, "Basisfall: Schuldendienstdeckung je Planjahr",
                [str(schuldendienstdeckung(e.plan, x)[0].quantize(D("0.001"))) for x in range(1, 13)])
    pruefe_fest(k, "Basisfall: Deckung im ersten Jahr nach der Zinsbindung", str(e.deckung_nach_bindung["Bankdarlehen"][1].quantize(D("0.0001"))))
    pruefe_fest(k, "Basisfall: Anteil der Miete und Mietausfall, bei denen die Deckung 1 ist (%)",
                [str((x * 100).quantize(D("0.01"))) for x in (e.anteil_miete_deckung_eins, e.ausfall_deckung_eins)])
    info(f"Endwert {de(e.plan.endwert)}, Endwertdifferenz {de(e.kennzahlen['endwertdifferenz'])}, "
         f"Rendite {proz(e.kennzahlen['rendite'])}, Darlehen {de(e.darlehen)} {bm.bank['bindend']}")
    # kombinierter Stressfall: Darlehen aus dem Basisfall (R-11.8)
    es = rechne_grob(A.ANKAUF, VG, KAT, stress=True)
    blatt(k, "kombinierter Stressfall", es)
    pruefe_gleich(k, "Stressfall: Bankdarlehen mit dem Zinsanstieg bis zur Zusage neu bemessen, sonst aus dem Basisfall (R-11.8)",
                  (es.darlehen < e.darlehen, es.darlehen_basis == e.darlehen), (True, True))
    pruefe(k, "Stressfall: Bankdarlehen bei 4,5 % Zins und 5,5 % kalkulatorisch (Gegenrechnung Bank und Finanzmathematiker)",
           es.darlehen, "1144835.99", "0")
    pruefe(k, "Stressfall: Endwertdifferenz mit neu bemessenem Darlehen (Gegenrechnung Finanzmathematiker 216.856,20 mit dem Stress auf die Instandhaltung, der entfallen ist)",
           es.kennzahlen["endwertdifferenz"], "237324.51", "0")
    pruefe_fest(k, "Stressfall: Schuldendienstdeckung je Planjahr",
                [str(schuldendienstdeckung(es.plan, x)[0].quantize(D("0.001"))) for x in range(1, 13)])
    # hoechster tragbarer Preis
    tp = tragbarer_preis(A.ANKAUF, VG, KAT)
    preis(k, "tragbarer Kaufpreis, Basisfall", tp)
    pruefe_fest(k, "tragbarer Kaufpreis, Basisfall: Faktor", tp["faktor"], 2)
    pruefe_fest(k, "tragbarer Kaufpreis, Basisfall: Endwertueberschuss beim Preis", tp["ergebnis"].kennzahlen["endwertueberschuss"])
    tps = tragbarer_preis(A.ANKAUF, VG, KAT, stress=True)
    preis(k, "tragbarer Kaufpreis, Stressfall", tps)
    pruefe_fest(k, "tragbarer Kaufpreis, Stressfall: kleinste Deckung", tps["ergebnis"].deckung_min, 4)
    tpe = tragbarer_preis(replace(A.ANKAUF, verfuegbares_ek=D(1200000)), VG, KAT)
    preis(k, "tragbarer Kaufpreis bei 1,2 Mio. Euro verfuegbarem Eigenkapital", tpe)
    pruefe_fest(k, "... Eigenkapitalbedarf einschliesslich aller Nachschuesse", tpe["ergebnis"].eigenkapitalbedarf)
    # Knick zwischen Beleihungsquote und Mindestdeckung (R-11.5)
    knick = int(bm.bank["b"] / VG.beleihungsquote)
    r = [rechne_grob(A.ANKAUF, VG, KAT, preis=knick + dx, mit_blatt=False).kennzahlen["rendite"]
         for dx in (-20000, -10000, 0, 10000, 20000)]
    pruefe_fest(k, "Knick b/beta: Preis", knick)
    pruefe_gleich(k, "Rendite faellt beiderseits des Knicks", all(b < a for a, b in zip(r, r[1:])), True)
    pruefe_fest(k, "Rendite um den Knick, je 10.000 Euro (%)", [str((x * 100).quantize(D("0.0001"))) for x in r])
    preise = range(1500000, 3600001, 100000)
    rs = [rechne_grob(A.ANKAUF, VG, KAT, preis=x, mit_blatt=False).kennzahlen["rendite"] for x in preise]
    pruefe_gleich(k, "Rendite faellt von 1,5 bis 3,6 Mio. Euro in jedem Schritt von 100.000 Euro", all(b < a for a, b in zip(rs, rs[1:])), True)
    # Zielwertsuche auf gekennzeichnete Eingaben (R-11.9, R-11.10)
    s = suche_eingabe(A.ANKAUF, VG, KAT, "vergleichsmiete", D("6.00"), D("20.00"), D("0.01"))
    pruefe_gleich(k, "Zielwertsuche Vergleichsmiete bei 2,4 Mio. Euro: Status", s["status"], "eine Loesung")
    pruefe_fest(k, "Zielwertsuche: noetige Vergleichsmiete", s["loesungen"][0]["wert"])
    s = suche_eingabe(replace(A.ANKAUF, kaufpreis=D(2200000)), VG, KAT, "stau_betrag", D(0), D(1000000), D(100))
    pruefe_fest(k, "Zielwertsuche: tragbarer Investitionsstau beim Kaufpreis 2,2 Mio. Euro", s["loesungen"][0]["wert"])
    s = suche_eingabe(A.ANKAUF, VG, KAT, "verkaufsfaktor", D(8), D(40), D("0.01"))
    pruefe_fest(k, "Zielwertsuche: kritischer Verkaufsfaktor", s["loesungen"][0]["wert"])
    s = suche_eingabe(A.ANKAUF, VG, KAT, "vergleichsmiete", D("6.00"), D("9.00"), D("0.01"))
    pruefe_gleich(k, "Zielwertsuche ohne Loesung im Bereich", s["status"], "keine Loesung: Ziel an allen Rasterstellen verfehlt")
    s = zielwertsuche(lambda x: (x - 3) * (x - 7), 0, 10, D("0.01"), VG.suchraster)
    pruefe_gleich(k, "Zielwertsuche auf eine nicht monotone Funktion: beide Loesungen gemeldet",
                  (s["status"], [str(l["wert"]) for l in s["loesungen"]]), ("2 Loesungen", ["3.00", "7.00"]))
    try:
        suche_eingabe(A.ANKAUF, VG, KAT, "haltedauer", 1, 30, 1)
        m = None
    except Meldung as x:
        m = x.kennung
    pruefe_gleich(k, "Zielwertsuche auf die Haltedauer ist nicht zugelassen", m, "M-30")
    # gebundener Bestand mit uebernommenem Darlehen
    eg = rechne_grob(GEBUNDEN, VG, KAT)
    blatt(k, "Ankauf gebundener Bestand mit uebernommenem Darlehen", eg, kurz=True)
    pruefe_fest(k, "gebundener Bestand: Miete je m2 im ersten Monat der Jahre 1 bis 12",
                [str(eg.miete_je_qm[(j - 1) * 12 + 1].quantize(D("0.0001"))) for j in range(1, 13)])
    pruefe_fest(k, "gebundener Bestand: kalkulatorischer Kapitaldienst des uebernommenen Darlehens", eg.bemessung.kd_uebrige)
    pruefe_fest(k, "gebundener Bestand: tatsaechlicher Kapitaldienst des uebernommenen Darlehens im ersten Jahr",
                eg.kd_je_darlehen["Uebernommenes Darlehen"])
    pruefe_fest(k, "gebundener Bestand: Grenzen (a), (b), (c)", [str(eg.bemessung.bank[x]) for x in "abc"])
    pruefe_fest(k, "gebundener Bestand: Deckung im ersten Jahr nach jeder Zinsbindung",
                {n: [j_, str(x.quantize(D("0.0001")))] for n, (j_, x) in eg.deckung_nach_bindung.items()})
    egs = rechne_grob(GEBUNDEN, VG, KAT, stress=True)
    pruefe_fest(k, "gebundener Bestand im Stressfall: Zins des uebernommenen Darlehens im Jahr 9 (Anschluss mit Aufschlag)",
                egs.plan.jahressumme("zins", 9) - sum(egs.plan.zeilen[u]["tranchen"]["Bankdarlehen"]["zins"] for u in range(97, 109)))
    pruefe_fest(k, "gebundener Bestand im Stressfall: kleinste Deckung und Jahr", [str(egs.deckung_min.quantize(D("0.0001"))), egs.deckung_min_jahr])
    # Vergleich zweier Fassungen (R-11.11): frei und gebunden
    v = vergleiche(e, eg)
    pruefe_fest(k, "Vergleich zweier Fassungen: Zahl der verglichenen Blattgroessen", len(v["zeilen"]))
    pruefe_fest(k, "Vergleich zweier Fassungen: Differenz der Endwertdifferenz (gebunden - frei)", v["zeilen"][2][3])
    pruefe_fest(k, "Vergleich zweier Fassungen: abweichende Werte des Auftrags", sorted(x[1] for x in v["abweichende_werte"]))
    pruefe_gleich(k, "Vergleich zweier Fassungen: gleiche Kernversion", v["versionsgleich"], True)
    # Haltedauertabelle (R-11.13)
    tab = haltedauer_tabelle(A.ANKAUF, VG, KAT, 8, 13)
    pruefe_fest(k, "Haltedauertabelle 8 bis 13 Jahre: VOFI-Rendite (%)", [str((x[3] * 100).quantize(D("0.001"))) for x in tab])


def rf12_neubau():
    k = fall("RF-12", "Grobkalkulation Neubau in Grobform (frei finanziert, mit KfW-Darlehen, mit Grobfoerderung)")
    n = rechne_grob(A.NEUBAU, VG, KATN)
    blatt(k, "Neubau frei finanziert", n)
    z = n.plan.zeilen
    bm = n.bemessung
    pruefe_fest(k, "Neubau: Baukosten zum Preisstand des Stichtags", bm.baukosten_stichtag)
    pruefe_fest(k, "Neubau: Baukosten mit Baupreissteigerung ueber die Bauzeit", bm.baukosten)
    pruefe_fest(k, "Neubau: Monatsraten 1, 2 und 18", [str(z[u]["investition"]) for u in (1, 2, 18)])
    pruefe_fest(k, "Neubau: Mittelbedarf ohne Bauzeitzinsen", bm.mittelbedarf)
    pruefe_fest(k, "Neubau: Grenzen (a), (b), (c)", [str(bm.bank[x]) for x in "abc"])
    pruefe_fest(k, "Neubau: Reinertrag im ersten Jahr der Vollvermietung", bm.reinertrag_vj)
    pruefe_fest(k, "Neubau: Bauzeitzinsen (Summe der Zinsen in der Bauzeit)", sum(x["zins"] for x in z[1:19]))
    pruefe_fest(k, "Neubau: Bereitstellungszinsen", sum(x["bereit"] for x in z))
    pruefe_fest(k, "Neubau: Monat der ersten Auszahlung des Bankdarlehens", min(u for u in range(19) if z[u]["auszahlung"] > 0))
    pruefe_fest(k, "Neubau: erster Monat mit Miete (nach dem Anlaufleerstand)", min(u for u in range(1, 60) if z[u]["miete"] > 0))
    pruefe_fest(k, "Neubau: Rate des Bankdarlehens im Monat 19 (Zins, Tilgung)", [str(z[19]["zins"]), str(z[19]["tilgung"])])
    pruefe_fest(k, "Neubau: Abschreibung im Planjahr 2 (sechs Monate)", z[24]["afa"])
    wechsel = [m for m in range(23, 100) if n.miete_je_qm[m] != n.miete_je_qm[m - 1]]
    pruefe_fest(k, "Neubau: Monate, ab denen eine Mieterhoehung wirkt (bis Monat 99)", wechsel)
    tp = tragbarer_preis(A.NEUBAU, VG, KATN)
    preis(k, "tragbarer Grundstueckspreis, frei finanziert", tp)
    if tp["preis"] is not None:
        pruefe_fest(k, "tragbarer Grundstueckspreis: je m2 Grundstueck", tp["preis_je_qm_grundstueck"])
    ns = rechne_grob(A.NEUBAU, VG, KATN, stress=True)
    blatt(k, "Neubau kombinierter Stressfall", ns, kurz=True)
    pruefe_gleich(k, "Neubau Stressfall: Mehrkosten traegt das Eigenkapital",
                  ns.eigenkapital_investitionsphase > n.eigenkapital_investitionsphase and ns.darlehen <= n.darlehen, True)
    pruefe(k, "Neubau Stressfall: Bankdarlehen neu bemessen mit 5,5 % und 2 %: 280.500 / 7,5 %", ns.darlehen, "3740000.00", "0")
    pruefe_fest(k, "Neubau Stressfall: Baukosten", ns.baukosten)
    # KfW-Darlehen als eigene Tranche (R-5.19)
    kf = rechne_grob(MIT_KFW, VG, KATN)
    blatt(k, "Neubau mit KfW-Darlehen", kf, kurz=True)
    pruefe_fest(k, "KfW: Grenzen (a), (b), (c)", [str(kf.bemessung.bank[x]) for x in "abc"])
    pruefe_fest(k, "KfW: kalkulatorischer Kapitaldienst", kf.bemessung.kd_uebrige)
    pruefe_fest(k, "KfW: Monat der ersten Auszahlung, erster Tilgungsmonat",
                [min(kf.plan.e.tranchen[1].auszahlung), min(u for u in range(1, 80) if kf.plan.zeilen[u]["tranchen"]["KfW-Darlehen"]["tilgung"] > 0)])
    pruefe_fest(k, "KfW: Kapitaldienst je Darlehen im ersten Jahr der Vollvermietung", {a: str(b) for a, b in kf.kd_je_darlehen.items()})
    tpk = tragbarer_preis(MIT_KFW, VG, KATN)
    preis(k, "tragbarer Grundstueckspreis mit KfW-Darlehen", tpk)
    # Stellplaetze (R-6.15)
    sp = rechne_grob(replace(A.NEUBAU, stellplaetze=20, stellplatz_miete=D(60)), VG, KATN)
    pruefe_fest(k, "Neubau mit 20 Stellplaetzen: Baukosten zum Preisstand des Stichtags", sp.bemessung.baukosten_stichtag)
    pruefe_fest(k, "Neubau mit 20 Stellplaetzen: Sollmiete im ersten Vermietungsmonat", sp.ertrag.soll(22))
    # Grobfoerderung (R-11.14), Haltedauer bis ein Jahr nach dem Bindungsende
    f = rechne_grob(GEFOERDERT, VG, KATN)
    blatt(k, "Neubau mit Grobfoerderung, Haltedauer 38 Jahre", f)
    bm = f.bemessung
    pruefe_fest(k, "Grobfoerderung: Foerderdarlehen", bm.foerderdarlehen)
    pruefe_fest(k, "Grobfoerderung: Zuschuss", bm.zuschuss)
    pruefe_fest(k, "Grobfoerderung: Anteil des Zuschusses, der auf das Gebaeude entfaellt", bm.zuschuss_gebaeude)
    pruefe_fest(k, "Grobfoerderung: Mindesteigenkapital", bm.ek_min)
    pruefe_fest(k, "Grobfoerderung: einbehaltene Entgelte", bm.einbehalt_darlehen + bm.einbehalt_zuschuss)
    pruefe_fest(k, "Grobfoerderung: Mittelbedarf", bm.mittelbedarf)
    pruefe_fest(k, "Grobfoerderung: Kapitaldienst des Foerderdarlehens im Jahr", bm.kd_uebrige)
    pruefe_fest(k, "Grobfoerderung: nachhaltiger Reinertrag", bm.ertrag_nachhaltig)
    pruefe_fest(k, "Grobfoerderung: Grenzen (a), (b), (c)", [str(bm.bank[x]) for x in "abc"])
    o = f.ohne_bankdarlehen
    pruefe_fest(k, "Grobfoerderung ohne Bankdarlehen: Deckung der uebrigen Darlehen", o["deckung_uebrige"], 4)
    pruefe_fest(k, "... Kapitaldienstreserve", o["reserve"])
    pruefe_fest(k, "... Reinertrag, bei dem die Restfinanzierung moeglich waere", o["reinertrag_noetig"])
    pruefe_fest(k, "... Miete je m2, bei der die Restfinanzierung moeglich waere", o["miete_noetig"])
    pruefe_fest(k, "... Eigenkapital ueber dem Mindesteigenkapital", o["eigenkapital_ueber_mindest"])
    pruefe_fest(k, "... Nachschuesse je Planjahr 1 bis 12", [str(x) for x in f.nachschuss_je_jahr[1:13]])
    pruefe_fest(k, "Grobfoerderung: Miete je m2 im Monat 22 und im ersten Monat der Bindungsjahre 4, 7 und 10",
                [str(f.miete_je_qm[m].quantize(D("0.0001"))) for m in (22, 55, 91, 127)])
    pruefe(k, "Grobfoerderung, 38 Jahre: Rueckzahlung des Zuschusses nach Bindungsende", f.verkauf.foerder_rueckzahlung, "0", "0")
    f20 = rechne_grob(replace(GEFOERDERT, haltedauer=20), VG, KATN)
    blatt(k, "Neubau mit Grobfoerderung, Verkauf nach 20 Jahren", f20, kurz=True)
    pruefe_fest(k, "Grobfoerderung, 20 Jahre: Rueckzahlung des Zuschusses beim Verkauf (MA-017)", f20.verkauf.foerder_rueckzahlung)
    pruefe_fest(k, "Grobfoerderung, 20 Jahre: Abloesung des Foerderdarlehens beim Verkauf", f20.plan.zeilen[240]["tranchen"]["Foerderdarlehen"]["abloesung"])
    pruefe_fest(k, "Grobfoerderung, 20 Jahre: Verkaufspreis aus der gebundenen Miete", f20.verkauf.preis_brutto)
    v = vergleiche(rechne_grob(replace(A.NEUBAU, haltedauer=38), VG, KATN), f)
    pruefe_fest(k, "Vergleich frei gegen gefoerdert (38 Jahre): Differenz der Endwertdifferenz", v["zeilen"][2][3])
    tab = haltedauer_tabelle(GEFOERDERT, VG, KATN, 36, 39)
    pruefe_fest(k, "Grobfoerderung, Haltedauertabelle 36 bis 39 Jahre: Rendite (%)", [str((x[3] * 100).quantize(D("0.001"))) for x in tab])


def rf13_steuerstatus():
    k = fall("RF-13", "Grobkalkulation Ankauf je Steuerstatus (derselbe Fall, angenommener Katalogstand)")
    faelle = (("Koerperschaft", A.steuer(KOERPERSCHAFT)),
              ("Koerperschaft mit erweiterter Kuerzung (MA-030: Verkaufsgewinn gewerbesteuerpflichtig)",   # seit Runde 2:
               A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True)),     # im Verkaufsjahr entfaellt die Kuerzung ganz
              ("Koerperschaft mit erweiterter Kuerzung, Kuerzung bleibt im Verkaufsjahr (E-69)",
               A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True, kuerzung_bleibt_verkaufsjahr=True)),
              ("Koerperschaft, Verluste sofort verrechnet", A.steuer(KOERPERSCHAFT, verlust="sofort")),
              ("Koerperschaft ohne Gewerbesteuer (Verein, Stiftung)", A.steuer(KOERPERSCHAFT_OHNE_GEWST)),
              ("originaer gewerbliche Personengesellschaft, Hebesatz 400 %", A.steuer(GEWERBLICHE_PG)),
              ("originaer gewerbliche Personengesellschaft, Hebesatz 440 %", A.steuer(GEWERBLICHE_PG, hebesatz=D("4.40"))),
              ("originaer gewerbliche Personengesellschaft, 440 %, natuerliche Personen 60 %",
               A.steuer(GEWERBLICHE_PG, hebesatz=D("4.40"), anteil_natuerliche=D("0.6"))),
              ("originaer gewerbliche Personengesellschaft, 440 %, Verluste sofort verrechnet",
               A.steuer(GEWERBLICHE_PG, hebesatz=D("4.40"), verlust="sofort")),
              ("gewerblich gepraegte Personengesellschaft, 440 %, mit Kuerzung",
               A.steuer(GEPRAEGTE_PG, hebesatz=D("4.40"), erweiterte_kuerzung=True)),
              ("gewerblich gepraegte Personengesellschaft, 440 %, 60 %, Objektverkauf als Aufgabegewinn (andere Lesart MA-036)",
               A.steuer(GEPRAEGTE_PG, hebesatz=D("4.40"), anteil_natuerliche=D("0.6"), aufgabegewinn=True)),
              ("Einzelunternehmen mit Betriebsvermoegen, Hebesatz 440 %", A.steuer(EINZELUNTERNEHMEN, hebesatz=D("4.40"))),
              ("Privatperson, Verkauf nach 12 Jahren", A.steuer(PRIVAT)),
              ("befreite Koerperschaft", A.steuer(BEFREIT)))
    for name, st in faelle:
        e = rechne_grob(replace(A.ANKAUF, steuer=st, begruendungen=GRUND), VG, KAT)
        kz = e.kennzahlen
        pruefe_gleich(k, f"{name}: Kontrollsummen", (e.gesperrt, len(e.befunde)), (False, 0))
        pruefe_fest(k, f"{name}: Endwert", e.plan.endwert)
        pruefe_fest(k, f"{name}: Endwertdifferenz", kz["endwertdifferenz"])
        proz_fest(k, f"{name}: VOFI-Rendite", kz["rendite"])
        proz_fest(k, f"{name}: Vergleichsrendite", kz["vergleichsrendite"])
        pruefe_fest(k, f"{name}: Summe der Steuerzahlungen", sum(e.plan.reihe("steuer")))
        pruefe_fest(k, f"{name}: Steuer auf den Verkaufsgewinn", e.steuer_verkaufsgewinn)
    p10 = rechne_grob(replace(A.ANKAUF, steuer=A.steuer(PRIVAT), haltedauer=10), VG, KAT)
    p11 = rechne_grob(replace(A.ANKAUF, steuer=A.steuer(PRIVAT), haltedauer=11), VG, KAT)
    pruefe_fest(k, "Privatperson, Verkauf nach 10 Jahren: Steuer auf den Verkaufsgewinn", p10.steuer_verkaufsgewinn)
    pruefe(k, "Privatperson, Verkauf nach 11 Jahren: Steuer auf den Verkaufsgewinn", p11.steuer_verkaufsgewinn, "0", "0")
    tab = haltedauer_tabelle(replace(A.ANKAUF, steuer=A.steuer(PRIVAT)), VG, KAT, 9, 12)
    pruefe_fest(k, "Privatperson, Haltedauertabelle 9 bis 12 Jahre: Rendite (%)", [str((x[3] * 100).quantize(D("0.001"))) for x in tab])


def rf14_randfaelle():
    k = fall("RF-14", "Randfaelle mit definiertem Ergebnis (Kapitel 14)")
    # R-14.1 Zinssaetze null
    plan, alt, kz = s1(h="0", kk="0", zins="0")
    pruefe(k, "alle Zinssaetze null: Endwert der Unterlassensalternative = Eigenkapital", alt.endwert, "400000", "0")
    pruefe_proz(k, "alle Zinssaetze null: Vergleichsrendite", kz["vergleichsrendite"], "0.000")
    pruefe_fest(k, "alle Zinssaetze null: Endwert", plan.endwert)
    # R-14.2 Eigenkapital null
    plan, alt, kz = s1(ek=0)
    pruefe_gleich(k, "Eigenkapital null: Rendite nicht definiert", kz["rendite"], None)
    pruefe_gleich(k, "Eigenkapital null: Status", kz["rendite_status"], "nicht definiert (kein Eigenkapital)")
    pruefe_fest(k, "Eigenkapital null: Endwert = Endwertdifferenz", plan.endwert)
    pruefe(k, "Eigenkapital null: Endwert der Unterlassensalternative", alt.endwert, "0", "0")
    # R-14.3 negativer Endwert (Kontokorrent unbegrenzt)
    plan, alt, kz = s1(verkauf=500000)
    pruefe_gleich(k, "negativer Endwert: Rendite -100 %", kz["rendite"], D(-1))
    pruefe_fest(k, "negativer Endwert: Endwert", plan.endwert)
    pruefe_gleich(k, "negativer Endwert: Kontrollsummen bestehen", len(__import__("proben").pruefe_plan(plan, alt)), 0)
    # R-14.4 Haltedauer endet vor der Vollvermietung (Bauzeit 18, Stressverlaengerung 3, Anlaufleerstand 3, dann 12 Monate)
    for jahre, soll in ((2, "eingabe"), (3, "ergebnis")):
        erg = kalkuliere(replace(A.NEUBAU, haltedauer=jahre), VG, KATN)
        pruefe_gleich(k, f"Neubau, Haltedauer {jahre} Jahre: Status und Meldung M-23",
                      (erg["status"], "M-23" in [m["kennung"] for m in erg["meldungen"]]), (soll, soll == "eingabe"))
    n3 = rechne_grob(replace(A.NEUBAU, haltedauer=3), VG, KATN)
    pruefe_fest(k, "Neubau, Haltedauer 3 Jahre: Endwert", n3.plan.endwert)
    pruefe_gleich(k, "Neubau, Haltedauer 3 Jahre: Kontrollsummen", len(n3.befunde), 0)
    # R-14.5 Verkauf im ersten Jahr
    e1 = rechne_grob(replace(A.ANKAUF, haltedauer=1, stau_betrag=NULL), VG, KAT)
    pruefe_fest(k, "Ankauf, Verkauf nach einem Jahr: Endwert", e1.plan.endwert)
    proz_fest(k, "Ankauf, Verkauf nach einem Jahr: Rendite", e1.kennzahlen["rendite"])
    pruefe_fest(k, "Ankauf, Verkauf nach einem Jahr: Vorfaelligkeitsentschaedigung (neun Jahre Restbindung)", e1.plan.zeilen[12]["vfe"])
    pruefe_fest(k, "Ankauf, Verkauf nach einem Jahr: Meldungen", kennungen(e1))
    pruefe_gleich(k, "Ankauf, Verkauf nach einem Jahr: Kontrollsummen", len(e1.befunde), 0)
    # R-14.6 Investitionsstau nach dem Verkauf: Abzug vom Verkaufserloes zum Preisstand des Stichtags
    spaet = rechne_grob(replace(A.ANKAUF, haltedauer=10, stau_betrag=D(100000), stau_jahr=12), VG, KAT)
    pruefe(k, "Stau 100.000 geplant fuer Jahr 12, Verkauf in Jahr 10: Abzug", spaet.verkauf.stau_abzug, "134391.64", "0.01")
    pruefe_gleich(k, "... Kontrollsummen einschliesslich P-05 und P-06", len(spaet.befunde), 0)
    # R-14.7 Ueberfinanzierung
    erg = kalkuliere(replace(A.ANKAUF, uebernommen=dict(restschuld=D(3000000), zins=D("0.01"), tilgungssatz=D("0.02"))), VG, KAT)
    pruefe_gleich(k, "uebernommenes Darlehen ueber dem Mittelbedarf: Meldung", erg["meldungen"][0]["kennung"], "M-22")
    # R-14.8 Leerstand 100 %: kein Ertrag, Bankdarlehen null, Verkaufspreis null
    leer = rechne_grob(A.ANKAUF, replace(VG, leerstand=D("0.995")), KAT)
    pruefe(k, "Leerstand und Forderungsausfall 100 %: Bankdarlehen", leer.darlehen, "0", "0")
    pruefe_gleich(k, "... Schuldendienstdeckung nicht definiert (kein Kapitaldienst)", leer.dscr_vj, None)
    pruefe_gleich(k, "... Kontrollsummen", len(leer.befunde), 0)
    pruefe_fest(k, "... Verkaufspreis (Faktor auf die Miete nach Leerstand)", leer.verkauf.preis_brutto)
    pruefe_fest(k, "Leerstand und Forderungsausfall 100 %: laufender Nachschussbedarf", leer.nachschuss_laufend)
    pruefe_fest(k, "... Meldungen", kennungen(leer))
    # R-14.9 kein tragbarer Preis / Preis ueber dem Suchbereich
    tp = tragbarer_preis(replace(A.ANKAUF, stau_betrag=D(6000000), stau_jahr=0), VG, KAT)
    pruefe_gleich(k, "Stau 6 Mio. Euro zum Stichtag: kein tragbarer Preis", (tp["preis"], tp["meldung"]), (None, "M-32"))
    proz_fest(k, "... Rendite beim kleinsten Preis (Angabe zu M-32)", tp["ergebnis_unten"].kennzahlen["rendite"])
    tp = tragbarer_preis(A.ANKAUF, replace(VG, zielrendite=D("-0.5")), KAT)
    pruefe_gleich(k, "Zielrendite -50 %: Ziel im ganzen Suchbereich erreicht", (tp["preis"], tp["meldung"]), (None, "M-33"))
    # R-14.10 interner Zinsfuss mehrdeutig, ohne Loesung, ausserhalb des Suchbereichs
    loes, wechsel, status = izf([D(-1000), D(5000), D(-6000)])
    pruefe_gleich(k, "interner Zinsfuss -1.000 / +5.000 / -6.000: zwei Vorzeichenwechsel", (wechsel, status), (2, "2 Loesungen"))
    pruefe_reihe(k, "... beide Loesungen 100 % und 200 %", loes, ["1", "2"], "0.000001")
    pruefe_gleich(k, "interner Zinsfuss ohne Vorzeichenwechsel: keine Loesung", izf([D(-1000), D(-50), D(-20)]), ([], 0, "keine Loesung"))
    pruefe_gleich(k, "interner Zinsfuss -100 / +1.200: Loesung ausserhalb des Suchbereichs", izf([D(-100), D(1200)])[1:],
                  (1, "Loesung ausserhalb des Suchbereichs"))
    # R-14.11 langer Zeitraum: 42 Jahre im Monatsraster, Abschreibung aufgebraucht, Zins nach der zinslosen Zeit
    lang = rechne_grob(replace(GEFOERDERT, haltedauer=42), VG, KATN)
    pruefe_gleich(k, "42 Jahre, 504 Perioden: Kontrollsummen", len(lang.befunde), 0)
    pruefe_fest(k, "42 Jahre: Endwert", lang.plan.endwert)
    pruefe_fest(k, "42 Jahre: Endwertdifferenz", lang.kennzahlen["endwertdifferenz"])
    proz_fest(k, "42 Jahre: VOFI-Rendite", lang.kennzahlen["rendite"])
    afa = [lang.plan.zeilen[j * 12]["afa"] for j in range(1, 43)]
    pruefe_fest(k, "42 Jahre: letztes Jahr mit Abschreibung", max(j + 1 for j, x in enumerate(afa) if x > 0))
    pruefe(k, "42 Jahre: Rueckzahlung des Zuschusses nach Bindungsende", lang.verkauf.foerder_rueckzahlung, "0", "0")
    zj = [lang.plan.jahressumme("zins", j) for j in range(1, 43)]
    pruefe_fest(k, "42 Jahre: erstes Planjahr mit Zins auf das Foerderdarlehen", min(j + 1 for j, x in enumerate(zj) if x > 0))
    pruefe_fest(k, "42 Jahre: Abloesung des Foerderdarlehens am Ende", lang.plan.zeilen[504]["tranchen"]["Foerderdarlehen"]["abloesung"])
    pruefe_fest(k, "42 Jahre: Instandhaltung steigt mit dem Gebaeudealter: Bewirtschaftung im Monat 19, 283 und 403 je Preisstand",
                [str(lang.plan.zeilen[u]["kosten"]) for u in (19, 283, 403)])
    # R-14.12 Jahresmodus und Monatsraster desselben Ankaufs
    ej = rechne_grob(A.ANKAUF, VG, KAT, p=1)
    pruefe_fest(k, "Ankauf im Jahresmodus: Endwert", ej.plan.endwert)
    proz_fest(k, "Ankauf im Jahresmodus: VOFI-Rendite", ej.kennzahlen["rendite"])
    pruefe_gleich(k, "Ankauf im Jahresmodus: Kontrollsummen", len(ej.befunde), 0)


def alle():
    rf11_ankauf()
    rf12_neubau()
    rf13_steuerstatus()
    rf14_randfaelle()
