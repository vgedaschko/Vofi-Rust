Rolle: Prüfer Investor (Geldgeber für das Softwarevorhaben und späterer Leser der Kennzahlen und Risikodarstellungen des Werkzeugs)
Prüfobjekt: reports/VOFI Immobiliensoftware Marktrecherche.md, Fassung nach Prüfrunde 3 (Z. 1–739 vollständig gelesen, einschließlich Anhang E.1), gegen Spezifikation, Entwicklungsplan und `TASKS.md` (Stand jeweils 18.11.2026), das Änderungsdiff seit Runde 3, die Sichtung der Runde 3 und den eigenen Bericht aus Runde 3

Gesamturteil: Ja, mit kleinen Auflagen. Alle neun Befunde aus Runde 3 sind aufgenommen, acht davon vollständig. Die Vorstudie kann ihr Abbruchkriterium jetzt tatsächlich prüfen: Der ungünstige Fall trifft je Weg dessen eigene Unsicherheit, und der Zins ist eine Freigabe. Zielrendite und Stresshöhen sind gegen Schönrechnen geschützt. Das Kennzahlenblatt beantwortet die Gremienfragen zu kritischem Ausstiegsfaktor und Anschlusszins. Eine Lücke bleibt am ersten Freigabepunkt. Die Schwelle „Bedarf bestätigt“ fragt nach einem Nutzen, den auch Kauf und Excel-Ausbau liefern. Ob es den Nutzen gibt, der nur den Eigenbau trägt, prüft sie nicht, obwohl der Bericht selbst das von den Gesprächen verlangt. Zudem fehlt die Mindestfallzahl in der Liste, nach der der Auftraggeber arbeitet.

Note: 8 von 10 (Runde 1: 5, Runde 2: 7, Runde 3: 8)
- **Auf 9er-Niveau:** Entscheidungslogik, Vorstudie, Ehrlichkeit über die Belege und Kennzahlenblatt.
- **Was zur 9 fehlt:** die Befunde 1 und 2. Beide lassen sich mit wenigen Sätzen beheben, Befund 1 im Bericht, Befund 2 in `TASKS.md` und Spezifikation Kap. 9.
- **Angaben des Auftraggebers:** Dafür braucht es keine. Die Schwellen selbst setzt er, aber der Bericht weist sie schon als seine Freigabe aus.
- **Ausblick:** Eine weitere Überarbeitung kann die 9 erreichen. Die übrigen Befunde sind Hinweise und für die 9 nicht nötig.
- **Wirtschaftlichkeitsrechnung:** Dass eine bezifferte Rechnung fehlt, ist gemäß Zweck kein Abzug. Sie bleibt offen beim Auftraggeber (Mengengerüst) und bei Phase 2 (Aufwandsschätzung).

## Befunde aus Runde 3

