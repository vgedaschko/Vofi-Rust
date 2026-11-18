"""Kapitel 13 der Fachspezifikation: Kontrollsummen und Proben (P-01 bis P-21).

Jede Probe rechnet aus den gebuchten Zeilen neu, nach denselben Rundungsregeln wie der Kern (R-13.2), und meldet
(Kennung, Periode oder Objekt, Abweichung). Ein Ergebnis gilt nur, wenn die Liste leer ist (R-13.1).
"""
from decimal import Decimal as D
from decimal import ROUND_FLOOR
from zahlen import NULL, EINS, periodensatz_konform, abrunden_auf, TOLERANZ_OHNE_RUNDUNG
from kennzahlen import vofi_rendite, vergleichsfaktoren
from darlehen import Tranche
from steuer import (KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST, PERSONENUNTERNEHMEN, PERSONENGESELLSCHAFT,
                    EINZELUNTERNEHMEN, PRIVAT, BEFREIT, LEHRBUCH)


def pruefe_plan(plan, alt=None):
    """Proben fuer jeden gerechneten Finanzplan: P-01 bis P-03, P-05, P-08, P-09, P-15, P-17, P-19, P-20; mit
    Unterlassensalternative zusaetzlich P-10, P-11, P-16."""
    e, z = plan.e, plan.zeilen
    r, rd = e.raster, e.rundung
    N, p = r.N, r.p
    # R-13.2: exakt im Rundungsmodus "cent"; im Lehrbuchmodus ohne Rundung gilt die Rechentoleranz
    tol = D(0) if rd.modus == "cent" else TOLERANZ_OHNE_RUNDUNG
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
    laufend = {tr.name: NULL for tr in e.tranchen}     # laufende Summe der Kreditprobe je Tranche
    for u in range(N + 1):
        # P-01 Finanzierungssaldo null
        if ungleich(z[u]["fin_saldo"], NULL):
            bef.append(("P-01", u, z[u]["fin_saldo"]))
        for tr in e.tranchen:
            t = z[u]["tranchen"][tr.name]
            # P-02 Kreditprobe je Tranche: Auszahlungen - Tilgungen - Tilgungszuschuesse - Abloesung = Restschuld.
            # Einbehaltene Betraege mindern die Auszahlung, nicht die Schuld; kapitalisierte Zinsen gibt es in
            # Teil 1 nicht (Glied null).
            laufend[tr.name] += t["auszahlung"] - t["tilgung"] - t["tilgungszuschuss"] - t["abloesung"]
            kum = laufend[tr.name]
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
    # P-20 Ratenprobe: die planmaessige Tilgung jeder Tranche, unabhaengig aus ihren Merkmalen neu gerechnet
    for tr in e.tranchen:
        bef += _pruefe_raten(tr, [zz["tranchen"][tr.name] for zz in z], p, rd, tol)
    # P-02 Schluss: nach der Abloesung ist jede Restschuld null
    if e.verkauf is not None:
        for tr in e.tranchen:
            if ungleich(z[N]["tranchen"][tr.name]["rest"], NULL):
                bef.append(("P-02", (N, tr.name), z[N]["tranchen"][tr.name]["rest"]))
        # P-05 Restwertprobe: gebuchter Erloes = Preis aus dem Massstab - Verkaufskosten - ausstehender Stau
        v = e.verkauf
        if ungleich(z[N]["verkauf"], v.preis_brutto - v.kosten - v.stau_abzug):
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
    # P-15 (e): Steuer je Planjahr unabhaengig nachgerechnet, mit eigenem Verlustvortrag und dem Satz des
    # Kalenderjahres aus dem Auftrag
    for j, soll in _steuer_nachgerechnet(e.steuer, r, rd, prot):
        if ungleich(prot[j - 1]["steuer"], soll):
            bef.append(("P-15", (j, "Steuer nachgerechnet"), prot[j - 1]["steuer"] - soll))
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
            if ungleich(alt.zeilen[u]["einlage"], plan.einlagen_netto[u]) or ungleich(alt.zeilen[u]["entnahme"], plan.entnahmen_netto[u]):
                bef.append(("P-10", u, None))
        # P-11 Renditeprobe (prueft die Stimmigkeit der Umsetzung; rechnerisch eine Identitaet, R-10.6 Nr. 2)
        w = vergleichsfaktoren(e)
        ren, Z, Dn, _ = vofi_rendite(plan.endwert, plan.einlagen_netto, plan.entnahmen_netto, w, r.n)
        ru, Zu, _, _ = vofi_rendite(alt.endwert, plan.einlagen_netto, plan.entnahmen_netto, w, r.n)
        if ren is not None and (Z > 0 or Zu > 0):
            if (ren > ru) != (plan.endwert > alt.endwert) and plan.endwert != alt.endwert:
                bef.append(("P-11", None, ren - ru))
        bef += pruefe_alternative(alt, rd, tol, e)
    return bef


