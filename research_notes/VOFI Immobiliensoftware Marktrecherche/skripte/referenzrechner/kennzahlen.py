"""Kapitel 10 der Fachspezifikation: Kennzahlen (R-10.1 bis R-10.23).

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
    Entlastungssatz s_FK der Sollzinsen entlastet (R-7.14)."""
    r = plan.e.raster
    st = Steuer(plan.e.steuer, r, plan.e.rundung)
    return sum(plan.jahressumme("zins", j) * (EINS - st.grenzsatz_sollzinsen(j)) for j in range(1, r.n + 1))


def investitionsbarwert(plan, w, phase_ende):
    """R-10.11: a_0 = Investitionsauszahlungen der Investitionsphase (Zeitpunkt 0 bis phase_ende), mit dem
    Vergleichsfaktor auf den Stichtag abgezinst. Beim Ankauf ist das die Auszahlung zum Stichtag."""
    return sum(plan.zeilen[u]["investition"] * w[u] for u in range(phase_ende + 1)) / w[0]


def kapitaldienst(plan, perioden, je_tranche=False):
    """R-10.14: Zins, planmaessige Tilgung und laufende Beitraege aller Darlehen einer Zeitspanne."""
    kd = {tr.name: NULL for tr in plan.e.tranchen}
    for u in perioden:
        for tr in plan.e.tranchen:
            t = plan.zeilen[u]["tranchen"][tr.name]
            kd[tr.name] += t["zins"] + t["beitrag"] + (NULL if tr.art == "frei" else t["tilgung"])
    return kd if je_tranche else sum(kd.values(), NULL)


def zinsdeckung(plan, perioden):
    """R-10.20: Reinertrag / (Zinsen + laufende Beitraege aller Darlehen)."""
    re = sum(plan.zeilen[u]["miete"] - plan.zeilen[u]["kosten"] for u in perioden)
    zi = sum(plan.zeilen[u]["zins"] + plan.zeilen[u]["beitrag"] for u in perioden)
    return re / zi if zi > 0 else None


def kapitaldienstreserve(reinertrag, kd, mindestdeckung):
    """R-10.21: Reinertrag - Mindestdeckung x Kapitaldienst, in Euro."""
    return reinertrag - mindestdeckung * kd


def deckungsgrenzen(sollmiete, mieteinzahlung, kosten, kd):
    """R-10.22: Anteil der heutigen Miete, bei dem die Deckung genau 1 ist, und Mietausfall (Anteil der
    Sollmiete), bis zu dem sie mindestens 1 bleibt. None ohne Miete."""
    if mieteinzahlung <= 0 or sollmiete <= 0:
        return None, None
    return (kosten + kd) / mieteinzahlung, EINS - (kosten + kd) / sollmiete


def schuldendienstdeckung(plan, j=None, perioden=None):
    """R-10.14: Reinertrag / Kapitaldienst (Zins, planmaessige Tilgung, laufende Beitraege aller Darlehen;
    ohne Abloesung, Vorfaelligkeit, freie Tilgung und Kontokorrent)."""
    per = perioden if perioden is not None else plan.e.raster.perioden(j)
    re = sum(plan.zeilen[u]["miete"] - plan.zeilen[u]["kosten"] for u in per)
    kd = kapitaldienst(plan, per)
    return (re / kd if kd > 0 else None), re, kd


def interner_zinsfuss(reihe, unten, oben, raster, p=1):
    """R-10.18: alle internen Zinsfuesse einer Zahlungsreihe im Suchbereich (effektiv je Jahr).

    Suchbereich und Rasterzahl sind Vorgaben (H-21). Rueckgabe (loesungen, vorzeichenwechsel, status).
    Null Wechsel: keine Loesung. Wechsel ohne Fund: "Loesung ausserhalb des Suchbereichs". Mehr als ein
    Wechsel: alle Loesungen im Bereich werden gemeldet; massgeblich bleibt die VOFI-Rendite.
    """
    unten, oben = d(unten), d(oben)
    werte = [x for x in reihe if x != 0]
    wechsel = sum(1 for a, b in zip(werte, werte[1:]) if (a > 0) != (b > 0))
    if wechsel == 0:
        return [], 0, "keine Loesung"

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
    if not loesungen:
        status = "Loesung ausserhalb des Suchbereichs"
    else:
        status = "eine Loesung" if len(loesungen) == 1 else f"{len(loesungen)} Loesungen"
    return loesungen, wechsel, status


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


def renditemeldungen(einlagen, entnahmen, kz):
    """R-10.6, R-10.7: Meldungen zur Rendite als Liste (Kennung, Text).
    M-27: Einlagen nach dem Stichtag treffen mit Entnahmen zusammen. M-28: keine Einlage. M-29: Zaehler nicht positiv."""
    m = []
    if any(x > 0 for x in einlagen[1:]) and any(x > 0 for x in entnahmen):
        m.append(("M-27", "Einlagen nach dem Stichtag und Entnahmen treffen zusammen; die Rendite haengt von ihrem Zeitpunkt ab"))
    if kz["rendite"] is None:
        m.append(("M-28", "Rendite nicht definiert: keine Einlage"))
    elif kz["zaehler"] <= 0:
        m.append(("M-29", "Rendite -100 %: Zaehler nicht positiv"))
    return m


def meldung_izf(loesungen):
    """R-10.18: Hinweis M-26, wenn der interne Zinsfuss mehrdeutig ist."""
    if len(loesungen) > 1:
        return ("M-26", "Interner Zinsfuss mehrdeutig; alle Loesungen sind genannt, massgeblich ist die VOFI-Rendite")
    return None
