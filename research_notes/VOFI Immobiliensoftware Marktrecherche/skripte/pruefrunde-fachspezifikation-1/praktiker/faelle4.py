exec(open("faelle.py").read().split("# ---------------------------------------------------------------- Fall 1")[0])
F3 = replace(A.NEUBAU, wohnflaeche=D(2450), einheiten=36, bgf=D(3400), kostenkennwert=D(3000),
             grundstueckspreis=D(2000000), grundstuecksflaeche=D(3200), bauzeit_monate=22, enk_satz=D("0.065"),
             markt_miete=D("17.50"), verkaufsfaktor=D(25), haltedauer=15)
tp("F3v Instandhaltung 9", F3, replace(VGN, instandhaltung_je_qm=D(9)))
F4 = replace(F3, kostenkennwert=D(3300), markt_miete=D("15.00"), foerderung=replace(A.FOERDERUNG_B, bodenrichtwert=D(450)), haltedauer=36)
e = rechne_grob(F4, VGN); z = e.plan.zeilen
print("  F4 Nachschuss je Planjahr 3..12:", [eur(sum(z[u]["nachschuss"] for u in range(j*12-11, j*12+1))) for j in range(3, 13)])
