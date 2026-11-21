"""Befund 2 der Runde 2 (NG-32): Sprung durch die 15-%-Regel in der Preissuche, Basis- und Stressfall."""
from h import *
import time
e = replace(ANK, stau_betrag=D(336000), stau_jahr=1)
vg = replace(VG, zielrendite=D("0.0371259"))
t0 = time.time()
print("Basis:", tp(e, vg), f"({time.time()-t0:.1f} s)")
for P in (2350070, 2350071, 2350089, 2350090):
    g = rechne_grob(e, vg, KAT, preis=P, mit_blatt=False)
    print(" ", P, de(g.kennzahlen["endwertueberschuss"]), [m["kennung"] for m in g.meldungen])
