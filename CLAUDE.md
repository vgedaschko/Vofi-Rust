# Vofi-Rust

Webanwendung zur Immobilien-Investitionsrechnung nach der VOFI-Methode (Vollständiger Finanzplan) mit Fördermodulen, Sensitivitäts- und Monte-Carlo-Analyse, Dashboard und Mehrbenutzerbetrieb. Stand: Konzeptphase, noch kein Code.

## Zusammenarbeit

- Der Auftraggeber ist Betriebswirt, kein Programmierer. Technische Entscheidungen selbst treffen und kurz in Geschäftssprache begründen (Kosten, Risiko, Nutzen) – nicht als Auswahlfrage zurückgeben.
- Rückfragen nur zu fachlichen und betriebswirtschaftlichen Themen (Rechenlogik, Kennzahlen, Förderung, Steuern, Abläufe im Unternehmen).
- Sprache: Deutsch, auch in Dokumenten, Commit-Nachrichten und Oberflächentexten.

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
