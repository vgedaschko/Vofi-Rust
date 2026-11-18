"""Grenzfaelle gegen den Referenzrechner (Kopie in ./rr). Aufruf: python3 grenzfaelle.py [Fallnummern]"""
import sys, os, traceback
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "rr"))
from decimal import Decimal as D
from dataclasses import replace
import annahmen as A
from grobkalkulation import rechne_grob, tragbarer_preis, suche_eingabe, Meldung, zielwertsuche
from steuer import PRIVAT, KOERPERSCHAFT, BEFREIT
from kennzahlen import interner_zinsfuss
from zahlen import de, proz

NULL = D(0)
ANK = replace(A.ANKAUF, stau_betrag=NULL)    # Ankauf ohne Investitionsstau als neutrale Basis
VG = A.VORGABEN


def kurz(e):
    k = e.kennzahlen
    b = e.bemessung.bank
    return (f"EW {de(e.plan.endwert)} | dEW {de(k['endwertdifferenz'])} | r {proz(k['rendite'])} ({k['rendite_status']}) | "
            f"L {de(e.darlehen)} bindend {b['bindend']} Meldung {b['meldung']} | EK {de(e.eigenkapital_investitionsphase)} | "
            f"Nachschuss {de(e.nachschuss_spaeter)} | VK-Preis {de(e.verkauf.preis_brutto)} | "
            f"DSCR {None if e.dscr_vj is None else round(e.dscr_vj, 4)} | Proben {e.befunde}")


def lauf(nr, titel, fn):
    print(f"\n=== GF-{nr:02d} {titel}")
    try:
        r = fn()
        if r is not None:
            print("   ", r)
    except Meldung as m:
        print("    MELDUNG", m.kennung, m.text)
    except Exception as x:
        print("    ABSTURZ", type(x).__name__, x)
        traceback.print_exc(limit=2, file=sys.stdout)


F = {}


def fall(nr, titel):
    def deko(fn):
        F[nr] = (titel, fn)
        return fn
    return deko


@fall(1, "Bankzins 0 %, Tilgung 2 %")
def _():
    return kurz(rechne_grob(replace(ANK, zins=NULL), VG))

@fall(2, "Bankzins 0 % und Tilgung 0 % (H-04 >= 0, E-64 >= H-04 zulaessig)")
def _():
    return kurz(rechne_grob(replace(ANK, zins=NULL, tilgungssatz=NULL), replace(VG, mindesttilgung=NULL)))

@fall(3, "Bankzins negativ -0,5 % (E-45 erlaubt 0 bis 20: M-20 erwartet)")
def _():
    return kurz(rechne_grob(replace(ANK, zins=D("-0.005")), VG))

@fall(4, "Bankzins -2 % bei 2 % Tilgung (i + tau = 0)")
def _():
    return kurz(rechne_grob(replace(ANK, zins=D("-0.02")), VG))

@fall(5, "Eigenkapital 0: Beleihungsquote 100 %, Nebenkosten 0 %, Deckung 1,0, Miete hoch")
def _():
    e = replace(ANK, enk_satz=NULL, ist_miete=D("20"), markt_miete=D("20"))
    return kurz(rechne_grob(e, replace(VG, beleihungsquote=D(1), mindestdeckung=D(1))))

@fall(6, "Kaufpreis 0 (E-10 > 0: M-20 erwartet)")
def _():
    return kurz(rechne_grob(replace(ANK, kaufpreis=NULL), VG))

@fall(7, "Ist- und Marktmiete 0 (E-16 > 0: M-20 erwartet)")
def _():
    return kurz(rechne_grob(replace(ANK, ist_miete=NULL, markt_miete=NULL), VG))

@fall(8, "Ist-Miete 0 (leerstehendes Objekt, E-15 >= 0 zulaessig), Marktmiete 9,20, Anpassung 4 Jahre")
def _():
    e = rechne_grob(replace(ANK, ist_miete=NULL), VG)
    return kurz(e) + "\n    Miete je m2 Jahr 1..13: " + " / ".join(str(round(x, 4)) for x in e.miete_je_qm[1:14])

@fall(9, "Ist-Miete 0: hoechster tragbarer Preis")
def _():
    t = tragbarer_preis(replace(ANK, ist_miete=NULL), VG)
    return (t["preis"], t["meldung"], t["suche"]["status"])