| Nr. | Befund Runde 3 | Stand | Fundstelle und Bemerkung |
|---|---|---|---|
| 1 | Ungünstiger Fall der Vorstudie wirkt auf alle Wege gleich; Zins fehlt | behoben | Z. 85 nennt, warum eine gleichmäßige Verteuerung nichts prüfte. E.1 Z. 723 rechnet mit dem Kalkulationszins des Hauses und begründet, warum er die Rangfolge mitbestimmt. E.1 Z. 725 setzt den ungünstigen Fall je Weg. Den Zins gibt der Auftraggeber unter Freigabe 5 frei (Z. 26). Restpunkt zu den Zuschlägen für Kauf und Excel-Ausbau in Befund 5 |
| 2 | Zielrendite frei je Projekt; Warnschwelle Restwertanteil ohne Zuständigkeit | behoben | Z. 161: Vorgabe je Investorensicht und Nutzungsart, Abweichung nur mit Begründung und sichtbar; in Kundenberichten gibt der Kunde die Zielrendite vor. Freigabe 7 (Z. 28) mit Warnschwelle; D.5 Z. 700; Spezifikation Kap. 2 „Zielrendite und Schwellen“ (fest) |
| 3 | Vorprüfung ohne Prüfliste und Schwellen; Mengengerüst ohne Kriterium | weitgehend behoben | Prüfliste aus Anhang D mit Beratungseinsatz, Kundenlizenz, Preis und Katalogpflege (Z. 79), zuständig ist das Projekt (Z. 347). Bedarfsschwelle „drei von fünf“ als Vorschlag (Z. 79). Mindestfallzahl als Abbruchkriterium (Z. 73), Freigabe vor den Gesprächen (Z. 23). Offen: Die Bedarfsschwelle prüft den falschen Nutzen (Befund 1). Die Mindestfallzahl fehlt in `TASKS.md` (Befund 2) und hat keine Bezugsgröße (Befund 3) |
| 4 | Kombinierter Stressfall in voller Höhe und mit allen Größen | behoben | Z. 163, D.5 Z. 701, Spezifikation Kap. 2: ermäßigte Höhen, nur wirksame Größen je Vorhabensart und Förderstatus; Freigabe der Höhen getrennt nach Einzel- und kombiniertem Fall (Z. 28) |
| 5 | Grobkalkulation ohne schlechten Fall | behoben | Z. 218, D.5 Z. 700 und 702: tragbarer Preis und verkürztes Blatt auch im kombinierten Stressfall. Die Stresshöhen sind vor dem Einsatz von 1a freizugeben (Z. 28, 174). Zusätzlich kam die Bankgrenze hinzu (Z. 228, D.4 Z. 677). Das Rechenbeispiel habe ich nachgerechnet und es stimmt: 107.712 € Reinertrag / 1,2 = 89.760 €; / 6 % = 1,496 Mio. €; / 65 % = 2,30 Mio. €; bei 2,6 Mio. € Deckung 1,06 |
| 6 | Mengengerüst in den steuernden Dateien uneinheitlich | behoben | Spezifikation Kap. 9 Nr. 3 und `TASKS.md` Z. 35 führen jetzt Beratungsmandate und Honorare |
| 7 | Sofortige Verteilung in 1a nur behauptet | behoben | Z. 236: Die Aufwandsschätzung der Phase 2 weist sie als eigenen Posten aus |
| 8 | Kritische Werte; Finanzierungslücke und Nachschuss nicht abgegrenzt | behoben | Z. 166–168: kritischer Anschlusszins und kritischer Ausstiegsfaktor; Finanzierungslücke ausdrücklich vor dem Ausgleich über Kontokorrent und Nachschuss, Nachschussbedarf als spätere Einlage. Die Endwertdifferenz führt (Z. 159). Die kritischen Werte stehen ab 1b; in 1a liefert sie die Zielwertsuche auf jede Eingabe (D.1 Z. 641). Das genügt |
| 9 | Was die Freigabe beim Auftraggeber bindet | teilweise | Z. 46 nennt die Aufträge 9 bis 14 und die Fremdkosten bis zur Vorprüfung. Zeitrahmen und Personentage fehlen weiterhin, und die Angabe zu Anwalt und Steuerberater ist ungenau (Befund 7) |

## Befunde

