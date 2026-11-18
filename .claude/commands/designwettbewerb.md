---
description: Design-Wettbewerb – mindestens fünf Agenten entwerfen dieselbe Ansicht nach demselben Auftrag in verschiedenen Richtungen; eine Jury bewertet verdeckt
---

Führe einen Design-Wettbewerb durch. Ansicht: $ARGUMENTS
(Ohne Angabe: die nächste Kernansicht ohne abgenommenen Entwurf laut `docs/gestaltungsreferenzen.md` und `docs/spezifikation.md`, Kapitel 6.)

Warum ein Wettbewerb: Ein einzelner Entwurf landet verlässlich beim Naheliegenden. Fünf Entwürfe, die sich unterscheiden müssen, zeigen den Lösungsraum; die Jury entscheidet am Sichtbaren, nicht an der Begründung.

1. **Auftrag schreiben** – ein Dokument, für alle Teilnehmer gleich, unter `gestaltung/wettbewerb/<Datum>-<Ansicht>/auftrag.md`:
   - Wer die Ansicht benutzt und welche drei bis fünf Aufgaben er dort erledigt (aus den Abläufen des Praktikers).
   - Echte Zahlen: ein Referenzfall aus den Abnahmetests, vollständig, mit langen Bezeichnungen, negativen Werten und einem Randfall. Kein Blindtext, keine erfundenen Schönwetterdaten.
   - Verbindliches: Spezifikation Kapitel 5 und 6, IBCS für Tabellen und Diagramme, WCAG 2.2 AA, deutsche Zahl- und Datumsformate, Bedienung per Tastatur, Verhalten bei 1280 und 1920 Pixeln Breite.
   - Vorbilder aus `docs/gestaltungsreferenzen.md` zu dieser Ansicht – als Anregung, nicht als Vorlage.
   - Abgabe: eine eigenständige, klickbare HTML-Seite ohne Server (`index.html`), dazu `begruendung.md` mit höchstens 200 Wörtern: welchem Muster der Entwurf folgt, was er bewusst anders macht, welche Bibliothek die Umsetzung tragen würde.

2. **Mindestens fünf Teilnehmer, jeder mit eigener Richtung.** Die Richtung wird zugewiesen, damit nicht fünfmal dasselbe entsteht; passe sie der Ansicht an:

   | Teilnehmer | Richtung |
   |---|---|
   | A | Tabellenkalkulation zuerst: maximale Dichte, Tastatur, Verhalten wie Excel |
   | B | Geführter Ablauf: Schritt für Schritt, wenige Entscheidungen je Bildschirm |
   | C | Bericht zuerst: die Ansicht sieht aus wie die fertige Vorlage und ist dort bearbeitbar |
   | D | Verdichtung: wenige Kennzahlen oben, Einzelheiten erst auf Abruf |
   | E | Radikal reduziert: nur was für die Aufgabe nötig ist, ein Blick, eine Handlung |
   | F (optional) | Freie Wahl – ausdrücklich gegen die anderen fünf |

   Jeder Teilnehmer ist ein eigener Agent (Modell: das neueste Opus), arbeitet in `…/<Buchstabe>/` und sieht die anderen Entwürfe nicht. Er lädt als Erstes den Skill `frontend-design` – das ist Pflicht; ist der Skill nicht verfügbar, findet der Wettbewerb nicht statt und der Auftraggeber wird gebeten, das Plugin zu aktivieren. Dazu nutzt er `dataviz` für Diagramme und `design:ux-copy` für Texte. Im Auftrag an ihn steht nur der Auftrag und seine Richtung – keine Erwartung, wie das Ergebnis aussehen soll.

3. **Sichtbar machen.** Jeden Entwurf im Browser rendern (Playwright ist vorhanden) und Bildschirmfotos bei 1280 und 1920 Pixeln sowie von einem bedienten Zustand ablegen. Was nicht rendert oder mit erfundenen Zahlen arbeitet, scheidet aus und wird nachgefordert.

4. **Verdeckte Jury.** Die Jury sieht Bildschirmfotos und Seiten unter den Buchstaben, nicht die Begründungen. Juroren, jeder für sich:
   - Rolle `pruefer-gestaltung` (führt `design:design-critique` und `design:accessibility-review` aus und misst an `frontend-design`)
   - Rollen `pruefer-praktiker`, `pruefer-endnutzer`, `pruefer-controller`, `pruefer-slop`

   Bewertet wird je Entwurf mit 1 bis 10:

   | Kriterium | Gewicht |
   |---|---|
   | Aufgaben lösbar: Schritte und Sucharbeit bis zum Ziel | 30 % |
   | Zahlen lesbar und einordenbar; IBCS eingehalten | 20 % |
   | Eigenständig und stimmig, kein Einheitsbrei | 15 % |
   | Barrierefreiheit und Tastaturbedienung | 15 % |
   | Verhalten bei vielen Zeilen, langen Texten, Randfall | 10 % |
   | Umsetzbar mit gepflegten Bibliotheken | 10 % |

   Jeder Juror nennt zusätzlich je Entwurf das eine Element, das übernommen werden sollte, auch wenn der Entwurf verliert.

5. **Auswerten.** Tabelle der gewichteten Noten je Juror; Abweichungen zwischen Juroren benennen statt mitteln. Vorschlag: Sieger plus die besten Einzelelemente der anderen. Die Bildschirmfotos der zwei bis drei besten Entwürfe gehen mit der Auswertung an den Auftraggeber; er entscheidet.

6. **Verfeinern und festhalten.** Den gewählten Entwurf mit den übernommenen Elementen überarbeiten und durch `/pruefrunde` schicken (Tabelle „Oberfläche, Eingabemasken"). Was dabei über die eine Ansicht hinaus gilt – Farben, Typografie, Raster, Tabellenregeln, Bausteine –, wandert in das Gestaltungssystem (Spezifikation Kapitel 6); die Entscheidung ins Entscheidungsprotokoll. Die unterlegenen Entwürfe bleiben im Ordner des Wettbewerbs als Beleg, nicht als Vorlage.

Umfang: Ein Wettbewerb kostet rund ein Dutzend Agentenläufe. Er lohnt sich für die prägenden Ansichten (Finanzplan-Tabelle, Eingabe der Annahmen, Kennzahlenblatt mit Bericht) – die übrigen folgen dem dort gefundenen Gestaltungssystem ohne eigenen Wettbewerb.
