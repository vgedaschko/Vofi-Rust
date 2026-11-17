# Vofi-Rust

Webanwendung zur Immobilien-Investitionsrechnung nach der VOFI-Methode (Vollständiger Finanzplan) mit Fördermodulen, Sensitivitäts- und Monte-Carlo-Analyse, Dashboard und Mehrbenutzerbetrieb. Stand: Konzeptphase, noch kein Code.

## Zusammenarbeit

- Der Auftraggeber ist Betriebswirt, kein Programmierer. Technische Entscheidungen selbst treffen und kurz in Geschäftssprache begründen (Kosten, Risiko, Nutzen) – nicht als Auswahlfrage zurückgeben.
- Rückfragen nur zu fachlichen und betriebswirtschaftlichen Themen (Rechenlogik, Kennzahlen, Förderung, Steuern, Abläufe im Unternehmen).
- Sprache: Deutsch, auch in Dokumenten, Commit-Nachrichten und Oberflächentexten.

## Qualitätsanspruch

Ziel ist 9 von 10 in Code, Gestaltung und Funktionsumfang. Maßstab ist der Geschäftsbericht eines Konzerns wie Airbus, nicht die Schülerpräsentation: fachlich belastbar, durchgestaltet, ohne Füllstoff. „Funktioniert" genügt nicht.

Strikt an Branchenstandards und anerkannten Best Practices ausrichten und im Zweifel den Standard nachschlagen statt eine eigene Lösung zu erfinden:

| Bereich | Maßstab |
|---|---|
| Fachlogik | Lehrbuch-VOFI (Grob; Schulte/Ropeter), gif-Richtlinien, DIN 276/277, WoFlV, II. BV, ImmoWertV, aktuelle Gesetzes- und Förderlage mit Quelle und Stand |
| Finanzmodell | FAST Standard und ICAEW Financial Modelling Code: Eingaben, Rechnung und Ausgabe getrennt, keine versteckten Konstanten, Kontrollsummen |
| Berichte und Diagramme | IBCS (einheitliche Notation, Aussage im Titel, keine Dekoration), Typografie und Raster auf Geschäftsberichtsniveau |
| Oberfläche | WCAG 2.2 AA, durchgängiges Gestaltungssystem, deutsche Zahl- und Datumsformate, fachlich präzise Texte |
| Code | Rust API Guidelines, `clippy` ohne Warnungen, jede fachliche Regel mit Test und Referenzfall, exakte Geldbeträge |
| Sicherheit und Daten | OWASP ASVS, DSGVO, lückenloses Änderungsprotokoll |

Wo ein Ergebnis den Maßstab noch nicht erreicht, das offen sagen und benennen, was zur 9 fehlt – nicht als fertig ausgeben.

## Prüfrunden

- Jedes größere Arbeitsergebnis (Bericht, Fachkonzept, Rechenfunktion, Oberfläche) durchläuft vor der Übergabe eine Prüfrunde mit `/pruefrunde`. Die Prüferrollen liegen in `.claude/agents/`, die gemeinsamen Regeln in `docs/pruefung/regeln.md`.
- Leerlauf nutzen: Wenn auf Hintergrundarbeit oder eine Antwort gewartet wird, das jüngste ungeprüfte Ergebnis prüfen lassen.
- Befunde der Prüfer sind Hinweise, keine Wahrheit: vor dem Einarbeiten an der Fundstelle nachprüfen.

## Orientierung

- `TASKS.md` – offene Arbeit; wird vom Hook `.claude/hooks/anything-else.sh` bei Sitzungsstart und vor jedem Stopp gelesen. Aktuell halten.
- `docs/entscheidungen.md` – festgelegte Rahmenbedingungen.
- `docs/skills-und-werkzeuge.md` – empfohlene Skills, Plugins und Hooks.
- `docs/pruefung/protokoll.md` – was wann von wem geprüft wurde.
- `reports/`, `research_notes/` – Rechercheergebnisse und ihre Quellnotizen.
