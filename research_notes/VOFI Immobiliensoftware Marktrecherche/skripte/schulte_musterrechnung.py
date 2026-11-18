"""Nachrechnung der Musterrechnungen aus Schulte et al., „Immobilieninvestition" (Quellnotiz 11).

Baut die Rechnungen des Kapitels aus den Eingangsdaten nach und vergleicht mit den Buchwerten:

  A  Standardbeispiel, klassische Verfahren (Buchseiten 802, 804, 808, 810)
  B  Standardbeispiel als VOFI ohne und mit Steuern, Immobilie und Finanzinvestition
     (Tab. 3 bis 6, Buchseiten 812, 814, 818, 820)
  C  Fallbeispiel Bürogebäude mit drei Kreditvarianten und Finanzinvestition
     (Tab. 7 bis 15, Buchseiten 822 bis 830)
  D  Zusatzrechnungen für die Notiz (kein Buchvergleich)

Gerechnet wird mit voller Genauigkeit (decimal); verglichen wird der kaufmännisch gerundete
Wert, weil das Buch ganze Geldeinheiten und Renditen mit zwei Nachkommastellen ausweist.
Die Buchwerte stehen unten als Prüfpunkte (Auswahl je Tabelle, keine Abschrift der Tabellen).
Kein Produktcode. Aufruf: python3 schulte_musterrechnung.py (Rückgabewert 1, solange Prüfungen abweichen).

Stand 2026-11-18: 50 von 53 Prüfungen treffen die Buchwerte. Die drei Abweichungen liegen alle in
der Finanzinvestition des Fallbeispiels (Tab. 13/14) und betragen je eine Einheit (Tausend Euro):
Steuerzahlung t_2, vier Werte der Reinvestition und das Endvermögen (30.444 statt 30.445); die
Rendite stimmt. Vermutung: Die Tabelle ist mit einem nicht gerundeten Zinsertrag gerechnet und in
sich um eine Einheit unstimmig; Abschnitt C zeigt, dass kein Zinsertrag zwischen 1.530,50 und
1.531,50 alle veröffentlichten Zellen zugleich trifft. Nichts ist angepasst.
"""
from decimal import Decimal as D, ROUND_HALF_UP, getcontext

getcontext().prec = 40
NULL, EINS = D(0), D(1)


def runden(x, stellen="1"):
    return x.quantize(D(stellen), ROUND_HALF_UP)


def rendite(endwert, ek, n):
    """VOFI-Rendite: (K_N / EK_0)^(1/N) - 1 (Buchseiten 814 bis 815)."""
    return (endwert / ek) ** (EINS / D(n)) - EINS


def annuitaet(kredit, i, n):
    q = (EINS + i) ** n
    return kredit * i * q / (q - EINS)


