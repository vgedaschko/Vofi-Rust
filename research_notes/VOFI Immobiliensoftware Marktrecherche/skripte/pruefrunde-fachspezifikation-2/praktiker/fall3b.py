"""Fall 3 Ergaenzung: P-14-Sperre nachstellen; KfW mit vertraglichem Kapitaldienst neben kalkulatorischem Bankdarlehen."""
import sys
sys.argv = [sys.argv[0], "x"]
exec(open("/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs2-praktiker/faelle_r2.py").read())
fk = replace(F3, kostenkennwert=D(2400), kfw_betrag=D(3600000))
vg0 = replace(VG, baupreissteigerung=D(0), bereit_satz=D(0), anlaufleerstand=0, ma026_vertragszins=True)
kat0 = replace(KATN, bewirtschaftung_mindest=D(0))
t = tragbarer_preis(fk, vg0, kat0)
print("Sperre:", t["meldung"], t.get("text"), t.get("angaben"), "Renditegrenze", t.get("renditegrenze"))
p = (t.get("angaben") or {}).get("preis") or t.get("renditegrenze")
if p:
    for q in range(p - 3, p + 4):
        e = rechne_grob(fk, vg0, kat0, preis=q)
        kz = e.kennzahlen
        print(q, "EUe", kz and round(kz.get("endwertueberschuss", kz.get("eu", 0)), 2) if kz else None,
              "r", kz and pz(kz["rendite"]), "gesperrt", e.gesperrt, "Bank", e.darlehen, e.bemessung.bank["bindend"])
# Teilmengen, um die Ursache einzugrenzen
for name, vg1, kat1 in (("nur Lesart 2 + H-14 0", replace(VG, baupreissteigerung=D(0), ma026_vertragszins=True), KATN),
                        ("Lesart 2 + KAT-14 0", replace(VG, ma026_vertragszins=True), kat0),
                        ("ohne Lesart 2, Rest zurueck", replace(VG, baupreissteigerung=D(0), bereit_satz=D(0), anlaufleerstand=0), kat0)):
    tp(name, fk, vg1, kat1)

# KfW mit vertraglichem Kapitaldienst (wie die Ausnahme fuer Foerderdarlehen in R-5.12), Bankdarlehen kalkulatorisch
orig = G.kapitaldienst_kalkulatorisch
def kd_hybrid(schuld, i, t_, p, rd):
    if schuld == D(3600000):
        return orig(schuld, A.KFW.zins, max(A.KFW.tilgungssatz, VG.mindesttilgung), p, rd)
    return orig(schuld, i, t_, p, rd)
G.kapitaldienst_kalkulatorisch = kd_hybrid
zeige("Hybrid: KfW vertraglich, Bank kalk., Grst 2,0 Mio", rechne_grob(fk, VG, KATN))
tp("Hybrid mit KfW", fk, VG, KATN)
tp("Hybrid mit KfW, Stress", fk, VG, KATN, stress=True)
G.kapitaldienst_kalkulatorisch = orig
