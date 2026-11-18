"""Referenzfaelle RF-01 bis RF-04: veroeffentlichte Rechenbeispiele im Jahresmodus (Kapitel 15).

RF-01 KIRCHNER-IWU-2004, RF-02 IWU-2013-ENDBERICHT (MA-015), RF-03/RF-04 SCHULTE-IMMOBILIENINVESTITION-2025.
Gerechnet wird ungerundet; verglichen wird mit den veroeffentlichten, gerundeten Werten.
"""
from decimal import Decimal as D
from zahlen import NULL, EINS, d, de, kaufm
from darlehen import Tranche
from finanzplan import lehrbuchansicht
from kennzahlen import interner_zinsfuss, kapitalwert
from rf_rahmen import (fall, pruefe, pruefe_proz, pruefe_reihe, pruefe_proben, pruefe_gleich, info, jahresplan,
                       lehrbuch_steuer)


def rf01_kirchner():
    k = fall("RF-01", "Kirchner (KIRCHNER-IWU-2004), drei Perioden, Sollzins 7,5 %, Habenzins 5,0 %")
    for name, reihe, ek, ew, rendite in (("Projekt A", (400, 0, 1000), 1000, "1322.48", "9.76"),
                                         ("Projekt B", (600, 450, 0), 1000, "1249.76", "7.71"),
                                         ("Projekt A, Eigenkapital 900", (400, 0, 1000), 900, "1203.96", "10.19")):
        a0 = 1100 if "A" in name else 900
        plan, alt, kz = jahresplan(3, a0, reihe, ek, [], "0.05", "0.075")
        pruefe(k, f"{name}: Endwert", plan.endwert, ew)
        pruefe_proz(k, f"{name}: VOFI-Rendite", kz["rendite"], rendite, 2)
        pruefe_proben(k, plan, alt, f"{name}: Kontrollsummen")
    plan, alt, kz = jahresplan(3, 1100, (400, 0, 1000), 1000, [], "0.05", "0.075")
    pruefe_reihe(k, "Projekt A: Kontokorrent t0, Guthaben t1, t2", [plan.zeilen[0]["kk"], plan.zeilen[1]["guthaben"],
                 plan.zeilen[2]["guthaben"]], ["100", "292.50", "307.13"], "0.005")
    plan, alt, kz = jahresplan(3, 1100, (400, 0, 1000), 1000, [], "0.075", "0.075")
    pruefe(k, "Projekt A bei einheitlich 7,5 %: Endwert", plan.endwert, "1338.02")


