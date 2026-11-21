Rolle: Bank (Kreditprüfer einer finanzierenden Bank, wohnungswirtschaftliche Immobilienfinanzierung)
Prüfobjekt: `docs/fachspezifikation-rechenkern.md`, eingefrorener Stand vom 2026-11-21. Vollständig gelesen: Kapitel 5, 10, 11 und 16. Aus Kapitel 3 die Zeilen E-35 bis E-38, E-45, E-46, E-59, E-60, E-64, E-65, H-02 bis H-07, H-10, H-11, H-18 bis H-20, H-25 bis H-39, KAT-10, KAT-13 und KAT-15. Dazu Anhang A.4 bis A.6, `MA-026`, `MA-033`, `MA-034` und `MA-040`, die Kataster-Einträge zu BelWertV, BGB und KfW, Quellnotiz 13 (Abschnitte KfW und Bank) und die Durchsicht an der Wesentlichkeitsschwelle, soweit sie die Finanzierung betrifft. Den Referenzrechner habe ich unverändert benutzt: `referenzfaelle.py` besteht mit 1.093 von 1.093 Prüfungen. Drei eigene Läufe kamen dazu.

Gesamturteil: Trägt, mit Auflagen. Ein Kreditprüfer würde das ausgewiesene Bankdarlehen in dieser Größenordnung zusagen; nach meiner Einschätzung ist es eher vorsichtig bemessen. Das gilt für den Ankauf (1,23 Mio. Euro, 51 % des Kaufpreises, Deckung 1,40 laut Finanzplan und 1,20 nach Bemessung) und für den Neubau (4,0 Mio. Euro, 44 % der Gesamtkosten; mit KfW-Darlehen 56 %). Schlüssig sind auch die Deckung über alle Darlehen, das schwächste Jahr, die ungünstigste Anschlussregel und der neu bemessene Stressfall. Alle acht Befunde der Runde 2 sind behoben oder vertretbar anders entschieden. Offen sind drei Stellen: Beim Neubau mit Vorlauf laufen Bereitstellungszins und KfW-Fristen ab dem Grundstückskauf. Die Zwischenfinanzierung der Fördermittel setzt eine Bank voraus, die sonst nichts finanziert. Und ein Beispiel samt Bedienhinweis zu H-25 stimmt nach dem Wegfall der Tranchensätze nicht mehr.

Note: 8 von 10. Zur 9 fehlen die Befunde 1 bis 3. Befund 1 liegt über der Wesentlichkeitsschwelle, Befund 2 entscheidet, ob die Finanzierung überhaupt steht, Befund 3 ist eine falsche Zahl. Alle drei lassen sich im Dokument beheben, ohne neue Eingabe.

## Stand der Befunde aus Runde 2