def _pruefe_raten(tr, zeilen, p, rd, tol):
    """P-20 Ratenprobe je Tranche: Die planmaessige Tilgung jeder Periode folgt aus der Rate nach R-5.4, R-5.5,
    R-5.9 und R-5.10; die Rate wird hier aus den Merkmalen der Tranche neu gebildet. Vor dem Tilgungsbeginn ist
    die Tilgung null; die erste Rate entsteht mit dem Zins der Periode des Tilgungsbeginns."""
    if tr.art not in ("annuitaet_prozent", "annuitaet_laufzeit", "raten"):
        return []
    bef, rate = [], None
    geld = lambda x: tr._geld(rd, x)
    for u in range(1, len(zeilen)):
        t = zeilen[u]
        rest = t["rest_vor"]
        if rest <= 0:
            continue
        if u < tr.tilgungsbeginn:
            soll = NULL
        else:
            k = u - tr.tilgungsbeginn
            nach = tr.bindung is not None and u > tr.bindung
            satz = tr.anschluss_zins if nach else tr.zins
            wechsel = tr.bindung is not None and u == tr.bindung + 1 and rate is not None
            if tr.art == "annuitaet_prozent":
                ts = tr.anschluss_tilgung if (tr.anschluss_tilgung is not None and nach) else tr.tilgungssatz
                if rate is None:
                    rate = geld(tr.rate_betrag * (satz + ts) / p)
                elif wechsel:
                    regel = tr.anschluss_regel
                    if regel == "restlaufzeit":
                        m = None if rate <= geld(rest * tr.zins / p) else Tranche.restlaufzeit(rest, rate, tr.zins / p)
                        if m is None:
                            regel = "tilgungssatz"
                        else:
                            rate = geld(Tranche.annuitaet(rest, satz / p, max(1, int(m.to_integral_value(ROUND_FLOOR)))))
                    if regel == "rate":
                        rate = max(rate, geld(rest * satz / p))
                    elif regel == "tilgungssatz":
                        rate = geld(rest * (satz + ts) / p)
                soll = min(rest, max(NULL, rate - t["zins"]))
            elif tr.art == "annuitaet_laufzeit":
                if rate is None:
                    rate = geld(Tranche.annuitaet(tr.betrag, satz / p, tr.laufzeit))
                elif wechsel:
                    rate = geld(Tranche.annuitaet(rest, satz / p, tr.laufzeit - k))
                soll = rest if k == tr.laufzeit - 1 else min(rest, max(NULL, rate - t["zins"]))
            else:
                if rate is None:
                    rate = geld(tr.betrag / tr.laufzeit)
                soll = rest if k == tr.laufzeit - 1 else min(rest, rate)
        if abs(t["tilgung"] - soll) > tol:
            bef.append(("P-20", (u, tr.name), t["tilgung"] - soll))
    return bef


