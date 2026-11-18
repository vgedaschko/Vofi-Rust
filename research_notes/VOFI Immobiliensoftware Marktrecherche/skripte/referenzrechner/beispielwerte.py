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
from kennzahlen import vergleichsfaktoren, zaehler_nenner, schuldendienstdeckung
from grobkalkulation import rechne_grob, tragbarer_preis
import annahmen as A
from rf_rahmen import jahresplan, lehrbuch_steuer
from rf_testfall import s1, s1_monat
from rf_lehrbuch import _schulte_standard
import restwert


def titel(t):
    print("\n== " + t)


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

    titel("R-2.3 Verdichtung, Testfall im Monatsraster, Jahr 1")
    pm, am, km = s1_monat(D("0.02"), D("0.08"), "cent")
    j = verdichte(pm)
    for jj in j[:3]:
        print("  Jahr", jj["jahr"], {k: de(jj[k]) for k in ("miete", "zins", "tilgung", "habenzins", "steuer", "guthaben", "restschuld")})
    print("  Monat 1:", {k: de(pm.zeilen[1][k]) for k in ("miete", "zins", "tilgung", "habenzins", "guthaben", "restschuld")})
    print("  Monat 2:", {k: de(pm.zeilen[2][k]) for k in ("miete", "zins", "tilgung", "habenzins", "guthaben", "restschuld")})
    print("  Endwert", de(pm.endwert), "Rendite", proz(km["rendite"]), "Differenz", de(km["endwertdifferenz"]))

    titel("R-4.7 Lehrbuchansicht, Schulte Standardbeispiel mit Steuern (Tab. 5)")
    p5, a5, k5, tr = _schulte_standard(lehrbuch_steuer("0.5"), 250)
    for z in lehrbuchansicht(p5):
        print("  t%d " % z["t"] + " | ".join(f"{k} {de(v, 0)}" for k, v in z.items() if k != "t"))
    titel("R-9 Unterlassensalternative, Schulte Standardbeispiel mit Steuern (Tab. 6)")
    for z in a5.zeilen:
        print(f"  t{z['u']}: Zins lang {de(z['zins_lang'], 0)} | Zins kurz {de(z['zins_kurz'], 0)} | Steuer {de(z['steuer'], 0)} | lang {de(z['lang'], 0)} | kurz {de(z['kurz'], 0)}")

    titel("R-10.4/R-10.5 Vergleichsfaktoren, Zaehler und Nenner im Testfall mit Nachschuss")
    pn, an, kn = s1(einlagen={2: 50000})
    print("  w:", [str(x) for x in kn["w"]])
    print("  Zaehler", de(kn["zaehler"]), "Nenner", de(kn["nenner"]), "Zaehler Alternative", de(kn["zaehler_alternative"]),
          "Rendite", proz(kn["rendite"]), "Vergleichsrendite", proz(kn["vergleichsrendite"]))
    pe, ae, ke = s1(entnahmen={t: 5000 for t in range(1, 6)})
    print("  Entnahmen: Zaehler", de(ke["zaehler"]), "Nenner", de(ke["nenner"]), "aufgezinste Entnahmen", de(ke["zaehler"] - pe.endwert))

    titel("R-6 Ankauf Basisfall: Mietpfad, Kosten, Stau")
    e = rechne_grob(A.ANKAUF, A.VORGABEN)
    print("  Miete je qm Jahre 1..13:", [de(x, 4) for x in e.miete_je_qm[1:14]])
    z = e.plan.zeilen
    print("  Monat 1: Sollmiete", de(D(1320) * D("8.50")), "Einzahlung", de(z[1]["miete"]), "Kosten", de(z[1]["kosten"]))
    print("  Monat 13: Einzahlung", de(z[13]["miete"]), "Kosten", de(z[13]["kosten"]))
    jv = verdichte(e.plan)
    for jj in jv:
        print("  Jahr", jj["jahr"], {k: de(jj[k]) for k in ("miete", "kosten", "erhaltung", "zins", "tilgung", "steuer", "afa", "nachschuss", "guthaben", "restschuld")})
    print("  Rate Monat 1:", de(z[1]["zins"] + z[1]["tilgung"]), "Rate Monat 121:", de(z[121]["zins"] + z[121]["tilgung"]),
          "Restschuld Monat 120:", de(z[120]["restschuld"]), "Abloesung:", de(z[144]["abloesung"]))
    print("  Verkauf: Preis", de(e.verkauf.preis_brutto), "Kosten", de(e.verkauf.kosten), "Erloes", de(e.verkauf.erloes),
          "Buchwert", de(e.verkauf.buchwert), "Gewinn", de(z[144]["g_v"]), "Steuer Jahr 12", de(z[144]["steuer"]))
    print("  Sollmiete Folgejahr:", de(e.verkauf.preis_brutto / 18))
    print("  Steuerprotokoll Jahr 1, 2, 12:", [(p["jahr"], str(p["e_op"]), str(p["z_h"]), str(p["g_v"]), str(p["koerperschaftsteuer"]), str(p["gewerbesteuer"]), str(p["vv"]), str(p["vv_gew"])) for p in e.plan.steuer.protokoll if p["jahr"] in (1, 2, 3, 12)])
    print("  Restwertbeitrag", de(e.restwertbeitrag), "Mittelherkunft", {k: de(v) for k, v in e.herkunft.items()}, "Verwendung", {k: de(v) for k, v in e.verwendung.items()})
    k = e.kennzahlen
    print("  Zaehler", de(k["zaehler"]), "Nenner", de(k["nenner"]), "w0", str(k["w"][0])[:16], "w24", str(k["w"][24])[:16])
    print("  DSCR je Jahr:", [de(schuldendienstdeckung(e.plan, j)[0], 3) for j in range(1, 13)])
    es = rechne_grob(A.ANKAUF, A.VORGABEN, stress=True)
    print("  Stress DSCR je Jahr:", [de(schuldendienstdeckung(es.plan, j)[0], 3) for j in range(1, 13)])

    titel("R-8.2 Nettoanfangsrendite als Massstab (Beispiel des Berichts D.4)")
    print("  Faktor 22,2 x 100.000:", de(restwert.preis_aus_faktor(D("22.2"), D(100000), rd)))
    print("  80.000 / 4,5 %:", de(D(80000) / D("0.045")), "| ohne 7 % Erwerbsnebenkosten:",
          de(restwert.preis_aus_nettoanfangsrendite(D("0.045"), D(80000), D("0.07"), rd)))
    print("  Stau 100.000, Verkauf Jahr 10, 3 %:", de(D(100000) * D("1.03") ** 10), "| Planjahr 12:", de(D(100000) * D("1.03") ** 12),
          "| 40 % in Jahr 9:", de(D(40000) * D("1.03") ** 9), "| 60 % am Stichtag:", de(D(60000) * D("1.03") ** 10))

    titel("R-11 Neubau frei finanziert: Mittelabruf")
    n = rechne_grob(A.NEUBAU, A.VORGABEN_NEUBAU)
    zn = n.plan.zeilen
    for u in (0, 1, 6, 7, 8, 18, 19, 20):
        print(f"  Monat {u}: Investition {de(zn[u]['investition'])} | Einlage {de(zn[u]['einlage'])} | Nachschuss {de(zn[u]['nachschuss'])} "
              f"| Auszahlung {de(zn[u]['auszahlung'])} | Zins {de(zn[u]['zins'])} | Tilgung {de(zn[u]['tilgung'])} | Miete {de(zn[u]['miete'])} | Restschuld {de(zn[u]['restschuld'])}")
    print("  Herkunft", {k: de(v) for k, v in n.herkunft.items()}, "Verwendung", {k: de(v) for k, v in n.verwendung.items()})
    print("  Reinertrag VJ", de(n.bemessung.reinertrag_vj), "a", de(n.bemessung.bank["a"]), "b", de(n.bemessung.bank["b"]), "c", de(n.bemessung.bank["c"]))
    f = rechne_grob(replace(A.NEUBAU, foerderung=A.FOERDERUNG_B, haltedauer=20), A.VORGABEN_NEUBAU)
    zf = f.plan.zeilen
    bm = f.bemessung
    print("  gefoerdert: a", de(bm.bank["a"]), "b", de(bm.bank["b"]), "c", de(bm.bank["c"]), "Reinertrag VJ", de(bm.reinertrag_vj), "Mittelbedarf", de(bm.mittelbedarf))
    for u in (0, 1, 2, 5, 6, 18, 19):
        t = zf[u]["tranchen"]["Foerderdarlehen"]
        print(f"  Monat {u}: Investition {de(zf[u]['investition'])} | Einlage {de(zf[u]['einlage'])} | Nachschuss {de(zf[u]['nachschuss'])} | Zuschuss {de(zf[u]['zuschuss'])} "
              f"| Einbehalt Z {de(zf[u]['zuschuss_einbehalt'])} | FD Auszahlung {de(t['auszahlung'])} Einbehalt {de(t['einbehalt'])} Beitrag {de(t['beitrag'])} Tilgung {de(t['tilgung'])} Rest {de(t['rest'])}")
    print("  Herkunft", {k: de(v) for k, v in f.herkunft.items()}, "Verwendung", {k: de(v) for k, v in f.verwendung.items()})

    titel("R-7.6, R-7.8, R-10.6, R-10.9, R-10.12: weitere Einzelwerte")
    from rf_rahmen import FEST
    print("  sofortige Verrechnung minus Vortrag (RF-10):",
          de(D(FEST["RF-10|Anlaufverlust, sofortige Verrechnung (andere Lesart): Endwert"])
             - D(FEST["RF-10|Anlaufverlust, Vortrag im Vorhaben (Voreinstellung MA-016): Endwert"])))
    p12 = [p for p in e.plan.steuer.protokoll if p["jahr"] == 12][0]
    laufend = ((p12["e_op"] + p12["z_h"]) / 100).to_integral_value(rounding="ROUND_FLOOR") * 100 * D("0.14")
    print("  Gewerbesteuer Jahr 12:", de(p12["gewerbesteuer"]), "| ohne Verkaufsgewinn:", de(laufend),
          "| auf den Verkaufsgewinn:", de(p12["gewerbesteuer"] - laufend))
    tp = tragbarer_preis(A.ANKAUF, A.VORGABEN)
    print("  Endwertueberschuss beim tragbaren Preis", tp["preis"], ":", de(tp["ergebnis"].kennzahlen["endwertueberschuss"]),
          "| Knick b/beta:", de(e.bemessung.bank["b"] / A.VORGABEN.beleihungsquote))
    # Amortisationsdauer: Vermoegen bei gedachtem Verkauf (Wertpfad linear 1,00 -> 1,15 Mio.) gegen Alternative
    plan, alt, kz = s1()
    zz = plan.zeilen
    for t in range(1, 6):
        verm = zz[t]["guthaben"] + D(1000000) + D(150000) * t / 5 - (zz[t]["restschuld"] if t < 5 else zz[5]["abloesung"])
        print(f"  Jahr {t}: Vermoegen {de(verm if t < 5 else plan.endwert)} | Alternative {de(alt.bestand(t))}")
    # Entnahme aus Guthaben bei laufendem Verlustvortrag (Grenze der Eigenschaft 3)
    re = [D(30000)] + [D(55000) * D("1.02") ** t for t in range(1, 5)]
    st = lehrbuch_steuer("0.30", "vortrag", False)
    pa, aa, ka = s1(ek=420000, reinertrag=re, steuer=st)
    pb, ab, kb = s1(ek=420000, reinertrag=re, steuer=lehrbuch_steuer("0.30", "vortrag", False), entnahmen={1: 5000})
    print("  Verlustvortrag, ohne Entnahme: Rendite", proz(ka["rendite"], 4), "| mit Entnahme 5.000 in t1:", proz(kb["rendite"], 4),
          "| Endwertdifferenz", de(ka["endwertdifferenz"]), "/", de(kb["endwertdifferenz"]))

    titel("R-4.3 Testfall: Bemessung je Jahr (e_op + Habenzins), ungerundete Werte, Deckung")
    from kennzahlen import sollzinsen_nach_steuern
    pc, ac, kc = s1(rundung="cent")
    print("  Bemessung t1..t5:", [de(z["e_op"] + z["habenzins"]) for z in pc.zeilen[1:]])
    print("  Probe P-03 Jahr 1:", de(pc.zeilen[1]["bestandssaldo"] - pc.zeilen[0]["bestandssaldo"]))
    pu, au, ku = s1()
    print("  ungerundet: Endwert", de(pu.endwert, 4), "Guthaben t4", de(pu.zeilen[4]["guthaben"]),
          "Sollzinsen nach Steuern", de(sollzinsen_nach_steuern(pu)))
    print("  Deckung t1..t5:", [de(schuldendienstdeckung(pu, j)[0], 4) for j in range(1, 6)])
    print("  w(0), w(2) gerundet:", de(ku["w"][0], 6), de(ku["w"][2], 6), "| Ankauf w(0), w(24):",
          de(e.kennzahlen["w"][0], 6), de(e.kennzahlen["w"][24], 6))
    pk, ak, kk_ = s1(ek=380000)
    print("  Kontokorrent t0..t3 bei 380.000 Eigenkapital:", [de(z["kk"]) for z in pk.zeilen[:4]])
    print("  Verlustvortrag-Fall: Aenderung der Endwertdifferenz durch die Entnahme:",
          de(ka["endwertdifferenz"] - kb["endwertdifferenz"]))

    titel("R-5 Darlehen: Einzelwerte")
    from darlehen import Tranche, bankdarlehen
    from rf_bausteine import lauf
    tr = Tranche("D", 600000, "raten", "0.03", laufzeit=20)
    zl = lauf(tr, 3, 1)
    print("  Ratentilgung: Zins", [de(x["zins"]) for x in zl[1:]], "Tilgung", de(zl[1]["tilgung"]))
    tr = Tranche("D", 100000, "raten", "0.03", laufzeit=7)
    zl = lauf(tr, 7, 12)
    print("  sieben Monatsraten:", de(zl[1]["tilgung"]), de(zl[7]["tilgung"]))
    pf, af, kf = jahresplan(n=10, a0=43738, ueberschuss=3606, ek=21869, h="0.05", kk="0.11", steuer=lehrbuch_steuer("0.5"),
                            verkauf=43738, afa=600, a_lang="0.07",
                            tranchen=[Tranche("Kredit", 21869, "frei", "0.10", rundung="keine")])
    print("  freie Tilgung: Tilgung t1..t3", [de(x, 0) for x in pf.reihe("tilgung")[1:4]],
          "Kreditstand t1..t3", [de(x, 0) for x in pf.reihe("restschuld")[1:4]])
    print("  Neubau Monat 19: Rate", de(zn[19]["zins"] + zn[19]["tilgung"]))
    print("  IWU: Fremdkapital", de(D(88992) * D("0.2")), "Eigenkapital", de(D(88992) * D("0.8")))
    kw = dict(mindestdeckung=D("1.2"), zins=D("0.04"), tilgungssatz=D("0.02"), p=1)
    fd = D(5400000)
    kd_fd = fd / 42 + fd * D("0.005")
    nb = dict(mittelbedarf=D(10000000), uebrige_darlehen=fd, kd_uebrige=kd_fd, zuschuesse=D(1800000), ek_min=D(1800000), **kw)
    for name, b_ in (
            ("Ankauf 2,6 Mio.", bankdarlehen(D(2600000), D("0.65"), D(107712), mittelbedarf=D(2600000) * D("1.07"), **kw)),
            ("Ankauf 2,2 Mio.", bankdarlehen(D(2200000), D("0.65"), D(107712), mittelbedarf=D(2200000) * D("1.07"), **kw)),
            ("Ankauf uebernommen", bankdarlehen(D(2000000), D("0.65"), D(140000), mittelbedarf=D(2200000),
                                                uebrige_darlehen=D(1000000), kd_uebrige=D(25000), **kw)),
            ("... andere Lesart", bankdarlehen(D(2000000), D("0.65"), D(140000), mittelbedarf=D(2200000),
                                               uebrige_darlehen=D(1000000), kd_uebrige=D(25000), nur_eigenes=True, **kw)),
            ("Neubau 65 %", bankdarlehen(D(10000000), D("0.65"), D(400000), **nb)),
            ("Neubau 60 %", bankdarlehen(D(10000000), D("0.60"), D(400000), **nb)),
            ("Neubau Reinertrag 200.000", bankdarlehen(D(10000000), D("0.65"), D(200000), **nb)),
            ("Neubau Reinertrag 180.000", bankdarlehen(D(10000000), D("0.65"), D(180000), **nb))):
        print(f"  {name}: A {de(b_['a'], 0)} | B {de(b_['b'])} | C {de(b_['c'], 0)} | Darlehen {de(b_['darlehen'])} "
              f"| bindet {b_['bindend']} | Eigenkapital {de(b_['eigenkapital'])}")
    print("  Monatsraster, geschlossene Form:", de(D("107712.37") / D("1.2") / D("0.06")))

    titel("R-6, R-7, R-8, R-10, R-11, R-13: Einzelwerte Ankauf und Foerderung")
    markt2 = D("9.20") * D("1.02")
    print("  Marktmiete Jahr 2:", de(markt2, 3), "| Abstand zur Ist-Miete:", de(markt2 - D("8.50"), 3),
          "| gebundene Miete nach dem ersten Schritt:", de(D("6.80") * D("1.0615"), 4))
    jahr1 = 350 * 20 + 14 * 1320 + 2 * 1320
    print("  Bewirtschaftung Jahr 1:", de(D(jahr1), 0), "| im Monat:", de(D(jahr1) / 12), "| Baupreisindex Jahr 2:", de(D("1.03") ** 2, 4))
    print("  Abschreibungsgrundlage:", de(D(2640000) * D("0.75"), 0), "| Boden:", de(D(2640000) * D("0.25"), 0),
          "| Summe der Abschreibungen:", de(sum(z["afa"] for z in e.plan.zeilen), 0), "| A:", de(e.bemessung.bank["a"], 0))
    print("  Sollmiete im Monat des Folgejahres:", de(e.verkauf.preis_brutto / 18 / 12),
          "| Jahressollmiete Jahr 1:", de(e.sollmiete_vj, 0), "| Bruttoanfangsrendite:", proz(e.bruttoanfangsrendite, 2))
    from steuer import Steuer, GEWERBLICHE_PG, PRIVAT
    from zeit import Raster
    r1 = Raster(1, 12, startjahr=2027)
    st = Steuer(A.steuer(GEWERBLICHE_PG, anteil_natuerliche=D("0.5")), r1, rd)
    st.jahr(1, D(100000), D(0))
    pr = st.protokoll[-1]
    print("  Personengesellschaft: Gewerbeertrag nach Freibetrag", de(D(100000) - A.FREIBETRAG, 0), "| Anrechnung bei 50 %:", de(pr["anrechnung"]))
    st = Steuer(A.steuer(PRIVAT, haltedauer=10), r1, rd)
    st.jahr(1, D(30000), D(1000))
    pr = st.protokoll[-1]
    print("  Privat: Vermietung", de(pr["vermietung"]), "| Zinsen", de(pr["kapital"]))
    zk = min(f.bemessung.baukosten, A.FOERDERUNG_B.bemessungsgrenze_je_qm * 2000) + min(D(1296000), D(400) * 2500)
    print("  zuwendungsfaehige Kosten:", de(zk, 0), "| verbleibender Zuschuss nach Rueckzahlung:",
          de(f.bemessung.zuschuss - f.verkauf.foerder_rueckzahlung))
