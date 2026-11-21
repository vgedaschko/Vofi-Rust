"""Kapitel 3 und 11 der Fachspezifikation: Eingaben der Grobkalkulation 1a, Eingabepruefung, Bemessung, Aufbau des
Finanzplans, Sperre bei verletzter Probe, Blatt, hoechster tragbarer Preis, Stressfall, Zielwertsuche, Vergleich.

Der Rechenkern erhaelt einen vollstaendig aufgeloesten Auftrag (R-3.1) aus drei getrennten Quellen: Eingaben des
Anwenders (Grobeingabe, E-..), Vorgaben des Hauses (Vorgaben, H-..) und Katalogwerte (Katalog, KAT-..; die
Steuerwerte in Steuerparameter). In diesem Modul steht kein Satz, keine Schwelle und keine Frist als Festwert.
"""
from dataclasses import dataclass, field, replace, fields
from decimal import Decimal as D
from typing import Optional
from zahlen import NULL, EINS, d, Rundung, ab_cent, Meldung, TOLERANZ_OHNE_RUNDUNG, FEHLER
from zeit import Raster
from darlehen import Tranche, bankdarlehen, kapitaldienst_kalkulatorisch, bemessungszins, bemessungskapitaldienst
from steuer import (Steuerparameter, MIT_KENNZEICHEN, BETRIEBSVERMOEGEN, PERSONENGESELLSCHAFT, PRIVAT, BEFREIT,
                    KOERPERSCHAFT, UEBERSCHUSS, PERSONENUNTERNEHMEN, KOERPERSCHAFT_OHNE_GEWST)
from finanzplan import PlanEingabe, Verkauf, rechne_plan, rechne_alternative
from kennzahlen import (werte_aus, schuldendienstdeckung, kapitaldienst, zinsdeckung, kapitaldienstreserve,
                        deckungsgrenzen, investitionsbarwert, gesamtkapitalrendite, sollzinsen_nach_steuern,
                        renditemeldungen)
from proben import (pruefe_plan, pruefe_mittel, pruefe_stau, pruefe_zuschuss, pruefe_index, pruefe_bemessung,
                    pruefe_tranchen)
import ertrag
import restwert

KERNVERSION = "referenzrechner-0.4"         # R-3.1: Version des Kerns, mit jedem Ergebnis zurueckgegeben
REGELSTAND = "Fachspezifikation Teil 1, eingefroren nach der Durchsicht vom 2026-11-21"
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
    stau_rel: D = NULL                  # Mehrkosten des Investitionsstaus, relativ (Ankauf)
    baukosten_rel: D = NULL             # Aufschlag auf die Baukosten, relativ (Neubau)
    bauzeit_monate: int = 0             # Verlaengerung der Bauzeit (Neubau)


@dataclass
class Vorgaben:
    """Vorgaben des Hauses (H-..) in drei Klassen (R-3.2, R-3.4): Vorgabe, im Vorhaben aenderbar (KENNUNG_VORGABE);
    fester Hauswert und Lesart des Hauses, nur im Katalog des Hauses aenderbar (FESTE_HAUSWERTE); fester Katalogwert
    (FESTE_KATALOGWERTE). In den Referenzfaellen Annahmen (annahmen.py). Voreinstellungen haben nur die Lesarten der
    Modellannahmen (vorsichtige Lesart) und Groessen, die leer sein duerfen."""
    zielrendite: D                      # H-01
    beleihungsquote: D                  # H-02
    mindestdeckung: D                   # H-03
    mindesttilgung: D                   # H-04
    anschluss_aufschlag: D              # H-05
    stress: Stress                      # H-06
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
    kalk_zins: Optional[D]              # H-25: fester kalkulatorischer Zins aller Tranchen; None = Anschlusszins der Tranche
    fluktuation: D                      # H-26
    forderungsausfall: D                # H-27: fester Katalogwert
    anlaufleerstand: int                # H-28: Monate bis zur Vermietung leerer Flaechen und bei Erstvermietung
    co2_preis: D                        # H-29: Euro je Tonne im Planjahr 1
    co2_steigerung: D                   # H-29
    zuschlag_kg_uebrige: D              # H-30: Kostengruppen 200, 500, 600 als Anteil der Kostengruppen 300 und 400
    zuschlag_kg700: D                   # H-30
    kosten_je_stellplatz: D             # H-30
    bereit_satz: D                      # H-31: Bereitstellungszins je Monat
    bereit_frei: int                    # H-31: bereitstellungsfreie Monate
    a_lang: Optional[D] = None          # H-09: None = gleich H-08
    warnschwelle_restwertanteil: Optional[D] = None     # H-20: Restwertanteil am Endwert, ab dem M-48 erscheint
    warnschwelle_faktorabstand: Optional[D] = None      # H-20: Ausstiegs- minus Einstiegsfaktor, ab dem M-48 erscheint
    zielrendite_neubau: Optional[D] = None      # H-01 je Vorhabensart; None = zielrendite
    zielrendite_gefoerdert: Optional[D] = None  # H-01 fuer gefoerderte Vorhaben; None = wie die Vorhabensart
    bemessungszeitraum: Optional[int] = None    # H-32 in Jahren; None = Zinsbindung des Bankdarlehens
    bewirtschaftung_mindest: Optional[D] = None     # H-33; None = Katalogwert KAT-14
    anlaufleerstand_neubau: Optional[int] = None    # H-34: Monate bis zur Erstvermietung; None = H-28
    bauabschnitt_rohbau: Optional[D] = None         # H-37: Anteil der Bauzeit bis zur Fertigstellung des Rohbaus
    bauabschnitt_innenputz: Optional[D] = None      # H-37: Anteil der Bauzeit bis zur Fertigstellung des Innenputzes
    vorlauf: Optional[int] = None               # H-35: Voreinstellung des Vorlaufs bis zum Baubeginn (E-23)
    anpassungsdauer: Optional[int] = None       # H-23: Anpassungsdauer der Ist-Miete (fester Katalogwert)
    bodenanteil: Optional[D] = None             # H-39: Bodenanteil im Ankauf, wo der Verkauf steuerpflichtig ist (E-12 sonst)
    # Lesarten des Hauses (R-3.2): im Vorhaben nicht umschaltbar; Voreinstellung ist die vorsichtige Lesart.
    # Die Verlustverrechnung H-38 (MA-016) und die Lesart von MA-036 stehen in den Steuerparametern.
    ma026_ertrag_vorhaben: bool = False     # Lesart 3: Ertrag und Bewirtschaftung des Vorhabens statt nachhaltig
    ma026_fremde_kalkulatorisch: bool = False   # Lesart 4: uebrige Tranchen ueber den ganzen Bemessungszeitraum kalkulatorisch
    ma031_zuschuss: Optional[str] = None    # Betriebsvermoegen: "verteilt" (None, Voreinstellung) oder "sofort" (R-7.19)
    ma038_rueckfuehrung: bool = True        # eine Miete ueber der Vergleichsmiete wird zurueckgefuehrt


@dataclass
class KfwKonditionen:
    """KAT-15: KfW-Neubaudarlehen nach dem Merkblatt (KFW-297-298-MERKBLATT); Zins nach KFW-KONDITIONENANZEIGER."""
    hoechstbetrag_je_einheit: D         # je Wohneinheit ohne Qualitaetssiegel
    hoechstbetrag_qng: D                # je Wohneinheit mit Qualitaetssiegel
    zins: D                             # Voreinstellung der Eingabe E-38
    varianten: list                     # Laufzeitvarianten: (Laufzeit in Jahren, tilgungsfreie Anlaufjahre von, bis)
    zinsbindung_jahre: int
    bereit_satz: D                      # Bereitstellungsprovision je Monat auf den nicht abgerufenen Betrag
    bereit_frei: int                    # provisionsfreie Monate ab der Zusage (Stichtag)
    abruffrist: int                     # Monate ab der Zusage
    abruf_verlaengerung: int            # hoechste Verlaengerung der Abruffrist in Monaten


@dataclass
class Katalog:
    """Aufgeloeste Katalogwerte des Auftrags (KAT-..), nach Land, Gemeinde und Objekt. None heisst: Der Katalog
    fuehrt den Wert fuer dieses Land oder diese Gemeinde nicht (R-3.7: Meldung M-47, keine Rechnung)."""
    afa_satz: Optional[D]               # KAT-07 (ESTG-7)
    wartefrist: Optional[int]           # KAT-08 (BGB-558): Monate zwischen zwei Erhoehungen
    kappung: Optional[D]                # KAT-08: Kappungsgrenze der Gemeinde am Stichtag
    kappung_monate: Optional[int]       # KAT-08: Kappungszeitraum
    mietpreisbremse: Optional[bool]     # KAT-08 (BGB-556D): gilt in der Gemeinde am Stichtag
    bremse_aufschlag: Optional[D]       # KAT-08: zulaessiger Aufschlag auf die Vergleichsmiete
    co2_vermieteranteil: Optional[D]    # KAT-09 (CO2KOSTAUFG-ANLAGE): Anteil nach der Stufe des Ausstosses
    geb_steigerung: Optional[D]         # KAT-11: zulaessige Steigerung uebernommener Bindungen je Schritt
    geb_fest_jahre: Optional[int]       # KAT-11
    geb_schritt_jahre: Optional[int]    # KAT-11
    ahk_quote: Optional[D]              # KAT-12 (ESTG-6): Schwelle anschaffungsnaher Herstellungskosten
    ahk_jahre: Optional[int]            # KAT-12: Zeitraum in Jahren
    ust_satz: Optional[D]               # KAT-12 (USTG-12): Umsatzsteuersatz zum Herausrechnen
    kuendigung_sperre: Optional[int]    # KAT-13 (BGB-489): Monate ab vollstaendigem Empfang
    kuendigung_frist: Optional[int]     # KAT-13: Kuendigungsfrist in Monaten
    bewirtschaftung_mindest: Optional[D]    # KAT-14 (BELWERTV-11): Mindestansatz als Anteil des Rohertrags
    kfw: Optional[KfwKonditionen] = None    # KAT-15
    land: Optional[str] = None          # Land und Gemeinde, fuer die der Katalog aufgeloest ist (R-3.7)
    gemeinde: Optional[str] = None
    enk_satz: Optional[D] = None        # KAT-01: Voreinstellung der Erwerbsnebenkosten (E-11)
    vorauszahlung_jahre: Optional[int] = None   # KAT-19 (ESTG-11): Verteilung nur bei Nutzungsueberlassung ueber dieser Dauer
    kappung_gesetzlich: Optional[D] = None      # KAT-08 (BGB-558): Kappungsgrenze ohne Gebietsverordnung
    kappung_ende_jahr: Optional[int] = None     # KAT-08: letztes Kalenderjahr der Kappungsverordnung; None = keine
    bremse_ende_jahr: Optional[int] = None      # KAT-08 (BGB-556D): letztes Kalenderjahr der Mietpreisbremse


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
    tilgung_jahre: int               # Rueckzahlung spaetestens so viele Jahre nach der Bezugsfertigkeit (Nr. 5.3.5)
    zinslos_jahre: int
    zins_danach: D
    teilraten: tuple                 # Auszahlung in Teilraten: nach Baubeginn, Rohbau, Innenputz, Fertigstellung und Belegung
    bank_mindesttilgung: D           # Mindesttilgung der vorrangigen Bankmittel (Nr. 5.3.6)
    tilgungsfrist_monate: int        # Tilgungsbeginn spaetestens so viele Monate nach dem Monat nach der Foerderentscheidung


@dataclass
class Grobeingabe:
    """Eingaben des Anwenders (E-..). None oder null heisst: nicht angegeben."""
    art: str                            # E-01
    land: str                           # E-03
    gemeinde: str                       # E-04 (amtlicher Gemeindeschluessel)
    stichtag_jahr: int                  # E-02
    stichtag_monat: int                 # E-02
    steuer: Steuerparameter             # E-40 bis E-43, E-69 mit den Steuerwerten des Katalogs, dem Hauswert H-38
                                        # (Verlustverrechnung, MA-016) und der Lesart des Hauses zu MA-036
    zins: D                             # E-45
    zinsbindung_jahre: int              # E-46
    verkaufsfaktor: D                   # E-47
    haltedauer: int                     # E-48
    wohnflaeche: D                      # E-13
    einheiten: int                      # E-14
    enk_satz: D                         # E-11 (Voreinstellung KAT-01)
    markt_miete: D = NULL               # E-16: Neuvermietungsmiete; beim Neubau die Miete bei Bezug
    tilgungssatz: Optional[D] = None    # E-64; None = H-04
    zuschuss_verteilung: bool = False   # E-70: Verteilung des Zuschusses ueber die Bindung beantragt (ESTG-11); nur bei
                                        # Ueberschusseinkuenften und einer Bindung ueber der Mindestdauer des Katalogs
    # Ankauf
    kaufpreis: D = NULL                 # E-10
    angebotspreis: Optional[D] = None   # E-18
    bodenanteil: Optional[D] = None     # E-12, nur bei Privatperson, Verein und Stiftung (sonst Hauswert H-39);
                                        # None = Voreinstellung aus Bodenrichtwert und Grundstuecksflaeche
    ist_miete: D = NULL                 # E-15 in Euro je m2 der vermieteten Flaeche
    vergleichsmiete: D = NULL           # E-19
    baujahr: Optional[int] = None       # E-17
    leere_flaeche: D = NULL             # E-31
    sonstige_ertraege: D = NULL         # E-32: Stellplaetze und anderes, Euro je Jahr
    mietenhistorie: Optional[tuple] = None  # E-33: (Monate seit der letzten Erhoehung, Miete drei Jahre zuvor)
    stau_betrag: D = NULL               # E-50
    stau_jahr: Optional[int] = None     # E-51; Pflicht, wenn E-50 angegeben ist
    co2_ausstoss: D = NULL              # E-34 in kg je m2 und Jahr, freiwillig; null = kein Vermieteranteil gerechnet
    im_kappungsgebiet: Optional[bool] = None    # E-05, nur Ankauf: abgesenkte Kappungsgrenze; None = nach Katalog der Gemeinde
    im_bremsgebiet: Optional[bool] = None       # E-05: Mietpreisbremse; None = nach Katalog der Gemeinde
    gebunden_anteil: D = NULL           # E-56
    bindung_jahre: int = 0              # E-57: Jahre ab dem Stichtag bis zum Bindungsende
    gebundene_miete: Optional[D] = None     # E-58
    uebernommen: Optional[dict] = None  # E-59: restschuld, nennbetrag, zins, tilgungssatz, bindung_jahre,
                                        #       anschluss_zins, beitrag_satz
    # Neubau
    grundstueckspreis: D = NULL         # E-20
    grundstuecksflaeche: D = NULL       # E-21
    bodenrichtwert: D = NULL            # E-30
    bgf: D = NULL                       # E-22
    kostenkennwert: D = NULL            # E-25: Kostengruppen 300 und 400 oder Gesamtkosten der Kostengruppen 200 bis 700
    kennwert_gesamt: bool = False       # E-25: True = der Kennwert umfasst die Kostengruppen 200 bis 700 (keine Zuschlaege)
    bauzeit_monate: int = 0             # E-26
    vorlauf_monate: Optional[int] = None    # E-23: Monate vom Grundstueckskauf bis zum Baubeginn; None = Vorgabe H-35
    festpreis: bool = False             # E-24: Festpreis des Bauvertrags: keine Baupreissteigerung
    vorvermietet: bool = False          # E-39: Vorvermietung: kein Anlaufleerstand
    nachhaltige_miete: Optional[D] = None   # E-65: nachhaltige Miete der Bank im ersten Vermietungsjahr; None = E-16
    stellplaetze: int = 0               # E-27
    stellplatz_miete: D = NULL          # E-27: Euro je Stellplatz und Monat
    kfw_betrag: D = NULL                # E-35
    kfw_laufzeit: Optional[int] = None  # E-36: Laufzeitvariante: Laufzeit in Jahren
    kfw_tilgungsfrei: Optional[int] = None  # E-36: tilgungsfreie Anlaufjahre
    kfw_qng: bool = False               # E-37: mit Qualitaetssiegel (hoeherer Hoechstbetrag je Wohneinheit)
    kfw_zins: Optional[D] = None        # E-38: Zins des KfW-Darlehens; None = Katalogwert KAT-15
    foerderung: Optional[Foerderung] = None     # E-28, E-29 aufgeloest (KAT-10)
    # freiwillig oder im Einzelfall
    verfuegbares_ek: Optional[D] = None     # E-60
    erbbauzins: D = NULL                # E-62; steigt mit der Kostensteigerung H-13
    abweichungen: Optional[dict] = None     # R-3.2: {Vorgabe: (Wert, Begruendung)}
    voreinstellungen: Optional[dict] = None     # R-3.1: {Eingabe: (Wert der Voreinstellung, Herkunft H-.. oder KAT-..)};
                                                # None = die Eingaben sind der Hausstandard (Referenzobjekte)
    begruendungen: Optional[dict] = None        # R-3.2: {Eingabe oder Lesart: Begruendung der Abweichung}


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
    bemessungszins: dict = field(default_factory=dict)      # je uebriger Tranche (R-5.12 b)
    bemessungszeitraum: int = 0                             # in Perioden
    mindestansatz: D = NULL                                 # H-33
    kfw_kond: Optional[dict] = None                         # aufgeloeste Konditionen des KfW-Darlehens


