"""Praktiker-Pruefung Fachspezifikation Rechenkern Teil 1: vier eigene Faelle mit dem Referenzrechner."""
import sys
from dataclasses import replace
from decimal import Decimal as D
RR = "/home/user/vofi-rust/research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner"
sys.path.insert(0, RR)
import annahmen as A
from grobkalkulation import rechne_grob, tragbarer_preis, Meldung, suche_eingabe
from steuer import KOERPERSCHAFT

VG = A.VORGABEN
VGN = A.VORGABEN_NEUBAU


def eur(x):
    return "-" if x is None else f"{x:,.0f}".replace(",", ".")


def pz(x):
    return "-" if x is None else f"{x*100:.3f} %"


def zeige(titel, e):
    b = e.bemessung.bank
    print(f"  {titel}: Preis {eur(e.preis)} | Bank {eur(e.darlehen)} bindet {b['bindend']} (A {eur(b['a'])}, B {eur(b['b'])}, C {eur(b['c'])})"
          f" | EK {eur(e.eigenkapital_investitionsphase)} Nachschuss {eur(e.nachschuss_spaeter)} | DSCR {getattr(e,'dscr_vj',None) and round(e.dscr_vj,3)}"
          f" | r {pz(e.kennzahlen['rendite'])} | dEW {eur(e.kennzahlen['endwertdifferenz'])} | Meldung {b.get('meldung')}")


def tp(titel, ein, vg, stress=False):
    t = tragbarer_preis(ein, vg, stress=stress)
    e = t.get("ergebnis")
    extra = ""
    if e is not None:
        extra = f" | Bank {eur(e.darlehen)} ({e.bemessung.bank['bindend']}) EK {eur(e.eigenkapital_investitionsphase)} Nachschuss {eur(e.nachschuss_spaeter)} DSCR {round(e.dscr_vj,3)}"
    print(f"  tragbar {titel}: {eur(t['preis'])} bindet {t['bindend']} Meldung {t['meldung']}{extra}")
    return t


print("FALL 1 Bestand mit Investitionsstau (24 WE, 1.560 m2, Bj. 1968, NI)")
F1 = replace(A.ANKAUF, wohnflaeche=D(1560), einheiten=24, kaufpreis=D(2650000), enk_satz=D("0.10"),
             bodenanteil=D("0.20"), ist_miete=D("7.20"), markt_miete=D("8.80"), anpassungsdauer=5,
             stau_betrag=D(420000), stau_jahr=1, stau_art="erhaltung", co2_je_qm=D("1.20"),
             co2_steigerung=D("0.05"), verkaufsfaktor=D(19), haltedauer=12)

tp("F1 EK 1,2 Mio, Stau k=0", replace(F1, verfuegbares_ek=D(1200000), stau_jahr=0), VG)
e15 = rechne_grob(replace(F1, zinsbindung_jahre=15), VG, preis=2435602)
N = e15.plan.e.raster.N
print("  F1 Bindung 15 J., Verkauf 12: VFE", eur(e15.plan.zeilen[N]["vfe"]))
tp("F1 Bindung 15", replace(F1, zinsbindung_jahre=15), VG)
