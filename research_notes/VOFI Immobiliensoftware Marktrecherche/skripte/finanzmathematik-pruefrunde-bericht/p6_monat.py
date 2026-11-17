from fractions import Fraction as F
K=F(700000);G=F(0)
for y in range(1,6):
    rent=F(55000)*F(102,100)**(y-1); sz=hz=F(0)
    for m in range(12):
        h=G*F(2,1200); z=K*F(4,1200); tl=3500-z; K-=tl; sz+=z; hz+=h
        G+=h+rent/12-3500
    G-=(rent-17600-sz+hz)*F(3,10)
EW=G+1150000-K
print("Monats-EW %.2f  Diff %.2f  Abloesung %.2f"%(EW, EW-F(58436628157064,100000000), K))