class Grobergebnis:
    pass


# ------------------------------------------------------------------------------------------------ R-3.2, R-3.7
# Drei Klassen der Vorgaben des Hauses (R-3.2, R-3.4), je Feld mit Kennung:
# (a) Vorgabe: im Vorhaben aenderbar, jede Abweichung steht in der Liste "Abweichungen vom Hausstandard"
KENNUNG_VORGABE = {
    "zielrendite": "H-01", "zielrendite_neubau": "H-01", "zielrendite_gefoerdert": "H-01", "beleihungsquote": "H-02",
    "mindestdeckung": "H-03", "mindesttilgung": "H-04", "anschluss_aufschlag": "H-05", "stress": "H-06",
    "mietsteigerung": "H-12", "leerstand": "H-15", "kalk_zins": "H-25", "anlaufleerstand": "H-28",
    "zuschlag_kg_uebrige": "H-30", "zuschlag_kg700": "H-30", "kosten_je_stellplatz": "H-30",
    "anlaufleerstand_neubau": "H-34",
}
# (b) fester Hauswert und Lesart des Hauses: nur im Katalog des Hauses aenderbar, nicht im Vorhaben, kein Feld der Maske
FESTE_HAUSWERTE = {
    "h_kurz": "H-08", "a_lang": "H-09", "kk_linie": "H-11", "kostensteigerung": "H-13", "baupreissteigerung": "H-14",
    "verkaufskostensatz": "H-16", "verwaltung_je_einheit": "H-17", "instandhaltung_staffel": "H-17",
    "betriebskosten_je_qm": "H-17", "vfe_satz": "H-18", "fluktuation": "H-26", "bereit_satz": "H-31",
    "bemessungszeitraum": "H-32", "bewirtschaftung_mindest": "H-33", "bodenanteil": "H-39",
    "ma026_ertrag_vorhaben": "MA-026", "ma026_fremde_kalkulatorisch": "MA-026", "ma031_zuschuss": "MA-031",
    "ma038_rueckfuehrung": "MA-038",
}
HAUSWERTE_STEUER = {"steuer.verlust": ("H-38 (MA-016)", "vortrag"), "steuer.aufgabegewinn": ("MA-036", False)}
# (c) fester Katalogwert: Wert mit Quelle im Katalog, ohne Freigabeentscheidung und ohne Feld
FESTE_KATALOGWERTE = {
    "kk_zins": "H-10", "warnschwelle_restwertanteil": "H-20", "warnschwelle_faktorabstand": "H-20",
    "such_obergrenze_faktor": "H-21", "suchraster": "H-21", "nachsuchfenster": "H-21", "such_miete_max": "H-21",
    "izf_unten": "H-21", "izf_oben": "H-21", "izf_raster": "H-21", "anpassungsdauer": "H-23", "forderungsausfall": "H-27",
    "co2_preis": "H-29", "co2_steigerung": "H-29", "bereit_frei": "H-31", "bauabschnitt_rohbau": "H-37",
    "bauabschnitt_innenputz": "H-37", "vorlauf": "H-35",
}
# Eingaben mit Voreinstellung aus Vorgabe oder Katalog (der Auftrag traegt Wert und Herkunft, R-3.1) ...
KENNUNG_EINGABE = {
    "enk_satz": "E-11", "zinsbindung_jahre": "E-46", "haltedauer": "E-48",
    "tilgungssatz": "E-64", "vorlauf_monate": "E-23", "kfw_zins": "E-38", "nachhaltige_miete": "E-65",
    "im_kappungsgebiet": "E-05", "im_bremsgebiet": "E-05", "steuer.est_satz": "E-42",
    "uebernommen.anschluss_zins": "E-59",
}
# ... und Eingaben mit fester Voreinstellung: {Feld: (Kennung, Voreinstellung)}
FESTE_VOREINSTELLUNG = {
    "festpreis": ("E-24", False), "vorvermietet": ("E-39", False),
    "steuer.kuerzung_bleibt_verkaufsjahr": ("E-69", False), "zuschuss_verteilung": ("E-70", False),
}
ANSCHLUSSREGEL = "tilgungssatz"                                # R-5.9: nach der Zinsbindung bleibt der Tilgungssatz (MA-034)
ANSCHLUSSREGELN = ("rate", "tilgungssatz", "restlaufzeit")     # nur fuer den Ausweis der kleinsten Deckung (R-10.14)


def _hole(ein, feld):
    teil, _, name = feld.rpartition(".")
    if teil == "steuer":
        return getattr(ein.steuer, name)
    if teil == "uebernommen":
        return ein.uebernommen.get(name) if ein.uebernommen else None
    return getattr(ein, feld)


def _setze(ein, feld, wert):
    teil, _, name = feld.rpartition(".")
    if teil == "steuer":
        return replace(ein, steuer=replace(ein.steuer, **{name: wert}))
    if teil == "uebernommen":
        return replace(ein, uebernommen=dict(ein.uebernommen, **{name: wert}))
    return replace(ein, **{feld: wert})


def vorgaben_im_vorhaben(vg: Vorgaben, ein: Grobeingabe):
    """R-3.2: wendet die Abweichungen des Vorhabens von den Vorgaben des Hauses an und stellt die Liste
    "Abweichungen vom Hausstandard" zusammen: jede Abweichung von einer Vorgabe (ein.abweichungen), von einer
    Voreinstellung (ein.voreinstellungen und die festen Voreinstellungen) und jede Lesart einer Modellannahme, die
    nicht die voreingestellte ist. Eine Richtung "strenger" gibt es nicht; die Wirkung wird am Fall gerechnet.
    Rueckgabe: (wirksame Vorgaben, Liste)."""
    liste, neu = [], {}
    grund = ein.begruendungen or {}
    standard = {f_.name: f_.default for f_ in fields(Vorgaben)}
    for feld, (wert, text) in (ein.abweichungen or {}).items():
        if feld not in KENNUNG_VORGABE:
            klasse = ("fester Hauswert oder Lesart des Hauses" if feld in FESTE_HAUSWERTE else "fester Katalogwert")
            kennung = FESTE_HAUSWERTE.get(feld) or FESTE_KATALOGWERTE.get(feld, "")
            raise Meldung("M-20", f"{kennung} Vorgabe '{feld}' ist im Vorhaben nicht aenderbar ({klasse})")
        haus = getattr(vg, feld)
        if wert == haus:
            continue
        kennung = KENNUNG_VORGABE[feld]
        liste.append(dict(kennung=kennung, vorgabe=feld, haus=haus, vorhaben=wert, begruendung=text or "",
                          art="Lesart" if kennung.startswith("MA-") else "Vorgabe", quelle="vg", feld=feld))
        neu[feld] = wert
    for feld, kennung in FESTE_HAUSWERTE.items():     # Lesarten, die das Haus umgeschaltet hat
        if kennung.startswith("MA-") and getattr(vg, feld) != standard[feld]:
            liste.append(dict(kennung=kennung, vorgabe=feld, haus=standard[feld], vorhaben=getattr(vg, feld),
                              begruendung="Lesart des Hauses", art="Lesart", quelle="haus", feld=feld))
    for feld, (kennung, wert) in HAUSWERTE_STEUER.items():    # H-38 und MA-036 stehen in den Steuerparametern
        if _hole(ein, feld) != wert:
            liste.append(dict(kennung=kennung, vorgabe=feld, haus=wert, vorhaben=_hole(ein, feld),
                              begruendung="Lesart des Hauses" if kennung.startswith("MA-") else "Hauswert",
                              art="Lesart" if kennung.startswith("MA-") else "Hauswert", quelle="haus", feld=feld))
    vor = dict(ein.voreinstellungen or {})
    for feld, (kennung, wert) in FESTE_VOREINSTELLUNG.items():
        vor.setdefault(feld, (wert, kennung))
    for feld, (wert, herkunft) in vor.items():
        ist = _hole(ein, feld)
        if feld in FESTE_VOREINSTELLUNG:
            kennung, ist = FESTE_VOREINSTELLUNG[feld][0], (wert if ist is None else ist)
        elif feld in KENNUNG_EINGABE:
            kennung = f"{KENNUNG_EINGABE[feld]} ({herkunft})"
        else:
            raise Meldung("M-20", f"Eingabe '{feld}' hat keine Voreinstellung aus Vorgabe oder Katalog")
        if ist is None or ist == wert:
            continue
        liste.append(dict(kennung=kennung, vorgabe=feld, haus=wert, vorhaben=ist, begruendung=grund.get(feld, ""),
                          art="Lesart" if kennung.startswith("MA-") else "Voreinstellung", quelle="ein", feld=feld))
    return (replace(vg, **neu) if neu else vg), liste


def _ohne(ein, vg, a):
    """Auftrag ohne die eine Abweichung a (fuer ihre Wirkung, R-3.2)."""
    if a["quelle"] == "vg":
        rest = {k: v for k, v in ein.abweichungen.items() if k != a["feld"]}
        return replace(ein, abweichungen=rest or None), vg
    if a["quelle"] == "haus":
        if a["feld"].startswith("steuer."):
            return _setze(ein, a["feld"], a["haus"]), vg
        return ein, replace(vg, **{a["feld"]: a["haus"]})
    return _setze(ein, a["feld"], a["haus"]), vg


def _wirkung_ewd(ein, vg, kat, a, ewd, stress, p, rundung):
    ein_o, vg_o = _ohne(ein, vg, a)
    try:
        e = rechne_grob(ein_o, vg_o, kat, stress=stress, p=p, rundung=rundung, mit_blatt=False, _begruendung=False)
    except Meldung:
        return None
    return None if (e.gesperrt or ewd is None) else ewd - e.kennzahlen["endwertdifferenz"]


def _wirkung_preis(ein, vg, kat, a, preis_voll, p):
    ein_o, vg_o = _ohne(ein, vg, a)
    ohne = _tragbarer_preis(ein_o, vg_o, kat, p=p)["preis"]
    return None if (preis_voll is None or ohne is None) else D(preis_voll) - D(ohne)


def _abstand(e):
    """Abstand der Rendite zur Zielrendite; ohne eingesetztes Eigenkapital der Endwertueberschuss."""
    if e is None or e.gesperrt:
        return None
    k = e.kennzahlen
    return k["abstand_zielrendite"] if k["abstand_zielrendite"] is not None else k["endwertueberschuss"]


def pruefe_begruendungen(ein, vg, kat, p=MONATE, rundung="cent", mit_preis=False):
    """R-3.2: Massstab ist der hoechste tragbare Preis im Basisfall. Eine Abweichung ohne Begruendung ist nur
    zulaessig, wenn sie ihn nicht erhoeht (je Abweichung gegen den Auftrag ohne sie). Laeuft keine Preissuche
    (mit_preis = False) oder liefert sie mit oder ohne die Abweichung keinen Preis, gilt derselbe Massstab am
    Abstand der Rendite zur Zielrendite beim eingegebenen Preis. Sonst M-20."""
    _, liste = vorgaben_im_vorhaben(vg, ein)
    offen = [a for a in liste if a["quelle"] != "haus" and not a["begruendung"]]
    if not offen:
        return
    preis_voll = _tragbarer_preis(ein, vg, kat, p=p)["preis"] if mit_preis else None
    voll = None
    for a in offen:
        w = _wirkung_preis(ein, vg, kat, a, preis_voll, p) if preis_voll is not None else None
        massstab = "den tragbaren Preis"
        if w is None:
            if voll is None:
                voll = rechne_grob(ein, vg, kat, p=p, rundung=rundung, mit_blatt=False, _begruendung=False)
            ein_o, vg_o = _ohne(ein, vg, a)
            try:
                ohne = rechne_grob(ein_o, vg_o, kat, p=p, rundung=rundung, mit_blatt=False, _begruendung=False)
            except Meldung:
                ohne = None
            mit_, ohne_ = _abstand(voll), _abstand(ohne)
            w = None if (mit_ is None or ohne_ is None) else mit_ - ohne_
            massstab = "den Abstand der Rendite zur Zielrendite"
        if w is not None and w > 0:
            raise Meldung("M-20", f"{a['kennung']} {a['vorgabe']}: Abweichung von {a['haus']} auf {a['vorhaben']} erhoeht "
                                  f"{massstab} und braucht eine Begruendung", dict(wirkung=w))


def abweichungsliste(ein, vg, kat, p=MONATE):
    """R-3.2: Liste "Abweichungen vom Hausstandard" mit der Wirkung jeder Abweichung in Euro auf die
    Endwertdifferenz und auf den hoechsten tragbaren Preis, je im Basisfall und je Abweichung gegen den Auftrag
    ohne sie; bei mehreren Abweichungen bleiben die uebrigen stehen."""
    pruefe_begruendungen(ein, vg, kat, p, mit_preis=True)
    _, liste = vorgaben_im_vorhaben(vg, ein)
    voll = rechne_grob(ein, vg, kat, p=p, mit_blatt=False, _begruendung=False)
    ewd = None if voll.gesperrt else voll.kennzahlen["endwertdifferenz"]
    preis_voll = _tragbarer_preis(ein, vg, kat, p=p)["preis"] if liste else None
    for a in liste:
        a["wirkung_endwertdifferenz"] = _wirkung_ewd(ein, vg, kat, a, ewd, False, p, "cent")
        a["wirkung_preis"] = _wirkung_preis(ein, vg, kat, a, preis_voll, p)
    return liste


def _bereich(kennung, name, wert, unten=None, oben=None, offen_unten=False):
    if wert is None:
        raise Meldung("M-20", f"{kennung} {name}: Angabe fehlt")
    if (unten is not None and (wert < unten or (offen_unten and wert == unten))) or (oben is not None and wert > oben):
        grenze = f"{'>' if offen_unten else '>='} {unten}" if oben is None else f"{unten} bis {oben}"
        raise Meldung("M-20", f"{kennung} {name}: Wert {wert} ausserhalb des zulaessigen Bereichs ({grenze})")