def rf02_iwu2013():
    k = fall("RF-02", "IWU 2013 (IWU-2013-ENDBERICHT, Anhang C; Umlage nach MA-015), 25 Jahre, ohne Steuern")
    # Veroeffentlichte Reihen (volle Euro), Quellnotiz 08
    miete_buch = [6883, 6377, 5866, 5350, 4829, 4303, 3771, 3234, 2888, 2917, 2946, 2975, 3005, 3035, 3066, 3096,
                  3127, 3158, 3190, 3222, 3254, 3287, 3320, 3353, 3386]
    zins_buch = [712, 695, 677, 659, 639, 619, 599, 577, 554, 531, 507, 481, 455, 428, 399, 370, 339, 307, 274,
                 239, 203, 166, 126, 86, 44]
    tilg_buch = [427, 444, 462, 481, 500, 520, 541, 562, 585, 608, 633, 658, 684, 712, 740, 770, 800, 832, 866,
                 900, 936, 974, 1013, 1053, 1095]
    reinv_buch = [30886, 37051, 42889, 48387, 53529, 58298, 62679, 66654, 70403, 74292, 78327, 82513, 86855,
                  91356, 96023, 100861, 105874, 111070, 116453, 122029, 127805, 133786, 139980, 146393]
    a0, zuschuss = D(88992), D(25143)
    # Mietreihe aus den Annahmen des Berichts (MA-015: 11 % Umlage auf Kosten abzueglich Zuschuss)
    flaeche = D(782)
    dm = D("0.11") * (a0 - zuschuss) / 12 / flaeche
    miete = []
    for t in range(1, 26):
        idx = D("1.01") ** (t - 1)
        miete.append((max(D("5.50") + dm, D("5.79") * idx) - D("5.50") * idx) * flaeche * 12 * D("0.98"))
    pruefe_reihe(k, "zusaetzliche Mieteinnahmen t1..t25 aus den Annahmen", miete, miete_buch, "0.5")
    ek, fk = a0 * D("0.8"), a0 * D("0.2")
    for name, reihe in (("Mietreihe aus Annahmen", miete), ("veroeffentlichte Mietreihe", [D(x) for x in miete_buch])):
        tr = Tranche("Darlehen", fk, "annuitaet_laufzeit", "0.04", laufzeit=25, rundung="keine")
        zus = [NULL, zuschuss] + [NULL] * 24
        plan, alt, kz = jahresplan(25, a0, reihe, ek, [tr], "0.03", "0.06", zuschuss=zus)
        pruefe(k, f"Endwert ({name})", plan.endwert, "153032", "3.40")
        pruefe_proz(k, f"VOFI-Rendite ({name})", kz["rendite"], "3.11", 2)
        if reihe is miete:
            pruefe_reihe(k, "Zinsen Fremdkapital t1..t25", plan.reihe("zins")[1:], zins_buch, "1")
            pruefe_reihe(k, "Tilgung t1..t25", plan.reihe("tilgung")[1:], tilg_buch, "1")
            pruefe_reihe(k, "Reinvestition t1..t24 (Guthabenstand)", plan.reihe("guthaben")[1:25], reinv_buch, "3.40")
            pruefe_proben(k, plan, alt)
            abw = max(abs(a - D(b)) for a, b in zip(plan.reihe("guthaben")[1:25], reinv_buch))
            info(f"Endwert genau {de(plan.endwert)}; groesste Abweichung der Reinvestition {de(abw)}; "
                 f"Annuitaet {de(tr.rate)}")
        else:
            info(f"Endwert genau {de(plan.endwert)}")


def _schulte_standard(steuer, afa):
    tr = Tranche("Kredit", 2000, "annuitaet_laufzeit", "0.075", laufzeit=5, rundung="keine")
    return jahresplan(5, 10000, 540, 8000, [tr], "0.045", "0.09", steuer=steuer, verkauf=10000, afa=afa,
                      a_lang="0.05") + (tr,)


