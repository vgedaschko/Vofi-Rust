# Skills und Werkzeuge für das VOFI-Projekt

Übersicht der eingesetzten und geprüften Skills, Plugins, Prüferrollen und Hooks. Leser: Entwicklung, wenn ein Werkzeug gewählt oder eingerichtet wird. Stand 2026-11-18. Sortiert nach erwartetem Nutzen. Leitlinie: Was deterministisch geprüft werden kann, gehört in Hooks und CI; Skills sind für Fachwissen und wiederkehrende Abläufe.

## 1. Wirkt am zuverlässigsten: keine Skills, sondern feste Mechanik

| Mechanik | Wofür | Stand |
|---|---|---|
| `CLAUDE.md` | Arbeitsregeln, Pflichtlektüre, Qualitätsmaßstab | Eingerichtet. Glossar, Vorzeichenkonvention, „Geld nie als Gleitkommazahl“ und Build- und Testbefehle kommen mit dem Rust-Workspace hinzu (Aufgabe in `TASKS.md`) |
| Hooks (Abschnitt 6) | Format nach jeder Änderung; `clippy` und Tests vor jedem Stopp; Gestaltungsprüfung; offene Aufgaben | Eingerichtet und mit Probeprojekten getestet; wirksam ab der ersten Rust- beziehungsweise Oberflächendatei |
| Prüfkette auf dem Server | Dieselben Prüfungen bei jeder Zusammenführung, dazu Referenzfälle des Rechenkerns | Phase 3 |
| Einrichtungsskript der Cloud-Umgebung | Rust-Werkzeuge, `wasm32`-Ziel und `wasm-bindgen-cli` in jeder Sitzung vorhanden (Bestandsaufnahme: Entwicklungsplan, Abschnitt 2a) | Phase 3 |

## 2. Vorhandene Skills, die hier direkt passen

| Skill | Einsatz im Projekt |
|---|---|
| `/code-review` | Vor jedem Merge; findet Korrektheitsfehler im Diff |
| `/security-review` | Pflicht bei allem rund um Anmeldung, Rollen, Mandantentrennung, Kundenzugang |
| `/simplify` | Nach größeren Umbauten am Rechenkern |
| `anthropic-skills:xlsx` | Lehrbuch-VOFI als Excel-Referenz nachbauen; Excel-Export des Tools gegenprüfen |
| `anthropic-skills:pdf` | KfW-Merkblätter und NBank-Förderbestimmungen auslesen, wenn Konditionen gepflegt werden |
| `anthropic-skills:deep-research` | Halbjährliche Aktualisierung der Förderlandschaft, Steueränderungen |
| `dataviz` | Dashboard-Diagramme (Tornado, Wasserfall, Fächer, Histogramm) einheitlich und barrierearm |
| `design:design-critique`, `design:accessibility-review`, `design:ux-copy` | Eingabemasken und Fehlermeldungen; lohnt sich ab dem ersten klickbaren Stand |
| `run` | Anwendung starten und eine Änderung im echten Browser prüfen |
| `anthropic-skills:skill-creator` | Die projekteigenen Skills aus Abschnitt 4 bauen und mit Testfällen messen |

## 3. Plugins aus dem Verzeichnis (noch nicht aktiviert)

| Plugin | Herausgeber | Einschätzung |
|---|---|---|
| Engineering | Anthropic | Empfohlen: `architecture` (Entscheidungsprotokolle), `system-design`, `testing-strategy`, `documentation`, `tech-debt` |
| Product Management | Anthropic | Empfohlen für die Konzeptphase: `write-spec`, `competitive-brief`, `roadmap-update` |
| Rust CLI Skills | Community (Dankosik) | Bedingt: auf Kommandozeilenwerkzeuge zugeschnitten; `rust-idiomatic`, `rust-errors`, `rust-testing`, `rust-performance` sind übertragbar. Qualität nicht von mir geprüft – erst an einer Aufgabe testen |
| Weitere Review-Plugins (finecomb, review-council, n360-engineering) | Community | Nicht empfohlen als Standard: überschneiden sich mit `/code-review` und `/security-review`; mehr Werkzeuge heißt hier nicht bessere Ergebnisse |

