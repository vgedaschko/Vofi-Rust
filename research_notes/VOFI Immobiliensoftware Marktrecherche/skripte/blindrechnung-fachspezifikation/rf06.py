# -*- coding: utf-8 -*-
"""RF-05 / RF-06 Testfall im Jahresmodus und im Monatsraster (R-2.2, R-2.3, R-2.6, R-4.3, R-5.3, R-10.x; Anhang A.2).
Eigener kleiner Finanzplan mit den Bausteinen des Kerns (Tranche, Steuer, Alternative)."""
from kern import *


def testfall(p, ek=D(400000), reinertrag=None, verlust='sofort', gv_pflichtig=False, zb=None, vorjahr=False, n=5):
    N = n * p
    c = dict(status='lehrbuch', lb_satz=D('0.30'), lb_gv=gv_pflichtig, startjahr=2027, n=n,
             H=dict(h=D('0.02'), aL=None, k=D('0.08'), h38=verlust), K=katalog())
    idx = index_reihe(D('0.02'), n + 1)
    tr = Tranche('bank', D(1100000) - ek if ek >= 400000 or ek < 380000 else D(700000), 'prozent', D('0.04'), D('0.02'),
                 zb_ende=None if zb is None else zb * p, anschluss=D('0.04'))
    s = tr.plan(N, p)
    hp, kp = psatz(D('0.02'), p), psatz(D('0.08'), p)
    st = Steuer(c)
    G = KK = D(0)
    rows = []
    acc = dict(m=D(0), z=D(0), hz=D(0), kz=D(0), t=D(0))
    e = [D(0)] * (N + 1)
    e[0] = ek
    kk0 = None
    vfe = r2(tr.abl_rest * D('0.01') * max(0, zb * p - N) / p) if zb else D(0)
    gv = D(1150000) - (D(1100000) - n * D(17600))
    for u in range(N + 1):
        j = (u - 1) // p + 1
        if u == 0:
            miete = D(0)
        elif reinertrag and j <= len(reinertrag):
            miete = r2(reinertrag[j - 1] / p)
        else:
            miete = r2(D(55000) * idx[j + (1 if vorjahr else 0)] / p)
        orig = miete - (D(1100000) if u == 0 else 0) + (D(1150000) if u == N else 0)
        hz = r2(G * hp) if u else D(0)
        kz = r2(KK * kp) if u else D(0)
        acc['m'] += miete; acc['z'] += s['zins'][u]; acc['hz'] += hz; acc['kz'] += kz; acc['t'] += s['tilg'][u]
        tax = D(0)
        if u and u % p == 0:
            bem = acc['m'] - D(17600) - acc['z'] - acc['kz'] - (vfe if u == N else 0)
            tax = st.jahr(j, bem, acc['hz'], gv if u == N else D(0))
            rows.append(dict(acc, tax=tax, bem=bem + acc['hz']))
            acc = {k: D(0) for k in acc}
        saldo = orig + s['ausz'][u] - s['zins'][u] - s['tilg'][u] - s['abl'][u] + hz - kz - tax + e[u] - (vfe if u == N else 0)
        net = G - KK + saldo
        G, KK = (net, D(0)) if net >= 0 else (D(0), -net)
        if u == 0:
            kk0 = KK
        if u and u % p == 0:
            rows[-1].update(G=G, KK=KK, rest=s['rest'][u], orig=acc.get('x'))
        if u == 1:
            m1 = (miete, s['zins'][1], s['tilg'][1])
    EW = G - KK
    EWU = alternative(c, N, p, e, [D(0)] * (N + 1))
    r = (EW / ek) ** (D(1) / n) - 1
    return dict(EW=EW, EWU=EWU, rows=rows, m1=m1, r=r, tr=tr, kk0=kk0, vv=st.vv_e, vfe=vfe)


