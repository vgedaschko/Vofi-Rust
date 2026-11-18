"""Kapitel 8 der Fachspezifikation: Restwert und Verkauf (R-8.1 bis R-8.9)."""
from decimal import Decimal as D
from zahlen import NULL, EINS


def preis_aus_faktor(faktor, jahressollmiete_folgejahr, rd):
    """R-8.1: Verkaufsfaktor x Jahresnettokaltmiete des Folgejahres = Kaufpreis ohne Erwerbsnebenkosten."""
    return rd.geld(faktor * jahressollmiete_folgejahr)


def preis_aus_nettoanfangsrendite(rendite, reinertrag_folgejahr, erwerbsnebenkosten_kaeufer, rd):
    """R-8.2: Reinertrag des Folgejahres / Nettoanfangsrendite = Kaufpreis einschliesslich der
    Erwerbsnebenkosten des Kaeufers; diese werden herausgerechnet."""
    return rd.geld(reinertrag_folgejahr / rendite / (EINS + erwerbsnebenkosten_kaeufer))


def verkaufskosten(preis, satz, rd):
    """R-8.3"""
    return rd.geld(preis * satz)


def stau_abzug(betrag_heute, baupreisindex_stichtag, anteil_ausstehend, rd):
    """R-8.4: ausstehender Investitionsstau zum Preisstand des Verkaufsstichtags."""
    return rd.geld(betrag_heute * anteil_ausstehend * baupreisindex_stichtag)


def zuschuss_rueckzahlung(zuschuss, bindung_monate, verbleibend_monate, rd):
    """R-8.7 (MA-017): anteilige Rueckzahlung fuer die verbleibende Bindungsdauer."""
    if bindung_monate <= 0 or verbleibend_monate <= 0:
        return NULL
    return rd.geld(zuschuss * D(verbleibend_monate) / D(bindung_monate))
