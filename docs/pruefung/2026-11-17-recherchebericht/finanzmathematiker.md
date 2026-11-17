```
Rolle: Prüfer Finanzmathematiker
Prüfobjekt: reports/VOFI Immobiliensoftware Marktrecherche.md (Schwerpunkt Abschnitt „Best Practice“, Z. 41–79;
            dazu Z. 137 Gewerbesteuer, Z. 160 NBank-Ausfinanzierung, Z. 170 Dezimalarithmetik, Z. 186 Laufzahlen)
Gesamturteil: Trägt mit Auflagen. Alle nachgerechneten Zahlen stimmen (Testfall, Varianten, Laufzahlen, Bauzeitzinsen,
Gewerbesteuer, 80-%-Summe). Die selbst gesetzte Rendite-Lesart bei Entnahmen passt zum Entscheidungskriterium
und liefert im Testfall tatsächlich 7,88 %. Lücken gibt es dort, wo der Bericht über die Notizen hinaus selbst
festlegt: gestaffelte Einlagen, eine Kontrollsumme, die Rundung, die Bemessung der Laufzahlen und die Aussage
„rechnerisch ausfinanziert“.
Note: 7 von 10. Zur 9 fehlen: eine Renditeformel, die auch Nachschüsse und Einlagen über die Bauzeit abdeckt; eine
Bestands-Kontrollsumme, die auch Zuschüsse und Disagio erfasst; eine Rundungsregel, die zu Bank- und Steuerbescheiden
passt; Laufzahlen, die zur gewählten Hauptgröße und zum Stichprobenverfahren passen; eine Ausfinanzierungsaussage,
die nicht zuwendungsfähige Kosten mit einrechnet.
```

Gegenrechnungen: eigene Python-Skripte (exakte Bruchrechnung oder `decimal` mit 40 Stellen) unter
`/tmp/claude-0/-home-user-Claude-Code/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/pruefrunde-finmath/`
(p1_kennzahlen.py bis p6_monat.py). Ich habe die Skripte der Notiz 09 nicht verwendet.

**Unabhängig bestätigt (keine Befunde):** Endwert 584.366,28; Endwertdifferenz 155.571,23; VOFI-Rendite 7,876 %.
Entnahmevariante: Endwert 558.656,41, naive Endwertdifferenz 129.861,36 (also 25.709,87 zu niedrig), naive Rendite 6,91 %.
Kontokorrentvariante: Endwert 561.526,16. Kapitalwert-Probe: 145.124,09 gegen 190.202,20, Abweichung 45.078,11.
Schuldendienstdeckung 1,4175 bzw. 0,0894. Mietindex-Lesart: Rendite 8,028 %. Monatsraster: +1.571,29.
Kirchner: (1.322,48/1.000)^(1/3) − 1 = 9,76 %. IWU: (153.032/71.194)^(1/25) − 1 = 3,11 %.
Bauzeitzinsen (10 Mio., 24 Monate linear, 5 %, Eigenkapital zuerst, Zins auf den Vormonatsstand kapitalisiert):
ein Durchlauf 235.370,02 Zins und 70,69 % Fremdkapital; Fixpunkt nach 6 Iterationen bei 3.069.183,25 Eigenkapital
und 230.610,83 Zins; Faustformel 500.000, also das 2,17-Fache.
Laufzahlen: (1,96·σ/0,0005)² = 6.146,56 / 13.829,76 / 38.416, aufgerundet 6.147 / 13.830 / 38.416.
Halbbreite bei 1.000 Läufen und σ = 3 % = 18,59 Basispunkte.
Mietniveau nach 10 Jahren: 5,7 / 11,6 / 18,1 %. Gewerbesteuer: 3,5 % × 200 % = 7,0 %, 3,5 % × 280 % = 9,8 %.
NBank: 40+40 = 60+20 = 70+10 = 80 %.

Zur Rendite-Lesart bei Entnahmen (Z. 51): Sie ist mit dem Entscheidungskriterium widerspruchsfrei. Mit q = 1 + h(1−s) und A = Σ Entnahme_t · q^(n−t) gilt
r > Alternativrendite ⇔ (EW + A)/EK > qⁿ ⇔ EW > EK·qⁿ − A = Endwert der gespiegelten Alternative ⇔ ΔEW > 0.
„Unverändert 7,88 %“ stimmt (7,8760 %). Der Wert bleibt aber nur deshalb gleich, weil die Investition ihr Guthaben im
Testfall selbst zum Alternativzins anlegt. Siehe Befund 1.

