from kern import *
from rf12 import show
import copy
def A(**kw):
    c = ankauf(); c['H'] = dict(c['H']); c['K'] = dict(c['K'])
    for k, v in kw.items():
        if k.startswith('H_'): c['H'][k[2:]] = v
        elif k.startswith('K_'): c['K'][k[2:]] = v
        else: c[k] = v
    return c
B0 = rechne(A())
print('== RF-14/R-14.12 Jahresmodus')
J = rechne(A(p=1)); show('Jahresmodus EW', J['EW'], '2.514.395,05'); show('Jahresmodus r', J['r'], '4,491 %', 3, True)
print('== RF-19 Anschlussregeln')
for reg, s1, s2 in (('tilgungssatz','753.701,96','2,0853'),('rate','754.107,08','1,8358'),('restlaufzeit','754.381,58','1,7002')):
    R = rechne(A(H_regel=reg)); show(f'{reg} dEW', R['dEW'], s1); show(f'{reg} Deckung J11', R['deck'][11][0], s2, 4)
print('== RF-19 Lesarten MA-026 / H-25')
R = rechne(A(ma026_2=True)); show('Lesart 2 L', R['L'], '1.431.044,99'); show('Lesart 2 P*', D(preissuche(A(ma026_2=True))['P']), '2.359.366', 0)
R = rechne(A(H_h25=D('0.06'))); show('H-25 6 % L', R['L'], '1.073.283,74')
print('== RF-19 Einzelstress')
names = [('st_anschl','-13.920,92'),('st_zins','-51.765,45'),('st_leer','-79.558,59'),('st_miete','-161.319,43'),('st_inst','-20.422,72'),('st_vf','-238.744,64'),('st_stau','-11.346,91')]
for nm, s_ in names:
    kw = {('H_'+k): D(0) for k, _ in names if k != nm}
    c = A(**kw); S = rechne(c, stress=True, basis=B0); show('Einzelstress '+nm, S['dEW']-B0['dEW'], s_)
print('== RF-14/RF-19 Vorfaelligkeit')
R = rechne(A(n=1, stau=D(0))); show('n=1 VFE', R['vfe'], '108.146,07'); show('n=1 EW', R['EW'], '1.071.298,15'); show('n=1 r', R['r'], '-24,204 %', 3, True); show('n=1 Restschuld', R['tr'][0].abl_rest, '1.201.623,01'); print('   ', sorted(R['meld']))
R = rechne(A(n=1, zb=40, stau=D(0))); show('n=1 ZB 40 VFE', R['vfe'], '114.154,19')
R = rechne(A(n=5, zb=20, stau=D(0))); show('n=5 ZB 20 VFE', R['vfe'], '60.008,94')
R = rechne(A(n=12, zb=15, stau=D(0))); show('n=12 ZB 15 VFE', R['vfe'], '0,00'); print('   ', sorted(R['meld']))
R = rechne(A(n=12, zb=12, stau=D(0))); print('   n=12 ZB 12 VFE', R['vfe'])
print('== RF-18 MA-037 andere Lesart')
R = rechne(A(ma037_alt=True)); ch = [(m, fmt(R['qm'](m),4)) for m in range(2,70) if R['qm'](m)!=R['qm'](m-1)]; print('  ', ch, 'soll 13/28/43/58: 8,7210 / 9,0358 / 9,4473 / 9,9584')
show('MA-037 alt P*', D(preissuche(A(ma037_alt=True))['P']), '2.322.775', 0)
print('== RF-20')
R = rechne(A(zins=D(0), tilg=D(0), H_mindtilg=D(0), H_anschl_auf=D(0))); show('Zins/Tilgung null: L', R['L'], '1.560.000,00'); show('  EW', R['EW'], '2.570.143,76'); print('   bind', R['bind'])
R = rechne(A(vf=D(4), n=2, stau=D(0), ma026_2=True)); show('VF 4, n=2: Fehlbetrag', R['fehl_vk'], '926.438,19'); show('  EW', R['EW'], '0,00'); print('   ', sorted(R['meld']), 'soll M-25, M-29, M-38, M-42')
ps = preissuche(A(H_z=D('0.05000253'))); print('   Zielrendite 5,000253 %:', ps, 'soll P* 2.317.188 mit M-34')
ps = preissuche(A(stau=D(6000000), stau_jahr=0)); print('   Stau 6 Mio zum Stichtag:', ps, 'soll M-32')
ps = preissuche(A(H_z=D('-0.5'))); print('   Zielrendite -50 %:', ps, 'soll M-33')
print('== RF-14 Leerstand 99,5 %')
R = rechne(A(H_leer=D('0.995'))); show('L', R['L'], '0,00'); show('Verkaufspreis', R['vpreis'], '16.307,50'); show('lfd Nachschuss', R['nach_lfd'], '514.035,60'); print('   ', sorted(R['meld']))
print('== RF-17 anschaffungsnahe HK')
R = rechne(A(stau=D(400000))); show('AfA J3', R['afa'][3], '48.087,20'); print('   ', sorted(R['meld']))
R = rechne(A(stau=D(320000))); print('   320.000:', sorted(R['meld']), 'AfA J3', R['afa'][3])
print('== RF-14 Massnahme nach Verkauf')
R = rechne(A(stau=D(100000), stau_jahr=12, n=10)); show('Abzug', R['vpreis']-R['vkost']-R['verl'], '134.391,64')
print('== RF-11 Zielwertsuche')
def zws(make, lo, hi, step, richtung):
    # Gitter in Vielfachen von step; richtung +1: Ziel erreicht fuer grosse Werte
    f = lambda i: rechne(make(lo + step*i), detail=False)['EU'] >= 0
    a, b = 0, int((hi-lo)/step)
    if f(a) == f(b): return None
    while b - a > 1:
        m = (a+b)//2
        if f(m) == f(a): a = m
        else: b = m
    return lo + step*(b if richtung > 0 else a)
show('noetige Vergleichsmiete', zws(lambda x: A(vm=x), D(6), D(20), D('0.01'), +1), '9,60')
show('tragbarer Stau bei 2,2 Mio', zws(lambda x: A(preis=D(2200000), stau=x), D(0), D(1000000), D(100), -1), '246.500', 0)
show('kritischer Verkaufsfaktor', zws(lambda x: A(vf=x), D(10), D(40), D('0.01'), +1), '19,06')
print('   Bereich 6..9:', zws(lambda x: A(vm=x), D(6), D(9), D('0.01'), +1), '(soll keine Loesung)')
