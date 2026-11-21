"""Gegenrechnung des Steuerberaters, Pruefrunde 3 zur Fachspezifikation des Rechenkerns (2026-11-21).

Teil A: Bausteine aus Kapitel 7 von Hand (Decimal), unabhaengig vom Referenzrechner.
Teil B: Szenarien mit dem Referenzrechner (nur gelesen, nicht geaendert); die Variante "Antrag nur bei positivem
Grundstuecksteil" wird zur Laufzeit ueber eine Unterklasse eingespielt, der Rechner auf der Platte bleibt unveraendert.
Aufruf: python3 gegenrechnung.py (aus diesem Ordner).
"""
import sys, os
from decimal import Decimal as D, ROUND_HALF_UP
from dataclasses import replace

def r(x):
    return D(x).quantize(D("0.01"), rounding=ROUND_HALF_UP)

def ab100(x):
    return (D(x) // 100) * 100

print("== Teil A: Bausteine Kapitel 7 ==")
kst = lambda jahr: {2027: D("0.15"), 2028: D("0.14"), 2029: D("0.13"), 2030: D("0.12"), 2031: D("0.11")}.get(jahr, D("0.15") if jahr < 2027 else D("0.10"))
zs = lambda jahr: kst(jahr) * D("1.055")
g = D("0.035") * D("4")
# R-7.7
print("R-7.7  100.000 (2027):", r(zs(2027) * 100000), r(g * 100000))
print("R-7.7  -50.000 / +80.049 (2028):", r(zs(2028) * 30049), r(g * ab100(30049)), r(zs(2028) * 30049 + g * ab100(30049)))
# R-7.8
print("R-7.8  Kennzeichen 2027:", r(zs(2027) * 110000), r(g * 10000))
print("R-7.8  Verkaufsjahr, Kuerzung entfaellt:", r(zs(2027) * 610000 + g * 610000))
print("R-7.8  Verkaufsjahr, E-69:", r(zs(2027) * 610000 + g * 10000))
print("R-7.8  Anlaufverlust 2027, Verkauf 2028 mit E-69:", r(zs(2028) * (610000 - 50000) + g * 10000))
print("R-7.8  ohne E-69 dagegen:", r(zs(2028) * 560000 + g * ab100(610000)))
print("R-7.8  RF-13 GewSt auf g_v 999.589,46:", r(g * ab100(D("999589.46"))))
# R-7.9 Tabelle
def pg(gewinn, hebesatz, anteil=D(1), satz=D("0.42")):
    est = r(satz * gewinn)
    mb = r(ab100(gewinn) - 24500) * D("0.035") if gewinn > 24500 else D(0)
    mb = r(mb)
    gst = r(mb * hebesatz)
    anr = min(anteil * 4 * mb, anteil * gst, anteil * est)
    return est, mb, gst, r(anr), r(est + gst - anr)
for h, a, s in ((D("4"), D(1), D("0.42")), (D("2.8"), D(1), D("0.42")), (D("4.8"), D(1), D("0.42")), (D("4"), D("0.5"), D("0.42")), (D("4"), D(1), D("0.08"))):
    print("R-7.9 ", h, a, s, pg(D(100000), h, a, s))
# R-7.18
def pg_verkauf(gv, h, anteil, aufgabe):
    est = D("0.42") * gv
    ge = gv * (1 - anteil) if aufgabe else gv
    mb = r((ab100(ge) - 24500) * D("0.035"))
    gst = r(mb * h)
    anr = anteil * min(4 * mb, gst)
    return r(est + gst - anr)
print("R-7.18 440 %, 60 %:", pg_verkauf(D(500000), D("4.4"), D("0.6"), False), pg_verkauf(D(500000), D("4.4"), D("0.6"), True))
# R-7.10, R-7.11, R-7.16, R-7.17
print("R-7.10", r(D("0.42") * 30000) + r(D("0.26375") * 1000), r(D("0.26375") * 500))
print("R-7.11 zehn Jahre:", r(D("0.42") * (-20000 + 200000 - 30000)))
print("R-7.16", r(zs(2027) * 100000 + g * (100000 + D("0.25") * (300000 + 20000 - 200000))), r(zs(2027) * 100000 + g * (100000 + D("0.25") * 60000)))
print("R-7.17", r(zs(2027) * 100000), r(zs(2036) * 150000), "Vortrag nach elf Jahren:", -20000 + 5000)
# R-7.15, R-7.19
print("R-7.15 Entgelt 52.314,91, Jahr 1 (10 Monate), Jahr 2:", r(D("52314.91") * 10 / 436), r(D("52314.91") * 12 / 436))
print("R-7.19 Zuschuss 6/420, 12/420; Entgelt:", r(D("1743830.47") * 6 / 420), r(D("1743830.47") * 12 / 420), r(D("13078.73") * 6 / 420), r(D("13078.73") * 12 / 420))
print("R-7.19 Entgelt 0,75 %:", r(D("1743830.47") * D("0.0075")))

print("\n== Teil B: Szenarien mit dem Referenzrechner ==")
RR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "referenzrechner"))
sys.path.insert(0, RR)
os.chdir(RR)
import types
VARIANTE = {"an": False}
_src = open(os.path.join(RR, "proben.py"), encoding="utf-8").read()
_alt = "            if kuerzung:\n                ertrag = z_h"
assert _alt in _src
_neu = ("            if kuerzung and VARIANTE['an']:\n"
        "                _h = par.hinzu_anteil * max(NULL, t.get('entgelte', NULL) + par.hinzu_pacht * t.get('pacht', NULL) - par.hinzu_freibetrag)\n"
        "                if e_op + _h < 0:\n                    kuerzung = False\n" + _alt)
