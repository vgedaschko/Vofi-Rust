Rolle: Steuerberater (Immobilienmandanten aller Rechtsformen)
Prüfobjekt: `docs/fachspezifikation-rechenkern.md`, eingefrorener Stand vom 2026-11-21, Runde 3. Ganz gelesen: Kapitel 7, R-6.10, R-6.16, R-9.5, Kapitel 16, die Steuerzeilen von Kapitel 17 und Anhang A.3 bis A.6. Dazu M-37, M-44, M-45 und M-51 aus Kapitel 14; `MA-016`, `MA-030`, `MA-031`, `MA-032`, `MA-036` und `MA-041` in `annahmen.toml`; die Katastereinträge zu den zitierten Kennungen. Vorab gelesen: mein Bericht und die Sichtung der Runde 2, die Quellnotizen 13 und 15 sowie die Durchsicht an der Wesentlichkeitsschwelle, Teil d.

Gesamturteil: Ja, mit zwei Auflagen. Die Steuer in Kurzform ist je Steuerstatus jetzt richtig gebaut. Die Befunde der Runde 2 sind behoben oder vertretbar anders entschieden. Alle Beispielzahlen aus Kapitel 7, die ich nachgerechnet habe, stimmen auf den Cent, ebenso die RF-13- und RF-17-Werte, die ich im Referenzrechner nachgefahren habe. Zwei Fehler stecken in der vorhandenen Regel R-7.8:
- Die Kürzung wird auch in Verlustjahren angesetzt. Dadurch rechnet das Kennzeichen E-41 im Neubau schlechter als ohne Kennzeichen.
- Die Personengesellschaft, die mit dem Verkauf aufgegeben wird, ist im Verkaufsjahr wie die fortbestehende GmbH behandelt.

Note: **8 von 10.** Zur 9 fehlen die Befunde 1 und 2 (je ein Satz in R-7.8 und an E-69) und die Reststellen aus den Befunden 3 und 4; alles andere ist Hinweis.

## Stand der Befunde aus Runde 2

| Nr. | Thema | Stand | Bemerkung |
|---|---|---|---|
| 1 | Voreinstellung des Zuschusses | **anders entschieden und vertretbar** | Ich folge der Quellnotiz 15:<br>- **Privatperson:** Mein Satz „in keinem Feld zwingend“ ist widerlegt. R 21.5 Abs. 2 EStR (heute in Verlagswiedergabe gelesen) macht den Bindungszuschuss zur Einnahme im Zuflussjahr. Die Verteilung ist das Wahlrecht nach § 11 Abs. 1 Satz 3 EStG (heute gelesen), also richtig als Eingabe E-70 geführt.<br>- **Betriebsvermögen:** Mein Befund ist bestätigt. R 6.5 Abs. 1 Satz 3 EStR und H 5.6 EStH, „Ertragszuschüsse“ (heute gelesen), tragen die Voreinstellung „verteilt“; als begründete Ausnahme von der Vorsichtsregel gekennzeichnet.<br>Dass die Kopplung an das Kennzeichen entfällt, ist vertretbar: Der Unterschied liegt bei 4,001 % gegen 3,993 %. |
| 2 | Rückzahlung des Zuschusses | **behoben** | Bei „sofort“ steht die Rückzahlung im laufenden Ergebnis des Verkaufsjahres, auch bei der Privatperson nach der Frist. Das stützt R 21.5 Abs. 1 Satz 10 EStR (heute gelesen): zurückgezahlte Zuschüsse sind „im Jahr der Rückzahlung als Werbungskosten abzuziehen“. Der Satz zu P-15 ist eingeschränkt; Reststelle in Befund 4 |
| 3 | Verein und Stiftung | **behoben** | R-7.17 nach § 8 Abs. 1 und 2 KStG mit Frist, Zahlungsprinzip und ohne Gewerbesteuer; die Verlustverrechnung mit Zinsen trägt § 8 Abs. 10 Satz 1 KStG (heute gelesen). Rest zu R-9.5: Befund 7 |
| 4 | Entgelt auf den Zuschuss | **behoben** | Es ist kein Entgelt für Schulden und keine Hinzurechnung mehr und folgt der Lesart des Zuschusses (R-7.2, R-7.15, R-7.16, R-7.19) |
| 5 | Laufzeitbezogene Entgelte der Privatperson | **behoben** | Verteilt nach § 11 Abs. 2 Satz 3 EStG (heute gelesen); Disagio-Prüfregel für Teil 2 vorgemerkt |
| 6 | Reihenfolge Kürzung vor Verlustabzug | **behoben** | Schritte 1 bis 7 in R-7.8 folgen §§ 7 bis 11 GewStG. Neu daran hängt Befund 1 |
| 7 | Kürzung im Verkaufsjahr | **behoben** | Fall 1 als Regel nach BFH III R 1/23, heute am Original ganz gelesen: Die Kürzung wird nicht zeitanteilig gewährt, es bleibt die einfache Kürzung (Gründe II.1.a, II.3). Rest für die Personengesellschaft: Befund 2 |
| 8 | „nahezu neutral“ bei `MA-036` | **behoben** in R-7.18 | In `MA-036`, Feld „grundlage“, steht der alte Satz noch ohne Einschränkung (Befund 4) |
| 9 | Erweiterungen in der 15-%-Regel | **behoben** | R-6.16 nimmt sie aus. Der Verweis „das Eingabefeld E-52 sagt das“ zielt auf ein gestrichenes Feld (Befund 4) |
| 10 | § 15a EStG bei „sofort“ | **behoben** | R-7.6 und `MA-016` |
| – | Kleinigkeiten (M-37, `GEWSTG-3`, „ohne Erbbauzins“, `MA-030` „Verwendet in“, Vorfälligkeit und Frist) | **behoben** | M-37 in R-7.1 und in der Meldungstabelle verschieden gefasst (Befund 4) |

