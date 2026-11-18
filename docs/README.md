# Dokumentation

Einstieg in alles, was zum Vorhaben und zur Anwendung geschrieben steht. Diese Seite ist das Inhaltsverzeichnis: Sie sagt, welches Dokument wofür gilt, wer es liest, wann es aktualisiert wird und ob es schon existiert.

**Stand:** 2026-11-18 · Phase 0 (Grundlagen)

## Grundsätze

1. **Ein Thema, ein Ort.** Jede Aussage hat genau eine Heimat. Andere Dokumente verweisen dorthin und wiederholen nichts. Steht etwas an zwei Stellen, ist eine davon zu löschen.
2. **Soll und Ist sind getrennt.** Die Spezifikation beschreibt, was gebaut werden soll. Sobald ein Teil gebaut und abgenommen ist, wird die Anwendungsdokumentation seine Quelle; die Spezifikation verweist dann nur noch dorthin.
3. **Im selben Arbeitsgang.** Eine Änderung ist erst fertig, wenn die zugehörige Dokumentation nachgezogen ist. Dokumentation wird nicht „später" geschrieben.
4. **Quellen stehen im Kataster.** Rechts-, Förder- und Normangaben nennen die Kennung aus dem Normen- und Quellenkataster; Fundstelle, Stand und Prüfdatum stehen nur dort.
5. **Ungeklärtes ist gekennzeichnet.** Wo das Modell auf einer ungeklärten Annahme rechnet, steht deren Kennung aus dem Verzeichnis der Modellannahmen.
6. **Erzeugen statt abschreiben.** Was sich aus Daten oder Code ableiten lässt (Kennzahlenliste, Regel- und Förderkatalog, Schnittstellen), wird daraus erzeugt und nicht von Hand gepflegt.
7. **Nichts auf Vorrat.** Ein Dokument entsteht, wenn es Inhalt hat. Leere Gerüste gibt es nicht; was in der Übersicht als „ab Phase …" steht, existiert noch nicht.
8. **Überholtes verschwindet.** Abgelöste Fassungen werden gelöscht, nicht daneben abgelegt; die Versionsverwaltung bewahrt die Geschichte.
9. **Jedes Dokument beginnt mit Zweck, Leser und Stand** – in zwei, drei Zeilen.

## Teil A: Projektdokumentation

Wie das Vorhaben gesteuert wird. Leser: Auftraggeber, Entwicklung, Prüfer.

| Dokument | Quelle für | Aktualisiert, wenn | Status |
|---|---|---|---|
| [`spezifikation.md`](spezifikation.md) | Was gebaut wird und warum; geltende Festlegungen mit Status | eine Festlegung entsteht oder sich ändert – vor der Umsetzung | vorhanden |
| [`fachspezifikation-rechenkern.md`](fachspezifikation-rechenkern.md) | Rechenregeln des Kerns mit Regelnummern, Proben, Randfällen und Referenzfällen; konkretisiert Spezifikation Kapitel 3. Teil 1: allgemeiner Kern und Grobkalkulation. Belegt durch den Referenzrechner unter `research_notes/…/skripte/referenzrechner/` | eine Rechenregel entsteht oder sich ändert – vor der Umsetzung; der Referenzrechner wird im selben Arbeitsgang nachgezogen | vorhanden (Teil 1, in Prüfung) |
| [`entwicklungsplan.md`](entwicklungsplan.md) | Phasen, Freigabepunkte, Bestandsaufnahme, Prüfplan | eine Phase endet oder die Reihenfolge sich ändert | vorhanden |
| [`entscheidungen.md`](entscheidungen.md) | Wann was warum entschieden oder geändert wurde | bei jeder Entscheidung | vorhanden |
| [`../TASKS.md`](../TASKS.md) | Offene Arbeit, auch beim Auftraggeber | laufend | vorhanden |
| [`quellenkataster.md`](quellenkataster.md) | Alle Gesetze, Förderrichtlinien, Normen, Standards, Fachliteratur und Datenquellen mit Stand, Beleg und Prüfturnus; erzeugt aus `quellenkataster/quellen.toml` | eine Quelle hinzukommt, sich ändert oder neu am Original gelesen wird | vorhanden |
| [`modellannahmen.md`](modellannahmen.md) | Annahmen über Recht, Förderpraxis und Methode, die sich vor dem Bau nicht klären lassen: Kennung, Lesart, Gewicht, Sichtbarkeit, Klärungsweg; erzeugt aus `modellannahmen/annahmen.toml` | eine Annahme gesetzt, geklärt oder widerlegt wird | vorhanden |
| [`gestaltungsreferenzen.md`](gestaltungsreferenzen.md) | Vorbilder je Kernansicht mit dem Muster, das übernommen wird, und dem, was bewusst anders gemacht wird | eine Ansicht entworfen wird oder ein Vorbild hinzukommt | vorhanden |
| [`pruefung/`](pruefung/) | Prüfregeln, Protokoll, Prüfberichte und Sichtung je Runde | nach jeder Prüfrunde | vorhanden |
| [`skills-und-werkzeuge.md`](skills-und-werkzeuge.md) | Eingesetzte Skills, Plugins, Hooks, Prüferrollen | ein Werkzeug hinzukommt oder entfällt | vorhanden |
| [`../reports/`](../reports/), [`../research_notes/`](../research_notes/) | Recherchebericht, Quellnotizen, Referenzrechnungen | eine Recherche abgeschlossen ist; Berichte werden danach nicht fortgeschrieben, sondern durch Spezifikation und Anwendungsdokumentation abgelöst | vorhanden |
| [`../CLAUDE.md`](../CLAUDE.md) | Arbeitsregeln für die Entwicklung mit Claude | eine Arbeitsregel sich ändert | vorhanden |

