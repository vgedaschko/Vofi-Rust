Rolle: Dokumentation
Prüfobjekt: Steuerungsdokumente als Ganzes – `CLAUDE.md`, `docs/README.md`, `docs/spezifikation.md`, `docs/entwicklungsplan.md`, `docs/entscheidungen.md`, `TASKS.md`, `docs/skills-und-werkzeuge.md`, `docs/gestaltungsreferenzen.md`, `docs/pruefung/regeln.md`, `docs/pruefung/protokoll.md`, `.claude/commands/`, `.claude/agents/`, `.claude/hooks/`, `.claude/settings.json` (Stand 2026-11-18)

Gesamturteil: Mit Auflagen tragfähig. Gerüst, Pflichtlektüre und Verweise stimmen. Eine neue Sitzung fände aus `CLAUDE.md` den richtigen Einstieg. Es gibt aber vier Stellen, an denen sie sich falsch orientieren würde: das Entscheidungsprotokoll ist nicht in der zugesagten Reihenfolge, die offenen Punkte beim Auftraggeber stehen doppelt und laufen auseinander, die Kennzeichnung von Annahmen und Quellen in der Spezifikation ist lückenhaft und wird von keiner Prüfung erfasst, und die Wirkung des Gestaltungs-Hooks ist an vier Orten stärker beschrieben, als der Code sie umsetzt.
Note: 7 von 10. Für die 9 fehlen: Befunde 1 bis 5 beheben (Reihenfolge, eine Heimat für offene Punkte, Kennungen in der Spezifikation samt Prüfung durch die Skripte, zutreffende Hook-Beschreibung an einem Ort) und `docs/skills-und-werkzeuge.md` auf den Stand bringen (Befund 7).

Am Bestand bestätigt (keine Befunde): alle Markdown-Verweise und Pfadangaben in den Prüfobjekten lösen sich auf. 17 Prüferrollen (Dateien = Plan = `skills-und-werkzeuge.md` §5). 211 Quellen (`quellenkataster.py --pruefen` fehlerfrei). 16 Einträge „Lizenz klären“ (`TASKS.md` Z. 17). Fünf Annahmen mit Gewicht hoch (MA-001, 004, 012, 014, 016; `TASKS.md` Z. 35). 34 Vorbilder in `gestaltungsreferenzen.md` (39 eindeutige Mobbin-Adressen, abzüglich Sammlung und vier Gegenbeispielen). Noten im Protokoll stimmen mit `TASKS.md` überein. Alle fünf Hooks bestehen `bash -n`. `settings.json` bindet genau die beschriebenen Hooks ein. Der Start-Hook läuft und meldet korrekt.

## Befunde

1. **[wichtig · belegt] `docs/entscheidungen.md` Z. 3 und Z. 36–43: Die Reihenfolge widerspricht der eigenen Regel.**
   - Problem: Der Kopf sagt „Neue Einträge oben“. Die acht jüngsten Einträge aus Prüfrunde 4 stehen aber am Tabellenende, unter den Einträgen vom 2026-11-17.
   - Szenario: Eine Sitzung, die vor dem Anfassen einer Festlegung oben liest („Bevor eine frühere Festlegung angefasst wird“, `CLAUDE.md`), trifft in Z. 9 zuerst auf „tragbarer Kaufpreis als niedrigerer aus Renditegrenze und Bankgrenze“. Diese Regel ist durch Z. 36 abgelöst. Z. 9 trägt keinen Hinweis darauf, die Ablösung steht nur in der Spalte „Ersetzt“ von Z. 36. Dasselbe gilt für die Bedarfsschwelle „drei von fünf“ (Z. 40) und den Pauschalsatz der Steuer (Z. 39).
   - Vorschlag: Die Z. 36–43 an den Tabellenanfang verschieben. Abgelöste Zeilen in der Entscheidungsspalte kurz mit „abgelöst am … (siehe oben)“ kennzeichnen. Maßgeblich bleibt die Spezifikation.