## Befunde

**1. [wichtig · belegt] Z. 51, Rendite-Lesart bei Entnahmen – nur für eine einzige Einlage in t = 0 definiert, obwohl der Bericht selbst Einlagen über die Zeit vorsieht.**
Die Formel (Endwert + aufgezinste Entnahmen) / Eigenmittel setzt genau eine Einlage voraus. Der Bericht verlangt aber selbst „Eigenkapital zuerst“ über die Bauzeit (Z. 63), eine Zeile für Eigenkapitalnachschuss (Z. 47) und den Neubau als Stufe 1. Dort fließt das Eigenkapital über viele Monate, und der Normalfall ist nicht abgedeckt.
Gegenrechnung: Testfall plus Nachschuss von 50.000 in t = 2 ergibt einen Endwert von 636.495,82. Die naheliegenden Lesarten liefern:
- 7,18 % (Summe der Einlagen als Nenner)
- 7,25 % (Einlagen zum Alternativzins auf t = 0 abgezinst)
- 7,50 % (interner Zins der Eigenkapitalreihe)
- 7,88 % (Nachschuss wie eine negative Entnahme aufgezinst)

Die Spanne beträgt 0,7 Prozentpunkte bei gleicher Endwertdifferenz von 155.571,23.
Ergänzend: Der Satz „liefert im Testfall unverändert 7,88 %“ lässt sich als allgemeine Eigenschaft missverstehen. In der Kontokorrentvariante (380.000 Eigenkapital) sinkt die Rendite mit Entnahmen von 8,12 % auf 8,09 %. Das ist richtig, weil die Entnahmen dort über Kontokorrent finanziert werden.
Vorschlag: Die Formel für beliebige Eigenkapitalreihen festschreiben, etwa r = ((EW + Σ Entnahme_t·q^(n−t)) / Σ Einlage_t·q^(−t))^(1/n) − 1 mit q je Periode, im Monatsraster q = 1 + h(1−s)/12. Auch diese Form ist mit ΔEW > 0 widerspruchsfrei. Den Satz ergänzen: „weil die Investition im Testfall ihr Guthaben selbst zum Alternativzins anlegt“. Einen Testfall mit Nachschuss aufnehmen.

**2. [wichtig · belegt] Z. 47, Kontrollsumme Bestandssaldo – schlägt bei Tilgungszuschuss und Disagio an, obwohl richtig gerechnet wurde.**
Der Bericht fordert: Die Veränderung des Bestandssaldos entspricht in jeder Periode originärer Zahlung plus Eigenkapital minus Sollzinsen plus Habenzinsen minus Steuer. Ein Tilgungszuschuss senkt aber die Restschuld ohne Geldfluss, und das sagt der Bericht in Z. 145 selbst. Beim Disagio ist die Restschuld höher als die Auszahlung.
Gegenrechnung: Testfall mit KfW-Tilgungszuschuss von 35.000 in t = 2. Die Veränderung des Bestandssaldos beträgt 60.484,52, die Formel liefert 25.484,52, die Abweichung genau 35.000. In allen anderen Perioden ist sie 0. Beim Disagio (3 % auf 700.000) entsteht analog −21.000 in t = 0.
Die Kreditprobe im selben Absatz berücksichtigt Zuschüsse und Disagio bereits, die Bestandsprobe nicht. Das ist inkonsistent und erzeugt Fehlalarme, die mit hoher Wahrscheinlichkeit abgeschaltet würden.
Vorschlag: „… + Zuschüsse ohne Geldfluss (Tilgungszuschuss, Teilschulderlass) − Disagio bzw. nicht ausgezahlte Kreditbeträge − kapitalisierte Zinsen“ ergänzen, oder alle Zinsen einschließlich kapitalisierter unter „Sollzinsen“ definieren und das ausdrücklich sagen.

