# Sichtung der Prüfrunde 4 – Recherchebericht (2026-11-18)

Noten (Runde 1 → 2 → 3 → 4): Finanzmathematiker 7 → 8 → 9 → **9** · Jurist 6 → 7 → 9 → **9** · Investor 5 → 7 → 8 → **8** · Praktiker 5 → 7 → 8 → **8** · Fachexperte 6 → 8 → 8 → **8** · Einheitsbrei-Prüfer 7 → 8 → 8 → **8**.

Alle Befunde der Runde 3 sind nach Angabe der Prüfer behoben, bis auf Reste beim Investor (Nr. 3, 9) und beim Einheitsbrei-Prüfer (Nr. 8). Die vier Prüfer mit Note 8 halten die 9 mit einer kurzen, gezielten Überarbeitung für erreichbar und nennen die Stellen. Nach der Abbruchregel in `/pruefrunde` folgt deshalb eine vierte Überarbeitung und als fünfte und letzte Runde eine gezielte Nachprüfung der geänderten Stellen.

## Nachgeprüft

- **Bankgrenze als Preisgrenze (Finanzmathematiker 1, Fachexperte 3, Praktiker 4):** Drei Prüfer kommen unabhängig zum selben Schluss. Am Berichtstext (Abschnitt 5, D.4, D.5) und an der Spezifikation Kapitel 2 bestätigt: Die Regel „niedrigerer Wert aus Rendite- und Bankgrenze" behandelt eine Grenze des Darlehens als Grenze des Preises. Über der Bankgrenze sinkt das Darlehen, der Preis bleibt mit mehr Eigenkapital erreichbar. Die Regel lag auf der sicheren Seite, nannte aber ein zu niedriges Gebot (Gegenrechnung des Finanzmathematikers: 2,30 statt 2,52 Mio. Euro). Die Festlegung in der Spezifikation war als **fest** markiert und wird geändert (Entscheidungsprotokoll).
- **Überfinanzierung im geförderten Neubau (Fachexperte 1, Praktiker 1):** Am Wortlaut von D.4 bestätigt („bezogen … beim Neubau auf die Gesamtkosten; dazu das NBank-Darlehen"). 65 % von 10 Mio. Euro zuzüglich 7,2 Mio. Euro Förderung ergeben 13,7 Mio. Euro Mittel.
- **Zinsbindung und Anschlusszins in 1a (Fachexperte 2, Praktiker 2):** Am Berichtstext bestätigt: D.1 nennt keine Zinsbindung, D.5 führt den kritischen Anschlusszins erst ab 1b; der heutige Zins gilt in 1a still bis zum Verkauf.
- **`MA-023` gegen Abschnitt 6 (Einheitsbrei-Prüfer 2):** Am Verzeichnis bestätigt. Die Voreinstellung lautet „dieselbe Kostensumme", der Berichtstext sagt „andere Kosten".
- **Kopfteil gegen `TASKS.md` (Einheitsbrei-Prüfer 4, Investor 2):** An beiden Dateien bestätigt.
- **Rechtsbefunde** stützen sich auf die im Prüfbericht des Juristen und des Fachexperten gelisteten, am 18.11.2026 am Original gelesenen Normen; rechnerische Befunde auf die Gegenrechnungen des Finanzmathematikers (Skripte `m3.py`, `a.py`, `b.py`, `c.py`, gesichert unter `research_notes/…/skripte/runde4/`).

Bereits nachgezogen (durch die Projektleitung, nicht Teil des Überarbeitungsauftrags): Spezifikation Kapitel 2 (Grobkalkulation, Entscheidungspunkte) und Kapitel 9, Entscheidungsprotokoll, `TASKS.md`.

## Übernommen (vierte Überarbeitung des Berichts)

### A. Tragbarer Preis und Finanzierung in 1a (Abschnitt 5, D.1, D.4, D.5)

1. **Neue Regel für den höchsten tragbaren Preis** (ersetzt „niedrigerer Wert aus zwei Grenzen"):
   - Das Bankdarlehen ist der kleinere Wert aus (a) Beleihungsquote mal Wertansatz und (b) dem Darlehen, dessen Schuldendienst die Mindestdeckung im ersten Jahr der Vollvermietung gerade einhält.
   - Der Wertansatz ist in 1a als Voreinstellung der Kaufpreis, beim Neubau die Gesamtkosten; er ist als „Wertansatz der Bank" überschreibbar. Die Rechengrundlage der Bankgrenze ist eine Modellannahme (`MA-026`, neu).
   - Der höchste tragbare Preis ist der Preis, bei dem die VOFI-Rendite nach Steuern **mit diesem gedeckelten Darlehen** die Zielrendite erreicht. Das dafür nötige Eigenkapital wird ausgewiesen.
   - Das verfügbare Eigenkapital ist eine freiwillige Eingabe und wirkt als zweite Grenze. Das Blatt nennt, was bindet: Rendite oder Eigenkapital; es zeigt außerdem, ob Beleihungsquote oder Mindestdeckung das Darlehen begrenzt.
   - Als Nebenangabe bleibt der Preis, bis zu dem die Finanzierung allein nach Beleihungsquote die Mindestdeckung einhält (die bisherige „Bankgrenze"). Das nachgerechnete Beispiel in D.4 bleibt dafür stehen und wird um den Preis nach der neuen Regel ergänzt, sofern der Überarbeiter ihn mit einem Skript nachrechnet; sonst entfällt die Ergänzung.
2. **Geförderter Neubau:** Das Bankdarlehen ist Restfinanzierung: Gesamtkosten abzüglich Förderdarlehen, Zuschuss und Eigenkapital (mindestens die Eigenmittelquote nach Katalog, `MA-004`), gedeckelt wie in Nr. 1. Kontrollsumme „Mittelherkunft gleich Mittelverwendung". Die Mindestdeckung rechnet mit dem Kapitaldienst aller Darlehen einschließlich des Förderdarlehens (vorsichtige Lesart, `MA-026`).
3. **Zinsbindung und Anschlusszins in 1a:** Zinsbindung als Eingabe mit Voreinstellung aus dem Katalog; Anschlusszins als Vorgabe des Hauses (Aufschlag auf den heutigen Zins); der kombinierte Stressfall erhöht ihn. Keine stille Fortschreibung des heutigen Zinses.
4. **Steuer in Kurzform:** Körperschaft mit Satz je Jahr aus der Katalogstaffel (sinkende Körperschaftsteuer bis 2032) und Kennzeichen „erweiterte Grundstückskürzung" (dann ohne Gewerbesteuer); bei Privatperson und Personengesellschaft der Steuersatz als Eingabe mit Voreinstellung; bei gewerblicher oder gewerblich geprägter Personengesellschaft und Einzelunternehmen die Anrechnung der Gewerbesteuer nach `ESTG-35` (Kurzform pauschal, Grundform nach Gesetz). In B.5 entfällt der Vermerk „nicht am Gesetz gelesen" zu § 35 EStG.
5. **Eingabeliste 1a (D.1) ergänzen:** beim Neubau Grundstücksfläche, Wohnfläche, Zahl der Einheiten; bei Förderung Mietenstufe und Einkommensgruppe; beide: Zinsbindung, freiwillig verfügbares Eigenkapital und Wertansatz der Bank. Das Arbeitsziel „rund 20 Eingaben" wird ehrlich nachgezählt und, wenn nötig, je Vorhabensart genannt.
6. **Übernommenes Förderdarlehen** beim Ankauf gebundener Bestände in 1a über die zweite Tranche.
7. **Druckbares Kurzblatt** in 1a für das indikative Gebot: das verkürzte Kennzahlenblatt mit Standkennung.
8. **Zielwertsuche:** nur auf Eingaben, bei denen das Ergebnis eindeutig ist oder alle Lösungen gemeldet werden. Zulässige Eingaben kennzeichnen; sonst meldet das Werkzeug alle Lösungen oder „keine Lösung". Nicht zulässig: Steuerstatus; Haltedauer nur als Tabelle je Jahr.
9. **Kreditauflagen** (Zeile in „Offen vor der Umsetzung" beziehungsweise deren Nachfolger): Vorgaben des Hauses, nicht `MA-014` und nicht „Anwender".

### B. Zuschnitt und Freigabepunkte (Abschnitt 1, 2, 5, E.1)

10. **Bedarfsschwelle zweiteilen:** (a) Allgemeiner Bedarf: Die Mehrheit der Befragten würde die Grobkalkulation statt Excel nutzen; fehlt er, wird abgebrochen. (b) Bedarf, der nur den Eigenbau trägt: Die Mehrheit braucht mindestens eines von Änderungsprotokoll, Arbeit mehrerer Personen an einem Projekt oder Berichten und Zugang für Kunden; fehlt er, wird auf den Vergleich von Kauf und Excel-Ausbau umgesteuert. „Mehrheit" statt „drei von fünf", damit die Schwelle auch bei drei oder vier Gesprächen bestimmt ist.
11. **Kauf-Kriterium der Vorprüfung:** Deckt ein Produkt den Bedarf, wird nicht unmittelbar gekauft, sondern auf eine Vorstudie umgesteuert, die nur Kauf und Excel-Ausbau vergleicht.
12. **Mindestfallzahl mit Bezugsgröße als Vorschlag:** Die Zeitersparnis über zehn Jahre muss mindestens den Lizenzpreis des günstigsten vorgeführten Produkts decken.
13. **Zuschläge im ungünstigen Fall (E.1):** Vorschlagswert +30 % für Einführung beim Kauf und für den Excel-Ausbau, als Teil der Freigabe.
14. **Freigabepunkt vor 1b:** Verweis auf die bezifferte Nutzungsschwelle aus E.1. Der in E.1 angekündigte Zinsvorschlag, den es nicht gibt, wird gestrichen oder durch den Verweis auf den Kalkulationszins des Hauses ersetzt.
15. **Kosten und Bindung der Prüfung selbst:** Steuerberater erst vor dem ersten Kundeneinsatz; Anwaltskosten und Design-Wettbewerbe vor der Bauentscheidung als Kosten der Prüfung benennen; Zahl der Termine nennen, die die Vorprüfung beim Auftraggeber bindet. Die Lage der Rechtsprüfung stimmt mit dem Entwicklungsplan überein (dort: vor der Spezifikation des Änderungsprotokolls).
16. **Geförderter Neubau als Hauptgeschäft:** In der umgekehrten Reihenfolge lässt 1b-2 eine Gremienvorlage mit Grobförderung unter Fördervorbehalt zu. Die Zahl der Freigaben in dieser Reihenfolge wird eindeutig genannt, und die Zeile des Freigabepunkts passt zu beiden Reihenfolgen.
17. **Zielrendite und Monatsverschiebung:** Hinweis in Abschnitt 3 oder 5, dass die Fachspezifikation prüft, den Abstand zur Zielrendite als Endwertüberschuss auszuweisen (`MA-012`).
18. Formulierung in Abschnitt 1 zur Vorstudie berichtigen: Der Abstand der Wege bleibt nur erhalten, wenn alle um denselben Betrag teurer werden.

### C. Rechenkern (Anhang A)

19. **Restwert:** eigene Restwertprobe, die eine doppelt gezählte Restschuld erkennt; Preisstand des Abzugs für Investitionsstau ist der Verkaufsstichtag; die anteilige Rückzahlung des NBank-Zuschusses nach `MA-017` ist immer eine Zahlung im Finanzplan, mit Kontrollsumme für den Zuschuss.
20. **Testfall vollständig an einem Ort (A.6):** alle Eingaben in der Zelle „Annahmen" (Kaufpreis 1.000.000 Euro und Erwerbsnebenkosten 100.000 Euro; Eigenkapital 400.000 Euro; Annuitätendarlehen 700.000 Euro zu 4 % mit 2 % Anfangstilgung; Reinertrag 55.000 Euro im ersten Jahr, plus 2 % je Jahr; Abschreibung 2 % auf 80 % Gebäudeanteil; Steuersatz 30 %, Verluste sofort verrechnet; Habenzins 2 %, Kontokorrentzins 8 %; Verkauf Ende Jahr 5 zu 1.150.000 Euro, Gewinn steuerfrei) – vor dem Eintragen gegen Quellnotiz 03, Testfall S1, und das Skript abgleichen; Verweis auf beide. Abschnitt 3 und der Vorspann von Anhang A verweisen nur noch auf A.6.
21. Offene Frage für die Fachspezifikation aufnehmen: Gehört das Zuschussentgelt in die Kreditprobe (A, Nr. 22)?

### D. Recht und Annahmen (Anhang B, C, Verzeichnisse)

22. **Kennung am Wirkort:** `MA-021` bis `MA-025` stehen in den Zeilen, für die sie gelten (B.1 Glasfaser und Wärmepumpe, B.3, C.1). Die Zeile „Modernisierungsumlage" in B.1 darf die Glasfaserumlage nicht als geklärt führen; `MA-025` stellt „keine Umlage" vor.
23. **Abschnitt 6 an `MA-023` angleichen:** Ob die Obergrenze der Sonderabschreibung andere Kosten misst als die Bemessungsgrenze der NBank, ist offen; voreingestellt ist dieselbe Kostensumme.
24. **Verlustvortrag ab 2028 (`MA-010`) an einem Ort:** in B.6, Zuständigkeit gleichlautend mit dem Verzeichnis („Projekt am Bundesgesetzblatt, Bestätigung durch den Steuerberater"); die anderen Stellen verweisen.
25. **De-minimis-Bindung der Sonderabschreibung einmal definieren (B.3), sonst verweisen:** gebunden sind Körperschaften nach § 1 Abs. 1 Nr. 1 bis 3 KStG einschließlich der steuerpflichtig gewordenen Genossenschaft (`KSTG-8`), gewerbliche und gewerblich geprägte Personengesellschaften und Einzelunternehmen mit Betriebsvermögen; nicht gebunden sind Privatperson, vermögensverwaltende Personengesellschaft sowie Verein und Stiftung mit Vermietungseinkünften.
26. **Verzeichnis der Modellannahmen** (`docs/modellannahmen/annahmen.toml`, danach `python3 scripts/modellannahmen.py`):
    - `MA-019`: andere Lesart „Abzug mit dem Nennbetrag" ergänzen; die Voreinstellung als begründete Abweichung kennzeichnen statt als „ungünstigere Lesart".
    - `MA-021`: „bis zu einem Sechstel" statt „rund ein Sechstel", mit dem Hinweis auf die Kappung an der Bemessungsgrenze und die umsatzsteuerfreien Grundstückskosten; Klärungsweg über die ANBest-P zu § 44 LHO, die die Richtlinie in Nr. 12.3.1 für anwendbar erklärt.
    - `MA-022`: schädlich bleiben Selbstnutzung, unentgeltliche Überlassung, vorübergehende Beherbergung und Aufgabe der Vermietungsabsicht; „Nutzungszeitraum nach § 7b" statt „Bindungszeitraum".
    - `MA-025`: Grund der Offenheit ist die Spannung im Wortlaut (§ 559 Abs. 1 Satz 1 nennt Nr. 4a nicht, Satz 2 setzt ihre Umlage voraus).
    - `MA-023`: Bemessungsgrundlage beim Ersterwerb ergänzen (Kaufpreis nebst Erwerbskosten, höchstens Marktwert; RL Nr. 5.3.2.1 und 5.3.2.4); für § 7b ist beim Kauf keine Kostensumme bestimmt.
    - `MA-026` neu, Gewicht mittel, umschaltbar: Rechengrundlage der Bankgrenze (Mindestdeckung aus dem Reinertrag im ersten Jahr der Vollvermietung gegen den Kapitaldienst aller Darlehen einschließlich Förderdarlehen; Beleihung auf Kaufpreis oder Gesamtkosten statt auf einen Beleihungswert). Andere Lesart: Die Bank rechnet nur ihr eigenes Darlehen oder setzt einen eigenen Wert an. Klären kann die Hausbank; die Schwellen selbst sind Vorgaben des Hauses.
27. **Quellenkataster** (`docs/quellenkataster/quellen.toml`, danach `python3 scripts/quellenkataster.py`): `ESTG-35` und die Abschlagszahlungsverordnung neu; `AO-233A` mit Stand; Lesedatum 18.11.2026 für die von Jurist und Fachexperte am Original gelesenen Normen (Listen in deren Berichten), nur soweit dort ausdrücklich als gelesen genannt.
28. **C.1:** Bemessungsgrundlage beim Ersterwerb ergänzen (wie Nr. 26, `MA-023`). **Randfälle:** Altfälle des § 7b bei abweichendem Wirtschaftsjahr nach § 52 Abs. 15a EStG.

### E. Ordnung des Berichts (Einheitsbrei-Prüfer)

29. **Eine Aufgabenliste:** Der Kopfteil heißt „Freigabepunkte und Abhängigkeiten" und behält die Freigaben, weil sie den Bau gliedern. Die Aufträge an den Auftraggeber und die Tabelle „Offen vor der Umsetzung" ersetzt ein Satz: Offene Aufträge führt `TASKS.md`; der Bericht nennt nur, an welchem Freigabepunkt ihr Ergebnis gebraucht wird. Der Satz „steht vollständig im Kopfteil" entfällt. Die Punkte, die bisher nur im Bericht standen, sind bereits nach `TASKS.md` übertragen.
30. **Dopplungen mit parallelem Wortlaut auflösen:** Restwert und Investitionsstau (Regel in A.1 Nr. 3, D.1 und D.4 verweisen); kombinierter Stressfall (Regel in D.5, Abschnitt 3 verweist); E.2 verweist auf D.5, A.7 und die Spezifikation, statt eine dritte Fassung zu führen. Die fünf nicht untersuchten Anbieter stehen an einer Stelle.
31. **Einzelstellen:** den verunglückten Satz in Abschnitt 3 (bisher Z. 149, „die ersten drei") berichtigen; die Vorbemerkung zu Anhang B entlasten.

## Nicht übernommen

- **Finanzmathematiker, Runde 3, schärfere Toleranz für aus Grafiken abgelesene Werte:** bleibt bei der beobachteten Höchstabweichung; der Prüfer selbst hält das für vertretbar.
- **Fachexperte, Themen für die Fachspezifikation** (Gewerbesteuer der Personengesellschaft beim Verkauf nach § 7 Satz 2 GewStG, Veräußerungsgewinn bei erweiterter Kürzung, Bewertung bei laufender Bindung über `MA-017` hinaus): nicht Sache des Rechercheberichts; als Aufgabe für Spezifikation Kapitel 3 in `TASKS.md` aufgenommen.
- **Jurist, niedersächsisches Haushaltsrecht (VV zu § 44 LHO, ANBest-P) und Übergangsrecht zu § 559f BGB:** von hier nicht erreichbar; als Leseauftrag in `TASKS.md`.

## Auftrag für Runde 5

Gezielte Nachprüfung der geänderten Stellen durch Investor, Praktiker, Fachexperte und Einheitsbrei-Prüfer; der Finanzmathematiker rechnet die neue Preisregel und die Restwertprobe nach; der Jurist prüft die Zeilen zu § 35 EStG und die geänderten Annahmen. Runde 5 ist die letzte. Bleibt eine Rolle unter 9, wird dem Auftraggeber benannt, was fehlt und wer es liefern kann.
