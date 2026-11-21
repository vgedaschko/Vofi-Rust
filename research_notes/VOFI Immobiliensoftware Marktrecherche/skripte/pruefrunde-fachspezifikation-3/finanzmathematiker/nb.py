"""Eigener Nachbau des Neubaus RF-12 (frei finanziert, mit KfW-Darlehen, mit Grobfoerderung) allein aus dem Text der
Fachspezifikation (Stand 2026-11-21) und Anhang A.4/A.6. Pruefrunde 3, Finanzmathematiker. Kein Code des
Referenzrechners oder der Blindrechnung verwendet. Monatsraster, Koerperschaft ohne Kennzeichen, Rundung 'Cent'."""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP, ROUND_FLOOR, ROUND_CEILING
getcontext().prec = 40
C = D("0.01")
def r2(x): return D(x).quantize(C, rounding=ROUND_HALF_UP)
def r12(x): return D(x).quantize(D("1e-12"), rounding=ROUND_HALF_UP)
def floorc(x): return D(x).quantize(C, rounding=ROUND_FLOOR)
def root(x, n): return (D(x).ln() / D(n)).exp()
def konform(x, p=12): return r12(root(1 + x, p) - 1)
def idx(g, n):
    i = [None, D(1)]
    for _ in range(n + 1): i.append(r12(i[-1] * (1 + g)))
    return i
def ceil_int(x): return int(D(x).to_integral_value(rounding=ROUND_CEILING))

BASIS = dict(
    P=D(1200000), enk=D("0.08"), gfl=D(2500), brw=D(400), wfl=D(2000), einh=D(30), bgf=D(2600), kw=D(2320),
    zuschlag=D("0.25"), bauzeit=18, vorlauf=0, anlauf=3, miete=D("16.50"), nachh=None,
    mietst=D("0.02"), kostst=D("0.02"), bauprst=D("0.03"), leer=D("0.015"), ausfall=D("0.005"),
    verw=D(350), inst=[(0, D(9)), (22, D("11.50")), (32, D(14))], bk=D(2),
    w=15, kappa=D("0.15"), T=36,
    zins=D("0.04"), tilg=D("0.02"), bindung=120, aufschlag=D("0.01"),
    bereit=D("0.0025"), bereit_frei=6,
    faktor=D(24), vk=D("0.015"), n=15, h=D("0.02"), k=D("0.08"),
    beta=D("0.65"), mu=D("1.2"), mintilg=D("0.02"), kat14=D("0.15"), H32=None,
    kst={2027: D("0.15"), 2028: D("0.14"), 2029: D("0.13"), 2030: D("0.12"), 2031: D("0.11")}, kst_ab=D("0.10"),
    soli=D("0.055"), messz=D("0.035"), hebe=D("4.00"), z=D("0.05"), start=2027, afa=D("0.03"),
    kfw=None,          # dict(betrag, T, f, zins)
    foerd=False,       # Grobfoerderung nach KAT-10 (Gruppe B)
    stress=set(),
)
FOE = dict(dq=D("0.60"), zq=D("0.20"), eq=D("0.20"), bemgr=D(5460), eingang=D("8.20"), fest=3, schritt=3,
           sigma=D("0.0615"), bindung_j=35, beitrag=D("0.005"), ent_d=D("0.01"), ent_z=D("0.0075"),
           rueck_j=42, frist_tilg=24, teil=[D("0.30"), D("0.30"), D("0.30"), D("0.10")], rohbau=D("0.5"),
           innenputz=D("0.75"), mintilg_bank=D("0.01"), zinslos_j=35, zins_danach=D("0.05"))
KFWK = dict(prov=D("0.0015"), prov_frei=12, bindung=120)

def kst(par, j):
    return par["kst"].get(par["start"] + j - 1, par["kst_ab"])

def annuitaet(K, ip, m):
    if ip == 0: return r2(K / m)
    q = (1 + ip) ** m
    return r2(K * ip * q / (q - 1))

