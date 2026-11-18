# Referenzrechner zur Fachspezifikation Rechenkern, Teil 1

**Zweck:** Beleg, dass die Regeln in `docs/fachspezifikation-rechenkern.md` eindeutig und rechenbar sind. Jede Zahl des Dokuments kommt aus diesen Skripten. Kein Produktcode; der Rechenkern entsteht in Rust und muss dieselben Werte liefern.
**Leser:** Entwicklung und Prüfer.
**Stand:** 2026-11-18 · 15 Referenzfälle, 529 Prüfungen, alle bestanden.

## Aufruf

Python 3 mit Standardbibliothek; gerechnet wird mit `decimal`, nie mit Gleitkommazahlen.

    python3 referenzfaelle.py                  alle Referenzfälle; Rückgabewert 0 nur, wenn alle in ihrer Toleranz liegen
    python3 beispielwerte.py                   Zahlenbeispiele des Dokuments, die keine Prüfwerte sind
    python3 gegenrechnung.py                   nur RF-15, die Gegenrechnung ohne die Module des Referenzrechners
    python3 referenzfaelle.py --festschreiben  erwartete Werte der eigenen Fälle neu schreiben (nur nach einer Regeländerung)

Laufzeit rund 20 Sekunden.

## Gliederung

Die Module folgen den Kapiteln des Dokuments; die Kommentare nennen die Regelnummern (`R-4.3`).

| Datei | Kapitel | Inhalt |
|---|---|---|
| `zahlen.py` | 12 | Dezimalrechnung, Rundungsmodi, konforme Periodensätze |
| `zeit.py` | 2 | Raster, Planjahr, Kalenderjahr |
| `darlehen.py` | 5 | Tranche mit allen Tilgungsarten, Anschluss nach der Zinsbindung, Regel des Bankdarlehens |
| `ertrag.py` | 6 | Indexreihe, Anpassungspfad, gebundene Miete |
| `steuer.py` | 7 | Steuer in Kurzform je Steuerstatus, Verlustvortrag, Grenzsteuersätze |
| `restwert.py` | 8 | Verkaufspreis aus Faktor und Nettoanfangsrendite, Abzüge, Rückzahlung |
| `finanzplan.py` | 4, 9 | Finanzplan der Investition (Schritte 1 bis 10), Unterlassensalternative, Verdichtung, Lehrbuchansicht |
| `kennzahlen.py` | 10 | Vergleichsfaktor, VOFI-Rendite, Endwertüberschuss, Gesamtkapitalrendite, Deckung, interner Zinsfuß, Amortisation |
| `grobkalkulation.py` | 3, 11 | Eingaben und Vorgaben, Bemessung, Mittelabruf, Blatt, tragbarer Preis, Stressfall, Zielwertsuche, Vergleich |
| `proben.py` | 13 | Kontrollsummen P-01 bis P-12 |
| `annahmen.py` | – | angenommener Katalog- und Vorgabenstand der Beispiele; der Rechenkern selbst enthält keinen Satz |
| `rf_rahmen.py`, `rf_lehrbuch.py`, `rf_testfall.py`, `rf_bausteine.py`, `rf_grob.py` | 15 | Referenzfälle RF-01 bis RF-14 |
| `gegenrechnung.py` | 15 | RF-15: vier Fälle in gerader Linie nachgerechnet, ohne die Module oben |
| `erwartete_werte.json` | 15 | festgeschriebene Sollwerte der eigenen Fälle (207 Werte) |

## Woher die Sollwerte stammen

| Art | Fälle | Sollwert |
|---|---|---|
| veröffentlicht | RF-01 Kirchner (`KIRCHNER-IWU-2004`), RF-02 IWU 2013 (`IWU-2013-ENDBERICHT`), RF-03 und RF-04 Schulte (`SCHULTE-IMMOBILIENINVESTITION-2025`) | im Code; Toleranz nach der Genauigkeit der Quelle |
| früher unabhängig bestätigt | RF-05 und RF-06 Testfall mit Varianten (Bericht Anhang A.6; `../finanzmathematik-pruefung/`, `../runde4/`, `../runde5/`); Darlehens-, Bank- und Steuerbeispiele des Berichts in RF-08 bis RF-10 | im Code; 0,01 Euro |
| eigene Fälle | RF-07 und RF-10 bis RF-14, soweit ohne veröffentlichten Wert | `erwartete_werte.json`; auf den Cent |
| Gegenrechnung | RF-15 | vier der eigenen Fälle ohne die Module nachgerechnet; auf den Cent |

Drei Werte der Buchtabelle zur Finanzinvestition im Fallbeispiel von Schulte sind in sich um eine Einheit unstimmig (Quellnotiz 11); RF-04 fasst das als Toleranz von einer Einheit. `../schulte_musterrechnung.py` zeigt dieselben drei Abweichungen einzeln.

## Grenzen

- Der Referenzrechner setzt Teil 1 um: allgemeiner Kern und Grobkalkulation 1a. Steuer in Grundform, Neubau in voller Tiefe, KfW, NBank in voller Tiefe, Mieterliste und Simulation fehlen.
- Die Meldungen M-21 bis M-24 und M-30 bis M-34 sind gebaut; die übrigen Meldungen und die Eingabeprüfung der Wertebereiche sind Vorgaben an den Kern und hier nicht umgesetzt.
- Alle Sätze und Vorgaben in `annahmen.py` sind Annahmen der Beispiele, keine freigegebenen Werte.
