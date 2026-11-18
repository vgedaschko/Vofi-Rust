import sys; sys.path.insert(0, sys.argv[1])
from decimal import Decimal as D
import grobkalkulation as g, annahmen as a, proben
cnt=[0,0]
orig=g.rechne_grob
def wrap(*k,**kw):
    e=orig(*k,**kw); cnt[0]+=1
    if e.befunde: cnt[1]+=1
    return e
g.rechne_grob=wrap
t=g.tragbarer_preis(a.ANKAUF,a.VORGABEN)
print("Preis",t["preis"],"Laeufe",cnt[0],"mit Befunden",cnt[1])
# Fehlerinjektion: P-04 verletzen -> wird trotzdem eine Rendite geliefert?
g.rechne_grob=orig
proben_orig=g.pruefe_mittel
g.pruefe_mittel=lambda h,v:[("P-04",None,D(1))]
e=orig(a.ANKAUF,a.VORGABEN)
print("Befunde",e.befunde,"Rendite trotzdem",e.kennzahlen["rendite"])
print("tragbarer Preis trotz verletzter Probe:", g.tragbarer_preis(a.ANKAUF,a.VORGABEN)["preis"])
g.pruefe_mittel=proben_orig
# Vergleich zweier Fassungen: welche Kennzahlen
e2=orig(a.ANKAUF,a.VORGABEN,preis=2500000)
for z in g.vergleiche(e,e2): print(z[0])
# Summe gerundeter Jahreswerte vs. gerundete Summe (Darstellung in vollen Euro)
from finanzplan import verdichte
j=verdichte(e.plan)
for k in ("miete","zins","steuer","kosten"):
    s=sum(x[k] for x in j); sr=sum(x[k].quantize(D(1)) for x in j)
    print(k, s, "Summe in vollen Euro gerundeter Jahre", sr, "Abw.", sr-s.quantize(D(1)))
