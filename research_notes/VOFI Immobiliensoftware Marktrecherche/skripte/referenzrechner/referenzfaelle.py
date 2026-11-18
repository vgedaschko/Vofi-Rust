#!/usr/bin/env python3
"""Referenzrechner zur Fachspezifikation Rechenkern, Teil 1: rechnet alle Referenzfaelle (Kapitel 15).

    python3 referenzfaelle.py
        alle Faelle; Rueckgabewert 0 nur, wenn alle in ihrer Toleranz liegen

    python3 referenzfaelle.py --festschreiben --ursachen DATEI.json --bericht DATEI.md [--basis ALT.json]
        erwartete Werte der eigenen Faelle neu schreiben. Geschrieben wird nur zusammen mit einem Differenzbericht
        (alt, neu, Ursache je Wert); hat ein geaenderter Wert keine Ursache in der Ursachendatei, bleibt die
        Festschreibung unveraendert und der Lauf endet mit Rueckgabewert 2 (R-15.2).

Kein Produktcode. Gliederung wie das Dokument docs/fachspezifikation-rechenkern.md; siehe LIESMICH.md.
"""
import sys
import rf_rahmen
import rf_lehrbuch
import rf_testfall
import rf_bausteine
import rf_grob
import rf_neu
import rf_runde2
import gegenrechnung


def _argument(name):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else None


if __name__ == "__main__":
    fest = "--festschreiben" in sys.argv
    if fest and not (_argument("--ursachen") and _argument("--bericht")):
        print("--festschreiben verlangt --ursachen DATEI.json und --bericht DATEI.md (R-15.2)")
        raise SystemExit(2)
    rf_rahmen.FESTSCHREIBEN[0] = fest
    rf_lehrbuch.alle()
    rf_testfall.alle()
    rf_bausteine.alle()
    rf_grob.alle()
    rf_neu.alle()
    rf_runde2.alle()
    if fest:
        import json
        im_code = json.load(open(_argument("--im-code"), encoding="utf-8")) if _argument("--im-code") else ()
        if not rf_rahmen.schreibe_fest(_argument("--basis") or rf_rahmen.FESTDATEI, _argument("--ursachen"),
                                       _argument("--bericht"), im_code):
            raise SystemExit(2)
        rf_rahmen.FEST.update(rf_rahmen.NEU)
    rf_rahmen.ERGEBNISSE.extend(gegenrechnung.alle())
    raise SystemExit(rf_rahmen.zusammenfassung())
