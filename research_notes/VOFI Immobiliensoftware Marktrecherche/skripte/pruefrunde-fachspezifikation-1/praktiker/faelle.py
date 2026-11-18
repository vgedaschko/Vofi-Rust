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


# ---------------------------------------------------------------- Fall 1 Exposé Bestand mit Investitionsstau
print("FALL 1 Bestand mit Investitionsstau (24 WE, 1.560 m2, Bj. 1968, NI)")
F1 = replace(A.ANKAUF, wohnflaeche=D(1560), einheiten=24, kaufpreis=D(2650000), enk_satz=D("0.10"),
             bodenanteil=D("0.20"), ist_miete=D("7.20"), markt_miete=D("8.80"), anpassungsdauer=5,
             stau_betrag=D(420000), stau_jahr=1, stau_art="erhaltung", co2_je_qm=D("1.20"),
             co2_steigerung=D("0.05"), verkaufsfaktor=D(19), haltedauer=12)
zeige("Angebot 2,65 Mio", rechne_grob(F1, VG))
t1 = tp("Basis", F1, VG)
tp("Stress", F1, VG, stress=True)
tp("Stau als Modernisierung (aktiviert)", replace(F1, stau_art="modernisierung"), VG)
tp("Stau zum Stichtag (k=0)", replace(F1, stau_jahr=0), VG)
tp("Stau +20 % (nicht im Stressfall)", replace(F1, stau_betrag=D(504000)), VG)
tp("Marktmiete = Angebotsmiete 10,00", replace(F1, markt_miete=D("10.00")), VG)
tp("verfuegbares EK 1,2 Mio", replace(F1, verfuegbares_ek=D(1200000)), VG)
# ---------------------------------------------------------------- Fall 2 gebundener Bestand
print("FALL 2 gebundener Bestand (40 WE, 2.800 m2, Bindung 8 Jahre, uebernommenes Foerderdarlehen 1,1 Mio)")
F2 = replace(A.ANKAUF, wohnflaeche=D(2800), einheiten=40, kaufpreis=D(3400000), enk_satz=D("0.10"),
             bodenanteil=D("0.25"), ist_miete=D("6.10"), markt_miete=D("8.50"), anpassungsdauer=4,
             stau_betrag=D(0), co2_je_qm=D("0.40"), co2_steigerung=D("0.05"), verkaufsfaktor=D(17),
             haltedauer=12, gebunden_anteil=D(1), bindung_jahre=8, gebundene_miete=D("6.10"),
             geb_steigerung=D("0.0615"),
             uebernommen=dict(restschuld=D(1100000), zins=D("0.005"), tilgungssatz=D("0.02"), bindung_jahre=8))
try:
    rechne_grob(F2, VG)
    print("  ohne Anschlusszins: gerechnet")
except (Meldung, ValueError) as m:
    print("  ohne Anschlusszins des uebernommenen Darlehens:", str(m)[:90])
F2a = replace(F2, uebernommen=dict(F2.uebernommen, anschluss_zins=D("0.05")))
zeige("Angebot 3,4 Mio, Anschluss 5 %", rechne_grob(F2a, VG))
zeige("andere Lesart MA-026", rechne_grob(F2a, replace(VG, nur_eigenes_darlehen=True)))
tp("Basis", F2a, VG)
tp("andere Lesart MA-026", F2a, replace(VG, nur_eigenes_darlehen=True))
tp("Stress", F2a, VG, stress=True)
F2b = replace(F2a, uebernommen=dict(F2a.uebernommen, anschluss_zins=D("0.015")))
tp("Anschluss = alter Zins + 1 Pkt (1,5 %)", F2b, VG)
F2c = replace(F2a, uebernommen=dict(F2a.uebernommen, bindung_jahre=14))
e2c = rechne_grob(F2c, VG)
print("  Zinsbindung uebernommen 14 J. > Haltedauer: Vorfaelligkeit in N:", eur(e2c.plan.zeilen[e2c.plan.e.raster.N]["vfe"]))
# ---------------------------------------------------------------- Fall 3 Neubau frei mit KfW
print("FALL 3 Neubau frei finanziert (36 WE, 2.450 m2, BGF 3.400, KKW 3.300, Bauzeit 22)")
F3 = replace(A.NEUBAU, wohnflaeche=D(2450), einheiten=36, bgf=D(3400), kostenkennwert=D(3300),
             grundstueckspreis=D(2000000), grundstuecksflaeche=D(3200), bauzeit_monate=22, enk_satz=D("0.065"),
             markt_miete=D("15.00"), verkaufsfaktor=D(25), haltedauer=15)
zeige("Grundstueck 2,0 Mio", rechne_grob(F3, VGN))
tp("Basis nur Bank 4 %", F3, VGN)
tp("Instandhaltung 9 EUR/m2 statt 14", F3, replace(VGN, instandhaltung_je_qm=D(9)))
# Mischzins-Naeherung: KfW 3,6 Mio zu angenommen 2,5 % nominal, Rest Bank 4 %
L = rechne_grob(F3, VGN).darlehen
for _ in range(6):
    kfw = min(D(3600000), L)
    i = (kfw * D("0.025") + (L - kfw) * D("0.04")) / L
    L = rechne_grob(replace(F3, zins=i), VGN).darlehen
print(f"  Mischzins {i*100:.3f} %, Darlehen gesamt {eur(L)}")
tp("Naeherung mit KfW-Tranche (Mischzins)", replace(F3, zins=i), VGN)
tp("Stress nur Bank", F3, VGN, stress=True)
# ---------------------------------------------------------------- Fall 4 gefoerderter Neubau NBank
print("FALL 4 gefoerderter Neubau (Objekt aus Fall 3, Gruppe B, Bodenrichtwert 450)")
F4 = replace(F3, foerderung=replace(A.FOERDERUNG_B, bodenrichtwert=D(450)), haltedauer=20)
e4 = rechne_grob(F4, VGN)
zeige("Grundstueck 2,0 Mio", e4)
bm = e4.bemessung
print(f"  Foerderdarlehen {eur(bm.foerderdarlehen)} Zuschuss {eur(bm.zuschuss)} EKmin {eur(bm.ek_min)} KD Foerder {eur(bm.kd_uebrige)} RE {eur(bm.reinertrag_vj)} "
      f"Deckung nur Foerder {bm.reinertrag_vj/bm.kd_uebrige:.3f}")
C = bm.bank["c"]
kd_rest = C * (D("0.04") + D("0.02"))
print(f"  Restfinanzierung C {eur(C)}: noetige Mindestdeckung, damit die Bank C gibt: {bm.reinertrag_vj/(bm.kd_uebrige+kd_rest):.3f}")
zeige("andere Lesart MA-026", rechne_grob(F4, replace(VGN, nur_eigenes_darlehen=True)))
tp("Basis", F4, VGN)
tp("andere Lesart", F4, replace(VGN, nur_eigenes_darlehen=True))
tp("Instandhaltung 9", F4, replace(VGN, instandhaltung_je_qm=D(9)))
tp("Stress", F4, VGN, stress=True)
