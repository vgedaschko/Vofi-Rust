```
Rolle: Prüfer Finanzmathematiker (Runde 3)
Prüfobjekt: docs/fachspezifikation-rechenkern.md, Teil 1, eingefrorener Stand 2026-11-21, mit Referenzrechner
            (referenzfaelle.py, gegenrechnung.py, wesentlichkeit.py), docs/modellannahmen.md, docs/quellenkataster.md
Gesamturteil: Trägt, mit kleinen Auflagen. Ich habe die Rechnung unabhängig nachgebaut, in eigenem Code mit
  exakter Dezimalrechnung: den Ankauf im Basis- und im Stressfall und den Neubau frei finanziert, mit KfW-Darlehen
  und gefördert über 38 Jahre. Den Neubau gab es in Runde 2 nur in Bausteinen, jetzt als ganzen Finanzplan.
  Dazu kommen die Steuerbeispiele, die Abweichungstabelle aus R-3.2 und neun Messungen der Durchsicht.
  Rund 420 Werte habe ich nachgerechnet. Alle treffen auf den Cent oder Euro, bis auf vier Zahlen im Text.
  Diese vier stammen aus einem älteren Stand oder aus einer Konstellation, die es nicht mehr gibt.
  Dazu kommt eine Lücke in zwei Proben: Eine wörtliche Umsetzung würde den KfW-Fall sperren.
Note: 9 von 10. An der Rechnung fehlt zur 9 nichts. Die Befunde 1 bis 3 sind Fehler im Text und müssen vor der
  Umsetzung in Rust berichtigt werden; zusammen sind das unter einer Stunde Arbeit, ohne Auskunft von außen.
```

Eigene Skripte unter `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/pruefrunde-fachspezifikation-3/finanzmathematiker/`. Sie importieren weder den Referenzrechner noch die Blindrechnung.

- `ank.py` ist mein Nachbau des Ankaufs aus Runde 2, nachgezogen auf den neuen Stand:
  - RE_n mit je Periode gerundetem Mietausfall;
  - Stress mit acht Größen und Neubemessung;
  - Rückführung der Übermiete;
  - Kennzeichen E-41 und E-69;
  - Erbbauzins.
- `nb.py` baut den Neubau neu aus R-2.5, R-5.4 bis R-5.19, R-6.5 bis R-6.8, R-7.2 bis R-7.19, R-8.1, R-8.7, R-9, R-10.4, R-10.5, R-11.2, R-11.3 und R-11.14: frei finanziert, mit KfW-Darlehen und mit Grobförderung, für Körperschaft und Privatperson.
- Läufe: `ank_lauf.py`, `abw.py`, `uebermiete.py`, `nb_lauf.py`, `nb_lauf2.py`, `gef_lauf.py`, `zuschuss.py`, `messung.py`.
- `reste.py` sucht im Text alte Sollwerte aus `aenderungen-runde2.md`.

Referenzrechner:
- `referenzfaelle.py`: 20 Fälle, 1.093 von 1.093 Prüfungen bestanden, Rückgabewert 0, 60 Sekunden.
- `gegenrechnung.py`: 16 von 16 bestanden.
- `wesentlichkeit.py`: 238 Messungen. Die 278 der Durchsicht gehören zum Stand vor der Umsetzung; so steht es in `durchsicht.md`, Zeile 453.

## Stand der Befunde aus Runde 2

