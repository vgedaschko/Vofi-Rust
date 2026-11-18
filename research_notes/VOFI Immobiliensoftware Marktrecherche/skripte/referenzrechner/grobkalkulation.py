"""Kapitel 3 und 11 der Fachspezifikation: Eingaben der Grobkalkulation 1a, Eingabepruefung, Bemessung, Aufbau des
Finanzplans, Sperre bei verletzter Probe, Blatt, hoechster tragbarer Preis, Stressfall, Zielwertsuche, Vergleich.

Der Rechenkern erhaelt einen vollstaendig aufgeloesten Auftrag (R-3.1) aus drei getrennten Quellen: Eingaben des
Anwenders (Grobeingabe, E-..), Vorgaben des Hauses (Vorgaben, H-..) und Katalogwerte (Katalog, KAT-..; die
Steuerwerte in Steuerparameter). In diesem Modul steht kein Satz, keine Schwelle und keine Frist als Festwert.
"""
from dataclasses import dataclass, field, replace, fields
from decimal import Decimal as D
from typing import Optional
from zahlen import NULL, EINS, d, Rundung, ab_cent
from zeit import Raster
from darlehen import Tranche, bankdarlehen, kapitaldienst_kalkulatorisch
from steuer import (Steuerparameter, MIT_KENNZEICHEN, BETRIEBSVERMOEGEN, PERSONENGESELLSCHAFT, PRIVAT, BEFREIT)
from finanzplan import PlanEingabe, Verkauf, rechne_plan, rechne_alternative
from kennzahlen import (werte_aus, schuldendienstdeckung, kapitaldienst, zinsdeckung, kapitaldienstreserve,
                        deckungsgrenzen, investitionsbarwert, gesamtkapitalrendite, sollzinsen_nach_steuern,
                        renditemeldungen)
from proben import pruefe_plan, pruefe_mittel, pruefe_stau, pruefe_zuschuss, pruefe_index
import ertrag
import restwert

KERNVERSION = "referenzrechner-0.2"         # R-3.1: Version des Kerns, mit jedem Ergebnis zurueckgegeben
REGELSTAND = "Fachspezifikation Teil 1, Stand nach Pruefrunde 1"
MONATE = 12                                 # Monate je Jahr
STOERUNG = [None]                           # nur fuer den Referenzfall mit absichtlich verletzter Probe (RF-16)


# ------------------------------------------------------------------------------------------------ Auftrag
@dataclass
class Stress:
    """H-06: Hoehen des kombinierten Stressfalls. Null heisst: die Groesse wird nicht gestresst."""
    anschlusszins_pp: D = NULL          # Aufschlag auf den Anschlusszins jeder Tranche mit Marktanschluss
    zusage_pp: D = NULL                 # Zinsanstieg bis zur Kreditzusage: Aufschlag auf den Zins des Bankdarlehens
    leerstand_pp: D = NULL              # Aufschlag auf die Leerstandsquote
    verkaufsfaktor_rel: D = NULL        # Abschlag auf den Verkaufsfaktor, relativ
    mietsteigerung_pp: D = NULL         # Abschlag auf die Mietsteigerung
    instandhaltung_rel: D = NULL        # Aufschlag auf die Instandhaltungskosten, relativ
    stau_rel: D = NULL                  # Mehrkosten des Investitionsstaus, relativ (Ankauf)
    baukosten_rel: D = NULL             # Aufschlag auf die Baukosten, relativ (Neubau)
    bauzeit_monate: int = 0             # Verlaengerung der Bauzeit (Neubau)


@dataclass
class Vorgaben:
    """Vorgaben des Hauses (H-..). In den Referenzfaellen Annahmen (annahmen.py). Voreinstellungen haben nur die
    Schalter der Modellannahmen (vorsichtige Lesart) und Groessen, die leer sein duerfen."""
    zielrendite: D                      # H-01
    beleihungsquote: D                  # H-02
    mindestdeckung: D                   # H-03
    mindesttilgung: D                   # H-04
    anschluss_aufschlag: D              # H-05
    stress: Stress                      # H-06
    anschluss_regel: str                # H-07
    h_kurz: D                           # H-08
    kk_zins: D                          # H-10
    kk_linie: Optional[D]               # H-11: Betrag oder None = unbegrenzt
    mietsteigerung: D                   # H-12
    kostensteigerung: D                 # H-13
    baupreissteigerung: D               # H-14
    leerstand: D                        # H-15: struktureller Leerstand
    verkaufskostensatz: D               # H-16
    verwaltung_je_einheit: D            # H-17
    instandhaltung_staffel: list        # H-17: Liste (Gebaeudealter ab, Euro je m2 und Jahr), Voreinstellung IIBV-28
    betriebskosten_je_qm: D             # H-17
    vfe_satz: D                         # H-18
    such_obergrenze_faktor: D           # H-21: Obergrenze der Preissuche als Vielfaches der Jahresmiete
    suchraster: int                     # H-21: Zahl der Rasterschritte
    nachsuchfenster: int                # H-21: Fenster der Nachsuche in Gitterschritten (R-11.5)
    such_miete_max: D                   # H-21: Obergrenze der Mietsuchen in Euro je m2
    izf_unten: D                        # H-21: Suchbereich des internen Zinsfusses
    izf_oben: D
    izf_raster: int
    kalk_zins: Optional[D]              # H-25: fester kalkulatorischer Zins; None = Anschlusszins der Tranche
    fluktuation: D                      # H-26
    forderungsausfall: D                # H-27
    anlaufleerstand: int                # H-28: Monate bis zur Vermietung leerer Flaechen und bei Erstvermietung
    co2_preis: D                        # H-29: Euro je Tonne im Planjahr 1
    co2_steigerung: D                   # H-29
    zuschlag_kg_uebrige: D              # H-30: Kostengruppen 200, 500, 600 als Anteil der Kostengruppen 300 und 400
    zuschlag_kg700: D                   # H-30
    kosten_je_stellplatz: D             # H-30
    bereit_satz: D                      # H-31: Bereitstellungszins je Monat
    bereit_frei: int                    # H-31: bereitstellungsfreie Monate
    a_lang: Optional[D] = None          # H-09: None = gleich H-08
    warnschwelle_restwertanteil: Optional[D] = None     # H-20
    # Schalter der Modellannahmen; Voreinstellung ist die vorsichtige Lesart
    ma026_foerder_nachrang: bool = False    # Foerderdarlehen belegt den Beleihungsraum der Bank nicht
    ma026_vertragszins: bool = False        # Kapitaldienstrechnung mit Vertragskonditionen statt kalkulatorisch
    ma026_ertrag_vorhaben: bool = False     # Ertrag und Bewirtschaftung des Vorhabens statt nachhaltig
    ma031_zuschuss: str = "sofort"          # "sofort", "verteilt" oder "minderung"
    ma032_entgelte_sofort: bool = False     # einbehaltene Entgelte im Betriebsvermoegen im Jahr der Zahlung
    ma037_vorsicht: bool = True             # Kappungsspielraum bei unbekannter Mietenhistorie ausgeschoepft


@dataclass
class KfwKonditionen:
    """KAT-15: KfW-Neubaudarlehen (KFW-297-298-MERKBLATT, KFW-296-MERKBLATT)."""
    hoechstbetrag_je_einheit: D
    zins: D
    tilgungssatz: D
    tilgungsfrei_jahre: int
    zinsbindung_jahre: int


@dataclass
class Katalog:
    """Aufgeloeste Katalogwerte des Auftrags (KAT-..), nach Land, Gemeinde und Objekt."""
    afa_satz: D                         # KAT-07 (ESTG-7)
    wartefrist: int                     # KAT-08 (BGB-558): Monate zwischen zwei Erhoehungen
    kappung: D                          # KAT-08: Kappungsgrenze der Gemeinde
    kappung_monate: int                 # KAT-08: Kappungszeitraum
    mietpreisbremse: bool               # KAT-08 (BGB-556D): gilt in der Gemeinde
    bremse_aufschlag: D                 # KAT-08: zulaessiger Aufschlag auf die Vergleichsmiete
    co2_vermieteranteil: D              # KAT-09 (CO2KOSTAUFG-ANLAGE): Anteil nach der Stufe des Ausstosses
    co2_kosten_5a_je_qm: D              # KAT-09 (CO2KOSTAUFG-5A): weitere Vermieterkosten je m2 und Jahr
    geb_steigerung: D                   # KAT-11: zulaessige Steigerung uebernommener Bindungen je Schritt
    geb_fest_jahre: int                 # KAT-11
    geb_schritt_jahre: int              # KAT-11
    ahk_quote: D                        # KAT-12 (ESTG-6): Schwelle anschaffungsnaher Herstellungskosten
    ahk_jahre: int                      # KAT-12: Zeitraum in Jahren
    ust_satz: D                         # KAT-12 (USTG-12): Umsatzsteuersatz zum Herausrechnen
    kuendigung_sperre: int              # KAT-13 (BGB-489): Monate ab vollstaendigem Empfang
    kuendigung_frist: int               # KAT-13: Kuendigungsfrist in Monaten
    bewirtschaftung_mindest: D          # KAT-14 (BELWERTV-11): Mindestansatz als Anteil des Rohertrags
    kfw: Optional[KfwKonditionen] = None    # KAT-15


@dataclass
class Foerderung:
    """Grobfoerderung (KAT-10; NBANK-RL-MIETWOHNRAUM-2026; MA-002, MA-003, MA-004, MA-005, MA-017, MA-021)."""
    darlehensquote: D
    zuschussquote: D
    eigenmittelquote: D
    bemessungsgrenze_je_qm: D
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
    """Eingaben des Anwenders (E-..). None oder null heisst: nicht angegeben."""
    art: str                            # E-01
    land: str                           # E-03
    gemeinde: str                       # E-04 (amtlicher Gemeindeschluessel)
    stichtag_jahr: int                  # E-02
    stichtag_monat: int                 # E-02
    steuer: Steuerparameter             # E-40 bis E-44 mit den Steuerwerten des Katalogs
    zins: D                             # E-45
    zinsbindung_jahre: int              # E-46
    verkaufsfaktor: D                   # E-47
    haltedauer: int                     # E-48
    wohnflaeche: D                      # E-13
    einheiten: int                      # E-14
    enk_satz: D                         # E-11
    markt_miete: D = NULL               # E-16: Neuvermietungsmiete; beim Neubau die Miete bei Bezug
    tilgungssatz: Optional[D] = None    # E-64; None = H-04
    # Ankauf
    kaufpreis: D = NULL                 # E-10
    angebotspreis: Optional[D] = None   # E-18
    bodenanteil: Optional[D] = None     # E-12; None = Voreinstellung aus Bodenrichtwert und Grundstuecksflaeche
    ist_miete: D = NULL                 # E-15 in Euro je m2 der vermieteten Flaeche
    vergleichsmiete: D = NULL           # E-19
    baujahr: Optional[int] = None       # E-17
    leere_flaeche: D = NULL             # E-31
    sonstige_ertraege: D = NULL         # E-32: Stellplaetze und anderes, Euro je Jahr
    mietenhistorie: Optional[tuple] = None  # E-33: (Monate seit der letzten Erhoehung, Miete drei Jahre zuvor)
    anpassungsdauer: int = 0            # E-53
    stau_betrag: D = NULL               # E-50
    stau_jahr: int = 0                  # E-51
    stau_art: str = "erhaltung"         # E-52
    co2_ausstoss: D = NULL              # E-34 in kg je m2 und Jahr, oder Naeherung aus E-54 und E-55
    co2_aus_naeherung: bool = False     # True: aus Effizienzklasse und Energietraeger abgeleitet (MA-035)
    gebunden_anteil: D = NULL           # E-56
    bindung_jahre: int = 0              # E-57: Jahre ab dem Stichtag bis zum Bindungsende
    gebundene_miete: Optional[D] = None     # E-58
    uebernommen: Optional[dict] = None  # E-59: restschuld, nennbetrag, zins, tilgungssatz, bindung_jahre,
                                        #       anschluss_zins, beitrag_satz, foerderdarlehen, rang
    # Neubau
    grundstueckspreis: D = NULL         # E-20
    grundstuecksflaeche: D = NULL       # E-21
    bodenrichtwert: D = NULL            # E-30
    bgf: D = NULL                       # E-22
    kostenkennwert: D = NULL            # E-25: Kostengruppen 300 und 400
    bauzeit_monate: int = 0             # E-26
    stellplaetze: int = 0               # E-27
    stellplatz_miete: D = NULL          # E-27: Euro je Stellplatz und Monat
    kfw_betrag: D = NULL                # E-35
    foerderung: Optional[Foerderung] = None     # E-28, E-29 aufgeloest (KAT-10)
    # freiwillig oder im Einzelfall
    verfuegbares_ek: Optional[D] = None     # E-60
    wertansatz_bank: Optional[D] = None     # E-61
    wertansatz_begruendung: str = ""
    erbbauzins: D = NULL                # E-62
    erbbauzins_steigerung: D = NULL     # E-63
    abweichungen: Optional[dict] = None     # R-3.2: {Vorgabe: (Wert, Begruendung)}


