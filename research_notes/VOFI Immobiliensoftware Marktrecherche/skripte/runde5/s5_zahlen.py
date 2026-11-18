#!/usr/bin/env python3
"""Schlussredaktion des Rechercheberichts (Sichtung Runde 5): Nachrechnung jeder
neuen oder geaenderten Zahl. Exakt mit Bruechen; Ausgabe mit den Stellen des Berichts.

    python3 s5_zahlen.py

Jeder Block nennt den Sichtungspunkt und die Fundstelle. Schlaegt eine Pruefung fehl,
bricht das Skript mit AssertionError ab. Der Testfall (A.6) ist hier eigenstaendig
nachgebaut, nicht aus den frueheren Skripten uebernommen.
"""
from fractions import Fraction as F


def de(x, nd=2):
    s = f"{float(x):,.{nd}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def titel(t):
    print("\n== " + t)


def wurzel(x, n):
    return float(x) ** (1.0 / n) - 1.0


# ---------------------------------------------------------------------------
titel("Punkt 8 | B.3 Gewerbesteuer und Anrechnung nach § 35 EStG: Freibetrag § 11 Abs. 1 GewStG")
gewerbeertrag = F(100000)
freibetrag = F(24500)
messzahl = F(35, 1000)
messbetrag = (gewerbeertrag - freibetrag) * messzahl
print("Messbetrag nach Freibetrag", de(messbetrag), "| ohne Freibetrag (alter Wortlaut)", de(gewerbeertrag * messzahl))
assert messbetrag == F(264250, 100)
for hebesatz, gewst_soll, erm_soll in ((F(4), 10570, 10570), (F(28, 10), 7399, 7399)):
    gewst = messbetrag * hebesatz
    ermaessigung = min(4 * messbetrag, gewst)   # Vierfaches des Messbetrags, hoechstens die Gewerbesteuer
    print(f"Hebesatz {de(hebesatz * 100, 0)} %: Gewerbesteuer", de(gewst), "| Ermaessigung", de(ermaessigung))
    assert gewst == gewst_soll and ermaessigung == erm_soll
punkte = 4 * messbetrag / gewerbeertrag * 100
print("Ermaessigung in Prozentpunkten des Gewerbeertrags, hoechstens", de(punkte, 2))
assert punkte == F(1057, 100)
# ueber 400 % bleibt es beim Vierfachen des Messbetrags
assert min(4 * messbetrag, messbetrag * F(48, 10)) == 10570

# Koerperschaft (unveraendert, zur Abgrenzung): kein Freibetrag in der Rechnung des Berichts
kst = F(15, 100) * F(1055, 1000)
print("Koerperschaft 2026 bei 400 %: ohne Kuerzung", de((kst + messzahl * 4) * 100, 3), "% | mit", de(kst * 100, 3), "%")
assert round(float(kst + messzahl * 4) * 100, 1) == 29.8 and round(float(kst) * 100, 1) == 15.8

# ---------------------------------------------------------------------------
titel("Punkte 1 und 2 | D.4 Darlehen: Bankdarlehen = kleinster Wert aus (a), (b), (c), nie negativ")


def bankdarlehen(wertansatz, quote, reinertrag, dscr_min, kd_satz, mittelbedarf,
                 uebrige_darlehen=F(0), kd_uebrige=F(0), zuschuesse=F(0), ek_min=F(0), nur_eigenes=False):
    """(a) Quote * Wertansatz abzueglich uebriger Darlehen; (b) Darlehen aus Mindestdeckung
    gegen den Kapitaldienst aller Darlehen; (c) Restfinanzierung. nur_eigenes = andere Lesart
    von MA-026: Quote und Deckung nur fuer das eigene Darlehen der Bank."""
    a = quote * wertansatz - (F(0) if nur_eigenes else uebrige_darlehen)
    b = (reinertrag / dscr_min - (F(0) if nur_eigenes else kd_uebrige)) / kd_satz
    c = mittelbedarf - uebrige_darlehen - zuschuesse - ek_min
    darlehen = max(F(0), min(a, b, c))
    ek = mittelbedarf - uebrige_darlehen - zuschuesse - darlehen
    return a, b, c, darlehen, ek


