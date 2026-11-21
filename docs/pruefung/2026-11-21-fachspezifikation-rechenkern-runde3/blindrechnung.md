# Blindrechnung zur Fachspezifikation Rechenkern (Prüfrunde 3)

**Stand:** 2026-11-21
**Quelle:** allein `docs/fachspezifikation-rechenkern.md` in der eingefrorenen Fassung vom 2026-11-21 (Regeln, Beispiele, Anhang A), dazu der eigene Stand und Bericht der Prüfrunde 2. Der Ordner des Referenzrechners, `erwartete_werte.json`, die Änderungsberichte, `wesentlichkeit.py`, die übrigen Prüfberichte unter `docs/pruefung/` und die Durchsicht an der Wesentlichkeitsschwelle wurden nicht geöffnet.
**Werkzeug:** zweite, unabhängige Umsetzung in Python (`decimal` mit 60 Stellen, nur Standardbibliothek) unter `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/blindrechnung-fachspezifikation/`. `kern.py` ist auf den heutigen Text gebracht; je Fall ein Skript (`rf11.py`, `rf11b.py`, `rf11g.py`, `rf13.py`, `rf12.py`, `rf12k.py`, `rf12f.py`, `rf17.py`, `rf06.py`, `extra.py`), `lesarten.py` beziffert die offenen Lesarten. `python3 blindwerte.py` gibt alle Werte mit Sollwert, die Zählung, die Abweichungen und die eigenen Werte in einem Lauf aus (rund 20 Sekunden; `--kurz` ohne die Einzelwerte). Der Stand nach Prüfrunde 1 liegt unverändert in `stand-runde2/`.

## Ergebnis

951 Sollwerte des Dokuments nachgerechnet, **946 getroffen, 5 abweichend** – Geldbeträge auf den Cent, Renditen und Deckungen auf die ausgewiesenen Stellen, Preise auf den Euro, Monate und Meldungen wörtlich.

- **Der Text trägt jetzt.** An keiner ergebniswirksamen Stelle musste der Sollwert entscheiden, welche Lesart gemeint ist. Die neuen Teile – Stressfall mit neu bemessenem Darlehen, Bemessungszins je Tranche, KfW-Darlehen nach dem Merkblatt, Fördermittel in Teilraten mit Zwischenfinanzierung, Tilgung nach der Richtlinie, Zuschuss nach Vermögenssphäre, Verkaufsjahr mit E-69, Verein und Stiftung, Übermiete, Mietenhistorie, leere Flächen, Fluktuation – trafen im ersten Lauf: alle 70 Werte der Steuerstatus-Tabelle, alle 30 Werte des Mittelabrufs, die Werte des KfW-Falls einschließlich der drei tragbaren Preise (bis auf eine Schreibweise).
- **Die sieben Lücken der Runde 2 sind geschlossen**, ebenso die acht Dokumentationslücken und die sechs Widersprüche von damals; an zwei Stellen steht die alte Formulierung noch neben der neuen.
- **Von den fünf Abweichungen sind vier erklärt und liegen am Dokument:** ein veralteter Beispielwert (Endwertüberschuss im Stressfall, noch mit neun Stressgrößen gerechnet), ein in sich nicht stimmiger Beispielwert (Rohertrag des gebundenen Bestands), zwei Schreibweisen. **Eine ist nicht geklärt:** der Vergleich „frei finanziert gegen gefördert über 38 Jahre“ (9.238,60 Euro).
- **Neu geraten werden musste an acht Stellen**, vier davon mit Wirkung auf eine ausgewiesene Zahl, keine mit Wirkung auf Endwert, Rendite oder tragbaren Preis der Referenzfälle. Die gewichtigste: Ein Beispiel in R-5.12 rechnet mit zwei Stellgrößen, die es nicht mehr gibt (H-25 je Tranchenart, Lesart 2), und die Aussage von V-06, H-25 in Höhe des Vertragszinses ergebe dasselbe wie die frühere Lesart 2, stimmt im Fall mit übernommenem Darlehen nicht.

**Urteil:** Nach dem heutigen Text lässt sich ohne Rückfrage programmieren; vor der Übernahme der Beispiele als Tests sind die fünf abweichenden Werte und die Reste entfallener Kennungen im Text zu bereinigen, und der Vergleichswert über 38 Jahre ist am Referenzrechner zu klären.

## Getroffen je Fall

