# -*- coding: utf-8 -*-
"""RF-12 Neubau mit KfW-Darlehen nach dem Merkblatt (R-5.9, R-5.12, R-5.16, R-5.19, R-10.14, R-10.23)."""
from kern import *


def kfwfall(**kw):
    return mit(neubau(), **dict(dict(kfw=D(3000000), kfw_T=35, kfw_f=1), **kw))


def main():
    s = Z.show
    c = kfwfall()
    R = rechne(c)
    Z.titel('RF-12 Neubau mit KfW-Darlehen')
    tk, tb = R['trd']['kfw'], R['trd']['bank']
    s('KfW: Abruf in den Monaten', f'{min(tk.ausz)} bis {max(tk.ausz)}', '7 bis 14'); s('KfW: Abruf M7', tk.s['ausz'][7], '320.711,03')
    s('Bank: Abruf in den Monaten', f'{min(tb.ausz)} bis {max(tb.ausz)}', '14 bis 18')
    s('Bereitstellungsprovision M13', tk.s['bz'][13], '798,90'); s('Bereitstellungsprovision M14', tk.s['bz'][14], '150,12')
    s('M-49', str('M-49' in R['meld']), 'True'); s('  Verlaengerung reicht', str(R.get('m49_reicht')), 'True')
    s('KfW: Zins M19', tk.s['zins'][19], '6.250,00'); s('KfW: erste Rate im Monat', tk.tilg_beginn, '20')
    s('KfW: erste Rate (Annuitaet ueber 408 Monate)', tk.s['zins'][20] + tk.s['tilg'][20], '10.922,62'); s('  davon Tilgung', tk.s['tilg'][20], '4.672,62')
    s('KfW: Restschuld nach 120 Monaten', tk.s['rest'][120], '2.475.346,10'); s('KfW: Rate ab M121', tk.s['zins'][121] + tk.s['tilg'][121], '14.305,24')
    kb = R['kd_bem']['kfw']
    s('Bemessungszins i_B', kb['iB'] * 100, '2,5', 1); s('Rate_B', kb['rate'], '11.250,00'); s('KD_UE', R['KD_U'], '135.000,00')
    s('B', R['B'], '2.078.571,42'); s('Bankdarlehen', R['L'], '2.078.571,42'); s('Summe der Darlehen', R['L'] + c['kfw'], '5.078.571,42')
    s('Rendite', R['r'], '4,995 %', 3, True); s('Endwertdifferenz', R['dEW'], '3.404.889,14')
    s('Kapitaldienst J1 Bankdarlehen', R['kd_je']['bank'], '124.714,32'); s('Kapitaldienst J1 KfW-Darlehen', R['kd_je']['kfw'], '131.071,44')
    s('Deckung im ersten Jahr', R['deck_vj'], '1,3857', 4); s('kleinste Deckung', R['deck_min'][0], '1,3850', 4); s('  im Planjahr', R['deck_min'][1], '3')
    s('Deckung PJ 11 nach beiden Zinsbindungen', R['deck'][11][0], '1,4270', 4)
    s('kleinste Deckung nach der unguenstigsten Anschlussregel', R['deck_min_regel'][0], '1,3373', 4)
    s('Darlehen zu Gesamtkosten', R['darl_quote'], '56,33 %', 2, True)
    for (T, f), r1, kd, l_ in [((35, 1), '10.922,62', '135.000,00', '2.078.571,42'), ((35, 5), '11.853,63', '142.243,56', '1.975.092,00'),
                               ((25, 3), '14.785,20', '177.422,40', '1.472.537,14'), ((10, 2), '34.511,53', '414.138,36', '0,00')]:
        X = rechne(kfwfall(kfw_T=T, kfw_f=f))
        xk = X['trd']['kfw']
        s(f'Variante {T}/{f}: erste Rate', xk.s['zins'][xk.tilg_beginn] + xk.s['tilg'][xk.tilg_beginn], r1)
        s(f'Variante {T}/{f}: KD_UE', X['KD_U'], kd); s(f'Variante {T}/{f}: Bankdarlehen', X['L'], l_)
        if T == 10:
            s('Variante 10/2: M-21', str('M-21' in X['meld']), 'True')
    X = rechne(kfwfall(H_h25=D('0.04')), nur_bemessung=True); s('H-25 fest 4 % (frueher Lesart 2): Bankdarlehen', X['L'], '2.425.000,00')
    X = rechne(kfwfall(ma026_4=True), nur_bemessung=True); s('Lesart 4: KD_UE', X['KD_U'], '210.000,00'); s('Lesart 4: Bankdarlehen', X['L'], '1.007.142,85')
    X = rechne(kfwfall(H_h32=15), nur_bemessung=True)
    s('H-32 15 Jahre: i_B', X['kd_bem']['kfw']['iB'] * 100, '3,333333333333', 12); s('H-32 15 Jahre: KD_UE', X['KD_U'], '159.999,96'); s('H-32 15 Jahre: Bankdarlehen', X['L'], '1.721.429,14')
    X = rechne(kfwfall(kfw_zins=D('0.03')), detail=False); s('KfW-Zins 3 %: Wirkung auf die Endwertdifferenz', X['dEW'] - R['dEW'], '-63.231,54')
    X = rechne(kfwfall(n=8))
    s('Verkauf nach 8 Jahren: Vorfaelligkeit Bank', X['trd']['bank'].vfe, '35.411,17'); s('  KfW', X['trd']['kfw'].vfe, '52.203,65'); s('  zusammen', X['vfe'], '87.614,82')
    try:
        rechne(kfwfall(kfw=D(3000001))); m = 'gerechnet'
    except Meldung as e:
        m = e.kennung
    s('KfW-Darlehen 3.000.001 Euro', m, 'M-20')
    Z.titel('RF-12 Neubau mit KfW-Darlehen: tragbarer Grundstueckspreis')
    s('tragbarer Grundstueckspreis', D(preissuche(c)['P']), '1.197.094', 0)
    s('  H-25 fest 4 % (frueher Lesart 2)', D(preissuche(kfwfall(H_h25=D('0.04')))['P']), '1.283.299', 0)
    s('  Lesart 4', D(preissuche(kfwfall(ma026_4=True))['P']), '920.435', 0)
    return R


if __name__ == '__main__':
    R = main()
    Z.summe()
    print('eigene Werte: EW', fmt(R['EW']), 'EW_U', fmt(R['EWU']), 'rU', pct(R['rU']))
