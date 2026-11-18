"""Kapitel 10 der Fachspezifikation: Kennzahlen (R-10.1 bis R-10.19).

Kennzahlen werden nicht gerundet (R-12.6); gerundet wird nur fuer die Darstellung.
"""
from decimal import Decimal as D
from zahlen import NULL, EINS, d, wurzel_rendite
from steuer import Steuer

MINUS_HUNDERT = D(-1)


def vergleichsfaktoren(e):
    """R-10.4: Aufzinsungsfaktor je Periode zum kurzfristigen Habenzins nach Steuern.

    f_u = (1 + h_kurz x (1 - s_Z(j)))^(1/p) fuer Periode u im Planjahr j. Rueckgabe: Liste w mit
    w[t] = Produkt der f_u fuer u = t+1..N (Aufzinsung von t auf N); w[N] = 1.
    """
    r, rd = e.raster, e.rundung
    st = Steuer(e.steuer, r, rd)
    f = [EINS] * (r.N + 1)
    for u in range(1, r.N + 1):
        k = e.h_kurz * (EINS - st.grenzsatz_zinsen(r.planjahr(u)))
        f[u] = rd.satz((EINS + k) ** (EINS / D(r.p))) if r.p > 1 else EINS + k
    w = [EINS] * (r.N + 1)
    for t in range(r.N - 1, -1, -1):
        w[t] = w[t + 1] * f[t + 1]
    return w


def zaehler_nenner(endwert, einlagen, entnahmen, w):
    """R-10.5: Zaehler Z = Endwert + aufgezinste Entnahmen; Nenner D = auf den Beginn abgezinste Einlagen."""
    Z = endwert + sum(a * w[t] for t, a in enumerate(entnahmen))
    Dn = sum(x * w[t] for t, x in enumerate(einlagen)) / w[0]
    return Z, Dn


def vofi_rendite(endwert, einlagen, entnahmen, w, n_jahre):
    """R-10.5/R-10.7: VOFI-Eigenkapitalrendite mit Randfaellen. Rueckgabe (r, Z, D, status)."""
    Z, Dn = zaehler_nenner(endwert, einlagen, entnahmen, w)
    if Dn == 0:
        return None, Z, Dn, "nicht definiert (kein Eigenkapital)"
    if Z <= 0:
        return MINUS_HUNDERT, Z, Dn, "Zaehler nicht positiv: -100 %"
    return wurzel_rendite(Z / Dn, n_jahre), Z, Dn, "ok"


def endwertueberschuss(Z, Dn, zielrendite, n_jahre):
    """R-10.9: Betrag, um den der Zaehler den Zaehler bei genau der Zielrendite uebertrifft."""
    return Z - Dn * (EINS + zielrendite) ** d(n_jahre)


def gesamtkapitalrendite(Z, Dn, sollzinsen_nach_steuern, a0, n_jahre):
    """R-10.11 (GABLER-BANKLEXIKON-GKR, MA-028): ((Z - D + Z_S nach Steuern + a_0) / a_0)^(1/n) - 1."""
    zaehler = Z - Dn + sollzinsen_nach_steuern + a0
    if a0 <= 0:
        return None
    if zaehler <= 0:
        return MINUS_HUNDERT
    return wurzel_rendite(zaehler / a0, n_jahre)


def sollzinsen_nach_steuern(plan):
    """MA-028: einfache Summe der Sollzinsen aller Darlehen ohne Kontokorrent, je Jahr um den
    Grenzsteuersatz auf operative Ertraege entlastet."""
    r = plan.e.raster
    st = Steuer(plan.e.steuer, r, plan.e.rundung)
    return sum(plan.jahressumme("zins", j) * (EINS - st.grenzsatz_operativ(j)) for j in range(1, r.n + 1))


def schuldendienstdeckung(plan, j=None, perioden=None):
    """R-10.14: Reinertrag / Kapitaldienst (Zins, planmaessige Tilgung, laufende Beitraege aller Darlehen;
    ohne Abloesung, Vorfaelligkeit, freie Tilgung und Kontokorrent)."""
    per = perioden if perioden is not None else plan.e.raster.perioden(j)
    re = sum(plan.zeilen[u]["miete"] - plan.zeilen[u]["kosten"] for u in per)
    kd = NULL
    for u in per:
        for tr in plan.e.tranchen:
            t = plan.zeilen[u]["tranchen"][tr.name]
            kd += t["zins"] + t["beitrag"] + (NULL if tr.art == "frei" else t["tilgung"])
    return (re / kd if kd > 0 else None), re, kd


