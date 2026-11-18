import sys; sys.path.insert(0, "/home/user/vofi-rust/research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner")
from decimal import Decimal as D
import annahmen as A, grobkalkulation as G, time
orig=G.bankdarlehen
t=time.time()
p0=G.tragbarer_preis(A.ANKAUF,A.VORGABEN)
print("Basis", p0 if not isinstance(p0,dict) else {k:v for k,v in p0.items() if k in('preis','bindend','darlehen')}, time.time()-t)
def kalk(wert, quote, re, mu, zins, tilg, mb, **kw):
    return orig(wert, quote, re, mu, zins+D("0.01"), tilg, mb, **kw)
G.bankdarlehen=kalk
e=G.rechne_grob(A.ANKAUF,A.VORGABEN); print("L kalk 5%", e.darlehen, e.bemessung.bank["bindend"], "EK", e.eigenkapital_investitionsphase)
p1=G.tragbarer_preis(A.ANKAUF,A.VORGABEN)
print("kalk", p1 if not isinstance(p1,dict) else {k:v for k,v in p1.items() if k in('preis','bindend','darlehen')})
