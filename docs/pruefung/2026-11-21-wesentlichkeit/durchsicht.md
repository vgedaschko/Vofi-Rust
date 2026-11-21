# Durchsicht an der Wesentlichkeitsschwelle – Rechenkern, Teil 1 (2026-11-21)

Gegenstand: jede Eingabe, jede Vorgabe des Hauses, jeder Schalter einer Modellannahme, die Steuerregeln des Kapitels 7 und die Rechenregeln aus Sonderfällen der Prüfrunden in `docs/fachspezifikation-rechenkern.md` (Stand nach dem teilweise eingearbeiteten Nachtrag 2; 20 Referenzfälle, 1.156 Prüfungen). Maßstab: Spezifikation, Zeile „Wesentlichkeit und Eingabensparsamkeit“ – tragbarer Preis über etwa 1 % oder VOFI-Rendite über 0,1 Prozentpunkte im typischen Fall. Dieser Schritt misst und schlägt vor; an Regeln, Voreinstellungen und Sollwerten ist nichts geändert. Leser: Koordination und Entwicklung, vor der Entscheidung über den Nachtrag 2.

## Ergebnis

| Gruppe | geprüft | über der Schwelle | Grenzfall | unter der Schwelle | ohne Rechenwirkung | Vorschlag |
|---|---|---|---|---|---|---|
| Eingaben mit Voreinstellung, freiwillig oder im Einzelfall | 55 | 27 | 18 | 8 | 2 | 43 Felder bleiben, 12 entfallen |
| Pflichteingaben ohne Voreinstellung | 21 | nicht an der Schwelle gemessen | | | | alle 21 bleiben; der Bodenanteil E-12 wird nur noch bei steuerfreiem Verkauf abgefragt |
| Vorgaben des Hauses (Einzelwerte, ohne Suchparameter H-21) | 57 | 24 | 15 | 16 | 2 | 27 bleiben im Vorhaben änderbar, 14 werden feste Hauswerte, 9 feste Katalogwerte, 7 entfallen |
| Schalter der Modellannahmen (Schalterstellungen) | 13 | 4 | 5 | 4 | 0 | 5 bleiben als Lesart des Hauses, 8 entfallen |
| Steuerregeln des Kapitels 7 und R-6.16 | 19 | 8 | 4 | 7 | 0 | alle Regeln bleiben bis auf R-7.6; es entfallen zwei Felder (E-44, E-52) und vier Schalterstellungen |
| Rechenregeln aus Sonderfällen der Prüfrunden | 17 | 4 | 7 | 5 | 1 | 13 bleiben, 4 werden benannte Vereinfachungen |

„Grenzfall“ heißt: knapp an der Schwelle (15 Gegenstände) oder im Referenzfall darunter, in einem benannten besonderen Fall aber deutlich darüber (25); beide Listen stehen im Abschnitt „Grenzfälle“. Steuer und Sonderfälle überschneiden sich mit den Zeilen darüber (ein Feld wie E-44 steht auch bei seiner Regel); die Zeilen sind deshalb nicht zu addieren.

- **Die Hauptannahmen tragen das Ergebnis.** Ein halber Euro Miete, ein Faktorpunkt, ein halber Prozentpunkt Zins bewegen den tragbaren Preis um 2 bis 5 % und die Rendite um 0,2 bis 0,7 Prozentpunkte (Abschnitt „Maßstab“). Daran gemessen liegen 8 der 55 Eingaben mit Voreinstellung, 16 der 57 Vorgabewerte und 4 der 13 Schalterstellungen unter der Schwelle.
- **Lesart der Schwelle im Neubau – bitte bestätigen:** Der tragbare Grundstückspreis ist ein Rest von einem Zwölftel der Gesamtkosten. Gemessen ist deshalb an der Rendite und an 1 % der Gesamtkosten; am Grundstückspreis gemessen bestünde fast alles die Schwelle. Beide Zahlen stehen in jeder Zeile.
- **Neuer Vorschlagstyp „fester Wert im Katalog des Hauses“:** Er ändert R-3.2, wonach jede Vorgabe außer H-20 und H-21 im Vorhaben änderbar ist. Das ist Teil des Vorschlags und mit ihm zu entscheiden.
- **Pflichteingaben:** Im Ankauf bleiben 12 Felder zu tippen (bisher 13), im Neubau 14 (wie bisher); mit den vorbelegten Feldern sind es 19 statt 21 und 21 statt 23. Im gebundenen Bestand sinkt die Maske von 39 auf 31 Felder, beim Ankauf mit Investitionsstau von 27 auf 21, im geförderten Neubau von 27 auf 24.
- **Freigabeblatt:** 41 Werte statt 57 – 27 wie bisher im Vorhaben änderbar, 14 als feste Werte im Katalog des Hauses. 9 weitere Werte werden feste Katalogwerte ohne Freigabeentscheidung, 7 entfallen.
- **Schalter:** Von 13 Schalterstellungen bestehen 4 die Schwelle im Referenzfall; zwei davon und eine weitere sind auf den Euro oder bis auf 0,03 Prozentpunkte deckungsgleich mit einer Eingabe oder Vorgabe, die es ohnehin gibt (`MA-026` Lesart 2 mit H-25, `MA-030` mit E-69, `MA-039` mit E-05). Es bleiben 5 Lesarten, alle nur noch auf der Ebene des Hauses.
- **Steuer:** Die Lehrbuchform trifft die Körperschaft ohne Kennzeichen auf den Euro. Was die Rechnung des Kapitels 7 von ihr unterscheidet, steckt in vier Dingen: Steuerstatus, erweiterte Kürzung samt Verkaufsjahr, Anteil natürlicher Personen und steuerfreier Verkauf nach der Frist.
- **Sonderfälle der Prüfrunden:** Bereitstellungsprovision des KfW-Darlehens, Betriebskosten leerstehender Flächen, hälftige CO2-Teilung, Aufschub der Fördertilgung und der Stress auf die Instandhaltung liegen unter der Schwelle und kosten Felder oder Katalogwerte; sie werden benannte Vereinfachungen. Vorfälligkeit, Bereitstellungszins, Kappungsgrenze, Übermiete und die CO2-Kosten sind Grenzfälle und bleiben, zum Teil schlanker.

## Vorgehen und Lesehilfe

Gemessen hat `wesentlichkeit.py` im Referenzrechner: Je Gegenstand ist eine Größe gegenüber dem Basisfall verändert; ausgegeben wird die Wirkung auf den höchsten tragbaren Preis und auf die VOFI-Rendite nach Steuern beim eingegebenen Preis. Die Spanne der Variation steht in der Spalte „Worum es geht“; sie ist so gewählt, wie die Größe zwischen zwei gewöhnlichen Vorhaben schwankt, bei Schaltern ist es die andere Lesart, bei Regeln das Weglassen.

| Fall | Kürzel | tragbarer Preis im Basisfall | Rendite beim eingegebenen Preis | Bezug der Preiswirkung |
|---|---|---|---|---|
| Ankauf Bestand (Referenzobjekt, 1.320 m², 20 Einheiten) | AN | 2.317.235 Euro Kaufpreis | 4,527 % | Kaufpreis |
| Neubau frei finanziert | NB | 702.767 Euro Grundstückspreis | 4,332 % | Gesamtkosten 8.478.141 Euro; daneben der Grundstückspreis |
| Neubau mit KfW-Darlehen 3 Mio. Euro | KfW | 1.197.094 Euro Grundstückspreis | 4,995 % | Gesamtkosten 9.012.014 Euro; daneben der Grundstückspreis |
| geförderter Neubau, 38 Jahre Haltedauer | GEF | keiner bei 5 % Zielrendite | 3,956 % | nur Rendite gemessen |

- **Schreibweise der Wirkung:** „AN +2,80 % / +0,371 PP“ heißt: tragbarer Preis im Ankauf +2,80 %, Rendite +0,371 Prozentpunkte. Im Neubau steht zuerst die Preiswirkung in Prozent der Gesamtkosten, in Klammern in Prozent des Grundstückspreises.
- **Schwelle im Neubau:** Der tragbare Grundstückspreis ist ein Rest von rund einem Zwölftel der Gesamtkosten; 1 % von ihm sind 0,08 % der Investition. Am Grundstückspreis gemessen bestünde fast jede Größe die Schwelle (166 statt 140 von 278 Messungen). Das Urteil folgt deshalb im Neubau der Rendite und der Preiswirkung in Prozent der Gesamtkosten; beide Zahlen stehen in der Tabelle, damit die andere Lesart der Schwelle nachvollziehbar bleibt.
- **Geförderter Neubau:** Bei 5 % Zielrendite gibt es keinen tragbaren Preis, und die Preissuche über 38 Jahre ist teuer; gemessen ist nur die Rendite.
- **Stressgrößen:** Jede ist einzeln aus dem kombinierten Stressfall genommen; die Wirkung bezieht sich auf Preis und Rendite des Stressfalls. Im Neubau gibt es im Stressfall keinen tragbaren Preis, dort steht nur die Rendite.
- **Proben:** Wo eine Größe im Referenzfall wenig bewegt, im erkennbaren Sonderfall aber viel, ist dieser Fall eigens gemessen (kursiv vorangestellt). Am häufigsten: die Ist-Miete 24 % unter der Vergleichsmiete (7,00 gegen 9,20 Euro) statt 8 % wie im Referenzobjekt.
- **Preissuche:** grobes Raster (10 Stützstellen, Nachsuche 2 Euro); für Prozentwerte genügt das. Die Fälle rechnen mit den angenommenen Vorgaben und dem angenommenen Katalogstand der Referenzfälle.

Die Vorschläge:

- **behalten** – bleibt, wie es ist.
- **fester Wert im Katalog des Hauses** – das Haus gibt den Wert einmal frei; im Vorhaben ist er nicht änderbar und steht nicht in der Liste der Abweichungen.
- **fester Katalogwert** – Wert mit Quelle im Katalog, ohne Freigabeentscheidung der Geschäftsführung und ohne Feld.
- **Lesart des Hauses** – die andere Lesart bleibt im Katalog wählbar, im Vorhaben nicht.
- **vereinfachen** – wie, steht im Halbsatz.
- **als Vereinfachung benennen** – Regel, Feld oder Schalter entfällt; der Satz in Anführungszeichen ist der Wortlaut für die Fachspezifikation.

Regeln, die gebaut sind, bestehen und weder Feld noch Vorgabe noch Schalter kosten, bleiben im Zweifel.

## Maßstab: die Hauptannahmen

| Kennung | Eingabe (Variation) | Wirkung: Preis / Rendite |
|---|---|---|
| E-15 | Ist-Miete (8,50 → 8,00 Euro) | AN −2,06 % / −0,236 PP |
| E-19 | Vergleichsmiete (9,20 → 8,70 Euro) | AN −4,79 % / −0,674 PP |
| E-45 | Zins des Bankdarlehens (4 % → 4,5 %) | AN −2,10 % / −0,248 PP<br>NB −1,99 % (Grundstück −24,06 %) / −0,195 PP |
| E-47 | Verkaufsfaktor (Ankauf 18 → 17; Neubau 24 → 22) | AN −3,37 % / −0,469 PP<br>NB −4,38 % (Grundstück −52,84 %) / −0,541 PP |
| E-16 | Miete bei Bezug im Neubau (16,50 → 15,50 Euro) | NB −5,71 % (Grundstück −68,89 %) / −0,650 PP |
| E-25 | Kostenkennwert (2.320 → 2.450 Euro je m²) | NB −4,67 % (Grundstück −56,28 %) / −0,475 PP |

## a) Eingaben

### Pflichteingaben ohne Voreinstellung

Nicht an der Schwelle gemessen, weil die Rechnung ohne sie nicht läuft; wo eine Messung steht, dient sie als Maßstab.

| Kennung | Eingabe | Fall | Bemerkung |
|---|---|---|---|
| E-01 | Vorhabensart | beide |  |
| E-03 | Land | beide | Schlüssel der Katalogwerte |
| E-04 | Gemeinde | beide | Schlüssel der Katalogwerte (Hebesatz, Gebietsverordnungen) |
| E-10 | Kaufpreis | Ankauf | für die Rendite beim eingegebenen Preis; die Preissuche ersetzt ihn |
| E-13 | Wohnfläche | beide |  |
| E-14 | Zahl der Einheiten | beide | Verwaltungskosten, Höchstbetrag des KfW-Darlehens |
| E-15 | Ist-Miete | Ankauf | Maßstab (8,50 → 8,00 Euro): AN −2,06 % / −0,236 PP |
| E-17 | Baujahr | Ankauf | Maßstab (1990 → 2008): AN +2,02 % / +0,259 PP |
| E-19 | Vergleichsmiete | Ankauf | Maßstab (9,20 → 8,70 Euro): AN −4,79 % / −0,674 PP |
| E-20 | Grundstückspreis | Neubau | für die Rendite beim eingegebenen Preis; die Preissuche ersetzt ihn |
| E-21 | Grundstücksfläche | Neubau | geht im frei finanzierten Neubau nur in die Kennzahl „Preis je m² Grundstück“ ein, im geförderten in die Bemessung der Förderung |
| E-22 | Brutto-Grundfläche | Neubau |  |
| E-25 | Kostenkennwert | Neubau | Maßstab (2.320 → 2.450 Euro je m²): NB −4,67 % (Grundstück −56,28 %) / −0,475 PP |
| E-26 | Bauzeit | Neubau | Maßstab (18 → 24 Monate): NB −2,13 % (Grundstück −25,72 %) / −0,237 PP |
| E-16 | Miete bei Bezug | Neubau | Maßstab (16,50 → 15,50 Euro): NB −5,71 % (Grundstück −68,89 %) / −0,650 PP |
| E-28 | Mietenstufe | geförderter Neubau |  |
| E-29 | Einkommensgruppe | geförderter Neubau |  |
| E-30 | Bodenrichtwert | geförderter Neubau | im Ankauf nur zur Vorbelegung von E-12 |
| E-40 | Steuerstatus | beide | Maßstab (Körperschaft → Privatperson; → gewerbliche Personengesellschaft): AN +4,56 % / +0,614 PP; AN −7,45 % / −0,878 PP |
| E-45 | Zins des Bankdarlehens | beide | Maßstab (4 % → 4,5 %): AN −2,10 % / −0,248 PP; NB −1,99 % (Grundstück −24,06 %) / −0,195 PP |
| E-47 | Verkaufsfaktor | beide | Maßstab (Ankauf 18 → 17; Neubau 24 → 22): AN −3,37 % / −0,469 PP; NB −4,38 % (Grundstück −52,84 %) / −0,541 PP |

