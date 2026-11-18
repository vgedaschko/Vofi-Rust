# Blindrechnung zur Fachspezifikation Rechenkern (Prüfrunde 2)

**Stand:** 2026-11-18
**Quelle:** allein `docs/fachspezifikation-rechenkern.md` (Regeln, Beispiele, Anhang A). Der Ordner des Referenzrechners, `erwartete_werte.json` und die Prüfberichte unter `docs/pruefung/` wurden nicht gelesen.
**Werkzeug:** eigener Nachbau von Grund auf in Python (`decimal` mit 60 Stellen, nur Standardbibliothek). Code im Scratchpad `fs2-blind/`: `kern.py` (Mietpfad, Darlehen, Bemessung, Mittelabruf, Finanzplan, Steuer je Status, Unterlassensalternative, Kennzahlen, Preissuche), dazu je Fall ein Skript (`rf11.py`, `rf11b.py`, `rf11g.py`, `rf12.py`, `rf12f.py`, `rf12k.py`, `rf13.py`, `rf17.py`, `rf06.py`, `extra.py`, `lesarten.py`, `blindwerte.py`).

## Ergebnis

Rund 340 Sollwerte des Dokuments nachgerechnet, **alle getroffen** – Geldbeträge auf den Cent, Renditen und Deckungen auf die ausgewiesenen Stellen, Preise auf den Euro. Keine Abweichung blieb stehen.

Das gilt aber nur, weil an **sieben Stellen** erst der Sollwert gezeigt hat, welche von mehreren möglichen Lesarten gemeint ist. Der Text allein hätte dort nicht entschieden; drei dieser Stellen ändern das Ergebnis deutlich (bis zu 1 Mio. Euro Endwert), vier nur um Cent. Dazu kommen kleinere Unschärfen ohne Wirkung auf die geprüften Werte. Diese Stellen sind der eigentliche Befund (Abschnitt „Stellen, an denen geraten werden musste“).

**Urteil:** Die Rechenregeln sind so genau, dass ein unabhängiger Nachbau alle Referenzwerte trifft – das spricht für die Regeln und für den Referenzrechner. Ohne Rückfrage implementieren lässt sich aber erst, wenn die sieben Lücken unten im Text geschlossen sind; bis dahin entscheiden die Sollwerte, nicht die Regeln, und wer nur grob vergleicht, baut an drei Stellen die falsche Lesart.

## Getroffen je Fall

