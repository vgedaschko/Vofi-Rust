# Referenzrechner zur Fachspezifikation Rechenkern, Teil 1

**Zweck:** Beleg, dass die Regeln in `docs/fachspezifikation-rechenkern.md` eindeutig und rechenbar sind. Jede Zahl des Dokuments kommt aus diesen Skripten. Kein Produktcode; der Rechenkern entsteht in Rust und muss dieselben Werte liefern.
**Leser:** Entwicklung und Prüfer.
**Stand:** 2026-11-18, überarbeitet nach Prüfrunde 2 · 20 Referenzfälle, 1.150 Prüfungen, alle bestanden · 525 festgeschriebene Sollwerte.

## Aufruf

Python 3 mit Standardbibliothek; gerechnet wird mit `decimal`, nie mit Gleitkommazahlen.

    python3 referenzfaelle.py        alle Referenzfälle; Rückgabewert 0 nur, wenn alle in ihrer Toleranz liegen
    python3 beispielwerte.py         Zahlenbeispiele des Dokuments, die keine Prüfwerte sind
    python3 gegenrechnung.py         nur RF-15, die Gegenrechnung ohne die Module des Referenzrechners

    python3 referenzfaelle.py --festschreiben --ursachen URSACHEN.json --bericht BERICHT.md [--basis ALT.json] [--im-code IMCODE.json]
                                     Sollwerte der eigenen Fälle neu schreiben; nur zusammen mit einem Differenzbericht

Laufzeit von `referenzfaelle.py` rund 135 Sekunden; den größten Teil brauchen die Preissuchen und die Wirkungsrechnung der Abweichungsliste (R-3.2).

## Festschreiben nur mit Differenzbericht

`--festschreiben` schreibt `erwartete_werte.json` nur, wenn jeder geänderte, neue oder entfallene Wert eine Ursache hat. Die Ursachendatei ordnet Mustern der Wertnamen einen Satz zu, der die Regel nennt; sie kann umbenannte Werte ihrem alten Namen zuordnen. Ein Muster, das jeden Wert eines Falls träfe, lehnt die Festschreibung ab (R-15.2); die Datei der Runde 2 führt je Wert ein eigenes, vollständiges Muster. Der Bericht führt je Wert alt, neu und Ursache. Fehlt eine Ursache, bleibt die Festschreibung unverändert, und der Lauf endet mit Rückgabewert 2. `--basis` vergleicht gegen einen früheren Stand statt gegen die Datei im Ordner; `--im-code` nimmt Sollwerte in den Bericht auf, die im Code der Fälle stehen.

Stand der Prüfrunde 1: `aenderungen-runde1.md` (140 geänderte, 256 neue, 22 entfallene Werte und fünf geänderte Sollwerte im Code), erzeugt aus `ursachen-runde1.json` und `im-code-runde1.json` gegen den Entwurf mit 207 Werten. Die veröffentlichten Werte (RF-01 bis RF-04, RF-05 im Jahresmodus) haben sich nicht geändert.

Stand der Prüfrunde 2: `aenderungen-runde2.md` (134 geänderte, 87 neue, 3 entfallene Werte und elf geänderte Sollwerte im Code), erzeugt aus `ursachen-runde2.json` und `im-code-runde2.json` gegen den Stand nach Prüfrunde 1 mit 441 Werten. Die veröffentlichten Werte, der Testfall und der Basisfall des Ankaufs (Endwert 2.524.305,59 Euro) haben sich nicht geändert.

## Gliederung

Die Module folgen den Kapiteln des Dokuments; die Kommentare nennen die Regelnummern (`R-4.3`).

| Datei | Kapitel | Inhalt |
|---|---|---|
| `zahlen.py` | 12 | Dezimalrechnung, Rundungsmodi, konforme Periodensätze |
| `zeit.py` | 2 | Raster, Planjahr, Kalenderjahr |
| `darlehen.py` | 5 | Tranche mit allen Tilgungsarten, Anschluss nach der Zinsbindung mit drei Regeln, Bereitstellungszins, Regel des Bankdarlehens mit kalkulatorischem Kapitaldienst |
| `ertrag.py` | 6 | Indexreihe, Mietpfad mit Wartefrist und Kappung, gebundene Miete, leere Flächen, Fluktuation, Instandhaltung nach Gebäudealter |
| `steuer.py` | 7 | Steuer in Kurzform je Steuerstatus, Kürzung, Hinzurechnung, Verlustvortrag mit Protokoll, Grenzsteuersätze |
| `restwert.py` | 8 | Verkaufspreis aus Faktor und Nettoanfangsrendite, Abzüge, Rückzahlung |
| `finanzplan.py` | 4, 9 | Finanzplan der Investition (Schritte 1 bis 10) mit Zeilenkennungen, Unterlassensalternative, Verdichtung, Lehrbuchansicht |
| `kennzahlen.py` | 10 | Vergleichsfaktor, VOFI-Rendite, Endwertüberschuss, Gesamtkapitalrendite, Deckung, Zinsdeckung, Kapitaldienstreserve, Deckungsgrenzen, interner Zinsfuß, Amortisation, Meldungen zur Rendite |
| `grobkalkulation.py` | 3, 11, 14 | Eingaben, Vorgaben und Katalog als getrennte Klassen; Eingabeprüfung; Bemessung, Mittelabruf, Blatt, Meldungen; tragbarer Preis, Stressfall, Zielwertsuche, Vergleich, Haltedauertabelle; Sperre bei verletzter Probe |
| `proben.py` | 13 | Kontrollsummen P-01 bis P-21, darunter Bemessungs-, Raten-, Steuer- und Tranchenprobe, die unabhängig nachrechnen |
| `annahmen.py` | Anhang A | angenommener Katalog- und Vorgabenstand und die Eingaben der Referenzobjekte, getrennt nach Herkunft; die Kernmodule enthalten keinen Satz, keine Schwelle und keine Frist (RF-20 prüft das) |
| `rf_rahmen.py` | 15 | Prüfhilfen, Festschreibung mit Differenzbericht |
| `rf_lehrbuch.py`, `rf_testfall.py`, `rf_bausteine.py`, `rf_grob.py` | 15 | Referenzfälle RF-01 bis RF-14 |
| `rf_neu.py` | 15 | RF-16 bis RF-20: Sperre der Proben, Steuerregeln, Miete im Bestand, Bankensicht, Ränder und Meldungen |
| `rf_runde2.py` | 15 | Prüfungen zu den Regeln der zweiten Überarbeitung, eingeordnet in RF-12, RF-13 und RF-16 bis RF-20: Abweichungen vom Hausstandard, Bemessungszins, KfW nach dem Merkblatt, Förderung nach der Richtlinie, Stressfall, Fehlerbilder in der Rechnung (über `zahlen.FEHLER`), Katalog, Suchen, Vergleich |
| `gegenrechnung.py` | 15 | RF-15: Testfall im Monatsraster, Alternative mit zwei Sätzen, Anlaufverlust und Ankauf Basisfall in gerader Linie nachgerechnet; importiert kein Modul des Referenzrechners und liest nur `erwartete_werte.json` |
| `erwartete_werte.json` | 15 | festgeschriebene Sollwerte der eigenen Fälle (525 Werte) |
| `ursachen-runde1.json`, `im-code-runde1.json`, `aenderungen-runde1.md` | 15 | Ursachen und Differenzbericht der Festschreibung nach Prüfrunde 1 |
| `ursachen-runde2.json`, `im-code-runde2.json`, `aenderungen-runde2.md` | 15 | dasselbe nach Prüfrunde 2 |
| `beispielwerte.py` | – | druckt die Beispielzahlen des Dokuments, die kein Prüfwert sind, je Regel |

