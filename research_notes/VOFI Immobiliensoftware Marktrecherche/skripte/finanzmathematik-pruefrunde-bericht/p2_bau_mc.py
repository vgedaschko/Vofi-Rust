import math, random, statistics as st
C=10e6; T=24; i=0.05/12
def bau(ek, costs):
    rest_ek=ek; kredit=0.0; zinsen=0.0
    for c in costs:
        z=kredit*i; zinsen+=z; kredit+=z      # Zins auf Vorperiodenstand, kapitalisiert
        use=min(rest_ek,c); rest_ek-=use; kredit+=c-use
    return zinsen, kredit
lin=[C/T]*T
z,k=bau(0.3*C,lin); print("ein Durchlauf: Zinsen %.2f, FK-Anteil %.4f %%"%(z, k/(C+z)*100))
ek=0.3*C
for it in range(1,50):
    z,k=bau(ek,lin); new=0.3*(C+z)
    if abs(new-ek)<0.005: break
    ek=new
z,k=bau(ek,lin); print("Fixpunkt: it=%d EK %.2f Zinsen %.2f FK %.4f %%"%(it,ek,z,k/(C+z)*100))
z0,_=bau(0,lin); print("100 %% Kredit: %.0f; Faustformel %.0f; Verhaeltnis Faust/EqFirst %.3f"%(z0,C*0.05*2*0.5,500000/z))
# alternative Konvention: Zins auf Stand nach Abfluss (vorschuessig)
def bau2(ek,costs):
    rest=ek;kr=0;zs=0
    for c in costs:
        use=min(rest,c);rest-=use;kr+=c-use; z=kr*i; zs+=z; kr+=z
    return zs,kr
print("Konvention Zins nach Abfluss, 100%% Kredit: %.0f"%bau2(0,lin)[0])
# Laufzahlen
for s in (0.02,0.03,0.05): print(s, (1.96*s/0.0005)**2, math.ceil((1.96*s/0.0005)**2))
print("Halbbreite 1000/3%%: %.2f bp"%(1.96*0.03/math.sqrt(1000)*1e4))
print("Standardfehler 1000/3%%: %.2f bp"%(0.03/math.sqrt(1000)*1e4))
# GewSt
print("GewSt", 0.035*2.0, 0.035*2.8)
# Annuitaet bei kleinen Zinsen
def ann(K,r,N): return K*r*(1+r)**N/((1+r)**N-1)
from fractions import Fraction as Fr
for r in (0.0001, 0.0001/12):
    N=10 if r==0.0001 else 120
    ex=Fr(100000)*Fr(r)*(1+Fr(r))**N/((1+Fr(r))**N-1)
    print("Annuitaet r=%g N=%d f64 %.10f exakt %.10f"%(r,N,ann(100000,r,N),float(ex)))
# NBank
for g,(d,z) in {"A":(40,40),"B":(60,20),"C":(70,10)}.items():
    print(g, d+z, "Entgelte in %% der zuw. Kosten:", round(d*0.01+z*0.0075,4))
# Mietniveau-Streuung
random.seed(1)
def lvl(mode,n=100000):
    out=[]
    for _ in range(n):
        L=1.0; e=random.gauss(0,0.015); g=0.02+e
        for t in range(10):
            if t>0:
                if mode=="iid": g=0.02+random.gauss(0,0.015)
                elif mode=="ar": e=0.7*e+math.sqrt(1-0.49)*random.gauss(0,0.015); g=0.02+e
            L*=1+g
        out.append(L)
    return st.pstdev(out)
for m in ("iid","ar","fix"): print(m, round(lvl(m)*100,2))