def _steuer_nachgerechnet(par, raster, rd, protokoll, alternative=False):
    """P-15 (e), P-16: Steuer je Planjahr aus den drei Bemessungsgroessen des Protokolls neu gerechnet (R-7.5 bis
    R-7.12, R-7.16, R-7.17), mit eigenem Verlustvortrag je Topf und dem Katalogsatz des Kalenderjahres
    Startjahr + j - 1 (R-2.8). Rueckgabe: Liste (Planjahr, Steuer)."""
    g = rd.geld
    vv = {"e": NULL, "g": NULL}

    def nach_vortrag(x, topf):
        verbrauch = min(vv[topf], max(x, NULL))
        vv[topf] += max(-x, NULL) - verbrauch
        return max(x, NULL) - verbrauch

    ergebnis = []
    sofort = par.verlust == "sofort"
    for t in protokoll:
        j, e_op, z_h, g_v = t["jahr"], t["e_op"], t["z_h"], t["g_v"]
        st = par.status
        if st == BEFREIT:
            ergebnis.append((j, NULL))
            continue
        if st == LEHRBUCH:
            sz = par.zins_satz if par.zins_satz is not None else par.satz
            basis = e_op + (g_v if par.verkaufsgewinn_pflichtig else NULL)
            if sofort:
                s = par.satz * basis + sz * z_h
            elif sz == par.satz:
                s = par.satz * nach_vortrag(basis + z_h, "e")
            else:
                s = par.satz * nach_vortrag(basis, "e") + sz * z_h
            ergebnis.append((j, g(s)))
            continue
        # Verkauf bei Ueberschusseinkuenften: nur innerhalb der Frist, nach Abzug der Vorfaelligkeit, nie negativ
        gewinn_frist = NULL
        if st in (PRIVAT, KOERPERSCHAFT_OHNE_GEWST):
            x = g_v - t.get("vfe_verkauf", NULL)
            gewinn_frist = x if (par.haltedauer <= par.frist_privatverkauf and x > 0) else NULL
        if st == PRIVAT:
            sz = par.zins_satz if par.zins_satz is not None else par.est_satz
            verm = e_op + gewinn_frist
            s = g(par.est_satz * (verm if sofort else nach_vortrag(verm, "e"))) + g(sz * z_h)
            ergebnis.append((j, s))
            continue
        # Gewerbeertrag: Gewinn + Hinzurechnung - Kuerzung, dann Vortrag, Abrundung, Freibetrag (GEWSTG-7 bis -11)
        mit_gew = st == KOERPERSCHAFT or st in PERSONENUNTERNEHMEN
        gew = anr = NULL
        if mit_gew:
            pg = st in PERSONENGESELLSCHAFT
            g_gew = g_v * (EINS - par.anteil_natuerliche) if (par.aufgabegewinn and pg) else g_v
            linear = sofort and not pg
            kuerzung = (par.erweiterte_kuerzung and not alternative
                        and not (j == par.haltedauer and not par.uebergang_jahresende))
            if kuerzung:
                ertrag = z_h + (NULL if par.kuerzung_verkauf else g_gew)
            else:
                frei = NULL if linear else par.hinzu_freibetrag
                hinzu = par.hinzu_anteil * max(NULL, t.get("entgelte", NULL) + par.hinzu_pacht * t.get("pacht", NULL) - frei)
                ertrag = e_op + z_h + g_gew + hinzu
            satz_gew = par.messzahl * par.hebesatz
            anteil = EINS if st == EINZELUNTERNEHMEN else par.anteil_natuerliche
            if linear:
                gew = g(satz_gew * ertrag)
                anr = g(anteil * par.messzahl * min(par.anrechnungsfaktor, par.hebesatz) * ertrag)
                messbetrag = None
            else:
                frei_b = par.freibetrag if st in PERSONENUNTERNEHMEN else NULL
                abgerundet = max(NULL, abrunden_auf(nach_vortrag(ertrag, "g"), par.abrundung) - frei_b)
                if st == KOERPERSCHAFT:
                    gew = g(abgerundet * par.messzahl * par.hebesatz)
                else:
                    messbetrag = g(abgerundet * par.messzahl)
                    gew = g(messbetrag * par.hebesatz)
        if st in (KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST):
            einkommen = e_op + z_h + (gewinn_frist if st == KOERPERSCHAFT_OHNE_GEWST else g_v)
            kst = par.kst_satz(raster.startjahr + j - 1) * (EINS + par.soli_satz)
            s = g(kst * (einkommen if sofort else nach_vortrag(einkommen, "e"))) + gew
        else:
            gewinn = e_op + z_h + g_v
            est = g(par.est_satz * (gewinn if sofort else nach_vortrag(gewinn, "e")))
            if not linear:
                grenzen = [anteil * par.anrechnungsfaktor * messbetrag, anteil * gew]
                if not sofort:
                    grenzen.append(anteil * est)
                anr = g(min(grenzen))
            s = est + gew - anr
        ergebnis.append((j, s))
    return ergebnis