## Befunde

1. **[wichtig · belegt (Wortlaut heute gelesen, Gegenrechnung)]**
   - **Fundstelle:** R-7.8, Satz „das operative Ergebnis e_op samt der darauf entfallenden Hinzurechnung, auch wenn es negativ ist. Weil die Kürzung vor dem Verlustabzug steht, bildet ein negatives e_op mit Kennzeichen keinen gewerbesteuerlichen Verlustvortrag.“
   - **Problem:** § 9 Nr. 1 Satz 2 GewStG gewährt die erweiterte Kürzung „auf Antrag“, und zwar je Erhebungszeitraum (§ 14 Satz 2 GewStG). Kein Unternehmen stellt den Antrag in einem Jahr, in dem der Grundstücksteil negativ ist. Es hat dann die einfache Kürzung nach Satz 1, die gerechnete Kurzform keine Kürzung. Der Fehlbetrag wird nach § 10a GewStG vorgetragen und steht im Verkaufsjahr gegen den gewerbesteuerpflichtigen Verkaufsgewinn, wenn die Kürzung dort nach Fall 1 entfällt. Kürzt die Regel auch den Verlust, geht dieser Vortrag verloren.
   - **Folge:** Mit Kennzeichen rechnet das Vorhaben schlechter als ohne. Das ist eine falsche Zahl, keine Vorsicht. Die Durchsicht hat das Symptom schon gemessen (E-41 im Neubau: tragbarer Grundstückspreis −0,76 %).
   - **Gegenrechnung** (`skripte/pruefrunde-fachspezifikation-3/steuerberater/gegenrechnung.py`): Referenzrechner unverändert gegen die Variante „Antrag nur, wenn e_op samt Hinzurechnung positiv ist“, Körperschaft, E-69 nein.

     | Fall | ohne Kennzeichen | Kennzeichen, wie gebaut | Kennzeichen, Antrag nur bei positivem Teil |
     |---|---|---|---|
     | Ankauf (RF-13 Nr. 1/2) | 4,527 % | 4,670 % | 4,724 % (+0,054 PP) |
     | Neubau frei finanziert | 4,332 % | **4,324 %** | 4,358 % (+0,034 PP) |
     | gefördert, 38 Jahre | 3,956 % | 4,001 % | 4,024 % (+0,023 PP) |
     | gefördert, 20 Jahre | 2,081 % | **1,979 %** | 2,089 % (**+0,110 PP**) |
     | Ankauf mit E-69 | – | 5,161 % | 5,183 % |

   - **Vorschlag:** In R-7.8 statt „auch wenn es negativ ist“: „Ist der Grundstücksteil (e_op samt Hinzurechnung) eines Jahres negativ, unterbleibt die Kürzung in diesem Jahr (Antrag nach `GEWSTG-9`); der Gewerbeertrag ist dann e_op + z_h + Hinzurechnung, ein negativer Betrag wird vorgetragen.“
     - Das gilt auch dann, wenn man die erweiterte Kürzung ohnehin nicht für negativ hält; dazu habe ich keine Rechtsprechung gelesen.
     - Ein Feld kostet es nicht. Die Sollwerte von RF-13 Nr. 2, 3 und 10 und von RF-17 „mit Kennzeichen“ ändern sich.
     - Neu ins Kataster: `GEWSTG-14`.