class Meldung(Exception):
    """Definiertes Ergebnis statt Fehler (Kapitel 14): Kennung und Klartext."""

    def __init__(self, kennung, text, angaben=None):
        super().__init__(f"{kennung}: {text}")
        self.kennung, self.text, self.angaben = kennung, text, angaben or {}


@dataclass
class Bemessung:
    """Groessen, die vor dem Finanzplan feststehen (R-11.2)."""
    preis: D
    enk: D
    baukosten_stichtag: D
    baukosten: D
    mittelbedarf: D
    wertansatz: D
    uebrige: D
    im_beleihungsraum: D
    zuschuss: D
    zuschuss_gebaeude: D
    foerderdarlehen: D
    kfw: D
    ek_min: D
    einbehalt_darlehen: D
    einbehalt_zuschuss: D
    reinertrag_vj: D
    ertrag_nachhaltig: D
    kd_uebrige: D
    kd_je_darlehen: dict
    zins_kalk: D
    tilgung_kalk: D
    bank: dict
    boden: D
    bodenanteil: D


class Grobergebnis:
    pass


# ------------------------------------------------------------------------------------------------ R-3.2, R-3.7
# Richtung "strenger" je Vorgabe (R-3.4): +1 = ein hoeherer Wert ist strenger, -1 = ein niedrigerer.
RICHTUNG = {
    "zielrendite": ("H-01", 1), "beleihungsquote": ("H-02", -1), "mindestdeckung": ("H-03", 1),
    "mindesttilgung": ("H-04", 1), "anschluss_aufschlag": ("H-05", 1), "h_kurz": ("H-08", -1),
    "a_lang": ("H-09", 1), "kk_zins": ("H-10", 1), "kk_linie": ("H-11", -1), "mietsteigerung": ("H-12", -1),
    "kostensteigerung": ("H-13", 1), "baupreissteigerung": ("H-14", 1), "leerstand": ("H-15", 1),
    "verkaufskostensatz": ("H-16", 1), "verwaltung_je_einheit": ("H-17", 1), "betriebskosten_je_qm": ("H-17", 1),
    "vfe_satz": ("H-18", 1), "kalk_zins": ("H-25", 1), "fluktuation": ("H-26", -1), "forderungsausfall": ("H-27", 1),
    "anlaufleerstand": ("H-28", 1), "co2_preis": ("H-29", 1), "co2_steigerung": ("H-29", 1),
    "zuschlag_kg_uebrige": ("H-30", 1), "zuschlag_kg700": ("H-30", 1), "kosten_je_stellplatz": ("H-30", 1),
    "bereit_satz": ("H-31", 1), "bereit_frei": ("H-31", -1),
}
ANSCHLUSSREGELN = ("rate", "tilgungssatz", "restlaufzeit")     # H-07; strenger ist nur "restlaufzeit" (R-3.4)


def vorgaben_im_vorhaben(vg: Vorgaben, abweichungen):
    """R-3.2: wendet die Abweichungen des Vorhabens an. Strengere Werte sind frei; eine Lockerung braucht eine
    Begruendung, sonst M-20. Rueckgabe: (wirksame Vorgaben, Abweichungsliste fuer das Blatt)."""
    liste, neu = [], {}
    for feld, (wert, grund) in (abweichungen or {}).items():
        if feld == "anschluss_regel":
            kennung, haus = "H-07", vg.anschluss_regel
            strenger = wert == "restlaufzeit"
        elif feld in RICHTUNG:
            kennung, vz = RICHTUNG[feld]
            haus = getattr(vg, feld)
            if haus is None or wert is None:    # H-11: None = unbegrenzt ist die lockerste Linie
                strenger = wert is not None
            else:
                strenger = (wert - haus) * vz >= 0
        else:
            raise Meldung("M-20", f"Vorgabe '{feld}' ist im Vorhaben nicht aenderbar")
        if wert == haus:
            continue
        if not strenger and not grund:
            raise Meldung("M-20", f"{kennung} {feld}: Lockerung von {haus} auf {wert} ohne Begruendung")
        liste.append(dict(kennung=kennung, vorgabe=feld, haus=haus, vorhaben=wert,
                          art="strenger" if strenger else "gelockert", begruendung=grund or ""))
        neu[feld] = wert
    return (replace(vg, **neu) if neu else vg), liste


def _bereich(kennung, name, wert, unten=None, oben=None, offen_unten=False):
    if wert is None:
        raise Meldung("M-20", f"{kennung} {name}: Angabe fehlt")
    if (unten is not None and (wert < unten or (offen_unten and wert == unten))) or (oben is not None and wert > oben):
        grenze = f"{'>' if offen_unten else '>='} {unten}" if oben is None else f"{unten} bis {oben}"
        raise Meldung("M-20", f"{kennung} {name}: Wert {wert} ausserhalb des zulaessigen Bereichs ({grenze})")


