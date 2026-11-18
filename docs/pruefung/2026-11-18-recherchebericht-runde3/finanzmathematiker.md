```
Rolle: Prüfer Finanzmathematiker (Runde 3)
Prüfobjekt: reports/VOFI Immobiliensoftware Marktrecherche.md, überarbeitete Fassung nach Runde 2
            (Schwerpunkt Abschnitt 3, Rechenaussagen in Abschnitt 4 bis 6 und 8, Anhang A Nr. 1–38,
            Rechenbeispiele in Anhang D)
Gesamturteil: Trägt. Alle neun Befunde aus Runde 2 sind behoben. Jede nachgerechnete Zahl stimmt auf
den Cent bzw. auf die ausgewiesene Nachkommastelle. Anhang A ist so eindeutig, dass die
Rechenkern-Spezifikation darauf aufbauen kann. Eine Auflage gilt: Die Saldierungsregel (Nr. 13)
beseitigt die Mehrdeutigkeit nur bei Zahlungen in exakt derselben Periode. Wird die Entnahme eine
Periode später gebucht, springt die Rendite um dieselben 0,63 Prozentpunkte (Befund 1). Diese
Eigenschaft muss die Spezifikation kennen und festhalten.
Note: 9 von 10. Der Bericht erreicht die 9 für seinen Zweck als Vorstufe.
  Im Bericht behebbar: ein Satz und ein Testfall zu Befund 1; die Formulierung in Nr. 10, letzter
  Spiegelstrich (Befund 3); die Herleitung der IWU-Toleranz (Befund 5).
  Erst die Fachspezifikation kann liefern: die Entscheidung, wie mit Befund 1 umzugehen ist; die
  Umrechnungsregel nominal/effektiv je Zahlungsart (2); die Operationsreihenfolge bei nicht
  abbrechenden Quotienten (3); die Buchung von Barzuschüssen in der Kontrollsumme (4); die
  Prozessdefinition der Simulation (6).
```

Gegenrechnungen: eigene Skripte unter `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/runde3-finmath/`.

| Skript | Inhalt |
|---|---|
| `m.py` | Testfall neu geschrieben, exakte Bruchrechnung; wahlweise Rundung nach Nr. 10; NBank-Tranche mit Entgelt und Verwaltungskostenbeitrag; Barzuschuss mit Entgelt; Kontrollsumme Nr. 22/23 |
| `r1.py` | Renditen, Saldierung, Verschiebung, Randfall, Schuldendienstdeckungsgrad (DSCR), Kirchner |
| `r2.py` | Rundung je Fall, Darlehensbeispiel, Operationsreihenfolge |
| `r3.py` | Kontrollsummen |
| `r4.py` | Laufzahlen; Simulationsbeispiele Nr. 31/32 |
| `r5.py` | Kapitalwert-Probe, Bauzeit, Einzelbeispiele |

**Unabhängig bestätigt (keine Befunde):**

Testfall und Varianten (A.6)
- Basis: Endwert 584.366,28, Endwertdifferenz 155.571,23, Rendite 7,8760 %.
- Entnahmen: Endwert 558.656,41, Rendite 7,8760 %. Ungespiegelt ergeben sich 129.861,36 und 6,91 %. Die Differenz von 25.709,87 € und 0,97 Prozentpunkten aus Abschnitt 3 stimmt.
- Kontokorrent: Endwert 561.526,16, Rendite 8,1228 %, mit Entnahmen 8,0886 %. Ohne Kontokorrentzins liegt der Endwert um 1.839,71 € höher.
- Nachschuss: Endwert 636.495,82, Endwertdifferenz unverändert. Die vier Lesarten ergeben 7,1807 / 7,2461 / 7,5045 / 7,8760 %; die Spanne beträgt 0,70 Punkte.
- Nachschuss und Entnahme in t = 2: saldiert 7,876 %, unsaldiert 7,246 %, also 0,63 Punkte Unterschied.
- Miete als Vorjahreswert: 8,0277 %, also +0,15 Punkte.
- DSCR im Verkaufsjahr: 59.533,77 / 42.000 = 1,42. Mit Ablösung der Restschuld von 624.171,48 sinkt er auf 0,09.

