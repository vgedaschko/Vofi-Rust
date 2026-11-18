import sys; sys.path.insert(0, "/home/user/vofi-rust/research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner")
from decimal import Decimal as D
import annahmen as A, grobkalkulation as G
e=G.rechne_grob(A.NEUBAU,A.VORGABEN_NEUBAU)
z=e.plan.zeilen; L=e.darlehen
aus=[z[u]["tranchen"]["Bankdarlehen"]["auszahlung"] for u in range(0,19)]
print("L",L, "Auszahlungen", [round(float(x)) for x in aus])
for frei in (0,6,12):
  offen=L; s=D(0)
  for m in range(0,19):
    if m>0 and m>frei: s+=offen*D("0.0025")
    offen-=aus[m]
  print("bereitstellungsfrei",frei,"Monate: ",round(float(s)))
print("Bauzeitzinsen", sum(z[u]["tranchen"]["Bankdarlehen"]["zins"] for u in range(0,19)))