| Fall | Was nachgebaut wurde | Sollwerte | getroffen | abweichend |
|---|---|---|---|---|
| RF-11 Ankauf Basisfall | Mietpfad mit sieben Erhöhungen, Bewirtschaftung mit CO2-Kosten, Bemessung mit drei Grenzen, Tilgungsplan mit Anschluss, Nachschuss, Verlustvortrag, Verkauf, Endwert 2.524.305,59, Alternative 1.770.603,63, Rendite 4,527 %, Vergleichsfaktoren, Endwertüberschuss, alle Deckungen einschließlich „nach der ungünstigsten Anschlussregel“, Deckung und Reserve nach Bemessung, Faktoren, Restwertanteil, Gesamtkapitalrendite | 79 | 79 | 0 |
| RF-11 Stressfall | acht Stressgrößen, Neubemessung (1.144.835,99), Eigenkapital, Endwertdifferenz 237.324,51, Rendite 2,489 %, Deckungen, Darlehen zu Kaufpreis, Restschuld zum Wert, sechs Einzelstresse | 20 | 19 | 1 |
| RF-11 Haltedauertabelle | 8 bis 13 Jahre | 6 | 6 | 0 |
| RF-11 Preissuche | P* 2.317.235 mit Rendite bei P* und P* + 1, Endwertüberschuss 0,35, Boden, Eigenkapital, drei Faktoren, Preis je m², Stress-P* 1.977.816 mit Eigenkapital, Jahresmiete und Faktoren, Knick mit fünf Renditen und Steigungen, Eigenkapitalgrenze 2.138.910 | 40 | 39 | 1 |
| RF-11 Zielwertsuche, Jahresmodus | 9,60 Euro; 246.500 Euro; 19,06; „keine Lösung“; drei Prüffunktionen; Jahresmodus 2.514.395,05 und 4,491 % | 10 | 10 | 0 |
| RF-11 gebundener Bestand mit übernommenem Darlehen | gebundene Miete und Miete nach der Bindung, Miete des Vorhabens je Jahr, Rate aus dem Nennbetrag, Bemessungszins 1,00 / 0,75 / 0,50 %, KD_Ü, Bankdarlehen 843.802,85 / 865.231,42 / 886.660,00, Lesart 4 (672.374,28), Endwertdifferenz 562.960,01, Differenz zum freien Ankauf, Stresszins im Jahr 9, Vorfälligkeit nach fünf Jahren 50.629,99 | 54 | 53 | 1 |
| RF-13 Steuerstatus im vollen Plan | 14 Ausprägungen nach Anhang A.5, je Endwert, Endwert der Alternative, Endwertdifferenz, Rendite, Vergleichsrendite | 70 | 70 | 0 |
| RF-13 / RF-17 Verkaufsjahr im vollen Plan | Kürzung im Verkaufsjahr (7.952,00 und 139.930,00), M-51, Privatperson 9 bis 12 Jahre mit 334.954,62 Euro Steuer, Verkauf nach fünf Jahren (54.553,59 / 207.510,06 / 102.563,99), Verein nach zehn und elf Jahren | 18 | 18 | 0 |
| RF-12 Neubau frei finanziert | Baukosten und Raten, Bemessung, Mittelabruf, Bauzeit- und Bereitstellungszinsen, erste Rate, Miete, Abschreibung, Eigenkapital, Endwert 9.796.187,08, Rendite 4,332 %, a_0, Stressfall mit neu bemessenem Darlehen (3.740.000,00; 5.851.491,95; 2,247 %); Varianten Anlaufleerstand, Vorvermietung, Vorlauf, Festpreis, Kennwert der Gesamtkosten, nachhaltige Miete, Mindestansatz, Stellplätze, Zinsbindung vor Tilgungsbeginn, M-23; tragbarer Grundstückspreis 702.767, 606.989 und 876.926 Euro, Stressfall M-32 | 90 | 90 | 0 |
| RF-12 Neubau mit KfW-Darlehen | Abrufmonate, Bereitstellungsprovision, M-49, erste Rate 10.922,62 im Monat 20, Rate nach der Zinsbindung 14.305,24, Bemessungszins, Bankdarlehen 2.078.571,42, Rendite 4,995 %, Kapitaldienst je Tranche, vier Deckungen, vier Laufzeitvarianten, H-25 fest 4 %, Lesart 4, Bemessungszeitraum 15 Jahre, Zins 3 % als Abweichung, Vorfälligkeit nach acht Jahren, tragbarer Preis 1.197.094 / 1.283.299 / 920.435 Euro | 56 | 55 | 1 |
| RF-12 Neubau gefördert, 38 Jahre | Bemessung (zuwendungsfähige Kosten bis Bankdarlehen null mit M-21), Teilraten mit Bereitschaftsmonaten und Obergrenzen, erster Abruf, Lücke je Monat, Abrufe der Monate 10, 15 und 22 mit Aufteilung, höchster Stand 1.045.063,54 und Zinsen 42.095,30 der Zwischenfinanzierung, Tilgung ab Monat 23 in 500 Raten, gebundene Miete, Eigenkapital, sechs Deckungsangaben, Angaben nach R-11.15, Nachschüsse je Planjahr, Verteilung von Zuschuss und Entgelten, Endwert 9.477.900,38, Rendite 3,956 %, Stressfall (Teilraten 1 / 12 / 17 / 25, 501 Raten, 1,0258); Haltedauer 36 bis 39 und 20 Jahre, Zielrendite 3 % (2.118.474 Euro), Eingangsmiete 7,60 Euro mit M-50, M-20, M-22, 42 Jahre | 133 | 132 | 1 |
| RF-17 Zuschuss nach Vermögenssphäre | sechs Zeilen der Tabelle in R-7.19, Rückzahlung im laufenden Ergebnis, Privatperson mit sofortiger Verlustverrechnung ohne und mit E-70, zweimal M-20 | 28 | 28 | 0 |
| RF-10 / RF-17 Steuerbausteine | Körperschaft, Kürzung im Verkaufsjahr in drei Fällen, Anlaufverlust mit Kennzeichen, Tabelle der Personengesellschaft, Privatperson, privater Verkauf, Hinzurechnung, Verein und Stiftung, Objektverkauf bei 440 % und bei 400 %, sofortige Verrechnung bei Personengesellschaft und Einzelunternehmen, Grenzsteuersätze | 53 | 53 | 0 |
| RF-05 / RF-06 Testfall | Monatsraster (Monat 1, Rate 2, Jahr 1, Endwert 585.918,65, Alternative 428.794,92, Rendite 7,9333 %, Restschuld nach 120 Raten, Effektivzins); Jahresmodus mit Rundung (ganze Tabelle aus R-4.3, Deckungen, Restwertanteil, Gesamtkapitalrendite, 380.000 Euro mit Kontokorrent, Hebelreihe, Anlaufverlust mit Vortrag und sofort, steuerpflichtiger Verkauf, Vorfälligkeit, Basisperiode) | 90 | 90 | 0 |
| RF-19 Abweichungen und Bankensicht | neun Zeilen der Tabelle in R-3.2 (Wirkung auf Endwertdifferenz, tragbaren Preis und Abstand der Rendite), H-25 fest 4 % und 6 %, Preise zu den beiden anderen Anschlussregeln, Bankfall in drei Zeilen, Vorfälligkeit mit Kündigungsrecht in sechs Fällen, Verkauf im ersten Jahr, Warnschwellen | 53 | 53 | 0 |
| RF-18 Miete im Bestand | Mietenhistorie, Anpassungsdauer null, Übermiete mit und ohne Rückführung (Mieten, Reinerträge, Darlehen, Endwertdifferenz, zwei Preise), Lesart 3, Baujahr 1996, Erbbauzins, ganz leeres Objekt (930.929,99; 2.290.699 Euro), 200 m² leer, Fluktuation (2.563.369,40), sonstige Erträge, außerhalb des Kappungsgebiets (acht Erhöhungen, 2.319.295 Euro), Leerstand 29,5 %, Rundungsdifferenz | 43 | 43 | 0 |
| RF-14 / RF-17 / RF-20 Randfälle | anschaffungsnahe Herstellungskosten, Maßnahme nach dem Verkauf, Zins und Tilgung null, Verlust beim Verkauf, Leerstand 99,5 %, M-22, Nichtmonotonie (2.317.188 mit M-34, Lage der zwölf Preise), Eigenkapital bindet, M-32 mit −1,905 %, M-33, Obergrenze am Preis, kleinster zulässiger Preis 1.818.182, M-41 mit 1.569.899, M-46, M-31, Eigenkapitalgrenze mit Maßnahme, Sprungstelle 2.350.070 mit M-34, Katalogvergleich (47.134 und 37.800 Euro) | 41 | 41 | 0 |
| RF-08 / RF-09 Bausteine | Annuitäten, Ratentilgung, Anschluss nach drei Regeln, Förderdarlehen 2.320.000 Euro; sieben Zeilen der Tabelle der drei Grenzen, Knick, Monatsraster | 67 | 67 | 0 |
| **Summe** | | **951** | **946** | **5** |