def rechne(par, P=None, **ueber):
    par = dict(par); par.update(ueber)
    if P is not None: par["P"] = D(P)
    st = par["stress"]
    n = par["n"]; N = 12 * n
    bz = par["bauzeit"] + (3 if "bauzeit" in st else 0)
    bauende = par["vorlauf"] + bz
    anlauf = par["anlauf"]
    v1 = bauende + anlauf + 1                # erster Vermietungsmonat
    # Baukosten R-11.2
    BK0 = r2(par["bgf"] * par["kw"] * (1 + par["zuschlag"]))
    if "baukosten" in st: BK0 = r2(BK0 * D("1.05"))
    raten = {}
    for m in range(1, bz + 1):
        f = r12(((1 + par["bauprst"]).ln() * D(par["vorlauf"] + m) / 12).exp())
        raten[par["vorlauf"] + m] = r2(BK0 / bz * f)
    BK = sum(raten.values())
    P = par["P"]; enk = r2(P * par["enk"])
    GK = P + enk + BK
    # Basiswerte fuer die Bemessung (R-11.8: Ertrag, Wertansatz, Mittelbedarf, Bauzeit des Basisfalls)
    if st:
        basis = rechne(par, stress=set(), _nur_bemessung=True)
    # Foerderung
    FD = Z = MEK = ENT = D(0); entd = entz = D(0)
    if par["foerd"]:
        F = FOE
        BKb = BK if not st else basis["BK"]
        zf = min(BKb, F["bemgr"] * par["wfl"]) + min(P + enk, par["brw"] * par["gfl"])
        FD = r2(F["dq"] * zf); Z = r2(F["zq"] * zf); MEK = r2(F["eq"] * zf)
        entd = r2(FD * F["ent_d"]); entz = r2(Z * F["ent_z"]); ENT = entd + entz
    KFW = par["kfw"]["betrag"] if par["kfw"] else D(0)
    M = GK + ENT
    # Mietpfad (frei: R-6.7 mit R-6.3 Zeile 3, d = 0; gefoerdert: R-6.5)
    mst = par["mietst"] - (D("0.005") if "mietst" in st else D(0))
    leer = par["leer"] + (D("0.02") if "leer" in st else D(0))
    mi = idx(mst, n + 3)
    def vj(m): return (m - v1) // 12 + 1     # Vermietungsjahr
    miete = {}
    if par["foerd"]:
        F = FOE
        for m in range(v1, N + 1):
            bj = (m - (bauende + 1)) // 12 + 1  # Bindungsjahr ab Bezug
            stufe = 0 if bj <= F["fest"] else (bj - F["fest"] - 1) // F["schritt"] + 1
            ende = bauende + 12 * F["bindung_j"]
            b_pj = (ende - 1) // 12 + 1
            pj = (m - 1) // 12 + 1
            if pj <= b_pj + 1:
                if m <= ende:
                    miete[m] = min(F["eingang"] * (1 + F["sigma"]) ** stufe, par["miete"] * mi[vj(m)])
                else:
                    miete[m] = miete[m - 1]
            else:
                raise NotImplementedError("Miete nach Bindungsende + 1 Jahr nicht gebaut")
    else:
        t_letzte = v1 - 1
        for m in range(v1, N + 1):
            if m == v1:
                miete[m] = par["miete"]; continue
            prev = miete[m - 1]
            ziel = par["miete"] * mi[vj(m)]
            if ziel > prev and m - 1 >= t_letzte + par["w"]:
                k = m - par["T"]
                bezug = miete[k] if k >= v1 else par["miete"]
                neu = min(ziel, bezug * (1 + par["kappa"]))
                if neu > prev:
                    miete[m] = neu; t_letzte = m - 1; continue
            miete[m] = prev
    ki = idx(par["kostst"], n + 2)
    soll, einz, bew = {}, {}, {}
    for m in range(1, N + 1):
        j = (m - 1) // 12 + 1
        soll[m] = r2(par["wfl"] * miete[m]) if m in miete else D(0)
        einz[m] = r2(soll[m] * (1 - leer - par["ausfall"]))
        if m >= bauende + 1:
            alter = (m - (bauende + 1)) // 12
            ih = [s for a, s in par["inst"] if alter >= a][-1]
            jb = (par["verw"] * par["einh"] + ih * par["wfl"] + par["bk"] * par["wfl"]) * ki[j]
            bew[m] = r2(jb / 12)
        else:
            bew[m] = D(0)
    # nachhaltiger Reinertrag R-5.12 (Basis)
    if st:
        REn = basis["REn"]
    else:
        nm = par["nachh"] if par["nachh"] is not None else par["miete"]
        rohs = [r2(par["wfl"] * min(miete[m], nm * mi[vj(m)])) for m in range(v1, v1 + 12)]
        roh = sum(rohs); ausf = sum(x - r2(x * (1 - par["leer"] - par["ausfall"])) for x in rohs)
        bw = sum(bew[m] for m in range(v1, v1 + 12))
        REn = roh - max(bw + ausf, r2(par["kat14"] * roh))
    # Bemessungskonditionen der uebrigen Tranchen
    mB = 12 * (par["H32"] if par["H32"] else par["bindung"] // 12)
    KDU = D(0)
    if KFW:
        kf = par["kfw"]; m = (kf["T"] - kf["f"]) * 12
        iv = kf["zins"]; ikal = max(iv, par["H25"] if par.get("H25") is not None else par["zins"] + par["aufschlag"])
        mv = min(mB, KFWK["bindung"])
        iB = r12((iv * mv + ikal * (mB - mv)) / mB)
        rb = max(annuitaet(KFW, iB / 12, m), r2(KFW * (iB + par["mintilg"]) / 12))
        KDU += 12 * rb
    # Grenzen
    zb = par["zins"] + (D("0.005") if "zusage" in st else D(0))
    ik = max(zb, par["H25"] if par.get("H25") is not None else zb + par["aufschlag"]); tk = max(par["tilg"], par["mintilg"])
    if par["foerd"]: tk = max(tk, FOE["mintilg_bank"])
    Wb = (basis["GK"] if st else GK)
    Mb = (basis["M"] if st else M)
    if par["foerd"]:
        # Kapitaldienst Foerderdarlehen zu Bemessungskonditionen; Ratenzahl aus dem Tilgungsplan (unten)
        letzte_teil = bauende + anlauf + 1
        T_til = min(letzte_teil + 1, par["vorlauf"] + 1 + FOE["frist_tilg"])  # Entscheidung im Monat 'Vorlauf'
        zahl = bauende + FOE["rueck_j"] * 12 - T_til + 1
        rate_fd = r2(FD / zahl)
        iB_fd = D(0)  # zinslos ueber den Bemessungszeitraum
        rb = r2(FD * (iB_fd + max(D(12) / zahl, par["mintilg"])) / 12)
        KDU += 12 * rb + 12 * r2(FD * FOE["beitrag"] / 12)
    A = par["beta"] * Wb - KFW - FD
    s = ik + tk
    Bg = floorc((REn / par["mu"] - KDU) / s)
    while Bg > 0 and REn < par["mu"] * (KDU + 12 * r2(Bg * s / 12)): Bg -= C
    Cg = Mb - KFW - FD - Z - MEK
    L = max(D(0), floorc(min(A, Bg, Cg)))
    if par.get("_nur_bemessung"):
        return dict(REn=REn, GK=GK, M=M, BK=BK, L=L)
    EKplan = M - KFW - FD - Z - L
    # Mittelabruf R-11.3
    bedarf = {0: P + enk}
    for m, r in raten.items(): bedarf[m] = bedarf.get(m, D(0)) + r
    ek_rest = EKplan
    ek_ein = {}; fd_aus = {}; z_aus = {}; kfw_aus = {}; bank_aus = {}
    luecke = D(0); luecke_m = {}
    abgerufen = D(0); FZ = FD + Z
    teil_m = []
    if par["foerd"]:
        F = FOE
        teil_m = [par["vorlauf"] + 1, par["vorlauf"] + ceil_int(F["rohbau"] * bz) + 1,
                  par["vorlauf"] + ceil_int(F["innenputz"] * bz) + 1, bauende + anlauf + 1]
    kfw_rest = KFW; bank_rest = L; erste_foe = True
    fd_offen, z_offen = FD, Z
    for m in range(0, max(bauende, teil_m[-1] if teil_m else 0) + 1):
        b = bedarf.get(m, D(0))
        e = min(ek_rest, b); ek_rest -= e; b -= e
        if e: ek_ein[m] = e
        if par["foerd"]:
            if b > 0 and erste_foe: b += ENT  # erster Abruf traegt die Entgelte
            anteil = sum(a for a, tm in zip(FOE["teil"], teil_m) if tm <= m)
            og = r2(anteil * FZ)
            if m == teil_m[-1]:
                ab = FZ - abgerufen
            else:
                ab = max(D(0), min(og - abgerufen, b + luecke))
            if ab > 0:
                if erste_foe: erste_foe = False
                dt = min(r2(ab * FD / FZ), fd_offen); zt = ab - dt
                if zt > z_offen: zt = z_offen; dt = ab - zt
                fd_offen -= dt; z_offen -= zt
                fd_aus[m] = dt; z_aus[m] = zt; abgerufen += ab
                deck = min(ab, b + luecke)
                # zuerst Bedarf des Monats, dann Luecke
                rest = ab
                x = min(rest, b); b -= x; rest -= x
                y = min(rest, luecke); luecke -= y; rest -= y
        if KFW and b > 0:
            x = min(kfw_rest, b); kfw_rest -= x; b -= x
            if x: kfw_aus[m] = x
        if b > 0:
            x = min(bank_rest, b); bank_rest -= x; b -= x
            if x: bank_aus[m] = x
        if m == bauende:
            if ek_rest > 0: ek_ein[m] = ek_ein.get(m, D(0)) + ek_rest; ek_rest = D(0)
            if KFW and kfw_rest > 0: kfw_aus[m] = kfw_aus.get(m, D(0)) + kfw_rest; kfw_rest = D(0)
            if bank_rest > 0: bank_aus[m] = bank_aus.get(m, D(0)) + bank_rest; bank_rest = D(0)
        luecke += b
        luecke_m[m] = luecke
    # Darlehensplaene
    ip = konform(par["h"]); kp = konform(par["k"])
    anschl = par["zins"] + (D("0.005") if "zusage" in st else D(0)) + par["aufschlag"] + (D("0.01") if "anschluss" in st else D(0))
    zins0 = par["zins"] + (D("0.005") if "zusage" in st else D(0))
    # Abschreibung R-7.3
    afa = {}; rest_g = BK
    for j in range(1, n + 1):
        nm = max(0, min(12 * j, N) - max(bauende, 12 * (j - 1)))
        a = min(rest_g, r2(BK * par["afa"] * nm / 12)); afa[j] = a; rest_g -= a
    # Entgeltverteilung Foerderdarlehen R-7.15 und Zuschuss R-7.19
    fd_ent_j = {}; z_ert_j = {}; z_ent_j = {}
    if par["foerd"]:
        S = min(fd_aus); E = bauende + 12 * FOE["zinslos_j"]; rest = entd
        for j in range(1, n + 1):
            if j < n:
                mo = max(0, min(12 * j, E) - max(S, 12 * (j - 1)))
                x = min(rest, r2(entd * mo / (E - S)))
            else: x = rest
            fd_ent_j[j] = x; rest -= x
        bm = 12 * FOE["bindung_j"]; b0 = bauende  # Bindungsmonate bauende+1 .. bauende+bm
        rueck = r2(Z * max(0, bauende + bm - N) / bm) if N < bauende + bm else D(0)
        rz = Z - rueck; re = entz
        for j in range(1, n + 1):
            mo = max(0, min(12 * j, b0 + bm) - max(b0, 12 * (j - 1)))
            if j < n:
                x = min(rz, r2(Z * mo / bm)); y = min(re, r2(entz * mo / bm))
            else:
                x = rz; y = re
            z_ert_j[j] = x; z_ent_j[j] = y; rz -= x; re -= y
    else:
        rueck = D(0)
    # Finanzplan
    rs_b = D(0); rs_k = D(0); rs_f = D(0); bank_n = D(0); kfw_n = D(0)
    rate_b = None; rate_k = None
    gut = D(0); kk = D(0)
    einl = {}; nach = {}
    acc = dict(eop=D(0), zh=D(0), ent=D(0)); vv_k = D(0); vv_g = D(0)
    bauz_zins = D(0); bereit_sum = D(0); prov_sum = D(0); kk_zins_sum = D(0); kk_max = D(0)
    kd_j = {}; re_j = {}
    t_b = bauende + 1
    if KFW:
        uA = min(kfw_aus); t_k = uA + 12 * par["kfw"]["f"] + 1
        m_k = (par["kfw"]["T"] - par["kfw"]["f"]) * 12; ende_k = t_k + m_k - 1
    if par["foerd"]:
        zinslos_ende = bauende + 12 * FOE["zinslos_j"]
        fd_letzte = bauende + FOE["rueck_j"] * 12
    vp = erl = gv = None; VFE = None
    for u in range(0, N + 1):
        j = max(1, (u - 1) // 12 + 1)
        orig = -bedarf.get(u, D(0)) + einz.get(u, D(0)) - bew.get(u, D(0))
        if par["foerd"]: orig += z_aus.get(u, D(0))
        ein_plan = ek_ein.get(u, D(0))
        fin = D(0); zinsen = D(0); tilg_u = D(0); kd = D(0)
        # Bankdarlehen
        if L:
            zb_u = r2(rs_b * (zins0 if u <= par["bindung"] else anschl) / 12) if u >= 1 else D(0)
            if 1 <= u <= bauende: bauz_zins += zb_u
            bz_u = D(0)
            if u > par["bereit_frei"] and bank_n < L and u >= 1:
                bz_u = r2((L - bank_n) * par["bereit"] * 12 / 12); bereit_sum += bz_u
            tb = D(0)
            if u == t_b:
                rate_b = r2(L * ((zins0 if u <= par["bindung"] else anschl) + par["tilg"]) / 12)
            if u == par["bindung"] + 1 and rate_b is not None:
                rate_b = r2(rs_b * (anschl + max(par["tilg"], par["mintilg"])) / 12)
            if u >= t_b and rate_b is not None:
                tb = min(rs_b, max(D(0), rate_b - zb_u))
            rs_b -= tb
            aus = bank_aus.get(u, D(0)); rs_b += aus; bank_n += aus
            fin += aus - zb_u - bz_u - tb; zinsen += zb_u; tilg_u += tb; acc["ent"] += zb_u + bz_u
            acc["eop"] -= zb_u + bz_u
            if u >= v1: kd += zb_u + tb
        if KFW:
            zk_u = r2(rs_k * (par["kfw"]["zins"] if u <= KFWK["bindung"] else anschl) / 12) if u >= 1 else D(0)
            if 1 <= u <= bauende: bauz_zins += zk_u
            pv = D(0)
            if u > KFWK["prov_frei"] and kfw_n < KFW and u >= 1:
                pv = r2((KFW - kfw_n) * KFWK["prov"]); prov_sum += pv
            tk_ = D(0)
            if u == t_k:
                rate_k = annuitaet(KFW, (par["kfw"]["zins"] if u <= KFWK["bindung"] else anschl) / 12, m_k)
            if u == KFWK["bindung"] + 1 and rate_k is not None:
                rate_k = annuitaet(rs_k, anschl / 12, ende_k - KFWK["bindung"])
            if rate_k is not None and u >= t_k:
                tk_ = min(rs_k, max(D(0), rate_k - zk_u)) if u < ende_k else rs_k
            rs_k -= tk_
            aus = kfw_aus.get(u, D(0)); rs_k += aus; kfw_n += aus
            fin += aus - zk_u - pv - tk_; zinsen += zk_u; tilg_u += tk_; acc["ent"] += zk_u + pv; acc["eop"] -= zk_u + pv
            if u >= v1: kd += zk_u + tk_
        if par["foerd"]:
            zf_u = r2(rs_f * FOE["zins_danach"] / 12) if u > zinslos_ende else D(0)
            bt = r2(rs_f * FOE["beitrag"] / 12) if u >= 1 else D(0)
            tf = D(0)
            if u >= T_til:
                tf = rs_f if u == fd_letzte else min(rs_f, rate_fd)
            rs_f -= tf
            aus = fd_aus.get(u, D(0))
            einb = D(0)
            if aus and u == min(fd_aus): einb += entd
            if z_aus.get(u) and u == min(z_aus): einb += entz
            rs_f += aus
            fin += aus - einb - zf_u - bt - tf; zinsen += zf_u; tilg_u += tf
            acc["ent"] += zf_u + bt; acc["eop"] -= zf_u + bt
            if u >= v1: kd += zf_u + bt + tf
        # Konten
        hz = r2(gut * ip) if u >= 1 else D(0); kz = r2(kk * kp) if u >= 1 else D(0)
        kk_zins_sum += kz
        acc["zh"] += hz; acc["ent"] += kz; acc["eop"] -= kz
        acc["eop"] += einz.get(u, D(0)) - bew.get(u, D(0))
        if par["foerd"]:
            acc["zsof"] = acc.get("zsof", D(0)) + z_aus.get(u, D(0)) - (entz if (z_aus.get(u) and u == min(z_aus)) else D(0))
        abl = D(0)
        if u == N:
            jm = 12 * soll[u] * (1 - leer)
            vp = r2(par["faktor"] * (D("0.90") if "faktor" in st else D(1)) * jm)
            erl = vp - r2(vp * par["vk"])
            orig += erl - rueck
            # Vorfaelligkeit R-5.16 (Bank- und KfW-Darlehen; Foerderdarlehen ohne), Satz 1 %, KAT-13 126 Monate
            vfe_b = vfe_k = D(0)
            if L and rs_b:
                rb_ = max(0, min(par["bindung"], max(bank_aus) + 126) - N); vfe_b = r2(rs_b * D("0.01") * rb_ / 12)
            if KFW and rs_k:
                rk_ = max(0, min(KFWK["bindung"], max(kfw_aus) + 126) - N); vfe_k = r2(rs_k * D("0.01") * rk_ / 12)
            VFE = (vfe_b, vfe_k)
            abl = rs_b + rs_k + rs_f + vfe_b + vfe_k; rs_b = rs_k = rs_f = D(0)
            acc["eop"] -= vfe_b + vfe_k; acc["ent"] += vfe_b + vfe_k
        steuer = D(0)
        if u >= 1 and u % 12 == 0:
            eop = acc["eop"] - afa[j]
            privat = par.get("status") == "privat"
            zl_ = par.get("zl") or ("verteilt" if (not privat or par.get("e70")) else "sofort")
            if par["foerd"]:
                if zl_ == "verteilt":
                    eop += z_ert_j[j] - z_ent_j[j]
                else:
                    eop += acc.get("zsof", D(0)) - (rueck if u == N else D(0))
                eop -= fd_ent_j[j]
                acc["ent"] += fd_ent_j[j]
            g = D(0)
            if u == N:
                rbw = P + enk + BK - sum(afa.values()); gv = erl - rbw; g = gv
                if privat and n > 10: g = D(0)
            if privat:
                ev = eop + g
                if par.get("h38") == "sofort": sv = r2(D("0.42") * ev)
                else:
                    if ev < 0: vv_k += -ev; sv = D(0)
                    else:
                        x = min(vv_k, ev); vv_k -= x; sv = r2(D("0.42") * (ev - x))
                steuer = sv + r2(D("0.26375") * acc["zh"])
                acc = dict(eop=D(0), zh=D(0), ent=D(0))
        if privat_jahr := (u >= 1 and u % 12 == 0 and par.get("status") == "privat"):
            pass
        elif u >= 1 and u % 12 == 0:
            ein = eop + acc["zh"] + g
            if ein < 0: vv_k += -ein; eb = D(0)
            else:
                x = min(vv_k, ein); vv_k -= x; eb = ein - x
            ks = r2(kst(par, j) * (1 + par["soli"]) * eb)
            ge = ein + D("0.25") * max(D(0), acc["ent"] - D(200000))
            if ge < 0: vv_g += -ge; g2 = D(0)
            else:
                x = min(vv_g, ge); vv_g -= x; g2 = ge - x
            g2 = (g2 / 100).to_integral_value(rounding=ROUND_FLOOR) * 100
            steuer = ks + r2(g2 * par["messz"] * par["hebe"])
            acc = dict(eop=D(0), zh=D(0), ent=D(0))
        saldo = orig + fin - abl + hz - kz - steuer + ein_plan
        netto = gut - kk + saldo
        erlaubt = luecke_m.get(u, D(0)) if u <= max(luecke_m) else D(0)
        if netto >= 0: gut, kk = netto, D(0)
        elif -netto <= erlaubt: gut, kk = D(0), -netto
        else:
            gut = D(0); kk = erlaubt; nach[u] = -netto - erlaubt
        kk_max = max(kk_max, kk)
        e = ein_plan + nach.get(u, D(0))
        if e: einl[u] = e
        if u >= v1:
            kd_j[j] = kd_j.get(j, D(0)) + kd; re_j[j] = re_j.get(j, D(0)) + einz.get(u, D(0)) - bew.get(u, D(0))
    EW = gut - kk
    # Unterlassensalternative (a_L = h)
    la = wa = ka = D(0); vk_ = vg_ = D(0); az = ak = D(0)
    for u in range(0, N + 1):
        j = max(1, (u - 1) // 12 + 1)
        zl = r2(la * ip) if u else D(0); zw = r2(wa * ip) if u else D(0); zk = r2(ka * kp) if u else D(0)
        az += zl + zw; ak += zk
        stv = D(0)
        if u >= 1 and u % 12 == 0:
            ein = az - ak
            if ein < 0: vk_ += -ein; b_ = D(0)
            else:
                x = min(vk_, ein); vk_ -= x; b_ = ein - x
            if par.get("status") == "privat":
                stv = r2(D("0.26375") * az); az = ak = D(0)
            else:
                ks = r2(kst(par, j) * (1 + par["soli"]) * b_)
                ge = ein + D("0.25") * max(D(0), ak - D(200000))
                if ge < 0: vg_ += -ge; g2 = D(0)
                else:
                    x = min(vg_, ge); vg_ -= x; g2 = ge - x
                g2 = (g2 / 100).to_integral_value(rounding=ROUND_FLOOR) * 100
                stv = ks + r2(g2 * par["messz"] * par["hebe"]); az = ak = D(0)
        e = einl.get(u, D(0))
        x_ = min(ka, e); ka -= x_; la += e - x_
        x = wa - ka + zl + zw - zk - stv
        if x >= 0: wa, ka = x, D(0)
        else:
            wa = D(0); y = -x; t = min(la, y); la -= t; ka = y - t
    EWU = la + wa - ka
    f = {}
    for u in range(1, N + 1):
        j = (u - 1) // 12 + 1
        sz = D("0.26375") if par.get("status") == "privat" else kst(par, j) * (1 + par["soli"]) + par["messz"] * par["hebe"]
        f[u] = r12(root(1 + par["h"] * (1 - sz), 12))
    w = {N: D(1)}
    for t in range(N - 1, -1, -1): w[t] = w[t + 1] * f[t + 1]
    Dn = sum(e * w[u] for u, e in einl.items()) / w[0]
    r = root(EW / Dn, n) - 1; rU = root(EWU / Dn, n) - 1
    EU = EW - Dn * (1 + par["z"]) ** n
    ek_inv = sum(e for u, e in einl.items() if u <= bauende)
    lauf = sum(v for u, v in nach.items() if bauende < u < N)
    deck = {j: re_j[j] / kd_j[j] for j in kd_j if kd_j[j]}
    return dict(BK0=BK0, BK=BK, raten=raten, GK=GK, M=M, REn=REn, KDU=KDU, A=A, B=Bg, C=Cg, L=L, EKplan=EKplan,
                FD=FD, Z=Z, ENT=ENT, EW=EW, EWU=EWU, dEW=EW - EWU, r=r, rU=rU, EU=EU, ek_inv=ek_inv, lauf=lauf,
                vp=vp, gv=gv, bauz_zins=bauz_zins, bereit=bereit_sum, prov=prov_sum, kk_max=kk_max,
                kk_zins=kk_zins_sum, rate_b=rate_b, rate_k=rate_k, afa=afa, miete=miete, nach=nach,
                ek_ein=ek_ein, fd_aus=fd_aus, z_aus=z_aus, kfw_aus=kfw_aus, bank_aus=bank_aus, deck=deck,
                luecke=luecke_m, v1=v1, T_til=(T_til if par["foerd"] else None),
                rate_fd=(rate_fd if par["foerd"] else None), z_ert=z_ert_j, rueck=rueck, VFE=VFE)
