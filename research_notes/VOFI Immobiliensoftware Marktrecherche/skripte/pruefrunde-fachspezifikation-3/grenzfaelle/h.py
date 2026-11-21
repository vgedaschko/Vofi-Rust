"""Hilfen fuer die Grenzfaelle der Pruefrunde 3. Importiert den Referenzrechner unveraendert aus ../../referenzrechner
(nur lesend; PYTHONDONTWRITEBYTECODE=1 setzen). Jeder Aufruf faengt Abstuerze und meldet sie als ABSTURZ."""
import sys, os, traceback
sys.dont_write_bytecode = True
RR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "referenzrechner"))
sys.path.insert(0, RR)
from decimal import Decimal as D
from dataclasses import replace
import annahmen as A
import grobkalkulation as G
from grobkalkulation import (rechne_grob, tragbarer_preis, suche_eingabe, kalkuliere, haltedauer_tabelle, Meldung,
                             Stress)
from steuer import KOERPERSCHAFT, PRIVAT, GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN, BEFREIT, KOERPERSCHAFT_OHNE_GEWST
from zahlen import de, proz

NULL = D(0)
ANK = replace(A.ANKAUF, stau_betrag=NULL, stau_jahr=None)
VG = A.VORGABEN
KAT = A.KATALOG
NB = A.NEUBAU
KATN = A.KATALOG_NEUBAU
GEF = replace(A.NEUBAU, foerderung=A.FOERDERUNG_B, haltedauer=38)
KFWF = replace(A.NEUBAU, kfw_betrag=D(3000000), kfw_laufzeit=35, kfw_tilgungsfrei=1)


def r4(x):
    return None if x is None else round(x, 4)


def wo(x):
    tb = traceback.extract_tb(x.__traceback__)[-1]
    return f"{type(x).__name__}: {str(x)[:100]} @ {os.path.basename(tb.filename)}:{tb.lineno} {tb.name}"


def kalk(ein, vg=VG, kat=KAT, **kw):
    try:
        r = kalkuliere(ein, vg, kat, **kw)
    except Exception as x:
        return "ABSTURZ", wo(x)
    if r["status"] == "eingabe":
        return "eingabe", r["meldungen"][0]["kennung"] + " " + r["meldungen"][0]["text"][:140]
    return r["status"], r["ergebnis"]


def kurz(e):
    if e.gesperrt:
        return f"GESPERRT {e.befunde[:4]}"
    k = e.kennzahlen
    b = e.bemessung.bank
    r = proz(k['rendite']) if k['rendite'] is not None else None
    return (f"EW {de(e.plan.endwert)} | dEW {de(k['endwertdifferenz'])} | r {r} | L {de(e.darlehen)} {b['bindend']} "
            f"| EK0 {de(e.eigenkapital_investitionsphase)} | NS {de(e.nachschuss_laufend)} | FB {de(e.fehlbetrag_verkauf)} "
            f"| M {[m['kennung'] for m in e.meldungen]}")


def zeig(ein, vg=VG, kat=KAT, extra=None, **kw):
    s, e = kalk(ein, vg, kat, **kw)
    if s in ("eingabe", "ABSTURZ"):
        return f"[{s}] {e}"
    out = f"[{s}] " + kurz(e)
    if extra and s == "ergebnis":
        try:
            out += " || " + extra(e)
        except Exception as x:
            out += " || extra ABSTURZ " + wo(x)
    return out


def tp(ein, vg=VG, kat=KAT, **kw):
    try:
        t = tragbarer_preis(ein, vg, kat, **kw)
    except Exception as x:
        return "ABSTURZ " + wo(x)
    return (f"Preis {t['preis']} bindend {t['bindend']} Meldung {t['meldung']} {t.get('meldungen')} "
            f"R-Grenze {t['renditegrenze']} EK-Grenze {t['ek_grenze']} U {t['unten']} O {t['oben']} "
            f"Neben {t.get('nebenangabe')}" + (f" Text {t.get('text','')[:110]}" if t.get('text') else ""))


def zws(ein, vg, kat, feld, u, o, s, **kw):
    try:
        r = suche_eingabe(ein, vg, kat, feld, u, o, s, **kw)
    except Exception as x:
        return "ABSTURZ " + wo(x)
    return f"{r['status']} {[(l['wert'], l.get('richtung')) for l in r['loesungen']]} M {r['meldungen']} unz {len(r['unzulaessig'])}"


def hdt(ein, vg, kat, von, bis, **kw):
    try:
        return haltedauer_tabelle(ein, vg, kat, von, bis, **kw)
    except Exception as x:
        return "ABSTURZ " + wo(x)
