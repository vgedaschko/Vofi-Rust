"""Kapitel 2 der Fachspezifikation: Zeitraster (R-2.1 bis R-2.9)."""
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Raster:
    """p Perioden je Jahr (12 = Monatsraster, 1 = Jahresmodus), n Planjahre, Stichtag = Zeitpunkt 0.

    Periode u (1..N) reicht von Zeitpunkt u-1 bis Zeitpunkt u; Zahlungen stehen am Periodenende.
    startjahr ist das Kalenderjahr des Stichtags E-02, in dem Planjahr 1 beginnt (R-2.8). Es ist eine
    Eingabe und hat keine Voreinstellung; Lehrbuchfaelle ohne Kalenderbezug lassen es leer.
    """
    p: int
    n: int
    startjahr: Optional[int] = None

    def __post_init__(self):
        assert self.p in (1, 12) and self.n >= 1

    @property
    def N(self):
        return self.p * self.n

    def planjahr(self, u):
        """Planjahr 1..n der Periode u >= 1; Zeitpunkt 0 gehoert zu keinem Planjahr."""
        return (u - 1) // self.p + 1

    def jahresende(self, u):
        return u >= 1 and u % self.p == 0

    def kalenderjahr(self, j):
        if self.startjahr is None:
            raise ValueError("Kalenderjahr verlangt, aber der Stichtag (E-02) fehlt")
        return self.startjahr + j - 1

    def perioden(self, j):
        return range((j - 1) * self.p + 1, j * self.p + 1)
