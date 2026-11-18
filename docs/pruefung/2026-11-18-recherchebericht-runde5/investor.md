Rolle: Prüfer Investor (Geldgeber für das Softwarevorhaben und späterer Leser der Kennzahlen und Risikodarstellungen des Werkzeugs)
Prüfobjekt: reports/VOFI Immobiliensoftware Marktrecherche.md, Fassung nach der vierten Überarbeitung. Gezielte Nachprüfung (Runde 5, letzte Runde). Vollständig gelesen: Kopfteil und Abschnitt 1 (Z. 1–79), Abschnitt 3 „Kennzahlen“ und „Risikoanalyse“ (Z. 151–170), Abschnitt 5 (Z. 200–236), Anhang D.1, D.4 und D.5 (Z. 625–704) sowie Anhang E.1 (Z. 716–725). Dazu `TASKS.md` (Stand 18.11.2026), `docs/spezifikation.md` Kap. 2 und Kap. 9, Diff von Bericht und Spezifikation seit Runde 4, Sichtung Runde 4 und mein Bericht aus Runde 4. Das Rechenbeispiel in D.4 habe ich nachgerechnet.

Gesamturteil: Ja, mit Auflagen. Sieben der acht Befunde aus Runde 4 sind behoben, Befund 2 nur für die Vorprüfung. Die neue Preisregel trägt aus Kapitalgebersicht: Sie rechnet mit dem Darlehen, das die Bank gibt, weist das nötige Eigenkapital aus und nennt, welche Grenze bindet. Offen sind zwei Dinge. (a) Die Maßstäbe der Vorprüfung und die der Vorstudie stehen in Bericht, `TASKS.md` und Spezifikation noch nicht gleichlautend. (b) Über drei frei änderbare Finanzierungseingaben lässt sich der tragbare Preis unbemerkt anheben: Beleihungsquote, Wertansatz der Bank und Tilgung.

Note: 8 von 10 (Runde 1: 5 · Runde 2: 7 · Runde 3: 8 · Runde 4: 8 · Runde 5: 8). **Die 9 ist nicht erreicht.**
- **Was zur 9 fehlt:** die Befunde 1 bis 3. Sie lassen sich mit wenigen Sätzen beheben. Befund 1 und 2 betreffen `TASKS.md`, Spezifikation Kap. 2 und je einen Satz im Bericht, Befund 3 den Bericht (D.1, D.4, D.5) und Spezifikation Kap. 2. Die Vorstudie muss dafür nicht abgewartet werden.
- **Angaben des Auftraggebers:** Zur Behebung braucht es keine. Die Werte (Schwellen, Kalkulationszins, Stundensatz, Ersparnisanteil, Beleihungsquote) setzt er ohnehin. Die Befunde betreffen nur, dass sie vorher und an der richtigen Stelle bei ihm ankommen und im Projekt nicht unbemerkt verändert werden können.
- **Auf 9er-Niveau:** die Entscheidungslogik der Vorprüfung im Bericht, die zweigeteilte Bedarfsschwelle, die Mindestfallzahl mit Bezugsgröße, der Auftrag der Vorstudie mit Zuschlägen je Weg, die Preisregel selbst und das Kennzahlenblatt.

## Befunde aus Runde 4