# Beispiel Ankauf mit uebernommenem Foerderdarlehen (Werte des Fachexperten, Runde 5, Befund 1)
kaufpreis, enk = F(2000000), F(200000)
uebernommen, kd_ueb = F(1000000), F(25000)
a, b, c, darl, ek = bankdarlehen(kaufpreis, F(65, 100), F(140000), F(12, 10), F(6, 100), kaufpreis + enk,
                                 uebrige_darlehen=uebernommen, kd_uebrige=kd_ueb)
print("Ankauf neu: (a)", de(a), "(b)", de(b), "(c)", de(c), "-> Bankdarlehen", de(darl), "| Eigenkapital", de(ek))
assert a == 300000 and c == 1200000 and darl == 300000 and ek == 900000
# alter Wortlaut: Quote auf den Kaufpreis ohne Abzug, keine Restfinanzierung
alt = min(F(65, 100) * kaufpreis, (F(140000) / F(12, 10) - kd_ueb) / F(6, 100))
print("Ankauf alt: Bankdarlehen", de(alt), "| Darlehen zusammen", de(alt + uebernommen),
      "| Mittelbedarf", de(kaufpreis + enk), "| Eigenkapital", de(kaufpreis + enk - alt - uebernommen))
assert alt == 1300000 and kaufpreis + enk - alt - uebernommen == -100000
# andere Lesart von MA-026 mit Restfinanzierung
a2, b2, c2, darl2, ek2 = bankdarlehen(kaufpreis, F(65, 100), F(140000), F(12, 10), F(6, 100), kaufpreis + enk,
                                      uebrige_darlehen=uebernommen, kd_uebrige=kd_ueb, nur_eigenes=True)
print("Ankauf, andere Lesart: Bankdarlehen", de(darl2), "| Eigenkapital", de(ek2))
assert darl2 == 1200000 and ek2 == 0

# Beispiel gefoerderter Neubau (D.4): 10 Mio. Gesamtkosten, 9 Mio. zuwendungsfaehig, Gruppe B
gk, zf = F(10000000), F(9000000)
fd, zuschuss, ek_min = zf * F(60, 100), zf * F(20, 100), zf * F(20, 100)
rest = gk - fd - zuschuss - ek_min
print("Neubau: Foerderdarlehen", de(fd), "| Zuschuss", de(zuschuss), "| Mindesteigenkapital", de(ek_min), "| Restfinanzierung (c)", de(rest))
assert (fd, zuschuss, ek_min, rest) == (5400000, 1800000, 1800000, 1000000)
for quote, a_soll in ((F(65, 100), 1100000), (F(60, 100), 600000)):
    a_n = quote * gk - fd
    print(f"  Beleihungsquote {de(quote * 100, 0)} %: (a) = {de(quote * gk)} - {de(fd)} = {de(a_n)};",
          "es gilt", de(min(a_n, rest)), "| Eigenkapital", de(gk - fd - zuschuss - min(a_n, rest)))
    assert a_n == a_soll
assert gk - fd - zuschuss - F(600000) == 2200000
# Kapitaldienst des Foerderdarlehens im ersten Jahr: Tilgung ueber 42 Jahre (MA-002), Verwaltungskostenbeitrag 0,5 %
tilgung_fd = fd / 42
vkb = fd * F(5, 1000)
kd_fd = tilgung_fd + vkb
schwelle = kd_fd * F(12, 10)
print("Kapitaldienst Foerderdarlehen", de(tilgung_fd), "+", de(vkb), "=", de(kd_fd),
      "| Reinertrag, ab dem bei Mindestdeckung 1,2 etwas fuer die Bank bleibt", de(schwelle))
assert round(float(kd_fd)) == 155571 and round(float(schwelle)) == 186686
# unter der Schwelle: Bankdarlehen null, Eigenkapital traegt die Restfinanzierung mit
_, b_n, _, darl_n, ek_n = bankdarlehen(gk, F(65, 100), F(180000), F(12, 10), F(6, 100), gk,
                                       uebrige_darlehen=fd, kd_uebrige=kd_fd, zuschuesse=zuschuss, ek_min=ek_min)
