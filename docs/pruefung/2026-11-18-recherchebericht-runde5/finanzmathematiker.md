```
Rolle: Prüfer Finanzmathematiker (Runde 5, letzte Änderungsprüfung)
Prüfobjekt: reports/VOFI Immobiliensoftware Marktrecherche.md, Änderungen seit Runde 4
            (bericht-aenderungen-seit-runde4.diff), soweit sie rechnen: Abschnitt 5 „Was die
            Grobkalkulation rechnet“; Anhang A Nr. 3, A.6; B.3 (§ 35 EStG); B.6 MA-021; D.1, D.4, D.5;
            dazu Spezifikation Kapitel 2 (Zeile „Grobkalkulation“, „Offene Lehrbuchdefinitionen“),
            MA-026, MA-027 und Quellnotiz 10 mit bewirtschaftungskosten_index.py
Gesamturteil: Trägt, mit zwei Auflagen. Befund 1 aus Runde 4 ist richtig umgestellt: Die Bank
  begrenzt jetzt das Darlehen, nicht den Preis. Die Preisgleichung hat genau eine Lösung, auch am
  Knick zwischen beiden Deckeln, und alle Zahlen des Beispiels stimmen. Der Testfall lässt sich
  unabhängig auf den Cent nachbauen. Falsch ist das neue Beispiel zu § 35 EStG: Es übergeht den
  Freibetrag von 24.500 Euro (Befund 1). Offen ist außerdem, worauf sich die Beleihungsquote im
  geförderten Neubau bezieht (Befund 2).
Note: 9 von 10 – die 9 hält. Zur stabilen 9 fehlen im Bericht zwei Korrekturen von je ein bis zwei
  Sätzen: das Beispiel in B.3 mit dem Freibetrag (Befund 1) und der Bezug der Beleihungsquote in
  D.4 und MA-026 (Befund 2). Die Befunde 3 bis 8 sind Hinweise; die Befunde 3, 4 und 6 sollten
  noch im Bericht nachgezogen werden, der Rest gehört in die Fachspezifikation.
```

Gegenrechnungen: eigene Skripte unter `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/runde5-finmath/`.

| Skript | Inhalt |
|---|---|
| `testfall.py` | Testfall A.6, unabhängig nachgebaut, mit exakter Bruchrechnung, wahlweise mit Cent-Rundung; dazu die Varianten Entnahmen, Kontokorrent und Nachschuss sowie die Restwertprobe |
| `preisgrenze.py` | Vereinfachtes Jahresmodell der Grobkalkulation mit Darlehen = min(Quote · P; Deckungsdarlehen). Geprüft werden Monotonie, Knick und Lösung der Preisgleichung, in sechs Parametersätzen mit und ohne Verkaufsteuer und Anschlusszins |
| `anschluss.py` | Wirkung der Lesart der Rate nach Ende der Zinsbindung |
| `amort.py` | Vermögenspfad des Testfalls für die Amortisationsdauer nach `MA-027` |
| `immowertv.py` | Anlage 3 ImmoWertV 2021 bis 2027, Rundungsprobe und II. BV |

Am Original gelesen am 18.11.2026 (für das Kataster):
- **`IMMOWERTV-ANLAGE-3`:** Anlage 3, Abschnitte I und III, gesetze-im-internet.de, Fundstelle BGBl. I 2021, 2822–2823. Der Text stimmt mit Quellnotiz 10 überein: Basiswerte 230 / 275 / 30 Euro und 9,00 / 68 Euro, Oktober 2001 gegen Oktober des Vorjahres, Instandhaltung je Quadratmeter auf eine Nachkommastelle, sonst kaufmännisch auf volle Euro.
- **`GEWSTG-11`:** § 11 Abs. 1 Satz 3 Nr. 1 GewStG, Freibetrag 24.500 Euro bei natürlichen Personen und Personengesellschaften.
- **`IIBV-26`:** § 26 Abs. 4 II. BV, Fortschreibung alle drei Jahre um den Prozentsatz der Veränderung des Verbraucherpreisindex von Oktober zu Oktober.