2. **[wichtig · begründete Einschätzung (Gesetz und Urteil heute gelesen, Schluss daraus nicht in Rechtsprechung belegt)]**
   - **Fundstelle:** R-7.8, Fall 1 („gedacht für die Objektgesellschaft“); E-69; M-51; R-7.18 mit der Lesart des Hauses „Verkauf im Rahmen der Aufgabe des Betriebs“ (`MA-036`).
   - **Problem:** BFH III R 1/23 begründet den Wegfall der Kürzung für eine GmbH: Sie bestand über den Verkauf hinaus fort, ihre Steuerpflicht dauerte nach § 2 Abs. 2 GewStG an, der Erhebungszeitraum war nicht abgekürzt (Gründe II.1.b, II.2). Für Mitunternehmerschaften sagt dasselbe Urteil: Sie sind gewerbesteuerpflichtig, „wenn und solange sie einen Gewerbebetrieb … unterhalten“.
   - **Folge:** Wird die gewerblich geprägte KG mit dem Verkauf aufgegeben, endet ihre Steuerpflicht. Der Erhebungszeitraum ist dann abgekürzt (§ 14 Satz 3 GewStG, heute gelesen), und in diesem Zeitraum hat sie ausschließlich eigenen Grundbesitz verwaltet. Die Kürzung bleibt also. Vom Aufgabegewinn nimmt § 9 Nr. 1 Satz 6 GewStG (heute gelesen) nur § 7 Satz 2 Nr. 2 und 3 aus, nicht Nr. 1. Der gewerbesteuerpflichtige Teil des Aufgabegewinns, der auf Kapitalgesellschaften entfällt, wäre nach H 9.2 (3) GewStH mitgekürzt.
   - **Der Kern rechnet heute** mit der Aufgabe-Lesart und Kennzeichen trotzdem Fall 1.
   - **Gegenrechnung** (Ankauf, geprägte KG, 440 %, 60 % natürliche Personen, Kennzeichen, Aufgabe): 3,531 % wie gebaut gegen 3,648 % mit Fall 2, also **0,117 PP**.
   - **Vorschlag:** E-69 und M-51 um den dritten Sachverhalt ergänzen: „… oder die Personengesellschaft wird mit dem Verkauf aufgegeben (abgekürzter Erhebungszeitraum, `GEWSTG-14`)“. Ist die Lesart „Aufgabe“ des Hauses gestellt, gilt bei der Personengesellschaft mit Kennzeichen Fall 2 ohne Eingabe. Die Frage 3 an den Steuerberater (`MA-036`) deckt den Sachverhalt schon ab. Sie wird damit wichtiger, wenn Kapitalgesellschaften Kommanditisten sind; bei 100 % natürlichen Personen ändert sich wenig.

