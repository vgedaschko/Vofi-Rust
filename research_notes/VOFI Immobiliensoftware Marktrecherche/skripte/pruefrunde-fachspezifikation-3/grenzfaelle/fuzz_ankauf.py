"""GF3-Z2 Zufallsfaelle Ankauf: uebernommenes Darlehen, gebundener Bestand, Stress mit Neubemessung, E-41/E-69, n 1 bis 42."""
from h import *
import random, sys, collections, time
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
ANZ = int(sys.argv[2]) if len(sys.argv) > 2 else 600
zaehler = collections.Counter(); auffaellig = []
GR = {"steuer.kuerzung_bleibt_verkaufsjahr": "x"}
t0 = time.time()
for i in range(ANZ):
    status = random.choice([KOERPERSCHAFT, PRIVAT, GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN, BEFREIT, KOERPERSCHAFT_OHNE_GEWST])
    kz = status in (KOERPERSCHAFT, GEPRAEGTE_PG) and random.random() < 0.6
    st = A.steuer(status, erweiterte_kuerzung=kz, kuerzung_bleibt_verkaufsjahr=kz and random.random() < 0.5)
    n = random.choice([1, 2, 3, 5, 9, 10, 11, 12, 20, 40, 42])
    ue = None
    if random.random() < 0.5:
        rs = random.choice([100000, 500000, 1300000, 1500000, 2000000])
        ue = dict(restschuld=D(rs), nennbetrag=D(rs) * D(random.choice(["1", "1.2", "2"])), zins=D(random.choice(["0", "0.005", "0.03", "0.06"])),
                  tilgungssatz=D(random.choice(["0", "0.01", "0.02", "0.05"])), bindung_jahre=random.choice([None, 1, 2, 5, 10, 20, 40]))
        if random.random() < 0.5:
            ue["anschluss_zins"] = D(random.choice(["0", "0.02", "0.07"]))
    geb = random.random() < 0.3
    e = replace(ANK, steuer=st, haltedauer=n, uebernommen=ue, bodenanteil=D("0.3") if status in (PRIVAT, KOERPERSCHAFT_OHNE_GEWST) else None,
                gebunden_anteil=D(random.choice(["0.4", "1"])) if geb else NULL, bindung_jahre=random.choice([1, 5, 12, 50]) if geb else 0,
                gebundene_miete=D("6.8") if geb else None, zins=D(random.choice(["0", "0.01", "0.04", "0.09"])),
                zinsbindung_jahre=random.choice([1, 5, 10, 15, 40]), verkaufsfaktor=D(random.choice(["4", "12", "18", "30"])),
                stau_betrag=D(random.choice([0, 0, 120000, 400000])), stau_jahr=random.choice([0, 1, 2, 3, 4, 50]), begruendungen=GR)
    vg = replace(VG, stress=replace(VG.stress, zusage_pp=D(random.choice(["0", "0.005", "0.03", "0.1"]))))
    stress = random.random() < 0.5
    s, r = kalk(e, vg, KAT, stress=stress, p=random.choice([12, 12, 1]))
    zaehler[s] += 1
    if s in ("ABSTURZ", "gesperrt"):
        auffaellig.append((i, s, r if isinstance(r, str) else r.befunde[:3], dict(status=status, n=n, ue=ue, geb=geb, stress=stress)))
        continue
    if s == "eingabe":
        zaehler["eingabe " + r[:60]] += 1
        continue
    for u, zz in enumerate(r.plan.zeilen):
        for name, t in zz["tranchen"].items():
            if t["rest"] < 0 or t["tilgung"] < 0 or t["zins"] < 0:
                auffaellig.append((i, "negativ", (u, name), dict(ue=ue)))
print(dict(zaehler), f"{time.time()-t0:.0f} s")
for a in auffaellig[:20]:
    print(" ", a)
