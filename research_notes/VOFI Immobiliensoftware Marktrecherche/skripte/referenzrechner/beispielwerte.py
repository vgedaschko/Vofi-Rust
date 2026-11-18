#!/usr/bin/env python3
"""Zahlenbeispiele der Fachspezifikation, die ueber die Pruefwerte der Referenzfaelle hinausgehen.

    python3 beispielwerte.py

Jede Zahl, die im Dokument steht und nicht in der Ausgabe von referenzfaelle.py vorkommt, steht hier.
Die Abschnitte tragen die Nummer der Regel, in deren Beispiel die Zahl verwendet wird.
"""
from decimal import Decimal as D
from dataclasses import replace
from zahlen import NULL, EINS, d, de, proz, Rundung, periodensatz_konform
from finanzplan import lehrbuchansicht, verdichte
from kennzahlen import schuldendienstdeckung, sollzinsen_nach_steuern
from grobkalkulation import rechne_grob, tragbarer_preis
from darlehen import Tranche, bankdarlehen
import annahmen as A
from rf_rahmen import jahresplan, lehrbuch_steuer, FEST
from rf_testfall import s1, s1_monat
from rf_lehrbuch import _schulte_standard
from rf_bausteine import lauf
from rf_grob import VG, KAT, KATN, GEBUNDEN, GEFOERDERT, MIT_KFW
import restwert


def titel(t):
    print("\n== " + t)


def q4(x):
    return de(x, 4)


