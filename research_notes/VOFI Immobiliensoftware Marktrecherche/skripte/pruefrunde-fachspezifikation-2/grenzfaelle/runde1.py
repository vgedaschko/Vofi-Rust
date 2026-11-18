"""Runde-1-Faelle (19 mit Befund, 7 der Eingabepruefung) gegen den ueberarbeiteten Referenzrechner."""
from h import *
from kennzahlen import interner_zinsfuss
from steuer import PRIVAT
import grobkalkulation

F = []


def fall(nr):
    def deko(fn):
        F.append((nr, fn))
        return fn
    return deko


null_vg = replace(VG, mindesttilgung=NULL, anschluss_aufschlag=NULL)


@fall("GF-02 Zins 0, Tilgung 0, Mindesttilgung 0 (Aufschlag 1 Pp. bleibt)")
def _():
    return zeig(replace(ANK, zins=NULL, tilgungssatz=NULL), replace(VG, mindesttilgung=NULL),
                extra=lambda e: f"b={e.bemessung.bank['b']}")


@fall("GF-02b Zins 0, Tilgung 0, Mindesttilgung 0, Aufschlag 0")
def _():
    return zeig(replace(ANK, zins=NULL, tilgungssatz=NULL), null_vg, extra=lambda e: f"b={e.bemessung.bank['b']}")


@fall("GF-03 Zins -0,5 %")
def _():
    return zeig(replace(ANK, zins=D("-0.005")))


@fall("GF-04 Zins -2 %")
def _():
    return zeig(replace(ANK, zins=D("-0.02")))


@fall("GF-06 Kaufpreis 0")
def _():
    return zeig(replace(ANK, kaufpreis=NULL))


@fall("GF-07 Ist-, Vergleichs- und Marktmiete 0")
def _():
    return zeig(replace(ANK, ist_miete=NULL, vergleichsmiete=NULL, markt_miete=NULL))


@fall("GF-08 Ist-Miete 0 bei vermieteter Flaeche")
def _():
    return zeig(replace(ANK, ist_miete=NULL))


@fall("GF-08b Objekt ganz leer (E-31 = E-13), Marktmiete 10,50")
def _():
    return zeig(replace(ANK, ist_miete=NULL, leere_flaeche=ANK.wohnflaeche),
                extra=lambda e: "Miete Monat 1..5 " + " / ".join(str(r4(x)) for x in e.miete_je_qm[1:6]))


@fall("GF-09 Objekt ganz leer: tragbarer Preis")
def _():
    return tp(replace(ANK, ist_miete=NULL, leere_flaeche=ANK.wohnflaeche))


@fall("GF-10 Leerstand 100 % (H-15 = 1, H-27 = 0)")
def _():
    return zeig(ANK, replace(VG, leerstand=D(1), forderungsausfall=NULL))


@fall("GF-48 Leerstand 30 %: Verkaufspreis")
def _():
    return zeig(ANK, replace(VG, leerstand=D("0.3")))


@fall("GF-13 Anpassungsdauer 0")
def _():
    return zeig(replace(ANK, anpassungsdauer=0), extra=lambda e: f"Miete M1 {r4(e.miete_je_qm[1])} M12 {r4(e.miete_je_qm[12])} M13 {r4(e.miete_je_qm[13])} M37 {r4(e.miete_je_qm[37])}; RE_VJ {de(e.bemessung.reinertrag_vj)}")


@fall("GF-11 Ist-Miete 11,00 ueber Vergleichsmiete 9,20")
def _():
    return zeig(replace(ANK, ist_miete=D(11)), extra=lambda e: "Jahr 1..6: " + " / ".join(str(r4(e.miete_je_qm[12 * j + 1])) for j in range(6)) + f"; RE_n {de(e.bemessung.ertrag_nachhaltig)}")


@fall("GF-19b uebernommenes Darlehen 2,0 Mio. zu 6 %, Faktor 4: tragbarer Preis")
def _():
    ue = dict(restschuld=D(2000000), zins=D("0.06"), tilgungssatz=D("0.02"), bindung_jahre=20, anschluss_zins=D("0.07"))
    return tp(replace(ANK, uebernommen=ue, verkaufsfaktor=D(4)))


@fall("GF-44 Vollfinanzierung ohne EK (ENK 0, Quote 100 %, Deckung 1, Miete 20, Faktor 5): tragbarer Preis und Zielwertsuche")
def _():
    e = replace(ANK, enk_satz=NULL, ist_miete=D(20), vergleichsmiete=D(20), markt_miete=D(20), verkaufsfaktor=D(5))
    vg = replace(VG, beleihungsquote=D(1), mindestdeckung=D(1), ma026_vertragszins=True)
    s = suche_eingabe(replace(e, kaufpreis=D(1000000)), vg, KAT, "verkaufsfaktor", 1, 30, D("0.01"))
    return tp(e, vg) + f"\n    Zielwertsuche Faktor bei 1 Mio.: {s['status']} {[str(l['wert']) for l in s['loesungen']]}"


@fall("GF-40 Neubau Bauzeit 60, Haltedauer 6 (Stress +3)")
def _():
    e = replace(NB, bauzeit_monate=60, haltedauer=6)
    return zeig(e, kat=KATN) + " | Stress: " + zeig(e, kat=KATN, stress=True) + " | tragbar Stress: " + tp(e, kat=KATN, stress=True)


