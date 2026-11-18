import sys; sys.path.insert(0,'.')
from m3 import *
from fractions import Fraction as F
# Testfall
EW0=modell(); print('Basis',float(EW0), rendite(EW0,{0:F(400000)},{}), float(dEW(EW0,{0:F(400000)},{})))
ek={0:F(400000),2:F(50000)}
for name,en in [('t2/t2',{2:F(50000)}),('t2/t3',{3:F(50000)})]:
    EW=modell(ek=ek,entn=en)
    print(name,float(EW),rendite(EW,ek,en),float(dEW(EW,ek,en)))
# gerundet nach Nr.10
EW=modell(ek=ek,entn={3:F(50000)},rz=cent,rst=cent,rm=cent); print('t2/t3 gerundet',float(EW))
# Restwert-Doppelzaehlung: Restschuld zusaetzlich vom Erloes abgezogen
# Restschuld t=5 bestimmen
K=F(700000)
for t in range(1,6): K-= F(42000)-K*F(4,100)
print('Restschuld t5',float(K))
EWd=EW0-K
print('EW bei doppeltem Abzug',float(EWd),'Restschuld nach Abloesung',0)
# Grobkalkulation Bankgrenze
miete=134640; noi=miete*0.8; ds=noi/1.2; L=ds/0.06; P=L/0.65
print('NOI',noi,'DS',ds,'L',L,'P',P)
print('DSCR 2.6',noi/(0.65*2.6e6*0.06))
