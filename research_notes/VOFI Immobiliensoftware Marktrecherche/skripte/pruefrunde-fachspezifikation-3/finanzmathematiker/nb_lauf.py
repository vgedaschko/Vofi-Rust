from nb import *
o = rechne(BASIS)
for k in ["BK0", "BK", "GK", "REn", "A", "B", "C", "L", "EKplan", "ek_inv", "lauf", "bauz_zins", "bereit", "rate_b", "vp", "gv", "EW", "EWU", "dEW", "EU"]:
    print(k, o[k])
print("r", o["r"] * 100, "rU", o["rU"] * 100)
print("raten 1,2,18", o["raten"][1], o["raten"][2], o["raten"][18], "afa2", o["afa"][2])
print("bank_aus", {k: v for k, v in list(o["bank_aus"].items())[:2]}, "ek_ein 9", o["ek_ein"].get(9))
print("Erhoehungen", [m for m in range(o["v1"] + 1, 100) if o["miete"][m] != o["miete"][m - 1]])
print("deck", {j: round(float(v), 4) for j, v in o["deck"].items()})
