"""GF3-I Zielwertsuche an den Raendern; GF3-J Haltedauer an der Obergrenze (42 Jahre)."""
from h import *
import sys, time
w = sys.argv[1:] or ["I", "J"]
if "I" in w:
    print("== GF3-I Zielwertsuche")
    t0 = time.time()
    print("  Zins 0 bis 20 %:", zws(ANK, VG, KAT, "zins", NULL, D("0.20"), D("0.00001"), raster=20), f"({time.time()-t0:.0f} s)")
    print("  Zins -1 bis 10 %:", zws(ANK, VG, KAT, "zins", D("-0.01"), D("0.10"), D("0.00001"), raster=22))
    print("  Faktor 0 bis 40:", zws(ANK, VG, KAT, "verkaufsfaktor", NULL, D(40), D("0.01"), raster=20))
    print("  Kaufpreis 0 bis 5 Mio.:", zws(ANK, VG, KAT, "kaufpreis", NULL, D(5000000), D(1), raster=20))
    print("  Ist-Miete 0 bis 20 (alles vermietet):", zws(ANK, VG, KAT, "ist_miete", NULL, D(20), D("0.01"), raster=20))
    print("  Stau 0 bis 1 Mio., Jahr fehlt:", zws(ANK, VG, KAT, "stau_betrag", NULL, D(1000000), D(100), raster=10))
    print("  Kostenkennwert 500 bis 6000 (Neubau):", zws(NB, VG, KATN, "kostenkennwert", D(500), D(6000), D(1), raster=10))
    print("  Haltedauer (nicht zugelassen):", zws(ANK, VG, KAT, "haltedauer", 1, 42, 1))
if "J" in w:
    print("== GF3-J Haltedauer 42")
    for n in (40, 41, 42):
        print(f"  Ankauf n {n}:", zeig(replace(ANK, haltedauer=n)))
    print("  Ankauf n 42, Bindung 40:", zeig(replace(ANK, haltedauer=42, zinsbindung_jahre=40)))
    print("  Ankauf n 42, Jahresmodus:", zeig(replace(ANK, haltedauer=42), p=1))
    print("  Neubau n 42:", zeig(replace(NB, haltedauer=42), kat=KATN))
    print("  Neubau n 42, Stress:", zeig(replace(NB, haltedauer=42), kat=KATN, stress=True))
    t0 = time.time()
    print("  Ankauf n 42 Preissuche:", tp(replace(ANK, haltedauer=42)), f"({time.time()-t0:.0f} s)")
    t0 = time.time()
    tab = hdt(ANK, VG, KAT, 1, 42)
    print("  Haltedauertabelle 1-42:", "ABSTURZ" if isinstance(tab, str) else
          [(n, None if r is None or isinstance(r, str) else proz(r)) for n, _, _, r in tab][:3], "...",
          [(n, r if isinstance(r, str) else proz(r)) for n, _, _, r in tab][-2:], f"({time.time()-t0:.0f} s)")
    tab = hdt(NB, VG, KATN, 1, 42)
    print("  Haltedauertabelle Neubau 1-42:", "ABSTURZ" if isinstance(tab, str) else [(n, r if isinstance(r, str) or r is None else proz(r)) for n, _, _, r in tab][:4])
    print("  Haltedauertabelle 41-43:", hdt(ANK, VG, KAT, 41, 43))