## Unabhängig bestätigt

**1. Regel für den höchsten tragbaren Preis**

Abschnitt 5, D.4, D.5, Spezifikation Kapitel 2 und `MA-026` sagen dasselbe. Die Regel ist eindeutig:

- Darlehen L(P) = min(β · W(P); L_D). Dabei ist β die Beleihungsquote, W(P) der Wertansatz und L_D = Reinertrag₁ / (Mindestdeckung · (Zins + Tilgung)) das Deckungsdarlehen.
- Preis P*: Die VOFI-Rendite nach Steuern mit L(P) erreicht die Zielrendite.
- Zweite Grenze P_EK: Der Eigenkapitalbedarf P · (1 + ENK) − L(P) erreicht das verfügbare Eigenkapital. Der Bedarf steigt streng in P (Steigung 1 + ENK − β, oberhalb des Knicks 1 + ENK).
- Ergebnis: min(P*; P_EK). P_EK ist deshalb ebenfalls eindeutig.

Genau eine Lösung:
- L(P) ist stetig und schwach steigend. Unterhalb des Knicks wachsen Eigenkapital und Zinslast mit dem Preis, oberhalb wächst das Eigenkapital eins zu eins. In beiden Ästen fällt die Rendite deshalb streng.
- Am Knick ist sie stetig. Die einseitigen Ableitungen sind beide negativ: −0,090 und −0,116 Prozentpunkte je 10.000 Euro im Grundmodell. In den übrigen fünf Parametersätzen (Verkaufsgewinn steuerpflichtig, Haltedauer 15 Jahre mit Anschlusszins 7 %, Steuer null, Faktor 12 ohne Mietsteigerung) ist das ebenfalls so.
- Gerechnet wurde von 0,5 bis 5 Mio. Euro in Schritten von 2.000 Euro. Die Rendite fällt überall streng.
- Analytisch hält die Monotonie oberhalb des Knicks, solange das Verhältnis von Endwert zu Eigenkapital über dem Steuervorteil je Euro Mehrpreis liegt. Das sind höchstens etwa 0,3 bis 0,45. Erst bei einer Rendite unter etwa −8 % über zehn Jahre könnte das kippen. Für jede sinnvolle Zielrendite gibt es also genau eine Lösung.
- Ergebnisse im Modell: Zielrendite 5 % ergibt 2,52 Mio. Euro (die Mindestdeckung bindet), Zielrendite 8 % ergibt 2,22 Mio. Euro (die Quote bindet). Das deckt sich mit `b.py` aus Runde 4.
- Für den Bau empfiehlt sich trotzdem eine Klammersuche mit Vorzeichenwechsel. Liegt die Rendite schon beim kleinsten Preis unter dem Ziel, meldet das Werkzeug „keine Lösung“, entsprechend D.1.

Beispiel D.4, alle Zahlen bestätigt:

| Größe | Rechnung | Ergebnis |
|---|---|---|
| Reinertrag | 134.640 · 0,8 | 107.712 € |
| Tragbarer Schuldendienst | 107.712 / 1,2 | 89.760 € |
| Darlehen | 89.760 / 0,06 | 1.496.000 € |
| Knick | 1.496.000 / 0,65 | 2.301.538 €, also „rund 2,30 Mio.“ |
| Darlehen nach Quote bei 2,6 Mio. € | 0,65 · 2,6 Mio. | 1,69 Mio. €, Deckung 107.712 / 101.400 = 1,0622, also „1,06“ |
| Gedeckelter Anteil am Kaufpreis | 1,496 / 2,6 | 57,54 %, also „57,5 %“ |
| Mehr Eigenkapital | 1,69 Mio. − 1,496 Mio. | 194.000 € |

**2. Geförderter Neubau**

