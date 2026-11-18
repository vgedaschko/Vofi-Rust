"""Kapitel 3 und 11 der Fachspezifikation: Eingaben der Grobkalkulation 1a, Aufbau des Finanzplans daraus,
hoechster tragbarer Preis, kombinierter Stressfall, Zielwertsuche, Vergleich zweier Fassungen.

Der Rechenkern erhaelt einen vollstaendig aufgeloesten Auftrag (R-3.1): Eingaben des Anwenders, Vorgaben des
Hauses und Katalogwerte. In diesem Modul steht kein Satz und keine Schwelle als Festwert.
"""
from dataclasses import dataclass, field, replace
from decimal import Decimal as D
from typing import Optional
from zahlen import NULL, EINS, d, Rundung, ab_cent
from zeit import Raster
from darlehen import Tranche, bankdarlehen
from steuer import Steuerparameter
from finanzplan import PlanEingabe, Verkauf, rechne_plan, rechne_alternative
from kennzahlen import werte_aus, schuldendienstdeckung
from proben import pruefe_plan, pruefe_mittel, pruefe_stau, pruefe_zuschuss, pruefe_abschreibung
import ertrag
import restwert


@dataclass
class Stress:
    """H-06: Hoehen des kombinierten Stressfalls (ermaessigt gegenueber den Einzelfaellen)."""
    anschlusszins_pp: D = NULL          # Aufschlag auf den Anschlusszins in Prozentpunkten (als Dezimalbruch)
    mietausfall_pp: D = NULL            # Aufschlag auf die Mietausfallquote
    verkaufsfaktor_rel: D = NULL        # Abschlag auf den Verkaufsfaktor, relativ
    mietsteigerung_pp: D = NULL         # Abschlag auf die Mietsteigerung
    instandhaltung_rel: D = NULL        # Aufschlag auf die Instandhaltungskosten, relativ
    baukosten_rel: D = NULL             # Aufschlag auf die Baukosten, relativ (nur Neubau)
    bauzeit_monate: int = 0             # Verlaengerung der Bauzeit (nur Neubau)


@dataclass
class Vorgaben:
    """Vorgaben des Hauses (H-..) und aufgeloeste Katalogwerte (KAT-..). In den Referenzfaellen Annahmen."""
    zielrendite: D
    beleihungsquote: D
    mindestdeckung: D
    mindesttilgung: D
    anschluss_aufschlag: D
    h_kurz: D
    kk_zins: D
    mietsteigerung: D
    kostensteigerung: D
    baupreissteigerung: D
    mietausfall: D
    verkaufskostensatz: D
    verwaltung_je_einheit: D
    instandhaltung_je_qm: D
    betriebskosten_je_qm: D
    kappung: D
    afa_satz: D
    a_lang: Optional[D] = None
    kk_linie: Optional[D] = NULL
    vfe_satz: D = NULL
    anschluss_regel: str = "tilgungssatz"
    nur_eigenes_darlehen: bool = False          # andere Lesart von MA-026
    stress: Stress = field(default_factory=Stress)
    suchobergrenze_faktor: D = D(100)           # H-21: Obergrenze der Preissuche als Vielfaches der Jahresmiete
    suchraster: int = 40
    warnschwelle_restwertanteil: Optional[D] = None


@dataclass
class Foerderung:
    """Grobfoerderung (aufgeloeste Katalogwerte, NBANK-RL-MIETWOHNRAUM-2026; MA-002, MA-004, MA-005, MA-017, MA-021)."""
    darlehensquote: D
    zuschussquote: D
    eigenmittelquote: D
    bemessungsgrenze_je_qm: D
    bodenrichtwert: D
    eingangsmiete: D
    steigerung: D                    # hoechste Steigerung je Schritt
    fest_jahre: int
    schritt_jahre: int
    bindung_jahre: int
    vkb_satz: D
    entgelt_darlehen: D
    entgelt_zuschuss: D
    tilgung_jahre: int
    zinslos_jahre: int
    zins_danach: D