Randfall Nr. 15
- Die Regel richtet sich jetzt nach dem Zähler und verläuft stetig: Geht der Zähler gegen null, geht die Rendite gegen −100 %.
- Beispiel: 0,1^(1/5) − 1 = −36,9 %.
- Die Äquivalenz „r > q^(N/n) − 1 ⇔ ΔEW > 0" gilt brutto wie saldiert, weil Zähler − q^N·Nenner = ΔEW ist.

Effektiver Vergleichszins Nr. 12
- (1 + 0,014/12)^12 − 1 = 1,40902 %.

Rundung Nr. 10
Darlehensbeispiel, Restschuld nach zehn Jahren:

| Rechenweise | Restschuld |
|---|---|
| Volle Genauigkeit | 528.208,5612 |
| Kaufmännische Rundung je Rate | 528.208,51 |
| Abschneiden | 528.207,91 |

Testfall mit allen Regeln aus Nr. 10 (Zinsen, Steuer und indexierte Miete je Zahlung auf Cent): Endwert 584.366,28. Die Abweichung zur ungerundeten Rechnung beträgt −0,0016 €. Eine auf volle Euro abgerundete Steuer ergibt +1,31 €.

Kontrollsummen Nr. 22/23
In jeder Periode beträgt die Abweichung exakt 0. Geprüft habe ich folgende Fälle:
- Basis
- Tilgungszuschuss 35.000
- Disagio 3 %
- NBank-Tranche mit 1 % einbehaltenem Entgelt, 0,5 % Verwaltungskostenbeitrag und 0 % Zins
- Barzuschuss brutto mit einbehaltenen 0,75 %
- alle Fälle kombiniert mit Nachschuss und Entnahmen, ungerundet und nach Nr. 10 gerundet

Beispielwerte:
- 23.200 € Entgelt bei 2,32 Mio. Darlehen.
- Entgelte der Gruppen A/B/C: 0,700 / 0,750 / 0,775 % der zuwendungsfähigen Kosten.
- Förderung der Gruppen A/B/C: 40+40 = 60+20 = 70+10 = 80 %.

Zinsstufe Nr. 16
Bei linearer Tilgung über 42 Jahre stehen nach 35 Jahren noch 7/42 = 1/6 des Darlehens aus.

Kapitalwert-Probe Nr. 24
- Einheitlich 4 %: 110.371,99 = 110.371,99, Differenz 0.
- Testfall: 145.124,09 gegen 190.202,20.

Bauzeit Nr. 26/27
- Ein Durchlauf: 235.370,02 Zins und 70,69 % Fremdkapital.
- Fixpunkt im 6. Durchlauf: 3.069.183,25 Eigenkapital, 230.610,83 Zins, 70,00 %.
- Volle Kreditfinanzierung: 494.133,56. Die Faustformel liefert das 2,168-Fache.

Laufzahlen Nr. 35 (mit z = 1,96)

| Streuung | 5-%-Quantil | Mittelwert | Halbbreite bei 10.000 Läufen |
|---|---|---|---|
| 2 % | 27.448 | 6.147 | 8,3 bp |
| 3 % | 61.758 | 13.830 | 12,4 bp |
| 5 % | 171.550 | 38.416 | 20,7 bp |

Das Verhältnis beträgt k² = 4,466. Mit dem exakten z = 1,95996 ergeben sich 27.447 / 61.756 / 171.543 Läufe; der Unterschied ist bedeutungslos.