@fall(10, "Leerstand 100 % (Mietausfallquote 1): Verkaufspreis")
def _():
    return kurz(rechne_grob(ANK, replace(VG, mietausfall=D(1))))

@fall(11, "Ist-Miete ueber Marktmiete (11,00 gegen 9,20)")
def _():
    e = rechne_grob(replace(ANK, ist_miete=D("11")), VG)
    return kurz(e) + "\n    Miete je m2 Jahr 1..6: " + " / ".join(str(round(x, 4)) for x in e.miete_je_qm[1:7])

@fall(12, "Mietanpassung an der Kappungsgrenze: Ist 8,00, Markt 9,20 (Pfad trifft Kappung genau), d = 3")
def _():
    e = rechne_grob(replace(ANK, ist_miete=D("8"), markt_miete=D("9.20"), anpassungsdauer=3), replace(VG, mietsteigerung=NULL))
    return "Miete je m2 Jahr 1..8: " + " / ".join(str(round(x, 6)) for x in e.miete_je_qm[1:9])

@fall(13, "Anpassungsdauer 0: gilt im Jahr 1 die Ist-Miete? (R-6.3 Satz 2)")
def _():
    e = rechne_grob(replace(ANK, anpassungsdauer=0), VG)
    return f"Miete Jahr 1 {round(e.miete_je_qm[1], 4)} (Ist 8,50; Markt 9,20); Reinertrag VJ {de(e.bemessung.reinertrag_vj)}; L {de(e.darlehen)}"

@fall(14, "Beleihungsquote 0 %")
def _():
    return kurz(rechne_grob(ANK, replace(VG, beleihungsquote=NULL)))

@fall(15, "Beleihungsquote 100 %")
def _():
    return kurz(rechne_grob(ANK, replace(VG, beleihungsquote=D(1))))

@fall(16, "Mindestdeckung verfehlt schon das uebernommene Darlehen (1,8 Mio. zu 3 %, 2 % Tilgung)")
def _():
    ue = dict(restschuld=D(1800000), zins=D("0.03"), tilgungssatz=D("0.02"), bindung_jahre=20, anschluss_zins=D("0.05"))
    return kurz(rechne_grob(replace(ANK, uebernommen=ue), VG))

@fall(17, "Uebernommenes Darlehen groesser als Mittelbedarf (3 Mio.)")
def _():
    ue = dict(restschuld=D(3000000), zins=D("0.01"), tilgungssatz=D("0.02"), bindung_jahre=20, anschluss_zins=D("0.05"))
    return kurz(rechne_grob(replace(ANK, uebernommen=ue), VG))

@fall(18, "Uebernommenes Darlehen genau gleich Mittelbedarf (2,64 Mio.)")
def _():
    ue = dict(restschuld=D(2640000), zins=D("0.01"), tilgungssatz=D("0.02"), bindung_jahre=20, anschluss_zins=D("0.05"))
    return kurz(rechne_grob(replace(ANK, uebernommen=ue), VG))

@fall(19, "Tragbarer Preis bei uebernommenem Darlehen 2,0 Mio. und unerreichbarer Zielrendite 12 %")
def _():
    ue = dict(restschuld=D(2000000), zins=D("0.01"), tilgungssatz=D("0.02"), bindung_jahre=20, anschluss_zins=D("0.05"))
    t = tragbarer_preis(replace(ANK, uebernommen=ue), replace(VG, zielrendite=D("0.12")))
    return (t["preis"], t["meldung"], t["suche"]["status"], [str(l["wert"]) for l in t["suche"]["loesungen"]])

@fall(20, "Zuschuss groesser als Baukosten (Neubau, Zuschussquote 80 %, Grundstueck teuer, Bau billig)")
def _():
    f = replace(A.FOERDERUNG_B, darlehensquote=NULL, zuschussquote=D("0.8"), eigenmittelquote=D("0.2"), bodenrichtwert=D("2000"))
    e = rechne_grob(replace(A.NEUBAU, foerderung=f, grundstueckspreis=D(5000000), kostenkennwert=D(1000), haltedauer=20), A.VORGABEN_NEUBAU)
    bm = e.bemessung
    return (f"Baukosten {de(bm.baukosten)} Zuschuss {de(bm.zuschuss)}; AfA Jahr 3 {de(e.plan.zeilen[36]['afa'])}; "
            f"Buchwert {de(e.verkauf.buchwert)}; Rueckzahlung {de(e.verkauf.foerder_rueckzahlung)}; " + kurz(e))

