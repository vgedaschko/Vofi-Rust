# Aufgaben – VOFI-Immobilienkalkulation

Quelle der Wahrheit für offene Arbeit. Der Hook `.claude/hooks/anything-else.sh` liest diese Datei:
bei Sitzungsstart werden offene Punkte angezeigt, vor jedem Stopp wird geprüft, ob unter „Jetzt" noch etwas offen ist.
Aufgaben als `- [ ] …`; `- [~] …` heißt „läuft im Hintergrund / wartet auf Ergebnis" (hält einen Stopp nicht auf). Nur die Abschnittsüberschriften unten verwenden.

## Jetzt

- [~] Recherchebericht: vierte Überarbeitung nach der Sichtung der Prüfrunde 4 läuft (31 Punkte), danach Prüfrunde 5 als gezielte Nachprüfung (letzte Runde)
- [~] Prüfung der Steuerungsdokumente durch die Rolle Dokumentation läuft (`docs/pruefung/2026-11-18-steuerungsdokumente/`)

## Als Nächstes

- [ ] Fachspezifikation: offene Punkte aus Prüfrunde 3 klären – Renditeformel bei Einlagen und Entnahmen in verschiedenen Perioden, Reihenfolge der Rechenschritte bei der Rundung, nominal/effektiv je Zahlungsart, Buchung von Barzuschüssen, Prozessdefinition der Simulation
- [ ] Recherche zu den fünf bisher nicht untersuchten Anbietern (Reasult, PROBIS und weitere) bis zur Vorprüfung
- [ ] Quellenkataster: als Nächstes am Original lesen – KfW-Merkblatt 459 (Heizungsförderung für Vermieter), niedersächsisches Landesrecht (Mietpreisbremse und Kappungsgrenze, Grunderwerbsteuersatz, Einkommensgrenzen NWoFG), amtliche Fassung BEG EM, De-minimis-Verordnung, gif-Kennzahlen; künftig geltende Fassungen am Bundesgesetzblatt (Verlustvortrag ab 2028)
- [ ] Quellenkataster: Lizenzen klären für DIN 276/277, MF-GIF, BKI-Kennwerte und die KfW-Zinsdatei (16 Einträge)
- [ ] Vorstudie Wirtschaftlichkeit: Eigenbau gegen Kauf und Excel-Ausbau, mit Mengengerüst des Auftraggebers und Aufwandsschätzung nach dem Architekturentwurf
- [ ] Spezifikation Kapitel 2 (Funktionsumfang, Stufen) aus dem überarbeiteten Bericht füllen
- [ ] Spezifikation Kapitel 5 zum Architekturentwurf ausbauen (Datenmodell, Schnittstellen, Rechte, Oberfläche)
- [ ] Spezifikation Kapitel 3 zur vollständigen Fachspezifikation des Rechenkerns ausbauen (Tabellenaufbau, Formeln, Konventionen, Testfälle)
- [ ] Fachliteratur auswerten, sobald der Auftraggeber sie bereitstellt: Grob (VOFI-Gesamtkapitalrendite, Amortisationsdauer), Schulte/Ropeter (Immobilien-VOFI); Fundstellen ins Kataster
- [ ] Fachspezifikation Steuern (aus Prüfrunde 4): Gewerbesteuer der Personengesellschaft beim Verkauf, Veräußerungsgewinn bei erweiterter Kürzung, Bewertung bei laufender Bindung über MA-017 hinaus, Zuschussentgelt in der Kreditprobe, Abstand zur Zielrendite als Endwertüberschuss (MA-012)
- [ ] Quellenkataster: niedersächsisches Haushaltsrecht (VV zu § 44 LHO, ANBest-P; klärt MA-021) und Übergangsrecht zu § 559f BGB am Original lesen – von der Cloud-Umgebung aus bisher nicht erreichbar

## Wartet auf Nutzer

