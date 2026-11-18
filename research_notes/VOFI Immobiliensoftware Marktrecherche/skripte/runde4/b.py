# Grobkalkulation-Modell (Jahresraster), nur zur Pruefung der Monotonie / Eindeutigkeit
def run(P, ltv=0.65, cap=None, rent=134640., cost=0.2, i=0.04, tilg=0.02, g=0.02, s=0.30,
        nk=0.07, geb=0.8, afa=0.02, fak=18.0, n=10, h=0.02, kk=0.08, hk=0.03):
    L = ltv*P if cap is None else min(ltv*P, cap)
    E = P*(1+nk) - L
    ann = (i+tilg)*L; K=L; G=0.; KK=0.; vv=0.
    for t in range(1,n+1):
        m = rent*(1+g)**(t-1); noi = m*(1-cost)
        z = K*i; tl = min(ann-z, K); hz=G*h; kz=KK*kk
        bm = noi - z - P*(1+nk)*geb*afa + hz - kz
        # Verlustvortrag
        if bm<0: vv += -bm; st=0
        else:
            use=min(vv,bm); vv-=use; st=(bm-use)*s
        K -= tl
        flow = noi - z - tl - st + hz - kz
        if t==n:
            flow += fak*rent*(1+g)**n*(1-hk) - K; K=0
        net=G-KK+flow; G,KK=(net,0.) if net>=0 else (0.,-net)
    EW=G-KK; q=1+h*(1-s)
    r = (EW/E)**(1/n)-1 if EW>0 else -1
    return r, EW, E, L
import numpy as np
if __name__!="__main__": pass
Ps=np.arange(1.0e6,4.0e6,1e4); rs=[run(p)[0] for p in Ps]
print('monoton fallend:', all(np.diff(rs)<0))
def solve(f,target,lo=5e5,hi=6e6):
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)>=target: lo=mid
        else: hi=mid
    return lo
for tgt in (0.05,0.06,0.07,0.08):
    PR=solve(lambda p: run(p)[0], tgt)
    PRc=solve(lambda p: run(p,cap=1.496e6)[0], tgt)
    print(f'Ziel {tgt:.0%}: Renditegrenze {PR:,.0f}; mit Kreditdeckel 1,496 Mio {PRc:,.0f}; min(PR,PB)={min(PR,2301538):,.0f}')
for p in (2.3e6,2.6e6):
    print(p, 'volle Quote', run(p)[0], 'gedeckelt', run(p,cap=1.496e6)[0], run(p,cap=1.496e6)[2])
# Ruecklaeufigkeit bei Zielwertsuche auf Beleihungsquote
for l in np.arange(0.5,0.96,0.05): print(round(l,2), round(run(2.3e6,ltv=l)[0],5))
