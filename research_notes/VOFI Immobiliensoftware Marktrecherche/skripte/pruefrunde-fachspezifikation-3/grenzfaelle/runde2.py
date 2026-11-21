"""Pruefrunde 3, Grenzfaelle: die Faelle der Befunde aus Runde 2 erneut gegen den eingefrorenen Stand."""
from h import *
import sys
from zahlen import FEHLER
w = sys.argv[1:] or ["B1", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]

if "B1" in w:
    print("== Befund 1 (NG-22, NG-14): Rate bei Tilgungsbeginn nach Bindungsende")
    for st in (False, True):
        s, e = kalk(replace(NB, bauzeit_monate=24, zinsbindung_jahre=2), VG, KATN, stress=st)
        bz = e.bauzeit; t = e.plan.zeilen[bz + 1]["tranchen"]["Bankdarlehen"]
        print(f"  Bauzeit 24, Bindung 2, Stress {st}: Monat {bz+1} Satz {t['satz']} Zins {de(t['zins'])} Tilgung {de(t['tilgung'])}"
              f" Deckung VJ {r4(e.dscr_vj)} gesperrt {e.gesperrt}")
    s, e = kalk(replace(NB, zinsbindung_jahre=1), VG, KATN)
    t = e.plan.zeilen[19]["tranchen"]["Bankdarlehen"]
    print(f"  Bindung 1: M19 Rate {de(t['zins']+t['tilgung'])} (Soll 23.375,00) Tilgung {de(t['tilgung'])}")
    kat = replace(KATN, kfw=replace(A.KFW, zinsbindung_jahre=3))
    s, e = kalk(replace(KFWF, kfw_tilgungsfrei=5, haltedauer=20), VG, kat)
    if s == "ergebnis":
        z = e.plan.zeilen; b = 7 + 60 + 1
        t = z[b]["tranchen"]["KfW-Darlehen"]
        print(f"  KfW 5 tilgungsfreie Jahre, Bindung 3 J.: M{b} Satz {t['satz']} Zins {de(t['zins'])} Tilgung {de(t['tilgung'])}; Rest M240 {de(z[239]['tranchen']['KfW-Darlehen']['rest'])}; gesperrt {e.gesperrt}")
    else:
        print("  KfW:", s, e)

if "B3" in w:
    print("== Befund 3 (NG-18): Kennzeichen Foerderdarlehen beim uebernommenen Darlehen")
    for fd in (True, False, None):
        ue = dict(restschuld=D(500000), nennbetrag=D(600000), zins=D("0.005"), tilgungssatz=D("0.02"), bindung_jahre=20, anschluss_zins=D("0.03"))
        if fd is not None:
            ue["foerderdarlehen"] = fd
        print(f"  Kennzeichen {fd}:", zeig(replace(ANK, uebernommen=ue, haltedauer=5), extra=lambda e: f"VFE {de(e.plan.zeilen[60]['vfe'])} KD_Ue {de(e.bemessung.kd_uebrige)}"))

if "B4" in w:
    print("== Befund 4 (NG-33): M-24 in Suchen")
    gef = replace(GEF, foerderung=replace(A.FOERDERUNG_B, zins_danach=None))
    print("  kalkuliere:", zeig(gef, kat=KATN))
    print("  tragbar:", tp(gef, kat=KATN))
    print("  Haltedauertabelle 37-38:", hdt(gef, VG, KATN, 37, 38))
    print("  Zielwertsuche Faktor:", zws(gef, VG, KATN, "verkaufsfaktor", D(10), D(30), D("0.01"), raster=5))

if "B5" in w:
    print("== Befund 5 (NG-31): Katalog")
    print("  Bayern:", zeig(replace(ANK, land="Bayern", gemeinde="Muenchen")))
    print("  Kappung fehlt:", zeig(ANK, kat=replace(KAT, kappung=None)))
    print("  Hebesatz fehlt:", zeig(replace(ANK, steuer=replace(ANK.steuer, hebesatz=None))))
    print("  Hebesatz fehlt, Preissuche:", tp(replace(ANK, steuer=replace(ANK.steuer, hebesatz=None))))