| Nr. | Befund Runde 2 | Stand | Beleg |
|---|---|---|---|
| 1 | KD_Ü des übernommenen Darlehens: Tilgungssatz auf die Restschuld statt auf den Nennbetrag | behoben | R-5.11 und R-5.12 setzen den Nennbetrag als Bezugsbetrag, dazu den Bemessungszins. Nachgerechnet: i_B 1,0 %, Rate_B 1.500,00, B = (92.479,44 / 1,2 − 18.000) / 7 % = 843.802,85; bei neun Jahren 865.231,42, ab zehn Jahren 886.660,00 Euro |
| 2 | Richtung „strenger“ trägt nicht (H-02 bis H-04, H-25, H-07) | anders entschieden und vertretbar | R-3.2 kennt keine Richtung mehr. Die Wirkung wird am Fall gemessen, die Begründungspflicht hängt am tragbaren Preis, H-07 ist entfallen. Alle Zeilen der Tabelle in R-3.2 habe ich nachgerechnet und getroffen (siehe unten), auch +10.228 Euro bei Zielrendite 2 % |
| 3 | Übermiete: alter Wortlaut zu NF-12, Formel ohne Rückführung | behoben | R-6.3 hat Zeile (2) im Formelblock, NF-12 ist angeglichen. Bei 11,00 Euro Ist-Miete nachgerechnet: 11,0000 / 10,5960 / 10,2858 / 10,0723 / 9,9584 / 10,1575 Euro; ΔEW 831.335,64 gegen 905.596,44 Euro, P* 2.424.974 gegen 2.470.976 Euro |
| 4 | Zinsanstieg bis zur Zusage ohne Neubemessung | behoben | R-11.8 bemisst neu: L_Stress 1.144.835,99, EK 1.495.164,01 Euro, mit acht Größen ΔEW 237.324,51 Euro und r 2,489 % |
| 5 | Mietausfall und Bewirtschaftung im RE_n nicht auf den Cent bestimmt | behoben | Formelblock in R-5.12. Gebundener Bestand 92.479,44 Euro, geförderter Neubau 159.216,75 Euro (Mietausfall 12 x 328,00 Euro), frei 336.600,00 Euro |
| 6 | R-7.16: Erbbauzins im zweiten Beispiel | behoben | „ohne Erbbauzins“ steht im Text; 31.925,00 Euro nachgerechnet |
| 7 | NF-47 ohne Beleg und ohne Kennung | anders entschieden und vertretbar | Belegt mit dem Wortlaut von `GEWSTG-9` („Summe aus Gewinn und Hinzurechnungen“). Rechtlich gehört das zum Steuerberater |
| 8 | Rangfolge der Vorsicht fehlte | behoben | „Maßstab der Vorsicht mit Rangfolge“: Preis, dann ΔEW, dann Rendite. Die Ausnahmen sind benannt (`MA-026`, `MA-031`, `MA-040`) |
| 9 | (a) Zählung R-3.6, (b) Modus 155.571,22/23, (c) R-15.6 | behoben | (a) Die Tabelle stimmt mit R-3.3: 19 (12) und 21 (14) Felder. (b) R-10.2 nennt beide Modi. (c) R-15.6 ist nachgezogen |
| 10 | R-11.4 und R-11.5 beschreiben nicht ganz dieselbe Größe | behoben | Schwellenpreise der R-6.16 sind Stützstellen, und die Zusicherung ist auf Stützstellen und Fenster beschränkt. Beleg der Nachsuche: Bei nachhaltiger Miete 15,00 Euro ist EÜ bei 606.989 Euro +0,59, bei 606.990 Euro −1,53 und bei 606.991 Euro +10,33 Euro. Der Referenzrechner findet 606.989 Euro mit M-34, eine reine Bisektion fände 606.995 Euro |

## Nachgerechnet, getroffen, abweichend