Simulationsbeispiele
- Nr. 31: Mit 20 Zufallsstarts zu je 10.000 Läufen (numpy, Startwerte 0–19) ergibt sich exakt die Spanne 18,0 bis 29,4. Der Erwartungswert von 1/y existiert bei normalverteiltem y nicht. Mit 200 Starts reichen die Startmittel von −38,6 bis 241,3. Die Spanne ist deshalb eine Illustration und kein Testwert. Der Bericht verwendet sie richtig.
- Nr. 32: 5,67 / 11,63 / 18,16 % (Streuung in % des Ausgangsniveaus, AR(1) mit stationärer Streuung 1,5 Punkte). Zur Definition siehe Befund 6.

Einzelbeispiele
- Abschnitt 4: 19 % von 10 Mio. sind 1,9 Mio.
- Restwert:
  - Faktor 22,2 ergibt 2,22 Mio.
  - Die Nettoanfangsrendite ergibt 1,78 Mio., abzüglich 7 % Erwerbsnebenkosten 1,66 Mio.
  - Der Faktor auf den Reinertrag ergibt −20 %.
  - Die Nettoanfangsrendite auf die Miete ergibt +25 % bzw. +33,8 %; die Aussage „mindestens ein Viertel" stimmt.
- Abschnitt 6: Abschreibung 16.000 gegen 40.000 €; Gewerbesteuer 7,0 / 9,8 %; Baukostenstress 4.900 · 1,1 = 5.390 > 5.200; Umlage 960 / 2.240 € und 1,52 €/m²; Kirchner 9,76 %.

## Befunde aus Runde 2

| Nr. | Befund Runde 2 | Stand | Fundstelle in der Überarbeitung |
|---|---|---|---|
| 1 | Saldierung von Einlagen und Entnahmen fehlt | behoben; Restproblem bei zeitversetzten Zahlungen siehe neuer Befund 1 | A.3 Nr. 13; Einordnung als modifizierter interner Zinsfuß in Nr. 12; Testfall „Nachschuss und Entnahme“ in A.6; Abschnitt 3, Tabelle Zeile 3 |
| 2 | Randfall „Endwert ≤ 0“ passt nicht zur Formel | behoben (Zähler maßgeblich, Nenner null = nicht definiert) | A.3 Nr. 15 |
| 3 | Rundungsregel gegen Abnahmekriterium „auf den Cent“ | behoben: Toleranz je Referenzfall; Rundung je Zahlungsart; Rundungsart und Zinstage je Darlehen einstellbar; Steuerregel; Abbruchkriterium umgestellt. Rest: Befunde 3 und 5 | A.2 Nr. 10; A.6 mit Nr. 28; Abschnitt 1, Tabelle „Freigabepunkte“, Zeile „Vor Teilschritt 1b“ |
| 4 | Kein Genauigkeitsziel für das 5-%-Quantil | behoben (Ziel, Laufzahlen, Schätzung aus Wiederholungen, Server für Berichtsläufe) | A.7 Nr. 35, 36; Abschnitt 3 letzter Absatz; Abschnitt 8 Tabelle |
| 5 | NBank-Entgelt in den Kontrollsummen | behoben (nachgerechnet, Abweichung 0). Rest zu Barzuschüssen: Befund 4 | A.4 Nr. 22, 23; Testfall in Nr. 29 |
| 6 | Effektiver statt nominaler Vergleichszins | behoben; neue Unschärfe bei der Eingabe: Befund 2 | A.3 Nr. 12; Abschnitt 3 „Empfehlung zur Renditeformel“ und „Kennzahlen“ |
| 7 | Zinsstufe ab Jahr 36 | behoben | A.3 Nr. 16; Anhang C.1 |
| 8 | Parameter der Simulationsbeispiele | behoben; Definition des AR-Prozesses offen: Befund 6 | A.7 Nr. 31, 32 |
| 9 | Finanzierungskosten zuwendungsfähig: Widerspruch | behoben | Abschnitt 6 „NBank: Darlehen und Zuschuss …“; Kopfteil Nr. 7 |

