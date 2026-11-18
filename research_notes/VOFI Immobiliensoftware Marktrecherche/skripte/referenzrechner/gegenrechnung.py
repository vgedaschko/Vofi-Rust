"""RF-15: Gegenrechnung ausgewaehlter eigener Faelle ohne die Module des Referenzrechners.

Zweck: Die festgeschriebenen Werte der eigenen Faelle (erwartete_werte.json) sollen nicht nur sich selbst
bestaetigen. Dieses Skript rechnet vier Faelle in gerader Linie nach, nur mit decimal und den Rechenregeln des
Dokuments: (1) Testfall im Monatsraster nach Kapitel 2, (2) Unterlassensalternative mit zwei Zinssaetzen,
(3) Anlaufverlust mit Verlustvortrag und mit sofortiger Verrechnung, (4) Basisfall der Grobkalkulation Ankauf.
Es importiert aus dem Referenzrechner nichts ausser dem Pruefrahmen fuer die Ausgabe.
"""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP, ROUND_FLOOR

getcontext().prec = 60
C = D("0.01")


def c(x):
    return x.quantize(C, ROUND_HALF_UP)


def s12(x):
    return x.quantize(D("1E-12"), ROUND_HALF_UP)


def monatssatz(i):
    return s12((1 + i) ** (D(1) / 12) - 1)


def testfall_monat():
    """Testfall S1 im Monatsraster: Kontenzins effektiv 2 %, Darlehen nominal 4 % / 12, Steuer je Planjahr."""
    h = monatssatz(D("0.02"))
    rest, guth = D(700000), D(0)
    rate = c(D(700000) * D("0.06") / 12)
    for jahr in range(1, 6):
        miete = c(D(55000) * D("1.02") ** (jahr - 1) / 12)
        bmg = D(0)
        for m in range(1, 13):
            zins = c(rest * D("0.04") / 12)
            hz = c(guth * h)
            rest -= rate - zins
            guth += miete - rate + hz
            bmg += miete - zins + hz
        steuer = c(D("0.30") * (bmg - c(D(17600) / 12) * 12))
        guth -= steuer
    endwert = guth + 1150000 - rest
    # Unterlassensalternative: 400.000 langfristig, Zinsen monatlich auf das Wiederanlagekonto, beide 2 %
    lang, kurz = D(400000), D(0)
    for jahr in range(1, 6):
        zj = D(0)
        for m in range(1, 13):
            z = c(lang * h) + c(kurz * h)
            kurz += z
            zj += z
        kurz -= c(D("0.30") * zj)
    return endwert, lang + kurz, rest


def alternative_zwei_saetze():
    """400.000 zu 3 % langfristig, Wiederanlage zu 2 %, Steuer 30 %, fuenf Jahre, Jahresmodus, ungerundet."""
    lang, kurz = D(400000), D(0)
    for jahr in range(1, 6):
        zinsen = lang * D("0.03") + kurz * D("0.02")
        kurz += zinsen * D("0.7")
    return lang + kurz


def anlaufverlust(vortrag):
    """Testfall mit Reinertrag 20.000 und 30.000 in den ersten beiden Jahren; Kontokorrent 8 %, Guthaben 2 %."""
    re = [D(20000), D(30000)] + [c(D(55000) * D("1.02") ** t) for t in (2, 3, 4)]
    rest, guth, kk, vv = D(700000), D(0), D(0), D(0)
    steuern = []
    for t in range(5):
        zins = c(rest * D("0.04"))
        hz, kz = c(guth * D("0.02")), c(kk * D("0.08"))
        bmg = re[t] - 17600 - zins - kz + hz
        if vortrag:
            if bmg < 0:
                vv, steuer = vv - bmg, D(0)
            else:
                nutz = min(vv, bmg)
                vv, steuer = vv - nutz, c(D("0.30") * (bmg - nutz))
        else:
            steuer = c(D("0.30") * bmg)
        steuern.append(steuer)
        rest -= 42000 - zins
        netto = guth - kk + re[t] - 42000 + hz - kz - steuer
        if t == 4:
            netto += 1150000 - rest
        guth, kk = (netto, D(0)) if netto >= 0 else (D(0), -netto)
    return guth - kk, steuern, vv


