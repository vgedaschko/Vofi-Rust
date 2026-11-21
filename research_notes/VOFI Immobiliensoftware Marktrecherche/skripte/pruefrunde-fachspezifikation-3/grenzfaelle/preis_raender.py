"""GF3-H Preissuche an den Raendern des Suchbereichs und bei nicht monotonem Verlauf."""
from h import *
import sys, time
w = sys.argv[1:] or ["H1", "H2", "H3"]
if "H1" in w:
    print("== GF3-H1 Verlauf des Endwertueberschusses ueber dem Grundstueckspreis im gefoerderten Neubau")
    for z in ("0.03", "0.04", "0.045"):
        vg = replace(VG, zielrendite_gefoerdert=D(z))
        out = []
        for P in (1, 100000, 300000, 500000, 700000, 900000, 925925, 925926, 1000000, 1200000, 1500000, 2000000):
            g = rechne_grob(GEF, vg, KATN, preis=P, mit_blatt=False)
            out.append(f"{P}: r {proz(g.kennzahlen['rendite'])} EUe {de(g.kennzahlen['endwertueberschuss'])}")
        print(f"  Ziel {z}:\n    " + "\n    ".join(out))
        t0 = time.time()
        print(f"  Preissuche Ziel {z}:", tp(GEF, vg, KATN), f"({time.time()-t0:.0f} s)")
if "H2" in w:
    print("== GF3-H2 Obergrenze an der Untergrenze")
    ue = dict(restschuld=D(2000000), zins=D("0.06"), tilgungssatz=D("0.02"), bindung_jahre=10)
    e = replace(ANK, uebernommen=ue, verkaufsfaktor=D(4))
    for f in ("13.0", "13.6", "13.7", "14", "100"):
        print(f"  uebernommen 2,0 Mio., H-21 Faktor {f}:", tp(e, replace(VG, such_obergrenze_faktor=D(f))))
    print("  H-21 Faktor 0,000001:", tp(ANK, replace(VG, such_obergrenze_faktor=D("0.000001"))))
    print("  H-21 Faktor 0,00001:", tp(ANK, replace(VG, such_obergrenze_faktor=D("0.00001"))))
    print("  H-21 Rasterzahl 1, Fenster 0:", tp(ANK, replace(VG, suchraster=1, nachsuchfenster=0)))
    print("  H-21 Rasterzahl 100000:", "uebersprungen (Laufzeit)")
if "H3" in w:
    print("== GF3-H3 Ziel genau an U, Ziel knapp ueber dem Maximum")
    print("  Ziel 1000 %:", tp(ANK, replace(VG, zielrendite=D(10))))
    print("  Ziel -99,99 %:", tp(ANK, replace(VG, zielrendite=D("-0.9999"))))
    print("  Ziel -100 % (unzulaessig):", tp(ANK, replace(VG, zielrendite=D("-1"))))
