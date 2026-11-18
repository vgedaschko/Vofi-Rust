Rolle: Dokumentation (Nachprüfung)
Prüfobjekt: Steuerungsdokumente nach Bearbeitung der zehn Befunde aus `dokumentation.md` (gleicher Ordner) – `CLAUDE.md`, `docs/README.md`, `docs/spezifikation.md`, `docs/entwicklungsplan.md`, `docs/entscheidungen.md`, `TASKS.md`, `docs/skills-und-werkzeuge.md`, `docs/pruefung/regeln.md`, `docs/pruefung/protokoll.md`, `.claude/agents/`, `.claude/hooks/`, `scripts/quellenkataster.py`, `scripts/modellannahmen.py` (Stand 2026-11-18)

Gesamturteil: Trägt, mit kleinen Auflagen. Die vier tragenden Befunde (Reihenfolge des Protokolls, eine Heimat für offene Punkte, Kennungen in der Spezifikation mit Prüfung, Hook-Beschreibung) sind im Kern behoben. Beide Prüfmodi laufen fehlerfrei und schlagen bei einer fehlenden Kennung an. Geblieben sind Reste an den Nahtstellen der Überarbeitung: zwei abgelöste Protokolleinträge ohne Vermerk, ein überholter Satz zur Literaturbeschaffung im Plan, eine fehlende Protokollzeile für diese Prüfung, und die Prüfmodi prüfen weniger, als Plan und Entscheidungsprotokoll zusagen.
Note: 8 von 10. Für die 9 fehlen die Befunde N1 bis N4 (alle in einem Arbeitsgang behebbar). N5 bis N7 sind Hinweise.

Am Bestand bestätigt (keine Befunde):
- `python3 scripts/quellenkataster.py --pruefen`: „in Ordnung: 215 Quellen“, Rückgabe 0. `python3 scripts/modellannahmen.py --pruefen`: „27 Einträge, 27 offen“, Rückgabe 0.
- Anschlagen erprobt an Kopien im Scratchpad (nicht am Bestand):
  - `GEWSTG-9` → `GEWSTG-99` in der Spezifikation: Fehler, Rückgabe 1.
  - `MA-099` in der Spezifikation (mit `.git`): Fehler, Rückgabe 1.
  - `MA-015` aus Kap. 3 entfernt: Gegenrichtung meldet Fehler, Rückgabe 1.
  - Grenzen der Prüfung siehe N3.
- Alle 27 Kennungen stehen in der Spezifikation. Alle Quellenkennungen in Backticks in den Steuerungsdokumenten, den Rollen und den Befehlen stehen im Kataster, auch `ESTG-35`, `BGB-559A`, `NBANK-RL-MIETWOHNRAUM-2026`.
- Zahlen stimmen überein:
  - 17 Prüferrollen: Dateien, Plan Z. 34, `skills-und-werkzeuge.md` §5 (5 + 5 + 6 + 1).
  - 215 Quellen und 27 Annahmen: `TASKS.md` Z. 63 und die Prüfmodi.
  - Fünf Annahmen mit Gewicht hoch (MA-001, 004, 012, 014, 016): `TASKS.md` Z. 38 und `modellannahmen.md` Z. 7.
  - Drei begründete Ausnahmen von der Vorsichtsregel (MA-019, 021, 022): `TASKS.md` Z. 38 und die Grundlagen in `annahmen.toml`.
  - 16 Einträge „Lizenz klären“: `TASKS.md` Z. 19 und `quellen.toml`.
  - `docs/README.md` und `CLAUDE.md` nennen keine Zählungen.
- Alle Markdown-Verweise und Pfadangaben lösen sich auf. Ausnahmen sind beabsichtigt: `docs/anwendung/` (entsteht ab Phase 1), Repository-Name, Platzhalter `begruendung.md` in `/designwettbewerb`.
- Pflichtlektüre in `CLAUDE.md` passt zu `docs/README.md` Teil A und zum Bestand. Alle neun Dateien existieren, alle stehen in der Übersicht. Kein steuerndes Dokument fehlt. `gestaltungsreferenzen.md` und `skills-und-werkzeuge.md` sind zu Recht nur Nachschlagewerke.

