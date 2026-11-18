import sys
sys.argv = [sys.argv[0], "x"]
exec(open("/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs2-praktiker/faelle_r2.py").read())
for b in (8, 10):
    f = replace(F2, uebernommen=dict(F2.uebernommen, bindung_jahre=b, foerderdarlehen=True))
    e = rechne_grob(f, VG, KAT)
    print(f"  Fall 2 Foerderkennzeichen ja, Bindung {b} J.: KD Bemessung {eur(e.bemessung.kd_uebrige)}", end="")
    tp("", f, VG, KAT)
f = replace(F2, uebernommen=dict(F2.uebernommen, foerderdarlehen=True), haltedauer=5)
e = rechne_grob(f, VG, KAT); print("  Haltedauer 5, Kennzeichen ja: VFE", eur(e.plan.zeilen[e.plan.e.raster.N]["vfe"]))
e = rechne_grob(replace(F2, haltedauer=5), VG, KAT); print("  Haltedauer 5, Kennzeichen nicht gesetzt: VFE", eur(e.plan.zeilen[e.plan.e.raster.N]["vfe"]))
