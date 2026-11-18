"""Neue Grenzfaelle der Pruefrunde 2 (NG-01 ...). Aufruf: python3 neue.py [Praefixe]"""
from h import *
import grobkalkulation
from steuer import PRIVAT, KOERPERSCHAFT

F = []


def fall(nr):
    def deko(fn):
        F.append((nr, fn))
        return fn
    return deko


def mieten(e, monate):
    return " / ".join(f"M{m} {r4(e.miete_je_qm[m])}" for m in monate)


def erh_monate(e, bis):
    """Monate, in denen die Miete je m2 steigt oder faellt."""
    out = []
    for m in range(2, bis + 1):
        if e.miete_je_qm[m] != e.miete_je_qm[m - 1]:
            out.append(f"{m}:{r4(e.miete_je_qm[m])}")
    return " ".join(out)


# ------------------------------------------------------------------ Mietpfad
@fall("NG-01 Ist 11,00 ueber Vergleichsmiete 9,20, Fluktuation 10 %, Mietpreisbremse")
def _():
    return zeig(replace(ANK, ist_miete=D(11)), replace(VG, fluktuation=D("0.1")),
                extra=lambda e: "Jahr 1..4: " + mieten(e, (1, 13, 25, 37)))


@fall("NG-02 Vergleichsmiete fehlt (0) bei vermieteter Flaeche; ganz leer ohne Vergleichsmiete")
def _():
    return (zeig(replace(ANK, vergleichsmiete=NULL)) + "\n    " +
            zeig(replace(ANK, vergleichsmiete=NULL, leere_flaeche=ANK.wohnflaeche)))


@fall("NG-03 Wartefrist am Rand der Haltedauer: n = 3 und 4 (MA-037 vorsichtig), n = 1 und 2 (andere Lesart)")
def _():
    out = []
    for n, vs in ((3, True), (4, True), (1, False), (2, False)):
        e = kalk(replace(ANK, haltedauer=n), replace(VG, ma037_vorsicht=vs))[1]
        out.append(f"n={n} vorsicht={vs}: Erhoehungen {erh_monate(e, n * 12)}; Miete M{n*12} {r4(e.miete_je_qm[n*12])}; VK {de(e.verkauf.preis_brutto)}")
    return "\n    ".join(out)


@fall("NG-04 Kappungsgrenze genau erreicht: Ist 8,00, Vergleichsmiete 9,20, d = 1, Steigerung 0, andere Lesart MA-037")
def _():
    e = kalk(replace(ANK, ist_miete=D(8), vergleichsmiete=D("9.20"), anpassungsdauer=1),
             replace(VG, mietsteigerung=NULL, ma037_vorsicht=False))[1]
    return "Erhoehungen " + erh_monate(e, 144) + f" | 8 x 1,15 = {D(8) * D('1.15')}"


@fall("NG-05 Objekt ganz leer und struktureller Leerstand 100 %")
def _():
    e = replace(ANK, ist_miete=NULL, leere_flaeche=ANK.wohnflaeche)
    vg = replace(VG, leerstand=D(1), forderungsausfall=NULL)
    return zeig(e, vg) + "\n    tragbar: " + tp(e, vg)


@fall("NG-06 Fluktuation 100 % (alle Bestandsflaechen wechseln in Jahr 2), mit und ohne Mietpreisbremse")
def _():
    a = zeig(ANK, replace(VG, fluktuation=D(1)), extra=lambda e: mieten(e, (12, 13, 28, 37)))
    b = zeig(ANK, replace(VG, fluktuation=D(1)), replace(KAT, mietpreisbremse=False), extra=lambda e: mieten(e, (12, 13, 28, 37)))
    return a + "\n    ohne Bremse: " + b


