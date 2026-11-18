from s1 import *
def w_fac(p,n,h=D("0.02"),s=D("0.3")):
    f=r12((1+h*(1-s))**(D(1)/D(p)))
    return lambda t: f**(p*n-t)
def rend(EW, ein, ent, p, n=5):
    w=w_fac(p,n); Z=EW+sum(a*w(u) for u,a in ent.items()); Dn=sum(e*w(u) for u,e in ein.items())/w(0)
    return (Z/Dn)**(D(1)/n)-1, Z, Dn
for p in (12,):
    EW,EWU,_=testfall(p=p); print("Basis", EW, EW-EWU, rend(EW,{0:D(400000)},{},p)[0])
    EW,EWU,_=testfall(p=p, entnahmen={30:D(10000)}); print("Entn M30", EW, EW-EWU, rend(EW,{0:D(400000)},{30:D(10000)},p)[0])
    for mE in (13,14,24):
        ein={13:D(50000)}; ent={mE:D(50000)}
        if mE==13: ein={}; ent={}
        EW,EWU,_=testfall(p=p, einlagen=ein, entnahmen=ent)
        e0={0:D(400000)}; e0.update(ein)
        print("Nachschuss M13, Entnahme M",mE, EW, EW-EWU, rend(EW,e0,ent,p)[0])
# Jahresmodus Eigenschaft 3 exakt?
EW,EWU,_=testfall(p=1, entnahmen={k:D(5000) for k in range(1,6)}); print("Jahr Entn", EW, EW-EWU, rend(EW,{0:D(400000)},{k:D(5000) for k in range(1,6)},1)[0])
