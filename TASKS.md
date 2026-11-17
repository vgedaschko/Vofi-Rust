# Aufgaben – VOFI-Immobilienkalkulation

Quelle der Wahrheit für offene Arbeit. Der Hook `.claude/hooks/anything-else.sh` liest diese Datei:
bei Sitzungsstart werden offene Punkte angezeigt, vor jedem Stopp wird geprüft, ob unter „Jetzt" noch etwas offen ist.
Aufgaben als `- [ ] …`; `- [~] …` heißt „läuft im Hintergrund / wartet auf Ergebnis" (hält einen Stopp nicht auf). Nur die Abschnittsüberschriften unten verwenden.

## Jetzt

- [ ] Recherchenotizen und Bericht nach Abschluss aus der Sitzung in dieses Repo übernehmen (`research_notes/`, `reports/`)
- [~] Recherche: bestehende Lösungen (VOFI-/Immobilienkalkulationssoftware) und ihr Funktionsumfang
- [~] Best Practices darstellen (VOFI-Methodik, Finanzmodellierung, Softwarearchitektur)
- [~] Fachberatung Einsatzgebiet Immobilien: wichtige Features, Kennzahlen, Fördermodule (KfW, NBank)
- [~] Einschätzung: Rust durchgängig sinnvoll oder Ausnahmen (v. a. Frontend)?

## Als Nächstes

- [ ] Anforderungsdokument / Feature-Scope (MVP vs. später) aus Recherche + Antworten ableiten
- [ ] Architekturentwurf (Rechenkern, API, Datenmodell, Mehrbenutzer/Rechte, Frontend)
- [ ] Fachliches Rechenmodell spezifizieren (VOFI-Tabellenstruktur, Kennzahlen, Steuern, Fördermittel)

## Wartet auf Nutzer

- [ ] Entscheiden: Arbeitsstand von Branch `ccr-f9f11dfd-jz4kva` nach `main` übernehmen?
- [ ] Klären: Enthalten die älteren Repos `VoFi` und `NBank` Vorarbeiten, die einfließen sollen?

## Später

- [ ] Projekteigene Skills bauen: `vofi-fachmodell`, `referenzfall-anlegen`, später `foerderprogramm-pflegen`, `steuer-regeln`
- [ ] Hooks für `cargo fmt`/`clippy`/`test` einrichten, sobald der Rust-Workspace steht
- [ ] Rust-Workspace aufsetzen, CI, SessionStart-Hook für Toolchain in Cloud-Sitzungen
- [ ] Referenzfälle (Golden-Master) aus Lehrbuch-/Excel-VOFI als Tests

## Erledigt

- [x] 2026-11-17 Repo `vgedaschko/Vofi-Rust` angelegt und angebunden; Hook, Aufgabenliste und Konzeptdokumente umgezogen
- [x] 2026-11-17 Skill-Empfehlungen → `docs/skills-und-werkzeuge.md`
- [x] 2026-11-17 Fragenkatalog beantwortet → `docs/entscheidungen.md`
- [x] 2026-11-17 „Anything else?"-Hook (SessionStart + Stop) und `/anything-else`-Befehl eingerichtet und getestet
