# Skills und Werkzeuge für das VOFI-Projekt

Stand 2026-11-17. Sortiert nach erwartetem Nutzen. Leitlinie: Was deterministisch geprüft werden kann, gehört in Hooks und CI; Skills sind für Fachwissen und wiederkehrende Abläufe.

## 1. Wirkt am zuverlässigsten: keine Skills, sondern feste Mechanik

| Mechanik | Wofür | Wann einrichten |
|---|---|---|
| `CLAUDE.md` im neuen Repo (`/init`) | Glossar (VOFI-Begriffe), Vorzeichenkonvention, „Geld nie als f64 im Rechenkern", Build-/Testbefehle | Sobald das Repo existiert |
| Hook nach Dateiänderung: `cargo fmt` + `cargo clippy` | Stil und typische Rust-Fehler sofort, ohne dass jemand daran denken muss | Mit dem Rust-Workspace |
| Hook/CI: `cargo test` für den Rechenkern | Jede Formeländerung läuft gegen die Referenzfälle | Mit dem ersten Referenzfall |
| „Anything else?"-Hook + `TASKS.md` | Offene Aufgaben über Sitzungen hinweg | Erledigt |
| Setup-Skript der Cloud-Umgebung | Rust-Toolchain, `wasm32`-Target, `wasm-pack`, `sqlx-cli` in jeder Sitzung vorhanden | Mit dem Rust-Workspace |

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

Sechzehn Prüferrollen in `.claude/agents/`, gestartet über `/pruefrunde`:

| Gruppe | Rollen |
|---|---|
| Fachlich | Fachexperte Immobilien · Finanzmathematiker · Steuerberater · Jurist · Fördermittelberater |
| Nutzer und Entscheider | Praktiker · unbedarfter Endnutzer · Controller · Investor · Bank |
| Qualität | KI-Einheitsbrei/Design · Grenzfälle · Software-Architekt · Revision und Datenschutz · Dokumentation |
| Brücke | Der Lotse (auf Zuruf und an Meilensteinen) |

Die Prüfer lesen nur und berichten; eingearbeitet wird erst nach Gegenprüfung. Ergebnisse stehen in `docs/pruefung/protokoll.md`.

Für Gestaltungsvorbilder stehen die Mobbin-Werkzeuge bereit (Bildschirme und Abläufe realer Anwendungen durchsuchen); sie werden vor jedem Oberflächenentwurf genutzt.

## 6 Hooks (eingerichtet)

| Hook | Auslöser | Wirkung |
|---|---|---|
| `anything-else.sh start` | Sitzungsstart | Zeigt Pflichtlektüre und offene Aufgaben; meldet fehlende Dateien der Pflichtlektüre und Dokumente, die in der Übersicht fehlen |
| `anything-else.sh stop` | Vor jedem Stopp | Hält einmal auf, solange unter „Jetzt" in `TASKS.md` etwas offen ist |
| `spezifikation-merker.sh` | Nach Änderung an Spezifikation oder Entwicklungsplan | Erinnert an Stand-Datum, Entscheidungsprotokoll und Folgeänderungen |
| `rust-format.sh` | Nach Änderung an einer Rust-Datei | Formatiert das Paket |
| `rust-pruefung.sh` | Vor jedem Stopp, wenn sich Rust-Code geändert hat | `clippy` ohne Warnungen und alle Tests; hält bei Fehlern einmal auf |

Dazu kommt der Hook der Cloud-Umgebung, der vor jedem Stopp nicht gesicherte Änderungen meldet. Noch nicht eingerichtet, weil sie vom Projektzuschnitt abhängen: Typprüfung und Lint der Oberfläche, die Prüfkette auf dem Server (Phase 3).