1. **[wichtig · belegt]** Abschnitt 1, Z. 54 gegen Z. 79 und Z. 73: Die Bedarfsschwelle prüft nicht den Nutzen, der den Eigenbau trägt
   - **Was der Bericht verlangt:** Z. 54 sagt, der Eigenbau müsse sich aus dem rechtfertigen, „was nur er bietet: lückenloses Änderungsprotokoll, Arbeit mehrerer Personen an einem Projekt und Berichte für Kunden. Ob dieser Nutzen besteht, fragen die Anwendergespräche ab.“
   - **Was die Schwelle prüft:** Z. 79 setzt nur: „mindestens drei von fünf Befragten [würden] die Grobkalkulation statt Excel nutzen“. Eine Grobkalkulation liefern aber auch ein gekauftes System und ein ausgebautes Excel-Modell mit Katalog. Die Frage, wie oft mehrere Personen mit Freigaben oder Kundenzugang arbeiten, wird gestellt (Z. 34), ist aber an kein Kriterium gebunden.
   - **Szenario:** Vier von fünf Befragten wollen eine schnellere Grobkalkulation. Alle arbeiten allein an ihren Projekten, und Kunden wollen PDF-Berichte, keinen Zugang. Die Vorprüfung gilt dann als bestanden, und Phase 2 beginnt mit Architektur, Gestaltung und Aufwandsschätzung. Erst die Vorstudie zeigt danach, dass der Excel-Ausbau denselben Nutzen billiger bringt. Die Vorprüfung hätte das früher und billiger erkannt.
   - **Mehrdeutige Schwelle:** „Drei von fünf“ ist bei nur drei Gesprächen nicht bestimmt; der Auftrag lautet „drei bis fünf“ (Z. 34).
   - **Vorschlag:** Die Bedarfsschwelle in zwei Teile teilen, beide als Freigabe 2.
     - (a) Bedarf an einem besseren Werkzeug: die Mehrheit der Befragten, mindestens drei, würde die Grobkalkulation statt Excel nutzen.
     - (b) Bedarf, der nur den Eigenbau trägt: mindestens eine benannte Zahl der Befragten braucht Änderungsprotokoll, Mehrpersonenarbeit mit Freigabe oder Berichte und Zugang für Kunden. Je nach Merkmal werden dafür interne Anwender oder Kunden befragt.
     - Folgen: Wird (a) verfehlt, wird abgebrochen. Wird nur (b) verfehlt, wird umgesteuert: Die Vorstudie entfällt oder vergleicht nur Kauf und Excel-Ausbau. Ein Satz in Z. 79 und eine Ergänzung in der Spalte „Umsteuern oder Abbruch“ in Z. 73 genügen.

2. **[wichtig · belegt]** `TASKS.md` „Wartet auf Nutzer“ Z. 25 und Spezifikation Kap. 9 Nr. 6 gegen Bericht Z. 23 und Z. 73: Mindestfallzahl fehlt, Zeitpunkt der Freigabe nicht erkennbar
   - **Warum es zählt:** Nach CLAUDE.md („Zusammenarbeit“) liest der Auftraggeber die internen Unterlagen nicht selbst. Was er entscheiden muss, bekommt er im Gespräch und über `TASKS.md`.
   - **Was dort fehlt:** `TASKS.md` Z. 25 führt die Schwelle für „Bedarf bestätigt“, aber nicht die Mindestfallzahl. Spezifikation Kap. 9 Nr. 6 führt keine der beiden.
   - **Zeitpunkt verdeckt:** Beide Schwellen sind nach Z. 23 „vor den Anwendergesprächen“ freizugeben. In `TASKS.md` stehen sie aber in einem Punkt mit den Vorgaben für 1a und dem Kalkulationszins der Vorstudie, die erst viel später fällig sind.
   - **Folge:** Spezifikation Kap. 2 „Entscheidungspunkte“ (fest) verlangt „vorher benannte Abbruchkriterien“. Wird die Mindestfallzahl erst gesetzt, wenn das Mengengerüst vorliegt, ist sie nicht mehr vorher benannt. Dann lässt sie sich an die gelieferte Zahl anpassen.
   - **Vorschlag:** In `TASKS.md` einen eigenen Punkt „Vor den Anwendergesprächen: Maßstäbe der Vorprüfung freigeben (Bedarfsschwelle nach Befund 1, Mindestfallzahl)“ anlegen. Kalkulationszins, ungünstigen Fall und Schwellen der Vorstudie getrennt davon „mit dem Auftrag der Vorstudie“ führen und die Vorgaben für 1a „vor dem Einsatz von 1a“. Spezifikation Kap. 9 entsprechend nachziehen. Nach CLAUDE.md ist ein solcher Widerspruch sofort zu beheben.

3. **[Hinweis · begründete Einschätzung]** Z. 79: Mindestfallzahl ohne Bezugsgröße
   - **Problem:** Die Mindestfallzahl setzt der Auftraggeber, „bevor das Mengengerüst vorliegt; ein Vorschlag wäre ohne Ihre Zahlen geraten.“ Woran er sie messen soll, sagt der Bericht nicht. Eine Aufwandsschätzung gibt es vor Phase 2 bewusst nicht. Eine Fallzahl, die ohne Bezug auf irgendeine Kostengröße gesetzt wird, ist genauso geraten.
   - **Vorschlag:** Statt einer Zahl eine Regel vorgeben, deren Größen zur Vorprüfung vorliegen. Die Fallzahl gilt als ausreichend, wenn die Zeitersparnis über zehn Jahre mindestens die Lizenzkosten des günstigsten vorgeführten Produkts deckt. Gerechnet wird Kalkulationen pro Jahr × Stunden je Kalkulation × Stundensatz des Hauses × angenommener Ersparnisanteil. Die Lizenzkosten kommen aus den Vorführungen, Ersparnisanteil und Stundensatz gibt der Auftraggeber vor. Trägt die Fallzahl nicht einmal den Kauf, trägt sie keinen Eigenbau.

