"""Kapitel 13 der Fachspezifikation: Kontrollsummen und Proben (P-01 bis P-19).

Jede Probe rechnet aus den gebuchten Zeilen neu, nach denselben Rundungsregeln wie der Kern (R-13.2), und meldet
(Kennung, Periode oder Objekt, Abweichung). Ein Ergebnis gilt nur, wenn die Liste leer ist (R-13.1).
"""
from decimal import Decimal as D
from zahlen import NULL, EINS, periodensatz_konform
from kennzahlen import vofi_rendite, vergleichsfaktoren


def pruefe_plan(plan, alt=None):
    """Proben fuer jeden gerechneten Finanzplan: P-01 bis P-03, P-05, P-08, P-09, P-15, P-17, P-19; mit
    Unterlassensalternative zusaetzlich P-10, P-11, P-16."""
    e, z = plan.e, plan.zeilen
    r, rd = e.raster, e.rundung
    N, p = r.N, r.p
    # R-13.2: exakt im Rundungsmodus "cent"; im Lehrbuchmodus ohne Rundung gilt die Rechentoleranz
    tol = D(0) if rd.modus == "cent" else D("1E-30")
    bef = []

    def ungleich(a, b):
        return abs(a - b) > tol

    def bestandsfluss(zz):              # rechte Seite der Bestandsprobe P-03
        return (zz["originaer"] + zz["einlage"] + zz["nachschuss"] - zz["entnahme"]
                - (zz["zins"] + zz["kkzins"] + zz["beitrag"] + zz["bereit"] + zz["vfe"])
                + zz["habenzins"] - zz["steuer"] + zz["tilgungszuschuss"]
                - (zz["einbehalt"] + zz["zuschuss_einbehalt"]))

    satz_h = periodensatz_konform(e.h_kurz, p, rd)
    satz_kk = periodensatz_konform(e.kk_zins, p, rd)
    for u in range(N + 1):
        # P-01 Finanzierungssaldo null
        if ungleich(z[u]["fin_saldo"], NULL):
            bef.append(("P-01", u, z[u]["fin_saldo"]))
        for tr in e.tranchen:
            t = z[u]["tranchen"][tr.name]
            # P-02 Kreditprobe je Tranche: Auszahlungen - Tilgungen - Tilgungszuschuesse - Abloesung = Restschuld.
            # Einbehaltene Betraege mindern die Auszahlung, nicht die Schuld; kapitalisierte Zinsen gibt es in
            # Teil 1 nicht (Glied null).
            kum = sum(z[v]["tranchen"][tr.name]["auszahlung"] - z[v]["tranchen"][tr.name]["tilgung"]
                      - z[v]["tranchen"][tr.name]["tilgungszuschuss"] - z[v]["tranchen"][tr.name]["abloesung"]
                      for v in range(u + 1))
            if ungleich(kum, t["rest"]):
                bef.append(("P-02", (u, tr.name), kum - t["rest"]))
            # P-17 Zinsprobe: Zins und Beitrag aus der Restschuld der Vorperiode und dem Satz der Periode
            if u >= 1:
                satz = tr.zins if (tr.bindung is None or u <= tr.bindung) else tr.anschluss_zins
                soll_zins = tr._geld(rd, t["rest_vor"] * satz / p) if t["rest_vor"] > 0 else NULL
                soll_beitrag = tr._geld(rd, t["rest_vor"] * tr.beitrag_satz / p) if t["rest_vor"] > 0 else NULL
                if ungleich(t["zins"], soll_zins):
                    bef.append(("P-17", (u, tr.name, "zins"), t["zins"] - soll_zins))
                if ungleich(t["beitrag"], soll_beitrag):
                    bef.append(("P-17", (u, tr.name, "beitrag"), t["beitrag"] - soll_beitrag))
        if u >= 1:
            for k, bestand, satz in (("habenzins", z[u - 1]["guthaben"], satz_h), ("kkzins", z[u - 1]["kk"], satz_kk)):
                if ungleich(z[u][k], rd.geld(bestand * satz)):
                    bef.append(("P-17", (u, k), z[u][k] - rd.geld(bestand * satz)))
        # P-03 Bestandsprobe
        vor = z[u - 1]["bestandssaldo"] if u >= 1 else NULL
        if ungleich(z[u]["bestandssaldo"] - vor, bestandsfluss(z[u])):
            bef.append(("P-03", u, z[u]["bestandssaldo"] - vor - bestandsfluss(z[u])))
        # P-19 Abschreibungstakt: Abschreibung wird nur am Ende eines Planjahres gebucht (R-7.3)
        if z[u]["afa"] != 0 and not r.jahresende(u):
            bef.append(("P-19", u, z[u]["afa"]))
    # P-02 Schluss: nach der Abloesung ist jede Restschuld null
    if e.verkauf is not None:
        for tr in e.tranchen:
            if ungleich(z[N]["tranchen"][tr.name]["rest"], NULL):
                bef.append(("P-02", (N, tr.name), z[N]["tranchen"][tr.name]["rest"]))
        # P-05 Restwertprobe: gebuchter Erloes = Preis aus dem Massstab - Verkaufskosten - ausstehender Stau
        v = e.verkauf
        if z[N]["verkauf"] != v.preis_brutto - v.kosten - v.stau_abzug:
            bef.append(("P-05", N, z[N]["verkauf"] - (v.preis_brutto - v.kosten - v.stau_abzug)))
    # P-08 Abschreibungsprobe (jeder Lauf, fuer den die Anschaffungskosten bekannt sind)
    summe_afa = sum(zz["afa"] for zz in z)
    if e.afa_grundlage is not None and summe_afa - e.afa_grundlage > tol:
        bef.append(("P-08", "Abschreibung ueber der Grundlage", summe_afa - e.afa_grundlage))
    if e.anschaffung is not None and e.verkauf is not None and ungleich(e.verkauf.buchwert, e.anschaffung - summe_afa):
        bef.append(("P-08", "Restbuchwert", e.verkauf.buchwert - (e.anschaffung - summe_afa)))
    # P-09 Verdichtung: Jahresbestandsprobe und Summenprobe der Jahresdarstellung
    from finanzplan import verdichte
    jahre = verdichte(plan)
    for j in range(len(jahre)):
        vj = jahre[j - 1] if j >= 1 else dict(guthaben=NULL, kk=NULL, restschuld=NULL, bestandssaldo=NULL)
        a = jahre[j]
        proben = (("guthaben", vj["guthaben"] + a["anlage"]), ("kk", vj["kk"] + a["kk_aufnahme"]),
                  ("restschuld", vj["restschuld"] + a["auszahlung"] - a["tilgung"] - a["tilgungszuschuss"] - a["abloesung"]),
                  ("bestandssaldo", vj["bestandssaldo"] + bestandsfluss(a)))
        for k, soll in proben:
            if ungleich(a[k], soll):
                bef.append(("P-09", (j, k), a[k] - soll))
    for k in jahre[0]:
        if k not in ("jahr", "guthaben", "kk", "restschuld", "bestandssaldo"):
            diff = sum(a[k] for a in jahre) - sum(zz[k] for zz in z)
            if ungleich(diff, NULL):
                bef.append(("P-09", k, diff))
    # P-15 Steuerprobe
    prot = plan.steuer.protokoll
    vor = dict(vv=NULL, vv_gew=NULL)
    for t in prot:
        for topf in ("vv", "vv_gew"):
            if ungleich(t[topf + "_anfang"], vor[topf]):
                bef.append(("P-15", (t["jahr"], topf, "Anfangsbestand"), t[topf + "_anfang"] - vor[topf]))
            if ungleich(t[topf], t[topf + "_anfang"] + t[topf + "_zugang"] - t[topf + "_genutzt"]):
                bef.append(("P-15", (t["jahr"], topf, "Fortschreibung"), t[topf]))
            vor[topf] = t[topf]
        if ungleich(t["steuer"], sum(t["arten"].values(), NULL) - t["anrechnung"]):
            bef.append(("P-15", (t["jahr"], "Summe der Steuerarten"), t["steuer"]))
        if ungleich(t["steuer"], z[t["jahr"] * p]["steuer"]):
            bef.append(("P-15", (t["jahr"], "gebuchte Steuer"), t["steuer"] - z[t["jahr"] * p]["steuer"]))
    if e.anschaffung is not None and e.verkauf is not None:
        # Bruecke vom Ergebnis zu den Zahlungen: Summe der Bemessungsgroessen = originaere Zahlungen
        # - Finanzierungskosten - einbehaltene Betraege + Habenzinsen
        bemessung = sum(zz["e_op"] + zz["habenzins"] for zz in z) + z[N]["g_v"] - z[N]["vfe_verkauf"]
        zahlungen = sum(zz["originaer"] - zz["zins"] - zz["kkzins"] - zz["beitrag"] - zz["bereit"] - zz["vfe"]
                        - zz["einbehalt"] - zz["zuschuss_einbehalt"] + zz["habenzins"] for zz in z)
        if ungleich(bemessung, zahlungen):
            bef.append(("P-15", "Bruecke Ergebnis zu Zahlungen", bemessung - zahlungen))
    if alt is not None:
        # P-10 Spiegelprobe: die Alternative fuehrt dieselbe Einlagen- und Entnahmenreihe
        for u in range(N + 1):
            if alt.zeilen[u]["einlage"] != plan.einlagen_netto[u] or alt.zeilen[u]["entnahme"] != plan.entnahmen_netto[u]:
                bef.append(("P-10", u, None))
        # P-11 Renditeprobe (prueft die Stimmigkeit der Umsetzung; rechnerisch eine Identitaet, R-10.6 Nr. 2)
        w = vergleichsfaktoren(e)
        ren, Z, Dn, _ = vofi_rendite(plan.endwert, plan.einlagen_netto, plan.entnahmen_netto, w, r.n)
        ru, Zu, _, _ = vofi_rendite(alt.endwert, plan.einlagen_netto, plan.entnahmen_netto, w, r.n)
        if ren is not None and (Z > 0 or Zu > 0):
            if (ren > ru) != (plan.endwert > alt.endwert) and plan.endwert != alt.endwert:
                bef.append(("P-11", None, ren - ru))
        bef += pruefe_alternative(alt, rd, tol)
    return bef