_mod = types.ModuleType("proben"); _mod.__file__ = os.path.join(RR, "proben.py"); _mod.VARIANTE = VARIANTE
exec(compile(_src.replace(_alt, _neu), _mod.__file__, "exec"), _mod.__dict__)
sys.modules["proben"] = _mod
import steuer as S
import annahmen as A
from grobkalkulation import rechne_grob
from rf_grob import VG, KAT, KATN, GEFOERDERT, GRUND

orig = S.Steuer._gewerbeertrag

def ohne_antrag_im_verlustjahr(self, e_op, z_h, g_v, entgelte, pacht, fv, teile):
    """Variante: Antrag auf erweiterte Kuerzung nur, wenn der Grundstuecksteil (e_op samt Hinzurechnung) positiv ist."""
    if self._kuerzung():
        p = self.par
        frei = S.NULL if fv else p.hinzu_freibetrag
        hinzu = p.hinzu_anteil * max(S.NULL, entgelte + p.hinzu_pacht * pacht - frei)
        if e_op + hinzu < 0:
            teile["hinzurechnung"] = hinzu
            teile["gewerbeertrag"] = e_op + z_h + hinzu
            return e_op + z_h + hinzu
    return orig(self, e_op, z_h, g_v, entgelte, pacht, fv, teile)

def lauf(name, ein, kat):
    e = rechne_grob(ein, VG, kat)
    k = e.kennzahlen
    if k is None:
        print(f"  {name}: kein Ergebnis", getattr(e, "meldungen", None)); return e
    print(f"  {name}: Rendite {k['rendite']*100:.3f} %, Endwertdifferenz {k.get('endwertdifferenz')}")
    return e

K = A.steuer(S.KOERPERSCHAFT)
KK = A.steuer(S.KOERPERSCHAFT, erweiterte_kuerzung=True)
KK69 = A.steuer(S.KOERPERSCHAFT, erweiterte_kuerzung=True, kuerzung_bleibt_verkaufsjahr=True)
P = A.steuer(S.PRIVAT)
for variante in ("Rechner wie gebaut", "Antrag nur bei positivem Grundstuecksteil"):
    S.Steuer._gewerbeertrag = orig if variante.startswith("Rechner") else ohne_antrag_im_verlustjahr
    VARIANTE["an"] = not variante.startswith("Rechner")
    print(variante)
    lauf("Ankauf Koerperschaft ohne Kennzeichen", replace(A.ANKAUF, steuer=K, begruendungen=GRUND), KAT)
    lauf("Ankauf Koerperschaft E-41, E-69 nein", replace(A.ANKAUF, steuer=KK, begruendungen=GRUND), KAT)
    lauf("Ankauf Koerperschaft E-41, E-69 ja", replace(A.ANKAUF, steuer=KK69, begruendungen=GRUND), KAT)
    lauf("Neubau frei Koerperschaft ohne Kennzeichen", replace(A.NEUBAU, steuer=K, begruendungen=GRUND), KATN)
    lauf("Neubau frei Koerperschaft E-41, E-69 nein", replace(A.NEUBAU, steuer=KK, begruendungen=GRUND), KATN)
    for n in (38, 20):
        lauf(f"gefoerdert {n} J. Koerperschaft ohne Kennzeichen", replace(GEFOERDERT, steuer=K, haltedauer=n, begruendungen=GRUND), KATN)
        lauf(f"gefoerdert {n} J. Koerperschaft E-41, E-69 nein", replace(GEFOERDERT, steuer=KK, haltedauer=n, begruendungen=GRUND), KATN)
