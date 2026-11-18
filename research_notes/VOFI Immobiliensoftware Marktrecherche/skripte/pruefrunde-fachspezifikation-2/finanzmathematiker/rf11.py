"""Eigener Nachbau RF-11 (Ankauf, Monatsraster, Koerperschaft) allein aus dem Text der Fachspezifikation, Runde 2.
Kein Code des Referenzrechners verwendet."""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP, ROUND_FLOOR
import math, sys
getcontext().prec = 40

C = D("0.01")
def r2(x):  # kaufmaennisch auf Cent
    return x.quantize(C, rounding=ROUND_HALF_UP)
def r12(x):
    return x.quantize(D("1e-12"), rounding=ROUND_HALF_UP)
def floorc(x):
    return x.quantize(C, rounding=ROUND_FLOOR)
def root(x, n):  # x^(1/n) mit hoher Genauigkeit
    return D(x).ln().__truediv__(n).exp() if False else (D(x).ln() / D(n)).exp()

def konform(x, p=12):
    return r12(root(1 + x, p) - 1)

def index_reihe(g, n):
    idx = [None, D(1)]
    for j in range(2, n + 2):
        idx.append(r12(idx[-1] * (1 + g)))
    return idx

BASIS = dict(
    P=D(2400000), enk=D("0.10"), boden=D("0.25"), afa=D("0.02"), flaeche=D(1320), einheiten=D(20),
    ist=D("8.50"), vm=D("9.20"), d=4, w=15, kappa=D("0.15"), T=36,
    mietst=D("0.02"), kostst=D("0.02"), bauprst=D("0.03"), leer=D("0.015"), ausfall=D("0.005"),
    verw=D(350), inst=D(14), bk=D(2), co2_aus=D(30), co2_ant=D("0.40"), co2_p=D(50), co2_st=D("0.05"),
    stau=D(120000), stau_k=2,
    zins=D("0.04"), tilg=D("0.02"), bindung=120, aufschlag=D("0.01"), anschl_stress=D(0), zusage=D(0),
    faktor=D(18), vk=D("0.015"), n=12,
    h=D("0.02"), k=D("0.08"),
    beta=D("0.65"), mu=D("1.2"), mintilg=D("0.02"), kat14=D("0.15"),
    kst={2027: D("0.15"), 2028: D("0.14"), 2029: D("0.13"), 2030: D("0.12"), 2031: D("0.11")}, kst_ab=D("0.10"),
    soli=D("0.055"), messz=D("0.035"), hebe=D("4.00"), z=D("0.05"), start=2027,
    fixL=None, regel="tilgungssatz",
)

def kst_satz(par, jahr):
    return par["kst"].get(jahr, par["kst_ab"])

def mietpfad(par, N):
    n_j = (N + 11) // 12 + 1
    idx = index_reihe(par["mietst"], n_j)
    ist, d = par["ist"], par["d"]
    miete = {}
    t_letzte = 0
    for m in range(1, N + 1):
        j = (m - 1) // 12 + 1
        vmj = par["vm"] * idx[j]
        if j == 1 or (d == 0):
            ziel = vmj if not (j == 1) else vmj
        if j == 1:
            ziel = vmj
        else:
            ziel = vmj if d == 0 else ist + (vmj - ist) * min(D(1), D(j - 1)) * 1 / 1
            if d != 0:
                ziel = ist + (vmj - ist) * min(D(d), D(j - 1)) / D(d)
        if m == 1:
            miete[1] = ist
            continue
        prev = miete[m - 1]
        if m >= 13 and m - 1 >= t_letzte + par["w"]:
            ref = miete[m - par["T"]] if m - par["T"] >= 1 else ist  # MA-037 vorsichtig: kein Spielraum gegen Vor-Stichtag
            cap = ref * (1 + par["kappa"]) if m - par["T"] >= 1 else ist
            neu = min(ziel, cap)
            if neu > prev:
                miete[m] = neu
                t_letzte = m - 1
                continue
        miete[m] = prev
    return miete

