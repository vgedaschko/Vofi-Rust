# Entwicklungsplan

Reihenfolge der Arbeit, Freigabepunkte und Prüfungen. Der Inhalt dessen, was gebaut wird, steht in `docs/spezifikation.md`; hier steht, in welcher Folge und mit welcher Absicherung.

**Stand:** 2026-11-18 · Phase 0 läuft. Termine und Aufwand werden erst nach dem Architekturentwurf (Phase 2) beziffert; vorher wären Zahlen geraten.

## 1 Phasen

Jede Phase endet mit einem Freigabepunkt. Ohne Freigabe des Auftraggebers beginnt die nächste nicht.

| Phase | Ergebnis | Prüfer | Freigabepunkt |
|---|---|---|---|
| **0 Grundlagen** (läuft) | Recherchebericht mit mindestens 9 von 10 in der Prüfrunde; Spezifikation angelegt; Prüfer, Aufgabenliste und Erinnerungs-Hook eingerichtet | Fachexperte, Finanzmathematiker, Investor, Praktiker, Jurist, Einheitsbrei-Prüfer, Lotse | Bericht abgenommen; Kapitel 2 der Spezifikation gefüllt |
| **1 Fachspezifikation** | Rechenkern vollständig beschrieben (Tabellenaufbau, Formeln, Konventionen, Randfälle, Referenzfälle); Datenmodell des Regel- und Förderkatalogs mit Erstbefüllung NBank und KfW; Umfang der Stufe 1 als prüfbare Anforderungen; Kennzahlenblatt je Vorhabensart | Finanzmathematiker (Fable), Fachexperte, Steuerberater, Jurist, Fördermittelberater, Controller, Grenzfälle, Praktiker | **Fachliche Freigabe** durch den Auftraggeber: Rechnet das Werkzeug so, wie Sie rechnen würden? |
| **2 Architektur und Vorstudie** | Architekturentwurf (Datenmodell, Schnittstellen, Rechte, Änderungsprotokoll, Datenschutzkonzept); Gestaltungssystem und klickbarer Entwurf der Kernansichten nach benannten Vorbildern; Aufwandsschätzung; Wirtschaftlichkeitsrechnung Eigenbau gegen Kauf und Excel-Ausbau | Architekt (Fable), Revision, Jurist, Controller, Praktiker, Endnutzer, Einheitsbrei-Prüfer, Investor | **Bauentscheidung**: bauen, kaufen oder lassen – mit Zahlen |
| **3 Technisches Fundament** | Rust-Arbeitsbereich, automatische Prüfkette, Projekt-Skills, Testgerüst mit den Referenzfällen; ein Durchstich: eine Eingabe läuft durch Rechenkern (Server und Browser), Anzeige und Änderungsprotokoll | Architekt, Grenzfälle | Durchstich vorgeführt |
| **4 Stufe 1 in Teilschritten** | 1a Rechenkern gegen Referenzfälle · 1b Grobkalkulation von Eingabe bis Kennzahl · 1c Förderung und Steuern · 1d Mehrbenutzerbetrieb, Rollen, Arbeitsstände · 1e Berichte, Exporte, Sensitivität | je Teilschritt nach Tabelle in `/pruefrunde` | **Abnahme Stufe 1**: Parallelrechnung mit echten Projekten des Auftraggebers gegen die bisherige Excel-Kalkulation |
| **5 Stufen 2 bis 4** | Nach Spezifikation: Sanierung und Simulation · Entwicklung mit Verkauf und Gewerbe · Sonderimmobilien und Unternehmensebene | wie Phase 4 | je Stufe Freigabe mit vorher benannten Abbruchkriterien |

Parallel beim Auftraggeber, spätestens bis zur Bauentscheidung: Gespräch mit der NBank, Gespräche mit Anwendern oder Kunden, Mengengerüst, Benennung der Katalogverantwortung, Beschaffung der Lehrbücher.

## 2 Grundlagen – was vorhanden ist und was fehlt

| Bereich | Vorhanden | Fehlt | Fällig |
|---|---|---|---|
| Steuerung | Spezifikation mit Status je Festlegung, Entscheidungsprotokoll, Aufgabenliste mit Erinnerungs-Hook, dieser Plan | – | – |
| Dokumentation | Übersicht mit Pflegegrundsätzen (`docs/README.md`); Projektdokumentation vollständig | Anwendungsdokumentation (Fachhandbuch, Katalog, Benutzerhandbuch, Architektur, Betrieb, Änderungshistorie) | je Dokument ab Phase 1 bis 4, siehe Übersicht |
| Recherche | Bericht (in Überarbeitung), neun Quellnotizen, am Original geprüfte Rechts- und Förderangaben, drei nachgerechnete Referenzfälle mit Skripten | Lehrbuchdefinitionen (Grob; Schulte/Ropeter) am Original | Phase 1 |
| Fachspezifikation | Leitlinien in Spezifikation Kapitel 3 und 4 | Vollständige Rechenkern-Spezifikation; Katalog-Datenmodell; Anforderungen Stufe 1 | Phase 1 |
| Architektur und Gestaltung | Grundsatzentscheidungen in Spezifikation Kapitel 5 und 6 | Architekturentwurf; Gestaltungssystem; Datenschutzkonzept | Phase 2 |
| Prüfung | 16 Prüferrollen, Ablauf `/pruefrunde`, gemeinsame Regeln, Protokoll | – | – |
| Skills | Eingebaut: `/code-review`, `/security-review`, `/simplify`, Tabellen-, PDF-, Diagramm- und Gestaltungs-Skills, Recherche | Projekt-Skills `vofi-fachmodell`, `referenzfall-anlegen`, `foerderprogramm-pflegen`, `steuer-regeln`; Plugins „Engineering" und „Product Management" sind vorgeschlagen, aber nicht aktiviert (nützlich, nicht notwendig) | Projekt-Skills mit Phase 1 und 3 |
| Entwicklungsumgebung | Rust 1.97 mit `clippy`, `rustfmt` und WebAssembly-Ziel; Node 22 mit `pnpm`; PostgreSQL-Client; Cloud-Umgebung mit freigegebenen Quellen (KfW, NBank, BAFA, Gesetze) | Einrichtungsskript für Zusatzwerkzeuge (`wasm-pack`, `cargo-nextest`, `cargo-deny`, `sqlx-cli`); Rust-Arbeitsbereich; Oberflächenprojekt | Phase 3 |
| Automatische Prüfkette | – | Hooks für Format, Lint und Tests; Prüfkette bei jeder Änderung auf dem Server; Abhängigkeitsprüfung | Phase 3 |
| Wirtschaftlichkeit | – | Vorstudie mit Mengengerüst und Aufwandsschätzung | Phase 2 |

