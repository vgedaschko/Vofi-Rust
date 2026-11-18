from rf11 import *
bad=[]
prev=None
for P in list(range(1,2317236,997))+[2317235]:
    o=rechne(BASIS,P=P)
    if o["EU"]<0: bad.append(P)
print("verfehlt unter P*:",bad[:10])
for d in [-20000,-10000,0,10000,20000]:
    o=rechne(BASIS,P=1887092+d); print(d, round(float(o["r"])*100,4), o["L"])
rs=[float(rechne(BASIS,P=P)["r"]) for P in range(1500000,3600001,100000)]
print("streng fallend 100k:", all(a>b for a,b in zip(rs,rs[1:])))
# Monotonie in 1-Euro-Schritten im Bereich um P*
cnt=0; last=None; wech=[]
for P in range(2310000,2325000):
    e=rechne(BASIS,P=P)["EU"]>=0
    if last is not None and e!=last: wech.append(P)
    last=e
print("Wechsel 2,310-2,325 Mio:",wech)
