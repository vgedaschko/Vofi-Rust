from preis import run
from decimal import Decimal as D
import time
t=time.time(); run(2425585); print("sec/run", time.time()-t)
# Suche Nicht-Monotonie: Schritte von 1 Euro um mehrere Stellen
prev=None; ups=[]
import sys
start=int(sys.argv[1]); cnt=int(sys.argv[2])
for P in range(start, start+cnt):
    x=run(P)["r"]
    if prev is not None and x>prev: ups.append((P, float(x-prev)))
    prev=x
print("Anstiege:", len(ups), ups[:10])