| Nr. | Befund Runde 4 | Stand | Fundstelle und Bemerkung |
|---|---|---|---|
| 1 | Bedarfsschwelle prüft nicht den Nutzen, der den Eigenbau trägt; „drei von fünf“ bei drei Gesprächen unbestimmt | behoben | **Zwei Schwellen:** Z. 71 (allgemeiner Bedarf, sonst Abbruch) und Z. 72 (Bedarf, der nur den Eigenbau trägt, sonst Umsteuern auf Kauf gegen Excel-Ausbau), Folgen in Z. 62. **Mehrheit:** Sie ist bei drei Gesprächen (zwei Zustimmungen) und vier Gesprächen (drei) bestimmt. Gleichlautend in `TASKS.md` Z. 31 (1) und (2) und in der Spezifikation Kap. 2 „Entscheidungspunkte“. **Kleiner Rest:** Bei drei Gesprächen genügen zwei Zustimmungen. Das ist weniger, als ich vorgeschlagen hatte („mindestens drei“), bleibt aber vertretbar, weil die Mindestfallzahl unabhängig davon prüft. |
| 2 | Mindestfallzahl fehlt in `TASKS.md` und Spezifikation; Zeitpunkt der Freigabe verdeckt; Vorstudienmaßstäbe getrennt führen | teilweise | **Behoben für die Vorprüfung:** Eigener Punkt „Vor den Anwendergesprächen freigeben“ in `TASKS.md` Z. 31, gleichlautend in Spezifikation Kap. 2; Kap. 9 verweist jetzt auf `TASKS.md`. **Offen für die Vorstudie:** Zeitraum, ungünstiger Fall und Schwellen fehlen in `TASKS.md`. Der Kalkulationszins steht dort mit „spätestens vor dem Einsatz der Grobkalkulation“, also nach der Bauentscheidung, an der er gebraucht wird (neuer Befund 2). Auch in der Vorprüfung sind die Maßstäbe nicht vollständig gleichlautend (neuer Befund 1). |
| 3 | Mindestfallzahl ohne Bezugsgröße | behoben | Z. 73: Die Zeitersparnis über zehn Jahre muss die Lizenzkosten des günstigsten vorgeführten Produkts decken. Die Rechengrößen sind benannt. Gleichlautend in `TASKS.md` Z. 31 (3) und in der Spezifikation. Rest zur Folge und zu den Eingangsgrößen: neuer Befund 1. |
| 4 | Kauf-Kriterium ohne Preis | behoben | Z. 62 und Z. 70: Es wird auf eine Vorstudie umgesteuert, die nur Kauf und Excel-Ausbau vergleicht. Der Architekturentwurf entfällt, und der Preis geht in die Entscheidung ein. E.1 Z. 720 passt dazu. |
| 5 | Zuschläge für Kauf und Excel-Ausbau setzt die Vorstudie selbst | behoben im Bericht | E.1 Z. 723: +30 % als Vorschlagswert ohne Marktbeleg und Teil der Freigabe; eine Abweichung steht mit Begründung im Ergebnis. Freigabe 5 in Z. 26 nennt „ungünstiger Fall mit den Zuschlägen je Weg“. In `TASKS.md` fehlt die Freigabe (neuer Befund 2). |
| 6 | Nutzungsschwelle am Freigabepunkt vor 1b nicht verknüpft | behoben | Z. 64 nennt die Schwelle und verweist auf E.1. E.1 Z. 724 legt die Zählweise fest (Projekte im Werkzeug gegen die Fallzahl des Mengengerüsts). Zum Zählzeitraum: Befund 5. |
| 7 | Was bis zur Bauentscheidung bindet | behoben | Z. 35: sieben bis neun Termine; Anwalt und Design-Wettbewerbe sind als Kosten der Prüfung benannt, ebenso, dass die Entwürfe bei Kauf oder Excel-Ausbau nicht verwertbar sind. Der Steuerberater folgt erst vor dem ersten Kundeneinsatz, gleichlautend mit `TASKS.md` Z. 34. Dass die Wettbewerbe vor der Bauentscheidung liegen, entspricht dem Entwicklungsplan (Phase 2, Z. 16) und ist jetzt als verlorener Aufwand offen benannt. Das genügt. |
| 8 | Zielrendite wird an der verschiebungsanfälligen Größe gemessen | behoben | Z. 155: Die Fachspezifikation prüft einen Endwertüberschuss gegenüber der Zielrendite (`MA-012`). Als Aufgabe in `TASKS.md` Z. 26. |

## Abbruch- und Umsteuerkriterien (Prüffrage 2)

| Freigabepunkt | Vorher benannt | Bestimmt (auch bei 3–4 Gesprächen) | Gleichlautend Bericht / Spezifikation / `TASKS.md` |
|---|---|---|---|
| Vorprüfung | ja, als Vorschläge vor den Gesprächen | Bedarfsschwellen ja. Bei Mindestfallzahl und Katalogpflege fehlt die Folge. | nein: Der Bericht nennt in Z. 68 vier Maßstäbe, in Z. 23, Spezifikation und `TASKS.md` stehen drei (Befund 1) |
| Bauentscheidung | ja, im Bericht (Z. 63, E.1) | ja (Endwertdifferenz im ungünstigen Fall gegen die beste Alternative) | nein: Die Maßstäbe fehlen in `TASKS.md` und in der Spezifikation, der Kalkulationszins ist falsch terminiert (Befund 2) |
| Vor 1b-1 bzw. 1b-2 | ja (Z. 64, E.1) | weitgehend; der Zählzeitraum des Nutzungsgrads fehlt (Befund 5) | nur im Bericht; die Freigabe der Schwellen fehlt in `TASKS.md` (Befund 2) |
| Weitere Teilschritte | ja (Z. 65) | „Vorlagen nicht annehmen“ ist nicht bestimmt (Befund 5) | nur im Bericht |