Alle 21 bleiben. E-21 rechnet im frei finanzierten Neubau nicht in Preis und Rendite; sie bleibt, weil der Preis je Quadratmeter Grundstück die Zahl ist, an der ein Grundstücksgebot geprüft wird.

### Eingaben mit Voreinstellung, freiwillige Eingaben und Eingaben im Einzelfall

| Kennung | Worum es geht (Variation) | Wirkung: Preis / Rendite | kostet | Urteil | Vorschlag |
|---|---|---|---|---|---|
| E-02 | Stichtag (2027 → 2029) | AN +0,02 % / +0,002 PP<br>NB +0,01 % (Grundstück +0,11 %) / +0,001 PP<br>KfW +0,01 % (Grundstück +0,04 %) / +0,001 PP | Feld, vorbelegt | unter | **behalten** – trägt den Kalender der Rechnung (Katalogstand je Jahr, Fristen, Gebäudealter); vorbelegt, kein Tippaufwand |
| E-05 | Lage im Gebiet der abgesenkten Kappungsgrenze (15 % → 20 %) | AN +0,09 % / +0,012 PP<br>*Ist-Miete 24 % unter der Vergleichsmiete:* AN +6,61 % / +0,737 PP<br>NB ±0,00 % (Grundstück ±0,00 %) / ±0,000 PP | Feld, aus KAT-08 vorbelegt | Grenzfall: groß nur bei großer Mietlücke | **vereinfachen** – im Ankauf als vorbelegtes Kennzeichen behalten; im Neubau entfällt das Feld, dort gilt der Katalogwert der Gemeinde |
| E-05 | Lage im Gebiet der Mietpreisbremse (im Gebiet → außerhalb) | *200 m² leer:* AN −0,04 % / −0,006 PP<br>*600 m² leer, Marktmiete 13,00 Euro:* AN +8,67 % / +1,043 PP | Feld, aus KAT-08 vorbelegt | Grenzfall: groß nur mit leerer Fläche und hoher Marktmiete | **behalten** als vorbelegtes Kennzeichen – wirkt nur mit leerer Fläche oder Fluktuation, dann stark |
| E-11 | Erwerbsnebenkosten (Ankauf 10 % → 7 %; Neubau 8 % → 6,5 %) | AN +2,80 % / +0,371 PP<br>NB +0,12 % (Grundstück +1,41 %) / +0,021 PP | Feld, aus KAT-01 vorbelegt | über | **behalten** – im Neubau klein, weil nur das Grundstück betroffen ist |
| E-12 | Bodenanteil (25 % → 35 %; Probe 25 % → 50 %) | *Körperschaft:* AN −0,06 % / −0,008 PP<br>*Körperschaft, 50 %:* AN −0,16 % / −0,021 PP<br>*Privatperson:* AN −0,66 % / −0,097 PP<br>*Privatperson, 50 %:* AN −1,63 % / −0,244 PP | Pflichtfeld | Grenzfall: über der Schwelle nur bei steuerfreiem Verkauf | **vereinfachen** – Feld nur, wo der Verkauf nach der Frist steuerfrei bleibt (Privatperson, Verein und Stiftung); sonst fester Hauswert ohne Feld, weil sich Abschreibung und Verkaufsgewinn ausgleichen |
| E-16 | Marktmiete im Ankauf (10,50 → 9,50 Euro) | AN ±0,00 % / ±0,000 PP<br>*600 m² leer:* AN −1,05 % / −0,130 PP | Feld, nur mit E-31 oder H-26 | Grenzfall: wirkt nur mit leerer Fläche oder Fluktuation | **behalten** als bedingtes Feld – erscheint nur mit leerer Fläche oder Fluktuation |
| E-18 | Angebotspreis (2,6 → 2,8 Mio. Euro) | AN ±0,00 % / ±0,000 PP | freiwilliges Feld | ohne Rechenwirkung | **behalten** – reine Vergleichsgröße (Abstand zum Angebot); keine Regel hängt daran |
| E-23 | Vorlauf bis zum Baubeginn (0 → 12 Monate) | NB −5,90 % (Grundstück −71,19 %) / −0,657 PP | Feld, aus H-35 vorbelegt | über | **behalten** |
| E-24 | Festpreis des Bauvertrags (nein → ja) | NB +1,93 % (Grundstück +23,23 %) / +0,210 PP | freiwilliges Kennzeichen | über | **behalten** |
| E-25 | Auswahl, wofür der Kostenkennwert gilt (Kostengruppen 300 und 400 mit Zuschlägen ↔ 200 bis 700 gesamt, gleichwertige Werte) | NB ±0,00 % (Grundstück ±0,00 %) / ±0,000 PP | Auswahlfeld | ohne Rechenwirkung | **behalten** – Eingabehilfe, kein zusätzlicher Parameter: Wer ein Gesamtangebot hat, muss die Zuschläge nicht herausrechnen |
| E-27 | Stellplätze im Neubau (0 → 20 zu 60 Euro Miete) | NB −0,94 % (Grundstück −11,38 %) / −0,073 PP<br>*dazu Herstellungskosten je Platz 30.000 statt 20.000 Euro:* NB −2,13 % (Grundstück −30,06 %) / −0,219 PP | freiwilliges Feld (Anzahl, Miete) | Grenzfall: knapp unter der Schwelle | **behalten** (freiwillig) – knapp unter der Schwelle, solange Miete und Kosten je Platz nahe beieinanderliegen; mit Tiefgaragenkosten klar darüber |
| E-31 | leerstehende Fläche am Stichtag (0 → 200 m² und 0 → 600 m² von 1.320 m²) | AN −0,17 % / −0,010 PP<br>AN −0,51 % / −0,030 PP<br>*600 m², Vermietung nach 12 statt 3 Monaten:* AN −7,34 % / −0,552 PP | Feld | Grenzfall: groß nur bei langer Vermarktung | **behalten** – im Referenzfall klein, weil die Fläche nach drei Monaten zur Marktmiete vermietet ist; bei längerer Vermarktung weit über der Schwelle |
| E-32 | sonstige Erträge (0 → 6.000 Euro im Jahr) | AN +4,93 % / +0,655 PP | Feld | über | **behalten** |
| E-33 | Mietenhistorie (ohne Angabe → letzte Erhöhung vor 6 Monaten) | AN +0,01 % / +0,001 PP<br>*Ist-Miete 24 % unter der Vergleichsmiete:* AN +6,53 % / +0,724 PP | freiwilliges Feld (zwei Werte) | Grenzfall: groß nur bei großer Mietlücke | **behalten** (freiwillig) – ersetzt bei bekannter Historie die vorsichtige Annahme `MA-037`; bei großer Mietlücke trägt sie das Ergebnis |
| E-34 | CO2-Ausstoß des Gebäudes (30 → 45 kg je m²; Probe → 60 kg) | AN −0,18 % / −0,023 PP<br>*60 kg je m²:* AN −0,37 % / −0,047 PP | Feld | Grenzfall: über der Schwelle erst bei hohem Ausstoß und doppeltem CO2-Preis | **vereinfachen** – als einziges, freiwilliges Feld der CO2-Rechnung behalten; ohne Angabe rechnet der Kern keinen Vermieteranteil (siehe R-6.9) |
| E-54, E-55 | Effizienzklasse und Energieträger: Näherung des CO2-Ausstoßes (`MA-035`) | *wie E-34:* AN −0,18 % / −0,023 PP | zwei Pflichtfelder, wenn E-34 fehlt | unter | **als Vereinfachung benennen** – „Den CO2-Ausstoß nähert die Grobkalkulation nicht aus Effizienzklasse und Energieträger; ohne Angabe des Ausstoßes rechnet sie keinen Vermieteranteil an den CO2-Kosten.“ |
| E-35 | KfW-Darlehen (0 → 3 Mio. Euro) | NB +5,83 % (Grundstück +70,34 %) / +0,664 PP | Feld | über | **behalten** |
| E-36 | KfW-Laufzeitvariante (35 Jahre, 1 Freijahr → 10/2 und 25/3) | KfW −4,65 % (Grundstück −34,98 %) / −0,471 PP<br>KfW −1,50 % (Grundstück −11,27 %) / −0,195 PP | Auswahlfeld | über | **behalten** |
| E-37 | KfW mit Qualitätssiegel (Darlehen 3,0 → 4,5 Mio. Euro) | KfW +2,67 % (Grundstück +20,13 %) / +0,436 PP | Kennzeichen | über | **behalten** |
| E-38 | Zins des KfW-Darlehens (2,5 % → 3,0 %) | KfW −1,34 % (Grundstück −10,09 %) / −0,189 PP | Feld, aus KAT-15 vorbelegt | über | **behalten** |
| E-39 | Vorvermietung: kein Anlaufleerstand (nein → ja) | NB +1,02 % (Grundstück +12,29 %) / +0,113 PP | freiwilliges Kennzeichen | Grenzfall: knapp über der Schwelle | **behalten** – knapp über der Schwelle |
| E-41 | Kennzeichen erweiterte Kürzung (nein → ja) | AN +1,11 % / +0,143 PP<br>NB −0,06 % (Grundstück −0,76 %) / −0,008 PP | Kennzeichen | über | **behalten** – trägt im Ankauf; im Neubau erst zusammen mit E-69 |
| E-42 | Steuersatz der Personen (42 % → 35 %) | *Personengesellschaft:* AN +3,48 % / +0,363 PP<br>*Privatperson:* AN +0,53 % / +0,080 PP | Feld, aus H-22 vorbelegt | über | **behalten** |
| E-43 | Anteil natürlicher Personen am Gewinn (100 % → 60 %) | AN −2,66 % / −0,259 PP | Feld, mit 100 % vorbelegt | über | **behalten** |
| E-44 | Verlustverrechnung: Vortrag im Vorhaben → sofort (`MA-016`) | *Körperschaft:* AN +0,03 % / −0,004 PP<br>*Körperschaft:* NB −0,26 % (Grundstück −3,11 %) / −0,033 PP<br>*Körperschaft:* GEF +0,010 PP<br>*Privatperson:* AN +0,66 % / +0,103 PP<br>*Privatperson:* GEF +0,082 PP<br>*Privatperson:* NB +0,21 % (Grundstück +1,39 %) / +0,029 PP<br>*Personengesellschaft:* AN +0,93 % / +0,075 PP | Pflichtfeld, vorbelegt | Grenzfall: knapp über der Schwelle nur bei der Privatperson im Ankauf | **vereinfachen** – Feld entfällt, fest „Vortrag im Vorhaben“; benannt: „Verluste trägt der Kern im Vorhaben vor; eine Verrechnung mit anderen Einkünften des Investors ist nicht abgebildet und hebt die Rendite bei Privatpersonen um rund 0,1 Prozentpunkte.“ |
| E-46 | Zinsbindung (10 → 5 und 10 → 15 Jahre) | AN −1,14 % / −0,156 PP<br>NB −0,94 % (Grundstück −11,32 %) / −0,113 PP<br>AN +0,37 % / +0,050 PP<br>NB +0,77 % (Grundstück +9,26 %) / +0,091 PP | Feld, aus H-24 vorbelegt | über | **behalten** |
| E-48 | Haltedauer (Ankauf 12 → 10 und 15; Neubau 15 → 20 Jahre) | AN −0,37 % / −0,144 PP<br>AN +0,22 % / +0,111 PP<br>NB −1,04 % (Grundstück −12,56 %) / +0,054 PP | Feld, aus H-19 vorbelegt | über | **behalten** |
| E-50 | Investitionsstau: Betrag (120.000 → 240.000 Euro) | AN −4,80 % / −0,582 PP | Feld | über | **behalten** |
| E-51 | Investitionsstau: Jahr der Ausführung (Jahr 2 → Jahr 5) | AN +0,91 % / +0,105 PP | Feld, vorbelegt | Grenzfall: knapp über der Schwelle | **behalten** – knapp über der Schwelle, wächst mit dem Betrag |
| E-52 | Investitionsstau: Erhaltung oder Modernisierung | AN −0,22 % / −0,028 PP<br>*400.000 Euro Erhaltung sofort abziehbar statt aktiviert:* AN +0,37 % / +0,029 PP | Feld, vorbelegt | unter | **als Vereinfachung benennen** – Feld entfällt: „Den Investitionsstau behandelt der Kern steuerlich als Erhaltungsaufwand, oberhalb der Grenze KAT-12 als anschaffungsnahe Herstellungskosten; eine Modernisierung mit eigener Abschreibung rechnet erst die Vollkalkulation.“ |
| E-53 | Anpassungsdauer der Ist-Miete an die Vergleichsmiete (4 → 1 Jahr) | AN +0,13 % / +0,018 PP<br>*Ist-Miete 24 % unter der Vergleichsmiete:* AN ±0,00 % / ±0,000 PP | Feld, aus H-23 vorbelegt | unter | **vereinfachen** – Feld entfällt, es gilt der feste Wert H-23; den Mietpfad bestimmen Wartefrist und Kappungsgrenze |
| E-56 bis E-58 | gebundener Bestand: Anteil, Bindungsende, gebundene Miete (0 → 40 % bis Jahr 6 zu 6,80 Euro) | AN −8,87 % / −1,134 PP<br>*Bindungsende Jahr 6 → 10:* AN −2,04 % / −0,266 PP<br>*gebundene Miete 6,80 → 7,50 Euro:* AN +4,17 % / +0,481 PP | drei Felder, nur im gebundenen Bestand | über | **behalten** |
| E-59 | übernommenes Darlehen: Restschuld, Zins, Tilgungssatz, Ende der Zinsbindung | *keines → 500.000 Euro zu 0,5 %:* AN +5,73 % / +0,800 PP<br>*Ende der Zinsbindung 8 → 3 Jahre:* AN −2,00 % / −0,321 PP | vier Felder, nur mit übernommenem Darlehen | über | **behalten** |
| E-59 | übernommenes Darlehen: Anschlusszins (3 % → 5 %) | AN −0,86 % / −0,141 PP | Feld, vorbelegt | über | **behalten** |
| E-59 | übernommenes Darlehen: laufender Beitrag (0 → 0,5 %) | AN −0,87 % / −0,143 PP | Feld, mit 0 vorbelegt | über | **behalten** |
| E-59 | übernommenes Darlehen: ursprünglicher Nennbetrag als Bezug der Rate (600.000 → 500.000 Euro) | AN +0,44 % / +0,083 PP | Feld, mit der Restschuld vorbelegt | Grenzfall: knapp unter der Schwelle | **behalten** – bestimmt die Rate; die Wirkung wächst mit dem Tilgungsstand des Darlehens |
| E-59 | übernommenes Darlehen: Kennzeichen Förderdarlehen (erspart die Vorfälligkeit) | *Verkauf nach 5 Jahren, vor dem Bindungsende:* AN +0,40 % / +0,141 PP | Kennzeichen, braucht eine Begründung | Grenzfall: wirkt nur bei Verkauf vor dem Bindungsende | **vereinfachen** – Feld entfällt; übernommene Darlehen rechnen beim Verkauf vor dem Bindungsende immer mit der Vorfälligkeit nach H-18 (vorsichtig) |
| E-59 | übernommenes Darlehen: Rang vor oder nach der Bank | AN ±0,00 % / ±0,000 PP | Auswahlfeld | unter | **vereinfachen** – Feld entfällt, fest „vor der Bank“ (vorsichtig) |
| E-60 | verfügbares Eigenkapital als zweite Preisgrenze (leer → 1,2 Mio. Euro) | AN −7,70 % / ±0,000 PP | freiwilliges Feld | über | **behalten** |
| E-61 | Wertansatz der Bank (Kaufpreis → 2,6 Mio. Euro) | *bei Beleihungsquote 45 %:* AN +1,33 % / +0,074 PP | freiwilliges Feld, braucht eine Begründung | Grenzfall: wirkt nur, wenn die Beleihungsquote bindet | **vereinfachen** – Feld entfällt: Wertansatz ist der Kaufpreis, im Neubau die Gesamtkosten; einen niedrigeren Beleihungswert bildet die Beleihungsquote H-02 ab |
| E-62 | Erbbauzins (0 → 12.000 Euro im Jahr) | AN −10,03 % / −1,277 PP | Feld im Einzelfall | über | **behalten** |
| E-63 | Steigerung des Erbbauzinses (2 % → 3 %) | AN −0,85 % / −0,109 PP | Feld, aus H-13 vorbelegt | Grenzfall: knapp über der Schwelle | **vereinfachen** – Feld entfällt; der Erbbauzins steigt mit der Kostensteigerung H-13 |
| E-64 | Tilgungssatz des Bankdarlehens (2 % → 3 %) | AN −1,28 % / −0,110 PP<br>NB −1,17 % (Grundstück −14,12 %) / −0,069 PP | Feld, aus H-04 vorbelegt | über | **behalten** |
| E-65 | nachhaltige Miete der Bank im Neubau (16,50 → 15,00 Euro) | NB −1,13 % (Grundstück −13,63 %) / −0,084 PP | freiwilliges Feld | Grenzfall: knapp an der Schwelle | **behalten** (freiwillig) – knapp an der Schwelle |
| E-66 | Heizung mit hälftiger Teilung der CO2-Kosten (nein → ja) | AN −0,06 % / −0,009 PP<br>*Regel weglassen:* AN +0,06 % / +0,009 PP | Kennzeichen | unter | **als Vereinfachung benennen** – „Die hälftige Teilung der CO2-Kosten nach `CO2KOSTAUFG-5A` und weitere Kosten des Vermieters daraus bildet die Grobkalkulation nicht ab; die Teilung bewegt den tragbaren Preis im Referenzfall um weniger als 0,1 %.“ |
| E-67 | weitere Kosten des Vermieters aus dieser Teilung (0 → 2.000 Euro im Jahr) | AN −0,83 % / −0,103 PP | Feld, nur mit E-66 | Grenzfall: knapp an der Schwelle | **als Vereinfachung benennen**, mit E-66 – eine freie Kostenzeile; ihre Wirkung ist die jeder Kostenposition dieser Höhe |
| E-68 | bewilligter Aufschub des Tilgungsbeginns des Förderdarlehens (0 → 60 Monate, der Höchstwert) | GEF +0,058 PP | Feld, mit 0 vorbelegt | unter | **als Vereinfachung benennen** – „Einen bewilligten Aufschub des Tilgungsbeginns des Förderdarlehens bildet die Grobkalkulation nicht ab; auch der längste Aufschub hebt die Rendite im Referenzfall um weniger als 0,06 Prozentpunkte.“ |
| E-69 | erweiterte Kürzung bleibt im Verkaufsjahr erhalten (nein → ja, mit Kennzeichen E-41) | AN +3,57 % / +0,490 PP<br>NB +4,98 % (Grundstück +60,47 %) / +0,563 PP | Kennzeichen im Einzelfall | über | **behalten** – entscheidet, ob der Verkaufsgewinn Gewerbesteuer trägt |
| E-70 | Verteilung des Zuschusses über die Bindung beantragt (Privatperson, Verein, Stiftung) | GEF +0,572 PP | Kennzeichen, erscheint nur bei diesen Status mit Zuschuss | Grenzfall: groß, aber nur für Privatperson, Verein und Stiftung im geförderten Neubau | **behalten** als bedingtes Feld |