| Nr. | Befund Runde 2 | Stand | Beleg im Prüfobjekt |
|---|---|---|---|
| 1 | Voreinstellung „Förderdarlehen: ja“ beim übernommenen Darlehen | behoben | Das Kennzeichen ist entfallen. Ein übernommenes Darlehen rechnet immer mit Vorfälligkeit (R-5.16, V-03). Im Bemessungszins ist es eine fremde Tranche (R-5.12); E-59 hat sieben Werte. |
| 2 | Zinsanstieg bis zur Zusage ohne neue Bemessung | behoben | R-11.8, NF-35. Nachgerechnet: L_Stress = 85.862,70 / 7,5 % = 1.144.835,99 Euro, im Neubau 280.500 / 7,5 % = 3.740.000,00 Euro. Das Eigenkapital ist Ausgleichsposten (R-11.3). |
| 3 | Prolongationsregel verbirgt Unterdeckung; H-07 widerspricht R-3.2 | behoben | R-10.14 Nr. 5: kleinste Deckung nach der ungünstigsten Regel. M-38 und M-39 prüfen den kleineren Wert, `MA-034` hat Gewicht mittel, H-07 ist entfallen. Das Wahlrecht ist eine benannte Vereinfachung (V-01); das ist vertretbar, weil die Deckung trotzdem ausgewiesen wird. |
| 4 | zwei „Kapitaldienstreserven“ | behoben | R-10.21 „laut Finanzplan“, R-10.24 „nach Bemessung“. Nachgerechnet: 103.035,24 − 1,2 x 85.862,64 = 0,07 Euro. |
| 5 | geförderter Neubau: Verlauf der Deckung und freier Beleihungsraum fehlen | behoben | R-11.15. Nachgerechnet: A − C = 628.357,62 − 361.393,64 = 266.963,98 Euro; nötiger Reinertrag 1,2 x (151.713,24 + 25.297,56) = 212.412,96 Euro; Mindestdeckung 0,8995; Planjahr 9, im Stressfall 11 (Referenzrechner). |
| 6 | nachhaltige Miete im Neubau | behoben | E-65, voreingestellt E-16. Die Voreinstellung ist als günstige Ausnahme in `MA-026` gekennzeichnet; Frage 4 ist auf den Neubau ausgedehnt. |
| 7 | Nahtstellen KfW und Deckung | behoben | Dass das KfW-Darlehen den Beleihungsraum belegt, ist Festlegung (R-5.12 (a), R-5.19). „Deckung bei voller Tilgung“ steht in R-10.14 Nr. 2. Das Ende der zinslosen Zeit zählt mit (Nr. 4: Planjahr 37, 1,8848). Reste in `MA-026`: Befund 4. |
| 8 | fehlende Fragen an die Hausbank | behoben, Frage zur Anschlussregel vertretbar gestrichen | Fragen 1, 4, 8 und 10 sind ergänzt. Die Frage zur Anschlussregel fällt nach V-01 unter die Schwelle; die Deckung danach steht auf dem Blatt. |

**Kreditrechnung der Grobkalkulation (Prüfauftrag 2):**
- **Bemessung R-5.12:** Die drei Grenzen, der Bemessungszins der fremden Tranchen, RE_n mit Mindestansatz und die Rundung zur sicheren Seite habe ich an RF-09, RF-11, RF-12 (frei, mit KfW-Darlehen, gefördert) und am gebundenen Bestand nachgerechnet. Alle Werte stimmen außer dem in Befund 3.
- **Deckung über alle Darlehen und schwächstes Jahr:** Das ist in sich widerspruchsfrei. Die Deckung laut Finanzplan (R-10.14) und die nach Bemessung (R-10.24) sind getrennt benannt. Die kleinste Deckung zählt erst die vollen Vermietungsjahre, die Deckung nach jeder Bindung und nach der ungünstigsten Regel steht daneben.
- **Stressfall:** Die Neubemessung nur mit dem Zinsanstieg bis zur Zusage und alle übrigen Größen auf dem Darlehen des Basisfalls bilden ab, wie eine Bank tatsächlich verfährt (Einschätzung). Dass das KfW-Darlehen im Stressfall auf dem Basiszins bleibt, ist durch das Merkblatt gedeckt: Der Zins richtet sich nach dem Tag der Zusage oder nach dem günstigeren Satz bei Antragseingang (Quellnotiz 13, `KFW-297-298-MERKBLATT`). Ein Satz mit diesem Beleg in R-11.8 würde die Frage eines Lesers vorwegnehmen.
- **KfW- und Förderdarlehen:** Rang, Bemessungszins, Kapitaldienst ohne Anlaufjahre, Vorfälligkeit und Anschluss zum Marktzins sind schlüssig. Dass das nachrangige Förderdarlehen in der Quote mitzählt, ist vorsichtig. Der Verzicht auf den Schalter dafür ist belegt: Im geförderten Fall bindet die Deckung.
- **Entfallene Eingaben auf der Finanzierungsseite:** V-03, V-05, V-06 (siehe Befund 3), V-07 und V-08 sind tragbar. Zu V-04 gibt es eine Anmerkung (Befund 6).

## Befunde