def pruefe_alternative(alt, rd, tol=D(0)):
    """P-16: Saldo- und Bestandsprobe der Unterlassensalternative je Periode; Zinsen neu gerechnet."""
    bef, az = [], alt.zeilen
    vor = dict(lang=NULL, kurz=NULL, kk=NULL)
    for u, a in enumerate(az):
        if u >= 1:
            for k, bestand, satz in (("zins_lang", vor["lang"], a["satz_lang"]), ("zins_kurz", vor["kurz"], a["satz_kurz"]),
                                     ("kkzins", vor["kk"], a["satz_kk"])):
                if abs(a[k] - rd.geld(bestand * satz)) > tol:
                    bef.append(("P-16", (u, k), a[k] - rd.geld(bestand * satz)))
        soll = (vor["lang"] + vor["kurz"] - vor["kk"] + a["einlage"] - a["entnahme"] + a["zins_lang"] + a["zins_kurz"]
                - a["kkzins"] - a["steuer"])
        ist = a["lang"] + a["kurz"] - a["kk"]
        if abs(ist - soll) > tol:
            bef.append(("P-16", (u, "Saldo"), ist - soll))
        if min(a["lang"], a["kurz"], a["kk"]) < 0:
            bef.append(("P-16", (u, "negativer Bestand"), min(a["lang"], a["kurz"], a["kk"])))
        vor = a
    if abs(alt.endwert - (az[-1]["lang"] + az[-1]["kurz"] - az[-1]["kk"])) > tol:
        bef.append(("P-16", "Endwert", alt.endwert))
    return bef