4. **[Hinweis · begründete Einschätzung]** Z. 73, Spalte „Umsteuern oder Abbruch“: Das Kauf-Kriterium ist ohne Preis
   - **Problem:** Deckt ein Produkt den Bedarf, heißt es „dann Kauf mit eigenem Katalog“, und zwar schon an der Vorprüfung, ohne Vorstudie. Der Preis steht zwar auf der Prüfliste (Z. 79), ist aber nicht Teil des Kriteriums. Ein Produkt, das alles kann, aber ein Vielfaches des Excel-Ausbaus kostet, führte so ohne Rechnung zum Kauf. Das kann bei einer Suite geschehen, die an das ERP gekoppelt ist (Z. 61).
   - **Vorschlag:** „Dann Umsteuern auf Kauf: Die Vorstudie vergleicht nur noch Kauf und Excel-Ausbau, ohne Architekturentwurf für den Eigenbau.“ Das erspart den größten Teil der Phase 2 und hält den Vergleich fair.

5. **[Hinweis · begründete Einschätzung]** E.1 Z. 725: Die Zuschläge für Kauf und Excel-Ausbau setzt die Vorstudie selbst
   - **Problem:** Beim Eigenbau ist der ungünstige Fall beziffert (+50 %) und eine Freigabe des Auftraggebers. Einführung beim Kauf und Excel-Ausbau „erhalten eigene Zuschläge, die die Vorstudie begründet“. Damit bestimmt der Bearbeiter, der die Vorstudie rechnet, die Hälfte des Vergleichs selbst. Werden die Zuschläge der Alternativen großzügig angesetzt, schließt sich der Abstand, den Z. 85 gerade offenhalten will.
   - **Vorschlag:** Auch für diese Zuschläge einen Vorschlag zur Freigabe nennen, etwa +30 % auf Einführung und Excel-Ausbau, und sie in Freigabe 5 (Z. 26) ausdrücklich aufnehmen. Weicht die Vorstudie davon ab, steht die Abweichung mit Begründung im Ergebnis.

6. **[Hinweis · belegt]** Z. 75 gegen E.1 Z. 726: Nutzungsschwelle am Freigabepunkt vor 1b nicht verknüpft
   - **Problem:** E.1 setzt eine bezifferte Schwelle: Nutzungsgrad unter der Hälfte der Kalkulationen aus dem Mengengerüst. Der Freigabepunkt vor der Vollkalkulation, an dem sie zuerst greifen müsste, nennt sie nicht. Dort steht nur „Grobkalkulationen weiter in Excel entstehen“, und auf E.1 verweist er allein beim Aufwand.
   - **Vorschlag:** In Z. 75 heißt es dann: „der Nutzungsgrad der Grobkalkulation unter der Schwelle liegt (Anhang E.1)“. Gezählt wird über die Projekte im Werkzeug gegen die Fallzahl des Mengengerüsts für denselben Zeitraum.