| Gegenstand | nachgerechnet | getroffen | abweichend |
|---|---|---|---|
| **Ankauf RF-11, Basisfall:** L 1.226.609,99; A, B, C; RE_n 103.035,24; EK 1.413.390,01; Nachschuss 72.484,81 (Monat 24); EW 2.524.305,59; EW_U 1.770.603,63; ΔEW 753.701,96; r 4,5271 %; r_U 1,4831 %; EÜ −140.507,34; Verkaufspreis 3.212.578,13; Ablösung 886.727,18; g_v 999.589,46; Deckung in den Jahren 1 bis 12 | 28 | 28 | – |
| **Tragbarer Preis RF-11:** P* 2.317.235; EÜ 0,35; r 5,000001 / 4,999995 %; EK 1.322.348,51 und 1.395.253,65; Faktoren 17,47 / 17,21 / 19,31; 1.755,48 Euro je m²; Boden 637.239,63; Grundlage 1.911.718,87 | 12 | 12 | – |
| **Stressfall RF-11 mit acht Größen:** L_Stress 1.144.835,99; EK 1.495.164,01; Nachschuss 90.811,24; EW 2.126.728,79; EW_U 1.889.404,28; ΔEW 237.324,51; r 2,489 %; Abstand −2,511; Deckung 1,3484 / 1,3321 / 1,7254; Verkaufspreis 2.683.562,66; P*_Stress 1.977.816 mit EK 1.030.761,61 / 1.123.696,87; Faktor 15,22 / 14,69; Darlehen zu Kaufpreis 47,70 %; **EÜ** | 18 | 17 | EÜ: Text −739.303,12, eigene Rechnung und Sollwert −716.938,74 (Befund 2) |
| **Einzelstress (R-11.8):** −13.920,92 / −32.897,46 / −79.558,59 / −161.319,43 / −238.744,64 / −11.346,91 | 6 | 6 | – |
| **Abweichungstabelle R-3.2:** H-12 1,5 % und 2,5 %; H-25 fest 1 %; H-02 60 %; H-03 1,3 bei z 5 % und 2 %; E-11 3 %; E-46 5 Jahre; H-09 0,5 %. Je ΔEW, Preiswirkung und Renditeabstand | 26 | 26 | – |
| **Steuerstatus RF-13**, Körperschaft ohne Kennzeichen, mit E-41 und mit E-69: EW, EW_U, ΔEW und r je Zeile (A.5, Nr. 1 bis 3); 7.952,00 + 139.930,00 = 147.882,00 | 13 | 13 | – |
| **Miete:** Übermiete in beiden Lesarten (siehe oben); R-6.18 außerhalb des Gebiets: Monate 37 bis 142, ΔEW 757.210,62, Wirkung 3.508,66, P* 2.319.295 | 14 | 14 | – |
| **Neubau frei finanziert (RF-12):** BK_0 7.540.000,00; Raten 419.921,98 / 420.957,62 / 437.879,56; BK 7.719.152,34; GK 9.015.152,34; RE_n; A, B, C; L 4.007.142,85; EK 5.008.009,49 und 5.141.964,13; Monat 9 mit 323.492,21 + 104.786,77; Bauzeitzinsen 54.961,41; Bereitstellungszins 78.993,23; Abschreibung im Planjahr 2 115.787,29; Erhöhungen in den Monaten 37 / 52 / 67 / 82 / 97; laufender Nachschuss 68.394,63; Verkaufspreis 11.872.569,69; EW 9.796.187,08; EW_U 6.471.824,38; ΔEW 3.324.362,70; EÜ −984.573,31; r 4,332 %; r_U 1,488 %; kleinste Deckung 1,4735 im Jahr 3; P* 702.767 | 30 | 30 | – |
| **Varianten des Neubaus:** Vorvermietung (Monat 19, 0, 3.439.793,85); Vorlauf 12 Monate (7.950.726,89 / 432.519,64 / 451.015,95 / Monat 34 / EK 5.493.273,85 / EW 9.409.416,51 / 3,675 %); Haltedauer 3 Jahre (EW 5.201.901,26, VFE 271.842,29); nachhaltige Miete 15 (606.989) | 13 | 13 | – |
| **Neubau mit KfW (RF-12, R-5.19):** KD_Ü 135.000,00; A, B, C; L 2.078.571,42; EK 4.051.620,80; Abruf ab Monat 7 (320.711,03) bis 14, Bank 14 bis 18; Provision 949,02; erste Raten der vier Varianten 10.922,62 / 11.853,63 / 14.785,20 / 34.511,53, je mit KD_Ü, L und ΔEW; Rate nach der Bindung 14.305,24; EW 8.527.589,11; EW_U 5.122.699,97; ΔEW 3.404.889,14; r 4,995 %; Deckung 1,3850 (Jahr 3) und 1,4270 (Jahr 11); H-32 15 Jahre (159.999,96 / 1.721.429,14); KfW-Zins 3 % (−63.231,54 / 150.000,00); VFE nach acht Jahren 35.411,17 + 52.203,65; P* 1.197.094; H-25 = 4 % (L 4.675.000,00 und 2.425.000,00, P* 876.926 und 1.283.299) | 40 | 40 | – |
| **Neubau Stressfall:** BK 8.135.353,14; L 3.740.000,00; EK 5.851.491,95; EW 8.211.748,74; EW_U 7.343.460,94; ΔEW 868.287,80; r 2,247 % | 7 | 7 | – |
| **Geförderter Neubau, 38 Jahre:** FD 5.231.491,40; Z 1.743.830,47; Entgelte 65.393,64; M 9.080.545,98; RE_n 159.216,75; KD_Ü 151.713,24; A 628.357,62, B −271.894,50, C 361.393,64; L 0; EK 2.105.224,11 / 2.144.688,71; laufender Nachschuss 27.636,75; Nachschüsse 16.422,18 / 50.679,17; 13 Abrufe der Teilraten mit 97.049,13 (Monat 2), 1.409.704,46 = 1.057.278,34 + 352.426,12 (Monat 10), 1.479.719,23 (Monat 15), 697.532,19 (Monat 22); Lücke 124.864,92 / 980.369,23 / 1.045.063,54 / 697.532,19; Zinsen der Zwischenfinanzierung 42.095,30; Tilgung ab Monat 23 mit 500 Raten zu 10.462,98; Ertrag aus dem Zuschuss 24.911,86 / 49.823,73; Verkaufspreis 8.970.001,32; EW 9.477.900,38; EW_U 3.821.690,66; ΔEW 5.656.209,72; EÜ −4.376.742,89; r 3,956 %; r_U 1,501 %; kleinste Deckung 1,0510 (Jahr 4); Deckung 1,8848 im Planjahr 37; nach 20 Jahren 6.655.683,14 / 822.091,51 / 3.275.573,58 / 2.918.482,73 / 357.090,85 / 2,081 %; Haltedauer 36 und 37 Jahre (4,027 / 3,996 %); R-11.15 (212.412,96 / 0,8995 / 266.963,98 / 1,0495 / −22.839,14 / 400.858,24) | 72 | 72 | – |
| **Vergleich frei gegen gefördert, 38 Jahre (R-11.11):** ΔEW frei 16.392.138,25 − 5.656.209,72 | 1 | – | Text −10.726.689,93, eigene Rechnung und Sollwert −10.735.928,53 (Befund 3) |
| **Zuschuss nach Vermögenssphäre (R-7.19, E-70):** Körperschaft „verteilt“ und „sofort“, Privatperson mit Zufluss und mit E-70: je r, ΔEW und EK; EW, Rendite nach 20 Jahren; Privatperson mit sofortiger Verrechnung 2,421 % und mit E-70 2,913 % | 22 | 22 | – |
| **Steuerbeispiele von Hand:** R-7.8 (17.407,50 + 1.400,00; 181.932,50; 97.932,50; 84.112,00 = 14,77 % von 560.000 + 1.400); R-7.16 (34.025,00; 31.925,00); R-7.9, Tabelle (15 Werte); R-7.7; R-2.8; R-7.6 (−21.000,00; 770,00; 33.600,00; −22.400,00); R-7.10; R-7.11; R-7.17; R-7.18 (243.285,00 / 222.285,00); R-6.16 (356.605,04; 48.087,20); R-5.11 (55.238,10; 386.666,50; 19.333,33) | 43 | 43 | – |
| **Kennzahlen von Hand:** R-10.13, R-10.15 (51,11 %; 29,98 %), R-10.16, R-10.20 bis R-10.22, R-10.24 (85.862,64; 1,200001; 0,07), R-5.12 Gegenüberstellung (1.431.044,99; 1.073.283,74), R-14.7, R-14.1 | 20 | 20 | – |
| **Bemessungszins, gebundener Bestand, mit einem H-25 für alle Tranchen (R-5.12, Absatz nach der Tabelle):** fester kalkulatorischer Zins 4 % | 1 | – | Text 826.660,00 (alte Vorgabe je Tranchenart), nach geltender Regel 964.436,66 Euro (Befund 4) |
| **V-06 „deckungsgleich auf den Cent“** am gebundenen Bestand | 1 | – | H-25 = 4 % ergibt 964.436,66, Lesart 2 ergab 1.034.436,66 Euro (Befund 4) |
| **Messungen der Durchsicht (Stichprobe):** V-22 Instandhaltungsstress (+0,67 % / +0,084 PP; P*_Stress mit neun Größen 1.964.653); H-16 im Ankauf und Neubau (−0,62 % / −0,084; −0,53 % GK, Grundstück −6,44 % / −0,064); H-17 Verwaltung im Ankauf und Neubau (−0,58 % / −0,072; −0,17 % GK / −0,020); H-08 im Ankauf und Neubau, Grenzfall (−0,49 % / −0,067; −0,77 % GK, Grundstück −9,27 % / −0,090); E-63 / V-14, Grenzfall (−0,85 % / −0,109 PP); E-65, Grenzfall (−1,13 % GK, Grundstück −13,63 %); E-46 (−1,14 % / −0,156) | 18 | 18 | – |
| **Summe** | **rund 420** | **rund 416** | **4** |

