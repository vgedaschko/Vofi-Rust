import sys; sys.path.insert(0, "/home/user/vofi-rust/research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner")
from decimal import Decimal as D
from dataclasses import replace
import annahmen as A, grobkalkulation as G
from kennzahlen import schuldendienstdeckung
def dscr_reihe(e):
    n=e.ein.haltedauer
    return [round(float(schuldendienstdeckung(e.plan, j=j)[0] or 0),3) for j in range(1,n+1)]
def zeige(name, ein, vg):
    b=G.rechne_grob(ein,vg); s=G.rechne_grob(ein,vg,stress=True)
    bm=b.bemessung.bank
    print(name, "L=",b.darlehen, "bindet",bm["bindend"], "A",round(bm["a"]),"B",round(bm["b"]),"C",round(bm["c"]))
    print("  DSCR basis", dscr_reihe(b)); print("  DSCR stress", dscr_reihe(s))
    print("  EK", b.eigenkapital_investitionsphase, "Nachschuss", b.nachschuss_spaeter, "Rendite", round(float(b.kennzahlen.r if hasattr(b.kennzahlen,'r') else 0),5) if False else "")
    return b,s
print("== RF-11 Basis"); zeige("RF11",A.ANKAUF,A.VORGABEN)
print("== Ankauf, Zins 3 %, Miete ohne Anpassung, Mietsteigerung 0,5 %")
zeige("lowrate", replace(A.ANKAUF, zins=D("0.03"), markt_miete=D("8.50")), replace(A.VORGABEN, mietsteigerung=D("0.005")))
print("== gebundener Bestand mit uebernommenem Darlehen (RF-11 Variante)")
eg=replace(A.ANKAUF, gebunden_anteil=D("0.4"), bindung_jahre=6, gebundene_miete=D("6.80"), geb_steigerung=D("0.0615"),
  uebernommen=dict(restschuld=D(500000), zins=D("0.005"), tilgungssatz=D("0.02"), bindung_jahre=8, anschluss_zins=D("0.03")))
zeige("geb", eg, A.VORGABEN)
print("== Ankauf ueber Marktmiete: Ist 10,00, Markt 9,20")
zeige("over", replace(A.ANKAUF, ist_miete=D("10.00")), A.VORGABEN)
zeige("markt", replace(A.ANKAUF, ist_miete=D("9.20")), A.VORGABEN)
print("== RF-12 gefoerdert 20 J")
gef=replace(A.NEUBAU, foerderung=A.FOERDERUNG_B, haltedauer=20)
b,s=zeige("gef", gef, A.VORGABEN_NEUBAU)
print("  KD_ue", b.bemessung.kd_uebrige, "RE_VJ", b.bemessung.reinertrag_vj)
vg2=replace(A.VORGABEN_NEUBAU, nur_eigenes_darlehen=True)
b2,s2=zeige("gef andere Lesart", gef, vg2)