Für Rust-Webentwicklung (axum, sqlx, WASM) gibt es im Verzeichnis kein passendes fertiges Skill-Paket. Das decken `CLAUDE.md`, Clippy und die projekteigenen Skills besser ab.

## 4. Projekteigene Skills, die sich lohnen (selbst bauen)

Hier steckt der größte Hebel, weil kein allgemeiner Skill das Fachwissen mitbringt.

| Skill | Inhalt | Auslöser |
|---|---|---|
| `vofi-fachmodell` | Aufbau der VOFI-Tabelle, Rechenreihenfolge, Definition jeder Kennzahl mit Quelle, Vorzeichen- und Rundungsregeln | Jede Änderung am Rechenkern |
| `foerderprogramm-pflegen` | Ablauf: Merkblatt lesen → Programm als Konfigurationsdatei erfassen → Stand-Datum und Quelle eintragen → Testfall anlegen | „Programm X hinzufügen/aktualisieren" |
| `steuer-regeln` | Regeln je Investorentyp mit Paragraf und Gültigkeitszeitraum; Checkliste bei Gesetzesänderung | Arbeit am Steuermodul |
| `referenzfall-anlegen` | Wie ein Lehrbuch- oder Praxisfall zum automatischen Test wird (Eingaben, erwartete Tabelle, Toleranzen, Invarianten wie Finanzierungssaldo = 0) | Neue Formel, neuer Fehlerfall |

Reihenfolge: `vofi-fachmodell` und `referenzfall-anlegen` zuerst (entstehen aus dem Fachkonzept), `foerderprogramm-pflegen` mit dem Fördermodul, `steuer-regeln` mit dem Steuermodul.

## 5. Prüfer (eingerichtet)

Siebzehn Prüferrollen in `.claude/agents/`, gestartet über `/pruefrunde`:

| Gruppe | Rollen |
|---|---|
| Fachlich | Fachexperte Immobilien · Finanzmathematiker · Steuerberater · Jurist · Fördermittelberater |
| Nutzer und Entscheider | Praktiker · unbedarfter Endnutzer · Controller · Investor · Bank |
| Qualität | Gestaltung · KI-Einheitsbrei · Grenzfälle · Software-Architekt · Revision und Datenschutz · Dokumentation |
| Brücke | Der Lotse (auf Zuruf und an Meilensteinen) |

Die Prüfer lesen nur und berichten; eingearbeitet wird erst nach Gegenprüfung. Ergebnisse stehen in `docs/pruefung/protokoll.md`.

## 6. Hooks (eingerichtet)

| Hook | Auslöser | Wirkung |
|---|---|---|
| `anything-else.sh start` | Sitzungsstart | Zeigt Pflichtlektüre und offene Aufgaben; meldet fehlende Dateien der Pflichtlektüre und Dokumente, die in der Übersicht fehlen |
| `anything-else.sh stop` | Vor jedem Stopp | Hält einmal auf, solange unter „Jetzt" in `TASKS.md` etwas offen ist |
| `spezifikation-merker.sh` | Nach Änderung an Spezifikation oder Entwicklungsplan | Erinnert an Stand-Datum, Entscheidungsprotokoll und Folgeänderungen |
| `gestaltung.sh merker` | Erste Änderung an einer Oberflächendatei je Sitzung | Erinnert an `frontend-design`, Vorbilder und Gestaltungsprüfung |
| `gestaltung.sh stop` | Vor jedem Stopp, wenn sich Oberflächendateien geändert haben | Hält den Stopp einmal auf und nennt die fällige Gestaltungsprüfung; sie gilt als erledigt, wenn `gestaltung.sh bestanden` vermerkt ist |
| `rust-format.sh` | Nach Änderung an einer Rust-Datei | Formatiert das Paket |
| `rust-pruefung.sh` | Vor jedem Stopp, wenn sich Rust-Code geändert hat | `clippy` ohne Warnungen und alle Tests; hält bei Fehlern einmal auf |

