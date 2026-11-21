from nb import *
G = dict(BASIS, foerd=True, n=38)
o = rechne(G)
for k in ["FD", "Z", "ENT", "M", "REn", "KDU", "A", "B", "C", "L", "EKplan", "ek_inv", "lauf", "kk_max", "kk_zins", "T_til", "rate_fd", "vp", "EW", "EWU", "dEW", "EU"]:
    print(k, o[k])
print("r", o["r"] * 100, "rU", o["rU"] * 100)
fa = o["fd_aus"]; za = o["z_aus"]
print("Abrufe FD+Z:", {m: fa[m] + za[m] for m in sorted(fa)})
print("Abruf Monat 10", fa[10], za[10])
print("Luecke Ende 7, 9, 14, 21:", o["luecke"].get(7), o["luecke"].get(9), o["luecke"].get(14), o["luecke"].get(21))
print("Ertrag Zuschuss PJ2, PJ3", o["z_ert"][2], o["z_ert"][3])
print("Nachschuesse je PJ 1..3", [sum(v for u, v in o["nach"].items() if (u - 1) // 12 + 1 == j and u > 0) for j in (1, 2, 3)], "u0", o["nach"].get(0))
print("deck min", min((float(v), j) for j, v in o["deck"].items() if j >= 3), "PJ37", o["deck"].get(37))
g20 = rechne(dict(G, n=20))
for k in ["vp", "rueck", "EW", "EWU", "dEW", "ek_inv"]: print("20J", k, g20[k])
print("20J r", g20["r"] * 100)
for n in (36, 37, 39):
    print(n, rechne(dict(G, n=n))["r"] * 100)
