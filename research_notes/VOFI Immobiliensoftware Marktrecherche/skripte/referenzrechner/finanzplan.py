"""Kapitel 4 und 9 der Fachspezifikation: Finanzplan der Investition und der Unterlassensalternative.

Jede Zeile des Finanzplans hat eine stabile Zeilenkennung (R-4.1, ZEILEN).

Rechenreihenfolge je Periode nach R-4.3 (Schritte 1 bis 10). Zinsen und Steuern einer Periode haengen
nur von Bestaenden der Vorperiode und von Zahlungen der laufenden Periode ab; es gibt keinen Zirkelbezug.
"""
from dataclasses import dataclass, field
from decimal import Decimal as D
from typing import List, Optional
from zahlen import NULL, EINS, d, Rundung, periodensatz_konform, FEHLER
from zeit import Raster
from steuer import Steuer, Steuerparameter, PRIVAT, UEBERSCHUSS

# R-4.1: stabile Zeilenkennungen (Schluessel des Referenzrechners -> Kennung, Bezeichnung)
ZEILEN = {
    "investition": ("Z-A1", "Investition"), "miete": ("Z-A2", "Miete"), "kosten": ("Z-A3", "Bewirtschaftung"),
    "erhaltung": ("Z-A4", "Erhaltung"), "zuschuss": ("Z-A5", "Zuschuss"), "verkauf": ("Z-A6", "Verkauf"),
    "foerder_rueck": ("Z-A7", "Rueckzahlung von Foerdermitteln"),
    "einlage": ("Z-B1", "Einlage"), "entnahme": ("Z-B2", "Entnahme"), "nachschuss": ("Z-B3", "Nachschuss"),
    "auszahlung": ("Z-B4", "Darlehen: Auszahlung"), "einbehalt": ("Z-B5", "Darlehen: einbehaltener Betrag"),
    "zins": ("Z-B6", "Darlehen: Zins"), "tilgung": ("Z-B7", "Darlehen: Tilgung"),
    "beitrag": ("Z-B8", "Darlehen: laufender Beitrag"), "bereit": ("Z-B9", "Darlehen: Bereitstellungszins"),
    "abloesung": ("Z-B10", "Darlehen: Abloesung"), "vfe": ("Z-B11", "Vorfaelligkeit"),
    "zuschuss_einbehalt": ("Z-B12", "einbehaltenes Entgelt auf Zuschuesse"),
    "anlage": ("Z-B13", "Geldanlage: Anlage und Aufloesung"), "habenzins": ("Z-B14", "Geldanlage: Habenzins"),
    "kk_aufnahme": ("Z-B15", "Kontokorrent: Aufnahme und Rueckfuehrung"), "kkzins": ("Z-B16", "Kontokorrent: Zins"),
    "steuer": ("Z-B17", "Steuer"), "fin_saldo": ("Z-S", "Finanzierungssaldo"),
    "guthaben": ("Z-C1", "Guthaben"), "kk": ("Z-C2", "Kontokorrent"), "restschuld": ("Z-C3", "Restschuld"),
    "bestandssaldo": ("Z-C4", "Bestandssaldo"), "afa": ("Z-N1", "Abschreibung"), "e_op": ("Z-N2", "operatives Ergebnis"),
}


@dataclass
class Verkauf:
    """Kapitel 8: Verkauf am Ende der letzten Periode."""
    preis_brutto: D                 # Preis aus dem gewaehlten Massstab (R-8.1, R-8.2)
    kosten: D = NULL                # Verkaufskosten (R-8.3)
    stau_abzug: D = NULL            # ausstehender Investitionsstau zum Preisstand des Stichtags (R-8.4)
    foerder_rueckzahlung: D = NULL  # Rueckzahlung von Foerdermitteln, Zahlung im Finanzplan (R-8.7)
    buchwert: D = NULL              # steuerlicher Restbuchwert (R-7.4)

    @property
    def erloes(self):
        """Im Finanzplan gebuchter Verkaufserloes (Restwertprobe P-05)."""
        return self.preis_brutto - self.kosten - self.stau_abzug


