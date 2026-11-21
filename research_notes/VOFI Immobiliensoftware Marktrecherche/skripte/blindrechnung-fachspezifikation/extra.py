# -*- coding: utf-8 -*-
"""Stichproben aus RF-08, RF-14, RF-18, RF-19, RF-20: Abweichungen vom Hausstandard (R-3.2), Bemessung (R-5.12),
Vorfaelligkeit (R-5.16), Miete im Bestand (R-6.3, R-6.13, R-6.14, R-6.18), Raender (Kapitel 14)."""
from kern import *


def A(**kw):
    return mit(ankauf(), **kw)


def meld(f):
    try:
        f()
        return 'gerechnet'
    except Meldung as e:
        return e.kennung


def main():
    s = Z.show
    c = A()
    B0 = rechne(c)
    P0 = preissuche(c)['P']

    Z.titel('RF-19 Abweichungen vom Hausstandard (R-3.2) und Bemessung (R-5.12)')
    def wirk(name, kw, dew=None, dp=None, abst=None, z=None):
        cc = A(**kw)
        base = c if z is None else A(H_z=z)
        if z is not None:
            cc = mit(cc, H_z=z)
        R = rechne(cc, detail=False)
        if dew is not None:
            s(name + ': Wirkung auf die Endwertdifferenz', R['dEW'] - B0['dEW'], dew)
        if dp is not None:
            s(name + ': Wirkung auf den tragbaren Preis', D(preissuche(cc)['P'] - preissuche(base)['P']), dp, 0)
        if abst is not None:
            s(name + ': Abstand der Rendite (Prozentpunkte)', (R['r'] - B0['r']) * 100, abst)
        return R
    wirk('Mietsteigerung 1,5 %', dict(H_miet=D('0.015')), '-161.319,43', '-95.011')
    wirk('Beleihungsquote 60 %', dict(H_beta=D('0.60')), '0,00', '0')
    wirk('Mietsteigerung 2,5 %', dict(H_miet=D('0.025')), '165.880,04', '97.715', '0,56')
    wirk('H-25 fest 1 %', dict(H_h25=D('0.01')), '-38.496,31', '42.131', '0,21')
    R = wirk('Anlagezins 0,5 % als Hauswert', dict(H_aL=D('0.005')), '212.995,21', '0'); s('  Endwertdifferenz', R['dEW'], '966.697,17')
    wirk('Mindestdeckung 1,3 bei Zielrendite 5 %', dict(H_mu=D('1.3')), '17.737,72', '-19.471', '-0,08')
    s('  tragbarer Preis', D(preissuche(A(H_mu=D('1.3')))['P']), '2.297.764', 0)
    wirk('Mindestdeckung 1,3 bei Zielrendite 2 %', dict(H_mu=D('1.3')), None, '10.228', None, z=D('0.02'))
    wirk('Erwerbsnebenkosten 3 %', dict(enk=D('0.03')), None, '157.482')
    wirk('Zinsbindung 5 Jahre', dict(zb=5), '-44.943,46', '-26.475', '-0,16')
    X = rechne(A(H_h25=D('0.04')), nur_bemessung=True)
    s('H-25 fest 4 % (Vertragszins): Bankdarlehen', X['L'], '1.431.044,99'); s('  mehr als kalkulatorisch', X['L'] - B0['L'], '204.435,00')
    s('  tragbarer Preis', D(preissuche(A(H_h25=D('0.04')))['P']), '2.359.366', 0)
    s('H-25 fest 6 %: Bankdarlehen', rechne(A(H_h25=D('0.06')), nur_bemessung=True)['L'], '1.073.283,74')
    s('MA-034 "Rate bleibt": tragbarer Preis', D(preissuche(A(regel='rate'))['P']), '2.317.477', 0)
    s('MA-034 "Restlaufzeit bleibt": tragbarer Preis', D(preissuche(A(regel='restlaufzeit'))['P']), '2.317.632', 0)

    Z.titel('RF-19 Bankfall: Deckung nach der unguenstigsten Anschlussregel (R-10.14)')
    bf = dict(zins=D('0.03'), ist=D('8.50'), vm=D('8.50'), stau=D(0), H_miet=D('0.005'))
    X = rechne(A(H_h25=D('0.03'), **bf))
    s('H-25 3 %, Basisfall: kleinste Deckung', X['deck_min'][0], '1,3054', 4); s('  im Planjahr', X['deck_min'][1], '3')
    s('  unguenstigste Regel', X['deck_min_regel'][0], '1,1975', 4); s('  Regel', X['deck_min_regel'][2], 'restlaufzeit')
    s('  M-38, nicht M-39', str(('M-38' in X['meld'], 'M-39' in X['meld'])), '(True, False)')
    X = rechne(A(H_h25=D('0.03'), **bf), stress=True)
    s('H-25 3 %, Stressfall: kleinste Deckung', X['deck_min'][0], '1,0439', 4); s('  im Planjahr', X['deck_min'][1], '12')
    s('  unguenstigste Regel', X['deck_min_regel'][0], '0,9193', 4); s('  M-39', str('M-39' in X['meld']), 'True')
    X = rechne(A(**bf), stress=True)
    s('Anschlusszins, Stressfall: kleinste Deckung', X['deck_min'][0], '1,2328', 4); s('  unguenstigste Regel', X['deck_min_regel'][0], '1,0857', 4)
    s('  M-38, nicht M-39', str(('M-38' in X['meld'], 'M-39' in X['meld'])), '(True, False)')

    Z.titel('RF-14 / RF-19 Vorfaelligkeit (R-5.16), Verkauf im ersten Jahr (R-14.5), Warnschwellen (R-10.25)')
    R = rechne(A(n=1, stau=D(0)))
    s('n = 1: abgeloeste Restschuld', R['trd']['bank'].abl_rest, '1.201.623,01'); s('n = 1: Vorfaelligkeit', R['vfe'], '108.146,07')
    s('n = 1: Endwert', R['EW'], '1.071.298,15'); s('n = 1: Rendite', R['r'], '-24,204 %', 3, True); s('n = 1: M-25', str('M-25' in R['meld']), 'True')
    s('n = 1: Restwertanteil', R['restwertbeitrag'] / R['EW'], '97,23 %', 2, True)
    s('Bindung 40 Jahre, Verkauf nach einem Jahr', rechne(A(n=1, zb=40, stau=D(0)))['vfe'], '114.154,19')
    s('Bindung 20 Jahre, Verkauf nach fuenf', rechne(A(n=5, zb=20, stau=D(0)))['vfe'], '60.008,94')
    R = rechne(A(n=12, zb=15, stau=D(0))); s('Bindung 15 Jahre, Verkauf nach zwoelf', R['vfe'], '0,00'); s('  M-25', str('M-25' in R['meld']), 'False')
    s('Bindung 15 Jahre, Verkauf nach zehn, Monatsraster', rechne(A(n=10, zb=15))['vfe'], '4.627,90')
    s('Bindung 15 Jahre, Verkauf nach zehn, Jahresmodus', rechne(A(n=10, zb=15, p=1))['vfe'], '9.320,73')
    s('Verkaufsfaktor 20: Abstand zum Einstiegsfaktor', D(20) - c['preis'] / B0['mjm_1'], '1,90')

    Z.titel('RF-18 Miete im Bestand (R-6.3, R-6.8, R-6.11, R-6.13 bis R-6.15, R-6.18, R-8.1)')
    R = rechne(A(historie=(6, D('7.50'))), detail=False)
    s('Mietenhistorie: erste Erhoehung im Monat', min(m for m in range(2, 145) if R['qm'](m) != R['qm'](m - 1)), '13'); s('  auf', R['qm'](13), '8,6250', 4)
    R = rechne(A(H_d=0), detail=False)
    s('d = 0: Miete M12', R['qm'](12), '8,5000', 4); s('d = 0: Miete ab M37', R['qm'](37), '9,7631', 4); s('d = 0: Miete M36', R['qm'](36), '8,5000', 4)
    s('MA-037 ueber E-33 (a = T, M_alt = Ist): tragbarer Preis', D(preissuche(A(historie=(36, D('8.50'))))['P']), '2.322.775', 0)
    R = rechne(A(ist=D('11.00')), detail=False)
    s('Ist-Miete 11,00: Miete zu Beginn der Jahre 1 bis 6', ' / '.join(fmt(R['qm']((j - 1) * 12 + 1), 4) for j in range(1, 7)),
      '11,0000 / 10,5960 / 10,2858 / 10,0723 / 9,9584 / 10,1575')
    s('Ist-Miete 11,00: Reinertrag des Vorhabens', R['re_vj'], '141.843,24'); s('Ist-Miete 11,00: nachhaltiger Reinertrag', R['re_n'], '113.901,48')
    s('Ist-Miete 11,00: Bankdarlehen', R['L'], '1.355.969,99'); s('Ist-Miete 11,00: Endwertdifferenz', R['dEW'], '831.335,64')
    s('Ist-Miete 11,00: tragbarer Preis', D(preissuche(A(ist=D('11.00')))['P']), '2.424.974', 0)
    s('  Lesart 3 von MA-026: Bankdarlehen', rechne(A(ist=D('11.00'), ma026_3=True), nur_bemessung=True)['L'], '1.560.000,00')
    R = rechne(A(ist=D('11.00'), ma038_alt=True), detail=False)
    s('  andere Lesart MA-038: Miete in den Jahren 1 bis 7', '/'.join(sorted(set(fmt(R['qm'](m), 4) for m in range(1, 85)))), '11,0000')
    s('  andere Lesart MA-038: Endwertdifferenz', R['dEW'], '905.596,44')
    s('  andere Lesart MA-038: tragbarer Preis', D(preissuche(A(ist=D('11.00'), ma038_alt=True))['P']), '2.470.976', 0)
    R = rechne(A(baujahr=1996), detail=False); s('Baujahr 1996: Bewirtschaftung M1', R['bew'][1], '2.134,33'); s('Baujahr 1996: Bewirtschaftung M13', R['bew'][13], '2.459,50')
    R = rechne(A(erbbau=D(12000)), detail=False)
    s('Erbbauzins: massgebliche Jahresmiete am Verkaufsstichtag', R['mjm_N'], '163.556,12'); s('Erbbauzins: Verkaufspreis', R['vpreis'], '2.944.010,21')
    s('Erbbauzins: Einstiegsfaktor', c['preis'] / R['mjm_1'], '19,90')
    cl = A(leerfl=D(1320)); R = rechne(cl, detail=False)
    s('ganz leer: Sollmiete M1 bis M3', R['soll'][1] + R['soll'][2] + R['soll'][3], '0,00'); s('ganz leer: Miete ab M4', R['qm'](4), '10,12')
    s('ganz leer: ohne Mietpreisbremse', rechne(A(leerfl=D(1320), im_bremsgebiet=False), detail=False)['qm'](4), '10,50')
    s('ganz leer: Bankdarlehen', R['L'], '930.929,99'); s('ganz leer: Verkaufspreis', R['vpreis'], '3.212.578,13')
    s('ganz leer: tragbarer Preis', D(preissuche(cl)['P']), '2.290.699', 0)
    R = rechne(A(leerfl=D(200)), detail=False); s('200 m2 leer: Sollmiete M1', R['soll'][1], '9.520,00'); s('200 m2 leer: Sollmiete M4', R['soll'][4], '11.544,00')
    s('  ausserhalb des Gebiets der Mietpreisbremse: M4', rechne(A(leerfl=D(200), im_bremsgebiet=False), detail=False)['soll'][4], '11.620,00')
    R = rechne(A(H_flukt=D('0.05')), detail=False)
    s('Fluktuation 5 %: Miete zu Beginn der Jahre 1 bis 6', ' / '.join(fmt(R['qm']((j - 1) * 12 + 1), 4) for j in range(1, 7)),
      '8,5000 / 8,5911 / 8,6875 / 9,6008 / 9,6654 / 9,9892'); s('Fluktuation 5 %: Endwert', R['EW'], '2.563.369,40')
    s('sonstige Ertraege 6.000: Sollmiete M1', rechne(A(sonst=D(6000)), detail=False)['soll'][1], '11.720,00')
    R = rechne(A(im_kappgebiet=False), detail=False)
    spr = [m for m in range(2, 145) if R['qm'](m) != R['qm'](m - 1)]
    s('ausserhalb Kappungsgebiet: Monate der Erhoehungen', '/'.join(map(str, spr)), '37/52/67/82/97/112/127/142')
    s('  Mieten', ' / '.join(fmt(R['qm'](m), 4) for m in spr), '9,4473 / 9,9584 / 10,1575 / 10,3607 / 10,7793 / 10,9949 / 11,2147 / 11,4390')
    s('  Endwertdifferenz', R['dEW'], '757.210,62'); s('  Wirkung', R['dEW'] - B0['dEW'], '3.508,66')
    s('  tragbarer Preis', D(preissuche(A(im_kappgebiet=False))['P']), '2.319.295', 0)
    R = rechne(A(H_leer=D('0.295')), detail=False)
    s('Leerstand 29,5 %: Verkaufspreis', R['vpreis'], '2.299.357,95'); s('Leerstand 29,5 %: Endwertdifferenz', R['dEW'], '-277.378,77'); s('Leerstand 29,5 %: Rendite', R['r'], '0,415 %', 3, True)
    js = [sum(B0['miete'][(j - 1) * 12 + 1:j * 12 + 1]) for j in range(1, 13)]      # Zeile Z-A2 Miete: Mieteinzahlung
    s('R-12.7: Summe der Jahresmieten (Mieteinzahlungen) in vollen Euro', sum(js).quantize(D(1), rounding=ROUND_HALF_UP), '1.850.876', 0)
    s('R-12.7: Summe der gerundeten Jahreswerte', sum(x.quantize(D(1), rounding=ROUND_HALF_UP) for x in js), '1.850.875', 0)

    Z.titel('RF-14 / RF-17 / RF-20 Randfaelle (R-6.16, R-8.4, Kapitel 14)')
    R = rechne(A(stau=D(400000)), detail=False)
    s('400.000 im Jahr 2: Zahlung', R['stau_zahl'], '424.360,00'); s('  Abschreibung J3', R['afa'][3], '48.087,20'); s('  M-36', str('M-36' in R['meld']), 'True')
    R = rechne(A(stau=D(320000)), detail=False); s('320.000 im Jahr 2: Zahlung', R['stau_zahl'], '339.488,00'); s('  M-36', str('M-36' in R['meld']), 'False')
    R = rechne(A(stau=D(100000), stau_jahr=12, n=10), detail=False); s('Massnahme nach dem Verkauf: Abzug', R['vpreis'] - R['vkost'] - R['verl'], '134.391,64')
    R = rechne(A(zins=D(0), tilg=D(0), H_mindtilg=D(0), H_anschl_auf=D(0)))
    s('Zins und Tilgung null: Bankdarlehen', R['L'], '1.560.000,00'); s('  bindet', ','.join(R['bind']), 'a'); s('  Endwert', R['EW'], '2.570.143,76')
    R = rechne(A(vf=D(4), n=2, stau=D(0), H_h25=D('0.04')))
    s('Verkaufsfaktor 4, zwei Jahre: Fehlbetrag beim Verkauf', R['fehl_vk'], '926.438,19'); s('  Endwert', R['EW'], '0,00'); s('  Rendite', R['r'], '-100,000 %', 3, True)
    s('  Meldungen', ','.join(sorted(m for m in R['meld'] if m in ('M-25', 'M-29', 'M-38', 'M-39', 'M-42'))), 'M-25,M-29,M-38,M-42')
    R = rechne(A(H_leer=D('0.995')))
    s('Leerstand 99,5 %: Bankdarlehen', R['L'], '0,00'); s('  Verkaufspreis', R['vpreis'], '16.307,50'); s('  laufender Nachschussbedarf', R['nach_lfd'], '514.035,60')
    s('  M-21', str('M-21' in R['meld']), 'True')
    s('uebernommenes Darlehen 3,0 Mio.', meld(lambda: rechne(A(uebern=dict(rest=D(3000000), zins=D('0.01'), tilg=D('0.02'), zb=10, anschluss=D('0.05'))))), 'M-22')
    ps = preissuche(A(H_z=D('0.05000253'))); s('Zielrendite 5,000253 %: P*', D(ps['P']), '2.317.188', 0); s('  Meldung', str(ps['meld']), 'M-34')
    lage = ''.join('1' if lauf(A(H_z=D('0.05000253')), P)['EU'] >= 0 else '0' for P in range(2317187, 2317199))
    s('  Ziel von 2.317.187 bis 2.317.198', lage, '110000111100')
    pe = tragbarer_preis(A(H_z=D('0.05000253'), ek_verf=D(1200000))); s('  mit 1,2 Mio. Eigenkapital: Grenze und Meldung', f"{pe['grenze']} {pe['meld']}", 'eigenkapital None')
    ps = preissuche(A(stau=D(6000000), stau_jahr=0)); s('Massnahme 6 Mio. zum Stichtag', str(ps['meld']), 'M-32'); s('  Rendite beim kleinsten Preis', ps['r_U'], '-1,905 %', 3, True)
    s('Zielrendite -50 %', str(preissuche(A(H_z=D('-0.5')))['meld']), 'M-33')
    ps = preissuche(mit(A(), O=2317235)); s('Obergrenze genau beim tragbaren Preis', f"{ps['P']} {ps['meld']}", '2317235 None')
    ue = dict(rest=D(2000000), zins=D('0.06'), tilg=D('0.02'), zb=10, anschluss=D('0.05'))
    ps = preissuche(A(vf=D(4), uebern=ue)); s('uebernommenes Darlehen 2,0 Mio., Verkaufsfaktor 4: U', D(ps['U']), '1.818.182', 0); s('  Meldung', str(ps['meld']), 'M-32')
    cv = A(enk=D(0), vf=D(5), stau=D(0), H_beta=D(1), H_mu=D(1), H_h25=D('0.04'))
    pv = tragbarer_preis(cv); s('Vollfinanzierung: Meldung', str(pv['meld']), 'M-41'); s('  Nebenangabe', D(pv['nebenangabe']), '1.569.899', 0)
    pv = tragbarer_preis(mit(cv, ek_verf=D(0))); s('Vollfinanzierung mit E-60 = 0: Meldung', str(pv['meld']), 'M-41'); s('  Nebenangabe', D(pv['nebenangabe']), '1.569.899', 0)
    for k, s_ in ((0, '1.733.333'), (1, '1.763.092')):
        pe = tragbarer_preis(A(stau=D(420000), stau_jahr=k, ek_verf=D(1200000))); s(f'Massnahme 420.000 im Jahr {k}, 1,2 Mio. Eigenkapital', D(pe['P']), s_, 0)
    pe = tragbarer_preis(A(stau_jahr=0, ek_verf=D(100), H_beta=D(0), H_z=D('0.01'))); s('Eigenkapital 100 Euro ohne Beleihung', str(pe['meld']), 'M-46')
    s('Leerstand 100 % ohne Forderungsausfall', str(preissuche(A(H_leer=D(1), H_ford=D(0)))['meld']), 'M-31')
    c36 = A(stau=D(336000), stau_jahr=1, H_z=D('0.0371259'))
    akt = lambda P: 'M-36' in lauf(c36, P)['meld']
    s('Erhaltung 336.000 im Jahr 1: aktiviert bis 2.350.089, ab 2.350.090 nicht', str((akt(2350089), akt(2350090))), '(True, False)')
    ps = preissuche(c36, zusatz=(2350089, 2350090)); s('  P*', D(ps['P']), '2.350.070', 0); s('  Meldung', str(ps['meld']), 'M-34')
    k15 = dict(K_kst={j: D('0.15') for j in range(2027, 2070)})
    s('Katalog mit 15 % Koerperschaftsteuer: tragbarer Preis niedriger um', D(P0 - preissuche(A(**k15))['P']), '47.134', 0)
    s('  im Stressfall', D(preissuche(c, stress=True)['P'] - preissuche(A(**k15), stress=True)['P']), '37.800', 0)

    Z.titel('RF-08 Darlehensbausteine (R-5.4, R-5.5, R-5.9, R-5.11, R-14.1)')
    s('Laufzeitannuitaet 2.000 zu 7,5 % ueber 5 Jahre', annuitaet(D(2000), D('0.075'), 5), '494', 0)
    s('  21.869 zu 10 % ueber 10 Jahre', annuitaet(D(21869), D('0.10'), 10), '3.559', 0)
    s('  17.798,40 zu 4 % ueber 25 Jahre', annuitaet(D('17798.40'), D('0.04'), 25), '1.139,31')
    s('  700.000 zinslos ueber 20 Jahre', annuitaet(D(700000), D(0), 20), '35.000,00'); s('  zu 0,01 %', annuitaet(D(700000), D('0.0001'), 20), '35.036,76')
    s('Prozentannuitaet 700.000, Zins 0, Tilgung 2 %: Monatsrate', r2(D(700000) * D('0.02') / 12), '1.166,67')
    t = Tranche('r', D(600000), 'raten', D('0.03'), m=20); t.plan(20, 1)
    s('Ratentilgung 600.000: Tilgung', t.s['tilg'][1], '30.000,00'); s('  Zins J1 bis J3', ' / '.join(fmt(t.s['zins'][j]) for j in (1, 2, 3)), '18.000,00 / 17.100,00 / 16.200,00')
    s('  Restschuld nach fuenf Jahren', t.s['rest'][5], '450.000,00')
    t = Tranche('r', D(100000), 'raten', D('0.03'), m=7); t.plan(7, 12)
    s('100.000 in sieben Monatsraten', fmt(t.s['tilg'][1]) + ' / ' + fmt(t.s['tilg'][6]) + ' / ' + fmt(t.s['tilg'][7] + t.s['abl'][7]), '14.285,71 / 14.285,71 / 14.285,74')
    RUNDEN[0] = False
    for regel, s_ in (('tilgungssatz', '90.942'), ('rate', '89.760'), ('restlaufzeit', '104.989')):
        t = Tranche('b', D(1496000), 'prozent', D('0.04'), D('0.02'), zb_ende=10, anschluss=D('0.06'), regel=regel); t.plan(12, 1)
        if regel == 'tilgungssatz':
            s('Anschluss: Restschuld nach zehn Jahren', t.s['rest'][10], '1.136.777,27')
        s(f'Anschluss "{regel}": Rate ab Jahr 11', t.s['zins'][11] + t.s['tilg'][11], s_, 0)
    RUNDEN[0] = True
    t = Tranche('f', D(2320000), 'raten', D(0), m=42, einb=D(23200), beitrag=D('0.005'), zb_ende=35, anschluss=D('0.05')); t.plan(40, 1)
    s('Foerderdarlehen 2.320.000: Rate', t.s['tilg'][1], '55.238,10'); s('  Beitrag im ersten Jahr', t.s['beitr'][1], '11.600,00')
    s('  Restschuld nach 35 Jahren', t.s['rest'][35], '386.666,50'); s('  Zins im 36. Jahr', t.s['zins'][36], '19.333,33')

    Z.titel('RF-09 Regel des Bankdarlehens, drei Grenzen (R-5.12)')

    def bank(W, M, re, beta=D('0.65'), ue=D(0), kd_ue=D(0), zus=D(0), mek=D(0), p=1, ik=D('0.06'), mu=D('1.2')):
        A_ = beta * W - ue
        C_ = M - ue - zus - mek
        B_ = floor2((re / mu - kd_ue) / ik)
        while B_ > 0 and re < mu * (kd_ue + p * r2(B_ * ik / p)):
            B_ -= CENT
        mn = min(A_, B_, C_)
        L_ = max(D(0), floor2(mn)) if B_ > 0 else D(0)
        return A_, B_, C_, L_, 'abc'[[A_, B_, C_].index(mn)], M - ue - zus - L_
    kdf = D(5400000) / 42 + D(27000)       # Anhang A.3: Kapitaldienst als Eingabe des Bausteins, ungerundet
    s('Kapitaldienst des Foerderdarlehens im Beispiel', kdf, '155.571,43'); s('  Reinertrag, ab dem etwas fuer die Bank bleibt', D('1.2') * kdf, '186.685,71')
    nbk = dict(ue=D(5400000), kd_ue=kdf, zus=D(1800000), mek=D(1800000))
    T = [('Ankauf 2,6 Mio.', bank(D(2600000), D(2782000), D(107712)), '1.690.000,00', '1.496.000,00', '2.782.000,00', '1.496.000,00', 'b', '1.286.000,00'),
         ('Ankauf 2,2 Mio.', bank(D(2200000), D(2354000), D(107712)), '1.430.000,00', '1.496.000,00', '2.354.000,00', '1.430.000,00', 'a', '924.000,00'),
         ('uebernommenes Darlehen 1,0 Mio.', bank(D(2000000), D(2200000), D(140000), ue=D(1000000), kd_ue=D(25000)), '300.000,00', '1.527.777,74', '1.200.000,00', '300.000,00', 'a', '900.000,00'),
         ('Neubau 65 %, 400.000', bank(D(10000000), D(10000000), D(400000), **nbk), '1.100.000,00', '2.962.698,41', '1.000.000,00', '1.000.000,00', 'c', '1.800.000,00'),
         ('Neubau 60 %', bank(D(10000000), D(10000000), D(400000), beta=D('0.6'), **nbk), '600.000,00', '2.962.698,41', '1.000.000,00', '600.000,00', 'a', '2.200.000,00'),
         ('Neubau 65 %, 200.000', bank(D(10000000), D(10000000), D(200000), **nbk), '1.100.000,00', '184.920,58', '1.000.000,00', '184.920,58', 'b', '2.615.079,42'),
         ('Neubau 180.000', bank(D(10000000), D(10000000), D(180000), **nbk), '1.100.000,00', '-92.857,14', '1.000.000,00', '0,00', 'b', '2.800.000,00')]
    for name, (A_, B_, C_, L_, bd, ek), a, b, c_, l, bi, e in T:
        s(name + ': A', A_, a); s(name + ': B', B_, b); s(name + ': C', C_, c_); s(name + ': Bankdarlehen', L_, l); s(name + ': bindet', bd, bi); s(name + ': Eigenkapital', ek, e)
    s('Knick zwischen (a) und (b)', D(1496000) / D('0.65'), '2.301.538,46')
    A_, B_, C_, L_, bd, ek = bank(D(2600000), D(2782000), D('107712.37'), p=12)
    s('Monatsraster: geschlossene Form', D('107712.37') / D('1.2') / D('0.06'), '1.496.005,14')
    s('Monatsraster: gewaehrt', B_, '1.496.004,99'); s('  Kapitaldienst', 12 * r2(B_ * D('0.06') / 12), '89.760,24'); s('  Deckung', D('107712.37') / (12 * r2(B_ * D('0.06') / 12)), '1,200001', 6)


if __name__ == '__main__':
    main()
    Z.summe()
