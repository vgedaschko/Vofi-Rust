"""Runde 2: eigenes Modell des Testfalls (exakte Brüche), Rendite, Kontrollsumme."""
from fractions import Fraction as F
from math import isclose

def modell(ek={0:400000}, entn={}, kk=F(8,100), h=F(2,100), i=F(4,100), s=F(3,10),
           tz={}, disagio=F(0), rnd=None, check=False):
    """Jahresraster, Zahlungen am Periodenende. tz: Tilgungszuschuss je t (ohne Geldfluss).
    disagio: Anteil vom Nennbetrag, einbehalten. rnd: Rundungsfunktion für Zins/Steuer."""
    R = rnd or (lambda x: x)
    K = F(700000); annu = F(42000)
    cash0 = -1100000 + ek.get(0,0) + K*(1-disagio)
    G, KK = (F(cash0), F(0)) if cash0 >= 0 else (F(0), F(-cash0))
    B_prev = G - KK - K
    if check:
        rhs = -1100000 + ek.get(0,0) - entn.get(0,0) - K*disagio
        dev0 = B_prev - rhs
        devs=[dev0]
    for t in range(1,6):
        miete = F(55000)*F(102,100)**(t-1)
        z = R['zins'](K*i) if rnd else K*i
        tl = annu - z
        hz = R['zins'](G*h) if rnd else G*h
        kz = R['zins'](KK*kk) if rnd else KK*kk
        bmg = miete - 17600 - z - kz + hz
        st = R['steuer'](bmg*s) if rnd else bmg*s
        K -= tl
        K -= tz.get(t,0)
        verk = abl = 0
        if t == 5: verk = 1150000; abl = K; K = F(0)
        orig = miete - 17600 + 17600*0 + verk  # Mietüberschuss ist hier 55000-Bewirtschaftung? s.u.
        flow = miete + hz + verk - z - tl - abl - kz - st - entn.get(t,0) + ek.get(t,0)
        net = G - KK + flow
        G, KK = (net, F(0)) if net >= 0 else (F(0), -net)
        B = G - KK - K
        if check:
            orig = miete + verk
            rhs = orig + ek.get(t,0) - entn.get(t,0) - z - kz + hz - st + tz.get(t,0)
            devs.append((B - B_prev) - rhs)
        B_prev = B
    EW = G - KK
    return (EW, devs) if check else EW

q = 1 + F(2,100)*F(7,10)
def rendite(EW, ek, entn, N=5, n=5, qq=q):
    zaehler = EW + sum(v*qq**(N-t) for t,v in entn.items())
    nenner = sum(v*qq**(-t) for t,v in ek.items())
    return (float(zaehler/nenner))**(1/n) - 1
def dEW(EW, ek, entn, N=5, qq=q):
    alt = sum(v*qq**(N-t) for t,v in ek.items()) - sum(v*qq**(N-t) for t,v in entn.items())
    return EW - alt

if __name__ == "__main__":
    EW = modell(); print("Basis EW %.2f dEW %.2f r %.4f%%" % (EW, dEW(EW,{0:400000},{}), 100*rendite(EW,{0:400000},{})))
    E5 = {t:5000 for t in range(1,6)}
    EWe = modell(entn=E5); print("Entnahme EW %.2f dEW %.2f r %.4f%%  naiv r %.4f%% naiv dEW %.2f" % (EWe, dEW(EWe,{0:400000},E5), 100*rendite(EWe,{0:400000},E5), 100*((float(EWe)/400000)**0.2-1), EWe-400000*q**5))
    for e0 in (380000,):
        a = modell(ek={0:e0}); b = modell(ek={0:e0}, entn=E5)
        print("KK-Var EW %.2f r %.4f%%  mit Entn EW %.2f r %.4f%%" % (a, 100*rendite(a,{0:e0},{}), b, 100*rendite(b,{0:e0},E5)))
        a0 = modell(ek={0:e0}, kk=F(0)); print("  ohne KK-Zins (KK-Zins 0) EW %.2f diff %.2f" % (a0, a0-a))
    ekn = {0:400000, 2:50000}; EWn = modell(ek=ekn)
    print("Nachschuss EW %.2f dEW %.2f r_empf %.4f%%" % (EWn, dEW(EWn,ekn,{}), 100*rendite(EWn,ekn,{})))
    print("  Summe EK %.4f%%  neg.Entn %.4f%%" % (100*((float(EWn)/450000)**0.2-1), 100*((float(EWn-50000*q**3)/400000)**0.2-1)))
    lo,hi=0.0,0.5
    for _ in range(200):
        r=(lo+hi)/2; v=400000*(1+r)**5+50000*(1+r)**3-float(EWn); lo,hi=(r,hi) if v<0 else (lo,r)
    print("  IRR EK-Reihe %.4f%%" % (100*r))
    # Brutto/Netto in gleicher Periode
    ekg={0:400000,2:50000}; eng={2:50000}; EWg=modell(ek=ekg, entn=eng)
    print("Einlage=Entnahme 50k in t=2: EW %.2f  netto r %.4f%%  brutto r %.4f%%  dEW %.2f" % (EWg, 100*rendite(EWg,{0:400000},{}), 100*rendite(EWg,ekg,eng), dEW(EWg,ekg,eng)))
    # Randfall: EW<=0 aber Zähler>0
    print("Randfall: EW=-10000, aufgez. Entnahmen 50000, EK 400000 ->", 100*((40000/400000)**0.2-1))
    # Schwelle im Monatsraster
    qm = 1 + F(2,100)*F(7,10)/12
    print("Monatsraster: Schwelle effektiv %.5f%% gegen nominal 1.4%%" % (100*(float(qm)**12-1)))
    # Kontrollsumme Nr. 23
    for kw in [dict(), dict(tz={2:35000}), dict(disagio=F(3,100)), dict(tz={2:35000},disagio=F(3,100),ek={0:400000,2:50000},entn=E5), dict(ek={0:380000},entn=E5,disagio=F(3,100))]:
        EWk, devs = modell(check=True, **kw)
        print("Kontrolle", {k:(str(v) if not isinstance(v,dict) else v) for k,v in kw.items()}, "max|Abw| =", float(max(abs(d) for d in devs)))