@dataclass
class PlanEingabe:
    """Vollstaendig aufgeloeste Eingabe eines Finanzplans. Alle Reihen haben die Laenge N+1 (Zeitpunkt 0..N)."""
    raster: Raster
    miete: List[D]                  # Mieteinzahlungen nach Mietausfall (steuerpflichtig)
    kosten: List[D]                 # laufende Bewirtschaftung, positiv (abziehbar; mindert den Reinertrag)
    erhaltung: List[D]              # Massnahmen mit Kennzeichen Erhaltung (sofort abziehbar)
    investition: List[D]            # Kaufpreis, Nebenkosten, Baukosten, aktivierte Massnahmen (nicht abziehbar)
    afa: List[D]                    # Abschreibung je Periode aus dem Abschreibungsplan (R-7.3)
    tranchen: list
    steuer: Steuerparameter
    einlagen: List[D]               # geplante Eigenkapitaleinlagen
    entnahmen: List[D]              # geplante Entnahmen
    h_kurz: D                       # kurzfristiger Habenzins, effektiv je Jahr (Geldanlage und Wiederanlage)
    kk_zins: D                      # Kontokorrentzins, effektiv je Jahr
    a_lang: Optional[D] = None      # langfristiger Anlagezins der Unterlassensalternative (None = h_kurz)
    kk_linie: Optional[D] = None    # Kontokorrentlinie; None = unbegrenzt (Lehrbuchfaelle)
    zuschuss: Optional[List[D]] = None          # Zuschuesse mit Geldfluss, brutto
    zuschuss_einbehalt: Optional[List[D]] = None
    verkauf: Optional[Verkauf] = None
    vfe_satz: D = NULL              # Vorfaelligkeitssatz je Jahr Restbindung (R-5.16)
    steuer_einbehalt: Optional[List[D]] = None  # steuerlich abziehbarer Teil der einbehaltenen Betraege je Periode
                                                # (R-7.15: im Betriebsvermoegen ueber die Zinsbindung verteilt);
                                                # None = im Jahr der Zahlung
    steuer_ertrag: Optional[List[D]] = None     # steuerpflichtiger Ertrag aus einem Zuschuss (MA-031)
    rueckzahlung_im_gewinn: bool = True         # R-7.4: die Rueckzahlung von Foerdermitteln mindert den Verkaufsgewinn
                                                # (nur Lesart "Minderung" von MA-031)
    rueckzahlung_laufend: bool = False          # R-7.19: die Rueckzahlung mindert das operative Ergebnis des
                                                # Verkaufsjahres (Lesart "sofortige Einnahme")
    steuer_zuschuss_entgelt: Optional[List[D]] = None   # R-7.19: abziehbarer Teil des Entgelts auf den Zuschuss je
                                                # Periode; None = im Jahr der Zahlung. Kein Entgelt fuer Schulden
    pacht: Optional[List[D]] = None             # Erbbauzins je Periode (in 'kosten' enthalten), fuer GEWSTG-8
    anschaffung: Optional[D] = None             # aktivierte Kosten einschliesslich Boden nach Zuschussminderung;
                                                # Grundlage der Abschreibungsprobe P-08 und der Steuerprobe P-15
    afa_grundlage: Optional[D] = None           # Abschreibungsgrundlage (Gebaeude und aktivierte Massnahmen)
    rundung: Rundung = field(default_factory=Rundung)


class Plan:
    def __init__(self, eingabe):
        self.e = eingabe
        self.zeilen = []            # je Periode ein dict
        self.steuer = None
        self.einlagen_netto = []    # nach Saldierung je Periode (R-10.3), einschliesslich Nachschuss
        self.entnahmen_netto = []
        self.endwert = None

    def reihe(self, schluessel):
        return [z[schluessel] for z in self.zeilen]

    def jahressumme(self, schluessel, j):
        return sum(self.zeilen[u][schluessel] for u in self.e.raster.perioden(j))


def _null(n):
    return [NULL] * (n + 1)


