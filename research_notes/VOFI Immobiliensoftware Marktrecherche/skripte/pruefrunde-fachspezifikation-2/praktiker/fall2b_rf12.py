"""Fall 2: Klippe bei der Zinsbindung des uebernommenen Foerderdarlehens (8 gegen 10 Jahre); RF-12 mit KfW hybrid."""
import sys
sys.argv = [sys.argv[0], "x"]
exec(open("/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs2-praktiker/faelle_r2.py").read())
for b in (8, 9, 10):
    f = replace(F2, uebernommen=dict(F2.uebernommen, bindung_jahre=b))
    e = rechne_grob(f, VG, KAT)
    print(f"  Fall 2 Bindung uebernommen {b} J.: KD Bemessung {eur(e.bemessung.kd_uebrige)}", end="")
    tp("", f, VG, KAT)
print("RF-12 Neubau Referenz")
tp("RF-12 ohne KfW", A.NEUBAU, VG, KATN)
tp("RF-12 KfW 3,0 Mio kalk.", replace(A.NEUBAU, kfw_betrag=D(3000000)), VG, KATN)
orig = G.kapitaldienst_kalkulatorisch
def kd_hybrid(schuld, i, t_, p, rd):
    if schuld == D(3000000):
        return orig(schuld, A.KFW.zins, max(A.KFW.tilgungssatz, VG.mindesttilgung), p, rd)
    return orig(schuld, i, t_, p, rd)
G.kapitaldienst_kalkulatorisch = kd_hybrid
tp("RF-12 KfW 3,0 Mio hybrid", replace(A.NEUBAU, kfw_betrag=D(3000000)), VG, KATN)
