# Vofi-Rust

Webanwendung zur Immobilien-Investitionsrechnung nach der VOFI-Methode (Vollständiger Finanzplan) mit Fördermodulen, Sensitivitäts- und Monte-Carlo-Analyse, Dashboard und Mehrbenutzerbetrieb. Stand: Konzeptphase, noch kein Code.

## Pflichtlektüre

Diese Dateien steuern das Projekt. Sie sind verbindlich, nicht Hintergrundmaterial: zu Beginn jeder Sitzung lesen, bei der Arbeit beachten und im selben Arbeitsgang aktuell halten.

| Datei | Inhalt | Lesen | Pflegen |
|---|---|---|---|
| `docs/README.md` | Dokumentationsübersicht: welches Dokument wofür gilt, Grundsätze der Pflege (ein Thema, ein Ort; im selben Arbeitsgang; nichts auf Vorrat) | Bevor ein Dokument angelegt, geteilt oder verschoben wird | Wenn ein Dokument entsteht, entfällt oder seinen Zweck ändert |
| `docs/spezifikation.md` | Was gebaut wird und warum; geltender Stand mit Status je Festlegung | Vor jeder inhaltlichen Arbeit | Bei jeder geänderten oder neuen Festlegung – vor der Umsetzung |
| `docs/fachspezifikation-rechenkern.md` | Rechenregeln des Kerns mit Regelnummern, Proben und Referenzfällen; konkretisiert Spezifikation Kapitel 3 | Vor jeder Arbeit am Rechenkern, an seinen Tests und an Kennzahlen | Bei jeder geänderten Rechenregel: erst hier, dann Referenzrechner (`research_notes/…/skripte/referenzrechner/`, Lauf `python3 referenzfaelle.py` muss bestehen), dann Code |
| `docs/entwicklungsplan.md` | Phasen, Freigabepunkte, Bestandsaufnahme der Grundlagen, Prüfplan | Zu Sitzungsbeginn: In welcher Phase sind wir, was ist dran, welche Prüfung ist fällig? | Wenn eine Phase endet oder sich die Reihenfolge ändert |
| `TASKS.md` | Offene Arbeit, auch die Punkte, die beim Auftraggeber liegen | Zu Sitzungsbeginn und vor jedem Stopp (der Hook erinnert daran) | Laufend |
| `docs/quellenkataster.md` | Normen- und Quellenkataster: jede Quelle mit Kennung, Stand, Beleg und Prüfturnus | Bevor eine Rechts-, Förder- oder Normangabe verwendet oder geändert wird | Daten in `docs/quellenkataster/quellen.toml` ändern, dann `python3 scripts/quellenkataster.py`; bei jeder neuen Quelle und jedem Lesen am Original |
| `docs/modellannahmen.md` | Verzeichnis der Modellannahmen: was das Modell annimmt, wo sich etwas vor dem Bau nicht klären lässt | Bevor eine Regel gebaut wird, deren Grundlage ungeklärt ist | Daten in `docs/modellannahmen/annahmen.toml` ändern, dann `python3 scripts/modellannahmen.py`; bei jeder neuen, geklärten oder widerlegten Annahme |
| `docs/entscheidungen.md` | Entscheidungsprotokoll: was wann warum geändert wurde | Bevor eine frühere Festlegung angefasst wird | Bei jeder Entscheidung oder Änderung |
| `docs/pruefung/regeln.md` und `docs/pruefung/protokoll.md` | Maßstab und Format der Prüfer; was wann mit welchem Ergebnis geprüft wurde | Vor jeder Prüfrunde | Nach jeder Prüfrunde |

Die Anwendungsdokumentation (Fachhandbuch, Benutzerhandbuch, Architektur, Betrieb, Änderungshistorie) entsteht mit der Anwendung unter `docs/anwendung/`; eine Änderung an der Anwendung ist erst fertig, wenn ihre Dokumentation nachgezogen ist.

Nachschlagen bei Bedarf: `reports/` und `research_notes/` (Recherchebericht, Quellnotizen, Referenzrechnungen), `docs/skills-und-werkzeuge.md` (Skills, Plugins, Hooks), `docs/pruefung/<Datum>-<Thema>/` (Prüfberichte und Sichtung je Runde).