## Woher die Sollwerte stammen

| Art | Fälle | Sollwert |
|---|---|---|
| veröffentlicht | RF-01 Kirchner (`KIRCHNER-IWU-2004`), RF-02 IWU 2013 (`IWU-2013-ENDBERICHT`), RF-03 und RF-04 Schulte (`SCHULTE-IMMOBILIENINVESTITION-2025`) | im Code; Toleranz nach der Genauigkeit der Quelle |
| früher unabhängig bestätigt | RF-05 und RF-06 Testfall mit Varianten im Jahresmodus (Bericht Anhang A.6; `../finanzmathematik-pruefung/`, `../runde4/`, `../runde5/`); Darlehens- und Steuerbeispiele des Berichts in RF-08 und RF-10 | im Code; 0,01 Euro |
| in Prüfrunde 1 unabhängig bestätigt | Testfall im Monatsraster (585.918,65 Euro), Anschlussfinanzierung (Finanzmathematiker); Bankdarlehen des Ankaufs mit kalkulatorischem Kapitaldienst (Bank) | im Code und in `erwartete_werte.json` |
| in Prüfrunde 2 von den Prüfern gegengerechnet | Stressfall mit neu bemessenem Darlehen, KfW-Raten, Bemessungszins am übernommenen Darlehen, Bankfall, Wirkungen der Abweichungen, tragbarer Preis je Anschlussregel, Sprungstelle der Preissuche, Steuer der geprägten Personengesellschaft | im Code von `rf_runde2.py`, mit Herkunft im Namen der Prüfung |
| eigene Fälle | RF-07, RF-10 bis RF-14 und RF-16 bis RF-20, soweit ohne veröffentlichten Wert | `erwartete_werte.json`; auf den Cent |
| Gegenrechnung | RF-15 | 16 Werte ohne die Module nachgerechnet; auf den Cent |

Die Gegenrechnung stammt vom selben Verfasser und schützt vor Programmfehlern, nicht vor einer falsch gelesenen Regel. Die zweite, unabhängige Umsetzung liegt unter `../blindrechnung-fachspezifikation/`; wer den Referenzrechner pflegt, liest sie nicht, und umgekehrt (R-15.6). Abnahmemaßstab für den Kern in Rust sind die Werte, die beide treffen. Sie ist auf diesen Stand noch nachzuziehen; die Parallelrechnung echter Vorhaben steht aus.

Drei Werte der Buchtabelle zur Finanzinvestition im Fallbeispiel von Schulte sind in sich um eine Einheit unstimmig (Quellnotiz 11); RF-04 fasst das als Toleranz von einer Einheit. `../schulte_musterrechnung.py` zeigt dieselben drei Abweichungen einzeln.

## Grenzen

- Der Referenzrechner setzt Teil 1 um: allgemeiner Kern und Grobkalkulation 1a, darin das KfW-Darlehen und die NBank-Förderung in Grobform. Steuer in Grundform, Neubau und Förderung in voller Tiefe, Mieterliste und Simulation fehlen.
- Die Eingabeprüfung und alle Meldungen M-10 bis M-50 sind gebaut und in einem Referenzfall ausgelöst. Der Aufruf `kalkuliere` endet nie mit einem Fehler, sondern mit „Ergebnis“, „Eingabe“ oder „gesperrt“. M-27 kann in der Grobkalkulation nicht auftreten; geprüft ist der Auslöser am Testfall.
- Der Wortlaut der Meldungen ist ein Arbeitsstand ohne Umlaute; den Wortlaut der Oberfläche legt die Gestaltung nach der Tabelle in R-14.13 fest.
- Alle Sätze und Vorgaben in `annahmen.py` sind Annahmen der Beispiele, keine freigegebenen Werte.
