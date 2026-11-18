"""Kapitel 12 der Fachspezifikation: Dezimalrechnung, Rundung, Saetze.

Regeln R-12.1 bis R-12.7. Kein Produktcode; Referenzrechner zur Fachspezifikation Rechenkern, Teil 1.
"""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP, ROUND_DOWN, ROUND_FLOOR

getcontext().prec = 60          # R-12.1: Rechengenauigkeit weit ueber den 12 Rechenstellen
NULL, EINS = D(0), D(1)
CENT = D("0.01")
STELLEN12 = D("1E-12")


def d(x):
    """Wandelt Eingaben exakt in Decimal (nie ueber float)."""
    if isinstance(x, D):
        return x
    if isinstance(x, float):
        raise TypeError("Gleitkommazahl als Eingabe ist unzulaessig (R-12.1): " + repr(x))
    return D(str(x))


class Rundung:
    """R-12.2/R-12.3: Rundungsverhalten eines Rechenlaufs.

    modus "cent":  Produktregel. Jede Zahlung wird nach ihrer Zahlungsart auf Cent gerundet,
                   abgeleitete Saetze und Indexstaende auf zwölf Nachkommastellen.
    modus "keine": Lehrbuchvergleich. Es wird nichts gerundet; verglichen wird der gerundete Endwert.
    """

    def __init__(self, modus="cent"):
        assert modus in ("cent", "keine")
        self.modus = modus

    def geld(self, x, art="kaufm"):
        if self.modus == "keine" or art == "keine":
            return x
        if art == "kaufm":
            return x.quantize(CENT, ROUND_HALF_UP)
        if art == "ab":                       # Abschneiden (andere Lesart MA-013)
            return x.quantize(CENT, ROUND_DOWN)
        raise ValueError(art)

    def satz(self, x):
        """R-12.4: abgeleitete Saetze, Faktoren und Indexstaende auf zwoelf Nachkommastellen."""
        return x if self.modus == "keine" else x.quantize(STELLEN12, ROUND_HALF_UP)


def ab_cent(x):
    """Abrunden auf Cent zur sicheren Seite (Darlehenshoehe, R-5.12)."""
    return x.quantize(CENT, ROUND_FLOOR)


def ab_hundert(x):
    """Abrunden auf volle 100 Euro (Gewerbeertrag, GEWSTG-11)."""
    return (x / 100).to_integral_value(ROUND_FLOOR) * 100


def kaufm(x, stellen="0.01"):
    return x.quantize(D(stellen), ROUND_HALF_UP)


def periodensatz_konform(jahressatz, p, rd):
    """R-2.6: effektiver Jahreszins -> konformer Periodensatz (1+i)^(1/p) - 1."""
    if p == 1:
        return jahressatz
    return rd.satz((EINS + jahressatz) ** (EINS / D(p)) - EINS)


def wurzel_rendite(verhaeltnis, n_jahre):
    """(Verhaeltnis)^(1/n) - 1 mit voller Genauigkeit (Kennzahlen werden nicht gerundet, R-12.6)."""
    return verhaeltnis ** (EINS / d(n_jahre)) - EINS


def de(x, nd=2):
    """Deutsche Zahldarstellung fuer die Ausgabe."""
    if x is None:
        return "n. def."
    x = d(x)
    q = D(1).scaleb(-nd)
    s = f"{x.quantize(q, ROUND_HALF_UP):,.{nd}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def proz(x, nd=3):
    return "n. def." if x is None else de(x * 100, nd) + " %"
