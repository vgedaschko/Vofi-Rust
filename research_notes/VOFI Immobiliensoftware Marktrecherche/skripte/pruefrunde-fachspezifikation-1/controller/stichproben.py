# Eigene Stichproben des Controllers, ohne Module des Referenzrechners
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_FLOOR, getcontext
getcontext().prec=50
c=lambda x: x.quantize(D("0.01"),ROUND_HALF_UP)
r12=lambda x: x.quantize(D("1E-12"),ROUND_HALF_UP)
print("== Stichprobe 1: RF-11 Ankauf, Ertrag, Bankdarlehen, Verkauf, Steuer auf Verkaufsgewinn")
fl=D(1320); ist=D("8.50"); markt=D("9.20"); g=D("0.02"); d=4; kap=D("0.15")
idx=[None,D(1)]
for j in range(2,16): idx.append(r12(idx[-1]*(1+g)))
miete=[None]
for j in range(1,15):
    mj=markt*idx[j]
    pfad=ist+(mj-ist)*min(D(1),D(j-1)/d)
    basis=miete[j-3] if j>3 else ist
    miete.append(min(pfad,basis*(1+kap)))
print("Miete 1..6:",[str(m.quantize(D('0.0001'))) for m in miete[1:7]])
# Jahr 1
soll=c(fl*miete[1]); ein=c(soll*D("0.98")); print("Soll/Einz Monat",soll,ein,"Jahr",ein*12)
best=(20*D(350)+fl*D(14)+fl*D(2)); k_m=c(best/12)+c(D("0.60")*fl/12)
re=ein*12-k_m*12; print("Kosten Monat",k_m,"Reinertrag VJ",re)
B=(re/D("1.2")/D("0.06")).quantize(D("0.01"),ROUND_FLOOR)
while D("1.2")*12*c(B*D("0.06")/12)>re: B-=D("0.01")
print("B",B,"Rate",c(B*D("0.06")/12),"A",D("0.65")*2400000,"Deckung",re/(12*c(B*D("0.06")/12)))
L=B; EK=D(2640000)-L; print("EK",EK)
soll13=c(fl*miete[13]); vp=c(D(18)*soll13*12); vk=c(vp*D("0.015")); erl=vp-vk
print("Miete13",miete[13].quantize(D('0.0001')),"Verkaufspreis",vp,"Kosten",vk,"Erloes",erl)
bw=D(2640000)-12*c(D(1980000)*D("0.02")); gv=erl-bw; print("Buchwert",bw,"g_v",gv)
kst=c(gv*D("0.10")*D("1.055")); ge=(gv/100).to_integral_value(ROUND_FLOOR)*100; gew=c(c(ge*D("0.035"))*4)
print("KSt+Soli auf g_v",kst,"GewSt",gew,"zusammen",kst+gew,"(Dok.: 272.999,11 / GewSt 155.680)")
print("== Stichprobe 2: RF-10 Personengesellschaft, Tabelle R-7.9")
def pg(gewinn,heb,est=D("0.42"),anteil=D(1)):
    ge=max(D(0),(gewinn/100).to_integral_value(ROUND_FLOOR)*100-24500)
    mb=c(ge*D("0.035")); gs=c(mb*heb); es=c(est*gewinn)
    an=min(anteil*4*mb,anteil*gs,anteil*es); return ge,mb,gs,c(an),es+gs-c(an)
for args in [(D(400)/100,),(D("2.8"),),(D("4.8"),),(D(4),D("0.42"),D("0.5")),(D(4),D("0.08"))]:
    print(args,[str(x) for x in pg(D(100000),*args)])
print("== Stichprobe 3: RF-12 Grobfoerderung und Rueckzahlung")
bk=c(D(2600)*D(2900)); P=D(1200000); enk=c(P*D("0.08"))
zk=min(bk,D(5460)*2000)+min(P+enk,D(400)*2500)
fd=c(D("0.6")*zk); zs=c(D("0.2")*zk); em=c(D("0.2")*zk); ent=c(fd*D("0.01"))+c(zs*D("0.0075"))
M=P+enk+bk+ent
print("Baukosten",bk,"zk",zk,"FD",fd,"Zuschuss",zs,"EKmin",em,"Entgelte",ent,"M",M,"C",M-fd-zs-em)
print("Rueckzahlung nach 240 Mon.", c(zs*D(18+420-240)/420))
print("Gesamtkosten fuer Wertansatz",P+enk+bk,"A=0.65*W-FD",D("0.65")*(P+enk+bk)-fd)
