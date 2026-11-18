# Vofi-Rust

Webanwendung zur Immobilien-Investitionsrechnung nach der VOFI-Methode (Vollständiger Finanzplan) mit Fördermodulen, Sensitivitäts- und Monte-Carlo-Analyse, Dashboard und Mehrbenutzerbetrieb. Stand: Konzeptphase, noch kein Code.

## Spezifikation ist der Pfad

`docs/spezifikation.md` ist das maßgebliche Entwicklungsdokument und wird laufend fortgeschrieben.

- Vor jeder inhaltlichen Arbeit lesen. Was dort als **fest** steht, gilt.
- Soll etwas anders gebaut werden, zuerst die Spezifikation ändern und die Änderung in `docs/entscheidungen.md` begründen, dann umsetzen. Frühere Festlegungen dürfen fallen – aber nachvollziehbar.
- Nach jeder Prüfrunde und nach jeder Antwort des Auftraggebers prüfen, ob eine Festlegung berührt ist, und sie nachziehen.
- Merkst du während der Arbeit, dass du von der Spezifikation abweichst oder sie eine Frage offenlässt: anhalten, Spezifikation klären, dann weiter.

## Zusammenarbeit

- Der Auftraggeber ist Betriebswirt, kein Programmierer. Technische Entscheidungen selbst treffen und kurz in Geschäftssprache begründen (Kosten, Risiko, Nutzen) – nicht als Auswahlfrage zurückgeben.
- Rückfragen nur zu fachlichen und betriebswirtschaftlichen Themen (Rechenlogik, Kennzahlen, Förderung, Steuern, Abläufe im Unternehmen).
- Sprache: Deutsch, auch in Dokumenten, Commit-Nachrichten und Oberflächentexten.

## Qualitätsanspruch

Ziel ist 9 von 10 in Code, Gestaltung und Funktionsumfang. Maßstab ist der Geschäftsbericht eines Konzerns wie Airbus, nicht die Schülerpräsentation: fachlich belastbar, durchgestaltet, ohne Füllstoff. „Funktioniert" genügt nicht.

Strikt an Branchenstandards und anerkannten Best Practices ausrichten und im Zweifel den Standard nachschlagen statt eine eigene Lösung zu erfinden:

| Bereich | Maßstab |
|---|---|
| Fachlogik | Lehrbuch-VOFI (Grob; Schulte/Ropeter), gif-Richtlinien, DIN 276/277, WoFlV, II. BV, ImmoWertV, aktuelle Gesetzes- und Förderlage mit Quelle und Stand. Fachliteratur bei Bedarf am Original beschaffen (rechtmäßige Quellen: frei zugängliche Fassungen, Verlags- oder Bibliothekszugang, vom Auftraggeber bereitgestellte Exemplare; notfalls über dessen Rechner) |
| Finanzmodell | FAST Standard und ICAEW Financial Modelling Code: Eingaben, Rechnung und Ausgabe getrennt, keine versteckten Konstanten, Kontrollsummen |
| Berichte und Diagramme | IBCS (einheitliche Notation, Aussage im Titel, keine Dekoration), Typografie und Raster auf Geschäftsberichtsniveau |
| Oberfläche | WCAG 2.2 AA, durchgängiges Gestaltungssystem, deutsche Zahl- und Datumsformate, fachlich präzise Texte |
| Code | Rust API Guidelines, `clippy` ohne Warnungen, jede fachliche Regel mit Test und Referenzfall, exakte Geldbeträge |
| Sicherheit und Daten | OWASP ASVS, DSGVO, lückenloses Änderungsprotokoll |

Wo ein Ergebnis den Maßstab noch nicht erreicht, das dem Auftraggeber offen sagen und benennen, was zur 9 fehlt – nicht als fertig ausgeben.

### Auftreten nach außen