def rf03_schulte_standard():
    k = fall("RF-03", "Schulte, Standardbeispiel (SCHULTE-IMMOBILIENINVESTITION-2025, Tab. 3 bis 6)")
    # ---- klassische Verfahren und Steuerparadoxon (Plausibilitaetstest R-15.4)
    a0, ue, rn, n = D(10000), D(540), D(10000), 5
    kzf = (D("0.05") * 8000 + D("0.075") * 2000) / 10000
    reihe = [-a0] + [ue] * 4 + [ue + rn]
    pruefe(k, "Kalkulationszinsfuss (Mischzins, %)", kzf * 100, "5.5", "0.05", 1)
    pruefe(k, "Kapitalwert vor Steuern", kapitalwert(reihe, kzf), "-43", "0.5", 0)
    izf, _ = interner_zinsfuss(reihe)
    pruefe(k, "interner Zinsfuss vor Steuern (%)", izf[0] * 100, "5.4", "0.05", 1)
    s, afa = D("0.5"), D(250)
    ue_s, rn_s = ue - s * (ue - afa), rn - s * (rn - (a0 - afa * n))
    reihe_s = [-a0] + [ue_s] * 4 + [ue_s + rn_s]
    kw_s = kapitalwert(reihe_s, kzf * (1 - s))
    pruefe(k, "Kapitalwert nach Steuern (Steuerparadoxon)", kw_s, "8", "0.5", 0)
    pruefe_gleich(k, "Steuerparadoxon: Kapitalwert vor Steuern negativ, nach Steuern positiv",
                  kapitalwert(reihe, kzf) < 0 < kw_s, True)
    # ---- Tab. 3: Immobilie ohne Steuern
    plan, alt, kz, tr = _schulte_standard(lehrbuch_steuer(0), 0)
    pruefe(k, "Tab. 3: Annuitaet", tr.rate, "494", "0.5", 0)
    pruefe_reihe(k, "Tab. 3: Kredit nach Tilgung t1..t5", plan.reihe("restschuld")[1:], [1656, 1286, 888, 460, 0])
    pruefe_reihe(k, "Tab. 3: Reinvestition t1..t4", plan.reihe("guthaben")[1:5], [46, 93, 143, 195])
    pruefe_reihe(k, "Tab. 3: Habenzinsen t2..t5", plan.reihe("habenzins")[2:], [2, 4, 6, 9])
    pruefe(k, "Tab. 3: Endvermoegen (gerundet)", kaufm(plan.endwert, "1"), "10250", "0", 0)
    pruefe(k, "Tab. 3: Endwert genau", plan.endwert, "10249.85")
    pruefe_proz(k, "Tab. 3: VOFI-Rendite", kz["rendite"], "5.08", 2)
    pruefe(k, "Tab. 4: Endvermoegen Finanzinvestition (gerundet)", kaufm(alt.endwert, "1"), "10188", "0", 0)
    pruefe(k, "Tab. 4: Endwert genau", alt.endwert, "10188.28")
    pruefe_reihe(k, "Tab. 4: Reinvestition t1..t4", [z["kurz"] for z in alt.zeilen[1:5]], [400, 818, 1255, 1711])
    pruefe_proz(k, "Tab. 4: Vergleichsrendite", kz["vergleichsrendite"], "4.95", 2)
    pruefe(k, "Vermoegensendwert (Endwertdifferenz) ohne Steuern", kz["endwertdifferenz"], "61.57")
    pruefe_proben(k, plan, alt)
    la = lehrbuchansicht(plan)
    pruefe_gleich(k, "Lehrbuchansicht: Saldo t0..t4 null, t5 = Endvermoegen",
                  [z["saldo"] for z in la[:5]] == [NULL] * 5 and la[5]["saldo"] == plan.endwert, True)
    # ---- Tab. 5/6: mit Steuern
    plan, alt, kz, tr = _schulte_standard(lehrbuch_steuer("0.5"), 250)
    pruefe_reihe(k, "Tab. 5: Steuerzahlung t1..t5", plan.reihe("steuer")[1:], [70, 82, 94, 106, 744])
    pruefe_reihe(k, "Tab. 5: Zwischenfinanzierung t1..t4", plan.reihe("kk")[1:5], [24, 63, 117, 188])
    pruefe_reihe(k, "Tab. 5: Sollzinsen Zwischenfinanzierung t2..t5", plan.reihe("kkzins")[2:], [2, 6, 10, 17])
    pruefe(k, "Tab. 5: Endvermoegen (gerundet)", kaufm(plan.endwert, "1"), "9097", "0", 0)
    pruefe(k, "Tab. 5: Endwert genau", plan.endwert, "9096.56")
    pruefe_proz(k, "Tab. 5: VOFI-Rendite nach Steuern", kz["rendite"], "2.60", 2)
    pruefe_reihe(k, "Tab. 6: Steuerzahlung t1..t5", [z["steuer"] for z in alt.zeilen[1:]], [200, 205, 209, 214, 219])
    pruefe_reihe(k, "Tab. 6: Reinvestition t1..t4", [z["kurz"] for z in alt.zeilen[1:5]], [200, 405, 614, 827])
    pruefe(k, "Tab. 6: Endvermoegen (gerundet)", kaufm(alt.endwert, "1"), "9046", "0", 0)
    pruefe(k, "Tab. 6: Endwert genau", alt.endwert, "9046.02")
    pruefe_proz(k, "Tab. 6: Vergleichsrendite nach Steuern", kz["vergleichsrendite"], "2.49", 2)
    pruefe(k, "Vermoegensendwert (Endwertdifferenz) mit Steuern", kz["endwertdifferenz"], "50.53")
    pruefe_proben(k, plan, alt)
    # ---- Ein-Satz-Formel gegen den Finanzplan mit zwei Saetzen (Anlass der Regel R-9.1)
    formel = D(8000) * (1 + D("0.05") * (1 - s)) ** 5
    info(f"Ein-Satz-Formel 8.000 x (1 + 5 % x 0,5)^5 = {de(formel)}; Finanzplan mit zwei Saetzen {de(alt.endwert)}; "
         f"Differenz {de(formel - alt.endwert)}")
    # ---- Hebelwirkung (Plausibilitaetstest R-15.5): Rendite steigt hier mit dem Eigenkapital
    renditen = []
    for ek in range(3000, 10001, 1000):
        trs = [] if ek == 10000 else [Tranche("Kredit", 10000 - ek, "annuitaet_laufzeit", "0.075", laufzeit=5,
                                               rundung="keine")]
        _, _, kzh = jahresplan(5, 10000, 540, ek, trs, "0.045", "0.09", verkauf=10000)
        renditen.append(kzh["rendite"])
    pruefe_gleich(k, "Hebelwirkung negativ: VOFI-Rendite steigt mit dem Eigenkapital (3.000 bis 10.000)",
                  all(b > a for a, b in zip(renditen, renditen[1:])), True)
    info("Renditen je Eigenkapital 3.000..10.000: " + " / ".join(de(x * 100, 2) for x in renditen))