## Befunde

**1. [wichtig · belegt] A.3 Nr. 13 (Festlegung „Ausschüttungen und Nachschüsse“ der Spezifikation, Status fest): Die Saldierung je Periode beseitigt den Renditesprung nur, wenn die Zahlungen in exakt derselben Periode liegen. Liegt die Entnahme eine Periode später, springt die Rendite um dieselben 0,63 Prozentpunkte.**

Gegenrechnung im Testfall, Jahresraster; die Endwertdifferenz beträgt in allen drei Fällen 155.571,23:

| Fall | Rendite |
|---|---|
| Nachschuss 50.000 und Entnahme 50.000, beide in t = 2 | 7,876 % |
| Nachschuss 50.000 in t = 2, Entnahme 50.000 in t = 3 (Endwert 585.086,02) | 7,246 % |
| Nachschuss 50.000 und Entnahme 49.000, beide in t = 2 | 7,862 % |

Ursache: Die Formel aus Nr. 12 ist für Entnahmen aus einem Guthaben, das zum Alternativzins steht, unempfindlich. Dieselbe Eigenschaft begründet Nr. 14. Eine Einlage verwässert die Rendite dagegen zum Alternativzins hin, solange sie ungenutzt liegt. Die spätere Entnahme hebt das nicht auf.

Folgen:
- Jahresmodus und Monatsraster weisen für dasselbe Vorhaben verschiedene Renditen aus, sobald Nachschuss und Ausschüttung im selben Jahr, aber in verschiedenen Monaten liegen. Der Jahresmodus saldiert dann, das Monatsraster nicht. Die Größenordnung ist dieselbe wie oben.
- Eine Sensitivität auf den Zahlungszeitpunkt hat eine Sprungstelle.
- Das Vorzeichen der Endwertdifferenz ändert sich nicht, die Ampel gegenüber der Alternative bleibt also richtig.
- Der Abstand zur Zielrendite und zur NBank-Schwelle (Swapsatz plus 100 Basispunkte) springt dagegen. Er kann deshalb allein durch einen Monat Verschiebung kippen.

Eine Formel, die gegen beides unempfindlich ist, gibt es in dieser Quotientenform nicht. Zum Vergleich habe ich die Variante „Endwert durch Barwert der Netto-Eigenkapitalreihe“ gerechnet:
- Sie ist zeitlich stetig: Bei Verschiebung um eine Periode ergibt sie 7,866 %.
- Sie hebt aber die Rendite bei Entnahmen aus dem Guthaben, im Testfall mit 5.000 € je Jahr auf 8,240 %.
- Ihr Nenner kann gegen null gehen.

Vorschlag:
- Im Bericht (Nr. 13) einen Satz ergänzen: Die Saldierung gilt nur periodengleich; eine Einlage, die bis zu einer späteren Entnahme ungenutzt bleibt, senkt die Rendite zum Alternativzins hin, ohne die Endwertdifferenz zu ändern.
- In A.6 den Testfall „Nachschuss t = 2, Entnahme t = 3: Rendite 7,246 %, Endwertdifferenz wie im Testfall“ aufnehmen.
- In der Spezifikation bewusst entscheiden, ob das hingenommen wird (die Endwertdifferenz ist ohnehin das Entscheidungsmaß) oder ob Rückführungen von Einlagen kumuliert gegen frühere Einlagen verrechnet werden. Die Entscheidung im Entscheidungsprotokoll festhalten.
- Die Abweichung zwischen Jahresmodus und Monatsraster als benannte Konventionswirkung führen.

**2. [Hinweis · belegt] A.3 Nr. 12: Ob der eingegebene Alternativzins nominal oder effektiv gemeint ist, bleibt offen.**

Nr. 12 bildet den Monatsfaktor als q = 1 + h·(1 − s)/12 und behandelt h damit als Nominalzins. Daraus folgt der ausgewiesene Vergleichszins von 1,409 %. Derselbe Absatz verlangt aber, alle Vergleichssätze einschließlich des Alternativzinses „als effektive Jahreszinsen“ zu führen.

