from rf11 import *
import time
t=time.time(); o=rechne(BASIS,P=2317235); print("t",time.time()-t)
for P in range(2317225,2317240):
    o=rechne(BASIS,P=P); print(P, o["L"], round(float(o["r"])*100,6), o["EU"].quantize(C), o["EK0"], o["ekbed"])
def stress(P):
    b=rechne(BASIS,P=P); return rechne(BASIS,P=P,stress=True,L_fix=b["L"])
for P in [1978672,1978673,1978674,1978675,1978676]:
    s=stress(P); print("S",P,s["L"],round(float(s["r"])*100,6),s["EU"].quantize(C), min(s["deck"].values()))
for P in [2138909,2138910,2138911]:
    o=rechne(BASIS,P=P); print("EK",P,o["EK0"],o["nach"],o["ekbed"])