## Preisregel (Prüffrage 3)

**Nachgerechnet:** das Beispiel in D.4, Z. 675.
- **Bankgrenze:** 107.712 € / 1,2 = 89.760 €; / 6 % = 1,496 Mio. €; / 65 % = 2,30 Mio. €.
- **Bei 2,6 Mio. €:** 0,65 × 2,6 = 1,69 Mio. €; Deckung 107.712 / 101.400 = 1,06; 1,69 − 1,496 = 0,194 Mio. €; 1,496 / 2,6 = 57,5 %.

Alle Zahlen stimmen.

**Was trägt:**
- **Was bindet, ist sichtbar.** Die Regel behandelt die Bankgrenze richtig als Grenze des Darlehens, nicht des Preises (Z. 219, 226). Das Blatt nennt zwei Bindungen: Rendite oder Eigenkapital, und Beleihungsquote oder Mindestdeckung. Das gilt im Basisfall und im kombinierten Stressfall (D.5 Z. 698, Kurzblatt Z. 700). Ich sehe also in einer Minute, ob der Preis an meiner Rendite, an meinem Eigenkapital oder an der Bank scheitert.
- **Keine Rendite auf einen Kredit, den es nicht gibt.** Das Darlehen ist gedeckelt. Oberhalb der Bankgrenze trägt jeder weitere Euro Eigenkapital nur noch die Objektrendite, die Eigenkapitalrendite sinkt also. Der Preis bleibt damit auch ohne eingegebenes verfügbares Eigenkapital durch die Zielrendite begrenzt.
- **Kein Ausweichen ins Nebeneinander.** Der geförderte Neubau rechnet als Restfinanzierung mit der Kontrollsumme „Mittelherkunft gleich Mittelverwendung“ (Z. 228, D.4 Z. 674). Die Überfinanzierung aus Runde 4 ist damit ausgeschlossen.

**Was nicht trägt:** Die Regel lässt sich über Eingaben schönrechnen, die nicht abgesichert sind (Befund 3). Zur Behandlung des Darlehens im Stressfall: Befund 4.

## Befunde

