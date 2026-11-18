from kern import *
from rf12 import show
def geb(**kw):
    c = ankauf()
    c.update(geb=D('0.4'), geb_ende=6, geb_miete=D('6.80'),
             uebern=dict(rest=D(500000), nenn=D(600000), zins=D('0.005'), tilg=D('0.02'), zb=8, anschluss=D('0.03'),
                         beitrag=D(0), foerder=True, rang='vor'))
    c.update(kw); return c
# GewSt auf Verkaufsgewinn mit Kennzeichen (RF-13)
c = ankauf(); c['kennz']=True; R = rechne(c)
print('Kennz. letztes Jahr Steuerdetails', R['st_log'][-1][5], ' z_h', R['st_log'][-1][2])
for basis in ('rest', 'nenn'):
  for al in ('exakt', 'runde', 'monat'):
    c = geb(ueb_kalk_basis=basis, ausfall_lesart=al)
    R = rechne(c)
    print(f'--- KD_U-Basis {basis}, Mietausfall {al}: RE_n {R["re_n"]}  KD_U {R["KD_U"]}  A {R["A"]} B {R["B"]} C {R["C"]} L {R["L"]} bind {R["bind"]}')
    show('dEW gebunden', R['dEW'], '581.756,83')
c = geb(); R = rechne(c)
soll = '7,8200 / 7,8200 / 7,8200 / 8,5557 / 8,5557 / 8,7523 / 9,1037 / 9,4387 / 9,5630 / 9,7879 / 10,3025 / 10,5690'.split(' / ')
for j, s_ in enumerate(soll, 1):
    show(f'Miete Vorhaben J{j}', R['qm']((j-1)*12+1), s_, 4)
gm = R['teile'][1][1]
for m, s_ in [(1,'6,8000'),(37,'7,2182'),(84,'7,2182'),(85,'8,0556'),(100,'8,3009'),(121,'9,2640'),(136,'9,5461')]:
    show(f'geb. Miete M{m}', gm[m], s_, 4)
print('Spruenge geb.', [m for m in range(2,145) if gm[m]!=gm[m-1]])
tu = [t for t in R['tr'] if t.name=='uebernommen'][0]
show('Rate uebern.', tu.s['zins'][1]+tu.s['tilg'][1], '1.250,00'); show('KD J1 uebern.', R['kd_je']['uebernommen'], '15.000,00')
B0 = rechne(ankauf(), detail=False)
show('Differenz dEW', R['dEW']-B0['dEW'], '-171.945,13')
S = rechne(c, stress=True, basis=R)
tus = [t for t in S['tr'] if t.name=='uebernommen'][0]
show('Stress: Zins uebern. J9', sum(tus.s['zins'][97:109]), '15.772,22')
# RF-19: Verkauf nach 5 Jahren
c5 = geb(n=5); R5 = rechne(c5); show('VFE 5 J (Bank allein)', R5['vfe'], '33.080,71')
c5b = geb(n=5); c5b['uebern'] = dict(c5b['uebern'], foerder=False); R5b = rechne(c5b); show('VFE 5 J ohne Kennz. FD', R5b['vfe'], '46.182,48')
print('   L mit/ohne Kennzeichen', R5['L'], R5b['L'])