- In Einkommensgruppe B gelten 60 % Darlehen und 20 % Zuschuss (C.1).
- Auf 9 Mio. Euro zuwendungsfähige Kosten sind das 5,4 Mio. Euro Darlehen und 1,8 Mio. Euro Zuschuss.
- Die Eigenmittel betragen 20 % der zuwendungsfähigen Kosten (RL 5.2.6, Quellnotiz 07), also 1,8 Mio. Euro.
- Probe: 5,4 + 1,8 + 1,8 + 1,0 = 10,0 Mio. Euro. Mittelherkunft gleich Mittelverwendung stimmt.
- Darlehen und Zuschuss zusammen ergeben 7,2 Mio. Euro, das sind 80 % der zuwendungsfähigen Kosten. Das stimmt mit Abschnitt 6 überein.

**3. Zinsbindung und Zielwertsuche**

- Die Zinsbindung ist Eingabe, der Anschlusszins eine Vorgabe des Hauses, der Stressfall erhöht ihn. Der heutige Zins wird nicht still fortgeschrieben.
- Die Zielwertsuche ist auf gekennzeichnete Eingaben beschränkt und meldet alle Lösungen oder „keine Lösung“. Das Beispiel der Beleihungsquote mit zwei Lösungen ist genannt, ebenso der Steuerstatus und die Haltedauer.
- Restpunkte stehen in den Befunden 7 und 8.

**4. Steuer in Kurzform, Körperschaft**

| Fall | Rechnung | Ergebnis | Bericht |
|---|---|---|---|
| Ohne erweiterte Kürzung | 15 % · 1,055 + 3,5 % · 400 % = 15,825 % + 14 % | 29,825 % | „rund 29,8 %“ |
| Mit erweiterter Kürzung | 15 % · 1,055 | 15,825 % | „rund 15,8 %“ |

Zu § 35 EStG siehe Befund 1.

**5. Restwert, A.1 Nr. 3**

- Investitionsstau:
  - 100.000 · 1,03¹⁰ = 134.391,64 €, also 134.392 €.
  - 100.000 · 1,03¹² = 142.576,09 €, also 142.576 €.
- Restschuld des Testfalls nach fünf Jahren: 624.171,48 € (624.171,484 € exakt).
- Endwert bei doppelt abgezogener Restschuld: 584.366,28 − 624.171,48 = −39.805,20 €. Der Gewinn ist steuerfrei und der Verkauf fällt ans Periodenende, deshalb ist die Minderung genau die Restschuld.
- Die Restwertprobe erkennt die Doppelzählung. Die Rückzahlung von Fördermitteln steht jetzt als Zahlung im Finanzplan, ihre Kontrollsumme ist ergänzt. Restpunkt siehe Befund 5.

**6. Testfall A.6**

Unabhängig nachgebaut mit den Rechenregeln aus A.1 Nr. 1 (Zinsen auf den Bestand der Vorperiode, Steuer in der Periode). Der Alternativzins musste dabei aus Nr. 12 erschlossen werden (Befund 6).

| Größe | Eigene Rechnung | Bericht |
|---|---|---|
| Endwert | 584.366,2816 € | 584.366,28 € |
| Endwert mit Cent-Rundung von Zinsen und Steuer | 584.366,2788 € | 584.366,28 € |
| Alternative | 400.000 · 1,014⁵ = 428.795,05 € | – |
| Endwertdifferenz | 155.571,2285 € | 155.571,23 € |
| Rendite | 7,8760 % | 7,876 % |
| Variante Entnahmen | 558.656,41 € | 558.656,41 € |
| Variante Kontokorrent | 561.526,16 € und 8,123 % | 561.526,16 € und 8,123 % |
| Variante Nachschuss | 636.495,82 € und 7,246 %, Endwertdifferenz unverändert | wie berechnet |
| Variante Nachschuss, Entnahme ein Jahr später | 585.086,02 € und 7,246 % | wie berechnet |