@fall(21, "Verkaufsfaktor 0 (E-47 > 0: M-20 erwartet)")
def _():
    return kurz(rechne_grob(replace(ANK, verkaufsfaktor=NULL), VG))

@fall(22, "Negativer Endwert und Verlust in jedem Jahr (Mietausfall 60 %, Faktor 8)")
def _():
    e = rechne_grob(replace(ANK, verkaufsfaktor=D(8)), replace(VG, mietausfall=D("0.6")))
    st = [x["steuer"] for x in e.plan.steuer.protokoll]
    return kurz(e) + f"\n    Steuer je Jahr {[str(s) for s in st]}; Vortrag am Ende {de(e.plan.steuer.vv)}"

@fall(23, "Verkaufsgewinn negativ (Faktor 10), Koerperschaft und Privatperson (n = 5 <= Frist)")
def _():
    a = rechne_grob(replace(ANK, verkaufsfaktor=D(10), haltedauer=5), VG)
    b = rechne_grob(replace(ANK, verkaufsfaktor=D(10), haltedauer=5, steuer=A.steuer(PRIVAT)), VG)
    return (f"KSt: g_v {de(a.plan.zeilen[60]['g_v'])} Steuer J5 {de(a.plan.zeilen[60]['steuer'])} | " + kurz(a) +
            f"\n    Privat: g_v {de(b.plan.zeilen[60]['g_v'])} Steuer J5 {de(b.plan.zeilen[60]['steuer'])} | " + kurz(b))

@fall(24, "Steuersatz 0 % (Privatperson, Zinssatz 0)")
def _():
    return kurz(rechne_grob(replace(ANK, steuer=A.steuer(PRIVAT, est_satz=NULL, zins_satz=NULL)), VG))

@fall(25, "Steuersatz 100 % (E-42 bis 60: M-20 erwartet)")
def _():
    return kurz(rechne_grob(replace(ANK, steuer=A.steuer(PRIVAT, est_satz=D(1), zins_satz=D(1))), VG))

@fall(26, "Haltedauer 1 Jahr, Zinsbindung 10 Jahre")
def _():
    e = rechne_grob(replace(ANK, haltedauer=1), VG)
    return kurz(e) + f" | VFE {de(e.plan.zeilen[12]['vfe'])}"

@fall(27, "Haltedauer 1 Jahr, Zinsbindung 40 Jahre (E-46 Hoechstwert): Vorfaelligkeit")
def _():
    e = rechne_grob(replace(ANK, haltedauer=1, zinsbindung_jahre=40), VG)
    return kurz(e) + f" | VFE {de(e.plan.zeilen[12]['vfe'])} bei Ablosung {de(e.plan.zeilen[12]['abloesung'])}"

@fall(28, "Haltedauer 42 Jahre Ankauf, Zinsbindung 10")
def _():
    e = rechne_grob(replace(ANK, haltedauer=42), VG)
    return kurz(e)

@fall(29, "Zinsbindung laenger als Haltedauer (15 gegen 12) und gleich (12 gegen 12)")
def _():
    a = rechne_grob(replace(ANK, zinsbindung_jahre=15), VG)
    b = rechne_grob(replace(ANK, zinsbindung_jahre=12), VG)
    return (f"15/12: VFE {de(a.plan.zeilen[144]['vfe'])} EW {de(a.plan.endwert)}\n    "
            f"12/12: VFE {de(b.plan.zeilen[144]['vfe'])} EW {de(b.plan.endwert)}")

@fall(30, "Tilgung 0 % (H-04 = 0)")
def _():
    return kurz(rechne_grob(replace(ANK, tilgungssatz=NULL), replace(VG, mindesttilgung=NULL)))

@fall(31, "Tilgung 0 % mit Anschlussregel 'Restlaufzeit bleibt' (H-07)")
def _():
    return kurz(rechne_grob(replace(ANK, tilgungssatz=NULL), replace(VG, mindesttilgung=NULL, anschluss_regel="restlaufzeit")))

@fall(32, "Tilgung 100 %")
def _():
    e = rechne_grob(replace(ANK, tilgungssatz=D(1)), VG)
    return kurz(e) + f" | Restschuld nach Monat 12 {de(e.plan.zeilen[12]['restschuld'])}"

