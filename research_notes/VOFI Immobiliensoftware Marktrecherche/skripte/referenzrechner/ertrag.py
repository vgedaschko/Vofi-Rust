"""Kapitel 6 der Fachspezifikation: Ertraege und laufende Auszahlungen der Grobkalkulation (R-6.1 bis R-6.17).

Mieten werden je Monat und je Teilflaeche (Pool) gefuehrt, ungerundet in Euro je Quadratmeter; gerundet wird
erst die Sollmiete der Periode (R-6.4). Wartefrist, Kappungsgrenze und Kappungszeitraum sind Katalogwerte
(KAT-08, BGB-558); in diesem Modul steht keiner davon als Festwert.
"""
from decimal import Decimal as D
from zahlen import NULL, EINS, d, FEHLER


def indexreihe(jahre, steigerung, rd):
    """R-6.1: Indexstand je Jahr 1..jahre; Jahr 1 = 1 (der Eingabewert gilt fuer das erste Jahr).
    Fortschreibung Index_j = Index_(j-1) x (1 + Steigerung), auf zwoelf Nachkommastellen (R-12.4)."""
    idx = [None, EINS]
    for j in range(2, jahre + 1):
        if "index_potenz" in FEHLER:    # Fehlerbild RF-16: Potenz ohne Rundung je Schritt
            idx.append((EINS + steigerung) ** (j - 1))
        else:
            idx.append(rd.satz(idx[-1] * (EINS + steigerung)))
    return idx


MONATE = 12


def jahr_von(m):
    return (m - 1) // MONATE + 1


class Mietrecht:
    """KAT-08 fuer ein Vorhaben aufgeloest (R-6.18): Wartefrist und Kappungszeitraum in Monaten; Kappungsgrenze und
    Geltung der Mietpreisbremse je Monat (sie koennen mit dem Ende einer Gebietsverordnung wechseln, MA-039)."""

    def __init__(self, wartefrist, kappung_monate, kappung, bremse, bremse_aufschlag):
        self.wartefrist, self.kappung_monate = wartefrist, kappung_monate
        self.kappung, self.bremse, self.bremse_aufschlag = kappung, bremse, bremse_aufschlag


def erhoehungspfad(start, ziel, erste, letzter, kat, t_letzte, bezug_vorher, frei_ab, senken=False):
    """R-6.3: Miete eines bestehenden Mietverhaeltnisses je Monat (BGB-558).

    start         Miete je Quadratmeter im Monat 'erste'
    ziel          Funktion Monat -> Zielmiete (Anpassungspfad zur ortsueblichen Vergleichsmiete)
    kat           Mietrecht: wartefrist (Monate), kappung(m) (Anteil im Monat der Erhoehung), kappung_monate
    t_letzte      Zeitpunkt der letzten Erhoehung (Monatsende; 0 = Stichtag, negativ = davor)
    bezug_vorher  Funktion Monat k < erste -> Bezugsmiete der Kappungsgrenze (aus der Mietenhistorie oder nach
                  MA-037); None = die Kappungsgrenze ist ausgeschoepft, keine Erhoehung
    frei_ab       erster Monat, in dem sich die Miete aendern darf
    senken        True: liegt die Zielmiete unter der Miete, folgt die Miete ihr ohne Wartefrist und Kappung, und
                  t_letzte bleibt unveraendert (Bestand am Stichtag, MA-038)
    Eine Erhoehung wirkt ab dem Monat m, wenn seit der letzten mindestens die Wartefrist vergangen ist
    (m - 1 >= t_letzte + Wartefrist) und die Kappungsgrenze gegen die Miete des Monats m - Kappungszeitraum
    Spielraum laesst. Rueckgabe: {Monat: Miete} fuer erste..letzter.
    """
    miete, pfad = start, {}
    for m in range(erste, letzter + 1):
        z = ziel(m)
        if m >= frei_ab:
            if z < miete:
                if senken:
                    miete = z
            elif z > miete and m - 1 >= t_letzte + kat.wartefrist:
                k = m - kat.kappung_monate
                bezug = pfad[k] if k >= erste else bezug_vorher(k)
                neu = miete if bezug is None else min(z, bezug * (EINS + kat.kappung(m)))
                if neu > miete:
                    miete, t_letzte = neu, m - 1
        pfad[m] = miete
    return pfad


def anpassungsziel(start, vergleich, jahr0, dauer):
    """R-6.3: Zielmiete Pfad_j = Start + (Vergleichsmiete_j - Start) x min(1; (j - jahr0) / d); im Jahr jahr0 der
    Start selbst, bei d = 0 ab dem Folgejahr die Vergleichsmiete. vergleich: Funktion Monat -> Vergleichsmiete."""
    def ziel(m):
        k = jahr_von(m) - jahr0
        if k <= 0:
            return start
        if dauer == 0 or k >= dauer:
            return vergleich(m)
        return start + (vergleich(m) - start) * k / dauer      # erst multiplizieren, zuletzt teilen (R-12.5)
    return ziel