def kst(jahr):
    return {2027: D("0.15"), 2028: D("0.14"), 2029: D("0.13"), 2030: D("0.12"), 2031: D("0.11")}.get(jahr, D("0.10"))


def steuer_koerperschaft(jahr, einkommen, zustand):
    """Koerperschaftsteuer mit Zuschlag und Gewerbesteuer (Hebesatz 400 % als Annahme), je eigener Verlustvortrag."""
    summe = D(0)
    for topf in ("kst", "gew"):
        vv = zustand[topf]
        if einkommen < 0:
            zustand[topf], basis = vv - einkommen, D(0)
        else:
            nutz = min(vv, einkommen)
            zustand[topf], basis = vv - nutz, einkommen - nutz
        if topf == "kst":
            summe += c(kst(jahr) * D("1.055") * basis)
        else:
            summe += c((basis / 100).to_integral_value(ROUND_FLOOR) * 100 * D("0.035") * 4)
    return summe


def ankauf_basisfall():
    """Grobkalkulation Ankauf, Basisfall (annahmen.py): Kaufpreis 2,4 Mio., zwoelf Jahre, Monatsraster."""
    n, flaeche = 12, D(1320)
    # Mietpfad: Ist 8,50, Markt 9,20 (+2 % je Jahr), Anpassung ueber vier Jahre, Kappung 15 % in drei Jahren
    idx = [None, D(1)]
    for j in range(2, n + 2):
        idx.append(s12(idx[-1] * D("1.02")))
    miete = {}
    for j in range(1, n + 2):
        markt = D("9.20") * idx[j]
        m = D("8.50") + (markt - D("8.50")) * min(D(1), D(j - 1) / 4)
        basis = miete[j - 3] if j - 3 >= 1 else D("8.50")
        miete[j] = min(m, basis * D("1.15"))
    soll = {j: c(flaeche * miete[j]) for j in miete}
    ein = {j: c(soll[j] * D("0.98")) for j in miete}
    idx_co2 = [None, D(1)]
    for j in range(2, n + 1):
        idx_co2.append(s12(idx_co2[-1] * D("1.05")))
    kosten = {j: c((350 * 20 + 14 * flaeche + 2 * flaeche) * idx[j] / 12) + c(D("0.60") * flaeche * idx_co2[j] / 12)
              for j in range(1, n + 1)}
    reinertrag1 = 12 * (ein[1] - kosten[1])
    # Bankdarlehen: kleinster Wert aus Beleihungsquote, Mindestdeckung, Restfinanzierung
    preis, enk = D(2400000), D(240000)
    tragbar = reinertrag1 / D("1.2")
    b = (tragbar / D("0.06")).quantize(C, ROUND_FLOOR)
    while 12 * c(b * D("0.06") / 12) > tragbar:
        b -= C
    darlehen = min(D("0.65") * preis, b, preis + enk)
    ek = preis + enk - darlehen
    # Finanzplan
    h = monatssatz(D("0.02"))
    rest, guth = darlehen, D(0)
    rate = c(darlehen * D("0.06") / 12)
    afa = c((preis + enk) * D("0.75") * D("0.02"))
    stau = c(D(120000) * D("1.03") ** 2)
    zustand = dict(kst=D(0), gew=D(0))
    einlagen = {0: ek}
    for j in range(1, n + 1):
        ergebnis, hz_jahr = D(0), D(0)
        for m in range(1, 13):
            u = (j - 1) * 12 + m
            satz = D("0.04") if u <= 120 else D("0.05")
            if u == 121:
                rate = c(rest * (D("0.05") + D("0.02")) / 12)
            zins = c(rest * satz / 12)
            hz = c(guth * h)
            rest -= rate - zins
            aus = stau if u == 24 else D(0)
            ergebnis += ein[j] - kosten[j] - zins - aus
            hz_jahr += hz
            fluss = ein[j] - kosten[j] - rate + hz - aus
            if m == 12:
                gewinn = D(0)
                if j == n:
                    vk = c(18 * 12 * soll[n + 1])
                    vk_kosten = c(vk * D("0.015"))
                    gewinn = vk - vk_kosten - ((preis + enk) - n * afa)
                    fluss += vk - vk_kosten - rest
                fluss -= steuer_koerperschaft(2026 + j, ergebnis - afa + hz_jahr + gewinn, zustand)
            guth += fluss
            if guth < 0:                      # Kontokorrentlinie null: Nachschuss aus Eigenkapital
                einlagen[u] = -guth
                guth = D(0)
    endwert = guth
    # Unterlassensalternative mit derselben Einlagenreihe, beide Saetze 2 %
    lang, kurz = D(0), D(0)
    zustand = dict(kst=D(0), gew=D(0))
    lang += einlagen.get(0, D(0))
    for j in range(1, n + 1):
        zj = D(0)
        for m in range(1, 13):
            u = (j - 1) * 12 + m
            z = c(lang * h) + c(kurz * h)
            zj += z
            kurz += z
            lang += einlagen.get(u, D(0))
            if m == 12:
                kurz -= steuer_koerperschaft(2026 + j, zj, zustand)
    alt = lang + kurz
    # VOFI-Rendite: Einlagen mit dem Habenzins nach Steuern auf den Beginn abgezinst
    w = {12 * n: D(1)}
    for u in range(12 * n, 0, -1):
        j = (u - 1) // 12 + 1
        sz = kst(2026 + j) * D("1.055") + D("0.14")
        w[u - 1] = w[u] * s12((1 + D("0.02") * (1 - sz)) ** (D(1) / 12))
    nenner = sum(v * w[u] for u, v in einlagen.items()) / w[0]
    rendite = (endwert / nenner) ** (D(1) / n) - 1
    return dict(darlehen=darlehen, eigenkapital=ek, endwert=endwert, alternative=alt, rendite=rendite,
                nachschuss=sum(v for u, v in einlagen.items() if u > 0), reinertrag=reinertrag1)


