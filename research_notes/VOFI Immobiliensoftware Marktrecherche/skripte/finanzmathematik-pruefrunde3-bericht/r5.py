from m import *
for z in (F(4,100),):
    EW=modell(h=z,kk=z,i=z); qq=1+z*F(7,10); d=EW-400000*qq**5
    kw=-1100000+sum((F(55000)*F(102,100)**(t-1)*F(7,10)+F(3,10)*17600)/qq**t for t in range(1,6))+F(1150000)/qq**5
    print("einheitlich: dEW/q5 %.2f KW %.2f diff %.8f"%(d/qq**5,kw,float(d/qq**5-kw)))
EW=modell(); d=EW-400000*q**5
kw=-1100000+sum((F(55000)*F(102,100)**(t-1)*F(7,10)+F(3,10)*17600)/q**t for t in range(1,6))+F(1150000)/q**5
print("Testfall dEW/q5 %.2f KW %.2f"%(d/q**5,kw))
# Bauzeit
C=10_000_000; T=24; m=0.05/12
def lauf(ek):
    rest=ek; kr=0.0; zs=0.0
    for _ in range(T):
        z=kr*m; zs+=z; kr+=z
        u=min(rest,C/T); rest-=u; kr+=C/T-u
    return zs,kr
z,k=lauf(.3*C); print("1 DL %.2f FK %.4f%%"%(z,100*k/(C+z)))
ek=.3*C; n=0
while True:
    n+=1; z,k=lauf(ek); neu=.3*(C+z)
    if abs(neu-ek)<0.5: break
    ek=neu
print("DL",n+1,"EK %.2f Z %.2f FK %.4f%%"%(ek,z,100*k/(C+z)), "voll %.2f Faktor %.3f"%(lauf(0)[0],500000/z))
for it in range(1,8):
    pass
ek=.3*C
for it in range(1,8):
    z,k=lauf(ek); print(" Durchlauf",it,"EK %.2f Zins %.2f FK %.4f%%"%(ek,z,100*k/(C+z))); ek=.3*(C+z)
print("Restwert", 100000*22.2, 80000/.045, 80000/.045/1.07, 100000/.045/(80000/.045), (100000/.045)/(80000/.045/1.07))
print("AfA",800000*.02,800000*.05," GewSt",3.5*2,3.5*2.8," SoAfA",4900*1.1)
print("Umlage",(40000*.6-12000)*.08,(40000-12000)*.08,((40000-12000)*.08-(40000*.6-12000)*.08)/70/12)