## Stand der sieben Lücken aus Runde 2

| Nr. | Regel | Lücke in Runde 2 | Stand | Wo entschieden |
|---|---|---|---|---|
| 1 | R-6.7 | Anpassungsdauer der frei finanzierten Neubaumiete | geschlossen | R-6.7: „nach R-6.3 Zeile (3) ohne Anpassungsdauer (d = 0 …)“, Wartefrist ab Mietbeginn, Anfangsmiete als Bezug der Kappung |
| 2 | R-6.6 | Bindungsende im Neubau: Planjahr oder Bindungsjahr | geschlossen | R-6.6: „b ist das Planjahr, in dem der letzte Monat der Bindung liegt … Monat 438, Planjahr b = 37“; die Haltedauern 39 und 42 Jahre treffen damit (4,190 %; 12.824.337,47 Euro) |
| 3 | R-5.12 | „Schuld“ im kalkulatorischen Kapitaldienst | geschlossen | R-5.12: Bezugsbetrag ist der Nennbetrag; „Schuld“ im Beitragsglied ist beim übernommenen Darlehen die Restschuld, sonst der Nennbetrag; dazu die Formeln je Tilgungsart |
| 4 | R-5.12 | Rundung des Mietausfalls im nachhaltigen Reinertrag | geschlossen | Formelblock Roh_u, Einz_u; R-12.3 Zeile „Bemessung“. Das Zahlenbeispiel dazu ist in sich nicht stimmig (Abweichung 3) |
| 5 | R-7.15 | Rundungsrest der Entgeltverteilung; Entgelt auf den Zuschuss | geschlossen | R-7.15: „abziehbar im Verkaufsjahr n = der ganze noch nicht abgezogene Rest“; R-7.19: Entgelt folgt der Lesart des Zuschusses mit dem Schlüssel der Bindung |
| 6 | R-2.2 gegen R-6.4 | Jahresmiete im Jahresmodus | geschlossen | R-2.2: „die einmal gerundete Summe der zwölf ungerundeten Monatswerte (R-6.4), nicht die Summe gerundeter Monatsmieten“. R-12.5 sagt daneben weiter „der Jahreswert ist die Summe der Monatswerte (P-09)“; ein Halbsatz „für die Verdichtung des Monatsrasters“ würde den Rest beseitigen |
| 7 | R-7.3 gegen R-7.2 | Abschreibung einer aktivierten Maßnahme zum Stichtag | geschlossen | R-7.3 und R-6.16: „eine Maßnahme zum Stichtag (k = 0) ab dem Planjahr 1“. R-6.10 und der erste Satz dazu in R-6.16 sagen weiter nur „ab dem Folgejahr“ |