def alle():
    from rf_rahmen import fall, pruefe, pruefe_gleich, FEST

    def fest(schluessel):
        return FEST.get(schluessel, "0")

    k = fall("RF-15", "Gegenrechnung ohne die Module des Referenzrechners (gegenrechnung.py)")
    ew, alt, rest = testfall_monat()
    pruefe(k, "Testfall im Monatsraster: Endwert", ew, fest("RF-06|Monatsraster nach Kapitel 2 (Kontenzins effektiv, Rundung je Zahlung): Endwert"), "0")
    pruefe(k, "Testfall im Monatsraster: Unterlassensalternative", alt, fest("RF-06|Monatsraster nach Kapitel 2: Endwert der Unterlassensalternative"), "0")
    pruefe(k, "Testfall im Monatsraster: Abloesung", rest, fest("RF-06|Monatsraster nach Kapitel 2: Abloesung"), "0")
    pruefe(k, "Unterlassensalternative mit zwei Zinssaetzen (3 % und 2 %)", alternative_zwei_saetze(), "443192.58")
    for vortrag, name in ((True, "Vortrag im Vorhaben (Voreinstellung MA-016)"), (False, "sofortige Verrechnung (andere Lesart)")):
        ew, steuern, vv = anlaufverlust(vortrag)
        pruefe(k, f"Anlaufverlust, {name}: Endwert", ew, fest(f"RF-10|Anlaufverlust, {name}: Endwert"), "0")
    e = ankauf_basisfall()
    pruefe(k, "Ankauf Basisfall: Reinertrag im ersten Jahr", e["reinertrag"], fest("RF-11|Basisfall: Reinertrag im ersten Jahr"), "0")
    pruefe(k, "Ankauf Basisfall: Bankdarlehen", e["darlehen"], fest("RF-11|Basisfall: Bankdarlehen"), "0")
    pruefe(k, "Ankauf Basisfall: Nachschussbedarf", e["nachschuss"], fest("RF-11|Basisfall: Nachschussbedarf nach der Investitionsphase"), "0")
    pruefe(k, "Ankauf Basisfall: Endwert", e["endwert"], fest("RF-11|Basisfall: Endwert"), "0")
    pruefe(k, "Ankauf Basisfall: Endwert der Unterlassensalternative", e["alternative"], fest("RF-11|Basisfall: Endwert der Unterlassensalternative"), "0")
    pruefe(k, "Ankauf Basisfall: VOFI-Rendite (%)", e["rendite"] * 100, fest("RF-11|Basisfall: VOFI-Rendite (%)"), "0.0005", 3)


if __name__ == "__main__":
    import rf_rahmen
    alle()
    raise SystemExit(rf_rahmen.zusammenfassung())