Bewertung: Für Phase 0 und 1 ist alles Nötige da. Die technischen Werkzeuge der Phase 3 jetzt schon einzurichten wäre verfrüht, weil ihr Zuschnitt vom Architekturentwurf abhängt.

## 3 Prüfplan

| Anlass oder Turnus | Was wird geprüft | Werkzeug | Status |
|---|---|---|---|
| Jeder Sitzungsstart und jeder Stopp | Offene Aufgaben | Hook `anything-else.sh` mit `TASKS.md` | aktiv |
| Jedes Arbeitsergebnis (Bericht, Spezifikationskapitel, Entwurf, Rechenfunktion) | Fachlich, rechnerisch, rechtlich, aus Nutzer- und Entscheidersicht | `/pruefrunde` mit den passenden Rollen, wiederholt bis mindestens 9 von 10 (Abbruchregeln siehe dort) | aktiv |
| Jede Antwort des Auftraggebers, jede Prüfrunde | Berührt das eine Festlegung? | Abgleich mit `docs/spezifikation.md`, Eintrag in `docs/entscheidungen.md` | aktiv |
| Jede Codeänderung | Format, typische Fehler, Tests | Hooks mit `cargo fmt`, `cargo clippy`, `cargo test`; dieselbe Kette auf dem Server | ab Phase 3 |
| Jede Änderung am Rechenkern | Referenzfälle, Eigenschaftstests (Finanzierungssaldo null, Kontrollsummen), Ergebnisgleichheit Server und Browser | Testgerüst in der Prüfkette; Rolle Finanzmathematiker bei Formeländerungen | ab Phase 3 |
| Jede Zusammenführung von Code | Korrektheit, Wartbarkeit | `/code-review`; Rolle Architekt bei größeren Änderungen | ab Phase 3 |
| Jede Änderung an Anmeldung, Rechten, Kundenzugang, Datenhaltung | Sicherheit, Datenschutz, Nachweisbarkeit | `/security-review`; Rollen Revision und Jurist | ab Phase 3 |
| Jede Oberfläche vor Freigabe | Bedienung, Verständlichkeit, Barrierefreiheit, Gestaltung | Rollen Praktiker, Endnutzer, Einheitsbrei-Prüfer; Skills `design:design-critique`, `design:accessibility-review`, `dataviz` | ab Phase 2 |
| Jeder Freigabepunkt | Gesamtbild und Zielkonflikte; Abgleich Spezifikation gegen Ergebnis | Volle Runde einschließlich Lotse, Jurist, Revision, Controller | ab Phase 1 |
| Jeder Freigabepunkt und nach größeren Änderungen | Dokumentation als Ganzes: aktuell, widerspruchsfrei, auffindbar, ohne Dopplungen; Anwendungsdokumentation gegen tatsächliches Verhalten | Rolle Dokumentation gegen `docs/README.md` | aktiv |
| Abnahme einer Stufe | Stimmen die Ergebnisse mit echten Fällen? | Parallelrechnung gegen Excel-Kalkulationen des Auftraggebers; Rolle Grenzfälle | ab Phase 4 |
| Wöchentlich | Sicherheitslücken und Lizenzen der eingesetzten Bibliotheken | `cargo-deny`, `cargo-audit`, `pnpm audit` als geplanter Lauf der Prüfkette | ab Phase 3 |
| Monatlich | Förderkonditionen und Zinsen gegen KfW, BAFA, NBank | Geplante Aufgabe mit Rolle Fördermittelberater und Skill `pdf` | einrichtbar, sobald der Katalog steht (Phase 1) |
| Vierteljährlich und zum Jahreswechsel | Rechtsstand: Steuern, Mietrecht, laufende Gesetzgebung | Geplante Aufgabe mit Rollen Jurist und Steuerberater | einrichtbar, sobald der Katalog steht (Phase 1) |
| Halbjährlich | Wettbewerber und Markt | Skill `deep-research` | ab Bauentscheidung |

Die zeitgesteuerten Prüfungen laufen als geplante Aufgaben in einer eigenen Sitzung und melden nur Abweichungen. Sie werden eingerichtet, wenn es einen Katalog gibt, gegen den sie prüfen können.