2. **[wichtig · belegt] `docs/spezifikation.md` Kap. 9 gegen `TASKS.md` „Wartet auf Nutzer“: dieselbe Liste an zwei Orten, inzwischen auseinandergelaufen.**
   - Problem: Kap. 9 führt 8 Punkte, `TASKS.md` 16. In Kap. 9 fehlen die Herstellervorführungen, der Auftrag an Anwalt und Steuerberater, die Fachbücher, die Zustimmung der KfW, die Sichtbarkeit des Repositorys und die Zusatzfragen an die NBank. Kap. 9 Nr. 6 verweist für die Schwellen auf „Vorschläge in Kapitel 2, Zeile Entscheidungspunkte“. Dort steht die Mindestfallzahl aber nur als Wort. Der Vorschlag dazu („Zeitersparnis über zehn Jahre deckt mindestens den Lizenzpreis …“) steht allein in `TASKS.md` Z. 28.
   - Widerspricht: Grundsatz 1 der Übersicht („Ein Thema, ein Ort“), der Spezifikation selbst (Z. 14: offene Ideen gehören in `TASKS.md`), dem Entscheidungsprotokoll Z. 42 („Offene Aufträge stehen nur in `TASKS.md`“) und dem Protokoll Z. 28.
   - Vorschlag: Kap. 9 durch einen Satz mit Verweis auf `TASKS.md` ersetzen. Den Schwellenvorschlag, auch die Mindestfallzahl, als vorläufige Festlegung in Kap. 2 „Entscheidungspunkte“ aufnehmen, denn er ist eine Festlegung, die auf Freigabe wartet. `TASKS.md` verweist dann nur dorthin.

3. **[wichtig · belegt] `docs/spezifikation.md`: Kennungen von Modellannahmen fehlen an den Regeln, an denen sie laut Verzeichnis wirken. Die Prüfung bemerkt das nicht.**
   - Problem: Kap. 8 „Kennzeichnung“ (fest) verlangt die Kennung an der betroffenen Regel. Zwölf von 25 Annahmen geben in `verwendet_in` eine Stelle der Spezifikation an, die Kennung steht dort aber nicht: MA-008, 009, 010, 011, 015, 017, 018, 019, 020, 023, 024, 025. Beispiele: MA-015 → „Kap. 3, Abnahmetests“ (Z. 64 ohne Kennung); MA-019 → „Kap. 4, Kopplungen“ (Z. 73 nennt nur MA-007); MA-011 → „Kap. 2, Stufe 3“ (Z. 37 ohne Kennung). MA-003 bis 005 erscheinen nur in der Spanne „MA-002 bis MA-006“ (Z. 76), nicht an ihren Regeln (MA-003 gehört laut Verzeichnis zu Kap. 3 „Zeithorizont“, Z. 56). MA-021 und MA-022 stehen nur in der Aufgabenliste Kap. 9, an keiner Regel.
   - Lücke in der Prüfung: `scripts/modellannahmen.py --pruefen` prüft nur eine Richtung: Jede genannte Kennung muss im Verzeichnis stehen. Ob eine verzeichnete Annahme an ihrer Wirkstelle steht, prüft es nicht.
   - Einschränkung: `annahmen.toml` ist in Überarbeitung, `verwendet_in` kann sich ändern. Die Lücke auf Seiten der Spezifikation besteht unabhängig davon.
   - Vorschlag: Die Kennungen an die Zeilen der Spezifikation setzen. `--pruefen` um eine Warnung erweitern, wenn eine offene Annahme außerhalb des Verzeichnisses nirgends genannt wird, oder wenn `verwendet_in` „Spezifikation …“ angibt und die Kennung in `docs/spezifikation.md` fehlt.

