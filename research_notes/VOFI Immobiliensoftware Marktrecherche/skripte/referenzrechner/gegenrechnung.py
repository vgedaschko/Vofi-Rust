#!/usr/bin/env python3
"""RF-15: Gegenrechnung ausgewaehlter eigener Faelle ohne die Module des Referenzrechners.

Zweck: Die festgeschriebenen Werte der eigenen Faelle (erwartete_werte.json) sollen nicht nur sich selbst
bestaetigen. Dieses Skript rechnet vier Faelle in gerader Linie nach, nur mit decimal und den Rechenregeln des
Dokuments: (1) Testfall im Monatsraster nach Kapitel 2 und R-7.3, (2) Unterlassensalternative mit zwei
Zinssaetzen, (3) Anlaufverlust mit Verlustvortrag und mit sofortiger Verrechnung, (4) Basisfall der
Grobkalkulation Ankauf (Anhang A.3 des Dokuments). Es importiert kein Modul des Referenzrechners; die Sollwerte
liest es selbst aus erwartete_werte.json. Eingaben stehen als Zahlen im Skript, weil es die Regeln nachrechnet
und nicht den Auftrag aufloest.

    python3 gegenrechnung.py        Rueckgabewert 0 nur, wenn alle Werte auf den Cent stimmen

Grenze: Das Skript stammt vom Verfasser des Referenzrechners. Es schuetzt vor Programmierfehlern, nicht vor
einer gemeinsamen falschen Lesart der Regeln; dafuer ist die Blindrechnung durch einen zweiten Bearbeiter
vorgesehen (R-15.2).
"""
import json
import os
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
    """Testfall S1 im Monatsraster: Kontenzins effektiv 2 %, Darlehen nominal 4 % / 12, Abschreibung 17.600 Euro
    und Steuer je Planjahr (R-7.3, R-2.7)."""
    h = monatssatz(D("0.02"))
    rest, guth = D(700000), D(0)
    rate = c(D(700000) * D("0.06") / 12)
    steuer1 = guth1 = None
    for jahr in range(1, 6):
        miete = c(D(55000) * D("1.02") ** (jahr - 1) / 12)
        bmg = D(0)
        for m in range(1, 13):
            zins = c(rest * D("0.04") / 12)
            hz = c(guth * h)
            rest -= rate - zins
            guth += miete - rate + hz
            bmg += miete - zins + hz
        steuer = c(D("0.30") * (bmg - D(17600)))
        guth -= steuer
        if jahr == 1:
            steuer1, guth1 = steuer, guth
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
    return endwert, lang + kurz, rest, steuer1, guth1


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
    """Grobkalkulation Ankauf, Basisfall (Anhang A.3): Kaufpreis 2,4 Mio. Euro, zwoelf Jahre, Monatsraster."""
    n, flaeche = 12, D(1320)
    idx = [None, D(1)]
    for j in range(2, n + 2):
        idx.append(s12(idx[-1] * D("1.02")))
    # R-6.3: Bestandsmiete nach BGB-558. Ziel ist der Anpassungspfad zur Vergleichsmiete 9,20 Euro (+2 % je Jahr,
    # Anpassung ueber vier Jahre); Wartefrist 15 Monate, Kappung 15 % gegen die Miete 36 Monate zuvor; im
    # Planjahr 1 keine Erhoehung; Mietenhistorie unbekannt: letzte Erhoehung zum Stichtag, kein Kappungsspielraum
    # gegen Mieten vor dem Stichtag (MA-037).
    miete, laufend, letzte = {}, D("8.50"), 0
    for m in range(1, 12 * (n + 1) + 1):
        j = (m - 1) // 12 + 1
        vergleich = D("9.20") * idx[j]
        ziel = D("8.50") + (vergleich - D("8.50")) * min(j - 1, 4) / 4
        if m >= 13 and ziel > laufend and m - 1 >= letzte + 15:
            grenze = miete[m - 36] * D("1.15") if m - 36 >= 1 else D("8.50")
            if min(ziel, grenze) > laufend:
                laufend, letzte = min(ziel, grenze), m - 1
        miete[m] = laufend
    soll = {m: c(flaeche * miete[m]) for m in miete}                   # R-6.4
    ein = {m: c(soll[m] * (1 - D("0.015") - D("0.005"))) for m in miete}   # Leerstand 1,5 %, Forderungsausfall 0,5 %
    idx_co2 = [None, D(1)]
    for j in range(2, n + 1):
        idx_co2.append(s12(idx_co2[-1] * D("1.05")))
    # R-6.8, R-6.9: Verwaltung 350 je Einheit, Instandhaltung 14 Euro (Gebaeudealter ab 32 Jahren), Betriebskosten
    # 2 Euro; CO2: 30 kg x 40 % x 50 Euro je Tonne
    kosten = {j: c((350 * 20 + 14 * flaeche + 2 * flaeche) * idx[j] / 12)
              + c(D(30) * flaeche * D("0.4") * 50 * idx_co2[j] / 1000 / 12) for j in range(1, n + 1)}
    reinertrag1 = sum(ein[m] for m in range(1, 13)) - 12 * kosten[1]
    # R-5.12: nachhaltiger Ertrag (Ist-Miete unter der Vergleichsmiete; Bewirtschaftung und Ausfall ueber 15 %),
    # kalkulatorischer Zins = Anschlusszins 5 %, Tilgung 2 %
    roh = sum(soll[m] for m in range(1, 13))
    abzug = max(12 * kosten[1] + roh - sum(ein[m] for m in range(1, 13)), c(D("0.15") * roh))
    tragbar = (roh - abzug) / D("1.2")
    b = (tragbar / D("0.07")).quantize(C, ROUND_FLOOR)
    while 12 * c(b * D("0.07") / 12) > tragbar:
        b -= C
    preis, enk = D(2400000), D(240000)
    darlehen = min(D("0.65") * preis, b, preis + enk)
    ek = preis + enk - darlehen
    # Finanzplan
    h = monatssatz(D("0.02"))
    rest, guth = darlehen, D(0)
    rate = c(darlehen * D("0.06") / 12)
    afa = c((preis + enk) * D("0.75") * D("0.02"))
    stau = c(D(120000) * D("1.03") ** 2)
    assert stau / D("1.19") <= D("0.15") * (preis + enk) * D("0.75")      # R-6.16: keine Aktivierung
    zustand = dict(kst=D(0), gew=D(0))
    einlagen = {0: ek}
    for j in range(1, n + 1):
        ergebnis, hz_jahr, entgelte = D(0), D(0), D(0)
        for mm in range(1, 13):
            u = (j - 1) * 12 + mm
            satz = D("0.04") if u <= 120 else D("0.05")
            if u == 121:
                rate = c(rest * (D("0.05") + D("0.02")) / 12)
            zins = c(rest * satz / 12)
            hz = c(guth * h)
            rest -= rate - zins
            aus = stau if u == 24 else D(0)
            ergebnis += ein[u] - kosten[j] - zins - aus
            entgelte += zins
            hz_jahr += hz
            fluss = ein[u] - kosten[j] - rate + hz - aus
            if mm == 12:
                gewinn = D(0)
                if j == n:
                    # R-8.1: Faktor auf die Jahresmiete zum Stand des Verkaufsstichtags nach strukturellem Leerstand
                    vk = c(18 * (12 * soll[12 * n] * (1 - D("0.015"))))
                    vk_kosten = c(vk * D("0.015"))
                    gewinn = vk - vk_kosten - ((preis + enk) - n * afa)
                    fluss += vk - vk_kosten - rest
                assert entgelte <= 200000                               # R-7.16: keine Hinzurechnung
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
        for mm in range(1, 13):
            u = (j - 1) * 12 + mm
            z = c(lang * h) + c(kurz * h)
            zj += z
            kurz += z
            lang += einlagen.get(u, D(0))
            if mm == 12:
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
                nachschuss=sum(v for u, v in einlagen.items() if u > 0), reinertrag=reinertrag1, verkaufspreis=vk)


