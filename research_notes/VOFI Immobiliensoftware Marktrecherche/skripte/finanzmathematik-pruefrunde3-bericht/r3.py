from m import *
E5={t:F(5000) for t in range(1,6)}
nb=dict(betrag=F(232000),entgelt=F(2320),vkb=F(5,1000))
zus=dict(betrag=F(100000),entgelt=F(750))
for name,kw in [("Basis",{}),("TZ 35k",dict(tz={2:F(35000)})),("Disagio 3%",dict(disagio=F(3,100))),
  ("NBank+Entgelt+VKB",dict(nb=nb)),("Barzuschuss brutto + Entgelt",dict(zus=zus)),
  ("alles",dict(nb=nb,zus=zus,tz={2:F(35000)},disagio=F(3,100),ek={0:F(300000),2:F(50000)},entn=E5)),
  ("alles gerundet",dict(nb=nb,zus=zus,tz={2:F(35000)},disagio=F(3,100),ek={0:F(300000),2:F(50000)},entn=E5,rz=cent,rst=cent,rm=cent))]:
    EW,d=modell(check=True,**kw); print("%-30s EW %12.2f max|Abw| %s"%(name,EW,float(max(abs(x) for x in d))))
# Zuschuss netto als originaere Zahlung gebucht -> Doppelzaehlung
EW,d=modell(check=True,zus=zus)
print("Wird Zuschuss netto (99.250) als orig. Zahlung UND Entgelt 750 als einbehalten abgezogen: Abw t0 =", 750)
print("NBank Gruppe A: 5,8 Mio zuwf. -> Darlehen", 5.8e6*0.4, "Entgelt", 5.8e6*0.4*0.01, "Zuschussentgelt", 5.8e6*0.4*0.0075)
for g,(d_,z_) in dict(A=(40,40),B=(60,20),C=(70,10)).items(): print(g,d_+z_,"%  Entgelt %.3f%%"%(d_*0.01+z_*0.0075))
print("Restschuld nach 35 J bei linear 42 J:",7/42)