- Abschreibung: 2 % · 80 % · 1,1 Mio. € = 17.600 €. Das ist richtig umgestellt.
- Vergleichszins im Monatsraster: (1 + 0,014 / 12)¹² − 1 = 1,409 %. Das bestätigt Nr. 12.

**7. ImmoWertV, Modellansätze**

Die Rechnung folgt dem Verordnungstext: Basiswert mal VPI(Oktober des Vorjahres) / VPI(Oktober 2001), dann gerundet. Die Werte für 2026 (367 / 439 / 48 / 14,40 / 108 Euro) und 2027 (377 / 451 / 49 / 14,80 / 112 Euro) stimmen.

Die Rundung ist robust:
- Keiner der Werte liegt näher als 0,02 an einer Rundungsgrenze. Die engsten Fälle sind 2026 die 108,48 Euro und 2027 die 14,77 Euro je Quadratmeter.
- Wird der Prozentsatz der Indexveränderung vorher auf eine Nachkommastelle gerundet (59,5 % und 64,1 %), ändert sich kein Wert.

Die Probe für 2021 trifft vier von fünf Werten. Bei der Eigentumswohnung ergeben sich 356,32 statt 357 Euro, wie in der Notiz angegeben. Der Faktor 123,0 / 77,1 = 1,5953 stimmt, ebenso 230 · 1,5953 = 366,93 Euro und der Faktor 372,46 / 230 = 1,6194. Zur Erklärung der Abweichung siehe Befund 4.

**8. Hinweise 2 bis 5 aus Runde 4**

| Nr. | Befund Runde 4 | Stand |
|---|---|---|
| 1 | Bankgrenze begrenzt das Darlehen, nicht den Preis | behoben |
| 2 | Zielwertsuche nicht für jede Eingabe eindeutig | weitgehend behoben (D.1). Suchbereich und Raster fehlen (Befund 8) |
| 3 | Kontrollsumme: Restschuld, Fördermittel, Preisstand | behoben (A.1 Nr. 3). Die Kontrollsumme zum Investitionsstau ist bei teilweise ausgeführter Maßnahme noch nicht eindeutig (Befund 5) |
| 4 | `MA-021`, „rund ein Sechstel“ | behoben: „bis zu einem Sechstel, weniger, wenn die Bemessungsgrenze kappt“. 19/119 = 16,0 % bleibt unter einem Sechstel, die Obergrenze stimmt |
| 5 | Begründung „gleich verteuert“ | behoben („um denselben Betrag“) |

## Befunde

**1. [wichtig · belegt] B.3, Zeile „Anrechnung der Gewerbesteuer“, und D.4 „Ertragsteuern“: Das Beispiel übergeht den Freibetrag von 24.500 Euro. Die Kurzform nennt ihn nicht.**

Problem:
- § 35 EStG gilt nur für Einzelunternehmer und Mitunternehmer.
- Genau für sie kürzt § 11 Abs. 1 Satz 3 Nr. 1 GewStG den Gewerbeertrag um 24.500 Euro (am Original gelesen am 18.11.2026).
- Der Satz „Bei 100.000 € Gewerbeertrag beträgt der Messbetrag 3.500 €“ gilt nur für Körperschaften, auf die § 35 nicht anwendbar ist.

Gegenrechnung:

| Größe | Bericht | Richtig |
|---|---|---|
| Messbetrag | 3.500 € | 3,5 % · 75.500 = 2.642,50 € |
| Gewerbesteuer und Ermäßigung bei 400 % | 14.000 € | 10.570 € |
| Ermäßigung bei 280 % | 9.800 € | 7.399 € |
| Entlastung | „bis zu 14 Prozentpunkte des Gewerbeertrags“ | 10,57 Prozentpunkte |

Die 14 Prozentpunkte sind nur der Grenzwert für sehr große Gewerbeerträge.

