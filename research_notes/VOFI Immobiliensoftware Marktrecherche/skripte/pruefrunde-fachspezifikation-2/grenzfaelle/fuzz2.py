"""Zufallsfaelle Neubau mit Grobfoerderung, KfW und allen Lesarten von MA-031, MA-032, MA-026; Ankauf mit Kennzeichen E-41."""
import random
from fuzz import *

if __name__ == "__main__":
    anzahl, saat = int(sys.argv[1]), int(sys.argv[2])
    random.seed(saat)
    zaehl = {}
    for i in range(anzahl):
        e = zufall_neubau()
        if e.foerderung is None:
            e = replace(e, foerderung=replace(A.FOERDERUNG_B, darlehensquote=q(0, 0.6), zuschussquote=q(0, 0.4), eigenmittelquote=q(0, 0.2)))
        e = replace(e, haltedauer=random.randint(max(1, (e.bauzeit_monate + 30) // 12 + 1), 42))
        vg = replace(zufall_vg(), ma031_zuschuss=random.choice(["sofort", "verteilt", "minderung"]),
                     ma032_entgelte_sofort=random.random() < 0.3, ma026_foerder_nachrang=random.random() < 0.3,
                     anlaufleerstand=random.randint(0, 6), bereit_satz=q(0, 0.005), bereit_frei=random.randint(0, 24))
        stress = random.random() < 0.4
        s, r = kalk(e, vg, KATN, stress=stress)
        key = s if s != "eingabe" else "eingabe " + r[:4]
        zaehl[key] = zaehl.get(key, 0) + 1
        if s in ("ABSTURZ", "gesperrt"):
            print(f"--- Fall {i}: {s} stress {stress} Lesart {vg.ma031_zuschuss}")
            print("    ", r if s == "ABSTURZ" else r.befunde[:5])
            print("     EIN", e)
    print("Zaehlung", zaehl)