@fall(33, "Investitionsstau im Verkaufsjahr (k = n = 12), Erhaltung und Modernisierung")
def _():
    a = rechne_grob(replace(A.ANKAUF, stau_jahr=12), VG)
    b = rechne_grob(replace(A.ANKAUF, stau_jahr=12, stau_art="modernisierung"), VG)
    c = rechne_grob(replace(A.ANKAUF, stau_jahr=13), VG)
    return (f"k=12 Erh: Zahlung M144 {de(a.plan.zeilen[144]['erhaltung'])}, Abzug {de(a.verkauf.stau_abzug)}, EW {de(a.plan.endwert)}\n"
            f"    k=12 Mod: Invest M144 {de(b.plan.zeilen[144]['investition'])}, Buchwert {de(b.verkauf.buchwert)}, EW {de(b.plan.endwert)}\n"
            f"    k=13: Abzug {de(c.verkauf.stau_abzug)}, EW {de(c.plan.endwert)}")

@fall(34, "Tragbarer Preis ohne Loesung (Zielrendite 30 %)")
def _():
    t = tragbarer_preis(ANK, replace(VG, zielrendite=D("0.30")))
    return (t["preis"], t["meldung"], t["suche"]["status"])

@fall(35, "Tragbarer Preis mit Loesung genau an der Obergrenze (Obergrenze = P* aus RF-11)")
def _():
    t0 = tragbarer_preis(A.ANKAUF, VG)
    pstar = t0["preis"]
    sm = t0["ergebnis"].sollmiete_vj
    vg2 = replace(VG, suchobergrenze_faktor=D(pstar) / sm)
    t = tragbarer_preis(A.ANKAUF, vg2)
    return f"P* = {pstar}; Obergrenze {(vg2.suchobergrenze_faktor * sm).quantize(D(1))}; Ergebnis {t['preis']} {t['meldung']} {t['suche']['status']}"

@fall(36, "Zielwertsuche mit zwei Loesungen naeher als die Rasterweite: (x-3)(x-3,2) auf [0;10], Raster 40")
def _():
    s = zielwertsuche(lambda x: (x - D(3)) * (x - D("3.2")), 0, 10, D("0.01"), 40)
    return (s["status"], [str(l["wert"]) for l in s["loesungen"]], s["rasterweite"])

@fall(37, "Sehr grosse Betraege: Kaufpreis 2,4 Mrd., Flaeche x1000")
def _():
    e = rechne_grob(replace(ANK, kaufpreis=D(2400000000), wohnflaeche=D(1320000), einheiten=20000), VG)
    return kurz(e)

@fall(38, "Kleinstbetraege: Kaufpreis 2.400 Euro, 1,32 m2, 1 Einheit")
def _():
    e = rechne_grob(replace(ANK, kaufpreis=D(2400), wohnflaeche=D("1.32"), einheiten=1), replace(VG, verwaltung_je_einheit=D("0.35")))
    return kurz(e)

@fall(39, "Interner Zinsfuss unter -99 %: Einlage 400.000, Endwert 1 Euro nach 1 Jahr")
def _():
    return interner_zinsfuss([D(-400000), D(1)])

@fall(40, "Neubau Bauzeit 60 Monate, Haltedauer 6: Basisfall und Stressfall (+3 Monate)")
def _():
    e = replace(A.NEUBAU, bauzeit_monate=60, haltedauer=6)
    a = rechne_grob(e, A.VORGABEN_NEUBAU)
    out = "Basis: " + kurz(a)
    try:
        rechne_grob(e, A.VORGABEN_NEUBAU, stress=True)
    except Meldung as m:
        out += f"\n    Stress: MELDUNG {m.kennung}"
    try:
        t = tragbarer_preis(e, A.VORGABEN_NEUBAU, stress=True)
        out += f"\n    tragbarer Preis Stress: {t['preis']} {t['meldung']}"
    except Exception as x:
        out += f"\n    tragbarer Preis Stress: ABSTURZ {type(x).__name__} {x}"
    return out

@fall(41, "Neubau Bauzeit 0 (E-26 1 bis 60: M-20 erwartet)")
def _():
    return kurz(rechne_grob(replace(A.NEUBAU, bauzeit_monate=0), A.VORGABEN_NEUBAU))

