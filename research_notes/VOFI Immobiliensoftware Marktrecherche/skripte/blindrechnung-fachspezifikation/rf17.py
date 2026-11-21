# -*- coding: utf-8 -*-
"""RF-17 / RF-10: Zuschuss in der Steuer nach Vermoegenssphaere (R-7.19), Entgelte (R-7.15),
Steuerbausteine zum Verkaufsjahr und je Steuerstatus (R-7.6 bis R-7.11, R-7.16 bis R-7.18)."""
from kern import *
from rf12f import foerderfall


def st(status='koerp', **kw):
    c = mit(ankauf(), status=status, **kw)
    return Steuer(c)


def main():
    s = Z.show
    Z.titel('RF-17 Zuschuss in der Steuer (R-7.19), gefoerderter Neubau')
    T = [('Koerperschaft ohne E-41, verteilt', dict(), '3,956 %', '5.656.209,72', '2.144.688,71', '9.477.900,38', '2,081 %'),
         ('Koerperschaft ohne E-41, sofortige Einnahme', dict(ma031='sofort'), '3,559 %', '5.272.665,63', '2.447.577,01', '9.881.567,90', '1,640 %'),
         ('Koerperschaft mit E-41, verteilt', dict(kennz=True), '4,001 %', '5.811.051,82', None, None, '1,979 %'),
         ('Koerperschaft mit E-41, sofortige Einnahme', dict(kennz=True, ma031='sofort'), '3,771 %', '5.569.808,93', None, None, '1,867 %'),
         ('Privatperson, Einnahme im Zuflussjahr', dict(status='privat'), '3,808 %', '6.731.341,45', None, None, None),
         ('Privatperson, verteilt auf Antrag (E-70)', dict(status='privat', e70=True), '4,380 %', '7.281.505,57', None, None, None)]
    eig = []
    for name, kw, r38, dew, ek, ew, r20 in T:
        R = rechne(foerderfall(**kw), detail=False)
        s(name + ': Rendite 38 J', R['r'], r38, 3, True); s(name + ': Endwertdifferenz 38 J', R['dEW'], dew)
        if ek:
            s(name + ': Eigenkapital der Investitionsphase', R['ek_inv'], ek); s(name + ': Endwert 38 J', R['EW'], ew)
        else:
            eig.append((name, R['ek_inv'], R['EW']))
        if r20:
            s(name + ': Rendite 20 J', rechne(foerderfall(n=20, **kw), detail=False)['r'], r20, 3, True)
    R = rechne(foerderfall(ma031='sofort', n=20))
    s('sofort, 20 J: operatives Ergebnis des Verkaufsjahres', R['jahr'][-1]['e_op'], '-873.383,25'); s('sofort, 20 J: Verkaufsgewinn', R['g_v'], '1.824.825,10')
    R = rechne(foerderfall(status='privat', n=20, H_h38='sofort'))
    s('Privatperson sofortige Verlustverrechnung, 20 J: Steuer im Verkaufsjahr', R['jahr'][-1]['tax'], '-359.862,30'); s('  Rendite', R['r'], '2,421 %', 3, True)
    R = rechne(foerderfall(status='privat', n=20, H_h38='sofort', e70=True))
    s('  mit E-70: Steuer im Verkaufsjahr', R['jahr'][-1]['tax'], '1.876,05'); s('  mit E-70: Rendite', R['r'], '2,913 %', 3, True)
    for name, kw in (('E-70 im Betriebsvermoegen', dict(e70=True)), ('E-70 bei fuenf Jahren Bindung', dict(status='privat', e70=True, K_f_bindung=5))):
        try:
            rechne(foerderfall(**kw), detail=False); m = 'gerechnet'
        except Meldung as e:
            m = e.kennung
        s(name, m, 'M-20')

    Z.titel('RF-10 / RF-17 Steuerbausteine (R-7.6 bis R-7.18)')
    x = st(); s('Koerperschaft 100.000 im Jahr 2027', x.jahr(1, D(100000), D(0), D(0)), '29.825,00')
    s('  im Planjahr 6 (2032)', st().jahr(6, D(100000), D(0), D(0)), '24.550,00')
    s('  mit erweiterter Kuerzung', st(kennz=True).jahr(1, D(100000), D(0), D(0)), '15.825,00')
    x = st(); x.jahr(1, D(-50000), D(0), D(0)); t2 = x.jahr(2, D(80049), D(0), D(0))
    s('nach -50.000 und +80.049', t2, '8.638,24'); s('  davon Koerperschaftsteuer', x.log[-1]['det']['kst'], '4.438,24'); s('  davon Gewerbesteuer', x.log[-1]['det']['gst'], '4.200,00')
    x = st(kennz=True); t = x.jahr(1, D(100000), D(10000), D(0))
    s('E-41: 100.000 Ergebnis, 10.000 Zinsen: Koerperschaftsteuer', x.log[-1]['det']['kst'], '17.407,50'); s('  Gewerbesteuer', x.log[-1]['det']['gst'], '1.400,00')
    s('E-41, Verkaufsjahr mit 500.000 Verkaufsgewinn (Kuerzung entfaellt)', st(kennz=True).jahr(1, D(100000), D(10000), D(500000), letztes=True), '181.932,50')
    x = st(kennz=True, e69=True); t = x.jahr(1, D(100000), D(10000), D(500000), letztes=True)
    s('E-41 mit E-69', t, '97.932,50'); s('  Koerperschaftsteuer', x.log[-1]['det']['kst'], '96.532,50')
    x = st(kennz=True, e69=True); t1 = x.jahr(1, D(-50000), D(0), D(0)); t2 = x.jahr(2, D(100000), D(10000), D(500000), letztes=True)
    s('E-41, Anlaufverlust 50.000 im Jahr 2027: Steuer', t1, '0,00'); s('  gewerbesteuerlicher Vortrag', x.log[0]['vv_g'], '0,00'); s('  Folgejahr 2028 als Verkaufsjahr mit E-69', t2, '84.112,00')
    for name, kw, g, a, tt in [('400 %', dict(), '10.570,00', '10.570,00', '42.000,00'), ('280 %', dict(K_hebesatz=D('2.8')), '7.399,00', '7.399,00', '42.000,00'),
                               ('480 %', dict(K_hebesatz=D('4.8')), '12.684,00', '10.570,00', '44.114,00'), ('400 %, Anteil 50 %', dict(anteil=D('0.5')), '10.570,00', '5.285,00', '47.285,00'),
                               ('400 %, Steuersatz 8 %', dict(H_e42=D('0.08')), '10.570,00', '8.000,00', '10.570,00')]:
        x = st('pg_orig', **kw); t = x.jahr(1, D(100000), D(0), D(0)); d_ = x.log[-1]['det']
        s(f'PersGes {name}: Gewerbesteuer', d_['gst'], g); s(f'PersGes {name}: Anrechnung', d_['anr'], a); s(f'PersGes {name}: Steuer gesamt', t, tt)
    s('Privatperson 30.000 Vermietung, 1.000 Zinsen', st('privat').jahr(1, D(30000), D(1000), D(0)), '12.863,75')
    s('Privatperson -10.000 Vermietung, 500 Zinsen', st('privat').jahr(1, D(-10000), D(500), D(0)), '131,88')
    s('Privater Verkauf nach zehn Jahren', st('privat', n=10).jahr(10, D(-20000), D(0), D(200000), vfe=D(30000), letztes=True), '63.000,00')
    x = st('privat', n=11); t = x.jahr(11, D(-20000), D(0), D(200000), vfe=D(30000), letztes=True)
    s('Privater Verkauf nach elf Jahren', t, '0,00'); s('  Vermietungsverlust vorgetragen', x.vv_e, '20.000,00')
    s('Hinzurechnung: 100.000 Ergebnis, 300.000 Entgelte, 40.000 Erbbauzins', st().jahr(1, D(100000), D(0), D(0), entg=D(300000), erbbau=D(40000)), '34.025,00')
    s('  sofortige Verrechnung, 60.000 Entgelte', st(H_h38='sofort').jahr(1, D(100000), D(0), D(0), entg=D(60000)), '31.925,00')
    s('Verein 100.000 im Jahr 2027', st('verein').jahr(1, D(100000), D(0), D(0)), '15.825,00')
    s('Verein, Verkauf nach zehn Jahren (Satz 2036)', st('verein', n=10).jahr(10, D(-20000), D(0), D(200000), vfe=D(30000), letztes=True), '15.825,00')
    x = st('verein', n=11); t = x.jahr(11, D(-20000), D(5000), D(200000), vfe=D(30000), letztes=True)
    s('Verein, Verkauf nach elf Jahren mit 5.000 Zinsen', t, '0,00'); s('  Verlustvortrag', x.vv_e, '15.000,00')
    kw = dict(K_hebesatz=D('4.4'), anteil=D('0.6'))
    s('Objektverkauf PersGes 440 %, 60 %: laufender Gewinn', st('pg_gepr', **kw).jahr(1, D(0), D(0), D(500000), letztes=True), '243.285,00')
    s('  Verkauf im Rahmen der Aufgabe', st('pg_gepr', ma036_alt=True, **kw).jahr(1, D(0), D(0), D(500000), letztes=True), '222.285,00')
    kw = dict(anteil=D('0.6'))
    s('Objektverkauf PersGes 400 %, 60 % (Anhang A.3, R-15.6): laufender Gewinn', st('pg_gepr', **kw).jahr(1, D(0), D(0), D(500000), letztes=True), '236.628,00')
    s('  Verkauf im Rahmen der Aufgabe', st('pg_gepr', ma036_alt=True, **kw).jahr(1, D(0), D(0), D(500000), letztes=True), '219.828,00')
    x = st('pg_orig', H_h38='sofort'); t1 = x.jahr(1, D(-50000), D(0), D(0)); t2 = x.jahr(2, D(80000), D(0), D(0))
    s('PersGes sofort, 50.000 Verlust', t1, '-21.000,00'); s('  Folgejahr 80.000 Gewinn: Gewerbesteuer', x.log[-1]['det']['gst'], '770,00'); s('  Steuer', t2, '33.600,00')
    s('Einzelunternehmen sofort, 50.000 Verlust, 400 %', st('einzel', H_h38='sofort').jahr(1, D(-50000), D(0), D(0)), '-21.000,00')
    s('  bei 480 %', st('einzel', H_h38='sofort', K_hebesatz=D('4.8')).jahr(1, D(-50000), D(0), D(0)), '-22.400,00')
    x = st(); s('s_Z Koerperschaft 2027', x.s_z(1) * 100, '29,825', 3); x = st(kennz=True); s('s_FK mit Kennzeichen', x.s_fk(1) * 100, '15,825', 3)
    s('s_FK bei sofortiger Verrechnung', st(H_h38='sofort').s_fk(1) * 100, '26,325', 3); s('s_op PersGes 400 %', st('pg_orig').s_fk(1) * 100, '42', 0)
    return eig


if __name__ == '__main__':
    eig = main()
    Z.summe()
    for name, ek, ew in eig:
        print('eigene Werte:', name, 'EK Investitionsphase', fmt(ek), 'EW', fmt(ew))