def pruefe_eingaben(ein: Grobeingabe, vg: Vorgaben, kat: Katalog, p):
    """R-3.7: Eingabepruefung gegen die zulaessigen Bereiche aus R-3.3 und R-3.4. Verletzung: Meldung M-20
    (M-23 fuer die Haltedauer des Neubaus) mit Kennung und Namen der Eingabe; keine Rechnung."""
    b = _bereich
    if ein.art not in ("ankauf", "neubau"):
        raise Meldung("M-20", f"E-01 Vorhabensart: '{ein.art}' ist nicht zulaessig")
    neubau = ein.art == "neubau"
    if not ein.land or not ein.gemeinde:
        raise Meldung("M-20", "E-03, E-04 Land und Gemeinde: Angabe fehlt")
    b("E-02", "Stichtag, Monat", ein.stichtag_monat, 1, MONATE)
    b("E-13", "Wohnflaeche", ein.wohnflaeche, NULL, None, True)
    b("E-14", "Zahl der Einheiten", ein.einheiten, 1)
    b("E-11", "Erwerbsnebenkosten", ein.enk_satz, NULL, vg_grenze("enk_max"))
    b("E-45", "Zins des Bankdarlehens", ein.zins, NULL, vg_grenze("zins_max"))
    b("E-46", "Zinsbindung", ein.zinsbindung_jahre, 1, vg_grenze("bindung_max"))
    b("E-47", "Verkaufsfaktor", ein.verkaufsfaktor, NULL, None, True)
    b("E-48", "Haltedauer", ein.haltedauer, 1, vg_grenze("haltedauer_max"))
    if ein.tilgungssatz is not None:
        b("E-64", "Tilgungssatz des Bankdarlehens", ein.tilgungssatz, vg.mindesttilgung)
    b("E-62", "Erbbauzins", ein.erbbauzins, NULL)
    b("E-63", "Steigerung des Erbbauzinses", ein.erbbauzins_steigerung, vg_grenze("steigerung_min"), vg_grenze("steigerung_max"))
    if ein.verfuegbares_ek is not None:
        b("E-60", "verfuegbares Eigenkapital", ein.verfuegbares_ek, NULL)
    st = ein.steuer
    if st.erweiterte_kuerzung and st.status not in MIT_KENNZEICHEN:
        raise Meldung("M-20", "E-41 Kennzeichen erweiterte Grundstueckskuerzung: bei diesem Steuerstatus nicht zulaessig")
    b("E-42", "Steuersatz des Investors", st.est_satz, NULL, vg_grenze("steuersatz_max"))
    b("E-43", "Anteil natuerlicher Personen", st.anteil_natuerliche, NULL, EINS)
    if neubau:
        if p != MONATE:
            raise Meldung("M-20", "E-01: Der Neubau wird nur im Monatsraster gerechnet")
        b("E-20", "Grundstueckspreis", ein.grundstueckspreis, NULL, None, True)
        b("E-21", "Grundstuecksflaeche", ein.grundstuecksflaeche, NULL, None, True)
        b("E-22", "Brutto-Grundflaeche", ein.bgf, NULL, None, True)
        b("E-25", "Kostenkennwert", ein.kostenkennwert, NULL, None, True)
        b("E-26", "Bauzeit", ein.bauzeit_monate, 1, vg_grenze("bauzeit_max"))
        b("E-16", "Miete bei Bezug", ein.markt_miete, NULL, None, True)
        b("E-27", "Stellplaetze", ein.stellplaetze, 0)
        b("E-27", "Miete je Stellplatz", ein.stellplatz_miete, NULL)
        b("E-35", "KfW-Darlehen", ein.kfw_betrag, NULL)
        if ein.kfw_betrag > 0:
            if kat.kfw is None:
                raise Meldung("M-20", "E-35 KfW-Darlehen: Konditionen fehlen im Katalog (KAT-15)")
            b("E-35", "KfW-Darlehen", ein.kfw_betrag, NULL, ein.einheiten * kat.kfw.hoechstbetrag_je_einheit)
        if ein.foerderung is not None:
            b("E-30", "Bodenrichtwert", ein.bodenrichtwert, NULL, None, True)
        # R-14.4: die Haltedauer reicht bis zum Ende des ersten Jahres der Vollvermietung, auch im Stressfall
        if ein.haltedauer * p < ein.bauzeit_monate + vg.stress.bauzeit_monate + vg.anlaufleerstand + MONATE:
            raise Meldung("M-23", "E-48 Haltedauer endet vor dem Ende des ersten Jahres der Vollvermietung "
                                  "(Bauzeit einschliesslich der Verlaengerung im Stressfall und Anlaufleerstand)")
    else:
        b("E-10", "Kaufpreis", ein.kaufpreis, NULL, None, True)
        b("E-17", "Baujahr", ein.baujahr, None, ein.stichtag_jahr)
        b("E-31", "leerstehende Flaeche", ein.leere_flaeche, NULL, ein.wohnflaeche)
        vermietet = ein.wohnflaeche - ein.leere_flaeche
        if vermietet > 0:
            if ein.ist_miete <= 0:
                raise Meldung("M-20", "E-15 Ist-Miete: null oder negativ bei vermieteter Flaeche; leerstehende "
                                      "Flaeche ist als E-31 einzugeben")
            b("E-19", "ortsuebliche Vergleichsmiete", ein.vergleichsmiete, NULL, None, True)
        if ein.leere_flaeche > 0 or vg.fluktuation > 0:
            b("E-16", "Neuvermietungsmiete", ein.markt_miete, NULL, None, True)
            b("E-19", "ortsuebliche Vergleichsmiete", ein.vergleichsmiete, NULL, None, True)
        if ein.bodenanteil is None:
            if not (ein.bodenrichtwert > 0 and ein.grundstuecksflaeche > 0):
                raise Meldung("M-20", "E-12 Bodenanteil: Angabe fehlt (oder Bodenrichtwert E-30 und Grundstuecksflaeche E-21)")
        else:
            b("E-12", "Bodenanteil", ein.bodenanteil, NULL, EINS)
        b("E-32", "sonstige Ertraege", ein.sonstige_ertraege, NULL)
        b("E-50", "Investitionsstau", ein.stau_betrag, NULL)
        b("E-51", "Jahr der Ausfuehrung", ein.stau_jahr, 0)
        b("E-53", "Anpassungsdauer", ein.anpassungsdauer, 0, vg_grenze("anpassung_max"))
        b("E-34", "CO2-Ausstoss", ein.co2_ausstoss, NULL)
        b("E-56", "gebundener Flaechenanteil", ein.gebunden_anteil, NULL, EINS)
        if ein.gebunden_anteil > 0:
            b("E-57", "Bindungsende", ein.bindung_jahre, 1)
        if ein.mietenhistorie is not None:
            b("E-33", "Monate seit der letzten Mieterhoehung", ein.mietenhistorie[0], 0)
            b("E-33", "Miete drei Jahre vor dem Stichtag", ein.mietenhistorie[1], NULL, ein.ist_miete, True)
        ue = ein.uebernommen
        if ue:
            b("E-59", "uebernommenes Darlehen, Restschuld", d(ue["restschuld"]), NULL, None, True)
            b("E-59", "uebernommenes Darlehen, urspruenglicher Nennbetrag", d(ue.get("nennbetrag", ue["restschuld"])), d(ue["restschuld"]))
            b("E-59", "uebernommenes Darlehen, Zins", d(ue["zins"]), NULL, vg_grenze("zins_max"))
            b("E-59", "uebernommenes Darlehen, Tilgungssatz", d(ue["tilgungssatz"]), NULL)
            if ue.get("rang", "vor") not in ("vor", "nach"):
                raise Meldung("M-20", "E-59 uebernommenes Darlehen, Rang: 'vor' oder 'nach' der Bank")
    if ein.wertansatz_bank is not None:
        b("E-61", "Wertansatz der Bank", ein.wertansatz_bank, NULL, None, True)
    # Vorgaben des Hauses (R-3.4)
    b("H-01", "Zielrendite", vg.zielrendite, -EINS, None, True)
    b("H-02", "Beleihungsquote", vg.beleihungsquote, NULL, EINS)
    b("H-03", "Mindestdeckung", vg.mindestdeckung, EINS)
    b("H-04", "Mindesttilgung", vg.mindesttilgung, NULL)
    b("H-05", "Anschlussaufschlag", vg.anschluss_aufschlag, NULL)
    b("H-08", "kurzfristiger Habenzins", vg.h_kurz, NULL)
    b("H-10", "Kontokorrentzins", vg.kk_zins, vg.h_kurz)
    for kennung, name, wert in (("H-12", "Mietsteigerung", vg.mietsteigerung), ("H-13", "Kostensteigerung", vg.kostensteigerung),
                                ("H-14", "Baupreissteigerung", vg.baupreissteigerung)):
        b(kennung, name, wert, vg_grenze("steigerung_min"), vg_grenze("steigerung_max"))
    b("H-15, H-27", "Leerstand und Forderungsausfall", vg.leerstand + vg.forderungsausfall, NULL, EINS)
    b("H-16", "Verkaufskosten", vg.verkaufskostensatz, NULL, vg_grenze("enk_max"))
    b("H-26", "Fluktuation", vg.fluktuation, NULL, EINS)
    b("H-28", "Anlaufleerstand", vg.anlaufleerstand, 0)
    if vg.anschluss_regel not in ANSCHLUSSREGELN:
        raise Meldung("M-20", f"H-07 Regel fuer die Rate nach der Zinsbindung: '{vg.anschluss_regel}' ist nicht zulaessig")
    if vg.ma031_zuschuss not in ("sofort", "verteilt", "minderung"):
        raise Meldung("M-20", "MA-031: Lesart des Zuschusses unbekannt")


# Grenzen der zulaessigen Bereiche (R-3.3, Spalte "zulaessig"): Teil des Auftrags, von annahmen.py gesetzt
GRENZEN = {}


def vg_grenze(name):
    if name not in GRENZEN:
        raise Meldung("M-20", f"Grenze '{name}' der Eingabepruefung fehlt im Auftrag")
    return GRENZEN[name]


# ------------------------------------------------------------------------------------------------ Kapitel 6
class Ertragsreihen:
    """Mieteinzahlungen, laufende Kosten, Sollmieten und Indexreihen eines Laufs (Kapitel 6)."""