if __name__ == "__main__":
    rd = Rundung("cent")
    titel("R-2.6 konforme Monatssaetze")
    for i in ("0.02", "0.08", "0.05"):
        print(f"  {i}: {periodensatz_konform(D(i), 12, rd)}")
    print("  nominal 4 % / 12 auf 700.000:", de(D(700000) * D("0.04") / 12, 4), "| effektiv dazu:", proz((1 + D("0.04") / 12) ** 12 - 1, 4))

    titel("R-4.3 Testfall, Zeilen je Jahr (Rundungsmodus Cent)")
    plan, alt, kz = s1(rundung="cent")
    for z in plan.zeilen:
        print(f"  t{z['u']}: originaer {de(z['originaer'])} | Zins {de(z['zins'])} | Tilgung {de(z['tilgung'])} | Abloesung {de(z['abloesung'])} "
              f"| Habenzins {de(z['habenzins'])} | e_op {de(z['e_op'])} | Steuer {de(z['steuer'])} | Anlage {de(z['anlage'])} "
              f"| Guthaben {de(z['guthaben'])} | Restschuld {de(z['restschuld'])} | Bestandssaldo {de(z['bestandssaldo'])}")
    print("  Alternative:", [de(alt.bestand(t)) for t in range(6)])
    print("  Bemessung t1..t5:", [de(z["e_op"] + z["habenzins"]) for z in plan.zeilen[1:]])
    pu, au, ku = s1()
    print("  ungerundet: Endwert", de(pu.endwert, 4), "Guthaben t4", de(pu.zeilen[4]["guthaben"]),
          "Sollzinsen nach Steuern", de(sollzinsen_nach_steuern(pu)), "| w(0), w(2):", de(ku["w"][0], 6), de(ku["w"][2], 6))
    print("  Deckung t1..t5:", [de(schuldendienstdeckung(pu, j)[0], 4) for j in range(1, 6)])

    titel("R-2.3 Verdichtung, Testfall im Monatsraster, Jahr 1")
    pm, am, km = s1_monat(D("0.02"), D("0.08"), "cent")
    j = verdichte(pm)
    print("  Jahr 1", {k: de(j[1][k]) for k in ("miete", "zins", "tilgung", "habenzins", "afa", "steuer", "guthaben", "restschuld")})
    print("  Monat 1:", {k: de(pm.zeilen[1][k]) for k in ("miete", "zins", "tilgung", "habenzins", "guthaben", "restschuld")})
    print("  Endwert", de(pm.endwert), "Alternative", de(am.endwert), "Rendite", proz(km["rendite"]), "Differenz", de(km["endwertdifferenz"]))

    titel("R-4.7 Lehrbuchansicht, Schulte Standardbeispiel mit Steuern (Tab. 5)")
    p5, a5, k5, tr = _schulte_standard(lehrbuch_steuer("0.5"), 250)
    for z in lehrbuchansicht(p5):
        print("  t%d " % z["t"] + " | ".join(f"{k} {de(v, 0)}" for k, v in z.items() if k != "t"))
    titel("R-9 Unterlassensalternative, Schulte Standardbeispiel mit Steuern (Tab. 6)")
    for z in a5.zeilen:
        print(f"  t{z['u']}: Zins lang {de(z['zins_lang'], 0)} | Zins kurz {de(z['zins_kurz'], 0)} | Steuer {de(z['steuer'], 0)} | lang {de(z['lang'], 0)} | kurz {de(z['kurz'], 0)}")

    titel("R-10.4/R-10.5 Vergleichsfaktoren, Zaehler und Nenner im Testfall mit Nachschuss")
    pn, an, kn = s1(einlagen={2: 50000})
    print("  Zaehler", de(kn["zaehler"]), "Nenner", de(kn["nenner"]), "Rendite", proz(kn["rendite"]), "Vergleichsrendite", proz(kn["vergleichsrendite"]))
    pe, ae, ke = s1(entnahmen={t: 5000 for t in range(1, 6)})
    print("  Entnahmen: Zaehler", de(ke["zaehler"]), "aufgezinste Entnahmen", de(ke["zaehler"] - pe.endwert))
    re = [D(30000)] + [D(55000) * D("1.02") ** t for t in range(1, 5)]
    pa, aa, ka = s1(ek=420000, reinertrag=re, steuer=lehrbuch_steuer("0.30", "vortrag", False))
    pb, ab, kb = s1(ek=420000, reinertrag=re, steuer=lehrbuch_steuer("0.30", "vortrag", False), entnahmen={1: 5000})
    print("  Verlustvortrag, ohne Entnahme: Rendite", proz(ka["rendite"], 4), "| mit Entnahme 5.000 in t1:", proz(kb["rendite"], 4),
          "| Aenderung der Endwertdifferenz", de(ka["endwertdifferenz"] - kb["endwertdifferenz"]))
    print("  sofortige Verrechnung minus Vortrag (RF-10):",
          de(D(FEST["RF-10|Anlaufverlust, sofortige Verrechnung (andere Lesart): Endwert"])
             - D(FEST["RF-10|Anlaufverlust, Vortrag im Vorhaben (Voreinstellung MA-016): Endwert"])))
    plan, alt, kz = s1()
    zz = plan.zeilen
    for t in range(1, 4):
        verm = zz[t]["guthaben"] + D(1000000) + D(150000) * t / 5 - zz[t]["restschuld"]
        print(f"  R-10.12 Jahr {t}: Vermoegen {de(verm)} | Alternative {de(alt.bestand(t))}")

    titel("R-5 Darlehen: Einzelwerte")
    tr = Tranche("D", 600000, "raten", "0.03", laufzeit=20)
    zl = lauf(tr, 3, 1)
    print("  Ratentilgung: Zins", [de(x["zins"]) for x in zl[1:]], "Tilgung", de(zl[1]["tilgung"]))
    kw = dict(mindestdeckung=D("1.2"), zins_kalk=D("0.04"), tilgung_kalk=D("0.02"), p=1)
    fd = D(5400000)
    kd_fd = fd / 42 + fd * D("0.005")
    nb = dict(mittelbedarf=D(10000000), uebrige_darlehen=fd, kd_uebrige=kd_fd, zuschuesse=D(1800000), ek_min=D(1800000), **kw)
    ue = dict(mittelbedarf=D(2200000), uebrige_darlehen=D(1000000), kd_uebrige=D(25000), **kw)
    for name, b_ in (
            ("Ankauf 2,6 Mio.", bankdarlehen(D(2600000), D("0.65"), D(107712), mittelbedarf=D(2600000) * D("1.07"), **kw)),
            ("Ankauf 2,2 Mio.", bankdarlehen(D(2200000), D("0.65"), D(107712), mittelbedarf=D(2200000) * D("1.07"), **kw)),
            ("Ankauf uebernommen, Rang vor der Bank", bankdarlehen(D(2000000), D("0.65"), D(140000), **ue)),
            ("Ankauf uebernommen, Rang nach der Bank", bankdarlehen(D(2000000), D("0.65"), D(140000), uebrige_im_beleihungsraum=NULL, **ue)),
            ("Neubau 65 %", bankdarlehen(D(10000000), D("0.65"), D(400000), **nb)),
            ("Neubau 60 %", bankdarlehen(D(10000000), D("0.60"), D(400000), **nb)),
            ("Neubau Reinertrag 200.000", bankdarlehen(D(10000000), D("0.65"), D(200000), **nb)),
            ("Neubau Reinertrag 180.000", bankdarlehen(D(10000000), D("0.65"), D(180000), **nb)),
            ("Neubau 60 %, Foerderdarlehen im Nachrang, Reinertrag 180.000", bankdarlehen(D(10000000), D("0.60"), D(180000), uebrige_im_beleihungsraum=NULL, **nb))):
        print(f"  {name}: A {de(b_['a'], 0)} | B {de(b_['b'])} | C {de(b_['c'], 0)} | Darlehen {de(b_['darlehen'])} "
              f"| bindet {b_['bindend']} | Eigenkapital {de(b_['eigenkapital'])}")
    print("  Monatsraster, geschlossene Form:", de(D("107712.37") / D("1.2") / D("0.06")))

    titel("Kapitel 6 bis 11: Ankauf Basisfall (RF-11)")
    e = rechne_grob(A.ANKAUF, VG, KAT)
    z = e.plan.zeilen
    er = e.ertrag
    print("  Vergleichsmiete Jahr 4:", q4(er.vm(37)), "| Anpassungsziel Jahr 4:", q4(D("8.50") + (er.vm(37) - D("8.50")) * 3 / 4),
          "| Kappungsgrenze 8,50 x 1,15:", q4(D("8.50") * D("1.15")), "| Vergleichsmiete Jahr 5, 7, 12:", q4(er.vm(49)), q4(er.vm(73)), q4(er.vm(133)))
    print("  Monat 1: Sollmiete", de(er.soll(1)), "Einzahlung", de(z[1]["miete"]), "Kosten", de(z[1]["kosten"]),
          "| Jahr 1: Verwaltung, Instandhaltung, Betriebskosten", de(D(350 * 20 + 14 * 1320 + 2 * 1320), 0), "CO2", de(D(30) * 1320 * D("0.4") * 50 / 1000, 0))
    jv = verdichte(e.plan)
    for jj in jv[1:4] + jv[10:13]:
        print("  Jahr", jj["jahr"], {k: de(jj[k]) for k in ("miete", "kosten", "erhaltung", "zins", "tilgung", "steuer", "afa", "nachschuss", "guthaben", "restschuld")})
    print("  Rate Monat 1:", de(z[1]["zins"] + z[1]["tilgung"]), "(Zins", de(z[1]["zins"]), ") Rate Monat 121:", de(z[121]["zins"] + z[121]["tilgung"]),
          "| Nachschuss Monat 24:", de(z[24]["nachschuss"]))
    v = e.verkauf
    print("  Verkauf: Sollmiete Monat 144", de(er.soll_monat(144)), "Jahresmiete", de(er.jahresmiete(144)), "Preis", de(v.preis_brutto),
          "Kosten", de(v.kosten), "Erloes", de(v.erloes), "Buchwert", de(v.buchwert), "Gewinn", de(z[144]["g_v"]), "Steuer Jahr 12", de(z[144]["steuer"]))
    p12 = e.plan.steuer.protokoll[-1]
    print("  Steuer Jahr 12: Koerperschaftsteuer", de(p12["koerperschaftsteuer"]), "Gewerbesteuer", de(p12["gewerbesteuer"]),
          "| Verlustvortrag Ende Jahr 2:", de(e.plan.steuer.protokoll[1]["vv"]), de(e.plan.steuer.protokoll[1]["vv_gew"]))
    k = e.kennzahlen
    print("  Zaehler", de(k["zaehler"]), "Nenner", de(k["nenner"]), "w0", de(k["w"][0], 6), "w24", de(k["w"][24], 6),
          "| Jahresmiete Einstieg", de(e.jahresmiete_einstieg), "Bruttoanfangsrendite", proz(e.bruttoanfangsrendite, 2),
          "| Restwertbeitrag", de(e.restwertbeitrag), "| a0", de(e.a0), "| Kapitaldienst Jahr 1", de(e.kd_vj))
    print("  Mittelherkunft", {a: de(b) for a, b in e.herkunft.items()}, "Verwendung", {a: de(b) for a, b in e.verwendung.items()})
    tp = tragbarer_preis(A.ANKAUF, VG, KAT)
    print("  tragbarer Preis", tp["preis"], "Suchbereich", tp["unten"], tp["oben"], "| Rendite dort", proz(tp["ergebnis"].kennzahlen["rendite"], 6),
          "| einen Euro darueber", proz(rechne_grob(A.ANKAUF, VG, KAT, preis=tp["preis"] + 1, mit_blatt=False).kennzahlen["rendite"], 6))
    eg = rechne_grob(GEBUNDEN, VG, KAT)
    print("  gebunden: gebundene Miete Monat 1, 37, 72:", [q4(eg.ertrag.pools[-1].miete[m]) for m in (1, 37, 72)],
          "| Monatsrate uebernommenes Darlehen", de(eg.plan.zeilen[1]["tranchen"]["Uebernommenes Darlehen"]["zins"] + eg.plan.zeilen[1]["tranchen"]["Uebernommenes Darlehen"]["tilgung"]),
          "| nachhaltiger Reinertrag", de(eg.bemessung.ertrag_nachhaltig), "| Mieterhoehungen der gebundenen Flaeche nach Bindungsende:",
          [(m, q4(eg.ertrag.pools[-1].miete[m])) for m in range(73, 157) if eg.ertrag.pools[-1].miete[m] != eg.ertrag.pools[-1].miete[m - 1]])

    titel("Kapitel 5, 6, 11: Neubau (RF-12)")
    n = rechne_grob(A.NEUBAU, VG, KATN)
    zn = n.plan.zeilen
    for u in (0, 1, 2, 8, 9, 10, 18, 19, 21, 22):
        print(f"  Monat {u}: Investition {de(zn[u]['investition'])} | Einlage {de(zn[u]['einlage'])} | Nachschuss {de(zn[u]['nachschuss'])} "
              f"| Auszahlung {de(zn[u]['auszahlung'])} | Zins {de(zn[u]['zins'])} | Bereitstellung {de(zn[u]['bereit'])} | Tilgung {de(zn[u]['tilgung'])} | Miete {de(zn[u]['miete'])} | Kosten {de(zn[u]['kosten'])}")
    print("  Herkunft", {a: de(b) for a, b in n.herkunft.items()})
    print("  Verwendung", {a: de(b) for a, b in n.verwendung.items()})
    print("  Eigenkapital als Ausgleichsposten", de(n.ek_soll), "| Rohertrag", de(sum(n.ertrag.nachhaltig(u) for u in range(22, 34))),
          "| Bewirtschaftung und Ausfall im Vorhaben", de(sum(n.ertrag.bewirtschaftung(u) for u in range(22, 34)) + sum(n.ertrag.soll(u) - n.ertrag.einzahlung(u) for u in range(22, 34))),
          "| Sollmiete Monat 22", de(n.ertrag.soll(22)), "| a0", de(n.a0), "Gesamtkapitalrendite", proz(n.gesamtkapitalrendite))
    ns = rechne_grob(A.NEUBAU, VG, KATN, stress=True)
    print("  Stressfall: Eigenkapital", de(ns.eigenkapital_investitionsphase), "Rendite", proz(ns.kennzahlen["rendite"]), "erster Monat mit Miete",
          min(u for u in range(1, 60) if ns.plan.zeilen[u]["miete"] > 0))
    kf = rechne_grob(MIT_KFW, VG, KATN)
    zk = kf.plan.zeilen
    print("  KfW: Auszahlungen", {m: de(x) for m, x in kf.plan.e.tranchen[1].auszahlung.items() if m in (9, 10, 15, 16, 17)},
          "| Bank erste Auszahlung", min(kf.plan.e.tranchen[0].auszahlung), "| Zins Monat 19", de(zk[19]["tranchen"]["KfW-Darlehen"]["zins"]),
          "| Rate Monat 31", de(zk[31]["tranchen"]["KfW-Darlehen"]["zins"] + zk[31]["tranchen"]["KfW-Darlehen"]["tilgung"]))
    f = rechne_grob(GEFOERDERT, VG, KATN)
    zf = f.plan.zeilen
    bm = f.bemessung
    print("  gefoerdert: zuwendungsfaehige Kosten", de(bm.zuschuss / D("0.2")), "| Mittelbedarf", de(bm.mittelbedarf), "| Eigenkapital als Ausgleichsposten", de(f.ek_soll),
          "| Rohertrag", de(sum(f.ertrag.nachhaltig(u) for u in range(22, 34))), "| Reinertrag VJ", de(bm.reinertrag_vj),
          "| Steuer Jahr 1, 2", de(f.plan.jahressumme("steuer", 1)), de(f.plan.jahressumme("steuer", 2)),
          "| Zuschuss Zufluss Jahr 1, 2", de(f.plan.jahressumme("zuschuss", 1)), de(f.plan.jahressumme("zuschuss", 2)))
    for u in (0, 1, 2, 3, 4, 18, 19):
        t = zf[u]["tranchen"]["Foerderdarlehen"]
        print(f"  Monat {u}: Investition {de(zf[u]['investition'])} | Einlage {de(zf[u]['einlage'])} | Nachschuss {de(zf[u]['nachschuss'])} | Zuschuss {de(zf[u]['zuschuss'])} "
              f"| Einbehalt Z {de(zf[u]['zuschuss_einbehalt'])} | FD Auszahlung {de(t['auszahlung'])} Einbehalt {de(t['einbehalt'])} Beitrag {de(t['beitrag'])} Tilgung {de(t['tilgung'])}")
    f20 = rechne_grob(replace(GEFOERDERT, haltedauer=20), VG, KATN)
    print("  20 Jahre: verbleibender Zuschuss", de(f20.bemessung.zuschuss - f20.verkauf.foerder_rueckzahlung), "| Anteil 198/420")

    titel("Abgeleitete Beispielzahlen (Rechenschritte der Beispiele, die kein Pruefwert sind)")
    pk, ak, kk_ = s1(ek=380000)
    print("  R-4.5 Kontokorrent t0..t2 bei 380.000 Eigenkapital:", [de(x) for x in pk.reihe("kk")[:3]])
    print("  R-5.3 Rate 2 von 700.000 zu 4 %, Rate 3.500: Zins", de(rd.geld((D(700000) - D("1166.67")) * D("0.04") / 12)),
          "Tilgung", de(D(3500) - rd.geld((D(700000) - D("1166.67")) * D("0.04") / 12)))
    print("  R-5.4 IWU: Darlehen 20 % von 88.992:", de(D(88992) * D("0.2")))
    print("  R-5.11 uebernommenes Darlehen, Rate aus der Restschuld gerechnet:", de(12 * rd.geld(D(500000) * D("0.025") / 12)),
          "| aus dem Nennbetrag:", de(12 * rd.geld(D(600000) * D("0.025") / 12)))
    print("  R-5.12 Unterschied der Lesarten:", de(D("1431044.99") - D("1226609.99")), "| Knick:", de(D("1226609.99") / D("0.65"), 0))
    print("  R-6.3 Abstand zur Vergleichsmiete im Jahr 4:", q4(er.vm(37) - D("8.50")))
    print("  R-6.8 Bewirtschaftung Jahr 1 / 12:", de(D(28120) / 12), "| R-6.9 CO2 je Monat:", de(D(792) / 12),
          "| Baujahr 1996, Monat 1 und 13:", [de(rechne_grob(replace(A.ANKAUF, baujahr=1996), VG, KAT).plan.zeilen[m]["kosten"]) for m in (1, 13)])
    print("  R-6.16 netto:", de(D("127308.00") / D("1.19")), de(D("339488.00") / D("1.19")), de(D("424360.00") / D("1.19")),
          "| Schwelle", de(D("0.15") * 1980000, 0), "| Abschreibung der aktivierten Massnahme:", de(D("48087.20") - D("39600.00")))
    print("  R-7.3 Abschreibung je Monat (Fehlerbild):", de(D(17600) / 12), "x 12 =", de(12 * rd.geld(D(17600) / 12)))
    print("  R-7.8 Gewerbesteuer 14 % auf 10.000 und auf 510.000:", de(D("0.14") * 10000), de(D("0.14") * 510000),
          "| Unterschied der Steuer auf den Verkaufsgewinn (MA-030):", de(D("245386.69") - D("105456.69")))
    print("  R-7.9 Anrechnung bei 50 %:", de(D(10570) / 2), "| R-7.10:", de(D("0.42") * 30000), de(D("0.26375") * 1000),
          "| R-7.14 s_FK:", proz(D("0.29825") - D("0.25") * D("0.14")))
    print("  R-10.22:", de(D("28911.96") + D("73596.60")), "| Jahressollmiete", de(D(1320) * D("8.50") * 12),
          "| R-10.17 Eigenkapitalbedarf insgesamt:", de(e.eigenkapitalbedarf))
    print("  R-11.2 Fortschreibung der Baukosten:", de(n.bemessung.baukosten - n.bemessung.baukosten_stichtag),
          proz((n.bemessung.baukosten - n.bemessung.baukosten_stichtag) / n.bemessung.baukosten_stichtag, 2),
          "| Jahresmiete Einstieg Neubau", de(n.jahresmiete_einstieg))
    print("  R-11.5 Steigung am Knick in Basispunkten je 10.000 Euro:", de((D("8.3164") - D("8.2453")) * 100), de((D("8.2453") - D("8.1492")) * 100))
    te = tragbarer_preis(replace(A.ANKAUF, verfuegbares_ek=D(1200000)), VG, KAT)
    ee = te["ergebnis"]
    print("  R-11.6 Eigenkapitalgrenze: Preis", te["preis"], "Stichtag", de(ee.eigenkapital_investitionsphase), "Nachschuss",
          de(ee.eigenkapitalbedarf - ee.eigenkapital_investitionsphase), "zusammen", de(ee.eigenkapitalbedarf))
    et = tp["ergebnis"]
    ts = tragbarer_preis(A.ANKAUF, VG, KAT, stress=True)
    print("  R-11.7 beim tragbaren Preis: Eigenkapital", de(et.eigenkapital_investitionsphase), "insgesamt", de(et.eigenkapitalbedarf),
          "Faktor", de(tp["faktor"], 2), "je m2", de(tp["preis_je_qm"]), "| Stressfall: Faktor", de(ts["faktor"], 2), "je m2", de(ts["preis_je_qm"]))
    print("  R-11.14 zuwendungsfaehige Kosten:", de(bm.baukosten + D(2500) * D(400)))
    print("  R-12.3 beim tragbaren Preis: Nebenkosten", de(et.bemessung.enk), "Boden ungerundet", de((et.bemessung.preis + et.bemessung.enk) * D("0.25"), 3),
          "Boden", de(et.bemessung.boden), "Abschreibungsgrundlage", de(et.bemessung.preis + et.bemessung.enk - et.bemessung.boden))
    print("  R-13.3 P-03 Testfall Jahr 1:", de(D("-675820.00") + D(700000)), "| P-07:", de(D("1743830.47") - D("822091.51")),
          "| P-04 Neubau:", de(D("5141964.13") + D("4007142.85")), "=", de(D("9015152.34") + D("133954.64")))
    print("  Kapitel 17 KfW-Vorteil:", 924244 - 702767, "| mit Vertragskonditionen:", 1286380 - 876926)
    fs = rechne_grob(GEFOERDERT, replace(VG, ma032_entgelte_sofort=True), KATN)
    print("  R-7.15 Entgelte verteilt: Rendite", proz(f.kennzahlen["rendite"], 3), "Endwertdifferenz", de(f.kennzahlen["endwertdifferenz"]),
          "| im Jahr der Zahlung (andere Lesart MA-032): Rendite", proz(fs.kennzahlen["rendite"], 3), "Endwertdifferenz", de(fs.kennzahlen["endwertdifferenz"]))
    zr = [x for x in lauf(Tranche("D", 100000, "raten", "0.03", laufzeit=7), 7, 12)]
    print("  R-5.5 sieben Monatsraten auf 100.000:", [de(x["tilgung"]) for x in zr[1:]])
    tr10 = Tranche("D", 1496000, "annuitaet_prozent", "0.04", tilgungssatz="0.02", rundung="keine")
    lauf(tr10, 10, 1, Rundung("keine"))
    print("  R-5.9 Restschuld nach zehn Jahren (1.496.000, 4 % und 2 %, ohne Rundung):", de(tr10.rest))
    titel("R-8.2 Nettoanfangsrendite als Massstab (Beispiel des Berichts D.4), R-8.4")
    print("  Faktor 22,2 x 100.000:", de(restwert.preis_aus_faktor(D("22.2"), D(100000), rd)))
    print("  80.000 / 4,5 %:", de(D(80000) / D("0.045")), "| ohne 7 % Erwerbsnebenkosten:",
          de(restwert.preis_aus_nettoanfangsrendite(D("0.045"), D(80000), D("0.07"), rd)))
    print("  Stau 100.000, Verkauf Jahr 10, 3 %:", de(D(100000) * D("1.03") ** 10), "| Planjahr 12:", de(D(100000) * D("1.03") ** 12),
          "| 40 % in Jahr 9:", de(D(40000) * D("1.03") ** 9), "| 60 % am Stichtag:", de(D(60000) * D("1.03") ** 10))