## Teil B: Anwendungsdokumentation

Was die Anwendung tut, wie man sie benutzt und betreibt. Sie entsteht mit der Anwendung und liegt unter `docs/anwendung/`.

| Dokument | Leser | Quelle für | Form | Aktualisiert, wenn | Status |
|---|---|---|---|---|---|
| **Fachhandbuch** | Anwender, Controlling, Banken, Prüfer | Rechenweise: Aufbau des Finanzplans, Rechenreihenfolge, Konventionen, Definition jeder Kennzahl mit Quelle | geschrieben; Kennzahlenliste erzeugt | eine Rechenregel abgenommen oder geändert wird | ab Phase 1 (aus Spezifikation Kapitel 3), fortgeschrieben ab Phase 4 |
| **Regel- und Förderkatalog** | Anwender, Katalogverantwortliche | Geltende Steuer-, Mietrechts- und Förderregeln; jede Regel verweist auf ihre Quelle im Kataster | aus den Katalogdaten erzeugt | sich der Katalog ändert – automatisch | ab Phase 1 |
| **Benutzerhandbuch** | Anwender | Einstieg, Anleitungen je Aufgabe, Nachschlageteil; dieselben Texte speisen die Hilfe in der Anwendung | geschrieben, gegliedert nach Diátaxis | eine Ansicht oder ein Ablauf abgenommen oder geändert wird | ab Phase 4, je Teilschritt |
| **Architekturdokumentation** | Entwicklung, Revision | Aufbau, Bausteine, Schnittstellen, Datenmodell, Qualitätsziele, Risiken | geschrieben nach arc42; Schnittstellen- und Code-Referenz erzeugt | sich Aufbau oder Schnittstellen ändern | ab Phase 2 |
| **Betriebshandbuch** | Betrieb, Datenschutz | Einrichtung, Sicherung und Wiederherstellung, Rechteverwaltung, Aktualisierung, Lösch- und Auskunftsverfahren | geschrieben | sich der Betrieb ändert | ab Phase 3 |
| **Änderungshistorie** | alle | Was sich je Version für Anwender geändert hat, einschließlich Regelstand | geschrieben nach „Keep a Changelog", Versionen nach SemVer | mit jeder Version | ab Phase 3 |

## Pflege

- **Zuständig** ist, wer die Sache ändert. Bei einer Entscheidung des Auftraggebers zieht Claude Spezifikation, Protokoll und diese Übersicht im selben Arbeitsgang nach.
- **Bei jedem Freigabepunkt** wird die Dokumentation als Ganzes geprüft (Rolle Dokumentation, siehe Prüfplan): Ist sie aktuell, widerspruchsfrei und auffindbar? Steht etwas doppelt? Beschreibt die Anwendungsdokumentation das, was die Anwendung tatsächlich tut?
- **Diese Übersicht** wird aktualisiert, sobald ein Dokument entsteht, entfällt oder seinen Zweck ändert. Ein Dokument, das hier nicht steht, gehört nicht zur Dokumentation.