if "B6" in w:
    print("== Befund 6 (NG-09, NG-34, NG-35): Eingabepruefung")
    print("  E-58 = 0:", zeig(replace(ANK, gebunden_anteil=D("0.4"), bindung_jahre=5, gebundene_miete=NULL)))
    print("  E-58 = -1:", zeig(replace(ANK, gebunden_anteil=D(1), bindung_jahre=5, gebundene_miete=D(-1))))
    for name, vg in (("H-18 -1 %", replace(VG, vfe_satz=D("-0.01"))), ("H-11 -100.000", replace(VG, kk_linie=D(-100000))),
                     ("H-09 -50 %", replace(VG, a_lang=D("-0.5"))), ("H-25 -10 %", replace(VG, kalk_zins=D("-0.1"))),
                     ("H-29 -500", replace(VG, co2_preis=D(-500))), ("H-17 -2000", replace(VG, verwaltung_je_einheit=D(-2000))),
                     ("H-06 Leerstand -50 Pp.", replace(VG, stress=replace(VG.stress, leerstand_pp=D("-0.5")))),
                     ("H-21 Suchraster 0", replace(VG, suchraster=0)), ("H-17 Staffel leer", replace(VG, instandhaltung_staffel=[]))):
        print(f"  {name}:", zeig(replace(ANK, haltedauer=5), vg, stress=name.startswith("H-06")))
    print("  H-21 Suchraster 0, Preissuche:", tp(ANK, replace(VG, suchraster=0)))
    ue = dict(restschuld=D(500000), zins=D("0.02"), tilgungssatz=D("0.02"), bindung_jahre=3, anschluss_zins=D("-0.05"), beitrag_satz=D("-0.01"))
    print("  E-59 Anschluss -5 %:", zeig(replace(ANK, uebernommen=ue)))
    print("  E-59 Bindung 0:", zeig(replace(ANK, uebernommen=dict(restschuld=D(500000), zins=D("0.02"), tilgungssatz=D("0.02"), bindung_jahre=0))))

if "B7" in w:
    print("== Befund 7 (NG-36): Fehlerbilder Bemessung, Rate")
    for f in ("mindestdeckung_vergessen", "rate_ohne_anschluss"):
        pass
    print("  verfuegbare Fehlerbilder:", sorted(set(open(os.path.join(RR, "rf_runde2.py")).read().split("FEHLER.add(\"")[1:])) and
          sorted({s.split('"')[0] for s in open(os.path.join(RR, "rf_runde2.py")).read().split('FEHLER.add("')[1:]}))
    orig = G.bankdarlehen
    def falsch(*a, **k):
        a = list(a); a[3] = D(1)
        return orig(*a, **k)
    G.bankdarlehen = falsch
    print("  Mindestdeckung vergessen (von aussen):", zeig(ANK))
    G.bankdarlehen = orig
    FEHLER.add("rate_ohne_anschluss")
    print("  Rate ohne Anschluss, Neubau Bindung 1:", zeig(replace(NB, zinsbindung_jahre=1), kat=KATN))
    FEHLER.discard("rate_ohne_anschluss")

if "B8" in w:
    print("== Befund 8 (NG-25, NG-37): ohne Eigenkapital")
    e = replace(ANK, enk_satz=NULL, verkaufsfaktor=D(5))
    vg = replace(VG, beleihungsquote=D(1), mindestdeckung=D(1), kalk_zins=D("0.04"), zielrendite=D("0.02"))
    print("  E-60 leer:", tp(e, vg))
    print("  E-60 = 0:", tp(replace(e, verfuegbares_ek=NULL), vg))
    print("  Zielwertsuche Faktor:", zws(e, vg, KAT, "verkaufsfaktor", D(3), D(30), D("0.01"), raster=10))

if "B9" in w:
    print("== Befund 9 (NG-39): Rundungsmodus keine")
    print("  Neubau keine:", zeig(NB, kat=KATN, rundung="keine"))
    print("  Ankauf Jahresmodus keine:", zeig(ANK, rundung="keine", p=1))

if "B10" in w:
    print("== Befund 10 (NG-16, NG-24)")
    for n in (10, 11):
        for p in (12, 1):
            s, e = kalk(replace(ANK, zinsbindung_jahre=15, haltedauer=n), p=p)
            print(f"  Bindung 15 n={n} p={p}: VFE {de(e.plan.zeilen[n*p]['vfe'])}")
    g = kalk(replace(ANK, kaufpreis=D(2000000)))[1]
    print("  E-60 = Bedarf bei 2,0 Mio.:", tp(replace(ANK, verfuegbares_ek=g.eigenkapitalbedarf)))