Nicht als Sollwert im Referenzrechner geführt, von mir aber getroffen:
- R-6.18: 757.210,62 Euro und 2.319.295 Euro;
- R-3.2, Zeile Zinsbindung: −44.943,46 Euro und −26.475 Euro;
- R-5.19 mit H-25 = 4 %: 876.926 und 1.283.299 Euro.

Siehe Befund 6.

**Messmethode und Schwelle im Neubau (Auftrag 3).**
- Die neun nachgerechneten Messungen stimmen alle, die drei Grenzfälle eingeschlossen. Das Verfahren hält:
  - eine Größe ändern;
  - P* mit derselben Zielgröße EÜ suchen;
  - die Rendite beim eingegebenen Preis messen.
- Die Schwelle im Neubau ist rechnerisch sinnvoll umgesetzt:
  - Nenner sind die Gesamtkosten beim tragbaren Grundstückspreis: 702.767 x 1,08 + 7.719.152,34 = 8.478.140,70 Euro, bei KfW 9.012.013,86 Euro.
  - Am Grundstückspreis gemessen wäre die Schwelle zwölfmal so streng wie am Kaufpreis im Ankauf.
  - Am Rest gemessen, rechnet sie wie die Renditeschwelle. In meinen Messungen entspricht 1 % der Gesamtkosten im Neubau 0,12 Prozentpunkten Rendite (H-08: 0,77 % zu 0,090; H-16: 0,53 % zu 0,064). Im Ankauf entspricht 1 % des Preises 0,13 bis 0,14 Prozentpunkten (H-16: 0,62 % zu 0,084).
  - Beide Teile der Schwelle sind damit im Neubau etwa gleich streng, wie im Ankauf.
