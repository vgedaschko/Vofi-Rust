"""GF3-Z Zufallsfaelle ueber die neuen Regeln: gefoerderter Neubau, KfW, Stress, E-69, E-70, Vorlauf, Bauzeit, Haltedauer.
Zaehlt Abstuerze, gesperrte Laeufe (verletzte Proben), negative Restschulden, negative Tilgungen und Status."""
from h import *
import random, sys, collections, time
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
ANZ = int(sys.argv[2]) if len(sys.argv) > 2 else 400
zaehler = collections.Counter()
auffaellig = []
t0 = time.time()
GR = {"steuer.kuerzung_bleibt_verkaufsjahr": "x", "zuschuss_verteilung": "x", "festpreis": "x", "vorvermietet": "x"}
for i in range(ANZ):
    status = random.choice([KOERPERSCHAFT, PRIVAT, GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN, BEFREIT])
    kz = status in (KOERPERSCHAFT, GEPRAEGTE_PG) and random.random() < 0.5
    st = A.steuer(status, erweiterte_kuerzung=kz, kuerzung_bleibt_verkaufsjahr=kz and random.random() < 0.5)
    gef = random.random() < 0.6
    bz = random.choice([1, 2, 3, 5, 7, 11, 13, 17, 18, 19, 20, 21, 23, 24, 25, 30, 36, 47, 59, 60])
    vl = random.choice([0, 0, 1, 5, 12, 24, 60])
    min_n = -(-(vl + bz + 3 + 3 + 12) // 12)
    n = random.choice([min_n, min_n + 1, 10, 20, 35, 36, 37, 38, 42])
    n = min(max(n, min_n), 42)
    f = A.FOERDERUNG_B
    if gef:
        f = replace(f, bindung_jahre=random.choice([6, 10, 20, 35]), teilraten=random.choice(
            [f.teilraten, (D("0.5"), D("0.2"), D("0.2"), D("0.1")), (D(1), NULL, NULL, NULL), (NULL, NULL, NULL, D(1))]),
            eingangsmiete=random.choice([D("7.6"), D("8.2"), D(10), D(12)]))
    kfw = random.random() < 0.4
    lz, tf = random.choice([(10, 1), (10, 2), (25, 1), (25, 3), (35, 1), (35, 5)])
    e = replace(NB, steuer=st, bauzeit_monate=bz, vorlauf_monate=vl, haltedauer=n, foerderung=f if gef else None,
                kfw_betrag=D(random.choice([100000, 1000000, 3000000])) if kfw else NULL, kfw_laufzeit=lz, kfw_tilgungsfrei=tf,
                zuschuss_verteilung=gef and status in (PRIVAT, BEFREIT) and random.random() < 0.5 and False,
                vorvermietet=random.random() < 0.2, festpreis=random.random() < 0.2,
                zinsbindung_jahre=random.choice([1, 2, 5, 10, 15, 20, 40]), zins=D(random.choice(["0", "0.01", "0.04", "0.08"])),
                begruendungen=GR)
    if gef and status == PRIVAT and random.random() < 0.5:
        e = replace(e, zuschuss_verteilung=True)
    vg = replace(VG, kk_linie=random.choice([D(0), D(0), None, D(200000)]),
                 stress=replace(VG.stress, zusage_pp=D(random.choice(["0", "0.005", "0.03"])), bauzeit_monate=random.choice([0, 3, 12])))
    stress = random.random() < 0.5
    s, r = kalk(e, vg, KATN, stress=stress)
    zaehler[s] += 1
    if s == "ABSTURZ" or s == "gesperrt":
        auffaellig.append((i, s, r if isinstance(r, str) else r.befunde[:3], dict(status=status, gef=gef, bz=bz, vl=vl, n=n, kfw=kfw, lz=lz, tf=tf, stress=stress, linie=vg.kk_linie)))
        continue
    if s == "eingabe":
        zaehler["eingabe " + r.split()[0]] += 1
        continue
    z = r.plan.zeilen
    for u, zz in enumerate(z):
        for name, t in zz["tranchen"].items():
            if t["rest"] < 0 or t["tilgung"] < 0 or t["zins"] < 0:
                auffaellig.append((i, "negativ", (u, name, t["rest"], t["tilgung"]), dict(gef=gef, bz=bz, vl=vl, n=n)))
                break
    if r.kennzahlen["rendite"] is None:
        zaehler["rendite n.d."] += 1
print(dict(zaehler), f"{time.time()-t0:.0f} s")
for a in auffaellig[:20]:
    print(" ", a)