Folge: Wer die Kurzform nach D.4 baut, rechnet die Gewerbesteuer der Personengesellschaft ohne Freibetrag. Bei 100.000 Euro Gewerbeertrag und einem Hebesatz von 400 % sind das 3.430 Euro Gewerbesteuer zu viel je Jahr. Weil die Anrechnung im Beispiel die Gewerbesteuer genau ausgleicht, ist es auf Einkommensteuerseite derselbe Betrag zu viel Anrechnung. Netto heben sich beide Fehler nur bei einem Hebesatz von genau 400 % auf. Bei 280 % oder 480 % und bei Begrenzung durch den Ermäßigungshöchstbetrag tun sie das nicht.

Verstoßene Maßstäbe:
- FAST: keine versteckten Konstanten.
- Projektregel: Rechtsangabe nach Kataster. `GEWSTG-11` verzeichnet den Freibetrag, der Bericht nicht.

Nebenpunkt: Die Kurzform der Körperschaft übergeht ohne Hinweis die Hinzurechnung von einem Viertel der Schuldzinsen über 200.000 Euro (B.3, Zeile „Gewerbesteuer“). Bis etwa 200.000 Euro Zinsen im Jahr ist das wirkungslos. Bei 400.000 Euro Zinsen sind es 50.000 Euro Hinzurechnung und 7.000 Euro Gewerbesteuer im Jahr.

Vorschlag, im Bericht:
- B.3: „Bei 100.000 € Gewerbeertrag beträgt der Messbetrag nach dem Freibetrag von 24.500 € 2.642,50 €; die Ermäßigung erreicht bei 400 % die Gewerbesteuer von 10.570 € und ist bei 280 % auf 7.399 € begrenzt.“ Den letzten Satz streichen oder „bis zu 14 Prozentpunkte des Gewerbeertrags oberhalb des Freibetrags“ schreiben.
- D.4, Kurzform: „Gewerbesteuer mit Freibetrag (`GEWSTG-11`)“ ergänzen.
- Für die Körperschaft „ohne Hinzurechnung“ als benannte Vereinfachung der Kurzform aufnehmen, oder die Hinzurechnung mitrechnen. Sie ist eine Zeile.

**2. [wichtig · belegt] D.4 „Darlehen“ und `MA-026`: Im geförderten Neubau ist offen, ob die Beleihungsquote nur das Bankdarlehen oder alle Darlehen gegen die Gesamtkosten begrenzt. Für den Fall, dass die Mindestdeckung schon am Förderdarlehen scheitert, fehlt die Regel.**

(a) Bezug der Quote:
- `MA-026` regelt für die Deckung „Kapitaldienst aller Darlehen“. Für die Quote steht dort nur „beleiht … die Gesamtkosten“.
- D.4 misst den Beleihungsauslauf beim Neubau als „Fremdkapital zu Gesamtkosten“, also über alle Darlehen. Deckel (a) heißt aber „Beleihungsquote mal Wertansatz“, also nur das Bankdarlehen.
- Im Beispiel (10 Mio. Euro, 5,4 Mio. Euro Förderdarlehen) bei einer Quote von 60 %:

| Lesart | Höchstbetrag der Bank | Folge |
|---|---|---|
| Nur Bankdarlehen | 6,0 Mio. € | Die Restfinanzierung von 1,0 Mio. € ist frei |
| Alle Darlehen | 6,0 − 5,4 = 0,6 Mio. € | 400.000 € mehr Eigenkapital |

- Bei 65 % bindet keine der beiden Lesarten (6,5 − 5,4 = 1,1 > 1,0). Das Beispiel verdeckt die Frage also nur.
- Das war in Runde 4, Befund 1, letzter Spiegelstrich, ausdrücklich gefragt und ist nur für die Deckung beantwortet.

