"""Runde 3: Basisfall und Stressfall RF-11 mit eigenem Nachbau (ank.py), tragbare Preise."""
from ank import *
def f(x, k=2): return f"{float(x):,.{k}f}"
b = rechne(BASIS)
print("Basis L", b["L"], "A", b["A"], "B", b["B"], "REn", b["REn"], "EK0", b["EK0"], "Nachschuss", b["nach"])
print("Basis EW", b["EW"], "EWU", b["EWU"], "dEW", b["dEW"], "r %.4f" % (b["r"]*100), "rU %.4f" % (b["rU"]*100), "EU", r2(b["EU"]))
print("Basis vp", b["vp"], "abl", b["abl"], "gv", b["gv"])
print("Deck", {j: round(float(v), 4) for j, v in b["deck"].items()})
s = rechne(BASIS, stress=True)
print("Stress L", s["L"], "B", s["B"], "EK0", s["EK0"], "Nachschuss", s["nach"])
print("Stress EW", s["EW"], "EWU", s["EWU"], "dEW", s["dEW"], "r %.4f" % (s["r"]*100), "rU %.4f" % (s["rU"]*100), "EU", r2(s["EU"]))
print("Stress Deck", {j: round(float(v), 4) for j, v in s["deck"].items()})
print("Stress vp", s["vp"])
def ok(P, st=False):
    return rechne(BASIS, P=P, stress=st)["EU"] >= 0
def pstar(st=False, lo=1500000, hi=3000000):
    assert ok(lo, st) and not ok(hi, st)
    while hi - lo > 1:
        m = (lo + hi) // 2
        if ok(m, st): lo = m
        else: hi = m
    return lo
p = pstar(); o = rechne(BASIS, P=p); o1 = rechne(BASIS, P=p+1)
print("P* Basis", p, "EU", r2(o["EU"]), "r", o["r"]*100, "r(P+1)", o1["r"]*100, "EK0", o["EK0"], "EKges", o["ekbed"])
ps = pstar(True); os_ = rechne(BASIS, P=ps, stress=True)
print("P* Stress", ps, "EU", r2(os_["EU"]), "L", os_["L"], "EK0", os_["EK0"], "EKges", os_["ekbed"], "kleinste Deck", min(os_["deck"].values()))