| Fall | Was nachgebaut wurde | Sollwerte | getroffen | abweichend |
|---|---|---|---|---|
| RF-12 gefördert, 38 Jahre | Bemessung (zuwendungsfähige Kosten, Förderdarlehen, Zuschuss, Mindesteigenkapital, Entgelte, Mittelbedarf, Rohertrag, nachhaltiger Reinertrag, Kapitaldienst des Förderdarlehens, A, B, C, Bankdarlehen null), Mittelabruf, Zufluss des Zuschusses je Planjahr, Steuer der Planjahre 1 und 2, Nachschüsse je Planjahr, Eigenkapital der Investitionsphase, Deckungen (erstes Jahr, kleinste mit Planjahr, Stress), Angaben nach R-11.15 einschließlich nötiger Miete 10,40 Euro, Endwert 9.943.743,02, Endwertdifferenz 5.305.318,55, Rendite 3,558 %, Renditen 36 bis 39 Jahre, Verkauf nach 20 Jahren (Rendite, Endwertdifferenz, Rückzahlung, Verkaufspreis, Ablösung), Vergleich mit frei finanziert, Lesart 1 von `MA-026`, Meldungen M-21 und M-38 | 48 | 48 | 0 |
| RF-12 frei finanziert, 15 Jahre | Baukosten und Raten, Bankdarlehen, Abruf, Bauzeit- und Bereitstellungszinsen, Miete und Erhöhungsmonate, Abschreibung, Eigenkapital, Nachschussbedarf, Endwert 9.796.187,08, Rendite 4,332 %, a_0, Gesamtkapitalrendite, Faktoren, Stressfall (Baukosten, Eigenkapital, Rendite), tragbarer Grundstückspreis 702.767 Euro | 41 | 41 | 0 |
| RF-12 mit KfW-Tranche | Bemessung, Abrufmonate, Zins, Tilgungsbeginn, Rate, Kapitaldienst je Tranche, Rendite 4,630 %, tragbarer Preis 924.244 Euro, Lesart 2 (2.425.000,00 Euro; 1.286.380 und 876.926 Euro), Stellplätze | 14 | 14 | 0 |
| RF-17, Zuschuss in drei Lesarten (`MA-031`), Sofortabzug der Entgelte | Rendite, Endwertdifferenz, Eigenkapital, Endwert je Lesart für 38 Jahre, Rendite für 20 Jahre; Gebäudeanteil; anschaffungsnahe Herstellungskosten | 16 | 16 | 0 |
| RF-11 Basisfall | Mietpfad mit allen sieben Erhöhungen, Bewirtschaftung, Bemessung, Tilgungsplan mit Anschluss, Nachschuss, Verlustvortrag, Verkauf, Steuer auf den Verkaufsgewinn, Endwert 2.524.305,59, Alternative 1.770.603,63, Rendite 4,527 %, Vergleichsfaktoren, Endwertüberschuss, alle Deckungs- und Bankkennzahlen, Restwertanteil, Gesamtkapitalrendite | 60 | 60 | 0 |
| RF-11 Stressfall, Haltedauertabelle, Preissuche | Stress (Endwertdifferenz, Rendite, Endwertüberschuss, Deckungen, Restschuld zum Wert), Haltedauer 8 bis 13 Jahre, P* 2.317.235 Euro mit Rendite bei P* und P* + 1, Endwertüberschuss 0,35 Euro, Boden, Eigenkapital, Faktor, Preis je m², Knick (fünf Renditen), Stress-P* 1.978.674 Euro, Eigenkapitalgrenze 2.138.910 Euro, Zielwertsuchen (9,60 Euro; 246.500 Euro; 19,06), Jahresmodus | 44 | 44 | 0 |
| RF-11 gebundener Bestand mit übernommenem Förderdarlehen | gebundene Miete und Miete nach Bindungsende (alle Sprünge), Miete des Vorhabens je Jahr, Rate und Kapitaldienst des übernommenen Darlehens, Endwertdifferenz 581.756,83, Differenz zum freien Ankauf, Stresszins im Jahr 9, Vorfälligkeit nach fünf Jahren mit und ohne Kennzeichen | 26 | 26 | 0 |
| RF-13 Steuerstatus im vollen Plan | 13 der 14 Renditen direkt, die 14. nach Probieren (siehe Lücke 8); Vergleichsrenditen 1,483 % und 1,763 %; Privatperson 9 bis 12 Jahre; Steuer auf den Verkaufsgewinn 334.954,62 Euro; Gewerbesteuer auf den Verkaufsgewinn 139.930,00 Euro | 21 | 21 | 0 |
| RF-05/RF-06 Testfall | Monatsraster (Monat 1, Jahr 1, Endwert 585.918,65, Alternative 428.794,92, Endwertdifferenz, Rendite 7,9333 %), Jahresmodus mit Rundung, Variante 380.000 Euro mit Kontokorrent, Hebelreihe | 27 | 27 | 0 |
| Stichproben RF-14, RF-18, RF-19, RF-20 | Anschlussregeln, Lesart 2 und H-25, sieben Einzelstresse, Vorfälligkeit mit Kündigungsrecht, andere Lesart von `MA-037`, Zins und Tilgung null, Verlust beim Verkauf, Nichtmonotonie (P* 2.317.188 mit M-34), M-32, M-33, Leerstand 99,5 %, Maßnahme nach dem Verkauf, Neubau über 42 und 3 Jahre, Eigenkapitalgrenze mit Maßnahme, kleinster zulässiger Preis 1.818.182 Euro, Nebenangabe 1.569.899 Euro | rund 45 | alle | 0 |

## Stellen, an denen geraten werden musste

Jede Zeile ist eine Lücke des Texts. „Entscheidet“ heißt: Nur diese Lesart trifft den Sollwert.

