from grob import *
import sys
STRESS=dict(anschluss=D("0.01"), ausfall=D("0.02"), ms=D("0.005"), inst=D("0.10"), faktor=D("0.10"))
def run(P, stress=False):
    c=dict(BASE); c["P"]=D(P)
    if stress: c["stress"]=STRESS
    return rechne(c)
def suche(stress, lo=1_000_000, hi=4_000_000):
    f=lambda P: run(P,stress)["r"]>=D("0.05")
    assert f(lo) and not f(hi)
    while hi-lo>1:
        m=(lo+hi)//2
        if f(m): lo=m
        else: hi=m
    return lo
x=run(2400000,True); print("Stress EW",x["EW"],"dEW",x["dEW"],"r",x["r"],"deck",x["deck1"],"L",x["L"], "EUe", x["EUe"])
for s in (False,True):
    P=suche(s); a=run(P,s); b=run(P+1,s)
    print("stress" if s else "basis", P, a["r"], b["r"], "L",a["L"],a["grenze"],"EK",a["EK"],"EUe",a["EUe"], "deck", a["deck1"])
