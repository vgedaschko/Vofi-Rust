# Aufgaben – VOFI-Immobilienkalkulation

Quelle der Wahrheit für offene Arbeit. Der Hook `.claude/hooks/anything-else.sh` liest diese Datei:
bei Sitzungsstart werden offene Punkte angezeigt, vor jedem Stopp wird geprüft, ob unter „Jetzt" noch etwas offen ist.
Aufgaben als `- [ ] …`; `- [~] …` heißt „läuft im Hintergrund / wartet auf Ergebnis" (hält einen Stopp nicht auf). Nur die Abschnittsüberschriften unten verwenden.

## Jetzt

- [~] Recherchebericht wird nach Prüfrunde 1 überarbeitet (Auftrag: `docs/pruefung/2026-11-17-recherchebericht/sichtung.md`); danach zweite Runde mit den Rollen unter 8 und Protokoll

## Als Nächstes

- [ ] Vorstudie Wirtschaftlichkeit: Eigenbau gegen Kauf und Excel-Ausbau, mit Mengengerüst des Auftraggebers und Aufwandsschätzung nach dem Architekturentwurf
- [ ] Anforderungsdokument / Feature-Scope (MVP vs. später) aus Recherche + Antworten ableiten
- [ ] Architekturentwurf (Rechenkern, API, Datenmodell, Mehrbenutzer/Rechte, Frontend)
- [ ] Fachliches Rechenmodell spezifizieren (VOFI-Tabellenstruktur, Kennzahlen, Steuern, Fördermittel)

## Wartet auf Nutzer

- [ ] Gespräch mit der NBank: Rechenweise der Renditeprüfung (Überkompensation) erfragen
- [ ] Drei bis fünf Gespräche mit Anwendern oder Kunden: Würden sie das Werkzeug nutzen, was fehlt ihnen heute?
- [ ] Mengengerüst für die Wirtschaftlichkeitsrechnung: Projekte pro Jahr, Zeitaufwand je Kalkulation heute, Zahl der Nutzer, Anteil geförderter Mietwohnungsbau


## Später

- [ ] Projekteigene Skills bauen: `vofi-fachmodell`, `referenzfall-anlegen`, später `foerderprogramm-pflegen`, `steuer-regeln`
- [ ] Hooks für `cargo fmt`/`clippy`/`test` einrichten, sobald der Rust-Workspace steht
- [ ] Rust-Workspace aufsetzen, CI, SessionStart-Hook für Toolchain in Cloud-Sitzungen
- [ ] Referenzfälle (Golden-Master) aus Lehrbuch-/Excel-VOFI als Tests

## Erledigt

- [x] 2026-11-17 Prüfrunde 1 zum Recherchebericht: sechs Prüfer plus Lotse, Befunde nachgeprüft und gesichtet
- [x] 2026-11-17 Prüfer eingerichtet: 14 Rollen (inkl. Jurist) in `.claude/agents/`, Ablauf `/pruefrunde`, Regeln und Protokoll in `docs/pruefung/`
- [x] 2026-11-17 Geklärt: Arbeitsstand liegt auf `main` von `Vofi-Rust`; die älteren Repos `VoFi` und `NBank` werden nicht weiterverwendet
- [x] 2026-11-17 Repo `vgedaschko/Vofi-Rust` angelegt und angebunden; Hook, Aufgabenliste und Konzeptdokumente umgezogen
- [x] 2026-11-17 Skill-Empfehlungen → `docs/skills-und-werkzeuge.md`
- [x] 2026-11-17 Fragenkatalog beantwortet → `docs/entscheidungen.md`
- [x] 2026-11-17 „Anything else?"-Hook (SessionStart + Stop) und `/anything-else`-Befehl eingerichtet und getestet
