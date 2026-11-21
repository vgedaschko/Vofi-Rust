"""GF3-C KfW-Anlaufjahre gegen Haltedauer; GF3-D Stress-Neubemessung bis null und Stresshoehen am Rand."""
from h import *
import sys


def kfw(e):
    z = e.plan.zeilen; N = e.plan.e.raster.N
    tr = {t.name: t for t in e.plan.e.tranchen}["KfW-Darlehen"]
    til = sum(zz["tranchen"]["KfW-Darlehen"]["tilgung"] for zz in z)
    return (f"KfW TB {tr.tilgungsbeginn} N {N} Tilgung {de(til)} Abloesung {de(z[N]['tranchen']['KfW-Darlehen']['abloesung'])} "
            f"VFE {de(z[N]['vfe'])} KD_Ue {de(e.bemessung.kd_uebrige)}")


w = sys.argv[1:] or ["C", "D"]
if "C" in w:
    print("== GF3-C KfW-Anlaufjahre und Haltedauer")
    for lz, tf, n in ((35, 5, 3), (35, 5, 5), (35, 5, 6), (10, 2, 3), (10, 1, 15), (10, 2, 15), (25, 3, 42), (35, 5, 42)):
        print(f"  {lz} J., {tf} tilgungsfrei, n {n}:", zeig(replace(KFWF, kfw_laufzeit=lz, kfw_tilgungsfrei=tf, haltedauer=n), kat=KATN, extra=kfw))
    print("  35/6 (nicht im Katalog):", zeig(replace(KFWF, kfw_tilgungsfrei=6), kat=KATN))
    print("  35/0 (nicht im Katalog):", zeig(replace(KFWF, kfw_tilgungsfrei=0), kat=KATN))
    print("  KfW-Zins 0:", zeig(replace(KFWF, kfw_zins=NULL), kat=KATN, extra=kfw))
    print("  KfW, Stress:", zeig(replace(KFWF, kfw_tilgungsfrei=5, haltedauer=5), kat=KATN, stress=True, extra=kfw))
    print("  KfW Vorlauf 60, Bauzeit 60, n 42:", zeig(replace(KFWF, vorlauf_monate=60, bauzeit_monate=60, haltedauer=42, kfw_tilgungsfrei=5), kat=KATN, extra=kfw))
if "D" in w:
    print("== GF3-D Stress-Neubemessung")
    # uebernommenes Darlehen mit voreingestelltem Anschlusszins (folgt dem Bankzins) und kurzer Bindung: KD_Ue steigt im Stress
    for rs in (1300000, 1400000, 1450000, 1500000):
        ue = dict(restschuld=D(rs), zins=D("0.03"), tilgungssatz=D("0.02"), bindung_jahre=2)
        for st in (False, True):
            print(f"  uebernommen {rs}, Stress {st}:", zeig(replace(ANK, uebernommen=ue), stress=st,
                  extra=lambda e: f"L_Basis {de(e.darlehen_basis)} B {e.bemessung.bank.get('b')} KD_Ue {de(e.bemessung.kd_uebrige)} EK-Soll {de(e.ek_soll)}"))
    # Zusage-Stress gross
    for zp in ("0.05", "0.20"):
        vg = replace(VG, stress=replace(VG.stress, zusage_pp=D(zp)))
        print(f"  Zinsanstieg bis Zusage {zp}:", zeig(ANK, vg, stress=True))
    vg = replace(VG, stress=replace(VG.stress, leerstand_pp=D("1.5")))
    print("  Stress Leerstand +150 Pp.:", zeig(ANK, vg, stress=True, extra=lambda e: f"Miete M1 {de(e.plan.zeilen[1]['miete'])} VK {de(e.verkauf.preis_brutto)}"))
    vg = replace(VG, stress=replace(VG.stress, verkaufsfaktor_rel=D(1)))
    print("  Stress Faktor -100 %:", zeig(ANK, vg, stress=True, extra=lambda e: f"VK {de(e.verkauf.preis_brutto)}"))
    print("  Stress Faktor -100 %, Preissuche:", tp(ANK, vg, stress=True))
    vg = replace(VG, stress=replace(VG.stress, mietsteigerung_pp=D("0.3")))
    print("  Stress Mietsteigerung -30 Pp.:", zeig(ANK, vg, stress=True, extra=lambda e: f"VK {de(e.verkauf.preis_brutto)}"))
    vg = replace(VG, stress=replace(VG.stress, bauzeit_monate=200))
    print("  Stress Bauzeit +200:", zeig(NB, vg, KATN, stress=True))
    print("  Gefoerdert, Stress, Preissuche (Ziel 3 %):", tp(GEF, replace(VG, zielrendite_gefoerdert=D("0.03")), KATN, stress=True))
