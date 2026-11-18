"""Pruefrunde 2, Rolle Bank: eigene Faelle mit den unveraenderten Modulen des Referenzrechners."""
import sys
from dataclasses import replace
from decimal import Decimal as D
sys.path.insert(0, sys.argv[1])
import annahmen as A
from grobkalkulation import rechne_grob, kalkuliere, bemesse, tragbarer_preis
import rf_grob as G
from kennzahlen import schuldendienstdeckung

VG, KAT, KATN = A.VORGABEN, A.KATALOG, A.KATALOG_NEUBAU


def deck(e):
    r = e.plan.e.raster
    return [(j, round(float(schuldendienstdeckung(e.plan, j)[0] or 0), 4)) for j in range(1, r.n + 1)]


def kurz(t, e):
    bm = e.bemessung
    print(f"--- {t}")
    print("  RE_n", bm.ertrag_nachhaltig, "RE_vj", bm.reinertrag_vj, "kd_ue", bm.kd_uebrige, dict(bm.kd_uebrige_je) if hasattr(bm, 'kd_uebrige_je') else "")
    b = bm.bank
    print("  A", b["a"], "B", b["b"], "C", b["c"], "L", b["darlehen"], b["bindend"], "ik", bm.zins_kalk, "tk", bm.tilgung_kalk)
    if e.kennzahlen:
        print("  EWD", e.kennzahlen.get("ewd") if isinstance(e.kennzahlen, dict) else None)
    print("  DSCR vj", e.dscr_vj, "min", e.deckung_min, e.deckung_min_jahr, "nach Bindung", e.deckung_nach_bindung)
    print("  Meldungen", sorted(m["kennung"] for m in e.meldungen))
    print("  Deckung je Jahr", deck(e))


# 1 Ankaufsfall RF-11 Basis und Stress
b = rechne_grob(A.ANKAUF, VG, KAT)
kurz("RF-11 Basis", b)
print("  kd je Darlehen", b.kd_je_darlehen)
s = rechne_grob(A.ANKAUF, VG, KAT, stress=True)
kurz("RF-11 Stress", s)

# 2 Zinsanstieg bis zur Zusage: Bank bemisst mit dem gestiegenen Zins (eigene Lesart)
ein_z = replace(A.ANKAUF, zins=A.ANKAUF.zins + VG.stress.zusage_pp)
bz = bemesse(ein_z, VG, KAT, b.plan.e.raster, __import__('zahlen').Rundung('cent'))
print("--- Zusage +0,5: Bankdarlehen bei Bemessung mit 4,5 %:", bz.bank["darlehen"], "statt", b.darlehen,
      "Differenz", b.darlehen - bz.bank["darlehen"])

# 3 gebundener Bestand
g = rechne_grob(G.GEBUNDEN, VG, KAT)
kurz("gebunden Basis", g)
print("  kd", g.bemessung.kd_je_darlehen)
gs = rechne_grob(G.GEBUNDEN, VG, KAT, stress=True)
kurz("gebunden Stress", gs)
# Default-Kennzeichen Foerderdarlehen weggelassen (Code-Voreinstellung)
ue = dict(G.GEBUNDEN.uebernommen); ue.pop("foerderdarlehen")
g0 = rechne_grob(replace(G.GEBUNDEN, uebernommen=ue), VG, KAT)
print("--- gebunden ohne Angabe Foerderkennzeichen: tranche foerder =",
      [t.foerder for t in g0.plan.e.tranchen if t.name.startswith("Ueber")], "L", g0.darlehen)
# Uebernommenes mit Bindung ueber der Bank, Foerder ja -> vertraglicher KD
ue2 = dict(G.GEBUNDEN.uebernommen, bindung_jahre=12)
g2 = rechne_grob(replace(G.GEBUNDEN, uebernommen=ue2), VG, KAT)
print("--- gebunden, Bindung uebernommen 12 J, Foerder ja: kd", g2.bemessung.kd_je_darlehen, "L", g2.darlehen)
ue3 = dict(ue2, foerderdarlehen=False)
g3 = rechne_grob(replace(G.GEBUNDEN, uebernommen=ue3), VG, KAT)
print("--- dasselbe Foerder nein: kd", g3.bemessung.kd_je_darlehen, "L", g3.darlehen)

# 4 Neubau frei, mit KfW, gefoerdert
n = rechne_grob(A.NEUBAU, VG, KATN)
kurz("RF-12 frei", n)
nk = rechne_grob(G.MIT_KFW, VG, KATN)
kurz("RF-12 KfW", nk)
print("  kd je Darlehen", nk.kd_je_darlehen)
nks = rechne_grob(G.MIT_KFW, VG, KATN, stress=True)
kurz("RF-12 KfW Stress", nks)
gf = rechne_grob(G.GEFOERDERT, VG, KATN)
kurz("RF-12 gefoerdert", gf)
print("  ohne Bankdarlehen", gf.ohne_bankdarlehen, "Reserve R-10.21", gf.kapitaldienstreserve)
gfs = rechne_grob(G.GEFOERDERT, VG, KATN, stress=True)
kurz("RF-12 gefoerdert Stress", gfs)

# 5 RF-19-Fall mit den drei Anschlussregeln, Stress
f2 = replace(A.ANKAUF, zins=D("0.03"), ist_miete=D("8.50"), vergleichsmiete=D("8.50"), stau_betrag=D(0),
             )
for regel in ("tilgungssatz", "rate", "restlaufzeit"):
    vg = replace(VG, anschluss_regel=regel)
    for lesart in (False, True):
        vg2 = replace(vg, ma026_vertragszins=lesart)
        for st in (False, True):
            try:
                e = rechne_grob(replace(f2, steigerung_override=None) if False else f2,
                                replace(vg2, mietsteigerung=D("0.005")), KAT, stress=st)
                print(f"RF19 regel={regel} vertrag={lesart} stress={st}: L {e.darlehen} vj {e.dscr_vj:.4f} min {e.deckung_min:.4f} J{e.deckung_min_jahr} "
                      f"nachB {e.deckung_nach_bindung} M {sorted(m['kennung'] for m in e.meldungen)}")
            except Exception as ex:
                print("Fehler", regel, lesart, st, ex)