Ein Anwender, der 2 % als Effektivzins einer Anlage eingibt, erhält mit h/12 im Monatsraster tatsächlich 2,018 % vor Steuern. Die Abweichung zur konformen Umrechnung (1 + h)^(1/12) beträgt rund einen Basispunkt nach Steuern. Bei Darlehen ist die Frage gewichtiger: Ein Sollzins von 4 % nominal/12 und 4 % konform umgerechnet unterscheiden sich um rund 0,07 Prozentpunkte. Auf 700.000 € sind das etwa 500 € Zins im Jahr.

Vorschlag: In Nr. 6 je Zahlungsart die Umrechnung des Jahressatzes festschreiben:
- Darlehen nominal geteilt durch zwölf, wie der Vertrag es vorsieht;
- Alternativzins, Zielrendite und NBank-Schwelle als effektive Eingabe, konform umgerechnet, oder ausdrücklich nominal mit ausgewiesenem Effektivwert.

Danach das Beispiel 1,409 % entsprechend benennen.

**3. [Hinweis · belegt] A.2 Nr. 10, letzter Spiegelstrich: Die Formulierung widerspricht sich, und für nicht abbrechende Quotienten fehlt eine Regel.**

„Kennzahlen bleiben ungerundet“ steht direkt neben „Potenzen und Wurzeln … bleiben gerundete Größen“. Gemeint ist vermutlich: Sie sind nicht exakt darstellbar und werden mit der Rechengenauigkeit geführt.

Exakt nicht darstellbar sind aber schon i/12 (0,04/12 = 0,00333…) und jede Zinstagezählung act/360. Die Reihenfolge der Operationen entscheidet deshalb über Cent-Rundungen. Bei 28 Stellen weichen K·(i/12) und (K·i)/12 nach kaufmännischer Rundung in 22 von 200.000 zufälligen Zinsbuchungen um einen Cent voneinander ab. Bei 120 Raten kann das die Restschuld gegen den Kontoauszug verschieben, also genau das, was Nr. 10 verhindern soll.

Vorschlag:
- Den Satz neu fassen: „Kennzahlen werden nicht gerundet; Potenzen und Wurzeln werden mit der vollen Rechengenauigkeit geführt.“
- In die Spezifikation aufnehmen: „Zinsbetrag = Kapital × Satz × Tage ÷ Basis, Division zuletzt, dann Rundung“.

**4. [Hinweis · begründete Einschätzung] A.4 Nr. 23: Barzuschüsse sind keinem Glied der Bestandsprobe zugeordnet.**

Die Probe nennt „Zuschüsse ohne Geldfluss“, aber nicht den NBank-Zuschuss mit Geldfluss. Er beträgt bis zu 40 % der zuwendungsfähigen Kosten; in Gruppe A sind das 2,32 Mio. €. Auf diesen Zuschuss werden 0,75 % einbehalten, in Gruppe A 17.400 €.

Nachgerechnet: Wird der Zuschuss brutto als originäre Zahlung gebucht und das Entgelt als einbehaltener Betrag abgezogen, schließt die Probe mit Abweichung 0. Wird er netto gebucht und das Entgelt trotzdem abgezogen, meldet sie in Gruppe A 17.400 € Abweichung.

Nr. 22 lässt außerdem offen, ob das Zuschussentgelt gegen die erste Darlehensrate aufgerechnet wird. In diesem Fall gehört es in die Darlehensprobe.

Vorschlag: In Nr. 23 „Zuschüsse mit Geldfluss brutto als originäre Zahlung“ ergänzen. Den Testfall in Nr. 29 um den Zuschuss mit Entgelt erweitern.

