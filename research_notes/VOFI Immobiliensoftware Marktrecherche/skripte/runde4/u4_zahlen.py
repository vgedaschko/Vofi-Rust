#!/usr/bin/env python3
"""Vierte Ueberarbeitung des Rechercheberichts (Sichtung Runde 4): Nachrechnung jeder
neuen oder geaenderten Zahl. Exakt mit Bruechen; Ausgabe mit den Stellen des Berichts.

    python3 u4_zahlen.py

Jeder Block nennt die Fundstelle im Bericht. Schlaegt eine Pruefung fehl, bricht das
Skript mit AssertionError ab.
"""
from fractions import Fraction as F


def de(x, nd=2):
    s = f"{float(x):,.{nd}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def titel(t):
    print("\n== " + t)


# ---------------------------------------------------------------------------
titel("D.4 Kreditkennzahlen: Beispiel der Darlehensgrenze (bisherige Bankgrenze)")
miete = F(134640)
nuk = F(20, 100)            # nicht umlagefaehige Kosten
quote = F(65, 100)          # Beleihungsquote
kd_satz = F(6, 100)         # Zins und Tilgung
dscr_min = F(12, 10)        # Mindestdeckung
reinertrag = miete * (1 - nuk)
sd_tragbar = reinertrag / dscr_min
darlehen_deckung = sd_tragbar / kd_satz
preis_gleichstand = darlehen_deckung / quote
print("Reinertrag", de(reinertrag), "| tragbarer Schuldendienst", de(sd_tragbar))
print("Darlehen aus Mindestdeckung", de(darlehen_deckung))
print("Preis, bis zu dem die Quote allein die Mindestdeckung einhaelt", de(preis_gleichstand))
assert reinertrag == 107712 and sd_tragbar == 89760 and darlehen_deckung == 1496000
assert round(float(preis_gleichstand) / 1e6, 2) == 2.30

# Neue Regel am selben Beispiel: Darlehen = min(Quote * Wertansatz, Darlehen aus Mindestdeckung)
preis = F(2600000)
darlehen_quote = quote * preis
deckung_quote = reinertrag / (darlehen_quote * kd_satz)
darlehen = min(darlehen_quote, darlehen_deckung)
deckung = reinertrag / (darlehen * kd_satz)
print("bei 2,6 Mio.: Darlehen nach Quote", de(darlehen_quote), "| Deckung", de(deckung_quote, 4))
print("bei 2,6 Mio.: gedeckeltes Darlehen", de(darlehen), "| Deckung", de(deckung, 2),
      "| Anteil am Kaufpreis", de(darlehen / preis * 100, 2), "%",
      "| mehr Eigenkapital", de(darlehen_quote - darlehen))
assert darlehen_quote == 1690000 and round(float(deckung_quote), 2) == 1.06
assert darlehen == 1496000 and deckung == dscr_min
assert round(float(darlehen / preis) * 100, 1) == 57.5
assert darlehen_quote - darlehen == 194000
# Unter dem Gleichstandspreis bindet die Quote, darueber die Mindestdeckung
for p in (F(2000000), F(2300000), F(2310000), F(2600000)):
    bindet = "Quote" if quote * p <= darlehen_deckung else "Mindestdeckung"
    print("  Preis", de(p, 0), "-> es bindet:", bindet)
assert quote * F(2300000) < darlehen_deckung < quote * F(2310000)

# ---------------------------------------------------------------------------
titel("D.4 Darlehen: gefoerderter Neubau, Bankdarlehen als Restfinanzierung")
gesamt = F(10_000_000)
zuwendungsfaehig = F(9_000_000)
q_darlehen, q_zuschuss, q_eigen = F(60, 100), F(20, 100), F(20, 100)   # Einkommensgruppe B (C.1); Eigenmittel 20 %
foerderdarlehen = q_darlehen * zuwendungsfaehig
zuschuss = q_zuschuss * zuwendungsfaehig
eigen_min = q_eigen * zuwendungsfaehig
bank_rest = gesamt - foerderdarlehen - zuschuss - eigen_min
print("Foerderdarlehen", de(foerderdarlehen, 0), "| Zuschuss", de(zuschuss, 0),
      "| Eigenkapital mindestens", de(eigen_min, 0), "| Bankdarlehen hoechstens", de(bank_rest, 0))
assert (foerderdarlehen, zuschuss, eigen_min, bank_rest) == (5_400_000, 1_800_000, 1_800_000, 1_000_000)
# Kontrollsumme Mittelherkunft = Mittelverwendung
assert foerderdarlehen + zuschuss + eigen_min + bank_rest == gesamt
# Alter Wortlaut (Quote auf Gesamtkosten, Foerderung obendrauf): Ueberfinanzierung
alt = quote * gesamt + foerderdarlehen + zuschuss
print("alter Wortlaut: Mittel", de(alt, 0), "gegen Kosten", de(gesamt, 0))
assert alt == 13_700_000

# ---------------------------------------------------------------------------
titel("D.4 Ertragsteuern, Kurzform: Belastung der Koerperschaft (Saetze aus B.3; Hebesatz 400 % angenommen)")
kst, soli, messzahl, hebesatz = F(15, 100), F(55, 1000), F(35, 1000), F(400, 100)
kst_soli = kst * (1 + soli)
gewst = messzahl * hebesatz
print("Koerperschaftsteuer mit Solidaritaetszuschlag", de(kst_soli * 100, 3), "%",
      "| Gewerbesteuer", de(gewst * 100, 1), "%", "| zusammen", de((kst_soli + gewst) * 100, 3), "%")