3. **[Hinweis · belegt]**
   - **Fundstelle:** R-7.11, Kopf „(`MA-032`)“ und Satz „… und nicht zum operativen Ergebnis (`MA-032`, vorsichtige Lesart)“.
   - **Problem:** R-7.15, `MA-032` und Kapitel 16 sagen übereinstimmend, die Vorfälligkeit der Privatperson als Veräußerungskosten sei Verwaltungsauffassung und „Regel, keine Annahme mehr“ (BMF vom 27.07.2015, Nr. 2; Kernsatz heute in Verlagswiedergabe gelesen). R-7.11 führt sie noch als Lesart einer Annahme. Das ist ein Widerspruch zweier Regeln.
   - **Vorschlag:** Kennung `MA-032` in R-7.11 durch `BMF-SCHULDZINSEN-2015` ersetzen und „vorsichtige Lesart“ streichen.

4. **[Hinweis · belegt]**
   - **Fundstelle:** Reststellen aus entfallenen Lesarten, Schaltern und Feldern:
     - R-6.16: „das Eingabefeld E-52 sagt das“. E-52 ist entfallen (R-6.10, NF-68); der Hinweis gehört an E-50.
     - R-7.19, Absatz nach „Vorsicht“: „Die Brücke der Probe P-15 (d) schließt in allen drei Lesarten“. Es gibt noch zwei Lesarten, „verteilt“ und „sofort“, und E-70.
     - R-7.8: „Die Voreinstellung ist die ungünstigste der drei Rechnungen“. Es gibt zwei Fälle; gemeint ist wohl: zwei Fälle und die nicht mehr gerechnete strengere Lesart (V-19). So schreiben.
     - Anhang A.5, Zeile RF-13: „Lesarten von `MA-030` … wie bezeichnet“. `MA-030` hat keine Lesart mehr.
     - Anhang A.3, Zeile RF-17: „Hebesatz 400 %, 60 % natürlichen Personen“. Das Beispiel in R-7.18 rechnet mit 440 %, der Rechner führt beide (236.628,00 / 219.828,00 und 243.285,00 / 222.285,00 Euro). Im Anhang beide nennen.
     - `MA-031`, Feld „alternative“: „Beide sind umschaltbar“. Umschaltbar ist nur noch „sofort“; die Minderung ist V-21.
     - `MA-036`, Feld „grundlage“: „Bis zu einem Hebesatz in Höhe des Anrechnungsfaktors ist das … nahezu neutral“. Es fehlt die Einschränkung „bei ausschließlich natürlichen Personen“, die R-7.18 hat.
     - `MA-032`: „klaerung“ und „wiedervorlage“ nennen noch den Steuerberater, obwohl die Frage gestrichen ist (Kapitel 16, Bemerkung der Annahme).
     - M-37: R-7.1 fügt den Zusatz mit Semikolon in den ersten Satz ein, die Meldungstabelle als eigenen Satz „Ob die Voraussetzungen …“. Ein Wortlaut, an einer Stelle festgelegt.
   - **Vorschlag:** Je Stelle wie angegeben. Zahlen aus altem Stand ohne Kennzeichnung habe ich in Kapitel 7 und Anhang A sonst nicht gefunden.

5. **[Hinweis · belegt am Wortlaut]**
   - **Fundstelle:** R-7.8, Satz „Die einfache Kürzung nach `GEWSTG-9` rechnet die Kurzform nicht; das ist eine bewusste Vereinfachung und wirkt vorsichtig“; Liste V-01 bis V-22.
   - **Problem:** § 9 Nr. 1 Satz 1 GewStG (heute gelesen, Fassung zuletzt geändert am 29.06.2026) kürzt um „die im Erhebungszeitraum als Betriebsausgabe erfasste Grundsteuer“, nicht mehr um 1,2 % des Einheitswerts. Das gilt in jedem Jahr ohne Kennzeichen bei Körperschaft, Personengesellschaft und Einzelunternehmen. Die Umlage auf die Mieter ändert daran nichts, die Grundsteuer bleibt Betriebsausgabe. Bei einigen tausend Euro Grundsteuer im Jahr sind das rund 14 % davon, weit unter der Schwelle.
   - **Bruch mit der eigenen Regel:** Die Vereinfachung steht nicht in der Liste, die nach Kapitel 16 „der eine Ort“ ist.
   - **Vorschlag:** Als V-23 aufnehmen. Wortlaut: „Einfache Kürzung um die Grundsteuer (`GEWSTG-9`, Satz 1) nicht gerechnet; je Jahr 14 % der Grundsteuer bei 400 %“.

