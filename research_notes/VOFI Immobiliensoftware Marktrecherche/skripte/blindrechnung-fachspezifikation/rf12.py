# -*- coding: utf-8 -*-
"""RF-12 Neubau frei finanziert (R-5.10, R-5.12, R-5.18, R-6.7, R-7.3, R-10.11, R-10.13, R-10.17, R-11.2, R-11.3, R-11.8)."""
from kern import *


def main():
    s = Z.show
    c = neubau()
    R = rechne(c)
    Z.titel('RF-12 Neubau frei finanziert, 15 Jahre')
    s('BK_0', R['bk0'], '7.540.000,00'); s('Rate M1', R['raten'][1], '419.921,98'); s('Rate M2', R['raten'][2], '420.957,62')
    s('Rate M18', R['raten'][18], '437.879,56'); s('Baukosten', R['baukosten'], '7.719.152,34')
    s('  ueber dem Preisstand des Stichtags', R['baukosten'] - R['bk0'], '179.152,34'); s('  in Prozent', (R['baukosten'] / R['bk0'] - 1), '2,38 %', 2, True)
    s('M', R['M'], '9.015.152,34')
    s('Rohertrag_n', R['roh_n'], '396.000,00'); s('Bewirtschaftung + Mietausfall des Vorhabens', R['bew_vj'] + R['ausf_n'], '41.567,25')
    s('  Anteil am Rohertrag', (R['bew_vj'] + R['ausf_n']) / R['roh_n'], '10,5 %', 1, True)
    s('RE_n', R['re_n'], '336.600,00'); s('Reinertrag des Vorhabens', R['re_vj'], '354.432,75')
    s('Bankdarlehen', R['L'], '4.007.142,85'); s('bindet', ','.join(R['bind']), 'b'); s('Eigenkapital als Ausgleichsposten', R['EK'], '5.008.009,49')
    t = R['trd']['bank']
    s('Stichtag aus Eigenkapital', R['einl'][0], '1.296.000,00')
    s('Bank: erste Auszahlung im Monat', min(t.ausz), '9'); s('Bank: Auszahlung M9', t.s['ausz'][9], '104.786,77')
    s('Eigenkapital M9', R['einl'][9], '323.492,21'); s('Bank: Auszahlung M10', t.s['ausz'][10], '429.335,23')
    s('Zins M10', t.s['zins'][10], '349,29'); s('Bereitstellungszins M10', t.s['bz'][10], '9.755,89')
    s('Nachschuss M10', R['nach'][10], '10.105,18')
    for m in (7, 8, 9):
        s(f'Bereitstellungszins M{m}', t.s['bz'][m], '10.017,86')
    s('Bereitstellungszins M18', t.s['bz'][18], '1.094,70'); s('Bereitstellungszins zusammen', sum(t.s['bz']), '78.993,23')
    s('Zinsen der Bauzeit', sum(t.s['zins'][:19]), '54.961,41')
    s('Finanzierungskosten der Investitionsphase', sum(t.s['zins'][:19]) + sum(t.s['bz'][:19]), '133.954,64')
    s('Rate M19', t.s['zins'][19] + t.s['tilg'][19], '20.035,71'); s('  Zins M19', t.s['zins'][19], '13.357,14'); s('  Tilgung M19', t.s['tilg'][19], '6.678,57')
    s('Bewirtschaftung M19', R['bew'][19], '2.762,50'); s('erste Miete im Monat', R['m0'], '22')
    s('Sollmiete M22', R['soll'][22], '33.000,00'); s('Einzahlung M22', R['miete'][22], '32.340,00')
    s('Monate der Erhoehungen bis M100', '/'.join(str(m) for m in range(23, 101) if R['qm'](m) != R['qm'](m - 1)), '37/52/67/82/97')
    s('Abschreibung PJ2 (sechs Monate)', R['afa'][2], '115.787,29')
    s('Eigenkapital der Investitionsphase', R['ek_inv'], '5.141.964,13'); s('laufender Nachschussbedarf', R['nach_lfd'], '68.394,63')
    s('P-04: Mittelherkunft = Mittelverwendung', R['ek_inv'] + R['L'], fmt(R['M'] + D('133954.64')))
    s('Endwert', R['EW'], '9.796.187,08'); s('Endwertdifferenz', R['dEW'], '3.324.362,70'); s('Rendite', R['r'], '4,332 %', 3, True)
    s('a_0', R['a0'], '8.929.843,91'); s('Gesamtkapitalrendite', R['g'], '3,549 %', 3, True)
    s('massgebliche Jahresmiete, erster Vermietungsmonat', R['mjm_1'], '390.060,00')
    s('Einstiegsfaktor', R['gesamt'] / R['mjm_1'], '23,11'); s('Darlehen zu Gesamtkosten', R['darl_quote'], '44,45 %', 2, True)
    S = rechne(c, stress=True)
    s('Stress: Baukosten', S['baukosten'], '8.135.353,14'); s('Stress: Bankdarlehen', S['L'], '3.740.000,00')
    s('Stress: Eigenkapital der Investitionsphase', S['ek_inv'], '5.851.491,95'); s('Stress: Rendite', S['r'], '2,247 %', 3, True)
    s('Stress: erste Miete im Monat', S['m0'], '25')

    Z.titel('RF-12 Neubau frei: Varianten (R-5.12, R-6.7, R-6.15, R-11.2)')
    X = rechne(mit(c, H_anlauf_nb=1), detail=False); s('Anlaufleerstand ein Monat: erste Miete im Monat', X['m0'], '20')
    X = rechne(mit(c, vorverm=True), detail=False); s('Vorvermietung: erste Miete im Monat', X['m0'], '19')
    s('Vorvermietung: laufender Nachschussbedarf', X['nach_lfd'], '0,00'); s('Vorvermietung: Endwertdifferenz', X['dEW'], '3.439.793,85')
    X = rechne(mit(c, vorlauf=12), detail=False)
    s('Vorlauf 12: Rate M13', X['raten'][13], '432.519,64'); s('Vorlauf 12: Rate M30', X['raten'][30], '451.015,95')
    s('Vorlauf 12: Baukosten', X['baukosten'], '7.950.726,89'); s('Vorlauf 12: erste Miete im Monat', X['m0'], '34'); s('Vorlauf 12: Rendite', X['r'], '3,675 %', 3, True)
    X = rechne(mit(c, festpreis=True), detail=False)
    s('Festpreis: Rate', X['raten'][1], '418.888,89'); s('Festpreis: Baukosten', X['baukosten'], '7.540.000,02')
    s('Festpreis: Endwertdifferenz', X['dEW'], '3.500.639,76'); s('Festpreis: ueber dem Lauf mit Fortschreibung', X['dEW'] - R['dEW'], '176.277,06')
    X = rechne(mit(c, kkw=D(2900), kkw_gesamt=True), detail=False)
    s('Kennwert 2.900 fuer KG 200 bis 700: BK_0', X['bk0'], '7.540.000,00'); s('  Endwert', X['EW'], '9.796.187,08')
    X = rechne(mit(c, e65=D('15.00')), detail=False)
    s('nachhaltige Miete 15,00: RE_n', X['re_n'], '306.000,00'); s('nachhaltige Miete 15,00: Bankdarlehen', X['L'], '3.642.857,14')
    X = rechne(mit(c, H_h33=D('0.10')), detail=False)
    s('Mindestansatz 10 %: es bindet der Reinertrag des Vorhabens', X['re_n'], '354.432,75')
    X = rechne(mit(c, stp=20, stp_miete=D(60)), detail=False)
    s('Stellplaetze: BK_0', X['bk0'], '7.940.000,00'); s('Stellplaetze: Sollmiete im ersten Vermietungsmonat', X['soll'][22], '34.200,00')
    X = rechne(mit(c, zb=1)); tb = X['trd']['bank']
    s('Zinsbindung ein Jahr: Rate M19 mit Anschlusszins', tb.s['zins'][19] + tb.s['tilg'][19], '23.375,00')
    c24 = mit(c, bauzeit=24, zb=2)
    X, XS = rechne(c24), rechne(c24, stress=True)
    s('Bauzeit 24, Bindung 2: Tilgung M25', X['trd']['bank'].s['tilg'][25], '6.678,57'); s('  Deckung im ersten Jahr', X['deck_vj'], '1,2624', 4)
    s('  Stress: Tilgung M28', XS['trd']['bank'].s['tilg'][28], '6.233,34'); s('  Stress: Deckung im ersten Jahr', XS['deck_vj'], '1,0884', 4)
    try:
        rechne(mit(c, n=2)); m = 'gerechnet'
    except Meldung as e:
        m = e.kennung
    s('Haltedauer zwei Jahre', m, 'M-23')
    s('Haltedauer drei Jahre: Endwert', rechne(mit(c, n=3), detail=False)['EW'], '5.201.901,26')
    try:
        rechne(mit(c, bauzeit=60, n=6)); m = 'gerechnet'
    except Meldung as e:
        m = e.kennung
    s('Bauzeit 60 Monate, Haltedauer sechs Jahre', m, 'M-23')

    Z.titel('RF-12 Neubau frei: tragbarer Grundstueckspreis (R-11.4, R-11.7)')
    ps = preissuche(c)
    s('tragbarer Grundstueckspreis', D(ps['P']), '702.767', 0)
    s('  je m2 Grundstueck', D(ps['P']) / c['gfl'], '281,11'); s('  je m2 Wohnflaeche', D(ps['P']) / c['wfl'], '351,38')
    pss = preissuche(c, stress=True); s('Stressfall', str(pss['meld']), 'M-32')
    s('nachhaltige Miete 15,00: tragbarer Grundstueckspreis', D(preissuche(mit(c, e65=D('15.00')))['P']), '606.989', 0)
    s('H-25 fest 4 % ohne KfW: tragbarer Grundstueckspreis', D(preissuche(mit(c, H_h25=D('0.04')))['P']), '876.926', 0)
    return R, S, pss


if __name__ == '__main__':
    R, S, pss = main()
    Z.summe()
    print('eigene Werte: frei EW_U', fmt(R['EWU']), 'rU', pct(R['rU']), '| Stress EW', fmt(S['EW']), 'EW_U', fmt(S['EWU']), 'dEW', fmt(S['dEW']),
          '| Stress-Preissuche: Rendite bei U', pct(pss.get('r_U')))