### Mit Wirkung auf das Ergebnis

| Nr. | Regel | Was fehlt oder mehrdeutig ist | Lesarten und Wirkung | trifft |
|---|---|---|---|---|
| 1 | R-6.7 (mit R-6.3, E-53) | Neubau, frei finanziert: „die Miete folgt ihr nach R-6.3“. R-6.3 braucht die Anpassungsdauer d; E-53 gilt laut Tabelle nur für den Ankauf, H-23 setzt vier Jahre vor. Ob im Neubau d = 0 gilt (Ziel = Vergleichsmiete des Vermietungsjahres), steht nirgends | d = 0: Endwert 9.796.187,08 Euro · d = 4 (H-23): 9.773.829,65 Euro | d = 0 |
| 2 | R-6.6, R-6.7, R-11.14 | Geförderter Neubau, Miete nach dem Bindungsende: „Endet die Bindung nach dem Jahr b“. Im Neubau endet die Bindung mitten im Planjahr (Monat 438). Ob b das Planjahr des Bindungsendes (37) oder das Bindungsjahr 35 ist, ist nicht gesagt; R-6.5 zählt für die Stufen ausdrücklich Bindungsjahre ab Bezugsfertigkeit | b = Planjahr 37, Erhöhungen ab Monat 457: Endwert 9.943.743,02 Euro, 3,558 % · b = Bindungsjahr 35, Erhöhungen ab Monat 451: 10.964.813,36 Euro, 3,825 % | Planjahr |
| 3 | R-5.12 | Kalkulatorischer Kapitaldienst der übrigen Darlehen: „p x runde(Schuld x (i_k + τ_k) / p)“. „Schuld“ ist nicht definiert; beim übernommenen Darlehen kommen Restschuld (500.000 Euro) und ursprünglicher Nennbetrag (600.000 Euro, Bezug des Tilgungssatzes nach R-5.11) in Frage. Unklar auch, ob „zuzüglich des laufenden Beitrags“ zu beiden Gliedern des Vergleichs gehört | Restschuld: KD_Ü 24.999,96, Bankdarlehen 743.803,42, Endwertdifferenz 581.756,83 Euro · Nennbetrag: KD_Ü 30.000,00, Endwertdifferenz 595.162,47 Euro | Restschuld |

### Mit Wirkung im Cent-Bereich (bei „exakt“ als Toleranz trotzdem Testbruch)

| Nr. | Regel | Was fehlt oder mehrdeutig ist | Lesarten und Wirkung | trifft |
|---|---|---|---|---|
| 4 | R-5.12 | „Mietausfall auf den Rohertrag_n“: Rundung nicht festgelegt. In RF-11 und RF-12 fällt es nicht auf, weil die Beträge glatt sind; im gebundenen Bestand entscheidet es | Rohertrag x Ausfallsatz ungerundet: RE_n 92.479,464, Darlehen 743.803,71, Endwertdifferenz 581.756,72 · auf Cent gerundet: 743.803,66, ebenfalls 581.756,72 · je Monat wie R-6.4 (Sollmiete runden, Einzahlung runden, Ausfall als Differenz): RE_n 92.479,44, Darlehen 743.803,42, Endwertdifferenz 581.756,83 | je Monat wie R-6.4 |
| 5 | R-7.15 | Verteilung der einbehaltenen Entgelte: Die gerundeten Jahresbeträge summieren sich nicht auf den Betrag. „Der nicht verteilte Rest wird im Verkaufsjahr abgezogen“ meint dem Wortlaut nach den Verkauf vor Ende der Zinsbindung; ob auch der Rundungsrest nach vollständiger Verteilung dort abgezogen wird, steht nicht da. Ebenso nicht gesagt: Das Entgelt auf den Zuschuss wird über die zinslose Zeit des Förderdarlehens verteilt (folgt nur aus der Summe 65.393,64 im Beispiel) | Rundungsrest im Verkaufsjahr: Endwert 9.943.743,02 · ohne: 9.943.743,00 | Rest im Verkaufsjahr |
| 6 | R-2.2, R-12.5 gegen R-6.4 | Jahresmodus: R-2.2 nennt die Sollmiete des Jahres „die Summe der zwölf Monatswerte“ und R-12.5 „der Jahreswert ist die Summe der Monatswerte“; R-6.4 rechnet runde(Summe über die Monate der Periode), also einmal gerundet aus ungerundeten Monaten | Summe gerundeter Monatswerte: Endwert 2.514.395,03 · einmal gerundete Summe: 2.514.395,05 | R-6.4 |
| 7 | R-6.10, R-6.16, R-7.3 gegen R-7.2 | Aktivierte Maßnahme zum Stichtag (k = 0): abgeschrieben „ab dem Folgejahr“ / „ab dem Jahr nach ihrer Zahlung“. Nach R-7.2 zählen Zahlungen zum Stichtag zum Planjahr 1; dann wäre das Folgejahr Planjahr 2 | Abschreibung ab Planjahr 2: Rendite beim kleinsten Preis −1,975 % · ab Planjahr 1: −1,905 % (RF-14, Maßnahme 6 Mio. Euro) | ab Planjahr 1 |

