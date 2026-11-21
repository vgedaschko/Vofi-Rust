from kern import *
from rf12 import show
c = neubau(); f = dict(c); f.update(foerder=True, n=38)
soll = {'zufluss': ('3,558 %','5.305.318,55','2.444.791,88','9.943.743,02','1,675 %'),
        'verteilt': ('3,973 %','5.700.811,35','2.121.717,82','9.514.153,26','2,137 %'),
        'minderung': ('3,974 %','5.706.360,57','2.121.717,82','9.519.702,48','2,137 %')}
for les, s_ in soll.items():
    ff = dict(f); ff['ma031']=les
    R = rechne(ff, detail=False)
    show(les+' Rendite 38', R['r'], s_[0], 3, True); show(les+' dEW', R['dEW'], s_[1]); show(les+' EK Invphase', R['ek_inv'], s_[2]); show(les+' EW', R['EW'], s_[3])
    ff['n']=20; show(les+' Rendite 20', rechne(ff, detail=False)['r'], s_[4], 3, True)
ff = dict(f); ff['ma032_sofort']=True
R = rechne(ff, detail=False); show('Entgelte sofort: Rendite', R['r'], '3,573 %', 3, True); show('Entgelte sofort: dEW', R['dEW'], '5.321.983,34')
R = rechne(f)
print('Entgelt-Verteilung PJ1..3 (soll 1.499,85 / 1.799,82 / 1.799,82): siehe einb_abz im Code; Probe ueber e_op')
ff = dict(f); ff['ma031']='minderung'; R = rechne(ff, detail=False)
print('Gebaeudeanteil soll 1.543.830,47: ', fmt(r2(R['zu']*R['zk_bau']/R['zk'])))