(b) Untergrenze:
- Das Deckungsdarlehen ist L_D = (Reinertrag / Mindestdeckung − Kapitaldienst Förderdarlehen) / (Zins + Tilgung). Es kann null oder negativ werden.
- Beispiel mit gleichmäßiger Tilgung über 42 Jahre nach `MA-002`, einem Verwaltungskostenbeitrag von 0,5 % und 200.000 Euro Reinertrag im ersten Jahr (gebundene Miete):
  - Kapitaldienst Förderdarlehen: 128.571 + 27.000 = 155.571 Euro.
  - Tragbar bei Mindestdeckung 1,2: 166.667 Euro.
  - Für die Bank bleiben 11.095 Euro Schuldendienst, das sind 184.921 Euro Darlehen statt 1,0 Mio. Euro.
- Bei 180.000 Euro Reinertrag wird L_D negativ. Ohne Regel entstünde ein negatives Darlehen.

(c) Ausgleichsgröße: Im geförderten Neubau ist die Ausgleichsgröße das Eigenkapital. Das steht nur mittelbar da („höchstens 1,0 Mio. Euro“).

Vorschlag, im Bericht in D.4 und `MA-026` je ein Satz:
- Bankdarlehen = max(0; min(GK − FD − Z − EK_min; Deckel a; Deckel b)), Eigenkapital = GK − FD − Z − Bankdarlehen.
- Den Bezug der Quote als zweite Frage in `MA-026` aufnehmen. Vorsichtig ist „alle Darlehen gegen den Wertansatz“; die andere Lesart ist „nur das Bankdarlehen im Nachrang“.
- Ist die Mindestdeckung schon ohne Bankdarlehen verfehlt, meldet das Blatt das, statt einen Preis zu nennen.
- Für die Mittelherkunft festlegen, dass Darlehen brutto und einbehaltene Entgelte als Mittelverwendung zählen, wie A Nr. 23. Sonst schließt 5,4 + 1,8 + 1,8 + 1,0 nicht, sobald das Bearbeitungsentgelt einbehalten wird.

**3. [Hinweis · belegt] `MA-027`, Spezifikation Kapitel 2 („Offene Lehrbuchdefinitionen“) gegen Bericht A Nr. 18: Die gewählte Regel ergibt bei jedem fremdfinanzierten Bestand die Haltedauer und widerspricht dem Bericht.**

Problem:
- Ohne Restwert vor dem Verkauf ist das „Vermögen aus der Investition“ bis zum Verkauf entweder nur das Guthaben, oder es ist Guthaben minus Restschuld.
- Im Testfall (`amort.py`):

| Jahr | Guthaben | Guthaben minus Restschuld | Alternative |
|---|---|---|---|
| 1 | 10.180 € | −675.820 € | 405.600 € |
| 4 | 45.264 € | −595.286 € | 422.875 € |

- In beiden Lesarten wird die Alternative erst mit dem Verkauf in Jahr 5 erreicht. Die Kennzahl gibt dann stets die Haltedauer aus, sofern die Endwertdifferenz positiv ist, und sonst nichts. Sie sagt also nichts über die Endwertdifferenz hinaus.
- A Nr. 18 nennt dagegen „zwei oder drei Jahre“ im Testfall und setzt einen Wertpfad voraus. Quellnotiz 03, Zeile 147, nennt als übliche Lesart die „fiktive Veräußerung in t“.

Zwei weitere Lücken:
- Es fehlt die Festlegung, ob die erste oder die dauerhafte Überschreitung zählt. Ein späterer Investitionsstau kann das Vermögen wieder unter die Alternative drücken.
- Es fehlt, wie Nachschüsse und Entnahmen in die Vergleichsanlage eingehen. Nach Nr. 11 wäre das gespiegelt.

Vorschlag:
- In `MA-027` „ohne Restwert“ ersetzen durch „mit dem Liquidationswert aus dem Wertpfad (Nr. 18: Marktwert abzüglich Verkaufskosten, Vorfälligkeit, Steuer)“, mit der Voreinstellung „ab der Periode, von der an die Alternative dauerhaft erreicht ist“, und mit gespiegelten Einlagen und Entnahmen.
- Oder die Kennzahl erst mit dem Wertpfad in 1b ausweisen.
- Den Widerspruch zu Nr. 18 im Bericht und in der Spezifikationszeile beheben.

