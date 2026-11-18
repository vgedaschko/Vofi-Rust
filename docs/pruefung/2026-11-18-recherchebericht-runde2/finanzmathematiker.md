```
Rolle: Prüfer Finanzmathematiker (Runde 2)
Prüfobjekt: reports/VOFI Immobiliensoftware Marktrecherche.md, überarbeitete Fassung nach Runde 1
            (Schwerpunkt Abschnitt 3, Rechenaussagen in Abschnitt 6 und 8, Anhang A)
Gesamturteil: Trägt mit Auflagen. Alle nachgerechneten Zahlen stimmen auf den Cent. Sieben der acht
Befunde aus Runde 1 sind behoben, einer teilweise. Die Vorgaben in Anhang A taugen als Grundlage der
Rechenkern-Spezifikation, sobald vier Stellen eindeutig gefasst sind: die Saldierung von Einlagen und
Entnahmen in der Renditeformel, der Randfall „Endwert ≤ 0“, die Rundungsregel im Verhältnis zu den
Abnahmekriterien und das Genauigkeitsziel für das 5-%-Quantil. Dazu kommt eine Lücke in den
Kontrollsummen beim NBank-Bearbeitungsentgelt.
Note: 8 von 10. Zur 9 fehlen: die Saldierungsregel für Einlagen und Entnahmen (Befund 1); das
Randfallkriterium auf den Zähler der Renditeformel umstellen (2); Rundungsregel und Abnahmekriterium
in Einklang bringen (3); ein Genauigkeitsziel für die Hauptgrößen mit dazu passenden Laufzahlen (4);
einbehaltene Entgelte in den Kontrollsummen (5).
```

Gegenrechnungen: eigene Python-Skripte mit exakter Bruchrechnung bzw. `decimal` mit 40 Stellen unter
`/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/runde2-finmath/`
(`r1_modell.py` Testfall, Rendite und Kontrollsumme; `r2_kw_rundung.py` Kapitalwert-Probe und Rundung;
`r3_laufzahlen.py` Laufzahlen; `r4_bau_nbank.py` Bauzeitzinsen, NBank und Beispiele aus Abschnitt 4 und 6).
Das Testfallmodell ist neu geschrieben; die Skripte aus Runde 1 habe ich nur zum Abgleich der Annahmen gelesen.

**Unabhängig bestätigt (keine Befunde):**

Testfall und Varianten
- Testfall: Endwert 584.366,28, Endwertdifferenz 155.571,23, Rendite 7,8760 %.
- Entnahmevariante: Endwert 558.656,41, ungespiegelte Endwertdifferenz 129.861,36, naive Rendite 6,91 %. Mit der empfohlenen Formel 7,8760 %.
- Kontokorrentvariante: Endwert 561.526,16, ohne Kontokorrentzins 1.839,71 mehr. Rendite 8,1228 %, mit Entnahmen 8,0886 %.

Nachschuss (Nr. 14)
- Endwert 636.495,82, Endwertdifferenz 155.571,23.
- Die vier Lesarten ergeben 7,1807 %, 7,2461 % (empfohlene Formel), 7,5045 % und 7,8760 %.
- Äquivalenz in Nr. 12 algebraisch geprüft: Mit Spiegelung gilt EW_Alt = q^N·Σ Einlage·q^(−t) − Σ Entnahme·q^(N−t). Daraus folgt ΔEW > 0 ⇔ Zähler/Nenner > q^N ⇔ r > q^(N/n) − 1.

Kontrollsumme Nr. 23
Die erweiterte Formel ergibt in jeder Periode eine Abweichung von exakt 0. Geprüft habe ich folgende Fälle:
- Basis
- Tilgungszuschuss 35.000 in t = 2
- Disagio 3 %
- Tilgungszuschuss, Disagio, Nachschuss und Entnahmen kombiniert
- Kontokorrent mit Entnahmen und Disagio

Kapitalwert-Probe Nr. 24
- Bei einheitlich 4 % sind Kapitalwert und abgezinste Endwertdifferenz beide 110.371,99 (Differenz 0).
- Im Testfall stehen 145.124,09 gegen 190.202,20, die Abweichung beträgt 45.078,11.

Rundung Nr. 10
Restschuld bei voller Genauigkeit 528.208,5612, bei kaufmännischer Cent-Rundung je Rate 528.208,51.

Monatsraster Nr. 8
Ergebnis aus Runde 1 übernommen (585.937,57, also 1.571,29 mehr), unverändert im Text.

