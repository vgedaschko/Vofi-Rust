# Sichtung der Prüfrunde 5 – Recherchebericht (2026-11-18)

Letzte Runde, gezielte Nachprüfung der Stellen, die nach Runde 4 geändert wurden.

Noten (Runde 1 → 2 → 3 → 4 → 5): Finanzmathematiker 7 → 8 → 9 → 9 → **9** · Jurist 6 → 7 → 9 → 9 → **9** · Fachexperte 6 → 8 → 8 → 8 → **9** · Praktiker 5 → 7 → 8 → 8 → **9** · Einheitsbrei-Prüfer 7 → 8 → 8 → 8 → **9** · Investor 5 → 7 → 8 → 8 → **8**.

Fünf von sechs Rollen stehen bei 9. Fachexperte, Finanzmathematiker und Einheitsbrei-Prüfer knüpfen die 9 an Auflagen, die ohne weitere Runde zu beheben sind; sie sind unten übernommen. Der Investor bleibt bei 8: Die Maßstäbe der Freigabepunkte stehen in Bericht, Spezifikation und `TASKS.md` nicht gleichlautend, und der tragbare Preis lässt sich über Finanzierungseingaben unbemerkt anheben. Beides braucht keine neuen Angaben des Auftraggebers und ist unten übernommen. Eine sechste Runde gibt es nach der Abbruchregel nicht; die Schlussredaktion wird am Text gegengelesen und mit den Prüfskripten geprüft.

## Nachgeprüft

- **Freibetrag der Gewerbesteuer:** Fachexperte, Finanzmathematiker und Jurist haben § 11 Abs. 1 GewStG unabhängig am Original gelesen und kommen auf denselben Messbetrag (2.642,50 Euro statt 3.500 Euro bei 100.000 Euro Gewerbeertrag). Der Fehler stammt aus dem Vorschlag des Juristen in Runde 4.
- **Überfinanzierung beim Ankauf mit übernommenem Förderdarlehen:** Praktiker und Fachexperte unabhängig, je mit Gegenrechnung (negatives Eigenkapital). Am Wortlaut von D.4 bestätigt: Die Restfinanzierung ist nur für den Neubau geregelt.
- **Bezug der Beleihungsquote und Untergrenze des Bankdarlehens:** Finanzmathematiker, Praktiker und Fachexperte unabhängig; im Bericht und in `MA-026` nicht festgelegt.
- **`MA-027` ohne Restwert:** Der Finanzmathematiker zeigt am Testfall, dass die Amortisationsdauer dann bei jedem fremdfinanzierten Bestand gleich der Haltedauer ist. Die Voreinstellung war unbrauchbar und wird geändert.
- **II. BV:** Der Finanzmathematiker weist zu Recht darauf hin, dass eine reine Umrechnung der Indexbasis die Abweichung von 1,5 % nicht erklärt. Quellnotiz 10 und Kataster nennen jetzt nur noch den Befund und kennzeichnen die Ursache als ungeklärt.
- **Formel der VOFI-Gesamtkapitalrentabilität:** liegt seit dem 18.11.2026 als Bildschirmfoto des Lexikoneintrags vor (Quellnotiz 10).

## Übernommen (Schlussredaktion)

### A. Finanzierung in der Grobkalkulation (Abschnitt 5, D.1, D.4, D.5, `MA-026`)

1. **Restfinanzierung gilt immer, nicht nur im geförderten Neubau.** Das Bankdarlehen ist höchstens der Mittelbedarf, der nach den übrigen Darlehen (Förderdarlehen, übernommene Darlehen), den Zuschüssen und dem Mindesteigenkapital bleibt, und nie negativ. Das Eigenkapital ist der Ausgleichsposten der Kontrollsumme „Mittelherkunft gleich Mittelverwendung"; Darlehen zählen dort mit dem Auszahlungsbetrag.
2. **Bezug der Deckel:** Die Beleihungsquote begrenzt die Summe aller Darlehen gegen den Wertansatz; die Mindestdeckung rechnet mit dem Kapitaldienst aller Darlehen. Reicht der Reinertrag schon für die übrigen Darlehen nicht, ist das Bankdarlehen null, und das Blatt meldet es. Beides ist die vorsichtige Lesart von `MA-026`; die andere Lesart (nur das eigene Darlehen der Bank) ist umschaltbar.
3. **`MA-026`:** Titel „Rechengrundlage des Bankdarlehens"; Gewicht **hoch**, weil die Lesart im geförderten Neubau und beim Ankauf gebundener Bestände über das Eigenkapital und damit über den tragbaren Preis entscheidet; der Wertansatz „Kaufpreis" ist als begründete Ausnahme von der Vorsichtsregel gekennzeichnet; offen und in der Bemerkung genannt: ob die Bank den Reinertrag mit eigenen Bewirtschaftungspauschalen rechnet (Frage an die Hausbank).
4. **Darlehen im kombinierten Stressfall:** Es wird aus dem Basisfall übernommen, nicht neu bemessen; ausgewiesen wird die Deckung im Stressfall. Im Bericht ein Halbsatz in D.5; die Einzelheiten legt die Fachspezifikation fest.
5. **Gegen Schönrechnen:** Beleihungsquote, Mindestdeckung, Mindesttilgung und Anschlusszins sind Vorgaben des Hauses und im Projekt nur zu verschärfen. Eine Lockerung und ein Wertansatz der Bank über dem Kaufpreis brauchen eine Begründung und stehen sichtbar auf dem Kurzblatt. D.1 führt die Beleihungsquote und die Tilgung deshalb als Voreinstellung aus den Vorgaben des Hauses, nicht als freie Eingabe.
6. **Abschnitt 5** liefert nur die Begründung und verweist für die Regel auf D.4 und D.5, statt sie zu wiederholen.
7. **Gremienvorlage unter Fördervorbehalt** ist in 1b-2 immer verfügbar, nicht nur in der umgekehrten Reihenfolge.