## Stand der zehn Befunde

| Nr. | Befund | Stand | Fundstelle |
|---|---|---|---|
| 1 | Reihenfolge Entscheidungsprotokoll, Vermerk „abgelöst“ | **teilweise** | Reihenfolge behoben (`entscheidungen.md` Z. 7–46 absteigend), Vermerke an Z. 17 und Z. 20. Es fehlen die Vermerke an Z. 19 und Z. 36, siehe N1 |
| 2 | Offene Punkte doppelt (Spez. Kap. 9 / `TASKS.md`) | **behoben** | Spez. Z. 138–140 nur noch Verweis. Schwellen samt Mindestfallzahl in Kap. 2, Z. 44. `TASKS.md` Z. 31 führt denselben Vorschlag für den Auftraggeber; das ist vertretbar, weil er die Spezifikation nicht liest |
| 3 | Kennungen der Annahmen am Wirkort, Gegenprüfung | **teilweise** | Alle 27 Kennungen in der Spezifikation. Gegenrichtung in `modellannahmen.py` Z. 140–146 eingebaut und wirksam. Rest: Sechs Annahmen stehen nicht an der Zeile, die das Verzeichnis nennt, und die Prüfung prüft nur, ob die Kennung irgendwo vorkommt, siehe N3 |
| 4 | Quellenkennungen ungeprüft, `ESTG-35` fehlt | **behoben** | `ESTG-35` in `quellen.toml` Z. 713. Abgleich in `quellenkataster.py` Z. 44–45 und Z. 94–111. Die sechs genannten Zeilen tragen jetzt Kennungen (Spez. Z. 41, 46, 56, 64, 73, 117). Grenzen der Prüfung und zwei Restangaben siehe N3 |
| 5 | Hook-Wirkung zu stark beschrieben | **behoben** | Einheitlich „hält einmal auf“: `CLAUDE.md` Z. 92, Spez. Z. 103, Plan Z. 82, `skills-und-werkzeuge.md` Z. 71–78, passend zu `gestaltung.sh` Z. 55. Rest im Entscheidungsprotokoll Z. 19, siehe N1 |
| 6 | Zahl der Annahmen von Hand, `MA-026` vor dem Eintrag | **behoben** | Plan Z. 30 verweist auf `modellannahmen.md`. `MA-026` ist verzeichnet, `--pruefen` läuft fehlerfrei |
| 7 | `skills-und-werkzeuge.md` veraltet | **behoben** | Stand 2026-11-18, Abschnitte 1–7 der Reihe nach. Mobbin stimmt (Z. 84, 90). `clippy` und `wasm-bindgen-cli` stimmen (Z. 10, 12). Glossar und Konventionen als Aufgabe in `TASKS.md` Z. 58. Rest: Z. 48, siehe N6 |
| 8 | Auslöser der zeitgesteuerten Prüfungen; Turnus jährlich / bei Neuausgabe | **behoben** | Plan Z. 90, 91, 96 und `TASKS.md` Z. 54 einheitlich („sobald der Katalog steht; bis dahin an jedem Freigabepunkt“). Neue Zeile Z. 93. `MA-010` ist in Z. 96 überbrückt |
| 9 | Rolle Steuerberater nach Investorentyp | **behoben** | `pruefer-steuerberater.md` prüft je Steuerstatus mit Verweis auf Spez. Kap. 1 |
| 10 | Kopfzeilen, Verweis Gestaltungsreferenzen, Lotsen-Ausnahme | **teilweise** | Behoben: `entscheidungen.md` Z. 3, `protokoll.md` Z. 3, `regeln.md` Z. 3, Leser in Spezifikation und Plan, `CLAUDE.md` Z. 94, Lotsen-Ausnahme in `regeln.md` Z. 3. Offen: `TASKS.md` hat weiter weder Stand noch Leser, siehe N7 |