def bank_B(RE, mu, ik, tk, KDU=D(0)):
    s = ik + tk
    B = floorc((RE / mu - KDU) / s)
    while RE < mu * (KDU + 12 * r2(B * s / 12)):
        B -= C
    return B

RESTLZ=[]
VFE=[]
def rechne(par, P=None, stress=None, L_fix=None, voll=False):
    par = dict(par)
    if P is not None:
        par["P"] = D(P)
    n = par["n"]; N = 12 * n
    P = par["P"]
    enk = r2(P * par["enk"]); M = P + enk
    boden = r2(M * par["boden"]); grundl = M - boden
    afa_j = r2(grundl * par["afa"] * 12 / 12)
    # Basis-Ertraege fuer Bemessung (immer Basisannahmen)
    def ertrag(pr):
        miete = mietpfad(pr, N)
        kidx = index_reihe(pr["kostst"], n + 1)
        cidx = index_reihe(pr["co2_st"], n + 1)
        soll, einz, bew = {}, {}, {}
        for m in range(1, N + 1):
            j = (m - 1) // 12 + 1
            soll[m] = r2(pr["flaeche"] * miete[m])
            einz[m] = r2(soll[m] * (1 - pr["leer"] - pr["ausfall"]))
            jb = (pr["verw"] * pr["einheiten"] + pr["inst"] * pr["flaeche"] + pr["bk"] * pr["flaeche"]) * kidx[j]
            co2 = r2(pr["co2_aus"] * pr["flaeche"] * pr["co2_ant"] * pr["co2_p"] * cidx[j] / 1000 / 12)
            bew[m] = r2(jb / 12) + co2
        return miete, soll, einz, bew
    miete_b, soll_b, einz_b, bew_b = ertrag(par)
    roh = sum(par["flaeche"] * min(miete_b[m], par["vm"] * index_reihe(par["mietst"], 2)[1]) for m in range(1, 13))
    roh = r2(roh)
    bew1 = sum(bew_b[m] for m in range(1, 13))
    abzug = max(bew1 + roh * (par["leer"] + par["ausfall"]), r2(par["kat14"] * roh))
    REn = roh - abzug
    ik = max(par["zins"], par["zins"] + par["aufschlag"]); tk = max(par["tilg"], par["mintilg"])
    A = floorc(par["beta"] * P); B = bank_B(REn, par["mu"], ik, tk); Cc = M
    L = max(D(0), min(A, B, Cc)) if L_fix is None else L_fix
    EK0 = M - L
    # Stress anwenden
    sp = dict(par)
    if stress:
        sp["leer"] = par["leer"] + D("0.02"); sp["mietst"] = par["mietst"] - D("0.005")
        sp["inst"] = par["inst"] * D("1.10"); sp["faktor"] = par["faktor"] * D("0.90")
        sp["stau"] = par["stau"] * D("1.10"); sp["zusage"] = D("0.005"); sp["anschl_stress"] = D("0.01")
    miete, soll, einz, bew = ertrag(sp)
    zins0 = sp["zins"] + sp["zusage"]
    anschl = sp["zins"] + sp["aufschlag"] + sp["zusage"] + sp["anschl_stress"]
    rate = r2(L * (zins0 + sp["tilg"]) / 12)
    stau_z = r2(sp["stau"] * (1 + sp["bauprst"]) ** sp["stau_k"]); stau_m = 12 * sp["stau_k"]
    aktiv = (stau_z / D("1.19") > D("0.15") * grundl) and sp["stau_k"] <= 3
    afa_m = r2(stau_z * par["afa"]) if aktiv else D(0)
    ph = konform(par["h"]); pk = konform(par["k"])
    rs = L; gut = D(0); kk = D(0)
    ek = {0: EK0}; nach = {}
    vv_k = D(0); vv_g = D(0)
    acc = dict(eop=D(0), zh=D(0), ent=D(0))
    rows = []
    zinsen_j = {}; kd_j = {}; re_j = {}
    vp = None; abl = None; gv = None
    for u in range(1, N + 1):
        j = (u - 1) // 12 + 1
        i_u = zins0 if u <= sp["bindung"] else anschl
        if u == sp["bindung"] + 1:
            if sp["regel"] == "tilgungssatz":
                rate = r2(rs * (anschl + sp["tilg"]) / 12)
            elif sp["regel"] == "rate":
                rate = max(rate, r2(rs * anschl / 12))
            elif sp["regel"] == "restlaufzeit":
                ip = zins0 / 12
                mreal = (rate / (rate - rs * ip)).ln() / (1 + ip).ln()
                mm = max(1, int(mreal))
                ipn = anschl / 12; q = (1 + ipn) ** mm
                rate = r2(rs * ipn * q / (q - 1))
                RESTLZ.append((mreal, mm, rate))
        z = r2(rs * i_u / 12)
        tilg = min(rs, max(D(0), rate - z))
        rs -= tilg
        hz = r2(gut * ph); kz = r2(kk * pk)
        orig = einz[u] - bew[u]
        erh = stau_z if u == stau_m else D(0)
        orig -= erh
        abl_u = D(0); vk_u = D(0)
        if u == N:
            jm = 12 * soll[u] * (1 - sp["leer"])
            vp = r2(sp["faktor"] * jm)
            vk = r2(vp * sp["vk"])
            erl = vp - vk
            orig += erl
            abl_u = rs; rs = D(0); abl = abl_u
            rb = max(0, min(sp["bindung"], 0 + 120 + 6) - N)
            vfe = r2(abl_u * D("0.01") * rb / 12)
            VFE.append(vfe)
        vfe_u = VFE[-1] if (u == N and VFE) else D(0)
        acc["eop"] += einz[u] - bew[u] - (D(0) if aktiv else erh) - z - kz - vfe_u
        acc["zh"] += hz; acc["ent"] += z + kz + vfe_u
        zinsen_j[j] = zinsen_j.get(j, D(0)) + z
        kd_j[j] = kd_j.get(j, D(0)) + z + tilg
        re_j[j] = re_j.get(j, D(0)) + einz[u] - bew[u]
        steuer = D(0)
        if u % 12 == 0:
            jahr = par["start"] + j - 1
            eop = acc["eop"] - afa_j - (afa_m if (aktiv and j > sp["stau_k"]) else D(0))
            g = D(0)
            if u == N:
                rbw = M - n * afa_j + ((stau_z - (n - sp["stau_k"]) * afa_m) if aktiv else D(0))
                gv = erl - rbw; g = gv
            ein = eop + acc["zh"] + g
            # KSt
            if ein < 0:
                vv_k += -ein; ek_bem = D(0)
            else:
                v = min(vv_k, ein); vv_k -= v; ek_bem = ein - v
            kst = r2(kst_satz(par, jahr) * (1 + par["soli"]) * ek_bem)
            hinz = D("0.25") * max(D(0), acc["ent"] - D(200000))
            ge = ein + hinz
            if ge < 0:
                vv_g += -ge; ge2 = D(0)
            else:
                v = min(vv_g, ge); vv_g -= v; ge2 = ge - v
            ge2 = (ge2 / 100).to_integral_value(rounding=ROUND_FLOOR) * 100
            mb = r2(ge2 * par["messz"]); gst = r2(mb * par["hebe"])
            steuer = kst + gst
            acc = dict(eop=D(0), zh=D(0), ent=D(0))
        saldo = orig - z - tilg - abl_u - vfe_u + hz - kz - steuer
        netto = gut - kk + saldo
        if netto >= 0:
            gut, kk = netto, D(0)
        else:
            gut = D(0); nach[u] = -netto; kk = D(0)
        rows.append((u, z, tilg, rs, hz, steuer, gut))
    EW = gut - kk
    # Unterlassensalternative
    einl = {0: EK0}; einl.update(nach)
    la = D(0); wa = D(0); kka = D(0)
    vvk = D(0); vvg = D(0); acz = D(0); ack = D(0)
    la = EK0
    for u in range(1, N + 1):
        j = (u - 1) // 12 + 1
        zl = r2(la * ph); zw = r2(wa * ph); zk = r2(kka * pk)
        acz += zl + zw; ack += zk
        st = D(0)
        if u % 12 == 0:
            jahr = par["start"] + j - 1
            ein = acz - ack
            if ein < 0: vvk += -ein; b = D(0)
            else:
                v = min(vvk, ein); vvk -= v; b = ein - v
            kst = r2(kst_satz(par, jahr) * (1 + par["soli"]) * b)
            ge = ein + D("0.25") * max(D(0), ack - D(200000))
            if ge < 0: vvg += -ge; g2 = D(0)
            else:
                v = min(vvg, ge); vvg -= v; g2 = ge - v
            g2 = (g2 / 100).to_integral_value(rounding=ROUND_FLOOR) * 100
            st = kst + r2(r2(g2 * par["messz"]) * par["hebe"])
            acz = D(0); ack = D(0)
        e = einl.get(u, D(0))
        # Einlage: zuerst KK zurueck, Rest in langfristige Anlage
        rk = min(kka, e); kka -= rk; la += e - rk
        x = wa - kka + zl + zw - zk - st
        if x >= 0: wa, kka = x, D(0)
        else:
            wa = D(0); y = -x
            t = min(la, y); la -= t; kka = y - t
    EWU = la + wa - kka
    # Vergleichsfaktor
    f = {}
    for u in range(1, N + 1):
        j = (u - 1) // 12 + 1
        jahr = par["start"] + j - 1
        sz = kst_satz(par, jahr) * (1 + par["soli"]) + par["messz"] * par["hebe"]
        f[u] = r12(root(1 + par["h"] * (1 - sz), 12))
    w = {N: D(1)}
    for t in range(N - 1, -1, -1):
        w[t] = w[t + 1] * f[t + 1]
    Dn = sum(e * w[u] for u, e in einl.items()) / w[0]
    Z = EW; ZU = EWU
    r = root(Z / Dn, n) - 1; rU = root(ZU / Dn, n) - 1
    EU = Z - Dn * (1 + par["z"]) ** n
    deck = {j: (re_j[j] / kd_j[j] if kd_j[j] else None) for j in kd_j}
    out = dict(P=P, L=L, A=A, B=B, REn=REn, EK0=EK0, nach=nach, EW=EW, EWU=EWU, dEW=EW - EWU, r=r, rU=rU,
               EU=EU, w0=w[0], w24=w.get(24), vp=vp, abl=abl, gv=gv, deck=deck, rows=rows, miete=miete,
               zinsen=zinsen_j, ekbed=EK0 + sum(nach.values()), afa=afa_j, boden=boden)
    return out

if __name__ == "__main__":
    o = rechne(BASIS)
    for k in ["L", "A", "B", "REn", "EK0", "nach", "vp", "abl", "gv", "EW", "EWU", "dEW", "r", "rU", "EU", "w0", "w24", "ekbed"]:
        print(k, o[k])
    print("deck", {j: round(float(v), 4) for j, v in o["deck"].items()})
    print("Mieten Aenderung:", [(m, round(float(o['miete'][m]), 4)) for m in range(2, 145) if o['miete'][m] != o['miete'][m-1]])
    print("rows120,121,144", o["rows"][119], o["rows"][120], o["rows"][143])
    s = rechne(BASIS, stress=True, L_fix=o["L"])
    for k in ["L", "EK0", "nach", "vp", "EW", "EWU", "dEW", "r", "rU", "EU"]:
        print("S", k, s[k])
    print("Sdeck", {j: round(float(v), 4) for j, v in s["deck"].items()})