@dataclass
class Grobeingabe:
    art: str                          # "ankauf" oder "neubau"
    steuer: Steuerparameter
    zins: D
    zinsbindung_jahre: int
    verkaufsfaktor: D
    haltedauer: int
    wohnflaeche: D
    einheiten: int
    startjahr: int = 2027
    # Ankauf
    kaufpreis: D = NULL
    enk_satz: D = NULL
    bodenanteil: D = NULL
    ist_miete: D = NULL
    markt_miete: D = NULL
    # Neubau
    grundstueckspreis: D = NULL
    grundstuecksflaeche: D = NULL
    bgf: D = NULL
    kostenkennwert: D = NULL
    bauzeit_monate: int = 0
    # Pauschalen
    tilgungssatz: Optional[D] = None
    anpassungsdauer: int = 0
    stau_betrag: D = NULL
    stau_jahr: int = 0
    stau_art: str = "erhaltung"
    co2_je_qm: D = NULL
    co2_steigerung: D = NULL
    gebunden_anteil: D = NULL
    bindung_jahre: int = 0
    gebundene_miete: Optional[D] = None
    geb_steigerung: D = NULL
    geb_fest_jahre: int = 3
    geb_schritt_jahre: int = 3
    uebernommen: Optional[dict] = None     # restschuld, zins, tilgungssatz, bindung_jahre, anschluss_zins, beitrag_satz
    # freiwillig oder im Einzelfall
    verfuegbares_ek: Optional[D] = None
    wertansatz_bank: Optional[D] = None
    erbbauzins: D = NULL
    erbbauzins_steigerung: D = NULL
    foerderung: Optional[Foerderung] = None


class Meldung(Exception):
    """Definiertes Ergebnis statt Fehler (Kapitel 14): Kennung und Klartext."""

    def __init__(self, kennung, text):
        super().__init__(f"{kennung}: {text}")
        self.kennung, self.text = kennung, text


@dataclass
class Bemessung:
    """Groessen, die vor dem Finanzplan feststehen (R-11.2)."""
    preis: D
    enk: D
    baukosten: D
    mittelbedarf: D
    wertansatz: D
    uebrige: D
    zuschuss: D
    foerderdarlehen: D
    ek_min: D
    einbehalt_darlehen: D
    einbehalt_zuschuss: D
    reinertrag_vj: D
    kd_uebrige: D
    bank: dict


class Grobergebnis:
    pass