print("  Reinertrag 180.000: (b)", de(b_n), "-> Bankdarlehen", de(darl_n), "| Eigenkapital", de(ek_n))
assert b_n < 0 and darl_n == 0 and ek_n == 2800000
# andere Lesart von MA-026 (nur das eigene Darlehen zaehlt), Quote 60 %, Bankkonditionen 6 % wie im Beispiel der Kreditkennzahlen
_, _, _, darl_o, ek_o = bankdarlehen(gk, F(60, 100), F(180000), F(12, 10), F(6, 100), gk, uebrige_darlehen=fd,
                                     kd_uebrige=kd_fd, zuschuesse=zuschuss, ek_min=ek_min, nur_eigenes=True)
print("  andere Lesart: Bankdarlehen", de(darl_o), "| Eigenkapital", de(ek_o),
      "| Unterschied der Lesarten im Eigenkapital", de(ek_n - ek_o),
      "| Reinertrag, der 1,0 Mio. Bankdarlehen allein mit Mindestdeckung traegt", de(rest * F(6, 100) * F(12, 10)))
assert darl_o == 1000000 and ek_o == 1800000 and ek_n - ek_o == 1000000
# einbehaltene Entgelte der NBank (C.1): 1 % des Darlehens, 0,75 % des Zuschusses
entgelt = fd * F(1, 100) + zuschuss * F(75, 10000)
print("Einbehaltene Entgelte der NBank", de(entgelt), "| in % der zuwendungsfaehigen Kosten", de(entgelt / zf * 100, 3))
assert entgelt == 67500

# ---------------------------------------------------------------------------
titel("Punkt 5 | Abschnitt 5: Wirkung einer um einen Prozentpunkt niedrigeren Tilgung (Beispiel D.4)")
sd_tragbar = F(134640) * F(80, 100) / F(12, 10)
print("tragbarer Schuldendienst", de(sd_tragbar), "| Darlehen bei 6 %", de(sd_tragbar / F(6, 100)), "| bei 5 %", de(sd_tragbar / F(5, 100)))
assert sd_tragbar == 89760 and sd_tragbar / F(6, 100) == 1496000 and sd_tragbar / F(5, 100) == 1795200

# ---------------------------------------------------------------------------
titel("Punkt 5 und 10 | D.1 Zahl der Eingaben der Grobkalkulation nach Umstellung")
ankauf = ["Kaufpreis", "Erwerbsnebenkosten", "Bodenanteil", "Wohnflaeche", "Zahl der Einheiten", "Ist-Miete", "Marktmiete", "Baujahr"]
neubau = ["Grundstueckspreis", "Grundstuecksflaeche", "Brutto-Grundflaeche", "Wohnflaeche", "Zahl der Einheiten", "Kostenkennwert", "Bauzeit", "Miete"]
foerderung = ["Mietenstufe", "Einkommensgruppe", "Bodenrichtwert"]
beide = ["Steuerstatus", "Kennzeichen oder Steuersatz", "Zins", "Zinsbindung", "Restwertfaktor", "Haltedauer"]
pauschalen = 6   # wie bisher: 22 - 16
# Beleihungsquote und Tilgung zaehlen nicht mehr: Voreinstellung aus den Vorgaben des Hauses
n_ankauf, n_neubau = len(ankauf) + len(beide), len(neubau) + len(beide)
print("Ankauf", n_ankauf, "| mit Pauschalen", n_ankauf + pauschalen, "| Neubau", n_neubau, "| mit Grobfoerderung", n_neubau + len(foerderung),
      "| gewerbliche Personengesellschaft und Einzelunternehmen je eine mehr (Kennzeichen und Steuersatz)")
assert (n_ankauf, n_ankauf + pauschalen, n_neubau, n_neubau + len(foerderung)) == (14, 20, 14, 17)

# ---------------------------------------------------------------------------
titel("Punkt 18 | A.1 Nr. 3: Kontrollsumme des Investitionsstaus bei teilweise ausgefuehrter Massnahme")
massnahme, index = F(100000), F(103, 100)
gezahlt = F(40, 100) * massnahme * index ** 9      # 40 % in Jahr 9 ausgefuehrt
abgezogen = F(60, 100) * massnahme * index ** 10   # 60 % stehen am Stichtag Jahr 10 aus
print("gezahlt", de(gezahlt), "| abgezogen", de(abgezogen), "| Summe in Euro", de(gezahlt + abgezogen),
      "| Stichtag", de(massnahme * index ** 10), "| Planjahr 12", de(massnahme * index ** 12))