6. **[Hinweis · belegt durch Gegenrechnung]**
   - **Fundstelle:** V-17 („bis +0,103 Prozentpunkte (Privatperson im Ankauf)“); R-7.5 („Ein Vortrag, der am Ende der Haltedauer übrig ist, verfällt für das Vorhaben“); R-7.19, Beispiel zur Rückzahlung.
   - **Problem:** Die Angabe zu V-17 stimmt im typischen Fall, nicht aber beim Verkauf vor dem Bindungsende. Geförderter Neubau als Privatperson, 20 Jahre, ohne E-70:
     - Mit dem voreingestellten Vortrag verfällt der Verlust aus der Rückzahlung im Verkaufsjahr, rund 857.000 Euro. Die Rendite ist 1,240 %, mit „sofort“ 2,421 %.
     - Mit E-70 sind es 2,573 % gegen 2,913 %.

     Der Investor würde den Verlust gegen andere Einkünfte verrechnen oder zurücktragen; die Regeln des § 10d Abs. 1 EStG zum Rücktrag habe ich heute nicht gelesen. Der Fall ist nicht typisch, deshalb keine neue Regel.
   - **Vorschlag:**
     - In V-17 den Satz anfügen: „Ausnahme: Verkauf vor Bindungsende mit Rückzahlung des Zuschusses (bis 1,2 Prozentpunkte)“.
     - Den verfallenden Vortrag am Ende der Haltedauer in Euro im Annahmenblatt ausweisen; das kostet kein Feld.

7. **[Hinweis · belegt am Wortlaut]**
   - **Fundstelle:** R-9.5: „bei Verein und Stiftung mindern sie das Einkommen (R-7.17)“.
   - **Problem:** § 8 Abs. 10 Satz 2 KStG (heute gelesen) schließt § 20 Abs. 6 und 9 EStG nur in den Fällen des § 32d Abs. 2 aus. Im Übrigen gilt für die Körperschaft mit Überschusseinkünften über § 8 Abs. 1 KStG auch § 20 Abs. 9 EStG: Der Abzug der tatsächlichen Werbungskosten bei Kapitalerträgen ist ausgeschlossen. Die Alternative soll aber dieselbe Logik haben wie bei der Privatperson, deren Kontokorrentzinsen die Regel mit `ESTG-20` nicht abzieht. Die Wirkung ist sehr klein.
   - **Vorschlag:** Den Satz an die Privatperson angleichen („mindern keine Steuer“, `ESTG-20`, `KSTG-8`). Wer das nicht will, benennt es als Vereinfachung. Den Sparer-Pauschbetrag wie bei der Privatperson nicht ansetzen.

### Steuerliche Richtigkeit je Status (Auftrag 2)

- **Körperschaft:** richtig, bis auf Befund 1.
  - Der Satz nach `KSTG-23` stimmt: 15 % bis 2027, dann 14/13/12/11 %, ab 2032 10 % (heute gelesen).
  - Ohne Gewerbesteuer-Freibetrag, Abrundung auf 100 Euro nach § 11 Abs. 1 Satz 3 GewStG (heute gelesen).
  - Hinzurechnung mit Freibetrag und halbem Erbbauzins.
- **Körperschaft mit Kennzeichen, Verkaufsjahr:** Beide Fälle sind richtig.
  - Fall 1 trägt BFH III R 1/23 (am Original).
  - Fall 2 tragen BFH I R 89/03, Leitsatz, und H 9.2 (1) und (3) GewStH, heute in Verlagswiedergabe gelesen; H 9.2 (3) weiter nur in einer Wiedergabe, die Annahme bleibt also mit `MA-030` gekennzeichnet.
  - M-51 trifft den Punkt; ergänzen nach Befund 2.
