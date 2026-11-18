# -*- coding: utf-8 -*-
"""Blindrechnung: Nachbau der Grobkalkulation allein aus docs/fachspezifikation-rechenkern.md.
Nur Standardbibliothek, decimal. Kein Blick in den Referenzrechner."""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP, ROUND_FLOOR
import copy

getcontext().prec = 60
CENT = D('0.01')
E12 = D('1e-12')


def r2(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def r12(x):
    return D(x).quantize(E12, rounding=ROUND_HALF_UP)


def floor2(x):
    return D(x).quantize(CENT, rounding=ROUND_FLOOR)


_ps = {}


def psatz(x, p):
    """konformer Periodensatz R-2.6"""
    key = (x, p)
    if key not in _ps:
        _ps[key] = r12((1 + D(x)) ** (D(1) / D(p)) - 1) if p != 1 else D(x)
    return _ps[key]


def index_reihe(steig, n):
    idx = [None, D(1)]
    for _ in range(2, n + 2):
        idx.append(r12(idx[-1] * (1 + D(steig))))
    return idx


# ---------------------------------------------------------------- Vorgaben / Katalog (Anhang A.4)
def haus():
    return dict(
        z=D('0.05'), beta=D('0.65'), mu=D('1.2'), mindtilg=D('0.02'), anschl_auf=D('0.01'),
        st_anschl=D('0.01'), st_zins=D('0.005'), st_leer=D('0.02'), st_miete=D('0.005'),
        st_inst=D('0.10'), st_vf=D('0.10'), st_stau=D('0.10'), st_bk=D('0.05'), st_bz=3,
        regel='tilgungssatz', h=D('0.02'), aL=D('0.02'), k=D('0.08'), linie=D(0),
        miet=D('0.02'), kost=D('0.02'), bau=D('0.03'), leer=D('0.015'), vk=D('0.015'),
        verw=D(350), inst=[(0, D('9.00')), (22, D('11.50')), (32, D('14.00'))], bk=D(2),
        vfe=D('0.01'), such_ober=D(100), raster=40, fenster=20,
        e42=D('0.42'), d=4, zb=10, h25=None, flukt=D(0), ford=D('0.005'), anlauf=3,
        co2preis=D(50), co2steig=D('0.05'), zus1=D('0.05'), zus2=D('0.20'), stp=D(20000),
        bz_satz=D('0.0025'), bz_frei=6,
    )


def katalog():
    return dict(
        kst={2027: D('0.15'), 2028: D('0.14'), 2029: D('0.13'), 2030: D('0.12'), 2031: D('0.11')},
        kst_ab=D('0.10'), kst_bis=D('0.15'), zus=D('0.055'),
        messzahl=D('0.035'), abr=D(100), fb=D(24500), hebesatz=D(4),
        anrf=D(4), frist=10, afa_ankauf=D('0.02'), afa_neubau=D('0.03'),
        warte=15, kappung=D('0.15'), kap_T=36, bremse=True, bremse_auf=D('0.10'),
        co2_anteil=D('0.40'), weitere=D(0),
        f_darl=D('0.60'), f_zus=D('0.20'), f_ek=D('0.20'), f_grenze=D(5460), f_miete=D('8.20'),
        f_steig=D('0.0615'), f_fest=3, f_schritt=3, f_bindung=35, f_beitrag=D('0.005'),
        f_entg_d=D('0.01'), f_entg_z=D('0.0075'), f_tilg_j=42, f_zinslos=35, f_zins_danach=D('0.05'),
        g_steig=D('0.0615'), g_fest=3, g_schritt=3,
        anh_quote=D('0.15'), anh_jahre=3, ust=D('0.19'),
        kuend_sperr=120, kuend_frist=6, bank_mind=D('0.15'),
        kfw_max=D(100000), kfw_zins=D('0.025'), kfw_tilg=D('0.02'), kfw_frei=1, kfw_zb=10,
        hz_anteil=D('0.25'), hz_fb=D(200000), hz_pacht=D('0.5'),
        sockel=D(1000000), kap=D('0.26375'),
    )


def ankauf():
    return dict(
        art='ankauf', startjahr=2027, p=12, preis=D(2400000), enk=D('0.10'), boden=D('0.25'),
        baujahr=1990, wfl=D(1320), einh=20, ist=D('8.50'), vm=D('9.20'), markt=D('10.50'),
        leerfl=D(0), sonst=D(0), co2=D(30), status='koerp', kennz=False, verlust='vortrag',
        zins=D('0.04'), zb=10, tilg=D('0.02'), vf=D(18), n=12,
        stau=D(120000), stau_jahr=2, stau_art='erhaltung', d=4,
        geb=D(0), geb_ende=None, geb_miete=None, uebern=None, ek_verf=None, wert=None,
        erbbau=D(0), anteil=D(1), ma030_alt=False, ma036_alt=False, ma026_2=False, ma026_1=False,
        ma037_alt=False, H=haus(), K=katalog(), foerder=False, kfw=D(0),
    )


def neubau():
    return dict(
        art='neubau', startjahr=2027, p=12, preis=D(1200000), enk=D('0.08'), gfl=D(2500),
        brw=D(400), wfl=D(2000), einh=30, bgf=D(2600), kkw=D(2320), bauzeit=18, markt=D('16.50'),
        stp=0, stp_miete=D(0), co2=D(0), kfw=D(0), status='koerp', kennz=False, verlust='vortrag',
        zins=D('0.04'), zb=10, tilg=D('0.02'), vf=D(24), n=15, foerder=False,
        stau=D(0), stau_jahr=1, stau_art='erhaltung', d=0, erbbau=D(0), anteil=D(1),
        ma030_alt=False, ma036_alt=False, ma026_2=False, ma026_1=False, ma031='zufluss',
        ma032_sofort=False, wert=None, ek_verf=None, uebern=None,
        H=haus(), K=katalog(),
        # Lesart-Schalter fuer Luecken der Spezifikation (siehe Bericht)
        nb_d=0,                 # Anpassungsdauer der Neubaumiete (0: Ziel = Vergleichsmiete)
        bind_jahr='planjahr',   # R-6.6 im Neubau: 'planjahr' oder 'bindungsjahr'
        split='zuschuss_rest',  # Rundung der Aufteilung Foerderdarlehen/Zuschuss im Mittelabruf
    )


# ---------------------------------------------------------------- Miete
def pfad(N, start, anfang, ziel, kap_ref, t_letzte, w, kap, T, erster):
    """R-6.3: Miete je m2 und Monat fuer m = start..N (ungerundet)."""
    miete = {start: anfang}
    for m in range(start + 1, N + 1):
        prev = miete[m - 1]
        neu = prev
        if m >= erster and m - 1 >= t_letzte + w:
            ref = kap_ref(m - T, miete)
            if ref is not None:
                cand = min(ziel(m), ref * (1 + kap))
                if cand > prev:
                    neu = cand
                    t_letzte = m - 1
        miete[m] = neu
    return miete


def stufe(j, fest, schritt):
    return 0 if j <= fest else (j - fest - 1) // schritt + 1


# ---------------------------------------------------------------- Steuer
class Steuer:
    def __init__(self, c, ua=False):
        self.c = c
        self.K = c['K']
        self.ua = ua
        self.vv_e = D(0)
        self.vv_g = D(0)
        self.log = []

    def kst(self, j):
        jahr = self.c['startjahr'] + j - 1
        K = self.K
        if jahr in K['kst']:
            return K['kst'][jahr]
        return K['kst_bis'] if jahr < min(K['kst']) else K['kst_ab']

    # Grenzsteuersatz auf Zinsertraege (R-7.14)
    def s_z(self, j):
        c, K = self.c, self.K
        st = c['status']
        g = K['messzahl'] * K['hebesatz']
        if st == 'koerp':
            return self.kst(j) * (1 + K['zus']) + g
        if st == 'koerp_ohne':
            return self.kst(j) * (1 + K['zus'])
        if st in ('pg_gepr', 'pg_orig', 'einzel'):
            ant = D(1) if st == 'einzel' else c['anteil']
            a = ant * K['messzahl'] * min(K['anrf'], K['hebesatz'])
            return c['H']['e42'] + g - a
        if st == 'privat':
            return K['kap']
        if st == 'befreit':
            return D(0)
        if st == 'lehrbuch':
            return c['lb_satz']
        raise ValueError(st)

    def _vortrag(self, topf, x):
        """Verlustvortrag verrechnen; gibt Betrag nach Vortrag zurueck (>=0)."""
        vv = getattr(self, topf)
        if x < 0:
            setattr(self, topf, vv - x)
            return D(0)
        use = min(vv, x)
        setattr(self, topf, vv - use)
        return x - use

    def gewst(self, e_op, z_h, g_v, entg, erbbau, personen, sofort_linear, anteil=D(1)):
        c, K = self.c, self.K
        kennz = c['kennz'] and not self.ua and c['status'] in ('koerp', 'pg_gepr')
        fb_hz = D(0) if sofort_linear else K['hz_fb']
        hinzu = K['hz_anteil'] * max(D(0), entg + K['hz_pacht'] * erbbau - fb_hz)
        gv = g_v
        if c.get('ma036_alt') and c['status'] in ('pg_gepr', 'pg_orig') and not self.ua:
            gv = (1 - anteil) * g_v
        if kennz:
            ge0 = z_h + (D(0) if c['ma030_alt'] else gv)
        else:
            ge0 = e_op + z_h + gv + hinzu
        if sofort_linear:
            ge = ge0
        else:
            ge = self._vortrag('vv_g', ge0)
            ge = (ge / K['abr']).to_integral_value(rounding=ROUND_FLOOR) * K['abr']
            if personen:
                ge = max(D(0), ge - K['fb'])
        mb = r2(ge * K['messzahl'])
        return r2(mb * K['hebesatz']), mb

    def jahr(self, j, e_op, z_h, g_v, entg=D(0), erbbau=D(0), vfe=D(0), letztes=False):
        """Jahressteuer. e_op enthaelt die Vorfaelligkeit NICHT bei der Privatperson (Aufrufer)."""
        c, K = self.c, self.K
        st = c['status']
        sofort = c['verlust'] == 'sofort'
        det = {}
        if st == 'befreit':
            t = D(0)
        elif st in ('koerp', 'koerp_ohne'):
            gew = e_op + z_h + g_v
            satz = self.kst(j) * (1 + K['zus'])
            if sofort:
                kst = r2(satz * gew)
            else:
                kst = r2(satz * self._vortrag('vv_e', gew))
            gst = D(0)
            if st == 'koerp':
                gst, mb = self.gewst(e_op, z_h, g_v, entg, erbbau, False, sofort)
            t = kst + gst
            det = dict(kst=kst, gst=gst)
        elif st in ('pg_gepr', 'pg_orig', 'einzel'):
            ant = D(1) if st == 'einzel' else c['anteil']
            gew = e_op + z_h + g_v
            e42 = c['H']['e42']
            if sofort:
                est = r2(e42 * gew)
            else:
                est = r2(e42 * self._vortrag('vv_e', gew))
            lin = sofort and st == 'einzel'
            gst, mb = self.gewst(e_op, z_h, g_v, entg, erbbau, True, lin, ant)
            if sofort:
                anr = min(ant * K['anrf'] * mb, ant * gst)
            else:
                anr = min(ant * K['anrf'] * mb, ant * gst, ant * est)
            anr = r2(anr)
            t = est + gst - anr
            det = dict(est=est, gst=gst, anr=anr)
        elif st == 'privat':
            e = e_op
            if letztes and c['n'] <= K['frist']:
                gvs = g_v - vfe
                if gvs > 0:
                    e = e + gvs
            e42 = c['H']['e42']
            if sofort:
                tv = r2(e42 * e)
            else:
                tv = r2(e42 * self._vortrag('vv_e', e))
            tz = r2(K['kap'] * z_h)
            t = tv + tz
            det = dict(tv=tv, tz=tz)
        elif st == 'lehrbuch':
            gew = e_op + z_h + (g_v if c.get('lb_gv') else D(0))
            if sofort:
                t = r2(c['lb_satz'] * gew)
            else:
                t = r2(c['lb_satz'] * self._vortrag('vv_e', gew))
        else:
            raise ValueError(st)
        self.log.append((j, e_op, z_h, g_v, t, det, self.vv_e, self.vv_g))
        return t


# ---------------------------------------------------------------- Darlehen
class Tranche:
    def __init__(self, name, nenn, art, zins, tilg=D(0), bezug=None, ausz=None, einb=D(0),
                 tilg_beginn=1, zb_ende=None, anschluss=None, regel='tilgungssatz', beitrag=D(0),
                 bz_satz=D(0), bz_frei=0, m=None, foerder=False, bank=False, mindtilg=D(0)):
        self.name, self.nenn, self.art, self.zins, self.tilg = name, nenn, art, zins, tilg
        self.bezug = nenn if bezug is None else bezug
        self.ausz = ausz or {0: nenn}
        self.einb = einb
        self.tilg_beginn, self.zb_ende, self.anschluss, self.regel = tilg_beginn, zb_ende, anschluss, regel
        self.beitrag, self.bz_satz, self.bz_frei, self.m = beitrag, bz_satz, bz_frei, m
        self.foerder, self.bank, self.mindtilg = foerder, bank, mindtilg

    def plan(self, N, p):
        Z = [D(0)] * (N + 1)
        s = dict(ausz=list(Z), einb=list(Z), zins=list(Z), tilg=list(Z), beitr=list(Z), bz=list(Z),
                 abl=list(Z), rest=list(Z))
        rest = D(0)
        cum = D(0)
        first = min(self.ausz)
        t_voll = max(self.ausz)
        rate = r2(self.bezug * (self.zins + self.tilg) / p) if self.art == 'prozent' else None
        rate_r = r2(self.nenn / self.m) if self.art == 'raten' else None
        for u in range(0, N + 1):
            zins = beitr = bz = tilg = D(0)
            if u >= 1:
                satz = self.zins if (self.zb_ende is None or u <= self.zb_ende) else self.anschluss
                zins = r2(rest * satz / p)
                beitr = r2(rest * self.beitrag / p)
                if self.bz_satz and u > self.bz_frei and cum < self.nenn:
                    bz = r2((self.nenn - cum) * self.bz_satz * 12 / p)
                if u >= self.tilg_beginn:
                    if self.art == 'prozent':
                        if self.zb_ende is not None and u == self.zb_ende + 1:
                            if self.regel == 'tilgungssatz':
                                rate = r2(rest * (self.anschluss + max(self.tilg, self.mindtilg)) / p)
                            elif self.regel == 'rate':
                                rate = max(rate, zins)
                            elif self.regel == 'restlaufzeit':
                                ip_alt = self.zins / p
                                R, S = rate, rest
                                if ip_alt == 0:
                                    m = int(S / R)
                                else:
                                    m = int(((R / (R - S * ip_alt)).ln() / (1 + ip_alt).ln()))
                                m = max(1, m)
                                ip = self.anschluss / p
                                q = (1 + ip) ** m
                                rate = r2(S * ip * q / (q - 1)) if ip != 0 else r2(S / m)
                        tilg = min(rest, max(D(0), rate - zins))
                    elif self.art == 'raten':
                        k = u - self.tilg_beginn + 1
                        tilg = rest if k >= self.m else min(rest, rate_r)
            a = self.ausz.get(u, D(0))
            if a:
                s['ausz'][u] = a
                if u == first:
                    s['einb'][u] = self.einb
            cum += a
            rest = rest + a - tilg
            s['zins'][u], s['beitr'][u], s['bz'][u], s['tilg'][u] = zins, beitr, bz, tilg
            if u == N:
                s['abl'][u] = rest
                self.abl_rest = rest
                rest = D(0)
            s['rest'][u] = rest
        self.s = s
        self.first, self.t_voll = first, t_voll
        return s


# ---------------------------------------------------------------- Unterlassensalternative
def alternative(c, N, p, e, a):
    H = c['H']
    aLp, hp, kp = psatz(H['aL'], p), psatz(H['h'], p), psatz(H['k'], p)
    st = Steuer(c, ua=True)
    LA = WA = KK = D(0)
    zh_j = zk_j = D(0)
    for u in range(0, N + 1):
        zl = zw = zk = tax = D(0)
        if u >= 1:
            zl, zw, zk = r2(LA * aLp), r2(WA * hp), r2(KK * kp)
            zh_j += zl + zw
            zk_j += zk
            if u % p == 0:
                j = u // p
                if c['status'] == 'privat':
                    tax = st.jahr(j, D(0), zh_j, D(0))
                else:
                    tax = st.jahr(j, -zk_j, zh_j, D(0), entg=zk_j)
                zh_j = zk_j = D(0)
        ein = e[u]
        if ein > 0:
            rk = min(KK, ein)
            KK -= rk
            LA += ein - rk
        x = WA - KK + zl + zw - zk - tax - a[u]
        if x >= 0:
            WA, KK = x, D(0)
        else:
            WA = D(0)
            fehl = -x
            auf = min(LA, fehl)
            LA -= auf
            KK = fehl - auf
    return LA + WA - KK


# ---------------------------------------------------------------- Grobkalkulation
class M22(Exception):
    pass


def rechne(c0, stress=False, L_fix=None, detail=True, basis=None):
    c = copy.copy(c0)
    H = dict(c['H'])
    K = c['K']
    p = c['p']
    n = c['n']
    N = n * p
    nb = c['art'] == 'neubau'
    R = dict(meld=set())

    # ---- Stress (R-11.8)
    zins = c['zins']
    anschl_auf = H['anschl_auf']
    leer = H['leer']
    miet = H['miet']
    inst_fakt = D(1)
    vf = c['vf']
    stau = c['stau']
    bk_fakt = D(1)
    bauzeit = c.get('bauzeit', 0)
    st_anschl = D(0)
    if stress:
        zins = zins + H['st_zins']
        st_anschl = H['st_anschl']
        leer = min(D(1), leer + H['st_leer'])
        miet = miet - H['st_miete']
        inst_fakt = 1 + H['st_inst']
        vf = vf * (1 - H['st_vf'])
        stau = stau * (1 + H['st_stau'])
        bk_fakt = 1 + H['st_bk']
        if nb:
            bauzeit += H['st_bz']
    anschluss_bank = (c['zins'] if c.get('stress_anschl_alt') else zins) + anschl_auf + st_anschl
    ausfall = leer + H['ford']

    nj = n + 3
    iM = index_reihe(miet, nj)
    iK = index_reihe(H['kost'], nj)
    iC = index_reihe(H['co2steig'], nj)
    wfl = c['wfl']

    def pj(m):
        return (m - 1) // 12 + 1

    NM = n * 12                      # Monate
    # ---- Mieten je Teilflaeche (Monatswerte, ungerundet)
    teile = []                       # (Flaeche, {m: Miete})
    sonst = {m: D(0) for m in range(1, NM + 1)}
    if not nb:
        m0 = 1
        fl_geb = (wfl - c['leerfl']) * c['geb']
        fl_frei = (wfl - c['leerfl']) - fl_geb
        vmj = lambda m: c['vm'] * iM[pj(m)]
        ist, d = c['ist'], c['d']

        def ziel(m):
            j = pj(m)
            if j == 1 or d == 0:
                return vmj(m)
            return ist + (vmj(m) - ist) * min(D(1), D(j - 1) / D(d))
        if c.get('ma037_alt'):
            kap_ref = lambda k, mi: mi[k] if k >= 1 else ist
            tl = -K['kap_T']
        else:
            kap_ref = lambda k, mi: mi[k] if k >= 1 else None
            tl = 0
        frei = pfad(NM, 1, ist, ziel, kap_ref, tl, K['warte'], K['kappung'], K['kap_T'], 13)
        teile.append((fl_frei, frei))
        if fl_geb > 0:
            b = c['geb_ende']
            A0 = c['geb_miete']
            gm = {}
            last_step = 0
            prev = None
            for m in range(1, min(NM, (b + 1) * 12) + 1):
                j = pj(m)
                jj = min(j, b)
                val = min(A0 * (1 + K['g_steig']) ** stufe(jj, K['g_fest'], K['g_schritt']), vmj(m) if j <= b else D('1e9'))
                if j == b + 1:
                    val = gm[b * 12]
                if prev is not None and val != prev:
                    last_step = m - 1
                gm[m] = val
                prev = val
            if NM > (b + 1) * 12:
                aus = gm[(b + 1) * 12]

                def zielg(m):
                    j = pj(m)
                    return aus + (vmj(m) - aus) * min(D(1), D(j - (b + 1)) / D(d)) if d else vmj(m)
                st_m = (b + 1) * 12
                rest = pfad(NM, st_m, aus, zielg, lambda k, mi: (mi[k] if k >= st_m else gm[k]) if k >= 1 else None,
                            last_step, K['warte'], K['kappung'], K['kap_T'], st_m + 1)
                gm.update(rest)
            teile.append((fl_geb, gm))
        for m in range(1, NM + 1):
            sonst[m] = c['sonst'] * iM[pj(m)] / 12
    else:
        m0 = bauzeit + H['anlauf'] + 1
        vj = lambda m: (m - m0) // 12 + 1          # Vermietungsjahr
        vmj = lambda m: c['markt'] * iM[vj(m)]
        if not c['foerder']:
            anf = c['markt']
            dd = c['nb_d']

            def ziel(m):
                if dd == 0:
                    return vmj(m)
                return anf + (vmj(m) - anf) * min(D(1), D(vj(m) - 1) / D(dd))
            mi = pfad(NM, m0, anf, ziel, lambda k, mi_: mi_[k] if k >= m0 else anf, m0 - 1,
                      K['warte'], K['kappung'], K['kap_T'], m0 + 1)
        else:
            bz1 = bauzeit + 1
            bjahr = lambda m: (m - bz1) // 12 + 1
            B = K['f_bindung']
            bind_ende = bauzeit + B * 12          # letzter Monat der Bindung
            if c['bind_jahr'] == 'bindungsjahr':
                last_m = bind_ende + 12           # Ende von Jahr b+1 (Bindungsjahr)
                jb = lambda m: bjahr(m) - (B + 1)
            else:
                b_pj = pj(bind_ende)              # Planjahr des Bindungsendes
                last_m = (b_pj + 1) * 12
                jb = lambda m: pj(m) - (b_pj + 1)
            gm = {}
            prev = None
            last_step = m0 - 1
            for m in range(bz1, min(NM, last_m) + 1):
                bj = min(bjahr(m), B)
                val = K['f_miete'] * (1 + K['f_steig']) ** stufe(bj, K['f_fest'], K['f_schritt'])
                if m > bind_ende:
                    val = gm[bind_ende]
                if prev is not None and val != prev:
                    last_step = m - 1
                gm[m] = val
                prev = val
            if NM > last_m:
                aus = gm[last_m]
                dd = c['nb_d_bind'] if 'nb_d_bind' in c else H['d']

                def zielg(m):
                    return aus + (vmj(m) - aus) * min(D(1), D(jb(m)) / D(dd)) if dd else vmj(m)
                rest = pfad(NM, last_m, aus, zielg, lambda k, mi_: mi_[k] if k >= last_m else gm[k],
                            last_step, K['warte'], K['kappung'], K['kap_T'], last_m + 1)
                gm.update(rest)
            mi = {m: gm[m] for m in range(m0, NM + 1)}
        teile.append((wfl, mi))
        for m in range(m0, NM + 1):
            sonst[m] = D(c['stp']) * c['stp_miete'] * iM[vj(m)]

    def qm(m):
        return sum((fl * mi.get(m, D(0)) for fl, mi in teile), D(0)) / wfl if m >= m0 else D(0)

    soll_m = {}
    for m in range(1, NM + 1):
        if m < m0:
            soll_m[m] = D(0)
        else:
            soll_m[m] = r2(sum((fl * mi[m] for fl, mi in teile), D(0)) + sonst[m])

    # ---- Bewirtschaftung, CO2, Erbbauzins je Monat
    def inst_satz(alter):
        s = None
        for ab, v in H['inst']:
            if alter >= ab:
                s = v
        return s * inst_fakt

    bew_m, co2_m = {}, {}
    bezug = bauzeit + 1 if nb else 1
    for m in range(1, NM + 1):
        j = pj(m)
        if m < bezug:
            bew_m[m] = co2_m[m] = D(0)
            continue
        alter = (m - bezug) // 12 if nb else c['startjahr'] + j - 1 - c['baujahr']
        jb_ = (H['verw'] * c['einh'] + inst_satz(alter) * wfl + H['bk'] * wfl + K['weitere'] * wfl) * iK[j]
        bew_m[m] = r2(jb_ / 12)
        co2_m[m] = r2(c['co2'] * wfl * K['co2_anteil'] * H['co2preis'] * iC[j] / 1000 / 12)
    erb_m = {m: r2(c['erbbau'] * index_reihe(H['kost'], nj)[pj(m)] / 12) for m in range(1, NM + 1)}

    # ---- Perioden (p = 12: Monat; p = 1: Jahr)
    mp = 12 // p

    def monate(u):
        return range((u - 1) * mp + 1, u * mp + 1)
    Zr = [D(0)] * (N + 1)
    soll, miete, bew, erb = list(Zr), list(Zr), list(Zr), list(Zr)
    for u in range(1, N + 1):
        if p == 12:
            soll[u] = soll_m[u]
            bew[u] = bew_m[u] + co2_m[u]
            erb[u] = erb_m[u]
        else:
            soll[u] = r2(sum(sum((fl * mi.get(m, D(0)) for fl, mi in teile), D(0)) + sonst[m] for m in monate(u)))
            if c.get('jm_soll_alt'):
                soll[u] = sum((soll_m[m] for m in monate(u)), D(0))
            j = u
            alter = c['startjahr'] + j - 1 - c['baujahr']
            jb_ = (H['verw'] * c['einh'] + inst_satz(alter) * wfl + H['bk'] * wfl + K['weitere'] * wfl) * iK[j]
            bew[u] = r2(jb_) + r2(c['co2'] * wfl * K['co2_anteil'] * H['co2preis'] * iC[j] / 1000)
            erb[u] = r2(c['erbbau'] * iK[j])
        miete[u] = max(D(0), r2(soll[u] * (1 - ausfall)))

    # ---- Bemessung (R-11.2)
    preis = c['preis']
    enk = r2(preis * c['enk'])
    inv = list(Zr)
    erh = list(Zr)
    bau_raten = {}
    if nb:
        bk0 = r2(c['bgf'] * c['kkw'] * (1 + H['zus1'] + H['zus2']) * bk_fakt) + r2(D(c['stp']) * H['stp'] * bk_fakt)
        for m in range(1, bauzeit + 1):
            f = r12((1 + H['bau']) ** (D(m) / D(12)))
            bau_raten[m] = r2(bk0 / bauzeit * f)
        baukosten = sum(bau_raten.values(), D(0))
        gesamt = preis + enk + baukosten
        inv[0] = preis + enk
        for m, v in bau_raten.items():
            inv[m] += v
        R.update(bk0=bk0, baukosten=baukosten, gesamt=gesamt, raten=bau_raten)
        boden_w = preis + enk
        afa_grund = baukosten
        afa_satz = K['afa_neubau']
        W = gesamt
    else:
        baukosten = D(0)
        gesamt = preis + enk
        inv[0] = preis + enk
        boden_w = r2((preis + enk) * c['boden'])
        afa_grund = preis + enk - boden_w
        afa_satz = K['afa_ankauf']
        W = preis
    if c.get('wert'):
        W = c['wert']

    # Investitionsstau (R-6.10, R-6.16, R-8.4)
    stau_zahl = D(0)
    stau_abzug = D(0)
    akt_massn = {}     # Planjahr der Zahlung -> aktivierter Betrag
    stau0 = D(0)
    if stau > 0:
        k = c['stau_jahr']
        if k > n:
            stau_abzug = r2(stau * (1 + H['bau']) ** n)
        else:
            stau_zahl = r2(stau * (1 + H['bau']) ** k)
            u_st = k * p
            aktiv = c['stau_art'] == 'modernisierung'
            if k <= K['anh_jahre'] and not nb:
                if stau_zahl / (1 + K['ust']) > K['anh_quote'] * afa_grund:
                    aktiv = True
                    R['meld'].add('M-36')
            if aktiv:
                inv[u_st] += stau_zahl
                akt_massn[k if c.get('akt0_ab_j1', True) else max(k, 1)] = stau_zahl
            else:
                erh[u_st] += stau_zahl
            if k == 0:
                stau0 = stau_zahl
    R['stau_zahl'] = stau_zahl

    # Foerderung (R-11.14)
    fd = zu = mind_ek = entg_d = entg_z = D(0)
    if c['foerder']:
        zk_bau = min(baukosten, K['f_grenze'] * wfl)
        zk_gr = min(preis + enk, c['brw'] * c['gfl'])
        zk = zk_bau + zk_gr
        fd = r2(K['f_darl'] * zk)
        zu = r2(K['f_zus'] * zk)
        mind_ek = r2(K['f_ek'] * zk)
        entg_d = r2(fd * K['f_entg_d'])
        entg_z = r2(zu * K['f_entg_z'])
        if basis is not None:      # R-11.8: Foerdermittel bleiben auf dem Stand des Basisfalls
            fd, zu, mind_ek, entg_d, entg_z = basis['fd'], basis['zu'], basis['mind_ek'], basis['entg_d'], basis['entg_z']
            zk, zk_bau = basis['zk'], basis['zk_bau']
        R.update(zk=zk, zk_bau=zk_bau, fd=fd, zu=zu, mind_ek=mind_ek, entg=entg_d + entg_z, entg_d=entg_d, entg_z=entg_z)
    Mbed = preis + enk + baukosten + stau0 + entg_d + entg_z
    R['M'] = Mbed

    # ---- nachhaltiger Reinertrag (R-5.12) und Reinertrag im ersten Jahr der Vollvermietung
    vj_mon = range(m0, m0 + 12)
    vj_per = range((m0 - 1) // mp + 1, (m0 - 1) // mp + 1 + p)
    roh_n = D(0)
    roh_mon = []
    for m in vj_mon:
        x = D(0)
        for fl, mi in teile:
            vgl = vmj(m)
            x += fl * min(mi[m], vgl) if not c.get('ma026_3') else fl * mi[m]
        x += sonst[m]
        roh_mon.append(x)
        roh_n += x
    bew_vj = sum((bew[u] for u in vj_per), D(0))
    erb_vj = sum((erb[u] for u in vj_per), D(0))
    miete_vj = sum((miete[u] for u in vj_per), D(0))
    soll_vj = sum((soll[u] for u in vj_per), D(0))
    re_vj = miete_vj - bew_vj - erb_vj
    lesart_ausfall = c.get('ausfall_lesart', 'monat')
    if lesart_ausfall == 'exakt':
        ausf_n = roh_n * ausfall
    elif lesart_ausfall == 'runde':
        ausf_n = r2(roh_n * ausfall)
    else:  # 'monat'
        # je Monat wie R-6.4: Sollmiete gerundet, Einzahlung gerundet; Ausfall ist die Differenz
        ausf_n = sum((r2(x) - max(D(0), r2(r2(x) * (1 - ausfall))) for x in roh_mon), D(0))
        roh_n = sum((r2(x) for x in roh_mon), D(0))
    abzug = max(bew_vj + ausf_n, r2(K['bank_mind'] * roh_n))
    re_n = roh_n - abzug - erb_vj
    if c.get('ma026_3'):
        re_n = re_vj
    R.update(roh_n=roh_n, re_n=re_n, re_vj=re_vj, bew_vj=bew_vj, miete_vj=miete_vj, soll_vj=soll_vj)

    # ---- uebrige Darlehen
    tr = []
    U_sum = U_B = KD_U = D(0)
    zb_bank = c['zb'] * p
    i_k_bank = max(c['zins'], H['h25'] if H['h25'] is not None else c['zins'] + H['anschl_auf'])
    t_k_bank = max(c['tilg'], H['mindtilg'])
    if c.get('ma026_2'):
        i_k_bank, t_k_bank = c['zins'], c['tilg']
    foerd_tr = kfw_tr = ueb_tr = None
    if c.get('uebern'):
        ue = c['uebern']
        anschl_u = ue['anschluss'] + st_anschl
        ueb_tr = Tranche('uebernommen', ue['rest'], 'prozent', ue['zins'], ue['tilg'], bezug=ue['nenn'],
                         ausz={0: ue['rest']}, zb_ende=ue['zb'] * p, anschluss=anschl_u, regel=H['regel'],
                         beitrag=ue.get('beitrag', D(0)), foerder=ue.get('foerder', True), mindtilg=H['mindtilg'])
        tr.append(ueb_tr)
        U_sum += ue['rest']
        if ue.get('rang', 'vor') == 'vor':
            U_B += ue['rest']
        vertr = 12 * r2(ue['nenn'] * (ue['zins'] + ue['tilg']) / 12)
        ik = max(ue['zins'], H['h25'] if H['h25'] is not None else ue['anschluss'])
        tk = max(ue['tilg'], H['mindtilg'])
        basis_k = ue['rest'] if c.get('ueb_kalk_basis', 'rest') == 'rest' else ue['nenn']
        kalk = p * r2(basis_k * (ik + tk) / p) + r2(ue['rest'] * ue.get('beitrag', D(0)))
        if c.get('ma026_2') or (ue.get('foerder', True) and ue['zb'] * p >= zb_bank):
            kd = vertr
        else:
            kd = max(vertr, kalk)
        KD_U += kd
        R['kd_ueb'] = kd
    if nb and c['kfw'] > 0:
        U_sum += c['kfw']
        U_B += c['kfw']
        ik = max(K['kfw_zins'], H['h25'] if H['h25'] is not None else c['zins'] + H['anschl_auf'])
        tk = max(K['kfw_tilg'], H['mindtilg'])
        if c.get('ma026_2'):
            # Vertragskonditionen: Kapitaldienst der ersten zwoelf Tilgungsmonate
            kd = 12 * r2(c['kfw'] * (K['kfw_zins'] + K['kfw_tilg']) / 12)
        else:
            kd = p * r2(c['kfw'] * (ik + tk) / p)
        KD_U += kd
        R['kd_kfw_kalk'] = kd

    # Foerderdarlehen: vertraglicher Kapitaldienst der ersten zwoelf Tilgungsmonate
    if c['foerder']:
        U_sum += fd
        if not c.get('ma026_1'):
            U_B += fd
        mt = K['f_tilg_j'] * 12
        rate_f = r2(fd / mt)
        rest = fd
        kd = D(0)
        for _ in range(12):
            kd += r2(rest * K['f_beitrag'] / 12) + rate_f
            rest -= rate_f
        KD_U += kd
        R['kd_foerder'] = kd

    # ---- Bankdarlehen (R-5.12)
    A = H['beta'] * W - U_B
    C = Mbed - U_sum - zu - mind_ek
    if C < 0:
        raise M22()
    ik_tk = i_k_bank + t_k_bank
    if ik_tk == 0:
        Bv = None if re_n / H['mu'] >= KD_U else D(0)
    else:
        Bv = floor2((re_n / H['mu'] - KD_U) / ik_tk)
        while Bv > 0 and re_n < H['mu'] * (KD_U + p * r2(Bv * ik_tk / p)):
            Bv -= CENT
    cands = [('a', A), ('c', C)] + ([('b', Bv)] if Bv is not None else [])
    mn = min(v for _, v in cands)
    L = max(D(0), floor2(mn))
    bind = [k for k, v in cands if v == mn]
    if Bv is not None and Bv <= 0:
        L = D(0)
        R['meld'].add('M-21')
        bind = ['b']
    if basis is not None:
        L_fix = basis['L']
    if L_fix is not None:
        L = L_fix
    EK = Mbed - U_sum - zu - L
    R.update(A=A, B=Bv, C=C, L=L, bind=bind, EK=EK, W=W, KD_U=KD_U)

    # ---- Mittelabruf (R-11.3)
    einl = list(Zr)
    zus_fl = list(Zr)
    zus_entg = list(Zr)
    ausz_fd, ausz_kfw, ausz_bank = {}, {}, {}
    ek_r, fd_r, zu_r, kfw_r, L_r = EK, fd, zu, c.get('kfw', D(0)) if nb else D(0), L
    erster_f = True
    for u in range(0, (bauzeit if nb else 0) + 1):
        need = inv[u] + (erh[u] if u == 0 else D(0))
        if u >= 1 and not nb:
            need = D(0)
        if u >= 1 and nb:
            need = bau_raten.get(u, D(0))
        if u == 0 and c.get('uebern'):
            need -= c['uebern']['rest']
        x = min(ek_r, need)
        einl[u] += x
        ek_r -= x
        need -= x
        if need > 0 and (fd_r + zu_r) > 0:
            if erster_f:
                need += entg_d + entg_z
                zus_entg[u] = entg_z
                erster_f = False
            y = min(need, fd_r + zu_r)
            if y == fd_r + zu_r:
                yd, yz = fd_r, zu_r
            else:
                if c['split'] == 'zuschuss_rest':
                    yd = min(fd_r, r2(y * fd / (fd + zu)))
                    yz = y - yd
                else:
                    yz = min(zu_r, r2(y * zu / (fd + zu)))
                    yd = y - yz
            ausz_fd[u] = yd
            zus_fl[u] = yz
            fd_r -= yd
            zu_r -= yz
            need -= y
        if need > 0 and kfw_r > 0:
            y = min(need, kfw_r)
            ausz_kfw[u] = y
            kfw_r -= y
            need -= y
        if need > 0 and L_r > 0:
            y = min(need, L_r)
            ausz_bank[u] = y
            L_r -= y
            need -= y
        if need > 0:           # Rest (sollte null sein)
            einl[u] += need
    if not nb and c.get('uebern'):
        pass
    R['mittelabruf'] = dict(einl=[x for x in einl if x], fd=ausz_fd, kfw=ausz_kfw, bank=ausz_bank)

    # ---- Tranchen
    tb = bauzeit + 1 if nb else 1
    if L > 0:
        bank_tr = Tranche('bank', L, 'prozent', zins, c['tilg'], ausz=ausz_bank or {0: L}, tilg_beginn=tb,
                          zb_ende=zb_bank, anschluss=anschluss_bank, regel=H['regel'], bank=True,
                          bz_satz=H['bz_satz'] if nb else D(0), bz_frei=H['bz_frei'] * p // 12,
                          mindtilg=H['mindtilg'])
        tr.append(bank_tr)
    else:
        bank_tr = None
    if nb and c['kfw'] > 0:
        kfw_tr = Tranche('kfw', c['kfw'], 'prozent', K['kfw_zins'], K['kfw_tilg'], ausz=ausz_kfw,
                         tilg_beginn=bauzeit + 1 + K['kfw_frei'] * 12, zb_ende=K['kfw_zb'] * 12,
                         anschluss=anschluss_bank, regel=H['regel'], mindtilg=H['mindtilg'])
        tr.append(kfw_tr)
    if c['foerder']:
        foerd_tr = Tranche('foerder', fd, 'raten', D(0), ausz=ausz_fd, einb=entg_d, tilg_beginn=bauzeit + 1,
                           zb_ende=bauzeit + K['f_zinslos'] * 12, anschluss=K['f_zins_danach'],
                           beitrag=K['f_beitrag'], m=K['f_tilg_j'] * 12, foerder=True)
        tr.append(foerd_tr)
    for t in tr:
        t.plan(N, p)

    # ---- Verkauf (Kap. 8)
    mjm = lambda u: 12 * (soll[u] if p == 12 else r2(sum((fl * mi[u * 12] for fl, mi in teile), D(0)) + sonst[u * 12])) * (1 - leer) \
        - 12 * (erb[u] if p == 12 else erb_m[u * 12])
    vpreis = max(D(0), r2(vf * mjm(N)))
    vkost = r2(vpreis * H['vk'])
    verl = vpreis - vkost - stau_abzug
    rueck = D(0)
    bind_m_ges = K['f_bindung'] * 12
    if c['foerder']:
        offen = max(0, bauzeit + bind_m_ges - N)
        rueck = r2(zu * offen / bind_m_ges)
    R.update(vpreis=vpreis, vkost=vkost, verl=verl, rueck=rueck, mjm_N=mjm(N))

    # ---- Vorfaelligkeit (R-5.16)
    vfe = D(0)
    for t in tr:
        if t.foerder or t.zb_ende is None:
            continue
        t_voll = 0 if t.name == 'uebernommen' else t.t_voll
        rb = max(0, min(t.zb_ende, t_voll + (K['kuend_sperr'] + K['kuend_frist']) * p // 12) - N)
        v = r2(t.abl_rest * H['vfe'] * rb / p)
        t.vfe = v
        vfe += v
    if vfe > 0:
        R['meld'].add('M-25')
    R['vfe'] = vfe

    # ---- Abschreibung (R-7.3)
    afa = [D(0)] * (n + 1)
    rest_g = afa_grund
    zu_geb = D(0)
    ma031 = c.get('ma031', 'zufluss')
    if c['foerder'] and ma031 == 'minderung':
        zu_geb = r2(zu * zk_bau / zk)
        rest_g = afa_grund - zu_geb
    grund_eff = rest_g
    akt_rest = {}
    akt_sum = D(0)
    for j in range(1, n + 1):
        if nb:
            mon = sum(1 for m in range((j - 1) * 12 + 1, j * 12 + 1) if m > bauzeit)
        else:
            mon = 12
        x = min(rest_g, r2(grund_eff * afa_satz * mon / 12))
        rest_g -= x
        for jz, betrag in akt_massn.items():
            if j > jz:
                r_ = akt_rest.get(jz, betrag)
                y = min(r_, r2(betrag * afa_satz))
                akt_rest[jz] = r_ - y
                x += y
        afa[j] = x
    akt_sum = sum(akt_massn.values(), D(0))
    buchwert = boden_w - (zu - zu_geb if (c['foerder'] and ma031 == 'minderung') else D(0)) + grund_eff + akt_sum - sum(afa)
    R.update(afa=afa, buchwert=buchwert, boden=boden_w, afa_grund=afa_grund)

    # ---- steuerliche Nebenreihen: einbehaltene Betraege (R-7.15), Zuschuss (R-7.19)
    einb_abz = [D(0)] * (n + 1)
    einb_ges = entg_d + entg_z
    if einb_ges > 0:
        u1 = foerd_tr.first
        zbe = foerd_tr.zb_ende
        if c['status'] == 'privat' or c.get('ma032_sofort'):
            einb_abz[(max(u1, 1) - 1) // p + 1] = einb_ges
        else:
            ges_mon = zbe - u1
            done = D(0)
            for j in range(1, n + 1):
                mon = sum(1 for u in range((j - 1) * p + 1, j * p + 1) if u1 < u <= zbe)
                einb_abz[j] = r2(einb_ges * mon / ges_mon)
                done += einb_abz[j]
            if c.get('einb_rest', True):
                einb_abz[n] += einb_ges - done
    zus_ertrag = [D(0)] * (n + 1)
    if c['foerder']:
        if ma031 == 'zufluss':
            for u in range(0, N + 1):
                if zus_fl[u]:
                    zus_ertrag[max(1, (u - 1) // p + 1)] += zus_fl[u]
        elif ma031 == 'verteilt':
            done = D(0)
            for j in range(1, n + 1):
                mon = sum(1 for u in range((j - 1) * p + 1, j * p + 1) if bauzeit < u <= bauzeit + bind_m_ges)
                zus_ertrag[j] = r2(zu * mon / bind_m_ges)
                done += zus_ertrag[j]
            zus_ertrag[n] += (zu - rueck) - done
    g_v = verl - buchwert - (rueck if ma031 != 'verteilt' else D(0))
    R['g_v'] = g_v

    # ---- Finanzplan (R-4.3)
    hp, kp = psatz(H['h'], p), psatz(H['k'], p)
    stz = Steuer(c)
    G = KKt = D(0)
    linie = H['linie']
    nach = list(Zr)
    steuer_u = list(Zr)
    hz_u, kz_u = list(Zr), list(Zr)
    G_u, KK_u = list(Zr), list(Zr)
    acc = dict(miete=D(0), bew=D(0), erb=D(0), erh=D(0), zins=D(0), kkz=D(0), beitr=D(0), bz=D(0), hz=D(0))
    jahr = []
    zeilen = []
    for u in range(0, N + 1):
        orig = -inv[u] + miete[u] - bew[u] - erb[u] - erh[u] + zus_fl[u]
        if u == N:
            orig += verl - rueck
        dl = D(0)
        zins_u = beitr_u = bz_u = tilg_u = abl_u = D(0)
        for t in tr:
            s = t.s
            dl += s['ausz'][u] - s['einb'][u] - s['zins'][u] - s['tilg'][u] - s['beitr'][u] - s['bz'][u] - s['abl'][u]
            zins_u += s['zins'][u]
            beitr_u += s['beitr'][u]
            bz_u += s['bz'][u]
            tilg_u += s['tilg'][u]
            abl_u += s['abl'][u]
        dl -= zus_entg[u]
        hz = kz = D(0)
        if u >= 1:
            hz = r2(G * hp)
            kz = r2(KKt * kp)
        v = vfe if u == N else D(0)
        acc['miete'] += miete[u]
        acc['bew'] += bew[u]
        acc['erb'] += erb[u]
        acc['erh'] += erh[u]
        acc['zins'] += zins_u
        acc['kkz'] += kz
        acc['beitr'] += beitr_u
        acc['bz'] += bz_u
        acc['hz'] += hz
        tax = D(0)
        if u >= 1 and u % p == 0:
            j = u // p
            letzt = u == N
            entg = acc['zins'] + acc['kkz'] + acc['beitr'] + acc['bz'] + einb_abz[j]
            e_op = acc['miete'] - acc['bew'] - acc['erb'] - acc['erh'] - afa[j] - entg + zus_ertrag[j]
            gv = g_v if letzt else D(0)
            if letzt and c['status'] != 'privat':
                e_op -= vfe
                entg += vfe
            if letzt:
                st_ohne = copy.deepcopy(stz)
                tax_ohne = st_ohne.jahr(j, e_op, acc['hz'], D(0), entg, acc['erb'], D(0), True)
            tax = stz.jahr(j, e_op, acc['hz'], gv, entg, acc['erb'], vfe if letzt else D(0), letzt)
            if letzt:
                R['steuer_verkauf'] = tax - tax_ohne
            jahr.append(dict(j=j, e_op=e_op, z_h=acc['hz'], entg=entg, tax=tax, miete=acc['miete'],
                             bew=acc['bew'] + acc['erb'], zins=acc['zins'], beitr=acc['beitr'], bz=acc['bz'],
                             vv_e=stz.vv_e, vv_g=stz.vv_g, kkz=acc['kkz']))
            for kk in acc:
                acc[kk] = D(0)
        steuer_u[u] = tax
        saldo = orig + dl + hz - kz - v - tax + einl[u]
        netto = G - KKt + saldo
        if netto >= 0:
            G, KKt = netto, D(0)
        else:
            G = D(0)
            fehl = -netto
            if linie is None:
                KKt = fehl
            else:
                KKt = min(fehl, linie)
                nach[u] = fehl - KKt
        hz_u[u], kz_u[u], G_u[u], KK_u[u] = hz, kz, G, KKt
        if detail:
            zeilen.append(dict(u=u, orig=orig, zins=zins_u, tilg=tilg_u, beitr=beitr_u, bz=bz_u, abl=abl_u, hz=hz,
                               kz=kz, tax=tax, einl=einl[u], nach=nach[u], G=G, KK=KKt, miete=miete[u], bew=bew[u],
                               soll=soll[u]))
    EW = G - KKt
    R.update(st_log=stz.log, EW=EW, jahr=jahr, zeilen=zeilen, nach=nach, einl=einl, tr=tr, steuer_u=steuer_u, soll=soll, miete=miete,
             bew=bew, qm=qm, m0=m0, teile=teile, zus_fl=zus_fl, bauzeit=bauzeit, N=N)

    # ---- Kennzahlen
    e = [einl[u] + nach[u] for u in range(N + 1)]
    a = [D(0)] * (N + 1)
    EWU = alternative(c, N, p, e, a)
    f = {}
    for j in range(1, n + 1):
        f[j] = r12((1 + H['h'] * (1 - stz.s_z(j))) ** (D(1) / D(p)))
    w = [D(1)] * (N + 1)
    for t in range(N - 1, -1, -1):
        w[t] = w[t + 1] * f[t // p + 1]
    Zz = EW + sum((a[u] * w[u] for u in range(N + 1)), D(0))
    Dn = sum((e[u] * w[u] / w[0] for u in range(N + 1) if e[u]), D(0))
    ZU = EWU
    nn = D(n)

    def rend(z_, d_):
        if d_ == 0:
            return None
        if z_ <= 0:
            return D(-1)
        return (z_ / d_) ** (1 / nn) - 1
    r = rend(Zz, Dn)
    rU = rend(ZU, Dn)
    EU = Zz - Dn * (1 + H['z']) ** n
    inv_ende = bauzeit if nb else 0
    ek_inv = sum(e[0:inv_ende + 1], D(0))
    nach_lfd = sum(nach[inv_ende + 1:N], D(0))
    fehl_vk = nach[N]
    if r == D(-1):
        R['meld'].add('M-29')
    if r is None:
        R['meld'].add('M-28')
    if fehl_vk > 0:
        R['meld'].add('M-42')
    R.update(EWU=EWU, dEW=EW - EWU, r=r, rU=rU, EU=EU, Z=Zz, Dn=Dn, w=w, ek_inv=ek_inv, nach_lfd=nach_lfd,
             fehl_vk=fehl_vk, ek_ges=ek_inv + nach_lfd + fehl_vk, e=e)

    # Deckungen je Planjahr
    deck = {}
    for jd in jahr:
        j = jd['j']
        re_ = jd['miete'] - jd['bew']
        tilg_j = sum((t.s['tilg'][u] for t in tr for u in range((j - 1) * p + 1, j * p + 1)), D(0))
        kd = jd['zins'] + jd['beitr'] + tilg_j
        deck[j] = (re_ / kd if kd else None, re_, kd)
    R['deck'] = deck
    # erstes Jahr der Vollvermietung
    kd_vj = sum((t.s['zins'][u] + t.s['tilg'][u] + t.s['beitr'][u] for t in tr for u in vj_per), D(0))
    zi_vj = sum((t.s['zins'][u] + t.s['beitr'][u] for t in tr for u in vj_per), D(0))
    R['kd_vj'] = kd_vj
    R['deck_vj'] = re_vj / kd_vj if kd_vj else None
    R['zinsdeck_vj'] = re_vj / zi_vj if zi_vj else None
    R['kd_je'] = {t.name: sum((t.s['zins'][u] + t.s['tilg'][u] + t.s['beitr'][u] for u in vj_per), D(0)) for t in tr}
    erstes_voll = (m0 - 1 + 11) // 12 + 1 if nb else 1   # erstes Planjahr ganz in der Vermietung
    if nb:
        erstes_voll = (m0 - 1 + 11) // 12 + 1
    kl = [(deck[j][0], j) for j in deck if j >= erstes_voll and deck[j][0] is not None]
    if kl:
        R['deck_min'] = min(kl)
        if R['deck_min'][0] < H['mu']:
            R['meld'].add('M-38')
        if R['deck_min'][0] < 1:
            R['meld'].add('M-39')
    # Gesamtkapitalrendite (R-10.11)
    a0 = sum((inv[u] * w[u] / w[0] for u in range(0, inv_ende + 1)), D(0))
    ZS = D(0)
    for jd in jahr:
        ZS += jd['zins'] * (1 - stz.s_z(jd['j']))     # s_FK = s_op (Vortrag); Koerperschaft ohne Kennzeichen
    R['a0'] = a0
    R['g'] = ((Zz - Dn + ZS + a0) / a0) ** (1 / nn) - 1 if a0 > 0 and (Zz - Dn + ZS + a0) > 0 else None
    # Faktoren
    u0 = (m0 - 1) // mp + 1
    mj1 = mjm(u0) if p == 12 else None
    R['mjm_1'] = mj1
    R['restwertbeitrag'] = verl - sum((t.s['abl'][N] for t in tr), D(0)) - vfe - rueck - R.get('steuer_verkauf', D(0))
    R['darl_quote'] = (L + U_sum) / W
    R['meld'].add('M-37')
    return R


def ziel_eu(c, P, stress=False):
    """Endwertueberschuss beim Preis P (Stress mit L_Basis(P))."""
    cc = copy.copy(c)
    cc['preis'] = D(P)
    if stress:
        return rechne(cc, stress=True, basis=rechne(cc, detail=False), detail=False)
    return rechne(cc, detail=False)


def preissuche(c, stress=False, krit=None, verbose=False):
    """R-11.5. krit(R) -> bool (Ziel erreicht)."""
    H = c['H']
    if krit is None:
        krit = lambda R: R['EU'] >= 0
    cache = {}

    def ok(P):
        if P not in cache:
            try:
                cache[P] = krit(ziel_eu(c, P, stress))
            except M22:
                cache[P] = None
        return cache[P]
    base = rechne(c, detail=False)
    O = int(r2(H['such_ober'] * max(base['mjm_1'], base['mjm_N'])).to_integral_value(rounding=ROUND_HALF_UP))
    U = 1
    if ok(U) is None:
        lo, hi = 1, O
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if ok(mid) is None:
                lo = mid
            else:
                hi = mid
        U = hi
    if not ok(U):
        return dict(P=None, meld='M-32', U=U, O=O)
    nst = H['raster']
    st = [U + (O + 1 - U) * i // nst for i in range(nst + 1)]
    lo = hi = None
    for i in range(nst):
        if ok(st[i]) and not ok(st[i + 1]):
            lo, hi = st[i], st[i + 1]
            break
    if lo is None:
        return dict(P=None, meld='M-33', U=U, O=O)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    g = lo
    F = H['fenster']
    meld = None
    while True:
        bad = [q for q in range(max(U, g - F), g) if not ok(q)]
        if not bad:
            break
        g = min(bad) - 1
        meld = 'M-34'
    if any(ok(q) for q in range(g + 2, g + F + 1)):
        meld = 'M-34'
    return dict(P=g, meld=meld, U=U, O=O, n_eval=len(cache))


def fmt(x, nd=2):
    if x is None:
        return 'n.d.'
    q = D(1).scaleb(-nd)
    s = f"{D(x).quantize(q, rounding=ROUND_HALF_UP):,}"
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')


def pct(x, nd=3):
    return 'n.d.' if x is None else fmt(D(x) * 100, nd) + ' %'