- [ ] **Vor den Anwendergesprächen freigeben:** Schwellen der Vorprüfung. Vorschlag: (1) Bedarf allgemein – die Mehrheit der Befragten würde die Grobkalkulation statt Excel nutzen, sonst Abbruch; (2) Bedarf, der nur den Eigenbau trägt – die Mehrheit braucht Änderungsprotokoll, Arbeit mehrerer Personen an einem Projekt oder Berichte und Zugang für Kunden, sonst Vergleich nur von Kauf und Excel-Ausbau; (3) Mindestfallzahl – die Zeitersparnis über zehn Jahre deckt mindestens den Lizenzpreis des günstigsten vorgeführten Produkts
- [ ] Vorgaben des Hauses (fällig mit der Fachspezifikation): Kalkulationszins, Zielrendite, Höhe der Stressfälle, Beleihungsquote, Mindestdeckung des Schuldendienstes, Anschlusszins, Warnschwellen
- [ ] Vorführungen bei den drei VOFI-Anbietern anfordern (Prüfliste kommt aus Anhang D des Berichts)
- [ ] Anwalt beauftragen (Datenschutz, Mitbestimmung, Nutzungsrechte, Haftung der Beratung) – vor der Bauentscheidung; Steuerberater für die Durchsicht der Steuerlogik – vor dem ersten Kundeneinsatz
- [ ] Zustimmung der KfW zur Nutzung der Zinsdatei einholen, sobald die Lizenzfrage geklärt ist
- [ ] Fachbücher bereitstellen: zuerst „Immobilienökonomie I" (De Gruyter, eBook) und Grob, „Einführung in die Investitionsrechnung" (gebraucht oder Bibliothek); im Gespräch hochladen, nicht ins öffentliche Repository
- [ ] Fachfrage: Ist der geförderte Neubau das Hauptgeschäft? Davon hängt die Reihenfolge der Teilschritte ab
- [ ] Durchsicht der fünf Modellannahmen mit hohem Gewicht (`docs/modellannahmen.md`: MA-001, MA-004, MA-012, MA-014, MA-016) und der zwei Ausnahmen von der Vorsichtsregel (MA-021, MA-022)
- [ ] Fachfrage: Kommt Erbbaurecht bei euren geförderten Neubauten häufig genug vor, um es in Stufe 1 vorzuziehen?
- [ ] Fachfrage: Steht beim Neubau die Frage „gefördert oder frei finanziert" am Anfang der Kalkulation?
- [ ] Im NBank-Gespräch zusätzlich klären: Aufteilung bei teilgeförderten Vorhaben; Zuwendungsfähigkeit von Finanzierungskosten
- [ ] Sichtbarkeit des Repositorys `Vofi-Rust` entscheiden: derzeit öffentlich, enthält interne Planungsunterlagen
- [ ] Gespräch mit der NBank: Rechenweise der Renditeprüfung (Überkompensation) erfragen
- [ ] Drei bis fünf Gespräche mit Anwendern oder Kunden: Würden sie das Werkzeug nutzen, was fehlt ihnen heute?
- [ ] Verantwortung für die Pflege des Regel- und Förderkatalogs im Unternehmen benennen
- [ ] Mengengerüst für die Wirtschaftlichkeitsrechnung: Projekte pro Jahr, Zeitaufwand je Kalkulation heute, Zahl der Nutzer, Anteil geförderter Mietwohnungsbau; für das Beratungsgeschäft Mandate pro Jahr und Honorare


## Später

- [ ] Gestaltungsreferenzen: Lücken schließen vor dem jeweiligen Entwurf – IBCS am Original, Gestaltungssysteme für datendichte Tabellen, Tornado- und Bandbreitendiagramm, Tilgungsplan, Ablauf „Projekt anlegen"
- [ ] Phase 2: Design-Wettbewerbe für die drei prägenden Ansichten (`/designwettbewerb`), daraus das Gestaltungssystem
- [ ] Geplante Aufgaben einrichten, sobald der Regel- und Förderkatalog steht: monatlich Förderkonditionen, vierteljährlich Rechtsstand
- [ ] Projekteigene Skills bauen: `vofi-fachmodell`, `referenzfall-anlegen`, später `foerderprogramm-pflegen`, `steuer-regeln`
- [ ] Phase 3: Einrichtungsskript der Cloud-Umgebung, Prüfkette auf dem Server, Hooks für die Oberfläche
- [ ] Rust-Workspace aufsetzen, CI, SessionStart-Hook für Toolchain in Cloud-Sitzungen
- [ ] Referenzfälle (Golden-Master) aus Lehrbuch-/Excel-VOFI als Tests