def _ertragsreihen(ein, vg, kat, raster, rd, stress, bauzeit):
    p, N = raster.p, raster.N
    st = vg.stress if stress else Stress()
    M = raster.n * MONATE + MONATE                       # Monate der Mietreihe: Haltedauer und ein Folgejahr
    jahre = raster.n + 2
    steig = vg.mietsteigerung - st.mietsteigerung_pp
    leer = min(EINS, vg.leerstand + st.leerstand_pp)     # im Stressfall hoechstens 100 %
    ausfall = min(EINS, leer + vg.forderungsausfall)
    neubau = ein.art == "neubau"
    r = Ertragsreihen()
    r.erste = (bauzeit + vg.anlaufleerstand + 1) if neubau else 1    # erster Vermietungsmonat
    r.bezug = bauzeit + 1
    if neubau:
        pools, vm = ertrag.mieten_neubau(M, ein, kat, r.erste, r.bezug, steig, ein.anpassungsdauer, rd, ein.foerderung)
        sonst_jahr = ein.stellplaetze * ein.stellplatz_miete * MONATE
    else:
        pools, vm = ertrag.mieten_ankauf(M, ein, kat, vg.fluktuation, vg.anlaufleerstand, steig, ein.anpassungsdauer,
                                         rd, vg.ma037_vorsicht)
        sonst_jahr = ein.sonstige_ertraege
    soll_roh, nachh_roh, flaeche = ertrag.monatswerte(pools, vm, M)
    idx_m = ertrag.indexreihe(jahre, steig, rd)
    idx_k = ertrag.indexreihe(jahre, vg.kostensteigerung, rd)
    idx_co2 = ertrag.indexreihe(jahre, vg.co2_steigerung, rd)
    idx_erb = ertrag.indexreihe(jahre, ein.erbbauzins_steigerung, rd)
    r.indexreihen = {"Mieten": (idx_m, steig), "Kosten": (idx_k, vg.kostensteigerung),
                     "CO2-Preis": (idx_co2, vg.co2_steigerung), "Erbbauzins": (idx_erb, ein.erbbauzins_steigerung)}
    r.pools, r.vm, r.flaeche, r.leer, r.ausfall = pools, vm, flaeche, leer, ausfall
    r.miete_je_qm = [None] + [soll_roh[m] / ein.wohnflaeche for m in range(1, M + 1)]

    def sonstige(m):                                     # R-6.15: sonstige Ertraege mit dem Mietindex, ab der Vermietung
        if m < r.erste:
            return NULL
        j = ertrag.jahr_von(m - r.erste + 1) if neubau else ertrag.jahr_von(m)
        return sonst_jahr * idx_m[j] / MONATE

    def monate(u):                                       # Monate der Periode u
        return range((u - 1) * MONATE // p + 1, u * MONATE // p + 1)

    r.soll_monat = lambda m: rd.geld(soll_roh[m] + sonstige(m))                 # R-6.4, je Monat
    r.soll = lambda u: rd.geld(sum(soll_roh[m] + sonstige(m) for m in monate(u)))
    r.nachhaltig = lambda u: rd.geld(sum(nachh_roh[m] + sonstige(m) for m in monate(u)))
    r.einzahlung = lambda u: rd.geld(r.soll(u) * (EINS - ausfall))
    alter0 = None if neubau else raster.startjahr - ein.baujahr
    inst_rel = EINS + st.instandhaltung_rel

    def bewirtschaftung(u):                              # R-6.8, R-6.9 ohne Erbbauzins
        if u * MONATE // p < r.bezug:
            return NULL
        j = raster.planjahr(u)
        # Gebaeudealter im Planjahr: Ankauf Kalenderjahr - Baujahr, Neubau Jahre seit dem Bezug
        alter = (alter0 + j - 1) if not neubau else (u * MONATE // p - r.bezug) // MONATE
        inst = ertrag.instandhaltung_je_qm(vg.instandhaltung_staffel, alter) * inst_rel
        jahr = (vg.verwaltung_je_einheit * ein.einheiten + inst * ein.wohnflaeche
                + vg.betriebskosten_je_qm * ein.wohnflaeche + kat.co2_kosten_5a_je_qm * ein.wohnflaeche) * idx_k[j]
        co2 = ein.co2_ausstoss * ein.wohnflaeche * kat.co2_vermieteranteil * vg.co2_preis * idx_co2[j] / 1000
        return rd.geld(jahr / p) + rd.geld(co2 / p)

    r.erbbau = lambda u: rd.geld(ein.erbbauzins * idx_erb[raster.planjahr(u)] / p) if u >= 1 else NULL
    r.erbbau_monat = lambda m: rd.geld(ein.erbbauzins * idx_erb[min(ertrag.jahr_von(m), jahre)] / MONATE)
    r.bewirtschaftung = bewirtschaftung
    r.kosten = lambda u: bewirtschaftung(u) + r.erbbau(u)

    def jahresmiete(m):                                  # R-8.1: massgebliche Jahresmiete zum Stand des Monats m
        return MONATE * r.soll_monat(m) * (EINS - leer) - MONATE * r.erbbau_monat(m)

    r.jahresmiete = jahresmiete
    return r


def _baukosten(ein, vg, rd, bauzeit, aufschlag=NULL):
    """R-11.2: Baukosten zum Preisstand des Stichtags und Monatsraten, mit der Baupreissteigerung fortgeschrieben."""
    stichtag = (rd.geld(ein.bgf * ein.kostenkennwert * (EINS + vg.zuschlag_kg_uebrige + vg.zuschlag_kg700))
                + rd.geld(ein.stellplaetze * vg.kosten_je_stellplatz))
    stichtag = rd.geld(stichtag * (EINS + aufschlag))
    raten = {m: rd.geld(stichtag / bauzeit * rd.satz((EINS + vg.baupreissteigerung) ** (D(m) / MONATE)))
             for m in range(1, bauzeit + 1)}
    return stichtag, raten


def _tranche_uebernommen(ein, vg, kat, p, stress_pp=NULL):
    ue = ein.uebernommen
    bindung = ue.get("bindung_jahre")
    anschluss = ue.get("anschluss_zins")
    if anschluss is None:                                # Voreinstellung: Anschlusszins des Bankdarlehens (R-5.8)
        anschluss = ein.zins + vg.anschluss_aufschlag
    foerder = bool(ue.get("foerderdarlehen", False))
    ende = None if bindung is None else bindung * p
    # BGB-489: der Beginn der Zinsbindung ist nicht bekannt; vorsichtig zaehlt die Frist ab dem Stichtag
    kuendbar = (kat.kuendigung_sperre + kat.kuendigung_frist) * p // MONATE
    return Tranche("Uebernommenes Darlehen", ue["restschuld"], "annuitaet_prozent", ue["zins"],
                   tilgungssatz=ue["tilgungssatz"], rate_betrag=ue.get("nennbetrag", ue["restschuld"]),
                   bindung=ende, anschluss_zins=d(anschluss) + stress_pp, anschluss_regel=vg.anschluss_regel,
                   anschluss_tilgung=max(d(ue["tilgungssatz"]), vg.mindesttilgung),
                   beitrag_satz=ue.get("beitrag_satz", 0), bank=False, foerder=foerder,
                   vfe_bis=None if ende is None else min(ende, kuendbar))


def _tranche_foerder(f, betrag, auszahlung, einbehalt, tilgungsbeginn, p):
    # MA-002: gleichbleibende Raten ueber die Tilgungsdauer ab dem Monat nach der Bauzeit; zinslos, danach MA-003
    return Tranche("Foerderdarlehen", betrag, "raten", 0, laufzeit=f.tilgung_jahre * p, auszahlung=auszahlung,
                   einbehalt=einbehalt, tilgungsbeginn=tilgungsbeginn,
                   bindung=f.zinslos_jahre * p + tilgungsbeginn - 1, anschluss_zins=f.zins_danach,
                   beitrag_satz=f.vkb_satz, bank=False, foerder=True)


def _kd_zwoelf(tr, p, rd, ab):
    """Vertraglicher Kapitaldienst der zwoelf Monate ab der Periode 'ab'."""
    tr.periode(0, p, rd)
    kd = NULL
    for u in range(1, ab + p):
        t = tr.periode(u, p, rd)
        if u >= ab:
            kd += t["zins"] + t["tilgung"] + t["beitrag"]
    return kd


def bemesse(ein, vg, kat, raster, rd, preis=None, miete_ansatz=None):
    """R-11.2: Mittelbedarf, uebrige Darlehen, Zuschuesse und Bankdarlehen nach R-5.12 aus den Basisannahmen.
    miete_ansatz: einheitliche Miete je m2 anstelle der nachhaltigen Miete (nur fuer R-11.15)."""
    p = raster.p
    neubau = ein.art == "neubau"
    P = d(preis) if preis is not None else (ein.grundstueckspreis if neubau else ein.kaufpreis)
    enk = rd.geld(P * ein.enk_satz)
    bauzeit = ein.bauzeit_monate if neubau else 0
    bk0, raten = _baukosten(ein, vg, rd, bauzeit) if neubau else (NULL, {})
    baukosten = sum(raten.values(), NULL)
    stau0 = rd.geld(ein.stau_betrag) if (ein.stau_betrag and ein.stau_jahr == 0) else NULL
    er = _ertragsreihen(ein, vg, kat, raster, rd, False, bauzeit)
    ab = (er.erste - 1) * p // MONATE + 1
    vj = range(ab, ab + p)                               # erstes Jahr der Vollvermietung
    reinertrag_vj = sum(er.einzahlung(u) - er.kosten(u) for u in vj)
    # ---- nachhaltiger Reinertrag der Bank (R-5.12 b, MA-026)
    if vg.ma026_ertrag_vorhaben:
        ertrag_n = reinertrag_vj
    else:
        if miete_ansatz is None:
            roh = [er.nachhaltig(u) for u in vj]
        else:
            roh = [rd.geld(ein.wohnflaeche * miete_ansatz * MONATE / p) for u in vj]
        einz = sum(rd.geld(x * (EINS - er.ausfall)) for x in roh)
        roh = sum(roh)
        bew = sum(er.bewirtschaftung(u) for u in vj)
        abzug = max(bew + (roh - einz), rd.geld(kat.bewirtschaftung_mindest * roh))
        ertrag_n = roh - abzug - sum(er.erbbau(u) for u in vj)
    # ---- kalkulatorische Konditionen (R-5.12 b)
    tilg = ein.tilgungssatz if ein.tilgungssatz is not None else vg.mindesttilgung
    anschluss_bank = ein.zins + vg.anschluss_aufschlag
    def kalk(zins, anschluss):
        if vg.ma026_vertragszins:
            return zins
        return max(zins, vg.kalk_zins if vg.kalk_zins is not None else anschluss)
    zins_kalk, tilg_kalk = kalk(ein.zins, anschluss_bank), max(tilg, vg.mindesttilgung)
    uebrige = im_raum = zuschuss = zuschuss_geb = fd = ek_min = e_d = e_z = kfw = NULL
    kd = {}
    bindung_bank = ein.zinsbindung_jahre * p
    if ein.uebernommen and not neubau:
        ue = ein.uebernommen
        schuld = d(ue["restschuld"])
        uebrige += schuld
        if ue.get("rang", "vor") == "vor":               # Rang aus dem Grundbuch (Eingabe), Voreinstellung "vor"
            im_raum += schuld
        tr = _tranche_uebernommen(ein, vg, kat, p)
        vertrag = _kd_zwoelf(tr, p, rd, 1)
        fest = tr.foerder and (tr.bindung is None or tr.bindung >= bindung_bank)
        if vg.ma026_vertragszins or fest:
            kd[tr.name] = vertrag
        else:
            i_k = kalk(tr.zins, tr.anschluss_zins)
            t_k = max(tr.tilgungssatz, vg.mindesttilgung)
            beitrag = p * rd.geld(schuld * tr.beitrag_satz / p)
            kd[tr.name] = max(vertrag, kapitaldienst_kalkulatorisch(schuld, i_k, t_k, p, rd) + beitrag)
    if neubau and ein.kfw_betrag > 0:
        k = kat.kfw
        kfw = ein.kfw_betrag
        uebrige += kfw
        im_raum += kfw                                   # Festlegung: das durchgeleitete KfW-Darlehen belegt den Raum
        i_k = kalk(k.zins, anschluss_bank)
        kd["KfW-Darlehen"] = kapitaldienst_kalkulatorisch(kfw, i_k, max(k.tilgungssatz, vg.mindesttilgung), p, rd)
    zk_bau = zk = NULL
    if ein.foerderung:
        f = ein.foerderung
        # zuwendungsfaehige Kosten: Herstellung bis zur Bemessungsgrenze, Grundstueck bis zum Bodenrichtwert
        zk_bau = min(baukosten, f.bemessungsgrenze_je_qm * ein.wohnflaeche)
        zk = zk_bau + min(P + enk, ein.bodenrichtwert * ein.grundstuecksflaeche)
        fd, zuschuss, ek_min = rd.geld(f.darlehensquote * zk), rd.geld(f.zuschussquote * zk), rd.geld(f.eigenmittelquote * zk)
        e_d, e_z = rd.geld(fd * f.entgelt_darlehen), rd.geld(zuschuss * f.entgelt_zuschuss)
        zuschuss_geb = rd.geld(zuschuss * zk_bau / zk) if zk > 0 else NULL     # R-7.3: Anteil des Gebaeudes
        if zuschuss_geb > zk_bau or zuschuss - zuschuss_geb > zk - zk_bau:
            raise Meldung("M-43", "Der Zuschuss uebersteigt die Kosten, auf die er entfaellt")
        uebrige += fd
        if not vg.ma026_foerder_nachrang:                # MA-026: Foerderdarlehen belegt den Beleihungsraum
            im_raum += fd
        tr = _tranche_foerder(f, fd, {0: fd}, NULL, 1, p)
        kd[tr.name] = _kd_zwoelf(tr, p, rd, 1)           # feste Konditionen: vertraglicher Kapitaldienst
    kd_ue = sum(kd.values(), NULL)
    mittelbedarf = P + enk + baukosten + stau0 + e_d + e_z
    gesamtkosten = P + enk + baukosten                   # R-1.1: Gesamtkosten ohne Finanzierungskosten
    wert = ein.wertansatz_bank if ein.wertansatz_bank is not None else (gesamtkosten if neubau else P)
    bank = bankdarlehen(wert, vg.beleihungsquote, ertrag_n, vg.mindestdeckung, zins_kalk, tilg_kalk, mittelbedarf,
                        uebrige_darlehen=uebrige, uebrige_im_beleihungsraum=im_raum, kd_uebrige=kd_ue,
                        zuschuesse=zuschuss, ek_min=ek_min, p=p, rd=rd)
    if bank["c"] < 0:
        raise Meldung("M-22", "Uebrige Darlehen, Zuschuesse und Mindesteigenkapital uebersteigen den Mittelbedarf")
    # ---- Boden und Gebaeude (R-7.3, R-12.3)
    if neubau:
        boden, anteil = P + enk, None
    else:
        anteil = ein.bodenanteil
        if anteil is None:                               # Voreinstellung E-12 aus Bodenrichtwert und Flaeche
            anteil = min(EINS, ein.bodenrichtwert * ein.grundstuecksflaeche / P)
        boden = rd.geld((P + enk) * anteil)
    return Bemessung(P, enk, bk0, baukosten, mittelbedarf, wert, uebrige, im_raum, zuschuss, zuschuss_geb, fd, kfw,
                     ek_min, e_d, e_z, reinertrag_vj, ertrag_n, kd_ue, kd, zins_kalk, tilg_kalk, bank, boden, anteil)


# ------------------------------------------------------------------------------------------------ R-11.1
def rechne_grob(ein: Grobeingabe, vg: Vorgaben, kat: Katalog, preis=None, stress=False, rundung="cent", p=MONATE,
                mit_blatt=True, geprueft=False) -> Grobergebnis:
    """R-11.1: eine Grobkalkulation im Basisfall oder im kombinierten Stressfall.

    Ergebnis mit erg.gesperrt = True und ohne Kennzahlen, wenn eine Probe verletzt ist (R-13.1, M-10).
    Eingabefehler enden als Meldung (M-20, M-22, M-23, M-24, M-43); Hinweise stehen in erg.meldungen.
    """
    rd = Rundung(rundung)
    abweichungen = []
    if not geprueft:
        vg, abweichungen = vorgaben_im_vorhaben(vg, ein.abweichungen)
        pruefe_eingaben(ein, vg, kat, p)
    raster = Raster(p=p, n=ein.haltedauer, startjahr=ein.stichtag_jahr)
    N = raster.N
    neubau = ein.art == "neubau"
    st = vg.stress if stress else Stress()
    meldungen = []

    def melde(kennung, text, **angaben):
        meldungen.append(dict(kennung=kennung, text=text, **angaben))

    bm = bemesse(ein, vg, kat, raster, rd, preis)        # Darlehen stets aus dem Basisfall (R-11.8)
    L = bm.bank["darlehen"]
    wert_ueber = ein.wertansatz_bank is not None and ein.wertansatz_bank > (bm.preis + bm.enk + bm.baukosten if neubau else bm.preis)
    if wert_ueber and not ein.wertansatz_begruendung:
        raise Meldung("M-20", "E-61 Wertansatz der Bank ueber dem Kaufpreis oder den Gesamtkosten ohne Begruendung")
    bauzeit = (ein.bauzeit_monate + st.bauzeit_monate) if neubau else 0
    er = _ertragsreihen(ein, vg, kat, raster, rd, stress, bauzeit)
    null = lambda: [NULL] * (N + 1)
    miete, kost, erh, inv, zus = null(), null(), null(), null(), null()
    zus_einb, afa, einl, pacht = null(), null(), null(), null()
    for u in range(1, N + 1):
        miete[u], kost[u], pacht[u] = er.einzahlung(u), er.kosten(u), er.erbbau(u)
    # ---- Investitionsauszahlungen
    inv[0] = bm.preis + bm.enk
    baukosten = NULL
    if neubau:
        _, raten = _baukosten(ein, vg, rd, bauzeit, st.baukosten_rel)
        for m, rate in raten.items():
            inv[m] = rate
        baukosten = sum(raten.values(), NULL)
    # ---- Investitionsstau (R-6.10) mit der Regel der anschaffungsnahen Herstellungskosten (R-6.16, ESTG-6)
    bpi = ertrag.indexreihe(raster.n + 2, vg.baupreissteigerung, rd)     # bpi[k+1] = Preisstand Ende Jahr k
    stau_zahlung = stau_aktiv = stau_offen = NULL
    stau_jahr = None
    stau_betrag = rd.geld(ein.stau_betrag * (EINS + st.stau_rel))
    gebaeude_ak = bm.preis + bm.enk - bm.boden           # Gebaeudeanschaffungskosten vor Zuschuessen (Ankauf)
    if stau_betrag:
        if ein.stau_jahr <= raster.n:
            stau_zahlung = rd.geld(stau_betrag * bpi[ein.stau_jahr + 1])
            stau_jahr = ein.stau_jahr
            aktivieren = ein.stau_art != "erhaltung"
            if (not aktivieren and not neubau and stau_jahr <= kat.ahk_jahre
                    and stau_zahlung / (EINS + kat.ust_satz) > kat.ahk_quote * gebaeude_ak):
                aktivieren = True
                melde("M-36", "Erhaltungsmassnahmen der ersten Jahre uebersteigen die Schwelle der anschaffungsnahen "
                              "Herstellungskosten und werden aktiviert")
            ziel = inv if aktivieren else erh
            ziel[stau_jahr * p] += stau_zahlung
            if aktivieren:
                stau_aktiv = stau_zahlung
        else:
            stau_offen = restwert.stau_abzug(stau_betrag, bpi[raster.n + 1], EINS, rd)
    stau0 = stau_zahlung if stau_jahr == 0 else NULL
    # ---- Mittelabruf: Eigenkapital, Foerdermittel im Verhaeltnis, KfW-Darlehen, Bankdarlehen (R-11.3)
    mittelbedarf = bm.preis + bm.enk + baukosten + stau0 + bm.einbehalt_darlehen + bm.einbehalt_zuschuss
    ek_soll = mittelbedarf - bm.uebrige - bm.zuschuss - L        # Ausgleichsposten; Mehrkosten traegt das Eigenkapital
    aus_bank, aus_fd, aus_kfw = {}, {}, {}
    rest_ek, rest_fd, rest_zs, rest_kfw, rest_bank = ek_soll, bm.foerderdarlehen, bm.zuschuss, bm.kfw, L
    uebern = d(ein.uebernommen["restschuld"]) if (ein.uebernommen and not neubau) else NULL
    foerder_gezogen = False
    for m in range(0, bauzeit + 1):
        bedarf = inv[m] + (erh[0] if m == 0 else NULL) - (uebern if m == 0 else NULL)
        x = min(rest_ek, bedarf)
        if x > 0:
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
        for rest_name, plan_aus in (("kfw", aus_kfw), ("bank", aus_bank)):
            rest = rest_kfw if rest_name == "kfw" else rest_bank
            if bedarf > 0 and rest > 0:
                y = min(rest, bedarf)
                plan_aus[m] = y
                bedarf -= y
                if rest_name == "kfw":
                    rest_kfw -= y
                else:
                    rest_bank -= y
        if bedarf > 0:                                   # darf nicht vorkommen; die Probe P-04 meldet es
            einl[m] += bedarf
    # nicht abgerufene Mittel fliessen mit der letzten Bauperiode (R-11.3)
    if rest_bank > 0:
        aus_bank[bauzeit] = aus_bank.get(bauzeit, NULL) + rest_bank
    if rest_kfw > 0:
        aus_kfw[bauzeit] = aus_kfw.get(bauzeit, NULL) + rest_kfw
    if rest_fd > 0:
        aus_fd[bauzeit] = aus_fd.get(bauzeit, NULL) + rest_fd
    if rest_zs > 0:
        zus[bauzeit] += rest_zs
    if rest_ek > 0:
        einl[bauzeit] += rest_ek
    if STOERUNG[0]:
        STOERUNG[0](locals())
    # ---- Tranchen
    tilg = ein.tilgungssatz if ein.tilgungssatz is not None else vg.mindesttilgung
    kuendbar = kat.kuendigung_sperre + kat.kuendigung_frist      # BGB-489, in Monaten ab vollstaendigem Empfang
    zins_bank = ein.zins + st.zusage_pp
    anschluss_bank = zins_bank + vg.anschluss_aufschlag + st.anschlusszins_pp
    tranchen = []
    if L > 0:
        plan_aus = aus_bank or {0: L}
        bindung = ein.zinsbindung_jahre * p
        tranchen.append(Tranche(
            "Bankdarlehen", L, "annuitaet_prozent", zins_bank, tilgungssatz=tilg, auszahlung=plan_aus,
            tilgungsbeginn=bauzeit + 1, bindung=bindung, anschluss_zins=anschluss_bank,
            anschluss_regel=vg.anschluss_regel, anschluss_tilgung=max(tilg, vg.mindesttilgung), bank=True,
            vfe_bis=min(bindung, (max(plan_aus) + kuendbar) * p // MONATE),
            bereit_satz=vg.bereit_satz if neubau else NULL, bereit_frei=vg.bereit_frei))
    if bm.kfw > 0:
        k = kat.kfw
        bindung = k.zinsbindung_jahre * p
        plan_aus = aus_kfw or {0: bm.kfw}
        tranchen.append(Tranche(
            "KfW-Darlehen", bm.kfw, "annuitaet_prozent", k.zins, tilgungssatz=k.tilgungssatz, auszahlung=plan_aus,
            tilgungsbeginn=bauzeit + k.tilgungsfrei_jahre * p + 1, bindung=bindung, anschluss_zins=anschluss_bank,
            anschluss_regel=vg.anschluss_regel, anschluss_tilgung=max(k.tilgungssatz, vg.mindesttilgung), bank=False,
            vfe_bis=min(bindung, (max(plan_aus) + kuendbar) * p // MONATE)))
    if ein.uebernommen and not neubau:
        tranchen.append(_tranche_uebernommen(ein, vg, kat, p, st.anschlusszins_pp))
    if ein.foerderung and bm.foerderdarlehen > 0:
        tranchen.append(_tranche_foerder(ein.foerderung, bm.foerderdarlehen, aus_fd, bm.einbehalt_darlehen,
                                         bauzeit + 1, p))
    # ---- Abschreibungsplan (R-7.3): linear, Buchung am Ende jedes Planjahres, zeitanteilig ab Nutzungsbeginn
    boden = bm.boden
    basis = baukosten if neubau else gebaeude_ak
    lesart = vg.ma031_zuschuss
    steuer_ertrag = null()
    rueck_im_gewinn = True
    if bm.zuschuss > 0 and lesart == "minderung":        # MA-031: Zuschuss mindert Gebaeude und Boden anteilig
        z_boden = bm.zuschuss - bm.zuschuss_gebaeude
        if bm.zuschuss_gebaeude > basis or z_boden > boden:
            raise Meldung("M-43", "Der Zuschuss uebersteigt die Kosten, auf die er entfaellt")
        basis -= bm.zuschuss_gebaeude
        boden -= z_boden
    rest_basis = basis
    rest_stau = stau_aktiv                               # aktivierte Massnahme: Abschreibung ab dem Folgejahr
    for j in range(1, raster.n + 1):
        ende = j * p
        monate = max(0, ende - max(bauzeit, (j - 1) * p))
        a = min(rest_basis, rd.geld(basis * kat.afa_satz * D(monate) / p))
        rest_basis -= a
        a_stau = NULL
        if stau_aktiv and j > stau_jahr:
            a_stau = min(rest_stau, rd.geld(stau_aktiv * kat.afa_satz))
            rest_stau -= a_stau
        afa[ende] = a + a_stau
    buchwert = boden + rest_basis + rest_stau
    # ---- Verkauf (Kapitel 8)
    faktor = ein.verkaufsfaktor * (EINS - st.verkaufsfaktor_rel)
    jahresmiete_n = er.jahresmiete(raster.n * MONATE)
    preis_vk = restwert.preis_aus_faktor(faktor, max(jahresmiete_n, NULL), rd)
    rueck = NULL
    bindung_perioden = verbleibend = 0
    if ein.foerderung and bm.zuschuss > 0:
        bindung_perioden = ein.foerderung.bindung_jahre * p      # Bindung beginnt mit der Bezugsfertigkeit
        verbleibend = max(0, bauzeit + bindung_perioden - N)
        rueck = restwert.zuschuss_rueckzahlung(bm.zuschuss, bindung_perioden, verbleibend, rd)
        if lesart == "sofort":                           # MA-031: Ertrag im Jahr des Zuflusses
            steuer_ertrag = list(zus)
        elif lesart == "verteilt":                       # MA-031: Ertrag ueber die Bindung, Rest gleicht die Rueckzahlung aus
            rueck_im_gewinn = False
            offen = bm.zuschuss - rueck
            for j in range(1, raster.n + 1):
                monate = max(0, min(j * p, bauzeit + bindung_perioden) - max(bauzeit, (j - 1) * p))
                teil = offen if j == raster.n else min(offen, rd.geld(bm.zuschuss * D(monate) / D(bindung_perioden)))
                steuer_ertrag[j * p] = teil
                offen -= teil
    vk = Verkauf(preis_brutto=preis_vk, kosten=restwert.verkaufskosten(preis_vk, vg.verkaufskostensatz, rd),
                 stau_abzug=stau_offen, foerder_rueckzahlung=rueck, buchwert=buchwert)
    # ---- einbehaltene Entgelte steuerlich (R-7.15): im Betriebsvermoegen ueber die Zinsbindung verteilt
    einbehalten = bm.einbehalt_darlehen + bm.einbehalt_zuschuss
    steuer_einbehalt = None
    steuer = replace(ein.steuer, haltedauer=ein.haltedauer)
    if einbehalten > 0 and steuer.status in BETRIEBSVERMOEGEN and not vg.ma032_entgelte_sofort:
        steuer_einbehalt = null()
        start = min(aus_fd) if aus_fd else 0
        ende_bindung = ein.foerderung.zinslos_jahre * p + bauzeit
        offen = einbehalten
        for j in range(1, raster.n + 1):
            monate = max(0, min(j * p, ende_bindung) - max(start, (j - 1) * p))
            teil = offen if j == raster.n else min(offen, rd.geld(einbehalten * D(monate) / D(ende_bindung - start)))
            steuer_einbehalt[j * p] = teil
            offen -= teil
    pe = PlanEingabe(raster=raster, miete=miete, kosten=kost, erhaltung=erh, investition=inv, afa=afa,
                     tranchen=tranchen, steuer=steuer, einlagen=einl, entnahmen=null(), h_kurz=vg.h_kurz,
                     kk_zins=vg.kk_zins, a_lang=vg.a_lang, kk_linie=vg.kk_linie, zuschuss=zus,
                     zuschuss_einbehalt=zus_einb, verkauf=vk, vfe_satz=vg.vfe_satz, rundung=rd,
                     steuer_einbehalt=steuer_einbehalt, steuer_ertrag=steuer_ertrag,
                     rueckzahlung_im_gewinn=rueck_im_gewinn, pacht=pacht,
                     anschaffung=boden + basis + stau_aktiv, afa_grundlage=basis + stau_aktiv)
    plan = rechne_plan(pe)
    alt = rechne_alternative(pe, plan.einlagen_netto, plan.entnahmen_netto)
    erg = Grobergebnis()
    erg.ein, erg.vg, erg.kat, erg.stress, erg.bemessung, erg.plan, erg.alt = ein, vg, kat, stress, bm, plan, alt
    erg.darlehen, erg.preis, erg.verkauf, erg.bauzeit, erg.ertrag = L, bm.preis, vk, bauzeit, er
    erg.miete_je_qm = er.miete_je_qm
    erg.baukosten, erg.mittelbedarf, erg.ek_soll = baukosten, mittelbedarf, ek_soll
    erg.abweichungen = abweichungen
    erg.auftrag = dict(kernversion=KERNVERSION, regelstand=REGELSTAND, rundung=rundung, raster=p)
    # ---- Proben (Kapitel 13)
    bef = pruefe_plan(plan, alt)
    invest_ende = bauzeit * p // MONATE
    ph = plan.zeilen[:invest_ende + 1]                    # Investitionsphase: Zeitpunkt 0 bis Ende der Bauzeit
    herkunft = dict(
        eigenkapital=sum(plan.einlagen_netto[:invest_ende + 1]),
        darlehen=sum((z["auszahlung"] for z in ph), NULL),
        zuschuesse=sum((z["zuschuss"] for z in ph), NULL))
    verwendung = dict(
        investition=sum(z["investition"] for z in ph),
        erhaltung=sum(z["erhaltung"] for z in ph),
        einbehaltene_betraege=sum(z["einbehalt"] + z["zuschuss_einbehalt"] for z in ph),
        finanzierungskosten=sum(z["zins"] + z["beitrag"] + z["bereit"] + z["kkzins"] - z["habenzins"] for z in ph),
        bewirtschaftung_abzueglich_miete=sum(z["kosten"] - z["miete"] for z in ph),
        steuer=sum(z["steuer"] for z in ph),
        planmaessige_tilgung=sum(z["tilgung"] for z in ph),
        guthaben_am_ende=ph[-1]["guthaben"] - ph[-1]["kk"])
    bef += pruefe_mittel(sum(pe.einlagen[:invest_ende + 1]), ek_soll, herkunft, verwendung,
                         None if neubau else plan.zeilen[0]["guthaben"] + plan.zeilen[0]["kk"])
    # P-12 Bankdarlehen: nie negativ, hoechstens jede der Grenzen, Eigenkapital mindestens das Mindesteigenkapital
    gr = bm.bank
    grenzen = [gr["a"], gr["c"]] + ([gr["b"]] if gr["b"] is not None else [])
    if not (NULL <= L <= max(NULL, min(grenzen))) or gr["eigenkapital"] < bm.ek_min:
        bef.append(("P-12", None, L))
    if stau_betrag:
        bef += pruefe_stau(EINS if stau_zahlung else NULL, EINS if stau_offen else NULL)
    if bm.zuschuss:
        bef += pruefe_zuschuss(sum(zus), plan.zeilen[N]["foerder_rueck"], bm.zuschuss, bindung_perioden, verbleibend, rd)
    bef += pruefe_index(er.indexreihen, rd)
    erg.befunde = bef
    erg.herkunft, erg.verwendung = herkunft, verwendung
    erg.eigenkapital_investitionsphase = herkunft["eigenkapital"]
    spaeter = plan.reihe("nachschuss")[invest_ende + 1:]
    erg.fehlbetrag_verkauf = plan.zeilen[N]["nachschuss"]            # R-10.17: Verlust beim Verkauf
    erg.nachschuss_laufend = sum(spaeter, NULL) - erg.fehlbetrag_verkauf
    erg.eigenkapitalbedarf = sum(plan.einlagen_netto, NULL)          # R-11.6: Einlagen und alle Nachschuesse
    erg.nachschuss_je_jahr = [None] + [plan.jahressumme("nachschuss", j) for j in range(1, raster.n + 1)]
    erg.gesperrt = bool(bef)
    if bef:                                              # R-13.1: verletzte Probe sperrt das Ergebnis
        erg.kennzahlen = None
        erg.meldungen = [dict(kennung="M-10", text="Kontrollsumme verletzt; das Ergebnis ist gesperrt. Es liegt kein "
                                                    "Eingabefehler vor; der Fehler ist gemeldet.", befunde=bef)]
        return erg
    erg.kennzahlen = kz = werte_aus(plan, alt, vg.zielrendite)
    # ---- Meldungen des Laufs (R-14.13)
    if gr["meldung"]:
        melde("M-21", "Der nachhaltige Reinertrag traegt nach der Mindestdeckung kein Bankdarlehen")
    for tr in tranchen:
        for h in tr.hinweise:
            melde(h, f"{tr.name}: Regel 'Restlaufzeit bleibt' ohne Tilgung nicht anwendbar; gerechnet ist 'Tilgungssatz bleibt'")
    if plan.zeilen[N]["vfe"] > 0:
        melde("M-25", "Zinsbindung reicht ueber die Haltedauer; Vorfaelligkeit angesetzt", betrag=plan.zeilen[N]["vfe"])
    for kennung, text in renditemeldungen(plan.einlagen_netto, plan.entnahmen_netto, kz):
        melde(kennung, text)
    if abweichungen or wert_ueber:
        melde("M-35", "Abweichungen von den Vorgaben des Hauses oder Wertansatz der Bank ueber dem Kaufpreis",
              liste=abweichungen, wertansatz_begruendung=ein.wertansatz_begruendung if wert_ueber else "")
    melde("M-37", "Die Steuer ist vereinfacht gerechnet: ohne Mindestbesteuerung, Zinsschranke, Sonderabschreibung und "
                  "Reinvestitionsruecklage"
                  + ("; das Kennzeichen der erweiterten Kuerzung ist ungeprueft uebernommen" if steuer.erweiterte_kuerzung else "")
                  + ". Sie ersetzt keine steuerliche Pruefung des Einzelfalls.")
    if erg.fehlbetrag_verkauf > 0:
        melde("M-42", "Verlust beim Verkauf: Der Verkaufserloes deckt Abloesung, Steuer und Kosten nicht",
              betrag=erg.fehlbetrag_verkauf)
    if steuer.status == BEFREIT:
        melde("M-44", "Verkauf in befreiter Koerperschaft: Die Befreiung im Verkaufsjahr ist vom Steuerberater zu pruefen (KSTG-5)")
    if "M-45" in plan.steuer.hinweise:
        melde("M-45", "Ein Verlustvortrag ueber dem Sockelbetrag wird in einem Jahr verrechnet; die Mindestbesteuerung ist nicht gerechnet")
    erg.meldungen = meldungen
    erg.modellannahmen = _modellannahmen(erg, tranchen, einbehalten)
    if mit_blatt:
        _blatt(erg, pe, rd)
    return erg


def _modellannahmen(erg, tranchen, einbehalten):
    """R-3.1: Kennungen der Modellannahmen, die in diesem Lauf gewirkt haben."""
    ein, vg, plan, bm = erg.ein, erg.vg, erg.plan, erg.bemessung
    N = plan.e.raster.N
    ma = {"MA-013"} if tranchen else set()
    if bm.uebrige > 0 or erg.darlehen > 0:
        ma.add("MA-026")
    if sum(1 for x in plan.einlagen_netto if x > 0) > 1 or sum(plan.entnahmen_netto) > 0:
        ma.add("MA-012")
    if ein.steuer.verlust == "sofort" or any(t["vv_zugang"] > 0 or t["vv_gew_zugang"] > 0 for t in plan.steuer.protokoll):
        ma.add("MA-016")
    if ein.foerderung:
        ma |= {"MA-002", "MA-003", "MA-004", "MA-005", "MA-017", "MA-021", "MA-031"}
    if ein.steuer.erweiterte_kuerzung and plan.zeilen[N]["g_v"] != 0:
        ma.add("MA-030")
    if einbehalten > 0 or (ein.steuer.status == PRIVAT and plan.zeilen[N]["vfe"] > 0):
        ma.add("MA-032")
    if plan.zeilen[N]["vfe"] > 0:
        ma.add("MA-033")
    if any(tr.bindung is not None and tr.bindung < N and not tr.foerder for tr in tranchen):
        ma.add("MA-034")
    if ein.co2_aus_naeherung:
        ma.add("MA-035")
    if ein.steuer.status in PERSONENGESELLSCHAFT and plan.zeilen[N]["g_v"] != 0:
        ma.add("MA-036")
    if ein.art == "ankauf" and ein.mietenhistorie is None and ein.wohnflaeche > ein.leere_flaeche:
        ma.add("MA-037")
    return sorted(ma)


def _blatt(erg, pe, rd):
    """R-11.12: Groessen des verkuerzten Kennzahlenblatts ueber Endwert und Rendite hinaus."""
    ein, vg, plan, bm, er = erg.ein, erg.vg, erg.plan, erg.bemessung, erg.ertrag
    r = plan.e.raster
    p, N = r.p, r.N
    z = plan.zeilen
    neubau = ein.art == "neubau"
    st = vg.stress if erg.stress else Stress()
    ab = (er.erste - 1) * p // MONATE + 1
    vj = range(ab, ab + p)
    erg.dscr_vj, erg.reinertrag_vj, erg.kd_vj = schuldendienstdeckung(plan, perioden=vj)
    erg.kd_je_darlehen = kapitaldienst(plan, vj, je_tranche=True)
    erg.zinsdeckung_vj = zinsdeckung(plan, vj)
    erg.kapitaldienstreserve = kapitaldienstreserve(erg.reinertrag_vj, erg.kd_vj, vg.mindestdeckung)
    sollmiete_vj = sum(er.soll(u) for u in vj)
    erg.sollmiete_vj = sollmiete_vj
    erg.anteil_miete_deckung_eins, erg.ausfall_deckung_eins = deckungsgrenzen(
        sollmiete_vj, sum(z[u]["miete"] for u in vj), sum(z[u]["kosten"] for u in vj), erg.kd_vj)
    # kleinste Deckung ab dem ersten vollen Planjahr der Vermietung (R-10.14)
    erstes = (ab - 1 + p - 1) // p + 1
    decken = [(schuldendienstdeckung(plan, j)[0], j) for j in range(erstes, r.n + 1)]
    decken = [x for x in decken if x[0] is not None]
    erg.deckung_min, erg.deckung_min_jahr = min(decken) if decken else (None, None)
    erg.deckung_nach_bindung = {}
    for tr in plan.e.tranchen:
        if tr.bindung is not None and tr.bindung < N and not (tr.foerder and tr.name == "Foerderdarlehen"):
            j = r.planjahr(tr.bindung + 1)
            erg.deckung_nach_bindung[tr.name] = (j, schuldendienstdeckung(plan, j)[0])
    if erg.deckung_min is not None and erg.deckung_min < vg.mindestdeckung:
        kennung = "M-39" if erg.deckung_min < 1 else "M-38"
        text = ("Die Schuldendienstdeckung faellt unter 1: Der Reinertrag deckt den Kapitaldienst nicht" if kennung == "M-39"
                else "Die Schuldendienstdeckung faellt unter die Mindestdeckung")
        erg.meldungen.append(dict(kennung=kennung, text=text, jahr=erg.deckung_min_jahr, deckung=erg.deckung_min))
    # Darlehen zu Kaufpreis oder Gesamtkosten (R-10.15) und Restschuld zum Wert am Ende der Zinsbindung
    erg.darlehen_zu_wert = (erg.darlehen + bm.uebrige) / bm.wertansatz if bm.wertansatz > 0 else None
    erg.restschuld_zu_wert = None
    tb = ein.zinsbindung_jahre * p
    if erg.darlehen > 0 and tb < N:
        faktor = ein.verkaufsfaktor * (EINS - st.verkaufsfaktor_rel)
        wert = rd.geld(faktor * max(er.jahresmiete(tb * MONATE // p), NULL))
        erg.restschuld_zu_wert = z[tb]["restschuld"] / wert if wert > 0 else None
    # Anfangsrendite und Faktoren (R-10.13): Einstieg und Ausstieg messen dieselbe Jahresmiete (R-8.1)
    gesamt = bm.preis + bm.enk + erg.baukosten
    basis_preis = gesamt if neubau else bm.preis
    jm = er.jahresmiete(er.erste)
    erg.jahresmiete_einstieg = jm
    erg.einstiegsfaktor = basis_preis / jm if jm > 0 else None
    erg.bruttoanfangsrendite = jm / basis_preis if basis_preis else None
    erg.nettoanfangsrendite = erg.reinertrag_vj / gesamt if gesamt else None
    erg.ausstiegsfaktor = ein.verkaufsfaktor * (EINS - st.verkaufsfaktor_rel)
    erg.preis_je_qm = bm.preis / ein.wohnflaeche
    erg.preis_je_qm_grundstueck = bm.preis / ein.grundstuecksflaeche if (neubau and ein.grundstuecksflaeche > 0) else None
    erg.abstand_angebot = None if ein.angebotspreis is None else bm.preis - ein.angebotspreis
    # Gesamtkapitalrendite (R-10.11): a_0 = abgezinste Investitionsauszahlungen der Investitionsphase
    kz = erg.kennzahlen
    a0 = investitionsbarwert(plan, kz["w"], erg.bauzeit * p // MONATE)
    zs = sollzinsen_nach_steuern(plan)
    erg.a0 = a0
    erg.gesamtkapitalrendite = gesamtkapitalrendite(kz["zaehler"], kz["nenner"], zs, a0, r.n)
    # Restwertanteil (R-10.16): Verkauf nach Abloesung, Vorfaelligkeit, Rueckzahlung und Steuer auf den Gewinn
    steuer_gewinn = NULL
    if z[N]["g_v"] != 0:
        ohne = replace(pe, verkauf=replace(pe.verkauf, buchwert=pe.verkauf.erloes
                                           - (pe.verkauf.foerder_rueckzahlung if pe.rueckzahlung_im_gewinn else NULL)),
                       tranchen=_kopie(pe.tranchen), anschaffung=None)
        steuer_gewinn = z[N]["steuer"] - rechne_plan(ohne).zeilen[N]["steuer"]
    erg.steuer_verkaufsgewinn = steuer_gewinn
    beitrag = z[N]["verkauf"] - z[N]["abloesung"] - z[N]["vfe"] - z[N]["foerder_rueck"] - steuer_gewinn
    erg.restwertbeitrag = beitrag
    erg.restwertanteil = beitrag / plan.endwert if plan.endwert > 0 else None
    # R-11.15: Zusatzangaben, wenn der Ertrag kein Bankdarlehen traegt
    erg.ohne_bankdarlehen = None
    if bm.bank["meldung"] == "M-21":
        satz, c = bm.bank["satz"], max(bm.bank["c"], NULL)
        noetig = vg.mindestdeckung * (bm.kd_uebrige + kapitaldienst_kalkulatorisch(c, bm.zins_kalk, bm.tilgung_kalk, p, rd))
        erg.ohne_bankdarlehen = dict(
            deckung_uebrige=bm.ertrag_nachhaltig / bm.kd_uebrige if bm.kd_uebrige > 0 else None,
            reserve=kapitaldienstreserve(bm.ertrag_nachhaltig, bm.kd_uebrige, vg.mindestdeckung),
            restfinanzierung=c, reinertrag_noetig=noetig,
            miete_noetig=_noetige_miete(erg, c, rd),
            eigenkapital_ueber_mindest=erg.eigenkapital_investitionsphase - bm.ek_min)


def _noetige_miete(erg, c, rd):
    """R-11.15: kleinste einheitliche Miete je m2 (Gitter ein Cent), bei der (b) die Restfinanzierung traegt."""
    ein, vg, kat, r = erg.ein, erg.vg, erg.kat, erg.plan.e.raster
    cent = D("0.01")

    def reicht(i):
        b = bemesse(ein, vg, kat, r, rd, erg.preis, miete_ansatz=cent * i).bank["b"]
        return b is None or b >= c
    lo, hi = 0, int(vg.such_miete_max / cent)
    if not reicht(hi):
        return None
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if reicht(mid):
            hi = mid
        else:
            lo = mid
    return cent * hi


def _kopie(tranchen):
    neu = []
    for t in tranchen:
        neu.append(Tranche(t.name, t.betrag, t.art, t.zins, tilgungssatz=t.tilgungssatz, laufzeit=t.laufzeit,
                           auszahlung=dict(t.auszahlung), einbehalt=t.einbehalt, tilgungsbeginn=t.tilgungsbeginn,
                           bindung=t.bindung, anschluss_zins=t.anschluss_zins, anschluss_regel=t.anschluss_regel,
                           anschluss_tilgung=t.anschluss_tilgung, beitrag_satz=t.beitrag_satz,
                           tilgungszuschuss=dict(t.tilgungszuschuss), rundung=t.rundung_art, bank=t.bank,
                           foerder=t.foerder, rate_betrag=t.rate_betrag, vfe_bis=t.vfe_bis,
                           bereit_satz=t.bereit_satz, bereit_frei=t.bereit_frei))
    return neu


def kalkuliere(ein, vg, kat, **kw):
    """Aufruf, der nie mit einem Fehler endet (Kapitel 14): Rueckgabe dict(status, meldungen, ergebnis).
    status: "ergebnis", "gesperrt" (M-10) oder "eingabe" (Meldung ohne Rechnung)."""
    try:
        erg = rechne_grob(ein, vg, kat, **kw)
    except Meldung as m:
        return dict(status="eingabe", meldungen=[dict(kennung=m.kennung, text=m.text)], ergebnis=None)
    except ValueError as x:
        if str(x).startswith("M-24"):
            return dict(status="eingabe", meldungen=[dict(kennung="M-24", text=str(x))], ergebnis=None)
        raise
    return dict(status="gesperrt" if erg.gesperrt else "ergebnis", meldungen=erg.meldungen, ergebnis=erg)


# ------------------------------------------------------------------------------------------------ R-11.10
def zielwertsuche(f, unten, oben, schritt, raster):
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
            loesungen.append(dict(wert=wert(innen), index=innen, richtung="fallend" if fa >= 0 else "steigend",
                                  f_innen=g(innen), f_aussen=g(hi if fa >= 0 else lo)))
    if not loesungen:
        status = "keine Loesung: Ziel an allen Rasterstellen erreicht" if g(punkte[0]) >= 0 else \
            "keine Loesung: Ziel an allen Rasterstellen verfehlt"
    else:
        status = "eine Loesung" if len(loesungen) == 1 else f"{len(loesungen)} Loesungen"
    return dict(status=status, loesungen=loesungen, bereich=(unten, oben), schritt=schritt,
                rasterweite=(oben - unten) / raster, auswertungen=len(cache), g=g, wert=wert)


def _zielgroesse(erg, zielgroesse):
    """R-11.5, R-11.10: Zielfunktion eines Laufs. "rendite": Endwertueberschuss (R-10.9); er hat dasselbe
    Vorzeichen wie Rendite minus Zielrendite und ist auch ohne Einlage definiert."""
    if erg.gesperrt:
        raise Meldung("M-10", "Kontrollsumme in einem Suchschritt verletzt; die Suche endet ohne Ergebnis",
                      dict(befunde=erg.befunde, preis=erg.preis))
    kz = erg.kennzahlen
    return kz["endwertdifferenz"] if zielgroesse == "endwertdifferenz" else kz["endwertueberschuss"]


def tragbarer_preis(ein: Grobeingabe, vg: Vorgaben, kat: Katalog, stress=False, p=MONATE):
    """R-11.4 bis R-11.7: hoechster tragbarer Kauf- oder Grundstueckspreis in vollen Euro.

    Der tragbare Preis ist der groesste Preis, bis zu dem die Zielrendite fuer jeden kleineren Preis des
    Suchbereichs erreicht ist. Zweite, freiwillige Grenze: das verfuegbare Eigenkapital gegen Einlagen und alle
    Nachschuesse. Eine verletzte Probe in einem Suchschritt beendet die Suche mit M-10 und ohne Preis.
    """
    erg = dict(renditegrenze=None, ek_grenze=None, preis=None, bindend=None, meldung=None, meldungen=[],
               unten=None, oben=None, ergebnis=None)
    try:
        vg, abweichungen = vorgaben_im_vorhaben(vg, ein.abweichungen)
        pruefe_eingaben(ein, vg, kat, p)
        ein = replace(ein, abweichungen=None)
        erg["abweichungen"] = abweichungen
        rd = Rundung("cent")
        raster = Raster(p=p, n=ein.haltedauer, startjahr=ein.stichtag_jahr)
        bauzeit = ein.bauzeit_monate if ein.art == "neubau" else 0
        er = _ertragsreihen(ein, vg, kat, raster, rd, False, bauzeit)
        # Obergrenze: Vielfaches der hoeheren Jahresmiete aus Vermietungsbeginn und Verkaufsstichtag (H-21)
        bezug = max(er.jahresmiete(er.erste), er.jahresmiete(raster.n * MONATE), NULL)
        oben = int((vg.such_obergrenze_faktor * bezug).quantize(D(1)))
        if oben < 1:
            raise Meldung("M-31", "Suchbereich leer: keine Miete im Vorhaben")

        def zulaessig(x):
            try:
                bemesse(ein, vg, kat, raster, rd, x)
                return True
            except Meldung as m:
                if m.kennung != "M-22":
                    raise
                return False
        # kleinster zulaessiger Preis: Unterhalb uebersteigen die uebrigen Mittel den Bedarf (M-22)
        unten = 1
        if not zulaessig(unten):
            if not zulaessig(oben):
                raise Meldung("M-22", "Uebrige Darlehen, Zuschuesse und Mindesteigenkapital uebersteigen den "
                                      "Mittelbedarf bei jedem Preis des Suchbereichs")
            lo, hi = unten, oben
            while hi - lo > 1:
                mid = (lo + hi) // 2
                lo, hi = (lo, mid) if zulaessig(mid) else (mid, hi)
            unten = hi
        erg["unten"], erg["oben"] = unten, oben
        laeufe = {}

        def lauf(x):
            x = int(x)
            if x not in laeufe:
                e = rechne_grob(ein, vg, kat, preis=x, stress=stress, p=p, mit_blatt=False, geprueft=True)
                laeufe[x] = (_zielgroesse(e, "rendite"), e.kennzahlen["nenner"], e.eigenkapitalbedarf)
            return laeufe[x]

        def grenze(f, name):
            """Groesster Preis, bis zu dem f >= 0 fuer jeden kleineren Preis gilt (Raster, Bisektion, Nachsuche)."""
            if f(unten) < 0:
                return None, "verfehlt"
            if oben + 1 - unten < 1:
                return (unten, "eine") if f(unten + 1) < 0 else (None, "erreicht")
            s = zielwertsuche(f, unten, oben + 1, 1, vg.suchraster)
            fallend = [l for l in s["loesungen"] if l["richtung"] == "fallend"]
            if not fallend:
                return None, "erreicht"
            x = int(fallend[0]["wert"])
            mehrfach = len(s["loesungen"]) > 1
            # Nachsuche: jeder Preis im Fenster unter der Grenze muss das Ziel erreichen (R-11.5)
            weiter = True
            while weiter:
                weiter = False
                for y in range(x - 1, max(unten, x - vg.nachsuchfenster) - 1, -1):
                    if f(y) < 0:
                        x, mehrfach, weiter = y - 1, True, True
                        break
            # ... und oberhalb der Grenze darf im Fenster kein Preis das Ziel wieder erreichen (sonst M-34)
            if not mehrfach:
                mehrfach = any(f(y) >= 0 for y in range(x + 2, min(oben + 1, x + vg.nachsuchfenster) + 1))
            if mehrfach:
                erg["meldungen"].append("M-34")
            return x, "eine"

        x, status = grenze(lambda v: lauf(v)[0], "Rendite")
        if x is None:
            erg["meldung"] = "M-32" if status == "verfehlt" else "M-33"
            if status == "verfehlt":                     # R-14.13: Rendite beim kleinsten zulaessigen Preis
                erg["ergebnis_unten"] = rechne_grob(ein, vg, kat, preis=unten, stress=stress, p=p, geprueft=True)
            return erg
        erg["renditegrenze"] = x
        if lauf(x)[1] == 0:                              # R-11.5: ohne eingesetztes Eigenkapital kein tragbarer Preis
            erg["meldung"] = "M-41"
            return erg
        preis, bindend = x, "Rendite"
        if ein.verfuegbares_ek is not None:
            y, status = grenze(lambda v: ein.verfuegbares_ek - lauf(v)[2], "Eigenkapital")
            if status == "verfehlt":
                erg["ek_grenze"], erg["preis"], erg["bindend"], erg["meldung"] = 0, None, "Eigenkapital", "M-46"
                return erg
            if y is not None:
                erg["ek_grenze"] = y
                if y < preis:
                    preis, bindend = y, "Eigenkapital"
        erg["preis"], erg["bindend"] = preis, bindend
        erg["meldung"] = "M-34" if "M-34" in erg["meldungen"] else None
        e = erg["ergebnis"] = rechne_grob(ein, vg, kat, preis=preis, stress=stress, p=p, geprueft=True)
        if e.gesperrt:
            raise Meldung("M-10", "Kontrollsumme beim tragbaren Preis verletzt", dict(befunde=e.befunde))
        # P-14 Preisprobe: Ziel bei P* erreicht und einen Euro darueber verfehlt (fuer die bindende Grenze)
        if bindend == "Rendite":
            erg["p14"] = lauf(preis)[0] >= 0 > lauf(preis + 1)[0]
        else:
            erg["p14"] = ein.verfuegbares_ek - lauf(preis)[2] >= 0 > ein.verfuegbares_ek - lauf(preis + 1)[2]
        if not erg["p14"]:
            raise Meldung("M-10", "Preisprobe P-14 verletzt", dict(preis=preis))
        # R-11.7: Angaben zum tragbaren Preis
        jm = e.jahresmiete_einstieg
        erg["faktor"] = preis / jm if (ein.art == "ankauf" and jm > 0) else None
        erg["preis_je_qm"] = D(preis) / ein.wohnflaeche
        erg["preis_je_qm_grundstueck"] = D(preis) / ein.grundstuecksflaeche if ein.art == "neubau" else None
        erg["abstand_angebot"] = None if ein.angebotspreis is None else D(preis) - ein.angebotspreis
    except Meldung as m:
        erg.update(preis=None, bindend=None, meldung=m.kennung, text=m.text, angaben=m.angaben, ergebnis=None)
    return erg


def suche_eingabe(ein, vg, kat, feld, unten, oben, schritt, zielgroesse="rendite", stress=False, p=MONATE, raster=None):
    """R-11.9/R-11.10: Zielwertsuche auf eine dafuer gekennzeichnete Eingabe.

    zielgroesse "rendite": die VOFI-Rendite erreicht die Zielrendite (gemessen am Endwertueberschuss);
    "endwertdifferenz": Endwertdifferenz >= 0. Gitterwerte, an denen der Lauf mit einer Eingabemeldung endet,
    gelten als verfehlt und werden gezaehlt. Eine verletzte Probe beendet die Suche mit M-10.
    """
    if feld not in SUCHBARE_EINGABEN:
        raise Meldung("M-30", f"Eingabe '{feld}' ist fuer die Zielwertsuche nicht zugelassen")
    unzulaessig = []

    def f(x):
        try:
            erg = rechne_grob(replace(ein, **{feld: x}), vg, kat, stress=stress, p=p, mit_blatt=False)
        except Meldung as m:
            if m.kennung == "M-10":
                raise
            unzulaessig.append((x, m.kennung))
            return -EINS
        return _zielgroesse(erg, zielgroesse)

    s = zielwertsuche(f, unten, oben, schritt, raster or vg.suchraster)
    s["unzulaessig"] = unzulaessig
    return s


# R-11.9: gekennzeichnete Eingaben. Nicht zugelassen sind Auswahlfelder (Steuerstatus), ganzzahlige
# Zeitgroessen (Haltedauer, Zinsbindung, Bauzeit) und die Vorgaben des Hauses.
SUCHBARE_EINGABEN = ("kaufpreis", "grundstueckspreis", "markt_miete", "vergleichsmiete", "ist_miete", "stau_betrag",
                     "verkaufsfaktor", "zins", "kostenkennwert")


def haltedauer_tabelle(ein, vg, kat, von, bis, p=MONATE):
    """R-11.13: statt einer Zielwertsuche auf die Haltedauer eine Tabelle je Jahr."""
    zeilen = []
    for n in range(von, bis + 1):
        try:
            e = rechne_grob(replace(ein, haltedauer=n), vg, kat, p=p, mit_blatt=False)
            if e.gesperrt:
                zeilen.append((n, None, None, "M-10"))
            else:
                zeilen.append((n, e.plan.endwert, e.kennzahlen["endwertdifferenz"], e.kennzahlen["rendite"]))
        except Meldung as m:
            zeilen.append((n, None, None, m.kennung))
    return zeilen


BLATTGROESSEN = (
    ("Endwert", lambda e: e.plan.endwert), ("Endwert der Unterlassensalternative", lambda e: e.alt.endwert),
    ("Endwertdifferenz", lambda e: e.kennzahlen["endwertdifferenz"]), ("VOFI-Rendite", lambda e: e.kennzahlen["rendite"]),
    ("Vergleichsrendite", lambda e: e.kennzahlen["vergleichsrendite"]),
    ("Abstand zur Zielrendite", lambda e: e.kennzahlen["abstand_zielrendite"]),
    ("Endwertueberschuss", lambda e: e.kennzahlen["endwertueberschuss"]), ("Restwertanteil", lambda e: e.restwertanteil),
    ("Einstiegsfaktor", lambda e: e.einstiegsfaktor), ("Ausstiegsfaktor", lambda e: e.ausstiegsfaktor),
    ("Bruttoanfangsrendite", lambda e: e.bruttoanfangsrendite), ("Nettoanfangsrendite", lambda e: e.nettoanfangsrendite),
    ("Darlehen zu Kaufpreis oder Gesamtkosten", lambda e: e.darlehen_zu_wert),
    ("Restschuld zum Wert am Ende der Zinsbindung", lambda e: e.restschuld_zu_wert),
    ("Bankdarlehen", lambda e: e.darlehen),
    ("Schuldendienstdeckung im ersten Jahr der Vollvermietung", lambda e: e.dscr_vj),
    ("kleinste Schuldendienstdeckung", lambda e: e.deckung_min), ("Zinsdeckung im ersten Jahr", lambda e: e.zinsdeckung_vj),
    ("Kapitaldienstreserve", lambda e: e.kapitaldienstreserve),
    ("Eigenkapital der Investitionsphase", lambda e: e.eigenkapital_investitionsphase),
    ("laufender Nachschussbedarf", lambda e: e.nachschuss_laufend), ("Fehlbetrag beim Verkauf", lambda e: e.fehlbetrag_verkauf),
)


def vergleiche(a: Grobergebnis, b: Grobergebnis):
    """R-11.11: Vergleich zweier Fassungen: alle Groessen des Blatts mit Wert A, Wert B und Differenz B - A; dazu
    die abweichenden Werte des Auftrags (Eingaben, Vorgaben, Katalog) und die Versionen des Kerns."""
    if a.gesperrt or b.gesperrt:
        raise Meldung("M-10", "Vergleich nur zwischen Fassungen, die alle Kontrollsummen bestehen")
    zeilen = []
    for name, f in BLATTGROESSEN:
        fa, fb = f(a), f(b)
        zeilen.append((name, fa, fb, None if (fa is None or fb is None) else fb - fa))
    abweichend = []
    for quelle, xa, xb in (("E", a.ein, b.ein), ("H", a.vg, b.vg), ("KAT", a.kat, b.kat), ("E", a.ein.steuer, b.ein.steuer)):
        for f_ in fields(xa):
            va, vb = getattr(xa, f_.name), getattr(xb, f_.name)
            if va != vb and f_.name not in ("steuer", "kst_satz"):
                abweichend.append((quelle, f_.name, va, vb))
    versionen = (a.auftrag["kernversion"], b.auftrag["kernversion"])
    return dict(zeilen=zeilen, abweichende_werte=abweichend, kernversionen=versionen,
                versionsgleich=versionen[0] == versionen[1])


def darstellung(werte, einheit=D(1)):
    """R-12.7: Darstellung einer Spalte in vollen Euro. Die Summe wird aus den ungerundeten Werten gebildet;
    addieren die gerundeten Zeilen nicht zur gerundeten Summe, wird die Rundungsdifferenz ausgewiesen."""
    from zahlen import kaufm
    zeilen = [kaufm(x, str(einheit)) for x in werte]
    summe = kaufm(sum(werte, NULL), str(einheit))
    return dict(zeilen=zeilen, summe=summe, rundungsdifferenz=summe - sum(zeilen, NULL))