def rechne_plan(e: PlanEingabe) -> Plan:
    """R-4.3: Finanzplan der Investition."""
    r, rd = e.raster, e.rundung
    N, p = r.N, r.p
    zuschuss = e.zuschuss or _null(N)
    zus_einb = e.zuschuss_einbehalt or _null(N)
    plan = Plan(e)
    steuer = plan.steuer = Steuer(e.steuer, r, rd)
    satz_h = periodensatz_konform(e.h_kurz, p, rd)
    satz_kk = periodensatz_konform(e.kk_zins, p, rd)
    guth = kk = NULL
    e_op_jahr = z_h_jahr = entgelte_jahr = pacht_jahr = NULL
    st_einb = e.steuer_einbehalt
    st_ertrag = e.steuer_ertrag or _null(N)
    pacht = e.pacht or _null(N)
    privat = e.steuer.status in UEBERSCHUSS      # R-7.11, R-7.17: die Vorfaelligkeit gehoert zum Verkauf
    st_zus = e.steuer_zuschuss_entgelt

    for u in range(N + 1):
        letzte = u == N and N >= 1
        z = dict(u=u, tranchen={})
        # Schritt 1: originaere Zahlungen
        z["miete"], z["kosten"], z["erhaltung"] = e.miete[u], e.kosten[u], e.erhaltung[u]
        z["investition"], z["zuschuss"], z["zuschuss_einbehalt"] = e.investition[u], zuschuss[u], zus_einb[u]
        z["verkauf"] = e.verkauf.erloes if (letzte and e.verkauf) else NULL
        z["foerder_rueck"] = e.verkauf.foerder_rueckzahlung if (letzte and e.verkauf) else NULL
        z["originaer"] = (z["miete"] - z["kosten"] - z["erhaltung"] - z["investition"] + z["zuschuss"]
                          + z["verkauf"] - z["foerder_rueck"])
        # Schritt 2: Darlehen (ohne freie Tilgung, die Schritt 7 bestimmt)
        freie = []
        for tr in e.tranchen:
            if tr.art == "frei":
                freie.append(tr)
                vorab = NULL if u == 0 else tr._geld(rd, tr.rest * tr.zins_der_periode(u) / p)
                beitr = NULL if u == 0 else tr._geld(rd, tr.rest * tr.beitrag_satz / p)
                aus = tr.auszahlung.get(u, NULL)
                einb = tr.einbehalt if (u == tr._erste_auszahlung and u in tr.auszahlung) else NULL
                z["tranchen"][tr.name] = dict(auszahlung=aus, einbehalt=einb, zins=vorab, tilgung=NULL,
                                              beitrag=beitr, tilgungszuschuss=NULL, abloesung=NULL, bereit=NULL,
                                              satz=NULL if u == 0 else tr.zins_der_periode(u), rest_vor=tr.rest)
            else:
                rest_vor = tr.rest
                tz = tr.periode(u, p, rd, letzte=letzte)
                tz["rest_vor"] = rest_vor
                z["tranchen"][tr.name] = tz
        # Schritt 3: Zinsen auf die Bestaende der Vorperiode
        z["habenzins"] = rd.geld(guth * satz_h) if u >= 1 else NULL
        z["kkzins"] = rd.geld(kk * satz_kk) if u >= 1 else NULL
        z["satz_h"], z["satz_kk"] = satz_h, satz_kk
        # Schritt 4: Vorfaelligkeitsentschaedigung bei Abloesung in der Zinsbindung (R-5.16)
        z["vfe"] = NULL
        if letzte and e.vfe_satz:
            for tr in e.tranchen:
                # Restbindung bis zum Ende der Zinsbindung, hoechstens bis zum fruehesten Kuendigungstermin
                # (BGB-489); keine Entschaedigung fuer Foerderdarlehen
                if not tr.foerder and tr.vfe_bis is not None and tr.vfe_bis > N:
                    basis = z["tranchen"][tr.name]["abloesung"] if tr.art != "frei" else tr.rest
                    z["vfe"] += rd.geld(basis * e.vfe_satz * D(tr.vfe_bis - N) / p)

        def summe(k):
            return sum(t[k] for t in z["tranchen"].values())

        # Schritt 5: steuerliche Nebenrechnung; Zahlung am Ende des Planjahres (R-2.7)
        z["afa"] = e.afa[u]
        sollzins, beitrag, bereit = summe("zins"), summe("beitrag"), summe("bereit")
        einbehalt = summe("einbehalt")
        # R-7.15: einbehaltene Betraege steuerlich im Jahr der Zahlung oder verteilt; R-7.11: die Vorfaelligkeit
        # der Privatperson gehoert zum Verkauf
        z["einbehalt_steuer"] = einbehalt if st_einb is None else st_einb[u]
        # R-7.19: das Entgelt auf einen Zuschuss folgt der Lesart des Zuschusses und ist kein Entgelt fuer Schulden
        z["zuschuss_entgelt_steuer"] = z["zuschuss_einbehalt"] if st_zus is None else st_zus[u]
        z["steuer_ertrag"] = st_ertrag[u]
        vfe_op = NULL if privat else z["vfe"]
        z["entgelte"] = sollzins + z["kkzins"] + beitrag + bereit + z["einbehalt_steuer"] + vfe_op
        z["e_op"] = (z["miete"] - z["kosten"] - z["erhaltung"] - z["afa"] - z["entgelte"] + z["steuer_ertrag"]
                     - z["zuschuss_entgelt_steuer"])
        if letzte and e.verkauf and e.rueckzahlung_laufend:
            z["e_op"] -= e.verkauf.foerder_rueckzahlung
        if "afa_doppelt" in FEHLER:             # Fehlerbild RF-16: Abschreibung zweimal abgezogen
            z["e_op"] -= z["afa"]
        e_op_jahr += z["e_op"]
        z_h_jahr += z["habenzins"]
        entgelte_jahr += z["entgelte"]
        pacht_jahr += pacht[u]
        z["steuer"] = NULL
        z["g_v"] = NULL
        z["vfe_verkauf"] = z["vfe"] if privat else NULL
        if r.jahresende(u):
            if letzte and e.verkauf:
                z["g_v"] = e.verkauf.erloes - e.verkauf.buchwert
                if e.rueckzahlung_im_gewinn:
                    z["g_v"] -= e.verkauf.foerder_rueckzahlung
            z["steuer"] = steuer.jahr(r.planjahr(u), e_op_jahr, z_h_jahr, z["g_v"], entgelte_jahr, pacht_jahr,
                                      z["vfe_verkauf"])
            e_op_jahr = z_h_jahr = entgelte_jahr = pacht_jahr = NULL
        # Schritt 6: vorlaeufiger Saldo ohne freie Tilgung und ohne Eigenkapitalbewegungen
        vorlaeufig = (z["originaer"] + summe("auszahlung") - einbehalt - z["zuschuss_einbehalt"]
                      - sollzins - beitrag - bereit - summe("tilgung") - summe("abloesung") - z["vfe"]
                      + z["habenzins"] - z["kkzins"] - z["steuer"])
        # Schritt 7: freie Tilgung aus der verfuegbaren Liquiditaet (R-5.7)
        for tr in freie:
            liquid = guth - kk + vorlaeufig + e.einlagen[u] - e.entnahmen[u]
            rest_vor = tr.rest
            tz = tr.periode(u, p, rd, letzte=letzte, liquiditaet=liquid)
            tz["rest_vor"] = rest_vor
            z["tranchen"][tr.name] = tz
            vorlaeufig -= tz["tilgung"] + tz["abloesung"]
        for k in ("auszahlung", "einbehalt", "zins", "tilgung", "beitrag", "tilgungszuschuss", "abloesung", "bereit"):
            z[k] = summe(k)
        # Schritt 8: Eigenkapital
        einlage, entnahme = e.einlagen[u], e.entnahmen[u]
        saldo = vorlaeufig + einlage - entnahme
        # Schritt 9: Ausgleich ueber Geldanlage und Kontokorrent; Nachschuss bei erschoepfter Linie (R-4.5)
        netto = guth - kk + saldo
        nachschuss = NULL
        if netto >= 0:
            guth_neu, kk_neu = netto, NULL
        else:
            guth_neu, kk_neu = NULL, -netto
            if e.kk_linie is not None and kk_neu > e.kk_linie:
                nachschuss = kk_neu - e.kk_linie
                kk_neu = e.kk_linie
        z["einlage"], z["entnahme"], z["nachschuss"] = einlage, entnahme, nachschuss
        z["anlage"] = guth_neu - guth                 # + Anlage, - Aufloesung
        z["kk_aufnahme"] = kk_neu - kk                # + Aufnahme, - Rueckfuehrung
        z["fin_saldo"] = saldo + nachschuss - z["anlage"] + z["kk_aufnahme"]
        guth, kk = guth_neu, kk_neu
        # Schritt 10: Bestaende
        z["guthaben"], z["kk"] = guth, kk
        z["restschuld"] = sum(tr.rest for tr in e.tranchen)
        for tr in e.tranchen:
            z["tranchen"][tr.name]["rest"] = tr.rest
        z["bestandssaldo"] = guth - kk - z["restschuld"]
        z["guthaben_vor"], z["kk_vor"] = guth - z["anlage"], kk - z["kk_aufnahme"]
        # Saldierung der Eigenkapitalbewegungen je Periode (R-10.3)
        ek = einlage + nachschuss - entnahme
        plan.einlagen_netto.append(max(ek, NULL))
        plan.entnahmen_netto.append(max(-ek, NULL))
        plan.zeilen.append(z)
    plan.endwert = plan.zeilen[-1]["bestandssaldo"]
    return plan