**5. [Hinweis · belegt] A.6 Tabelle und Nr. 28: Die Begründung der IWU-Toleranz trägt den Wert nicht, und die Neufestschreibung betrifft auch die Varianten.**

(a) „3,40 Euro je veröffentlichtem Wert, weil die Quelle volle Euro ausweist“: Rundung auf volle Euro erklärt höchstens 0,50 € je Wert. Die 3,40 € sind offenbar die beobachtete größte Abweichung der Nachrechnung, kumuliert aus gerundeten Zwischenwerten der Quelle. Eine Toleranz, die gleich der beobachteten Abweichung gesetzt ist, prüft nur, dass sich nichts verschlechtert. Das ist vertretbar, sollte aber so benannt werden.

(b) Nr. 28 belegt den unveränderten Endwert unter den Rundungsregeln nur für den Testfall. Für die Varianten zeigt die Nachrechnung:

| Fall | Endwert nach Nr. 10 | Referenzwert in A.6 | Abweichung |
|---|---|---|---|
| Nachschuss | 636.495,81 € | 636.495,82 € | genau 0,01 €, an der Toleranzgrenze |
| Kontokorrent mit Entnahmen | 534.928,69 € | 534.928,6878 € (ungerundet) | – |
| Miete als Vorjahreswert | 588.484,90 € | 588.484,9051 € (ungerundet) | – |

Die angekündigte Neufestschreibung ist also nötig, nicht nur vorsorglich.

Vorschlag:
- Die Toleranz für IWU 2013 als „0,50 € je unmittelbar abgelesenem Wert, 3,40 € für fortgeschriebene Werte (beobachtete Höchstabweichung aus gerundeten Zwischenwerten der Quelle)“ fassen.
- In Nr. 28 nennen, dass die Variante Nachschuss sich durch die Rundung um einen Cent verschiebt.

**6. [Hinweis · belegt] A.7 Nr. 32: Die Prozessdefinition ist für einen Testfall nicht eindeutig.**

Die Werte 5,7 / 11,6 / 18 % ergeben sich nur unter zwei Annahmen, die der Text nicht nennt:
- „1,5 Punkte Streuung“ ist die stationäre Randstreuung des AR(1)-Prozesses, also eine Innovation von 1,5·√(1 − 0,7²) = 1,07 Punkten mit Startwert aus der stationären Verteilung.
- Die Streuung des Mietniveaus ist in Prozent des Ausgangsniveaus gemessen.

Mit 1,5 Punkten als Innovation ergeben sich 15,3 % statt 11,6 %. Bezogen auf das mittlere Niveau sind es 4,7 / 9,5 / 14,8 %.

Vorschlag: Beide Festlegungen in einem Halbsatz nennen. Sie sind zugleich die Vorgabe dafür, wie das Werkzeug die Eingabe „Streuung“ bei eingestellter Beharrung deutet. Die stationäre Deutung empfehle ich, weil die eingegebene Streuung dann unabhängig von der Beharrung die Streuung eines Jahreswerts bleibt.

## Nicht geprüft

- IWU-Beispiel 2013: Für eine Nachrechnung fehlen die vollständigen Zahlungsreihen.
- Monatsraster-Variante (585.937,57): nicht neu gerechnet, weil die Monatskonventionen (Steuermonat, Mietzahlung) im Bericht nicht vollständig festgelegt sind. Der Wert ist gegenüber Runde 2 unverändert.
- Lesarten der Gesamtkapitalrendite (4,61 / 4,69 / 4,76 %) und Amortisationsdauer (2 gegen 3 Jahre): Der Text ist unverändert.
- Anstieg der NBank-Bemessungsgrenze um „gut 9 %“: Der Vorwert steht nicht im Bericht.
- Richtlinientexte der NBank und Rechtsgeltung der Parameter in Anhang B und C gehören zu anderen Rollen. Gerechnet habe ich mit den Werten des Berichts.
- Gleichheit von Server und Browser lässt sich ohne Code nicht messen.
