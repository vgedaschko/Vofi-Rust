import ank
from ank import *
from decimal import Decimal as D
def pst(par, lo=1500000, hi=3200000):
    ok = lambda P: rechne(par, P=P)["EU"] >= 0
    while hi - lo > 1:
        m = (lo + hi) // 2
        lo, hi = (m, hi) if ok(m) else (lo, m)
    return lo
for ma in (True, False):
    p = dict(BASIS, ist=D("11.00"), ma038=ma); o = rechne(p)
    print("MA-038", ma, "Miete Jahresbeginn 1..7", [round(float(o["miete"][12*j+1]), 4) for j in range(7)], "dEW", o["dEW"], "P*", pst(p))
o = rechne(BASIS); print("Basis unveraendert dEW", o["dEW"])
