"""Kapitel 13 der Fachspezifikation: Kontrollsummen und Proben (P-01 bis P-14).

Jede Probe rechnet aus den gebuchten Zeilen neu und meldet (Kennung, Periode oder Objekt, Abweichung).
Ein Ergebnis gilt nur, wenn die Liste leer ist (R-13.1). Die Proben gelten exakt (Abweichung null),
weil alle Zahlungen exakte Dezimalzahlen sind.
"""
from decimal import Decimal as D
from zahlen import NULL
from kennzahlen import vofi_rendite, vergleichsfaktoren


def pruefe_plan(plan, alt=None):
    """Proben P-01 bis P-03, P-05, P-09 bis P-11 fuer einen gerechneten Finanzplan."""
    e, z = plan.e, plan.zeilen
    N = e.raster.N
    # R-13.2: exakt im Rundungsmodus "cent"; im Lehrbuchmodus ohne Rundung gilt die Rechentoleranz
    tol = D(0) if e.rundung.modus == "cent" else D("1E-30")
    bef = []
    for u in range(N + 1):
        # P-01 Finanzierungssaldo null
        if abs(z[u]["fin_saldo"]) > tol:
            bef.append(("P-01", u, z[u]["fin_saldo"]))
        # P-02 Kreditprobe je Tranche: Auszahlungen - Tilgungen - Tilgungszuschuesse - Abloesung = Restschuld.
        # Einbehaltene Betraege mindern die Auszahlung, nicht die Schuld; kapitalisierte Zinsen gibt es in
        # Teil 1 nicht (Glied null).
        for tr in e.tranchen:
            kum = sum(z[v]["tranchen"][tr.name]["auszahlung"] - z[v]["tranchen"][tr.name]["tilgung"]
                      - z[v]["tranchen"][tr.name]["tilgungszuschuss"] - z[v]["tranchen"][tr.name]["abloesung"]
                      for v in range(u + 1))
            if abs(kum - z[u]["tranchen"][tr.name]["rest"]) > tol:
                bef.append(("P-02", (u, tr.name), kum - z[u]["tranchen"][tr.name]["rest"]))
        # P-03 Bestandsprobe
        vor = z[u - 1]["bestandssaldo"] if u >= 1 else NULL
        soll = (z[u]["originaer"] + z[u]["einlage"] + z[u]["nachschuss"] - z[u]["entnahme"]
                - (z[u]["zins"] + z[u]["kkzins"] + z[u]["beitrag"] + z[u]["vfe"])
                + z[u]["habenzins"] - z[u]["steuer"] + z[u]["tilgungszuschuss"]
                - (z[u]["einbehalt"] + z[u]["zuschuss_einbehalt"]))
        if abs(z[u]["bestandssaldo"] - vor - soll) > tol:
            bef.append(("P-03", u, z[u]["bestandssaldo"] - vor - soll))
    # P-02 Schluss: nach der Abloesung ist jede Restschuld null
    if e.verkauf is not None:
        for tr in e.tranchen:
            if abs(z[N]["tranchen"][tr.name]["rest"]) > tol:
                bef.append(("P-02", (N, tr.name), z[N]["tranchen"][tr.name]["rest"]))
        # P-05 Restwertprobe: gebuchter Erloes = Preis aus dem Massstab - Verkaufskosten - ausstehender Stau
        v = e.verkauf
        if z[N]["verkauf"] != v.preis_brutto - v.kosten - v.stau_abzug:
            bef.append(("P-05", N, z[N]["verkauf"] - (v.preis_brutto - v.kosten - v.stau_abzug)))
    # P-09 Verdichtung: Summe der Periodenwerte = Jahreswert (nur Zahlungen)
    from finanzplan import verdichte
    jahre = verdichte(plan)
    for k in ("originaer", "steuer", "zins", "tilgung"):
        if abs(sum(j[k] for j in jahre) - sum(zz[k] for zz in z)) > tol:
            bef.append(("P-09", k, sum(j[k] for j in jahre) - sum(zz[k] for zz in z)))
    if alt is not None:
        # P-10 Spiegelprobe: die Alternative fuehrt dieselbe Einlagen- und Entnahmenreihe
        for u in range(N + 1):
            if alt.zeilen[u]["einlage"] != plan.einlagen_netto[u] or alt.zeilen[u]["entnahme"] != plan.entnahmen_netto[u]:
                bef.append(("P-10", u, None))
        # P-11 Renditeprobe: Rendite ueber der Vergleichsrendite genau dann, wenn die Endwertdifferenz positiv ist
        w = vergleichsfaktoren(e)
        r, Z, Dn, _ = vofi_rendite(plan.endwert, plan.einlagen_netto, plan.entnahmen_netto, w, e.raster.n)
        ru, Zu, _, _ = vofi_rendite(alt.endwert, plan.einlagen_netto, plan.entnahmen_netto, w, e.raster.n)
        if r is not None and (Z > 0 or Zu > 0):
            if (r > ru) != (plan.endwert > alt.endwert) and plan.endwert != alt.endwert:
                bef.append(("P-11", None, r - ru))
    return bef


def pruefe_mittel(herkunft: dict, verwendung: dict):
    """P-04 Mittelherkunft gleich Mittelverwendung der Investitionsphase."""
    diff = sum(herkunft.values()) - sum(verwendung.values())
    return [] if diff == 0 else [("P-04", None, diff)]


def pruefe_stau(anteil_gezahlt, anteil_abgezogen):
    """P-06 je Massnahme: gezahlter und abgezogener Anteil ergeben zusammen 100 %."""
    diff = anteil_gezahlt + anteil_abgezogen - 1
    return [] if diff == 0 else [("P-06", None, diff)]


def pruefe_zuschuss(erhalten, zurueckgezahlt, verbleibend_nach_regel):
    """P-07 je Zuschuss: erhalten - zurueckgezahlt = Betrag, der nach der Rueckzahlungsregel verbleibt."""
    diff = erhalten - zurueckgezahlt - verbleibend_nach_regel
    return [] if diff == 0 else [("P-07", None, diff)]


def pruefe_abschreibung(basis, afa_reihe, buchwert_ende, boden):
    """P-08: Summe der Abschreibungen hoechstens die Abschreibungsgrundlage; Buchwert = Boden + Rest."""
    summe = sum(afa_reihe)
    bef = []
    if summe > basis:
        bef.append(("P-08", "afa>basis", summe - basis))
    if buchwert_ende != boden + basis - summe:
        bef.append(("P-08", "buchwert", buchwert_ende - (boden + basis - summe)))
    return bef
