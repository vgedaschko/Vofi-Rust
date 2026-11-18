# Entwicklungsplan

Reihenfolge der Arbeit, Freigabepunkte und Prüfungen. Der Inhalt dessen, was gebaut wird, steht in `docs/spezifikation.md`; hier steht, in welcher Folge und mit welcher Absicherung.

**Stand:** 2026-11-18 · Phase 0 läuft. Termine und Aufwand werden erst nach dem Architekturentwurf (Phase 2) beziffert; vorher wären Zahlen geraten.

## 1 Phasen

Jede Phase endet mit einem Freigabepunkt. Ohne Freigabe des Auftraggebers beginnt die nächste nicht.

| Phase | Ergebnis | Prüfer | Freigabepunkt |
|---|---|---|---|
| **0 Grundlagen** (läuft) | Recherchebericht mit mindestens 9 von 10 in der Prüfrunde; Spezifikation angelegt; Prüfer, Aufgabenliste und Erinnerungs-Hook eingerichtet | Fachexperte, Finanzmathematiker, Investor, Praktiker, Jurist, Einheitsbrei-Prüfer, Lotse | Bericht abgenommen; Kapitel 2 der Spezifikation gefüllt |
| **Vorprüfung** (beim Auftraggeber, parallel zu Phase 1) | Gespräch mit der NBank über die Rechenweise der Renditeprüfung; drei bis fünf Gespräche mit Anwendern oder Kunden, auch zur Frage der Mehrpersonenarbeit; Vorführungen der drei VOFI-Anbieter; Benennung der Katalogverantwortung; Mengengerüst einschließlich Beratungsgeschäft. Vom Projekt beizusteuern: Recherche zu den fünf bisher nicht untersuchten Anbietern | – | **Erster Freigabepunkt, vor Beginn der Phase 2:** Tragen die Ergebnisse das Vorhaben? Bei Abbruch bleibt die Fachspezifikation aus Phase 1 verwertbar – als Pflichtenheft für eine gekaufte Lösung oder als Bauplan für ein Excel-Modell |
| **1 Fachspezifikation** | Rechenkern vollständig beschrieben (Tabellenaufbau, Formeln, Konventionen, Randfälle, Referenzfälle); Datenmodell des Regel- und Förderkatalogs mit Erstbefüllung NBank und KfW; Umfang der Stufe 1 als prüfbare Anforderungen; Kennzahlenblatt je Vorhabensart | Finanzmathematiker (Fable), Fachexperte, Steuerberater, Jurist, Fördermittelberater, Controller, Grenzfälle, Praktiker | **Fachliche Freigabe** durch den Auftraggeber: Rechnet das Werkzeug so, wie Sie rechnen würden? |
| **2 Architektur und Vorstudie** | Architekturentwurf (Datenmodell, Schnittstellen, Rechte, Änderungsprotokoll, Datenschutzkonzept); Gestaltungssystem und klickbare Entwürfe der Kernansichten: für die drei prägenden Ansichten (Finanzplan-Tabelle, Eingabe der Annahmen, Kennzahlenblatt mit Bericht) je ein Design-Wettbewerb mit mindestens fünf Teilnehmern und verdeckter Jury (`/designwettbewerb`), die übrigen nach dem dort gefundenen System; Aufwandsschätzung; Wirtschaftlichkeitsrechnung Eigenbau gegen Kauf und Excel-Ausbau | Architekt (Fable), Revision, Jurist, Controller, Praktiker, Endnutzer, Einheitsbrei-Prüfer, Investor | **Bauentscheidung**: bauen, kaufen oder lassen – mit Zahlen |
| **3 Technisches Fundament** | Rust-Arbeitsbereich, automatische Prüfkette, Projekt-Skills, Testgerüst mit den Referenzfällen; ein Durchstich: eine Eingabe läuft durch Rechenkern (Server und Browser), Anzeige und Änderungsprotokoll | Architekt, Grenzfälle | Durchstich vorgeführt |
| **4 Stufe 1 in Teilschritten** | Teilschritte nach dem Zuschnitt in Spezifikation Kapitel 2, jeder mit nutzbarem Ergebnis und eigener Freigabe; der erste liefert eine belegbare Grobkalkulation | je Teilschritt nach Tabelle in `/pruefrunde` | **Abnahme Stufe 1**: Parallelrechnung mit echten Projekten des Auftraggebers gegen die bisherige Excel-Kalkulation |
| **5 Stufen 2 bis 4** | Nach Spezifikation: Sanierung und Simulation · Entwicklung mit Verkauf und Gewerbe · Sonderimmobilien und Unternehmensebene | wie Phase 4 | je Stufe Freigabe mit vorher benannten Abbruchkriterien |

