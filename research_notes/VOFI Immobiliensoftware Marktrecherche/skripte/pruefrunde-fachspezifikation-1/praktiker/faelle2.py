exec(open("faelle.py").read().split("# ---------------------------------------------------------------- Fall 1")[0])
F3 = replace(A.NEUBAU, wohnflaeche=D(2450), einheiten=36, bgf=D(3400), kostenkennwert=D(3300),
             grundstueckspreis=D(2000000), grundstuecksflaeche=D(3200), bauzeit_monate=22, enk_satz=D("0.065"),
             markt_miete=D("15.00"), verkaufsfaktor=D(25), haltedauer=15)
for p in (1, 1000000):
    zeige(f"F3 Grundstueck {p}", rechne_grob(F3, VGN, preis=p))
s = suche_eingabe(replace(F3, grundstueckspreis=D(1500000)), VGN, "markt_miete", D("10"), D("30"), D("0.01"))
print("  noetige Miete bei 1,5 Mio Grundstueck:", s["status"], [l["wert"] for l in s["loesungen"]])
F3v = replace(F3, markt_miete=D("17.50"), kostenkennwert=D(3000))
zeige("F3v 17,50 / KKW 3000", rechne_grob(F3v, VGN))
tp("F3v Basis Bank", F3v, VGN)
L = rechne_grob(F3v, VGN).darlehen
for _ in range(6):
    kfw = min(D(3600000), L); i = (kfw * D("0.025") + (L - kfw) * D("0.04")) / L
    L = rechne_grob(replace(F3v, zins=i), VGN).darlehen
print(f"  Mischzins {i*100:.3f} %, Darlehen gesamt {eur(L)}")
tp("F3v mit KfW (Mischzins)", replace(F3v, zins=i), VGN)
tp("F3v Stress", F3v, VGN, stress=True)
tp("F3v verfuegbares EK 5 Mio", replace(F3v, verfuegbares_ek=D(5000000)), VGN)
F4 = replace(F3, foerderung=replace(A.FOERDERUNG_B, bodenrichtwert=D(450)), haltedauer=20)
for n in (20, 36, 42):
    e = rechne_grob(replace(F4, haltedauer=n), VGN)
    zeige(f"F4 Haltedauer {n}", e)
tp("F4 Haltedauer 36", replace(F4, haltedauer=36), VGN)
tp("F4 Haltedauer 36, Ziel 3 %", replace(F4, haltedauer=36), replace(VGN, zielrendite=D("0.03")))
e = rechne_grob(replace(F4, haltedauer=36), VGN)
z = e.plan.zeilen
ns = [sum(z[u]["nachschuss"] if "nachschuss" in z[u] else 0 for u in range(j*12-11, j*12+1)) for j in range(1, 8)]
print("  Keys:", list(z[30].keys())[:40])