**4. [Hinweis · begründete Einschätzung] Quellnotiz 10, II. BV, und Bericht B.4, Zeile „Kostenmiete: anzusetzende Beträge“: Die Erklärung der Abweichung von 1,5 % trägt nicht. B.4 widerspricht der Notiz.**

Die Erklärung trägt nicht:
- § 26 Abs. 4 II. BV schreibt multiplikativ von Oktober zu Oktober fort (am Original gelesen). Eine solche Kette ergibt sich auf das Gesamtverhältnis VPI(Okt. 2025) / VPI(Okt. 2001), unabhängig von der Zahl der Schritte.
- Eine Umbasierung ändert Verhältnisse nur durch die Rundung der Indexstände auf eine Nachkommastelle und durch die Revision weniger Jahre um das neue Basisjahr. Die Notiz misst die Wirkung selbst: 356,32 statt 357 Euro, also 0,19 %.
- Acht Kettenschritte mit je auf eine Nachkommastelle gerundetem Prozentsatz ergäben höchstens rund 0,4 %, nicht 1,5 %.
- Rechnet man die Sekundärwerte mit dem letzten Schritt von 8,37 % zurück, ergibt sich für 2023 343,69 Euro je Wohnung. Aus der heutigen Reihe folgen 338,59 Euro. Die Lücke besteht also schon vor 2023.
- Die Ursache ist damit offen. Möglich ist auch, dass die Sekundärquelle anders rechnet oder irrt.

Die Folgerung der Notiz bleibt richtig: veröffentlichte Werte führen.

Widerspruch zu B.4:
- B.4 sagt weiter: „passen rechnerisch zu den Beträgen der Verordnung“.
- Das stimmt nur in dem Sinn, dass alle vier Sekundärwerte denselben Faktor haben (11,50 / 7,10 = 1,6197; 14,58 / 9,00 = 1,6200; 18,62 / 11,50 = 1,6191; 372,46 / 230 = 1,6194).
- Aus dem Index nachrechenbar sind sie nicht.

Vorschlag:
- In der Notiz „erklärt sich daraus, dass …“ ersetzen durch „Ursache nicht geklärt; Umbasierung erklärt höchstens einige Zehntelprozent“.
- In B.4 schreiben: „untereinander mit einem Faktor stimmig, aus dem Verbraucherpreisindex nicht nachrechenbar (Abweichung 1,5 %)“.

**5. [Hinweis · belegt] A.1 Nr. 3, Kontrollsumme Investitionsstau: Bei teilweise ausgeführter Maßnahme gibt es keinen Eurobetrag, gegen den die Probe schließt.**

- Gezahlter und abgezogener Anteil haben verschiedene Preisstände.
- Beispiel aus Nr. 3: 40 % in Jahr 9 ausgeführt, also 40.000 · 1,03⁹ = 52.190,93 €. 60 % stehen am Stichtag Jahr 10 aus, also 60.000 · 1,03¹⁰ = 80.634,98 €. Summe 132.825,91 €.
- Diese Summe entspricht weder 100.000 € (heute) noch 134.392 € (Stichtag) noch 142.576 € (Planjahr).

Vorschlag: Die Probe in Anteilen oder zu Basispreisen fassen: „gezahlter Anteil + abgezogener Anteil = 100 % der Maßnahme; jeder Anteil zum Preisstand seines Zeitpunkts bewertet“. Das kann im Bericht stehen (ein Halbsatz) oder in der Fachspezifikation.

**6. [Hinweis · belegt] A.6, Zeile „Testfall“: Der Alternativzins fehlt unter den Annahmen.**

- Der Nachbau trifft alle Werte auf den Cent, aber nur, weil sich h = 2 % vor Steuern und 30 % Steuer aus Nr. 12 (Vergleichszins 1,409 % im Monatsraster) erschließen lassen.
- Ohne diese Angabe sind Endwertdifferenz und Vergleich mit der Rendite aus A.6 allein nicht nachbaubar.