- **Gewerblich geprägte und originär gewerbliche Personengesellschaft, Einzelunternehmen:** richtig.
  - Freibetrag 24.500 Euro, Messzahl 3,5 % (heute gelesen).
  - Anrechnung mit dem Vierfachen des Messbetrags, begrenzt auf die tatsächliche Gewerbesteuer (§ 35 Abs. 1 Satz 1 Nr. 2 und Satz 5 EStG, heute gelesen).
  - Aufgabegewinn nach § 7 Satz 2 GewStG (heute gelesen).
  - Rest: Befund 2.
- **Privatperson:** richtig.
  - Frist „nicht mehr als zehn Jahre“, die Gebäudeerrichtung einbezogen.
  - Die Abschreibungen mindern die Anschaffungskosten.
  - Werbungskosten, also die Vorfälligkeit, gehören zum Veräußerungsgewinn (§ 23 Abs. 1 Satz 1 Nr. 1, Abs. 3 Satz 1 und 4 EStG, heute gelesen).
  - Der Zuschuss ist Einnahme im Zuflussjahr, mit Wahl nach § 11 Abs. 1 Satz 3 EStG.
  - Die Freigrenze von 1.000 Euro (§ 23 Abs. 3 Satz 5) ist unbeachtlich.
- **Verein und Stiftung:** richtig; Befund 7.
- **Befreite Körperschaft:** richtig, M-44 nach dem BMF vom 22.11.1991 (Quellnotiz 15, heute nicht selbst gelesen).
- **Zuschuss im Betriebsvermögen:** richtig.
  - PRAP nach § 5 Abs. 5 Satz 1 Nr. 2 EStG (heute gelesen), mit H 5.6 „Ertragszuschüsse“ gegen „Investitionszuschüsse“ (heute gelesen).
  - R 6.5 Abs. 1 Satz 3: kein Zuschuss bei unmittelbarem Zusammenhang mit einer Leistung (heute gelesen).
  - Die Kennzeichnung als begründete Ausnahme von der Vorsichtsregel ist richtig.
- **Die Regel kann den Steuerberater nicht ersetzen:** M-37 sagt das einmal und an der richtigen Stelle. Der Wortlaut genügt; mehr Hinweise braucht der Kunde nicht.

### Nachgerechnet (Auftrag 3)

Alles mit `gegenrechnung.py`: Teil A von Hand mit Decimal, Teil B mit dem Referenzrechner, der nur gelesen und nicht geändert wurde.

- **Körperschaft mit Kennzeichen (R-7.8):**
  - 17.407,50 und 1.400,00 Euro.
  - Verkaufsjahr ohne E-69: 181.932,50 Euro, mit E-69: 97.932,50 Euro.
  - Anlaufverlust und Verkauf 2028 mit E-69: 84.112,00 Euro; ohne E-69 wären es 168.112,00 Euro.
  - RF-13: 139.930,00 Euro Gewerbesteuer auf den Verkaufsgewinn. Rendite 4,527 / 4,670 / 5,161 % stimmen.
- **Körperschaft ohne Kennzeichen:** R-7.7 mit 15.825,00 und 14.000,00 Euro; 8.638,24 Euro mit dem Satz 2028.
- **Hinzurechnung (R-7.16):** 34.025,00 und 31.925,00 Euro.
- **Personengesellschaft:** alle fünf Zeilen der Tabelle in R-7.9.
  - R-7.18: 243.285,00 und 222.285,00 Euro.
  - RF-13 Nr. 10: 3,594 %.
- **Privatperson:**
  - R-7.10: 12.863,75 und 131,88 Euro; R-7.11: 63.000,00 Euro.
  - Verkauf nach 9 / 10 / 11 / 12 Jahren: 3,365 / 3,528 / 4,882 / 5,141 %. Steuer auf den Verkaufsgewinn 289.237,34 und 334.954,62 Euro, nach elf Jahren null.
- **Verein und Stiftung:** 15.825,00 Euro (Satz 2036: 10,55 %); Vortrag 15.000 Euro.
- **Zuschuss im geförderten Neubau:**
  - Körperschaft: verteilt 3,956 %, mit Kennzeichen 4,001 %.
  - Privatperson: ohne E-70 3,808 %, mit E-70 4,380 %.
  - Rückzahlung nach 20 Jahren, Privatperson mit „sofort“: Erstattung 359.862,30 Euro und 2,421 %; mit E-70 1.876,05 Euro Steuer und 2,913 %.
  - Verteilung 24.911,86 / 49.823,73 Euro, Entgelt 186,84 / 373,68 Euro.
