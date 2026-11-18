"""Praktiker, Pruefrunde 2 Fachspezifikation Rechenkern: die vier Faelle aus Runde 1 mit dem ueberarbeiteten
Referenzrechner. Aufruf: python3 -I faelle_r2.py [1|2|3|4]"""
import sys
from dataclasses import replace
from decimal import Decimal as D
RR = "/home/user/vofi-rust/research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner"
sys.path.insert(0, RR)
import annahmen as A
import grobkalkulation as G
from grobkalkulation import rechne_grob, tragbarer_preis, Meldung, suche_eingabe, kalkuliere

VG, KAT, KATN = A.VORGABEN, A.KATALOG, A.KATALOG_NEUBAU
WAHL = sys.argv[1:] or ["1", "2", "3", "4"]


def eur(x):
    return "-" if x is None else f"{x:,.0f}".replace(",", ".")


def pz(x):
    return "-" if x is None else f"{x*100:.3f} %"


def zeige(titel, e):
    b = e.bemessung.bank
    kz = e.kennzahlen or {}
    print(f"  {titel}: Preis {eur(e.preis)} | Bank {eur(e.darlehen)} bindet {b['bindend']} (A {eur(b['a'])}, B {eur(b['b'])}, C {eur(b['c'])})"
          f" | EK {eur(e.eigenkapital_investitionsphase)} lfd. Nachschuss {eur(e.nachschuss_laufend)} EK-Bedarf ges. {eur(e.eigenkapitalbedarf)}"
          f" | DSCR {e.dscr_vj and round(e.dscr_vj,3)} min {e.deckung_min and round(e.deckung_min,3)} (J {e.deckung_min_jahr})"
          f" | r {pz(kz.get('rendite'))} | dEW {eur(kz.get('endwertdifferenz'))} | M {[m['kennung'] for m in e.meldungen]}")


def tp(titel, ein, vg, kat, stress=False):
    t = tragbarer_preis(ein, vg, kat, stress=stress)
    e = t.get("ergebnis")
    extra = ""
    if e is not None:
        extra = (f" | Bank {eur(e.darlehen)} ({e.bemessung.bank['bindend']}) EK {eur(e.eigenkapital_investitionsphase)}"
                 f" EK ges. {eur(e.eigenkapitalbedarf)} DSCR {round(e.dscr_vj,3)} min {e.deckung_min and round(e.deckung_min,3)}")
        if t.get("faktor"):
            extra += f" | Faktor {t['faktor']:.2f}"
        extra += f" | {t['preis_je_qm']:.0f} EUR/m2 WF"
        if t.get("preis_je_qm_grundstueck"):
            extra += f" | {t['preis_je_qm_grundstueck']:.0f} EUR/m2 Grst"
        if t.get("abstand_angebot") is not None:
            extra += f" | Abstand Angebot {eur(t['abstand_angebot'])}"
    rnd = ""
    if t.get("ergebnis_unten") is not None:
        rnd = f" | Rendite beim kleinsten Preis {pz(t['ergebnis_unten'].kennzahlen['rendite'])}"
    print(f"  tragbar {titel}: {eur(t['preis'])} bindet {t['bindend']} M {t['meldung']} {t.get('text','') or ''}{extra}{rnd}")
    return t


# ---------------------------------------------------------------- Fall 1 Bestand mit Investitionsstau
F1 = replace(A.ANKAUF, wohnflaeche=D(1560), einheiten=24, kaufpreis=D(2650000), angebotspreis=D(2650000),
             enk_satz=D("0.10"), bodenanteil=D("0.20"), baujahr=1968,
             ist_miete=D(134784) / 12 / D(1560), vergleichsmiete=D("8.80"), markt_miete=D("10.00"),
             anpassungsdauer=5, stau_betrag=D(420000), stau_jahr=1, stau_art="erhaltung", co2_ausstoss=D(35),
             verkaufsfaktor=D(19), haltedauer=12)
if "1" in WAHL:
    print("FALL 1 Bestand mit Investitionsstau (24 WE, 1.560 m2, Bj. 1968, Ist 7,20, Mietspiegel 8,80)")
    zeige("Angebot 2,65 Mio", rechne_grob(F1, VG, KAT))
    tp("Basis", F1, VG, KAT)
    tp("Stress", F1, VG, KAT, stress=True)
    tp("Lesart 2 MA-026 (Vertragskonditionen)", F1, replace(VG, ma026_vertragszins=True), KAT)
    tp("Lesart 3 MA-026 (Ertrag des Vorhabens)", F1, replace(VG, ma026_ertrag_vorhaben=True), KAT)
    tp("MA-037 andere Lesart (Miete seit 36 Mon. unveraendert)", F1, replace(VG, ma037_vorsicht=False), KAT)
    tp("Mietenhistorie bekannt: letzte Erhoehung vor 24 Mon., Miete vor 3 J. 6,60", replace(F1, mietenhistorie=(24, D("6.60"))), VG, KAT)
    tp("ohne Anlaufleerstand/Baupreissteigerung (H-14 = 0)", F1, replace(VG, baupreissteigerung=D(0)), KAT)
    tp("verfuegbares EK 1,2 Mio", replace(F1, verfuegbares_ek=D(1200000)), VG, KAT)
    tp("verfuegbares EK 1,2 Mio, Stau zum Stichtag", replace(F1, verfuegbares_ek=D(1200000), stau_jahr=0), VG, KAT)
    tp("Vergleichsmiete = Angebotsmiete 10,00 (Fehleingabe)", replace(F1, vergleichsmiete=D("10.00")), VG, KAT)

