"""GF3-G2 Begruendungspflicht (R-3.2 Nr. 5) in den Suchen: Abweichung ohne Begruendung, die die Rendite hebt."""
from h import *
e = replace(ANK, abweichungen={"mietsteigerung": (D("0.025"), "")})
print("  Einzellauf:", zeig(e))
print("  Stressfall:", zeig(e, stress=True))
print("  Preissuche:", tp(e))
print("  Zielwertsuche Faktor:", zws(e, VG, KAT, "verkaufsfaktor", D(8), D(40), D("0.01"), raster=8))
tab = hdt(e, VG, KAT, 10, 12)
print("  Haltedauertabelle 10-12:", [(n, r if isinstance(r, str) else proz(r)) for n, _, _, r in tab])
tab0 = hdt(ANK, VG, KAT, 10, 12)
print("  ohne Abweichung:          ", [(n, r if isinstance(r, str) else proz(r)) for n, _, _, r in tab0])
try:
    v = G.vergleiche(rechne_grob(ANK, VG, KAT), rechne_grob(e, VG, KAT))
    print("  Vergleich: gerechnet")
except Exception as x:
    print("  Vergleich:", wo(x))