def _katalog(kennung, name, wert, ein):
    """R-3.7: fehlender Katalogwert: Meldung M-47, keine Rechnung."""
    if wert is None:
        raise Meldung("M-47", f"{kennung} {name}: Katalogwert fehlt fuer Land '{ein.land}', Gemeinde '{ein.gemeinde}'")


def pruefe_eingaben(ein: Grobeingabe, vg: Vorgaben, kat: Katalog, p):
    """R-3.7: Eingabepruefung gegen die zulaessigen Bereiche aus R-3.3 und R-3.4 und Vollstaendigkeit des
    aufgeloesten Katalogs. Verletzung: Meldung M-20 (M-23 fuer die Haltedauer des Neubaus, M-47 fuer einen
    fehlenden Katalogwert) mit Kennung und Namen der Eingabe; keine Rechnung."""
    b = _bereich
    if ein.art not in ("ankauf", "neubau"):
        raise Meldung("M-20", f"E-01 Vorhabensart: '{ein.art}' ist nicht zulaessig")
    neubau = ein.art == "neubau"
    if not ein.land or not ein.gemeinde:
        raise Meldung("M-20", "E-03, E-04 Land und Gemeinde: Angabe fehlt")
    # ---- Katalog: fuer dieses Land und diese Gemeinde aufgeloest und vollstaendig (R-3.5, R-3.7)
    if kat.land != ein.land or kat.gemeinde != ein.gemeinde:
        raise Meldung("M-47", f"Der Katalog fuehrt keine Werte fuer Land '{ein.land}', Gemeinde '{ein.gemeinde}' (KAT-01, KAT-04, KAT-08)")
    kg = lambda kennung, name, feld: _katalog(kennung, name, getattr(kat, feld), ein)
    kg("KAT-07", "Abschreibungssatz", "afa_satz")
    for feld, name in (("wartefrist", "Wartefrist"), ("kappung", "Kappungsgrenze"), ("kappung_monate", "Kappungszeitraum"),
                       ("mietpreisbremse", "Geltung der Mietpreisbremse"), ("bremse_aufschlag", "Aufschlag der Mietpreisbremse"),
                       ("kappung_gesetzlich", "Kappungsgrenze ohne Gebietsverordnung")):
        kg("KAT-08", name, feld)
    kg("KAT-09", "Anteil des Vermieters an den CO2-Kosten", "co2_vermieteranteil")
    kg("KAT-13", "Kuendigungsrecht: Sperrfrist", "kuendigung_sperre")
    kg("KAT-13", "Kuendigungsrecht: Kuendigungsfrist", "kuendigung_frist")
    if vg.bewirtschaftung_mindest is None:
        kg("KAT-14", "Mindestansatz der Bewirtschaftung", "bewirtschaftung_mindest")
    st = ein.steuer
    if st.status in (KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST):
        _katalog("KAT-03", "Koerperschaftsteuersatz", st.kst_satz, ein)
    if st.status == KOERPERSCHAFT or st.status in PERSONENUNTERNEHMEN:
        _katalog("KAT-04", "Hebesatz der Gemeinde", st.hebesatz, ein)
        _katalog("KAT-04", "Messzahl", st.messzahl, ein)
    if st.status in UEBERSCHUSS:
        _katalog("KAT-06", "Frist des privaten Verkaufs", st.frist_privatverkauf, ein)
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
    b("E-34", "CO2-Ausstoss", ein.co2_ausstoss, NULL)
    if ein.verfuegbares_ek is not None:
        b("E-60", "verfuegbares Eigenkapital", ein.verfuegbares_ek, NULL)
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
        b("E-23", "Vorlauf bis zum Baubeginn", _vorlauf(ein, vg), 0, vg_grenze("vorlauf_max"))
        b("E-16", "Miete bei Bezug", ein.markt_miete, NULL, None, True)
        if ein.nachhaltige_miete is not None:
            b("E-65", "nachhaltige Miete", ein.nachhaltige_miete, NULL, None, True)
        b("E-27", "Stellplaetze", ein.stellplaetze, 0)
        b("E-27", "Miete je Stellplatz", ein.stellplatz_miete, NULL)
        b("E-35", "KfW-Darlehen", ein.kfw_betrag, NULL)
        if ein.kfw_betrag > 0:
            if kat.kfw is None:
                raise Meldung("M-47", "E-35 KfW-Darlehen: Konditionen fehlen im Katalog (KAT-15)")
            k = kat.kfw
            hoechst = k.hoechstbetrag_qng if ein.kfw_qng else k.hoechstbetrag_je_einheit
            b("E-35", "KfW-Darlehen", ein.kfw_betrag, NULL, ein.einheiten * hoechst)
            if not any(lz == ein.kfw_laufzeit and von <= (ein.kfw_tilgungsfrei if ein.kfw_tilgungsfrei is not None else -1) <= bis
                       for lz, von, bis in k.varianten):
                raise Meldung("M-20", f"E-36 Laufzeitvariante des KfW-Darlehens: Laufzeit {ein.kfw_laufzeit} Jahre mit "
                                      f"{ein.kfw_tilgungsfrei} tilgungsfreien Jahren gibt es im Katalog nicht (KAT-15)")
            if ein.kfw_zins is not None:
                b("E-38", "Zins des KfW-Darlehens", ein.kfw_zins, NULL, vg_grenze("zins_max"))
        if ein.foerderung is not None:
            f = ein.foerderung
            b("E-30", "Bodenrichtwert", ein.bodenrichtwert, NULL, None, True)
            if ein.zuschuss_verteilung:
                if ein.steuer.status not in UEBERSCHUSS:
                    raise Meldung("M-20", "E-70 Verteilung des Zuschusses beantragt: nur bei Privatperson, Verein und Stiftung; "
                                          "im Betriebsvermoegen gilt die Lesart nach MA-031")
                kg("KAT-19", "Mindestdauer der Nutzungsueberlassung fuer die Verteilung", "vorauszahlung_jahre")
                if f.bindung_jahre <= kat.vorauszahlung_jahre:
                    raise Meldung("M-20", f"E-70 Verteilung des Zuschusses beantragt: nur bei einer Bindung von mehr als "
                                          f"{kat.vorauszahlung_jahre} Jahren (ESTG-11)")
            if len(f.teilraten) != len(BAUABSCHNITTE) or sum(f.teilraten) != 1 or min(f.teilraten) < 0:
                raise Meldung("M-20", "KAT-10 Teilraten der Foerderauszahlung: je Bauabschnitt ein Anteil, zusammen eins")
            # NBANK-RL-MIETWOHNRAUM-2026 Nr. 5.3.6: Mindesttilgung der vorrangigen Bankmittel
            if ein.tilgungssatz is not None and ein.tilgungssatz < f.bank_mindesttilgung:
                raise Meldung("M-20", f"E-64 Tilgungssatz des Bankdarlehens: Die Foerderrichtlinie verlangt fuer die "
                                      f"vorrangigen Bankmittel mindestens den Satz {f.bank_mindesttilgung} (KAT-10)")
        # R-14.4: die Haltedauer reicht bis zum Ende des ersten Jahres der Vollvermietung, auch im Stressfall
        if ein.haltedauer * p < (_vorlauf(ein, vg) + ein.bauzeit_monate + vg.stress.bauzeit_monate
                                 + _anlauf(ein, vg) + MONATE):
            raise Meldung("M-23", "E-48 Haltedauer endet vor dem Ende des ersten Jahres der Vollvermietung "
                                  "(Vorlauf, Bauzeit einschliesslich der Verlaengerung im Stressfall und Anlaufleerstand)")
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
        if ein.steuer.status not in UEBERSCHUSS:
            b("H-39", "Bodenanteil", vg.bodenanteil, NULL, EINS)
        elif ein.bodenanteil is None:
            if not (ein.bodenrichtwert > 0 and ein.grundstuecksflaeche > 0):
                raise Meldung("M-20", "E-12 Bodenanteil: Angabe fehlt (oder Bodenrichtwert E-30 und Grundstuecksflaeche E-21)")
        else:
            b("E-12", "Bodenanteil", ein.bodenanteil, NULL, EINS)
        b("E-32", "sonstige Ertraege", ein.sonstige_ertraege, NULL)
        b("E-50", "Investitionsstau", ein.stau_betrag, NULL)
        if ein.stau_betrag > 0:
            b("E-51", "Jahr der Ausfuehrung", ein.stau_jahr, 0)
            for feld, name in (("ahk_quote", "Schwelle"), ("ahk_jahre", "Zeitraum"), ("ust_satz", "Umsatzsteuersatz")):
                kg("KAT-12", "anschaffungsnahe Herstellungskosten: " + name, feld)
        b("H-23", "Anpassungsdauer", vg.anpassungsdauer, 0, vg_grenze("anpassung_max"))
        b("E-56", "gebundener Flaechenanteil", ein.gebunden_anteil, NULL, EINS)
        if ein.gebunden_anteil > 0:
            b("E-57", "Bindungsende", ein.bindung_jahre, 1)
            if ein.gebundene_miete is not None:
                b("E-58", "gebundene Miete", ein.gebundene_miete, NULL, None, True)
            for feld in ("geb_steigerung", "geb_fest_jahre", "geb_schritt_jahre"):
                kg("KAT-11", "uebernommene Bindung", feld)
        if ein.mietenhistorie is not None:
            b("E-33", "Monate seit der letzten Mieterhoehung", ein.mietenhistorie[0], 0)
            b("E-33", "Miete drei Jahre vor dem Stichtag", ein.mietenhistorie[1], NULL, ein.ist_miete, True)
        ue = ein.uebernommen
        if ue:
            b("E-59", "uebernommenes Darlehen, Restschuld", d(ue["restschuld"]), NULL, None, True)
            b("E-59", "uebernommenes Darlehen, urspruenglicher Nennbetrag", d(ue.get("nennbetrag", ue["restschuld"])), d(ue["restschuld"]))
            b("E-59", "uebernommenes Darlehen, Zins", d(ue["zins"]), NULL, vg_grenze("zins_max"))
            b("E-59", "uebernommenes Darlehen, Tilgungssatz", d(ue["tilgungssatz"]), NULL)
            if ue.get("bindung_jahre") is not None:
                b("E-59", "uebernommenes Darlehen, Ende der Zinsbindung", ue["bindung_jahre"], 1, vg_grenze("bindung_max"))
            if ue.get("anschluss_zins") is not None:
                b("E-59", "uebernommenes Darlehen, Anschlusszins", d(ue["anschluss_zins"]), NULL, vg_grenze("zins_max"))
            b("E-59", "uebernommenes Darlehen, laufender Beitrag", d(ue.get("beitrag_satz", 0)), NULL, vg_grenze("zins_max"))
    # ---- Vorgaben des Hauses (R-3.4): jede Vorgabe hat einen zulaessigen Bereich
    b("H-01", "Zielrendite", zielrendite(ein, vg), -EINS, None, True)
    b("H-02", "Beleihungsquote", vg.beleihungsquote, NULL, EINS)
    b("H-03", "Mindestdeckung", vg.mindestdeckung, EINS)
    b("H-04", "Mindesttilgung", vg.mindesttilgung, NULL)
    b("H-05", "Anschlussaufschlag", vg.anschluss_aufschlag, NULL)
    s = vg.stress
    for name, wert in (("Anschlusszins", s.anschlusszins_pp), ("Zins bis zur Zusage", s.zusage_pp), ("Leerstand", s.leerstand_pp),
                       ("Verkaufsfaktor", s.verkaufsfaktor_rel), ("Mietsteigerung", s.mietsteigerung_pp),
                       ("Investitionsstau", s.stau_rel),
                       ("Baukosten", s.baukosten_rel), ("Bauzeit", s.bauzeit_monate)):
        b("H-06", "Stresshoehe " + name, wert, 0)
    b("H-06", "Stresshoehe Verkaufsfaktor", s.verkaufsfaktor_rel, NULL, EINS)
    b("H-08", "kurzfristiger Habenzins", vg.h_kurz, NULL)
    if vg.a_lang is not None:
        b("H-09", "langfristiger Anlagezins", vg.a_lang, NULL)
    b("H-10", "Kontokorrentzins", vg.kk_zins, vg.h_kurz)
    if vg.kk_linie is not None:
        b("H-11", "Kontokorrentlinie", vg.kk_linie, NULL)
    for kennung, name, wert in (("H-12", "Mietsteigerung", vg.mietsteigerung), ("H-13", "Kostensteigerung", vg.kostensteigerung),
                                ("H-14", "Baupreissteigerung", vg.baupreissteigerung)):
        b(kennung, name, wert, vg_grenze("steigerung_min"), vg_grenze("steigerung_max"))
    b("H-15, H-27", "Leerstand und Forderungsausfall", vg.leerstand + vg.forderungsausfall, NULL, EINS)
    b("H-15", "struktureller Leerstand", vg.leerstand, NULL, EINS)
    b("H-27", "Forderungsausfall", vg.forderungsausfall, NULL, EINS)
    b("H-16", "Verkaufskosten", vg.verkaufskostensatz, NULL, vg_grenze("enk_max"))
    b("H-17", "Verwaltung je Einheit", vg.verwaltung_je_einheit, NULL)
    b("H-17", "Betriebskosten je m2", vg.betriebskosten_je_qm, NULL)
    staffel = vg.instandhaltung_staffel
    if not staffel or staffel[0][0] != 0 or any(x[1] < 0 for x in staffel) or [x[0] for x in staffel] != sorted({x[0] for x in staffel}):
        raise Meldung("M-20", "H-17 Staffel der Instandhaltung: mindestens eine Stufe ab dem Gebaeudealter null, "
                              "aufsteigend, Betraege nicht negativ")
    b("H-18", "Vorfaelligkeitssatz", vg.vfe_satz, NULL)
    b("H-21", "Obergrenze der Preissuche", vg.such_obergrenze_faktor, NULL, None, True)
    b("H-21", "Rasterzahl", vg.suchraster, 1)
    b("H-21", "Fenster der Nachsuche", vg.nachsuchfenster, 0)
    b("H-21", "Obergrenze der Mietsuche", vg.such_miete_max, NULL, None, True)
    b("H-21", "interner Zinsfuss, Untergrenze", vg.izf_unten, -EINS, None, True)
    b("H-21", "interner Zinsfuss, Obergrenze", vg.izf_oben, vg.izf_unten, None, True)
    b("H-21", "interner Zinsfuss, Rasterzahl", vg.izf_raster, 1)
    if vg.kalk_zins is not None:
        b("H-25", "kalkulatorischer Zins", vg.kalk_zins, NULL, vg_grenze("zins_max"))
    b("H-26", "Fluktuation", vg.fluktuation, NULL, EINS)
    b("H-28", "Anlaufleerstand", vg.anlaufleerstand, 0)
    if vg.anlaufleerstand_neubau is not None:
        b("H-34", "Anlaufleerstand bei Erstvermietung", vg.anlaufleerstand_neubau, 0)
    if ein.art == "neubau" and ein.foerderung is not None:
        if vg.bauabschnitt_rohbau is None or vg.bauabschnitt_innenputz is None:
            raise Meldung("M-20", "H-37 Bauabschnitte der Foerderauszahlung: Vorgabe fehlt")
        b("H-37", "Anteil der Bauzeit bis zum Rohbau", vg.bauabschnitt_rohbau, NULL, EINS, True)
        b("H-37", "Anteil der Bauzeit bis zum Innenputz", vg.bauabschnitt_innenputz, vg.bauabschnitt_rohbau, EINS)
    b("H-29", "CO2-Preis", vg.co2_preis, NULL)
    b("H-29", "Steigerung des CO2-Preises", vg.co2_steigerung, vg_grenze("steigerung_min"), vg_grenze("steigerung_max"))
    for name, wert in (("Zuschlag Kostengruppen 200, 500, 600", vg.zuschlag_kg_uebrige), ("Zuschlag Kostengruppe 700", vg.zuschlag_kg700),
                       ("Herstellungskosten je Stellplatz", vg.kosten_je_stellplatz)):
        b("H-30", name, wert, NULL)
    b("H-31", "Bereitstellungszins", vg.bereit_satz, NULL)
    b("H-31", "bereitstellungsfreie Zeit", vg.bereit_frei, 0)
    if vg.bemessungszeitraum is not None:
        b("H-32", "Bemessungszeitraum", vg.bemessungszeitraum, 1, vg_grenze("bindung_max"))
    if vg.bewirtschaftung_mindest is not None:
        b("H-33", "Mindestansatz der Bewirtschaftung", vg.bewirtschaftung_mindest, NULL, EINS)
    if vg.ma031_zuschuss not in (None, "sofort", "verteilt"):
        raise Meldung("M-20", "MA-031: Lesart des Zuschusses unbekannt")


