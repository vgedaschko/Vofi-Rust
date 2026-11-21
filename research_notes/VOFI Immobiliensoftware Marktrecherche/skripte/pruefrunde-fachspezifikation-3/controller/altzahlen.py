"""Pruefrunde 3, Controller: Zahlen im Text, die nach der Durchsicht keine Lesart mehr haben (Lesart 1 und 2 von
MA-026), mit dem Referenzrechner nachgerechnet, soweit das ueber die verbliebenen Stellgroessen geht.
Lesart 2 (Vertragskonditionen) ist nach V-06 deckungsgleich mit H-25 = 0 (i_kalk = max(Vertragszins; 0))."""
import sys, io, contextlib
from dataclasses import replace
from decimal import Decimal as D
R = "/home/user/vofi-rust/research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner"
sys.path.insert(0, R)
with contextlib.redirect_stdout(io.StringIO()):
    from rf_grob import VG, KAT, KATN, GEBUNDEN, GEFOERDERT, MIT_KFW
    import grobkalkulation as g
def bank(ein, vg, kat):
    return g.rechne_grob(ein, vg, kat).darlehen
print("R-5.12 Z. 527: gebundener Bestand, H-25 fest 4 %:", bank(GEBUNDEN, replace(VG, kalk_zins=D("0.04")), KAT), "(Text 826.660,00)")
print("R-5.12 Z. 527: gebundener Bestand, Lesart 2 ~ H-25 = 0:", bank(GEBUNDEN, replace(VG, kalk_zins=D("0")), KAT), "(Text 1.034.436,66)")
print("R-5.19 Z. 588: KfW, Lesart 2 ~ H-25 = 0: Bankdarlehen", bank(MIT_KFW, replace(VG, kalk_zins=D("0")), KATN), "(Text 2.425.000,00)")
tp = g.tragbarer_preis(MIT_KFW, replace(VG, kalk_zins=D("0")), KATN)
print("   tragbarer Grundstueckspreis:", tp["preis"], "(Text 1.283.299)")
tp0 = g.tragbarer_preis(replace(MIT_KFW, kfw_betrag=D(0)), replace(VG, kalk_zins=D("0")), KATN)
print("   ohne KfW, H-25 = 0:", tp0["preis"], "(Text 876.926)")
tp4 = g.tragbarer_preis(MIT_KFW, replace(VG, ma026_fremde_kalkulatorisch=True), KATN)
print("   Lesart 4:", tp4["preis"], "(Text 920.435)")
print("\nV-06: 'fester Satz in Hoehe des Vertragszinses' = Lesart 2?")
for name, ein, kat in (("Ankauf", None, KAT), ("gebundener Bestand", GEBUNDEN, KAT), ("Neubau mit KfW", MIT_KFW, KATN)):
    if ein is None:
        from rf_grob import A
        ein = A.ANKAUF
    for h25 in ("0", "0.04"):
        e = g.rechne_grob(ein, replace(VG, kalk_zins=D(h25)), kat)
        tp = g.tragbarer_preis(ein, replace(VG, kalk_zins=D(h25)), kat)
        print(f"   {name:<20} H-25 = {h25:<5}: Bankdarlehen {e.darlehen:>14}  tragbarer Preis {tp['preis']}")