### Dokumentationslücken ohne Rechenregel dahinter

| Nr. | Stelle | Befund |
|---|---|---|
| 8 | R-15.3 (RF-13), Anhang A.5 | Die 14 Ausprägungen von RF-13 sind nirgends mit ihren Eingaben aufgelistet. A.5 verweist auf „die Tabelle in R-7.9“; die zeigt nur die Anrechnung. 13 Renditen ließen sich aus dem Fließtext von R-7.6 bis R-7.18 zuordnen. Die neunte (3,659 %) fand sich nur durch Probieren: originär gewerbliche Personengesellschaft, Hebesatz 440 %, Anteil 100 %, Verlustverrechnung „sofort“ |
| 9 | R-7.5 bis R-7.11, R-9.5 | Für Personengesellschaft, Einzelunternehmen und Privatperson nennt das Dokument nur Renditen mit drei Stellen, keinen Endwert und keinen Endwert der Unterlassensalternative. Die Besteuerung der Alternative bei diesen Status (Freibetrag der Gewerbesteuer, Anrechnung, Satz auf Kapitalerträge) ist damit aus dem Text nicht prüfbar; meine Werte stehen unten zum Abgleich |
| 10 | R-11.10 | „den letzten Gitterwert, bei dem das Ziel noch erreicht ist“: Bei einem Wechsel von verfehlt nach erreicht (Vergleichsmiete, Verkaufsfaktor) ist der ausgewiesene Wert der erste erreichte Gitterwert (9,60 Euro; 19,06). Der Suchbereich des Verkaufsfaktors und die Rasterzahl der Zielwertsuche fehlen im Anhang A (A.4 nennt nur die 40 Schritte der Preissuche, A.5 nur die Bereiche für Vergleichsmiete und Investitionsstau) |
| 11 | R-11.5 | „gleichmäßig verteilte Stützstellen von U bis O + 1“: Wie die Stützstellen auf volle Euro gebracht werden und ob 40 Rasterschritte 41 Stützstellen bedeuten, ist nicht gesagt. Auf P* ohne Wirkung; bei Nichtmonotonie kann es entscheiden, ob M-34 erscheint |
| 12 | R-11.3 | Aufteilung des Abrufs auf Förderdarlehen und Zuschuss „im Verhältnis ihrer Beträge“: Welcher Teil gerundet wird und welcher den Rest trägt, fehlt. Beide Varianten treffen hier (Zufluss 1.091.037,68 und 652.792,79 Euro); bei anderen Beträgen kann ein Cent wandern |
| 13 | R-6.6, R-6.7 | Geförderter Neubau nach der Bindung: Anpassungsdauer und Vergleichsmiete sind nicht genannt. Mit vier Jahren (H-23) und mit null ergeben 39 und 42 Jahre dieselben Werte, weil die Kappung bindet; bei kleinerem Abstand zur Marktmiete wäre das nicht so |
| 14 | R-7.6 | Sofortige Verrechnung beim Einzelunternehmen: Das Beispiel (−21.000,00 Euro) verlangt, dass die Begrenzung der Anrechnung auf die Einkommensteuer bei negativem Ergebnis entfällt. Die Formel ohne dieses Glied nennt R-7.6 nur für die Personengesellschaft |
| 15 | R-11.7 | Faktor im Stressfall (15,23): Bezug ist die maßgebliche Jahresmiete des Stressfalls mit erhöhtem Leerstand; mit der des Basisfalls wären es 14,92. Der Text sagt „alles im Basisfall und im kombinierten Stressfall“, nicht ausdrücklich, dass auch der Nenner gestresst ist |

