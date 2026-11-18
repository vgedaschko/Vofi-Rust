from h import *
import grobkalkulation, darlehen
from grobkalkulation import haltedauer_tabelle
import sys
w = sys.argv[1]
if w == "T1":
    for st in (False, True):
        s, e = kalk(replace(NB, bauzeit_monate=24, zinsbindung_jahre=2), VG, KATN, stress=st)
        bz = e.bauzeit; t = e.plan.zeilen[bz + 1]["tranchen"]["Bankdarlehen"]
        print(f"stress {st}: Bauzeit {bz} Tilgungsbeginn {bz+1} Bindung 24: Satz {t['satz']} Zins {de(t['zins'])} Tilgung {de(t['tilgung'])} Rate {de(t['zins']+t['tilgung'])} | Deckung VJ {r4(e.dscr_vj)} min {r4(e.deckung_min)} | dEW {de(e.kennzahlen['endwertdifferenz'])}")
        L = e.darlehen
        print("   erwartet Rate", de((L*(D('0.055' if st else '0.05')+D('0.02'))/12).quantize(D('0.01'))), "Zinssatz", t['satz'])
if w == "T2":
    print(tp(ANK))
if w == "T3":
    for z in ("0.05", "0.08", "0.10"):
        e = replace(ANK, enk_satz=NULL, verfuegbares_ek=NULL)
        vg = replace(VG, beleihungsquote=D(1), mindestdeckung=D(1), ma026_vertragszins=True, zielrendite=D(z))
        print(z, tp(replace(e, verfuegbares_ek=None), vg)); print("   E-60=0:", tp(e, vg))
if w == "T5":
    gef = replace(NB, foerderung=replace(A.FOERDERUNG_B, zins_danach=None), haltedauer=38)
    print("kalkuliere:", zeig(gef, kat=KATN))
    print("tragbar:", tp(gef, kat=KATN))
    try: print("haltedauer_tabelle:", haltedauer_tabelle(gef, VG, KATN, 37, 38))
    except Exception as x: print("haltedauer_tabelle ABSTURZ", type(x).__name__, str(x)[:80])
    try:
        s = suche_eingabe(gef, VG, KATN, "grundstueckspreis", 100000, 2000000, 1, raster=5); print("suche:", s["status"])
    except Exception as x: print("suche_eingabe ABSTURZ", type(x).__name__, str(x)[:80])
if w == "T6":
    orig = grobkalkulation.bankdarlehen
    def falsch(*a, **k):
        a = list(a); a[3] = D(1)          # Mindestdeckung vergessen
        return orig(*a, **k)
    grobkalkulation.bankdarlehen = falsch
    print("Mindestdeckung vergessen:", zeig(ANK))
    grobkalkulation.bankdarlehen = orig
    print("richtig:                 ", zeig(ANK))
if w == "T7":
    for name, vg in (("H-18 Vorfaelligkeitssatz -1 %", replace(VG, vfe_satz=D("-0.01"))),
                     ("H-11 Linie -100.000", replace(VG, kk_linie=D(-100000))),
                     ("H-09 Anlagezins -50 %", replace(VG, a_lang=D("-0.5"))),
                     ("H-25 kalk. Zins -10 %", replace(VG, kalk_zins=D("-0.1"))),
                     ("H-29 CO2-Preis -500", replace(VG, co2_preis=D(-500))),
                     ("H-17 Verwaltung -2000 je Einheit", replace(VG, verwaltung_je_einheit=D(-2000))),
                     ("H-06 Stress Leerstand -50 Pp.", replace(VG, stress=replace(VG.stress, leerstand_pp=D("-0.5")))),
                     ("H-21 Suchraster 0", replace(VG, suchraster=0)),
                     ("H-17 Staffel leer", replace(VG, instandhaltung_staffel=[]))):
        print(name, "->", zeig(replace(ANK, haltedauer=5), vg, stress=name.startswith("H-06")))
    print("H-21 Suchraster 0, tragbar:", tp(ANK, replace(VG, suchraster=0)))
if w == "T8":
    ue = dict(restschuld=D(500000), zins=D("0.02"), tilgungssatz=D("0.02"), bindung_jahre=3, anschluss_zins=D("-0.05"), beitrag_satz=D("-0.01"))
    print("E-59 Anschlusszins -5 %, Beitrag -1 %:", zeig(replace(ANK, uebernommen=ue), extra=lambda e: f"Zins M40 {de(e.plan.zeilen[40]['tranchen']['Uebernommenes Darlehen']['zins'])} Beitrag {de(e.plan.zeilen[40]['tranchen']['Uebernommenes Darlehen']['beitrag'])}"))
    ue = dict(restschuld=D(500000), zins=D("0.02"), tilgungssatz=D("0.02"), bindung_jahre=0)
    print("E-59 Bindung 0:", zeig(replace(ANK, uebernommen=ue)))
