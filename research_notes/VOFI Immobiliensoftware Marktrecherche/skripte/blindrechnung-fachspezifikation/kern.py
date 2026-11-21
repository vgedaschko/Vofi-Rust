# -*- coding: utf-8 -*-
"""Blindrechnung: Nachbau der Grobkalkulation allein aus docs/fachspezifikation-rechenkern.md
(Stand 2026-11-21, Teil 1 eingefroren). Nur Standardbibliothek, decimal.
Kein Blick in den Referenzrechner. Der Stand nach Pruefrunde 1 liegt in stand-runde2/."""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP, ROUND_FLOOR, ROUND_CEILING
import copy

getcontext().prec = 60
CENT = D('0.01')
E12 = D('1e-12')


RUNDEN = [True]      # Rundungsmodus "Cent"; [False] = Modus "keine" (R-12.2), nur fuer den Testfall im Jahresmodus


def r2(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP) if RUNDEN[0] else D(x)


def r12(x):
    return D(x).quantize(E12, rounding=ROUND_HALF_UP)


def floor2(x):
    return D(x).quantize(CENT, rounding=ROUND_FLOOR)


def ceil_int(x):
    return int(D(x).to_integral_value(rounding=ROUND_CEILING))


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


def annuitaet(K, ip, m):
    """Laufzeitannuitaet R-5.4"""
    if ip == 0:
        return r2(K / m)
    q = (1 + ip) ** m
    return r2(K * ip * q / (q - 1))


# ---------------------------------------------------------------- Vorgaben / Katalog (Anhang A.4)
def haus():
    return dict(
        z=D('0.05'), z_foerder=None, beta=D('0.65'), mu=D('1.2'), mindtilg=D('0.02'), anschl_auf=D('0.01'),
        # H-06, acht Groessen
        st_anschl=D('0.01'), st_zins=D('0.005'), st_leer=D('0.02'), st_miete=D('0.005'),
        st_vf=D('0.10'), st_stau=D('0.10'), st_bk=D('0.05'), st_bz=3,
        h=D('0.02'), aL=None, k=D('0.08'), linie=D(0),
        miet=D('0.02'), kost=D('0.02'), bau=D('0.03'), leer=D('0.015'), vk=D('0.015'),
        verw=D(350), inst=[(0, D('9.00')), (22, D('11.50')), (32, D('14.00'))], bk=D(2),
        vfe=D('0.01'), such_ober=D(100), raster=40, fenster=20, miet_ober=D(100),
        e42=D('0.42'), d=4, zb=10, h25=None, flukt=D(0), ford=D('0.005'), anlauf=3,
        co2preis=D(50), co2steig=D('0.05'), zus1=D('0.05'), zus2=D('0.20'), stp=D(20000),
        bz_satz=D('0.0025'), bz_frei=6,
        h32=None, h33=None, anlauf_nb=3, vorlauf=0, h37=(D('0.5'), D('0.75')),
        h38='vortrag', h39=D('0.25'),
    )


def katalog():
    return dict(
        kst={2027: D('0.15'), 2028: D('0.14'), 2029: D('0.13'), 2030: D('0.12'), 2031: D('0.11')},
        kst_ab=D('0.10'), kst_bis=D('0.15'), zus=D('0.055'),
        messzahl=D('0.035'), abr=D(100), fb=D(24500), hebesatz=D(4),
        anrf=D(4), frist=10, afa_ankauf=D('0.02'), afa_neubau=D('0.03'),
        warte=15, kappung=D('0.15'), kappung_ohne=D('0.20'), kap_T=36, bremse=True, bremse_auf=D('0.10'),
        co2_anteil=D('0.40'),
        f_darl=D('0.60'), f_zus=D('0.20'), f_ek=D('0.20'), f_grenze=D(5460), f_miete=D('8.20'),
        f_steig=D('0.0615'), f_fest=3, f_schritt=3, f_bindung=35, f_beitrag=D('0.005'),
        f_entg_d=D('0.01'), f_entg_z=D('0.0075'), f_tilg_j=42, f_zinslos=35, f_zins_danach=D('0.05'),
        f_frist=24, f_teil=(D('0.3'), D('0.3'), D('0.3'), D('0.1')), f_mindtilg=D('0.01'),
        g_steig=D('0.0615'), g_fest=3, g_schritt=3,
        anh_quote=D('0.15'), anh_jahre=3, ust=D('0.19'),
        kuend_sperr=120, kuend_frist=6, bank_mind=D('0.15'),
        kfw_max=D(100000), kfw_max_siegel=D(150000), kfw_var={10: (1, 2), 25: (1, 3), 35: (1, 5)},
        kfw_zins=D('0.025'), kfw_zb=10, kfw_bp=D('0.0015'), kfw_bp_frei=12, kfw_abruf=12, kfw_abruf_verl=24,
        hz_anteil=D('0.25'), hz_fb=D(200000), hz_pacht=D('0.5'),
        sockel=D(1000000), kap=D('0.26375'), kat19=5,
    )


def ankauf():
    return dict(
        art='ankauf', startjahr=2027, p=12, preis=D(2400000), enk=D('0.10'), boden=D('0.25'),
        baujahr=1990, wfl=D(1320), einh=20, ist=D('8.50'), vm=D('9.20'), markt=D('10.50'),
        leerfl=D(0), sonst=D(0), co2=D(30), historie=None, im_kappgebiet=True, im_bremsgebiet=True,
        status='koerp', kennz=False, e69=False,
        zins=D('0.04'), zb=10, tilg=D('0.02'), vf=D(18), n=12,
        stau=D(120000), stau_jahr=2,
        geb=D(0), geb_ende=None, geb_miete=None, uebern=None, ek_verf=None,
        erbbau=D(0), anteil=D(1),
        ma026_3=False, ma026_4=False, ma031='verteilt', ma036_alt=False, ma038_alt=False,
        H=haus(), K=katalog(), foerder=False, kfw=D(0),
    )


def neubau():
    return dict(
        art='neubau', startjahr=2027, p=12, preis=D(1200000), enk=D('0.08'), gfl=D(2500),
        brw=D(400), wfl=D(2000), einh=30, bgf=D(2600), kkw=D(2320), kkw_gesamt=False, bauzeit=18,
        vorlauf=None, festpreis=False, vorverm=False, markt=D('16.50'), e65=None,
        stp=0, stp_miete=D(0), co2=D(0), kfw=D(0), kfw_T=35, kfw_f=1, kfw_zins=None, kfw_siegel=False,
        status='koerp', kennz=False, e69=False, e70=False,
        zins=D('0.04'), zb=10, tilg=D('0.02'), vf=D(24), n=15, foerder=False,
        stau=D(0), stau_jahr=1, erbbau=D(0), anteil=D(1), im_kappgebiet=True,
        ma026_3=False, ma026_4=False, ma031='verteilt', ma036_alt=False, ma038_alt=False,
        ek_verf=None, uebern=None, H=haus(), K=katalog(),
    )


def mit(c, **kw):
    """Kopie eines Auftrags mit Aenderungen; H_x aendert eine Vorgabe, K_x einen Katalogwert."""
    c = dict(c)
    c['H'] = dict(c['H'])
    c['K'] = dict(c['K'])
    for k, v in kw.items():
        if k.startswith('H_'):
            c['H'][k[2:]] = v
        elif k.startswith('K_'):
            c['K'][k[2:]] = v
        else:
            c[k] = v
    return c


# ---------------------------------------------------------------- Miete (R-6.3)
def pfad(N, start, anfang, ziel, bezug_vor, t_letzte, w, kap, T, sperre_bis=0, rueck=False):
    """Mietpfad je m2 und Monat fuer m = start..N, ungerundet.
    Zeile (1): m <= sperre_bis; Zeile (2) nur mit rueck; Zeile (3) Erhoehung; Zeile (4) sonst.
    bezug_vor(k): Miete fuer k < start oder None (keine Erhoehung, MA-037)."""
    miete = {start: anfang}
    for m in range(start + 1, N + 1):
        prev = miete[m - 1]
        neu = prev
        if m <= sperre_bis:
            pass
        else:
            z = ziel(m)
            if rueck and z < prev:
                neu = z
            elif z > prev and m - 1 >= t_letzte + w:
                k = m - T
                ref = miete[k] if k >= start else bezug_vor(k)
                if ref is not None:
                    cand = min(z, ref * (1 + kap))
                    if cand > prev:
                        neu = cand
                        t_letzte = m - 1
        miete[m] = neu
    return miete


def stufe(j, fest, schritt):
    return 0 if j <= fest else (j - fest - 1) // schritt + 1