Von 55 Eingabewerten bestehen 27 die Schwelle im Referenzfall, 18 sind Grenzfälle, 8 liegen darunter, 2 rechnen nicht mit. Nach den Vorschlägen entfallen 12 Felder: E-44, E-52, E-53, E-54, E-55, in E-59 das Kennzeichen Förderdarlehen und der Rang, E-61, E-63, E-66, E-67 und E-68. E-05 (Kappungsgrenze) wird im Neubau nicht mehr gezeigt, E-12 nur noch bei steuerfreiem Verkauf, E-34 wird freiwillig.

### Felder der Maske je Fall

Gezählt wie in R-3.6: Pflichtfelder der Maske ohne freiwillige Eingaben und Eingaben im Einzelfall; in Klammern die Felder, die der Bearbeiter tippen muss, weil sie keine Voreinstellung haben.

| Fall | bisher | nach den Vorschlägen | was entfällt |
|---|---|---|---|
| Ankauf | 21 (13) | 19 (12) | E-44; E-12 außer bei steuerfreiem Verkauf (dann 20 und 13) |
| Ankauf mit leerer Fläche | 23 (15) | 21 (14) | wie Ankauf |
| Ankauf mit Investitionsstau | 27 (16) | 21 (13) | dazu E-52, E-53, E-54, E-55; es bleiben E-50 und E-51 |
| Ankauf gebundener Bestände | 39 (22) | 31 (19) | dazu Kennzeichen Förderdarlehen und Rang in E-59 |
| Neubau | 23 (14) | 21 (14) | E-44; E-05 |
| Neubau mit KfW-Darlehen | 27 (16) | 25 (16) | wie Neubau |
| Neubau mit Grobförderung | 27 (17) | 24 (17) | dazu E-68 |

## b) Vorgaben des Hauses

