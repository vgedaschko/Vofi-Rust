# -*- coding: utf-8 -*-
"""RF-11 Ankauf: Stressfall, Haltedauertabelle, Preissuche mit beiden Grenzen, Knick, Zielwertsuche, Jahresmodus
(R-11.4 bis R-11.10, R-11.13, R-2.2)."""
from kern import *


def main():
    c = ankauf()
    s = Z.show
    B = rechne(c)
    S = rechne(c, stress=True)
    Z.titel('RF-11 Ankauf Stressfall (R-11.8)')
    t = S['trd']['bank']
    s('Stress: Zins M1 entspricht 4,5 %', t.s['zins'][1], fmt(r2(S['L'] * D('0.045') / 12)))
    s('Stress: Anschlusszins 6,5 % (Zins M121)', t.s['zins'][121], fmt(r2(t.s['rest'][120] * D('0.065') / 12)))
    s('Stress: Bankdarlehen', S['L'], '1.144.835,99')
    s('Stress: Eigenkapital', S['EK'], '1.495.164,01')
    s('Stress: Endwertdifferenz', S['dEW'], '237.324,51')
    s('Stress: Rendite', S['r'], '2,489 %', 3, True)
    s('Stress: Abstand zur Zielrendite', S['r'] - c['H']['z'], '-2,511 %', 3, True)
    s('Stress: Endwertueberschuss', S['EU'], '-739.303,12')
    s('Stress: Deckung J1', S['deck'][1][0], '1,3484', 4)
    s('Stress: kleinste Deckung', S['deck_min'][0], '1,3321', 4); s('  im Planjahr', S['deck_min'][1], '3')
    s('Stress: Deckung J11', S['deck'][11][0], '1,7254', 4)
    s('Stress: Darlehen zu Kaufpreis', S['darl_quote'], '47,70 %', 2, True)
    wert120 = c['vf'] * D('0.9') * S['mjm'](120)
    s('Stress: Restschuld zum Wert', t.s['rest'][120] / wert120, '32,88 %', 2, True)
    names = [('st_anschl', '-13.920,92'), ('st_zins', '-32.897,46'), ('st_leer', '-79.558,59'), ('st_miete', '-161.319,43'),
             ('st_vf', '-238.744,64'), ('st_stau', '-11.346,91')]
    for nm, s_ in names:
        kw = {('H_' + k): D(0) for k, _ in names if k != nm}
        E = rechne(mit(c, **kw), stress=True, detail=False)
        s('Einzelstress ' + nm, E['dEW'] - B['dEW'], s_)

    Z.titel('RF-11 Haltedauertabelle (R-11.13)')
    for n_, s_ in zip(range(8, 14), ['3,953 %', '4,203 %', '4,383 %', '4,276 %', '4,527 %', '4,577 %']):
        s(f'Haltedauer {n_} Jahre', rechne(mit(c, n=n_), detail=False)['r'], s_, 3, True)

    Z.titel('RF-11 hoechster tragbarer Preis (R-11.4 bis R-11.7)')
    ps = preissuche(c)
    s('U', ps['U'], '1'); s('O', D(ps['O']), '17.847.656', 0)
    s('P* Basisfall', D(ps['P']), '2.317.235', 0); s('  Meldung', str(ps['meld']), 'None')
    Rp, Rp1 = lauf(c, ps['P'], detail=True), lauf(c, ps['P'] + 1)
    s('r bei P*', Rp['r'], '5,000001 %', 6, True); s('r bei P* + 1', Rp1['r'], '4,999995 %', 6, True)
    s('Endwertueberschuss bei P*', Rp['EU'], '0,35')
    s('Boden bei P*', Rp['boden'], '637.239,63'); s('AfA-Grundlage bei P*', Rp['afa_grund'], '1.911.718,87')
    s('Darlehen bei P*', Rp['L'], '1.226.609,99'); s('  bindet', ','.join(Rp['bind']), 'b')
    s('noetiges Eigenkapital bei P*', Rp['ek_inv'], '1.322.348,51'); s('Eigenkapital insgesamt bei P*', Rp['ek_ges'], '1.395.253,65')
    s('Faktor bei P*', D(ps['P']) / Rp['mjm_1'], '17,47')
    ist_jm = 12 * c['ist'] * (c['wfl'] - c['leerfl'])
    s('Faktor auf die Ist-Miete', D(ps['P']) / ist_jm, '17,21'); s('Faktor des Angebots', D(2600000) / ist_jm, '19,31')
    s('Preis je m2', D(ps['P']) / c['wfl'], '1.755,48')
    s('Abstand zum Angebot', D(2600000 - ps['P']), '282.765', 0)
    pss = preissuche(c, stress=True)
    s('P* Stressfall', D(pss['P']), '1.977.816', 0)
    Rs = lauf(c, pss['P'], True, detail=True)
    s('Stress-P*: noetiges Eigenkapital', Rs['ek_inv'], '1.030.761,61'); s('Stress-P*: Eigenkapital insgesamt', Rs['ek_ges'], '1.123.696,87')
    s('Stress-P*: Jahresmiete', Rs['mjm_1'], '129.927,60'); s('Stress-P*: Faktor', D(pss['P']) / Rs['mjm_1'], '15,22')
    s('Stress-P*: Faktor auf die Ist-Miete', D(pss['P']) / ist_jm, '14,69')
    s('Stress-P*: kleinste Deckung', Rs['deck_min'][0], '1,3321', 4); s('  bindet', ','.join(Rs['bind']), 'b')
    s('Knick B / beta', (B['L'] / c['H']['beta']).quantize(D(1)), '1.887.092', 0)
    for dP, s_ in zip([-20000, -10000, 0, 10000, 20000], ['8,3876 %', '8,3164 %', '8,2453 %', '8,1492 %', '8,0542 %']):
        s(f'Rendite am Knick {dP:+d}', lauf(c, 1887092 + dP)['r'], s_, 4, True)
    r0, r1, r2_ = (lauf(c, 1887092 + x)['r'] for x in (-10000, 0, 10000))
    s('Steigung links (Basispunkte)', (r1 - r0) * 10000, '-7,11'); s('Steigung rechts (Basispunkte)', (r2_ - r1) * 10000, '-9,61')
    rr = [lauf(c, P)['r'] for P in range(1500000, 3700000, 100000)]
    s('Rendite faellt 1,5 bis 3,6 Mio. in jedem Schritt', str(all(a > b for a, b in zip(rr, rr[1:]))), 'True')
    ce = mit(c, ek_verf=D(1200000))
    pe = tragbarer_preis(ce)
    s('P_EK bei 1,2 Mio. Eigenkapital', D(pe['P']), '2.138.910', 0); s('  bindende Grenze', pe['grenze'], 'eigenkapital')
    Re = lauf(c, pe['P'])
    s('  Eigenkapital zum Stichtag', Re['ek_inv'], '1.126.191,01'); s('  Nachschuss', Re['nach_lfd'], '73.808,50'); s('  zusammen', Re['ek_ges'], '1.199.999,51')

    Z.titel('RF-11 Zielwertsuche (R-11.10)')
    eu = lambda **kw: (lambda x: rechne(mit(c, **{k: (x if v is None else v) for k, v in kw.items()}), detail=False)['EU'])
    l = zielwertsuche(eu(vm=None), 6, 20, '0.01'); s('noetige Vergleichsmiete', l[0][0], '9,60'); s('  Richtung', l[0][1], 'steigend')
    l = zielwertsuche(eu(stau=None, preis=D(2200000)), 0, 1000000, 100); s('tragbarer Investitionsstau bei 2,2 Mio.', l[0][0], '246.500', 0)
    l = zielwertsuche(eu(vf=None), 8, 40, '0.01'); s('kritischer Verkaufsfaktor', l[0][0], '19,06')
    s('Bereich 6 bis 9 Euro', str(zielwertsuche(eu(vm=None), 6, 9, '0.01')), 'keine Loesung: Ziel an allen Rasterstellen verfehlt')
    l = zielwertsuche(lambda x: (x - 3) * (x - 7), 0, 10, '0.01'); s('Prueffunktion (x-3)(x-7)', ' / '.join(fmt(v) for v, _ in l), '3,00 / 7,00')
    s('Prueffunktion (x-3)(x-3,2), Rasterweite 0,25', str(zielwertsuche(lambda x: (x - 3) * (x - D('3.2')), 0, 10, '0.01')),
      'keine Loesung: Ziel an allen Rasterstellen erreicht')
    l = zielwertsuche(lambda x: x - D('2.5'), 0, 10, 1); s('Prueffunktion x - 2,5, Aufloesung 1', fmt(l[0][0], 0) + ' ' + l[0][1], '3 steigend')

    Z.titel('RF-11 / RF-14 Jahresmodus (R-2.2, R-14.12)')
    J = rechne(mit(c, p=1))
    s('Jahresmodus: Endwert', J['EW'], '2.514.395,05'); s('Jahresmodus: Rendite', J['r'], '4,491 %', 3, True)


if __name__ == '__main__':
    main()
    Z.summe()