**3. [wichtig · belegt] Z. 79 und Z. 186, Laufzahlen der Simulation – Rechnung richtig, Bezugsgröße und Verfahren passen nicht.**
(a) Die Laufzahlen werden aus der Genauigkeit der *erwarteten Rendite* abgeleitet. Z. 57 erklärt aber Endwertdifferenz und Quantile zu Hauptgrößen, „nicht der Mittelwert der Rendite“. Bei negativen Endwerten setzt Z. 57 die Rendite auf −100 %, was die Streuung künstlich erhöht. Die Kapazitätsaussage in Z. 186 („Bedarf von rund 6.000 bis 40.000 Läufen“) beruht damit auf einer Größe, die der Bericht selbst nicht als Hauptgröße will.
(b) „Auf fünf Basispunkte genau“ und „Unschärfe 18,6 Basispunkte“ sind Halbbreiten des 95-%-Konfidenzintervalls. Der Standardfehler beträgt 9,5 Basispunkte. Das steht nicht da.
(c) Die Formel N = (1,96·σ/Genauigkeit)² gilt nur für einfache Zufallsziehung. Notiz 09 (Befund 10b) hat gezeigt, dass Latin Hypercube Sampling bei 1.000 Läufen 0,5 statt 4,8 Basispunkte Fehler hat. Der Bericht übernimmt die Laufzahlen ohne diese Einschränkung.
Vorschlag: Das Genauigkeitsziel an Endwertdifferenz, Median und 5-%-Quantil festmachen (für das Quantil laut Notiz mindestens etwa 10.000 Läufe). „95-%-Konfidenz“ und „bei einfacher Zufallsziehung“ dazuschreiben. Den Fehler bei geschichteten Verfahren über unabhängige Wiederholungen schätzen.

**4. [wichtig · belegt (Rechnung) / begründete Einschätzung (Kostenabgrenzung)] Z. 160, NBank-Ausfinanzierung – 80 % stimmt, der Schluss „rechnerisch ausfinanziert“ nicht.**
Darlehen und Zuschuss ergeben in A, B und C je 80 % der *zuwendungsfähigen* Kosten. Es sind Höchstsätze („bis“). Mit 20 % Eigenmitteln sind damit aber nur die zuwendungsfähigen Kosten gedeckt. Laut Notiz 07 (RL 1.5, 5.3.2) sind das Kostengruppen 100–700, mit dem Grundstück höchstens zum Bodenrichtwert. Nicht gedeckt sind:
- Kostengruppe 800, also Finanzierungskosten einschließlich der vom Bericht selbst geforderten Bauzeitzinsen
- der Grundstückspreis über dem Bodenrichtwert
- die NBank-Entgelte aus Z. 149, rechnerisch 0,70 % (A), 0,75 % (B) und 0,775 % (C) der zuwendungsfähigen Kosten (A: 0,4·1 % + 0,4·0,75 %)

Dazu kommt die Auszahlung 30/30/30/10 nach Baufortschritt, die eine Zwischenfinanzierung erfordert. Beispiel mit 5,8 Mio. zuwendungsfähigen Kosten in Gruppe A: allein 40.600 Euro Entgelte zusätzlich zu den Eigenmitteln von 1,16 Mio., Bauzeitzinsen noch nicht eingerechnet. Die Bedingung „solange die Kosten die Bemessungsgrenze nicht überschreiten“ ist notwendig, aber nicht hinreichend. In der Kundenberatung würde so eine Finanzierungslücke übersehen.
Vorschlag: „Darlehen und Zuschuss decken höchstens 80 % der zuwendungsfähigen Kosten; Finanzierungskosten, Entgelte, Grundstücksanteile über dem Bodenrichtwert und Kosten über der Bemessungsgrenze sind zusätzlich zu finanzieren, die Auszahlung nach Baufortschritt erfordert eine Zwischenfinanzierung.“ Die Kostenabgrenzung habe ich an Notiz 07 geprüft, nicht an der Richtlinie selbst.