| Kennung | Worum es geht (Variation) | Wirkung: Preis / Rendite | kostet | Urteil | Vorschlag |
|---|---|---|---|---|---|
| H-01 | Zielrendite je Vorhabensart und für geförderte Vorhaben (5 % → 4,5 %) | AN +3,78 % / ±0,000 PP<br>NB +4,32 % (Grundstück +52,07 %) / ±0,000 PP<br>KfW +3,58 % (Grundstück +26,97 %) / ±0,000 PP | Vorgabe (drei Werte) | über | **behalten** |
| H-02 | Beleihungsquote (65 % → 50 %; der Schritt auf 60 % bewegt in keinem der drei Fälle etwas) | AN −0,68 % / −0,024 PP<br>NB ±0,00 % (Grundstück ±0,00 %) / ±0,000 PP<br>KfW −1,90 % (Grundstück −14,29 %) / −0,213 PP | Vorgabe | Grenzfall: wirkt nur, wenn die Quote bindet | **behalten** – bindet im Referenzfall nicht, begrenzt aber das Darlehen, sobald die Schuldendienstdeckung es nicht tut |
| H-03 | Mindestdeckung des Schuldendienstes (1,2 → 1,3 und 1,1) | AN −0,84 % / −0,082 PP<br>NB −0,96 % (Grundstück −11,53 %) / −0,071 PP<br>KfW −0,88 % (Grundstück −6,62 %) / −0,121 PP<br>AN +0,99 % / +0,109 PP<br>NB +1,12 % (Grundstück +13,53 %) / +0,093 PP<br>KfW +1,01 % (Grundstück +7,58 %) / +0,158 PP | Vorgabe | über | **behalten** – die Grenze, die das Darlehen bestimmt |
| H-04 | Mindesttilgung (2 % → 1 %) | AN +1,69 % / +0,186 PP<br>NB +1,51 % (Grundstück +18,21 %) / +0,106 PP | Vorgabe | über | **behalten** |
| H-05 | Anschlusszins als Aufschlag (1 → 2 Prozentpunkte) | AN −1,68 % / −0,169 PP<br>NB −2,17 % (Grundstück −26,21 %) / −0,182 PP<br>KfW −1,60 % (Grundstück −12,05 %) / −0,224 PP | Vorgabe | über | **behalten** |
| H-06 | Stress: Anschlusszins (+1 Prozentpunkt) | AN im Stressfall +0,39 % / +0,052 PP<br>NB im Stressfall +0,093 PP (kein tragbarer Preis)<br>*Zinsbindung 5 Jahre:* AN im Stressfall +1,59 % / +0,216 PP | Vorgabe | Grenzfall: groß nur bei kurzer Zinsbindung | **behalten** – klein nur, solange die Zinsbindung fast die Haltedauer deckt |
| H-06 | Stress: Zins bis zur Zusage mit Neubemessung (+0,5 Prozentpunkte) | AN im Stressfall +2,45 % / +0,183 PP<br>NB im Stressfall +0,124 PP (kein tragbarer Preis) | Vorgabe | über | **behalten** |
| H-06 | Stress: Leerstand (+2 Prozentpunkte) | AN im Stressfall +2,23 % / +0,289 PP<br>NB im Stressfall +0,203 PP (kein tragbarer Preis) | Vorgabe | über | **behalten** |
| H-06 | Stress: Mietsteigerung (−0,5 Prozentpunkte) | AN im Stressfall +4,37 % / +0,572 PP<br>NB im Stressfall +0,461 PP (kein tragbarer Preis) | Vorgabe | über | **behalten** |
| H-06 | Stress: Verkaufsfaktor (−10 %) | AN im Stressfall +6,64 % / +0,856 PP<br>NB im Stressfall +0,649 PP (kein tragbarer Preis) | Vorgabe | über | **behalten** |
| H-06 | Stress: Baukosten (+5 %) | NB im Stressfall +0,379 PP (kein tragbarer Preis) | Vorgabe | über | **behalten** |
| H-06 | Stress: Bauzeit (+3 Monate) | NB im Stressfall +0,109 PP (kein tragbarer Preis) | Vorgabe | Grenzfall: knapp über der Schwelle | **behalten** – knapp über der Schwelle |
| H-06 | Stress: Investitionsstau (+10 %) | AN im Stressfall +0,57 % / +0,053 PP<br>*Investitionsstau 500.000 Euro:* AN im Stressfall +3,45 % / +0,167 PP | Vorgabe | Grenzfall: groß nur bei hohem Investitionsstau | **behalten** – wächst mit dem Betrag; Gegenstück zu den Baukosten im Neubau |
| H-06 | Stress: Instandhaltung (+10 %) | AN im Stressfall +0,67 % / +0,084 PP<br>NB im Stressfall +0,020 PP (kein tragbarer Preis) | Vorgabe | unter | **als Vereinfachung benennen** – Stressgröße entfällt: „Der Stressfall erhöht die laufende Instandhaltung nicht eigens; 10 % mehr bewegen den Preis des Stressfalls um weniger als 1 %.“ |
| H-07 | Regel für die Rate nach der Zinsbindung (`MA-034`) | AN +0,01 % / +0,001 PP<br>NB +0,03 % (Grundstück +0,37 %) / +0,004 PP<br>AN +0,02 % / +0,002 PP<br>NB +0,07 % (Grundstück +0,83 %) / +0,008 PP | Vorgabe mit Auswahl | unter | **vereinfachen** – fest „Tilgungssatz bleibt“, die Auswahl entfällt; `MA-034` bleibt als benannte Annahme |
| H-08 | kurzfristiger Habenzins (2 % → 1 %) | AN −0,49 % / −0,067 PP<br>NB −0,77 % (Grundstück −9,27 %) / −0,090 PP<br>KfW −0,58 % (Grundstück −4,35 %) / −0,085 PP<br>GEF −0,098 PP | Vorgabe | Grenzfall: knapp unter der Schwelle | **fester Wert im Katalog des Hauses**, nicht je Vorhaben – Kernannahme des VOFI (Wiederanlage), knapp unter der Schwelle |
| H-09 | langfristiger Anlagezins der Unterlassensalternative (gleich Habenzins → 3 %) | AN ±0,00 % / ±0,000 PP<br>NB ±0,00 % (Grundstück ±0,00 %) / ±0,000 PP | Vorgabe | Grenzfall: bewegt nur die Endwertdifferenz | **fester Wert im Katalog des Hauses** – bewegt weder Preis noch Rendite, aber die Endwertdifferenz (R-3.2, Beispiel: 212.995 Euro bei 0,5 % statt 2 %) |
| H-10 | Kontokorrentzins (8 % → 6 %) | GEF +0,011 PP | Vorgabe | unter | **fester Katalogwert** ohne Freigabeentscheidung – wirkt nur über die Zwischenfinanzierung der Bauzeit |
| H-11 | Kontokorrentlinie (0 → 250.000 Euro) | AN +0,96 % / +0,111 PP<br>NB +0,87 % (Grundstück +10,47 %) / +0,079 PP | Vorgabe | Grenzfall: knapp an der Schwelle | **fester Wert im Katalog des Hauses** – Grundsatzfrage (Nachschuss oder Linie), nicht je Vorhaben |
| H-12 | Mietsteigerung (2 % → 1,5 %) | AN −4,10 % / −0,574 PP<br>NB −3,81 % (Grundstück −45,98 %) / −0,469 PP<br>KfW −3,59 % (Grundstück −27,02 %) / −0,545 PP<br>GEF ±0,000 PP | Vorgabe | über | **behalten** – im geförderten Neubau des Referenzfalls ohne Wirkung, weil dort die gebundene Miete gilt |
| H-13 | Kostensteigerung (2 % → 3 %) | AN −0,45 % / −0,061 PP<br>NB −0,21 % (Grundstück −2,49 %) / −0,025 PP<br>KfW −0,20 % (Grundstück −1,48 %) / −0,029 PP<br>GEF −0,130 PP | Vorgabe | Grenzfall: über der Schwelle nur bei langer Haltedauer | **fester Wert im Katalog des Hauses** – über der Schwelle nur im geförderten Neubau mit 38 Jahren Haltedauer |
| H-14 | Baupreissteigerung (3 % → 2 %; Probe 3 % → 5 %) | NB +0,64 % (Grundstück +7,75 %) / +0,069 PP<br>*3 % → 5 %:* NB −1,28 % (Grundstück −15,50 %) / −0,135 PP<br>AN +0,09 % / +0,012 PP | Vorgabe | Grenzfall: knapp unter der Schwelle | **fester Wert im Katalog des Hauses** – Markterwartung, für alle Vorhaben gleich; das Vorhaben weicht über den Festpreis E-24 ab |
| H-15 | struktureller Leerstand (1,5 % → 3 %) | AN −1,78 % / −0,233 PP<br>NB −1,25 % (Grundstück −15,06 %) / −0,150 PP<br>KfW −1,18 % (Grundstück −8,86 %) / −0,174 PP<br>GEF −0,075 PP | Vorgabe | über | **behalten**; nimmt den Forderungsausfall H-27 auf |
| H-16 | Verkaufskosten (1,5 % → 2,5 %) | AN −0,62 % / −0,084 PP<br>NB −0,53 % (Grundstück −6,44 %) / −0,064 PP | Vorgabe | Grenzfall: knapp unter der Schwelle | **fester Wert im Katalog des Hauses** – knapp unter der Schwelle |
| H-17 | Verwaltung je Einheit (350 → 420 Euro) | AN −0,58 % / −0,072 PP<br>NB −0,17 % (Grundstück −2,06 %) / −0,020 PP | Vorgabe | unter | **fester Wert im Katalog des Hauses** |
| H-17 | Instandhaltung je m² als Staffel nach Gebäudealter (+20 %) | AN −1,53 % / −0,188 PP<br>NB −0,29 % (Grundstück −3,53 %) / −0,035 PP | Vorgabe (Staffel) | über | **fester Wert im Katalog des Hauses** – stark, aber Hausstandard; das Vorhaben wirkt über Baujahr und Investitionsstau |
| H-17 | nicht umlagefähige Betriebskosten je m² (2 → 3 Euro) | AN −0,54 % / −0,068 PP<br>NB −0,16 % (Grundstück −1,96 %) / −0,019 PP | Vorgabe | unter | **fester Wert im Katalog des Hauses** |
| H-18 | Vorfälligkeitssatz (1 % → 2 % je Jahr Restbindung, Verkauf nach 8 Jahren) | AN −0,49 % / −0,097 PP<br>*Regel weglassen im Neubau mit KfW-Darlehen, Verkauf nach 8 Jahren:* KfW +0,57 % (Grundstück +4,71 %) / +0,148 PP | Vorgabe | Grenzfall: wirkt nur bei Verkauf vor dem Bindungsende | **fester Wert im Katalog des Hauses** |
| H-19 | Voreinstellung der Haltedauer | wie E-48 | Vorgabe (Voreinstellung von E-48) | über | **behalten** – Wirkung wie E-48 |
| H-20 | Warnschwellen: Restwertanteil am Endwert, Abstand von Ausstiegs- und Einstiegsfaktor | rechnen nicht mit | feste Vorgabe (zwei Werte) | ohne Rechenwirkung | **feste Katalogwerte** – lösen nur Hinweise aus, rechnen nicht mit |
| H-22 | Voreinstellung des Steuersatzes der Personen | wie E-42 | Vorgabe (Voreinstellung von E-42) | über | **behalten** – Wirkung wie E-42 |
| H-23 | Anpassungsdauer (4 → 1 Jahr), auch nach dem Bindungsende im Neubau | *Ankauf, wie E-53:* AN +0,13 % / +0,018 PP<br>GEF ±0,000 PP | Vorgabe (Voreinstellung von E-53) | unter | **fester Katalogwert** ohne Freigabeentscheidung |
| H-24 | Voreinstellung der Zinsbindung | wie E-46 | Vorgabe (Voreinstellung von E-46) | über | **behalten** – Wirkung wie E-46 |
| H-25 | kalkulatorischer Zins des Bankdarlehens (Anschlusszins 5 % → fest 6 % und 4 %) | AN −1,37 % / −0,130 PP<br>NB −1,56 % (Grundstück −18,76 %) / −0,113 PP<br>KfW −0,74 % (Grundstück −5,57 %) / −0,103 PP<br>AN +1,82 % / +0,211 PP<br>NB +2,05 % (Grundstück +24,78 %) / +0,180 PP<br>KfW +0,96 % (Grundstück +7,20 %) / +0,150 PP | Vorgabe | über | **behalten** |
| H-25 | kalkulatorischer Zins je für KfW-Darlehen, Förderdarlehen und übernommenes Darlehen | *KfW-Darlehen fest 4 %:* KfW ±0,00 % (Grundstück ±0,00 %) / ±0,000 PP<br>*Förderdarlehen fest 2 %:* GEF ±0,000 PP<br>*übernommenes Darlehen fest 5 %:* AN −0,29 % / −0,053 PP | Vorgabe (drei Werte) | unter | **vereinfachen** – ein Satz für alle Tranchenarten; drei Werte entfallen |
| H-26 | Fluktuation (0 % → 5 % je Jahr) | AN +1,06 % / +0,142 PP | Vorgabe, mit 0 vorbelegt | Grenzfall: knapp über der Schwelle | **fester Wert im Katalog des Hauses** – knapp über der Schwelle; ab Werk null |
| H-27 | Forderungsausfall (0,5 % → 1,5 %) | AN −0,57 % / −0,072 PP<br>NB −0,30 % (Grundstück −3,60 %) / −0,036 PP<br>KfW −0,28 % (Grundstück −2,13 %) / −0,042 PP<br>GEF −0,030 PP | Vorgabe | unter | **vereinfachen** – mit dem strukturellen Leerstand H-15 zu einem Wert „Mietausfall“ zusammenlegen |
| H-28 | Anlaufleerstand leerer Flächen im Ankauf (3 → 6 Monate bei 200 m² leer) | AN −0,77 % / −0,078 PP<br>*600 m² leer, 3 → 12 Monate:* AN −6,87 % / −0,522 PP | Vorgabe | Grenzfall: groß nur mit viel leerer Fläche | **behalten** – hängt am Zustand der leeren Flächen und damit am Vorhaben |
| H-29 | CO2-Preis im Planjahr 1 und seine Steigerung (50 → 100 Euro je Tonne; 5 % → 10 % je Jahr) | AN −0,37 % / −0,047 PP<br>AN −0,09 % / −0,012 PP | Vorgabe (zwei Werte) | unter | **feste Katalogwerte** ohne Freigabeentscheidung; wirken nur noch, wenn E-34 angegeben ist |
| H-30 | Zuschlag der Kostengruppe 700 (20 % → 15 %) | NB +3,33 % (Grundstück +40,14 %) / +0,368 PP | Vorgabe | über | **behalten** |
| H-30 | Zuschlag der Kostengruppen 200, 500, 600 (5 % → 8 %) | NB −2,00 % (Grundstück −24,10 %) / −0,209 PP | Vorgabe | über | **behalten** |
| H-30 | Herstellungskosten je Stellplatz (20.000 → 30.000 Euro bei 20 Stellplätzen) | NB −2,13 % (Grundstück −30,06 %) / −0,219 PP | Vorgabe | über | **behalten** – hängt an der Bauart (ebenerdig oder Tiefgarage) und damit am Vorhaben |
| H-31 | Bereitstellungszins des Bankdarlehens (0,25 % je Monat → 0) | NB +0,85 % (Grundstück +10,20 %) / +0,091 PP | Vorgabe | Grenzfall: knapp unter der Schwelle | **fester Wert im Katalog des Hauses** |
| H-31 | bereitstellungsfreie Zeit (6 → 12 Monate) | NB +0,60 % (Grundstück +7,26 %) / +0,065 PP | Vorgabe | unter | **fester Katalogwert** ohne Freigabeentscheidung |
| H-32 | Bemessungszeitraum der Kapitaldienstrechnung (Zinsbindung 10 → 15 Jahre) | KfW −1,00 % (Grundstück −7,57 %) / −0,137 PP<br>AN −0,48 % / −0,086 PP | Vorgabe | Grenzfall: über der Schwelle nur mit KfW-Darlehen | **fester Wert im Katalog des Hauses** – Bankpraxis, je Vorhaben selten bekannt |
| H-33 | Mindestansatz der Bewirtschaftung in der Kapitaldienstrechnung (15 % → 25 %) | AN −0,22 % / −0,022 PP<br>NB −1,46 % (Grundstück −17,66 %) / −0,107 PP<br>KfW −1,34 % (Grundstück −10,06 %) / −0,179 PP | Vorgabe | über | **fester Wert im Katalog des Hauses** – stark im Neubau, aber Bankpraxis und je Vorhaben selten bekannt |
| H-34 | Anlaufleerstand im Neubau (3 → 6 Monate) | NB −1,02 % (Grundstück −12,29 %) / −0,112 PP<br>KfW −0,98 % (Grundstück −7,37 %) / −0,142 PP<br>GEF −0,046 PP | Vorgabe | über | **behalten** |
| H-35 | Voreinstellung des Vorlaufs bis zum Baubeginn | wie E-23 | Vorgabe (Voreinstellung von E-23) | über | **behalten** – Wirkung wie E-23 |
| H-36 | Betriebskosten leerstehender Flächen (0 → 30 Euro je m² und Jahr) | NB −0,16 % (Grundstück −1,95 %) / −0,017 PP | Vorgabe | unter | **als Vereinfachung benennen** – Vorgabe und Regel R-6.17 entfallen: „Betriebskosten leerstehender Flächen setzt die Grobkalkulation nicht eigens an; sie sind mit dem strukturellen Leerstand und den nicht umlagefähigen Betriebskosten abgegolten.“ |
| H-37 | Bauabschnitte der Förderauszahlung (Rohbau 50 % → 40 %, Innenputz 75 % → 70 % der Bauzeit) | GEF +0,014 PP | Vorgabe (zwei Werte) | unter | **feste Katalogwerte** ohne Freigabeentscheidung |