1. **[wichtig · Zahl belegt, Bankpraxis begründete Einschätzung] R-5.18, R-5.19 (Zins, Bereitstellungsprovision, Abruffrist), R-5.8 (NF-08) mit R-11.2 (Vorlauf E-23), R-5.11 (NF-65) und R-11.8: Beim Neubau mit Vorlauf gilt der Grundstückskauf als Tag der Kreditzusage. Bereitstellungszins, Fristen und Zinsbindung laufen deshalb schon im Vorlauf. Die Wirkung liegt über der Schwelle, und das Dokument widerspricht sich in dieser Frage.**
   - **Was die Regeln sagen:** Die bereitstellungsfreie Zeit zählt „ab dem Stichtag“ (R-5.18), ebenso die Provision, die Abruffrist und die Zinsbindung des KfW-Darlehens (R-5.19: „ab dem Stichtag, der für die Zusage steht“). Der Stichtag des Neubaus ist der Grundstückskauf (R-2.1), der Bau beginnt nach dem Vorlauf E-23.
   - **Widerspruch 1:** Für die NBank setzt dasselbe Dokument die Förderentscheidung auf den Monat vor dem Baubeginn (NF-65).
   - **Widerspruch 2:** Der Stressfall unterstellt einen Zinsanstieg *bis zur* Zusage (R-11.8). Das setzt eine Zusage nach dem Stichtag voraus. Beim Neubau mit Vorlauf rechnet der Kern also beides: Bereitstellung ab dem Grundstückskauf und Zinsrisiko bis zu einer späteren Zusage.
   - **Bankpraxis (Einschätzung):** Bei vorgeschaltetem Grundstückserwerb sagt eine Bank die Baufinanzierung erst zu, wenn Baugenehmigung und Kostenschätzung vorliegen, also kurz vor dem Baubeginn. Das Grundstück trägt nach „Eigenkapital zuerst“ ohnehin das Eigenkapital.
   - **Gegenrechnung** (RF-12 mit zwölf Monaten Vorlauf, Referenzrechner, eigener Lauf; verschoben ist nur die bereitstellungsfreie Zeit um den Vorlauf, also 18 statt 6 Monate ab dem Stichtag):

     | Größe | Zusage zum Stichtag (heute) | Zusage zum Baubeginn |
     |---|---|---|
     | Finanzierungskosten der Investitionsphase | 253.689,81 Euro | 133.475,49 Euro |
     | Rendite | 3,675 % | 3,804 % |
     | tragbarer Grundstückspreis | 202.494 Euro | 311.986 Euro |

     Der Unterschied beträgt 120.214 Euro oder 1,30 % der Gesamtkosten von 9.246.726,89 Euro und 0,129 Prozentpunkte Rendite. Das liegt über beiden Schwellen. Der tragbare Grundstückspreis steigt um 109.492 Euro oder 54 %.
   - **KfW-Darlehen:** Abruffrist und Provision zählen ebenfalls ab dem Stichtag. Bei mehr als zwölf Monaten Vorlauf liegt jeder Abruf nach der Frist, und M-49 kommt dann regelmäßig.
   - *Vorschlag:* Beim Neubau gilt als Tag der Zusage des Bankdarlehens und des KfW-Darlehens der Monat „Vorlauf“, wie bei der NBank (NF-65). Ab diesem Monat zählen die bereitstellungsfreie Zeit, die Fristen der KfW und die Zinsbindung; ohne Vorlauf ändert sich nichts. Wer das nicht als Regel will, führt es als Modellannahme mit der heutigen Fassung als anderer Lesart. Dann gehört in Frage 7 der Zusatz: „Wann sagen Sie bei vorgeschaltetem Grundstückskauf die Baufinanzierung zu, und ab wann laufen Bereitstellungszinsen?“ Die Verschiebung der Zinsbindung habe ich nicht gesondert gemessen; sie wirkt in dieselbe Richtung.

