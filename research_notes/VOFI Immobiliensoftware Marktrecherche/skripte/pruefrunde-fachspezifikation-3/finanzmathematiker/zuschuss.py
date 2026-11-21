"""R-7.19 Zuschuss nach Vermoegenssphaere (E-70) mit eigenem Nachbau."""
from nb import *
G = dict(BASIS, foerd=True, n=38)
for name, kw in [("KSt verteilt", {}), ("KSt sofort", dict(zl="sofort")), ("Privat Zufluss", dict(status="privat")),
                 ("Privat E-70", dict(status="privat", e70=True))]:
    o = rechne(dict(G, **kw)); o20 = rechne(dict(G, n=20, **kw))
    print(f"{name:15s} r {float(o['r'])*100:.3f}  dEW {o['dEW']}  EK {o['ek_inv']}  EW {o['EW']}  | 20 J r {float(o20['r'])*100:.3f}")
for name, kw in [("Privat sofort-Verr.", dict(status="privat", h38="sofort")), ("Privat sofort-Verr. E-70", dict(status="privat", h38="sofort", e70=True))]:
    o20 = rechne(dict(G, n=20, **kw)); print(name, "20 J r %.3f" % (float(o20["r"]) * 100))