Widersprechen sich zwei dieser Dateien, gilt die Spezifikation; der Widerspruch wird sofort behoben, nicht umgangen.

**Diese Liste aktuell halten.** Sie ist nur nützlich, wenn sie stimmt. Prüfen, ob sie noch zur Dokumentationsübersicht (`docs/README.md`) und zum tatsächlichen Bestand passt,
- sofort, wenn ein steuerndes Dokument entsteht, entfällt, umbenannt wird oder seinen Zweck ändert,
- am Ende jeder Phase und an jedem Freigabepunkt (die Rolle Dokumentation prüft das mit),
- wenn der Hook beim Sitzungsstart eine fehlende oder nicht verzeichnete Datei meldet.

Gehört ein Dokument neu zu denen, ohne die man nicht richtig arbeiten kann, kommt es in die Tabelle; hat eines diese Rolle verloren, fliegt es raus. Die Tabelle bleibt kurz – alles Übrige steht in der Übersicht.

## Quellen

- Keine Rechts-, Förder- oder Normangabe ohne Eintrag im Normen- und Quellenkataster. Neue Quelle: erst ins Kataster, dann verwenden.
- Bevor eine Frage an Dritte geht (Förderbank, Hausbank, Steuerberater, Anwalt) oder eine Modellannahme gesetzt wird, wird sie am Text der einschlägigen Quelle gegengelesen; gefragt wird nur, wozu die Quelle schweigt.
- Als „am Original gelesen" gilt nur, was in dieser oder einer protokollierten Prüfung tatsächlich am Originaltext gelesen wurde; das Datum wird im Kataster nachgetragen. Zahlen und Paragrafen aus dem Gedächtnis sind keine Quelle. Ist die amtliche Stelle nicht erreichbar (etwa wegen eines Captchas; Zugangssperren werden nicht umgangen), zählt der vollständige wörtliche Abdruck bei einem Fachverlag oder in einer Volltextsammlung als eigene Belegstufe „Wortlaut in Verlagswiedergabe“, nicht als Original; eine Zusammenfassung bleibt Sekundärquelle.
- Spezifikation, Katalog, Code und Tests nennen die Kennung (zum Beispiel `BGB-559`), nicht Fundstelle und Stand – die stehen nur im Kataster.

## Modellannahmen

Lässt sich etwas vor dem Bau nicht klären, wird nicht stillschweigend eine Lesart eingebaut. Die Konvention steht in `docs/spezifikation.md`, Kapitel 8; in Kürze:

- Jede solche Setzung bekommt eine Kennung (`MA-000`) im Verzeichnis der Modellannahmen – mit der anderen Lesart, dem Gewicht und dem, der klären kann.
- Die Kennung steht überall, wo die Annahme wirkt: Spezifikation, Katalog, Code, Tests.
- Voreingestellt ist die vorsichtige Lesart; bei Gewicht hoch oder mittel nach Möglichkeit umschaltbar.
- Nicht verwechseln: eine Festlegung ist unsere Bauentscheidung, eine Eingabe gehört dem Anwender, eine ungeprüfte Quelle steht im Kataster. Eine Modellannahme ist eine Annahme über die Außenwelt, die sich als falsch herausstellen kann.

## Spezifikation ist der Pfad

`docs/spezifikation.md` ist das maßgebliche Entwicklungsdokument und wird laufend fortgeschrieben.

- Vor jeder inhaltlichen Arbeit lesen. Was dort als **fest** steht, gilt.
- Soll etwas anders gebaut werden, zuerst die Spezifikation ändern und die Änderung in `docs/entscheidungen.md` begründen, dann umsetzen. Frühere Festlegungen dürfen fallen – aber nachvollziehbar.
- Nach jeder Prüfrunde und nach jeder Antwort des Auftraggebers prüfen, ob eine Festlegung berührt ist, und sie nachziehen.
- Merkst du während der Arbeit, dass du von der Spezifikation abweichst oder sie eine Frage offenlässt: anhalten, Spezifikation klären, dann weiter.

