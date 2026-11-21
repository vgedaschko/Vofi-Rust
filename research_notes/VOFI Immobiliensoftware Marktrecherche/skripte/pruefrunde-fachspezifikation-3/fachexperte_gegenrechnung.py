"""Gegenrechnungen des Fachexperten, Pruefrunde 3 (2026-11-21). Nur Standardbibliothek."""
from decimal import Decimal as D, ROUND_HALF_UP, getcontext
getcontext().prec = 40
def r2(x): return x.quantize(D("0.01"), ROUND_HALF_UP)
def ann(K, i, m):
    ip = i / 12; q = 1 + ip
    return r2(K * ip * q**m / (q**m - 1))
print("KfW 3 Mio, 2,5 %, 408 Monate:", ann(D(3000000), D("0.025"), 408))
print("KfW 3 Mio, 2,5 %, 360 Monate (35/5):", ann(D(3000000), D("0.025"), 360))
# Beispiel zum Bemessungszins R-5.12, gebundener Bestand
RE = D("92479.44"); mu = D("1.2")
def B(KD, ik_tk): return ((RE / mu - KD) / ik_tk)
# H-25 je Tranchenart (Text): Bank 5 %+2 %, uebernommenes Darlehen i_kalk 4 %
iB = (D("0.005") * 96 + D("0.04") * 24) / 120
KD = 12 * r2(D(600000) * (iB + D("0.02")) / 12)
print("i_B bei 4 %:", iB, "KD_Ue:", KD)
print("Bank mit 7 % (Text 826.660,00):", B(KD, D("0.07")))
print("Bank mit H-25 = 4 % fuer alle Tranchen (ein Wert, R-3.4):", B(KD, D("0.06")))
print("Lesart 2 Vertragskonditionen (Text 1.034.436,66):", B(D(15000), D("0.06")))
# V-12 / CO2KostAufG 5a: Groessenordnung weiterer Vermieterkosten (Schaetzung, ungepruefte Preise)
flaeche = 1320; verbrauch = 120  # kWh je m2 und Jahr, Annahme
kwh = flaeche * verbrauch
netz = D("0.018") * kwh / 2       # halbe Gasnetzentgelte, 1,8 ct/kWh Annahme
for anteil in (D("0.15"), D("0.30")):
    bio = D("0.06") * kwh * anteil   # Mehrkosten Biogas 6 ct/kWh Annahme
    print("weitere Kosten bei Bioanteil", anteil, ":", r2(netz + bio), "Euro je Jahr")
# Schoenheitsreparaturen nach II. BV 28 Abs. 4 (Hoechstbetrag laut Quellnotiz 10: 8,50 Euro je m2, Basis)
print("Schoenheitsreparaturen 8,50 x 1.320 m2:", 8.5 * flaeche, "Euro je Jahr;",
      "Verhaeltnis zu +1 Euro Betriebskosten (AN -0,54 %):", round(8.5, 1), "fach")
