# -*- coding: utf-8 -*-
"""RF-11 / RF-19: Ankauf gebundener Bestaende mit uebernommenem Darlehen (R-5.11, R-5.12, R-5.16, R-6.5, R-6.6)."""
from kern import *


def geb(zb=8, **kw):
    ue = dict(rest=D(500000), nenn=D(600000), zins=D('0.005'), tilg=D('0.02'), zb=zb, anschluss=D('0.03'), beitrag=D(0))
    return mit(ankauf(), geb=D('0.4'), geb_ende=6, geb_miete=D('6.80'), uebern=ue, **kw)


def main():
    s = Z.show
    c = geb()
    R = rechne(c)
    Z.titel('RF-11 gebundener Bestand mit uebernommenem Darlehen')
    gm = R['teile'][-1][1]
    for m, s_ in [(1, '6,8000'), (36, '6,8000'), (37, '7,2182'), (84, '7,2182'), (85, '8,0556'), (100, '8,3009'), (121, '9,2640'), (136, '9,5461')]:
        s(f'gebundene Miete M{m}', gm[m], s_, 4)
    s('Spruenge der gebundenen Miete', '/'.join(str(m) for m in range(2, 145) if gm[m] != gm[m - 1]), '37/85/100/121/136')
    soll = '7,8200 / 7,8200 / 7,8200 / 8,5557 / 8,5557 / 8,7523 / 9,1037 / 9,4387 / 9,5630 / 9,7879 / 10,3025 / 10,5690'.split(' / ')
    for j, s_ in enumerate(soll, 1):
        s(f'Miete des Vorhabens, Beginn J{j}', R['qm']((j - 1) * 12 + 1), s_, 4)
    tu = R['trd']['uebernommen']
    s('Rate des uebernommenen Darlehens', tu.s['zins'][1] + tu.s['tilg'][1], '1.250,00')
    s('Kapitaldienst J1 uebernommen', R['kd_je']['uebernommen'], '15.000,00')
    s('  aus der Restschuld waeren es', 12 * r2(D(500000) * D('0.025') / 12), '12.500,04')
    kb = R['kd_bem']['uebernommen']
    s('Bemessungszins i_B', kb['iB'] * 100, '1,00'); s('Rate_B', kb['rate'], '1.500,00'); s('KD_UE', R['KD_U'], '18.000,00')
    s('Rohertrag_n', R['roh_n'], '123.869,76'); s('Mietausfall_n', R['ausf_n'], '2.477,40'); s('Bewirtschaftung_n', R['bew_vj'], '28.911,96')
    s('RE_n', R['re_n'], '92.479,44')
    s('A', R['A'], '1.060.000,00'); s('B', R['B'], '843.802,85'); s('C', R['C'], '2.140.000,00')
    s('Bankdarlehen', R['L'], '843.802,85'); s('bindet', ','.join(R['bind']), 'b')
    for zb, i_, kd_, l_ in [(8, '1,00', '18.000,00', '843.802,85'), (9, '0,75', '16.500,00', '865.231,42'), (10, '0,50', '15.000,00', '886.660,00'),
                            (12, '0,50', '15.000,00', '886.660,00')]:
        X = rechne(geb(zb), nur_bemessung=True)
        s(f'Zinsbindung {zb} J: i_B', X['kd_bem']['uebernommen']['iB'] * 100, i_); s(f'Zinsbindung {zb} J: KD_UE', X['KD_U'], kd_)
        s(f'Zinsbindung {zb} J: Bankdarlehen', X['L'], l_)
    X = rechne(geb(ma026_4=True), nur_bemessung=True)
    s('Lesart 4: KD_UE', X['KD_U'], '30.000,00'); s('Lesart 4: Bankdarlehen', X['L'], '672.374,28')
    B0 = rechne(ankauf(), detail=False)
    s('Endwertdifferenz gebunden', R['dEW'], '562.960,01')
    s('Differenz zum freien Ankauf', R['dEW'] - B0['dEW'], '-190.741,95')
    S = rechne(c, stress=True)
    tus = S['trd']['uebernommen']
    s('Stress: Zins des uebernommenen Darlehens J9', sum(tus.s['zins'][97:109]), '15.772,22')
    R5 = rechne(geb(n=5))
    s('Verkauf nach 5 Jahren: Vorfaelligkeit Bank + uebernommen', R5['vfe'], '50.629,99')
    return R


if __name__ == '__main__':
    R = main()
    Z.summe()
    print('eigene Werte: EW', fmt(R['EW']), 'EW_U', fmt(R['EWU']), 'r', pct(R['r']), 'rU', pct(R['rU']))
