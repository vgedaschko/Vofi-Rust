"""Tilgungsplan mit voller Genauigkeit vs. Cent-Rundung je Rate (Bankpraxis)."""
from decimal import Decimal as D, ROUND_HALF_UP, getcontext
getcontext().prec=40
def plan(K,p,rate,months,rund):
    K=D(K); m=D(p)/D(1200)
    for _ in range(months):
        z=K*m
        if rund: z=z.quantize(D("0.01"),ROUND_HALF_UP)
        K-= D(rate)-z
    return K
for K,p,rate,mon in ((700000,"4",D(700000)*D("0.06")/12,120),(10_000_000,"3.65",D(10_000_000)*D("0.0565")/12,360)):
    a=plan(K,p,rate,mon,False); b=plan(K,p,rate,mon,True)
    print(K,p,mon,"voll %.6f  cent %.2f  Diff %.4f"%(a,b,a-b))
