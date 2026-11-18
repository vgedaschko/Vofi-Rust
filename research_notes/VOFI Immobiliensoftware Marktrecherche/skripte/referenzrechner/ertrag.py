"""Kapitel 6 der Fachspezifikation: Ertraege und laufende Auszahlungen der Grobkalkulation (R-6.1 bis R-6.12)."""
from decimal import Decimal as D
from zahlen import NULL, EINS, d


def indexreihe(jahre, steigerung, rd):
    """R-6.1: Indexstand je Jahr 1..jahre; Jahr 1 = 1 (der Eingabewert gilt fuer das erste Jahr).
    Fortschreibung Index_j = Index_(j-1) x (1 + Steigerung), auf zwoelf Nachkommastellen (R-12.4)."""
    idx = [None, EINS]
    for j in range(2, jahre + 1):
        idx.append(rd.satz(idx[-1] * (EINS + steigerung)))
    return idx


def anpassungspfad(start, markt, ab_jahr, dauer, kappung, kappung_jahre=3):
    """R-6.3: Annaeherung einer Ausgangsmiete an die Marktmiete.

    start    Miete je Quadratmeter und Monat im Jahr ab_jahr (Ist-Miete oder letzte gebundene Miete)
    markt    Liste der Marktmiete je Jahr (Index 1..J)
    dauer    Anpassungsdauer in Jahren: im Jahr ab_jahr + dauer ist die Marktmiete erreicht
    kappung  hoechste Steigerung innerhalb von kappung_jahre Jahren (Katalogwert, BGB-558)
    Rueckgabe: {Jahr: Miete} fuer ab_jahr..J.
    """
    J = len(markt) - 1
    pfad = {}
    for j in range(ab_jahr, J + 1):
        k = j - ab_jahr                                   # 0 im ersten Jahr
        anteil = EINS if dauer == 0 else min(EINS, D(k) / D(dauer))
        m = start + (markt[j] - start) * anteil
        basis = pfad[j - kappung_jahre] if (j - kappung_jahre) >= ab_jahr else start
        m = min(m, basis * (EINS + kappung))              # Kappung wirkt nur nach oben
        pfad[j] = m
    return pfad


def gebundene_miete(start, jahre, steigerung, fest_jahre=3, schritt_jahre=3):
    """R-6.5: gebundene Miete: fest_jahre unveraendert, danach je schritt_jahre hoechstens 'steigerung'."""
    pfad = {}
    for j in range(1, jahre + 1):
        stufe = 0 if j <= fest_jahre else (j - fest_jahre - 1) // schritt_jahre + 1
        pfad[j] = start * (EINS + steigerung) ** stufe
    return pfad


def mietreihe_je_qm(jahre, ist, markt1, steigerung, dauer, kappung, rd, gebunden_anteil=NULL,
                    gebunden_start=None, bindung_jahre=0, geb_steigerung=NULL, geb_fest=3, geb_schritt=3):
    """R-6.2 bis R-6.6: Miete je Quadratmeter und Monat fuer die Jahre 1..jahre als Mischung aus freiem
    und gebundenem Flaechenanteil. bindung_jahre = Zahl der Jahre, in denen die Bindung noch gilt."""
    idx = indexreihe(jahre, steigerung, rd)
    markt = [None] + [markt1 * idx[j] for j in range(1, jahre + 1)]
    frei = anpassungspfad(ist, markt, 1, dauer, kappung)
    if gebunden_anteil == 0:
        return [None] + [frei[j] for j in range(1, jahre + 1)], markt
    start = ist if gebunden_start is None else gebunden_start
    geb = gebundene_miete(start, jahre, geb_steigerung, geb_fest, geb_schritt)
    geb = {j: min(geb[j], markt[j]) for j in geb}        # nie ueber der Marktmiete
    if bindung_jahre < jahre:                             # nach Bindungsende: Anpassungspfad (R-6.6)
        letzte = geb[bindung_jahre] if bindung_jahre >= 1 else start
        nach = anpassungspfad(letzte, markt, bindung_jahre + 1, dauer, kappung)
        # das erste Jahr nach der Bindung traegt noch die letzte gebundene Miete (wie Jahr 1 die Ist-Miete)
        for j in range(bindung_jahre + 1, jahre + 1):
            geb[j] = nach[j]
    misch = [None] + [gebunden_anteil * geb[j] + (EINS - gebunden_anteil) * frei[j] for j in range(1, jahre + 1)]
    return misch, markt


def monatsbetrag(jahresbetrag, p, rd):
    """R-6.8: laufende Zahlung je Periode = Jahresbetrag / p, je Zahlung auf Cent gerundet (R-12.3)."""
    return rd.geld(jahresbetrag / p)
