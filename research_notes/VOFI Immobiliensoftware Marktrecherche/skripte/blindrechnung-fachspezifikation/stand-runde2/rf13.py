from kern import *
from rf12 import show
def fall(**kw):
    c = ankauf(); c['K'] = dict(c['K'])
    for k, v in kw.items():
        if k == 'hebesatz': c['K']['hebesatz'] = D(v)
        else: c[k] = v
    return c
F = [
 ('1 Koerperschaft', fall(), '4,527 %'),
 ('2 Koerperschaft mit Kennzeichen', fall(kennz=True), '4,697 %'),
 ('3 Koerperschaft Kennz., andere Lesart MA-030', fall(kennz=True, ma030_alt=True), '5,161 %'),
 ('4 Koerperschaft sofort', fall(verlust='sofort'), '4,523 %'),
 ('5 Koerperschaft ohne GewSt', fall(status='koerp_ohne'), '5,185 %'),
 ('6 PG originaer 400', fall(status='pg_orig'), '3,649 %'),
 ('7 PG originaer 440', fall(status='pg_orig', hebesatz='4.4'), '3,585 %'),
 ('8 PG originaer 440, 60 %', fall(status='pg_orig', hebesatz='4.4', anteil=D('0.6')), '3,324 %'),
 ('9 ??? (im Text nicht benannt)', None, '3,659 %'),
 ('10 PG gepraegt Kennz. 440', fall(status='pg_gepr', hebesatz='4.4', kennz=True), '3,597 %'),
 ('11 PG 440, 60 %, MA-036 andere Lesart', fall(status='pg_orig', hebesatz='4.4', anteil=D('0.6'), ma036_alt=True), '3,487 %'),
 ('12 Einzelunternehmen 440', fall(status='einzel', hebesatz='4.4'), '3,585 %'),
 ('13 Privatperson 12 J', fall(status='privat'), '5,141 %'),
 ('14 befreit', fall(status='befreit'), '5,661 %'),
]
res = {}
for name, c, s_ in F:
    if c is None: print('--  ', name, 'soll', s_); continue
    R = rechne(c, detail=False); res[name] = R
    show(name, R['r'], s_, 3, True)
show('rU Koerp. mit Kennz.', res['2 Koerperschaft mit Kennzeichen']['rU'], '1,483 %', 3, True)
show('rU Koerp. ohne GewSt', res['5 Koerperschaft ohne GewSt']['rU'], '1,763 %', 3, True)
# GewSt auf Verkaufsgewinn mit Kennzeichen
c = fall(kennz=True); R = rechne(c)
print('Kennz.: Steuer letztes Jahr', R['jahr'][-1]['tax'], 'Steuer auf Verkauf', R['steuer_verkauf'], '(GewSt auf Verkaufsgewinn soll 139.930,00)')
for n, s_ in zip((9,10,11,12), ('3,365 %','3,528 %','4,882 %','5,141 %')):
    R = rechne(fall(status='privat', n=n)); show(f'Privat {n} J', R['r'], s_, 3, True)
    if n == 10: show('Privat 10 J Steuer auf Gewinn', R['steuer_verkauf'], '334.954,62'); print('   vfe', R['vfe'], sorted(R['meld']))
# Kandidaten fuer Nr. 9 (3,659 %)
K9 = [
 ('PG orig 400 sofort', fall(status='pg_orig', verlust='sofort')),
 ('PG orig 440 sofort', fall(status='pg_orig', hebesatz='4.4', verlust='sofort')),
 ('PG orig 440 60% sofort', fall(status='pg_orig', hebesatz='4.4', anteil=D('0.6'), verlust='sofort')),
 ('PG gepr 400 Kennz', fall(status='pg_gepr', kennz=True)),
 ('PG gepr 440 Kennz MA-030 alt', fall(status='pg_gepr', hebesatz='4.4', kennz=True, ma030_alt=True)),
 ('PG gepr 400 Kennz MA-030 alt', fall(status='pg_gepr', kennz=True, ma030_alt=True)),
 ('PG gepr 440 ohne Kennz', fall(status='pg_gepr', hebesatz='4.4')),
 ('PG gepr 440 60% Kennz', fall(status='pg_gepr', hebesatz='4.4', anteil=D('0.6'), kennz=True)),
 ('PG gepr 440 60% Kennz MA-030 alt', fall(status='pg_gepr', hebesatz='4.4', anteil=D('0.6'), kennz=True, ma030_alt=True)),
 ('Einzel 400', fall(status='einzel')),
 ('Einzel 440 sofort', fall(status='einzel', hebesatz='4.4', verlust='sofort')),
 ('Einzel 400 sofort', fall(status='einzel', verlust='sofort')),
 ('PG orig 400 MA-036', fall(status='pg_orig', ma036_alt=True)),
 ('PG orig 440 MA-036', fall(status='pg_orig', hebesatz='4.4', ma036_alt=True)),
 ('PG orig 400 60%', fall(status='pg_orig', anteil=D('0.6'))),
 ('Privat sofort', fall(status='privat', verlust='sofort')),
 ('Privat 10 J', fall(status='privat', n=10)),
]
for name, c in K9:
    print(f'   Kandidat {name:36s}', pct(rechne(c, detail=False)['r']))