Eindeutig genug, obwohl nur knapp gesagt: der Anschlusszins im Stressfall (gestresster Zins + H-05 + Aufschlag, hier 6,5 %; mit 6,0 % wären es 203.854,02 statt 196.967,13 Euro Endwertdifferenz) und der Stand der Fördermittel im Stressfall (Basisfall; neu bemessen ergäbe die kleinste Deckung 0,9728 statt 1,0192).

## Widersprüche zwischen Regeln oder zwischen Regel und Beispiel

| Stelle | Widerspruch |
|---|---|
| R-2.2 und R-12.5 gegen R-6.4 | Jahresmiete im Jahresmodus: Summe gerundeter Monatswerte gegen einmal gerundete Summe (Lücke 6). Der Sollwert folgt R-6.4 |
| R-7.2 gegen R-7.3 und R-6.10 | Zahlung zum Stichtag zählt zum Planjahr 1, die Abschreibung einer aktivierten Maßnahme zum Stichtag beginnt aber schon im Planjahr 1 und nicht im Folgejahr (Lücke 7) |
| R-3.3 (E-53 „gilt für: Ankauf“) gegen R-6.7 | R-6.7 wendet R-6.3 auf den Neubau an, ohne zu sagen, welche Anpassungsdauer gilt (Lücke 1) |
| R-6.5, Beispiel RF-12 | „9,8079 ab Jahr 10“: Nach der Formel steigt die gebundene Miete im Jahr 13 weiter (Stufe 4). Der Verkaufspreis nach 20 Jahren (6.655.683,14 Euro) bestätigt die Formel; das „ab“ im Beispiel ist irreführend |
| R-6.3, Zeile zum Ziel | Die Anmerkung „im Planjahr 1 … Ziel = Vergleichsmiete_j“ widerspricht der Formel (dort ist das Ziel im Planjahr 1 die Ist-Miete) und dem Satz „Im Planjahr 1 gilt für jedes d die Ist-Miete“. Für Erhöhungen ohne Wirkung (m ≥ 13); bei einer Ist-Miete über der Vergleichsmiete gelten Wartefrist und Kappung nicht, und dort hält nur der Fließtext die Senkung im Planjahr 1 auf |
| Anhang A.5, RF-13 | Verweis auf eine „Tabelle in R-7.9“, die die Ausprägungen nicht enthält (Lücke 8) |

## Was nicht nachgebaut wurde

- Die Lehrbuchfälle RF-01 bis RF-04 und die Bausteine RF-07 bis RF-10 als eigene Fälle (nicht beauftragt; Darlehens- und Steuerregeln sind über RF-11 bis RF-13 mitgeprüft).
- Aus RF-18: leere Flächen, Fluktuation, Erbbauzins, Mietenhistorie, Ist-Miete über der Vergleichsmiete. Mein Kern führt diese Teilflächen nicht.
- Die Proben P-01 bis P-19 als eigene Prüfungen, die Sperre M-10 (RF-16) und die Eingabeprüfung (RF-20). Geprüft ist die Rechnung, nicht das Meldewesen; Meldungen sind nur dort verglichen, wo sie aus der Rechnung folgen (M-21, M-25, M-29, M-32 bis M-34, M-36, M-38, M-42).
- Diese Teile lagen außerhalb des beauftragten Umfangs; an den Regeln selbst ist dort nichts aufgefallen, was den Nachbau verhindert hätte.

## Eigene Werte ohne Sollwert im Dokument (zum Abgleich mit dem Referenzrechner)

Diese Größen nennt das Dokument nicht; sie stammen allein aus meiner Rechnung und eignen sich als zusätzliche unabhängige Probe.