# ---------------------------------------------------------------------------------------------
class Alternative:
    def __init__(self):
        self.zeilen = []
        self.endwert = None
        self.steuer = None

    def bestand(self, u):
        z = self.zeilen[u]
        return z["lang"] + z["kurz"] - z["kk"]


def rechne_alternative(e: PlanEingabe, einlagen, entnahmen) -> Alternative:
    """Kapitel 9: Unterlassensalternative als eigener Finanzplan (R-9.1 bis R-9.7).

    Einlagen werden zum langfristigen Anlagezins angelegt; die Zinsen fliessen je Periode auf ein
    Wiederanlagekonto zum kurzfristigen Satz. Entnahmen und Steuern werden zuerst vom Wiederanlagekonto
    bedient, dann durch Aufloesung der langfristigen Anlage zum Nennwert, zuletzt ueber Kontokorrent.
    """
    r, rd = e.raster, e.rundung
    N, p = r.N, r.p
    alt = Alternative()
    steuer = alt.steuer = Steuer(e.steuer, r, rd, alternative=True)
    privat = e.steuer.status == PRIVAT      # R-9.5 (ESTG-20): Kontokorrentzinsen der Privatperson nicht abziehbar
    a_lang = e.h_kurz if e.a_lang is None else e.a_lang
    if "alternative_zins" in FEHLER:            # Fehlerbild RF-16: Anlagezins mit dem Kontokorrentzins verwechselt
        a_lang = e.kk_zins
    s_lang = periodensatz_konform(a_lang, p, rd)
    s_kurz = periodensatz_konform(e.h_kurz, p, rd)
    s_kk = periodensatz_konform(e.kk_zins, p, rd)
    lang = kurz = kk = NULL
    zinsen_jahr = kkz_jahr = NULL
    for u in range(N + 1):
        z = dict(u=u, einlage=einlagen[u], entnahme=entnahmen[u])
        z["zins_lang"] = rd.geld(lang * s_lang) if u >= 1 else NULL
        z["zins_kurz"] = rd.geld(kurz * s_kurz) if u >= 1 else NULL
        z["kkzins"] = rd.geld(kk * s_kk) if u >= 1 else NULL
        zinsen_jahr += z["zins_lang"] + z["zins_kurz"]
        kkz_jahr += z["kkzins"]
        z["steuer"] = NULL
        if r.jahresende(u):
            z["steuer"] = steuer.jahr(r.planjahr(u), NULL if privat else -kkz_jahr, zinsen_jahr, NULL,
                                      NULL if privat else kkz_jahr)
            zinsen_jahr = kkz_jahr = NULL
        # Einlage: zuerst Kontokorrent zurueckfuehren, der Rest in die langfristige Anlage
        einl = einlagen[u]
        tilg_kk = min(kk, einl)
        kk -= tilg_kk
        lang += einl - tilg_kk
        netto = kurz - kk + z["zins_lang"] + z["zins_kurz"] - z["kkzins"] - z["steuer"] - entnahmen[u]
        if "alternative_ohne_steuerabzug" in FEHLER:    # Fehlerbild RF-16: Steuer gerechnet, aber nicht gebucht
            netto += z["steuer"]
        if netto >= 0:
            kurz, kk = netto, NULL
        else:
            fehl = -netto
            aus_lang = min(lang, fehl)
            lang -= aus_lang
            kurz, kk = NULL, fehl - aus_lang
        z["lang"], z["kurz"], z["kk"] = lang, kurz, kk
        z["satz_lang"], z["satz_kurz"], z["satz_kk"] = s_lang, s_kurz, s_kk
        alt.zeilen.append(z)
    alt.endwert = lang + kurz - kk
    return alt


