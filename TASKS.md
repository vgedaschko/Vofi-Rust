# Aufgaben – VOFI-Immobilienkalkulation

Quelle der Wahrheit für offene Arbeit; Stand ist der letzte Eintrag unter „Erledigt". Leser: Auftraggeber (Abschnitt „Wartet auf Nutzer") und Entwicklung. Der Hook `.claude/hooks/anything-else.sh` liest diese Datei:
bei Sitzungsstart werden offene Punkte angezeigt, vor jedem Stopp wird geprüft, ob unter „Jetzt" noch etwas offen ist.
Aufgaben als `- [ ] …`; `- [~] …` heißt „läuft im Hintergrund / wartet auf Ergebnis" (hält einen Stopp nicht auf). Nur die Abschnittsüberschriften unten verwenden.

## Jetzt

- [~] Fachspezifikation des Rechenkerns: Prüfrunde 2 mit denselben sieben Rollen und Blindrechnung der Referenzfälle durch einen zweiten Bearbeiter laufen → `docs/pruefung/2026-11-18-fachspezifikation-rechenkern-runde2/`

## Als Nächstes

- [ ] Nach dem NBank-Gespräch: Antworten mit Datum und Gesprächspartner im Verzeichnis der Modellannahmen nachtragen (Status, Voreinstellung), Spezifikation und Katalogvorgaben nachziehen
- [ ] Fachspezifikation: offene Punkte aus Prüfrunde 3 klären – Renditeformel bei Einlagen und Entnahmen in verschiedenen Perioden, Reihenfolge der Rechenschritte bei der Rundung, nominal/effektiv je Zahlungsart, Buchung von Barzuschüssen, Prozessdefinition der Simulation
- [ ] Recherche zu den fünf bisher nicht untersuchten Anbietern (Reasult, PROBIS und weitere) bis zur Vorprüfung
- [ ] Quellenkataster und Katalog für die vier weiteren Länder (Bremen, Hamburg, Schleswig-Holstein, Nordrhein-Westfalen): Grunderwerbsteuersätze, Verordnungen zu Mietpreisbremse und Kappungsgrenze am Original lesen und eintragen; dafür werden Landesrechtsportale gebraucht, die die Cloud-Umgebung bisher nicht erreicht
- [ ] Zuschnitt nachziehen (Fachspezifikation, Kapitel 2): KfW-Neubaudarlehen 297/298 und 296 in Teilschritt 1b-2 statt 1c; Prüfen, was von den KfW-Programmen für den Bestand schon in 1b-1 gebraucht wird
- [ ] Quellenkataster: als Nächstes am Original lesen – KfW-Merkblatt 459 (Heizungsförderung für Vermieter), niedersächsisches Landesrecht (Mietpreisbremse und Kappungsgrenze, Grunderwerbsteuersatz, Einkommensgrenzen NWoFG), amtliche Fassung BEG EM, De-minimis-Verordnung, gif-Kennzahlen; künftig geltende Fassungen am Bundesgesetzblatt (Verlustvortrag ab 2028)
- [ ] Quellenkataster: Mindestkapitalisierungszinssätze der BaFin am Original nachziehen
- [ ] Recherche zum Erbbaurecht, falls es nach der Antwort auf die Fachfrage vorgezogen wird
- [ ] Prüfliste für die Herstellervorführungen aus Anhang D des Berichts ableiten (vor der Vorprüfung)
- [ ] Quellenkataster: Lizenzen klären für DIN 276/277, MF-GIF, BKI-Kennwerte und die KfW-Zinsdatei (16 Einträge)
- [ ] Vorstudie Wirtschaftlichkeit: Eigenbau gegen Kauf und Excel-Ausbau, mit Mengengerüst des Auftraggebers und Aufwandsschätzung nach dem Architekturentwurf
- [ ] Spezifikation Kapitel 2 (Funktionsumfang, Stufen) aus dem überarbeiteten Bericht füllen
- [ ] Spezifikation Kapitel 5 zum Architekturentwurf ausbauen (Datenmodell, Schnittstellen, Rechte, Oberfläche)
- [ ] Spezifikation Kapitel 3 zur vollständigen Fachspezifikation des Rechenkerns ausbauen (Tabellenaufbau, Formeln, Konventionen, Testfälle)
- [ ] II. BV: amtliche oder verbandliche Veröffentlichung der Beträge ab 01.01.2026 beschaffen (aus dem heutigen Preisindex nicht nachrechenbar, Notiz 10)
- [ ] Fachspezifikation Rechenkern (aus Quellnotiz 11): Unterlassensalternative als eigener Finanzplan mit zwei Zinssätzen und Vergleichsfaktor der Rendite dazu (MA-012); „freie Tilgung" (Periodenüberschuss tilgt) als benannte Tilgungsart; Lehrbuchdarstellung als Ansicht; die beiden Musterrechnungen als automatische Tests
- [ ] Fachspezifikation Finanzierung (aus Prüfrunde 5): Anschlusszins und Tilgung nach Ende der Zinsbindung, auch für übernommene Förderdarlehen; Vorfälligkeitsentschädigung bei Zinsbindung über die Haltedauer hinaus; tragbarer Preis im Stressfall; Suchbereich und Raster der Zielwertsuche; Zahl der Eingaben beim Ankauf gebundener Bestände; Abgrenzung der Sollzinsen in der Gesamtkapitalrendite (MA-028)
- [ ] Fachspezifikation Steuern (aus Prüfrunde 4 und 5): Gewerbesteuer auf den Verkaufsgewinn je Steuerstatus, De-minimis-Bindung nach Person (MA-029); Gewerbesteuer der Personengesellschaft beim Verkauf, Veräußerungsgewinn bei erweiterter Kürzung, Bewertung bei laufender Bindung über MA-017 hinaus, Zuschussentgelt in der Kreditprobe, Abstand zur Zielrendite als Endwertüberschuss (MA-012)
- [ ] Quellenkataster: niedersächsisches Haushaltsrecht (VV zu § 44 LHO, ANBest-P; klärt MA-021) und Übergangsrecht zu § 559f BGB am Original lesen – von der Cloud-Umgebung aus bisher nicht erreichbar