7. **[Hinweis · belegt]** Z. 46: Was bis zur Bauentscheidung bindet, unvollständig und in einem Punkt ungenau
   - **Steuerberater zu früh angesetzt:** Z. 46 sagt: „Anwalt und Steuerberater werden erst in Phase 2 gebraucht.“ Nach B.5 (Z. 536–556) und Z. 42 braucht es in Phase 2 nur den Anwalt, für Datenschutz, Mitbestimmung und Nutzungsrechte. Der Steuerberater wird erst vor dem ersten Kundeneinsatz gebraucht.
   - **Kosten vor der Bauentscheidung nicht benannt:** Die Anwaltskosten entstehen vor der Bauentscheidung (Z. 74, 302). Sie sind damit Kosten der Prüfung und nicht des Baus, und als solche nennt sie der Bericht nicht.
   - **Gestaltung vor der Bauentscheidung:** Z. 52 setzt die Gestaltung vor die Bauentscheidung. Nach dem Entwicklungsplan sind das drei Design-Wettbewerbe mit je einer Auswahl durch den Auftraggeber. Endet das Vorhaben mit Kauf oder Excel, ist diese Arbeit anders als die Fachspezifikation nicht verwertbar, obwohl Z. 52 die Verwertbarkeit nur für die Fachspezifikation behauptet.
   - **Zeitrahmen fehlt:** Ein grober Zeitrahmen bleibt aus (siehe Tabelle, Nr. 9). Er wäre ohne erfundene Zahlen möglich, als Zahl der Termine: ein NBank-Gespräch, drei bis fünf Gespräche, drei Vorführungen.
   - **Vorschlag:**
     - (a) Z. 46 berichtigen: Bis zur Bauentscheidung fallen Lehrbücher und eine anwaltliche Prüfung an, der Steuerberater folgt vor dem ersten Kundeneinsatz.
     - (b) Den Bezug auf die Bauentscheidung begründen: Entweder sagt der Bericht in einem Satz, warum die Aufwandsschätzung die Gestaltung vorher braucht. Oder vor der Bauentscheidung entsteht nur der Wettbewerb, der die Schätzung trägt, und die übrigen folgen danach.
     - (c) Die Termine zählen, die die Vorprüfung beim Auftraggeber bindet.

8. **[Hinweis · begründete Einschätzung]** Z. 161 und Z. 227 mit A.3 Nr. 13 (Z. 385): Die Zielrendite wird an der Größe gemessen, die der Bericht selbst für verschiebungsanfällig erklärt
   - **Problem:** Die Endwertdifferenz führt, weil die Rendite davon abhängt, in welche Periode Einlagen und Entnahmen fallen (Z. 159). Die Zielrendite und damit der wichtigste Wert der Grobkalkulation werden aber über die Rendite geprüft. Gemeint sind der Abstand zur Zielrendite und die Renditegrenze des tragbaren Preises (Z. 227). A.3 Nr. 13 sagt selbst, dass dieser Abstand „durch einen Monat Verschiebung kippen“ kann. Die Endwertdifferenz misst nur gegen die nahezu risikolose Alternative (Z. 161).
   - **Folge:** Gerade die Prüfung gegen die Risikoprämie hängt an der anfälligen Größe. Bei einer einzigen Einlage zu Beginn spielt das keine Rolle. Bei Neubau mit Eigenkapital über die Bauzeit, mit Nachschüssen und Ausschüttungen schon.
   - **Vorschlag:** Neben die Rendite einen Endwertüberschuss gegenüber der Zielrendite stellen: den Endwert abzüglich der Einlagen, aufgezinst mit der Zielrendite, zuzüglich der aufgezinsten Entnahmen. Die Renditegrenze des tragbaren Preises lässt sich darauf beziehen. Im Bericht genügt ein Satz in Z. 161, der diese Möglichkeit als Frage an die Fachspezifikation neben die Entscheidung aus A.3 Nr. 13 stellt. Die Formel gehört in die Fachspezifikation und unter `MA-012`.

Nicht geprüft:
- **Fachwerte:** Rechts-, Steuer- und Förderwerte (Anhänge B und C) und die finanzmathematischen Referenzwerte in Anhang A habe ich nicht geprüft. Das ist Sache der Fach-, Rechts- und Rechenprüfer; ich habe die Werte als gegeben genommen. Nachgerechnet habe ich nur das Beispiel der Bankgrenze in D.4.
- **Herstellerangaben:** Nicht online nachrecherchiert, weil meine Rolle auf Lesen beschränkt ist.
- **Zahlen in den Vorschlägen:** Der Zuschlag von +30 % in Befund 5 und die Rechenregel in Befund 3 sind Vorschläge zur Freigabe, keine belegten Marktwerte.
- **Rechnerische Wirkung:** Wie stark der Endwertüberschuss gegenüber der Zielrendite (Befund 8) den tragbaren Preis eines Neubaus verschiebt, habe ich nicht am Testfall nachgerechnet.