assert kst_soli == F(15825, 100000) and gewst == F(14, 100)
assert round(float(kst_soli + gewst) * 100, 1) == 29.8 and round(float(kst_soli) * 100, 1) == 15.8

titel("B.3 Anrechnung der Gewerbesteuer (Par. 35 EStG): Vierfaches des Messbetrags, hoechstens die Gewerbesteuer")
ertrag = F(100000)
messbetrag = ertrag * messzahl
for h in (F(400, 100), F(280, 100)):
    g = messbetrag * h
    erm = min(4 * messbetrag, g)
    print(f"Hebesatz {int(h*100)} %: Gewerbesteuer {de(g, 0)}, Ermaessigung {de(erm, 0)}, verbleibend {de(g - erm, 0)}")
assert messbetrag == 3500 and messbetrag * 4 == 14000 and messbetrag * F(280, 100) == 9800
print("ohne Anrechnung zu hoch um bis zu", de(messzahl * 4 * 100, 0), "Prozentpunkte des Gewerbeertrags")

# ---------------------------------------------------------------------------
titel("B.6 / MA-021: Wirkung der Nettolesart auf die Foerderung")
anteil = F(19, 119)
print("Umsatzsteueranteil der Bruttokosten 19/119 =", de(anteil * 100, 2), "% (ein Sechstel =", de(F(100, 6), 2), "%)")
assert anteil < F(1, 6) and round(float(anteil) * 100, 1) == 16.0
brutto, grenze = F(5800), F(5250)
netto = brutto / F(119, 100)
print("Kappung: brutto 5.800, netto", de(netto, 0), "| Foerderbasis sinkt um", de((grenze - netto) / grenze * 100, 1), "%")
assert round(float(netto)) == 4874 and round(float((grenze - netto) / grenze) * 100, 1) == 7.2

# ---------------------------------------------------------------------------
titel("A.1 Nr. 3: Preisstand des Abzugs fuer ausstehenden Investitionsstau")
stau, index = F(100000), F(103, 100)
plan, stichtag = stau * index ** 12, stau * index ** 10
print("geplant fuer Jahr 12:", de(plan, 0), "| Abzug zum Preisstand des Verkaufs in Jahr 10:", de(stichtag, 0))
assert round(float(plan)) == 142576 and round(float(stichtag)) == 134392

titel("A.1 Nr. 3: doppelt gezaehlte Restschuld im Testfall (Restwertprobe)")
K = F(700000)
for t in range(1, 6):
    K -= F(42000) - K * F(4, 100)
endwert = F("584366.2815706428")          # Testfall, siehe u4_testfall.py
print("Restschuld Ende Jahr 5:", de(K), "| Endwert bei doppeltem Abzug:", de(endwert - K))
assert round(float(K), 2) == 624171.48 and round(float(endwert - K), 2) == -39805.20

# ---------------------------------------------------------------------------
titel("Kopfteil: Termine der Vorpruefung beim Auftraggeber")
nbank, gespraeche, vorfuehrungen = 1, (3, 5), 3
print("Termine:", nbank + gespraeche[0] + vorfuehrungen, "bis", nbank + gespraeche[1] + vorfuehrungen)
assert (nbank + gespraeche[0] + vorfuehrungen, nbank + gespraeche[1] + vorfuehrungen) == (7, 9)

# ---------------------------------------------------------------------------
titel("D.1: Eingaben der Grobkalkulation, nachgezaehlt")
ankauf = ["Kaufpreis", "Erwerbsnebenkosten", "Bodenanteil", "Wohnflaeche", "Zahl der Einheiten",
          "Ist-Miete", "Marktmiete", "Baujahr"]
neubau = ["Grundstueckspreis", "Grundstuecksflaeche", "Brutto-Grundflaeche", "Wohnflaeche",
          "Zahl der Einheiten", "Kostenkennwert", "Bauzeit", "Miete"]
beide = ["Steuerstatus", "Beleihungsquote", "Zins", "Tilgung", "Zinsbindung", "Restwertfaktor", "Haltedauer"]
steuer = ["Kennzeichen erweiterte Grundstueckskuerzung (Koerperschaft) oder Steuersatz (Person, Personengesellschaft)"]
foerderung = ["Mietenstufe", "Einkommensgruppe", "Bodenrichtwert"]
pauschalen_ankauf = ["Investitionsstau: Betrag", "Investitionsstau: Zeitpunkt", "Investitionsstau: Kennzeichen",
                     "Anpassungsdauer der Miete", "Effizienzklasse", "Energietraeger"]
freiwillig = ["verfuegbares Eigenkapital", "Wertansatz der Bank"]
gebunden = ["gebundener Flaechenanteil", "Bindungsende", "zulaessige Steigerung"]
uebernommen = ["Restschuld", "Zins", "Tilgung", "Ende der Zinsbindung"]
erbbau = ["Erbbauzins", "Index"]
a0 = len(ankauf) + len(beide) + len(steuer)
n0 = len(neubau) + len(beide) + len(steuer)
print("Ankauf:", a0, "| mit Pauschalen:", a0 + len(pauschalen_ankauf))
print("Neubau frei finanziert:", n0, "| mit Grobfoerderung:", n0 + len(foerderung))
print("dazu nur im Einzelfall: freiwillig", len(freiwillig), "| gebundener Bestand", len(gebunden),
      "| uebernommenes Foerderdarlehen", len(uebernommen), "| Erbbaurecht", len(erbbau))
assert (a0, a0 + len(pauschalen_ankauf)) == (16, 22)
assert (n0, n0 + len(foerderung)) == (16, 19)

print("\nAlle Pruefungen bestanden.")