def vofi(n, a0, ue, rn, ek, kredit, kreditart, i_kredit, i_haben_kurz, i_soll_kurz, s, afa):
    """Vollständiger Finanzplan nach dem Schema der Tab. 3 und 5.

    Zeilen: direkte Zahlungen (a0, ü_t, R_n); indirekte Zahlungen (Eigenkapital, Fremdkapital,
    Zinsen FK, Tilgung, Steuerzahlung, je Periode einjährige Reinvestition oder
    Zwischenfinanzierung mit Zins und Rückzahlung in der Folgeperiode). Der Periodensaldo ist
    in t_0 bis t_(n-1) null, in t_n ist er das Endvermögen.

    kurz[t] > 0: Reinvestition in t (Anlage für ein Jahr); kurz[t] < 0: Zwischenfinanzierung.
    kreditart: "annuitaet" | "endfaellig" | "frei" | "ohne".
    """
    assert ek + kredit - a0 == 0, "t_0 muss ausgeglichen sein"
    rate = annuitaet(kredit, i_kredit, n) if kreditart == "annuitaet" else NULL
    stand, kurz_alt, buchwert = kredit, NULL, a0
    z = {k: [NULL] for k in ("zins_fk", "tilgung", "steuer", "kurz", "kurz_zins", "ergebnis", "saldo")}
    z["kreditstand"], z["buchwert"] = [kredit], [a0]
    for t in range(1, n + 1):
        letzte = t == n
        zins_fk = i_kredit * stand
        kurz_zins = kurz_alt * (i_haben_kurz if kurz_alt > 0 else i_soll_kurz)  # + Haben-, - Sollzins
        buchwert -= afa
        gewinn = (rn - buchwert) if letzte else NULL
        ergebnis = ue - afa + kurz_zins - zins_fk + gewinn
        steuer = s * ergebnis  # negativ = Erstattung (sofortiger Verlustausgleich)
        vor_tilgung = ue + (rn if letzte else NULL) - zins_fk - steuer + kurz_alt + kurz_zins
        if kreditart == "annuitaet":
            tilgung = rate - zins_fk
        elif kreditart == "endfaellig":
            tilgung = stand if letzte else NULL
        elif kreditart == "frei":  # freie Liquidität tilgt; Rest am Ende
            tilgung = stand if letzte else max(NULL, min(stand, vor_tilgung))
        else:
            tilgung = NULL
        stand -= tilgung
        saldo = vor_tilgung - tilgung
        kurz_neu = NULL if letzte else saldo
        for k, v in (("zins_fk", zins_fk), ("tilgung", tilgung), ("steuer", steuer), ("kurz", kurz_neu),
                     ("kurz_zins", kurz_zins), ("ergebnis", ergebnis), ("saldo", saldo - kurz_neu),
                     ("kreditstand", stand), ("buchwert", buchwert)):
            z[k].append(v)
        kurz_alt = kurz_neu
    z["endwert"] = z["saldo"][n]
    z["rendite"] = rendite(z["endwert"], ek, n) if ek > 0 else None
    return z


def finanzinvestition(n, ek, i_lang, i_haben_kurz, s):
    """Unterlassungsalternative des Buchs: Anlage des Eigenkapitals zum langfristigen Habenzins,
    jährliche Zinszahlung, Wiederanlage der Zinsen für je ein Jahr zum kurzfristigen Satz."""
    return vofi(n, ek, i_lang * ek, ek, ek, NULL, "ohne", NULL, i_haben_kurz, NULL, s, NULL)


def kapitalwert(ue, rn, a0, i, n):
    return sum(ue * (EINS + i) ** -t for t in range(1, n + 1)) + rn * (EINS + i) ** -n - a0


def interner_zins(ue, rn, a0, n):
    lo, hi = D("0.0001"), D("0.5")
    for _ in range(120):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if kapitalwert(ue, rn, a0, mid, n) > 0 else (lo, mid)
    return (lo + hi) / 2


# ---------------------------------------------------------------- Vergleich mit den Buchwerten
ERGEBNIS = {"ok": 0, "abw": 0, "max": D(0)}
ABWEICHUNGEN = []


def pruefe(name, buch, wert, stellen="1", seite=""):
    """Vergleicht den gerundeten Skriptwert mit dem Buchwert und druckt eine Zeile."""
    ger = runden(wert, stellen)
    ok = ger == D(str(buch))
    ERGEBNIS["ok" if ok else "abw"] += 1
    if not ok:
        ABWEICHUNGEN.append((name, buch, ger, seite))
        if stellen == "1":
            ERGEBNIS["max"] = max(ERGEBNIS["max"], abs(ger - D(str(buch))))
    print(f"  {'ok ' if ok else 'ABW'} {name:<58} Buch {str(buch):>9}  Skript {str(ger):>9}  (genau {wert:.4f})  {seite}")


def pruefe_reihe(name, buch, werte, seite=""):
    ger = [runden(w) for w in werte]
    soll = [D(str(b)) for b in buch]
    diff = [(t + 1, b, g) for t, (b, g) in enumerate(zip(soll, ger)) if b != g]
    ok = not diff and len(soll) == len(ger)
    ERGEBNIS["ok" if ok else "abw"] += 1
    if not ok:
        ABWEICHUNGEN.append((name, buch, [str(g) for g in ger], seite))
        ERGEBNIS["max"] = max([ERGEBNIS["max"]] + [abs(b - g) for _, b, g in diff])
    print(f"  {'ok ' if ok else 'ABW'} {name:<58} {len(soll)} Werte" + ("" if ok else f"; abweichend (t, Buch, Skript): {diff}") + f"  {seite}")


def prozent(x):
    return x * 100


