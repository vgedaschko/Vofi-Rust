"""Zufallsfaelle Ankauf mit allen Steuerschaltern (E-41 bis E-44, MA-030, MA-036)."""
import random
from fuzz import *
if __name__ == "__main__":
    anzahl, saat = int(sys.argv[1]), int(sys.argv[2])
    random.seed(saat); zaehl = {}
    for i in range(anzahl):
        e = zufall_ankauf()
        st = replace(e.steuer, verlust=random.choice(["vortrag", "sofort"]), anteil_natuerliche=q(0, 1),
                     kuerzung_verkauf=random.random() < 0.5, aufgabegewinn=random.random() < 0.5, est_satz=q(0, 0.6))
        e = replace(e, steuer=st)
        vg = zufall_vg()
        s, r = kalk(e, vg, KAT, stress=random.random() < 0.3, p=random.choice([12, 12, 1]))
        key = s if s != "eingabe" else "eingabe " + r[:4]
        zaehl[key] = zaehl.get(key, 0) + 1
        if s in ("ABSTURZ", "gesperrt"):
            print(f"--- Fall {i}: {s}"); print("    ", r if s == "ABSTURZ" else r.befunde[:5]); print("     EIN", e)
    print("Zaehlung", zaehl)