4. **[wichtig · belegt] Quellen-Kennungen in Steuerungsdokumenten werden nicht geprüft. Eine fehlt bereits im Kataster, mehrere Rechts- und Förderangaben stehen ohne Kennung.**
   - Fehlende Kennung: `docs/spezifikation.md` Z. 46 nennt `ESTG-35`. Der Eintrag fehlt in `quellen.toml`; die 211 Kennungen sind abgeglichen, `ESTG-15` ist vorhanden. Er kommt vielleicht mit der laufenden Überarbeitung hinzu. Bemerkt hätte das aber keine Prüfung: `quellenkataster.py --pruefen` prüft nur die Datensätze, `modellannahmen.py` nur die `quellen`-Felder der Annahmen.
   - Irreführende Angabe im Prüfplan: `docs/entwicklungsplan.md` Z. 86 verspricht „genannte Quellen stehen im Quellenkataster“. Für Spezifikation, `CLAUDE.md` und später Code trifft das nicht zu.
   - Angaben ohne Kennung, entgegen `CLAUDE.md` („Spezifikation … nennt die Kennung“), obwohl die passenden Einträge im Kataster existieren:
     - Z. 41 CO2-Kosten (`CO2KOSTAUFG-*`)
     - Z. 46 erweiterte Grundstückskürzung (`GEWSTG-9`)
     - Z. 56 Laufzeit der NBank-Darlehen 42 Jahre, Bindungen 35 Jahre (`NBANK-RL-MIETWOHNRAUM-2026` o. ä.)
     - Z. 64 IWU 2004/2013 (`KIRCHNER-IWU-2004`, `IWU-2013-ENDBERICHT`)
     - Z. 73 Modernisierungsumlage und Vergleichsmiete (`BGB-559`, `BGB-558`)
     - Z. 116 De-minimis (`EU-DE-MINIMIS-2023-2831`)
   - Vorschlag: `ESTG-35` ins Kataster aufnehmen. `quellenkataster.py --pruefen` um einen Abgleich erweitern: Kennungen in Backticks nach dem Muster `[A-Z][A-Z0-9]+(-[A-Z0-9]+)+` außerhalb von `MA-` in den versionierten Dateien (ohne `reports/`, `research_notes/`, `docs/pruefung/`) müssen im Kataster stehen. Die genannten Zeilen kennzeichnen.

5. **[wichtig · belegt] Gestaltungs-Hook: Die Wirkung ist an vier Orten zu stark beschrieben, und an jedem anders.**
   - Was der Code tut: `.claude/hooks/gestaltung.sh` Z. 55 lässt den Stopp durch, sobald `stop_hook_active` gesetzt ist. Der Hook hält also jeden Stopp genau einmal auf und erinnert. Er erzwingt die Prüfung nicht.
   - Was die Dokumente sagen:
     - `CLAUDE.md` („Der Hook hält jeden Stopp auf, solange das nicht geschehen ist“)
     - Spezifikation Kap. 6 Z. 102 („ein Hook erzwingt das“)
     - Entwicklungsplan Z. 82 („erzwingt die Prüfung vor dem Stopp“)
     - `skills-und-werkzeuge.md` Z. 102 („Hält auf, bis die Gestaltungsprüfung gelaufen … ist“)
   - Zum Vergleich: Für `rust-pruefung.sh` steht korrekt „hält bei Fehlern einmal auf“. Die Ein-Mal-Regel ist als Schutz vor Endlosschleifen richtig. Eine Sitzung, die sich auf die Zusage „erzwingt“ verlässt, kann die Prüfung aber nach der ersten Erinnerung überspringen.
   - Dazu kommt die Dopplung: Die Hook-Wirkung steht an vier Orten, entgegen Grundsatz 1 der Übersicht.
   - Vorschlag: Die Wirkung einmal zutreffend beschreiben, in `skills-und-werkzeuge.md` §6 („hält jeden Stopp einmal auf und nennt die Pflichtschritte“). Die übrigen Stellen formulieren die Pflicht („vor dem Stopp ist die Gestaltungsprüfung durchzuführen; ein Hook erinnert“) und verweisen dorthin.

