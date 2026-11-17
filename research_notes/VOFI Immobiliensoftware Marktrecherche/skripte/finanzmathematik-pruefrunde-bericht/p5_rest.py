from fractions import Fraction as F
def s1(idx0=0):
    i=F(4,100);K=F(700000);G=F(0)
    for t in range(1,6):
        rent=F(55000)*F(102,100)**(t-1+idx0); z=K*i; tl=42000-z; hz=G*F(2,100)
        tax=(rent-17600-z+hz)*F(3,10); K-=tl
        G+=rent-z-tl-tax+hz
    return G+1150000-K
ew=s1(); ew2=s1(1)
print("EW", float(ew), "Vorjahreslesart EW", float(ew2), "r", (float(ew2)/400000)**0.2-1)
q=F(1014,1000); dEW=ew-400000*q**5
kw=-1100000+sum((F(55000)*F(102,100)**(t-1)*F(7,10)+F(3,10)*17600)/q**t for t in range(1,6))+F(1150000)/q**5
print("dEW/q^5 %.2f  KW(1,4%%) %.2f  Diff %.2f"%(float(dEW/q**5), float(kw), float(dEW/q**5-kw)))
print("DSCR5", float(F(55000)*F(102,100)**4/42000), float(F(55000)*F(102,100)**4/(42000+F(62417148416,100000))))
