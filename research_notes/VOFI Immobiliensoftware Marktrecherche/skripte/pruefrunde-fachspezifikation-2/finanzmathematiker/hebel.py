from extra import pstar
from rf11 import *
for zins in ["0.04","0.06","0.07"]:
    for mu in ["1.2","1.3"]:
        p=dict(BASIS); p["zins"]=D(zins); p["mu"]=D(mu)
        p["z"]=D("0.02")
        P=pstar(p,lo=500000,hi=4000000)
        o=rechne(p,P=P)
        print("Zins",zins,"mu",mu,"z 2%","P*",P,"L",o["L"])