Ebenfalls erledigt: die Liste der 14 Ausprägungen von RF-13 mit Endwerten (Anhang A.5; die neunte Ausprägung, in Runde 2 nur durch Probieren gefunden, steht jetzt da); erster oder letzter Gitterwert der Zielwertsuche und ihre Suchbereiche (R-11.10, A.4); Stützstellen der Preissuche als Formel (R-11.5); Rundung der Aufteilung auf Darlehen und Zuschuss (R-11.3); Anpassungsdauer nach der Bindung im Neubau (H-23); Einzelunternehmen bei sofortiger Verrechnung (R-7.6); Faktor im Stressfall (R-11.7); die Stufen der gebundenen Miete im Beispiel zu R-6.5; die Zielzeile für das Planjahr 1 in R-6.3.

## Neue Stellen, an denen geraten werden musste

„Gewählt“ ist die Lesart der Blindrechnung; „Text“ heißt, der Sollwert bestätigt sie.

### Mit Wirkung auf eine ausgewiesene Zahl

| Nr. | Fundstelle | Was offen ist | Lesarten und Wirkung | Formulierungsvorschlag |
|---|---|---|---|---|
| 1 | R-5.12, Satz nach der Tabelle zur Zinsbindung; R-5.19 („Nach Lesart (2) …“); Kapitel 16, V-06 und V-07; R-3.4 zu H-25 | Das Beispiel rechnet „mit einem festen kalkulatorischen Zins von 4 % für übernommene Darlehen (H-25)“ und „nach Lesart (2)“. H-25 ist nach R-3.4 und V-07 ein Wert für alle Tranchen, Lesart 2 ist nach V-06 entfallen und soll durch H-25 in Höhe des Vertragszinses „deckungsgleich auf den Cent“ ersetzt sein | Gebundener Bestand, Zinsbindung acht Jahre: H-25 fest 4 % als ein Wert für alle Tranchen: i_k der Bank 4 %, i_B 1,2 %, KD_Ü 19.200,00, Bankdarlehen **964.436,66 Euro** · Text: 826.660,00 Euro (nur mit H-25 allein für das übernommene Darlehen: (RE_n / 1,2 − 19.200) / 7 %) · „Lesart (2)“: 1.034.436,66 Euro (KD_Ü 15.000,00, 6 %). V-06 trifft nur zu, wo keine übrige Tranche vor dem Ende des Bemessungszeitraums aus ihrer Bindung läuft (Ankauf ohne übriges Darlehen 1.431.044,99 und Neubau mit KfW 2.425.000,00 Euro: getroffen) | Beispielsatz ersetzen: „Mit einem festen kalkulatorischen Zins von 4 % (H-25, ein Wert für alle Tranchen) sind es bei acht Jahren 964.436,66 Euro: Die Bank bemisst ihr Darlehen mit 4 % und 2 %, das übernommene Darlehen geht mit i_B = 1,2 % und 19.200,00 Euro ein.“ V-06 ergänzen: „deckungsgleich, solange keine übrige Tranche vor dem Ende des Bemessungszeitraums aus ihrer Zinsbindung läuft; sonst rechnet H-25 deren Anschluss mit dem festen Satz statt mit dem Vertragszins (gebundener Bestand: 964.436,66 statt 1.034.436,66 Euro)“ |
| 2 | R-10.14 Nr. 4 | „Deckung im ersten Planjahr nach dem Ende jeder Zinsbindung“, wenn die Bindung mitten im Planjahr endet (zinslose Zeit des Förderdarlehens: Monat 438 im Planjahr 37) | Planjahr der ersten Periode nach dem Ende (gewählt, Text): Planjahr 37, **1,8848** – das Jahr trägt nur sechs Monate Zins · erstes Planjahr, das ganz nach dem Ende liegt: Planjahr 38, **1,6943** | „… im Planjahr, in das die erste Periode nach dem Ende der Zinsbindung fällt. Endet die Bindung nicht am Ende eines Planjahres, nennt das Blatt zusätzlich das folgende Planjahr; erst dieses trägt den neuen Zins voll.“ |
| 3 | R-11.8 mit R-5.8 und E-59 | Übernommenes Darlehen, dessen Anschlusszins nicht überschrieben ist (Voreinstellung E-45 + H-05): „folgt“ er im Stressfall dem Bankdarlehen (beide Aufschläge, auch in der Bemessung), oder gilt er als „eingegeben“ (nur Anschlussstress)? | folgt der Bank, 6,5 % (gewählt): Bankdarlehen im Stressfall 747.549,33, Endwertdifferenz 107.615,44 Euro · gilt als eingegeben, 6,0 %: 755.549,33 und 111.601,99 Euro (gebundener Bestand mit voreingestelltem Anschlusszins; kein Sollwert im Dokument) | R-11.8: „Ist der Anschlusszins des übernommenen Darlehens nicht überschrieben, folgt er dem Bankdarlehen und steigt um beide Aufschläge; ein überschriebener Wert steigt nur um den Anschlussstress.“ |
| 4 | R-10.16 | „Steuer, die ohne Verkaufsgewinn anfiele“ bei gesetztem Kennzeichen E-41 ohne E-69: Bleibt es in der Vergleichsrechnung das Verkaufsjahr (Kürzung entfällt), oder ist es ein Jahr ohne Verkauf (Kürzung bleibt)? | Verkaufsjahr mit g_v = 0 (gewählt): Steuer auf den Verkaufsgewinn 245.400,69 Euro, Restwertanteil 79,30 % · Jahr ohne Verkauf: 253.352,69 Euro und 78,99 % (Ankauf als Körperschaft mit Kennzeichen; kein Sollwert im Dokument) | „… abzüglich der Steuer desselben Planjahres mit g_v = 0 und sonst unveränderter Rechnung; die Regeln des Verkaufsjahres (R-7.8) gelten auch in dieser Vergleichsrechnung.“ |

