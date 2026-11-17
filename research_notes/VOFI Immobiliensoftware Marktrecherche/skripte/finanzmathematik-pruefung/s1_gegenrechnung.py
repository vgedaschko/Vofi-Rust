#!/usr/bin/env python3
"""Unabhaengige Gegenrechnung zum synthetischen Testfall S1 und zu den Formeln
der Recherchenotiz 03_vofi_methodik_steuern_risiko.md (Pruefer Finanzmathematik).

Rechnet exakt mit Bruechen (fractions.Fraction); Rundung nur bei der Ausgabe
bzw. wahlweise kaufmaennisch je Zahlung auf Cent (Modus 'cent').
"""
from fractions import Fraction as F
from decimal import Decimal, ROUND_HALF_UP


def cent(x):
    """Kaufmaennisch auf Cent runden (Fraction -> Fraction)."""
    d = (Decimal(x.numerator) / Decimal(x.denominator)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return F(d)


def fmt(x, nd=2):
    d = (Decimal(x.numerator) / Decimal(x.denominator)).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)
    s = f"{d:,.{nd}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def vofi(n, Z, steuerbar, afa, ek, K0, i, annuitaet, h, kk_zins, s,
         s_zins=None, verlust="sofort", kk_zins_buchen=True, runden=False,
         entnahme=None):
    """Jahres-VOFI nach der Rechenreihenfolge der Notiz (Zinsen auf Vorperiodenbestand).

    Z[t]          originaere Zahlung (t=0..n), inkl. Kauf in 0 und Verkauf in n
    steuerbar[t]  steuerpflichtiger Teil von Z[t] (Reinertrag)
    ek[t]         EK-Einlage (+)
    entnahme[t]   EK-Entnahme (+ = Abfluss)
    Kredit: K0 in t=0, Zins i auf Vorjahresrestschuld, feste Annuitaet, Abloesung in n
    """
    r = cent if runden else (lambda x: x)
    s_zins = s if s_zins is None else s_zins
    entnahme = entnahme or [F(0)] * (n + 1)
    rows = []
    guth = F(0); kk = F(0); rs = F(0); vv = F(0)
    for t in range(n + 1):
        aufnahme = K0 if t == 0 else F(0)
        sollz = r(i * rs) if t > 0 else F(0)
        tilg = (annuitaet - sollz) if t > 0 else F(0)
        abl = F(0)
        if t == n and t > 0:
            abl = rs - tilg
        habenz = r(h * guth)
        kkz = r(kk_zins * kk)
        kkz_wirksam = kkz if kk_zins_buchen else F(0)
        # Steuer-Nebenrechnung
        bmg_op = steuerbar[t] - afa[t] - sollz - kkz_wirksam
        bmg_zins = habenz
        bmg = bmg_op + bmg_zins
        if verlust == "sofort":
            steuer = r(s * bmg_op + s_zins * bmg_zins)
        else:  # Verlustvortrag, einheitlicher Satz
            basis = bmg - vv
            if basis < 0:
                vv = -basis; steuer = F(0)
            else:
                vv = F(0); steuer = r(s * basis)
        saldo = (Z[t] + ek[t] - entnahme[t] + aufnahme - tilg - abl - sollz
                 - kkz_wirksam + habenz - steuer)
        netto_alt = guth - kk
        netto_neu = netto_alt + saldo
        guth_neu = max(netto_neu, F(0)); kk_neu = max(-netto_neu, F(0))
        anlage = guth_neu - guth          # + = Anlage, - = Aufloesung
        kk_aufn = kk_neu - kk             # + = Aufnahme, - = Tilgung
        fin_saldo = saldo - anlage + kk_aufn
        rs = rs + aufnahme - tilg - abl
        guth, kk = guth_neu, kk_neu
        rows.append(dict(t=t, Z=Z[t], ek=ek[t], entn=entnahme[t], aufn=aufnahme, sollz=sollz,
                         tilg=tilg, abl=abl, habenz=habenz, kkz=kkz, afa=afa[t], bmg=bmg,
                         steuer=steuer, anlage=anlage, kk_aufn=kk_aufn, fin=fin_saldo,
                         guth=guth, kk=kk, rs=rs, bestand=guth - kk - rs))
    return rows