Alles, was Nutzer oder Kunden sehen (Oberfläche, Kundenberichte, Exporte), tritt auf wie das Produkt eines professionellen Hauses. Für interne Entwicklungsunterlagen (Recherchen, Spezifikation, Prüfprotokolle, Berichte an den Auftraggeber) gilt das nicht: Dort werden Prüfungen, Einschränkungen und Unsicherheiten offen benannt.

- Keine Hinweisflut. Interne Einschränkungen, Unsicherheiten und Entstehungsdetails bleiben hinter den Kulissen (Protokoll, `TASKS.md`, Entwicklerdokumentation).
- Ein Hinweis erscheint nur, wenn er fachlich, technisch oder rechtlich Gewicht hat – etwa Stand-Datum einer Förderkondition, eine Annahme, die das Ergebnis trägt, eine Rechengrenze, eine rechtlich gebotene Abgrenzung. Dann einmal, an der Stelle, an der er gebraucht wird, in einem Satz.
- Auch interne Dokumente bleiben lesbar: Ergebnis zuerst, Belegqualität gebündelt statt als wiederholte Vorbehalte.

### Gestaltung und Bedienung

- An bewährten Vorbildern ausrichten, nicht frei erfinden: vor dem Entwurf einer Ansicht Referenzen aus guten Finanz-, Analyse- und Tabellenanwendungen ansehen (über die Mobbin-Werkzeuge, sofern verfügbar) und das Muster benennen, dem der Entwurf folgt.
- Fertige, gepflegte Bibliotheken für Standardbausteine einsetzen (Tabellen, Diagramme, Formulare, Dialoge, Datumswahl) statt sie neu zu bauen. Eigenbau nur dort, wo das Fachliche es verlangt (VOFI-Tabelle, Förderlogik) – mit kurzer Begründung.
- Auswahl einer Bibliothek nach Pflegezustand, Lizenz, Barrierefreiheit und Passung zum Gestaltungssystem; die Entscheidung trifft Claude und hält sie fest.

## Agenten und Modelle

- Agenten (Recherche, Prüfer, Zuarbeit) laufen standardmäßig mit dem neuesten Opus-Modell.
- Das neueste Fable-Modell nur für wirklich komplexe oder folgenreiche Aufgaben: Spezifikation und Nachrechnen des Rechenkerns, Steuer- und Rechtslogik mit Auswirkung auf Ergebnisse, Sicherheits- und Rechtearchitektur, abschließende Berichte.

## Prüfrunden

- Jedes größere Arbeitsergebnis (Bericht, Fachkonzept, Rechenfunktion, Oberfläche) durchläuft vor der Übergabe Prüfrunden mit `/pruefrunde`, wiederholt bis mindestens 9 von 10 oder bis feststeht, warum das nicht erreichbar ist. Die Prüferrollen liegen in `.claude/agents/`, die gemeinsamen Regeln in `docs/pruefung/regeln.md`.
- Leerlauf nutzen: Wenn auf Hintergrundarbeit oder eine Antwort gewartet wird, das jüngste ungeprüfte Ergebnis prüfen lassen.
- Befunde der Prüfer sind Hinweise, keine Wahrheit: vor dem Einarbeiten an der Fundstelle nachprüfen.

## Orientierung

- `TASKS.md` – offene Arbeit; wird vom Hook `.claude/hooks/anything-else.sh` bei Sitzungsstart und vor jedem Stopp gelesen. Aktuell halten.
- `docs/spezifikation.md` – was gebaut wird und warum; geltender Stand.
- `docs/entscheidungen.md` – Entscheidungsprotokoll: wie der Stand zustande kam.
- `docs/entwicklungsplan.md` – Phasen, Freigabepunkte, Bestandsaufnahme der Grundlagen und Prüfplan.
- `docs/skills-und-werkzeuge.md` – empfohlene Skills, Plugins und Hooks.
- `docs/pruefung/protokoll.md` – was wann von wem geprüft wurde.
- `reports/`, `research_notes/` – Rechercheergebnisse und ihre Quellnotizen.
