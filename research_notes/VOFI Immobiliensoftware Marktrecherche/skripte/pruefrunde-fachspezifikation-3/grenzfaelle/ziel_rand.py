"""GF3-I2 Zielwertsuche: Wechsel an der Grenze des zulaessigen Bereichs wird als Loesung ausgegeben."""
from h import *
ue = dict(restschuld=D(1500000), zins=D("0.03"), tilgungssatz=D("0.02"), bindung_jahre=10)
e = replace(ANK, uebernommen=ue)
print("  Preissuche (Vergleich):", tp(e))
r = suche_eingabe(e, VG, KAT, "kaufpreis", D(1), D(5000000), D(1), raster=40)
print("  Zielwertsuche Kaufpreis 1 bis 5 Mio.:", r["status"], [(l["wert"], l["richtung"]) for l in r["loesungen"]],
      "unzulaessig:", len(r["unzulaessig"]), sorted({k for _, k in r["unzulaessig"]}), "Meldungen", r["meldungen"])
for P in (1666666, 1666667, 1666668):
    print("   ", P, zeig(replace(e, kaufpreis=D(P))))
r = suche_eingabe(ANK, VG, KAT, "kaufpreis", NULL, D(5000000), D(1), raster=40)
print("  ohne uebernommenes Darlehen, Kaufpreis 0 bis 5 Mio.:", r["status"], [(l["wert"], l["richtung"]) for l in r["loesungen"]], "unzulaessig:", len(r["unzulaessig"]))