- Zwei Lücken, siehe Befund 7: Der Nenner ist nirgends definiert, und die Liste der Vereinfachungen nennt im Neubau nur den Anteil an den Gesamtkosten.

## Befunde

**1. [wichtig · belegt] R-13.3, P-03 und P-04 (b), auch R-10.17 und R-11.3: In den Finanzierungskosten fehlt die Bereitstellungsprovision des KfW-Darlehens. Eine wörtliche Umsetzung sperrt den KfW-Fall mit M-10.**

- Die Bereitstellungsprovision ist geblieben (Durchsicht, Zeile 448; R-5.19). R-7.2 führt sie als Entgelt neben dem Bereitstellungszins.
- P-03 zählt aber abschließend auf: „Finanzierungskosten sind Zinsen, Kontokorrentzinsen, Beiträge, Bereitstellungszinsen und Vorfälligkeit“. P-04 (b) sagt: „Finanzierungskosten (Zinsen, Beiträge, Bereitstellungszinsen, Kontokorrentzinsen)“.
- RF-12 mit KfW-Darlehen, eigene Rechnung:
  - Mittelherkunft der Investitionsphase: 4.051.620,80 + 3.000.000,00 + 2.078.571,42 = 9.130.192,22 Euro.
  - Mittelverwendung: Investition 9.015.152,34 Euro und Finanzierungskosten 115.039,88 Euro.
  - Die Finanzierungskosten setzen sich zusammen aus 61.599,34 Euro Zinsen der Bauzeit, 52.491,52 Euro Bereitstellungszins und 949,02 Euro Bereitstellungsprovision.
  - P-04 (b) nach dem Wortlaut verfehlt die Gleichheit um 949,02 Euro.
  - P-03 verfehlt sie im Monat 13 um 798,90 Euro und im Monat 14 um 150,12 Euro.
- Folge: Nach R-13.1 ist das Ergebnis gesperrt, in der Preissuche jeder Schritt, also der ganze KfW-Neubau. Der Referenzrechner besteht nur, weil er die Provision mitzählt. Die Regel steht damit im Code, nicht im Text.
- Vorschlag: In P-03, P-04 (b), R-10.17 („Nachschüsse für Zinsen, Bereitstellungszinsen …“) und R-11.3 („Zinsen, Bereitstellungszinsen, Beiträge und Steuern der Bauzeit“) jeweils „Bereitstellungsprovision“ ergänzen. Besser: Den Begriff „Finanzierungskosten“ einmal in R-1.1 definieren und in den Proben nur darauf verweisen.