S.Steuer._gewerbeertrag = orig
VARIANTE["an"] = False

print("Privatperson Ankauf je Haltedauer (Spez.: 3,365 / 3,528 / 4,882 / 5,141 %)")
for n in (9, 10, 11, 12):
    e = lauf(f"Privatperson {n} J.", replace(A.ANKAUF, steuer=P, haltedauer=n, begruendungen=GRUND), KAT)
    print("     Steuer auf den Verkaufsgewinn:", getattr(e, "steuer_verkaufsgewinn", None))
print("Zuschuss im gefoerderten Neubau, Privatperson (Spez.: 3,808 % / 4,380 %)")
lauf("Privatperson ohne E-70", replace(GEFOERDERT, steuer=P, begruendungen=GRUND), KATN)
lauf("Privatperson mit E-70", replace(GEFOERDERT, steuer=P, zuschuss_verteilung=True, begruendungen=GRUND), KATN)
lauf("Koerperschaft (verteilt, Voreinstellung)", replace(GEFOERDERT, steuer=K, begruendungen=GRUND), KATN)
lauf("Koerperschaft mit Kennzeichen", replace(GEFOERDERT, steuer=KK, begruendungen=GRUND), KATN)
lauf("gepraegte PG 440 % mit Kennzeichen (Spez. 3,594 %)", replace(A.ANKAUF, steuer=A.steuer(S.GEPRAEGTE_PG, hebesatz=D("4.40"), erweiterte_kuerzung=True), begruendungen=GRUND), KAT)
lauf("gepraegte PG 440 %, 60 %, Kennzeichen, E-69 nein", replace(A.ANKAUF, steuer=A.steuer(S.GEPRAEGTE_PG, hebesatz=D("4.40"), anteil_natuerliche=D("0.6"), erweiterte_kuerzung=True), begruendungen=GRUND), KAT)
lauf("gepraegte PG 440 %, 60 %, Kennzeichen, E-69 ja", replace(A.ANKAUF, steuer=A.steuer(S.GEPRAEGTE_PG, hebesatz=D("4.40"), anteil_natuerliche=D("0.6"), erweiterte_kuerzung=True, kuerzung_bleibt_verkaufsjahr=True), begruendungen=GRUND), KAT)

print("Gepraegte PG 440 %, 60 % natuerliche Personen, Kennzeichen, Lesart des Hauses 'Aufgabe' (MA-036)")
for e69 in (False, True):
    lauf(f"Aufgabe, E-69 {'ja' if e69 else 'nein'}", replace(A.ANKAUF, steuer=A.steuer(S.GEPRAEGTE_PG, hebesatz=D("4.40"), anteil_natuerliche=D("0.6"), erweiterte_kuerzung=True, kuerzung_bleibt_verkaufsjahr=e69, aufgabegewinn=True), begruendungen=GRUND), KAT)

print("Rueckzahlung des Zuschusses, Verkauf nach 20 Jahren (Spez.: Privatperson sofortige Verrechnung 359.862,30 Erstattung, 2,421 %; mit E-70 1.876,05 Steuer, 2,913 %)")
for e70 in (False, True):
    for verl in ("vortrag", "sofort"):
        e = lauf(f"Privatperson 20 J., E-70 {'ja' if e70 else 'nein'}, Verlust {verl}", replace(GEFOERDERT, steuer=A.steuer(S.PRIVAT, verlust=verl), haltedauer=20, zuschuss_verteilung=e70, begruendungen=GRUND), KATN)
        if e.kennzahlen is not None:
            print("     Steuer im Verkaufsjahr:", e.plan.jahressumme("steuer", 20) if hasattr(e.plan, "jahressumme") else None)
