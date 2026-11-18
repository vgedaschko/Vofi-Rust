from preis import run
from decimal import Decimal as D
a=run(2425541); b=run(2425542)
print("EW", a["EW"], b["EW"], "dEW", b["EW"]-a["EW"], "EK", a["EK"], b["EK"])
z=(a["r"]+b["r"])/2
print("z'", z)
sig=[]
for P in range(2425480, 2425620):
    sig.append((P, run(P)["r"]>=z))
ch=[(sig[k][0], sig[k+1][0]) for k in range(len(sig)-1) if sig[k][1]!=sig[k+1][1]]
print("Vorzeichenwechsel bei z':", ch)