Bauzeit Nr. 26 und 27
Gerechnet unter den jetzt genannten Annahmen:
- Ein Durchlauf ergibt 235.370,02 Zins und 70,69 % Fremdkapital.
- Der Fixpunkt ist nach 6 Durchläufen erreicht: 3.069.183,25 Eigenkapital, 230.610,83 Zins, 70,00 %.
- Bei voller Kreditfinanzierung ergibt sich 494.134. Die Faustformel liefert 500.000, das 2,168-Fache.

Laufzahlen Nr. 37
- Mittelwert der Rendite: 6.146,56 / 13.829,76 / 38.416 Läufe, aufgerundet 6.147 / 13.830 / 38.416.
- Bei 1.000 Läufen und 3 % Streuung: Halbbreite 18,59 Basispunkte, Standardfehler 9,49 Basispunkte.

NBank (Abschnitt 6)
- 40+40 = 60+20 = 70+10 = 80 %.
- Entgelte 0,700 / 0,750 / 0,775 % der zuwendungsfähigen Kosten.

Weitere Beispiele
- Abschnitt 6, Mietrecht: Umlage 960 bzw. 2.240 €/Jahr, Differenz 1,52 €/m² im Monat; Drittmittelabzug 960.
- Abschnitt 4, Restwert: 2,22 bzw. 1,78 Mio., Faktor 1,25.
- Abschnitt 4: 19 % von 10 Mio. sind 1,9 Mio.

## Befunde aus Runde 1

| Nr. | Befund Runde 1 | Stand | Fundstelle in der Überarbeitung |
|---|---|---|---|
| 1 | Renditeformel nur für eine Einlage in t = 0 | behoben; neue Lücken siehe Befunde 1, 2, 6 | A.3 Nr. 12–14; Abschnitt 3 „Empfehlung zur Renditeformel“; Testfall Nachschuss in Nr. 31 vorgesehen; Begründungssatz in Nr. 13 ergänzt |
| 2 | Bestands-Kontrollsumme ohne Tilgungszuschuss und Disagio | behoben (nachgerechnet); Lücke beim Bearbeitungsentgelt siehe Befund 5 | A.4 Nr. 22, 23 |
| 3 | Laufzahlen: Bezugsgröße, Konfidenzniveau, Verfahren | teilweise: Konfidenzniveau, Standardfehler und Einschränkung auf einfache Zufallsziehung ergänzt; Bezugsgröße weiter der Mittelwert der Rendite, Quantil ohne Genauigkeitsziel, siehe Befund 4 | A.7 Nr. 37; Abschnitt 8, letzter Absatz |
| 4 | „Rechnerisch ausfinanziert“ falsch | behoben | Abschnitt 6, „NBank: Darlehen und Zuschuss decken höchstens 80 %“; kleiner Rest siehe Befund 9 |
| 5 | Rundung: „centgenau“ und „Rundung nur in der Anzeige“ | behoben im Grundsatz; Rundungsregel kollidiert mit dem Abnahmekriterium, siehe Befund 3 | A.2 Nr. 10; Abschnitt 8, zweiter Absatz |
| 6 | Kapitalwert-Probe ohne Abzinsungssatz | behoben (110.371,99 nachgerechnet) | A.4 Nr. 24 |
| 7 | Bauzeitzins-Beispiel ohne tragende Annahmen | behoben | A.5 Nr. 26 |
| 8 | Randfall Zins null; NBank-Darlehen | behoben; Zinsstufe ab Jahr 36 fehlt, siehe Befund 7 | A.3 Nr. 15, 16; Abschnitt 3, Absatz „Vier weitere Punkte“ |

## Befunde

**1. [wichtig · belegt] A.3 Nr. 12: Die Renditeformel ergibt für denselben Zahlungsstrom verschiedene Renditen, je nachdem, ob Einlage und Entnahme einer Periode brutto oder saldiert eingehen.**
Die Formel setzt Entnahmen in den Zähler (aufgezinst) und Einlagen in den Nenner (abgezinst). Eine Saldierungsregel fehlt. Der Fehler fällt nur weg, wenn die Rendite gerade dem Alternativzins entspricht.

Gegenrechnung: Testfall mit Nachschuss 50.000 und Entnahme 50.000, beide in t = 2. Der Endwert bleibt bei 584.366,28, die Endwertdifferenz bei 155.571,23.
- Saldiert ergibt die Formel 7,876 %.
- Brutto ergibt sie (584.366,28 + 50.000·1,014³) / (400.000 + 50.000·1,014⁻²), also 7,246 %.

