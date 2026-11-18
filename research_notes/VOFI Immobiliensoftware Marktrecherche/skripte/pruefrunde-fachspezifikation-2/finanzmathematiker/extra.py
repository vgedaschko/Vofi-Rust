import rf11
from rf11 import *
def pstar(par, lo=1500000, hi=3000000, stress=False):
    def ok(P):
        if stress:
            b=rechne(par,P=P); o=rechne(par,P=P,stress=True,L_fix=b["L"])
        else: o=rechne(par,P=P)
        return o["EU"]>=0
    while hi-lo>1:
        m=(lo+hi)//2
        if ok(m): lo=m
        else: hi=m
    return lo
for reg in ["tilgungssatz","rate","restlaufzeit"]:
    p=dict(BASIS); p["regel"]=reg; print("H-07",reg,"P*",pstar(p))
# Stress mit Neubemessung zum Zins nach Zusage
b=rechne(BASIS)
p=dict(BASIS); p["zins"]=BASIS["zins"]+D("0.005")
o=rechne(p); print("Neubemessung bei 4,5 %: L",o["L"],"B",o["B"])
s1=rechne(BASIS,stress=True,L_fix=b["L"])
s2=rechne(BASIS,stress=True,L_fix=o["L"])
print("Stress L_basis: r",round(float(s1["r"])*100,3),"dEW",s1["dEW"],"EK0",s1["EK0"])
print("Stress L neu   : r",round(float(s2["r"])*100,3),"dEW",s2["dEW"],"EK0",s2["EK0"])
# Bankfall RF-19
p=dict(BASIS); p["zins"]=D("0.03"); p["vm"]=D("8.50"); p["stau"]=D(0); p["mietst"]=D("0.005")
p["aufschlag"]=D(0)  # Lesart 2: kalkulatorisch = Vertrag -> ik = 3 %
o=rechne(p); print("Bankfall L",o["L"], {j:round(float(v),4) for j,v in o["deck"].items()})
p2=dict(p); p2["aufschlag"]=BASIS["aufschlag"]
s=rechne(p2,stress=True,L_fix=o["L"]); print("Bankfall Stress", {j:round(float(v),4) for j,v in s["deck"].items()})
