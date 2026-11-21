"""GF3-G3 Zielwertsuche: Begruendungspflicht wird je Gitterwert statt fuer den Ausgangsauftrag geprueft (R-11.9)."""
from h import *
vg = replace(VG, zielrendite=D("0.02"))
e = replace(ANK, abweichungen={"mindestdeckung": (D("1.3"), "")})
print("  Ausgangsauftrag 2,4 Mio.:", zeig(e, vg))
r = suche_eingabe(e, vg, KAT, "kaufpreis", D(1), D(8000000), D(1), raster=40)
print("  Zielwertsuche Kaufpreis (Abweichung ohne Begruendung):", r["status"], [(l["wert"], l["richtung"]) for l in r["loesungen"]],
      "unzulaessig", len(r["unzulaessig"]), sorted({k for _, k in r["unzulaessig"]}), "ab", min((x for x, _ in r["unzulaessig"]), default=None))
e2 = replace(ANK, abweichungen={"mindestdeckung": (D("1.3"), "Bankzusage")})
r2 = suche_eingabe(e2, vg, KAT, "kaufpreis", D(1), D(8000000), D(1), raster=40)
print("  dieselbe Suche mit Begruendung:                    ", r2["status"], [(l["wert"], l["richtung"]) for l in r2["loesungen"]], "unzulaessig", len(r2["unzulaessig"]))
