"""Runde 3: Testfall neu, exakte Brueche, optionale Rundung nach A.2 Nr. 10, Kontrollsumme Nr. 22/23."""
from fractions import Fraction as F
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_DOWN
def cent(x, mode=ROUND_HALF_UP):
    d = D(x.numerator)/D(x.denominator)
    return F(str(d.quantize(D("0.01"), mode)))
def euro_ab(x):
    d = D(x.numerator)/D(x.denominator); return F(str(d.quantize(D("1"), ROUND_DOWN)))
ID = lambda x: x
def modell(ek=None, entn=None, kk=F(8,100), h=F(2,100), i=F(4,100), s=F(3,10), miete0=F(55000),
           rz=ID, rst=ID, rm=ID, tz=None, disagio=F(0), check=False, nb=None, zus=None):
    """nb: NBank-Tranche dict(betrag, entgelt, vkb) in t=0 voll ausgezahlt, 0 % Zins, VKB auf Restschuld,
       Tilgung linear 1/42 je Jahr. zus: Barzuschuss dict(betrag, entgelt) in t=0 (originaere Zahlung brutto)."""
    ek = ek or {0:F(400000)}; entn = entn or {}; tz = tz or {}
    K = F(700000); annu = F(42000)
    NB = F(0); vkb=F(0); einb0 = K*disagio
    cash0 = -1100000 + ek.get(0,0) - entn.get(0,0) + K*(1-disagio)
    if nb:
        NB = F(nb['betrag']); cash0 += NB - nb['entgelt']; einb0 += nb['entgelt']
    zus_brutto = 0
    if zus:
        zus_brutto = F(zus['betrag']); cash0 += zus_brutto - zus['entgelt']; einb0 += zus['entgelt']
    G, KK = (F(cash0), F(0)) if cash0 >= 0 else (F(0), F(-cash0))
    Bp = G - KK - K - NB
    devs = []
    if check:
        rhs = -1100000 + zus_brutto + ek.get(0,0) - entn.get(0,0) - einb0
        devs.append(Bp - rhs)
    for t in range(1,6):
        miete = rm(miete0*F(102,100)**(t-1))
        z = rz(K*i); tl = annu - z
        hz = rz(G*h); kz = rz(KK*kk)
        v = rz(NB*nb['vkb']) if nb else F(0)
        tlnb = F(nb['betrag'])/42 if nb else F(0)
        bmg = miete - 17600 - z - kz + hz - v
        st = rst(bmg*s)
        K -= tl; K -= tz.get(t,0); NB -= tlnb
        verk = abl = 0
        if t == 5: verk = 1150000; abl = K + NB; K = F(0); NB = F(0)
        flow = miete + hz + verk - z - tl - tlnb - abl - kz - v - st - entn.get(t,0) + ek.get(t,0)
        net = G - KK + flow
        G, KK = (net, F(0)) if net >= 0 else (F(0), -net)
        B = G - KK - K - NB
        if check:
            rhs = miete + verk + ek.get(t,0) - entn.get(t,0) - (z + kz + v) + hz - st + tz.get(t,0)
            devs.append((B-Bp) - rhs)
        Bp = B
    EW = G - KK
    return (EW, devs) if check else EW
q = 1 + F(2,100)*F(7,10)
def rendite(EW, ek, entn, N=5, n=5, qq=q, saldo=True):
    ek = dict(ek); entn = dict(entn)
    if saldo:
        for t in set(ek)|set(entn):
            s_ = ek.get(t,0) - entn.get(t,0)
            ek[t] = max(s_,0); entn[t] = max(-s_,0)
    Z = EW + sum(v*qq**(N-t) for t,v in entn.items())
    Nn = sum(v*qq**(-t) for t,v in ek.items())
    if Nn == 0: return None
    if Z <= 0: return -1.0
    return float(Z/Nn)**(1/n) - 1
def dEW(EW, ek, entn, N=5, qq=q):
    return EW - (sum(v*qq**(N-t) for t,v in ek.items()) - sum(v*qq**(N-t) for t,v in entn.items()))
