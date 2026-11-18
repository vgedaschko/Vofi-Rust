import sys; sys.path.insert(0,"rr")
from decimal import Decimal as D
from dataclasses import replace
from zahlen import Rundung
import annahmen as A
from grobkalkulation import rechne_grob
rd=Rundung("cent")
gef=None
for i in range(0,101):
    bgf=D("2600")+D(i)/100
    for j in range(0,200):
        kw=D("2900")+D(j)/100
        bau=rd.geld(bgf*kw); zk=bau+D(1000000); Z=rd.geld(D("0.2")*zk)
        if rd.geld(Z*2/D(420))!=rd.geld(Z*(D(2)/D(420))):
            gef=(bgf,kw,bau,Z); break
    if gef: break
print("Eingabe:",gef)
bgf,kw,bau,Z=gef
e=rechne_grob(replace(A.NEUBAU, foerderung=A.FOERDERUNG_B, bgf=bgf, kostenkennwert=kw, bauzeit_monate=14, haltedauer=36), A.VORGABEN_NEUBAU)
print("Zuschuss",e.bemessung.zuschuss,"Rueckzahlung",e.verkauf.foerder_rueckzahlung,"Proben",e.befunde)
