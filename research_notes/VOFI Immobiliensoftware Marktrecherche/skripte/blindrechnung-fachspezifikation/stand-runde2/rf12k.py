from kern import *
from rf12 import show
import time
c = neubau()
t0=time.time()
ps = preissuche(c); print(ps, round(time.time()-t0,1))
show('tragbarer Grundstueckspreis frei', D(ps['P']), '702.767', 0)
show('je m2 Grundstueck', D(ps['P'])/2500, '281,11'); show('je m2 Wfl', D(ps['P'])/2000, '351,38')
k = dict(c); k['kfw']=D(3000000)
R = rechne(k)
show('KfW: KD kalk', R['kd_kfw_kalk'], '210.000,00'); show('KfW: B', R['B'], '1.007.142,85'); show('KfW: L', R['L'], '1.007.142,85')
tk = [t for t in R['tr'] if t.name=='kfw'][0]; tb = [t for t in R['tr'] if t.name=='bank'][0]
print('KfW Abruf ab', min(tk.ausz), 'Bank ab', min(tb.ausz), '(soll 9 / 16)')
show('KfW Zins M19', tk.s['zins'][19], '6.250,00'); print('erste Tilgung KfW Monat', min(u for u in range(1,181) if tk.s['tilg'][u]>0), '(soll 31)')
show('KfW Rate M31', tk.s['zins'][31]+tk.s['tilg'][31], '11.250,00')
show('KfW Rendite', R['r'], '4,630 %', 3, True)
show('KD VJ Bank', R['kd_je']['bank'], '60.428,52'); show('KD VJ KfW', R['kd_je']['kfw'], '90.000,00')
ps = preissuche(k); show('tragbarer Grundstueckspreis KfW', D(ps['P']), '924.244', 0)
k2 = dict(k); k2['ma026_2']=True
R2 = rechne(k2); show('Lesart 2 KfW: L', R2['L'], '2.425.000,00')
ps = preissuche(k2); show('Lesart 2 KfW: Preis', D(ps['P']), '1.286.380', 0)
c2 = dict(c); c2['ma026_2']=True
ps = preissuche(c2); show('Lesart 2 ohne KfW: Preis', D(ps['P']), '876.926', 0)
# Stellplaetze
s = dict(c); s.update(stp=20, stp_miete=D(60))
Rs = rechne(s); show('Stellpl BK0', Rs['bk0'], '7.940.000,00'); show('Stellpl Soll M22', Rs['soll'][22], '34.200,00')
