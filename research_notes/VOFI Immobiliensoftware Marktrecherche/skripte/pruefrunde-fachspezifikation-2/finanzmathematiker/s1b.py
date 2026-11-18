# Unabhaengiger Nachbau Testfall S1 allein aus dem Text der Fachspezifikation (+ Eingaben aus Bericht A.6)
from decimal import Decimal as D, getcontext, ROUND_HALF_UP, ROUND_DOWN
getcontext().prec = 50
C = D("0.01")
def r(x): return x.quantize(C, rounding=ROUND_HALF_UP)
def r12(x): return x.quantize(D("1e-12"), rounding=ROUND_HALF_UP)
def konf(x, p):  # R-2.6
    if p == 1 or NOMINAL: return x/p
    return r12((1+x) ** (D(1)/D(p)) - 1)

def testfall(p=12, h=D("0.02"), aL=None, s=D("0.30"), EK=D(400000), einlagen=None, entnahmen=None,
             verkauf=D(1150000), kk=D("0.08"), rund=True, rent1=D(55000), n=5, zins=D("0.04"), tilg=D("0.02"),
             afa=D(17600), steuer_verkauf=False, verbose=False):
    rr = r if rund else (lambda x: x)
    aL = h if aL is None else aL
    N = p*n
    hp, kp, ap = konf(h,p), konf(kk,p), konf(aL,p)
    K = D(700000); rate = rr(K*(zins+tilg)/p)
    einl = dict(einlagen or {}); entn = dict(entnahmen or {})
    einl[0] = einl.get(0, D(0)) + EK
    # Investition
    G = D(0); KK = D(0); RS = K
    # t=0: -1.100.000 + 700.000 + EK
    s0 = D(-1100000) + K + einl[0] - entn.get(0, D(0))
    if s0 >= 0: G = s0
    else: KK = -s0
    ein_ser = {0: einl[0]-entn.get(0,D(0))}
    bem = D(0); sumzins = D(0)
    for u in range(1, N+1):
        j = (u-1)//p + 1
        idx = D(1)
        for _ in range(j-1): idx = r12(idx*D("1.02"))
        miete = rr(rent1*idx/p)
        zi = rr(RS*zins/p); ti = min(RS, max(D(0), rate-zi)); RS -= ti
        sumzins += zi
        abl = D(0); orig = miete
        if u == N:
            abl = RS; RS = D(0); orig += verkauf
        hz = rr(G*hp); kz = rr(KK*kp)
        bem += miete - zi + hz - kz
        st = D(0)
        if u % p == 0:
            b = bem - afa
            if u == N and steuer_verkauf:
                b += verkauf - (D(1100000) - afa*n)
            st = rr(s*b); bem = D(0)
            if verbose: print("Jahr", j, "Steuer", st, "Bem", b)
        sal = orig - zi - ti - abl + hz - kz - st + einl.get(u,D(0)) - entn.get(u,D(0))
        net = G - KK + sal
        if net >= 0: G, KK = net, D(0)
        else: G, KK = D(0), -net
        if verbose and u % p == 0: print("  u", u, "G", G, "KK", KK, "RS", RS, "Zins kum", sumzins)
    EW = G - KK
    # Unterlassensalternative (R-9.3), spiegelt Einlagen/Entnahmen
    L = einl[0]-entn.get(0,D(0)); W = D(0); KU = D(0); zh = D(0)
    for u in range(1, N+1):
        zl = rr(L*ap); zw = rr(W*hp); zk = rr(KU*kp)
        zh += zl + zw - zk
        st = D(0)
        if u % p == 0:
            st = rr(s*zh); zh = D(0)
        e = einl.get(u, D(0)); a = entn.get(u, D(0))
        sd = e - a
        e, a = max(sd, D(0)), max(-sd, D(0))
        # Einlage: erst KK zurueck, Rest langfristig
        back = min(KU, e); KU -= back; L += e - back
        x = W - KU + zl + zw - zk - st - a
        if x >= 0: W, KU = x, D(0)
        else:
            need = -x; W = D(0); KU = D(0)
            take = min(L, need); L -= take; need -= take
            KU = need
    EWU = L + W - KU
    return EW, EWU, sumzins

NOMINAL=False
for p in (1, 12):
    EW, EWU, sz = testfall(p=p, verbose=(p==12))
    print("p", p, "EW", EW, "EWU", EWU, "dEW", EW-EWU, "r", (EW/400000)**(D(1)/5)-1, "Zins", sz)
EW,EWU,_ = testfall(p=12, rund=False); print("monat ungerundet", EW, EWU)
NOMINAL=True
EW,EWU,_ = testfall(p=12, rund=False); print("nominal/12, ungerundet, AfA jaehrlich:", EW)
EW,EWU,_ = testfall(p=12, rund=True); print("nominal/12, gerundet, AfA jaehrlich:", EW)