# ---------------------------------------------------------------- Steuer (Kapitel 7)
BV = ('koerp', 'pg_gepr', 'pg_orig', 'einzel')          # Betriebsvermoegen
UEB = ('privat', 'verein')                              # Ueberschusseinkuenfte


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

    def s_z(self, j):
        """Grenzsteuersatz auf Zinsertraege (R-7.14)"""
        c, K = self.c, self.K
        st = c['status']
        g = K['messzahl'] * K['hebesatz']
        if st == 'koerp':
            return self.kst(j) * (1 + K['zus']) + g
        if st == 'verein':
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

    def s_fk(self, j):
        """Entlastungssatz der Sollzinsen (R-7.14); nur fuer die Gesamtkapitalrendite."""
        c, K = self.c, self.K
        st = c['status']
        g = K['messzahl'] * K['hebesatz']
        kennz = c.get('kennz') and st in ('koerp', 'pg_gepr')
        g_op = D(0) if kennz else g
        if st == 'koerp':
            s = self.kst(j) * (1 + K['zus']) + g_op
            if c['H'].get('h38') == 'sofort' and not kennz:
                s -= K['hz_anteil'] * g
            return s
        if st == 'verein':
            return self.kst(j) * (1 + K['zus'])
        if st in ('pg_gepr', 'pg_orig', 'einzel'):
            ant = D(1) if st == 'einzel' else c['anteil']
            a = ant * K['messzahl'] * min(K['anrf'], K['hebesatz'])
            a_op = D(0) if kennz else a
            return c['H']['e42'] + g_op - a_op
        if st == 'privat':
            return c['H']['e42']
        if st == 'befreit':
            return D(0)
        return c['lb_satz']

    def _vortrag(self, topf, x):
        vv = getattr(self, topf)
        if x < 0:
            setattr(self, topf, vv - x)
            return D(0)
        use = min(vv, x)
        setattr(self, topf, vv - use)
        return x - use

    def gewst(self, e_op, z_h, g_v, entg, erbbau, letztes):
        """R-7.8 mit R-7.6, R-7.16, R-7.18. Rueckgabe (Gewerbesteuer, Messbetrag, Gewerbeertrag)."""
        c, K = self.c, self.K
        st = c['status']
        sofort = c['H'].get('h38', 'vortrag') == 'sofort'
        personen = st in ('pg_gepr', 'pg_orig', 'einzel')
        linear = sofort and st in ('koerp', 'einzel')        # Personengesellschaft: GewSt immer mit Vortrag
        kennz = c.get('kennz') and not self.ua and st in ('koerp', 'pg_gepr')
        fb_hz = D(0) if linear else K['hz_fb']
        hinzu = K['hz_anteil'] * max(D(0), entg + K['hz_pacht'] * erbbau - fb_hz)
        gv = g_v
        if c.get('ma036_alt') and st in ('pg_gepr', 'pg_orig') and not self.ua:
            gv = (1 - c['anteil']) * g_v
        if kennz and not (letztes and not c.get('e69')):
            ge0 = z_h                                        # Kuerzung; mit E-69 auch der Verkaufsgewinn
        else:
            ge0 = e_op + z_h + gv + hinzu                    # ohne Kennzeichen; Verkaufsjahr ohne E-69
        if linear:
            ge = ge0
        else:
            ge = self._vortrag('vv_g', ge0)
            ge = (ge / K['abr']).to_integral_value(rounding=ROUND_FLOOR) * K['abr']
            if personen:
                ge = max(D(0), ge - K['fb'])
        if st == 'koerp':
            return r2(ge * K['messzahl'] * K['hebesatz']), ge * K['messzahl'], ge
        if linear:                                           # Einzelunternehmen, sofort
            return r2(K['messzahl'] * K['hebesatz'] * ge), K['messzahl'] * ge, ge
        mb = r2(ge * K['messzahl'])
        return r2(mb * K['hebesatz']), mb, ge

    def jahr(self, j, e_op, z_h, g_v, entg=D(0), erbbau=D(0), vfe=D(0), letztes=False):
        """Jahressteuer. Bei Privatperson und Verein/Stiftung enthaelt e_op die Vorfaelligkeit nicht."""
        c, K = self.c, self.K
        st = c['status']
        sofort = c['H'].get('h38', 'vortrag') == 'sofort'
        det = {}
        if st == 'befreit':
            t = D(0)
        elif st == 'koerp':
            eink = e_op + z_h + g_v
            satz = self.kst(j) * (1 + K['zus'])
            kst = r2(satz * eink) if sofort else r2(satz * self._vortrag('vv_e', eink))
            gst, mb, ge = self.gewst(e_op, z_h, g_v, entg, erbbau, letztes)
            t = kst + gst
            det = dict(kst=kst, gst=gst, ge=ge)
        elif st == 'verein':
            gvs = D(0)
            if letztes and c['n'] <= K['frist']:
                gvs = max(D(0), g_v - vfe)
            eink = e_op + z_h + gvs
            satz = self.kst(j) * (1 + K['zus'])
            t = r2(satz * eink) if sofort else r2(satz * self._vortrag('vv_e', eink))
            det = dict(kst=t, gvs=gvs)
        elif st in ('pg_gepr', 'pg_orig', 'einzel'):
            ant = D(1) if st == 'einzel' else c['anteil']
            gew = e_op + z_h + g_v
            e42 = c['H']['e42']
            est = r2(e42 * gew) if sofort else r2(e42 * self._vortrag('vv_e', gew))
            gst, mb, ge = self.gewst(e_op, z_h, g_v, entg, erbbau, letztes)
            if sofort and st == 'einzel':
                anr = r2(K['messzahl'] * min(K['anrf'], K['hebesatz']) * ge)
            elif sofort:
                anr = r2(min(ant * K['anrf'] * mb, ant * gst))
            else:
                anr = r2(min(ant * K['anrf'] * mb, ant * gst, ant * est))
            t = est + gst - anr
            det = dict(est=est, gst=gst, anr=anr, ge=ge)
        elif st == 'privat':
            e = e_op
            gvs = D(0)
            if letztes and c['n'] <= K['frist']:
                gvs = max(D(0), g_v - vfe)
                e = e + gvs
            e42 = c['H']['e42']
            tv = r2(e42 * e) if sofort else r2(e42 * self._vortrag('vv_e', e))
            tz = r2(K['kap'] * z_h)
            t = tv + tz
            det = dict(tv=tv, tz=tz, gvs=gvs)
        elif st == 'lehrbuch':
            gew = e_op + z_h + (g_v if c.get('lb_gv') else D(0))
            t = r2(c['lb_satz'] * gew) if sofort else r2(c['lb_satz'] * self._vortrag('vv_e', gew))
        else:
            raise ValueError(st)
        self.log.append(dict(j=j, e_op=e_op, z_h=z_h, g_v=g_v, t=t, det=det, vv_e=self.vv_e, vv_g=self.vv_g))
        return t


