"""Angenommener Katalog- und Vorgabenstand fuer die Referenzfaelle.

Kein Bestandteil des Rechenkerns: Die Werte stehen hier, weil der Rechenkern keinen Satz und keine Schwelle
als Festwert kennt (R-3.1). Steuerwerte nach dem Stand des Rechercheberichts, Anhang B.3 (Kennungen des
Quellenkatasters in Klammern); Vorgaben des Hauses sind Annahmen der Beispiele, die der Auftraggeber noch
freigibt (TASKS.md, "Vorgaben des Hauses").
"""
from decimal import Decimal as D
from dataclasses import replace
from steuer import (Steuerparameter, KOERPERSCHAFT, GEWERBLICHE_PG, EINZELUNTERNEHMEN, PRIVAT, BEFREIT)
from grobkalkulation import Vorgaben, Stress, Grobeingabe, Foerderung


def kst_satz(jahr):
    """Koerperschaftsteuersatz je Kalenderjahr (KSTG-23), Stand Bericht B.3."""
    staffel = {2028: "0.14", 2029: "0.13", 2030: "0.12", 2031: "0.11"}
    if jahr <= 2027:
        return D("0.15")
    return D(staffel.get(jahr, "0.10"))


SOLI = D("0.055")                 # SOLZG-4
MESSZAHL = D("0.035")             # GEWSTG-11
HEBESATZ = D("4.00")              # Annahme: 400 % (GEWSTG-16)
FREIBETRAG = D("24500")           # GEWSTG-11, natuerliche Personen und Personengesellschaften
ANRECHNUNGSFAKTOR = D("4")        # ESTG-35
FRIST_PRIVATVERKAUF = 10          # ESTG-23
EST_SATZ = D("0.42")              # Annahme: eingegebener Steuersatz
ZINS_SATZ_PRIVAT = D("0.26375")   # Annahme: Satz auf Zinsertraege (Kataster-Luecke, Vorschlagsliste)


def steuer(status, **kw):
    basis = dict(status=status, kst_satz=kst_satz, soli_satz=SOLI, messzahl=MESSZAHL, hebesatz=HEBESATZ,
                 est_satz=EST_SATZ, anrechnungsfaktor=ANRECHNUNGSFAKTOR, frist_privatverkauf=FRIST_PRIVATVERKAUF)
    if status in (GEWERBLICHE_PG, EINZELUNTERNEHMEN):
        basis["freibetrag"] = FREIBETRAG
    if status == PRIVAT:
        basis["zins_satz"] = ZINS_SATZ_PRIVAT
    basis.update(kw)
    return Steuerparameter(**basis)


STRESS = Stress(anschlusszins_pp=D("0.01"), mietausfall_pp=D("0.02"), verkaufsfaktor_rel=D("0.10"),
                mietsteigerung_pp=D("0.005"), instandhaltung_rel=D("0.10"), baukosten_rel=D("0.05"),
                bauzeit_monate=3)

VORGABEN = Vorgaben(
    zielrendite=D("0.05"), beleihungsquote=D("0.65"), mindestdeckung=D("1.2"), mindesttilgung=D("0.02"),
    anschluss_aufschlag=D("0.01"), h_kurz=D("0.02"), kk_zins=D("0.08"), mietsteigerung=D("0.02"),
    kostensteigerung=D("0.02"), baupreissteigerung=D("0.03"), mietausfall=D("0.02"),
    verkaufskostensatz=D("0.015"), verwaltung_je_einheit=D("350"), instandhaltung_je_qm=D("14"),
    betriebskosten_je_qm=D("2"), kappung=D("0.15"), afa_satz=D("0.02"), kk_linie=D(0), vfe_satz=D("0.01"),
    stress=STRESS)

# Referenzobjekt Ankauf: 20 Wohnungen, 1.320 m2, Ist-Miete 8,50 Euro/m2 (Jahresmiete 134.640 Euro)
ANKAUF = Grobeingabe(
    art="ankauf", steuer=steuer(KOERPERSCHAFT), zins=D("0.04"), zinsbindung_jahre=10, verkaufsfaktor=D("18"),
    haltedauer=12, wohnflaeche=D("1320"), einheiten=20, startjahr=2027, kaufpreis=D("2400000"),
    enk_satz=D("0.10"), bodenanteil=D("0.25"), ist_miete=D("8.50"), markt_miete=D("9.20"), anpassungsdauer=4,
    stau_betrag=D("120000"), stau_jahr=2, stau_art="erhaltung", co2_je_qm=D("0.60"), co2_steigerung=D("0.05"))

# Referenzobjekt Neubau: 30 Wohnungen, 2.000 m2 Wohnflaeche, 2.600 m2 Brutto-Grundflaeche
NEUBAU = Grobeingabe(
    art="neubau", steuer=steuer(KOERPERSCHAFT), zins=D("0.04"), zinsbindung_jahre=10, verkaufsfaktor=D("24"),
    haltedauer=15, wohnflaeche=D("2000"), einheiten=30, startjahr=2027, grundstueckspreis=D("1200000"),
    grundstuecksflaeche=D("2500"), bgf=D("2600"), kostenkennwert=D("2900"), bauzeit_monate=18,
    enk_satz=D("0.08"), markt_miete=D("16.50"), co2_je_qm=D(0), co2_steigerung=D(0))

# Grobfoerderung: Werte nach Bericht Anhang C.1 fuer Einkommensgruppe B und Mietenstufe IV bis VII
# (NBANK-RL-MIETWOHNRAUM-2026; MA-002, MA-003, MA-004); Annahmen des Beispiels: Zins danach 5 %, Bodenrichtwert 400 Euro/m2
FOERDERUNG_B = Foerderung(
    darlehensquote=D("0.60"), zuschussquote=D("0.20"), eigenmittelquote=D("0.20"),
    bemessungsgrenze_je_qm=D("5460"), bodenrichtwert=D("400"), eingangsmiete=D("8.20"), steigerung=D("0.0615"),
    fest_jahre=3, schritt_jahre=3, bindung_jahre=35, vkb_satz=D("0.005"), entgelt_darlehen=D("0.01"),
    entgelt_zuschuss=D("0.0075"), tilgung_jahre=42, zinslos_jahre=35, zins_danach=D("0.05"))

VORGABEN_NEUBAU = replace(VORGABEN, afa_satz=D("0.03"))