Die Fachspezifikation (Phase 1) läuft parallel zur Vorprüfung, weil sie in jedem Fall verwertbar bleibt. Architektur, Gestaltung und Aufwandsschätzung (Phase 2) beginnen erst nach bestandener Vorprüfung. Ebenfalls beim Auftraggeber: Beschaffung der Lehrbücher, Klärung von Datenschutz und Mitbestimmung vor der Spezifikation des Änderungsprotokolls.

## 2 Grundlagen – was vorhanden ist und was fehlt

| Bereich | Vorhanden | Fehlt | Fällig |
|---|---|---|---|
| Steuerung | Spezifikation mit Status je Festlegung, Entscheidungsprotokoll, Aufgabenliste mit Erinnerungs-Hook, dieser Plan | – | – |
| Dokumentation | Übersicht mit Pflegegrundsätzen (`docs/README.md`); Projektdokumentation vollständig | Anwendungsdokumentation (Fachhandbuch, Katalog, Benutzerhandbuch, Architektur, Betrieb, Änderungshistorie) | je Dokument ab Phase 1 bis 4, siehe Übersicht |
| Quellen | Normen- und Quellenkataster mit Erzeuger und Prüfmodus | Lesen der noch nicht am Original geprüften Quellen; Lizenzen für Normen und Kennwerte | laufend; Lizenzen vor Phase 3 |
| Modellannahmen | Konvention (Spezifikation Kapitel 8) und Verzeichnis mit 15 offenen Annahmen, Erzeuger mit Prüfmodus | Klärung über NBank, Anwalt, Steuerberater, Fachliteratur; Kennzeichnung in Katalog, Code und Tests | Kennzeichnung ab Phase 1 und 3; Klärung laufend |
| Recherche | Bericht (in Überarbeitung), neun Quellnotizen, am Original geprüfte Rechts- und Förderangaben, drei nachgerechnete Referenzfälle mit Skripten | Lehrbuchdefinitionen (Grob; Schulte/Ropeter) am Original | Phase 1 |
| Fachspezifikation | Leitlinien in Spezifikation Kapitel 3 und 4 | Vollständige Rechenkern-Spezifikation; Katalog-Datenmodell; Anforderungen Stufe 1 | Phase 1 |
| Architektur und Gestaltung | Grundsatzentscheidungen in Spezifikation Kapitel 5 und 6 | Architekturentwurf; Gestaltungssystem; Datenschutzkonzept | Phase 2 |
| Prüfung | 17 Prüferrollen, Ablauf `/pruefrunde`, gemeinsame Regeln, Protokoll | – | – |
| Skills | Eingebaut: `/code-review`, `/security-review`, `/simplify`, Tabellen-, PDF-, Diagramm- und Gestaltungs-Skills, Recherche | Projekt-Skills `vofi-fachmodell`, `referenzfall-anlegen`, `foerderprogramm-pflegen`, `steuer-regeln`; Plugins „Engineering" und „Product Management" sind vorgeschlagen, aber nicht aktiviert (nützlich, nicht notwendig) | Projekt-Skills mit Phase 1 und 3 |
| Entwicklungsumgebung | Am 18.11.2026 mit Probeläufen bestätigt, siehe Abschnitt 2a | Rust-Arbeitsbereich und Oberflächenprojekt; Einrichtungsskript der Cloud-Umgebung; Prüfkette auf dem Server | Phase 3 |
| Automatische Prüfkette | Hooks für Formatierung nach jeder Änderung und für Lint und Tests vor jedem Stopp (getestet, wirksam ab der ersten Rust-Datei); Merker bei Änderungen an Spezifikation und Plan | Dieselbe Kette auf dem Server (GitHub Actions); Prüfungen für die Oberfläche; Abhängigkeitsprüfung | Phase 3 |
| Wirtschaftlichkeit | – | Vorstudie mit Mengengerüst und Aufwandsschätzung | Phase 2 |

Bewertung: Für Phase 0 und 1 ist alles Nötige da. Die technischen Werkzeuge der Phase 3 jetzt schon einzurichten wäre verfrüht, weil ihr Zuschnitt vom Architekturentwurf abhängt.

## 2a Bereitschaft für den Programmierstart

Geprüft am 18.11.2026 mit Probeläufen in der Cloud-Umgebung „VOFI Immobilienkalkulation".

