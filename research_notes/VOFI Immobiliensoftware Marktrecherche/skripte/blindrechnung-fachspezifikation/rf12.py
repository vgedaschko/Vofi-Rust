from kern import *
import sys
def show(name, val, soll, nd=2, p=False):
    v = pct(val, nd) if p else fmt(val, nd)
    ok = 'OK ' if v == soll else 'ABW'
    print(f"{ok} {name:45s} ist {v:>18s}  soll {soll:>18s}")
    return v == soll
if __name__ == '__main__':
    c = neubau()
    R = rechne(c)
    show('BK0', R['bk0'], '7.540.000,00'); show('Rate M1', R['raten'][1], '419.921,98'); show('Rate M2', R['raten'][2], '420.957,62'); show('Rate M18', R['raten'][18], '437.879,56')
    show('Baukosten', R['baukosten'], '7.719.152,34'); show('M', R['M'], '9.015.152,34')
    show('RE_n', R['re_n'], '336.600,00'); show('RE Vorhaben', R['re_vj'], '354.432,75')
    show('L', R['L'], '4.007.142,85'); show('EK Ausgleich', R['EK'], '5.008.009,49')
    t = R['tr'][0]
    show('Bank Ausz M9', t.s['ausz'][9], '104.786,77'); show('EK M9', R['einl'][9], '323.492,21'); show('Bank M10', t.s['ausz'][10], '429.335,23')
    show('Zins M10', t.s['zins'][10], '349,29'); show('BZ M10', t.s['bz'][10], '9.755,89'); show('BZ M7', t.s['bz'][7], '10.017,86'); show('BZ M18', t.s['bz'][18], '1.094,70')
    show('BZ gesamt', sum(t.s['bz']), '78.993,23'); show('Zinsen Bauzeit', sum(t.s['zins'][:19]), '54.961,41')
    show('Rate M19', t.s['zins'][19]+t.s['tilg'][19], '20.035,71'); show('Zins M19', t.s['zins'][19], '13.357,14'); show('Tilg M19', t.s['tilg'][19], '6.678,57')
    show('Bew M19', R['bew'][19], '2.762,50'); show('Soll M22', R['soll'][22], '33.000,00'); show('Einz M22', R['miete'][22], '32.340,00')
    ch = [m for m in range(23, 100) if R['qm'](m) != R['qm'](m-1)]
    print('Erhoehungen', ch, 'soll 37,52,67,82,97')
    show('AfA PJ2', R['afa'][2], '115.787,29')
    show('EK Investitionsphase', R['ek_inv'], '5.141.964,13'); show('lfd Nachschuss', R['nach_lfd'], '68.394,63')
    show('Endwert', R['EW'], '9.796.187,08'); show('Rendite', R['r'], '4,332 %', 3, True)
    show('a0', R['a0'], '8.929.843,91'); show('g', R['g'], '3,549 %', 3, True)
    show('Einstiegsfaktor', R['gesamt']/R['mjm_1'], '23,11'); show('Darlehen zu GK', R['darl_quote'], '44,45 %', 2, True)
    print('EWU', R['EWU'], 'dEW', R['dEW'], 'meld', R['meld'])
    S = rechne(c, stress=True, L_fix=R['L'])
    show('Stress Baukosten', S['baukosten'], '8.135.353,14'); show('Stress EK', S['ek_inv'], '5.597.473,18'); show('Stress Rendite', S['r'], '2,176 %', 3, True)
    show('Stress erste Miete M25', S['miete'][25], '31.680,00'); print('M24', S['miete'][24])