assert round(float(gezahlt)) == 52191 and round(float(abgezogen)) == 80635 and round(float(gezahlt + abgezogen)) == 132826
assert round(float(massnahme * index ** 10)) == 134392 and round(float(massnahme * index ** 12)) == 142576
assert F(40, 100) + F(60, 100) == 1   # die Probe schliesst in Anteilen

# ---------------------------------------------------------------------------
titel("Punkt 20 | B.4 und Quellnotiz 10: II. BV, Betraege ab 01.01.2026")
paare = ((F(37246, 100), F(230)), (F(1150, 100), F(710, 100)), (F(1458, 100), F(9)), (F(1862, 100), F(1150, 100)))
faktoren = [neu / basis for neu, basis in paare]
print("Faktoren der Sekundaerwerte auf die Betraege der Verordnung:", ", ".join(de(f, 4) for f in faktoren))
assert all(round(float(f), 2) == 1.62 for f in faktoren)
vpi = {2001: F(771, 10), 2022: F(1135, 10), 2025: F(1230, 10)}
f_index = vpi[2025] / vpi[2001]
eigen = 230 * f_index
abw = F(37246, 100) / eigen - 1
print("Index Okt. 2025 / Okt. 2001", de(f_index, 4), "| eigene Rechnung", de(eigen), "| Abweichung der Sekundaerquelle", de(abw * 100, 2), "%")
assert round(float(f_index), 4) == 1.5953 and round(float(eigen), 2) == 366.93 and round(float(abw) * 100, 1) == 1.5
letzter = vpi[2025] / vpi[2022]
print("letzter Schritt Okt. 2022 -> Okt. 2025", de((letzter - 1) * 100, 2), "% | Sekundaerwert zurueckgerechnet auf 2023",
      de(F(37246, 100) / letzter), "| heutige Reihe fuer 2023", de(230 * vpi[2022] / vpi[2001]))
assert round(float(letzter - 1) * 100, 2) == 8.37
assert round(float(F(37246, 100) / letzter), 2) == 343.69 and round(float(230 * vpi[2022] / vpi[2001]), 2) == 338.59
print("ImmoWertV-Probe 2021, Eigentumswohnung: 357 gegen 356,32 =", de((F(357) / F(35632, 100) - 1) * 100, 2), "%",
      "| acht Kettenschritte mit je hoechstens 0,05 Punkten Rundung:", de((F(10005, 10000) ** 8 - 1) * 100, 2), "%")
assert round(float(F(357) / F(35632, 100) - 1) * 100, 2) == 0.19 and round(float(F(10005, 10000) ** 8 - 1) * 100, 1) == 0.4

# ---------------------------------------------------------------------------
titel("Testfall A.6, eigenstaendig nachgebaut (Grundlage fuer Punkte 16, 17 und 19)")
n = 5
ek0, k0, a0 = F(400000), F(700000), F(1100000)
i_soll, annuitaet = F(4, 100), F(42000)
h, s = F(2, 100), F(30, 100)            # Habenzins = Alternativzins vor Steuern; Steuersatz
afa = F(17600)
verkauf = F(1150000)
guthaben, restschuld = ek0 + k0 - a0, k0
assert guthaben == 0
sollzinsen, pfad = [], []
for t in range(1, n + 1):
    reinertrag = F(55000) * F(102, 100) ** (t - 1)
    sz = i_soll * restschuld
    hz = h * guthaben
    steuer = s * (reinertrag - afa - sz + hz)
    tilgung = annuitaet - sz
    restschuld -= tilgung
    guthaben += reinertrag - annuitaet + hz - steuer
    sollzinsen.append(sz)
    pfad.append((t, guthaben, restschuld))
ew = guthaben + verkauf - restschuld
q = 1 + h * (1 - s)
alt_ew = ek0 * q ** n
print("Restschuld Ende Jahr 5", de(restschuld), "| Endwert", de(ew), "| Alternative", de(alt_ew),
      "| Endwertdifferenz", de(ew - alt_ew), "| VOFI-Rendite", de(wurzel(ew / ek0, n) * 100, 3), "%")
assert round(float(restschuld), 2) == 624171.48 and round(float(ew), 2) == 584366.28
assert round(float(ew - alt_ew), 2) == 155571.23 and round(wurzel(ew / ek0, n) * 100, 3) == 7.876
print("Punkt 19: Alternativzins", de(h * 100, 0), "% vor Steuern,", de(h * (1 - s) * 100, 1), "% nach Steuern")
assert h * (1 - s) == F(14, 1000)

