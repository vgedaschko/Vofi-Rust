from kern import *
from rf12 import show
c = neubau()
c4 = dict(c); c4['nb_d'] = 4
print('Lesart nb_d=4: EW', fmt(rechne(c4)['EW']), ' (Soll 9.796.187,08)')
# ---------- gefoerdert, 38 Jahre
for bj in ('planjahr', 'bindungsjahr'):
  for sp in ('zuschuss_rest', 'darlehen_rest'):
    f = dict(c); f.update(foerder=True, n=38, bind_jahr=bj, split=sp)
    R = rechne(f)
    print('---', bj, sp)
    show('Endwert 38', R['EW'], '9.943.743,02'); show('dEW', R['dEW'], '5.305.318,55'); show('Rendite', R['r'], '3,558 %', 3, True)
    show('Zuschuss PJ1', sum(R['zus_fl'][:13]), '1.091.037,68'); show('Zuschuss PJ2', sum(R['zus_fl'][13:25]), '652.792,79')
f = dict(c); f.update(foerder=True, n=38)
R = rechne(f)
print('=== Voreinstellung')
show('zuwendungsfaehig', R['zk'], '8.719.152,34'); show('Foerderdarlehen', R['fd'], '5.231.491,40'); show('Zuschuss', R['zu'], '1.743.830,47')
show('MindestEK', R['mind_ek'], '1.743.830,47'); show('Entgelte', R['entg'], '65.393,64'); show('M', R['M'], '9.080.545,98')
show('Rohertrag', R['roh_n'], '196.800,00'); show('RE_n', R['re_n'], '159.216,75'); show('KD Foerder', R['kd_foerder'], '150.431,28')
show('A', R['A'], '628.357,62'); show('B', R['B'], '-253.580,79'); show('C', R['C'], '361.393,64'); show('L', R['L'], '0,00')
show('EK Ausgleich', R['EK'], '2.105.224,11'); show('EK Invphase', R['ek_inv'], '2.444.791,88')
show('Steuer PJ1', R['jahr'][0]['tax'], '323.074,06'); show('Steuer PJ2', R['jahr'][1]['tax'], '156.396,63')
show('Nachschuss PJ1', sum(R['nach'][1:13]), '329.350,86'); show('Nachschuss PJ2', sum(R['nach'][13:25]), '210.262,24'); print('  spaeter', sum(R['nach'][25:]))
show('Deckung VJ', R['deck_vj'], '1,0595', 4); show('kleinste Deckung', R['deck_min'][0], '1,0594', 4); print('   Planjahr', R['deck_min'][1], 'soll 4')
show('KD-Reserve', R['re_vj']-D('1.2')*R['kd_vj'], '-21.113,95')
show('Deckung uebrige', R['re_n']/R['KD_U'], '1,0584', 4); show('KD-Reserve uebrige', R['re_n']-D('1.2')*R['KD_U'], '-21.300,79')
show('noetiger RE', D('1.2')*(R['KD_U']+12*r2(R['C']*D('0.07')/12)), '210.874,61')
show('EK ueber MindEK', R['ek_inv']-R['mind_ek'], '700.961,41')
print('Meldungen', sorted(R['meld']))
for m,s_ in [(22,'8,2000'),(55,'8,7043'),(91,'9,2396'),(127,'9,8079')]:
    show(f'geb. Miete M{m}', R['qm'](m), s_, 4)
S = rechne(f, stress=True, basis=R)
show('Stress kleinste Deckung', S['deck_min'][0], '1,0192', 4); print(' Stress Deckung VJ', S['deck_vj'], sorted(S['meld']))
for n, s_ in zip((36,37,38,39), ('3,610 %','3,589 %','3,558 %','3,788 %')):
    ff = dict(f); ff['n']=n
    show(f'Rendite {n} J', rechne(ff, detail=False)['r'], s_, 3, True)
f20 = dict(f); f20['n']=20
R20 = rechne(f20)
show('20 J Rendite', R20['r'], '1,675 %', 3, True); show('20 J dEW', R20['dEW'], '129.107,95'); show('20 J Rueckzahlung', R20['rueck'], '822.091,51')
show('20 J Verkaufspreis', R20['vpreis'], '6.655.683,14'); show('20 J Abloesung FD', R20['tr'][0].s['abl'][240], '2.927.144,72')
# frei finanziert 38 Jahre (Vergleich)
fr = dict(c); fr['n']=38
Rf = rechne(fr, detail=False)
show('Differenz dEW gefoerdert-frei', R['dEW']-Rf['dEW'], '-11.086.819,70')
# Lesart 1 MA-026
f1 = dict(f); f1['ma026_1']=True
R1 = rechne(f1, detail=False)
show('Lesart 1: A', R1['A'], '5.859.849,02'); show('Lesart 1: L', R1['L'], '0,00')