def rf04_schulte_fallbeispiel():
    k = fall("RF-04", "Schulte, Fallbeispiel Buerogebaeude (Tab. 7 bis 14), Betraege in Tausend Euro")
    basis = dict(n=10, a0=43738, ueberschuss=3606, ek=21869, h="0.05", kk="0.11", steuer=lehrbuch_steuer("0.5"),
                 verkauf=43738, afa=600, a_lang="0.07")
    tr = Tranche("Kredit", 21869, "endfaellig", "0.10", rundung="keine")
    plan, alt, kz = jahresplan(tranchen=[tr], **basis)
    pruefe_reihe(k, "endfaellig: Steuerzahlung t1..t10", plan.reihe("steuer")[1:],
                 [410, 435, 461, 487, 514, 542, 571, 600, 630, 3661])
    pruefe_reihe(k, "endfaellig: Reinvestition t1..t9", plan.reihe("guthaben")[1:10],
                 [1010, 2044, 3105, 4192, 5307, 6449, 7620, 8820, 10050])
    pruefe(k, "endfaellig: Endvermoegen (gerundet)", kaufm(plan.endwert, "1"), "30179", "0", 0)
    pruefe(k, "endfaellig: Endwert genau", plan.endwert, "30179.37")
    pruefe_proz(k, "endfaellig: VOFI-Rendite", kz["rendite"], "3.27", 2)
    pruefe_gleich(k, "endfaellig: unvorteilhaft (Endwertdifferenz negativ)", kz["endwertdifferenz"] < 0, True)
    pruefe_proben(k, plan, alt, "endfaellig: Kontrollsummen")
    ew_end = plan.endwert

    tr = Tranche("Kredit", 21869, "annuitaet_laufzeit", "0.10", laufzeit=10, rundung="keine")
    plan, alt, kz = jahresplan(tranchen=[tr], **basis)
    pruefe(k, "Annuitaet: Rate", tr.rate, "3559", "0.5", 0)
    pruefe_reihe(k, "Annuitaet: Zinsen t1..t10", plan.reihe("zins")[1:],
                 [2187, 2050, 1899, 1733, 1550, 1349, 1128, 885, 618, 324])
    pruefe_reihe(k, "Annuitaet: Kreditstand t1..t10", plan.reihe("restschuld")[1:],
                 [20497, 18987, 17327, 15501, 13492, 11282, 8851, 6177, 3236, 0])
    pruefe_reihe(k, "Annuitaet: Zwischenfinanzierung t1..t9", plan.reihe("kk")[1:10],
                 [363, 814, 1365, 2030, 2823, 3760, 4858, 6139, 7624])
    pruefe(k, "Annuitaet: Endvermoegen (gerundet)", kaufm(plan.endwert, "1"), "31400", "0", 0)
    pruefe(k, "Annuitaet: Endwert genau", plan.endwert, "31400.46")
    pruefe_proz(k, "Annuitaet: VOFI-Rendite", kz["rendite"], "3.68", 2)
    pruefe_proben(k, plan, alt, "Annuitaet: Kontrollsummen")

    tr = Tranche("Kredit", 21869, "frei", "0.10", rundung="keine")
    plan, alt, kz = jahresplan(tranchen=[tr], **basis)
    pruefe_reihe(k, "freie Tilgung: Tilgung t1..t9", plan.reihe("tilgung")[1:10],
                 [1010, 1060, 1113, 1169, 1227, 1288, 1353, 1421, 1492])
    pruefe(k, "freie Tilgung: Rueckzahlung in t10 (Tab. 11: 10.737)",
           plan.zeilen[10]["tilgung"] + plan.zeilen[10]["abloesung"], "10737", "0.5", 0)
    pruefe_reihe(k, "freie Tilgung: Kreditstand t1..t10", plan.reihe("restschuld")[1:],
                 [20859, 19799, 18686, 17518, 16291, 15002, 13649, 12229, 10737, 0])
    pruefe_reihe(k, "freie Tilgung: Steuerzahlung t1..t10", plan.reihe("steuer")[1:],
                 [410, 460, 513, 569, 627, 688, 753, 821, 892, 3966])
    pruefe(k, "freie Tilgung: Endvermoegen nach Tab. 11 (gerundet)", kaufm(plan.endwert, "1"), "31567", "0", 0)
    pruefe(k, "freie Tilgung: Endwert genau", plan.endwert, "31567.01")
    pruefe_proz(k, "freie Tilgung: VOFI-Rendite", kz["rendite"], "3.74", 2)
    pruefe_proben(k, plan, alt, "freie Tilgung: Kontrollsummen")
    pruefe_gleich(k, "freie Tilgung ist die beste der drei Kreditvarianten", plan.endwert > ew_end, True)

    # Finanzinvestition: Buchtabelle in sich um eine Einheit unstimmig -> Toleranz eine Einheit
    pruefe(k, "Finanzinvestition: Endvermoegen (Tab. 13: 30.445)", alt.endwert, "30445", "1", 2)
    pruefe(k, "Finanzinvestition: Endwert genau", alt.endwert, "30444.24")
    pruefe_reihe(k, "Finanzinvestition: Steuerzahlung t1..t10", [z["steuer"] for z in alt.zeilen[1:]],
                 [765, 784, 804, 824, 845, 866, 888, 910, 933, 956], "1")
    pruefe_reihe(k, "Finanzinvestition: Reinvestition t1..t9", [z["kurz"] for z in alt.zeilen[1:10]],
                 [765, 1550, 2354, 3179, 4024, 4890, 5777, 6687, 7620], "1")
    pruefe_proz(k, "Finanzinvestition: Vergleichsrendite", kz["vergleichsrendite"], "3.36", 2)
    formel = D(21869) * (1 + D("0.07") * D("0.5")) ** 10
    info(f"Ein-Satz-Formel {de(formel)} gegen Finanzplan {de(alt.endwert)}: Differenz {de(formel - alt.endwert)} "
         f"({de((formel / alt.endwert - 1) * 100, 2)} %)")


def alle():
    rf01_kirchner()
    rf02_iwu2013()
    rf03_schulte_standard()
    rf04_schulte_fallbeispiel()