H-21 (Suchparameter) ist technisch, bewegt kein Ergebnis über die Rechengenauigkeit hinaus und ist nicht gezählt; die Werte bleiben feste Katalogwerte.

**Freigabeblatt nach den Vorschlägen:** 41 Werte statt 57.

- 27 Werte bleiben Vorgaben, die ein Vorhaben mit Begründung ändern kann: Zielrendite (drei Werte), Beleihungsquote, Mindestdeckung, Mindesttilgung, Anschlussaufschlag, acht Stresshöhen, Mietsteigerung, Mietausfall (Leerstand mit Forderungsausfall), kalkulatorischer Zins, Anlaufleerstand im Ankauf und im Neubau, drei Baukostenwerte und die vier Voreinstellungen (Haltedauer, Steuersatz, Zinsbindung, Vorlauf).
- 14 Werte gibt das Haus einmal frei, ohne dass ein Vorhaben davon abweicht: Habenzins, Anlagezins der Alternative, Kontokorrentlinie, Kostensteigerung, Baupreissteigerung, Verkaufskosten, die drei Bewirtschaftungswerte, Vorfälligkeitssatz, Fluktuation, Bereitstellungszins, Bemessungszeitraum, Mindestansatz der Bewirtschaftung.
- 9 Werte werden feste Katalogwerte ohne Freigabeentscheidung: Kontokorrentzins, zwei Warnschwellen, Anpassungsdauer, CO2-Preis und seine Steigerung, bereitstellungsfreie Zeit, zwei Bauabschnitte.
- 7 Werte entfallen: Stress auf die Instandhaltung, Regel nach der Zinsbindung, drei kalkulatorische Zinssätze fremder Tranchen, Forderungsausfall als eigener Wert, Betriebskosten leerstehender Flächen.

Mit weniger änderbaren Vorgaben wird auch die Liste der Abweichungen (R-3.2) kürzer, und die zweite Preissuche je Abweichung läuft seltener.

## c) Lesarten der Modellannahmen mit Schalter

| Kennung | Worum es geht (Variation) | Wirkung: Preis / Rendite | kostet | Urteil | Vorschlag |
|---|---|---|---|---|---|
| MA-026, Lesart 1 | Bank rechnet ihre Quote ohne das nachrangige Förderdarlehen | GEF ±0,000 PP<br>*Förderdarlehen 30 % statt 60 %, Beleihungsquote 40 %:* GEF ±0,000 PP | Schalter | unter | **als Vereinfachung benennen** – Schalter entfällt: „Im geförderten Neubau begrenzt die Schuldendienstdeckung das Bankdarlehen, nicht die Beleihungsquote; ob die Bank das nachrangige Förderdarlehen in ihre Quote rechnet, bildet der Kern deshalb nicht als Lesart ab.“ |
| MA-026, Lesart 2 | Bank rechnet mit Vertragskonditionen | AN +1,82 % / +0,211 PP<br>NB +2,05 % (Grundstück +24,78 %) / +0,180 PP<br>KfW +0,96 % (Grundstück +7,20 %) / +0,150 PP | Schalter | über | **vereinfachen** – Schalter entfällt: auf den Euro deckungsgleich mit dem festen kalkulatorischen Zins H-25 in Höhe des Vertragszinses |
| MA-026, Lesart 3 | Bank setzt den Ertrag des Vorhabens statt des nachhaltigen Ertrags an | AN ±0,00 % / ±0,000 PP<br>*Ist-Miete 11,00 Euro über der Vergleichsmiete 9,20 Euro:* AN +2,18 % / +0,326 PP | Schalter | Grenzfall: wirkt nur bei Miete über der Vergleichsmiete | **behalten als Lesart des Hauses**, nicht je Vorhaben umschaltbar |
| MA-026, Lesart 4 | Bank rechnet fremde Tranchen durchgehend kalkulatorisch | KfW −3,07 % (Grundstück −23,11 %) / −0,370 PP<br>*übernommenes Darlehen:* AN −1,45 % / −0,242 PP | Schalter | über | **behalten als Lesart des Hauses** |
| MA-030 | strengere Lesart: Verkaufsgewinn trotz E-69 gewerbesteuerpflichtig | AN −3,26 % / −0,463 PP | Schalter | über | **vereinfachen** – Schalter entfällt: Sein Ergebnis weicht von „E-69 nein“ nur um die Kürzung des laufenden Ertrags im Verkaufsjahr ab (0,027 Prozentpunkte) |
| MA-031 | Zuschuss im Betriebsvermögen als Minderung der Herstellungskosten statt verteilt | GEF +0,002 PP | Schalter | unter | **als Vereinfachung benennen** – Lesart entfällt: „Im Betriebsvermögen verteilt der Kern den Zuschuss über die Bindung; die Minderung der Herstellungskosten führt im Referenzfall zur selben Rendite und ist nicht eigens abgebildet.“ |
| MA-031 | Zuschuss im Betriebsvermögen als sofortige Einnahme statt verteilt | GEF −0,398 PP | Schalter | über | **behalten als Lesart des Hauses** |
| MA-032 | einbehaltene Entgelte der Förderdarlehen im Jahr der Zahlung statt verteilt | GEF ±0,000 PP | Schalter | unter | **als Vereinfachung benennen** – Schalter entfällt: „Einbehaltene Entgelte der Förderdarlehen verteilt der Kern über die Laufzeit; der Abzug im Jahr der Zahlung ändert die Rendite im Referenzfall nicht.“ |
| MA-036 | Objektverkauf der gewerblich geprägten Personengesellschaft im Rahmen der Aufgabe des Betriebs (440 %, 60 % natürliche Personen) | AN +1,79 % / +0,163 PP | Schalter | Grenzfall: wirkt nur mit Kapitalgesellschaften als Gesellschaftern | **behalten als Lesart des Hauses** |
| MA-037 | Mietenhistorie unbekannt: Kappungsspielraum frei statt ausgeschöpft | AN +0,24 % / +0,031 PP<br>*Ist-Miete 24 % unter der Vergleichsmiete:* AN +7,39 % / +0,815 PP | Schalter | Grenzfall: groß nur bei großer Mietlücke | **vereinfachen** – Schalter entfällt; die vorsichtige Annahme bleibt, und wer die Historie kennt oder begründet annimmt, gibt E-33 ein |
| MA-038 | Miete über der Vergleichsmiete bleibt stehen statt Rückführung (Ist-Miete 11,00 Euro) | AN +1,90 % / +0,283 PP | Schalter | Grenzfall: wirkt nur bei Miete über der Vergleichsmiete | **behalten als Lesart des Hauses** |
| MA-039 | Gebietsverordnungen enden mit ihrem Geltungsende statt Fortgeltung | AN +0,09 % / +0,012 PP<br>*Ist-Miete 24 % unter der Vergleichsmiete:* AN +6,61 % / +0,737 PP | Schalter | Grenzfall: groß nur bei großer Mietlücke | **vereinfachen** – Schalter entfällt: auf den Euro deckungsgleich mit dem Kennzeichen E-05 „außerhalb“; `MA-039` bleibt als benannte Annahme „Fortgeltung“ |
| MA-040 | tilgungsfreie Jahre des KfW-Darlehens ab Bezugsfertigkeit statt ab dem ersten Abruf | KfW −0,02 % (Grundstück −0,12 %) / −0,002 PP | Schalter | unter | **als Vereinfachung benennen** – Schalter entfällt: „Die tilgungsfreien Jahre des KfW-Darlehens zählt der Kern ab dem ersten Abruf; ein Beginn mit der Bezugsfertigkeit bewegt die Rendite um 0,002 Prozentpunkte und ist nicht abgebildet.“ |

`MA-016` wirkt als Eingabe E-44, `MA-034` als Vorgabe H-07, `MA-035` über E-54 und E-55; sie stehen dort. Entfällt ein Schalter, bleibt die Modellannahme im Verzeichnis: mit der Lesart, mit der der Kern rechnet, und der gemessenen Wirkung der anderen.

## d) Steuer: Kapitel 7 gegen die Lehrbuchform

Lehrbuchform ist die Steuer der Musterrechnung: ein Satz auf eine einheitliche Bemessungsgrundlage, lineare Abschreibung, steuerpflichtiger Verkaufsgewinn, sofortige Erstattung von Verlusten. Gemessen ist je Regel, was sich ändert, wenn man sie durch die Lehrbuchform ersetzt oder weglässt.

| Kennung | Worum es geht (Variation) | Wirkung: Preis / Rendite | kostet | Urteil | Vorschlag |
|---|---|---|---|---|---|
| R-7.1 | Steuerstatus (Körperschaft → Privatperson; → gewerbliche Personengesellschaft) | AN +4,56 % / +0,614 PP<br>AN −7,45 % / −0,878 PP | Pflichteingabe E-40 | über | **behalten** |
| R-7.2 bis R-7.4 | Bemessung, lineare Abschreibung, steuerpflichtiger Verkaufsgewinn | kein Unterschied zur Lehrbuchform | nichts | – | **behalten** – das ist die Lehrbuchform selbst |
| R-7.5, R-7.6 | Verlustvortrag im Vorhaben statt Soforterstattung des Lehrbuchs (`MA-016`) | *Körperschaft:* AN +0,03 % / −0,004 PP<br>*Körperschaft:* NB −0,26 % (Grundstück −3,11 %) / −0,033 PP<br>*Körperschaft:* GEF +0,010 PP<br>*Privatperson:* AN +0,66 % / +0,103 PP<br>*Privatperson:* GEF +0,082 PP<br>*Privatperson:* NB +0,21 % (Grundstück +1,39 %) / +0,029 PP<br>*Personengesellschaft:* AN +0,93 % / +0,075 PP | Eingabe E-44 | Grenzfall: knapp über der Schwelle nur bei der Privatperson im Ankauf | **vereinfachen** – nur der Vortrag bleibt (R-7.5); R-7.6 und das Feld E-44 entfallen, siehe E-44 |
| R-7.7 | Körperschaftsteuersatz je Kalenderjahr statt eines Satzes (15 % in allen Jahren) | AN −2,03 % / −0,254 PP<br>NB −2,14 % (Grundstück −25,83 %) / −0,231 PP | nichts (Katalogtabelle KAT-03) | über | **behalten** |
| R-7.8 | erweiterte Kürzung: nur der Ertrag aus dem Grundbesitz, nicht „Kennzeichen heißt keine Gewerbesteuer“ | *Lehrbuchform mit Kennzeichen:* AN +3,75 % / +0,515 PP<br>*Lehrbuchform mit Kennzeichen:* NB +5,25 % (Grundstück +63,78 %) / +0,595 PP | Eingabe E-41 | über | **behalten** |
| R-7.8 | erweiterte Kürzung im Verkaufsjahr: drei Fälle (`MA-030`) | *Wegfall im Verkaufsjahr weglassen:* AN +0,20 % / +0,027 PP<br>*Wegfall im Verkaufsjahr weglassen:* NB +0,06 % (Grundstück +0,72 %) / +0,007 PP<br>*E-69 ja: Kürzung bleibt, Verkaufsgewinn mitgekürzt:* AN +3,57 % / +0,490 PP<br>*E-69 ja: Kürzung bleibt, Verkaufsgewinn mitgekürzt:* NB +4,98 % (Grundstück +60,47 %) / +0,563 PP<br>*dazu die strengere Lesart:* AN −3,26 % / −0,463 PP | Eingabe E-69, Schalter | über | **vereinfachen** – zwei Fälle statt drei: ohne E-69 entfällt die Kürzung im Verkaufsjahr, mit E-69 bleibt sie einschließlich des Verkaufsgewinns; der Schalter entfällt |
| R-7.8 | Abrundung des Gewerbeertrags auf volle 100 Euro | AN ±0,00 % / ±0,000 PP | nichts | unter | **behalten** – eine Zeile, kostet nichts |
| R-7.16 | Hinzurechnung der Entgelte für Schulden | *Körperschaft:* AN ±0,00 % / ±0,000 PP<br>*Körperschaft:* NB ±0,00 % (Grundstück ±0,00 %) / ±0,000 PP<br>*Personengesellschaft:* AN ±0,00 % / ±0,000 PP<br>KfW ±0,00 % (Grundstück +0,01 %) / ±0,000 PP<br>*zehnfaches Vorhaben, Darlehen über 10 Mio. Euro:* AN +0,29 % / +0,039 PP | nichts (Katalogwert KAT-16) | unter | **behalten** – gebaut, kein Feld; auch beim zehnfachen Vorhaben unter der Schwelle |
| R-7.9 | Gewerbesteuer der Personengesellschaft mit Anrechnung statt nur des Steuersatzes E-42 | *Hebesatz 400 %, nur natürliche Personen:* AN ±0,00 % / ±0,000 PP<br>*Hebesatz 440 %:* AN +0,65 % / +0,064 PP<br>*440 %, 60 % natürliche Personen:* AN +3,48 % / +0,325 PP | Eingabe E-43 | Grenzfall: wirkt nur bei hohem Hebesatz oder Kapitalgesellschaften als Gesellschaftern | **behalten** – ohne Wirkung, solange die Anrechnung die Gewerbesteuer deckt; darüber trägt sie |
| R-7.9 | Freibetrag der Gewerbesteuer bei Personenunternehmen | AN ±0,00 % / ±0,000 PP | nichts | unter | **behalten** – eine Zeile, kostet nichts |
| R-7.9 | Einzelunternehmen: Gewerbesteuer mit Anrechnung statt nur des Steuersatzes | AN ±0,00 % / ±0,000 PP | nichts | unter | **behalten** – derselbe Rechenweg wie bei der Personengesellschaft |
| R-7.10 | Privatperson: eigener Satz auf Zinsen statt des Steuersatzes E-42 | AN −0,17 % / −0,025 PP | nichts (Katalogwert KAT-18) | unter | **behalten** – eine Zeile, kostet nichts |
| R-7.11 | Privatperson: steuerfreier Verkauf nach der Frist statt immer steuerpflichtig | AN −11,29 % / −1,464 PP | nichts (Katalogwert KAT-06) | über | **behalten** |
| R-7.12 | befreite Körperschaft (gegen die Körperschaft) | AN +8,11 % / +1,134 PP | Steuerstatus | über | **behalten**; der Hinweis M-44 kostet nichts |
| R-7.13, R-7.14 | Lehrbuchsteuer der Referenzfälle; Grenzsteuersätze für Kennzahlen | rechnen in Preis und Rendite nicht mit | nichts | – | **behalten** – wirken nicht auf Preis und Rendite der Grobkalkulation |
| R-7.15 | Verteilung einbehaltener Entgelte über die Laufzeit (`MA-032`) | GEF ±0,000 PP | Schalter | unter | **vereinfachen** – Regel bleibt wie gebaut, der Schalter entfällt, siehe `MA-032` |
| R-7.17 | Verein und Stiftung: Verkauf nach der Frist steuerfrei, keine Gewerbesteuer (gegen die Lehrbuchform der Körperschaft) | AN −2,12 % / −0,334 PP | Steuerstatus | über | **behalten** |
| R-7.18 | Objektverkauf der Personengesellschaft als laufender Gewinn (`MA-036`) | *andere Lesart: Aufgabe des Betriebs:* AN +1,79 % / +0,163 PP | Schalter | Grenzfall: wirkt nur mit Kapitalgesellschaften als Gesellschaftern | **behalten**; die andere Lesart nur noch als Lesart des Hauses, siehe `MA-036` |
| R-7.19 | Zuschuss in der Steuer nach Vermögenssphäre (`MA-031`) | *Privatperson: verteilt statt im Zuflussjahr:* GEF +0,572 PP<br>*Betriebsvermögen: sofort statt verteilt:* GEF −0,398 PP<br>*Betriebsvermögen: Minderung statt verteilt:* GEF +0,002 PP | Eingabe E-70, Schalter | über | **vereinfachen** – Regel und E-70 bleiben; im Betriebsvermögen entfällt die Lesart „Minderung“, „sofort“ bleibt Lesart des Hauses |
| R-6.16 | anschaffungsnahe Herstellungskosten (Erhaltung 400.000 Euro im Jahr 2) | AN +0,37 % / +0,029 PP | Eingabe E-52 (Katalogwert KAT-12) | unter | **vereinfachen** – Regel bleibt ohne Feld; E-52 entfällt |

