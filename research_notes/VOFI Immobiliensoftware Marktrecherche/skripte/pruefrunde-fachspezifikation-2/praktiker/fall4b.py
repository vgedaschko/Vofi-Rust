"""Fall 4 Ergaenzung: Kostenkennwert wie in Runde 1 gemeint (3.300 gesamt = 2.640 KG 300/400), MA-031, KfW als Restfinanzierung."""
import sys
sys.argv = [sys.argv[0], "x"]
exec(open("/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs2-praktiker/faelle_r2.py").read())
F4a = replace(F4, kostenkennwert=D(2640))
print("FALL 4a KKW 2.640 (KG 300/400) = 3.300 gesamt wie Runde 1")
for n in (20, 36, 38):
    zeige(f"Haltedauer {n}", rechne_grob(replace(F4a, haltedauer=n), VG, KATN))
e = rechne_grob(F4a, VG, KATN)
print("   R-11.15:", {k: (round(v, 4) if v is not None else None) for k, v in (e.ohne_bankdarlehen or {}).items()})
print("   Nachschuss je Planjahr 1..14:", [eur(x) for x in e.nachschuss_je_jahr[1:15]])
print("   Steuer je Planjahr 1..4:", [eur(e.plan.jahressumme("steuer", j)) for j in range(1, 5)])
for les in ("verteilt", "minderung"):
    zeige(f"MA-031 {les}", rechne_grob(F4a, replace(VG, ma031_zuschuss=les), KATN))
tp("4a Ziel 5 %", F4a, VG, KATN)
tp("4a Ziel 3 %", F4a, replace(VG, zielrendite=D("0.03")), KATN)
tp("4a Ziel 3 %, MA-031 minderung", F4a, replace(VG, zielrendite=D("0.03"), ma031_zuschuss="minderung"), KATN)
c = e.bemessung.bank["c"]
kf = (c / 100000).quantize(D(1)) * 100000 - 100000
print("   KfW in Hoehe der Restfinanzierung:", eur(kf))
zeige("4a mit KfW = Restfinanzierung", rechne_grob(replace(F4a, kfw_betrag=kf), VG, KATN))
tp("4a mit KfW, Ziel 3 %", replace(F4a, kfw_betrag=kf), replace(VG, zielrendite=D("0.03")), KATN)