def wurzel(x, n):
    return float(x) ** (1.0 / n) - 1.0


def irr(cf, lo=-0.99, hi=1.0):
    f = lambda r: sum(float(c) / (1 + r) ** k for k, c in enumerate(cf))
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


# ---------------------------------------------------------------- S1 Eingaben
n = 5
KP, ENK = F(1_000_000), F(100_000)
EK0, K0 = F(400_000), F(700_000)
i, tilg0 = F(4, 100), F(2, 100)
ANN = K0 * (i + tilg0)
RE1, g = F(55_000), F(2, 100)
AFA = F(2, 100) * F(80, 100) * (KP + ENK)
s, h, kkz = F(30, 100), F(2, 100), F(8, 100)
VK = F(1_150_000)

reinertrag = [F(0)] + [RE1 * (1 + g) ** (t - 1) for t in range(1, n + 1)]
Z = [-(KP + ENK)] + reinertrag[1:]
Z[n] += VK
afa = [F(0)] + [AFA] * n
ek = [EK0] + [F(0)] * n


def tabelle(rows, titel):
    print(f"\n=== {titel} ===")
    print(" t |   Reinertrag |    Sollzins |    Tilgung |    Abloesung | Habenzins |      BMG |   Steuer |  Geldanl.(+/-) | Fin.saldo |   Guthaben |   Restschuld | Bestandssaldo")
    for r_ in rows:
        t = r_["t"]
        print(f"{t:2d} | {fmt(reinertrag[t]):>12} | {fmt(r_['sollz']):>11} | {fmt(r_['tilg']):>10} | {fmt(r_['abl']):>12} | "
              f"{fmt(r_['habenz']):>9} | {fmt(r_['bmg']):>8} | {fmt(r_['steuer']):>8} | {fmt(r_['anlage']):>14} | {fmt(r_['fin']):>9} | "
              f"{fmt(r_['guth']):>10} | {fmt(r_['rs']):>12} | {fmt(r_['bestand']):>13}")


def kennzahlen(rows, label):
    EW = rows[-1]["bestand"]
    EWO = EK0 * (1 + h * (1 - s)) ** n
    print(f"[{label}] EW = {fmt(EW, 4)}  EW_O = {fmt(EWO, 4)}  dEW = {fmt(EW - EWO, 4)}  "
          f"r_EK = {wurzel(EW / EK0, n) * 100:.4f} %  r_Opp = {wurzel(EWO / EK0, n) * 100:.4f} %")
    return EW, EWO


