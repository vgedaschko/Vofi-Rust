"""R-3.2 Tabelle der Abweichungen und Einzelstress R-11.8 mit eigenem Nachbau."""
from ank import *
def pstar(par, st=None, lo=1200000, hi=3600000):
    ok = lambda P: rechne(par, P=P, stress=st)["EU"] >= 0
    assert ok(lo) and not ok(hi)
    while hi - lo > 1:
        m = (lo + hi) // 2
        lo, hi = (m, hi) if ok(m) else (lo, m)
    return lo
b = rechne(BASIS); pb = pstar(BASIS)
def zeile(name, **kw):
    p = dict(BASIS); p.update(kw)
    o = rechne(p); ps = pstar(p); bz = pstar(dict(BASIS, z=p["z"])) if p["z"] != BASIS["z"] else pb
    print(f"{name:40s} dEW {r2(o['dEW']-b['dEW'])}  Preis {ps-bz:+d} ({ps})  r-z {float((o['r']-b['r'])*100):+.3f} PP")
zeile("H-12 1,5 %", mietst=D("0.015"))
zeile("H-12 2,5 %", mietst=D("0.025"))
zeile("H-25 fest 1 %", H25=D("0.01"))
zeile("H-02 60 %", beta=D("0.60"))
zeile("H-03 1,3 bei z 5 %", mu=D("1.3"))
zeile("H-03 1,3 bei z 2 %", mu=D("1.3"), z=D("0.02"))
zeile("E-11 3 %", enk=D("0.03"))
zeile("E-46 5 Jahre", bindung=60)
o = rechne(dict(BASIS, aL=D("0.005"))); print("H-09 0,5 %: dEW", o["dEW"], "r", o["r"]*100)
for g in ["anschluss", "zusage", "leer", "mietst", "faktor", "stau"]:
    s = rechne(BASIS, stress={g}); print("Einzelstress", g, r2(s["dEW"] - b["dEW"]), "L", s["L"])