def gebundene_stufe(jahr, fest_jahre, schritt_jahre):
    """R-6.5: Zahl der Erhoehungsschritte der gebundenen Miete im Jahr 'jahr' der Bindung."""
    return 0 if jahr <= fest_jahre else (jahr - fest_jahre - 1) // schritt_jahre + 1


class Pool:
    """Teilflaeche mit einheitlicher Miete: flaeche (m2), miete {Monat: Euro je m2}; ausserhalb null."""

    def __init__(self, name, flaeche, miete):
        self.name, self.flaeche, self.miete = name, flaeche, miete


def mieten_ankauf(M, ein, kat, vg_fluktuation, anlauf, steigerung, dauer, rd, vorsicht_ma037=True, rueckfuehrung=True):
    """R-6.2 bis R-6.6, R-6.13, R-6.14: Pools eines Ankaufs fuer die Monate 1..M.

    ein: Eingaben (wohnflaeche, leere_flaeche, ist_miete, vergleichsmiete, markt_miete, gebunden_anteil,
    bindung_jahre, gebundene_miete, mietenhistorie); kat: Mietrecht mit den Staffelwerten uebernommener Bindungen.
    rueckfuehrung: MA-038, eine Miete ueber dem Ziel wird zurueckgefuehrt (Voreinstellung) oder bleibt stehen.
    Rueckgabe: (pools, vergleich, vergleich), vergleich = Funktion Monat -> ortsuebliche Vergleichsmiete.
    """
    jahre = jahr_von(M)
    idx = indexreihe(jahre, steigerung, rd)
    vm = lambda m: ein.vergleichsmiete * idx[jahr_von(m)]

    def neuvermietung(m):               # R-6.13: Neuvermietungsmiete, begrenzt durch die Mietpreisbremse (BGB-556D)
        markt = ein.markt_miete * idx[jahr_von(m)]
        return min(markt, vm(m) * (EINS + kat.bremse_aufschlag)) if kat.bremse(m) else markt

    def kohorte(name, flaeche, erste):  # neu vermietete Flaeche: Anfangsmiete, danach BGB-558 zur Vergleichsmiete
        start = neuvermietung(erste)
        pfad = erhoehungspfad(start, vm, erste, M, kat, erste - 1, lambda k: start, erste)
        return Pool(name, flaeche, pfad)

    vermietet = ein.wohnflaeche - ein.leere_flaeche
    pools = []
    ist = ein.ist_miete
    # ---- Mietenhistorie oder MA-037 (R-6.3)
    hist = ein.mietenhistorie
    if hist is not None:                # (Monate seit der letzten Erhoehung, Miete drei Jahre vor dem Stichtag)
        seit, alt = hist
        t_letzte = -seit
        kappe = lambda k: ist if k >= -seit + 1 else alt
    elif vorsicht_ma037:                # letzte Erhoehung unmittelbar vor dem Stichtag, Kappungsgrenze ausgeschoepft
        t_letzte, kappe = 0, (lambda k: None)
    else:                               # andere Lesart: seit dem Kappungszeitraum unveraendert
        t_letzte, kappe = -kat.kappung_monate, (lambda k: ist)
    # ---- freie Bestandsflaeche mit Fluktuation (R-6.14)
    frei = vermietet * (EINS - ein.gebunden_anteil)
    if frei > 0:
        pfad = erhoehungspfad(ist, anpassungsziel(ist, vm, 1, dauer), 1, M, kat, t_letzte, kappe, MONATE + 1,
                              senken=rueckfuehrung)
        rest = frei
        flaechen = {}
        for j in range(1, jahre + 1):
            if j >= 2 and vg_fluktuation > 0:
                wechsel = rest * vg_fluktuation
                rest -= wechsel
                pools.append(kohorte(f"Neuvermietung Jahr {j}", wechsel, (j - 1) * MONATE + 1))
            flaechen[j] = rest
        pools.append(Pool("Bestand frei", flaechen, pfad))
    # ---- gebundene Bestandsflaeche (R-6.5, R-6.6)
    geb = vermietet * ein.gebunden_anteil
    if geb > 0:
        g0 = ist if ein.gebundene_miete is None else ein.gebundene_miete
        ende = min(ein.bindung_jahre * MONATE, M)
        pfad, t_stufe = {}, 0
        for m in range(1, ende + 1):
            stufe = gebundene_stufe(jahr_von(m), kat.geb_fest_jahre, kat.geb_schritt_jahre)
            pfad[m] = min(g0 * (EINS + kat.geb_steigerung) ** stufe, vm(m))
            if m > 1 and pfad[m] > pfad[m - 1]:
                t_stufe = m - 1
        if ende < M:
            letzte = pfad[ende] if ende >= 1 else g0
            b = ein.bindung_jahre
            ziel = anpassungsziel(letzte, vm, b + 1, dauer)
            # Bezugsmiete der Kappung: gebundene Miete des Plans; vor dem Stichtag gilt MA-037
            def kappe_g(k, _p=dict(pfad)):
                if k >= 1:
                    return _p[k]
                return None if (hist is None and vorsicht_ma037) else g0
            nach = erhoehungspfad(letzte, ziel, ende + 1, M, kat, t_stufe, kappe_g, ende + MONATE + 1,
                                  senken=rueckfuehrung)
            pfad.update(nach)
        pools.append(Pool("Bestand gebunden", geb, pfad))
    # ---- leerstehende Flaeche: nach dem Anlaufleerstand zur Neuvermietungsmiete (R-6.13)
    if ein.leere_flaeche > 0 and anlauf + 1 <= M:
        pools.append(kohorte("Leerstand am Stichtag", ein.leere_flaeche, anlauf + 1))
    return pools, vm, vm


