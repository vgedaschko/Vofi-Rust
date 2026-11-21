"""GF3-A, GF3-B: Mittelabruf in Teilraten (R-11.3) und Tilgung des Foerderdarlehens (R-5.11) an den Raendern."""
from h import *
import sys


def foerder(e):
    z = e.plan.zeilen
    tr = {t.name: t for t in e.plan.e.tranchen}
    fd = tr.get("Foerderdarlehen")
    neg = [u for u in range(len(z)) if any(z[u]["tranchen"][n]["rest"] < 0 for n in tr)]
    kk_max = max(zz["kk"] for zz in z)
    erste_t = next((u for u in range(len(z)) if z[u]["tranchen"]["Foerderdarlehen"]["tilgung"] > 0), None) if fd else None
    ausz = sorted(fd.auszahlung.items()) if fd else []
    rate = fd.rate if fd else None
    return (f"FD TB {fd.tilgungsbeginn if fd else '-'} Laufzeit {fd.laufzeit if fd else '-'} Rate {rate} erste Tilgung {erste_t} "
            f"Abrufe {[(m, de(b)) for m, b in ausz]} | Zwischenfin. max {de(e.zwischenfinanzierung)} KK max {de(kk_max)} "
            f"| neg. Restschuld {neg[:3]} | Bauende {e.bauzeit}")


w = sys.argv[1:] or ["A", "B"]
if "A" in w:
    print("== GF3-A Teilraten: Bauzeit, Vorlauf, Linie")
    for bz in (1, 2, 3, 7, 13, 17, 18, 59, 60):
        for st in (False, True):
            print(f"  Bauzeit {bz} Stress {st}:", zeig(replace(GEF, bauzeit_monate=bz), kat=KATN, stress=st, extra=foerder))
    print("  Vorlauf 12, Bauzeit 18:", zeig(replace(GEF, vorlauf_monate=12), kat=KATN, extra=foerder))
    print("  Vorlauf 60, Bauzeit 60:", zeig(replace(GEF, vorlauf_monate=60, bauzeit_monate=60), kat=KATN, extra=foerder))
    for lin in (None, D(500000), D(5000000)):
        print(f"  Linie {lin}:", zeig(GEF, replace(VG, kk_linie=lin), KATN, extra=foerder))
    print("  vorvermietet (Anlauf 0):", zeig(replace(GEF, vorvermietet=True, begruendungen={"vorvermietet": "Test"}), kat=KATN, extra=foerder))
    print("  H-37 Rohbau = Innenputz = 1:", zeig(GEF, replace(VG, bauabschnitt_rohbau=D(1), bauabschnitt_innenputz=D(1)), KATN, extra=foerder))
    print("  H-37 Rohbau 0,01:", zeig(GEF, replace(VG, bauabschnitt_rohbau=D("0.01"), bauabschnitt_innenputz=D("0.01")), KATN, extra=foerder))
    print("  nur Darlehen (Zuschussquote 0):", zeig(replace(GEF, foerderung=replace(A.FOERDERUNG_B, zuschussquote=NULL)), kat=KATN, extra=foerder))
    print("  nur Zuschuss (Darlehensquote 0):", zeig(replace(GEF, foerderung=replace(A.FOERDERUNG_B, darlehensquote=NULL)), kat=KATN, extra=foerder))
    print("  Teilraten 100/0/0/0:", zeig(replace(GEF, foerderung=replace(A.FOERDERUNG_B, teilraten=(D(1), NULL, NULL, NULL))), kat=KATN, extra=foerder))
    print("  Teilraten 0/0/0/100:", zeig(replace(GEF, foerderung=replace(A.FOERDERUNG_B, teilraten=(NULL, NULL, NULL, D(1)))), kat=KATN, extra=foerder))
    print("  mit KfW 100.000:", zeig(replace(GEF, kfw_betrag=D(100000), kfw_laufzeit=35, kfw_tilgungsfrei=1), kat=KATN, extra=foerder))
    print("  Miete 12 (Bankdarlehen > 0):", zeig(replace(GEF, foerderung=replace(A.FOERDERUNG_B, eingangsmiete=D(12))), kat=KATN, extra=foerder))
if "B" in w:
    print("== GF3-B Tilgungsbeginn des Foerderdarlehens an der Frist (24 Monate) und Haltedauer 42")
    for bz in (19, 20, 21, 22):
        print(f"  Bauzeit {bz}:", zeig(replace(GEF, bauzeit_monate=bz), kat=KATN, extra=foerder))
    for f in (0, 1, 24, 600):
        print(f"  Frist {f} Monate:", zeig(replace(GEF, foerderung=replace(A.FOERDERUNG_B, tilgungsfrist_monate=f)), kat=KATN, extra=foerder))
    for n in (37, 42, 43):
        print(f"  Haltedauer {n}:", zeig(replace(GEF, haltedauer=n), kat=KATN, extra=foerder))
    print("  Haltedauer 42, Bauzeit 60, Vorlauf 60:", zeig(replace(GEF, haltedauer=42, bauzeit_monate=60, vorlauf_monate=60), kat=KATN, extra=foerder))
    print("  Rueckzahlungsfrist 3 Jahre:", zeig(replace(GEF, foerderung=replace(A.FOERDERUNG_B, tilgung_jahre=3)), kat=KATN, extra=foerder))
    print("  Rueckzahlungsfrist 1 Jahr, Bauzeit 18:", zeig(replace(GEF, foerderung=replace(A.FOERDERUNG_B, tilgung_jahre=1)), kat=KATN, extra=foerder))
    print("  Rueckzahlungsfrist 0:", zeig(replace(GEF, foerderung=replace(A.FOERDERUNG_B, tilgung_jahre=0)), kat=KATN, extra=foerder))