Vorschlag, im Bericht: „Alternativzins 2 % vor Steuern, also 1,4 % nach Steuern“ in die Annahmenspalte.

**7. [Hinweis · belegt] D.4 „Darlehen“: Nach Ende der Zinsbindung ist die Rate nicht festgelegt.**

Drei Lesarten liegen nahe: Rate bleibt, Tilgungssatz bleibt, oder Restlaufzeit bleibt.

Wirkung im Modell (`anschluss.py`: 1,496 Mio. Euro, 4 % und 2 %, zehn Jahre Bindung, 6 % Anschlusszins, Haltedauer 15 Jahre):

| Lesart | Rate ab Jahr 11 | Deckung ab Jahr 11 |
|---|---|---|
| Rate bleibt | 89.760 € | 1,20 |
| Tilgungssatz bleibt | 90.942 € | – |
| Restlaufzeit bleibt | 104.952 € | 1,03 |

- Auf den Endwert wirkt die Wahl wenig: rund 4.600 Euro über fünf Jahre.
- Auf die Deckung wirkt sie stark, siehe Tabelle. Für den Stressfall und die Kreditkennzahlen ab 1b zählt das.

Vorschlag, in der Fachspezifikation: Die Voreinstellung „Tilgungssatz bleibt“ festlegen. Das ist die übliche Prolongation. Die Lesart gehört zur „erzwungenen Anschlussannahme je Tranche“.

**8. [Hinweis · begründete Einschätzung] D.1 „Vergleich und Zielwertsuche“: „das Werkzeug alle Lösungen findet“ setzt einen Suchbereich und ein Raster voraus.**

- Anders als beim internen Zinsfuß gibt es für eine allgemeine Eingabe keine Obergrenze der Zahl der Lösungen, wie sie die Vorzeichenregel beim internen Zinsfuß liefert.
- „Alle Lösungen“ ist daher nur „alle Lösungen im Suchbereich bei Rasterweite x“.

Vorschlag, in der Fachspezifikation: Je gekennzeichneter Eingabe einen Suchbereich (Voreinstellung aus dem Katalog) und ein Raster festlegen, mit Verfeinerung durch Bisektion an jedem Vorzeichenwechsel. Ausgabe: „Lösungen im Bereich [a; b]“.

## Zuordnung

| Befund | Wo beheben |
|---|---|
| 1, 2 | Im Bericht, Auflage für die 9 |
| 3, 4, 6 | Im Bericht, kurz; Kern von 3 auch in `MA-027` und Spezifikation Kapitel 2 |
| 5 | Bericht oder Fachspezifikation |
| 7, 8 | Fachspezifikation |

## Nicht geprüft

- **Änderungen ohne Rechenbezug:** Rechtsinhalte in B.1, B.2 und B.5, C.1 außer den Förderquoten, Zuschnitt und Reihenfolge der Teilschritte sowie Wortlaut und Gestaltung gehören zu anderen Rollen.
- **Skripte der Überarbeitung:** `u4_zahlen.py` und `u4_testfall.py` sind nicht zeilenweise gelesen. Der Testfall wurde bewusst unabhängig davon nachgebaut.
- **Variante Monatsraster und Variante einheitlicher Zins (A.6):** In dieser Runde unverändert, nicht erneut gerechnet.
- **VPI-Stände:** Die Werte der Notiz (77,1 / 123,0 / 126,5 und weitere) sind nicht an Destatis nachgelesen. Gerechnet wurde mit den Werten der Notiz. Ob der Oktoberwert 2026 schon endgültig ist, ist nicht geprüft.
- **Sekundärwerte der II. BV:** Die Haufe-Werte sind nicht am Original gelesen.
- **Grobkalkulationsmodell:** Es ist eine eigene Vereinfachung. Monotonie und Eindeutigkeit hängen in der Richtung nicht an den Parametern, die Höhe der Preise schon.