# ---------------------------------------------------------------- Darlehen (Kapitel 5)
class Tranche:
    """art: 'prozent' (Prozentannuitaet), 'laufzeit' (Laufzeitannuitaet), 'raten' (Ratentilgung)."""

    def __init__(self, name, nenn, art, zins, tilg=D(0), bezug=None, ausz=None, einb=D(0),
                 tilg_beginn=1, zb_ende=None, anschluss=None, regel='tilgungssatz', beitrag=D(0),
                 bz_satz=D(0), bz_frei=0, m=None, foerder=False, mindtilg=D(0), t_voll_fix=None):
        self.name, self.nenn, self.art, self.zins, self.tilg = name, nenn, art, zins, tilg
        self.bezug = nenn if bezug is None else bezug
        self.ausz = ausz or {0: nenn}
        self.einb = einb
        self.tilg_beginn, self.zb_ende, self.anschluss, self.regel = tilg_beginn, zb_ende, anschluss, regel
        self.beitrag, self.bz_satz, self.bz_frei, self.m = beitrag, bz_satz, bz_frei, m
        self.foerder, self.mindtilg, self.t_voll_fix = foerder, mindtilg, t_voll_fix
        self.m40 = False

    def satz(self, u):
        return self.zins if (self.zb_ende is None or u <= self.zb_ende) else self.anschluss

    def plan(self, N, p):
        Z = [D(0)] * (N + 1)
        s = dict(ausz=list(Z), einb=list(Z), zins=list(Z), tilg=list(Z), beitr=list(Z), bz=list(Z),
                 abl=list(Z), rest=list(Z))
        rest = D(0)
        cum = D(0)
        first = min(self.ausz)
        rate = None
        lz_rest = None              # verbleibende Perioden einer Laufzeitannuitaet (auch 'Restlaufzeit bleibt')
        self.rate_first = None
        self.kd_first = None
        rate_r = r2(self.nenn / self.m) if self.art == 'raten' else None
        for u in range(0, N + 1):
            zins = beitr = bz = tilg = D(0)
            if u >= 1:
                satz = self.satz(u)
                zins = r2(rest * satz / p)
                beitr = r2(rest * self.beitrag / p)
                if self.bz_satz and u > self.bz_frei and cum < self.nenn:
                    bz = r2((self.nenn - cum) * self.bz_satz * 12 / p)
                if u >= self.tilg_beginn:
                    nach_bindung = self.zb_ende is not None and u > self.zb_ende
                    if self.art == 'prozent':
                        if u == self.tilg_beginn:
                            # R-5.10: erste Rate mit dem Zins der Periode des Tilgungsbeginns
                            tau = max(self.tilg, self.mindtilg) if nach_bindung else self.tilg
                            rate = r2(self.bezug * (satz + tau) / p)
                        elif self.zb_ende is not None and u == self.zb_ende + 1:
                            regel = self.regel
                            if regel == 'restlaufzeit':
                                ip_alt = self.zins / p
                                R_, S = rate, rest
                                if R_ <= r2(S * ip_alt):
                                    regel = 'tilgungssatz'
                                    self.m40 = True
                                else:
                                    if ip_alt == 0:
                                        mm = int(S / R_)
                                    else:
                                        mm = int((R_ / (R_ - S * ip_alt)).ln() / (1 + ip_alt).ln())
                                    mm = max(1, mm)
                                    rate = annuitaet(S, self.anschluss / p, mm)
                                    lz_rest = mm
                            if regel == 'tilgungssatz':
                                rate = r2(rest * (self.anschluss + max(self.tilg, self.mindtilg)) / p)
                            elif regel == 'rate':
                                rate = max(rate, zins)
                        tilg = min(rest, max(D(0), rate - zins))
                        if lz_rest is not None:
                            lz_rest -= 1
                            if lz_rest <= 0:
                                tilg = rest
                    elif self.art == 'laufzeit':
                        k = u - self.tilg_beginn + 1
                        if u == self.tilg_beginn:
                            rate = annuitaet(self.nenn, satz / p, self.m)
                        elif self.zb_ende is not None and u == self.zb_ende + 1:
                            rate = annuitaet(rest, satz / p, self.m - (k - 1))
                        tilg = rest if k >= self.m else min(rest, max(D(0), rate - zins))
                    elif self.art == 'raten':
                        k = u - self.tilg_beginn + 1
                        tilg = rest if k >= self.m else min(rest, rate_r)
                    if u == self.tilg_beginn:
                        self.rate_first = rate if rate is not None else rate_r
                        self.kd_first = zins + tilg + beitr
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
        self.first = first
        self.t_voll = max(self.ausz) if self.t_voll_fix is None else self.t_voll_fix
        return s

    def kd(self, u):
        return self.s['zins'][u] + self.s['tilg'][u] + self.s['beitr'][u]


# ---------------------------------------------------------------- Unterlassensalternative (Kapitel 9)
def alternative(c, N, p, e, a):
    H = c['H']
    aL = H['h'] if H.get('aL') is None else H['aL']
    aLp, hp, kp = psatz(aL, p), psatz(H['h'], p), psatz(H['k'], p)
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


# ---------------------------------------------------------------- Grobkalkulation (Kapitel 11)
class Meldung(Exception):
    def __init__(self, kennung, text=''):
        super().__init__(kennung + ' ' + text)
        self.kennung = kennung
        self.text = text


