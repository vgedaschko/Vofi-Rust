C=10_000_000; T=24; m=0.05/12
def lauf(ek, nach_abfluss=False):
    rest=ek; kr=0.0; zs=0.0
    for _ in range(T):
        if not nach_abfluss:
            z=kr*m; zs+=z; kr+=z
        use=min(rest,C/T); rest-=use; kr+=C/T-use
        if nach_abfluss:
            z=kr*m; zs+=z; kr+=z
    return zs, kr
z,k=lauf(0.3*C); print("1 Durchlauf: Zins %.2f FK %.4f%%" % (z, 100*k/(C+z)))
ek=0.3*C
for it in range(1,30):
    z,k=lauf(ek); neu=0.3*(C+z)
    if abs(neu-ek)<0.01: break
    ek=neu
print("Fixpunkt nach %d: EK %.2f Zins %.2f FK %.4f%%" % (it, ek, z, 100*k/(C+z)))
print("voll Kredit Vormonat %.0f, nach Abfluss %.0f, Faustformel %.0f, Faktor %.3f" % (lauf(0)[0], lauf(0,True)[0], C*0.05*2/2, 500000/z))
for g,(d,zu) in dict(A=(40,40),B=(60,20),C=(70,10)).items():
    print("NBank", g, d+zu, "%% ; Entgelt %.3f%%" % (d*0.01+zu*0.0075))
# Mietrecht-Beispiel Abschnitt 6
print("Umlage", (40000*0.6-12000)*0.08, (40000-12000)*0.08, ((40000-12000)*0.08-(40000*0.6-12000)*0.08)/70/12, 12000*0.08)
print("Restwert", 100000/0.045, 100000*0.8/0.045, (100000/0.045)/(80000/0.045))