if __name__ == "__main__":
    print("Annuitaet:", fmt(ANN), " AfA:", fmt(AFA))
    exakt = vofi(n, Z, reinertrag, afa, ek, K0, i, ANN, h, kkz, s)
    tabelle(exakt, "S1 exakt (Rundung nur in der Anzeige)")
    EW, EWO = kennzahlen(exakt, "exakt")
    print("Finanzierungssaldo je Periode null:", all(r_["fin"] == 0 for r_ in exakt))
    print("KK nie beansprucht:", all(r_["kk"] == 0 for r_ in exakt))
    print("Summen: Sollzins", fmt(sum(r_["sollz"] for r_ in exakt)), " Tilgung lfd.", fmt(sum(r_["tilg"] for r_ in exakt)),
          " Abloesung", fmt(sum(r_["abl"] for r_ in exakt)), " Steuer", fmt(sum(r_["steuer"] for r_ in exakt)),
          " Habenzins", fmt(sum(r_["habenz"] for r_ in exakt)))
    # Fortschreibungsprobe Bestandssaldo
    ok = True
    for a, b in zip(exakt[:-1], exakt[1:]):
        d = b["bestand"] - a["bestand"]
        soll = b["Z"] + b["ek"] - b["sollz"] + b["habenz"] - b["steuer"]
        ok &= (d == soll)
    print("Bestandssaldo-Fortschreibung (dB = Z + EK - Sollzins + Habenzins - Steuer) erfuellt:", ok)

    gerundet = vofi(n, Z, [cent(x) for x in reinertrag], afa, ek, K0, i, ANN, h, kkz, s, runden=True)
    # Reinertrag selbst auf Cent gerundet
    Zr = [cent(x) for x in Z]
    gerundet = vofi(n, Zr, [cent(x) for x in reinertrag], afa, ek, K0, i, ANN, h, kkz, s, runden=True)
    tabelle(gerundet, "S1 mit kaufmaennischer Cent-Rundung jeder Zahlung")
    kennzahlen(gerundet, "cent")

    print("\n--- DSCR (Reinertrag / Kapitaldienst) ---")
    for r_ in exakt[1:]:
        kd = r_["sollz"] + r_["tilg"]
        print(f"t={r_['t']}: ohne Abloesung {float(reinertrag[r_['t']] / kd):.4f}   mit Abloesung {float(reinertrag[r_['t']] / (kd + r_['abl'])):.4f}")

    print("\n--- IRR der EK-Zahlungsreihe ---")
    print("EK-Reihe (-400.000, 0,0,0,0, EW):", f"{irr([-EK0, 0, 0, 0, 0, EW]) * 100:.4f} %")
    # 'levered' ohne Wiederanlage: Ueberschuss nach Kapitaldienst und Steuer (ohne Habenzins) wird jaehrlich entnommen
    cf = [-EK0]
    for t in range(1, n + 1):
        r_ = exakt[t]
        st = s * (reinertrag[t] - AFA - r_["sollz"])
        c = reinertrag[t] - r_["sollz"] - r_["tilg"] - st
        if t == n:
            c += VK - r_["abl"]
        cf.append(c)
    print("levered CF bei Vollausschuettung:", [fmt(c) for c in cf], " IRR =", f"{irr(cf) * 100:.4f} %")
    print("unlevered Objekt-CF vor Steuern IRR =", f"{irr(Z) * 100:.4f} %")
    print("Equity Multiple EW/EK =", f"{float(EW / EK0):.4f}")

    # ------------------------------------------------ Befund Entnahmen
    print("\n--- Variante: jaehrliche Entnahme 5.000 (t=1..5) ---")
    entn = [F(0)] + [F(5000)] * n
    ve = vofi(n, Z, reinertrag, afa, ek, K0, i, ANN, h, kkz, s, entnahme=entn)
    EWe = ve[-1]["bestand"]
    q = 1 + h * (1 - s)
    EWO_naiv = EK0 * q ** n
    EWO_korr = EWO_naiv - sum(F(5000) * q ** (n - t) for t in range(1, n + 1))
    print("EW mit Entnahmen:", fmt(EWe), " KK beansprucht:", any(r_["kk"] > 0 for r_ in ve))
    print("dEW nach Formel der Notiz (EW_O = EK*q^n):", fmt(EWe - EWO_naiv), "  r_EK naiv:", f"{wurzel(EWe / EK0, n) * 100:.4f} %")
    print("dEW mit gleichen Entnahmen in der Opportunitaet:", fmt(EWe - EWO_korr))
    # r_EK als Loesung von EK*(1+r)^n = EW + Summe Entnahme*(1+r)^(n-t)  (= IRR der EK-Reihe)
    print("IRR der EK-Reihe mit Entnahmen:", f"{irr([-EK0] + [F(5000)] * (n - 1) + [F(5000) + EWe]) * 100:.4f} %")
    ew_aufgez = EWe + sum(F(5000) * q ** (n - t) for t in range(1, n + 1))
    print("r_EK mit zum Opp.-Satz aufgezinsten Entnahmen:", f"{wurzel(ew_aufgez / EK0, n) * 100:.4f} %")

    # ------------------------------------------------ Befund KK-Zins
    print("\n--- Variante: EK nur 380.000 -> 20.000 Kontokorrent in t=0 ---")
    ek2 = [F(380_000)] + [F(0)] * n
    mit = vofi(n, Z, reinertrag, afa, ek2, K0, i, ANN, h, kkz, s)
    ohne = vofi(n, Z, reinertrag, afa, ek2, K0, i, ANN, h, kkz, s, kk_zins_buchen=False)
    for lab, v in (("KK-Zins gebucht", mit), ("KK-Zins woertlich nach Schritt 4/5 weggelassen", ohne)):
        print(f"{lab}: KK-Staende", [fmt(r_["kk"]) for r_ in v], " KK-Zinsen", [fmt(r_["kkz"]) for r_ in v], " EW", fmt(v[-1]["bestand"]))
    print("Differenz EW:", fmt(ohne[-1]["bestand"] - mit[-1]["bestand"]))

    # ------------------------------------------------ Befund Indexstart
    print("\n--- Variante: 55.000 als Miete_0 gelesen, Jahr 1 = 55.000*1,02 ---")
    re2 = [F(0)] + [RE1 * (1 + g) ** t for t in range(1, n + 1)]
    Z2 = [-(KP + ENK)] + re2[1:]; Z2[n] += VK
    v2 = vofi(n, Z2, re2, afa, ek, K0, i, ANN, h, kkz, s)
    print("EW:", fmt(v2[-1]["bestand"]), " Differenz zu S1:", fmt(v2[-1]["bestand"] - EW),
          " r_EK:", f"{wurzel(v2[-1]['bestand'] / EK0, n) * 100:.4f} %")

    # ------------------------------------------------ Kapitalwert-Konsistenz
    print("\n--- Kapitalwert-Konsistenztest ---")

    def kw_test(i_all, s_, verlust="sofort", s_zins=None, afa_=afa, reinertrag_=reinertrag, Z_=Z, label=""):
        v = vofi(n, Z_, reinertrag_, afa_, ek, K0, i_all, K0 * (i_all + tilg0), i_all, i_all, s_, verlust=verlust, s_zins=s_zins)
        ew = v[-1]["bestand"]
        qs = 1 + i_all * (1 - s_)
        dEW = ew - EK0 * qs ** n
        kw_nach = sum((Z_[t] - s_ * (reinertrag_[t] - afa_[t])) / qs ** t for t in range(n + 1))
        kw_vor_is = sum(Z_[t] / qs ** t for t in range(n + 1))
        print(f"{label}: EW={fmt(ew)}  dEW/q_s^n={fmt(dEW / qs ** n, 4)}  KW(nach Steuern, i_s)={fmt(kw_nach, 4)}  "
              f"Abweichung={fmt(dEW / qs ** n - kw_nach, 4)} | zum Vergleich KW(Vorsteuer-CF, i_s)={fmt(kw_vor_is)}  EW/q_s^n={fmt(ew / qs ** n)}")
        return v

    kw_test(F(4, 100), F(0), label="a) alle Zinsen 4 %, s=0")
    kw_test(F(4, 100), F(30, 100), label="b) alle Zinsen 4 %, s=30 %, sofortiger Verlustausgleich")
    # c) Original S1: Kredit 4 %, Haben 2 %
    qs = 1 + h * (1 - s)
    kw_s1 = sum((Z[t] - s * (reinertrag[t] - afa[t])) / qs ** t for t in range(n + 1))
    print(f"c) Original S1 (Kredit 4 %, Haben 2 %): dEW/q^n={fmt((EW - EWO) / qs ** n)}  KW(nach Steuern, 1,4 %)={fmt(kw_s1)}  Abweichung={fmt((EW - EWO) / qs ** n - kw_s1)}")
    # d) Verlustvortrag statt Sofortausgleich: Reinertrag Jahr 1 und 2 niedrig (Leerstand), damit BMG negativ wird
    re3 = list(reinertrag); re3[1] = F(20_000); re3[2] = F(30_000)
    Z3 = [-(KP + ENK)] + re3[1:]; Z3[n] += VK
    v_s = kw_test(F(4, 100), F(30, 100), reinertrag_=re3, Z_=Z3, label="d1) Anlaufverlust, Sofortausgleich")
    v_v = kw_test(F(4, 100), F(30, 100), verlust="vortrag", reinertrag_=re3, Z_=Z3, label="d2) Anlaufverlust, Verlustvortrag")
    print("    BMG d1:", [fmt(r_["bmg"]) for r_ in v_s], " Steuer d2:", [fmt(r_["steuer"]) for r_ in v_v])
    kw_test(F(4, 100), F(30, 100), s_zins=F(26375, 100000), label="e) Zinsen mit anderem Satz (26,375 %) als Mietueberschuss (30 %)")

    # ------------------------------------------------ GK-Rentabilitaet Lesarten
    print("\n--- VOFI-GK-Rentabilitaet: Lesarten der verbalen Rekonstruktion ---")
    A0 = KP + ENK
    sz = [r_["sollz"] for r_ in exakt]; tg = [r_["tilg"] + r_["abl"] for r_ in exakt]
    a = EW + sum(tg) + sum(x * (1 - s) for x in sz)
    b = EW + sum((tg[t] + sz[t] * (1 - s)) * (1 + h * (1 - s)) ** (n - t) for t in range(n + 1))
    c = EW + K0 * (1 + i * (1 - s)) ** n
    for lab, zaehler in (("(a) Tilgungen + Sollzinsen n.St. unverzinst addiert", a),
                         ("(b) dito, mit Habenzins n.St. auf t=n aufgezinst", b),
                         ("(c) FK mit Sollzins n.St. aufgezinst", c)):
        print(f"{lab}: Zaehler {fmt(zaehler)}  r_GK = {wurzel(zaehler / A0, n) * 100:.4f} %")
    print("Grenzen zur Einordnung: r_EK", f"{wurzel(EW / EK0, n) * 100:.4f} %", " Sollzins n.St.", f"{float(i * (1 - s)) * 100:.2f} %")

    # ------------------------------------------------ Amortisationsdauer, zwei Lesarten
    print("\n--- Amortisationsdauer: zwei Lesarten (ANNAHME Pruefer: Netto-Liquidationserloes linear 1,00 -> 1,15 Mio.) ---")
    for r_ in exakt[1:]:
        t = r_["t"]
        liq = F(1_000_000) + F(150_000) * t / n
        b_t = r_["guth"] + liq - (r_["rs"] if t < n else F(0)) - (F(0) if t < n else liq - VK)
        if t == n:
            b_t = r_["bestand"]
        opp = EK0 * q ** t
        print(f"t={t}: Bestandssaldo inkl. Liquidation {fmt(b_t)}  >= EK 400.000: {b_t >= EK0}   >= EW_O(t) {fmt(opp)}: {b_t >= opp}")

    # ------------------------------------------------ Literatur-Eckwerte
    print("\n--- L1-L4 ---")
    print("L1: 5000*1,025^5 =", f"{5000 * 1.025 ** 5:.4f}", " dEW =", 10079 - 5657, " r_EK =", f"{((10079 / 5000) ** 0.2 - 1) * 100:.4f} %",
          " r_Opp = 2,5 %")
    for nn in (3, 4, 5, 6):
        print(f"L2: n={nn}: r = {((2852.08 / 2100) ** (1 / nn) - 1) * 100:.4f} %")
    print("L3: EK = 0 -> r_EK = (2100/0)^(1/5)-1 nicht definiert; Zins t=1: 0,10*10000 =", 0.10 * 10000)
    print("L3: bei durchgehend 10 % waere der Kapitalwert", f"{2100 / 1.1 ** 5:.2f}", "(nur unter Annahme Soll=Haben=10 %)")
    print("L4: Endwertfaktor je EK-Euro n=5: 1,015^5 =", f"{1.015 ** 5:.5f}", " vs 1,02^5 =", f"{1.02 ** 5:.5f}")