Alle Stopp-Hooks halten einen Stopp genau einmal auf und nennen, was fehlt; ein zweiter Stoppversuch geht durch, damit keine Endlosschleife entsteht. Die Pflicht selbst steht in `CLAUDE.md`. Dazu kommt der Hook der Cloud-Umgebung, der vor jedem Stopp nicht gesicherte Änderungen meldet. Noch nicht eingerichtet, weil sie vom Projektzuschnitt abhängen: Typprüfung und Lint der Oberfläche, die Prüfkette auf dem Server (Phase 3).

## 7. Gestaltungsreferenzen

| Quelle | Wofür | Stand 18.11.2026 |
|---|---|---|
| Mobbin (angebunden) | Bildschirme und Abläufe realer Anwendungen: Tabellen mit Zeitachse, Szenariowechsel, Versionen, Umschalter Monat/Jahr, Kennzahlenleisten | Probesuche erfolgreich. Stark bei allgemeinen Mustern aus Finanz- und Planungsanwendungen (Causal, Monarch, Fey, YNAB, Origin); für immobilienspezifische Fachsoftware fand die Suche nichts Brauchbares. Sammlung „VOFI Referenzen“ mit 34 Vorbildern angelegt |
| IBCS | Notation und Aufbau von Berichten und Diagrammen | Maßstab laut `CLAUDE.md`; Regelwerk noch nicht am Original gelesen (siehe Quellenkataster) |
| Öffentliche Gestaltungssysteme für datendichte Fachanwendungen | Bausteine und Regeln für Tabellen, Formulare, Zustände, Barrierefreiheit | Auswahl in Phase 2 |
| Produktseiten und Handbücher der Fachsoftware (ARGUS, Forbury, Causal) | Fachliche Bedienmuster: Mieterliste, Szenarien, Bandbreiteneingabe | In der Recherche ausgewertet |
| Geschäftsberichte großer Unternehmen | Typografie, Raster und Tabellensatz der Berichte | In Phase 2 |

Sammlung in Mobbin: „VOFI Referenzen" (privat). Ausgewertet in `docs/gestaltungsreferenzen.md`.

### Gegen Einheitsbrei in der Oberfläche

| Mittel | Art | Einschätzung |
|---|---|---|
| Design-Wettbewerb `/designwettbewerb` | eigener Ablauf | Stärkstes Mittel: Vielfalt durch zugewiesene Richtungen, Urteil am gerenderten Ergebnis |
| Rolle `pruefer-slop` | eigener Prüfer | Vorhanden; prüft Text und Oberfläche |
| `design:design-critique`, `design:accessibility-review`, `design:ux-copy`, `design:design-system` | Anthropic, in der Sitzung verfügbar | Für Kritik, Barrierefreiheit, Texte, Gestaltungssystem |
| `dataviz` | eingebaut | Diagramme mit geprüfter Farb- und Formlogik |
| `frontend-design` | Anthropic, Plugin-Verzeichnis | **Pflicht bei jeder Gestaltungsarbeit.** Am 18.11.2026 für das Projekt installiert (`claude plugin install frontend-design@anthropic-plugin-directory --scope project`); der Eintrag steht in `.claude/settings.json` und gilt für Sitzungen, die mit diesem Repository starten |
| Rolle `pruefer-gestaltung` | eigener Prüfer | Prüft am gerenderten Ergebnis; führt Designkritik und Barrierefreiheitsprüfung selbst aus |
| VectorLab UI/UX Skills (`anti-slop`, Typografie, Abstände, Formulare, Leerzustände, Tastatur) | Community, nicht aktiviert | Nicht eingesetzt: Der Auftraggeber setzt auf `frontend-design` von Anthropic (Entscheidung 18.11.2026) |
| UXKIN (`no-ui-slop`), UI Design Review, ux-ui-audit | Community, nicht aktiviert | Überschneiden sich mit Mobbin, den `design:`-Skills und der Jury; nicht nötig |

Vorgehen in Phase 2: je Kernansicht (Projektübersicht, Eingabe, Finanzplan-Tabelle, Szenariovergleich, Sensitivität, Förderung, Bericht) drei bis fünf Referenzen sammeln, das Muster benennen, dem der Entwurf folgt, und festhalten, was bewusst anders gemacht wird.