- **R-7.15:** 1.199,88 und 1.439,86 Euro. **R-6.16:** 48.087,20 Euro.

Alles stimmt.

### Vereinfachungen und Fragen (Auftrag 4)

- **Steuerliche Vereinfachungen:** V-13, V-18, V-19, V-20 und V-21 sind tragbar; gemessen und von mir bestätigt: V-21 0,008 PP auch mit Kennzeichen, V-19 0,027 PP. V-17 ist im typischen Fall tragbar, Ausnahme nach Befund 6.
- **Wegfall der Schalter:** tragbar, bei `MA-030`, `MA-031` „Minderung“ und `MA-032` ebenso wie bei `MA-036` im Vorhaben. Bei `MA-036` setzt das voraus, dass Befund 2 aufgenommen wird.
- **Die drei Fragen an den Steuerberater sind die richtigen.**
  - Frage 3 sollte um den Satz ergänzt werden: „Wird die KG mit dem Verkauf eingestellt, sodass der Erhebungszeitraum abgekürzt ist?“ (Befund 2).
  - Der Teil „Tilgungsnachlass“ in Frage 2 betrifft erst den Förderteil; er kann dort bleiben.
  - Eine weitere Frage braucht es nicht. Befund 1 ist am Gesetzeswortlaut entschieden.

## Heute am Text gelesen (2026-11-21)

`www.gesetze-im-internet.de` war heute aus der Sitzung nicht erreichbar: Die Verbindung wurde zurückgesetzt, die Namensauflösung schlug fehl. Den Host muss jemand in den Netzeinstellungen der Sitzung freigeben, wenn die Gesetzestexte wieder am Original gelesen werden sollen. Die Gesetzestexte sind deshalb bei buzer.de gelesen, einer Volltextsammlung mit Fassungsangabe. Belegstufe: **Wortlaut in Verlagswiedergabe**. Abrufkopien liegen nur im Scratchpad der Sitzung, nicht im Repository.