**5. [wichtig · belegt] Z. 61 und Z. 170, Rundung und Dezimalarithmetik – „volle Genauigkeit, Rundung nur in der Anzeige“ und „centgenau über jeden Planungshorizont“ passen nicht zusammen.**
28 Stellen garantieren nur, dass Addition und Multiplikation keinen nennenswerten Fehler erzeugen. Centgenau gegenüber einem Bank- oder Förderbank-Tilgungsplan wird das Ergebnis dadurch nicht, denn Banken runden Zins und Tilgung je Rate auf den Cent.
Gegenrechnung: 700.000 zu 4 %, monatliche Rate 3.500, 10 Jahre. Die Restschuld beträgt bei voller Genauigkeit 528.208,5612, bei Cent-Rundung je Rate 528.208,51; die Abweichung liegt bei 5 Cent. Im Testfall erzeugt die Cent-Rundung je Zahlung schon nach 4 Jahren drei Abweichungen von je 1 Cent (Notiz 09).
Steuerbeträge werden nach gesetzlichen Regeln gerundet (ungeprüft im Einzelnen). Potenz-, Wurzel- und Logarithmusfunktionen (Rendite, Monatszins aus Jahreszins, Abzinsung) sind auch in Dezimalarithmetik nur gerundet. Die Quellnotiz 05 empfiehlt das Gegenteil des Berichts: „Rundung explizit an fachlich definierten Stellen (Cent je Periode, Steuer nach Vorschrift)“.
Vorschlag: Je Kontoart eine Rundungsregel festschreiben (Darlehenskonten Cent je Buchung, Steuer nach Vorschrift, Kennzahlen ungerundet). „Centgenau“ ersetzen durch „rechnet ohne Rundungsfehler der Zahldarstellung; Centgenauigkeit gegenüber Bank- und Steuerbescheiden folgt aus den festgelegten Rundungsregeln“.

**6. [Hinweis · belegt] Z. 53, Kapitalwert-Probe – die Bedingungsliste nennt den Abzinsungssatz nicht.**
Die Probe stimmt nur, wenn Kapitalwert und Endwertdifferenz mit i(1−s) abgezinst werden. Die naheliegende Abzinsung der Vorsteuer-Zahlungen mit i(1−s) liefert laut Notiz 09 165.065,96 statt 110.371,99.
Vorschlag: „… Kapitalwert der Zahlungsfolge nach Steuern ohne Zinsen, abgezinst mit i(1−s); die Endwertdifferenz wird mit demselben Satz über n Perioden abgezinst“ ergänzen.

**7. [Hinweis · belegt] Z. 63, Bauzeitzins-Beispiel – die Eingaben, die das Ergebnis tragen, fehlen.**
Zinssatz 5 %, linearer Abfluss, Eigenkapital zuerst und Zins auf den Vormonatsstand stehen nicht im Bericht. Ohne sie sind 70,69 %, 3,07 Mio. und 230.611 nicht nachvollziehbar. Die Aussage „Faustformel trifft bei voller Kreditfinanzierung“ hängt an der Zinskonvention: Zins auf den Vormonatsstand ergibt 494.134, Zins auf den Stand nach dem Abfluss des Monats 537.859, beides gegen 500.000.
Vorschlag: Die vier Annahmen in einem Halbsatz nennen.

**8. [Hinweis · belegt] Z. 57, Randfall Zinssatz null – KfW 296 mit 0,01 % ist kein numerischer Randfall, und beim NBank-Darlehen geht die Annuitätenformel ohnehin nicht direkt.**
Bei 0,01 % rechnet die Annuitätenformel in Gleitkomma auf 10⁻⁹ Euro genau (10.005,5008249595 gegen exakt …587 bei 100.000 über 10 Jahre). Das NBank-Darlehen trägt zusätzlich 0,5 % Verwaltungskostenbeitrag auf die Restschuld, und den Tilgungsplan legt nach Z. 160 die NBank fest.
Vorschlag: Den Randfall auf „Zins exakt 0“ begrenzen. Für das NBank-Darlehen den von der NBank festgesetzten Tilgungsplan plus Verwaltungskostenbeitrag als eigene Darlehensart vorsehen.

## Nicht geprüft

- Die drei Lesarten der Gesamtkapitalrendite (4,61 / 4,69 / 4,76 %) und die Amortisationsdauer (2 gegen 3 Jahre) habe ich nicht neu gerechnet. Sie stammen aus Notiz 09 und hängen an Prüferannahmen.
- Die Streuung des Verkaufsfaktors (18,0–29,4) habe ich nicht neu simuliert. Die Wahrscheinlichkeit negativer Renditen Φ(−3) = 0,135 % passt zu 272 von 200.000.
- Rechtliche Geltung von Mindesthebesatz, NBank-Konditionen und KfW-Zinsen (andere Rolle). Gerechnet habe ich nur mit den Werten des Berichts.
- Abweichungen zwischen Server und Browser lassen sich ohne Code nicht messen.
