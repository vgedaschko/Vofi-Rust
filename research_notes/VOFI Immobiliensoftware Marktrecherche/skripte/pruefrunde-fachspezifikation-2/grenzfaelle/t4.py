"""NG-32: 15-%-Regel macht die Rendite im Preis sprunghaft (nicht monoton); Preissuche gegen die Definition R-11.4."""
from h import *
X = D(336000)
e = replace(ANK, stau_betrag=X, stau_jahr=1, stau_art="erhaltung")
Ps = X * D("1.03") / D("1.19") / (D("0.15") * D("1.1") * D("0.75"))
print("Schwellenpreis rechnerisch", Ps)
def lauf(P, vg=VG):
    g = rechne_grob(e, vg, KAT, preis=P, mit_blatt=False)
    return g
for P in (2300000, 2350000, 2350071, 2350072, 2400000):
    g = lauf(P)
    print(P, "r", proz(g.kennzahlen["rendite"]), "M", [m["kennung"] for m in g.meldungen], "EUe", de(g.kennzahlen["endwertueberschuss"]))
r_unter = lauf(2350071).kennzahlen["rendite"]; r_ueber = lauf(2350072).kennzahlen["rendite"]
z = ((r_unter + r_ueber) / 2).quantize(D("0.0000001"))
print("Zielrendite", z)
vg = replace(VG, zielrendite=z)
t = tragbarer_preis(e, vg, KAT)
print("Preissuche:", t["preis"], t["meldung"], t.get("meldungen"))
# Definition R-11.4 pruefen: erster Preis, bei dem das Ziel verfehlt ist
def eue(P): return lauf(P, vg).kennzahlen["endwertueberschuss"]
lo, hi = 2000000, 2350071           # EUe(lo) >= 0 ?, EUe(hi) < 0 ?
print("EUe(2.000.000)", de(eue(2000000)), "EUe(2.350.071)", de(eue(2350071)), "EUe(2.350.072)", de(eue(2350072)))
while hi - lo > 1:
    m = (lo + hi) // 2
    if eue(m) >= 0: lo = m
    else: hi = m
print("nach Definition R-11.4: P* = ", lo, "(erster verfehlter Preis", hi, ")")
print("Preis der Suche - P* nach Definition:", (t["preis"] or 0) - lo)
for P in (2350088, 2350089, 2350090, 2357457, 2357458):
    g = lauf(P, vg)
    print(P, "EUe", de(g.kennzahlen["endwertueberschuss"]), "r", g.kennzahlen["rendite"].quantize(D("0.0000001")), [m["kennung"] for m in g.meldungen])