# ---------------------------------------------------------------------------------------------
def verdichte(plan: Plan):
    """R-2.3: Jahresdarstellung. Zahlungen werden je Planjahr summiert, Bestaende sind der Stand am Jahresende."""
    r = plan.e.raster
    fluss = ("miete", "kosten", "erhaltung", "investition", "zuschuss", "verkauf", "foerder_rueck", "originaer",
             "auszahlung", "einbehalt", "zuschuss_einbehalt", "zins", "tilgung", "beitrag", "bereit",
             "tilgungszuschuss", "abloesung", "vfe", "habenzins", "kkzins", "steuer", "afa", "e_op",
             "einlage", "entnahme", "nachschuss", "anlage", "kk_aufnahme", "fin_saldo")
    bestand = ("guthaben", "kk", "restschuld", "bestandssaldo")
    jahre = [dict(jahr=0, **{k: plan.zeilen[0][k] for k in fluss + bestand})]
    for j in range(1, r.n + 1):
        zeile = dict(jahr=j)
        for k in fluss:
            zeile[k] = plan.jahressumme(k, j)
        for k in bestand:
            zeile[k] = plan.zeilen[j * r.p - (1 if "verdichtung_bestand" in FEHLER else 0)][k]   # Fehlerbild RF-16
        jahre.append(zeile)
    return jahre


