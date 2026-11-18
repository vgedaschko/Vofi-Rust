from kern import *
from rf12 import show
def testfall(p, ek=D(400000), darl=None):
    n = 5; N = n*p
    c = dict(status='lehrbuch', lb_satz=D('0.30'), lb_gv=False, verlust='sofort', startjahr=2027, n=n,
             H=dict(h=D('0.02'), aL=D('0.02'), k=D('0.08')), K=katalog())
    idx = index_reihe(D('0.02'), n)
    tr = Tranche('bank', D(1100000)-ek if darl is None else darl, 'prozent', D('0.04'), D('0.02'))
    s = tr.plan(N, p)
    hp, kp = psatz(D('0.02'), p), psatz(D('0.08'), p)
    st = Steuer(c)
    G = KK = D(0); rows = []; acc = dict(m=D(0), z=D(0), hz=D(0), kz=D(0), t=D(0)); e=[D(0)]*(N+1); e[0]=ek
    for u in range(N+1):
        j = (u-1)//p+1
        miete = r2(D(55000)*idx[j]/p) if u >= 1 else D(0)
        orig = miete - (D(1100000) if u == 0 else 0) + (D(1150000) if u == N else 0)
        hz = r2(G*hp) if u else D(0); kz = r2(KK*kp) if u else D(0)
        acc['m'] += miete; acc['z'] += s['zins'][u]; acc['hz'] += hz; acc['kz'] += kz; acc['t'] += s['tilg'][u]
        tax = D(0)
        if u and u % p == 0:
            tax = st.jahr(j, acc['m'] - D(17600) - acc['z'] - acc['kz'], acc['hz'], D(0))
            rows.append(dict(acc, tax=tax)); acc = {k: D(0) for k in acc}
        saldo = orig + s['ausz'][u] - s['zins'][u] - s['tilg'][u] - s['abl'][u] + hz - kz - tax + e[u]
        net = G - KK + saldo
        G, KK = (net, D(0)) if net >= 0 else (D(0), -net)
        if u and u % p == 0: rows[-1].update(G=G, KK=KK, rest=s['rest'][u])
        if u == 1: m1 = (miete, s['zins'][1], s['tilg'][1])
    EW = G - KK
    EWU = alternative(c, N, p, e, [D(0)]*(N+1))
    f = r12((1 + D('0.02')*(1-D('0.30'))) ** (D(1)/D(p)))
    w0 = f ** N
    r = (EW/ek) ** (D(1)/n) - 1
    return dict(EW=EW, EWU=EWU, rows=rows, m1=m1, r=r)
M = testfall(12)
show('RF-06 M1 Miete', M['m1'][0], '4.583,33'); show('M1 Zins', M['m1'][1], '2.333,33'); show('M1 Tilgung', M['m1'][2], '1.166,67')
y = M['rows'][0]
show('J1 Miete', y['m'], '54.999,96'); show('J1 Zins', y['z'], '27.740,46'); show('J1 Tilgung', y['t'], '14.259,54'); show('J1 Habenzins', y['hz'], '118,75')
show('J1 Steuer', y['tax'], '2.933,48'); show('J1 Guthaben', y['G'], '10.185,23'); show('J1 Restschuld', y['rest'], '685.740,46')
show('RF-06 Endwert Monatsraster', M['EW'], '585.918,65'); show('Alternative Monatsraster', M['EWU'], '428.794,92')
show('dEW Monatsraster', M['EW']-M['EWU'], '157.123,73'); show('Rendite Monatsraster', M['r'], '7,9333 %', 4, True)
J = testfall(1)
show('RF-05 Endwert Jahresmodus', J['EW'], '584.366,28'); show('Alternative Jahresmodus (Cent)', J['EWU'], '428.795,06'); show('Rendite', J['r'], '7,876 %', 3, True)
show('J4 Guthaben', J['rows'][3]['G'], '45.263,83'); show('J2 Steuer', J['rows'][1]['tax'], '3.379,08')
K = testfall(1, ek=D(380000), darl=D(700000))
show('RF-06 EK 380.000 Endwert', K['EW'], '561.526,16'); show('  KK t=1', K['rows'][0]['KK'], '10.940,00'); show('  KK t=2', K['rows'][1]['KK'], '770,64'); show('  Rendite', K['r'], '8,123 %', 3, True)
for ek, s_ in zip((300000, 400000, 500000, 600000), ('9,407 %', '7,876 %', '6,914 %', '6,253 %')):
    show(f'RF-05 Hebel EK {ek}', testfall(1, ek=D(ek))['r'], s_, 3, True)