Das ist dieselbe Spanne von 0,63 Prozentpunkten, die Nr. 14 als Mangel der Lesarten anführt. Der Fall entsteht zwangsläufig im Jahresmodus und in jeder Jahresverdichtung, sobald in einem Jahr ein Nachschuss in der Bauphase und eine Ausschüttung zusammenfallen. Ebenso entsteht er, wenn Förder-Eigenkapitalersatz und Ausschüttung in derselben Periode gebucht werden.

Vorschlag: In Nr. 12 festschreiben, dass Einlagen und Entnahmen je Rechenperiode des Kerns (monatlich) saldiert werden. Ein positiver Saldo zählt als Einlage, ein negativer als Entnahme. Der Jahresmodus rechnet mit den Jahressalden und weist das aus. Die Formel ist ein modifizierter interner Zinsfuß, bei dem Finanzierungs- und Wiederanlagesatz dem Alternativzins nach Steuern entsprechen. Das sollte zur Einordnung in der Literatur so benannt werden. Den Fall „Einlage und Entnahme in derselben Periode“ in Nr. 31 als Testfall aufnehmen.

**2. [wichtig · belegt] A.3 Nr. 15 gegen Nr. 12: Das Randfallkriterium „Endwert ≤ 0 ⇒ −100 %“ passt nicht mehr zur neuen Formel.**
Mit Entnahmen ist der Zähler EW + Σ Entnahme·q^(N−t). Er kann positiv sein, obwohl der Endwert negativ ist. Beispiel: Endwert −10.000, aufgezinste Entnahmen 50.000, Eigenkapital 400.000, fünf Jahre. Die Formel liefert (40.000/400.000)^(1/5) − 1 = −36,9 %, Nr. 15 schreibt −100 % vor.

Die Kennzahl springt dadurch unstetig: Ein Endwert von +1 Euro ergibt etwa −36,9 %, einer von −1 Euro ergibt −100 %. Das verzerrt Quantile der Rendite in der Simulation und widerspricht der Spezifikation (Abschnitt 3, „Randfälle … definierte Ergebnisse“), weil zwei verschiedene Ergebnisse definiert sind.

Vorschlag: „Ist der Zähler der Renditeformel null oder negativ, beträgt die Rendite −100 %; ist der Nenner null (keine Einlagen), ist sie nicht definiert und wird als solche ausgewiesen.“

**3. [wichtig · belegt] A.2 Nr. 10 gegen Abschnitt 1 (Abbruchkriterium vor Teilschritt 1b) und A.6: Rundungsregel und Abnahmekriterium „auf den Cent“ sind nicht miteinander vereinbar.**
(a) Das Abbruchkriterium lautet „die Referenzfälle nicht auf den Cent stimmen“. Der IWU-Fall 2013 ist nach Abschnitt 3 aber nur „bis auf Rundungsdifferenzen von höchstens 3,40 Euro reproduzierbar“, weil die Quelle volle Euro ausweist. Das Kriterium ist für diesen Fall nie erfüllbar.

(b) Der Testfall rechnet mit einem pauschalen Steuersatz von 30 %. „Steuerbeträge nach den jeweiligen Vorschriften“ ist dafür nicht definiert. Die Wahl verschiebt den Referenzwert:
- Zinsen und Steuer auf Cent gerundet: 584.366,28 (Abweichung unter 1 Cent).
- Steuer auf volle Euro abgerundet: 584.367,59, also 1,31 Euro mehr.

(c) „Runden wie die Bank“ (so auch die Spezifikation: „bankübliche Rundung“) ist nicht eindeutig. Im Beispiel aus Nr. 10 beträgt die Restschuld nach zehn Jahren:
- bei kaufmännischer Rundung 528.208,51
- bei Abschneiden 528.207,91 (60 Cent Unterschied)

Die Zinstagezählung, etwa 30/360 gegenüber act/360, ist ebenfalls nicht festgelegt.

(d) Die Regel „je Kontoart“ nennt nur Darlehen, Steuer und Kennzahlen. Offen bleiben Geldanlage, Kontokorrent (Habenzinsen, Kontokorrentzinsen) und indexierte Mieten, die im Testfall Bruchteile von Cent erzeugen (55.000·1,02^t).

Vorschlag: Je Darlehen den Rundungsmodus (Standard kaufmännisch) und die Zinstagezählung als Parameter festlegen. Geldanlage und Kontokorrent auf Cent je Buchung runden. Für pauschale Steuersätze „auf Cent“ festlegen, für tarifliche Steuern die gesetzliche Rundung. Je Referenzfall die Toleranz festschreiben: Kirchner und Testfall 0,01 €; IWU 2013 je Jahreswert 0,5 € gegen die veröffentlichte Tabelle, insgesamt 3,40 €. Das Abbruchkriterium in Abschnitt 1 auf „innerhalb der festgelegten Toleranz“ umstellen.