def mieten_neubau(M, ein, kat, erste, bezug, steigerung, dauer, rd, foerderung=None):
    """R-6.7: Pools eines Neubaus. erste = erster Vermietungsmonat (nach Bauzeit und Anlaufleerstand),
    bezug = Monat der Bezugsfertigkeit. Die eingegebene Miete gilt fuer das erste Vermietungsjahr; die
    Vergleichsmiete des Neubaus ist die eingegebene Miete mit dem Mietindex je Vermietungsjahr. Die frei
    finanzierte Flaeche folgt ihr ohne Anpassungsdauer (d = 0); 'dauer' gilt nach dem Ende einer Bindung (H-23).
    Rueckgabe: (pools, vergleich, nachhaltig); nachhaltig = Funktion Monat -> nachhaltige Miete der Bank (E-65)."""
    jahre = jahr_von(M) + 1
    idx = indexreihe(jahre, steigerung, rd)
    vm = lambda m: ein.markt_miete * idx[(m - erste) // MONATE + 1] if m >= erste else ein.markt_miete
    basis_n = ein.markt_miete if ein.nachhaltige_miete is None else ein.nachhaltige_miete
    vm_n = lambda m: basis_n * idx[(m - erste) // MONATE + 1] if m >= erste else basis_n
    pools = []
    geb_anteil = NULL
    if foerderung is not None:
        f = foerderung
        geb_anteil = EINS if ein.gebunden_anteil == 0 else ein.gebunden_anteil
        ende = min(bezug - 1 + f.bindung_jahre * MONATE, M)
        pfad, t_stufe = {}, erste - 1
        for m in range(erste, ende + 1):
            stufe = gebundene_stufe((m - bezug) // MONATE + 1, f.fest_jahre, f.schritt_jahre)
            pfad[m] = min(f.eingangsmiete * (EINS + f.steigerung) ** stufe, vm(m))
            if m > erste and pfad[m] > pfad[m - 1]:
                t_stufe = m - 1
        if ende < M:
            letzte = pfad[ende]
            ziel = anpassungsziel(letzte, vm, jahr_von(ende) + 1, dauer)
            def kappe_g(k, _p=dict(pfad)):
                return _p[max(k, erste)]
            pfad.update(erhoehungspfad(letzte, ziel, ende + 1, M, kat, t_stufe, kappe_g, ende + MONATE + 1))
        pools.append(Pool("gefoerdert gebunden", ein.wohnflaeche * geb_anteil, pfad))
    frei = ein.wohnflaeche * (EINS - geb_anteil)
    if frei > 0:
        start = ein.markt_miete
        pfad = erhoehungspfad(start, vm, erste, M, kat, erste - 1, lambda k: start, erste)
        pools.append(Pool("Neubau frei", frei, pfad))
    return pools, vm, vm_n


def monatswerte(pools, vm, M):
    """Summen je Monat 1..M, ungerundet: Sollmiete in Euro, nachhaltige Miete in Euro (je Pool der kleinere Wert
    aus Miete und Vergleichsmiete, R-5.12), vermietete Flaeche."""
    soll, nachh, flaeche = [NULL] * (M + 1), [NULL] * (M + 1), [NULL] * (M + 1)
    for m in range(1, M + 1):
        for p_ in pools:
            if m in p_.miete:
                a = p_.flaeche[jahr_von(m)] if isinstance(p_.flaeche, dict) else p_.flaeche
                soll[m] += a * p_.miete[m]
                nachh[m] += a * min(p_.miete[m], vm(m))
                flaeche[m] += a
    return soll, nachh, flaeche


def monatsbetrag(jahresbetrag, p, rd):
    """R-6.8: laufende Zahlung je Periode = Jahresbetrag / p, je Zahlung auf Cent gerundet (R-12.3)."""
    return rd.geld(jahresbetrag / p)


def instandhaltung_je_qm(staffel, alter):
    """R-6.8 (IIBV-28): Betrag der Altersstufe; staffel = Liste (Alter ab, Betrag je m2), aufsteigend."""
    betrag = staffel[0][1]
    for ab, wert in staffel:
        if alter >= ab:
            betrag = wert
    return betrag