# ---------------------------------------------------------------- Fall 2 gebundener Bestand
F2 = replace(A.ANKAUF, wohnflaeche=D(2800), einheiten=40, kaufpreis=D(3400000), angebotspreis=D(3400000),
             enk_satz=D("0.10"), bodenanteil=D("0.25"), baujahr=1994, ist_miete=D("6.10"), vergleichsmiete=D("8.50"),
             markt_miete=D("9.50"), anpassungsdauer=4, stau_betrag=D(0), stau_jahr=0, co2_ausstoss=D(20),
             verkaufsfaktor=D(17), haltedauer=12, gebunden_anteil=D(1), bindung_jahre=8, gebundene_miete=D("6.10"),
             uebernommen=dict(restschuld=D(1100000), zins=D("0.005"), tilgungssatz=D("0.02"), bindung_jahre=8))
if "2" in WAHL:
    print("FALL 2 gebundener Bestand (40 WE, 2.800 m2, ganz gebunden 6,10 bis Jahr 8, uebernommen 1,1 Mio 0,5 %)")
    r = kalkuliere(F2, VG, KAT)
    print("  nur Pflichtwerte des uebernommenen Darlehens:", r["status"], [m["kennung"] for m in r["meldungen"]])
    zeige("Angebot 3,4 Mio, Voreinstellungen E-59", r["ergebnis"])
    tp("Basis (Voreinstellungen: Anschluss 5 %, Foerder ja, Rang vor)", F2, VG, KAT)
    tp("Stress", F2, VG, KAT, stress=True)
    F2n = replace(F2, uebernommen=dict(F2.uebernommen, nennbetrag=D(1400000)))
    tp("Nennbetrag 1,4 Mio (Rate auf Nennbetrag)", F2n, VG, KAT)
    tp("Rang nach der Bank", replace(F2, uebernommen=dict(F2.uebernommen, rang="nach")), VG, KAT)
    tp("Anschluss laut Bescheid 1,5 %", replace(F2, uebernommen=dict(F2.uebernommen, anschluss_zins=D("0.015"))), VG, KAT)
    tp("VKB 0,5 %", replace(F2, uebernommen=dict(F2.uebernommen, beitrag_satz=D("0.005"))), VG, KAT)
    tp("Lesart 2 MA-026", F2, replace(VG, ma026_vertragszins=True), KAT)
    e = rechne_grob(replace(F2, uebernommen=dict(F2.uebernommen, bindung_jahre=14)), VG, KAT)
    print("  Bindung uebernommen 14 J., Verkauf 12: Vorfaelligkeit", eur(e.plan.zeilen[e.plan.e.raster.N]["vfe"]))
    print("  KD je Darlehen (Bemessung):", {k: eur(v) for k, v in e.bemessung.kd_je_darlehen.items()})

# ---------------------------------------------------------------- Fall 3 Neubau frei finanziert mit KfW
F3 = replace(A.NEUBAU, wohnflaeche=D(2450), einheiten=36, bgf=D(3400), kostenkennwert=D(3000),
             grundstueckspreis=D(2000000), grundstuecksflaeche=D(3200), bauzeit_monate=22, enk_satz=D("0.065"),
             markt_miete=D("17.50"), verkaufsfaktor=D(25), haltedauer=15)