1. **[wichtig · belegt]** Bericht Z. 23 und Z. 68, Z. 62; `TASKS.md` Z. 31; Spezifikation Kap. 2 „Entscheidungspunkte“: Die Maßstäbe der Vorprüfung sind nicht gleichlautend und nicht vollständig bestimmt
   - **Vier gegen drei:** Z. 68 sagt „Die folgenden vier sind Vorschläge“ und nennt als ersten „Ein Produkt deckt den Bedarf“ (Z. 70). Z. 23, `TASKS.md` und die Spezifikation führen nur drei: zwei Bedarfsschwellen und die Mindestfallzahl. Dem Auftraggeber wird also gerade das Kriterium nicht zur Freigabe vorgelegt, das über das Umsteuern auf Kauf entscheidet.
   - **Szenario dazu:** Wird erst nach den Vorführungen festgelegt, was „deckt den Bedarf“ heißt, lässt sich die Latte an das gewünschte Ergebnis anpassen. Je nach Wunsch fallen dann alle Produkte durch, oder eines genügt. Spezifikation Kap. 2 (fest) verlangt „vorher benannte Abbruchkriterien“.
   - **Folge der Mindestfallzahl unbenannt:** Z. 62 nennt „die Fallzahlen … unter der Mindestfallzahl liegen“ in der Spalte „Umsteuern oder Abbruch“, sagt aber nicht, was davon gilt. Z. 73 begründet nur, dass dann kein Eigenbau trägt. Weil schon der Kauf nicht trägt, bleibt offen, ob der Excel-Ausbau noch verglichen wird oder ob abgebrochen wird. `TASKS.md` (3) nennt anders als (1) und (2) keine Folge.
   - **Folge bei der Katalogpflege unbenannt:** Bei „niemand die Katalogpflege übernimmt“ ist die Folge ebenso offen.
   - **Stellschrauben ohne Termin:** Stundensatz und Ersparnisanteil gibt nach Z. 73 der Auftraggeber vor. `TASKS.md` nennt sie nicht als Teil der Freigabe vor den Gesprächen. Werden sie erst mit dem Mengengerüst gesetzt, lässt sich die Mindestfallzahl über den Ersparnisanteil passend machen. Das ist genau die Lücke aus Runde 4, Befund 2.
   - **Vorschlag:**
     - (a) `TASKS.md` Z. 31 und Spezifikation um den vierten Maßstab ergänzen: „Ein Produkt deckt den Bedarf, wenn es die Prüfliste aus Anhang D erfüllt oder die Lücke mit benanntem Zukauf schließt; dann Vorstudie nur Kauf gegen Excel-Ausbau“. Die Freigabe vor den Vorführungen ansetzen, nicht erst vor den Gesprächen.
     - (b) Bei der Mindestfallzahl die Folge nennen. Mein Vorschlag: „Abbruch; der Excel-Ausbau wird nur weiterverfolgt, wenn seine Kosten unter der Zeitersparnis liegen, ohne Vorstudie“. Außerdem „Stundensatz und Ersparnisanteil geben Sie mit frei“.
     - (c) Bei der Katalogpflege die Folge „Abbruch, weil jeder Weg den Katalog braucht“ in Z. 62 ergänzen.
     - (d) Z. 23 auf „vier Maßstäbe“ berichtigen.
   - **Wo zu beheben:** in `TASKS.md`, Spezifikation Kap. 2 und Bericht Z. 23 und 62. **Wer:** das Projekt. Die Werte gibt der Auftraggeber.

2. **[wichtig · belegt]** `TASKS.md` Z. 32, Spezifikation Kap. 2 gegen Bericht Z. 26, Z. 63–64 und E.1: Die Maßstäbe der Bauentscheidung und der Teilschritte kommen beim Auftraggeber nicht an, der Kalkulationszins ist zu spät terminiert
   - **Was der Bericht vorsieht:** Freigabe 5 (Z. 26) verlangt „mit dem Auftrag der Vorstudie“ Kalkulationszins, Betrachtungszeitraum, den ungünstigen Fall mit Zuschlägen je Weg und die Schwellen für Aufwand und Nutzungsgrad.
   - **Was `TASKS.md` daraus macht:** Ein Punkt dafür fehlt. Der Kalkulationszins steht unter „Vorgaben des Hauses (fällig mit der Fachspezifikation, spätestens vor dem Einsatz der Grobkalkulation)“. Die Grobkalkulation wird erst nach der Bauentscheidung eingesetzt. Nach dem Wortlaut der Aufgabenliste darf der Zins also noch gesetzt werden, wenn die Vorstudie gerechnet ist.
   - **Warum das zählt:** Der Bericht sagt selbst, der Kalkulationszins „entscheidet über die Rangfolge mit“ (E.1 Z. 721). Ein Zins, der nach dem Ergebnis gewählt wird, ist das klassische Mittel, einen Eigenbau mit frühen Kosten schönzurechnen. Dasselbe gilt für die Zuschläge +50 %, +30 % und −50 % Nutzen und für die Schwellen +50 % Aufwand und Nutzungsgrad unter der Hälfte. Sie stehen nur im Bericht, den der Auftraggeber nicht liest (CLAUDE.md, „Zusammenarbeit“).
   - **Spezifikation:** Kap. 2 führt nur die Schwellen der Vorprüfung. Für die Bauentscheidung und die Teilschritte, die ebenfalls „vorher benannte Abbruchkriterien“ brauchen, steht dort nichts.
   - **Vorschlag:**
     - In `TASKS.md` einen eigenen Punkt anlegen: „Mit dem Auftrag der Vorstudie freigeben, bevor sie gerechnet wird: Kalkulationszins; Zeitraum zehn Jahre; ungünstiger Fall (Eigenbau +50 % Entwicklung, Einführung beim Kauf und Excel-Ausbau +30 %, Nutzen −50 %); Schwellen für den Bau (Aufwand je Teilschritt mehr als 50 % über der Schätzung, Nutzungsgrad unter der Hälfte)“.
     - Den Kalkulationszins aus den „Vorgaben des Hauses“ streichen oder dort auf „spätestens mit dem Auftrag der Vorstudie“ terminieren.
     - In Spezifikation Kap. 2 „Entscheidungspunkte“ einen Satz ergänzen: „Die Maßstäbe der Bauentscheidung und der Teilschritte gibt der Auftraggeber mit dem Auftrag der Vorstudie frei (Bericht, Anhang E.1)“.
   - **Wo zu beheben:** in `TASKS.md` und der Spezifikation, nicht erst in der Vorstudie. **Wer:** das Projekt. Die Werte gibt der Auftraggeber.