**2. [wichtig · belegt] R-10.9, Beispiel RF-11: Der Endwertüberschuss im Stressfall ist der Wert mit neun Stressgrößen.**

- Der Text nennt −739.303,12 Euro. `aenderungen-runde2.md`, Zeile 311, ersetzt diesen Wert durch −716.938,74 Euro (Instandhaltungsstress entfallen).
- Eigene Rechnung mit acht Größen: Z = EW = 2.126.728,79 Euro; Einlagen 1.495.164,01 Euro zum Stichtag und 90.811,24 Euro im Monat 24; EÜ = −716.938,74 Euro.
- Die übrigen Zahlen des Stressfalls im Text gehören zu acht Größen: r 2,489 %, ΔEW 237.324,51 Euro, P* 1.977.816 Euro. Damit widerspricht sich das Dokument selbst.
- Vorschlag: −716.938,74 Euro einsetzen.

**3. [wichtig · belegt] R-11.11 und R-11.12: In den Beispielen zum Vergleich stehen drei Werte, die kein Stand des Referenzrechners führt oder je geführt hat.**

- (a) RF-12, frei gegen gefördert über 38 Jahre:
  - Der Text nennt −10.726.689,93 Euro.
  - Eigene Rechnung: ΔEW frei über 38 Jahre 16.392.138,25 Euro, gefördert 5.656.209,72 Euro, Differenz −10.735.928,53 Euro. So steht der Wert auch in `erwartete_werte.json`.
  - Den Textwert führt kein Differenzbericht, weder als alten noch als neuen Wert.
- (b) RF-11:
  - Der Text sagt „36 Größen“, der Sollwert ist 35. Der Wertansatz E-61 ist entfallen (`aenderungen-runde2.md`, Durchsicht).
  - „Begründungen“ steht noch bei den abweichenden Werten; im Sollwert ist es entfallen.
- (c) R-11.12: „Der Vergleich führt 36 Größen des Blatts“ muss 35 heißen.
- Vorschlag: Die drei Stellen berichtigen. Außerdem für R-11.11 einen Lauf von `reste.py` (mein Skript) oder einen gleichwertigen Abgleich Text gegen Sollwerte in die Festschreibung aufnehmen.

**4. [Hinweis · belegt] R-5.12, Absatz nach der Tabelle zum Bemessungszins, Anhang A.4 (Zeile H-25 bis H-28), V-06 in Kapitel 16: Text und Liste rechnen noch mit einem kalkulatorischen Zins je Tranchenart und mit Lesart 2. Die Aussage „deckungsgleich auf den Cent“ stimmt nur eingeschränkt.**

- Der Satz „Mit einem festen kalkulatorischen Zins von 4 % für übernommene Darlehen (H-25) sind es bei acht Jahren 826.660,00 Euro“ setzt voraus, dass das Bankdarlehen bei 5 % bleibt. H-25 ist aber jetzt „ein Wert für alle Tranchen“ (R-3.4, V-07). A.4 sagt noch „für jede Tranchenart“.
- Gebundener Bestand nach geltender Regel mit H-25 = 4 %:
  - Bankdarlehen: i_k = max(4 %; 4 %) = 4 %.
  - Übernommenes Darlehen: i_B = (0,5 % x 96 + 4 % x 24) / 120 = 1,2 %, Rate_B = 600.000 x 3,2 % / 12 = 1.600,00, KD_Ü = 19.200,00 Euro.
  - B = (77.066,20 − 19.200,00) / 6 % = **964.436,66 Euro**. Die Probe mit gerundeter Rate besteht: 1,2 x (19.200,00 + 12 x 4.822,18) = 92.479,39 ≤ 92.479,44.
- Lesart 2, also Vertragskonditionen für alle Tranchen, ergab 1.034.436,66 Euro. V-06 sagt „ein fester Satz in Höhe des Vertragszinses ergibt dasselbe … deckungsgleich auf den Cent“. Das gilt nur, wenn jede fremde Tranche über den ganzen Bemessungszeitraum H-32 fest ist:
  - Im KfW-Neubau stimmt es: 2.425.000,00 Euro und P* 1.283.299 Euro, nachgerechnet.
  - Im gebundenen Bestand mit acht Jahren Bindung stimmt es nicht: 70.000,00 Euro weniger Darlehen.