def pruefe_alternative(alt, rd, tol=D(0), e=None):
    """P-16: Saldo- und Bestandsprobe der Unterlassensalternative je Periode. Mit der Planeingabe e werden die
    Zinsen aus den Saetzen des Auftrags (H-08, H-09, H-10) neu gerechnet und die Steuer je Planjahr nach dem
    Steuerstatus des Vorhabens nachgerechnet (R-9.5); ohne e mit den Saetzen der Zeile."""
    bef, az = [], alt.zeilen
    vor = dict(lang=NULL, kurz=NULL, kk=NULL)
    saetze = None
    if e is not None:
        pp = e.raster.p
        saetze = (periodensatz_konform(e.h_kurz if e.a_lang is None else e.a_lang, pp, rd),
                  periodensatz_konform(e.h_kurz, pp, rd), periodensatz_konform(e.kk_zins, pp, rd))
        for j, soll in _steuer_nachgerechnet(e.steuer, e.raster, rd, alt.steuer.protokoll, alternative=True):
            ist = alt.steuer.protokoll[j - 1]["steuer"]
            if abs(ist - soll) > tol:
                bef.append(("P-16", (j, "Steuer nachgerechnet"), ist - soll))
            if abs(az[j * pp]["steuer"] - ist) > tol:
                bef.append(("P-16", (j, "gebuchte Steuer"), az[j * pp]["steuer"] - ist))
    for u, a in enumerate(az):
        if u >= 1:
            s3 = saetze or (a["satz_lang"], a["satz_kurz"], a["satz_kk"])
            for k, bestand, satz in (("zins_lang", vor["lang"], s3[0]), ("zins_kurz", vor["kurz"], s3[1]),
                                     ("kkzins", vor["kk"], s3[2])):
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


def pruefe_mittel(einlagen_geplant, soll_eigenkapital, herkunft: dict, verwendung: dict, nach_stichtag=None, tol=D(0)):
    """P-04: (a) die gebuchten Einlagen der Investitionsphase ohne Nachschuesse sind der Ausgleichsposten
    Mittelbedarf - uebrige Darlehen - Zuschuesse - Bankdarlehen; (b) Mittelherkunft gleich Mittelverwendung;
    (c) beim Ankauf sind Guthaben und Kontokorrent nach dem Stichtag null."""
    bef = []
    if abs(einlagen_geplant - soll_eigenkapital) > tol:
        bef.append(("P-04", "Eigenkapital als Ausgleichsposten", einlagen_geplant - soll_eigenkapital))
    diff = sum(herkunft.values()) - sum(verwendung.values())
    if abs(diff) > tol:
        bef.append(("P-04", "Mittelherkunft gegen Mittelverwendung", diff))
    if nach_stichtag is not None and abs(nach_stichtag) > tol:
        bef.append(("P-04", "Guthaben oder Kontokorrent nach dem Stichtag", nach_stichtag))
    return bef


def pruefe_stau(anteil_gezahlt, anteil_abgezogen, tol=D(0)):
    """P-06 je Massnahme: gezahlter und abgezogener Anteil ergeben zusammen 100 %."""
    diff = anteil_gezahlt + anteil_abgezogen - 1
    return [] if abs(diff) <= tol else [("P-06", None, diff)]


def pruefe_zuschuss(erhalten, zurueckgezahlt, zuschuss, bindung_perioden, verbleibend, rd, tol=D(0)):
    """P-07 je Zuschuss: erhalten - zurueckgezahlt = Betrag, der nach der Rueckzahlungsregel R-8.7 verbleibt.
    Die Probe rechnet die Rueckzahlung mit derselben Rechenfolge und Rundung wie die Regel (R-12.5)."""
    rueck = rd.geld(zuschuss * D(verbleibend) / D(bindung_perioden)) if (bindung_perioden > 0 and verbleibend > 0) else NULL
    diff = erhalten - zurueckgezahlt - (zuschuss - rueck)
    return [] if abs(diff) <= tol else [("P-07", None, diff)]