def rechne(c0, stress=False, detail=True, nur_bemessung=False, bem_zins=None):
    """Ein Lauf der Grobkalkulation. stress=True: kombinierter Stressfall (R-11.8); das Bankdarlehen
    wird dann mit dem erhoehten Zins und sonst den Annahmen des Basisfalls neu bemessen.
    nur_bemessung / bem_zins dienen dieser Neubemessung."""
    c = copy.copy(c0)
    H = dict(c['H'])
    K = c['K']
    p = c['p']
    n = c['n']
    N = n * p
    nb = c['art'] == 'neubau'
    R = dict(meld=set())
    foerder = bool(c.get('foerder'))
    status = c['status']
    if nb and p != 12:
        raise Meldung('M-20', 'Neubau nur im Monatsraster')

    # ---- Stress (R-11.8), acht Groessen
    zins = c['zins']
    leer = H['leer']
    miet = H['miet']
    vf = c['vf']
    stau = c['stau']
    bk_fakt = D(1)
    bauzeit = c.get('bauzeit', 0) if nb else 0
    st_anschl = D(0)
    basis = None
    if stress:
        basis = rechne(c0, nur_bemessung=True, bem_zins=c['zins'] + H['st_zins'])
        zins = zins + H['st_zins']
        st_anschl = H['st_anschl']
        leer = min(D(1), leer + H['st_leer'])
        miet = miet - H['st_miete']
        vf = vf * (1 - H['st_vf'])
        stau = stau * (1 + H['st_stau'])
        if nb:
            bk_fakt = 1 + H['st_bk']
            bauzeit += H['st_bz']
    zins_bem = zins if bem_zins is None else bem_zins          # E-45 der Bemessung
    anschluss_bank = zins + H['anschl_auf'] + st_anschl        # R-5.8, im Stressfall R-11.8
    ausfall = leer + H['ford']
    vorlauf = 0
    if nb:
        vorlauf = H['vorlauf'] if c.get('vorlauf') is None else c['vorlauf']
        if n * 12 < vorlauf + c['bauzeit'] + H['st_bz'] + (0 if c.get('vorverm') else H['anlauf_nb']) + 12:
            raise Meldung('M-23')
    bauende = vorlauf + bauzeit
    anlauf_nb = 0 if c.get('vorverm') else H['anlauf_nb']

    nj = n + 3
    iM = index_reihe(miet, nj)
    iK = index_reihe(H['kost'], nj)
    iC = index_reihe(H['co2steig'], nj)
    wfl = c['wfl']
    kap = K['kappung'] if c.get('im_kappgebiet', True) else K['kappung_ohne']
    w_, T_ = K['warte'], K['kap_T']
    d = H['d']

    def pj(m):
        return (m - 1) // 12 + 1

    NM = n * 12
    # ---- Mieten je Teilflaeche (Monatswerte, ungerundet)
    teile = []                       # (Flaeche, {m: Miete}); ein Monat ohne Eintrag traegt keine Miete
    sonst = {m: D(0) for m in range(1, NM + 1)}
    if not nb:
        m0 = 1
        vmj = lambda m: c['vm'] * iM[pj(m)]
        nachh = vmj
        marktj = lambda m: c['markt'] * iM[pj(m)]

        def nvm(m):                  # Neuvermietungsmiete R-6.13
            x = marktj(m)
            if K['bremse'] and c.get('im_bremsgebiet', True):
                x = min(x, vmj(m) * (1 + K['bremse_auf']))
            return x

        def neu_vermietet(start):    # bestehendes Mietverhaeltnis ab start, nur Zeile (3), Ziel Vergleichsmiete
            anf = nvm(start)
            return pfad(NM, start, anf, vmj, lambda k: anf, start - 1, w_, kap, T_)
        fl_verm = wfl - c['leerfl']
        fl_geb = fl_verm * c['geb']
        fl_frei = fl_verm - fl_geb
        ist = c['ist']
        if fl_frei > 0:
            def ziel(m):
                j = pj(m)
                if j == 1:
                    return ist
                if d == 0 or j - 1 >= d:
                    return vmj(m)
                return ist + (vmj(m) - ist) * (j - 1) / d
            hist = c.get('historie')
            if hist is None:         # MA-037: letzte Erhoehung zum Stichtag, Kappung ausgeschoepft
                bez = lambda k: None
                tl = 0
            else:
                a_mon, m_alt = hist
                bez = lambda k: ist if k > -a_mon else m_alt
                tl = -a_mon
            frei = pfad(NM, 1, ist, ziel, bez, tl, w_, kap, T_, sperre_bis=12, rueck=not c.get('ma038_alt'))
            # Fluktuation R-6.14: je Planjahr ab dem zweiten wechselt der Anteil H-26 des Restbestands
            rest_fl = fl_frei
            if H['flukt'] > 0:
                for j in range(2, n + 1):
                    ab = rest_fl * H['flukt']
                    s_ = (j - 1) * 12 + 1
                    teile.append((ab, {m: frei[m] for m in range(1, s_)}))
                    teile.append((ab, neu_vermietet(s_)))
                    rest_fl -= ab
            teile.append((rest_fl, frei))
        if fl_geb > 0:
            b = c['geb_ende']        # Planjahr des letzten Bindungsmonats (R-6.6)
            A0 = c['geb_miete']
            gm = {}
            last_step = 0
            prev = None
            ende_fest = min(NM, (b + 1) * 12)
            for m in range(1, ende_fest + 1):
                j = pj(m)
                if j <= b:
                    val = min(A0 * (1 + K['g_steig']) ** stufe(j, K['g_fest'], K['g_schritt']), vmj(m))
                else:
                    val = gm[b * 12]
                if prev is not None and val != prev:
                    last_step = m - 1
                gm[m] = val
                prev = val
            if NM > ende_fest:
                aus = gm[ende_fest]

                def zielg(m):
                    k = pj(m) - (b + 1)
                    if d == 0 or k >= d:
                        return vmj(m)
                    return aus + (vmj(m) - aus) * k / d
                fest = dict(gm)
                rest = pfad(NM, ende_fest, aus, zielg, lambda k: fest[k] if k >= 1 else None,
                            last_step, w_, kap, T_)
                gm.update(rest)
            teile.append((fl_geb, gm))
        if c['leerfl'] > 0:
            teile.append((c['leerfl'], neu_vermietet(H['anlauf'] + 1)))
        for m in range(1, NM + 1):
            sonst[m] = c['sonst'] * iM[pj(m)] / 12
    else:
        bezug = bauende + 1
        m0 = bauende + anlauf_nb + 1
        vj = lambda m: (m - m0) // 12 + 1          # Vermietungsjahr
        vmj = lambda m: c['markt'] * iM[vj(m)]
        e65 = c['markt'] if c.get('e65') is None else c['e65']
        nachh = lambda m: e65 * iM[vj(m)]
        if not foerder:
            anf = c['markt']
            mi = pfad(NM, m0, anf, vmj, lambda k: anf, m0 - 1, w_, kap, T_)
        else:
            bjahr = lambda m: (m - bezug) // 12 + 1          # Bindungsjahr ab Bezugsfertigkeit
            Bj = K['f_bindung']
            bind_ende = bauende + Bj * 12                    # letzter Monat der Bindung
            b_pj = pj(bind_ende)                             # Planjahr b
            ende_fest = min(NM, (b_pj + 1) * 12)
            gm = {}
            prev = None
            last_step = m0 - 1
            for m in range(bezug, ende_fest + 1):
                if m <= bind_ende:
                    val = min(K['f_miete'] * (1 + K['f_steig']) ** stufe(bjahr(m), K['f_fest'], K['f_schritt']),
                              vmj(m) if m >= m0 else K['f_miete'] * D(1000))
                else:
                    val = gm[bind_ende]
                if prev is not None and val != prev:
                    last_step = m - 1
                gm[m] = val
                prev = val
            if NM > ende_fest:
                aus = gm[ende_fest]

                def zielg(m):
                    k = pj(m) - (b_pj + 1)
                    if d == 0 or k >= d:
                        return vmj(m)
                    return aus + (vmj(m) - aus) * k / d
                fest = dict(gm)
                rest = pfad(NM, ende_fest, aus, zielg, lambda k: fest[k] if k >= m0 else K['f_miete'],
                            last_step, w_, kap, T_)
                gm.update(rest)
            mi = {m: gm[m] for m in range(m0, NM + 1)}
        teile.append((wfl, mi))
        for m in range(m0, NM + 1):
            sonst[m] = D(c['stp']) * c['stp_miete'] * iM[vj(m)]

    def summe_m(m, nachhaltig=False):
        x = D(0)
        for fl, mi_ in teile:
            v = mi_.get(m)
            if v is None:
                continue
            x += fl * (min(v, nachh(m)) if nachhaltig else v)
        return x + sonst[m]

    def qm(m):
        return (summe_m(m) - sonst[m]) / wfl

    soll_m = {m: r2(summe_m(m)) for m in range(1, NM + 1)}

    # ---- Bewirtschaftung, CO2, Erbbauzins
    # nur zur Ursachensuche (Altstand mit neun Stressgroessen, V-22): H['st_inst'] ist im Auftrag nicht gesetzt
    inst_fakt = 1 + H.get('st_inst', D(0)) if stress else D(1)

    def inst_satz(alter):
        s = None
        for ab, v in H['inst']:
            if alter >= ab:
                s = v
        return s * inst_fakt

    def bew_jahr(j, alter):
        return (H['verw'] * c['einh'] + inst_satz(alter) * wfl + H['bk'] * wfl) * iK[j]

    def co2_jahr(j):
        return c['co2'] * wfl * K['co2_anteil'] * H['co2preis'] * iC[j] / 1000

    mp = 12 // p

    def monate(u):
        return range((u - 1) * mp + 1, u * mp + 1)
    Zr = [D(0)] * (N + 1)
    soll, miete, bew, erb = list(Zr), list(Zr), list(Zr), list(Zr)
    bezug_m = bauende + 1 if nb else 1
    for u in range(1, N + 1):
        j = (u - 1) // p + 1
        if p == 12:
            soll[u] = soll_m[u]
            if u >= bezug_m:
                alter = (u - bezug_m) // 12 if nb else c['startjahr'] + j - 1 - c['baujahr']
                bew[u] = r2(bew_jahr(j, alter) / 12) + r2(co2_jahr(j) / 12)
            erb[u] = r2(c['erbbau'] * iK[j] / 12)
        else:
            soll[u] = r2(sum((summe_m(m) for m in monate(u)), D(0)))      # R-2.2, R-6.4
            alter = c['startjahr'] + j - 1 - c['baujahr']
            bew[u] = r2(bew_jahr(j, alter)) + r2(co2_jahr(j))
            erb[u] = r2(c['erbbau'] * iK[j])
        miete[u] = max(D(0), r2(soll[u] * (1 - ausfall)))

    # ---- Bemessung (R-11.2)
    preis = c['preis']
    enk = r2(preis * c['enk'])
    inv = list(Zr)
    erh = list(Zr)
    bau_raten = {}
    if nb:
        zuschlag = D(0) if c.get('kkw_gesamt') else H['zus1'] + H['zus2']
        bk0 = r2(c['bgf'] * c['kkw'] * (1 + zuschlag) * bk_fakt) + r2(D(c['stp']) * H['stp'] * bk_fakt)
        for m in range(1, bauzeit + 1):
            f = D(1) if c.get('festpreis') else r12((1 + H['bau']) ** (D(vorlauf + m) / D(12)))
            bau_raten[vorlauf + m] = r2(bk0 / bauzeit * f)
        baukosten = sum(bau_raten.values(), D(0))
        gesamt = preis + enk + baukosten
        inv[0] = preis + enk
        for m, v in bau_raten.items():
            inv[m] += v
        R.update(bk0=bk0, baukosten=baukosten, raten=bau_raten)
        boden_w = preis + enk
        afa_grund = baukosten
        afa_satz = K['afa_neubau']
        W = gesamt
    else:
        baukosten = D(0)
        gesamt = preis + enk
        inv[0] = preis + enk
        bod = c['boden'] if status in UEB else H['h39']
        boden_w = r2((preis + enk) * bod)
        afa_grund = preis + enk - boden_w
        afa_satz = K['afa_ankauf']
        W = preis
    R['gesamt'] = gesamt

    # Investitionsstau (R-6.10, R-6.16, R-8.4)
    stau_zahl = D(0)
    stau_abzug = D(0)
    akt_massn = {}     # Jahr der Ausfuehrung k -> aktivierter Betrag
    stau0 = D(0)
    if stau > 0:
        k = c['stau_jahr']
        if k > n:
            stau_abzug = r2(stau * (1 + H['bau']) ** n)
        else:
            stau_zahl = r2(stau * (1 + H['bau']) ** k)
            u_st = k * p
            aktiv = False
            if k <= K['anh_jahre'] and not nb:
                if stau_zahl / (1 + K['ust']) > K['anh_quote'] * afa_grund:
                    aktiv = True
                    R['meld'].add('M-36')
            if aktiv:
                inv[u_st] += stau_zahl
                akt_massn[k] = stau_zahl
            else:
                erh[u_st] += stau_zahl
            if k == 0:
                stau0 = stau_zahl
    R['stau_zahl'] = stau_zahl

    # Foerderung (R-11.14); im Stressfall auf dem Stand des Basisfalls
    fd = zu = mind_ek = entg_d = entg_z = D(0)
    if foerder:
        if basis is not None:
            fd, zu, mind_ek, entg_d, entg_z = (basis[k_] for k_ in ('fd', 'zu', 'mind_ek', 'entg_d', 'entg_z'))
            zk = basis['zk']
        else:
            zk_bau = min(baukosten, K['f_grenze'] * wfl)
            zk_gr = min(preis + enk, c['brw'] * c['gfl'])
            zk = zk_bau + zk_gr
            fd = r2(K['f_darl'] * zk)
            zu = r2(K['f_zus'] * zk)
            mind_ek = r2(K['f_ek'] * zk)
            entg_d = r2(fd * K['f_entg_d'])
            entg_z = r2(zu * K['f_entg_z'])
        R.update(zk=zk, fd=fd, zu=zu, mind_ek=mind_ek, entg=entg_d + entg_z, entg_d=entg_d, entg_z=entg_z)
    Mbed = preis + enk + baukosten + stau0 + entg_d + entg_z
    R['M'] = Mbed

    # ---- nachhaltiger Reinertrag (R-5.12) und Reinertrag im ersten Jahr der Vollvermietung (R-6.12)
    u0 = (m0 - 1) // mp + 1
    vj_per = range(u0, u0 + p)
    roh_u, einz_u = [], []
    for u in vj_per:
        x = r2(sum((summe_m(m, nachhaltig=True) for m in monate(u)), D(0)))
        roh_u.append(x)
        einz_u.append(max(D(0), r2(x * (1 - H['leer'] - H['ford']))))
    roh_n = sum(roh_u, D(0))
    ausf_n = roh_n - sum(einz_u, D(0))
    bew_vj = sum((bew[u] for u in vj_per), D(0))
    erb_vj = sum((erb[u] for u in vj_per), D(0))
    miete_vj = sum((miete[u] for u in vj_per), D(0))
    soll_vj = sum((soll[u] for u in vj_per), D(0))
    re_vj = miete_vj - bew_vj - erb_vj
    h33 = K['bank_mind'] if H.get('h33') is None else H['h33']
    abzug = max(bew_vj + ausf_n, r2(h33 * roh_n))
    re_n = roh_n - abzug - erb_vj
    if c.get('ma026_3'):
        re_n = re_vj
    R.update(roh_n=roh_n, ausf_n=ausf_n, re_n=re_n, re_vj=re_vj, bew_vj=bew_vj, erb_vj=erb_vj,
             miete_vj=miete_vj, soll_vj=soll_vj)

    # ---- uebrige Darlehen zu Bemessungskonditionen (R-5.12)
    zb_bank = c['zb'] * p
    m_B = (c['zb'] if H.get('h32') is None else H['h32']) * p
    h25 = H.get('h25')
    mindtilg = H['mindtilg']
    mind_bank = max(mindtilg, K['f_mindtilg']) if foerder else mindtilg
    if foerder and c['tilg'] < K['f_mindtilg']:
        raise Meldung('M-20', 'E-64 unter der Mindesttilgung nach KAT-10')

    def bem_zins_tr(vertrag, zb_per, anschluss_tr):
        i_kalk = max(vertrag, anschluss_tr if h25 is None else h25)
        if c.get('ma026_4'):
            return r12(i_kalk)
        m_V = m_B if zb_per is None else min(m_B, zb_per)
        return r12((vertrag * m_V + i_kalk * (m_B - m_V)) / m_B)

    U_sum = U_B = KD_U = D(0)
    kd_bem = {}
    anschluss_bem = zins_bem + H['anschl_auf']            # Anschlusszins, der dem Bankdarlehen folgt (ohne Anschlussstress)
    if c.get('uebern'):
        ue = c['uebern']
        nenn_u = ue.get('nenn') or ue['rest']
        anschl_ue = ue.get('anschluss')
        if anschl_ue is None:
            anschl_ue_bem = anschluss_bem
        else:
            anschl_ue_bem = anschl_ue
        zb_u = None if ue.get('zb') is None else ue['zb'] * p
        iB = bem_zins_tr(ue['zins'], zb_u, anschl_ue_bem)
        rate_B = r2(nenn_u * (iB + max(ue['tilg'], mindtilg)) / p)
        kd = p * rate_B + p * r2(ue['rest'] * ue.get('beitrag', D(0)) / p)
        U_sum += ue['rest']
        U_B += ue['rest']
        KD_U += kd
        kd_bem['uebernommen'] = dict(iB=iB, kd=kd, rate=rate_B)
    kfw = c.get('kfw', D(0)) if nb else D(0)
    if kfw > 0:
        Tk, fk = c['kfw_T'], c['kfw_f']
        var = K['kfw_var'].get(Tk)
        hoechst = c['einh'] * (K['kfw_max_siegel'] if c.get('kfw_siegel') else K['kfw_max'])
        if var is None or not (var[0] <= fk <= var[1]) or kfw > hoechst:
            raise Meldung('M-20', 'KfW-Darlehen: Betrag oder Laufzeitvariante')
        kfw_zins = K['kfw_zins'] if c.get('kfw_zins') is None else c['kfw_zins']
        kfw_m = (Tk - fk) * 12
        iB = bem_zins_tr(kfw_zins, K['kfw_zb'] * p, anschluss_bem)
        rate_B = max(annuitaet(kfw, iB / p, kfw_m), r2(kfw * (iB + mindtilg) / p))
        kd = p * rate_B
        U_sum += kfw
        U_B += kfw
        KD_U += kd
        kd_bem['kfw'] = dict(iB=iB, kd=kd, rate=rate_B)

    # ---- Mittelabruf Teil 1: Termine der Foerdermittel (R-11.3, R-5.11)
    if foerder:
        a1, a2, a3, a4 = K['f_teil']
        bereit = [vorlauf + 1,
                  vorlauf + ceil_int(H['h37'][0] * bauzeit) + 1,
                  vorlauf + ceil_int(H['h37'][1] * bauzeit) + 1,
                  bauende + anlauf_nb + 1]
        ges_f = fd + zu
        ober = [r2(a1 * ges_f), r2((a1 + a2) * ges_f), r2((a1 + a2 + a3) * ges_f), ges_f]
        R.update(bereit=bereit, ober=ober)
        f_T = min(bereit[3] + 1, vorlauf + 1 + K['f_frist'])                 # Tilgungsbeginn
        f_m = bauende + K['f_tilg_j'] * 12 - f_T + 1                         # Zahl der Raten
        f_zb = bauende + K['f_zinslos'] * 12                                 # Ende der zinslosen Zeit
        iB = bem_zins_tr(D(0), f_zb, K['f_zins_danach'])
        rate_B = r2(fd * (iB + max(D(p) / D(f_m), mindtilg)) / p)
        kd = p * rate_B + p * r2(fd * K['f_beitrag'] / p)
        U_sum += fd
        U_B += fd
        KD_U += kd
        kd_bem['foerder'] = dict(iB=iB, kd=kd, rate=rate_B)
        R.update(f_T=f_T, f_m=f_m)
    R['kd_bem'] = kd_bem

    # ---- Bankdarlehen (R-5.12)
    i_k = max(zins_bem, anschluss_bem if h25 is None else h25)
    t_k = max(c['tilg'], mind_bank)
    ik_tk = i_k + t_k
    A = H['beta'] * W - U_B
    C = Mbed - U_sum - zu - mind_ek
    if C < 0:
        raise Meldung('M-22', 'hoechster KfW-Betrag: %s' % floor2(max(D(0), kfw + C)))
    if ik_tk == 0:
        Bv = None if re_n / H['mu'] >= KD_U else D(0)
    else:
        Bv = floor2((re_n / H['mu'] - KD_U) / ik_tk)
        while Bv > 0 and re_n < H['mu'] * (KD_U + p * r2(Bv * ik_tk / p)):
            Bv -= CENT
    cands = [('a', A), ('c', C)] + ([('b', Bv)] if Bv is not None else [])
    mn = min(v for _, v in cands)
    L = max(D(0), floor2(mn))
    bind = [k_ for k_, v in cands if v == mn]
    if Bv is not None and Bv <= 0:
        L = D(0)
        R['meld'].add('M-21')
        bind = ['b']
    R.update(A=A, B=Bv, C=C, L=L, bind=bind, W=W, KD_U=KD_U, i_k=i_k, t_k=t_k, U_sum=U_sum)
    if nur_bemessung:
        return R
    if basis is not None:                                  # R-11.8: neu bemessen mit den Annahmen des Basisfalls
        L = basis['L']
        R.update(L=L, bind=basis['bind'], A=basis['A'], B=basis['B'], C=basis['C'], re_n=basis['re_n'],
                 KD_U=basis['KD_U'], i_k=basis['i_k'], t_k=basis['t_k'], kd_bem=basis['kd_bem'],
                 gesamt_basis=basis['gesamt'])
        if 'M-21' in basis['meld']:
            R['meld'].add('M-21')
        else:
            R['meld'].discard('M-21')
        re_n, KD_U, i_k, t_k = basis['re_n'], basis['KD_U'], basis['i_k'], basis['t_k']
        ik_tk = i_k + t_k
    EK = Mbed - U_sum - zu - L
    R['EK'] = EK
    KD_B = KD_U + p * r2(L * ik_tk / p)
    R.update(KD_B=KD_B, deck_bem=(re_n / KD_B if KD_B else None), res_bem=re_n - H['mu'] * KD_B)

    # ---- Mittelabruf (R-11.3)
    einl = list(Zr)
    zus_fl = list(Zr)
    zus_entg = list(Zr)
    luecke = list(Zr)                     # Stand der Zwischenfinanzierung am Periodenende
    ausz_fd, ausz_kfw, ausz_bank = {}, {}, {}
    ek_r, fd_r, zu_r, kfw_r, L_r = EK, fd, zu, kfw, L
    erster_f = True
    lue = D(0)
    ende_abruf = bereit[3] if foerder else bauende
    for u in range(0, (ende_abruf if nb else 0) + 1):
        if u == 0:
            need = inv[0] + erh[0]
            if c.get('uebern'):
                need -= c['uebern']['rest']
        else:
            need = bau_raten.get(u, D(0))
        x = min(ek_r, need)
        einl[u] += x
        ek_r -= x
        need -= x
        if foerder and (fd_r + zu_r) > 0:
            if u >= bereit[3]:
                y = fd_r + zu_r
            else:
                extra = (entg_d + entg_z) if (erster_f and need > 0) else D(0)
                frei_ = sum((1 for b_ in bereit[:3] if u >= b_))
                grenze = (ober[frei_ - 1] if frei_ else D(0)) - (ges_f - fd_r - zu_r)
                y = max(D(0), min(grenze, need + extra + lue))
            if y > 0:
                if erster_f:
                    need += entg_d + entg_z
                    zus_entg[u] = entg_z
                    erster_f = False
                yd = min(fd_r, r2(y * fd / ges_f))
                yz = y - yd
                if yz > zu_r:
                    yz = zu_r
                    yd = y - yz
                ausz_fd[u] = yd
                zus_fl[u] = yz
                fd_r -= yd
                zu_r -= yz
                need -= y                 # negativ: die Teilrate holt die Luecke nach
        if need > 0 and kfw_r > 0:
            y = min(need, kfw_r)
            ausz_kfw[u] = ausz_kfw.get(u, D(0)) + y
            kfw_r -= y
            need -= y
        if need > 0 and L_r > 0:
            y = min(need, L_r)
            ausz_bank[u] = ausz_bank.get(u, D(0)) + y
            L_r -= y
            need -= y
        lue += need
        if u == bauende and nb:           # was am Bauende nicht abgerufen ist, fliesst im Monat des Bauendes
            if ek_r > 0:
                einl[u] += ek_r
                lue -= ek_r
                ek_r = D(0)
            if kfw_r > 0:
                ausz_kfw[u] = ausz_kfw.get(u, D(0)) + kfw_r
                lue -= kfw_r
                kfw_r = D(0)
            if L_r > 0:
                ausz_bank[u] = ausz_bank.get(u, D(0)) + L_r
                lue -= L_r
                L_r = D(0)
        luecke[u] = max(D(0), lue)
    R['mittelabruf'] = dict(einl=einl, fd=ausz_fd, kfw=ausz_kfw, bank=ausz_bank, zus=zus_fl, luecke=luecke)

    # ---- Tranchen
    def tranchen(regel):
        tr = []
        if c.get('uebern'):
            ue = c['uebern']
            a_ue = ue.get('anschluss')
            a_ue = (anschluss_bank if a_ue is None else a_ue + st_anschl)
            tr.append(Tranche('uebernommen', ue['rest'], 'prozent', ue['zins'], ue['tilg'],
                              bezug=ue.get('nenn') or ue['rest'], ausz={0: ue['rest']},
                              zb_ende=None if ue.get('zb') is None else ue['zb'] * p, anschluss=a_ue,
                              regel=regel, beitrag=ue.get('beitrag', D(0)), mindtilg=mindtilg, t_voll_fix=0))
        if L > 0:
            tr.append(Tranche('bank', L, 'prozent', zins, c['tilg'], ausz=ausz_bank or {0: L},
                              tilg_beginn=bauende + 1 if nb else 1, zb_ende=zb_bank, anschluss=anschluss_bank,
                              regel=regel, bz_satz=H['bz_satz'] if nb else D(0), bz_frei=H['bz_frei'],
                              mindtilg=mind_bank))
        if kfw > 0:
            uA = min(ausz_kfw)
            tr.append(Tranche('kfw', kfw, 'laufzeit', kfw_zins, ausz=ausz_kfw,
                              tilg_beginn=uA + 12 * c['kfw_f'] + 1, zb_ende=K['kfw_zb'] * 12,
                              anschluss=anschluss_bank, m=kfw_m, bz_satz=K['kfw_bp'],
                              bz_frei=K['kfw_bp_frei']))
        if foerder:
            tr.append(Tranche('foerder', fd, 'raten', D(0), ausz=ausz_fd, einb=entg_d, tilg_beginn=f_T,
                              zb_ende=f_zb, anschluss=K['f_zins_danach'], beitrag=K['f_beitrag'], m=f_m,
                              foerder=True))
        for t in tr:
            t.plan(N, p)
        return tr
    tr = tranchen(c.get('regel', 'tilgungssatz'))      # 'regel' nur zum Nachrechnen der Zahlen zu MA-034 / V-01
    trd = {t.name: t for t in tr}
    if kfw > 0 and max(ausz_kfw) > K['kfw_abruf']:
        R['meld'].add('M-49')
        R['m49_reicht'] = max(ausz_kfw) <= K['kfw_abruf'] + K['kfw_abruf_verl']

    # ---- Verkauf (Kapitel 8)
    def mjm_monat(m):
        return 12 * soll_m[m] * (1 - leer) - 12 * r2(c['erbbau'] * iK[pj(m)] / 12)
    vpreis = max(D(0), r2(vf * mjm_monat(NM)))
    vkost = r2(vpreis * H['vk'])
    verl = vpreis - vkost - stau_abzug
    rueck = D(0)
    bind_m_ges = K['f_bindung'] * 12
    if foerder:
        offen = max(0, bauende + bind_m_ges - N)
        rueck = r2(zu * offen / bind_m_ges)
    R.update(vpreis=vpreis, vkost=vkost, verl=verl, rueck=rueck, mjm_N=mjm_monat(NM), mjm_1=mjm_monat(m0),
             mjm=mjm_monat)

    # ---- Vorfaelligkeit (R-5.16)
    kuend = (K['kuend_sperr'] + K['kuend_frist']) * p
    kuend = kuend // 12 + (1 if kuend % 12 else 0)             # im Jahresmodus aufgerundet
    vfe = D(0)
    for t in tr:
        t.vfe = D(0)
        if t.foerder or t.zb_ende is None:
            continue
        rb = max(0, min(t.zb_ende, t.t_voll + kuend) - N)
        t.vfe = r2(t.abl_rest * H['vfe'] * rb / p)
        vfe += t.vfe
    if vfe > 0:
        R['meld'].add('M-25')
    R['vfe'] = vfe

    # ---- Abschreibung (R-7.3)
    afa = [D(0)] * (n + 1)
    rest_g = afa_grund
    akt_rest = dict(akt_massn)
    for j in range(1, n + 1):
        mon = sum(1 for m in range((j - 1) * 12 + 1, j * 12 + 1) if m > bauende) if nb else 12
        x = min(rest_g, r2(afa_grund * afa_satz * mon / 12))
        rest_g -= x
        for k_, betrag in akt_massn.items():
            if j > k_:
                y = min(akt_rest[k_], r2(betrag * afa_satz))
                akt_rest[k_] -= y
                x += y
        afa[j] = x
    buchwert = boden_w + afa_grund + sum(akt_massn.values(), D(0)) - sum(afa)
    R.update(afa=afa, buchwert=buchwert, boden=boden_w, afa_grund=afa_grund)

    # ---- steuerliche Nebenreihen: einbehaltene Betraege (R-7.15), Zuschuss (R-7.19)
    einb_abz = [D(0)] * (n + 1)           # Entgelt des Foerderdarlehens: Entgelt fuer Schulden
    zus_ertrag = [D(0)] * (n + 1)         # steuerpflichtiger Ertrag aus dem Zuschuss
    zentg_abz = [D(0)] * (n + 1)          # abziehbarer Teil des Entgelts auf den Zuschuss
    rueck_op = D(0)                       # Rueckzahlung im operativen Ergebnis (sofortige Einnahme)
    if foerder:
        S_, E_ = trd['foerder'].first, f_zb
        rest_e = entg_d
        for j in range(1, n):
            mon = max(0, min(j * p, E_) - max(S_, (j - 1) * p))
            x = min(rest_e, r2(entg_d * mon / (E_ - S_)))
            einb_abz[j] = x
            rest_e -= x
        einb_abz[n] = rest_e
        if status in UEB:
            verteilt = bool(c.get('e70'))
            if verteilt and K['f_bindung'] <= K['kat19']:
                raise Meldung('M-20', 'E-70 nur bei einer Bindung ueber der Mindestdauer KAT-19')
        else:
            if c.get('e70'):
                raise Meldung('M-20', 'E-70 nur bei Privatperson, Verein und Stiftung')
            verteilt = c.get('ma031', 'verteilt') == 'verteilt'
        R['zuschuss_lesart'] = 'verteilt' if verteilt else 'sofort'
        if verteilt:
            rest_z, rest_ze = zu, entg_z
            for j in range(1, n):
                mon = sum(1 for u in range((j - 1) * p + 1, j * p + 1) if bauende < u <= bauende + bind_m_ges)
                x = min(rest_z, r2(zu * mon / bind_m_ges))
                zus_ertrag[j] = x
                rest_z -= x
                y = min(rest_ze, r2(entg_z * mon / bind_m_ges))
                zentg_abz[j] = y
                rest_ze -= y
            zus_ertrag[n] = rest_z - rueck
            zentg_abz[n] = rest_ze
        else:
            for u in range(0, N + 1):
                jj = max(1, (u - 1) // p + 1)
                zus_ertrag[jj] += zus_fl[u]
                zentg_abz[jj] += zus_entg[u]
            rueck_op = rueck
    g_v = verl - buchwert                 # R-7.4: die Rueckzahlung mindert den Verkaufsgewinn nicht
    R['g_v'] = g_v
    R.update(einb_abz=einb_abz, zus_ertrag=zus_ertrag, zentg_abz=zentg_abz)

    # ---- Finanzplan (R-4.3)
    hp, kp = psatz(H['h'], p), psatz(H['k'], p)
    stz = Steuer(c)
    G = KKt = D(0)
    linie = H['linie']
    nach = list(Zr)
    steuer_u = list(Zr)
    G_u, KK_u, kz_u = list(Zr), list(Zr), list(Zr)
    acc = dict(miete=D(0), bew=D(0), erb=D(0), erh=D(0), zins=D(0), kkz=D(0), beitr=D(0), bz=D(0), hz=D(0))
    jahr = []
    zeilen = []
    vfe_verkauf = status in UEB           # Vorfaelligkeit gehoert zum Verkauf (R-7.11, R-7.17)
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
            if letzt and not vfe_verkauf:
                entg += vfe
            e_op = (acc['miete'] - acc['bew'] - acc['erb'] - acc['erh'] - afa[j] - entg
                    + zus_ertrag[j] - zentg_abz[j] - (rueck_op if letzt else D(0)))
            gv = g_v if letzt else D(0)
            if letzt:
                st_ohne = copy.deepcopy(stz)
                tax_ohne = st_ohne.jahr(j, e_op, acc['hz'], D(0), entg, acc['erb'], D(0), True)
            tax = stz.jahr(j, e_op, acc['hz'], gv, entg, acc['erb'], vfe if letzt else D(0), letzt)
            if letzt:
                R['steuer_verkauf'] = tax - tax_ohne
            jahr.append(dict(j=j, e_op=e_op, z_h=acc['hz'], entg=entg, tax=tax, miete=acc['miete'],
                             bew=acc['bew'] + acc['erb'], zins=acc['zins'], beitr=acc['beitr'], bz=acc['bz'],
                             vv_e=stz.vv_e, vv_g=stz.vv_g, kkz=acc['kkz'], det=stz.log[-1]['det']))
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
                KKt = min(fehl, linie + (luecke[u] if u < len(luecke) else D(0)))
                nach[u] = fehl - KKt
        G_u[u], KK_u[u], kz_u[u] = G, KKt, kz
        if detail:
            zeilen.append(dict(u=u, orig=orig, zins=zins_u, tilg=tilg_u, beitr=beitr_u, bz=bz_u, abl=abl_u, hz=hz,
                               kz=kz, tax=tax, einl=einl[u], nach=nach[u], G=G, KK=KKt, miete=miete[u], bew=bew[u],
                               soll=soll[u]))
    EW = G - KKt
    R.update(st_log=stz.log, EW=EW, jahr=jahr, zeilen=zeilen, nach=nach, einl=einl, tr=tr, trd=trd,
             steuer_u=steuer_u, soll=soll, miete=miete, bew=bew, qm=qm, m0=m0, teile=teile, zus_fl=zus_fl,
             bauende=bauende, N=N, KK_u=KK_u, kz_u=kz_u, G_u=G_u, zwifi_max=max(luecke), zwifi_zins=sum(kz_u, D(0)))

    # ---- Kennzahlen (Kapitel 10)
    e = [einl[u] + nach[u] for u in range(N + 1)]
    a = [D(0)] * (N + 1)
    EWU = alternative(c, N, p, e, a)
    f = {j: r12((1 + H['h'] * (1 - stz.s_z(j))) ** (D(1) / D(p))) for j in range(1, n + 1)}
    w = [D(1)] * (N + 1)
    for t_ in range(N - 1, -1, -1):
        w[t_] = w[t_ + 1] * f[t_ // p + 1]
    Zz = EW
    Dn = sum((e[u] * w[u] / w[0] for u in range(N + 1) if e[u]), D(0))
    nn = D(n)

    def rend(z_, d_):
        if d_ == 0:
            return None
        if z_ <= 0:
            return D(-1)
        return (z_ / d_) ** (1 / nn) - 1
    r = rend(Zz, Dn)
    rU = rend(EWU, Dn)
    z_ziel = H['z_foerder'] if (foerder and H.get('z_foerder') is not None) else H['z']
    EU = Zz - Dn * (1 + z_ziel) ** n
    ek_inv = sum(e[0:bauende + 1], D(0))
    nach_lfd = sum(nach[bauende + 1:N], D(0))
    fehl_vk = nach[N]
    if r == D(-1):
        R['meld'].add('M-29')
    if r is None:
        R['meld'].add('M-28')
    if fehl_vk > 0:
        R['meld'].add('M-42')
    R.update(EWU=EWU, dEW=EW - EWU, r=r, rU=rU, EU=EU, Z=Zz, Dn=Dn, w=w, ek_inv=ek_inv, nach_lfd=nach_lfd,
             fehl_vk=fehl_vk, ek_ges=ek_inv + nach_lfd + fehl_vk, e=e, z_ziel=z_ziel)

    # Deckungen (R-10.14)
    re_j = {jd['j']: jd['miete'] - jd['bew'] for jd in jahr}

    def kd_jahr(trs, j):
        return sum((t.kd(u) for t in trs for u in range((j - 1) * p + 1, j * p + 1)), D(0))
    deck = {}
    for j in re_j:
        kd = kd_jahr(tr, j)
        deck[j] = (re_j[j] / kd if kd else None, re_j[j], kd)
    R['deck'] = deck
    kd_vj = sum((t.kd(u) for t in tr for u in vj_per), D(0))
    zi_vj = sum((t.s['zins'][u] + t.s['beitr'][u] for t in tr for u in vj_per), D(0))
    R['kd_vj'] = kd_vj
    R['deck_vj'] = re_vj / kd_vj if kd_vj else None
    R['zinsdeck_vj'] = re_vj / zi_vj if zi_vj else None
    R['kd_je'] = {t.name: sum((t.kd(u) for u in vj_per), D(0)) for t in tr}
    kd_voll = D(0)                                   # Nr. 2: erstes Jahr bei voller Tilgung
    spaet = False
    for t in tr:
        if t.tilg_beginn > vj_per[0] and t.kd_first is not None:
            kd_voll += p * t.kd_first
            spaet = True
        else:
            kd_voll += sum((t.kd(u) for u in vj_per), D(0))
    R['deck_voll'] = (re_vj / kd_voll) if (spaet and kd_voll) else None
    erstes_voll = (m0 - 1 + 11) // 12 + 1            # erstes Planjahr, das ganz in der Vermietung liegt

    def kleinste(trs):
        kl = []
        for j in re_j:
            if j < erstes_voll:
                continue
            kd = kd_jahr(trs, j)
            if kd:
                kl.append((re_j[j] / kd, j))
        return min(kl) if kl else None
    R['deck_min'] = kleinste(tr)
    R['erstes_voll'] = erstes_voll
    # Nr. 4: erstes Planjahr nach dem Ende jeder Zinsbindung
    R['deck_nach_zb'] = {}
    for t in tr:
        if t.zb_ende is not None and t.zb_ende < N:
            j = t.zb_ende // p + 1
            R['deck_nach_zb'][t.name] = (j, deck[j][0])
    # Nr. 5: kleinste Deckung nach der unguenstigsten Anschlussregel (MA-034)
    R['deck_min_regel'] = None
    if detail and any(t.art == 'prozent' and t.zb_ende is not None and t.zb_ende < N for t in tr) and R['deck_min']:
        best = (R['deck_min'][0], R['deck_min'][1], 'tilgungssatz')
        for regel in ('rate', 'restlaufzeit'):
            trs = tranchen(regel)
            km = kleinste(trs)
            if km and km[0] < best[0]:
                best = (km[0], km[1], regel)
        R['deck_min_regel'] = best
    pruef = [x for x in (R['deck_min'][0] if R['deck_min'] else None,
                         R['deck_min_regel'][0] if R['deck_min_regel'] else None) if x is not None]
    if pruef:
        if min(pruef) < H['mu']:
            R['meld'].add('M-38')
        if min(pruef) < 1:
            R['meld'].add('M-39')
    if foerder:
        if (R['deck_bem'] is not None and R['deck_bem'] < 1) or (R['deck_min'] and R['deck_min'][0] < 1):
            R['meld'].add('M-50')
    # Gesamtkapitalrendite (R-10.11)
    a0 = sum((inv[u] * w[u] / w[0] for u in range(0, bauende + 1)), D(0))
    ZS = sum((jd['zins'] * (1 - stz.s_fk(jd['j'])) for jd in jahr), D(0))
    R['a0'] = a0
    zg = Zz - Dn + ZS + a0
    R['g'] = (zg / a0) ** (1 / nn) - 1 if a0 > 0 and zg > 0 else None
    R['restwertbeitrag'] = verl - sum((t.s['abl'][N] for t in tr), D(0)) - vfe - rueck - R.get('steuer_verkauf', D(0))
    nenner = R.get('gesamt_basis', gesamt) if nb else preis
    R['darl_quote'] = (L + U_sum) / nenner
    if status != 'befreit':
        R['meld'].add('M-37')
    else:
        R['meld'].add('M-44')
    if c.get('kennz') and not c.get('e69') and status in ('koerp', 'pg_gepr'):
        R['meld'].add('M-51')
    return R


def lauf(c, P=None, stress=False, detail=False):
    cc = c if P is None else mit(c, preis=D(P))
    return rechne(cc, stress=stress, detail=detail)


# ---------------------------------------------------------------- Preissuche (R-11.4 bis R-11.6)
def preissuche(c, stress=False, krit=None, zusatz=()):
    """Groesster Preis in vollen Euro, bis zu dem krit fuer jeden kleineren Preis des Suchbereichs gilt.
    krit(R) -> bool; Voreinstellung Endwertueberschuss >= 0. zusatz: weitere Stuetzstellen (R-6.16)."""
    H = c['H']
    if krit is None:
        krit = lambda R: R['EU'] >= 0
    cache = {}
    info = {}

    def ok(P):
        if P not in cache:
            try:
                Rr = lauf(c, P, stress)
                cache[P] = bool(krit(Rr))
                info[P] = Rr['Dn']
            except Meldung as m_:
                if m_.kennung != 'M-22':
                    raise
                cache[P] = None
        return cache[P]
    base = rechne(mit(c, preis=D(10) ** 7 if c['art'] == 'ankauf' else c['preis']), detail=False)
    mj = max(base['mjm_1'], base['mjm_N'])
    if mj <= 0:
        return dict(P=None, meld='M-31')
    O = int(r2(H['such_ober'] * mj).to_integral_value(rounding=ROUND_HALF_UP))
    if 'O' in c:
        O = c['O']
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
        return dict(P=None, meld='M-32', U=U, O=O, r_U=lauf(c, U, stress)['r'])
    Rz = H['raster']
    st = sorted(set([U + (i * (O + 1 - U)) // Rz for i in range(Rz + 1)] + [q for q in zusatz if U <= q <= O + 1]))
    lo = hi = None
    wechsel = 0
    for i in range(len(st) - 1):
        if ok(st[i]) != ok(st[i + 1]):
            wechsel += 1
            if lo is None and ok(st[i]):
                lo, hi = st[i], st[i + 1]
    if lo is None:
        return dict(P=None, meld='M-33', U=U, O=O)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    x = lo
    F = H['fenster']
    m34 = wechsel > 1
    while True:
        while x > U and not ok(x):
            x -= 1
        bad = [q for q in range(max(U, x - F), x) if not ok(q)]
        if not bad:
            break
        x = max(bad) - 1
        m34 = True
    if any(ok(q) for q in range(x + 2, x + F + 1)):
        m34 = True
    return dict(P=x, meld='M-34' if m34 else None, U=U, O=O, n_eval=len(cache), D=info.get(x))


def tragbarer_preis(c, stress=False):
    """min(P*; P_EK) mit bindender Grenze (R-11.6) und M-41."""
    ps = preissuche(c, stress)
    erg = dict(ps, grenze='rendite')
    if c.get('ek_verf') is not None:
        pe = preissuche(c, stress, krit=lambda R: R['ek_ges'] <= c['ek_verf'])
        if pe['P'] is None:
            return dict(P=None, meld='M-46')
        if ps['P'] is None or pe['P'] < ps['P']:
            erg = dict(pe, grenze='eigenkapital', meld=None)
    if erg.get('P') is not None and lauf(c, erg['P'], stress)['Dn'] == 0:
        erg = dict(erg, meld='M-41', nebenangabe=erg['P'], P=None)
    return erg


# ---------------------------------------------------------------- Zielwertsuche (R-11.9, R-11.10)
def zielwertsuche(f, u, o, a, Rz=40):
    """f(x) -> Zielfunktion (>= 0: erreicht). Gitter der Aufloesung a in [u; o], Rasterzahl Rz."""
    u, o, a = D(u), D(o), D(a)
    nsch = int(((o - u) / a).to_integral_value(rounding=ROUND_FLOOR))
    idx = sorted(set((i * nsch) // Rz for i in range(Rz + 1)))
    cache = {}

    def ok(i):
        if i not in cache:
            try:
                cache[i] = f(u + a * i) >= 0
            except Meldung:
                cache[i] = False
        return cache[i]
    loes = []
    for i0, i1 in zip(idx, idx[1:]):
        if ok(i0) != ok(i1):
            lo, hi = i0, i1
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if ok(mid) == ok(lo):
                    lo = mid
                else:
                    hi = mid
            if ok(lo):
                loes.append((u + a * lo, 'fallend'))      # erreicht -> verfehlt: letzter erreichter Wert
            else:
                loes.append((u + a * hi, 'steigend'))     # verfehlt -> erreicht: erster erreichter Wert
    if loes:
        return loes
    return 'keine Loesung: Ziel an allen Rasterstellen ' + ('erreicht' if ok(idx[0]) else 'verfehlt')


# ---------------------------------------------------------------- Ausgabe
def fmt(x, nd=2):
    if x is None:
        return 'n.d.'
    q = D(1).scaleb(-nd)
    s = f"{D(x).quantize(q, rounding=ROUND_HALF_UP):,}"
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')


def pct(x, nd=3):
    return 'n.d.' if x is None else fmt(D(x) * 100, nd) + ' %'


class Zaehler:
    """Sammelt Soll-Ist-Vergleiche je Fall."""

    def __init__(self):
        self.zeilen = []
        self.fall = ''

    def titel(self, t):
        self.fall = t
        print('\n== ' + t)

    def show(self, name, val, soll, nd=2, p=False):
        if isinstance(val, str):
            v = val
        elif isinstance(val, int) and not isinstance(val, bool):
            v = str(val)
        else:
            v = pct(val, nd) if p else fmt(val, nd)
        ok = v == soll
        self.zeilen.append((self.fall, name, v, soll, ok))
        print(f"{'OK ' if ok else 'ABW'} {name:58s} ist {v:>18s}  soll {soll:>18s}")
        return ok

    def summe(self):
        from collections import OrderedDict
        d = OrderedDict()
        for fall, name, v, soll, ok in self.zeilen:
            x = d.setdefault(fall, [0, 0])
            x[0] += 1
            x[1] += 1 if ok else 0
        print('\n== Zaehlung')
        ges = tr = 0
        for fall, (n_, k_) in d.items():
            print(f"{fall:70s} {n_:4d} Sollwerte, {k_:4d} getroffen, {n_ - k_:3d} abweichend")
            ges += n_
            tr += k_
        print(f"{'Summe':70s} {ges:4d} Sollwerte, {tr:4d} getroffen, {ges - tr:3d} abweichend")
        abw = [z for z in self.zeilen if not z[4]]
        if abw:
            print('\n== Abweichungen')
            for fall, name, v, soll, ok in abw:
                print(f"   {fall} | {name}: ist {v}, soll {soll}")
        return ges, tr


Z = Zaehler()