**4. [wichtig · belegt (unter Normalannahme)] A.7 Nr. 37 und Abschnitt 8, letzter Absatz: Das Genauigkeitsziel für das 5-%-Quantil fehlt, und die genannte Laufzahl passt nicht zum Ziel, das für den Mittelwert gesetzt ist.**
Nr. 37 sagt „Die Zahl der Läufe folgt aus dem Genauigkeitsziel der Hauptgrößen“, setzt ein solches Ziel aber nur für den Mittelwert der Rendite. Diese Größe ist nach Nr. 32 gerade keine Hauptgröße. Für das 5-%-Quantil gilt der Standardfehler √(p(1−p))/φ(z_p)·σ/√N = 2,113·σ/√N. Die nötige Laufzahl ist damit 4,47-mal so hoch wie beim Mittelwert. Bei demselben Ziel (5 Basispunkte Halbbreite, 95 %) braucht es:
- 27.448 Läufe bei 2 % Streuung
- 61.758 Läufe bei 3 % Streuung
- 171.550 Läufe bei 5 % Streuung

Mit 10.000 Läufen beträgt die Halbbreite 8,3 / 12,4 / 20,7 Basispunkte. Eine Simulationsprobe mit 400 Wiederholungen und 3 % Streuung ergab einen Standardfehler von 6,1 Basispunkten, die Formel liefert 6,3.

„Mindestens rund 10.000“ ist als Untergrenze nicht falsch, folgt aber aus keinem genannten Ziel. Bei 3 % Streuung liegt die Zahl über dem Planungswert „10.000 bis 50.000 Läufe im Browser“ (Abschnitt 8). Für die Größe, die die Risikoaussage trägt, kann die Aufteilung zwischen Browser und Server damit anders ausfallen als geplant.

Vorschlag: Genauigkeitsziele unmittelbar an den Hauptgrößen festmachen, zum Beispiel Endwertdifferenz in Euro relativ zur Investitionssumme, Median und 5-%-Quantil, jeweils mit 95-%-Halbbreite. Für das Quantil den Standardfehler über unabhängige Wiederholungen oder Bootstrap schätzen und anzeigen, statt eine feste Laufzahl vorzugeben. Die Rechnung für den Mittelwert der Rendite nur als Einordnung führen oder streichen.

**5. [wichtig · belegt (Rechnung) / Kostenregel nach Notiz 07, nicht an der Richtlinie selbst geprüft] A.4 Nr. 22 und 23: Das NBank-Bearbeitungsentgelt löst denselben Fehlalarm aus, den die Überarbeitung beim Disagio behoben hat.**
Nach Notiz 07 (RL Nr. 12.7.2, 12.7.3) wird das Entgelt von 1 % des Darlehens und 0,75 % des Zuschusses gegen die erste Auszahlungsrate aufgerechnet. Die Restschuld steigt also um den vollen Darlehensbetrag, ausgezahlt werden 99 %. Nr. 22 und 23 kennen als einbehaltenen Betrag nur das Disagio. Beispiel: Gruppe A mit 5,8 Mio. zuwendungsfähigen Kosten ergibt 2,32 Mio. Darlehen und 23.200 € Entgelt. Beide Proben melden 23.200 € Abweichung, obwohl richtig gerechnet wurde. Das betrifft genau das Fördergeschäft aus Teilschritt 1c.

Der laufende Verwaltungskostenbeitrag (0,5 % auf die Restschuld) ist in Nr. 23 keinem Glied zugeordnet, weder Sollzins noch originäre Zahlung. Ebenso fehlen Bereitstellungszinsen und Vorfälligkeitsentschädigung.

Vorschlag: In Nr. 22 und 23 „einbehaltenes Disagio“ ersetzen durch „bei Auszahlung einbehaltene Beträge (Disagio, Bearbeitungsentgelte, sonstige Abzüge)“. Ein Glied „Finanzierungskosten“ definieren, das Sollzinsen, Kontokorrentzinsen, kapitalisierte Zinsen, Bereitstellungszinsen, laufende Beiträge und Vorfälligkeitsentschädigung umfasst. Einen Testfall „NBank-Darlehen mit Entgelt und Verwaltungskostenbeitrag“ in Nr. 31 aufnehmen.