def pruefe_mittel(einlagen_geplant, soll_eigenkapital, herkunft: dict, verwendung: dict, nach_stichtag=None):
    """P-04: (a) die gebuchten Einlagen der Investitionsphase ohne Nachschuesse sind der Ausgleichsposten
    Mittelbedarf - uebrige Darlehen - Zuschuesse - Bankdarlehen; (b) Mittelherkunft gleich Mittelverwendung;
    (c) beim Ankauf sind Guthaben und Kontokorrent nach dem Stichtag null."""
    bef = []
    if einlagen_geplant != soll_eigenkapital:
        bef.append(("P-04", "Eigenkapital als Ausgleichsposten", einlagen_geplant - soll_eigenkapital))
    diff = sum(herkunft.values()) - sum(verwendung.values())
    if diff != 0:
        bef.append(("P-04", "Mittelherkunft gegen Mittelverwendung", diff))
    if nach_stichtag is not None and nach_stichtag != 0:
        bef.append(("P-04", "Guthaben oder Kontokorrent nach dem Stichtag", nach_stichtag))
    return bef


def pruefe_stau(anteil_gezahlt, anteil_abgezogen):
    """P-06 je Massnahme: gezahlter und abgezogener Anteil ergeben zusammen 100 %."""
    diff = anteil_gezahlt + anteil_abgezogen - 1
    return [] if diff == 0 else [("P-06", None, diff)]


def pruefe_zuschuss(erhalten, zurueckgezahlt, zuschuss, bindung_perioden, verbleibend, rd):
    """P-07 je Zuschuss: erhalten - zurueckgezahlt = Betrag, der nach der Rueckzahlungsregel R-8.7 verbleibt.
    Die Probe rechnet die Rueckzahlung mit derselben Rechenfolge und Rundung wie die Regel (R-12.5)."""
    rueck = rd.geld(zuschuss * D(verbleibend) / D(bindung_perioden)) if (bindung_perioden > 0 and verbleibend > 0) else NULL
    diff = erhalten - zurueckgezahlt - (zuschuss - rueck)
    return [] if diff == 0 else [("P-07", None, diff)]


def pruefe_index(reihen, rd):
    """P-18 Indexprobe: Index_1 = 1 und Index_j = runde12(Index_(j-1) x (1 + Steigerung)) je Indexreihe."""
    bef = []
    for name, (idx, steigerung) in reihen.items():
        if idx[1] != EINS:
            bef.append(("P-18", (name, 1), idx[1] - EINS))
        for j in range(2, len(idx)):
            if idx[j] != rd.satz(idx[j - 1] * (EINS + steigerung)):
                bef.append(("P-18", (name, j), idx[j]))
    return bef