def alle(ausgabe=print):
    """Rechnet die vier Faelle und vergleicht mit den festgeschriebenen Werten. Rueckgabe: Liste von
    (Kennung, Name, bestanden, Ist, Soll, Toleranz)."""
    datei = os.path.join(os.path.dirname(os.path.abspath(__file__)), "erwartete_werte.json")
    fest = json.load(open(datei, encoding="utf-8"))
    k = "RF-15"
    erg = []

    def pruefe(name, ist, soll, toleranz="0"):
        ok = soll is not None and abs(ist - D(str(soll))) <= D(toleranz)
        erg.append((k, name, ok, ist, soll, D(toleranz)))
        ausgabe(f"  {'ok ' if ok else 'ABW'} {name:<62} Ist {ist:>22.4f}  Soll {str(soll):>18}  Tol. {toleranz}")

    ausgabe(f"\n{k}  Gegenrechnung ohne die Module des Referenzrechners (gegenrechnung.py)")
    ew, alt, rest, steuer1, guth1 = testfall_monat()
    pruefe("Testfall im Monatsraster: Endwert", ew, fest.get("RF-06|Monatsraster nach Kapitel 2 (Kontenzins effektiv, Rundung je Zahlung): Endwert"))
    pruefe("Testfall im Monatsraster: Endwert wie in der Rechnung des Finanzmathematikers (Pruefrunde 1)", ew, "585918.65")
    pruefe("Testfall im Monatsraster: Steuer im ersten Jahr", steuer1, "2933.48")
    pruefe("Testfall im Monatsraster: Guthaben am Ende des ersten Jahres", guth1, "10185.23")
    pruefe("Testfall im Monatsraster: Unterlassensalternative", alt, fest.get("RF-06|Monatsraster nach Kapitel 2: Endwert der Unterlassensalternative"))
    pruefe("Testfall im Monatsraster: Abloesung", rest, fest.get("RF-06|Monatsraster nach Kapitel 2: Abloesung"))
    pruefe("Unterlassensalternative mit zwei Zinssaetzen (3 % und 2 %)", alternative_zwei_saetze(), "443192.58", "0.005")
    for vortrag, name in ((True, "Vortrag im Vorhaben (Voreinstellung MA-016)"), (False, "sofortige Verrechnung (andere Lesart)")):
        ew, steuern, vv = anlaufverlust(vortrag)
        pruefe(f"Anlaufverlust, {name}: Endwert", ew, fest.get(f"RF-10|Anlaufverlust, {name}: Endwert"))
    e = ankauf_basisfall()
    pruefe("Ankauf Basisfall: Reinertrag im ersten Jahr", e["reinertrag"], fest.get("RF-11|Basisfall: Reinertrag im ersten Jahr"))
    pruefe("Ankauf Basisfall: Bankdarlehen", e["darlehen"], fest.get("RF-11|Basisfall: Bankdarlehen"))
    pruefe("Ankauf Basisfall: Verkaufspreis", e["verkaufspreis"], fest.get("RF-11|Basisfall: Verkaufspreis"))
    pruefe("Ankauf Basisfall: laufender Nachschussbedarf", e["nachschuss"], fest.get("RF-11|Basisfall: laufender Nachschussbedarf nach der Investitionsphase"))
    pruefe("Ankauf Basisfall: Endwert", e["endwert"], fest.get("RF-11|Basisfall: Endwert"))
    pruefe("Ankauf Basisfall: Endwert der Unterlassensalternative", e["alternative"], fest.get("RF-11|Basisfall: Endwert der Unterlassensalternative"))
    pruefe("Ankauf Basisfall: VOFI-Rendite (%)", e["rendite"] * 100, fest.get("RF-11|Basisfall: VOFI-Rendite (%)"), "0.0005")
    return erg


if __name__ == "__main__":
    ergebnis = alle()
    abw = [x for x in ergebnis if not x[2]]
    print(f"\nGegenrechnung: {len(ergebnis)} Pruefungen; {len(ergebnis) - len(abw)} bestanden, {len(abw)} abweichend.")
    raise SystemExit(0 if not abw else 1)
