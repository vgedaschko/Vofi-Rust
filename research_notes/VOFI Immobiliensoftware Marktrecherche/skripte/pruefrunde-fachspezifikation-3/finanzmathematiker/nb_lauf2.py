from nb import *
import sys
def pstar(par, lo, hi):
    ok = lambda P: rechne(par, P=P)["EU"] >= 0
    assert ok(lo) and not ok(hi)
    while hi - lo > 1:
        m = (lo + hi) // 2
        lo, hi = (m, hi) if ok(m) else (lo, m)
    return lo
KF = dict(BASIS, kfw=dict(betrag=D(3000000), T=35, f=1, zins=D("0.025")))
o = rechne(KF)
for k in ["KDU", "A", "B", "C", "L", "EKplan", "ek_inv", "prov", "rate_k", "EW", "EWU", "dEW"]:
    print("KfW", k, o[k])
print("KfW r", o["r"] * 100, "kfw_aus erster", min(o["kfw_aus"]), o["kfw_aus"][min(o["kfw_aus"])], "letzter", max(o["kfw_aus"]), "bank", min(o["bank_aus"]), max(o["bank_aus"]))
print("KfW deck", {j: round(float(v), 4) for j, v in o["deck"].items()})
for T, f in [(35, 5), (25, 3), (10, 2)]:
    x = rechne(dict(KF, kfw=dict(betrag=D(3000000), T=T, f=f, zins=D("0.025"))))
    print("Variante", T, f, x["rate_k"], x["KDU"], x["L"], x["dEW"])
x = rechne(dict(KF, H32=15)); print("H-32 15 J: KDU", x["KDU"], "L", x["L"])
x = rechne(dict(KF, kfw=dict(betrag=D(3000000), T=35, f=1, zins=D("0.03")))); print("KfW 3 %: dEW-Wirkung", x["dEW"] - o["dEW"], "KDU", x["KDU"])
if "preis" in sys.argv:
    print("P* frei", pstar(BASIS, 500000, 900000))
    print("P* KfW", pstar(KF, 1000000, 1400000))
    print("P* nachh 15", pstar(dict(BASIS, nachh=D(15)), 400000, 800000))
