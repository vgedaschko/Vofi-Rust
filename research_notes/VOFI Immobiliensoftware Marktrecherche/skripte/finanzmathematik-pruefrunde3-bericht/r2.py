from m import *
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_DOWN, getcontext
getcontext().prec=40
E0={0:F(400000)}; E5={t:F(5000) for t in range(1,6)}
R=dict(rz=cent, rst=cent, rm=cent)
faelle={'Basis':{}, 'Entnahmen':dict(entn=E5), 'KK':dict(ek={0:F(380000)}), 'KK+Entn':dict(ek={0:F(380000)},entn=E5),
 'Nachschuss':dict(ek={0:F(400000),2:F(50000)}), 'N+E':dict(ek={0:F(400000),2:F(50000)},entn={2:F(50000)}),
 'MieteVJ':dict(miete0=F(56100))}
for k,kw in faelle.items():
    a=modell(**kw); b=modell(**kw,**R); c=modell(**kw,rz=cent,rst=euro_ab,rm=cent)
    print("%-10s voll %.4f  Nr10 %.2f (diff %+.4f)  Steuer volle Euro ab %.2f (diff %+.2f)"%(k,a,b,b-a,c,c-a))
# Darlehensbeispiel Nr. 10
def plan(mode):
    K=D(700000)
    for _ in range(120):
        z=K*D(4)/D(1200)
        if mode: z=z.quantize(D("0.01"),mode)
        K-=D(3500)-z
    return K
for n,mo in (("voll",None),("kaufm",ROUND_HALF_UP),("ab",ROUND_DOWN)): print("Restschuld",n,plan(mo))
# Reihenfolge der Operationen: K*(i/12) mit 28 Stellen vs (K*i)/12
getcontext().prec=28
cnt=0
import random; random.seed(1)
for _ in range(200000):
    K=D(random.randint(100000,99999999))/D(100); i=D(random.choice(["0.0375","0.04","0.0425","0.0333","0.0295"]))
    a=(K*(i/D(12))).quantize(D("0.01"),ROUND_HALF_UP); b=((K*i)/D(12)).quantize(D("0.01"),ROUND_HALF_UP)
    if a!=b: cnt+=1
print("Abweichende Cent-Rundung K*(i/12) vs (K*i)/12 bei 28 Stellen:",cnt,"von 200000")
# gezielter Fall: exakt halber Cent
K=D("1500.15"); i=D("0.04")
print("K=1500,15 4%: exakt", K*i/12, " via i/12:", (K*(i/D(12))), "->", (K*(i/D(12))).quantize(D("0.01"),ROUND_HALF_UP), "vs", (K*i/D(12)).quantize(D("0.01"),ROUND_HALF_UP))
