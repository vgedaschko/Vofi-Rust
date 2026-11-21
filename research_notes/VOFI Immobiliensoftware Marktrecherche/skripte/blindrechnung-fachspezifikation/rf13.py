# -*- coding: utf-8 -*-
"""RF-13: Ankauf je Steuerstatus, 14 Auspraegungen nach Anhang A.5 (R-7.5 bis R-7.18, R-9.5);
Steuerbeispiele zum Verkaufsjahr (R-7.8, R-7.11, R-7.17)."""
from kern import *


def fall(**kw):
    return mit(ankauf(), **kw)


def F():
    return [
        ('1 Koerperschaft', fall(), '2.524.305,59', '1.770.603,63', '753.701,96', '4,527 %', '1,483 %'),
        ('2 Koerperschaft mit E-41', fall(kennz=True), '2.562.727,38', '1.768.249,69', '794.477,69', '4,670 %', '1,483 %'),
        ('3 wie 2 mit E-69', fall(kennz=True, e69=True), '2.710.609,38', '1.768.249,69', '942.359,69', '5,161 %', '1,483 %'),
        ('4 Koerperschaft, sofort', fall(H_h38='sofort'), '2.475.876,30', '1.737.298,55', '738.577,75', '4,523 %', '1,483 %'),
        ('5 Verein oder Stiftung', fall(status='verein'), '2.822.736,55', '1.826.982,29', '995.754,26', '5,520 %', '1,763 %'),
        ('6 PersGes originaer', fall(status='pg_orig'), '2.284.696,57', '1.706.648,99', '578.047,58', '3,649 %', '1,160 %'),
        ('7 wie 6, 440 %', fall(status='pg_orig', K_hebesatz=D('4.4')), '2.267.845,35', '1.705.425,92', '562.419,43', '3,585 %', '1,154 %'),
        ('8 wie 7, 60 %', fall(status='pg_orig', K_hebesatz=D('4.4'), anteil=D('0.6')), '2.200.475,99', '1.700.569,96', '499.906,03', '3,324 %', '1,129 %'),
        ('9 wie 7, sofort', fall(status='pg_orig', K_hebesatz=D('4.4'), H_h38='sofort'), '2.217.038,80', '1.653.094,49', '563.944,31', '3,659 %', '1,154 %'),
        ('10 PersGes gepraegt, 440 %, E-41', fall(status='pg_gepr', K_hebesatz=D('4.4'), kennz=True), '2.270.137,97', '1.705.425,92', '564.712,05', '3,594 %', '1,154 %'),
        ('11 PersGes gepraegt, 440 %, 60 %, MA-036 andere Lesart', fall(status='pg_gepr', K_hebesatz=D('4.4'), anteil=D('0.6'), ma036_alt=True),
         '2.242.461,99', '1.700.569,96', '541.892,03', '3,487 %', '1,129 %'),
        ('12 Einzelunternehmen, 440 %', fall(status='einzel', K_hebesatz=D('4.4')), '2.267.845,35', '1.705.425,92', '562.419,43', '3,585 %', '1,154 %'),
        ('13 Privatperson', fall(status='privat'), '2.711.417,29', '1.770.641,79', '940.775,50', '5,141 %', '1,473 %'),
        ('14 befreite Koerperschaft', fall(status='befreit'), '2.863.247,28', '1.875.297,60', '987.949,68', '5,661 %', '2,000 %'),
    ]


def main():
    s = Z.show
    Z.titel('RF-13 Steuerstatus im vollen Plan (Anhang A.5)')
    res = {}
    for name, c, ew, ewu, dew, r, ru in F():
        R = rechne(c, detail=False)
        res[name[:2].strip()] = R
        s(name + ': EW', R['EW'], ew); s(name + ': EW_U', R['EWU'], ewu); s(name + ': dEW', R['dEW'], dew)
        s(name + ': r', R['r'], r, 3, True); s(name + ': r_U', R['rU'], ru, 3, True)
    Z.titel('RF-13 / RF-17 Steuer im Verkaufsjahr im vollen Plan')
    s('E-41: Endwert aus Kuerzung des laufenden Ertrags im Verkaufsjahr + GewSt auf Verkaufsgewinn', res['3']['EW'] - res['2']['EW'], '147.882,00')
    R2, R3 = rechne(fall(kennz=True)), rechne(fall(kennz=True, e69=True))
    gv = R2['g_v']
    s('  davon Gewerbesteuer auf den Verkaufsgewinn', r2(((gv / 100).to_integral_value(rounding=ROUND_FLOOR) * 100) * D('0.14')), '139.930,00')
    s('  davon Kuerzung des laufenden Ertrags', R3['EW'] - R2['EW'] - D('139930.00'), '7.952,00')
    s('  M-51 ohne E-69', str('M-51' in R2['meld']), 'True'); s('  M-51 mit E-69', str('M-51' in R3['meld']), 'False')
    for n_, s_ in zip((9, 10, 11, 12), ('3,365 %', '3,528 %', '4,882 %', '5,141 %')):
        R = rechne(fall(status='privat', n=n_))
        s(f'Privatperson {n_} Jahre', R['r'], s_, 3, True)
        if n_ == 10:
            s('Privatperson 10 Jahre: Steuer auf den Gewinn', R['steuer_verkauf'], '334.954,62')
        if n_ == 11:
            s('Privatperson 11 Jahre: Steuer auf den Gewinn', R['steuer_verkauf'], '0,00')
    R5 = rechne(fall(status='privat', n=5, stau=D(0)))
    s('Privatperson, 5 Jahre ohne Massnahme: Vorfaelligkeit', R5['vfe'], '54.553,59')
    s('  steuerlicher Verkaufsgewinn', R5['jahr'][-1]['det']['gvs'], '207.510,06')
    s('  Steuer des Verkaufsjahres', R5['jahr'][-1]['tax'], '102.563,99')
    V10, V11 = rechne(fall(status='verein', n=10)), rechne(fall(status='verein', n=11))
    s('Verein 10 Jahre: Steuer auf den Verkaufsgewinn', V10['steuer_verkauf'], '84.137,42'); s('Verein 10 Jahre: Rendite', V10['r'], '5,051 %', 3, True)
    s('Verein 11 Jahre: Steuer auf den Verkaufsgewinn', V11['steuer_verkauf'], '0,00'); s('Verein 11 Jahre: Rendite', V11['r'], '5,249 %', 3, True)
    return res


if __name__ == '__main__':
    main()
    Z.summe()