@fall("NG-07 leere Flaeche 200 m2: Mietpreisbremse greift (Markt 10,50 > 10,12) / greift nicht (Markt 9,80) / Bremse aus")
def _():
    out = []
    for name, mm, bremse in (("greift", D("10.50"), True), ("greift nicht", D("9.80"), True), ("aus", D("10.50"), False)):
        e = kalk(replace(ANK, leere_flaeche=D(200), markt_miete=mm), VG, replace(KAT, mietpreisbremse=bremse))[1]
        neu = e.ertrag.pools[-1]
        out.append(f"{name}: Neuvermietung M4 {r4(neu.miete[4])}; Sollmiete M4 {de(e.ertrag.soll(4))}; VK {de(e.verkauf.preis_brutto)}")
    return "\n    ".join(out)


@fall("NG-08 gebundener Bestand 40 %: Bindungsende Jahr 1 / Jahr 12 = n / Jahr 13 / Jahr 50")
def _():
    out = []
    for b in (1, 12, 13, 50):
        s, e = kalk(replace(ANK, gebunden_anteil=D("0.4"), bindung_jahre=b, gebundene_miete=D("6.80")))
        if s != "ergebnis":
            out.append(f"b={b}: {s} {e}")
            continue
        g = [p for p in e.ertrag.pools if p.name == "Bestand gebunden"][0]
        out.append(f"b={b}: gebunden M12 {r4(g.miete[12])} M13 {r4(g.miete[13])} M25 {r4(g.miete[25])} M37 {r4(g.miete[37])} M144 {r4(g.miete[144])}; VK {de(e.verkauf.preis_brutto)}")
    return "\n    ".join(out)


@fall("NG-09 gebundene Miete E-58 = 0 und = -1 (zulaessig > 0)")
def _():
    return (zeig(replace(ANK, gebunden_anteil=D("0.4"), bindung_jahre=5, gebundene_miete=NULL), extra=lambda e: f"Einzahlung M1 {de(e.plan.zeilen[1]['miete'])}") + "\n    " +
            zeig(replace(ANK, gebunden_anteil=D(1), bindung_jahre=5, gebundene_miete=D(-1)), extra=lambda e: f"Sollmiete M1 {de(e.ertrag.soll(1))} Einzahlung M1 {de(e.plan.zeilen[1]['miete'])}"))


# ------------------------------------------------------------------ kalkulatorischer Kapitaldienst
@fall("NG-10 kalkulatorischer Zins H-25 fest 2 % unter dem Vertragszins 4 %")
def _():
    a = kalk(ANK, replace(VG, kalk_zins=D("0.02")))[1]
    b = kalk(ANK, replace(VG, ma026_vertragszins=True))[1]
    return f"H-25 2 %: L {de(a.darlehen)} i_k {a.bemessung.zins_kalk}; Lesart 2 (Vertrag): L {de(b.darlehen)}"


@fall("NG-11 Mindesttilgung 0 und Tilgung 0 bei Zins 4 %")
def _():
    return zeig(replace(ANK, tilgungssatz=NULL), replace(VG, mindesttilgung=NULL),
                extra=lambda e: f"i_k {e.bemessung.zins_kalk} tau_k {e.bemessung.tilgung_kalk} B {de(e.bemessung.bank['b'])}")


@fall("NG-12 nachhaltiger Reinertrag negativ (Leerstand 80 %) und null bei Zins, Tilgung, Aufschlag null")
def _():
    a = zeig(ANK, replace(VG, leerstand=D("0.8")), extra=lambda e: f"RE_n {de(e.bemessung.ertrag_nachhaltig)} B {e.bemessung.bank['b']}")
    vg0 = replace(VG, leerstand=D("0.8"), mindesttilgung=NULL, anschluss_aufschlag=NULL)
    b = zeig(replace(ANK, zins=NULL, tilgungssatz=NULL), vg0, extra=lambda e: f"RE_n {de(e.bemessung.ertrag_nachhaltig)} B {e.bemessung.bank['b']}")
    return a + "\n    i+tau=0: " + b