### Ohne Wirkung auf ein Ergebnis (Darstellung, Bausteine)

| Nr. | Fundstelle | Was offen ist | Lesarten und Wirkung | Formulierungsvorschlag |
|---|---|---|---|---|
| 5 | R-5.12, „abrunden_Cent“; Tabelle zu RF-09 | Richtung der Abrundung bei negativem B | zur Null hin: −92.857,14 (Text, erst der Sollwert zeigte es) · nach unten: −92.857,15. Das Darlehen ist in beiden Fällen null | „abrunden_Cent schneidet nach dem Cent ab (zur Null hin).“ |
| 6 | R-5.12, Tabelle zu RF-09 | Der Text nennt den Kapitaldienst des Förderdarlehens gerundet (155.571,43 Euro); die Tabelle rechnet mit 5.400.000 / 42 + 27.000 ungerundet | ungerundet (Text, erst der Sollwert zeigte es): B 2.962.698,41, Schwelle 186.685,71 · mit dem gerundeten Wert: 2.962.698,38 und 186.685,72 | Im Beispiel: „Kapitaldienst 155.571,428571 Euro (Eingabe des Bausteins, ungerundet)“ |
| 7 | R-12.7, Beispiel RF-18 | „Jahresmieten des Ankaufs“: Sollmiete oder Mieteinzahlung | Mieteinzahlungen (Text, erst der Sollwert zeigte es): 1.850.876 und 1.850.875 Euro · Sollmieten: 1.888.649 und 1.888.647 Euro | „Mieteinzahlungen je Planjahr (Zeile Z-A2)“ |
| 8 | R-12.4 mit R-5.12 (`runde12` des Bemessungszinses) | Zwölf Stellen des Satzes als Dezimalzahl oder des Prozentwerts | Dezimalzahl 0,033333333333 (gewählt, wie der Monatssatz in R-2.6) · Text schreibt 3,333333333333 %. KD_Ü ist in beiden Fällen 159.999,96 Euro | Beispiel als „3,3333333333 %“ schreiben oder in R-12.4: „Sätze werden als Dezimalzahl gerundet“ |