| Fall | Endwert | Endwert der Alternative | Endwertdifferenz | Rendite | Vergleichsrendite |
|---|---|---|---|---|---|
| Ankauf gebunden (Rang vor der Bank), Bankdarlehen 743.803,42 | 2.325.926,95 | 1.744.170,12 | 581.756,83 | 3,947 % | 1,483 % |
| Ankauf gebunden, Stressfall | 1.892.878,26 | 1.775.152,44 | 117.725,82 | 2,028 % | 1,483 % |
| Ankauf gebunden, Rang nach der Bank | wie Rang vor der Bank, weil (b) bindet | | | | |
| Ankauf gebunden, Lesart 2 von `MA-026`, Bankdarlehen 1.034.436,66 | 1.961.590,54 | 1.434.494,92 | 527.095,62 | 4,164 % | 1,483 % |
| Ankauf gebunden, Haltedauer fünf Jahre | 1.411.077,77 | 1.570.518,22 | −159.440,45 | −0,703 % | 1,446 % |
| RF-13 Körperschaft mit Kennzeichen | 2.570.679,38 | 1.768.249,69 | 802.429,69 | 4,697 % | 1,483 % |
| RF-13 Körperschaft, sofortige Verrechnung | 2.475.876,39 | 1.737.298,50 | 738.577,89 | 4,523 % | 1,483 % |
| RF-13 Körperschaft ohne Gewerbesteuer | 2.717.279,86 | 1.826.982,29 | 890.297,57 | 5,185 % | 1,763 % |
| RF-13 Personengesellschaft originär, 400 % | 2.284.696,57 | 1.706.648,99 | 578.047,58 | 3,649 % | 1,160 % |
| RF-13 Personengesellschaft originär, 440 % | 2.267.845,35 | 1.705.425,92 | 562.419,43 | 3,585 % | 1,154 % |
| RF-13 Personengesellschaft originär, 440 %, Anteil 60 % | 2.200.475,99 | 1.700.569,96 | 499.906,03 | 3,324 % | 1,129 % |
| RF-13 Personengesellschaft originär, 440 %, sofort | 2.217.038,80 | 1.653.094,49 | 563.944,31 | 3,659 % | 1,154 % |
| RF-13 Personengesellschaft geprägt, 440 %, Kennzeichen | 2.270.933,17 | 1.705.425,92 | 565.507,25 | 3,597 % | 1,154 % |
| RF-13 Privatperson, zwölf Jahre | 2.711.417,29 | 1.770.641,79 | 940.775,50 | 5,141 % | 1,473 % |
| RF-13 Privatperson, zehn Jahre | 2.101.425,28 | 1.719.625,94 | 381.799,34 | 3,528 % | 1,473 % |
| RF-13 befreite Körperschaft | 2.863.247,28 | 1.875.297,60 | 987.949,68 | 5,661 % | 2,000 % |
| Neubau frei, 15 Jahre | 9.796.187,08 | 6.471.824,38 | 3.324.362,70 | 4,332 % | 1,488 % |
| Neubau frei, 15 Jahre, Stressfall | 7.787.062,25 | 7.036.488,55 | 750.573,70 | 2,176 % | 1,488 % |
| Neubau mit KfW-Darlehen, 15 Jahre | 10.037.310,64 | 6.353.337,95 | 3.683.972,69 | 4,630 % | 1,488 % |
| Neubau gefördert, 38 Jahre, Stressfall | 8.867.740,83 | 5.379.707,84 | 3.488.032,99 | 2,845 % | 1,501 % |
| Neubau frei, 38 Jahre | 25.525.695,66 | 9.133.557,41 | 16.392.138,25 | 4,283 % | 1,501 % |

Dazu: Für den geförderten Neubau über 38 Jahre und für den frei finanzierten Neubau im Stressfall findet meine Preissuche keinen tragbaren Grundstückspreis (Ziel schon bei 1 Euro verfehlt, M-32). Operatives Ergebnis des geförderten Neubaus in den Planjahren 1 bis 3: 1.083.261,03 / 543.615,92 / −99.883,99 Euro.
