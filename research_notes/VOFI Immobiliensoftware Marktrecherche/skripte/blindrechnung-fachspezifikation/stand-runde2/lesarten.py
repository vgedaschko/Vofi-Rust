from kern import *
from rf12 import show
def A(**kw):
    c = ankauf(); c['H'] = dict(c['H']); c['K'] = dict(c['K'])
    for k, v in kw.items():
        if k.startswith('H_'): c['H'][k[2:]] = v
        elif k.startswith('K_'): c['K'][k[2:]] = v
        else: c[k] = v
    return c
def NB(**kw):
    c = neubau(); c['H'] = dict(c['H']); c['K'] = dict(c['K'])
    for k, v in kw.items():
        if k.startswith('H_'): c['H'][k[2:]] = v
        elif k.startswith('K_'): c['K'][k[2:]] = v
        else: c[k] = v
    return c
print('(a) Rundungsrest der Entgeltverteilung im Verkaufsjahr ja/nein')
for er in (True, False):
    R = rechne(NB(foerder=True, n=38, einb_rest=er), detail=False); print('   einb_rest', er, fmt(R['EW']), '(Soll 9.943.743,02)')
    R = rechne(NB(foerder=True, n=20, einb_rest=er), detail=False); print('   einb_rest', er, '20 J dEW', fmt(R['dEW']), '(Soll 129.107,95)')
print('(b) Anpassungsdauer nach Bindungsende im Neubau: 4 (H-23) oder 0')
for dd in (4, 0):
    R = rechne(NB(foerder=True, n=39, nb_d_bind=dd), detail=False); print('   d', dd, '39 J', pct(R['r']), '(Soll 3,788 %)')
    R = rechne(NB(foerder=True, n=42, nb_d_bind=dd), detail=False); print('   d', dd, '42 J EW', fmt(R['EW']), pct(R['r']), '(Soll 13.319.334,95 / 3,935 %)')
print('(e) Stress: Anschlusszins = gestresster Zins + H-05 + Aufschlag (6,5 %) oder Basiszins + H-05 + Aufschlag (6,0 %)')
B0 = rechne(A())
for alt in (False, True):
    S = rechne(A(stress_anschl_alt=alt), stress=True, basis=B0); print('   alt', alt, fmt(S['dEW']), fmt(S['deck'][11][0],3), '(Soll 196.967,13 / 1,581)')
print('(17) Jahresmodus: Sollmiete = runde(Summe ungerundeter Monate) oder Summe gerundeter Monate')
for alt in (False, True):
    R = rechne(A(p=1, jm_soll_alt=alt)); print('   alt', alt, fmt(R['EW']), '(Soll 2.514.395,05)')
print('(c) Mittelabruf: Rundung der Aufteilung Darlehen/Zuschuss -> kein Unterschied (siehe rf12f.py)')
print('== RF-14 Neubau')
R = rechne(NB(foerder=True, n=42)); show('42 J EW', R['EW'], '13.319.334,95'); show('42 J r', R['r'], '3,935 %', 3, True)
tf = R['tr'][0]; show('Abloesung FD', tf.s['abl'][504], '186.840,56'); show('Rueckzahlung', R['rueck'], '0,00')
show('Bew M283', R['bew'][283], '4.927,81'); show('Bew M403', R['bew'][403], '6.807,90')
print('   letzte AfA im Planjahr', max(j for j in range(1,43) if R['afa'][j] > 0), '(soll 35); erster Zins FD im Planjahr', (min(u for u in range(1,505) if tf.s['zins'][u] > 0)-1)//12+1, '(soll 37)')
R = rechne(NB(n=3)); show('3 J EW frei', R['EW'], '5.201.901,26')
print('== R-11.15 noetige Miete')
f = NB(foerder=True, n=38); R = rechne(f, detail=False); H = f['H']
x = None
for cent in range(820, 2000):
    m = D(cent)/100
    roh = 12*r2(D(2000)*m); einz = 12*r2(r2(D(2000)*m)*D('0.98'))
    ren = roh - max(R['bew_vj'] + (roh-einz), r2(D('0.15')*roh))
    Bv = floor2((ren/H['mu'] - R['KD_U'])/D('0.07'))
    if Bv >= R['C']: x = m; break
show('noetige Miete', x, '10,40')
print('== RF-19/RF-20 weitere Preissuchen')
ps = preissuche(A(stau=D(420000), stau_jahr=0), krit=lambda R: R['ek_ges'] <= D(1200000)); show('Stau 420.000 Stichtag, EK 1,2 Mio', D(ps['P']), '1.733.333', 0)
ps = preissuche(A(stau=D(420000), stau_jahr=1), krit=lambda R: R['ek_ges'] <= D(1200000)); show('Stau 420.000 Jahr 1, EK 1,2 Mio', D(ps['P']), '1.763.092', 0)
ue = dict(rest=D(2000000), nenn=D(2000000), zins=D('0.06'), tilg=D('0.02'), zb=10, anschluss=D('0.05'), foerder=True, rang='vor')
ps = preissuche(A(vf=D(4), uebern=ue)); print('   uebern. 2,0 Mio 6 %, VF 4:', ps, '(soll U 1.818.182, M-32)')
c = A(stau=D(6000000), stau_jahr=0); c['preis']=D(1); print('   Stau 6 Mio, Rendite bei U:', pct(rechne(c, detail=False)['r']), '(soll -1,905 %)')
c = A(enk=D(0), vf=D(5), stau=D(0), H_beta=D(1), H_mu=D(1), ma026_2=True)
ps = preissuche(c); R = ziel_eu(c, ps['P']); print('   Vollfinanzierung:', ps, 'D', R['Dn'], '(soll M-41, Nebenangabe 1.569.899)')