- Die Abweichung ist die vorsichtige Richtung. Der Satz in V-06 ist aber als Aussage falsch.
- Vorschlag:
  - Den Satz in R-5.12 auf „Mit H-25 fest 4 % (für alle Tranchen) sind es 964.436,66 Euro“ umstellen und die Angabe zu Lesart 2 streichen.
  - A.4 an R-3.4 angleichen.
  - V-06 einschränken: „deckungsgleich, solange die Zinsbindung jeder fremden Tranche den Bemessungszeitraum deckt; sonst rechnet H-25 vorsichtiger“.

**5. [Hinweis · belegt] Entfallene Kennungen und Schalter im Fließtext (Auftrag 4).**

- R-6.7: „bis dahin ist die ganze Fläche leer und trägt die Betriebskosten leerstehender Flächen (R-6.17)“. R-6.17 ist entfallen (V-15), der Satz behauptet eine Zahlung, die nicht gerechnet wird. Ebenso R-10.22, letzter Satz, und R-5.12, RE_n-Block („nach R-6.8, R-6.9 und R-6.17“).
- R-6.16: „das Eingabefeld E-52 sagt das“. E-52 ist entfallen (V-13). Den Satz trägt jetzt das Eingabefeld E-50.
- R-11.9: Unter den Auswahlfeldern steht „Verlustverrechnung“. Sie ist kein Feld mehr, sondern Hauswert H-38.
- Anhang A.4, Zeile H-32 bis H-37: „Betriebskosten leerstehender Flächen 0 Euro, in den bezeichneten Fällen 30 Euro je m²“. H-36 ist entfallen.
- Kapitel 17, NF-07: „zwei weitere Regeln wählbar“. Das widerspricht R-5.9 („keine Wahl mehr“) und V-01. Die Spalte gilt laut Kopf als „geltender Wortlaut“.
- R-5.19, Absatz nach der Variantentabelle: „Nach Lesart (2) von `MA-026` …“. Lesart 2 ist entfallen. Die Zahlen stimmen mit H-25 = 4 % (nachgerechnet: 2.425.000,00 / 1.283.299 / 876.926); nur die Bezeichnung ist alt. Ebenso Kapitel 17, Setzung 10, das schon „früher Lesart 2“ sagt.
- Kapitel 16, „Was Teil 2 regelt“, Zeile KfW: nennt die „Bereitstellungsprovision“, die nach R-5.19 schon in 1a gerechnet wird.
- R-5.12, Beispiel E-65: „der tragbare Grundstückspreis 606.989“. Der Referenzrechner gibt dazu M-34 aus (EÜ wechselt bei 606.990 und 606.991 Euro das Vorzeichen); der Text sollte das nennen, damit der Rust-Kern nicht ohne Meldung abgenommen wird.
- Vorschlag: die Stellen streichen oder umstellen. Keine davon ändert eine Zahl.

**6. [Hinweis · belegt] „Jede Zahl kommt aus dem Referenzrechner“ (Kopf) gilt nicht mehr für alle Zahlen. Mit der Durchsicht sind Sollwerte entfallen, die der Text weiter nennt.**

- Ohne Sollwert, von mir aber nachgerechnet und getroffen:
  - R-6.18: 757.210,62 Euro und 2.319.295 Euro. `erwartete_werte.json` führt nur 3.508,66 Euro.
  - R-3.2, Zeile Zinsbindung: −44.943,46 Euro und −26.475 Euro.
  - R-5.19: 2.425.000,00 / 1.283.299 Euro.
  - R-5.12: 876.926 Euro (nur in `beispielwerte.py`).
- Ohne Sollwert und mit dem Code nicht mehr rechenbar, weil die Lesart entfallen ist:
  - R-7.8, RF-13: 7.952,00 Euro. Rechnerisch stimmt es: 2.570.679,38 − 2.562.727,38.
  - R-7.15: 9.478.243,94 Euro.
  - R-5.19: 1.195.647 Euro und 3.394.433,81 Euro. Diese sind als „Stand vor der Durchsicht“ bezeichnet.