def main():
    s = Z.show
    Z.titel('RF-05 / RF-06 Testfall im Monatsraster (R-2.3, R-2.6)')
    M = testfall(12)
    s('M1 Miete', M['m1'][0], '4.583,33'); s('M1 Zins', M['m1'][1], '2.333,33'); s('M1 Tilgung', M['m1'][2], '1.166,67')
    t = M['tr']
    s('Rate 2: Zins', t.s['zins'][2], '2.329,44'); s('Rate 2: Tilgung', t.s['tilg'][2], '1.170,56')
    y = M['rows'][0]
    s('J1 Miete', y['m'], '54.999,96'); s('J1 Zins', y['z'], '27.740,46'); s('J1 Tilgung', y['t'], '14.259,54'); s('J1 Habenzins', y['hz'], '118,75')
    s('J1 Steuer', y['tax'], '2.933,48'); s('J1 Guthaben', y['G'], '10.185,23'); s('J1 Restschuld', y['rest'], '685.740,46')
    s('Endwert Monatsraster', M['EW'], '585.918,65'); s('Alternative Monatsraster', M['EWU'], '428.794,92')
    s('Endwertdifferenz Monatsraster', M['EW'] - M['EWU'], '157.123,73'); s('Rendite Monatsraster', M['r'], '7,9333 %', 4, True)
    T10 = Tranche('b', D(700000), 'prozent', D('0.04'), D('0.02')); T10.plan(120, 12)
    s('R-5.3: Restschuld nach 120 Raten', T10.s['rest'][119] - T10.s['tilg'][120], '528.208,51')
    ip = D('0.04') / 12
    s('R-2.6: Effektivzins bei monatlicher Zahlung', (1 + ip) ** 12 - 1, '4,0742 %', 4, True)

    Z.titel('RF-05 / RF-06 Testfall im Jahresmodus mit Rundung je Zahlung (R-4.3)')
    J = testfall(1)
    soll = [('28.000,00', '14.000,00', '0,00', '9.400,00', '2.820,00', '10.180,00', '686.000,00'),
            ('27.440,00', '14.560,00', '203,60', '11.263,60', '3.379,08', '21.104,52', '671.440,00'),
            ('26.857,60', '15.142,40', '422,09', '13.186,49', '3.955,95', '32.792,66', '656.297,60'),
            ('26.251,90', '15.748,10', '655,85', '15.170,39', '4.551,12', '45.263,83', '640.549,50'),
            ('25.621,98', '16.378,02', '905,28', '17.217,07', '5.165,12', '584.366,28', '0,00')]
    for j, (z_, t_, h_, b_, x_, g_, r_) in enumerate(soll, 1):
        y = J['rows'][j - 1]
        s(f't={j} Zins', y['z'], z_); s(f't={j} Tilgung', y['t'], t_); s(f't={j} Habenzins', y['hz'], h_); s(f't={j} Bemessung', y['bem'], b_)
        s(f't={j} Steuer', y['tax'], x_); s(f't={j} Guthaben', y['G'], g_); s(f't={j} Restschuld', y['rest'], r_)
    s('Abloesung t=5', J['tr'].s['abl'][5], '624.171,48')
    s('Endwert Jahresmodus', J['EW'], '584.366,28'); s('Alternative Jahresmodus mit Rundung', J['EWU'], '428.795,06')
    s('Endwertdifferenz mit Rundung', J['EW'] - J['EWU'], '155.571,22'); s('Rendite', J['r'], '7,876 %', 3, True)
    for j, d_ in enumerate(('1,3095', '1,3357', '1,3624', '1,3897', '1,4175'), 1):
        y = J['rows'][j - 1]
        s(f'Deckung t={j}', y['m'] / (y['z'] + y['t']), d_, 4)
    s('Restwertanteil', (D(1150000) - J['tr'].s['abl'][5]) / J['EW'], '89,98 %', 2, True)
    zs = sum(y['z'] for y in J['rows'])
    s('Sollzinsen', zs, '134.171,48'); s('Z_S', zs * D('0.7'), '93.920,04')
    s('Gesamtkapitalrendite', ((J['EW'] - 400000 + zs * D('0.7') + 1100000) / 1100000) ** (D(1) / 5) - 1, '4,61 %', 2, True)
    s('Referenzzinsfuss', ((J['EWU'] - 400000 + zs * D('0.7') + 1100000) / 1100000) ** (D(1) / 5) - 1, '2,14 %', 2, True)
    K = testfall(1, ek=D(380000))
    s('EK 380.000: Kontokorrent t=0', K['kk0'], '20.000,00'); s('  Kontokorrent t=1', K['rows'][0]['KK'], '10.940,00'); s('  Kontokorrent t=2', K['rows'][1]['KK'], '770,64')
    s('  Endwert', K['EW'], '561.526,16'); s('  Rendite', K['r'], '8,123 %', 3, True)
    for ek, s_ in zip((300000, 400000, 500000, 600000), ('9,407 %', '7,876 %', '6,914 %', '6,253 %')):
        s(f'Hebel: Eigenkapital {ek}', testfall(1, ek=D(ek))['r'], s_, 3, True)
    V = testfall(1, reinertrag=[D(20000), D(30000)], verlust='vortrag')
    s('Anlaufverlust, Vortrag: Summe der Steuer', sum(y['tax'] for y in V['rows']), '0,00'); s('  ungenutzter Vortrag', V['vv'], '4.254,31'); s('  Endwert', V['EW'], '533.745,69')
    V = testfall(1, reinertrag=[D(20000), D(30000)], verlust='sofort')
    s('Anlaufverlust, sofort: Steuer', ' / '.join(fmt(y['tax']) for y in V['rows']), '-7.680,00 / -4.855,68 / 3.286,68 / 4.054,76 / 4.865,45'); s('  Endwert', V['EW'], '537.232,83')
    X = testfall(1, gv_pflichtig=True)
    s('steuerpflichtiger Verkauf: Steuer auf 138.000 Gewinn', X['rows'][-1]['tax'] - J['rows'][-1]['tax'], '41.400,00'); s('  Endwert', X['EW'], '542.966,28')
    X = testfall(1, zb=10)
    s('Vorfaelligkeit bei zehn Jahren Bindung, Verkauf nach fuenf', X['vfe'], '31.208,57'); s('  Endwert', X['EW'], '562.520,28')
    RUNDEN[0] = False          # Anhang A.2: diese Variante ist ohne Rundung gerechnet
    X = testfall(1, vorjahr=True)
    RUNDEN[0] = True
    s('Reinertrag als Vorjahreswert (ohne Rundung): Rendite', X['r'], '8,028 %', 3, True); s('  Endwert', X['EW'], '588.484,91')
    U_ = testfall(1)
    RUNDEN[0] = False
    U = testfall(1)
    RUNDEN[0] = True
    s('Testfall ohne Rundung: Endwert auf vier Stellen', U['EW'], '584.366,2816', 4); s('  Endwertdifferenz ohne Rundung', U['EW'] - U['EWU'], '155.571,23')


if __name__ == '__main__':
    main()
    Z.summe()
