# -*- coding: utf-8 -*-
"""RF-12 Neubau mit Grobfoerderung: Teilraten, Zwischenfinanzierung, Tilgung nach Richtlinie, Bemessung,
Ergebnis ohne Bankdarlehen (R-5.11, R-5.12, R-6.5, R-6.6, R-8.7, R-8.8, R-10.14, R-10.21, R-10.24, R-11.3, R-11.14, R-11.15)."""
from kern import *


def foerderfall(**kw):
    return mit(neubau(), **dict(dict(foerder=True, n=38), **kw))


def main():
    s = Z.show
    c = foerderfall()
    R = rechne(c)
    Z.titel('RF-12 Neubau gefoerdert: Bemessung (R-11.14, R-5.12)')
    s('zuwendungsfaehige Kosten', R['zk'], '8.719.152,34'); s('Foerderdarlehen', R['fd'], '5.231.491,40'); s('Zuschuss', R['zu'], '1.743.830,47')
    s('Mindesteigenkapital', R['mind_ek'], '1.743.830,47'); s('Entgelt Darlehen', R['entg_d'], '52.314,91'); s('Entgelt Zuschuss', R['entg_z'], '13.078,73')
    s('Entgelte', R['entg'], '65.393,64'); s('Mittelbedarf', R['M'], '9.080.545,98')
    s('Rohertrag', R['roh_n'], '196.800,00'); s('nachhaltiger Reinertrag', R['re_n'], '159.216,75')
    kb = R['kd_bem']['foerder']
    s('Rate_B des Foerderdarlehens', kb['rate'], '10.462,98'); s('Beitrag je Monat', (kb['kd'] - 12 * kb['rate']) / 12, '2.179,79')
    s('Kapitaldienst des Foerderdarlehens zu Bemessungskonditionen', R['KD_U'], '151.713,24')
    s('A', R['A'], '628.357,62'); s('B', R['B'], '-271.894,50'); s('C', R['C'], '361.393,64'); s('Bankdarlehen', R['L'], '0,00')
    s('M-21', str('M-21' in R['meld']), 'True'); s('Eigenkapital als Ausgleichsposten', R['EK'], '2.105.224,11')
    s('ohne Rang in der Quote (frueher Lesart 1): A', R['A'] + R['fd'], '5.859.849,02')

    Z.titel('RF-12 Neubau gefoerdert: Teilraten und Zwischenfinanzierung (R-11.3)')
    ma = R['mittelabruf']
    s('Foerdermittel', R['fd'] + R['zu'], '6.975.321,87')
    s('Teilraten bereit ab Monat', '/'.join(map(str, R['bereit'])), '1/10/15/22')
    s('Obergrenze 1', R['ober'][0], '2.092.596,56'); s('Obergrenze 2', R['ober'][1], '4.185.193,12'); s('Obergrenze 3', R['ober'][2], '6.277.789,68')
    s('Eigenkapital Stichtag', ma['einl'][0], '1.296.000,00'); s('Eigenkapital M1', ma['einl'][1], '419.921,98'); s('Eigenkapital M2', ma['einl'][2], '389.302,13')
    ab = lambda u: ma['fd'].get(u, D(0)) + ma['zus'][u]
    s('erster Abruf im Monat', min(ma['fd']), '2'); s('erster Abruf einschliesslich Entgelte', ab(2), '97.049,13')
    s('Luecke M6', ma['luecke'][6], '0,00'); s('Luecke M7', ma['luecke'][7], '124.864,92'); s('Luecke Ende M9', ma['luecke'][9], '980.369,23')
    s('Abruf M10', ab(10), '1.409.704,46'); s('  davon Darlehen', ma['fd'][10], '1.057.278,34'); s('  davon Zuschuss', ma['zus'][10], '352.426,12')
    s('Kontokorrent M10', R['KK_u'][10], '0,00'); s('Kontokorrent M9', R['KK_u'][9], '980.369,23')
    s('Zwischenfinanzierung Ende M14', R['KK_u'][14], '1.045.063,54'); s('Abruf M15', ab(15), '1.479.719,23')
    for m in (18, 19, 20, 21):
        s(f'offen M{m}', R['KK_u'][m], '697.532,19')
    s('letzte Teilrate M22', ab(22), '697.532,19'); s('Kontokorrent M22', R['KK_u'][22], '0,00')
    s('hoechster Stand der Zwischenfinanzierung', R['zwifi_max'], '1.045.063,54'); s('Zinsen der Zwischenfinanzierung', R['zwifi_zins'], '42.095,30')
    s('Summe Abrufe Darlehen', sum(ma['fd'].values()), '5.231.491,40'); s('Summe Abrufe Zuschuss', sum(ma['zus']), '1.743.830,47')

    Z.titel('RF-12 Neubau gefoerdert: Foerderdarlehen, Miete, Ergebnis')
    tf = R['trd']['foerder']
    s('letzte Teilrate im Monat', max(tf.ausz), '22'); s('Tilgung ab Monat', tf.tilg_beginn, '23'); s('Zahl der Raten', tf.m, '500')
    s('Rate', tf.s['tilg'][23], '10.462,98'); s('zinslos bis Monat', tf.zb_ende, '438')
    s('erster Zins im Monat', min(u for u in range(1, R['N'] + 1) if tf.s['zins'][u] > 0), '439')
    for m, s_ in [(22, '8,2000'), (54, '8,2000'), (55, '8,7043'), (91, '9,2396'), (127, '9,8079')]:
        s(f'gebundene Miete M{m}', R['qm'](m), s_, 4)
    s('Stufe 11 ab Bindungsjahr 34 (M415)', str(R['qm'](415) > R['qm'](414) and R['qm'](456) == R['qm'](415)), 'True')
    s('Eigenkapital der Investitionsphase', R['ek_inv'], '2.144.688,71'); s('Eigenkapitalbedarf insgesamt', R['ek_ges'], '2.172.325,46')
    s('Deckung nach Bemessung', R['deck_bem'], '1,0495', 4); s('Reserve nach Bemessung', R['res_bem'], '-22.839,14')
    s('Deckung im ersten Jahr der Vollvermietung', R['deck_vj'], '1,1309', 4); s('  mit vollem Kapitaldienst', R['deck_voll'], '1,0495', 4)
    s('kleinste Deckung', R['deck_min'][0], '1,0510', 4); s('  im Planjahr', R['deck_min'][1], '4')
    s('Deckung nach dem Ende der zinslosen Zeit: Planjahr', R['deck_nach_zb']['foerder'][0], '37'); s('  Deckung', R['deck_nach_zb']['foerder'][1], '1,8848', 4)
    s('M-38', str('M-38' in R['meld']), 'True'); s('M-50', str('M-50' in R['meld']), 'False')
    s('Kapitaldienstreserve laut Finanzplan', R['re_vj'] - c['H']['mu'] * R['kd_vj'], '-9.734,23')
    s('Endwert', R['EW'], '9.477.900,38'); s('Endwertdifferenz', R['dEW'], '5.656.209,72'); s('Rendite', R['r'], '3,956 %', 3, True)
    s('Rueckzahlung des Zuschusses nach 38 Jahren', R['rueck'], '0,00')
    # R-11.15
    mu = c['H']['mu']
    kdc = R['KD_U'] + 12 * r2(R['C'] * (R['i_k'] + R['t_k']) / 12)
    s('R-11.15: Deckung der uebrigen Darlehen', R['re_n'] / R['KD_U'], '1,0495', 4)
    s('R-11.15: Restfinanzierung C', R['C'], '361.393,64'); s('R-11.15: freier Beleihungsraum', R['A'] - R['C'], '266.963,98')
    s('R-11.15: noetiger Reinertrag', mu * kdc, '212.412,96'); s('R-11.15: moegliche Mindestdeckung', R['re_n'] / kdc, '0,8995', 4)
    s('R-11.15: Mindestdeckung laut Finanzplan ab Planjahr', min(j for j in R['deck'] if j >= R['erstes_voll'] and R['deck'][j][0] >= mu), '9')
    s('R-11.15: Eigenkapital ueber dem Mindesteigenkapital', R['ek_inv'] - R['mind_ek'], '400.858,24')
    s('Nachschuesse PJ1', sum(R['nach'][1:13]), '16.422,18'); s('Nachschuesse PJ2', sum(R['nach'][13:25]), '50.679,17'); s('Nachschuesse danach', sum(R['nach'][25:]), '0,00')
    s('Steuer PJ1 und PJ2', R['jahr'][0]['tax'] + R['jahr'][1]['tax'], '0,00')
    s('Zuschuss: Ertrag PJ2', R['zus_ertrag'][2], '24.911,86'); s('Zuschuss: Entgelt PJ2', R['zentg_abz'][2], '186,84')
    s('Zuschuss: Ertrag PJ3', R['zus_ertrag'][3], '49.823,73'); s('Zuschuss: Entgelt PJ3', R['zentg_abz'][3], '373,68')
    s('Entgelt des Foerderdarlehens PJ1 (zehn Monate)', R['einb_abz'][1], '1.199,88'); s('  PJ2', R['einb_abz'][2], '1.439,86'); s('  PJ3', R['einb_abz'][3], '1.439,86')
    s('  Summe ueber die Haltedauer', sum(R['einb_abz']), '52.314,91')
    S = rechne(c, stress=True)
    ts = S['trd']['foerder']
    s('Stress: Teilraten bereit ab Monat', '/'.join(map(str, S['bereit'])), '1/12/17/25')
    s('Stress: Tilgung ab Monat', ts.tilg_beginn, '25'); s('Stress: Zahl der Raten', ts.m, '501'); s('Stress: Rate', ts.s['tilg'][25], '10.442,10')
    s('Stress: kleinste Deckung', S['deck_min'][0], '1,0258', 4)
    s('Stress: Mindestdeckung laut Finanzplan ab Planjahr', min(j for j in S['deck'] if j >= S['erstes_voll'] and S['deck'][j][0] >= mu), '11')

    Z.titel('RF-12 Neubau gefoerdert: Haltedauern, Verkauf in der Bindung, Varianten')
    for n_, s_ in zip((36, 37, 38, 39), ('4,027 %', '3,996 %', '3,956 %', '4,190 %')):
        s(f'Rendite {n_} Jahre', rechne(foerderfall(n=n_), detail=False)['r'], s_, 3, True)
    R20 = rechne(foerderfall(n=20))
    s('20 Jahre: Rendite', R20['r'], '2,081 %', 3, True); s('20 Jahre: Endwertdifferenz', R20['dEW'], '357.090,85')
    s('20 Jahre: Verkaufspreis', R20['vpreis'], '6.655.683,14'); s('20 Jahre: Abloesung des Foerderdarlehens', R20['trd']['foerder'].s['abl'][240], '2.950.561,76')
    s('20 Jahre: Rueckzahlung des Zuschusses', R20['rueck'], '822.091,51'); s('20 Jahre: Vorfaelligkeit', R20['vfe'], '0,00')
    s('20 Jahre: P-07 verbleibender Zuschuss', R20['zu'] - R20['rueck'], '921.738,96')
    Rf = rechne(mit(neubau(), n=38), detail=False)
    s('Vergleich frei gegen gefoerdert, 38 Jahre: Differenz der Endwertdifferenz', R['dEW'] - Rf['dEW'], '-10.726.689,93')
    s('Zielrendite 3 % fuer gefoerderte Vorhaben: tragbarer Grundstueckspreis', D(preissuche(foerderfall(H_z_foerder=D('0.03')))['P']), '2.118.474', 0)
    s('Zielrendite 5 %', str(preissuche(c)['meld']), 'M-32')
    X = rechne(foerderfall(K_f_miete=D('7.60')))
    s('Eingangsmiete 7,60: Deckung nach Bemessung', X['deck_bem'], '0,9564', 4); s('Eingangsmiete 7,60: kleinste Deckung', X['deck_min'][0], '0,9573', 4)
    s('Eingangsmiete 7,60: M-50', str('M-50' in X['meld']), 'True')
    try:
        rechne(foerderfall(tilg=D('0.005'))); m = 'gerechnet'
    except Meldung as e:
        m = e.kennung
    s('Tilgungssatz 0,5 %', m, 'M-20')
    X = rechne(foerderfall(H_mindtilg=D('0.005'), tilg=D('0.01')), nur_bemessung=True); s('Mindesttilgung des Hauses 0,5 %: bemisst mit', X['t_k'] * 100, '1', 0)
    try:
        rechne(foerderfall(kfw=D(3000000))); m = 'gerechnet'
    except Meldung as e:
        m = e.kennung + ' ' + e.text
    s('KfW-Darlehen 3 Mio. daneben', m, 'M-22 hoechster KfW-Betrag: 361393.64')
    R42 = rechne(foerderfall(n=42))
    t42 = R42['trd']['foerder']
    s('42 Jahre: letzte Abschreibung im Planjahr', max(j for j in range(1, 43) if R42['afa'][j] > 0), '35')
    s('42 Jahre: erster Zins auf das Foerderdarlehen im Planjahr', (min(u for u in range(1, 505) if t42.s['zins'][u] > 0) - 1) // 12 + 1, '37')
    s('42 Jahre: Abloesung des Foerderdarlehens', t42.s['abl'][504], '188.335,04'); s('42 Jahre: Rueckzahlung', R42['rueck'], '0,00')
    s('42 Jahre: Endwert', R42['EW'], '12.824.337,47'); s('42 Jahre: Rendite', R42['r'], '4,321 %', 3, True)
    s('42 Jahre: Bewirtschaftung M19', R42['bew'][19], '2.762,50'); s('42 Jahre: Bewirtschaftung M283', R42['bew'][283], '4.927,81'); s('42 Jahre: Bewirtschaftung M403', R42['bew'][403], '6.807,90')
    return R, S


if __name__ == '__main__':
    R, S = main()
    Z.summe()
    print('eigene Werte: gefoerdert 38 J EW_U', fmt(R['EWU']), 'rU', pct(R['rU']), '| Stress EW', fmt(S['EW']), 'dEW', fmt(S['dEW']), 'r', pct(S['r']),
          'EK Investitionsphase', fmt(S['ek_inv']))