# ------------------------------------------------------------------ KfW-Tranche
@fall("NG-13 KfW genau Hoechstbetrag / einen Cent darueber")
def _():
    return (zeig(replace(NB, kfw_betrag=D(3000000)), kat=KATN) + "\n    " +
            zeig(replace(NB, kfw_betrag=D("3000000.01")), kat=KATN))


@fall("NG-14 KfW: tilgungsfreie Jahre 20 > Haltedauer 15; tilgungsfrei 12 > Zinsbindung 10 (n = 25)")
def _():
    out = []
    for tf, n in ((20, 15), (12, 25)):
        kat = replace(KATN, kfw=replace(A.KFW, tilgungsfrei_jahre=tf))
        s, e = kalk(replace(NB, kfw_betrag=D(3000000), haltedauer=n), VG, kat)
        if s != "ergebnis":
            out.append(f"tf={tf} n={n}: {s} {e}")
            continue
        z = e.plan.zeilen
        beginn = 18 + tf * 12 + 1
        t = z[beginn]["tranchen"]["KfW-Darlehen"] if beginn <= e.plan.e.raster.N else None
        out.append(f"tf={tf} n={n}: Ablosung KfW {de(z[-1]['tranchen']['KfW-Darlehen']['abloesung'])}; "
                   + (f"Monat {beginn}: Zins {de(t['zins'])} Tilgung {de(t['tilgung'])} Satz {t['satz']}" if t else "Tilgung beginnt nach N"))
    return "\n    ".join(out)


@fall("NG-15 KfW 3 Mio. plus Grobfoerderung B (Darlehen 60 %, Zuschuss 20 %, Eigenmittel 20 %): tragbarer Preis")
def _():
    e = replace(NB, kfw_betrag=D(3000000), foerderung=A.FOERDERUNG_B, haltedauer=38)
    return zeig(e, kat=KATN) + "\n    tragbar: " + tp(e, kat=KATN)


# ------------------------------------------------------------------ Vorfaelligkeit
@fall("NG-16 Verkauf am Kuendigungstermin: Bindung 15, n = 10 und 11; Monatsraster und Jahresmodus")
def _():
    out = []
    for n in (10, 11):
        for p in (12, 1):
            s, e = kalk(replace(ANK, zinsbindung_jahre=15, haltedauer=n), p=p)
            N = n * p
            out.append(f"n={n} p={p}: VFE {de(e.plan.zeilen[N]['vfe'])} Abl {de(e.plan.zeilen[N]['abloesung'])} M {[m['kennung'] for m in e.meldungen]}")
    return "\n    ".join(out)


@fall("NG-17 Bindung 5 < zehn Jahre: n = 3 und n = 5")
def _():
    out = []
    for n in (3, 5):
        e = kalk(replace(ANK, zinsbindung_jahre=5, haltedauer=n))[1]
        out.append(f"n={n}: VFE {de(e.plan.zeilen[n*12]['vfe'])} Abl {de(e.plan.zeilen[n*12]['abloesung'])}")
    return " | ".join(out)


@fall("NG-18 uebernommenes Darlehen, Bindung 20, n = 5: Kennzeichen Foerderdarlehen ja / nein / nicht angegeben")
def _():
    out = []
    for fd in (True, False, None):
        ue = dict(restschuld=D(500000), nennbetrag=D(600000), zins=D("0.005"), tilgungssatz=D("0.02"), bindung_jahre=20, anschluss_zins=D("0.03"))
        if fd is not None:
            ue["foerderdarlehen"] = fd
        e = kalk(replace(ANK, uebernommen=ue, haltedauer=5))[1]
        out.append(f"Kennzeichen {fd}: VFE {de(e.plan.zeilen[60]['vfe'])} KD_Ue {de(e.bemessung.kd_uebrige)} L {de(e.darlehen)}")
    return "\n    ".join(out)


