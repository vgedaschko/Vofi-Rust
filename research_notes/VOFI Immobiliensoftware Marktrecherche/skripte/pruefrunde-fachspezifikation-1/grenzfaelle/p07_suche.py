import sys; sys.path.insert(0,"rr")
from decimal import Decimal as D
from zahlen import Rundung
rd=Rundung("cent")
b=420
treffer=[]
for v in range(1,420):
    for zc in range(1708000*100, 1708000*100+5000):
        Z=D(zc)/100
        a=rd.geld(Z*D(v)/D(b)); c=rd.geld(Z*(D(v)/D(b)))
        if a!=c: treffer.append((str(Z),v,str(a),str(c)))
    if len(treffer)>3: break
print(treffer[:5])