6. **[wichtig · belegt] Zahl der Modellannahmen und Reihenfolge der Pflege.**
   - Veraltete Zahl: `docs/entwicklungsplan.md` Z. 30 nennt „Verzeichnis mit 25 offenen Annahmen“.
   - Kennung vor dem Eintrag verwendet: `MA-026` steht schon in Spezifikation Z. 46 und Entscheidungsprotokoll Z. 37, aber nicht im Verzeichnis. `modellannahmen.py --pruefen` endet deshalb mit Fehler, und der Start-Hook meldet ihn jeder neuen Sitzung (nachgeprüft). Das kehrt die Reihenfolge aus `CLAUDE.md` um, nach der die Kennung zuerst ins Verzeichnis kommt. Der Grund liegt im Prüfauftrag: Die Überarbeitung auf 26 läuft.
   - Folgepflege: Nach der Überarbeitung ist die Zahl im Plan zu ändern. Hat MA-026 Gewicht hoch, sind auch `TASKS.md` Z. 35 („fünf Modellannahmen mit hohem Gewicht“) und Spezifikation Kap. 9 Nr. 5 anzupassen.
   - Vorschlag: Im Plan keine Zählung von Hand („Verzeichnis, Bestand siehe `docs/modellannahmen.md`“), nach Grundsatz 6 „Erzeugen statt abschreiben“. Kennungen künftig erst eintragen, dann verwenden.

7. **[wichtig · belegt] `docs/skills-und-werkzeuge.md` ist veraltet und widerspricht sich selbst.**
   - Stand: Der Kopf nennt „Stand 2026-11-17“, der Inhalt reicht bis 18.11.
   - Gliederung: Die Abschnitte folgen in der Reihenfolge 1, 2, 3, 4, 5, 7, 6.
   - Widerspruch zu Mobbin: §7 Z. 71 sagt „Noch keine Sammlung angelegt“, Z. 77 und `gestaltungsreferenzen.md` nennen die Sammlung „VOFI Referenzen“ mit 34 Vorbildern.
   - Widersprüche in §1 Z. 9–13:
     - `clippy` gilt als „Hook nach Dateiänderung … mit dem Rust-Workspace“. Tatsächlich läuft `clippy` vor dem Stopp und ist schon eingerichtet (§6, `settings.json`, Plan Z. 37).
     - „`CLAUDE.md` im neuen Repo (`/init`) – Glossar, Vorzeichenkonvention, ‚Geld nie als f64‘ – sobald das Repo existiert“: Das Repo existiert, `CLAUDE.md` enthält nichts davon. Es ist weder erledigt noch als Aufgabe geführt.
     - Für das Einrichtungsskript nennt §1 `wasm-pack`, `sqlx-cli`, Plan 2a Z. 55/60 dagegen `wasm-bindgen-cli`.
   - Szenario: Eine Sitzung, die laut `CLAUDE.md` hier nachschlägt, erhält ein falsches Bild der eingerichteten Prüfkette.
   - Vorschlag: Stand aktualisieren und Abschnitte neu nummerieren. §1 auf das Eingerichtete umschreiben oder in §6 aufgehen lassen. Glossar und Konventionen für `CLAUDE.md` als Aufgabe für Phase 3 in `TASKS.md` aufnehmen oder streichen.

8. **[Hinweis · belegt] Zeitgesteuerte Prüfungen: Der Auslöser ist widersprüchlich beschrieben, und zwei Prüfturnusse haben keinen Prüfweg.**
   - Widerspruch beim Auslöser: Plan Z. 90/91 sagt „einrichtbar, sobald das Kataster befüllt ist“, und das ist es (211 Quellen). Plan Z. 95 und `TASKS.md` Z. 50 sagen „sobald der Regel- und Förderkatalog steht“, und den gibt es erst ab Phase 1.
   - Wiedervorlage ohne Termin: MA-010 hat als Wiedervorlage „mit der nächsten vierteljährlichen Rechtsprüfung“, und diese Prüfung existiert noch nicht.
   - Turnusse ohne Prüfweg: Für die Turnusse „jährlich“ (7 Quellen) und „bei Neuausgabe“ (46 Quellen) hat der Prüfplan keine Zeile.
   - Vorschlag: Einen Auslöser festlegen. Für die Gesetzes- und Förderquellen des Katasters ist das schon jetzt sinnvoll, weil der Bericht auf ihnen ruht. Eine Prüfplanzeile für „jährlich / bei Neuausgabe“ ergänzen, etwa die Durchsicht an jedem Freigabepunkt.

