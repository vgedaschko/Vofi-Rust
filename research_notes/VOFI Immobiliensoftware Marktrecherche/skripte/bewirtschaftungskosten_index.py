"""Fortschreibung der Bewirtschaftungskosten nach Anlage 3 ImmoWertV und §§ 26, 28 II. BV.

Verbraucherpreisindex für Deutschland, 2020 = 100, Monat Oktober.
Quelle: Destatis, Tabelle „Verbraucherpreisindex für Deutschland" (12 Abteilungen) und
Statistischer Bericht „Lange Reihen ab 1948" (Ausgabe Juni 2025), gelesen am 2026-11-18.
"""
from decimal import Decimal as D, ROUND_HALF_UP

VPI_OKT = {2001: D("77.1"), 2020: D("99.9"), 2022: D("113.5"), 2024: D("120.2"), 2025: D("123.0"), 2026: D("126.5")}
BASIS_IMMOWERTV = {"Verwaltung je Wohnung": (D("230"), "1"), "Verwaltung je Eigentumswohnung": (D("275"), "1"),
                   "Verwaltung je Stellplatz": (D("30"), "1"), "Instandhaltung je m²": (D("9.00"), "0.1"),
                   "Instandhaltung je Stellplatz": (D("68"), "1")}
BASIS_IIBV = {"Verwaltung je Wohnung": D("230"), "Instandhaltung unter 22 Jahre": D("7.10"),
              "Instandhaltung ab 22 Jahre": D("9.00"), "Instandhaltung ab 32 Jahre": D("11.50")}


def immowertv(stichtagsjahr):
    faktor = VPI_OKT[stichtagsjahr - 1] / VPI_OKT[2001]
    return {k: (b * faktor).quantize(D(r), ROUND_HALF_UP) for k, (b, r) in BASIS_IMMOWERTV.items()}


if __name__ == "__main__":
    for jahr in (2021, 2025, 2026, 2027):
        print(jahr, {k: str(v) for k, v in immowertv(jahr).items()})
    # Proben: 2021 laut Anlage 3: 298 / 357 / 39 / 11,70 / 88; 2025 laut Sekundärquelle: 359 / 429 / 47 / 14,00
    f = VPI_OKT[2025] / VPI_OKT[2001]
    print("II. BV, Faktor aus heutiger Reihe:", f.quantize(D("0.0001")), {k: str((b * f).quantize(D("0.01"))) for k, b in BASIS_IIBV.items()})
    print("II. BV, Faktor der Sekundärquelle: 1.6194; letzter Kettenschritt 2022→2025:", (VPI_OKT[2025] / VPI_OKT[2022]).quantize(D("0.0001")))