| Baustein | Befund | Beleg |
|---|---|---|
| Rust-Werkzeuge | bereit | Rust 1.97 mit `clippy` und `rustfmt`; Probepaket mit exakter Dezimalrechnung gebaut und getestet |
| WebAssembly | bereit | Dasselbe Probepaket für den Browser gebaut und in Node ausgeführt |
| Bibliotheken aus den Paketregistern | bereit | Abruf von crates.io und npm funktioniert |
| Oberflächen-Werkzeuge | bereit | Node 22, `pnpm`; Vite, TypeScript und Vitest installierbar; Chromium für Oberflächentests vorhanden |
| Datenbank | bereit | PostgreSQL 16 vorinstalliert, gestartet, Geldbeträge exakt summiert |
| Rechenleistung | ausreichend | 4 Prozessorkerne, 15 GB Arbeitsspeicher, 30 GB frei |
| Hooks | bereit | Formatierung, Lint und Tests gegen ein Probepaket getestet, einschließlich Fehlerfall |
| WebAssembly-Bindewerkzeug | nachzuinstallieren | `wasm-bindgen-cli` in rund einer Minute installiert; geht bei einem Neustart der Umgebung verloren |

Vor der ersten Zeile Produktcode noch zu tun (Phase 3, je rund ein Arbeitsgang):

1. Rust-Arbeitsbereich und Oberflächenprojekt nach dem Architekturentwurf anlegen.
2. Einrichtungsskript der Cloud-Umgebung: Bindewerkzeug in der festgelegten Version installieren, Datenbank starten.
3. Prüfkette auf dem Server (GitHub Actions): Format, Lint, Tests, WebAssembly-Bau, Abhängigkeitsprüfung.
4. Hooks für die Oberfläche (Typprüfung, Lint).
5. Projekt-Skills `vofi-fachmodell` und `referenzfall-anlegen`.
6. Sichtbarkeit des Repositorys entscheiden: `Vofi-Rust` ist derzeit öffentlich.

Betriebsrisiko: Die Cloud-Umgebung wurde am 17./18.11.2026 zweimal neu gestartet; dabei gehen laufende Hintergrundarbeiten und nachinstallierte Werkzeuge verloren. Gegenmaßnahmen: früh und abschnittsweise speichern, Zwischenstände auf dem Arbeitszweig sichern, Werkzeuge über das Einrichtungsskript statt von Hand installieren.

Die Umgebung ist damit nicht der Engpass. Was den Programmierstart bestimmt, sind die Ergebnisse der Phasen 1 und 2: die Fachspezifikation des Rechenkerns und der Architekturentwurf.

## 3 Prüfplan