def _bodenanteil(ein, vg, preis):
    """E-12 gilt nur, wo der Verkauf nach der Frist steuerfrei bleiben kann (Privatperson, Verein, Stiftung); sonst
    gleichen sich Abschreibung und Verkaufsgewinn aus, und der Kern rechnet mit dem festen Hauswert H-39."""
    if ein.steuer.status not in UEBERSCHUSS:
        return vg.bodenanteil
    if ein.bodenanteil is not None:
        return ein.bodenanteil
    return min(EINS, ein.bodenrichtwert * ein.grundstuecksflaeche / D(preis))


def zielrendite(ein, vg):
    """H-01: Zielrendite je Vorhabensart, fuer gefoerderte Vorhaben eigens."""
    if ein.foerderung is not None and vg.zielrendite_gefoerdert is not None:
        return vg.zielrendite_gefoerdert
    if ein.art == "neubau" and vg.zielrendite_neubau is not None:
        return vg.zielrendite_neubau
    return vg.zielrendite


def _vorlauf(ein, vg):
    """E-23: Monate vom Grundstueckskauf bis zum Baubeginn; Voreinstellung H-35."""
    if ein.art != "neubau":
        return 0
    if ein.vorlauf_monate is not None:
        return ein.vorlauf_monate
    return vg.vorlauf if vg.vorlauf is not None else 0


def _anlauf(ein, vg):
    """H-28, H-34, E-39: Monate bis zur Vermietung leerer Flaechen (Ankauf) oder bis zur Erstvermietung (Neubau);
    bei Vorvermietung null."""
    if ein.art != "neubau":
        return vg.anlaufleerstand
    if ein.vorvermietet:
        return 0
    return vg.anlaufleerstand_neubau if vg.anlaufleerstand_neubau is not None else vg.anlaufleerstand


# Grenzen der zulaessigen Bereiche (R-3.3, Spalte "zulaessig"): Teil des Auftrags, von annahmen.py gesetzt
GRENZEN = {}


def vg_grenze(name):
    if name not in GRENZEN:
        raise Meldung("M-20", f"Grenze '{name}' der Eingabepruefung fehlt im Auftrag")
    return GRENZEN[name]


# ------------------------------------------------------------------------------------------------ Kapitel 6
class Ertragsreihen:
    """Mieteinzahlungen, laufende Kosten, Sollmieten und Indexreihen eines Laufs (Kapitel 6)."""


def _mietrecht(ein, vg, kat, raster):
    """R-6.18 (KAT-08, MA-039): Kappungsgrenze und Mietpreisbremse je Monat. Am Stichtag gilt der Katalogwert der
    Gemeinde, je Vorhaben ueberschreibbar (E-05). Nach dem Geltungsende einer Gebietsverordnung gilt sie
    voreingestellt fort (MA-039); in der anderen Lesart gelten ab dem folgenden Kalenderjahr die Kappungsgrenze
    ohne Verordnung und keine Mietpreisbremse. Ein Neubau unterliegt der Mietpreisbremse nicht (BGB-556F)."""
    gebiet_k = ((kat.kappung != kat.kappung_gesetzlich) if (ein.im_kappungsgebiet is None or ein.art == "neubau")
                else ein.im_kappungsgebiet)             # E-05 nur im Ankauf; im Neubau gilt der Katalogwert
    gebiet_b = kat.mietpreisbremse if ein.im_bremsgebiet is None else ein.im_bremsgebiet
    if ein.art == "neubau":
        gebiet_b = False
    abgesenkt = kat.kappung if gebiet_k else kat.kappung_gesetzlich

    def kappung(m):                                      # MA-039: die Gebietsverordnungen gelten fort
        return abgesenkt

    def bremse(m):
        return gebiet_b

    mr = ertrag.Mietrecht(kat.wartefrist, kat.kappung_monate, kappung, bremse, kat.bremse_aufschlag)
    mr.geb_steigerung, mr.geb_fest_jahre, mr.geb_schritt_jahre = kat.geb_steigerung, kat.geb_fest_jahre, kat.geb_schritt_jahre
    mr.gebiet = (gebiet_k, gebiet_b)
    return mr