@fall("GF-27 Haltedauer 1, Bindung 40")
def _():
    return zeig(replace(ANK, haltedauer=1, zinsbindung_jahre=40), extra=lambda e: f"VFE {de(e.plan.zeilen[12]['vfe'])} Abl {de(e.plan.zeilen[12]['abloesung'])}")


@fall("GF-29 Bindung 15 bei n 12; 12 bei 12")
def _():
    return (zeig(replace(ANK, zinsbindung_jahre=15), extra=lambda e: f"VFE {de(e.plan.zeilen[144]['vfe'])}") + "\n    " +
            zeig(replace(ANK, zinsbindung_jahre=12), extra=lambda e: f"VFE {de(e.plan.zeilen[144]['vfe'])}"))


@fall("GF-31 Tilgung 0, 'Restlaufzeit bleibt'")
def _():
    return zeig(replace(ANK, tilgungssatz=NULL), replace(VG, mindesttilgung=NULL, anschluss_regel="restlaufzeit"))


@fall("GF-47 Einlage zum Stichtag 100.000 zu hoch (eingeschleust)")
def _():
    def st(l):
        l["einl"][0] += D(100000)
    grobkalkulation.STOERUNG[0] = st
    try:
        return zeig(A.ANKAUF)
    finally:
        grobkalkulation.STOERUNG[0] = None


@fall("GF-46 P-07 halber Cent (BGF 2.600,12, Kennwert 2.901,89, Bauzeit 14, n 36, Foerderung B)")
def _():
    e = replace(NB, bgf=D("2600.12"), kostenkennwert=D("2901.89"), bauzeit_monate=14, haltedauer=36, foerderung=A.FOERDERUNG_B)
    return zeig(e, kat=KATN, extra=lambda x: f"Zuschuss {de(x.bemessung.zuschuss)} Rueck {de(x.verkauf.foerder_rueckzahlung)}")


@fall("GF-20 Zuschuss 80 % > Baukosten (Grundstueck 5 Mio., BRW 2000, Kennwert 1000), drei Lesarten MA-031")
def _():
    f = replace(A.FOERDERUNG_B, darlehensquote=NULL, zuschussquote=D("0.8"), eigenmittelquote=D("0.2"))
    e = replace(NB, foerderung=f, grundstueckspreis=D(5000000), bodenrichtwert=D(2000), kostenkennwert=D(1000), haltedauer=20)
    out = []
    for les in ("sofort", "verteilt", "minderung"):
        out.append(les + ": " + zeig(e, replace(VG, ma031_zuschuss=les), KATN,
                                     extra=lambda x: f"BK {de(x.bemessung.baukosten)} Z {de(x.bemessung.zuschuss)} Zgeb {de(x.bemessung.zuschuss_gebaeude)} Buchwert {de(x.verkauf.buchwert)}"))
    return "\n    ".join(out)


@fall("GF-35 Obergrenze genau P*")
def _():
    t0 = tragbarer_preis(A.ANKAUF, VG, KAT)
    e0 = t0["ergebnis"]
    bezug = max(e0.ertrag.jahresmiete(1), e0.ertrag.jahresmiete(144))
    return tp(A.ANKAUF, replace(VG, such_obergrenze_faktor=D(t0["preis"]) / bezug)) + f" (P* = {t0['preis']})"


@fall("GF-36 (x-3)(x-3,2) auf [0;10]")
def _():
    s = zielwertsuche(lambda x: (x - 3) * (x - D("3.2")), 0, 10, D("0.01"), 40)
    return (s["status"], s["rasterweite"])


@fall("GF-39 interner Zinsfuss -400.000 / +1 nach 12 Monaten; -100 / +1.200")
def _():
    a = interner_zinsfuss([D(-400000)] + [D(0)] * 11 + [D(1)], VG.izf_unten, VG.izf_oben, VG.izf_raster, p=12)
    b = interner_zinsfuss([D(-100), D(1200)], VG.izf_unten, VG.izf_oben, VG.izf_raster, p=1)
    return (a[1:], b[1:])


@fall("GF-21 Verkaufsfaktor 0; Faktor 4 nach 2 Jahren (Fehlbetrag)")
def _():
    return (zeig(replace(ANK, verkaufsfaktor=NULL)) + "\n    " +
            zeig(replace(ANK, verkaufsfaktor=D(4), haltedauer=2), replace(VG, ma026_vertragszins=True)))


@fall("GF-25 Steuersatz 100 %")
def _():
    return zeig(replace(ANK, steuer=A.steuer(PRIVAT, est_satz=D(1))))


@fall("GF-41 Neubau Bauzeit 0")
def _():
    return zeig(replace(NB, bauzeit_monate=0), kat=KATN)


@fall("GF-42 uebernommenes Darlehen ohne Anschlusszins, Bindung 5")
def _():
    ue = dict(restschuld=D(500000), zins=D("0.005"), tilgungssatz=D("0.02"), bindung_jahre=5)
    return zeig(replace(ANK, uebernommen=ue))


if __name__ == "__main__":
    wahl = sys.argv[1:]
    for nr, fn in F:
        if wahl and not any(nr.startswith(w) for w in wahl):
            continue
        try:
            print(f"=== {nr}\n    {fn()}")
        except Exception as x:
            print(f"=== {nr}\n    ABSTURZ IM SKRIPT {type(x).__name__}: {x}")
            traceback.print_exc(limit=3)
