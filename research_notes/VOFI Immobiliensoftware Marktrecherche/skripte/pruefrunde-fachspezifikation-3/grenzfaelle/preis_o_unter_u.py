"""GF3-H2b Obergrenze der Preissuche unter der Untergrenze: M-31 oder M-22?"""
from h import *
ue = dict(restschuld=D(2000000), zins=D('0.06'), tilgungssatz=D('0.02'), bindung_jahre=10)
e = replace(ANK, uebernommen=ue, verkaufsfaktor=D(4))
for f in ('5', '10', '10.18', '10.2'):
    print(f, tp(e, replace(VG, such_obergrenze_faktor=D(f))))