2. **[wichtig · Wirkung aus dem Prüfobjekt belegt, Verfügbarkeit begründete Einschätzung] R-11.3 (Zwischenfinanzierung der Teilraten), R-11.14, R-11.15 und Kapitel 16: Im geförderten Neubau setzt der Kern eine Zwischenfinanzierung von über einer Million Euro voraus. Sie soll von einer Bank kommen, die im selben Fall jedes Darlehen ablehnt (M-21). Kapitel 16 fragt nicht, ob es sie gibt.**
   - **Was der Kern rechnet:** Er lässt das Kontokorrent „über die Linie H-11 hinaus“ bis zur Höhe der Lücke zu. Die Linie H-11 ist mit null voreingestellt. Im Referenzfall gefördert erreicht die Zwischenfinanzierung 1.045.063,54 Euro, bei 42.095,30 Euro Zinsen. Das Bankdarlehen ist null, weil die Deckung 1,0495 beträgt.
   - **Was davon unter der Schwelle liegt:** Der Zins der Zwischenfinanzierung (GEF +0,011 Prozentpunkte). Die Durchsicht hat die Frage danach zu Recht gestrichen.
   - **Was nicht darunter liegt:** ob eine Bank sie überhaupt gibt.
     - Ohne Zwischenfinanzierung muss das Eigenkapital die Lücke tragen. Das Eigenkapital der Investitionsphase stiege von 2.144.688,71 Euro um bis zu 1,05 Mio. Euro, also um rund die Hälfte.
     - Nach NF-64 fiele die Rendite mit Einlage und Rückfluss um rund einen Prozentpunkt.
     - Die Eigenkapitalgrenze E-60 (R-11.6) prüft die Lücke nicht, weil sie keine Einlage ist.
   - **Bankpraxis (Einschätzung):** Eine Hausbank finanziert zugesagte Fördermittel häufig gegen Abtretung der Auszahlungsansprüche zwischen. Sie will dafür aber eine erstrangige Grundschuld und sieht den Kunden mit Deckung 1,05 kritisch. Selbstverständlich ist das nicht.
   - *Vorschlag:*
     - Frage 6 ergänzen: „Finanzieren Sie die Teilraten der NBank-Mittel zwischen, auch wenn Sie kein langfristiges Darlehen geben, bis zu welchem Betrag und gegen welche Sicherheit?“ Verantwortlich: Hausbank, dazu NBank (ob Abschläge früher ausgezahlt werden).
     - Bis zur Antwort als Modellannahme kennzeichnen: „Zwischenfinanzierung der Fördermittel durch die Hausbank verfügbar“, Gewicht mittel. Andere Lesart: Das Eigenkapital trägt die Lücke.
     - Auf dem Blatt erscheint der höchste Stand als „Zwischenfinanzierung durch die Bank nötig“ und nicht nur als Kennzahl. Eine neue Eingabe braucht es nicht.

3. **[wichtig · belegt] R-5.12, Beispiel unter der Tabelle zum Bemessungszins (Zeile 527), mit H-25 (Zeile 270), V-06 und V-07: Seit H-25 „ein Wert für alle Tranchen“ ist, stimmen ein Beispielwert und der Bedienhinweis für Lesart 2 nicht mehr, sobald ein übernommenes Darlehen im Fall ist.**
   - **Das falsche Beispiel:** „Mit einem festen kalkulatorischen Zins von 4 % für übernommene Darlehen (H-25) sind es bei acht Jahren 826.660,00 Euro.“ Der Wert setzt 4 % nur für das übernommene Darlehen und lässt das Bankdarlehen bei 5 %. Das ist der frühere Satz je Tranchenart, den V-07 abgeschafft hat. Mit H-25 = 4 % für alle Tranchen rechnet der Referenzrechner:
     - i_k = 4 % für das Bankdarlehen und i_B = 1,2 % für das übernommene Darlehen;
     - KD_Ü = 19.200,00 Euro;
     - B = (77.066,20 − 19.200,00) / 6 % = **964.436,66 Euro**, nicht 826.660,00 Euro (eigener Lauf).
   - **Der falsche Bedienhinweis:** V-06 und R-5.12 sagen, Lesart 2 (Vertragskonditionen) ergebe sich „mit einem festen Satz in Höhe des Vertragszinses“ auf den Cent. Das gilt nur, solange das Bankdarlehen die einzige Tranche mit kürzerer Bindung ist.
     - Mit übernommenem Darlehen (0,5 %, acht Jahre) ergibt H-25 = 4 % den Wert 964.436,66 Euro.
     - Lesart 2 ergibt 1.034.436,66 Euro. Diesen Wert liefert erst H-25 = 0 %, weil dann i_kalk = max(Vertragszins; 0) für jede Tranche der Vertragszins ist (eigener Lauf, deckungsgleich mit dem Text).
     - Wer dem Hinweis folgt, rechnet die „Vertragskonditionen“ um 70.000 Euro oder 6,8 % des Darlehens zu niedrig.
   - **Reste der Tranchensätze:** In der Formel steht „H-25 der Tranchenart“, in Anhang A.4 „H-25 bis H-28: kalkulatorischer Zins für jede Tranchenart“.
   - *Vorschlag:*
     - Beispiel auf 964.436,66 Euro berichtigen und als Probe in RF-11 aufnehmen.
     - V-06 und R-5.12 umformulieren: „Lesart 2 ergibt sich mit H-25 = 0 %, das heißt ohne Satz über dem Vertragszins; bei nur einem Darlehen auch mit einem Satz in Höhe seines Vertragszinses.“
     - In Formel und Anhang „H-25 (ein Wert, aufgelöst je Tranche)“ schreiben.

