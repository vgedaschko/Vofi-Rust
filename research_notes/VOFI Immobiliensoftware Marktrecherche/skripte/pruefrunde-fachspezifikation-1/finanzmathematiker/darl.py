# Zinsbindung kuerzer als Haltedauer, unabhaengig aus R-5.3, R-5.4, R-5.9
from decimal import Decimal as D, getcontext, ROUND_HALF_UP
import math
getcontext().prec = 50
def r(x): return x.quantize(D("0.01"), ROUND_HALF_UP)
# RF-08 Jahresmodus ungerundet
K=D(1496000); i=D("0.04"); t=D("0.02"); R=K*(i+t)
RS=K
for _ in range(10): RS -= R - RS*i
print("RS10", RS)
print("Tilgungssatz bleibt", RS*(D("0.06")+t))
mges = D(math.log(3)/math.log(1.04)); mrest = mges-10
print("Restlaufzeit gesamt", mges, "rest", mrest)
for m in (mrest, D(18), D(19), D(math.ceil(float(mrest)))):
    q=D("1.06"); print(" m",m, "Rate", RS*D("0.06")*q**m/(q**m-1))
# Restlaufzeit mit Anschlusszins statt Urspruengszins?
# RF-11 monatlich
L=D("1431044.99"); rate=r(L*D("0.06")/12); RS=L
for u in range(120):
    z=r(RS*D("0.04")/12); RS-= rate-z
print("RF-11 Rate", rate, "RS120", RS, "neue Rate", r(RS*D("0.07")/12))
# Restlaufzeit-Regel im Monatsraster: Formel ln((i+tau)/tau)/ln(1+i/p)
mges = math.log(3)/math.log(1+0.04/12); print("Monat: Restlaufzeit gesamt", mges, "Perioden; rest", mges-120)
# RF-08 Rundungsvarianten 700000 4 % Rate 3500, 120 Raten
from decimal import ROUND_DOWN
for mode in ("k","a","n"):
    RS=D(700000)
    for u in range(120):
        z=RS*D("0.04")/12
        z = r(z) if mode=="k" else (z.quantize(D("0.01"),ROUND_DOWN) if mode=="a" else z)
        RS -= D(3500)-z
    print(mode, RS)