def _ertragsreihen(ein, vg, kat, raster, rd, stress, bauende):
    """Kapitel 6. bauende = letzter Monat der Bauzeit (Vorlauf und Bauzeit, im Stressfall verlaengert); Ankauf 0."""
    p, N = raster.p, raster.N
    st = vg.stress if stress else Stress()
    M = raster.n * MONATE + MONATE                       # Monate der Mietreihe: Haltedauer und ein Folgejahr
    jahre = raster.n + 2
    steig = vg.mietsteigerung - st.mietsteigerung_pp
    leer = min(EINS, vg.leerstand + st.leerstand_pp)     # im Stressfall hoechstens 100 %
    ausfall = min(EINS, leer + vg.forderungsausfall)
    neubau = ein.art == "neubau"
    anlauf = _anlauf(ein, vg)
    mr = _mietrecht(ein, vg, kat, raster)
    r = Ertragsreihen()
    r.erste = (bauende + anlauf + 1) if neubau else 1    # erster Vermietungsmonat
    r.bezug = bauende + 1
    r.mietrecht = mr
    dauer = vg.anpassungsdauer or 0                      # H-23
    if neubau:
        # R-6.7: nach dem Ende einer Bindung gilt die Anpassungsdauer der Vorgabe H-23
        pools, vm, vm_n = ertrag.mieten_neubau(M, ein, mr, r.erste, r.bezug, steig, vg.anpassungsdauer or 0, rd, ein.foerderung)
        sonst_jahr = ein.stellplaetze * ein.stellplatz_miete * MONATE
    else:
        pools, vm, vm_n = ertrag.mieten_ankauf(M, ein, mr, vg.fluktuation, anlauf, steig, dauer, rd,
                                               rueckfuehrung=vg.ma038_rueckfuehrung)
        sonst_jahr = ein.sonstige_ertraege
    soll_roh, nachh_roh, flaeche = ertrag.monatswerte(pools, vm_n, M)
    idx_m = ertrag.indexreihe(jahre, steig, rd)
    idx_k = ertrag.indexreihe(jahre, vg.kostensteigerung, rd)
    idx_co2 = ertrag.indexreihe(jahre, vg.co2_steigerung, rd)
    idx_erb = idx_k                                      # R-6.11: der Erbbauzins steigt mit der Kostensteigerung H-13
    r.indexreihen = {"Mieten": (idx_m, steig), "Kosten": (idx_k, vg.kostensteigerung),
                     "CO2-Preis": (idx_co2, vg.co2_steigerung), "Erbbauzins": (idx_erb, vg.kostensteigerung)}
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

    def bewirtschaftung(u):                              # R-6.8, R-6.9 ohne Erbbauzins
        if u < 1 or u * MONATE // p < r.bezug:
            return NULL
        j = raster.planjahr(u)
        # Gebaeudealter im Planjahr: Ankauf Kalenderjahr - Baujahr, Neubau Jahre seit dem Bezug
        alter = (alter0 + j - 1) if not neubau else (u * MONATE // p - r.bezug) // MONATE
        inst = ertrag.instandhaltung_je_qm(vg.instandhaltung_staffel, alter)
        jahr = (vg.verwaltung_je_einheit * ein.einheiten + inst * ein.wohnflaeche
                + vg.betriebskosten_je_qm * ein.wohnflaeche) * idx_k[j]
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


def _baukosten(ein, vg, rd, bauzeit, vorlauf=0, aufschlag=NULL):
    """R-11.2: Baukosten zum Preisstand des Stichtags und Monatsraten ab dem Monat nach dem Vorlauf, jede mit der
    Baupreissteigerung vom Stichtag auf ihren Monat fortgeschrieben; bei Festpreis (E-24) ohne Fortschreibung.
    Der Kennwert E-25 gilt fuer die Kostengruppen 300 und 400 (dann mit den Zuschlaegen H-30) oder fuer die
    Gesamtkosten der Kostengruppen 200 bis 700 (dann ohne Zuschlaege)."""
    zuschlag = NULL if ein.kennwert_gesamt else vg.zuschlag_kg_uebrige + vg.zuschlag_kg700
    stichtag = (rd.geld(ein.bgf * ein.kostenkennwert * (EINS + zuschlag))
                + rd.geld(ein.stellplaetze * vg.kosten_je_stellplatz))
    stichtag = rd.geld(stichtag * (EINS + aufschlag))
    steig = NULL if ein.festpreis else vg.baupreissteigerung
    raten = {vorlauf + m: rd.geld(stichtag / bauzeit * rd.satz((EINS + steig) ** (D(vorlauf + m) / MONATE)))
             for m in range(1, bauzeit + 1)}
    return stichtag, raten


def _tranche_uebernommen(ein, vg, kat, p, stress_pp=NULL, zins_bank=None):
    ue = ein.uebernommen
    bindung = ue.get("bindung_jahre")
    anschluss = ue.get("anschluss_zins")
    if anschluss is None:                                # Voreinstellung: Anschlusszins des Bankdarlehens (R-5.8)
        anschluss = (ein.zins if zins_bank is None else zins_bank) + vg.anschluss_aufschlag
    ende = None if bindung is None else bindung * p
    # BGB-489: der Beginn der Zinsbindung ist nicht bekannt; vorsichtig zaehlt die Frist ab dem Stichtag
    kuendbar = _perioden_auf(kat.kuendigung_sperre + kat.kuendigung_frist, p)
    return Tranche("Uebernommenes Darlehen", ue["restschuld"], "annuitaet_prozent", ue["zins"],
                   tilgungssatz=ue["tilgungssatz"], rate_betrag=ue.get("nennbetrag", ue["restschuld"]),
                   bindung=ende, anschluss_zins=d(anschluss) + stress_pp, anschluss_regel=ANSCHLUSSREGEL,
                   anschluss_tilgung=max(d(ue["tilgungssatz"]), vg.mindesttilgung),
                   beitrag_satz=ue.get("beitrag_satz", 0), bank=False, foerder=False,
                   vfe_bis=None if ende is None else min(ende, kuendbar))


def _perioden_auf(monate, p):
    """Monate in Perioden, auf ganze Perioden aufgerundet (R-5.16: im Jahresmodus die laengere Restbindung)."""
    return -(-monate * p // MONATE)


# R-11.3: Bauabschnitte, nach denen die Teilraten der Foerderung fliessen (NBANK-RL-MIETWOHNRAUM-2026 Nr. 5.5.3)
BAUABSCHNITTE = ("Baubeginn", "Rohbau", "Innenputz", "Fertigstellung und Belegung")


def _auf_ganze(x):
    """Aufrunden auf die naechste ganze Zahl (Decimal teilt ganzzahlig zur Null hin, deshalb nicht ueber //)."""
    ganz = int(x)
    return ganz if ganz == x else ganz + 1


def _foerder_termine(ein, vg, vorlauf, bauzeit, bauende):
    """R-11.3, R-5.11 (NBANK-RL-MIETWOHNRAUM-2026 Nr. 5.3.5, 5.5.3): Monate der vier Teilraten mit ihrem
    kumulierten Anteil, Periode der ersten Tilgung und Zahl der Tilgungsperioden des Foerderdarlehens.

    Festlegung: Baubeginn ist der erste Monat der Bauzeit; Rohbau und Innenputz sind nach den Anteilen H-37 der
    Bauzeit fertig, aufgerundet auf ganze Monate; die Teilrate steht im Monat danach bereit; die letzte Teilrate
    im ersten Monat nach Bauzeit und Anlaufleerstand. Die Foerderentscheidung gilt als im Monat vor dem
    Baubeginn bekanntgegeben."""
    f = ein.foerderung
    a = f.teilraten
    m4 = bauende + _anlauf(ein, vg) + 1
    stufen = [(vorlauf + 1, a[0]),
              (vorlauf + _auf_ganze(vg.bauabschnitt_rohbau * bauzeit) + 1, a[0] + a[1]),
              (vorlauf + _auf_ganze(vg.bauabschnitt_innenputz * bauzeit) + 1, a[0] + a[1] + a[2]),
              (m4, EINS)]
    beginn = min(m4 + 1, vorlauf + 1 + f.tilgungsfrist_monate)
    laufzeit = bauende + f.tilgung_jahre * MONATE - beginn + 1
    return stufen, beginn, laufzeit


def _tranche_foerder(f, betrag, auszahlung, einbehalt, tilgungsbeginn, laufzeit, bauende, p):
    # MA-002: gleichbleibende Raten vom Tilgungsbeginn bis zum Ende der Rueckzahlungsfrist; zinslos bis zum Ablauf
    # der zinslosen Jahre nach der Bezugsfertigkeit, danach MA-003
    return Tranche("Foerderdarlehen", betrag, "raten", 0, laufzeit=laufzeit, auszahlung=auszahlung,
                   einbehalt=einbehalt, tilgungsbeginn=tilgungsbeginn,
                   bindung=f.zinslos_jahre * p + bauende, anschluss_zins=f.zins_danach,
                   beitrag_satz=f.vkb_satz, bank=False, foerder=True)


def _kfw_konditionen(ein, kat):
    """R-5.19 (KAT-15): aufgeloeste Konditionen des KfW-Darlehens."""
    k = kat.kfw
    return dict(zins=ein.kfw_zins if ein.kfw_zins is not None else k.zins, laufzeit=ein.kfw_laufzeit,
                tilgungsfrei=ein.kfw_tilgungsfrei, tilgungsperioden=(ein.kfw_laufzeit - ein.kfw_tilgungsfrei) * MONATE,
                bindung=k.zinsbindung_jahre * MONATE)


def bemesse(ein, vg, kat, raster, rd, preis=None, miete_ansatz=None, zusage_pp=NULL):
    """R-11.2: Mittelbedarf, uebrige Darlehen, Zuschuesse und Bankdarlehen nach R-5.12 aus den Basisannahmen.
    miete_ansatz: einheitliche Miete je m2 anstelle der nachhaltigen Miete (nur fuer R-11.15).
    zusage_pp: Zinsanstieg bis zur Kreditzusage (R-11.8): Aufschlag auf den Zins des Bankdarlehens E-45."""
    p = raster.p
    neubau = ein.art == "neubau"
    P = d(preis) if preis is not None else (ein.grundstueckspreis if neubau else ein.kaufpreis)
    enk = rd.geld(P * ein.enk_satz)
    bauzeit = ein.bauzeit_monate if neubau else 0
    vorlauf = _vorlauf(ein, vg)
    bauende = vorlauf + bauzeit
    bk0, raten = _baukosten(ein, vg, rd, bauzeit, vorlauf) if neubau else (NULL, {})
    baukosten = sum(raten.values(), NULL)
    stau0 = rd.geld(ein.stau_betrag) if (ein.stau_betrag and ein.stau_jahr == 0) else NULL
    er = _ertragsreihen(ein, vg, kat, raster, rd, False, bauende)
    ab = (er.erste - 1) * p // MONATE + 1
    vj = range(ab, ab + p)                               # erstes Jahr der Vollvermietung
    reinertrag_vj = sum(er.einzahlung(u) - er.kosten(u) for u in vj)
    mindest = vg.bewirtschaftung_mindest if vg.bewirtschaftung_mindest is not None else kat.bewirtschaftung_mindest
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
        abzug = max(bew + (roh - einz), rd.geld(mindest * roh))
        ertrag_n = roh - abzug - sum(er.erbbau(u) for u in vj)
    # ---- kalkulatorische Konditionen (R-5.12 b): Bankdarlehen mit dem hoeheren aus Vertragszins und
    # kalkulatorischem Zins; uebrige Tranchen mit dem Bemessungszins ueber den Bemessungszeitraum
    zins_bank = ein.zins + zusage_pp
    tilg = ein.tilgungssatz if ein.tilgungssatz is not None else vg.mindesttilgung
    anschluss_bank = zins_bank + vg.anschluss_aufschlag
    zeitraum = (vg.bemessungszeitraum if vg.bemessungszeitraum is not None else ein.zinsbindung_jahre) * p

    def kalk(zins, anschluss, vorgabe):                  # kalkulatorischer Zins einer Tranche (H-25)
        return max(zins, vorgabe if vorgabe is not None else anschluss)

    def zins_b(zins, bindung, anschluss, vorgabe):       # Bemessungszins einer uebrigen Tranche
        if vg.ma026_fremde_kalkulatorisch:               # Lesart 4 von MA-026: wie das Bankdarlehen
            return kalk(zins, anschluss, vorgabe)
        return bemessungszins(zins, bindung, kalk(zins, anschluss, vorgabe), zeitraum, rd)

    zins_kalk, tilg_kalk = kalk(zins_bank, anschluss_bank, vg.kalk_zins), max(tilg, vg.mindesttilgung)
    if neubau and ein.foerderung:                        # Nr. 5.3.6: Mindesttilgung der vorrangigen Bankmittel
        tilg_kalk = max(tilg_kalk, ein.foerderung.bank_mindesttilgung)
    uebrige = im_raum = zuschuss = zuschuss_geb = fd = ek_min = e_d = e_z = kfw = NULL
    kd, ib, kfw_kond = {}, {}, None
    if ein.uebernommen and not neubau:
        ue = ein.uebernommen
        schuld = d(ue["restschuld"])
        uebrige += schuld
        im_raum += schuld                                # vorsichtig: im Rang vor der Bank
        tr = _tranche_uebernommen(ein, vg, kat, p, zins_bank=zins_bank)
        ib[tr.name] = zins_b(tr.zins, tr.bindung, tr.anschluss_zins, vg.kalk_zins)
        # der Tilgungssatz bezieht sich wie in der Rate auf den urspruenglichen Nennbetrag (R-5.11)
        kd[tr.name] = bemessungskapitaldienst("annuitaet_prozent", tr.rate_betrag, ib[tr.name], vg.mindesttilgung, p, rd,
                                              tilgungssatz=tr.tilgungssatz, beitrag_basis=schuld, beitrag_satz=tr.beitrag_satz)
    if neubau and ein.kfw_betrag > 0:
        kfw = ein.kfw_betrag
        kfw_kond = _kfw_konditionen(ein, kat)
        uebrige += kfw
        im_raum += kfw                                   # Festlegung: das durchgeleitete KfW-Darlehen belegt den Raum
        ib["KfW-Darlehen"] = zins_b(kfw_kond["zins"], kfw_kond["bindung"] * p // MONATE, anschluss_bank, vg.kalk_zins)
        kd["KfW-Darlehen"] = bemessungskapitaldienst("annuitaet_laufzeit", kfw, ib["KfW-Darlehen"], vg.mindesttilgung, p, rd,
                                                     laufzeit=kfw_kond["tilgungsperioden"] * p // MONATE)
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
        # Der Nachrang steht in der Richtlinie (Nr. 5.3.6, 11.5); der Kern rechnet die Quote der Bank trotzdem ueber
        # alle Darlehen (MA-026). Im gefoerderten Neubau bindet die Schuldendienstdeckung, nicht die Quote
        im_raum += fd
        zinslos_bis = f.zinslos_jahre * p + bauende * p // MONATE
        danach = f.zins_danach if f.zins_danach is not None else NULL
        ib["Foerderdarlehen"] = zins_b(NULL, zinslos_bis, danach, vg.kalk_zins)
        _, _, laufzeit_fd = _foerder_termine(ein, vg, vorlauf, bauzeit, bauende)
        kd["Foerderdarlehen"] = bemessungskapitaldienst("raten", fd, ib["Foerderdarlehen"], vg.mindesttilgung, p, rd,
                                                        laufzeit=laufzeit_fd, beitrag_basis=fd, beitrag_satz=f.vkb_satz)
    kd_ue = sum(kd.values(), NULL)
    mittelbedarf = P + enk + baukosten + stau0 + e_d + e_z
    gesamtkosten = P + enk + baukosten                   # R-1.1: Gesamtkosten ohne Finanzierungskosten
    wert = gesamtkosten if neubau else P                 # Wertansatz der Bank: Kaufpreis, im Neubau die Gesamtkosten
    bank = bankdarlehen(wert, vg.beleihungsquote, ertrag_n, vg.mindestdeckung, zins_kalk, tilg_kalk, mittelbedarf,
                        uebrige_darlehen=uebrige, uebrige_im_beleihungsraum=im_raum, kd_uebrige=kd_ue,
                        zuschuesse=zuschuss, ek_min=ek_min, p=p, rd=rd)
    if bank["c"] < 0:
        text = "Uebrige Darlehen, Zuschuesse und Mindesteigenkapital uebersteigen den Mittelbedarf"
        angaben = dict(mittelbedarf=mittelbedarf, uebrige_mittel=uebrige + zuschuss + ek_min)
        if kfw > 0:                                      # R-14.7: hoechster KfW-Betrag, der passt
            angaben["kfw_hoechstens"] = max(NULL, ab_cent(kfw + bank["c"]))
            text += f"; KfW-Darlehen hoechstens {angaben['kfw_hoechstens']} Euro"
        raise Meldung("M-22", text, angaben)
    # ---- Boden und Gebaeude (R-7.3, R-12.3)
    if neubau:
        boden, anteil = P + enk, None
    else:
        anteil = _bodenanteil(ein, vg, P)
        boden = rd.geld((P + enk) * anteil)
    return Bemessung(P, enk, bk0, baukosten, mittelbedarf, wert, uebrige, im_raum, zuschuss, zuschuss_geb, fd, kfw,
                     ek_min, e_d, e_z, reinertrag_vj, ertrag_n, kd_ue, kd, zins_kalk, tilg_kalk, bank, boden, anteil,
                     bemessungszins=ib, bemessungszeitraum=zeitraum, mindestansatz=mindest, kfw_kond=kfw_kond)


# ------------------------------------------------------------------------------------------------ R-11.1
def rechne_grob(ein: Grobeingabe, vg: Vorgaben, kat: Katalog, preis=None, stress=False, rundung="cent", p=MONATE,
                mit_blatt=True, geprueft=False, _begruendung=True) -> Grobergebnis:
    """R-11.1: eine Grobkalkulation im Basisfall oder im kombinierten Stressfall.

    Ergebnis mit erg.gesperrt = True und ohne Kennzahlen, wenn eine Probe verletzt ist (R-13.1, M-10).
    Eingabefehler enden als Meldung (M-20, M-22, M-23, M-24, M-43, M-47); Hinweise stehen in erg.meldungen.
    """
    rd = Rundung(rundung)
    abweichungen = []
    vg_haus = vg
    if not geprueft:
        if rundung == "keine" and p != 1:                # R-12.2: ohne Rundung nur der Lehrbuchvergleich im Jahresmodus
            raise Meldung("M-20", "Rundungsmodus 'keine' ist nur im Jahresmodus zulaessig")
        vg, abweichungen = vorgaben_im_vorhaben(vg, ein)
        pruefe_eingaben(ein, vg, kat, p)
        if _begruendung:
            pruefe_begruendungen(ein, vg_haus, kat, p, rundung)
    raster = Raster(p=p, n=ein.haltedauer, startjahr=ein.stichtag_jahr)
    N = raster.N
    neubau = ein.art == "neubau"
    st = vg.stress if stress else Stress()
    meldungen = []

    def melde(kennung, text, **angaben):
        meldungen.append(dict(kennung=kennung, text=text, **angaben))

    bm = bemesse(ein, vg, kat, raster, rd, preis)        # Darlehen aus den Basisannahmen (R-11.8) ...
    darlehen_basis = bm.bank["darlehen"]
    if stress and st.zusage_pp:
        # ... im Stressfall aber mit dem Zinsanstieg bis zur Kreditzusage neu bemessen: Vor der Zusage ist nichts
        # bemessen; die Bank rechnet mit dem hoeheren Zins. Alle uebrigen Groessen der Bemessung bleiben Basis.
        bm = bemesse(ein, vg, kat, raster, rd, preis, zusage_pp=st.zusage_pp)
    L = bm.bank["darlehen"]
    vorlauf = _vorlauf(ein, vg)
    bauzeit = (ein.bauzeit_monate + st.bauzeit_monate) if neubau else 0
    bauende = vorlauf + bauzeit                           # letzter Monat der Bauzeit; Ende der Investitionsphase
    er = _ertragsreihen(ein, vg, kat, raster, rd, stress, bauende)
    null = lambda: [NULL] * (N + 1)
    miete, kost, erh, inv, zus = null(), null(), null(), null(), null()
    zus_einb, afa, einl, pacht, zwischen = null(), null(), null(), null(), null()
    for u in range(1, N + 1):
        miete[u], kost[u], pacht[u] = er.einzahlung(u), er.kosten(u), er.erbbau(u)
    # ---- Investitionsauszahlungen
    inv[0] = bm.preis + bm.enk
    baukosten = NULL
    if neubau:
        _, raten = _baukosten(ein, vg, rd, bauzeit, vorlauf, st.baukosten_rel)
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
            aktivieren = False                           # Erhaltungsaufwand, ausser anschaffungsnah (R-6.16)
            if (not neubau and stau_jahr <= kat.ahk_jahre
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
    fm_gesamt = bm.foerderdarlehen + bm.zuschuss
    stufen = fd_beginn = fd_laufzeit = None
    abruf_ende = bauende
    if neubau and ein.foerderung and fm_gesamt > 0:      # R-11.3: Teilraten der Foerderrichtlinie
        stufen, fd_beginn, fd_laufzeit = _foerder_termine(ein, vg, vorlauf, bauzeit, bauende)
        abruf_ende = stufen[-1][0]
    luecke = fm_gezogen = NULL
    for m in range(0, abruf_ende + 1):
        bedarf = (inv[m] if m <= bauende else NULL) + (erh[0] if m == 0 else NULL) - (uebern if m == 0 else NULL)
        x = min(rest_ek, bedarf)
        if x > 0:
            einl[m] += x
            rest_ek -= x
            bedarf -= x
        frei = rest_fd + rest_zs
        if stufen is not None:                           # kumulierte Obergrenze der Teilraten
            anteil = max([a for (ab, a) in stufen if ab <= m], default=NULL)
            frei = min(frei, rd.geld(anteil * fm_gesamt) - fm_gezogen)
        if (bedarf + luecke) > 0 and frei > 0:
            if not foerder_gezogen:
                bedarf += bm.einbehalt_darlehen + bm.einbehalt_zuschuss
                zus_einb[m] += bm.einbehalt_zuschuss
                foerder_gezogen = True
            # die Teilrate holt nach, was seit der letzten Obergrenze ungedeckt blieb; die letzte fliesst ganz
            y = min(frei, bedarf + luecke)
            if stufen is not None and m == abruf_ende:
                y = rest_fd + rest_zs
            if y == rest_fd + rest_zs:
                teil_fd, teil_zs = rest_fd, rest_zs
            else:
                # R-11.3: Darlehen und Zuschuss im Verhaeltnis ihrer Betraege; gerundet wird der Teil des
                # Darlehens, der Zuschuss traegt den Rest; keiner uebersteigt seinen offenen Betrag
                teil_fd = min(rest_fd, rd.geld(y * bm.foerderdarlehen / (bm.foerderdarlehen + bm.zuschuss)))
                teil_zs = y - teil_fd
                if teil_zs > rest_zs:
                    teil_zs, teil_fd = rest_zs, y - rest_zs
            if teil_fd:
                aus_fd[m] = teil_fd
            zus[m] += teil_zs
            rest_fd -= teil_fd
            rest_zs -= teil_zs
            fm_gezogen += y
            nachgeholt = max(NULL, y - bedarf)           # fuehrt die Zwischenfinanzierung zurueck
            luecke = max(NULL, luecke - nachgeholt)
            bedarf -= y - nachgeholt
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
        if bedarf > 0:
            if stufen is not None:                       # Luecke bis zur naechsten Teilrate (R-11.3)
                luecke += bedarf
            else:                                        # darf nicht vorkommen; die Probe P-04 meldet es
                einl[m] += bedarf
        zwischen[m] = luecke                             # Zwischenfinanzierung der zugesagten Foerdermittel
    # nicht abgerufene Mittel fliessen mit der letzten Bauperiode (R-11.3)
    if rest_bank > 0:
        aus_bank[bauende] = aus_bank.get(bauende, NULL) + rest_bank
    if rest_kfw > 0:
        aus_kfw[bauende] = aus_kfw.get(bauende, NULL) + rest_kfw
    if rest_fd > 0:
        aus_fd[abruf_ende] = aus_fd.get(abruf_ende, NULL) + rest_fd
    if rest_zs > 0:
        zus[abruf_ende] += rest_zs
    if rest_ek > 0:
        einl[bauende] += rest_ek
    if STOERUNG[0]:
        STOERUNG[0](locals())
    # ---- Tranchen
    tilg = ein.tilgungssatz if ein.tilgungssatz is not None else vg.mindesttilgung
    if neubau and ein.foerderung:                        # Nr. 5.3.6: Mindesttilgung der vorrangigen Bankmittel
        tilg = max(tilg, ein.foerderung.bank_mindesttilgung)
    kuendbar = kat.kuendigung_sperre + kat.kuendigung_frist      # BGB-489, in Monaten ab vollstaendigem Empfang
    zins_bank = ein.zins + st.zusage_pp
    anschluss_bank = zins_bank + vg.anschluss_aufschlag + st.anschlusszins_pp
    tranchen = []
    if L > 0:
        plan_aus = aus_bank or {0: L}
        bindung = ein.zinsbindung_jahre * p
        tranchen.append(Tranche(
            "Bankdarlehen", L, "annuitaet_prozent", zins_bank, tilgungssatz=tilg, auszahlung=plan_aus,
            tilgungsbeginn=bauende + 1, bindung=bindung,
            anschluss_zins=zins_bank + st.anschlusszins_pp if "tranche_ohne_aufschlag" in FEHLER else anschluss_bank,
            anschluss_regel=ANSCHLUSSREGEL, anschluss_tilgung=max(tilg, vg.mindesttilgung), bank=True,
            vfe_bis=min(bindung, _perioden_auf(max(plan_aus) * MONATE // p + kuendbar, p)),
            bereit_satz=vg.bereit_satz if neubau else NULL, bereit_frei=vg.bereit_frei))
    if bm.kfw > 0:
        # R-5.19 (KFW-297-298-MERKBLATT): tilgungsfreie Anlaufjahre, danach Annuitaet ueber die Restlaufzeit;
        # die Anlaufjahre zaehlen ab dem ersten Abruf (MA-040), in der anderen Lesart ab der Bezugsfertigkeit
        k, kk = kat.kfw, bm.kfw_kond
        plan_aus = aus_kfw or {0: bm.kfw}
        erster, letzter = min(plan_aus), max(plan_aus)
        start = erster                                   # MA-040: die Anlaufjahre zaehlen ab dem ersten Abruf
        tranchen.append(Tranche(
            "KfW-Darlehen", bm.kfw, "annuitaet_laufzeit", kk["zins"], laufzeit=kk["tilgungsperioden"],
            auszahlung=plan_aus, tilgungsbeginn=start + kk["tilgungsfrei"] * MONATE + 1, bindung=kk["bindung"],
            anschluss_zins=anschluss_bank, anschluss_regel=ANSCHLUSSREGEL, bank=False,
            vfe_bis=min(kk["bindung"], letzter + kuendbar), bereit_satz=k.bereit_satz, bereit_frei=k.bereit_frei))
        if letzter > k.abruffrist:
            reicht = letzter <= k.abruffrist + k.abruf_verlaengerung
            melde("M-49", "Das KfW-Darlehen wird nach dem Ende der Abruffrist abgerufen; "
                          + ("die Frist ist zu verlaengern" if reicht else "auch die laengste Verlaengerung reicht nicht"),
                  letzter_abruf=letzter, abruffrist=k.abruffrist, verlaengerung_reicht=reicht)
    if ein.uebernommen and not neubau:
        tranchen.append(_tranche_uebernommen(ein, vg, kat, p, st.anschlusszins_pp, zins_bank=zins_bank))
    if ein.foerderung and bm.foerderdarlehen > 0:
        tranchen.append(_tranche_foerder(ein.foerderung, bm.foerderdarlehen, aus_fd, bm.einbehalt_darlehen,
                                         fd_beginn, fd_laufzeit, bauende, p))
    # ---- Abschreibungsplan (R-7.3): linear, Buchung am Ende jedes Planjahres, zeitanteilig ab Nutzungsbeginn
    steuer = replace(ein.steuer, haltedauer=ein.haltedauer)
    boden = bm.boden
    basis = baukosten if neubau else gebaeude_ak
    # R-7.19: nach der Vermoegenssphaere. Ueberschusseinkuenfte (Privatperson, Verein, Stiftung): Einnahme im Jahr
    # des Zuflusses ist Regel (ESTR-21-5, BFH-IX-R-60-02); Verteilung ueber die Bindung nur auf Antrag (E-70, ESTG-11).
    # Betriebsvermoegen (MA-031): voreingestellt ueber die Bindung verteilt (ESTR-6-5, ESTH-5-6); "sofort" ist
    # Lesart des Hauses
    if steuer.status in UEBERSCHUSS:
        lesart = "verteilt" if ein.zuschuss_verteilung else "sofort"
    else:
        lesart = vg.ma031_zuschuss or "verteilt"
    steuer_ertrag = null()
    steuer_zus_entgelt = None                            # None: Entgelt auf den Zuschuss im Jahr der Zahlung
    rueck_im_gewinn = rueck_laufend = False
    e_z = bm.einbehalt_zuschuss
    rest_basis = basis
    rest_stau = stau_aktiv                               # aktivierte Massnahme: Abschreibung ab dem Jahr nach der Zahlung;
    for j in range(1, raster.n + 1):                     # eine Massnahme zum Stichtag (k = 0) also ab dem Planjahr 1
        ende = j * p
        monate = max(0, ende - max(bauende, (j - 1) * p))
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

    def verteile(betrag, rest_am_ende, von, bis):
        """Lineare Verteilung ueber die Perioden von+1 .. bis je Planjahr (R-7.15, R-7.19): Anteil je Planjahr
        kaufmaennisch gerundet; im Verkaufsjahr der ganze noch offene Betrag bis 'rest_am_ende'."""
        reihe, offen = null(), rest_am_ende
        for j in range(1, raster.n + 1):
            monate = max(0, min(j * p, bis) - max(von, (j - 1) * p))
            teil = offen if j == raster.n else min(offen, rd.geld(betrag * D(monate) / D(bis - von)))
            reihe[j * p] = teil
            offen -= teil
        return reihe

    if ein.foerderung and bm.zuschuss > 0:
        bindung_perioden = ein.foerderung.bindung_jahre * p      # Bindung beginnt mit der Bezugsfertigkeit
        verbleibend = max(0, bauende + bindung_perioden - N)
        rueck = restwert.zuschuss_rueckzahlung(bm.zuschuss, bindung_perioden, verbleibend, rd)
        if lesart == "sofort":                           # Einnahme im Jahr des Zuflusses; die Rueckzahlung mindert
            steuer_ertrag = list(zus)                    # das laufende Ergebnis des Verkaufsjahres
            rueck_laufend = True
        elif lesart == "verteilt":                       # Gegenleistung fuer die Bindung: Ertrag ueber die Bindung;
            # im Verkaufsjahr der Rest bis Zuschuss - Rueckzahlung; das Entgelt wird mit demselben Schluessel verteilt
            steuer_ertrag = verteile(bm.zuschuss, bm.zuschuss - rueck, bauende, bauende + bindung_perioden)
            steuer_zus_entgelt = verteile(e_z, e_z, bauende, bauende + bindung_perioden)
    vk = Verkauf(preis_brutto=preis_vk, kosten=restwert.verkaufskosten(preis_vk, vg.verkaufskostensatz, rd),
                 stau_abzug=stau_offen, foerder_rueckzahlung=rueck, buchwert=buchwert)
    # ---- einbehaltene Entgelte der Darlehen steuerlich (R-7.15): laufzeitbezogen ueber die Zinsbindung verteilt,
    # bei jedem Steuerstatus (ESTG-5, ESTG-11); andere Lesart MA-032: im Jahr der Zahlung
    einbehalten = bm.einbehalt_darlehen
    steuer_einbehalt = None
    if einbehalten > 0:
        start = min(aus_fd) if aus_fd else 0
        steuer_einbehalt = verteile(einbehalten, einbehalten, start, ein.foerderung.zinslos_jahre * p + bauende)
    pe = PlanEingabe(raster=raster, miete=miete, kosten=kost, erhaltung=erh, investition=inv, afa=afa,
                     tranchen=tranchen, steuer=steuer, einlagen=einl, entnahmen=null(), kk_zusatz=zwischen, h_kurz=vg.h_kurz,
                     kk_zins=vg.kk_zins, a_lang=vg.a_lang, kk_linie=vg.kk_linie, zuschuss=zus,
                     zuschuss_einbehalt=zus_einb, verkauf=vk, vfe_satz=vg.vfe_satz, rundung=rd,
                     steuer_einbehalt=steuer_einbehalt, steuer_ertrag=steuer_ertrag,
                     rueckzahlung_im_gewinn=rueck_im_gewinn, rueckzahlung_laufend=rueck_laufend,
                     steuer_zuschuss_entgelt=steuer_zus_entgelt, pacht=pacht,
                     anschaffung=boden + basis + stau_aktiv, afa_grundlage=basis + stau_aktiv)
    plan = rechne_plan(pe)
    alt = rechne_alternative(pe, plan.einlagen_netto, plan.entnahmen_netto)
    erg = Grobergebnis()
    erg.ein, erg.vg, erg.kat, erg.stress, erg.bemessung, erg.plan, erg.alt = ein, vg, kat, stress, bm, plan, alt
    erg.darlehen, erg.preis, erg.verkauf, erg.bauzeit, erg.ertrag = L, bm.preis, vk, bauende, er
    erg.darlehen_basis = darlehen_basis
    erg.miete_je_qm = er.miete_je_qm
    erg.baukosten, erg.mittelbedarf, erg.ek_soll = baukosten, mittelbedarf, ek_soll
    erg.abweichungen = abweichungen
    erg.zuschuss_lesart = lesart if bm.zuschuss > 0 else None
    erg.zielrendite = zielrendite(ein, vg)
    erg.auftrag = dict(kernversion=KERNVERSION, regelstand=REGELSTAND, rundung=rundung, raster=p)
    # ---- Proben (Kapitel 13)
    tol = NULL if rd.modus == "cent" else TOLERANZ_OHNE_RUNDUNG
    bef = pruefe_plan(plan, alt)
    invest_ende = bauende * p // MONATE
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
                         None if neubau else plan.zeilen[0]["guthaben"] + plan.zeilen[0]["kk"], tol)
    # P-12 Bemessungsprobe: die drei Grenzen unabhaengig nachgerechnet (R-13.3)
    gr = bm.bank
    bef += pruefe_bemessung(L, bm.wertansatz, vg.beleihungsquote, bm.im_beleihungsraum, bm.ertrag_nachhaltig,
                            vg.mindestdeckung, bm.kd_uebrige, bm.zins_kalk, bm.tilgung_kalk, bm.mittelbedarf, bm.uebrige,
                            bm.zuschuss, bm.ek_min, p, rd)
    # P-21 Tranchenprobe: jede Tranche traegt die Konditionen des Auftrags (Zins, Anschlusszins, Anschlussregel)
    soll = {"Bankdarlehen": dict(zins=ein.zins + st.zusage_pp,
                                 anschluss_zins=ein.zins + st.zusage_pp + vg.anschluss_aufschlag + st.anschlusszins_pp,
                                 anschluss_regel=ANSCHLUSSREGEL, bindung=ein.zinsbindung_jahre * p)}
    if bm.kfw > 0:
        soll["KfW-Darlehen"] = dict(zins=bm.kfw_kond["zins"], anschluss_zins=soll["Bankdarlehen"]["anschluss_zins"],
                                    bindung=bm.kfw_kond["bindung"])
    if ein.uebernommen and not neubau:
        ue = ein.uebernommen
        anschluss = (d(ue["anschluss_zins"]) if ue.get("anschluss_zins") is not None
                     else ein.zins + st.zusage_pp + vg.anschluss_aufschlag)
        soll["Uebernommenes Darlehen"] = dict(zins=d(ue["zins"]), anschluss_zins=anschluss + st.anschlusszins_pp,
                                              anschluss_regel=ANSCHLUSSREGEL)
    if ein.foerderung:
        soll["Foerderdarlehen"] = dict(zins=NULL, anschluss_zins=ein.foerderung.zins_danach)
    bef += pruefe_tranchen(tranchen, soll)
    if stau_betrag:
        bef += pruefe_stau(EINS if stau_zahlung else NULL, EINS if stau_offen else NULL)
    if bm.zuschuss:
        bef += pruefe_zuschuss(sum(zus), plan.zeilen[N]["foerder_rueck"], bm.zuschuss, bindung_perioden, verbleibend, rd, tol)
    bef += pruefe_index(er.indexreihen, rd, tol)
    erg.befunde = bef
    erg.herkunft, erg.verwendung = herkunft, verwendung
    erg.eigenkapital_investitionsphase = herkunft["eigenkapital"]
    spaeter = plan.reihe("nachschuss")[invest_ende + 1:]
    erg.fehlbetrag_verkauf = plan.zeilen[N]["nachschuss"]            # R-10.17: Verlust beim Verkauf
    erg.nachschuss_laufend = sum(spaeter, NULL) - erg.fehlbetrag_verkauf
    erg.eigenkapitalbedarf = sum(plan.einlagen_netto, NULL)          # R-11.6: Einlagen und alle Nachschuesse
    erg.zwischenfinanzierung = max(zwischen)                         # R-11.3: hoechster Stand
    erg.nachschuss_je_jahr = [None] + [plan.jahressumme("nachschuss", j) for j in range(1, raster.n + 1)]
    erg.gesperrt = bool(bef)
    if bef:                                              # R-13.1: verletzte Probe sperrt das Ergebnis
        erg.kennzahlen = None
        erg.meldungen = [dict(kennung="M-10", text="Kontrollsumme verletzt; das Ergebnis ist gesperrt. Es liegt kein "
                                                    "Eingabefehler vor; der Fehler ist gemeldet.", befunde=bef)]
        return erg
    erg.kennzahlen = kz = werte_aus(plan, alt, erg.zielrendite)
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
    if abweichungen:
        melde("M-35", "Abweichungen vom Hausstandard", liste=abweichungen)
    if steuer.status != BEFREIT:                         # R-7.1: bei der befreiten Koerperschaft genuegt M-44
        melde("M-37", "Die Steuer ist vereinfacht gerechnet: ohne Mindestbesteuerung, Zinsschranke, Sonderabschreibung und "
                      "Reinvestitionsruecklage"
                      + ("; ob die Voraussetzungen der erweiterten Kuerzung vorliegen, ist nicht geprueft" if steuer.erweiterte_kuerzung else "")
                      + ". Sie ersetzt keine steuerliche Pruefung des Einzelfalls.")
    if erg.fehlbetrag_verkauf > 0:
        melde("M-42", "Verlust beim Verkauf: Der Verkaufserloes deckt Abloesung, Steuer und Kosten nicht",
              betrag=erg.fehlbetrag_verkauf)
    if steuer.status == BEFREIT:
        melde("M-44", "Verkauf in befreiter Koerperschaft: Der Verkauf aus dem beguenstigten Bereich ist beguenstigtes Geschaeft "
                      "(BMF-VERMGEN-1991); das gilt nicht, wenn der Grundstueckshandel gewerblichen Charakter annimmt")
    if steuer.erweiterte_kuerzung and steuer.status in MIT_KENNZEICHEN and not steuer.kuerzung_bleibt_verkaufsjahr:
        melde("M-51", "Im Verkaufsjahr entfaellt die erweiterte Kuerzung ganz. Sie bleibt nur erhalten (E-69), wenn weiterer "
                      "Grundbesitz im Unternehmen verbleibt oder Besitz, Nutzen und Lasten zum 31.12., 23:59 Uhr, uebergehen")
    if "M-45" in plan.steuer.hinweise:
        melde("M-45", "Ein Verlustvortrag ueber dem Sockelbetrag wird in einem Jahr verrechnet; die Mindestbesteuerung ist nicht gerechnet")
    erg.meldungen = meldungen
    erg.modellannahmen = _modellannahmen(erg, tranchen, bm.einbehalt_darlehen + bm.einbehalt_zuschuss)
    if mit_blatt:
        for a in abweichungen:                           # R-3.2: Wirkung jeder Abweichung auf die Endwertdifferenz
            a["wirkung_endwertdifferenz"] = _wirkung_ewd(ein, vg_haus, kat, a, kz["endwertdifferenz"], stress, p, rundung)
        _blatt(erg, pe, rd)
    return erg


def _modellannahmen(erg, tranchen, einbehalten):
    """R-3.1: Kennungen der Modellannahmen, die in diesem Lauf gewirkt haben."""
    ein, vg, kat, plan, bm = erg.ein, erg.vg, erg.kat, erg.plan, erg.bemessung
    N = plan.e.raster.N
    r = plan.e.raster
    ma = {"MA-013"} if tranchen else set()
    if bm.uebrige > 0 or erg.darlehen > 0:
        ma.add("MA-026")
    if sum(1 for x in plan.einlagen_netto if x > 0) > 1 or sum(plan.entnahmen_netto) > 0:
        ma.add("MA-012")
    if ein.steuer.verlust == "sofort" or any(t["vv_zugang"] > 0 or t["vv_gew_zugang"] > 0 for t in plan.steuer.protokoll):
        ma.add("MA-016")
    if ein.foerderung:
        ma |= {"MA-002", "MA-003", "MA-004", "MA-005", "MA-017", "MA-021", "MA-031"}
    if ein.steuer.erweiterte_kuerzung:
        ma.add("MA-030")
    if einbehalten > 0 or (ein.steuer.status in UEBERSCHUSS and plan.zeilen[N]["vfe"] > 0):
        ma.add("MA-032")
    if plan.zeilen[N]["vfe"] > 0:
        ma.add("MA-033")
    if any(tr.bindung is not None and tr.bindung < N and not tr.foerder for tr in tranchen):
        ma.add("MA-034")
    if ein.steuer.status in PERSONENGESELLSCHAFT and plan.zeilen[N]["g_v"] != 0:
        ma.add("MA-036")
    vermietet = ein.art == "ankauf" and ein.wohnflaeche > ein.leere_flaeche
    if vermietet and ein.mietenhistorie is None:
        ma.add("MA-037")
    if vermietet and ein.ist_miete > ein.vergleichsmiete:
        ma.add("MA-038")
    letztes = r.startjahr + r.n - 1
    gebiet_k, gebiet_b = erg.ertrag.mietrecht.gebiet
    if ((gebiet_k and kat.kappung_ende_jahr is not None and kat.kappung_ende_jahr < letztes)
            or (gebiet_b and kat.bremse_ende_jahr is not None and kat.bremse_ende_jahr < letztes)):
        ma.add("MA-039")
    if bm.kfw > 0:
        ma.add("MA-040")
    if ein.steuer.status == KOERPERSCHAFT_OHNE_GEWST:
        ma.add("MA-041")
    return sorted(ma)


def _deckung_je_jahr(plan, erstes):
    r = plan.e.raster
    decken = [(schuldendienstdeckung(plan, j)[0], j) for j in range(erstes, r.n + 1)]
    return [x for x in decken if x[0] is not None]


def _erste_rate(tr, p, rd):
    """Kapitaldienst der ersten Tilgungsperiode einer Tranche (Zins, Tilgung, Beitrag), aus einer Kopie gerechnet."""
    t = _kopie([tr])[0]
    z = None
    for u in range(0, t.tilgungsbeginn + 1):
        z = t.periode(u, p, rd)
    return z["zins"] + z["tilgung"] + z["beitrag"]


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
    # R-10.14: Deckung im ersten Jahr bei voller Tilgung, wenn eine Tranche in diesem Jahr noch tilgungsfrei laeuft
    erg.dscr_vj_voll = None
    spaet = [tr for tr in plan.e.tranchen if tr.art != "endfaellig" and tr.tilgungsbeginn > ab]
    if spaet and erg.kd_vj:
        kd_voll = erg.kd_vj + sum(p * _erste_rate(tr, p, rd) - erg.kd_je_darlehen.get(tr.name, NULL) for tr in spaet)
        erg.dscr_vj_voll = erg.reinertrag_vj / kd_voll if kd_voll > 0 else None
    # R-10.24: Deckung und Reserve nach Bemessungskonditionen (Bankrechnung): nachhaltiger Reinertrag gegen den
    # kalkulatorischen Kapitaldienst aller Darlehen
    kd_bemessung = bm.kd_uebrige + kapitaldienst_kalkulatorisch(erg.darlehen, bm.zins_kalk, bm.tilgung_kalk, p, rd)
    erg.kd_bemessung = kd_bemessung
    erg.deckung_bemessung = bm.ertrag_nachhaltig / kd_bemessung if kd_bemessung > 0 else None
    erg.reserve_bemessung = bm.ertrag_nachhaltig - vg.mindestdeckung * kd_bemessung
    sollmiete_vj = sum(er.soll(u) for u in vj)
    erg.sollmiete_vj = sollmiete_vj
    erg.anteil_miete_deckung_eins, erg.ausfall_deckung_eins = deckungsgrenzen(
        sollmiete_vj, sum(z[u]["miete"] for u in vj), sum(z[u]["kosten"] for u in vj), erg.kd_vj)
    # kleinste Deckung ab dem ersten vollen Planjahr der Vermietung (R-10.14)
    erstes = (ab - 1 + p - 1) // p + 1
    decken = _deckung_je_jahr(plan, erstes)
    erg.deckung_je_jahr = decken
    erg.deckung_min, erg.deckung_min_jahr = min(decken) if decken else (None, None)
    erg.deckung_nach_bindung = {}
    for tr in plan.e.tranchen:                           # auch das Ende der zinslosen Zeit des Foerderdarlehens
        if tr.bindung is not None and tr.bindung < N:
            j = r.planjahr(tr.bindung + 1)
            erg.deckung_nach_bindung[tr.name] = (j, schuldendienstdeckung(plan, j)[0])
    # R-10.14 (MA-034): kleinste Deckung zusaetzlich nach der Anschlussregel, die die niedrigste Deckung ergibt
    erg.deckung_min_anschluss = None
    anschluss = [tr for tr in plan.e.tranchen if tr.art == "annuitaet_prozent" and tr.bindung is not None
                 and tr.tilgungsbeginn <= tr.bindung < N]
    if anschluss and decken:
        je_regel = {ANSCHLUSSREGEL: (erg.deckung_min, erg.deckung_min_jahr)}
        for regel in ANSCHLUSSREGELN:
            if regel not in je_regel:
                d2 = _deckung_je_jahr(rechne_plan(replace(pe, tranchen=_kopie(pe.tranchen, anschluss_regel=regel))), erstes)
                if d2:
                    je_regel[regel] = min(d2)
        regel = min(je_regel, key=lambda x: (je_regel[x][0], x != ANSCHLUSSREGEL, ANSCHLUSSREGELN.index(x)))
        erg.deckung_min_anschluss = (je_regel[regel][0], je_regel[regel][1], regel)
    klein, klein_jahr, klein_regel = erg.deckung_min, erg.deckung_min_jahr, ANSCHLUSSREGEL
    if erg.deckung_min_anschluss and erg.deckung_min_anschluss[0] < klein:
        klein, klein_jahr, klein_regel = erg.deckung_min_anschluss
    if klein is not None and klein < vg.mindestdeckung:
        kennung = "M-39" if klein < 1 else "M-38"
        text = ("Die Schuldendienstdeckung faellt unter 1: Der Reinertrag deckt den Kapitaldienst nicht" if kennung == "M-39"
                else "Die Schuldendienstdeckung faellt unter die Mindestdeckung")
        erg.meldungen.append(dict(kennung=kennung, text=text, jahr=klein_jahr, deckung=klein, anschlussregel=klein_regel))
    # Darlehen zu Kaufpreis oder Gesamtkosten (R-10.15) und Restschuld zum Wert am Ende der Zinsbindung
    nenner = (bm.preis + bm.enk + bm.baukosten) if neubau else bm.preis
    erg.darlehen_zu_wert = (erg.darlehen + bm.uebrige) / nenner if nenner > 0 else None
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
    # R-11.7: Faktor auf die Ist-Jahresnettokaltmiete des Exposes (ohne Leerstandsabschlag, ohne sonstige Ertraege)
    erg.ist_jahresmiete = NULL if neubau else MONATE * ein.ist_miete * (ein.wohnflaeche - ein.leere_flaeche)
    erg.faktor_ist = bm.preis / erg.ist_jahresmiete if erg.ist_jahresmiete > 0 else None
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
    # R-10.25 (H-20): Warnschwellen
    erg.warnungen = []
    if vg.warnschwelle_restwertanteil is not None and erg.restwertanteil is not None and erg.restwertanteil > vg.warnschwelle_restwertanteil:
        erg.warnungen.append(("Restwertanteil", erg.restwertanteil, vg.warnschwelle_restwertanteil))
    if (vg.warnschwelle_faktorabstand is not None and erg.einstiegsfaktor is not None
            and erg.ausstiegsfaktor - erg.einstiegsfaktor > vg.warnschwelle_faktorabstand):
        erg.warnungen.append(("Ausstiegsfaktor ueber Einstiegsfaktor", erg.ausstiegsfaktor - erg.einstiegsfaktor,
                              vg.warnschwelle_faktorabstand))
    for name, wert, schwelle in erg.warnungen:
        erg.meldungen.append(dict(kennung="M-48", text=f"Warnschwelle ueberschritten: {name}", kennzahl=name, wert=wert, schwelle=schwelle))
    # R-11.14 (NBANK-RL-MIETWOHNRAUM-2026 Nr. 4.1): die Miete deckt Finanzierung und Bewirtschaftung auf Dauer
    if ein.foerderung is not None:
        knapp = [(n_, w_) for n_, w_ in (("Deckung nach Bemessung", erg.deckung_bemessung),
                                         ("kleinste Schuldendienstdeckung", erg.deckung_min))
                 if w_ is not None and w_ < 1]
        if knapp:
            erg.meldungen.append(dict(kennung="M-50", text="Die Miete deckt Finanzierungs- und Bewirtschaftungskosten "
                                      "nicht auf Dauer; das ist Voraussetzung der Foerderung: "
                                      + ", ".join(n_ for n_, _ in knapp), werte=knapp))
    # R-11.15: Zusatzangaben, wenn der Ertrag kein Bankdarlehen traegt
    erg.ohne_bankdarlehen = None
    if bm.bank["meldung"] == "M-21":
        c = max(bm.bank["c"], NULL)
        kd_c = kapitaldienst_kalkulatorisch(c, bm.zins_kalk, bm.tilgung_kalk, p, rd)
        noetig = vg.mindestdeckung * (bm.kd_uebrige + kd_c)
        erreicht = [j for x, j in decken if x >= vg.mindestdeckung]
        gebunden = ein.foerderung is not None or ein.gebunden_anteil == 1
        erg.ohne_bankdarlehen = dict(
            deckung_uebrige=bm.ertrag_nachhaltig / bm.kd_uebrige if bm.kd_uebrige > 0 else None,
            reserve=kapitaldienstreserve(bm.ertrag_nachhaltig, bm.kd_uebrige, vg.mindestdeckung),
            restfinanzierung=c, reinertrag_noetig=noetig,
            # bei gebundener Miete ist die noetige Miete keine Handlungsgroesse und entfaellt
            miete_noetig=None if gebunden else _noetige_miete(erg, c, rd),
            mindestdeckung_moeglich=bm.ertrag_nachhaltig / (bm.kd_uebrige + kd_c) if (bm.kd_uebrige + kd_c) > 0 else None,
            freier_beleihungsraum=bm.bank["a"] - c,
            planjahr_mindestdeckung=min(erreicht) if erreicht else None,
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


def _kopie(tranchen, anschluss_regel=None):
    neu = []
    for t in tranchen:
        neu.append(Tranche(t.name, t.betrag, t.art, t.zins, tilgungssatz=t.tilgungssatz, laufzeit=t.laufzeit,
                           auszahlung=dict(t.auszahlung), einbehalt=t.einbehalt, tilgungsbeginn=t.tilgungsbeginn,
                           bindung=t.bindung, anschluss_zins=t.anschluss_zins,
                           anschluss_regel=anschluss_regel or t.anschluss_regel,
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
        return dict(status="eingabe", meldungen=[dict(kennung=m.kennung, text=m.text, **m.angaben)], ergebnis=None)
    return dict(status="gesperrt" if erg.gesperrt else "ergebnis", meldungen=erg.meldungen, ergebnis=erg)


# ------------------------------------------------------------------------------------------------ R-11.10
def zielwertsuche(f, unten, oben, schritt, raster, zusatz=()):
    """R-11.10: sucht alle Stellen im Bereich [unten; oben], an denen f das Vorzeichen wechselt.

    Gesucht wird auf dem Gitter der Aufloesung 'schritt' (ganzzahlige Bisektion, deterministisch). Der Bereich hat
    n = abrunden((oben - unten) / schritt) Gitterschritte; Stuetzstelle i (i = 0 .. raster) ist der Gitterwert mit
    dem Index (i x n) div raster, doppelte entfallen; 'zusatz' sind weitere Gitterindizes (bekannte Sprungstellen).
    f(x) >= 0 heisst "Ziel erreicht". Rueckgabe: dict(status, loesungen, ...). Jede Loesung ist der Gitterwert am
    Wechsel, an dem das Ziel erreicht ist: bei fallendem Wechsel der letzte erreichte, bei steigendem der erste.
    """
    unten, oben, schritt = d(unten), d(oben), d(schritt)
    n = int((oben - unten) / schritt)
    if n < 1:
        raise Meldung("M-31", "Suchbereich leer")
    punkte = sorted({i * n // raster for i in range(raster + 1)} | {int(i) for i in zusatz if 0 <= i <= n})
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
                rasterweite=(oben - unten) / raster, auswertungen=len(cache), g=g, wert=wert, punkte=punkte)


def _zielgroesse(erg, zielgroesse):
    """R-11.5, R-11.10: Zielfunktion eines Laufs. "rendite": Endwertueberschuss (R-10.9); er hat dasselbe
    Vorzeichen wie Rendite minus Zielrendite und ist auch ohne Einlage definiert."""
    if erg.gesperrt:
        raise Meldung("M-10", "Kontrollsumme in einem Suchschritt verletzt; die Suche endet ohne Ergebnis",
                      dict(befunde=erg.befunde, preis=erg.preis))
    kz = erg.kennzahlen
    return kz["endwertdifferenz"] if zielgroesse == "endwertdifferenz" else kz["endwertueberschuss"]


def preisgrenze(f, unten, oben, raster, fenster, zusatz=()):
    """R-11.4, R-11.5: groesster ganzzahliger Preis x in [unten; oben], fuer den f(x) >= 0 gilt und f an jeder
    Stuetzstelle und in jedem Fenster unter x ebenfalls. Rueckgabe: (x, Status, mehrfach); Status "eine",
    "verfehlt" (f(unten) < 0) oder "erreicht" (an allen Stuetzstellen bis oben + 1 erreicht).
    zusatz: Preise, die zusaetzlich Stuetzstellen sind (bekannte Sprungstellen des Ziels)."""
    if f(unten) < 0:
        return None, "verfehlt", False
    if oben + 1 - unten < 1:
        return (unten, "eine", False) if f(unten + 1) < 0 else (None, "erreicht", False)
    s = zielwertsuche(f, unten, oben + 1, 1, raster, [int(x) - unten for x in zusatz])
    fallend = [l for l in s["loesungen"] if l["richtung"] == "fallend"]
    if not fallend:
        return None, "erreicht", False
    x = int(fallend[0]["wert"])
    mehrfach = len(s["loesungen"]) > 1
    # Nachsuche: Das Ergebnis selbst und jeder Preis im Fenster darunter muessen das Ziel erreichen. Verfehlt es
    # einer, rueckt die Grenze unter den kleinsten verfehlenden Preis; dort beginnt die Nachsuche neu.
    weiter = True
    while weiter:
        weiter = False
        while x > unten and f(x) < 0:
            x, mehrfach = x - 1, True
        for y in range(x - 1, max(unten, x - fenster) - 1, -1):
            if f(y) < 0:
                x, mehrfach, weiter = y - 1, True, True
                break
    # ... und oberhalb der Grenze darf im Fenster kein Preis das Ziel wieder erreichen (sonst M-34)
    if not mehrfach:
        mehrfach = any(f(y) >= 0 for y in range(x + 2, min(oben + 1, x + fenster) + 1))
    return x, "eine", mehrfach


def _schwellenpreise(ein, vg, kat, raster, rd, unten, oben):
    """R-11.5: Sprungstelle des Ziels aus der 15-%-Regel (R-6.16): der groesste Preis, bei dem die
    Erhaltungsmassnahme der ersten Jahre noch aktiviert wird, und der Preis einen Euro darueber. Beide werden
    Stuetzstellen der Preissuche. Die Schwelle waechst mit dem Preis; gesucht wird ganzzahlig."""
    if ein.art != "ankauf" or not ein.stau_betrag or ein.stau_jahr > min(kat.ahk_jahre, raster.n):
        return []
    netto = {}
    for stress in (False, True):
        rel = vg.stress.stau_rel if stress else NULL
        bpi = ertrag.indexreihe(raster.n + 2, vg.baupreissteigerung, rd)
        netto[stress] = rd.geld(rd.geld(ein.stau_betrag * (EINS + rel)) * bpi[ein.stau_jahr + 1]) / (EINS + kat.ust_satz)

    def aktiviert(x, betrag):
        enk = rd.geld(D(x) * ein.enk_satz)
        anteil = _bodenanteil(ein, vg, x)
        gebaeude = D(x) + enk - rd.geld((D(x) + enk) * anteil)
        return betrag > kat.ahk_quote * gebaeude

    punkte = []
    for betrag in netto.values():
        if aktiviert(unten, betrag) and not aktiviert(oben, betrag):
            lo, hi = unten, oben
            while hi - lo > 1:
                mid = (lo + hi) // 2
                lo, hi = (mid, hi) if aktiviert(mid, betrag) else (lo, mid)
            punkte += [lo, hi]
    return punkte


def tragbarer_preis(ein: Grobeingabe, vg: Vorgaben, kat: Katalog, stress=False, p=MONATE):
    """R-11.4 bis R-11.7: hoechster tragbarer Kauf- oder Grundstueckspreis in vollen Euro.

    Der tragbare Preis ist der groesste Preis, bis zu dem die Zielrendite fuer jeden kleineren Preis des
    Suchbereichs erreicht ist. Zweite, freiwillige Grenze: das verfuegbare Eigenkapital gegen Einlagen und alle
    Nachschuesse. Jede Meldung eines Suchschritts beendet die Suche mit dieser Meldung und ohne Preis; die Suche
    endet nie mit einem Rechenfehler.
    """
    try:
        pruefe_begruendungen(ein, vg, kat, p, mit_preis=True)
    except Meldung as m:
        return dict(renditegrenze=None, ek_grenze=None, preis=None, bindend=None, meldung=m.kennung, text=m.text,
                    angaben=m.angaben, meldungen=[], unten=None, oben=None, ergebnis=None)
    return _tragbarer_preis(ein, vg, kat, stress, p)


def _tragbarer_preis(ein, vg, kat, stress=False, p=MONATE):
    erg = dict(renditegrenze=None, ek_grenze=None, preis=None, bindend=None, meldung=None, meldungen=[],
               unten=None, oben=None, ergebnis=None)
    try:
        vg, abweichungen = vorgaben_im_vorhaben(vg, ein)
        pruefe_eingaben(ein, vg, kat, p)
        ein = replace(ein, abweichungen=None)
        erg["abweichungen"] = abweichungen
        rd = Rundung("cent")
        raster = Raster(p=p, n=ein.haltedauer, startjahr=ein.stichtag_jahr)
        bauende = (_vorlauf(ein, vg) + ein.bauzeit_monate) if ein.art == "neubau" else 0
        er = _ertragsreihen(ein, vg, kat, raster, rd, False, bauende)
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
                bemesse(ein, vg, kat, raster, rd, oben)  # loest M-22 mit den Angaben der Meldung aus
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

        sprung = _schwellenpreise(ein, vg, kat, raster, rd, unten, oben)
        x, status, mehrfach_r = preisgrenze(lambda v: lauf(v)[0], unten, oben, vg.suchraster, vg.nachsuchfenster, sprung)
        if x is None:
            erg["meldung"] = "M-32" if status == "verfehlt" else "M-33"
            if status == "verfehlt":                     # R-14.13: Rendite beim kleinsten zulaessigen Preis
                erg["ergebnis_unten"] = rechne_grob(ein, vg, kat, preis=unten, stress=stress, p=p, geprueft=True)
            return erg
        erg["renditegrenze"] = x
        preis, bindend, mehrfach = x, "Rendite", mehrfach_r
        if ein.verfuegbares_ek is not None:
            y, status, mehrfach_e = preisgrenze(lambda v: ein.verfuegbares_ek - lauf(v)[2], unten, oben, vg.suchraster,
                                                vg.nachsuchfenster, sprung)
            if status == "verfehlt":
                erg["ek_grenze"], erg["preis"], erg["bindend"], erg["meldung"] = 0, None, "Eigenkapital", "M-46"
                return erg
            if y is not None:
                erg["ek_grenze"] = y
                if y < preis:
                    preis, bindend, mehrfach = y, "Eigenkapital", mehrfach_e
        if lauf(preis)[1] == 0:                          # R-11.5: ohne eingesetztes Eigenkapital kein tragbarer Preis,
            erg["meldung"] = "M-41"                      # gleich welche Grenze bindet
            erg["bindend"] = bindend
            erg["nebenangabe"] = preis
            return erg
        erg["preis"], erg["bindend"] = preis, bindend
        if mehrfach:                                     # M-34 nur aus der bindenden Grenze
            erg["meldungen"].append("M-34")
        erg["meldung"] = "M-34" if mehrfach else None
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
        # R-11.7: Angaben zum tragbaren Preis: Faktor nach strukturellem Leerstand und Faktor auf die Ist-Miete
        jm = e.jahresmiete_einstieg
        erg["faktor"] = preis / jm if (ein.art == "ankauf" and jm > 0) else None
        erg["faktor_ist"] = e.faktor_ist
        erg["angebotsfaktor_ist"] = (ein.angebotspreis / e.ist_jahresmiete
                                     if (ein.angebotspreis is not None and e.ist_jahresmiete > 0) else None)
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
    gelten als verfehlt und werden gezaehlt; enden alle ausgewerteten Gitterwerte mit derselben Meldung, ist sie
    das Ergebnis. Gitterwerte ohne eingesetztes Eigenkapital werden gezaehlt; eine Loesung ohne eingesetztes
    Eigenkapital traegt M-41. Eine verletzte Probe beendet die Suche mit M-10.
    """
    if feld not in SUCHBARE_EINGABEN:
        raise Meldung("M-30", f"Eingabe '{feld}' ist fuer die Zielwertsuche nicht zugelassen")
    unzulaessig, ohne_ek, nenner = [], [], {}

    def f(x):
        try:
            erg = rechne_grob(replace(ein, **{feld: x}), vg, kat, stress=stress, p=p, mit_blatt=False)
        except Meldung as m:
            if m.kennung == "M-10":
                raise
            unzulaessig.append((x, m.kennung))
            return -EINS
        wert = _zielgroesse(erg, zielgroesse)
        nenner[x] = erg.kennzahlen["nenner"]
        if nenner[x] == 0:
            ohne_ek.append(x)
        return wert

    s = zielwertsuche(f, unten, oben, schritt, raster or vg.suchraster)
    s["unzulaessig"], s["ohne_eigenkapital"] = unzulaessig, ohne_ek
    s["meldungen"] = []
    kennungen = {k for _, k in unzulaessig}
    if len(unzulaessig) == s["auswertungen"] and len(kennungen) == 1:
        s["status"] = f"keine Suche: jeder Gitterwert endet mit {kennungen.pop()}"
    for l in s["loesungen"]:
        l["ohne_eigenkapital"] = nenner.get(l["wert"]) == 0
    if any(l["ohne_eigenkapital"] for l in s["loesungen"]) or (ohne_ek and not s["loesungen"]):
        s["meldungen"].append("M-41")
    return s


# R-11.9: gekennzeichnete Eingaben. Nicht zugelassen sind Auswahlfelder (Steuerstatus), ganzzahlige
# Zeitgroessen (Haltedauer, Zinsbindung, Bauzeit) und die Vorgaben des Hauses.
SUCHBARE_EINGABEN = ("kaufpreis", "grundstueckspreis", "markt_miete", "vergleichsmiete", "ist_miete", "stau_betrag",
                     "verkaufsfaktor", "zins", "kostenkennwert")


def haltedauer_tabelle(ein, vg, kat, von, bis, p=MONATE):
    """R-11.13: statt einer Zielwertsuche auf die Haltedauer eine Tabelle je Jahr. Die Haltedauer der Zeile ist
    dabei keine Abweichung von ihrer Voreinstellung; jede Meldung steht in ihrer Zeile."""
    zeilen = []
    for n in range(von, bis + 1):
        try:
            e = rechne_grob(replace(ein, haltedauer=n), vg, kat, p=p, mit_blatt=False, _begruendung=False)
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
    ("Kapitaldienstreserve laut Finanzplan", lambda e: e.kapitaldienstreserve),
    ("Eigenkapital der Investitionsphase", lambda e: e.eigenkapital_investitionsphase),
    ("laufender Nachschussbedarf", lambda e: e.nachschuss_laufend), ("Fehlbetrag beim Verkauf", lambda e: e.fehlbetrag_verkauf),
    # ergaenzt nach Pruefrunde 2: die uebrigen Groessen des Blatts (R-11.12)
    ("bindende Grenze des Bankdarlehens", lambda e: e.bemessung.bank["bindend"]),
    ("Deckung im ersten Jahr bei voller Tilgung", lambda e: e.dscr_vj_voll),
    ("Planjahr der kleinsten Deckung", lambda e: e.deckung_min_jahr),
    ("kleinste Deckung nach der unguenstigsten Anschlussregel", lambda e: e.deckung_min_anschluss),
    ("Deckung nach jeder Zinsbindung", lambda e: e.deckung_nach_bindung),
    ("Deckung nach Bemessung", lambda e: e.deckung_bemessung), ("Reserve nach Bemessung", lambda e: e.reserve_bemessung),
    ("Mietanteil und Mietausfall bei Deckung 1", lambda e: (e.anteil_miete_deckung_eins, e.ausfall_deckung_eins)),
    ("Kapitaldienst je Darlehen", lambda e: e.kd_je_darlehen),
    ("Nachschuesse je Planjahr", lambda e: e.nachschuss_je_jahr[1:]),
    ("Angaben ohne Bankdarlehen", lambda e: e.ohne_bankdarlehen),
    ("Meldungen", lambda e: sorted(m["kennung"] for m in e.meldungen)),
    ("Modellannahmen, die gewirkt haben", lambda e: e.modellannahmen),
)
PREISGROESSEN = ("preis", "bindend", "meldung", "faktor", "faktor_ist", "preis_je_qm", "preis_je_qm_grundstueck", "abstand_angebot")

# R-3.1: Herkunft der Steuerwerte (Katalog, Eingabe des Anwenders, Lesart einer Modellannahme)
HERKUNFT_STEUER = {
    "status": "E", "verlust": "H", "erweiterte_kuerzung": "E", "est_satz": "E", "anteil_natuerliche": "E",
    "kuerzung_bleibt_verkaufsjahr": "E", "aufgabegewinn": "MA", "haltedauer": "E",
    "satz": "E", "verkaufsgewinn_pflichtig": "E",
}


def _wert_vergleich(wert, jahre):
    """Macht Katalogwerte vergleichbar: ein Satz je Kalenderjahr wird ueber die Jahre des Plans ausgewertet."""
    if callable(wert):
        return tuple(wert(j) for j in jahre)
    return wert


def auftragswerte(e: Grobergebnis):
    """R-3.1: jeder Wert des Auftrags mit seiner Herkunft: (Herkunft, Name, Wert); Herkunft "E" Eingabe,
    "H" Vorgabe des Hauses, "KAT" Katalogwert, "MA" Lesart einer Modellannahme."""
    r = e.plan.e.raster
    jahre = range(r.startjahr, r.startjahr + r.n)
    werte = []
    for f_ in fields(e.ein):
        if f_.name not in ("steuer", "foerderung"):
            werte.append(("E", f_.name, getattr(e.ein, f_.name)))
    for f_ in fields(e.vg):
        werte.append(("MA" if f_.name.startswith("ma0") else "H", f_.name, getattr(e.vg, f_.name)))
    for f_ in fields(e.kat):
        werte.append(("KAT", f_.name, getattr(e.kat, f_.name)))
    for f_ in fields(e.ein.steuer):
        werte.append((HERKUNFT_STEUER.get(f_.name, "KAT"), "steuer." + f_.name, _wert_vergleich(getattr(e.ein.steuer, f_.name), jahre)))
    if e.ein.foerderung is not None:
        for f_ in fields(e.ein.foerderung):
            werte.append(("KAT", "foerderung." + f_.name, getattr(e.ein.foerderung, f_.name)))
    return werte


def vergleiche(a, b):
    """R-11.11: Vergleich zweier Fassungen ueber das ganze Blatt: jede Groesse mit Wert A, Wert B und Differenz
    B - A; dazu die abweichenden Werte des Auftrags mit ihrer Herkunft (Eingabe, Vorgabe, Katalog, Lesart) und
    die Versionen des Kerns. a und b sind je ein Grobergebnis (eine Spalte) oder ein Blatt
    dict(basis=..., stress=..., preis=..., preis_stress=...) aus Basisfall, Stressfall und den tragbaren Preisen."""
    blatt_a = a if isinstance(a, dict) else dict(basis=a)
    blatt_b = b if isinstance(b, dict) else dict(basis=b)
    for x in (blatt_a, blatt_b):
        if any(isinstance(v, Grobergebnis) and v.gesperrt for v in x.values()) or \
                any(isinstance(v, dict) and v.get("meldung") == "M-10" for v in x.values()):
            raise Meldung("M-10", "Vergleich nur zwischen Fassungen, die alle Kontrollsummen bestehen")
    zeilen = []

    def zeile(name, fa, fb):
        zahl = lambda v: isinstance(v, (D, int)) and not isinstance(v, bool)
        zeilen.append((name, fa, fb, fb - fa if (zahl(fa) and zahl(fb)) else None))

    for spalte, titel in (("basis", ""), ("stress", "Stressfall: ")):
        if spalte in blatt_a and spalte in blatt_b:
            for name, f in BLATTGROESSEN:
                zeile(titel + name, f(blatt_a[spalte]), f(blatt_b[spalte]))
    for spalte, titel in (("preis", "tragbarer Preis: "), ("preis_stress", "tragbarer Preis im Stressfall: ")):
        if spalte in blatt_a and spalte in blatt_b:
            for name in PREISGROESSEN:
                zeile(titel + name, blatt_a[spalte].get(name), blatt_b[spalte].get(name))
    ea, eb = blatt_a["basis"], blatt_b["basis"]
    wa, wb = auftragswerte(ea), {(h, n): w for h, n, w in auftragswerte(eb)}
    abweichend = [(h, n, w, wb.get((h, n))) for h, n, w in wa if w != wb.get((h, n))]
    abweichend += [(h, n, None, w) for (h, n), w in wb.items() if (h, n) not in {(h_, n_) for h_, n_, _ in wa}]
    versionen = (ea.auftrag["kernversion"], eb.auftrag["kernversion"])
    return dict(zeilen=zeilen, abweichende_werte=abweichend, kernversionen=versionen,
                versionsgleich=versionen[0] == versionen[1])


def darstellung(werte, einheit=D(1)):
    """R-12.7: Darstellung einer Spalte in vollen Euro. Die Summe wird aus den ungerundeten Werten gebildet;
    addieren die gerundeten Zeilen nicht zur gerundeten Summe, wird die Rundungsdifferenz ausgewiesen."""
    from zahlen import kaufm
    zeilen = [kaufm(x, str(einheit)) for x in werte]
    summe = kaufm(sum(werte, NULL), str(einheit))
    return dict(zeilen=zeilen, summe=summe, rundungsdifferenz=summe - sum(zeilen, NULL))