4. **[Hinweis · belegt] `MA-026` und `MA-034` (Verzeichnis der Modellannahmen) sind nach der Durchsicht nur in der Bemerkung nachgezogen. Annahme, andere Lesart und Wirkung widersprechen dem Prüfobjekt.**
   - In `MA-026` stehen noch:
     - unter „Annahme“ (1): „für ein übernommenes Darlehen ist der Rang Eingabe“. Die Eingabe ist entfallen (V-03; R-5.12: fest vor der Bank).
     - unter „Andere Lesart“: „Diese vier sind umschaltbar“. Umschaltbar sind nur noch 3 und 4 (R-5.12, eigene Bemerkung).
     - ebenda Lesart (6): „Beleihungswert unter dem Kaufpreis (Eingabe)“. E-61 ist entfallen.
     - unter „Klärung durch“: „kalkulatorischer Zins je Tranchenart“ (V-07).
   - `MA-034`, „Wirkung“: „im Stressfall 1,0181 gegen 0,8966“. Das ist der Stand vor der Neubemessung. R-10.14 nennt für denselben Fall 1,0439 und 0,9193.
   - Wer das Verzeichnis liest, baut eine Rang-Eingabe und zwei Schalter, die es nicht mehr gibt.
   - *Vorschlag:* Die vier Felder in `annahmen.toml` auf den Stand von R-5.12 und R-10.14 bringen, dann `python3 scripts/modellannahmen.py` ausführen.

5. **[Hinweis · belegt] Reststellen im Prüfobjekt, an denen ein Programmierer stolpert:**
   - Anhang A.4, Zeile „H-32 bis H-37“: „Betriebskosten leerstehender Flächen 0 Euro, in den bezeichneten Fällen 30 Euro je m² und Jahr“. H-36 ist entfallen (Zeile 281, V-15, NF-60).
   - Kapitel 16, „Was Teil 2 regelt“, Zeile KfW: „Bereitstellungsprovision“. Sie ist schon in Teil 1 geregelt (R-5.19, KAT-15).
   - R-5.12, Absatz zu `MA-026`, und R-5.19 führen „Lesart (1)“ und „Lesart (2)“ mit Zahlen weiter, obwohl sie keine Lesarten mehr sind. Das ist in Ordnung, solange es dort einmal heißt „früher Lesart, jetzt V-05 und V-06“, wie in Kapitel 17 Nr. 10 („früher Lesart 2“).
   - *Vorschlag:* Die Zeile in A.4 kürzen, die Zeile KfW in Kapitel 16 auf „Tilgungszuschuss, mehrere Programme“ beschränken und in R-5.12 und R-5.19 „(früher Lesart 1 / 2, V-05 / V-06)“ setzen.

