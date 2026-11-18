from kern import *
import time
c = ankauf()
def show(name, val, soll, nd=2, p=False):
    v = pct(val, nd) if p else fmt(val, nd)
    ok = 'OK ' if v == soll else 'ABW'
    print(f"{ok} {name:45s} ist {v:>18s}  soll {soll:>18s}")
B = rechne(c)
S = rechne(c, stress=True, L_fix=B['L'])
show('Stress dEW', S['dEW'], '196.967,13')
show('Stress Rendite', S['r'], '2,362 %', 3, True)
show('Stress Abstand', S['r']-c['H']['z'], '-2,638 %', 3, True)
show('Stress EU', S['EU'], '-715.580,11')
show('Stress Deckung J1', S['deck'][1][0], '1,2354', 4)
show('Stress kleinste Deckung', S['deck_min'][0], '1,2191', 4); print('   Jahr', S['deck_min'][1])
show('Stress Deckung J11', S['deck'][11][0], '1,581', 3)
t=S['tr'][0]
wert120 = c['vf']*D('0.9')*12*S['soll'][120]*(1-D('0.035'))
show('Stress Restschuld zum Wert', t.s['rest'][120]/wert120, '35,22 %', 2, True)
show('Stress L', S['L'], '1.226.609,99')
# Haltedauertabelle
soll = ['3,953 %','4,203 %','4,383 %','4,276 %','4,527 %','4,577 %']
for n, s_ in zip(range(8,14), soll):
    cc = dict(c); cc['n']=n
    show(f'Haltedauer {n}', rechne(cc, detail=False)['r'], s_, 3, True)
# Preissuche
t0=time.time()
ps = preissuche(c)
print(ps, time.time()-t0)
show('tragbarer Preis Basis', D(ps['P']), '2.317.235', 0)
show('Obergrenze', D(ps['O']), '17.847.656', 0)
Rp = ziel_eu(c, ps['P']); Rp1 = ziel_eu(c, ps['P']+1)
show('r bei P*', Rp['r'], '5,000001 %', 6, True); show('r bei P*+1', Rp1['r'], '4,999995 %', 6, True)
show('EU bei P*', Rp['EU'], '0,35')
show('Boden bei P*', Rp['boden'], '637.239,63'); show('AfA-Grundlage', Rp['afa_grund'], '1.911.718,87')
show('noetiges EK bei P*', Rp['ek_inv'], '1.322.348,51'); show('EK gesamt bei P*', Rp['ek_ges'], '1.395.253,65')
show('Faktor bei P*', D(ps['P'])/Rp['mjm_1'], '17,47'); show('Preis je m2', D(ps['P'])/1320, '1.755,48')
show('Abstand Angebot', D(2600000-ps['P']), '282.765', 0)
print('bindet', Rp['bind'], 'L', Rp['L'])
t0=time.time()
pss = preissuche(c, stress=True)
print(pss, time.time()-t0)
show('tragbarer Preis Stress', D(pss['P']), '1.978.674', 0)
Rs = ziel_eu(c, pss['P'], True)
show('Faktor Stress', D(pss['P'])/Rs['mjm_1'], '15,23')
show('Stress kleinste Deckung bei P*', Rs['deck_min'][0], '1,2191', 4)
# Knick
for dP, s_ in zip([-20000,-10000,0,10000,20000], ['8,3876 %','8,3164 %','8,2453 %','8,1492 %','8,0542 %']):
    show(f'Rendite Knick {dP:+d}', ziel_eu(c, 1887092+dP)['r'], s_, 4, True)
# EK-Grenze
pek = preissuche(c, krit=lambda R: R['ek_ges'] <= D(1200000))
show('P_EK', D(pek['P']), '2.138.910', 0)
Re = ziel_eu(c, pek['P'])
show('EK Stichtag', Re['ek_inv'], '1.126.191,01'); show('Nachschuss', Re['nach_lfd'], '73.808,50'); show('zusammen', Re['ek_ges'], '1.199.999,51')