Knapp gesagt, aber aus dem Text entschieden und vom Sollwert bestätigt: der kalkulatorische Zins im Stressfall ohne den Anschlussstress (5,5 %; mit 6,5 % wären es 1.010.149,41 statt 1.144.835,99 Euro); die Bemessung im Stressfall mit Ertrag, Wertansatz, Mittelbedarf und Bauzeit des Basisfalls; der ganze Rest des Entgelts auf den Zuschuss im Verkaufsjahr auch beim Verkauf in der Bindung; neu vermietete Flächen ohne Sperrjahr und ohne Anpassungsdauer; Fluktuation als Anteil des jeweils verbliebenen Bestands; die Lücke der Zwischenfinanzierung als Obergrenze des Kontokorrents auch in den Monaten zwischen Bauende und letzter Teilrate; das Planjahr nach R-11.15 (mit und ohne die Abgrenzung „ganz in der Vermietung“ Planjahr 9).

## Abweichungen

| Nr. | Fundstelle | Wert der Blindrechnung | Sollwert | Ursache |
|---|---|---|---|---|
| 1 | R-10.9, Beispiel RF-11: Endwertüberschuss im Stressfall | −716.938,74 Euro | −739.303,12 Euro | **geklärt, Fehler im Text.** Der Sollwert stammt aus dem Stand mit neun Stressgrößen: Mit 10 % mehr Instandhaltung ergibt die Blindrechnung genau −739.303,12 Euro und die Endwertdifferenz 216.856,20 Euro, die R-15.6 als Wert „mit neun Stressgrößen“ nennt. Alle anderen Werte des Stressfalls (237.324,51 Euro; 2,489 %; Deckungen; 1.977.816 Euro) sind auf dem Stand mit acht Größen und getroffen |
| 2 | R-11.11, Beispiel RF-12: Differenz der Endwertdifferenz frei gegen gefördert, je 38 Jahre | −10.735.928,53 Euro | −10.726.689,93 Euro | **nicht geklärt (9.238,60 Euro).** Die Seite „gefördert“ ist getroffen (5.656.209,72 Euro). Für „frei, 38 Jahre“ rechnet die Blindrechnung Endwert 25.525.695,66, Alternative 9.133.557,41, Endwertdifferenz 16.392.138,25 Euro; der Sollwert setzt 16.382.899,65 Euro voraus, das Dokument nennt den Wert selbst nicht. Der Wert der Blindrechnung ist derselbe wie in Runde 2, als die Differenz getroffen wurde. Vermutung: Der Beispielwert ist wie Nr. 1 aus einem Zwischenstand stehen geblieben (das hieße 5.665.448,32 Euro für „gefördert“ zum Zeitpunkt des Vergleichs). Die andere Möglichkeit ist eine Regel, die nur im frei finanzierten Lauf nach dem Jahr 15 wirkt; davon gibt es nach meiner Lesart nur eine – das Bankdarlehen ist im Monat 422 getilgt –, alles Übrige (Abschreibungsende, Altersstaffel, Steuersätze, Guthaben, Alternative) ist durch die geförderten Läufe über 38 und 42 Jahre auf den Cent bestätigt. Zu klären am Referenzrechner mit den drei Werten oben |
| 3 | R-5.12, Beispiel zum Bemessungszins: Rohertrag_n des gebundenen Bestands | 123.868,80 Euro | 123.869,76 Euro | **geklärt, Beispiel in sich nicht stimmig.** 12 x 1.320 m² x 7,82 Euro = 123.868,80 Euro; damit ergeben sich Mietausfall_n 2.477,40, RE_n 92.479,44 und B 843.802,85 Euro wie im Text. Mit 123.869,76 Euro wäre RE_n 92.480,40 Euro. Auch „Satz mal Jahresrohertrag ergäbe 2.477,3952“ gehört zu diesem Wert; richtig wäre 2.477,3760 |
| 4 | R-11.5, Beispiel RF-11: Steigung links vom Knick | −7,10 Basispunkte (−7,104) | −7,11 | geklärt: Der Text bildet die Differenz der auf vier Stellen gerundeten Renditen (8,3164 − 8,2453); rechts stimmen beide Wege (−9,61) |
| 5 | R-5.19: Bemessungszins bei 15 Jahren Bemessungszeitraum | 3,3333333333 % | 3,333333333333 % | geklärt: Schreibweise (Stelle 8 oben); KD_Ü 159.999,96 und Bankdarlehen 1.721.429,14 Euro sind getroffen |