@fall(42, "Zinsbindung des uebernommenen Darlehens endet vor Verkauf, Anschlusszins fehlt (M-24)")
def _():
    ue = dict(restschuld=D(500000), zins=D("0.005"), tilgungssatz=D("0.02"), bindung_jahre=5)
    return kurz(rechne_grob(replace(ANK, uebernommen=ue), VG))

@fall(43, "Gebundener Bestand: Bindungsende im Verkaufsjahr (b = n = 12)")
def _():
    e = rechne_grob(replace(ANK, gebunden_anteil=D("0.4"), bindung_jahre=12, gebundene_miete=D("6.80"), geb_steigerung=D("0.0615")), VG)
    f = rechne_grob(replace(ANK, gebunden_anteil=D("0.4"), bindung_jahre=11, gebundene_miete=D("6.80"), geb_steigerung=D("0.0615")), VG)
    return (f"b=12: Miete J13 {round(e.miete_je_qm[13], 4)} VK {de(e.verkauf.preis_brutto)} | "
            f"b=11: Miete J13 {round(f.miete_je_qm[13], 4)} VK {de(f.verkauf.preis_brutto)}")

@fall(44, "Rendite nicht definiert in der Preissuche: Vollfinanzierung (EK 0) bei schlechtem Objekt")
def _():
    # Nebenkosten 0, Quote 100 %, Wertansatz frei, Deckung 1,0; Zielrendite 5 %
    e = replace(ANK, enk_satz=NULL, ist_miete=D("20"), markt_miete=D("20"), verkaufsfaktor=D(5))
    vg = replace(VG, beleihungsquote=D(1), mindestdeckung=D(1))
    t = tragbarer_preis(e, vg)
    s = suche_eingabe(replace(e, kaufpreis=D(1000000)), vg, "verkaufsfaktor", 1, 30, D("0.01"))
    return (f"tragbarer Preis {t['preis']} {t['meldung']} {t['suche']['status']}; "
            f"Zielwertsuche Faktor bei 1 Mio.: {s['status']} {[str(l['wert']) for l in s['loesungen']]}")

@fall(45, "Stichtag im Dezember: Startjahr der Steuersaetze (R-2.8) bei steigendem Satz")
def _():
    return "nicht rechenbar im Referenzrechner (Startjahr ganzzahlig, keine Monatsangabe); siehe Befund"


def reproduzierbarkeit():
    print("\n=== REPRO Reproduzierbarkeit und Reihenfolge der Tranchen")
    ue = dict(restschuld=D(500000), zins=D("0.005"), tilgungssatz=D("0.02"), bindung_jahre=20, anschluss_zins=D("0.03"))
    e = replace(A.ANKAUF, uebernommen=ue)
    a = rechne_grob(e, VG)
    b = rechne_grob(e, VG)
    print("    zweimal gleich:", a.plan.endwert == b.plan.endwert, a.kennzahlen["rendite"] == b.kennzahlen["rendite"])
    from finanzplan import rechne_plan, rechne_alternative
    from grobkalkulation import _kopie
    pe = a.plan.e
    pe2 = replace(pe, tranchen=list(reversed(_kopie(pe.tranchen))))
    pe1 = replace(pe, tranchen=_kopie(pe.tranchen))
    p1, p2 = rechne_plan(pe1), rechne_plan(pe2)
    print("    Tranchen umgekehrt: EW", de(p1.endwert), de(p2.endwert), "gleich:", p1.endwert == p2.endwert,
          "alle Zeilen gleich:", all(x["bestandssaldo"] == y["bestandssaldo"] for x, y in zip(p1.zeilen, p2.zeilen)))
    # Neubau mit Foerderung: Reihenfolge der Mittelquellen ist fest (R-11.3); zweimal rechnen
    n1 = rechne_grob(replace(A.NEUBAU, foerderung=A.FOERDERUNG_B, haltedauer=20), A.VORGABEN_NEUBAU)
    n2 = rechne_grob(replace(A.NEUBAU, foerderung=A.FOERDERUNG_B, haltedauer=20), A.VORGABEN_NEUBAU)
    print("    Neubau gefoerdert zweimal gleich:", n1.plan.endwert == n2.plan.endwert, de(n1.plan.endwert))


if __name__ == "__main__":
    wahl = [int(x) for x in sys.argv[1:] if x.isdigit()] or sorted(F)
    for nr in wahl:
        lauf(nr, *F[nr])
    if not sys.argv[1:] or "repro" in sys.argv:
        reproduzierbarkeit()
