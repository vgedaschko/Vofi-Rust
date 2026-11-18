#!/usr/bin/env python3
"""Referenzrechner zur Fachspezifikation Rechenkern, Teil 1: rechnet alle Referenzfaelle (Kapitel 15).

    python3 referenzfaelle.py                 alle Faelle; Rueckgabewert 0 nur, wenn alle in ihrer Toleranz liegen
    python3 referenzfaelle.py --festschreiben erwartete Werte der eigenen Faelle neu schreiben (nur mit Begruendung)

Kein Produktcode. Gliederung wie das Dokument docs/fachspezifikation-rechenkern.md; siehe LIESMICH.md.
"""
import sys
import rf_rahmen
import rf_lehrbuch
import rf_testfall
import rf_bausteine
import rf_grob
import gegenrechnung

if __name__ == "__main__":
    rf_rahmen.FESTSCHREIBEN[0] = "--festschreiben" in sys.argv
    rf_lehrbuch.alle()
    rf_testfall.alle()
    rf_bausteine.alle()
    rf_grob.alle()
    if rf_rahmen.FESTSCHREIBEN[0]:
        rf_rahmen.schreibe_fest()
        rf_rahmen.FEST.update(rf_rahmen.NEU)
    gegenrechnung.alle()
    raise SystemExit(rf_rahmen.zusammenfassung())