## Reste entfallener Kennungen und Beispiele, die nicht zu Anhang A passen

Keine dieser Stellen ändert eine Zahl; sie führen aber einen Entwickler auf Größen, die es nicht mehr gibt.

| Fundstelle | Befund |
|---|---|
| R-5.12, Formelblock „Bewirtschaftung_n“; R-6.7; R-10.22; Anhang A.4, Zeile „H-32 bis H-37“ | verweisen auf die Betriebskosten leerstehender Flächen (R-6.17, H-36), die entfallen sind; A.4 nennt dafür noch „0 Euro, in den bezeichneten Fällen 30 Euro je m² und Jahr“ |
| R-6.16 | „das Eingabefeld E-52 sagt das“ – E-52 ist entfallen |
| R-2.5 (Tabelle, Zeile Investitionsstau), R-7.3 (Beispiel RF-14), Kapitel 17 NF-15 | „Modernisierung … aktiviert“ – das Kennzeichen gibt es nicht mehr (V-13); aktiviert wird nur noch nach R-6.16 |
| R-5.12 (Tabelle RF-09, dritte Zeile), Anhang A.3 RF-09 | „im Rang vor der Bank“, „Rang vor und nach der Bank“ – der Rang ist keine Eingabe mehr (V-03) |
| R-15.3, Zeile RF-17 | „Zuschuss in drei Lesarten mit Voreinstellung nach Kennzeichen“ – R-7.19 kennt zwei Lesarten, und die Voreinstellung hängt nicht am Kennzeichen |
| Anhang A.5, Zeile RF-13 | „Steuerstatus nach der Tabelle in R-7.9 … Lesarten von `MA-030`“ – die Tabelle steht in A.5 selbst, `MA-030` hat keine Lesart mehr (E-69) |
| R-7.18 gegen Anhang A.3 (RF-17) und R-15.6 | Das Beispiel rechnet mit Hebesatz 440 % (243.285,00 und 222.285,00 Euro), A.3 nennt 400 %, R-15.6 die Werte dazu (236.628,00 und 219.828,00 Euro). Beide Paare sind getroffen; Text und Anhang nennen verschiedene Fälle |
| Kapitel 17, NF-07 und NF-06 | „zwei weitere Regeln wählbar“ gegen R-5.9 („keine Wahl mehr“); „Kontokorrentlinie als Vorgabe“ gegen H-11 (fester Hauswert) |
| R-11.14 | „eigene Ausprägung von H-01 (R-3.3)“ – H-01 steht in R-3.4 |
| R-11.9 | nennt „Verlustverrechnung“ als Auswahlfeld; sie ist Hauswert H-38 und kein Feld mehr |

## Was nicht nachgebaut wurde

- Die Lehrbuchfälle RF-01 bis RF-04 und RF-07 (Eigenschaften der Renditeformel mit geplanten Entnahmen; mein Kern führt wie die Grobkalkulation keine Entnahmen).
- Die Proben P-01 bis P-21 als eigene Prüfungen, die Sperre M-10 mit den Fehlerbildern (RF-16) und die Eingabeprüfung im Ganzen (RF-20); Meldungen sind dort verglichen, wo sie aus der Rechnung folgen (M-20 in vier Fällen, M-21 bis M-23, M-25, M-29, M-31 bis M-34, M-36, M-38, M-39, M-41, M-42, M-46, M-49 bis M-51).
- Die Liste der Abweichungen nach R-3.2 als Mechanik mit Begründungspflicht (gerechnet sind die Wirkungen der neun Zeilen), der Vergleich zweier Fassungen als Ausgabe (36 Größen, 86 Zeilen), der interne Zinsfuß, die Amortisationsdauer.
- Die Zahlen zur anderen Lesart von `MA-040` (das Dokument sagt selbst, dass sie aus dem Stand vor der Durchsicht stammen).