if "3" in WAHL:
    print("FALL 3 Neubau frei finanziert (36 WE, 2.450 m2, BGF 3.400, Bauzeit 22, 17,50, Faktor 25, 15 J.)")
    F3a = replace(F3, kostenkennwert=D(2400))   # 2.400 x 1,25 = 3.000 EUR/m2 BGF fuer KG 200-700 wie in Runde 1 gemeint
    for name, f in (("KKW 3.000 als KG 300/400 (+25 %)", F3), ("KKW 2.400 KG 300/400 = 3.000 gesamt wie Runde 1", F3a)):
        print(" ", name)
        zeige("Grundstueck 2,0 Mio, ohne KfW", rechne_grob(f, VG, KATN))
        tp("ohne KfW", f, VG, KATN)
        fk = replace(f, kfw_betrag=D(3600000))
        zeige("Grundstueck 2,0 Mio, mit KfW 3,6 Mio", rechne_grob(fk, VG, KATN))
        tp("mit KfW 3,6 Mio", fk, VG, KATN)
        tp("mit KfW, Lesart 2 MA-026", fk, replace(VG, ma026_vertragszins=True), KATN)
        tp("ohne KfW, Lesart 2 MA-026", f, replace(VG, ma026_vertragszins=True), KATN)
        tp("mit KfW Stress", fk, VG, KATN, stress=True)
    # Zerlegung der Vorsicht am Fall 3a mit KfW
    fk = replace(F3a, kfw_betrag=D(3600000))
    print("  Zerlegung (KKW 2.400, mit KfW): je eine neue Vorsicht abgeschaltet")
    tp("  Baupreissteigerung 0", fk, replace(VG, baupreissteigerung=D(0)), KATN)
    tp("  Bereitstellungszins 0", fk, replace(VG, bereit_satz=D(0)), KATN)
    tp("  Anlaufleerstand 0", fk, replace(VG, anlaufleerstand=0), KATN)
    tp("  Bereitstellungszins: 12 Monate frei, 0,25 %", fk, replace(VG, bereit_frei=12), KATN)
    tp("  kalk. Zins = Vertragszins (Lesart 2)", fk, replace(VG, ma026_vertragszins=True), KATN)
    tp("  Mindestansatz Bewirtschaftung Bank 0 (KAT-14)", fk, VG, replace(KATN, bewirtschaftung_mindest=D(0)))
    tp("  alles zusammen zurueck", fk, replace(VG, baupreissteigerung=D(0), bereit_satz=D(0), anlaufleerstand=0,
                                                ma026_vertragszins=True), replace(KATN, bewirtschaftung_mindest=D(0)))
    tp("  Ziel 4,5 % statt 5 %", fk, replace(VG, zielrendite=D("0.045")), KATN)
    tp("  Verkaufsfaktor 27", replace(fk, verkaufsfaktor=D(27)), VG, KATN)
    s = suche_eingabe(replace(fk, grundstueckspreis=D(1500000)), VG, KATN, "markt_miete", D("10"), D("30"), D("0.01"))
    print("  noetige Miete bei 1,5 Mio Grundstueck mit KfW:", s["status"], [l["wert"] for l in s["loesungen"]])

# ---------------------------------------------------------------- Fall 4 gefoerderter Neubau NBank
F4 = replace(F3, kostenkennwert=D(3300), markt_miete=D("15.00"),
             foerderung=replace(A.FOERDERUNG_B), bodenrichtwert=D(450), haltedauer=38)
if "4" in WAHL:
    print("FALL 4 gefoerderter Neubau (Objekt aus Fall 3, KKW 3.300 als KG 300/400, Gruppe B, BRW 450, Grst 2,0 Mio)")
    for n in (20, 36, 38, 40, 42):
        try:
            e = rechne_grob(replace(F4, haltedauer=n), VG, KATN)
            zeige(f"Haltedauer {n}", e)
            if n == 38:
                bm = e.bemessung
                print(f"   FD {eur(bm.foerderdarlehen)} Zuschuss {eur(bm.zuschuss)} EKmin {eur(bm.ek_min)} RE_n {eur(bm.ertrag_nachhaltig)}"
                      f" KD uebrige {eur(bm.kd_uebrige)}")
                print("   ohne Bankdarlehen (R-11.15):", {k: (round(v, 4) if v is not None else None) for k, v in (e.ohne_bankdarlehen or {}).items()})
                print("   Nachschuss je Planjahr 1..14:", [eur(x) for x in e.nachschuss_je_jahr[1:15]])
                print("   Meldungstexte:", [(m["kennung"], m["text"][:120]) for m in e.meldungen])
        except Exception as x:
            print(f"  Haltedauer {n}: {type(x).__name__} {x}")
    tp("Haltedauer 38, Ziel 5 %", F4, VG, KATN)
    tp("Haltedauer 38, Ziel 3,5 %", F4, replace(VG, zielrendite=D("0.035")), KATN)
    tp("Haltedauer 38, Ziel 3 %", F4, replace(VG, zielrendite=D("0.03")), KATN)
    tp("Haltedauer 38 mit KfW 3,6 Mio, Ziel 3 %", replace(F4, kfw_betrag=D(3600000)), replace(VG, zielrendite=D("0.03")), KATN)
    zeige("mit KfW 3,6 Mio, Grst 2,0 Mio", rechne_grob(replace(F4, kfw_betrag=D(3600000)), VG, KATN))