## Erledigt

- [x] 2026-11-18 Prüfrunde 4 zum Recherchebericht: Noten 9, 9, 8, 8, 8, 8; gesichtet (31 Punkte); Spezifikation, Entscheidungsprotokoll und Aufgabenliste nachgezogen
- [x] 2026-11-18 Recherchebericht nach Prüfrunde 3 überarbeitet (30 Sichtungspunkte); 25 Modellannahmen, 211 Quellen
- [x] 2026-11-18 Plugin `frontend-design` für das Projekt installiert (Eintrag in `.claude/settings.json`)
- [x] 2026-11-18 Gestaltungsreferenzen: 34 Vorbilder in der Mobbin-Sammlung, ausgewertet in `docs/gestaltungsreferenzen.md`
- [x] 2026-11-18 Gestaltung abgesichert: `frontend-design` als Pflicht, Hook für die Gestaltungsprüfung, Rolle Gestaltung
- [x] 2026-11-18 Prüfrunde 3 zum Recherchebericht: Noten 9, 9, 8, 8, 8, 8; gesichtet; Spezifikation, Kataster und Modellannahmen nachgezogen
- [x] 2026-11-18 Ablauf für den Design-Wettbewerb (`/designwettbewerb`) eingerichtet; Mobbin-Sammlung angelegt
- [x] 2026-11-18 Recherchebericht nach Prüfrunde 2 überarbeitet (30 Sichtungspunkte)
- [x] 2026-11-18 Konvention für Modellannahmen (Spezifikation Kapitel 8) und Verzeichnis mit 15 offenen Annahmen
- [x] 2026-11-18 Normen- und Quellenkataster angelegt und befüllt: 207 Quellen, davon 124 am Original gelesen
- [x] 2026-11-18 Prüfrunde 2 zum Recherchebericht: Noten 7, 7, 7, 8, 8, 8; gesichtet; Spezifikation und Plan nachgezogen
- [x] 2026-11-18 Entwicklungsumgebung mit Probeläufen geprüft; Hooks für Rust und Spezifikations-Merker eingerichtet und getestet
- [x] 2026-11-18 Dokumentationsübersicht mit Pflegegrundsätzen (`docs/README.md`), Rolle Dokumentation als 16. Prüfer
- [x] 2026-11-18 Recherchebericht nach Prüfrunde 1 überarbeitet
- [x] 2026-11-18 Entwicklungsplan mit Phasen, Bestandsaufnahme und Prüfplan → `docs/entwicklungsplan.md`
- [x] 2026-11-18 Lebende Spezifikation `docs/spezifikation.md` angelegt; `docs/entscheidungen.md` ist jetzt das Entscheidungsprotokoll
- [x] 2026-11-17 Prüfrunde 1 zum Recherchebericht: sechs Prüfer plus Lotse, Befunde nachgeprüft und gesichtet
- [x] 2026-11-17 Prüfer eingerichtet: 14 Rollen (inkl. Jurist) in `.claude/agents/`, Ablauf `/pruefrunde`, Regeln und Protokoll in `docs/pruefung/`
- [x] 2026-11-17 Geklärt: Arbeitsstand liegt auf `main` von `Vofi-Rust`; die älteren Repos `VoFi` und `NBank` werden nicht weiterverwendet
- [x] 2026-11-17 Repo `vgedaschko/Vofi-Rust` angelegt und angebunden; Hook, Aufgabenliste und Konzeptdokumente umgezogen
- [x] 2026-11-17 Skill-Empfehlungen → `docs/skills-und-werkzeuge.md`
- [x] 2026-11-17 Fragenkatalog beantwortet → `docs/entscheidungen.md`
- [x] 2026-11-17 „Anything else?"-Hook (SessionStart + Stop) und `/anything-else`-Befehl eingerichtet und getestet
