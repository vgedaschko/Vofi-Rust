"""Bestandssaldo-Kontrollsumme laut Bericht bei Tilgungszuschuss (S1, 5 % von 700.000 in t=2 als Sondertilgung ohne Geldfluss)."""
from fractions import Fraction as F
i=F(4,100);K=F(700000);G=F(0);prevB=-K;TZ={2:F(35000)}
for t in range(1,6):
    rent=F(55000)*F(102,100)**(t-1); z=K*i; tl=min(F(42000)-z,K); hz=G*F(2,100)
    tax=(rent-17600-z+hz)*F(3,10); K-=tl; K-=TZ.get(t,0)
    sale=abl=0
    if t==5: sale=1150000; abl=K; K=F(0)
    Z=rent+sale
    G+=Z+hz-z-tl-abl-tax
    B=G-K
    rhs=Z+0-z+hz-tax
    print(t, "dB=%.2f  Z+EK-Soll+Haben-Steuer=%.2f  Abw=%.2f"%(float(B-prevB),float(rhs),float(B-prevB-rhs)))
    prevB=B
print("EW", float(B))
