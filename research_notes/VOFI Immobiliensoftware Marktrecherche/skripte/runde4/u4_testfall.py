#!/usr/bin/env python3
"""Vierte Ueberarbeitung, Sichtungspunkt 20: Die Eingaben des Testfalls, wie sie in
Anhang A.6 des Berichts stehen, reichen aus, um die Referenzwerte nachzurechnen.

Unabhaengig von m3.py und s1_gegenrechnung.py neu aufgebaut, nur aus den Eingaben der
Zelle "Annahmen" (abgeglichen mit Quellnotiz 03, Testfall S1). Danach Vergleich mit m3.py.

    python3 u4_testfall.py
"""
from fractions import Fraction as F
import os
import sys

# Eingaben wie in Anhang A.6, Zeile "Testfall"
KAUFPREIS = F(1_000_000)
ERWERBSNEBENKOSTEN = F(100_000)
EIGENKAPITAL = F(400_000)
DARLEHEN = F(700_000)
ZINS = F(4, 100)
ANFANGSTILGUNG = F(2, 100)
REINERTRAG_1 = F(55_000)
STEIGERUNG = F(2, 100)
AFA_SATZ = F(2, 100)
GEBAEUDEANTEIL = F(80, 100)          # der Gesamtinvestition von 1,1 Mio. Euro
STEUERSATZ = F(30, 100)
HABENZINS = F(2, 100)
KONTOKORRENTZINS = F(8, 100)
VERKAUF = F(1_150_000)               # Ende Jahr 5, nach Verkaufskosten, Gewinn steuerfrei
JAHRE = 5

gesamt = KAUFPREIS + ERWERBSNEBENKOSTEN
assert gesamt == EIGENKAPITAL + DARLEHEN          # Mittelherkunft = Mittelverwendung
annuitaet = DARLEHEN * (ZINS + ANFANGSTILGUNG)
afa = gesamt * GEBAEUDEANTEIL * AFA_SATZ
assert annuitaet == 42_000 and afa == 17_600

guthaben, kk, rest = F(0), F(0), DARLEHEN
for t in range(1, JAHRE + 1):
    reinertrag = REINERTRAG_1 * (1 + STEIGERUNG) ** (t - 1)
    sollzins = rest * ZINS
    tilgung = annuitaet - sollzins
    habenzins = guthaben * HABENZINS
    kkzins = kk * KONTOKORRENTZINS
    steuer = (reinertrag - afa - sollzins - kkzins + habenzins) * STEUERSATZ   # Verluste sofort verrechnet
    rest -= tilgung
    zahlung = reinertrag + habenzins - sollzins - tilgung - kkzins - steuer
    if t == JAHRE:
        zahlung += VERKAUF - rest
        abloesung, rest = rest, F(0)
    saldo = guthaben - kk + zahlung
    guthaben, kk = (saldo, F(0)) if saldo >= 0 else (F(0), -saldo)

endwert = guthaben - kk
q = 1 + HABENZINS * (1 - STEUERSATZ)
alternative = EIGENKAPITAL * q ** JAHRE
rendite = float(endwert / EIGENKAPITAL) ** (1 / JAHRE) - 1
print(f"Endwert {float(endwert):.2f} | Endwertdifferenz {float(endwert - alternative):.2f} | "
      f"VOFI-Rendite {rendite * 100:.3f} % | Abloesung {float(abloesung):.2f}")
assert round(float(endwert), 2) == 584366.28
assert round(float(endwert - alternative), 2) == 155571.23
assert round(rendite * 100, 3) == 7.876
assert round(float(abloesung), 2) == 624171.48

# Vergleich mit der Gegenrechnung des Finanzmathematikers (m3.py im selben Ordner)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m3  # noqa: E402
assert m3.modell() == endwert
print("stimmt mit m3.modell() exakt ueberein; Eingaben aus A.6 sind vollstaendig.")