if __name__ == "__main__":
    # ============================================================ A  Standardbeispiel, klassisch
    print("A  Standardbeispiel, klassische Verfahren")
    a0, ue, rn, n = D(10000), D(540), D(10000), 5
    ek, fk = D(8000), D(2000)
    i_h, i_s_lang = D("0.05"), D("0.075")
    kzf = (i_h * ek + i_s_lang * fk) / (ek + fk)
    pruefe("Kalkulationszinsfuß (Mischzins) in %", "5.5", prozent(kzf), "0.1", "S. 802")
    pruefe("Kapitalwert C_0", -43, kapitalwert(ue, rn, a0, kzf, n), seite="S. 802")
    pruefe("Interner Zinsfuß in %", "5.4", prozent(interner_zins(ue, rn, a0, n)), "0.1", "S. 804")
    s, afa = D("0.5"), D(5000) / 20
    i_st = (EINS - s) * kzf
    ue_st = ue - s * (ue - afa)
    rn_st = rn - s * (rn - (a0 - afa * n))
    pruefe("Steuerkorrigierter Kalkulationszinsfuß in %", "2.75", prozent(i_st), "0.01", "S. 808")
    pruefe("Einnahmenüberschuss nach Steuern", 395, ue_st, seite="S. 808")
    pruefe("Netto-Veräußerungserlös", 9375, rn_st, seite="S. 808")
    pruefe("Kapitalwert nach Steuern C_0s", 8, kapitalwert(ue_st, rn_st, a0, i_st, n), seite="S. 808")
    pruefe("Interner Zinsfuß nach Steuern in %", "2.77", prozent(interner_zins(ue_st, rn_st, a0, n)), "0.01", "S. 810")

    # ============================================================ B  Standardbeispiel als VOFI
    print("\nB  Standardbeispiel als VOFI (Tab. 3 bis 6)")
    i_haben_kurz, i_soll_kurz = D("0.045"), D("0.09")
    args = dict(n=n, a0=a0, ue=ue, rn=rn, ek=ek, kredit=fk, kreditart="annuitaet", i_kredit=i_s_lang,
                i_haben_kurz=i_haben_kurz, i_soll_kurz=i_soll_kurz)

    print(" Tab. 3: Immobilie ohne Steuern")
    v = vofi(**args, s=NULL, afa=NULL)
    pruefe("Annuität", 494, annuitaet(fk, i_s_lang, n), seite="S. 811, 812")
    pruefe_reihe("Zinsen FK t1..t5", [150, 124, 96, 67, 34], v["zins_fk"][1:], "S. 812")
    pruefe_reihe("Tilgung t1..t5", [344, 370, 398, 428, 460], v["tilgung"][1:], "S. 812")
    pruefe_reihe("Kredit nach Tilgung t1..t5", [1656, 1286, 888, 460, 0], v["kreditstand"][1:], "S. 812")
    pruefe_reihe("Reinvestition t1..t4", [46, 93, 143, 195], v["kurz"][1:5], "S. 812")
    pruefe_reihe("Habenzinsen t2..t5", [2, 4, 6, 9], v["kurz_zins"][2:], "S. 812")
    pruefe("Endwert (Endvermögen) K_5", 10250, v["endwert"], seite="S. 812")
    pruefe("VOFI-Rendite in %", "5.08", prozent(v["rendite"]), "0.01", "S. 812, 815")
    ew_i = v["endwert"]

    print(" Tab. 4: Finanzinvestition ohne Steuern")
    f = finanzinvestition(n, ek, i_h, i_haben_kurz, NULL)
    pruefe_reihe("Reinvestition t1..t4", [400, 818, 1255, 1711], f["kurz"][1:5], "S. 814")
    pruefe_reihe("Habenzinsen t2..t5", [18, 37, 56, 77], f["kurz_zins"][2:], "S. 814")
    pruefe("Endwert K_5", 10188, f["endwert"], seite="S. 813, 814")
    pruefe("VOFI-Rendite in %", "4.95", prozent(f["rendite"]), "0.01", "S. 814, 815")
    ew_u = f["endwert"]

    print(" Tab. 5: Immobilie mit Steuern (s = 50 %, AfA 250, Veräußerungsgewinn steuerpflichtig)")
    vs = vofi(**args, s=s, afa=afa)
    pruefe_reihe("Steuerzahlung t1..t5", [70, 82, 94, 106, 744], vs["steuer"][1:], "S. 818")
    pruefe_reihe("Ergebnis vor Steuer t1..t5", [140, 164, 188, 213, 1489], vs["ergebnis"][1:], "S. 818")
    pruefe_reihe("Zwischenfinanzierung t1..t4", [24, 63, 117, 188], [-x for x in vs["kurz"][1:5]], "S. 818")
    pruefe_reihe("Sollzinsen Zwischenfinanzierung t2..t5", [2, 6, 10, 17], [-x for x in vs["kurz_zins"][2:]], "S. 818")
    pruefe_reihe("Buchwert t1..t5", [9750, 9500, 9250, 9000, 8750], vs["buchwert"][1:], "S. 818")
    pruefe("Endwert K_5", 9097, vs["endwert"], seite="S. 817, 818")
    pruefe("VOFI-Rendite nach Steuern in %", "2.60", prozent(vs["rendite"]), "0.01", "S. 817 bis 819")
    ew_is = vs["endwert"]

    print(" Tab. 6: Finanzinvestition mit Steuern")
    fs = finanzinvestition(n, ek, i_h, i_haben_kurz, s)
    pruefe_reihe("Steuerzahlung t1..t5", [200, 205, 209, 214, 219], fs["steuer"][1:], "S. 820")
    pruefe_reihe("Reinvestition t1..t4", [200, 405, 614, 827], fs["kurz"][1:5], "S. 820")
    pruefe("Endwert K_5", 9046, fs["endwert"], seite="S. 819, 820")
    pruefe("VOFI-Rendite nach Steuern in %", "2.49", prozent(fs["rendite"]), "0.01", "S. 819, 820")
    ew_us = fs["endwert"]

    # ============================================================ C  Fallbeispiel Bürogebäude
    # Eingangsdaten nach den Tabellen (Tausend Euro). Der Fließtext auf S. 819 nennt abweichend
    # 44.800.000 Euro Kaufpreis und 3.700.000 Euro Netto-Mieteinnahmen; die Tabellen und die
    # Annuitätenrechnung auf S. 821 rechnen mit 43.738 und 3.606.
    print("\nC  Fallbeispiel Bürogebäude (Tab. 7 bis 15), Beträge in Tausend Euro")
    n10, a0g, ueg = 10, D(43738), D(3606)
    ekg = fkg = D(21869)
    afag = D(15000) * D("0.04")
    argsg = dict(n=n10, a0=a0g, ue=ueg, rn=a0g, ek=ekg, kredit=fkg, i_kredit=D("0.10"),
                 i_haben_kurz=D("0.05"), i_soll_kurz=D("0.11"), s=D("0.5"), afa=afag)

    print(" Tab. 7/8: endfälliger Kredit")
    e = vofi(**argsg, kreditart="endfaellig")
    pruefe_reihe("Steuerzahlung t1..t10", [410, 435, 461, 487, 514, 542, 571, 600, 630, 3661], e["steuer"][1:], "S. 822, 823")
    pruefe_reihe("Reinvestition t1..t9", [1010, 2044, 3105, 4192, 5307, 6449, 7620, 8820, 10050], e["kurz"][1:10], "S. 822")
    pruefe_reihe("Ergebnis vor Steuer t1..t10", [819, 870, 921, 974, 1029, 1084, 1142, 1200, 1260, 7322], e["ergebnis"][1:], "S. 823")
    pruefe("Endvermögen", 30179, e["endwert"], seite="S. 822, 830")
    pruefe("EK-Rendite in %", "3.27", prozent(e["rendite"]), "0.01", "S. 823, 830")

    print(" Tab. 9/10: Annuitätendarlehen")
    an = vofi(**argsg, kreditart="annuitaet")
    pruefe("Annuität", 3559, annuitaet(fkg, D("0.10"), n10), seite="S. 821")
    pruefe_reihe("Zinsen t1..t10", [2187, 2050, 1899, 1733, 1550, 1349, 1128, 885, 618, 324], an["zins_fk"][1:], "S. 824")
    pruefe_reihe("Kreditstand t1..t10", [20497, 18987, 17327, 15501, 13492, 11282, 8851, 6177, 3236, 0], an["kreditstand"][1:], "S. 824, 825")
    pruefe_reihe("Steuerzahlung t1..t10", [410, 458, 509, 562, 616, 673, 732, 793, 857, 3922], an["steuer"][1:], "S. 824, 825")
    pruefe_reihe("Zwischenfinanzierung t1..t9", [363, 814, 1365, 2030, 2823, 3760, 4858, 6139, 7624], [-x for x in an["kurz"][1:10]], "S. 824")
    pruefe("Endvermögen", 31400, an["endwert"], seite="S. 824, 830")
    pruefe("EK-Rendite in %", "3.68", prozent(an["rendite"]), "0.01", "S. 825, 830")

    print(" Tab. 11/12: Kredit mit freier Tilgung")
    fr = vofi(**argsg, kreditart="frei")
    pruefe_reihe("Tilgung t1..t10", [1010, 1060, 1113, 1169, 1227, 1288, 1353, 1421, 1492, 10737], fr["tilgung"][1:], "S. 826")
    pruefe_reihe("Kreditstand t1..t10", [20859, 19799, 18686, 17518, 16291, 15002, 13649, 12229, 10737, 0], fr["kreditstand"][1:], "S. 826, 827")
    pruefe_reihe("Steuerzahlung t1..t10", [410, 460, 513, 569, 627, 688, 753, 821, 892, 3966], fr["steuer"][1:], "S. 826, 827")
    pruefe("Endvermögen laut Tab. 11", 31567, fr["endwert"], seite="S. 826")
    pruefe("EK-Rendite in %", "3.74", prozent(fr["rendite"]), "0.01", "S. 827, 830")
    print(f"      Hinweis: Tab. 15 (S. 830) nennt 31.576; Tab. 11 (S. 826) und die Nachrechnung ergeben "
          f"{runden(fr['endwert'])} (Zahlendreher in Tab. 15; die Rendite ist in beiden Fällen 3,74 %).")

    print(" Tab. 13/14: Finanzinvestition (7 % langfristig, Wiederanlage 5 %)")
    fg = finanzinvestition(n10, ekg, D("0.07"), D("0.05"), D("0.5"))
    pruefe("Zinseinnahmen je Jahr", 1531, D("0.07") * ekg, seite="S. 828, 829")
    pruefe_reihe("Steuerzahlung t1..t10", [765, 784, 804, 824, 845, 866, 888, 910, 933, 956], fg["steuer"][1:], "S. 828, 829")
    pruefe_reihe("Reinvestition t1..t9", [765, 1550, 2354, 3179, 4024, 4890, 5777, 6687, 7620], fg["kurz"][1:10], "S. 828")
    pruefe("Endvermögen", 30445, fg["endwert"], seite="S. 828, 830")
    pruefe("EK-Rendite in %", "3.36", prozent(fg["rendite"]), "0.01", "S. 829, 830")

    # Ursachensuche zu Tab. 13/14: Gibt es einen Zinsertrag, der gerundet 1.531 ergibt und alle
    # veröffentlichten Zellen (Steuer, Reinvestition, Endvermögen) zugleich trifft?
    buch_st = [765, 784, 804, 824, 845, 866, 888, 910, 933, 956]
    buch_re = [765, 1550, 2354, 3179, 4024, 4890, 5777, 6687, 7620]
    treffer = []
    for hundertstel in range(153050, 153150):
        u = D(hundertstel) / 100
        x = vofi(n10, ekg, u, ekg, ekg, NULL, "ohne", NULL, D("0.05"), NULL, D("0.5"), NULL)
        fehler = (sum(runden(a) != b for a, b in zip(x["steuer"][1:], buch_st))
                  + sum(runden(a) != b for a, b in zip(x["kurz"][1:10], buch_re)) + (runden(x["endwert"]) != 30445))
        treffer.append((fehler, u))
    kleinste = min(t[0] for t in treffer)
    beste = [u for fehl, u in treffer if fehl == kleinste]
    print(f"      Ursachensuche: Zinsertrag 1.530,50 bis 1.531,49 in Schritten von 0,01; kleinste Zahl abweichender "
          f"Zellen {kleinste} (bei {beste[0]} bis {beste[-1]}); mit 7 % auf 21.869 = {D('0.07') * ekg} sind es "
          f"{[fehl for fehl, u in treffer if u == D('1530.83')][0]}.")

    # ============================================================ Zusammenfassung
    print(f"\nVergleich mit den Buchwerten: {ERGEBNIS['ok']} Prüfungen bestanden, {ERGEBNIS['abw']} abweichend; "
          f"größte Abweichung eines Betrags: {ERGEBNIS['max']} Einheit(en).")
    for name, buch, wert, seite in ABWEICHUNGEN:
        print(f"  ABWEICHUNG {name}: Buch {buch}, Skript {wert} {seite}")

    # ============================================================ D  Zusatzrechnungen (kein Buchvergleich)
    print("\nD  Zusatzrechnungen für die Notiz (eigene Rechnung, nicht im Buch)")
    print(" Vermögensendwert (Differenz der Endvermögen, im Buch nur als Vergleich K_I > K_U):")
    print(f"   Standardbeispiel ohne Steuern {ew_i - ew_u:.2f}; mit Steuern {ew_is - ew_us:.2f}")
    for name, x in (("endfällig", e), ("Annuität", an), ("freie Tilgung", fr)):
        print(f"   Fallbeispiel {name:<14} {x['endwert'] - fg['endwert']:.2f}")
    print(" Unterlassungsalternative: Buch (zwei Zinssätze) gegen Projektformel EK * (1 + h * (1 - s))^n:")
    for name, buch, h, steuer, jahre, kapital in (("Standard ohne Steuern", ew_u, i_h, NULL, n, ek),
                                                  ("Standard mit Steuern", ew_us, i_h, s, n, ek),
                                                  ("Fallbeispiel mit Steuern", fg["endwert"], D("0.07"), D("0.5"), n10, ekg)):
        formel = kapital * (EINS + h * (EINS - steuer)) ** jahre
        print(f"   {name:<26} Buch {buch:>12.2f}  Formel {formel:>12.2f}  Differenz {formel - buch:>8.2f}")
    print(" Volle Genauigkeit der Endwerte (für einen Referenzfall mit Toleranz 0,01):")
    for name, x in (("Tab. 3", v), ("Tab. 4", f), ("Tab. 5", vs), ("Tab. 6", fs), ("Tab. 7", e), ("Tab. 9", an),
                    ("Tab. 11", fr), ("Tab. 13", fg)):
        print(f"   {name:<8} Endwert {x['endwert']:.6f}  Rendite {prozent(x['rendite']):.6f} %")
    print(" Kontrollsumme Finanzierungssaldo: Summe der Periodensalden t_0 bis t_(n-1) je Plan:",
          [str(runden(sum(x["saldo"][:-1]), "0.01")) for x in (v, f, vs, fs, e, an, fr, fg)])
    print(" Abb. 11 (S. 809), Kapitalwert nach Steuern je Steuersatz (Buch: -43 bei 0 %, 0 bei 100 %):")
    zeile = []
    for proz in (0, 20, 40, 50, 60, 70, 80, 100):
        st = D(proz) / 100
        c = kapitalwert(ue - st * (ue - afa), rn - st * (rn - (a0 - afa * n)), a0, (EINS - st) * kzf, n)
        zeile.append(f"{proz} %: {c:.1f}")
    print("   " + "; ".join(zeile))
    print(" Abb. 12 (S. 815), VOFI-Rendite ohne Steuern je Eigenkapitaleinsatz (Buch nur als Diagramm; abgelesen etwa")
    print("   -4,6 % bei 2.500, -1,9 % bei 3.000, -0,1 % bei 3.500). Zwischenfinanzierung 9 % wie Tab. 3 und zum Vergleich 10 %:")
    for satz in (i_soll_kurz, D("0.10")):
        zeile = []
        for kap in range(2500, 10001, 500):
            x = vofi(n, a0, ue, rn, D(kap), a0 - D(kap), "annuitaet" if kap < 10000 else "ohne", i_s_lang,
                     i_haben_kurz, satz, NULL, NULL)
            zeile.append(f"{kap}: {prozent(x['rendite']):.2f}")
        print(f"   {prozent(satz):.0f} %: " + "; ".join(zeile))
    raise SystemExit(1 if ERGEBNIS["abw"] else 0)