| Kennung | Vorschrift, Stelle | Fassung laut Quelle | Belegstufe |
|---|---|---|---|
| `BFH-III-R-1-23` | Urteil vom 17.10.2024, ganz (Leitsatz, Tatbestand, Gründe II.1 bis II.5) | ECLI:DE:BFH:2024:U.171024.IIIR1.23.0 | am Original (bundesfinanzhof.de) |
| `KSTG-23` | § 23 Abs. 1 KStG | i. d. F. G. v. 14.07.2025 (BGBl. 2025 I Nr. 161); zuletzt geändert 04.02.2026 | Wortlaut in Verlagswiedergabe; deckt sich mit dem Kataster |
| `KSTG-8` | § 8 Abs. 10 KStG | zuletzt geändert 29.06.2026 (BGBl. 2026 I Nr. 197) | Wortlaut in Verlagswiedergabe |
| `GEWSTG-9` | § 9 Nr. 1 Satz 1 bis 6 GewStG | zuletzt geändert 29.06.2026 | Wortlaut in Verlagswiedergabe; Satz 1: Grundsteuer als Betriebsausgabe (bestätigt Quellnotiz 13) |
| neu: `GEWSTG-14` | § 14 Satz 1 bis 3 GewStG (abgekürzter Erhebungszeitraum) | zuletzt geändert 29.06.2026 | Wortlaut in Verlagswiedergabe |
| `GEWSTG-2` | § 2 Abs. 1 bis 4 GewStG | zuletzt geändert 29.06.2026 | Wortlaut in Verlagswiedergabe |
| `GEWSTG-7` | § 7 Satz 2 GewStG | zuletzt geändert 29.06.2026 | Wortlaut in Verlagswiedergabe |
| `GEWSTG-11` | § 11 Abs. 1 und 2 GewStG | JStG 2010 | Wortlaut in Verlagswiedergabe |
| `ESTG-11` | § 11 Abs. 1 Satz 1 bis 5, Abs. 2 Satz 1 bis 6 EStG | JStG 2007; Gesetz zuletzt geändert 15.10.2026 | Wortlaut in Verlagswiedergabe |
| `ESTG-23` | § 23 Abs. 1 Satz 1 Nr. 1, Abs. 3 Satz 1 bis 8 EStG | JStG 2024; zuletzt geändert 10.02.2026 | Wortlaut in Verlagswiedergabe |
| `ESTG-5` | § 5 Abs. 5 Satz 1 und 2 EStG | Gesetz zuletzt geändert 15.10.2026 | Wortlaut in Verlagswiedergabe |
| `ESTG-35` | § 35 Abs. 1 Satz 1 bis 5 EStG | – | Wortlaut in Verlagswiedergabe |
| `ESTR-21-5` | R 21.5 Abs. 1 Satz 1 bis 10 und Abs. 2 EStR | EStR 2012 i. d. F. 25.03.2013 (VZ 2012–2026) | Wortlaut in Verlagswiedergabe (NWB); neu belegt: Abs. 1 Satz 10, Rückzahlung als Werbungskosten im Jahr der Rückzahlung |
| `ESTR-6-5` | R 6.5 Abs. 1 Satz 1 bis 3, Abs. 2 Satz 1 und 2 EStR | wie oben | Wortlaut in Verlagswiedergabe (NWB) |
| `ESTH-5-6` | H 5.6 EStH, „Ertragszuschüsse“, „Investitionszuschüsse“ | VZ 2025–2026 | Wortlaut in Verlagswiedergabe (NWB) |
| `GEWSTR-9-2` | H 9.2 (1) „Veräußerung des Grundbesitzes“, „Veräußerung eines Mitunternehmeranteils“; H 9.2 (3) „Veräußerungsgewinne“ | VZ 2024–2026 | Wortlaut in Verlagswiedergabe (NWB); H 9.2 (3) weiter eine Wiedergabe. Neu: H 9.2 (1) spricht von der „GmbH“ (Befund 2) |
| `BFH-I-R-89-03` | Leitsatz und Beginn der Gründe I | BStBl II 2004 S. 1080 | Wortlaut in Verlagswiedergabe (NWB) |
| `BMF-SCHULDZINSEN-2015` | Nr. 2, Kernsatz zur Vorfälligkeitsentschädigung | BStBl I 2015 S. 581 | Wortlaut in Verlagswiedergabe (NWB) |

Abweichungen vom Kataster: keine in der Sache. Die Fundstellen von `KSTG-23` und `KSTG-8` verweisen auf `kstg_1977/…`; heute nicht prüfbar, weil der Host nicht erreichbar war.

## Nicht geprüft

- Gesetzestexte am Original (gesetze-im-internet.de nicht erreichbar, siehe oben). § 6 Abs. 1 Nr. 1a EStG (R-6.16) und § 15a EStG habe ich heute nicht erneut gelesen; die Lesung aus Runde 2 gilt.
- Rechtsprechung zur Frage, ob die erweiterte Kürzung negativ sein kann (Befund 1 trägt unabhängig davon), und zum Ende der Steuerpflicht der geprägten KG bei Aufgabe (Befund 2: Schluss aus § 14 Satz 3 GewStG und BFH III R 1/23, Gründe II.1.b).
- BFH vom 29.04.1987 (Grundlage von H 9.2 (3)); BMF vom 22.11.1991 im BStBl; § 10d Abs. 1 EStG (Rücktrag).
- Förderrechtliche Verzinsung eines zurückgeforderten Zuschusses: Rolle Fachexperte, nicht Steuer.
- Die übrigen Steuerausprägungen von RF-13 (Nr. 4 bis 9, 11, 12, 14) und die Verein-Renditen 5,051 und 5,249 %: nicht einzeln nachgefahren.

Eigene Rechnung: `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/pruefrunde-fachspezifikation-3/steuerberater/gegenrechnung.py`, Ausgabe in `gegenrechnung.ausgabe.txt` daneben.