## Zusammenarbeit

- Der Auftraggeber ist Betriebswirt, kein Programmierer. Technische Entscheidungen selbst treffen und kurz in Geschäftssprache begründen (Kosten, Risiko, Nutzen) – nicht als Auswahlfrage zurückgeben.
- Rückfragen nur zu fachlichen und betriebswirtschaftlichen Themen (Rechenlogik, Kennzahlen, Förderung, Steuern, Abläufe im Unternehmen).
- Der Auftraggeber liest die internen Unterlagen (Recherchen, Spezifikation, Prüfberichte) nicht selbst; sie sind Arbeitsgrundlage für die Entwicklung. Was er wissen oder entscheiden muss, bekommt er kurz im Gespräch und in `TASKS.md` unter „Wartet auf Nutzer“. Für interne Unterlagen ist deshalb nicht die Länge der Maßstab, sondern ob man findet, was man braucht: eine Regel an einem Ort, stimmige Verweise, keine Widersprüche.
- Sprache: Deutsch, auch in Dokumenten, Commit-Nachrichten und Oberflächentexten.

## Qualitätsanspruch

Ziel ist 9 von 10 in Code, Gestaltung und Funktionsumfang. Maßstab ist der Geschäftsbericht eines Konzerns wie Airbus, nicht die Schülerpräsentation: fachlich belastbar, durchgestaltet, ohne Füllstoff. „Funktioniert" genügt nicht.

Strikt an Branchenstandards und anerkannten Best Practices ausrichten und im Zweifel den Standard nachschlagen statt eine eigene Lösung zu erfinden:

| Bereich | Maßstab |
|---|---|
| Fachlogik | Lehrbuch-VOFI (Grob; Schulte/Ropeter), gif-Richtlinien, DIN 276/277, WoFlV, II. BV, ImmoWertV, aktuelle Gesetzes- und Förderlage mit Quelle und Stand. Offene Lehrbuchfragen zuerst über frei zugängliche, seriöse Quellen klären (Verordnungstexte, amtliche Statistik, Fachlexika, Hochschulschriften); Fachliteratur nur bei verbleibender Lücke und nur aus rechtmäßigen Quellen, nie im öffentlichen Repository ablegen |
| Finanzmodell | FAST Standard und ICAEW Financial Modelling Code: Eingaben, Rechnung und Ausgabe getrennt, keine versteckten Konstanten, Kontrollsummen |
| Berichte und Diagramme | IBCS (einheitliche Notation, Aussage im Titel, keine Dekoration), Typografie und Raster auf Geschäftsberichtsniveau |
| Oberfläche | WCAG 2.2 AA, durchgängiges Gestaltungssystem, deutsche Zahl- und Datumsformate, fachlich präzise Texte |
| Code | Rust API Guidelines, `clippy` ohne Warnungen, jede fachliche Regel mit Test und Referenzfall, exakte Geldbeträge |
| Sicherheit und Daten | OWASP ASVS, DSGVO, lückenloses Änderungsprotokoll |

Wo ein Ergebnis den Maßstab noch nicht erreicht, das dem Auftraggeber offen sagen und benennen, was zur 9 fehlt – nicht als fertig ausgeben.

### Auftreten nach außen

Alles, was Nutzer oder Kunden sehen (Oberfläche, Kundenberichte, Exporte), tritt auf wie das Produkt eines professionellen Hauses. Für interne Entwicklungsunterlagen (Recherchen, Spezifikation, Prüfprotokolle, Berichte an den Auftraggeber) gilt das nicht: Dort werden Prüfungen, Einschränkungen und Unsicherheiten offen benannt.

- Keine Hinweisflut. Interne Einschränkungen, Unsicherheiten und Entstehungsdetails bleiben hinter den Kulissen (Protokoll, `TASKS.md`, Entwicklerdokumentation).
- Ein Hinweis erscheint nur, wenn er fachlich, technisch oder rechtlich Gewicht hat – etwa Stand-Datum einer Förderkondition, eine Annahme, die das Ergebnis trägt, eine Rechengrenze, eine rechtlich gebotene Abgrenzung. Dann einmal, an der Stelle, an der er gebraucht wird, in einem Satz.
- Auch interne Dokumente bleiben lesbar: Ergebnis zuerst, Belegqualität gebündelt statt als wiederholte Vorbehalte.

