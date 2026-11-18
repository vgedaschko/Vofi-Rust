import sys; sys.dont_write_bytecode=True; sys.path.insert(0, "/home/user/vofi-rust/research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner")
from decimal import Decimal as D
from dataclasses import replace
import annahmen as A, grobkalkulation as G
e=G.rechne_grob(A.NEUBAU,A.VORGABEN_NEUBAU); bm=e.bemessung
print("Neubau RE_VJ", bm.reinertrag_vj, "Soll VJ", e.sollmiete_vj, "Anteil Kosten+Ausfall", 1-bm.reinertrag_vj/e.sollmiete_vj, "L",e.darlehen, bm.bank["bindend"], "B", bm.bank["b"])
re15=e.sollmiete_vj*D("0.85"); print("RE bei 15%", re15, "B15", (re15/D("1.2"))/D("0.06"))
eg=replace(A.ANKAUF, gebunden_anteil=D("0.4"), bindung_jahre=6, gebundene_miete=D("6.80"), geb_steigerung=D("0.0615"),
  uebernommen=dict(restschuld=D(500000), zins=D("0.005"), tilgungssatz=D("0.02"), bindung_jahre=8, anschluss_zins=D("0.03")))
for z in ("0.005","0.03"):
  u=dict(eg.uebernommen); u["zins"]=D(z)
  b=G.rechne_grob(replace(eg,uebernommen=u),A.VORGABEN); bb=b.bemessung.bank
  print("uebernommen zins",z,"KD",b.bemessung.kd_uebrige,"B",round(bb["b"],2),"L",b.darlehen,bb["bindend"])