**Umgekehrter Test.** „Einfache Steuer“ heißt: Steuersatz je Steuerstatus, Verlustvortrag, steuerfreier Privatverkauf nach der Frist – ohne Hinzurechnung, Abrundung, Anrechnung und eigenen Satz auf Zinsen. Abweichung der einfachen Steuer von der Rechnung nach Kapitel 7:

| Steuerstatus und Fall | Abweichung: Preis / Rendite |
|---|---|
| Körperschaft, Ankauf und Neubau frei | AN ±0,00 % / ±0,000 PP<br>NB ±0,00 % (Grundstück ±0,00 %) / ±0,000 PP |
| Körperschaft, Neubau mit KfW-Darlehen | KfW ±0,00 % (Grundstück +0,01 %) / ±0,000 PP |
| Körperschaft, geförderter Neubau | GEF ±0,000 PP |
| Körperschaft mit Kennzeichen erweiterte Kürzung | AN +3,75 % / +0,515 PP |
| gewerbliche Personengesellschaft, Hebesatz 400 %, nur natürliche Personen | AN ±0,00 % / ±0,000 PP |
| gewerblich geprägte Personengesellschaft, 440 %, 60 % natürliche Personen | AN +3,48 % / +0,325 PP |
| Privatperson | AN −0,17 % / −0,025 PP |

Die einfache Steuer trifft die Körperschaft ohne Kennzeichen, die Personengesellschaft natürlicher Personen bei einem Hebesatz bis zum Anrechnungsfaktor, die Privatperson und den geförderten Neubau innerhalb der Schwelle. Sie verfehlt die Körperschaft mit erweiterter Kürzung und die Personengesellschaft mit Kapitalgesellschaften als Gesellschaftern um 0,3 bis 0,5 Prozentpunkte.

**Vorschlag.** Die Steuer des Kapitels 7 bleibt gebaut, wie sie ist: Was sie von der Lehrbuchform unterscheidet und die Schwelle besteht, sind Steuerstatus, erweiterte Kürzung mit der Frage des Verkaufsjahres (E-41, E-69), Anteil natürlicher Personen (E-43), Körperschaftsteuersatz je Jahr und der steuerfreie Verkauf nach der Frist; Hinzurechnung, Abrundung, Freibetrag und der Satz auf Zinsen bewegen nichts, kosten aber auch kein Feld. Es entfallen das Feld Verlustverrechnung (fest: Vortrag), das Feld Erhaltung oder Modernisierung und vier Schalterstellungen (`MA-030`, `MA-031` Minderung, `MA-032`, im Vorhaben auch `MA-036`).

## e) Rechenregeln aus Sonderfällen der Prüfrunden

Gemessen ist, was sich ändert, wenn die Regel fehlt.

| Kennung | Worum es geht (Variation) | Wirkung: Preis / Rendite | kostet | Urteil | Vorschlag |
|---|---|---|---|---|---|
| R-5.9 | Anschlusszins mit Aufschlag statt Fortgeltung des heutigen Zinses | AN +2,23 % / +0,273 PP<br>NB +2,89 % (Grundstück +34,83 %) / +0,290 PP | Vorgabe H-05 | über | **behalten** |
| R-5.12 | Mindestansatz der Bewirtschaftung in der Kapitaldienstrechnung | AN ±0,00 % / ±0,000 PP<br>NB +0,65 % (Grundstück +7,90 %) / +0,053 PP<br>KfW +0,58 % (Grundstück +4,38 %) / +0,089 PP<br>*15 % → 25 %:* AN −0,22 % / −0,022 PP<br>*15 % → 25 %:* NB −1,46 % (Grundstück −17,66 %) / −0,107 PP<br>*15 % → 25 %:* KfW −1,34 % (Grundstück −10,06 %) / −0,179 PP | Vorgabe H-33 | über | **behalten** – trägt im Neubau; Wert als fester Hauswert, siehe H-33 |
| R-5.16 | Vorfälligkeit beim Verkauf vor dem Ende der Zinsbindung | *Verkauf nach 8 Jahren:* AN +0,49 % / +0,096 PP<br>*Verkauf nach 8 Jahren:* KfW +0,57 % (Grundstück +4,71 %) / +0,148 PP | Vorgabe H-18 | Grenzfall: wirkt nur bei Verkauf vor dem Bindungsende | **behalten**; Satz als fester Hauswert, siehe H-18 |
| R-5.18 | Bereitstellungszins des Bankdarlehens | NB +0,85 % (Grundstück +10,20 %) / +0,091 PP<br>KfW +0,53 % (Grundstück +3,99 %) / +0,078 PP | Vorgabe H-31 (zwei Werte) | Grenzfall: knapp unter der Schwelle | **behalten**; Satz als fester Hauswert, freie Zeit als fester Katalogwert, siehe H-31 |
| R-5.19 | Bereitstellungsprovision des KfW-Darlehens | KfW +0,01 % (Grundstück +0,07 %) / +0,001 PP | kein Feld, aber Katalogwerte in KAT-15 | unter | **als Vereinfachung benennen** – „Die Bereitstellungsprovision des KfW-Darlehens rechnet die Grobkalkulation nicht; bei Abruf während der Bauzeit bewegt sie den tragbaren Grundstückspreis um weniger als 0,1 %.“ |
| R-5.11 | Aufschub des Tilgungsbeginns des Förderdarlehens | GEF +0,058 PP | Eingabe E-68 | unter | **als Vereinfachung benennen**, siehe E-68 |
| R-6.3 | Wartefrist und Kappungsgrenze der Mieterhöhung im Bestand | AN +0,38 % / +0,052 PP<br>*Ist-Miete 24 % unter der Vergleichsmiete:* AN +8,71 % / +0,960 PP | nichts (Katalogwert KAT-08) | Grenzfall: groß nur bei großer Mietlücke | **behalten** – Kern der Mietrechnung im Bestand |
| R-6.3 | Rückführung einer Miete über der Vergleichsmiete (`MA-038`) | AN +1,90 % / +0,283 PP | Schalter | Grenzfall: wirkt nur bei Miete über der Vergleichsmiete | **behalten**; die andere Lesart nur noch als Lesart des Hauses, siehe `MA-038` |
| R-6.8 | Instandhaltung als Staffel nach Gebäudealter statt eines Satzes | AN +1,36 % / +0,175 PP | nichts (Baujahr ist Pflichteingabe) | über | **behalten** |
| R-6.9 | CO2-Kostenanteil des Vermieters nach dem Stufenmodell | AN +0,37 % / +0,047 PP<br>*60 kg je m²:* AN +0,74 % / +0,093 PP<br>*60 kg je m² und 100 Euro je Tonne:* AN +1,49 % / +0,185 PP | Eingaben E-34, E-54, E-55; Vorgabe H-29 | Grenzfall: über der Schwelle erst bei hohem Ausstoß und doppeltem CO2-Preis | **vereinfachen** – Regel bleibt, gerechnet wird nur mit angegebenem Ausstoß (E-34, freiwillig); benannt: „Ohne Angabe des CO2-Ausstoßes rechnet die Grobkalkulation keinen Vermieteranteil an den CO2-Kosten; im Referenzfall sind das 0,4 % des tragbaren Preises.“ |
| R-6.9 | hälftige Teilung der CO2-Kosten nach `CO2KOSTAUFG-5A` | AN +0,06 % / +0,009 PP | Eingaben E-66, E-67 | unter | **als Vereinfachung benennen**, siehe E-66 |
| R-6.14 | Fluktuation: Neuvermietung zur Marktmiete | AN +1,06 % / +0,142 PP | Vorgabe H-26 | Grenzfall: knapp über der Schwelle | **behalten**; Wert als fester Hauswert, siehe H-26 |
| R-6.17 | Betriebskosten leerstehender Flächen | NB +0,16 % (Grundstück +1,99 %) / +0,017 PP | Vorgabe H-36 | unter | **als Vereinfachung benennen**, siehe H-36 |
| R-6.18 | Geltungsende der Gebietsverordnungen (`MA-039`) | AN +0,09 % / +0,012 PP | Schalter | Grenzfall: groß nur bei großer Mietlücke | **vereinfachen** – Fortgeltung fest; der Schalter entfällt, siehe `MA-039` |
| R-11.3 | Auszahlung der Fördermittel in vier Teilraten mit Zwischenfinanzierung über das Kontokorrent | GEF +0,043 PP | Vorgabe H-37 (zwei Werte) | unter | **behalten** – gebaut, folgt der Richtlinie und zeigt den Liquiditätsbedarf der Bauzeit; die Bauabschnitte werden feste Katalogwerte, siehe H-37 |
| R-11.8 | Stressfall mit neun Größen | siehe H-06 | Vorgabe H-06 (neun Werte) | über | **vereinfachen** – acht Größen statt neun, siehe H-06 |
| R-10.25 | Warnschwellen (Restwertanteil, Faktorabstand) | rechnen nicht mit | feste Vorgabe H-20 | ohne Rechenwirkung | **behalten** – lösen nur Hinweise aus; feste Katalogwerte |

## Grenzfälle

**Knapp an der Schwelle** (15): Die Wirkung liegt bei gewöhnlicher Spanne zwischen etwa der halben und der anderthalbfachen Schwelle.