# ---------------------------------------------------------------------------
titel("Punkt 17 | A Nr. 19: VOFI-Gesamtkapitalrendite und Referenzzinsfuss im Testfall (MA-028)")
z_s = sum(sollzinsen)            # einfache Summe der Sollzinsen des Darlehens, ohne Kontokorrent
g_zaehler = ew - ek0 + z_s * (1 - s) + a0
k_zaehler = ek0 * q ** n - ek0 + z_s * (1 - s) + a0
g_gk, k_ref = wurzel(g_zaehler / a0, n), wurzel(k_zaehler / a0, n)
print("Sollzinsen Z_S", de(z_s), "| nach Steuern", de(z_s * (1 - s)), "| g_GK", de(g_gk * 100, 2), "% | Referenzzinsfuss k", de(k_ref * 100, 2), "%")
assert round(float(z_s), 2) == 134171.48 and round(g_gk * 100, 2) == 4.61 and round(k_ref * 100, 2) == 2.14
assert (g_gk > k_ref) == (ew > alt_ew)
# die beiden frueheren Lesarten, die die Fremdkapitalbetraege aufzinsen (Notiz 09, Befund 4d)
tilgungen = [annuitaet - z for z in sollzinsen]
tilgungen[-1] += restschuld      # Abloesung im letzten Jahr
b_zaehler = ew + sum((tilgungen[t] + sollzinsen[t] * (1 - s)) * q ** (n - (t + 1)) for t in range(n))
c_zaehler = ew + k0 * (1 + i_soll * (1 - s)) ** n
print("fruehere Lesarten: aufgezinst mit Habenzins n. St.", de(wurzel(b_zaehler / a0, n) * 100, 2), "% | Fremdkapital mit Sollzins n. St.",
      de(wurzel(c_zaehler / a0, n) * 100, 2), "%")
assert round(wurzel(b_zaehler / a0, n) * 100, 2) == 4.69 and round(wurzel(c_zaehler / a0, n) * 100, 2) == 4.76
assert sum(tilgungen) == k0      # Tilgungen und Abloesung ergeben das Darlehen; Lesart (a) = Formel des Lexikons
assert ew + sum(tilgungen) + z_s * (1 - s) == g_zaehler

# ---------------------------------------------------------------------------
titel("Punkt 16 | A Nr. 18, MA-027: Amortisationsdauer im Testfall")
print("ohne Restwert vor dem Verkauf (alte Fassung): Guthaben | Guthaben - Restschuld | Alternative")
for t, g, rs in pfad[:-1]:
    print(f"  Jahr {t}: {de(g, 0)} | {de(g - rs, 0)} | {de(ek0 * q ** t, 0)}")
    assert g < ek0 * q ** t      # bis zum Verkauf nie erreicht -> Amortisationsdauer = Haltedauer
assert round(float(pfad[0][1])) == 10180 and round(float(pfad[3][1])) == 45264 and round(float(ek0 * q ** 4)) == 422875
# neue Fassung: gedachter Verkauf zum Wertpfad. ANNAHME (wie Notiz 09, Befund 4c): Erloes nach
# Verkaufskosten linear von 1,00 auf 1,15 Mio.; Gewinn steuerfrei, keine Vorfaelligkeit.
vermoegen = {}
for t, g, rs in pfad:
    liq = F(1000000) + F(150000) * t / n
    vermoegen[t] = g + liq - rs
    print(f"  Jahr {t}: Vermoegen bei gedachtem Verkauf {de(vermoegen[t])} | Eigenkapital gedeckt: {vermoegen[t] >= ek0}"
          f" | Alternative {de(ek0 * q ** t)} erreicht: {vermoegen[t] >= ek0 * q ** t}")
assert round(float(vermoegen[n]), 2) == round(float(ew), 2)
ek_gedeckt = min(t for t in vermoegen if vermoegen[t] >= ek0)
dauerhaft = min(t for t in vermoegen if all(vermoegen[u] >= ek0 * q ** u for u in vermoegen if u >= t))
print("Eigenkapital gedeckt ab Jahr", ek_gedeckt, "| Alternative dauerhaft erreicht ab Jahr", dauerhaft)
assert ek_gedeckt == 2 and dauerhaft == 3

print("\nAlle Pruefungen bestanden.")
