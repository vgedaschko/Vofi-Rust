"""Eigene Gegenrechnung: S1 mit Varianten, Rendite-Lesart bei Entnahmen."""
from fractions import Fraction as F

def s1(ek0=400000, entn=0, kk_rate=F(8,100), h=F(2,100), s=F(30,100), extra_ek=None):
    extra_ek = extra_ek or {}
    i=F(4,100); K=F(700000); annu=F(42000)
    G=F(0); KK=F(0)
    # t=0
    cash = -1100000 + ek0 + 700000
    if cash>=0: G=F(cash)
    else: KK=F(-cash)
    for t in range(1,6):
        rent = F(55000)*F(102,100)**(t-1)
        zins = K*i; tilg = annu-zins
        hz = G*h; kz = KK*kk_rate
        bmg = rent-17600-zins-kz+hz
        tax = bmg*s
        K -= tilg
        sale = 0; abl = 0
        if t==5: sale=1150000; abl=K; K=F(0)
        flow = rent + hz + sale - zins - tilg - abl - kz - tax - entn + extra_ek.get(t,0)
        # Bestand fortschreiben (Guthaben und KK, Zinsen auf Vorperiode bereits gezahlt)
        net = G - KK + flow
        G, KK = (net, F(0)) if net>=0 else (F(0), -net)
    return G-KK-K

def root(x,n): return float(x)**(1/n)-1
q = 1+F(2,100)*F(70,100)
base = s1()
print("EW Basis", float(base), "r", root(base/400000,5))
EWe = s1(entn=5000)
print("EW Entnahme", float(EWe))
EWO = 400000*q**5
print("EW Alternative", float(EWO), " dEW naiv", float(EWe-EWO), " r naiv", root(EWe/400000,5))
EWOm = EWO - sum(5000*q**(5-t) for t in range(1,6))
print("dEW gespiegelt", float(EWe-EWOm), " Differenz zu naiv", float(EWOm-EWO+0) )
aufg = sum(5000*q**(5-t) for t in range(1,6))
print("r Lesart Bericht (Entnahmen zum Alternativzins aufgezinst):", root((EWe+aufg)/400000,5))
# Lesart b: IRR
def irr_b(EW, entn):
    lo,hi=0.0,0.5
    for _ in range(200):
        r=(lo+hi)/2
        v=400000*(1+r)**5 - float(EW) - sum(entn*(1+r)**(5-t) for t in range(1,6))
        if v<0: lo=r
        else: hi=r
    return r
print("r Lesart b (IRR EK-Reihe):", irr_b(EWe,5000))
# KK-Variante: 380k EK, mit und ohne Entnahme
kk0 = s1(ek0=380000); kke = s1(ek0=380000, entn=5000)
print("KK-Var EW", float(kk0), " mit Entnahme", float(kke))
print(" r ohne Entn", root(kk0/380000,5), " r Lesart Bericht mit Entn", root((kke+aufg)/380000,5))
EWO38 = 380000*q**5; EWO38m = EWO38 - aufg
print(" dEW gesp. ohne/mit", float(kk0-EWO38), float(kke-EWO38m))
# Konsistenz Vorzeichen: r>r_alt <=> dEW_gesp>0 (algebraisch: (EW+A)/EK > q^n <=> EW > EKq^n - A)
# Gestaffelte Einlage: 400k t0 + Nachschuss 50k in t=2
EWn = s1(extra_ek={2:50000})
print("Nachschuss 50k t=2: EW", float(EWn))
print("  (EW/Summe EK)^(1/5)-1 =", root(EWn/450000,5))
print("  EK-Barwert zum Alternativzins:", root(EWn/(400000+50000/q**2),5))
print("  Nachschuss aufgezinst und vom EW abgezogen:", root((EWn-50000*q**3)/400000,5))
lo,hi=0.0,0.5
for _ in range(200):
    r=(lo+hi)/2; v=400000*(1+r)**5+50000*(1+r)**3-float(EWn)
    lo,hi=(r,hi) if v<0 else (lo,r)
print("  IRR der EK-Reihe:", r)
print("  dEW gespiegelt:", float(EWn-(400000*q**5+50000*q**3)))
