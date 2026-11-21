"""GF3-Z3 Preissuchen ueber die neuen Regeln (gefoerdert, KfW, Stress, Vorlauf, Bauzeit, E-60); Ergebnis gegen R-11.4 an P* und P*+1."""
from h import *
import random, sys, collections, time
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
ANZ = int(sys.argv[2]) if len(sys.argv) > 2 else 40
z = collections.Counter(); auff = []
t0 = time.time()
for i in range(ANZ):
    gef = random.random() < 0.5
    bz = random.choice([1, 7, 18, 21, 36, 60]); vl = random.choice([0, 12])
    n = max(-(-(vl + bz + 18) // 12), random.choice([5, 15, 38]))
    e = replace(NB, bauzeit_monate=bz, vorlauf_monate=vl, haltedauer=n, foerderung=A.FOERDERUNG_B if gef else None,
                kfw_betrag=D(random.choice([0, 500000, 3000000])), kfw_laufzeit=35, kfw_tilgungsfrei=random.choice([1, 5]),
                verfuegbares_ek=random.choice([None, None, D(0), D(2000000), D(5000000)]))
    vg = replace(VG, zielrendite=D(random.choice(["0.02", "0.03", "0.05"])), zielrendite_gefoerdert=D(random.choice(["0.02", "0.03", "0.04"])))
    stress = random.random() < 0.4
    try:
        t = tragbarer_preis(e, vg, KATN, stress=stress)
    except Exception as x:
        z["ABSTURZ"] += 1; auff.append((i, wo(x))); continue
    z[t["meldung"] or "Preis"] += 1
    if t["preis"] is not None:
        g0 = rechne_grob(e, vg, KATN, preis=t["preis"], stress=stress, mit_blatt=False)
        g1 = rechne_grob(e, vg, KATN, preis=t["preis"] + 1, stress=stress, mit_blatt=False)
        if t["bindend"] == "Rendite" and not (g0.kennzahlen["endwertueberschuss"] >= 0 > g1.kennzahlen["endwertueberschuss"]):
            auff.append((i, "P-14 Rendite", t["preis"]))
        if g0.gesperrt or g0.kennzahlen["nenner"] == 0:
            auff.append((i, "gesperrt oder ohne EK", t["preis"]))
print(dict(z), f"{time.time()-t0:.0f} s")
for a in auff:
    print(" ", a)