## Befunde

1. **[wichtig · belegt] `docs/entscheidungen.md` Z. 19 und Z. 36: Zwei abgelöste Einträge tragen keinen Vermerk, entgegen der eigenen Regel in Z. 3.**
   - Z. 19 sagt weiter, die Gestaltungsprüfung werde „per Hook vor jedem Stopp erzwungen“. Das ist genau die Aussage, die Z. 9 richtiggestellt hat. Z. 9 führt in „Ersetzt“ aber „–“.
   - Z. 36 („Fachliteratur wird bei Bedarf beschafft … notfalls über den Rechner des Auftraggebers“) ist laut Z. 7, Spalte „Ersetzt“, abgelöst. Z. 36 trägt keinen Vermerk.
   - Z. 14 nennt als ersetzt die „Schwelle ‚drei von fünf‘ vom 2026-11-18“. Einen solchen Eintrag gibt es im Protokoll nicht; der Verweis läuft ins Leere.
   - Szenario: Eine Sitzung, die vor dem Anfassen der Gestaltungspflicht das Protokoll liest, findet in Z. 19 wieder „erzwungen“. Das ist der Widerspruch aus dem früheren Befund 5, jetzt an der Stelle, die Festlegungen begründen soll.
   - Vorschlag:
     - Z. 9, Spalte „Ersetzt“: „Wortlaut ‚per Hook erzwungen‘ im Eintrag zur Gestaltungspflicht“.
     - Z. 19: „… und wird per Hook vor jedem Stopp angemahnt (**Wortlaut ‚erzwungen‘ abgelöst**, siehe oben)“.
     - Z. 36: „(**abgelöst**: Klärung über frei zugängliche Quellen, siehe oben)“.
     - Z. 14, Spalte „Ersetzt“: „Schwelle ‚drei von fünf‘ (Sichtung Runde 3)“, oder die tatsächliche Fundstelle nennen.

2. **[wichtig · belegt] `docs/entwicklungsplan.md` Z. 21 und Z. 31 sind überholt.**
   - Z. 21: „Ebenfalls beim Auftraggeber: Beschaffung der Lehrbücher“. Das widerspricht `entscheidungen.md` Z. 7: Lehrbuchfragen werden über frei zugängliche Quellen geklärt, nicht über den Kauf der Bücher. Es widerspricht auch `TASKS.md` Z. 36 („Ein Bildschirmfoto genügt statt eines Buchkaufs“). Szenario: Eine Sitzung liest zu Beginn den Plan und bittet den Auftraggeber, Lehrbücher zu beschaffen.
   - Z. 31: „neun Quellnotizen“. Unter `research_notes/…/` liegen zehn (01 bis 10). Notiz 10 trägt `MA-027` und Spez. Z. 65.
   - Ähnlich, aber schwächer: `CLAUDE.md` Z. 72 („Fachliteratur bei Bedarf am Original beschaffen … vom Auftraggeber bereitgestellte Exemplare; notfalls über dessen Rechner“) beschreibt noch den alten Weg als Regel.
   - Vorschlag:
     - Z. 21: „Ebenfalls beim Auftraggeber: Klärung von Datenschutz und Mitbestimmung vor der Spezifikation des Änderungsprotokolls; zur Lehrbuchfrage nur das Bildschirmfoto aus `TASKS.md`.“
     - Z. 31: Zahl streichen („Quellnotizen“), nach Grundsatz 6 und wie schon in Z. 30.
     - `CLAUDE.md` Z. 72: „Fachliteratur zuerst über frei zugängliche Quellen klären (Verordnungstexte, Fachlexika, Hochschulschriften); Bücher nur, wenn eine Lücke bleibt.“ Das entspricht `TASKS.md` Z. 24.