6. **[Hinweis · begründete Einschätzung] V-04 (Wertansatz der Bank) ist in der günstigen Richtung gemessen. Die Begründung „H-02 bildet einen niedrigeren Beleihungswert ab“ gilt nur zum eingegebenen Preis.**
   - Die Durchsicht misst E-61 mit 2,6 Mio. Euro über dem Kaufpreis (+1,33 % bei Quote 45 %, über der Schwelle). Ein Wertansatz unter dem Kaufpreis, die bankübliche Richtung (Quellnotiz 13: Ertragswert als Obergrenze, `BELWERTV-4`), „endete mit einer Eingabemeldung und ist nicht ausgewertet“ (Durchsicht, Zeile 437).
   - Über H-02 = β x Beleihungswert / Kaufpreis lässt sich ein niedrigerer Wert zum Angebotspreis auf den Cent abbilden. In der Preissuche wächst A dann aber mit dem Preis, ein Beleihungswert nicht.
   - Das schadet nicht, solange die Deckung (b) bindet. Das tut sie in allen Referenzfällen am tragbaren Preis: Im Ankauf liegt der Knick bei 1.887.092 Euro unter P* = 2.317.235 Euro, im Neubau ist A = 5,86 Mio. Euro größer als B = 4,01 Mio. Euro. Eine Regel ist deshalb nicht nötig.
   - *Vorschlag:* V-04 richtig beschreiben: „gemessen nur oberhalb des Kaufpreises; einen niedrigeren Beleihungswert bildet H-02 = β x BW/KP zum Angebotspreis ab; in der Preissuche wirkt das nur, wenn die Quote bindet.“ Frage 2 schärfen, wie Quellnotiz 13 vorschlägt: „Mit welchem Abschlag auf den Kaufpreis oder auf den Ertragswert nach BelWertV rechnen Sie bei Wohnanlagen?“

**Fragen an die Hausbank (Prüfauftrag 4):** Die zehn Fragen sind die richtigen. Ein Firmenkundenbetreuer kann sie ohne Rückfrage beantworten; jede nennt die Voreinstellung, mit der bis zur Antwort gerechnet wird. Drei Ergänzungen:
- Frage 6 um die Zwischenfinanzierung der Fördermittel (Befund 2);
- Frage 7 um den Zeitpunkt der Zusage bei vorgeschaltetem Grundstückskauf (Befund 1);
- Frage 2 schärfer fassen (Befund 6).

Bei Frage 1 hat der Teil „ein übernommenes Darlehen“ keine Wirkung (V-03: keine Wirkung) und ist eine Frage des Grundbuchs, nicht der Bankpolitik. Er kann entfallen. Frage 3 bündelt zwei Fragen, das ist für ein Gespräch in Ordnung.

## Nicht geprüft

- Kapitel 6 bis 9, 12 bis 15 und die Steuer, außer wo sie Reinertrag, Kapitaldienst, Eigenkapital und Bemessung berühren.
- Die Verschiebung der Zinsbindung von Bank- und KfW-Darlehen bei Vorlauf (Befund 1) habe ich nicht gesondert gemessen, nur die bereitstellungsfreie Zeit.
- Bankpraxis lässt sich nicht an einer veröffentlichten Quelle prüfen. Zeitpunkt der Zusage bei Vorlauf, Bereitschaft zur Zwischenfinanzierung ohne Darlehen, Abstand des Beleihungswerts zum Kaufpreis und das Urteil „würde zugesagt“ sind meine Einschätzung aus der Rolle.
- Keine Quelle neu am Original gelesen. Abgeglichen habe ich `BELWERTV-3`, `-4`, `-11`, `-12` und `-16`, `BGB-489` und `BGB-490` sowie `KFW-297-298-MERKBLATT` (Kataster: am Original gelesen am 17. und 18.11.2026). Der KfW-Zins bleibt Katasterlücke (`KFW-KONDITIONENANZEIGER`, nicht geprüft). Die Aussage „Zins am Tag der Zusage oder günstiger bei Antragseingang“ habe ich aus Quellnotiz 13 übernommen, nicht selbst am Merkblatt gelesen.
- Rust-Code gibt es noch nicht.
- Eigene Läufe unter `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs3-bank/` (`b1.py`: H-25 im gebundenen Bestand; `b2.py` und `b3.py`: Vorlauf und bereitstellungsfreie Zeit). Sie werden mit dem Ordner des Referenzrechners als Argument aufgerufen, benutzen dessen Module unverändert und ändern nur Eingaben und Vorgaben.
