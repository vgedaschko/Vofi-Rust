from m import *
E0={0:F(400000)}
EW=modell(); print("Basis EW %.4f dEW %.2f r %.4f%%"%(EW,dEW(EW,E0,{}),100*rendite(EW,E0,{})))
E5={t:F(5000) for t in range(1,6)}
EWe=modell(entn=E5); print("Entn EW %.2f r %.4f%% ungespiegelt dEW %.2f naiv r %.4f%%"%(EWe,100*rendite(EWe,E0,E5),EWe-400000*q**5,100*((float(EWe)/400000)**.2-1)))
a=modell(ek={0:F(380000)}); b=modell(ek={0:F(380000)},entn=E5); a0=modell(ek={0:F(380000)},kk=F(0))
print("KK EW %.2f r %.4f%% mitE %.4f%% ohneKKZins diff %.2f"%(a,100*rendite(a,{0:380000},{}),100*rendite(b,{0:380000},E5),a0-a))
en={0:F(400000),2:F(50000)}; EWn=modell(ek=en)
print("Nachschuss EW %.2f dEW %.2f r %.4f%% SummeEK %.4f%% negEntn %.4f%%"%(EWn,dEW(EWn,en,{}),100*rendite(EWn,en,{}),100*((float(EWn)/450000)**.2-1),100*((float(EWn-50000*q**3)/400000)**.2-1)))
lo,hi=0.0,.5
for _ in range(200):
    r=(lo+hi)/2; v=400000*(1+r)**5+50000*(1+r)**3-float(EWn); lo,hi=(r,hi) if v<0 else (lo,r)
print("  IRR %.4f%%"%(100*r))
# Saldierung: gleiche Periode
W2={2:F(50000)}; EWg=modell(ek=en,entn=W2)
print("E=W t=2: EW %.2f saldiert %.4f%% brutto %.4f%% dEW %.2f"%(EWg,100*rendite(EWg,en,W2),100*rendite(EWg,en,W2,saldo=False),dEW(EWg,en,W2)))
# Verschiebung um eine Periode
W3={3:F(50000)}; EWs=modell(ek=en,entn=W3)
print("E t=2, W t=3: EW %.2f r %.4f%% dEW %.2f"%(EWs,100*rendite(EWs,en,W3),dEW(EWs,en,W3)))
W25={2:F(49000)}; EWx=modell(ek=en,entn=W25)
print("E 50k t=2, W 49k t=2: r %.4f%%  dEW %.2f"%(100*rendite(EWx,en,W25),dEW(EWx,en,W25)))
# Alternative: Barwert der Nettoreihe im Nenner
def r_pv(EW,ek,entn):
    P=sum(v*q**(-t) for t,v in ek.items())-sum(v*q**(-t) for t,v in entn.items()); return float(EW/P)**.2-1
print("Nettobarwert-Formel: Basis %.4f%%  E=W t2 %.4f%%  E t2/W t3 %.4f%%  Entn5k %.4f%%"%(100*r_pv(EW,E0,{}),100*r_pv(EWg,en,W2),100*r_pv(EWs,en,W3),100*r_pv(EWe,E0,E5)))
# Miete als Vorjahreswert
EWv=modell(miete0=F(55000)*F(102,100)); print("Miete Vorjahr r %.4f%% diff %.4f"%(100*rendite(EWv,E0,{}),100*(rendite(EWv,E0,{})-rendite(EW,E0,{}))))
# Randfall
print("Randfall -36.9:", 100*(0.1**.2-1))
# DSCR
K=700000.; tl=0
for t in range(1,6):
    z=K*.04; K-=42000-z
print("DSCR J5 %.3f mit Abloesung %.4f Restschuld %.2f"%(55000*1.02**4/42000,55000*1.02**4/(42000+K),K))
print("Kirchner r %.4f%%"%(100*((1322.48/1000)**(1/3)-1)))
print("eff. Vergleichszins %.5f%%"%(100*((1+0.014/12)**12-1)))