9. **[Hinweis · begründete Einschätzung] `.claude/agents/pruefer-steuerberater.md` folgt noch der überholten Kopplung von Investorentyp und Steuerpflicht.**
   - Problem: Die Rolle prüft „je Investorentyp“ und zählt „steuerbefreite Genossenschaften und kommunale Unternehmen“ zusammen auf. Seit den Entscheidungen Z. 17 und Z. 11 gilt dagegen: Der Steuerstatus ist ein eigenes Merkmal, eine kommunale GmbH ist steuerpflichtig. Hinzugekommen sind die gewerblich geprägte Personengesellschaft und das Einzelunternehmen mit Betriebsvermögen, mit `ESTG-15` und `MA-016` (Spezifikation Z. 25).
   - Szenario: In der Fachspezifikation Steuern (Phase 1) prüft die Rolle entlang der alten Einteilung und übersieht die zwei neuen Ausprägungen.
   - Vorschlag: In der Rolle „je Steuerstatus (Spezifikation Kap. 1)“ prüfen lassen, statt eine Liste zu führen.

10. **[Hinweis · belegt] Kopfzeilen und Auffindbarkeit (Grundsatz 9 der Übersicht).**
    - Fehlender Stand: `entscheidungen.md`, `pruefung/protokoll.md`, `pruefung/regeln.md`, `TASKS.md`.
    - Fehlende Leserangabe: `spezifikation.md`, `entwicklungsplan.md`, `entscheidungen.md`. Nur `gestaltungsreferenzen.md` erfüllt die Vorgabe vollständig.
    - Kein Verweis auf die Gestaltungsreferenzen: Der Abschnitt „Gestaltung und Bedienung“ in `CLAUDE.md` verlangt, vor jedem Entwurf Referenzen anzusehen, nennt `docs/gestaltungsreferenzen.md` aber nicht. Darauf verweist nur der Merker im Hook, und der greift erst nach der ersten geänderten Oberflächendatei, also nach Entwurfsbeginn.
    - Widerspruch zur Lotsen-Rolle: `pruefung/regeln.md` gilt laut Einleitung für „alle Prüfer“. `pruefer-lotse.md` erklärt die gemeinsamen Regeln für nicht anwendbar, und `regeln.md` erwähnt diese Ausnahme nicht.
    - Vorschlag: Die Kopfzeilen nachtragen. In `CLAUDE.md` unter Gestaltung den Satz ergänzen: „Vorbilder: `docs/gestaltungsreferenzen.md`“. In `regeln.md` die Ausnahme für den Lotsen mit einem Halbsatz nennen.

## Nicht geprüft

- **Ausgenommene Dateien:** Inhalt von `reports/…Marktrecherche.md`, `quellen.toml`, `annahmen.toml`, `quellenkataster.md` und `modellannahmen.md` (laut Auftrag). Dort habe ich nur Zahlen und Kennungen gegen die Steuerungsdokumente abgeglichen.
- **Fachliche Richtigkeit** der Festlegungen: Das ist nicht diese Rolle.
- **Laufzeitverhalten der Hooks:** `gestaltung.sh` und `rust-pruefung.sh` habe ich nicht ausgeführt, weil sie intern git aufrufen und Markierungen in `.git/` schreiben. Ihr Verhalten ist aus dem Code abgeleitet. Ausgeführt habe ich nur `anything-else.sh start`, das nur liest.
- **Mobbin-Verweise:** nicht geöffnet.
- **Recherchenotizen und Prüfberichte:** `research_notes/` und die Prüfberichte der Runden 1 bis 4 nicht im Einzelnen gelesen, nur über Protokoll und Sichtung verwiesen.
- **Dokumente aus Teil B der Übersicht:** existieren noch nicht.