## Wartet auf Nutzer

- [ ] **Vor den Herstellervorführungen und Anwendergesprächen freigeben:** Maßstäbe der Vorprüfung (Wortlaut: Spezifikation Kapitel 2, Zeile „Entscheidungspunkte"). Vorschlag: (1) Deckt ein vorgeführtes Produkt den Bedarf, wird nur noch Kauf gegen Excel-Ausbau verglichen; (2) Bedarf allgemein – die Mehrheit der Befragten würde die Grobkalkulation statt Excel nutzen, sonst Abbruch; (3) Bedarf, der nur den Eigenbau trägt – die Mehrheit braucht mindestens eines von Änderungsprotokoll, Arbeit mehrerer Personen an einem Projekt, Berichten und Zugang für Kunden, sonst Umsteuern auf Kauf oder Excel-Ausbau; (4) Mindestfallzahl – die Zeitersparnis über zehn Jahre deckt mindestens die Lizenzkosten des günstigsten vorgeführten Produkts über dieselben zehn Jahre, sonst Abbruch; ohne Katalogverantwortung Abbruch. Dazu von Ihnen: Stundensatz und der Anteil der Zeit, den Sie als Ersparnis ansetzen
- [ ] **Mit dem Auftrag der Vorstudie freigeben, vor der Bauentscheidung:** Kalkulationszins, Zeitraum (Vorschlag zehn Jahre), ungünstiger Fall (Vorschlag: Entwicklungsaufwand plus 50 %, Einführung beim Kauf und Excel-Ausbau plus 30 %, Nutzen minus 50 %), Schwellen für den Bau (Aufwand eines Teilschritts mehr als 50 % über der Schätzung; Nutzungsgrad unter der Hälfte der Kalkulationen, gezählt über die ersten sechs Monate; Bank oder Gremium verlangen für mehr als eine von drei Vorlagen zusätzlich die Excel-Rechnung)
- [ ] Vorgaben des Hauses (fällig nach Abnahme der Fachspezifikation, spätestens vor dem Einsatz der Grobkalkulation): rund 60 Einzelwerte in 31 Gruppen, vollständig in `docs/fachspezifikation-rechenkern.md`, Kapitel 3 (H-01 bis H-31) – unter anderem Zielrendite, Stresshöhen, Beleihungsquote, Mindestdeckung, Mindesttilgung, kalkulatorischer Zins, Anschlusszins, Habenzinsen, Leerstand und Forderungsausfall, Steigerungsraten, Zuschläge der Kostengruppen, CO2-Preis, Warnschwellen. Ich bereite dafür ein Freigabeblatt mit Vorschlagswerten vor
- [ ] Vorführungen bei den drei VOFI-Anbietern anfordern (Prüfliste kommt aus Anhang D des Berichts)
- [ ] Anwalt beauftragen (Datenschutz, Mitbestimmung, Nutzungsrechte, Haftung der Beratung) – vor der Bauentscheidung; Steuerberater für die Durchsicht der Steuerlogik – vor dem ersten Kundeneinsatz
- [ ] Zustimmung der KfW zur Nutzung der Zinsdatei einholen, sobald die Lizenzfrage geklärt ist
- [ ] Falls greifbar, zwei Buchstellen als Foto oder Auszug: Grob, „Einführung in die Investitionsrechnung", S. 140 f. (Gesamtkapitalrentabilität: welche Sollzinsen zählen; dazu die Amortisationsdauer) und Ropeter, „Investitionsanalyse für Gewerbeimmobilien" (1998), S. 186 ff. (Rendite bei mehreren Einlagen und Entnahmen). Nicht dringend: Bis dahin rechnet das Werkzeug mit gekennzeichneten Annahmen (MA-012, MA-027, MA-028)
- [ ] Gespräch mit der Hausbank: zehn Fragen zur Kreditrechnung (Rang und Beleihungsraum, Wertansatz, kalkulatorischer Zins, Ertragsansatz, Deckung, Restfinanzierung neben dem NBank-Darlehen, Bereitstellungszinsen, Vorfälligkeit, Prolongation, Entgelte) – Leitfaden: https://claude.ai/artifact/Ui9nDDDYgHkpSa16V6wFVS (Antworten dort in die letzte Spalte)
- [ ] Fragen an Ihren Steuerberater (fünf Punkte): Gewerbesteuer auf den Verkaufsgewinn bei erweiterter Kürzung; steuerliche Einordnung des NBank-Zuschusses; Vorfälligkeitsentschädigung bei der Privatperson; Objektverkauf einer GmbH & Co. KG; Verkauf in der befreiten Genossenschaft – Leitfaden: https://claude.ai/artifact/Ui9nDDDYgHkpSa16V6wFVS (Antworten dort in die letzte Spalte)
- [ ] Zwei bis drei abgeschlossene eigene Kalkulationen (Excel) für die Parallelrechnung bereitstellen, hier im Gespräch, nicht im Repository; dazu, wenn greifbar, ein echter Tilgungsplan Ihrer Bank
- [ ] Entscheiden: Soll ein Fehlbetrag in der Kalkulation als Nachschuss aus Eigenkapital erscheinen (Voreinstellung) oder über eine Kontokorrentlinie laufen? Und: Haltedauer im geförderten Neubau – Vorschlag Bindungsende plus ein Jahr
- [ ] Durchsicht der sechs Modellannahmen mit hohem Gewicht (`docs/modellannahmen.md`: MA-001, MA-004, MA-012, MA-014, MA-016, MA-026) und der begründeten Ausnahmen von der Vorsichtsregel (MA-019, MA-022, MA-023 beim Erwerb, Wertansatz in MA-026)
- [ ] Fachfrage: Kommt Erbbaurecht bei euren geförderten Neubauten häufig genug vor, um es in Stufe 1 vorzuziehen?
- [ ] Fachfrage: Steht beim Neubau die Frage „gefördert oder frei finanziert" am Anfang der Kalkulation?
- [ ] Vertretung für die Katalogverantwortung benennen
- [ ] Sichtbarkeit des Repositorys `Vofi-Rust` entscheiden: derzeit öffentlich, enthält interne Planungsunterlagen
- [ ] Gespräch mit der NBank (Termin in der Woche ab 23.11.2026): Leitfaden mit 20 Fragen liegt als Dokument vor – https://claude.ai/artifact/H2xAUn4xT3EikxE8E1rqX1 . Danach Antworten zurückmelden (ausgefüllte Spalte oder Foto der Notizen)
- [ ] Drei bis fünf Gespräche mit Anwendern oder Kunden: Würden sie das Werkzeug nutzen, was fehlt ihnen heute?
- [ ] Verantwortung für die Pflege des Regel- und Förderkatalogs im Unternehmen benennen
- [ ] Mengengerüst für die Wirtschaftlichkeitsrechnung: Projekte pro Jahr, Zeitaufwand je Kalkulation heute, Zahl der Nutzer, Anteil geförderter Mietwohnungsbau; für das Beratungsgeschäft Mandate pro Jahr und Honorare


## Später

- [ ] Gestaltungsreferenzen: Lücken schließen vor dem jeweiligen Entwurf – IBCS am Original, Gestaltungssysteme für datendichte Tabellen, Tornado- und Bandbreitendiagramm, Tilgungsplan, Ablauf „Projekt anlegen"
- [ ] Phase 2: Design-Wettbewerbe für die drei prägenden Ansichten (`/designwettbewerb`), daraus das Gestaltungssystem
- [ ] Geplante Aufgaben einrichten, sobald der Regel- und Förderkatalog steht (Phase 1): monatlich Förderkonditionen, vierteljährlich Rechtsstand; bis dahin Durchsicht an jedem Freigabepunkt
- [ ] Projekteigene Skills bauen: `vofi-fachmodell`, `referenzfall-anlegen`, später `foerderprogramm-pflegen`, `steuer-regeln`
- [ ] Phase 3: Einrichtungsskript der Cloud-Umgebung, Prüfkette auf dem Server, Hooks für die Oberfläche
- [ ] Stufe 4: marktübliche Werte für Betreiberimmobilien recherchieren
- [ ] Rust-Workspace aufsetzen, CI, SessionStart-Hook für Toolchain in Cloud-Sitzungen; dabei `CLAUDE.md` um Glossar, Vorzeichenkonvention, „Geld nie als Gleitkommazahl“ und Build- und Testbefehle ergänzen
- [ ] Referenzfälle (Golden-Master) aus Lehrbuch-/Excel-VOFI als Tests

## Erledigt

- [x] 2026-11-18 Fachspezifikation des Rechenkerns nach Prüfrunde 1 überarbeitet: 167 Regeln, 19 Proben, 20 Referenzfälle mit 906 Prüfungen, alle bestanden; 37 Modellannahmen, 229 Quellen
- [x] 2026-11-18 Prüfrunde 1 zur Fachspezifikation des Rechenkerns: Noten 8, 7, 7, 7, 7, 7, 7; gesichtet (45 Punkte)
- [x] 2026-11-18 Fachspezifikation des Rechenkerns, Teil 1, als Entwurf mit Referenzrechner; in Dokumentationsübersicht und Pflichtlektüre aufgenommen
- [x] 2026-11-18 Reihenfolge der Stufe 1 entschieden (Auftraggeber): nach der Grobkalkulation zuerst der Neubau in voller Tiefe, dann NBank-Förderung, danach Ankauf Bestand
- [x] 2026-11-18 Regionaler Schwerpunkt geklärt (Auftraggeber): Niedersachsen, Bremen, Hamburg, Schleswig-Holstein, Nordrhein-Westfalen; Förderung überwiegend KfW und NBank – Spezifikation und Entscheidungsprotokoll nachgezogen
- [x] 2026-11-18 Lehrbuchkapitel „Immobilieninvestition" (Schulte et al., S. 787–838, vom Auftraggeber bereitgestellt) ausgewertet: Zeilenaufbau am Original belegt, zwei Musterrechnungen nachgebaut (50 von 53 Buchwerten getroffen, drei um je eine Einheit abweichend) → Quellnotiz 11
- [x] 2026-11-18 Recherchebericht abgenommen: Schlussredaktion nach Prüfrunde 5 eingearbeitet (24 Punkte), gegengelesen, Prüfskripte grün; 29 Modellannahmen, 219 Quellen
- [x] 2026-11-18 Gesprächsleitfaden für die NBank erstellt: 20 Fragen, je mit bisheriger Annahme und Zuordnung zu MA-001 bis MA-006, MA-017, MA-020, MA-021
- [x] 2026-11-18 Prüfrunde 5 zum Recherchebericht (letzte Runde): Noten 9, 9, 9, 9, 9, 8; gesichtet; Spezifikation, Entscheidungsprotokoll und Aufgabenliste nachgezogen
- [x] 2026-11-18 Formel der VOFI-Gesamtkapitalrentabilität liegt vor (Bildschirmfoto des Auftraggebers); Kennzahl kommt auf das Kennzahlenblatt
- [x] 2026-11-18 Nachprüfung der Steuerungsdokumente (Note 8): sieben neue Befunde behoben, Prüfskripte strenger
- [x] 2026-11-18 Recherchebericht nach Prüfrunde 4 überarbeitet (31 Sichtungspunkte); 27 Modellannahmen, 215 Quellen; Prüfmodi beider Verzeichnisse gleichen jetzt auch die Kennungen in der Spezifikation ab
- [x] 2026-11-18 Lehrbuchfragen ohne Buchkauf verfolgt (Quellnotiz 10): Eigenkapitalrentabilität bestätigt, Amortisationsdauer als Annahme mit zwei Lesarten, Gesamtkapitalrentabilität weiter offen; ImmoWertV-Werte 2026/2027 aus dem Preisindex nachgerechnet
- [x] 2026-11-18 Steuerungsdokumente durch die Rolle Dokumentation geprüft (Note 7); zehn Befunde am Bestand bestätigt, sieben behoben, drei teilweise (Rest in der Nachprüfung)
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