## Eigene Werte ohne Sollwert im Dokument (zum Abgleich mit dem Referenzrechner)

| Fall | Endwert | Endwert der Alternative | Endwertdifferenz | Rendite | Vergleichsrendite | Bankdarlehen |
|---|---|---|---|---|---|---|
| Ankauf Stressfall | 2.126.728,79 | 1.889.404,28 | 237.324,51 | 2,489 % | 1,483 % | 1.144.835,99 |
| Ankauf gebunden mit übernommenem Darlehen | 2.200.607,66 | 1.637.647,65 | 562.960,01 | 4,013 % | 1,483 % | 843.802,85 |
| Ankauf gebunden, Stressfall | 1.852.797,89 | 1.725.249,94 | 127.547,95 | 2,088 % | 1,483 % | 787.549,33 |
| Ankauf gebunden, Haltedauer fünf Jahre | 1.286.048,59 | 1.474.592,15 | −188.543,56 | −1,292 % | 1,446 % | 843.802,85 |
| Ankauf gebunden, Lesart 4 von `MA-026` | 2.415.460,39 | 1.820.297,92 | 595.162,47 | 3,904 % | 1,483 % | 672.374,28 |
| Ankauf im Jahresmodus | 2.514.395,05 | 1.770.987,08 | 743.407,97 | 4,491 % | 1,483 % | 1.226.609,49 |
| Neubau frei, 15 Jahre | 9.796.187,08 | 6.471.824,38 | 3.324.362,70 | 4,332 % | 1,488 % | 4.007.142,85 |
| Neubau frei, 15 Jahre, Stressfall | 8.211.748,74 | 7.343.460,94 | 868.287,80 | 2,247 % | 1,488 % | 3.740.000,00 |
| Neubau frei, 38 Jahre | 25.525.695,66 | 9.133.557,41 | 16.392.138,25 | 4,283 % | 1,501 % | 4.007.142,85 |
| Neubau mit KfW-Darlehen, 15 Jahre | 8.527.589,11 | 5.122.699,97 | 3.404.889,14 | 4,995 % | 1,488 % | 2.078.571,42 |
| Neubau mit KfW-Darlehen, Stressfall | 6.747.476,13 | 5.837.454,20 | 910.021,93 | 2,473 % | 1,488 % | 1.940.000,00 |
| Neubau gefördert, 38 Jahre | 9.477.900,38 | 3.821.690,66 | 5.656.209,72 | 3,956 % | 1,501 % | 0,00 |
| Neubau gefördert, 38 Jahre, Stressfall | 8.534.994,94 | 4.556.377,52 | 3.978.617,42 | 3,191 % | 1,501 % | 0,00 |
| Neubau gefördert, 20 Jahre | 3.275.573,58 | 2.918.482,73 | 357.090,85 | 2,081 % | 1,493 % | 0,00 |
| Neubau gefördert, sofortige Einnahme, 20 Jahre | 3.622.803,66 | 3.519.683,16 | 103.120,50 | 1,640 % | 1,493 % | 0,00 |
| Neubau gefördert als Privatperson | 11.628.291,89 | 4.896.950,44 | 6.731.341,45 | 3,808 % | 1,472 % | 0,00 |
| Neubau gefördert als Privatperson mit E-70 | 11.062.573,59 | 3.781.068,02 | 7.281.505,57 | 4,380 % | 1,472 % | 0,00 |

Dazu: geförderter Neubau, operatives Ergebnis der Planjahre 1 bis 3: −17.622,06 / −114.057,77 / −50.278,46 Euro; Zinsen der Zwischenfinanzierung bis zum Bauende 24.143,54 Euro (von 42.095,30 Euro); Eigenkapital der Investitionsphase im Stressfall 2.559.806,34 Euro. Eigenkapital der Investitionsphase und Endwert der vier Zeilen der Tabelle in R-7.19, die das Dokument offen lässt: Körperschaft mit Kennzeichen, verteilt 2.144.688,71 und 9.632.742,48 Euro; mit Kennzeichen, sofortige Einnahme 2.305.407,01 und 9.797.955,02 Euro; Privatperson 2.571.239,66 und 11.628.291,89 Euro; Privatperson mit E-70 2.144.688,71 und 11.062.573,59 Euro. Neubau frei im Stressfall: Rendite beim kleinsten Preis 3,683 % (M-32); Neubau mit KfW-Darlehen im Stressfall: ebenfalls kein tragbarer Grundstückspreis (M-32). Im Jahresmodus bemisst die Blindrechnung das Bankdarlehen des Ankaufs mit 1.226.609,49 Euro, 50 Cent unter dem Monatsraster, weil die kalkulatorische Rate einmal je Jahr gerundet wird.