# ------------------------------------------------------------------ Neubau
@fall("NG-19 Neubau Bauzeit 1 Monat; Bauzeit 60 bei Haltedauer 5 (> Haltedauer)")
def _():
    return zeig(replace(NB, bauzeit_monate=1), kat=KATN) + "\n    " + zeig(replace(NB, bauzeit_monate=60, haltedauer=5), kat=KATN)


@fall("NG-20 Neubau Baupreissteigerung -5 %")
def _():
    return zeig(NB, replace(VG, baupreissteigerung=D("-0.05")), KATN,
                extra=lambda e: f"BK0 {de(e.bemessung.baukosten_stichtag)} BK {de(e.baukosten)} Rate M1 {de(e.plan.zeilen[1]['investition'])} M18 {de(e.plan.zeilen[18]['investition'])}")


@fall("NG-21 Neubau gefoerdert ohne Bankdarlehen (M-21): Bereitstellungszinsen")
def _():
    return zeig(replace(NB, foerderung=A.FOERDERUNG_B, haltedauer=38), kat=KATN,
                extra=lambda e: f"Bereitstellung {de(sum(z['bereit'] for z in e.plan.zeilen))}")


@fall("NG-22 Neubau Zinsbindung 1 Jahr (endet vor dem Tilgungsbeginn in Monat 19)")
def _():
    s, e = kalk(replace(NB, zinsbindung_jahre=1), VG, KATN)
    t = e.plan.zeilen[19]["tranchen"]["Bankdarlehen"]
    L = e.darlehen
    soll_rate = (L * (D("0.05") + D("0.02")) / 12).quantize(D("0.01"))
    return (f"L {de(L)}; Monat 19: Satz {t['satz']} Zins {de(t['zins'])} Tilgung {de(t['tilgung'])} Rate {de(t['zins'] + t['tilgung'])}; "
            f"nach R-5.9 'Tilgungssatz bleibt' erwartet Rate {de(soll_rate)}, Tilgung {de(soll_rate - t['zins'])}; "
            f"Restschuld M180 {de(e.plan.zeilen[180]['restschuld'])}; Deckung VJ {r4(e.dscr_vj)}; Proben {e.befunde}")


@fall("NG-22b Vergleich: Zinsbindung 2 Jahre (endet nach dem Tilgungsbeginn)")
def _():
    s, e = kalk(replace(NB, zinsbindung_jahre=2), VG, KATN)
    t = e.plan.zeilen[25]["tranchen"]["Bankdarlehen"]
    return f"Monat 25: Satz {t['satz']} Zins {de(t['zins'])} Tilgung {de(t['tilgung'])}; Restschuld M180 {de(e.plan.zeilen[180]['restschuld'])}"


# ------------------------------------------------------------------ Eigenkapitalgrenze
@fall("NG-23 Eigenkapitalgrenze mit Fehlbetrag beim Verkauf (Faktor 4, n = 2, E-60 1,5 Mio.)")
def _():
    e = replace(ANK, verkaufsfaktor=D(4), haltedauer=2, verfuegbares_ek=D(1500000))
    vg = replace(VG, ma026_vertragszins=True, zielrendite=D("-0.5"))
    g = kalk(replace(e, verfuegbares_ek=None), vg)[1]
    return (f"bei 2,4 Mio.: EK0 {de(g.eigenkapital_investitionsphase)} FB {de(g.fehlbetrag_verkauf)} Bedarf {de(g.eigenkapitalbedarf)}"
            + "\n    tragbar: " + tp(e, vg))


@fall("NG-24 verfuegbares Eigenkapital genau gleich dem Bedarf bei 2,0 Mio.")
def _():
    g = kalk(replace(ANK, kaufpreis=D(2000000)))[1]
    g1 = kalk(replace(ANK, kaufpreis=D(2000001)))[1]
    return (f"Bedarf(2.000.000) {de(g.eigenkapitalbedarf)} Bedarf(2.000.001) {de(g1.eigenkapitalbedarf)}\n    tragbar: "
            + tp(replace(ANK, verfuegbares_ek=g.eigenkapitalbedarf)))