3. **[wichtig · belegt] Prüfmodi: Plan und Entscheidungsprotokoll versprechen mehr, als die Skripte prüfen. Sechs Annahmen stehen nicht an der Zeile, die das Verzeichnis nennt.**
   - Wirkort:
     - Plan Z. 86 („steht an jedem Wirkort, den das Verzeichnis in der Spezifikation nennt“) und `entscheidungen.md` Z. 8 („an jeder Stelle, die das Verzeichnis als Wirkort nennt“) sagen mehr, als das Skript tut. `modellannahmen.py` Z. 142–146 prüft nur, ob die Kennung irgendwo in der Spezifikation vorkommt.
     - Erprobt: `MA-019` aus der Zeile „Kopplungen“ entfernt, Prüfung bestanden, weil die Kennung in Z. 77 steht.
     - Im Bestand: MA-002, 004, 005, 006, 017 und 020 nennen als Wirkort „Kapitel 4, Fördermodul“. Die Zeile „Fördermodul“ (Spez. Z. 72) trägt keine Kennung. Sie stehen nur in der Sammelzeile Z. 77. MA-004 hat Gewicht hoch, und Kap. 8 „Kennzeichnung“ (fest) verlangt die Kennung „an der betroffenen Regel“.
   - Quellen:
     - `quellenkataster.py` Z. 103–109 prüft nur Kennungen, deren Vorsilbe schon im Kataster steht, und nur in Backticks. Erprobt: `GRSTG-13` (neue Vorsilbe) und `ESTG-36` ohne Backticks bestehen beide die Prüfung.
     - Plan Z. 92 sagt dagegen „jede Quellenkennung, die Spezifikation, Plan, `CLAUDE.md` … nennen, steht im Kataster“.
     - Die Fehlermeldung beginnt mit „Fehler in quellen.toml“, auch wenn der Fehler in der Spezifikation liegt (Z. 171). Das führt bei der Fehlersuche an die falsche Datei.
   - Zwei Förder- und Lexikonangaben der Spezifikation stehen noch ohne Kennung, obwohl Einträge existieren:
     - Z. 46: Bodenrichtwert begrenzt die zuwendungsfähigen Grundstückskosten, `BODENRICHTWERTE-NI` bzw. NBank-Richtlinie.
     - Z. 65: „über das Fachlexikon bestätigt“, `GABLER-BANKLEXIKON-VOFI`.
   - Vorschlag:
     - Entweder `verwendet_in` der sechs Annahmen auf „Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage“ ändern. Oder, besser für MA-004, die Kennungen in die Statusspalte der Zeile „Fördermodul“ setzen.
     - Plan Z. 86 und Entscheidung Z. 8 auf das Geprüfte zurücknehmen („steht in der Spezifikation“). Alternativ das Skript den Zeilennamen aus `verwendet_in` in der Tabellenzeile suchen lassen.
     - Plan Z. 92 auf „jede Kennung einer im Kataster geführten Vorsilbe“ zurücknehmen. Alternativ im Skript jede Kennung nach dem Muster melden, die weder im Kataster steht noch auf einer kurzen Ausnahmeliste.
     - Meldung in `quellenkataster.py` Z. 171 auf „Quellenkataster: Fehler“ ändern.
     - Die beiden Kennungen in Spez. Z. 46 und 65 nachtragen.