### Gestaltung und Bedienung

- **`frontend-design` ist Pflicht.** Bei jeder Gestaltungsarbeit – Entwurf, Wettbewerbsbeitrag, Umsetzung oder Überarbeitung einer Oberfläche oder eines Berichtslayouts – wird zuerst der Skill `frontend-design` geladen; das gilt auch für jeden Agenten, der gestaltet. Ist der Skill nicht verfügbar, wird nicht gestaltet, sondern der Auftraggeber gebeten, das Plugin zu aktivieren.
- **Die Gestaltungsprüfung läuft von selbst.** Nach jeder Änderung an Oberflächendateien: im Browser rendern, Bildschirmfotos ablegen, die Rolle `pruefer-gestaltung` prüfen lassen (sie führt `design:design-critique` und `design:accessibility-review` aus, bei Texten `design:ux-copy`, bei Diagrammen `dataviz`), Befunde beheben, dann `.claude/hooks/gestaltung.sh bestanden`. Der Hook hält den Stopp einmal auf und nennt, was fehlt; erledigt ist die Pflicht erst mit dem Vermerk, nicht mit dem zweiten Stoppversuch. Der Auftraggeber muss dafür nichts anstoßen.

- An bewährten Vorbildern ausrichten, nicht frei erfinden: vor dem Entwurf einer Ansicht Referenzen aus guten Finanz-, Analyse- und Tabellenanwendungen ansehen (über die Mobbin-Werkzeuge, sofern verfügbar) und das Muster benennen, dem der Entwurf folgt. Die ausgewerteten Vorbilder je Kernansicht stehen in `docs/gestaltungsreferenzen.md`.
- Fertige, gepflegte Bibliotheken für Standardbausteine einsetzen (Tabellen, Diagramme, Formulare, Dialoge, Datumswahl) statt sie neu zu bauen. Eigenbau nur dort, wo das Fachliche es verlangt (VOFI-Tabelle, Förderlogik) – mit kurzer Begründung.
- Auswahl einer Bibliothek nach Pflegezustand, Lizenz, Barrierefreiheit und Passung zum Gestaltungssystem; die Entscheidung trifft Claude und hält sie fest.

## Agenten und Modelle

- Agenten (Recherche, Prüfer, Zuarbeit) laufen standardmäßig mit dem neuesten Opus-Modell.
- Das neueste Fable-Modell nur für wirklich komplexe oder folgenreiche Aufgaben: Spezifikation und Nachrechnen des Rechenkerns, Steuer- und Rechtslogik mit Auswirkung auf Ergebnisse, Sicherheits- und Rechtearchitektur, abschließende Berichte.

## Prüfrunden

- Jedes größere Arbeitsergebnis (Bericht, Fachkonzept, Rechenfunktion, Oberfläche) durchläuft vor der Übergabe Prüfrunden mit `/pruefrunde`, wiederholt bis mindestens 9 von 10 oder bis feststeht, warum das nicht erreichbar ist. Die Prüferrollen liegen in `.claude/agents/`, die gemeinsamen Regeln in `docs/pruefung/regeln.md`.
- Leerlauf nutzen: Wenn auf Hintergrundarbeit oder eine Antwort gewartet wird, das jüngste ungeprüfte Ergebnis prüfen lassen.
- Befunde der Prüfer sind Hinweise, keine Wahrheit: vor dem Einarbeiten an der Fundstelle nachprüfen.
- Wesentlichkeit vor Vollständigkeit: Ein VOFI ist ein Modell. Ein Befund wird nur dann zur Regel oder Eingabe, wenn er die Schwelle der Spezifikation besteht (tragbarer Preis über etwa 1 %, Rendite über 0,1 Prozentpunkte) oder nichts kostet; sonst wird er eine benannte Vereinfachung. Keine Flut von Eingabefeldern.