3. **[wichtig · belegt]** Bericht D.1 Z. 634, D.4 Z. 674, D.5 Z. 698/700 gegen Spezifikation Kap. 2 „Zielrendite und Schwellen“: Der tragbare Preis lässt sich über Finanzierungseingaben unbemerkt anheben
   - **Widerspruch zur Spezifikation:** Spezifikation Kap. 2 (fest) führt die Beleihungsquote als „Vorgabe des Hauses aus dem Katalog“, ebenso der Bericht in Freigabe 7 (Z. 28). D.1 zählt sie dagegen zu den Eingaben der Grobkalkulation („Beide: … Beleihungsquote, Zins, Tilgung …“). Die Mindestdeckung kommt nur als Voreinstellung. Eine Regel wie bei den Stresshöhen, die im Projekt nur verschärft werden dürfen, und der Zielrendite, die nur mit sichtbarer Begründung abweicht, fehlt für Beleihungsquote, Mindestdeckung und Wertansatz.
   - **Drei Hebel:**
     - Die Beleihungsquote anheben.
     - Den Wertansatz der Bank über den Kaufpreis setzen, denn er ist „überschreibbar“ (D.4).
     - Die Tilgung senken. Bei gleicher Mindestdeckung erlaubt ein geringerer Kapitaldienst ein größeres Darlehen.
   - **Wirkung:** Jeder Hebel vergrößert das gedeckelte Darlehen, erhöht so den Hebel auf das Eigenkapital und hebt den höchsten tragbaren Preis.
   - **Gegenrechnung am Beispiel D.4:** Bei 6 % Kapitaldienst trägt die Deckung 1,496 Mio. €. Senkt der Bearbeiter die Tilgung um einen Prozentpunkt auf 5 % Kapitaldienst, trägt sie 89.760 / 0,05 = 1,795 Mio. €, also rund 300.000 € mehr Darlehen. Bei 65 % Beleihung begrenzt dann bis rund 2,76 Mio. € (statt 2,30 Mio. €) die Quote. Auf dem Kurzblatt stehen „Beleihungsquote bindet“ oder „Mindestdeckung bindet“, aber nicht, dass ein Wert von der Vorgabe des Hauses abweicht.
   - **Szenario:** Ein indikatives Gebot geht mit Kurzblatt und Standkennung hinaus (Z. 700). Es beruht auf 75 % Beleihung, 1 % Tilgung und einem Wertansatz über dem Kaufpreis, und keiner der Werte ist durch ein Bankangebot belegt. Das ist genau das, was die Zielrendite-Regel in Z. 155 verhindern soll („sonst ließe sich der tragbare Kaufpreis unbemerkt … heben“).
   - **Vorschlag:**
     - Beleihungsquote, Mindestdeckung und eine Mindesttilgung als Vorgaben des Hauses aus dem Katalog führen.
     - Im Projekt nur verschärfen; eine Lockerung nur mit Begründung, etwa einer vorliegenden Finanzierungszusage, und sichtbar auf Kurzblatt und Kennzahlenblatt („Finanzierung abweichend von der Vorgabe des Hauses: …“).
     - Den Wertansatz der Bank nur nach unten frei überschreiben; nach oben nur mit derselben Kennzeichnung.
     - D.1 entsprechend umsortieren: die Beleihungsquote aus den Eingaben zu den Voreinstellungen.
     - In Spezifikation Kap. 2 die Zeile „Zielrendite und Schwellen“ um einen Halbsatz ergänzen.
   - **Wo zu beheben:** im Bericht (D.1, D.4, D.5) und in der Spezifikation. **Wer:** das Projekt. Die Werte der Vorgaben gibt der Auftraggeber mit Freigabe 7.