def _ertragsreihen(ein, vg, raster, rd, stress, bauzeit):
    """Kapitel 6: Mieteinzahlungen, laufende Kosten und Sollmieten je Periode (unabhaengig von der Finanzierung)."""
    p, N = raster.p, raster.N
    st = vg.stress if stress else Stress()
    jahre = raster.n + 2
    steig = vg.mietsteigerung - st.mietsteigerung_pp
    ausfall = vg.mietausfall + st.mietausfall_pp
    if ein.art == "ankauf":
        je_qm, markt = ertrag.mietreihe_je_qm(
            jahre, ein.ist_miete, ein.markt_miete, steig, ein.anpassungsdauer, vg.kappung, rd,
            gebunden_anteil=ein.gebunden_anteil, gebunden_start=ein.gebundene_miete,
            bindung_jahre=ein.bindung_jahre, geb_steigerung=ein.geb_steigerung,
            geb_fest=ein.geb_fest_jahre, geb_schritt=ein.geb_schritt_jahre)
    elif ein.foerderung:
        f = ein.foerderung
        je_qm, markt = ertrag.mietreihe_je_qm(
            jahre, ein.markt_miete, ein.markt_miete, steig, ein.anpassungsdauer, vg.kappung, rd,
            gebunden_anteil=EINS if ein.gebunden_anteil == 0 else ein.gebunden_anteil,
            gebunden_start=f.eingangsmiete, bindung_jahre=f.bindung_jahre, geb_steigerung=f.steigerung,
            geb_fest=f.fest_jahre, geb_schritt=f.schritt_jahre)
    else:
        je_qm, markt = ertrag.mietreihe_je_qm(jahre, ein.markt_miete, ein.markt_miete, steig, 0, vg.kappung, rd)
    idx_k = ertrag.indexreihe(jahre + bauzeit // p + 1, vg.kostensteigerung, rd)
    idx_co2 = ertrag.indexreihe(jahre + bauzeit // p + 1, ein.co2_steigerung, rd)
    idx_erb = ertrag.indexreihe(jahre + bauzeit // p + 1, ein.erbbauzins_steigerung, rd)
    inst = vg.instandhaltung_je_qm * (EINS + st.instandhaltung_rel)

    def soll(u):                                         # Sollmiete der Periode u (auch u > N fuer den Restwert)
        if u <= bauzeit:
            return NULL
        v = (u - bauzeit - 1) // p + 1                   # Vermietungsjahr
        return rd.geld(ein.wohnflaeche * je_qm[v] * 12 / p)

    def kosten(u):
        j = (u - 1) // p + 1                             # Planjahr: Preisstand der Kosten (R-6.8)
        betrieb = NULL
        if u > bauzeit:
            jahr = (vg.verwaltung_je_einheit * ein.einheiten + inst * ein.wohnflaeche
                    + vg.betriebskosten_je_qm * ein.wohnflaeche) * idx_k[j]
            betrieb = rd.geld(jahr / p) + rd.geld(ein.co2_je_qm * ein.wohnflaeche * idx_co2[j] / p)
        return betrieb + rd.geld(ein.erbbauzins * idx_erb[j] / p)

    def einzahlung(u):
        return rd.geld(soll(u) * (EINS - ausfall))

    return soll, einzahlung, kosten, je_qm, markt


def bemesse(ein, vg, raster, rd, preis=None):
    """R-11.2: Mittelbedarf, uebrige Darlehen, Zuschuesse und Bankdarlehen nach R-5.12 aus den Basisannahmen."""
    p = raster.p
    neubau = ein.art == "neubau"
    P = d(preis) if preis is not None else (ein.grundstueckspreis if neubau else ein.kaufpreis)
    enk = rd.geld(P * ein.enk_satz)
    baukosten = rd.geld(ein.bgf * ein.kostenkennwert) if neubau else NULL
    bauzeit = ein.bauzeit_monate if neubau else 0
    if raster.N < bauzeit + p:
        raise Meldung("M-23", "Haltedauer endet vor dem Ende des ersten Jahres der Vollvermietung")
    stau0 = rd.geld(ein.stau_betrag) if (ein.stau_betrag and ein.stau_jahr == 0) else NULL
    soll, einzahlung, kosten, _, _ = _ertragsreihen(ein, vg, raster, rd, False, bauzeit)
    vj = range(bauzeit + 1, bauzeit + p + 1)             # erstes Jahr der Vollvermietung
    reinertrag_vj = sum(einzahlung(u) - kosten(u) for u in vj)
    uebrige = zuschuss = fd = ek_min = e_d = e_z = kd_ue = NULL
    if ein.uebernommen:
        ue = ein.uebernommen
        uebrige = d(ue["restschuld"])
        tr = _tranche_uebernommen(ue, p)
        tr.periode(0, p, rd)
        for u in vj:
            t = tr.periode(u, p, rd)
            kd_ue += t["zins"] + t["tilgung"] + t["beitrag"]
    if ein.foerderung:
        f = ein.foerderung
        # zuwendungsfaehige Kosten: Herstellung bis zur Bemessungsgrenze, Grundstueck bis zum Bodenrichtwert
        zk = (min(baukosten, f.bemessungsgrenze_je_qm * ein.wohnflaeche)
              + min(P + enk, f.bodenrichtwert * ein.grundstuecksflaeche))
        fd, zuschuss, ek_min = rd.geld(f.darlehensquote * zk), rd.geld(f.zuschussquote * zk), rd.geld(f.eigenmittelquote * zk)
        e_d, e_z = rd.geld(fd * f.entgelt_darlehen), rd.geld(zuschuss * f.entgelt_zuschuss)
        uebrige += fd
        tr = _tranche_foerder(f, fd, {0: fd}, NULL, 1, p)
        tr.periode(0, p, rd)
        for u in range(1, p + 1):                        # Kapitaldienst eines vollen Jahres ab Tilgungsbeginn
            t = tr.periode(u, p, rd)
            kd_ue += t["zins"] + t["tilgung"] + t["beitrag"]
    mittelbedarf = P + enk + baukosten + stau0 + e_d + e_z
    wert = ein.wertansatz_bank if ein.wertansatz_bank is not None else (P + enk + baukosten if neubau else P)
    tilg = ein.tilgungssatz if ein.tilgungssatz is not None else vg.mindesttilgung
    bank = bankdarlehen(wert, vg.beleihungsquote, reinertrag_vj, vg.mindestdeckung, ein.zins, tilg, mittelbedarf,
                        uebrige_darlehen=uebrige, kd_uebrige=kd_ue, zuschuesse=zuschuss, ek_min=ek_min,
                        nur_eigenes=vg.nur_eigenes_darlehen, p=p, rd=rd)
    if bank["c"] < 0:
        raise Meldung("M-22", "Uebrige Darlehen, Zuschuesse und Mindesteigenkapital uebersteigen den Mittelbedarf")
    return Bemessung(P, enk, baukosten, mittelbedarf, wert, uebrige, zuschuss, fd, ek_min, e_d, e_z,
                     reinertrag_vj, kd_ue, bank)


def _tranche_uebernommen(ue, p):
    bindung = ue.get("bindung_jahre")
    return Tranche("Uebernommenes Darlehen", ue["restschuld"], "annuitaet_prozent", ue["zins"],
                   tilgungssatz=ue["tilgungssatz"], bindung=None if bindung is None else bindung * p,
                   anschluss_zins=ue.get("anschluss_zins"), beitrag_satz=ue.get("beitrag_satz", 0), bank=False)


def _tranche_foerder(f, betrag, auszahlung, einbehalt, tilgungsbeginn, p):
    # MA-002: gleichbleibende Raten ueber die Tilgungsdauer ab Vollauszahlung; zinslos, danach MA-003
    return Tranche("Foerderdarlehen", betrag, "raten", 0, laufzeit=f.tilgung_jahre * p, auszahlung=auszahlung,
                   einbehalt=einbehalt, tilgungsbeginn=tilgungsbeginn,
                   bindung=f.zinslos_jahre * p + tilgungsbeginn - 1, anschluss_zins=f.zins_danach,
                   beitrag_satz=f.vkb_satz, bank=False, vfe_pflichtig=False)


def rechne_grob(ein: Grobeingabe, vg: Vorgaben, preis=None, stress=False, rundung="cent", p=12,
                mit_blatt=True) -> Grobergebnis:
    """R-11.1: eine Grobkalkulation im Basisfall oder im kombinierten Stressfall."""
    rd = Rundung(rundung)
    raster = Raster(p=p, n=ein.haltedauer, startjahr=ein.startjahr)
    N = raster.N
    neubau = ein.art == "neubau"
    st = vg.stress if stress else Stress()
    bm = bemesse(ein, vg, raster, rd, preis)             # Darlehen stets aus dem Basisfall (R-11.8)
    L = bm.bank["darlehen"]
    bauzeit = (ein.bauzeit_monate + st.bauzeit_monate) if neubau else 0
    if N < bauzeit + p:
        raise Meldung("M-23", "Haltedauer endet vor dem Ende des ersten Jahres der Vollvermietung")
    baukosten = rd.geld(bm.baukosten * (EINS + st.baukosten_rel))
    soll, einzahlung, kosten, je_qm, markt = _ertragsreihen(ein, vg, raster, rd, stress, bauzeit)
    null = lambda: [NULL] * (N + 1)
    miete, kost, erh, inv, zus, zus_einb, afa, einl = (null() for _ in range(8))
    for u in range(1, N + 1):
        miete[u], kost[u] = einzahlung(u), kosten(u)
    # ---- Investitionsauszahlungen
    inv[0] = bm.preis + bm.enk
    if neubau:
        rate = rd.geld(baukosten / bauzeit)
        for m in range(1, bauzeit + 1):
            inv[m] = rate if m < bauzeit else baukosten - rate * (bauzeit - 1)
    # ---- Investitionsstau (R-6.10)
    bpi = ertrag.indexreihe(raster.n + 2, vg.baupreissteigerung, rd)     # bpi[k+1] = Preisstand Ende Jahr k
    stau_zahlung = stau_aktiv = stau_offen = NULL
    stau_jahr = None
    if ein.stau_betrag:
        if ein.stau_jahr <= raster.n:
            stau_zahlung = rd.geld(ein.stau_betrag * bpi[ein.stau_jahr + 1])
            ziel = erh if ein.stau_art == "erhaltung" else inv
            ziel[ein.stau_jahr * p] += stau_zahlung
            stau_jahr = ein.stau_jahr
            if ein.stau_art != "erhaltung":
                stau_aktiv = stau_zahlung
        else:
            stau_offen = restwert.stau_abzug(ein.stau_betrag, bpi[raster.n + 1], EINS, rd)
    # ---- Mittelabruf: Eigenkapital zuerst, dann Foerdermittel im Verhaeltnis, dann Bankdarlehen (R-11.3)
    ek_basis = bm.mittelbedarf - bm.uebrige - bm.zuschuss - L + (baukosten - bm.baukosten)
    aus_bank, aus_fd = {}, {}
    rest_ek, rest_fd, rest_zs, rest_bank = ek_basis, bm.foerderdarlehen, bm.zuschuss, L
    uebern = d(ein.uebernommen["restschuld"]) if ein.uebernommen else NULL
    foerder_gezogen = False
    for m in range(0, bauzeit + 1):
        bedarf = inv[m] + (erh[0] if m == 0 else NULL) - (uebern if m == 0 else NULL)
        x = min(rest_ek, bedarf)
        if x:
            einl[m] += x
            rest_ek -= x
            bedarf -= x
        if bedarf > 0 and (rest_fd + rest_zs) > 0:
            if not foerder_gezogen:
                bedarf += bm.einbehalt_darlehen + bm.einbehalt_zuschuss
                zus_einb[m] += bm.einbehalt_zuschuss
                foerder_gezogen = True
            y = min(rest_fd + rest_zs, bedarf)
            if y == rest_fd + rest_zs:
                teil_fd, teil_zs = rest_fd, rest_zs
            else:                                        # Darlehen und Zuschuss im Verhaeltnis ihrer Betraege
                teil_fd = min(rest_fd, rd.geld(y * bm.foerderdarlehen / (bm.foerderdarlehen + bm.zuschuss)))
                teil_zs = y - teil_fd
                if teil_zs > rest_zs:
                    teil_zs, teil_fd = rest_zs, y - rest_zs
            if teil_fd:
                aus_fd[m] = teil_fd
            zus[m] += teil_zs
            rest_fd -= teil_fd
            rest_zs -= teil_zs
            bedarf -= y
        if bedarf > 0 and rest_bank > 0:
            y = min(rest_bank, bedarf)
            aus_bank[m] = y
            rest_bank -= y
            bedarf -= y
        if bedarf > 0:                                   # sonst deckt Eigenkapital (Stressfall, Rundungsrest)
            einl[m] += bedarf
    # nicht abgerufene Mittel fliessen mit der letzten Bauperiode (R-11.3)
    if rest_bank > 0:
        aus_bank[bauzeit] = aus_bank.get(bauzeit, NULL) + rest_bank
    if rest_fd > 0:
        aus_fd[bauzeit] = aus_fd.get(bauzeit, NULL) + rest_fd
    if rest_zs > 0:
        zus[bauzeit] += rest_zs
    if rest_ek > 0:
        einl[bauzeit] += rest_ek
    # ---- Tranchen
    tilg = ein.tilgungssatz if ein.tilgungssatz is not None else vg.mindesttilgung
    tranchen = []
    if L > 0:
        tranchen.append(Tranche(
            "Bankdarlehen", L, "annuitaet_prozent", ein.zins, tilgungssatz=tilg, auszahlung=aus_bank or {0: L},
            tilgungsbeginn=bauzeit + 1, bindung=ein.zinsbindung_jahre * p,
            anschluss_zins=ein.zins + vg.anschluss_aufschlag + st.anschlusszins_pp,
            anschluss_regel=vg.anschluss_regel, anschluss_tilgung=tilg, bank=True))
    if ein.uebernommen:
        tranchen.append(_tranche_uebernommen(ein.uebernommen, p))
    if ein.foerderung and bm.foerderdarlehen > 0:
        tranchen.append(_tranche_foerder(ein.foerderung, bm.foerderdarlehen, aus_fd, bm.einbehalt_darlehen,
                                         bauzeit + 1, p))
    # ---- Abschreibungsplan (R-7.3): linear, Buchung am Ende jedes Planjahres, zeitanteilig ab Nutzungsbeginn
    if neubau:
        boden, basis = bm.preis + bm.enk, max(NULL, baukosten - bm.zuschuss)
    else:
        boden = rd.geld((bm.preis + bm.enk) * ein.bodenanteil)
        basis = max(NULL, bm.preis + bm.enk - boden - bm.zuschuss)
    rest_basis = basis
    rest_stau = stau_aktiv                               # aktivierte Massnahme: Abschreibung ab dem Folgejahr
    for j in range(1, raster.n + 1):
        ende = j * p
        monate = max(0, ende - max(bauzeit, (j - 1) * p))
        a = min(rest_basis, rd.geld(basis * vg.afa_satz * D(monate) / p))
        rest_basis -= a
        a_stau = NULL
        if stau_aktiv and j > stau_jahr:
            a_stau = min(rest_stau, rd.geld(stau_aktiv * vg.afa_satz))
            rest_stau -= a_stau
        afa[ende] = a + a_stau
    buchwert = boden + rest_basis + rest_stau
    # ---- Verkauf (Kapitel 8)
    faktor = ein.verkaufsfaktor * (EINS - st.verkaufsfaktor_rel)
    sollmiete_folgejahr = sum(soll(u) for u in range(N + 1, N + p + 1))
    preis_vk = restwert.preis_aus_faktor(faktor, sollmiete_folgejahr, rd)
    rueck = NULL
    bindung_perioden = verbleibend = 0
    if ein.foerderung and bm.zuschuss > 0:
        bindung_perioden = ein.foerderung.bindung_jahre * p      # Bindung beginnt mit der Bezugsfertigkeit
        verbleibend = max(0, bauzeit + bindung_perioden - N)
        rueck = restwert.zuschuss_rueckzahlung(bm.zuschuss, bindung_perioden, verbleibend, rd)
    vk = Verkauf(preis_brutto=preis_vk, kosten=restwert.verkaufskosten(preis_vk, vg.verkaufskostensatz, rd),
                 stau_abzug=stau_offen, foerder_rueckzahlung=rueck, buchwert=buchwert)
    steuer = replace(ein.steuer, haltedauer=ein.haltedauer)
    pe = PlanEingabe(raster=raster, miete=miete, kosten=kost, erhaltung=erh, investition=inv, afa=afa,
                     tranchen=tranchen, steuer=steuer, einlagen=einl, entnahmen=null(), h_kurz=vg.h_kurz,
                     kk_zins=vg.kk_zins, a_lang=vg.a_lang, kk_linie=vg.kk_linie, zuschuss=zus,
                     zuschuss_einbehalt=zus_einb, verkauf=vk, vfe_satz=vg.vfe_satz, rundung=rd)
    plan = rechne_plan(pe)
    alt = rechne_alternative(pe, plan.einlagen_netto, plan.entnahmen_netto)
    erg = Grobergebnis()
    erg.ein, erg.vg, erg.stress, erg.bemessung, erg.plan, erg.alt = ein, vg, stress, bm, plan, alt
    erg.kennzahlen = kz = werte_aus(plan, alt, vg.zielrendite)
    erg.darlehen = L
    erg.preis = bm.preis
    erg.verkauf = vk
    erg.bauzeit = bauzeit
    erg.miete_je_qm = je_qm
    # ---- Proben (Kapitel 13)
    bef = pruefe_plan(plan, alt)
    invest_ende = bauzeit
    ph = plan.zeilen[:invest_ende + 1]                    # Investitionsphase: Zeitpunkt 0 bis Ende der Bauzeit
    bank_name = "Bankdarlehen"
    herkunft = dict(
        eigenkapital=sum(plan.einlagen_netto[:invest_ende + 1]),
        bankdarlehen=sum(z["tranchen"][bank_name]["auszahlung"] for z in ph) if L > 0 else NULL,
        uebrige_darlehen=sum((t["auszahlung"] for z in ph for n_, t in z["tranchen"].items() if n_ != bank_name), NULL),
        zuschuesse=sum((z["zuschuss"] for z in ph), NULL))
    verwendung = dict(
        investition=sum(z["investition"] for z in ph),
        erhaltung=sum(z["erhaltung"] for z in ph),
        einbehaltene_betraege=sum(z["einbehalt"] + z["zuschuss_einbehalt"] for z in ph),
        finanzierungskosten=sum(z["zins"] + z["beitrag"] + z["kkzins"] - z["habenzins"] for z in ph),
        laufende_zahlungen=sum(z["kosten"] - z["miete"] + z["steuer"] + z["tilgung"] for z in ph),
        guthaben_am_ende=ph[-1]["guthaben"] - ph[-1]["kk"])
    bef += pruefe_mittel(herkunft, verwendung)
    # P-12 Bankdarlehen: nie negativ, hoechstens jede der drei Grenzen, Eigenkapital mindestens das Mindesteigenkapital
    gr = bm.bank
    if not (NULL <= L <= max(NULL, min(gr["a"], gr["b"], gr["c"]))) or gr["eigenkapital"] < bm.ek_min:
        bef.append(("P-12", None, L))
    if ein.stau_betrag:
        bef += pruefe_stau(EINS if stau_zahlung else NULL, EINS if stau_offen else NULL)
    if bm.zuschuss:
        anteil = D(verbleibend) / D(bindung_perioden) if bindung_perioden else NULL
        bef += pruefe_zuschuss(sum(zus), rueck, bm.zuschuss - rd.geld(bm.zuschuss * anteil))
    bef += pruefe_abschreibung(basis + (stau_aktiv or NULL), afa, buchwert, boden)
    erg.befunde = bef
    erg.eigenkapital_investitionsphase = herkunft["eigenkapital"]
    erg.nachschuss_spaeter = sum(plan.einlagen_netto[invest_ende + 1:])
    erg.herkunft, erg.verwendung = herkunft, verwendung
    if mit_blatt:
        _blatt(erg, pe, rd)
    return erg


def _blatt(erg, pe, rd):
    """R-11.12: Groessen des verkuerzten Kennzahlenblatts ueber Endwert und Rendite hinaus."""
    ein, plan, bm, p = erg.ein, erg.plan, erg.bemessung, erg.plan.e.raster.p
    N = plan.e.raster.N
    z = plan.zeilen
    vj = range(erg.bauzeit + 1, erg.bauzeit + p + 1)
    erg.dscr_vj, erg.reinertrag_vj, erg.kd_vj = schuldendienstdeckung(plan, perioden=vj)
    erg.beleihungsauslauf = (erg.darlehen + bm.uebrige) / bm.wertansatz if bm.wertansatz > 0 else None
    sollmiete_vj = sum(rd.geld(ein.wohnflaeche * erg.miete_je_qm[1] * 12 / p) for _ in vj)
    erg.sollmiete_vj = sollmiete_vj
    gesamt = bm.preis + bm.enk + bm.baukosten
    basis_preis = gesamt if ein.art == "neubau" else bm.preis
    erg.einstiegsfaktor = basis_preis / sollmiete_vj if sollmiete_vj else None
    erg.bruttoanfangsrendite = sollmiete_vj / basis_preis if basis_preis else None
    erg.nettoanfangsrendite = erg.reinertrag_vj / gesamt if gesamt else None
    erg.ausstiegsfaktor = ein.verkaufsfaktor * (EINS - (erg.vg.stress.verkaufsfaktor_rel if erg.stress else NULL))
    # Restwertanteil (R-10.16): Verkauf nach Abloesung, Vorfaelligkeit, Rueckzahlung und Steuer auf den Gewinn
    steuer_gewinn = NULL
    if z[N]["g_v"] != 0:
        ohne = replace(pe, verkauf=replace(pe.verkauf, buchwert=pe.verkauf.erloes - pe.verkauf.foerder_rueckzahlung),
                       tranchen=_kopie(pe.tranchen))
        steuer_gewinn = z[N]["steuer"] - rechne_plan(ohne).zeilen[N]["steuer"]
    erg.steuer_verkaufsgewinn = steuer_gewinn
    beitrag = z[N]["verkauf"] - z[N]["abloesung"] - z[N]["vfe"] - z[N]["foerder_rueck"] - steuer_gewinn
    erg.restwertbeitrag = beitrag
    erg.restwertanteil = beitrag / plan.endwert if plan.endwert > 0 else None


def _kopie(tranchen):
    neu = []
    for t in tranchen:
        neu.append(Tranche(t.name, t.betrag, t.art, t.zins, tilgungssatz=t.tilgungssatz, laufzeit=t.laufzeit,
                           auszahlung=dict(t.auszahlung), einbehalt=t.einbehalt, tilgungsbeginn=t.tilgungsbeginn,
                           bindung=t.bindung, anschluss_zins=t.anschluss_zins, anschluss_regel=t.anschluss_regel,
                           anschluss_tilgung=t.anschluss_tilgung, beitrag_satz=t.beitrag_satz,
                           tilgungszuschuss=dict(t.tilgungszuschuss), rundung=t.rundung_art, bank=t.bank,
                           vfe_pflichtig=t.vfe_pflichtig))
    return neu


# ------------------------------------------------------------------------------------------------
def zielwertsuche(f, unten, oben, schritt, raster=40):
    """R-11.10: sucht alle Stellen im Bereich [unten; oben], an denen f das Vorzeichen wechselt.

    Gesucht wird auf dem Gitter der Aufloesung 'schritt' (ganzzahlige Bisektion, deterministisch).
    f(x) >= 0 heisst "Ziel erreicht". Rueckgabe: dict(status, loesungen, rand), wobei jede Loesung der
    letzte Gitterwert auf der Seite ist, auf der das Ziel erreicht ist, mit der Richtung des Wechsels.
    """
    unten, oben, schritt = d(unten), d(oben), d(schritt)
    n = int((oben - unten) / schritt)
    if n < 1:
        raise Meldung("M-31", "Suchbereich leer")
    punkte = sorted({round(i * n / raster) for i in range(raster + 1)})
    wert = lambda i: unten + schritt * i
    cache = {}

    def g(i):
        if i not in cache:
            cache[i] = f(wert(i))
        return cache[i]

    loesungen = []
    for a, b in zip(punkte, punkte[1:]):
        fa, fb = g(a), g(b)
        if (fa >= 0) != (fb >= 0):
            lo, hi = a, b
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if (g(mid) >= 0) == (fa >= 0):
                    lo = mid
                else:
                    hi = mid
            innen = lo if fa >= 0 else hi
            loesungen.append(dict(wert=wert(innen), richtung="fallend" if fa >= 0 else "steigend",
                                  f_innen=g(innen), f_aussen=g(hi if fa >= 0 else lo)))
    if not loesungen:
        status = "keine Loesung: Ziel im ganzen Bereich erreicht" if g(punkte[0]) >= 0 else \
            "keine Loesung: Ziel im ganzen Bereich verfehlt"
    else:
        status = "eine Loesung" if len(loesungen) == 1 else f"{len(loesungen)} Loesungen"
    return dict(status=status, loesungen=loesungen, bereich=(unten, oben), schritt=schritt,
                rasterweite=(oben - unten) / raster, auswertungen=len(cache))


def _rendite_minus_ziel(ein, vg, preis, stress, p):
    try:
        erg = rechne_grob(ein, vg, preis=preis, stress=stress, p=p, mit_blatt=False)
    except Meldung as m:
        if m.kennung != "M-22":
            raise
        return D(1)                      # unterhalb des zulaessigen Bereichs: als "erreicht" gewertet
    r = erg.kennzahlen["rendite"]
    return D(1) if r is None else r - vg.zielrendite


def tragbarer_preis(ein: Grobeingabe, vg: Vorgaben, stress=False, p=12):
    """R-11.4 bis R-11.7: hoechster tragbarer Kauf- oder Grundstueckspreis in vollen Euro.

    Renditegrenze: groesster Preis, bei dem die VOFI-Rendite nach Steuern die Zielrendite erreicht,
    gerechnet mit dem Bankdarlehen nach R-5.12. Zweite, freiwillige Grenze: verfuegbares Eigenkapital.
    """
    basis = rechne_grob(ein, vg, stress=False, p=p, mit_blatt=True)
    oben = (vg.suchobergrenze_faktor * basis.sollmiete_vj).quantize(D(1))
    suche = zielwertsuche(lambda x: _rendite_minus_ziel(ein, vg, x, stress, p), 1, oben, 1, vg.suchraster)
    fallend = [l for l in suche["loesungen"] if l["richtung"] == "fallend"]
    erg = dict(suche=suche, renditegrenze=None, ek_grenze=None, preis=None, bindend=None, meldung=None)
    if not fallend:
        erg["meldung"] = "M-32" if "verfehlt" in suche["status"] else "M-33"
        return erg
    erg["renditegrenze"] = fallend[0]["wert"]
    if len(suche["loesungen"]) > 1:
        erg["meldung"] = "M-34"          # mehrere Loesungen; ausgewiesen wird der kleinste Preis mit Wechsel nach unten
    preis, bindend = erg["renditegrenze"], "Rendite"
    if ein.verfuegbares_ek is not None:
        def ek_frei(x):
            try:
                e = rechne_grob(ein, vg, preis=x, stress=stress, p=p, mit_blatt=False)
            except Meldung:
                return D(1)
            return ein.verfuegbares_ek - e.eigenkapital_investitionsphase
        s2 = zielwertsuche(ek_frei, 1, oben, 1, vg.suchraster)
        f2 = [l for l in s2["loesungen"] if l["richtung"] == "fallend"]
        if f2:
            erg["ek_grenze"] = f2[0]["wert"]
            if erg["ek_grenze"] < preis:
                preis, bindend = erg["ek_grenze"], "Eigenkapital"
        elif "verfehlt" in s2["status"]:
            erg["ek_grenze"], preis, bindend = NULL, NULL, "Eigenkapital"
    erg["preis"], erg["bindend"] = preis, bindend
    if preis > 0:
        erg["ergebnis"] = rechne_grob(ein, vg, preis=preis, stress=stress, p=p)
    return erg


def suche_eingabe(ein, vg, feld, unten, oben, schritt, zielgroesse="rendite", stress=False, p=12, raster=None):
    """R-11.9/R-11.10: Zielwertsuche auf eine dafuer gekennzeichnete Eingabe.

    zielgroesse "rendite": VOFI-Rendite erreicht die Zielrendite; "endwertdifferenz": Endwertdifferenz >= 0.
    """
    if feld not in SUCHBARE_EINGABEN:
        raise Meldung("M-30", f"Eingabe '{feld}' ist fuer die Zielwertsuche nicht zugelassen")

    def f(x):
        erg = rechne_grob(replace(ein, **{feld: x}), vg, stress=stress, p=p, mit_blatt=False)
        if zielgroesse == "endwertdifferenz":
            return erg.kennzahlen["endwertdifferenz"]
        r = erg.kennzahlen["rendite"]
        return D(-1) if r is None else r - vg.zielrendite

    return zielwertsuche(f, unten, oben, schritt, raster or vg.suchraster)


# R-11.9: gekennzeichnete Eingaben. Nicht zugelassen sind Auswahlfelder (Steuerstatus), ganzzahlige
# Zeitgroessen (Haltedauer, Zinsbindung, Bauzeit) und die Vorgaben des Hauses.
SUCHBARE_EINGABEN = ("kaufpreis", "grundstueckspreis", "markt_miete", "ist_miete", "stau_betrag", "verkaufsfaktor",
                     "zins", "kostenkennwert")


def haltedauer_tabelle(ein, vg, von, bis, p=12):
    """R-11.13: statt einer Zielwertsuche auf die Haltedauer eine Tabelle je Jahr."""
    zeilen = []
    for n in range(von, bis + 1):
        try:
            e = rechne_grob(replace(ein, haltedauer=n), vg, p=p, mit_blatt=False)
            zeilen.append((n, e.plan.endwert, e.kennzahlen["endwertdifferenz"], e.kennzahlen["rendite"]))
        except Meldung as m:
            zeilen.append((n, None, None, m.kennung))
    return zeilen


def vergleiche(a: Grobergebnis, b: Grobergebnis):
    """R-11.11: Vergleich zweier Fassungen: Kennzahl, Wert A, Wert B, Differenz B - A."""
    zeilen = []
    for name, fa, fb in (
            ("Endwert", a.plan.endwert, b.plan.endwert),
            ("Endwertdifferenz", a.kennzahlen["endwertdifferenz"], b.kennzahlen["endwertdifferenz"]),
            ("VOFI-Rendite", a.kennzahlen["rendite"], b.kennzahlen["rendite"]),
            ("Eigenkapital der Investitionsphase", a.eigenkapital_investitionsphase, b.eigenkapital_investitionsphase),
            ("Bankdarlehen", a.darlehen, b.darlehen),
            ("Schuldendienstdeckung im ersten Jahr der Vollvermietung", a.dscr_vj, b.dscr_vj)):
        zeilen.append((name, fa, fb, None if (fa is None or fb is None) else fb - fa))
    return zeilen
