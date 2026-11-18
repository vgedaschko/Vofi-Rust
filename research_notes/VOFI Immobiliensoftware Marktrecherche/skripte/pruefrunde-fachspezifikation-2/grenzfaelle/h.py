"""Hilfen fuer die Grenzfaelle der Pruefrunde 2 (Referenzrechner-Kopie in ./rr, unveraendert)."""
import sys, os, traceback
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "rr"))
from decimal import Decimal as D
from dataclasses import replace
import annahmen as A
import grobkalkulation as G
from grobkalkulation import rechne_grob, tragbarer_preis, suche_eingabe, kalkuliere, zielwertsuche, Meldung
from zahlen import de, proz

NULL = D(0)
ANK = replace(A.ANKAUF, stau_betrag=NULL)      # Ankauf ohne Investitionsstau als neutrale Basis
VG = A.VORGABEN
KAT = A.KATALOG
NB = A.NEUBAU
KATN = A.KATALOG_NEUBAU


def r4(x):
    return None if x is None else round(x, 4)


def kurz(e):
    if e.gesperrt:
        return f"GESPERRT {e.befunde[:4]}"
    k = e.kennzahlen
    b = e.bemessung.bank
    return (f"EW {de(e.plan.endwert)} | dEW {de(k['endwertdifferenz'])} | r {proz(k['rendite']) if k['rendite'] is not None else None} "
            f"| L {de(e.darlehen)} {b['bindend']} | EK0 {de(e.eigenkapital_investitionsphase)} | NS {de(e.nachschuss_laufend)} "
            f"| FB {de(e.fehlbetrag_verkauf)} | VK {de(e.verkauf.preis_brutto)} | M {[m['kennung'] for m in e.meldungen]}")


def kalk(ein, vg=VG, kat=KAT, **kw):
    """Aufruf ueber kalkuliere (soll nie abstuerzen). Rueckgabe (status, ergebnis oder Text)."""
    try:
        r = kalkuliere(ein, vg, kat, **kw)
    except Exception as x:
        return "ABSTURZ", f"{type(x).__name__}: {x} @ {traceback.extract_tb(x.__traceback__)[-1].name}"
    if r["status"] == "eingabe":
        return "eingabe", r["meldungen"][0]["kennung"] + " " + r["meldungen"][0]["text"][:110]
    return r["status"], r["ergebnis"]


def zeig(ein, vg=VG, kat=KAT, extra=None, **kw):
    s, e = kalk(ein, vg, kat, **kw)
    if s in ("eingabe", "ABSTURZ"):
        return f"[{s}] {e}"
    out = f"[{s}] " + kurz(e)
    if extra and s == "ergebnis":
        out += " || " + extra(e)
    return out


def tp(ein, vg=VG, kat=KAT, **kw):
    try:
        t = tragbarer_preis(ein, vg, kat, **kw)
    except Exception as x:
        return f"ABSTURZ {type(x).__name__}: {x} @ {traceback.extract_tb(x.__traceback__)[-1].name}"
    e = t.get("ergebnis")
    zus = ""
    if e is not None and not e.gesperrt:
        k = e.kennzahlen
        zus = (f" | EK0 {de(e.eigenkapital_investitionsphase)} D {de(k['nenner'])} r "
               f"{proz(k['rendite']) if k['rendite'] is not None else 'n.d.'} EW {de(e.plan.endwert)}")
    return (f"Preis {t['preis']} bindend {t['bindend']} Meldung {t['meldung']} {t.get('meldungen')} "
            f"Rendite-Grenze {t['renditegrenze']} EK-Grenze {t['ek_grenze']} U {t['unten']} O {t['oben']}{zus}"
            + (f" Text {t.get('text','')[:90]}" if t.get('text') else ""))