**6. [Hinweis · belegt] A.3 Nr. 12, letzter Satz: Im Monatsraster ist die Vergleichsgröße der effektive, nicht der nominale Alternativzins.**
Mit q = 1 + h(1−s)/12 und dem Exponenten 1/n gilt ΔEW > 0 ⇔ r > (1 + h(1−s)/12)¹² − 1. Im Testfall sind das 1,40902 % statt 1,4 %. Liegt r zwischen beiden Werten, zeigt ein Vergleich mit dem nominalen Satz „über dem Alternativzins“ an, obwohl die Endwertdifferenz negativ ist. Die Spanne beträgt etwa ein Basispunkt, betrifft aber jede Ampel- oder Abstandsanzeige, auch den Abstand zur Zielrendite und die NBank-Schwelle.
Vorschlag: „r liegt genau dann über dem effektiven Jahreszins der Alternative, q^(N/n) − 1, wenn …“; alle Vergleichssätze (Zielrendite, Swapsatz plus 100 Basispunkte) als effektive Jahreszinsen definieren.

**7. [Hinweis · belegt am Bericht selbst] A.3 Nr. 16 und Abschnitt 3 („Das NBank-Darlehen ist 35 Jahre zinslos …“): Die Zinsstufe ab Jahr 36 fehlt in der Vorgabe an den Kern.**
Anhang C und Notiz 07 nennen 0 % bis zum 35. Jahr und danach bis Basiszinssatz plus 3 Prozentpunkte bei Rückzahlung binnen 42 Jahren. Die Spezifikation verlangt genau diesen 42-Jahres-Horizont. Bei linearer Tilgung über 42 Jahre stehen nach 35 Jahren noch 7/42 = 16,7 % des Darlehens aus und tragen dann Zins. Der tatsächliche Tilgungsplan ist offen und liegt bei der NBank.
Vorschlag: Nr. 16 ergänzen um „ab dem 36. Jahr variabler Zins bis Basiszinssatz (§ 247 BGB) plus 3 Prozentpunkte, als Annahme je Kalkulation; Auszahlung 30/30/30/10 nach Baufortschritt; Entgelt einbehalten (Befund 5)“.

**8. [Hinweis · belegt] A.7 Nr. 33 und 34: Die Simulationsbeispiele sind ohne ihre Parameter nicht nachrechenbar.**
Für die Spanne 18,0 bis 29,4 fehlt die Angabe „20 Zufallsstarts mit je 10.000 Läufen“ (Notiz 09). Für 5,7 / 11,6 / 18 % fehlen die Angaben „Wachstum normalverteilt mit 2 % Mittel und 1,5 % Streuung, mittlere Beharrung = AR(1) mit 0,7“. Ohne diese Angaben kann die Spezifikation die Zahlen nicht als Testfälle übernehmen. Meine Nachrechnung aus Runde 1 ergab mit diesen Parametern 5,7 / 11,6 / 18,1 %.
Vorschlag: Die Parameter je Beispiel in einem Halbsatz nennen.

**9. [Hinweis · begründete Einschätzung] Abschnitt 6 gegen Abschnitt 9: Finanzierungskosten sind einmal festgestellt nicht zuwendungsfähig, einmal offen.**
Abschnitt 6 zählt Finanzierungskosten einschließlich Bauzeitzinsen ohne Vorbehalt zu den „zusätzlich zu finanzieren[den]“ Kosten. Abschnitt 9 führt als offene Frage an die NBank, „ob nicht abziehbare Vorsteuer und Finanzierungskosten zu den zuwendungsfähigen Kosten zählen“. Für die Finanzierungslücke ist das erheblich: Die Bauzeitzinsen aus Nr. 26 (230.611 € bei 10 Mio.) wären je nach Antwort zu 80 % gefördert oder voll aus Eigenmitteln zu decken.
Vorschlag: In Abschnitt 6 „nach dem Wortlaut von RL Nr. 1.5 nicht zuwendungsfähig (Kostengruppe 800); Bestätigung durch die NBank offen“ schreiben.

## Nicht geprüft

- Die drei Lesarten der Gesamtkapitalrendite (4,61 / 4,69 / 4,76 %) und die Amortisationsdauer (2 gegen 3 Jahre) habe ich nicht neu gerechnet; der Text ist gegenüber Runde 1 unverändert.
- Die Streuung des Verkaufsfaktors (18,0 bis 29,4) habe ich nicht neu simuliert, ebenso wenig das IWU-Beispiel 2013. Für dieses fehlen die vollständigen Zahlungsreihen.
- Richtlinientext der NBank: Kostenabgrenzung und Aufrechnung des Entgelts habe ich an Notiz 07 geprüft, nicht am Original.
- Rechtliche Geltung von Steuer-, Miet- und Förderwerten in Anhang B und C gehört zu einer anderen Rolle. Gerechnet habe ich nur mit den Werten des Berichts.
- Abweichungen zwischen Server und Browser lassen sich ohne Code nicht messen.