- Vorschlag: Die erste Gruppe als Sollwerte festschreiben, weil sie mit geltenden Eingaben rechenbar ist. Die zweite Gruppe einheitlich als „Wert der früheren Lesart, nicht mehr gerechnet“ bezeichnen, wie es bei `MA-040` schon geschieht.

**7. [Hinweis · begründete Einschätzung] Kopf, „Wesentlichkeit“, Kapitel 16 und Spezifikation, Zeile „Wesentlichkeit und Eingabensparsamkeit“: Zwei Lücken in der Umsetzung der Schwelle.**

- (a) **Nenner im Neubau.** Die Durchsicht misst an den Gesamtkosten beim tragbaren Grundstückspreis (8.478.140,70 Euro), nicht beim eingegebenen Preis (9.015.152,34 Euro). Das ist die folgerichtige Wahl, weil auch im Ankauf am tragbaren Preis gemessen wird. Sie steht aber nur in der Durchsicht. Am eingegebenen Preis gemessen wäre jeder Prozentwert um rund 6 % kleiner; eine Grenzlage wie E-65 (1,13 % gegen dann 1,06 %) bliebe zwar darüber, knappere Fälle könnten aber kippen. Vorschlag: In der Spezifikation „1 % der Gesamtkosten beim tragbaren Grundstückspreis“ schreiben.
- (b) **Grundstücksbezug in der Liste.** Im Neubau entspricht 1 % der Gesamtkosten rund 12 % des tragbaren Grundstückspreises, mit KfW rund 7,5 %. Die Liste V-01 bis V-22 nennt im Neubau nur den Anteil an den Gesamtkosten. V-15 hat 0,16 %, das sind 1,95 % des Grundstücksgebots; V-01 hat 0,07 %, das sind 0,83 %. Wer ein Grundstück bietet, liest daraus eine kleinere Wirkung, als er am Gebot sieht. Vorschlag: in den Neubauzeilen beide Zahlen nennen, wie in der Durchsicht.
- (c) Nach eigener Messung liegen V-14 (−0,109 Prozentpunkte je Prozentpunkt) und V-17 (bis +0,103 Prozentpunkte) über der Renditeschwelle, V-03 (+0,141 Prozentpunkte bei Verkauf vor dem Bindungsende) ebenfalls. V-14 habe ich nachgerechnet: −0,85 % und −0,109 Prozentpunkte. Der Kopf von Kapitel 16 begründet eine Vereinfachung nur mit „unter der Schwelle oder eine andere Eingabe leistet dasselbe“; auf diese drei trifft keins zu. Die Durchsicht begründet sie mit „kein typischer Fall“ (Erbbaurecht mit eigener Staffel, Privatperson, Verkauf vor Bindungsende). Vorschlag: Diese Begründung in die drei Zeilen schreiben, damit die Liste ihre eigene Regel nicht scheinbar bricht. Das ist kein Verlangen nach einer Regel.

## Nicht geprüft

- **Gebundener Bestand im vollen Finanzplan:** Gerechnet habe ich nur die Bemessung (RE_n aus dem Text). Endwert, ΔEW 562.960,01 Euro und Mietpfad habe ich nicht im eigenen Code nachgebaut.
- **Haltedauer 39 Jahre im geförderten Neubau (4,190 %):** Mein Code rechnet die Miete nach R-6.6 ab dem Planjahr b + 2 nicht.
- **Kennzeichen E-41 im geförderten Neubau (4,001 / 3,771 %) und weitere Ausprägungen von RF-13:** Nur Nr. 1 bis 3 sind nachgerechnet, die Personengesellschaften nur als Steuerbausteine.
- **Gesamtkapitalrendite und Restwertanteil im Stressfall:** Nur die Formeln habe ich am Basisfall gesehen, nicht nachgerechnet.
- **Meldungen** habe ich nur dort ausgelöst, wo mein Nachbau sie berührt. M-34 beim Neubau mit nachhaltiger Miete 15,00 Euro habe ich am Referenzrechner bestätigt.
- **Rechtsinhalte** (`GEWSTG-9`, `ESTR-21-5`, `MA-030`, `MA-031`): gerechnet, wie sie geschrieben sind. Keine Quelle am Original gelesen.