### B. Steuer (B.3, B.5, D.4, Verzeichnis)

8. **Freibetrag nach § 11 Abs. 1 GewStG** (`GEWSTG-11`) in der Zeile „Gewerbesteuer" und im Beispiel zu § 35 EStG: Messbetrag 2.642,50 Euro; Ermäßigung 10.570 Euro bei 400 % Hebesatz, 7.399 Euro bei 280 %; „bis zu 10,57 Prozentpunkte" in diesem Beispiel. Mit Skript nachrechnen.
9. **Kurzform der Steuer in 1a (D.4)** ergänzen: Freibetrag bei Personenunternehmen; Ermäßigung nach `ESTG-35` nur für natürliche Personen, begrenzt auf die Einkommensteuer, die auf den gewerblichen Gewinn entfällt, ohne Vortrag; Gewerbesteuer ist keine Betriebsausgabe (§ 4 Abs. 5b EStG, neuer Katastereintrag); bei der Körperschaft rechnet die Kurzform ohne Hinzurechnung der Schuldzinsen und sagt das; befreite Genossenschaft, befreiter Verein und andere befreite Körperschaften rechnen mit Satz null; das Einzelunternehmen ist ausdrücklich genannt.
10. **Kennzeichen „erweiterte Grundstückskürzung"** auch für die gewerbliche und gewerblich geprägte Personengesellschaft in 1a, damit 1a und 1b denselben Fall gleich rechnen (D.1, D.4).
11. **Gewerbesteuer auf den Verkaufsgewinn je Steuerstatus:** eine Zeile in B.5 als Prüfauftrag an den Steuerberater (§ 7 Satz 2, § 9 Nr. 1 Satz 2 GewStG); die Regel selbst legt die Fachspezifikation fest.
12. **De-minimis-Bindung der Sonderabschreibung:** § 7b Abs. 5 Satz 2 EStG knüpft an die Person an („Anspruchsberechtigte mit Einkünften im Sinne der §§ 13, 15 und 18"). Neue Annahme `MA-029`, Voreinstellung „gebunden", sobald der Investor solche Einkünfte hat – auch die Privatperson mit Praxis oder Gewerbe und die Kapitalgesellschaft als Gesellschafterin einer vermögensverwaltenden Personengesellschaft; Merkmal am Investor; B.3 und D.4 (Zeile Privatperson) entsprechend fassen. Bestätigen muss der Steuerberater.
13. **`MA-023` beim Erwerb:** Die Baukostenobergrenze der Sonderabschreibung rechnet beim Erwerb mit dem Gebäudeanteil des Kaufpreises und den anteiligen Nebenkosten, ohne den Marktwertdeckel der NBank; C.1 und B.3 angleichen. Der Kaufpreis einschließlich Boden bleibt als andere, strengere Lesart stehen.
14. **`MA-021`:** Grundlage ist der NBank-Vordruck 4009 „Einfacher Verwendungsnachweis" (Stand Juli 2026, Nr. 5.4; neuer Katastereintrag `NBANK-VORDR-4009`, vom Juristen am 18.11.2026 gelesen): Die zuwendungsfähigen Ausgaben enthalten keine Umsatzsteuer, soweit sie als Vorsteuer abziehbar ist. Die Voreinstellung ist damit keine Ausnahme von der Vorsichtsregel mehr; Gewicht gering; die NBank bestätigt nur noch.
15. **`MA-019`:** einheitlich „Ausnahme von der Vorsichtsregel" statt „Abweichung".

### C. Kennzahlen (Abschnitt 3, Anhang A, B.6, Verzeichnis)

16. **`MA-027` neu gefasst:** Die Amortisationsdauer endet mit der Periode, von der an das Vermögen aus der Investition bei gedachtem Verkauf zum Wertpfad – nach Verkaufskosten, Ablösung der Restschuld und Steuern – die Anlage des Eigenkapitals zur Unterlassensalternative dauerhaft erreicht oder übertrifft. Das passt zu Anhang A Nr. 18, der den Wertpfad schon verlangt. Andere Lesart: Rückgewinnung des Eigenkapitals ohne Vergleich. `MA-027` steht in Abschnitt 3, A Nr. 18 und B.6.
17. **VOFI-Gesamtkapitalrentabilität:** Die Formel und der Referenzzinsfuß sind gelesen (Quellnotiz 10, `GABLER-BANKLEXIKON-GKR`); die Kennzahl gehört auf das volle Kennzahlenblatt ab 1b. Alle Stellen, die sie als „nicht ausgewiesen, bis gelesen" führen, werden angepasst. Die Abgrenzung der zuzurechnenden Sollzinsen ist `MA-028` (Voreinstellung: einfache Summe der Sollzinsen aller Darlehen, die die Anschaffungsauszahlung finanzieren, ohne Kontokorrent); `MA-028` steht in A Nr. 19 und B.6.
18. **A.1 Nr. 3:** Die Kontrollsumme des Investitionsstaus in Anteilen der Maßnahme fassen, damit sie auch bei teilweise ausgeführter Maßnahme schließt.
19. **A.6:** Alternativzins des Testfalls (2 % vor, 1,4 % nach Steuern) unter den Annahmen nennen.
20. **B.4, II. BV:** „passen rechnerisch" berichtigen: Die Beträge der Sekundärquelle sind aus der heutigen Indexreihe nicht nachrechenbar (Abweichung 1,5 %, Ursache ungeklärt); sie werden als veröffentlichte Werte geführt.

### D. Freigabepunkte (Kopfteil, Abschnitt 1, E.1; gleichlautend mit Spezifikation Kapitel 2 und `TASKS.md`)

21. **Vier Maßstäbe der Vorprüfung, jeder mit Folge:** (1) Ein Produkt deckt den Bedarf – dann Vorstudie nur zu Kauf und Excel-Ausbau. (2) Bedarf allgemein: Mehrheit der Befragten – sonst Abbruch. (3) Bedarf, der nur den Eigenbau trägt: Mehrheit braucht mindestens eines von Änderungsprotokoll, Arbeit mehrerer Personen, Berichten und Zugang für Kunden – sonst Umsteuern auf Kauf oder Excel-Ausbau. (4) Mindestfallzahl: Zeitersparnis über zehn Jahre deckt mindestens die Lizenzkosten des günstigsten vorgeführten Produkts über dieselben zehn Jahre, gerechnet mit Stundensatz und Ersparnisanteil, die der Auftraggeber vorab nennt – sonst Abbruch. Dazu: Übernimmt niemand die Katalogpflege – Abbruch. Der Kopfteil nennt die Freigaben und verweist für die Maßstäbe auf Abschnitt 1, statt sie verkürzt zu wiederholen; Freigabe 4 und die Tabelle in Abschnitt 1 nennen dieselben Voraussetzungen einschließlich der Fachfragen.
22. **Vorstudie:** Zeitraum, ungünstiger Fall, Zuschläge, Schwellen und der Kalkulationszins werden mit dem Auftrag der Vorstudie freigegeben, also vor ihrem Ergebnis und vor der Bauentscheidung.
23. **Teilschritte:** Der Nutzungsgrad wird über die ersten sechs Monate nach Einführung eines Teilschritts gezählt (Vorschlag); „Bank oder Gremium nehmen die Vorlagen nicht an" heißt: Für mehr als eine von drei Vorlagen wird zusätzlich die bisherige Excel-Rechnung verlangt (Vorschlag).

### E. Einzelstellen (Einheitsbrei-Prüfer)

24. Abschnitt 3: Der Begründungssatz zum kombinierten Stressfall hat seinen Bezug verloren (bisher Z. 157) – neu anschließen oder streichen. Abschnitt 5 „Reihenfolge": Mietenstufe und Einkommensgruppe mit aufzählen. Kopfteil: „drei Design-Wettbewerbe" mit Verweis auf den Entwicklungsplan.

## Nicht in den Bericht, sondern in die Fachspezifikation (als Aufgaben in `TASKS.md`)

- Anschlusszins und Tilgung nach Ende der Zinsbindung, auch für übernommene Förderdarlehen; Vorfälligkeitsentschädigung, wenn die Zinsbindung länger ist als die Haltedauer (Praktiker 3, 4; Finanzmathematiker 7).
- Zahl der Eingaben beim Ankauf gebundener Bestände (Praktiker 6).
- Suchbereich und Raster der Zielwertsuche (Finanzmathematiker 8).
- Tragbarer Preis im Stressfall: mit welchem Darlehen (Investor 4, Fachexperte 5 – Grundsatz in Nr. 4 oben).

## Nicht übernommen

- **Einheitsbrei-Prüfer, Anrede „Sie":** Der Bericht bleibt in der Anrede; er wird nach der Abnahme nicht fortgeschrieben, sondern durch Spezifikation und Anwendungsdokumentation abgelöst.

## Ergebnis für den Auftraggeber

Der Bericht ist nach fünf Runden abgenommen: fünf Rollen bei 9, der Investor bei 8. Was dem Investor zur 9 fehlte, ist in der Schlussredaktion behoben, aber nicht mehr von ihm nachgeprüft. Offen bleibt nur, was der Bericht nicht liefern kann: Antworten der NBank, der Hausbank und des Steuerberaters auf die gekennzeichneten Annahmen, die Vorgaben des Hauses und die Anwendergespräche.