def pruefe_index(reihen, rd, tol=D(0)):
    """P-18 Indexprobe: Index_1 = 1 und Index_j = runde12(Index_(j-1) x (1 + Steigerung)) je Indexreihe."""
    bef = []
    for name, (idx, steigerung) in reihen.items():
        if abs(idx[1] - EINS) > tol:
            bef.append(("P-18", (name, 1), idx[1] - EINS))
        for j in range(2, len(idx)):
            if abs(idx[j] - rd.satz(idx[j - 1] * (EINS + steigerung))) > tol:
                bef.append(("P-18", (name, j), idx[j]))
    return bef


def pruefe_bemessung(L, wertansatz, quote, im_beleihungsraum, ertrag_nachhaltig, mindestdeckung, kd_uebrige, zins_kalk,
                     tilgung_kalk, mittelbedarf, uebrige, zuschuesse, ek_min, p, rd):
    """P-12 Bemessungsprobe: Das gebuchte Bankdarlehen L ueberschreitet keine der drei Grenzen aus R-5.12, jede
    hier aus den Groessen des Auftrags neu gerechnet, und schoepft die engste Grenze aus.

    (a) L <= Beleihungsquote x Wertansatz - Darlehen im Beleihungsraum
    (b) nachhaltiger Reinertrag >= Mindestdeckung x (KD der uebrigen Darlehen + p x runde(L x (i_k + t_k) / p))
    (c) L <= Mittelbedarf - uebrige Darlehen - Zuschuesse - Mindesteigenkapital
    Ausschoepfung: L liegt hoechstens einen Cent unter (a) und (c) oder hoechstens um die Rundungsspanne der Rate
    unter der geschlossenen Form von (b); das Eigenkapital als Ausgleichsposten erreicht das Mindesteigenkapital."""
    bef = []
    cent = D("0.01")
    a = quote * wertansatz - im_beleihungsraum
    c = mittelbedarf - uebrige - zuschuesse - ek_min
    satz = zins_kalk + tilgung_kalk
    tragbar = ertrag_nachhaltig / mindestdeckung - kd_uebrige
    if L < 0:
        bef.append(("P-12", "Bankdarlehen negativ", L))
    if L > max(NULL, a):
        bef.append(("P-12", "Beleihungsgrenze (a)", L - a))
    if L > max(NULL, c):
        bef.append(("P-12", "Restfinanzierung (c)", L - c))
    if L > 0 and ertrag_nachhaltig < mindestdeckung * (kd_uebrige + p * rd.geld(L * satz / p, "kaufm")):
        bef.append(("P-12", "Mindestdeckung (b)", ertrag_nachhaltig - mindestdeckung * (kd_uebrige + p * rd.geld(L * satz / p, "kaufm"))))
    grenzen = [a, c]
    spanne = cent
    if satz > 0:
        grenzen.append(tragbar / satz)
        spanne = max(spanne, p * cent / 2 / satz + cent)       # je Rate hoechstens ein halber Cent Rundung
    elif tragbar < 0:
        grenzen.append(NULL)
    if L < max(NULL, min(grenzen)) - spanne:
        bef.append(("P-12", "engste Grenze nicht ausgeschoepft", L - min(grenzen)))
    if mittelbedarf - uebrige - zuschuesse - L < ek_min:
        bef.append(("P-12", "Mindesteigenkapital", mittelbedarf - uebrige - zuschuesse - L - ek_min))
    return bef


def pruefe_tranchen(tranchen, soll):
    """P-21 Tranchenprobe: Jede Tranche des Finanzplans traegt die Konditionen des Auftrags: Zins, Anschlusszins,
    Ende der Zinsbindung und bei Prozentannuitaeten die Anschlussregel H-07. soll: {Name: {Merkmal: Wert}}, aus dem
    Auftrag gebildet (im Stressfall mit den Stresshoehen)."""
    bef = []
    for tr in tranchen:
        if tr.name not in soll:
            bef.append(("P-21", (tr.name, "ohne Sollkonditionen"), None))
            continue
        for merkmal, wert in soll[tr.name].items():
            if merkmal == "anschluss_regel" and tr.art != "annuitaet_prozent":
                continue
            if getattr(tr, merkmal) != wert:
                bef.append(("P-21", (tr.name, merkmal), getattr(tr, merkmal)))
    return bef