def interner_zinsfuss(reihe, p=1, unten=D("-0.99"), oben=D("10"), raster=2000):
    """R-10.18: alle internen Zinsfuesse einer Zahlungsreihe im Suchbereich (effektiv je Jahr).

    Rueckgabe (loesungen, vorzeichenwechsel). Null Wechsel: keine Loesung. Mehr als ein Wechsel:
    alle Loesungen im Bereich werden gemeldet; massgeblich bleibt die VOFI-Rendite.
    """
    werte = [x for x in reihe if x != 0]
    wechsel = sum(1 for a, b in zip(werte, werte[1:]) if (a > 0) != (b > 0))
    if wechsel == 0:
        return [], 0

    def kw(rj):
        q = (EINS + rj) ** (EINS / D(p))
        return sum(x / q ** t for t, x in enumerate(reihe) if x != 0)

    loesungen = []
    schritt = (oben - unten) / raster
    x0, f0 = unten, kw(unten)
    for i in range(1, raster + 1):
        x1 = unten + schritt * i
        f1 = kw(x1)
        if f0 == 0:
            loesungen.append(x0)
        elif (f0 > 0) != (f1 > 0) and f1 != 0:
            lo, hi, flo = x0, x1, f0
            for _ in range(80):
                mid = (lo + hi) / 2
                fm = kw(mid)
                if (fm > 0) == (flo > 0):
                    lo, flo = mid, fm
                else:
                    hi = mid
            loesungen.append((lo + hi) / 2)
        x0, f0 = x1, f1
    if f0 == 0:
        loesungen.append(x0)
    return loesungen, wechsel


def kapitalwert(reihe, zins_periode):
    q = EINS + zins_periode
    return sum(x / q ** t for t, x in enumerate(reihe))


def amortisationsdauer(vermoegen, vergleich, lesart="alternative", eigenkapital=None):
    """R-10.12 (MA-027). vermoegen[t], vergleich[t] fuer t = 1..n (Index 0 unbenutzt).

    lesart "alternative" (Voreinstellung): kleinstes t, von dem an das Vermoegen bei gedachtem Verkauf
    den Stand der Unterlassensalternative dauerhaft erreicht. lesart "eigenkapital": erstes t, in dem es
    das eingesetzte Eigenkapital erreicht. None = im Planungszeitraum nicht erreicht.
    """
    n = len(vermoegen) - 1
    if lesart == "eigenkapital":
        for t in range(1, n + 1):
            if vermoegen[t] >= eigenkapital:
                return t
        return None
    ergebnis = None
    for t in range(n, 0, -1):
        if vermoegen[t] >= vergleich[t]:
            ergebnis = t
        else:
            break
    return ergebnis


class Kennzahlenblatt(dict):
    """Ergebnis von werte_aus(): Kennzahlen eines Finanzplans mit seiner Unterlassensalternative."""


def werte_aus(plan, alt, zielrendite=None):
    """Berechnet die Kennzahlen aus Finanzplan und Unterlassensalternative (R-10.1 bis R-10.11)."""
    e = plan.e
    n = e.raster.n
    w = vergleichsfaktoren(e)
    r, Z, Dn, status = vofi_rendite(plan.endwert, plan.einlagen_netto, plan.entnahmen_netto, w, n)
    r_u, Z_u, _, status_u = vofi_rendite(alt.endwert, plan.einlagen_netto, plan.entnahmen_netto, w, n)
    k = Kennzahlenblatt(
        endwert=plan.endwert, endwert_alternative=alt.endwert, endwertdifferenz=plan.endwert - alt.endwert,
        rendite=r, rendite_status=status, vergleichsrendite=r_u, zaehler=Z, nenner=Dn, zaehler_alternative=Z_u,
        einlagen=sum(plan.einlagen_netto), entnahmen=sum(plan.entnahmen_netto),
        nachschuss=sum(plan.reihe("nachschuss")), w=w)
    if zielrendite is not None:
        k["zielrendite"] = zielrendite
        k["abstand_zielrendite"] = None if r is None else r - zielrendite
        k["endwertueberschuss"] = endwertueberschuss(Z, Dn, zielrendite, n)
    return k