@fall("NG-25 verfuegbares Eigenkapital 0 bei Vollfinanzierung (ENK 0, Quote 100 %, Deckung 1, Lesart 2)")
def _():
    e = replace(ANK, enk_satz=NULL, verkaufsfaktor=D(5), verfuegbares_ek=NULL)
    vg = replace(VG, beleihungsquote=D(1), mindestdeckung=D(1), ma026_vertragszins=True, zielrendite=D("0.02"))
    return tp(replace(e, verfuegbares_ek=None), vg) + "\n    mit E-60 = 0: " + tp(e, vg)


# ------------------------------------------------------------------ Preissuche
@fall("NG-26 Zielrendite -50 % (ueberall erreicht) und 30 % (nie erreicht)")
def _():
    return tp(ANK, replace(VG, zielrendite=D("-0.5"))) + "\n    " + tp(ANK, replace(VG, zielrendite=D("0.3")))


@fall("NG-27 Probe schlaegt nur fuer Preise ueber 2,2 Mio. an (eingeschleust)")
def _():
    def st(l):
        if l["bm"].preis > 2200000:
            l["einl"][0] += D("0.01")
    grobkalkulation.STOERUNG[0] = st
    try:
        return tp(ANK)
    finally:
        grobkalkulation.STOERUNG[0] = None


# ------------------------------------------------------------------ 15-%-Regel
@fall("NG-28 15-%-Regel genau an der Schwelle (netto 297.000 zum Stichtag) und einen Cent darueber")
def _():
    out = []
    for b in (D("353430.00"), D("353430.02")):
        s, e = kalk(replace(ANK, stau_betrag=b, stau_jahr=0))
        out.append(f"Betrag {de(b)}: netto {de(b / D('1.19'))} Erhaltung M0 {de(e.plan.zeilen[0]['erhaltung'])} Invest M0 {de(e.plan.zeilen[0]['investition'])} M {[m['kennung'] for m in e.meldungen]}")
    return "\n    ".join(out)


@fall("NG-29 15-%-Regel: Massnahme 400.000 im Jahr 3 und im Jahr 4")
def _():
    out = []
    for k in (3, 4):
        e = kalk(replace(ANK, stau_betrag=D(400000), stau_jahr=k))[1]
        out.append(f"k={k}: Erhaltung {de(sum(z['erhaltung'] for z in e.plan.zeilen))} Invest nach Stichtag {de(sum(z['investition'] for z in e.plan.zeilen[1:]))} M {[m['kennung'] for m in e.meldungen]}")
    return " | ".join(out)


# ------------------------------------------------------------------ Zuschuss, Katalog
@fall("NG-30 Zuschussquote 100 % bei Darlehensquote 60 %")
def _():
    f = replace(A.FOERDERUNG_B, zuschussquote=D(1))
    return zeig(replace(NB, foerderung=f, haltedauer=38), kat=KATN)


@fall("NG-31 Land ohne Katalog (Bayern mit dem Katalog Niedersachsen); Katalogwert fehlt (Kappungsgrenze None)")
def _():
    return (zeig(replace(ANK, land="Bayern", gemeinde="Muenchen")) + "\n    " +
            zeig(ANK, kat=replace(KAT, kappung=None)) + "\n    Hebesatz fehlt: " +
            zeig(replace(ANK, steuer=replace(ANK.steuer, hebesatz=None))))


if __name__ == "__main__":
    wahl = sys.argv[1:]
    for nr, fn in F:
        if wahl and not any(nr.startswith(w) for w in wahl):
            continue
        try:
            print(f"=== {nr}\n    {fn()}", flush=True)
        except Exception as x:
            print(f"=== {nr}\n    ABSTURZ IM SKRIPT {type(x).__name__}: {x}")
            traceback.print_exc(limit=4)