| Kennung | Gegenstand | stärkste gemessene Wirkung | Vorschlag |
|---|---|---|---|
| E-27 | Stellplätze im Neubau (0 → 20 zu 60 Euro Miete) | *dazu Herstellungskosten je Platz 30.000 statt 20.000 Euro:* NB −2,13 % (Grundstück −30,06 %) / −0,219 PP | behalten |
| E-39 | Vorvermietung: kein Anlaufleerstand (nein → ja) | NB +1,02 % (Grundstück +12,29 %) / +0,113 PP | behalten |
| E-44 | Verlustverrechnung: Vortrag im Vorhaben → sofort (`MA-016`) | *Privatperson:* AN +0,66 % / +0,103 PP | vereinfachen |
| E-51 | Investitionsstau: Jahr der Ausführung (Jahr 2 → Jahr 5) | AN +0,91 % / +0,105 PP | behalten |
| E-59 | übernommenes Darlehen: ursprünglicher Nennbetrag als Bezug der Rate (600.000 → 500.000 Euro) | AN +0,44 % / +0,083 PP | behalten |
| E-63 | Steigerung des Erbbauzinses (2 % → 3 %) | AN −0,85 % / −0,109 PP | vereinfachen |
| E-65 | nachhaltige Miete der Bank im Neubau (16,50 → 15,00 Euro) | NB −1,13 % (Grundstück −13,63 %) / −0,084 PP | behalten |
| E-67 | weitere Kosten des Vermieters aus dieser Teilung (0 → 2.000 Euro im Jahr) | AN −0,83 % / −0,103 PP | als Vereinfachung benennen |
| H-06 | Stress: Bauzeit (+3 Monate) | NB im Stressfall +0,109 PP (kein tragbarer Preis) | behalten |
| H-08 | kurzfristiger Habenzins (2 % → 1 %) | GEF −0,098 PP | fester Wert im Katalog des Hauses |
| H-11 | Kontokorrentlinie (0 → 250.000 Euro) | AN +0,96 % / +0,111 PP | fester Wert im Katalog des Hauses |
| H-14 | Baupreissteigerung (3 % → 2 %; Probe 3 % → 5 %) | *3 % → 5 %:* NB −1,28 % (Grundstück −15,50 %) / −0,135 PP | fester Wert im Katalog des Hauses |
| H-16 | Verkaufskosten (1,5 % → 2,5 %) | AN −0,62 % / −0,084 PP | fester Wert im Katalog des Hauses |
| H-26 | Fluktuation (0 % → 5 % je Jahr) | AN +1,06 % / +0,142 PP | fester Wert im Katalog des Hauses |
| H-31 | Bereitstellungszins des Bankdarlehens (0,25 % je Monat → 0) | NB +0,85 % (Grundstück +10,20 %) / +0,091 PP | fester Wert im Katalog des Hauses |

**Groß nur im besonderen Fall** (25): Im Referenzfall unter der Schwelle oder ohne Wirkung, im genannten Fall deutlich darüber.

| Kennung | Gegenstand | wann es wirkt | stärkste gemessene Wirkung | Vorschlag |
|---|---|---|---|---|
| E-05 | Lage im Gebiet der abgesenkten Kappungsgrenze (15 % → 20 %) | groß nur bei großer Mietlücke | *Ist-Miete 24 % unter der Vergleichsmiete:* AN +6,61 % / +0,737 PP | vereinfachen |
| E-05 | Lage im Gebiet der Mietpreisbremse (im Gebiet → außerhalb) | groß nur mit leerer Fläche und hoher Marktmiete | *600 m² leer, Marktmiete 13,00 Euro:* AN +8,67 % / +1,043 PP | behalten |
| E-12 | Bodenanteil (25 % → 35 %; Probe 25 % → 50 %) | über der Schwelle nur bei steuerfreiem Verkauf | *Privatperson, 50 %:* AN −1,63 % / −0,244 PP | vereinfachen |
| E-16 | Marktmiete im Ankauf (10,50 → 9,50 Euro) | wirkt nur mit leerer Fläche oder Fluktuation | *600 m² leer:* AN −1,05 % / −0,130 PP | behalten |
| E-31 | leerstehende Fläche am Stichtag (0 → 200 m² und 0 → 600 m² von 1.320 m²) | groß nur bei langer Vermarktung | *600 m², Vermietung nach 12 statt 3 Monaten:* AN −7,34 % / −0,552 PP | behalten |
| E-33 | Mietenhistorie (ohne Angabe → letzte Erhöhung vor 6 Monaten) | groß nur bei großer Mietlücke | *Ist-Miete 24 % unter der Vergleichsmiete:* AN +6,53 % / +0,724 PP | behalten |
| E-59 | übernommenes Darlehen: Kennzeichen Förderdarlehen (erspart die Vorfälligkeit) | wirkt nur bei Verkauf vor dem Bindungsende | *Verkauf nach 5 Jahren, vor dem Bindungsende:* AN +0,40 % / +0,141 PP | vereinfachen |
| E-61 | Wertansatz der Bank (Kaufpreis → 2,6 Mio. Euro) | wirkt nur, wenn die Beleihungsquote bindet | *bei Beleihungsquote 45 %:* AN +1,33 % / +0,074 PP | vereinfachen |
| E-70 | Verteilung des Zuschusses über die Bindung beantragt (Privatperson, Verein, Stiftung) | groß, aber nur für Privatperson, Verein und Stiftung im geförderten Neubau | GEF +0,572 PP | behalten |
| H-02 | Beleihungsquote (65 % → 50 %; der Schritt auf 60 % bewegt in keinem der drei Fälle etwas) | wirkt nur, wenn die Quote bindet | KfW −1,90 % (Grundstück −14,29 %) / −0,213 PP | behalten |
| H-06 | Stress: Anschlusszins (+1 Prozentpunkt) | groß nur bei kurzer Zinsbindung | *Zinsbindung 5 Jahre:* AN im Stressfall +1,59 % / +0,216 PP | behalten |
| H-06 | Stress: Investitionsstau (+10 %) | groß nur bei hohem Investitionsstau | *Investitionsstau 500.000 Euro:* AN im Stressfall +3,45 % / +0,167 PP | behalten |
| H-09 | langfristiger Anlagezins der Unterlassensalternative (gleich Habenzins → 3 %) | bewegt nur die Endwertdifferenz | AN ±0,00 % / ±0,000 PP | fester Wert im Katalog des Hauses |
| H-13 | Kostensteigerung (2 % → 3 %) | über der Schwelle nur bei langer Haltedauer | GEF −0,130 PP | fester Wert im Katalog des Hauses |
| H-18 | Vorfälligkeitssatz (1 % → 2 % je Jahr Restbindung, Verkauf nach 8 Jahren) | wirkt nur bei Verkauf vor dem Bindungsende | *Regel weglassen im Neubau mit KfW-Darlehen, Verkauf nach 8 Jahren:* KfW +0,57 % (Grundstück +4,71 %) / +0,148 PP | fester Wert im Katalog des Hauses |
| H-28 | Anlaufleerstand leerer Flächen im Ankauf (3 → 6 Monate bei 200 m² leer) | groß nur mit viel leerer Fläche | *600 m² leer, 3 → 12 Monate:* AN −6,87 % / −0,522 PP | behalten |
| H-32 | Bemessungszeitraum der Kapitaldienstrechnung (Zinsbindung 10 → 15 Jahre) | über der Schwelle nur mit KfW-Darlehen | KfW −1,00 % (Grundstück −7,57 %) / −0,137 PP | fester Wert im Katalog des Hauses |
| MA-026, Lesart 3 | Bank setzt den Ertrag des Vorhabens statt des nachhaltigen Ertrags an | wirkt nur bei Miete über der Vergleichsmiete | *Ist-Miete 11,00 Euro über der Vergleichsmiete 9,20 Euro:* AN +2,18 % / +0,326 PP | Lesart des Hauses |
| MA-036 | Objektverkauf der gewerblich geprägten Personengesellschaft im Rahmen der Aufgabe des Betriebs (440 %, 60 % natürliche Personen) | wirkt nur mit Kapitalgesellschaften als Gesellschaftern | AN +1,79 % / +0,163 PP | Lesart des Hauses |
| MA-037 | Mietenhistorie unbekannt: Kappungsspielraum frei statt ausgeschöpft | groß nur bei großer Mietlücke | *Ist-Miete 24 % unter der Vergleichsmiete:* AN +7,39 % / +0,815 PP | vereinfachen |
| MA-038 | Miete über der Vergleichsmiete bleibt stehen statt Rückführung (Ist-Miete 11,00 Euro) | wirkt nur bei Miete über der Vergleichsmiete | AN +1,90 % / +0,283 PP | Lesart des Hauses |
| MA-039 | Gebietsverordnungen enden mit ihrem Geltungsende statt Fortgeltung | groß nur bei großer Mietlücke | *Ist-Miete 24 % unter der Vergleichsmiete:* AN +6,61 % / +0,737 PP | vereinfachen |
| R-7.9 | Gewerbesteuer der Personengesellschaft mit Anrechnung statt nur des Steuersatzes E-42 | wirkt nur bei hohem Hebesatz oder Kapitalgesellschaften als Gesellschaftern | *440 %, 60 % natürliche Personen:* AN +3,48 % / +0,325 PP | behalten |
| R-6.3 | Wartefrist und Kappungsgrenze der Mieterhöhung im Bestand | groß nur bei großer Mietlücke | *Ist-Miete 24 % unter der Vergleichsmiete:* AN +8,71 % / +0,960 PP | behalten |
| R-6.9 | CO2-Kostenanteil des Vermieters nach dem Stufenmodell | über der Schwelle erst bei hohem Ausstoß und doppeltem CO2-Preis | *60 kg je m² und 100 Euro je Tonne:* AN +1,49 % / +0,185 PP | vereinfachen |

Drei Fälle stehen hinter den meisten dieser Zeilen und sind als Maßstab für die Entscheidung brauchbarer als die einzelne Zahl:

1. **Große Mietlücke im Bestand.** Liegt die Ist-Miete ein Viertel unter der Vergleichsmiete, entscheiden Kappungsgrenze, Wartefrist und Mietenhistorie über 6 bis 9 % des tragbaren Preises. Die Regel R-6.3, das Kennzeichen der Kappungsgrenze (E-05) und die Mietenhistorie (E-33) bleiben deshalb; die Schalter `MA-037` und `MA-039` entfallen, weil E-33 und E-05 dasselbe leisten.
2. **Miete über der Vergleichsmiete.** Dann wirken die Rückführung (`MA-038`) und der Ertragsansatz der Bank (`MA-026`, Lesart 3) mit je rund 2 % des Preises. Beide bleiben als Lesart des Hauses.
3. **Leerstand mit langer Vermarktung.** Mit 45 % leerer Fläche und zwölf statt drei Monaten bis zur Vermietung sind es 7 % des Preises. E-31 und H-28 bleiben.

## Die größten und die kleinsten Wirkungen

Rangfolge nach dem Vielfachen der Schwelle (der größere Wert aus Rendite je 0,1 Prozentpunkte und Preis je 1 %, im Neubau je 1 % der Gesamtkosten); nur Messungen am Referenzfall, ohne die Hauptannahmen aus dem Abschnitt „Maßstab“.

| Kennung | Gegenstand (Variation) | Wirkung | Vielfaches der Schwelle |
|---|---|---|---|
| R-7.11 | Privatperson: steuerfreier Verkauf nach zehn Jahren → immer steuerpflichtig (frei → pflichtig) | AN −11,29 % / −1,464 PP | 14,64 |
| E-62 | Erbbauzins (0 → 12.000 Euro im Jahr) | AN −10,03 % / −1,277 PP | 12,77 |
| R-7.12 | befreite Körperschaft gegen Körperschaft (Bedeutung des Status) (Körperschaft → befreit) | AN +8,11 % / +1,134 PP | 11,34 |
| E-56 | gebundener Bestand (E-56 bis E-58) (0 → 40 % bis Jahr 6 zu 6,80 Euro) | AN −8,87 % / −1,134 PP | 11,34 |
| R-7.1 | Steuerstatus: Körperschaft → gewerbliche Personengesellschaft (Auswahl) | AN −7,45 % / −0,878 PP | 8,78 |
| H-06 | Stress: Verkaufsfaktor (−10 % → 0) | AN im Stressfall +6,64 % / +0,856 PP | 8,56 |
| E-59 | übernommenes Darlehen (keines → 500.000 Euro zu 0,5 %) | AN +5,73 % / +0,800 PP | 8,00 |
| E-60 | verfügbares Eigenkapital (zweite Preisgrenze) (leer → 1,2 Mio. Euro) | AN −7,70 % / ±0,000 PP | 7,70 |
| E-35 | KfW-Darlehen (0 → 3 Mio. Euro (35 Jahre, 1 Freijahr)) | NB +5,83 % (Grundstück +70,34 %) / +0,664 PP | 6,64 |
| E-23 | Vorlauf bis zum Baubeginn (0 → 12 Monate) | NB −5,90 % (Grundstück −71,19 %) / −0,657 PP | 6,57 |

Die zehn kleinsten Wirkungen über null:

| Kennung | Gegenstand (Variation) | Wirkung | Vielfaches der Schwelle |
|---|---|---|---|
| E-33 | Mietenhistorie (nicht angegeben → letzte Erhöhung vor 6 Monaten, 7,50 Euro vor drei Jahren) | AN +0,01 % / +0,001 PP | 0,01 |
| R-5.19 | Bereitstellungsprovision des KfW-Darlehens weglassen (0,15 % → 0) | KfW +0,01 % (Grundstück +0,07 %) / +0,001 PP | 0,01 |
| MA-031 | Zuschuss im Betriebsvermögen: Minderung der Herstellungskosten (verteilt → Minderung) | GEF +0,002 PP | 0,02 |
| E-02 | Stichtag (Katalogstand je Kalenderjahr) (2027 → 2029) | AN +0,02 % / +0,002 PP | 0,02 |
| MA-040 | tilgungsfreie Jahre des KfW-Darlehens ab Bezugsfertigkeit (ab Abruf → ab Bezug) | KfW −0,02 % (Grundstück −0,12 %) / −0,002 PP | 0,02 |
| E-05 | Lage im Gebiet: Mietpreisbremse, 200 m² leer (im Gebiet → außerhalb) | AN −0,04 % / −0,006 PP | 0,06 |
| E-12 | Bodenanteil (25 % → 35 %) | AN −0,06 % / −0,008 PP | 0,08 |
| H-07 | Regel nach der Zinsbindung (MA-034) (Tilgungssatz bleibt → Restlaufzeit bleibt) | NB +0,07 % (Grundstück +0,83 %) / +0,008 PP | 0,08 |
| E-66 | Heizung mit hälftiger CO2-Teilung (nein → ja) | AN −0,06 % / −0,009 PP | 0,09 |
| R-6.9 | hälftige Teilung nach 5a weglassen (Heizung nach 5a) (50 % → Stufenmodell) | AN +0,06 % / +0,009 PP | 0,09 |

Ohne jede Wirkung im Referenzfall (19 Gegenstände): E-16 Marktmiete im Ankauf (wirkt nur bei leerer Fläche und Fluktuation); E-18 Angebotspreis (nur Abstand zum Angebot); E-25 Kennzeichen des Kostenkennwerts (200 bis 700 statt 300 und 400); E-59 übernommenes Darlehen: Rang; H-09 langfristiger Anlagezins der Alternative; H-23 Voreinstellung der Anpassungsdauer (Neubau: nach Bindungsende); H-25 kalkulatorischer Zins des Förderdarlehens; H-25 kalkulatorischer Zins des KfW-Darlehens; MA-026/1 Bank rechnet ihre Quote ohne das nachrangige Förderdarlehen; MA-026/3 Bank setzt den Ertrag des Vorhabens an; MA-032 Entgelte der NBank im Jahr der Zahlung; R-7.15 Entgelte des Förderdarlehens verteilt → im Jahr der Zahlung (wie MA-032); R-7.8 Abrundung des Gewerbeertrags weglassen; R-7.8/7.16 Hinzurechnung der Entgelte für Schulden weglassen (Körperschaft); R-7.8/7.16 Hinzurechnung weglassen (Neubau mit KfW: Entgelte über dem Freibetrag); R-7.8/7.16 Hinzurechnung weglassen (gewerbliche Personengesellschaft); R-7.9 Einzelunternehmen: Gewerbesteuer-Mechanik → nur Steuersatz; R-7.9 Freibetrag der Gewerbesteuer weglassen (Personengesellschaft); R-7.9 Gewerbesteuer mit Freibetrag und Anrechnung → nur Steuersatz E-42 (Personengesellschaft, 400 %).

## Folgen für den Nachtrag 2

Stand auf der Platte: Der Nachtrag 2 ist im Referenzrechner, in der Fachspezifikation und in `annahmen.toml` teilweise eingearbeitet. Nicht nachgezogen sind `docs/spezifikation.md` (Zeilen „Zielrendite und Schwellen“, „Grobkalkulation“, „Teilschritte der Stufe 1“, Kapitel 1 „Steuerstatus“, Kapitel 4), `docs/entscheidungen.md` und die Zählwerte in `LIESMICH.md` des Referenzrechners (dort noch 1.150 Prüfungen und 525 Sollwerte statt 1.156 und 526).

| Punkt | Inhalt | Stand | Messung | Folge |
|---|---|---|---|---|
| A | `MA-030`: drei Fälle der erweiterten Kürzung im Verkaufsjahr, E-69 neu gefasst, Hinweis M-51 | eingearbeitet in Rechner, R-7.8 und `annahmen.toml`; Spezifikation und Protokoll offen | *E-69:* AN +3,57 % / +0,490 PP<br>*E-69:* NB +4,98 % (Grundstück +60,47 %) / +0,563 PP<br>*Wegfall im Verkaufsjahr allein:* AN +0,20 % / +0,027 PP<br>*Wegfall im Verkaufsjahr allein:* NB +0,06 % (Grundstück +0,72 %) / +0,007 PP<br>*strengere Lesart:* AN −3,26 % / −0,463 PP | **E-69 bleibt, der Schalter wird zurückgebaut.** Die Frage, ob der Verkaufsgewinn Gewerbesteuer trägt, besteht die Schwelle; der Wegfall der Kürzung für den laufenden Ertrag des Verkaufsjahres allein nicht, er kostet neben E-69 aber nichts. Die strengere Lesart ergibt bis auf diese 0,027 Prozentpunkte dasselbe wie „E-69 nein“. Spezifikation und Protokoll in der Fassung mit zwei Fällen nachziehen |
| B | `MA-031`: Zuschuss nach Vermögenssphäre, Eingabe E-70, Katalogwert KAT-19 | eingearbeitet in Rechner, R-7.19 und `annahmen.toml` | *E-70, Privatperson:* GEF +0,572 PP<br>*Betriebsvermögen sofort:* GEF −0,398 PP<br>*Betriebsvermögen Minderung:* GEF +0,002 PP | **Bleibt; die Lesart „Minderung“ wird zurückgebaut** und als Vereinfachung benannt. E-70 besteht die Schwelle, betrifft aber nur Privatperson, Verein und Stiftung im geförderten Neubau (Grenzfall, bedingtes Feld). „Sofort“ bleibt Lesart des Hauses |
| C | `MA-032`: einbehaltene Entgelte verteilt, Disagio als Vormerkung für Teil 2 | eingearbeitet in R-7.15 und `annahmen.toml`; Rechner unverändert | GEF ±0,000 PP | **Schalter zurückbauen, als Vereinfachung benennen.** Die Regel bleibt wie gebaut; die Frage an den Steuerberater entfällt |
| D | `MA-036`: Objektverkauf der gewerblich geprägten Personengesellschaft | eingearbeitet in R-7.18 und `annahmen.toml` | AN +1,79 % / +0,163 PP | **Bleibt als Lesart des Hauses**, im Vorhaben nicht umschaltbar: über der Schwelle nur mit Kapitalgesellschaften als Gesellschaftern (Grenzfall) |
| E | R-7.12, Hinweis M-44: Verkauf der befreiten Körperschaft | eingearbeitet in Rechner (Wortlaut) und R-7.12 | *Status befreit gegen Körperschaft:* AN +8,11 % / +1,134 PP | **Schon eingearbeitet.** Ein Hinweis ohne Rechenwirkung; kostet weder Feld noch Schalter |
| F.1 | `MA-040` bleibt | unverändert | KfW −0,02 % (Grundstück −0,12 %) / −0,002 PP | **Annahme bleibt im Verzeichnis, der Schalter wird zurückgebaut** und als Vereinfachung benannt |
| F.2 | Begründungspflicht nach dem tragbaren Preis | eingearbeitet in Rechner, Tests und R-3.2; Spezifikationszeile offen | – | **Schon eingearbeitet; Spezifikationszeile nachziehen.** Kostet kein Feld. Mit weniger änderbaren Vorgaben und Schaltern gibt es weniger Abweichungen zu begründen |
| F.3 | Zwischenfinanzierung der Teilraten über das Kontokorrent bleibt | unverändert | *Teilraten weglassen:* GEF +0,043 PP<br>*Bauabschnitte:* GEF +0,014 PP<br>*Kontokorrentzins:* GEF +0,011 PP | **Regel bleibt** (gebaut, folgt der Richtlinie, zeigt den Liquiditätsbedarf der Bauzeit); H-37 und H-10 werden feste Katalogwerte |
| F.4 | Spezifikationszeilen „Teilschritte der Stufe 1“, Kapitel 1 „Steuerstatus“, Kapitel 4 | nicht eingearbeitet | – | **Nach der Messung einarbeiten**, zusammen mit den Entscheidungen aus dieser Durchsicht, damit die Zeilen nur einmal angefasst werden |
| G | Einträge im Entscheidungsprotokoll, auch Belegstufe „Wortlaut in Verlagswiedergabe“ und Netzzugang | nicht eingearbeitet | – | **Nach der Messung einarbeiten.** Belegstufe und Netzzugang hängen nicht an der Schwelle und können sofort; die Einträge zu `MA-030` und `MA-031` gleich in der Fassung nach dieser Durchsicht |
| H | Kapitel 16 kürzen | eingearbeitet (13 Fragen an die Bank, vier an den Steuerberater) | *Frage 9, Regel nach der Zinsbindung:* AN +0,02 % / +0,002 PP<br>*Frage 9, Regel nach der Zinsbindung:* NB +0,07 % (Grundstück +0,83 %) / +0,008 PP<br>*Frage 12, Beginn der tilgungsfreien Jahre:* KfW −0,02 % (Grundstück −0,12 %) / −0,002 PP<br>*Frage 13, Zins der Zwischenfinanzierung:* GEF +0,011 PP | **Nach der Entscheidung weiter kürzen:** Die Fragen 9, 12 (zweiter Teil) und 13 an die Bank und die Frage zu `MA-032` an den Steuerberater betreffen Größen unter der Schwelle; Frage 1 bewegt im geförderten Neubau nichts |

## Grenzen der Messung

- **Eine Größe zur Zeit.** Wechselwirkungen sind nur dort gemessen, wo eine Probe sie eigens stellt. Mehrere Größen unter der Schwelle können sich addieren; das gilt für die Summe der benannten Vereinfachungen ebenso wie für die Summe der Hauptannahmen.
- **Der typische Fall ist der Referenzfall.** Die vier Fälle rechnen mit angenommenen Vorgaben und angenommenem Katalogstand, die das Haus noch nicht freigegeben hat. Mit anderen Vorgaben verschieben sich die Grenzfälle, nicht das Gesamtbild.
- **Nicht gemessen:** die 21 Pflichteingaben außer den sieben des Maßstabs; die Suchparameter H-21 und die Warnschwellen H-20 (keine Rechenwirkung); R-7.13 und R-7.14; E-54 und E-55 eigens (sie wirken nur über den Ausstoß E-34); im geförderten Neubau der tragbare Preis; im Stressfall des Neubaus der tragbare Preis.
- **E-61 unter dem Kaufpreis:** Ein Wertansatz der Bank von 2,2 Mio. Euro endete in der Messung mit einer Eingabemeldung und ist nicht ausgewertet; die Beleihungsquote bindet im Referenzfall ohnehin nicht (H-02).
- **Endwertdifferenz:** Die Schwelle misst Preis und Rendite. H-09 bewegt keines von beiden, wohl aber die Endwertdifferenz; deshalb der Vorschlag „fester Hauswert“ statt „entfällt“.

## Nachvollzug

`python3 wesentlichkeit.py --ausgabe DATEI.json` im Ordner des Referenzrechners; Laufzeit rund zwei Minuten, 278 Messungen. Das Skript ändert kein Modul und keinen Sollwert und ist kein Referenzfall; `python3 referenzfaelle.py` läuft unverändert. Jede Zeile der Tabellen oben nennt Kennung und Variation so, dass sie in der Ausgabe des Skripts zu finden ist.

## Umsetzung

Die Vorschläge sind am 2026-11-21 umgesetzt (Entscheidungsprotokoll, oberster Eintrag; Fachspezifikation R-3.2 bis R-3.6 und Kapitel 16 mit der Liste der benannten Vereinfachungen V-01 bis V-22). Vier Abweichungen von den Vorschlägen oben:

- **R-5.19, Bereitstellungsprovision des KfW-Darlehens:** bleibt (gebaut, kostet kein Feld).
- **E-44, Verlustverrechnung:** kein Feld im Vorhaben, aber fester Hauswert H-38 mit der Voreinstellung „Vortrag“ statt fest „Vortrag“.
- **H-27, Forderungsausfall:** fester Katalogwert statt Zusammenlegung mit dem Leerstand H-15, weil nur der Leerstand auf den Verkaufspreis wirkt und die Zusammenlegung jede Leitgröße verschoben hätte.
- **E-12, Bodenanteil:** wo der Verkauf steuerpflichtig ist, rechnet der Kern mit dem neuen festen Hauswert H-39.

Damit: 27 Vorgaben im Vorhaben änderbar, 16 feste Hauswerte, 10 feste Katalogwerte, 6 Vorgabewerte entfallen; alles Übrige wie in der Zählung oben. Die Zahlen dieser Durchsicht stammen aus dem Stand vor der Umsetzung; `wesentlichkeit.py` misst seither nur noch die verbliebenen Gegenstände (238 Messungen). Im Basisfall hat sich kein Sollwert geändert; im Stressfall rechnet der Kern mit acht statt neun Größen (tragbarer Preis des Ankaufs im Stressfall 1.977.816 statt 1.964.653 Euro).