def lehrbuchansicht(plan: Plan):
    """R-4.7: Darstellung als einjaehrige Reinvestition und Zwischenfinanzierung (nur Jahresmodus).

    Zeile 'reinvestition'[t] ist die Anlage am Ende von t (Guthabenstand), 'zwischenfinanzierung'[t]
    der Kontokorrentstand. Rueckfluss und Zins erscheinen in t+1. Die Spaltensumme ist in t < n null
    und in t = n das Endvermoegen.
    """
    assert plan.e.raster.p == 1, "Lehrbuchansicht nur im Jahresmodus"
    z, n = plan.zeilen, plan.e.raster.N
    ans = []
    for t in range(n + 1):
        v = z[t - 1] if t >= 1 else None
        zeile = dict(
            t=t,
            direkte_zahlungen=z[t]["originaer"],
            eigenkapital=z[t]["einlage"] + z[t]["nachschuss"] - z[t]["entnahme"],
            kreditaufnahme=z[t]["auszahlung"] - z[t]["einbehalt"] - z[t]["zuschuss_einbehalt"],
            zinsen_fk=-(z[t]["zins"] + z[t]["beitrag"] + z[t]["bereit"] + z[t]["vfe"]),
            tilgung=-(z[t]["tilgung"] + z[t]["abloesung"]),
            steuerzahlung=-z[t]["steuer"],
            rueckzahlung_reinvestition=v["guthaben"] if v else NULL,
            habenzinsen=z[t]["habenzins"],
            rueckzahlung_zwischenfinanzierung=-(v["kk"] if v else NULL),
            sollzinsen_zwischenfinanzierung=-z[t]["kkzins"],
            reinvestition=-z[t]["guthaben"] if t < n else NULL,
            zwischenfinanzierung=z[t]["kk"] if t < n else NULL,
            kredit_nach_tilgung=z[t]["restschuld"],
        )
        zeile["saldo"] = sum(v_ for k, v_ in zeile.items() if k not in ("t", "kredit_nach_tilgung"))
        ans.append(zeile)
    return ans