| Anlass oder Turnus | Was wird geprüft | Werkzeug | Status |
|---|---|---|---|
| Jeder Sitzungsstart und jeder Stopp | Offene Aufgaben; Pflichtlektüre und Dokumentationsübersicht stimmen mit dem Bestand überein | Hook `anything-else.sh` mit `TASKS.md` | aktiv |
| Jedes Arbeitsergebnis (Bericht, Spezifikationskapitel, Entwurf, Rechenfunktion) | Fachlich, rechnerisch, rechtlich, aus Nutzer- und Entscheidersicht | `/pruefrunde` mit den passenden Rollen, wiederholt bis mindestens 9 von 10 (Abbruchregeln siehe dort) | aktiv |
| Jede Antwort des Auftraggebers, jede Prüfrunde | Berührt das eine Festlegung? | Abgleich mit `docs/spezifikation.md`, Eintrag in `docs/entscheidungen.md`; Hook `spezifikation-merker.sh` erinnert bei jeder Änderung an Spezifikation oder Plan an die Folgepflichten | aktiv |
| Jede Codeänderung | Format, typische Fehler, Tests | Hooks `rust-format.sh` (nach jeder Änderung) und `rust-pruefung.sh` (vor jedem Stopp: `clippy` ohne Warnungen, alle Tests) | eingerichtet, wirksam ab der ersten Rust-Datei; Server-Kette ab Phase 3 |
| Jede Änderung am Rechenkern | Referenzfälle, Eigenschaftstests (Finanzierungssaldo null, Kontrollsummen), Ergebnisgleichheit Server und Browser | Testgerüst in der Prüfkette; Rolle Finanzmathematiker bei Formeländerungen | ab Phase 3 |
| Jede Zusammenführung von Code | Korrektheit, Wartbarkeit | `/code-review`; Rolle Architekt bei größeren Änderungen | ab Phase 3 |
| Jede Änderung an Anmeldung, Rechten, Kundenzugang, Datenhaltung | Sicherheit, Datenschutz, Nachweisbarkeit | `/security-review`; Rollen Revision und Jurist | ab Phase 3 |
| Jede prägende Ansicht vor dem ersten Entwurf | Lösungsraum: mindestens fünf Entwürfe in verschiedenen Richtungen, verdeckt bewertet | `/designwettbewerb`; Entscheidung beim Auftraggeber | ab Phase 2 |
| Jede Änderung an Oberflächendateien | Gestaltung am gerenderten Ergebnis: Designkritik, Barrierefreiheit, IBCS, Einheitsbrei | Hook `gestaltung.sh` erzwingt die Prüfung vor dem Stopp; Rolle Gestaltung mit `frontend-design` als Maßstab, `design:design-critique`, `design:accessibility-review`, `design:ux-copy`, `dataviz` | eingerichtet, wirksam ab der ersten Oberflächendatei |
| Jede Oberfläche vor Freigabe | Bedienung und Verständlichkeit aus Nutzersicht | Rollen Gestaltung, Praktiker, Endnutzer, Einheitsbrei-Prüfer, Controller über `/pruefrunde` | ab Phase 2 |
| Jeder Freigabepunkt | Gesamtbild und Zielkonflikte; Abgleich Spezifikation gegen Ergebnis | Volle Runde einschließlich Lotse, Jurist, Revision, Controller | ab Phase 1 |
| Jeder Freigabepunkt | Offene Modellannahmen: Ist eine inzwischen klärbar oder geklärt? Stimmt die vorsichtige Voreinstellung noch? Vor dem Kundeneinsatz keine offene Annahme mit hohem Gewicht ohne Freigabe des Auftraggebers | Durchsicht von `docs/modellannahmen.md`; je Klärungsweg die zuständige Rolle (Jurist, Steuerberater, Fördermittelberater, Finanzmathematiker) | aktiv |
| Bei jeder Änderung und bei jedem Sitzungsstart | Verzeichnis der Modellannahmen vollständig; jede im Projekt genannte Kennung ist verzeichnet; genannte Quellen stehen im Quellenkataster | `python3 scripts/modellannahmen.py --pruefen`; der Hook `anything-else.sh` meldet Fehler beim Sitzungsstart | aktiv |
| Jeder Freigabepunkt und nach größeren Änderungen | Dokumentation als Ganzes: aktuell, widerspruchsfrei, auffindbar, ohne Dopplungen; Anwendungsdokumentation gegen tatsächliches Verhalten | Rolle Dokumentation gegen `docs/README.md` | aktiv |
| Abnahme einer Stufe | Stimmen die Ergebnisse mit echten Fällen? | Parallelrechnung gegen Excel-Kalkulationen des Auftraggebers; Rolle Grenzfälle | ab Phase 4 |
| Wöchentlich | Sicherheitslücken und Lizenzen der eingesetzten Bibliotheken | `cargo-deny`, `cargo-audit`, `pnpm audit` als geplanter Lauf der Prüfkette | ab Phase 3 |
| Monatlich | Förderdokumente und Zinsen: alle Katastereinträge mit Turnus „monatlich" gegen die Originale bei KfW, BAFA, NBank | Geplante Aufgabe mit Rolle Fördermittelberater und Skill `pdf`; trägt Lesedatum und Fassung im Quellenkataster nach und meldet Abweichungen | einrichtbar, sobald das Kataster befüllt ist |
| Vierteljährlich und zum Jahreswechsel | Rechtsstand: alle Katastereinträge mit Turnus „vierteljährlich" am Gesetzestext; laufende Gesetzgebung | Geplante Aufgabe mit Rollen Jurist und Steuerberater; trägt Lesedatum und Fassung im Quellenkataster nach und meldet Abweichungen | einrichtbar, sobald das Kataster befüllt ist |
| Bei jeder Änderung am Kataster und bei jedem Sitzungsstart | Kataster vollständig ausgefüllt, Kennungen eindeutig, erzeugte Übersicht aktuell | `python3 scripts/quellenkataster.py --pruefen`; der Hook `anything-else.sh` meldet Fehler beim Sitzungsstart | aktiv |
| Halbjährlich | Wettbewerber und Markt | Skill `deep-research` | ab Bauentscheidung |

Die zeitgesteuerten Prüfungen laufen als geplante Aufgaben in einer eigenen Sitzung und melden nur Abweichungen. Sie werden eingerichtet, wenn es einen Katalog gibt, gegen den sie prüfen können.
