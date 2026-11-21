"""Eigene Werte zu Groessen, fuer die das Dokument keinen Sollwert nennt (zum Abgleich durch den Auftraggeber der Blindrechnung)."""
from kern import *
from rf11g import geb
from rf13 import fall
def z(name, R): print(f"{name:52s} EW {fmt(R['EW']):>16s}  EW_U {fmt(R['EWU']):>16s}  dEW {fmt(R['dEW']):>16s}  r {pct(R['r'])}  rU {pct(R['rU'])}  L {fmt(R['L'])}")
R = rechne(geb()); z('Ankauf gebunden (Rang vor)', R)
S = rechne(geb(), stress=True, basis=R); z('Ankauf gebunden, Stress', S)
c = geb(); c['uebern'] = dict(c['uebern'], rang='nach'); z('Ankauf gebunden, Rang nach der Bank', rechne(c))
z('Ankauf gebunden, Lesart 2 MA-026', rechne(geb(ma026_2=True)))
z('Ankauf gebunden, 5 Jahre', rechne(geb(n=5)))
for name, kw in [('Koerp. mit Kennzeichen', dict(kennz=True)), ('Koerp. sofort', dict(verlust='sofort')), ('Koerp. ohne GewSt', dict(status='koerp_ohne')),
                 ('PG orig. 400', dict(status='pg_orig')), ('PG orig. 440', dict(status='pg_orig', hebesatz='4.4')),
                 ('PG orig. 440, 60 %', dict(status='pg_orig', hebesatz='4.4', anteil=D('0.6'))),
                 ('PG orig. 440 sofort', dict(status='pg_orig', hebesatz='4.4', verlust='sofort')),
                 ('PG gepr. 440 Kennz.', dict(status='pg_gepr', hebesatz='4.4', kennz=True)),
                 ('Einzelunternehmen 440', dict(status='einzel', hebesatz='4.4')),
                 ('Privatperson 12 J', dict(status='privat')), ('Privatperson 10 J', dict(status='privat', n=10)), ('befreit', dict(status='befreit'))]:
    z('RF-13 ' + name, rechne(fall(**kw), detail=False))
n = neubau(); R = rechne(n); z('Neubau frei 15 J', R); z('Neubau frei 15 J Stress', rechne(n, stress=True, basis=R))
k = dict(n); k['kfw'] = D(3000000); z('Neubau KfW 15 J', rechne(k))
f = dict(n); f.update(foerder=True, n=38); R = rechne(f); z('Neubau gefoerdert 38 J', R); S = rechne(f, stress=True, basis=R); z('Neubau gefoerdert 38 J Stress', S)
fr = dict(n); fr['n'] = 38; z('Neubau frei 38 J', rechne(fr, detail=False))
ps = preissuche(f); print('tragbarer Grundstueckspreis gefoerdert 38 J:', ps)
ps = preissuche(n, stress=True); print('tragbarer Grundstueckspreis frei, Stress:', ps)
# Entgeltverteilung
c = dict(f); R = rechne(c)
print('e_op PJ1..3', [fmt(j['e_op']) for j in R['jahr'][:3]], ' Verlustvortrag Ende', R['jahr'][-1]['vv_e'], R['jahr'][-1]['vv_g'])