4. **[Hinweis · begründete Einschätzung]** D.5 Z. 698 und `MA-026`: Unklar, ob das Darlehen im kombinierten Stressfall neu bemessen wird
   - **Problem:** Der tragbare Preis steht „im Basisfall und im kombinierten Stressfall“. Nicht gesagt ist, ob die Deckelung im Stressfall aus dem gestressten Reinertrag neu gerechnet wird oder ob das Darlehen aus dem Basisfall stehen bleibt. Wirtschaftlich gilt meist der zweite Fall: Die Bank bemisst bei Abschluss, und der Stress trifft danach den Cashflow.
   - **Folge:** Eine Neubemessung im Stress senkt das Darlehen und erhöht das Eigenkapital. Das ergibt einen doppelt vorsichtigen, aber andersartigen Preis, und der Ausweis „Mindestdeckung bindet“ verlöre seinen Sinn. Zwei Bearbeiter könnten dasselbe Blatt verschieden lesen.
   - **Vorschlag:** In der Fachspezifikation festlegen, dass das Darlehen im Stressfall aus dem Basisfall stehen bleibt. Die gestresste Schuldendienstdeckung wird als Kennzahl ausgewiesen, nicht als neue Deckelung. Der Satz gehört in Spezifikation Kap. 3 oder unter `MA-026`.
   - **Wo zu beheben:** in der Fachspezifikation (Phase 1), nicht im Bericht. **Wer:** das Projekt, gegebenenfalls mit Bestätigung der Hausbank.

5. **[Hinweis · begründete Einschätzung]** Z. 64 und Z. 65 mit E.1 Z. 724: Zwei Kriterien an den Teilschritten sind nicht vollständig bestimmt
   - **Zählzeitraum fehlt:** Der Nutzungsgrad wird „für denselben Zeitraum“ gezählt, welcher Zeitraum das ist, steht nirgends. Szenario: Nach einem Monat sind zwei von zehn Grobkalkulationen im Werkzeug entstanden, nach sechs Monaten sieben von zehn. Ohne festen Zeitraum lässt sich der Zeitpunkt der Messung nach dem Ergebnis wählen.
   - **„Nicht annehmen“ ohne Maß:** Bei „Bank oder Gremium die Vorlagen nicht annehmen“ ist offen, ob eine einzige Ablehnung genügt.
   - **Vorschlag:** Festlegen, dass der Nutzungsgrad über die ersten sechs Monate nach Einsatz von 1a gezählt wird. Für das zweite Kriterium: „Mehr als eine von drei Vorlagen wird wegen der Form oder des Rechenwegs zurückgewiesen“. Ablehnungen aus anderen Gründen zählen nicht. Beides als Vorschlag in E.1, freizugeben mit den Schwellen der Vorstudie (Befund 2).
   - **Wo zu beheben:** in Bericht E.1 und `TASKS.md` (Punkt aus Befund 2). **Wer:** das Projekt schlägt vor, der Auftraggeber gibt frei.

Nicht geprüft:
- **Unveränderte Teile:** Auftragsgemäß nicht erneut geprüft wurden Abschnitte 2, 4, 6 bis 9 und die Anhänge A bis C.
- **Fachwerte:** Rechts-, Steuer- und Förderwerte sowie die Restwertprobe in Anhang A sind Sache von Jurist, Fachexperte und Finanzmathematiker.
- **Herstellerangaben:** Nicht online nachrecherchiert; meine Rolle liest nur.
- **Preisregel am Testfall:** Wie stark der Preis nach der neuen Regel vom alten „niedrigeren Wert“ abweicht, habe ich nicht nachgerechnet. Das liegt beim Finanzmathematiker. Gegengerechnet habe ich nur das Beispiel in D.4 und die Wirkung einer niedrigeren Tilgung in Befund 3.
- **Vorschlagswerte:** Sechs Monate und „eine von drei“ in Befund 5 sowie die Folge der Mindestfallzahl in Befund 1 sind Vorschläge zur Freigabe, keine belegten Werte.