4. **[wichtig · belegt] `docs/pruefung/protokoll.md`: Die Prüfung der Steuerungsdokumente (Note 7, zehn Befunde) fehlt. Ihr Ordner hat keine Sichtung.**
   - Problem: Das Protokoll ist laut `CLAUDE.md` der Ort für „was wann mit welchem Ergebnis geprüft wurde“, laut Kopfzeile „eine Zeile je Prüfrunde“. Es führt nur die vier Runden zum Recherchebericht.
   - Wo die Prüfung steht: Nur in `TASKS.md` Z. 65. Dort steht „zehn Befunde … behoben“. Diese Nachprüfung findet drei davon nur teilweise behoben.
   - Ordner: `docs/pruefung/2026-11-18-steuerungsdokumente/` hat keine `sichtung.md`. Nach Protokoll Z. 3 liegen „Berichte und Sichtung je Runde im Ordner der Runde“. Wie die zehn Befunde bewertet und umgesetzt wurden, steht damit nirgends.
   - Vorschlag:
     - Im Protokoll eine Zeile „2026-11-18 | Steuerungsdokumente | Dokumentation | 0 / 7 / 3 | Note 7; Nachprüfung Note 8 · [Bericht](…)“ ergänzen.
     - Eine kurze Sichtung je Befund anlegen (übernommen / wie umgesetzt). Alternativ im Protokoll festhalten, dass bei Einzelrollenprüfungen der Bericht die Sichtung ersetzt.

5. **[Hinweis · belegt] `scripts/modellannahmen.py` Z. 67–70: Ohne git-Arbeitskopie fällt die Hauptprüfung still aus.**
   - Problem: Scheitert `git ls-files`, gibt `verweise()` ein leeres Ergebnis zurück. Ob jede genannte Kennung im Verzeichnis steht, wird dann nicht geprüft, und die Prüfung meldet trotzdem „in Ordnung“.
   - Erprobt an einer Kopie ohne `.git`: `MA-099` in der Spezifikation besteht, Rückgabe 0. Mit `.git` schlägt die Prüfung an.
   - Wann das zählt: Heute ist es unkritisch, weil Sitzung und spätere Server-Prüfkette eine Arbeitskopie haben. Bei einem Export, einer Kopie oder einem eingeschränkten Checkout prüft der Modus aber still nichts.
   - Vorschlag: Bei gescheitertem git auf eine Dateisuche unter `WURZEL` zurückfallen, mit denselben Ausschlüssen. Mindestens einen Fehler „Verweise nicht prüfbar“ melden.

6. **[Hinweis · belegt] `docs/skills-und-werkzeuge.md` Z. 48: Der geplante Skill `steuer-regeln` soll „Regeln je Investorentyp“ führen.**
   - Problem: Das ist dieselbe überholte Kopplung, die in der Rolle Steuerberater behoben wurde (früherer Befund 9). Maßgeblich sind Spez. Z. 25 und `entscheidungen.md` Z. 28.
   - Vorschlag: „Regeln je Steuerstatus (Spezifikation Kapitel 1)“.

7. **[Hinweis · belegt] `TASKS.md` Z. 1–5: weder Stand noch Leser (Grundsatz 9 der Übersicht; Rest des früheren Befunds 10).**
   - Vorschlag: In Z. 3 ergänzen: „Leser: Entwicklung zu Sitzungsbeginn; der Auftraggeber über den Abschnitt ‚Wartet auf Nutzer‘. Stand: Datum des jüngsten Eintrags unter ‚Erledigt‘.“

## Nicht geprüft

- **Ausgenommene Teile:** Inhalt des Rechercheberichts unter `reports/` und der Ordner `docs/pruefung/2026-11-18-recherchebericht-runde5/` (laut Auftrag).
- **Kataster und Verzeichnis:** Inhalt von `quellen.toml`, `annahmen.toml` und der erzeugten Übersichten nicht fachlich geprüft, nur Kennungen, Zählungen und `verwendet_in` abgeglichen.
- **Quellnotiz 10:** nur ihre Existenz und ihre Nennung geprüft.
- **Laufzeitverhalten der Hooks:** Die Hooks rufen git auf und schreiben in `.git/`; ihr Verhalten ist aus dem Code abgeleitet. Ausgeführt habe ich nur die beiden Prüfmodi, am Bestand lesend und an Kopien im Scratchpad.
- **Fachliche Richtigkeit** der Festlegungen: Das ist nicht diese Rolle.
