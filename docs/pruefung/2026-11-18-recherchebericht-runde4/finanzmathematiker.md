```
Rolle: Prüfer Finanzmathematiker (Runde 4, Änderungsprüfung)
Prüfobjekt: reports/VOFI Immobiliensoftware Marktrecherche.md, Fassung nach Runde 3; geprüft wurden nur
            die Änderungen laut aenderungen-seit-runde3.diff, die Zahlen, Formeln oder Rechenregeln
            betreffen, und was von ihnen abhängt (Abschnitte 1, 3, 5; Anhang A Nr. 3, 10, 12, 13, 23,
            A.6, 28, 29, 31, 32; Anhang B.6 MA-021; Anhang D.1, D.4, D.5; Anhang E.1)
Gesamturteil: Trägt, mit einer Auflage. Alle sechs Hinweise aus Runde 3 sind eingearbeitet, jede neue
  Zahl stimmt nachgerechnet. Die neue Regel „höchster tragbarer Preis = niedrigere aus Rendite- und
  Bankgrenze" ist aber falsch gebaut: Sie behandelt eine Grenze für das Darlehen wie eine Grenze für den
  Preis. Dadurch nennt 1a einen zu niedrigen Preis, sobald die Bankgrenze bindet (Befund 1).
Note: 9 von 10 – die 9 hält. Zur stabilen 9 fehlt im Bericht: Befund 1 umstellen (zwei Sätze in
  Abschnitt 5 und D.5). Die Befunde 2 bis 5 kann auch die Fachspezifikation aufnehmen.
```

Gegenrechnungen: eigene Skripte unter `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/runde4-finmath/`.

| Skript | Inhalt |
|---|---|
| `m3.py` | Testfall aus Runde 3, exakte Bruchrechnung, wahlweise mit Rundung nach Nr. 10 |
| `a.py` | Neue Variante (Entnahme ein Jahr später), Restwert-Doppelzählung, Bankgrenze aus D.4 |
| `b.py`, `c.py` | Vereinfachtes Jahresmodell der Grobkalkulation: Monotonie der Rendite im Preis, Rendite- und Bankgrenze, Grenze bei gedeckeltem Darlehen, Rendite in Abhängigkeit von der Beleihungsquote |

**Unabhängig bestätigt (keine Befunde):**

- **Neue Variante A.6 „Nachschuss, Entnahme ein Jahr später":** Endwert 585.086,0188 €, mit den Rundungsregeln aus Nr. 10 585.086,01 €. Rendite 7,2461 %, Endwertdifferenz 155.571,23 € wie im Testfall. Dieselben Werte stehen in Nr. 13 und in Abschnitt 3 („Kennzahlen") (7,876 → 7,246 %). Gleichzeitig gebucht (t = 2/t = 2) bleibt es bei 7,8760 %.
- **Bankgrenze D.4:**
  - Reinertrag: 134.640 · 0,8 = 107.712 €.
  - Tragbarer Schuldendienst: 107.712 / 1,2 = 89.760 €.
  - Darlehen: 89.760 / 0,06 = 1.496.000 €.
  - Preis: 1.496.000 / 0,65 = 2.301.538 €, also „rund 2,30 Mio.".
  - Bei 2,6 Mio. €: 107.712 / (0,65 · 2,6 Mio. · 0,06) = 1,0622, also „1,06".
  - Die Bankgrenze ist in geschlossener Form eindeutig, weil die Deckung im Preis streng fällt.
- **Renditegrenze:** Im vereinfachten Modell fällt die VOFI-Rendite streng mit dem Preis. Gerechnet für 1,0 bis 4,0 Mio. € in Schritten von 10.000 €, mit fester Beleihungsquote, proportionalen Erwerbsnebenkosten, linearer Abschreibung, Verlustvortrag und Restwert über den Faktor auf die Miete. Grund: Der Endwert fällt mit dem Preis, das Eigenkapital steigt. Die Steuerersparnis aus der Abschreibung (rund 0,05 € je Euro Preis) gleicht das nicht aus. Für P → 0 geht die Rendite gegen unendlich. Die Grenze existiert deshalb und ist eindeutig. Die Zielwertsuche auf den Preis ist bei den genannten Eingaben eindeutig, ebenso die auf Restwertfaktor, Miete und Zins. Für die Beleihungsquote gilt das nicht (Befund 2).
- **Rundung Nr. 10:** Der Satz ist so gefasst wie in Runde 3 vorgeschlagen. Nr. 28 nennt den einen Cent der Variante Nachschuss (636.495,81 €).
- **Nominal und effektiv, Nr. 12:** Der Widerspruch ist aufgelöst. Der Alternativzins geht nominal durch zwölf ein, wird aber effektiv ausgewiesen. Zielrendite und NBank-Schwelle sind effektive Sätze. Die Festlegung je Zahlungsart ist an die Fachspezifikation verwiesen. Das stimmt mit der Spezifikation überein (Kapitel 3, „Ausschüttungen und Nachschüsse").
- **Simulationsbeispiele Nr. 31/32:** Die Spanne ist als Veranschaulichung gekennzeichnet. Die Streuung ist stationär und in Prozent des Ausgangsniveaus gedeutet. Die Werte 5,7 / 11,6 / 18 % gelten genau unter dieser Deutung (Runde 3).
- **Barzuschuss Nr. 23/29:** Er wird brutto als originäre Zahlung gebucht, das Entgelt zählt zu den einbehaltenen Beträgen. Die Probe schließt dann mit Abweichung 0 (Runde 3, Gruppe A: 17.400 €). Ein Testfall ist ergänzt.
- **IWU-Toleranz:** Sie ist jetzt als beobachtete Höchstabweichung benannt, die nur eine Verschlechterung erkennt. Die Begründung trägt. Die schärfere Toleranz von 0,50 € für unmittelbar abgelesene Werte ist nicht übernommen. Das ist vertretbar und kein Befund.
- **Restwertregel A Nr. 3 und D.4:** In sich widerspruchsfrei. Sie stimmt mit Spezifikation Kapitel 3 („Restwert", fest) überein. „Soweit am Stichtag noch aussteht" und „soweit nicht als Maßnahme im Finanzplan" sind gleichwertig, weil der Finanzplan am Stichtag endet. Die Kontrollsumme fängt eine doppelt gezählte Maßnahme ab: Wird der Stau gezahlt und zusätzlich abgezogen, ergibt sich das Doppelte der geplanten Kosten. Eine doppelt abgezogene Restschuld fängt sie nicht ab (Befund 3).
- **Weitere Zahlen:** Gewerbesteuer 3,5 % · 280 % = 9,8 %, 3,5 % · 200 % = 7,0 %. Bei 15 Eingaben im Ankauf zuzüglich der Pauschalen sind „rund 20 Eingaben" plausibel. Zum kombinierten Stressfall nennt der Bericht keine Zahlen, nur die Regel (ermäßigte Höhen, nur wirksame Größen). Rechnerisch ist daran nichts zu beanstanden.

## Befunde aus Runde 3

| Nr. | Befund Runde 3 | Stand | Fundstelle |
|---|---|---|---|
| 1 | Saldierung nur periodengleich | eingearbeitet: Satz, Testfall und Entscheidungsauftrag an die Fachspezifikation; die Endwertdifferenz führt | A Nr. 13; A.6; Abschnitt 3 „Kennzahlen" |
| 2 | Nominal oder effektiv | eingearbeitet; die Festlegung je Zahlungsart trifft die Fachspezifikation | A Nr. 12 |
| 3 | Rundungsregel, letzter Spiegelstrich | eingearbeitet; die Operationsreihenfolge „Division zuletzt" trifft die Fachspezifikation (sie ist laut Spezifikation Kapitel 3 Eingang) | A Nr. 10 |
| 4 | Barzuschüsse in der Kontrollsumme | eingearbeitet; offen bleibt nur, ob das Zuschussentgelt gegen die erste Darlehensrate aufgerechnet wird und dann in die Kreditprobe Nr. 22 gehört (Fachspezifikation) | A Nr. 23, 29 |
| 5 | IWU-Toleranz | eingearbeitet (Begründung); der Cent der Variante Nachschuss ist genannt | A.6, Nr. 28 |
| 6 | Prozessdefinition der Simulation | eingearbeitet | A Nr. 32 |

## Befunde

**1. [wichtig · belegt] Abschnitt 5 „Was die Grobkalkulation rechnet" und D.5 „Risiko": Die Bankgrenze begrenzt das Darlehen, nicht den Preis. Der niedrigere Wert aus beiden Grenzen unterschätzt den tragbaren Preis, sobald die Bankgrenze bindet.**

Die Bankgrenze ist definiert als der Preis, bei dem „das Darlehen in Höhe der Beleihungsquote" die Mindestdeckung gerade einhält. Über 2,30 Mio. € gibt die Bank aber nicht null, sondern weiterhin 1,496 Mio. €. Der Käufer kann den Mehrpreis mit Eigenkapital schließen. Ob er das darf, entscheidet die Zielrendite, nicht die Bank.

Gegenrechnung im vereinfachten Modell (`b.py`):
- Annahmen: Miete aus D.4, 2 % Mietsteigerung, 4 % Zins, 2 % Tilgung, 30 % Steuer, 7 % Erwerbsnebenkosten, 80 % Gebäudeanteil, 2 % Abschreibung, Ausstieg zum Faktor 18 nach zehn Jahren, 3 % Verkaufskosten.
- Tragbarer Preis bei einer Zielrendite von 5 %:

| Rechenweise | Tragbarer Preis |
|---|---|
| Regel des Berichts: min(Renditegrenze 2,56 Mio., Bankgrenze 2,30 Mio.) | 2,30 Mio. € |
| Darlehen auf 1,496 Mio. € gedeckelt, Rest Eigenkapital; Zielrendite und Mindestdeckung beide eingehalten | 2,52 Mio. € |

- Die Regel des Berichts nennt also 220.000 € (8,7 %) zu wenig. Bei 6 % Ziel sind es 2,30 gegen 2,42 Mio. €. Erst bei 8 % Ziel bindet die Renditegrenze, und beide Wege ergeben 2,22 Mio. €.

Die Regel liegt immer auf der sicheren Seite. Das richtige Ergebnis liegt zwischen der Bankgrenze und der Renditegrenze. Für ein Werkzeug, dessen Hauptzweck in 1a die Höhe des Gebots ist, ist das aber eine falsche Zahl. Es fehlt außerdem die dritte, tatsächlich bindende Größe, das verfügbare Eigenkapital.

Verstoßener Maßstab: FAST/ICAEW, „keine verdeckten Annahmen". Die feste Eigenkapitalquote ist hier eine verdeckte Annahme.

Vorschlag:
- Die Renditegrenze mit dem Darlehen min(Beleihungsquote · P; Darlehen aus der Mindestdeckung) rechnen. Die Bankgrenze dann als Darlehenshöchstbetrag ausweisen.
- Als zweite Grenze optional das verfügbare Eigenkapital führen (Preis, bei dem der Eigenkapitalbedarf das Budget erreicht).
- Das Blatt nennt die bindende Grenze und den nötigen Eigenkapitaleinsatz.
- Spricht etwas fachlich für die feste Quote (Vorgabe des Hauses), diese Vorgabe ausdrücklich nennen und die Grenze so bezeichnen: „Preisgrenze bei fester Beleihungsquote".
- Beim Neubau mit Förderung zusätzlich festlegen, ob die Mindestdeckung den Schuldendienst des NBank-Darlehens einschließt und auf welches Darlehen sich die Quote bezieht. Bisher nennt D.4 nur „Fremdkapital zu Gesamtkosten".

**2. [Hinweis · belegt] Abschnitt 5 und D.1 „Zielwertsuche auf jede Zahleneingabe": Sie ist nicht für jede Eingabe eindeutig.**

Gegenrechnung im selben Modell (`c.py`): Preis 2,3 Mio. €, Zins 6 %, Faktor 18. Die Rendite steigt mit der Beleihungsquote bis 5,97 % bei 63 % und fällt danach, weil die Steuer- und Kontokorrentwirkung die Hebelwirkung umkehrt. Für eine Zielrendite von 5,7 % gibt es zwei Lösungen, 55,5 % und 75,5 % Beleihung. Über 5,97 % gibt es keine Lösung.

Ähnlich verhält es sich bei anderen Größen:
- Die Haltedauer ist ganzzahlig.
- Der Steuerstatus ist eine Auswahl, keine Zahl.
- Der kritische Anschlusszins (Abschnitt 3, Kennzahlenblatt) hat keinen Wert, wenn die Zinsbindung die Haltedauer deckt.
- Ab 1b-2 springt die Rendite an der Baukostenobergrenze der Sonderabschreibung.

Vorschlag: Die Zielwertsuche je Eingabe als zulässig kennzeichnen (stetig und monoton im Suchbereich). Sonst mit Suchintervall arbeiten und alle Lösungen oder „keine Lösung im Bereich" melden, wie beim internen Zinsfuß (A Nr. 20). Für kritische Werte ohne Lösung ein definiertes Ergebnis festlegen (Randfall, Spezifikation Kapitel 3 „Randfälle").

**3. [Hinweis · belegt] A Nr. 3, Kontrollsumme: Sie fängt eine doppelt gezählte Restschuld nicht ab, und ihr Preisstand ist offen.**

(a) Angenommen, der Erlös wird schon nach Schulden eingegeben, und die Restschuld wird zusätzlich abgelöst. Dann ist die Restschuld nach der Ablösung trotzdem null, und die Probe besteht.

Im Testfall:
- Die Restschuld beträgt 624.171,48 €.
- Der Endwert fällt auf −39.805,20 €.
- Die Kontrollsumme meldet nichts.

Auch die Bestandsprobe Nr. 23 meldet nichts, weil sie die gebuchte originäre Zahlung als richtig voraussetzt. Geschützt ist das Werkzeug hier nur durch die Bauart: Der Restwert entsteht ausschließlich aus Faktor, Nettoanfangsrendite oder Ertragswert und hat kein Schuldenfeld. Die Kontrollsumme schützt nicht. Dasselbe gilt für die anteilige Rückzahlung des NBank-Zuschusses bei Ablösung (`MA-017`, C.1). Sie ist kein Kredit und von der Probe nicht erfasst.

(b) „Gezahlt + abgezogen = geplante Kosten" setzt einen Preisstand voraus. Ein Beispiel: Ein Stau von 100.000 € zu heutigen Preisen ist für Jahr 12 geplant, der Verkauf findet in Jahr 10 statt, der Baupreisindex steigt um 3 %.
- Geplante Kosten: 142.576 €.
- Abzug zum Preisstand des Stichtags: 134.392 €.

Je nach Lesart schlägt die Probe an, oder sie erzwingt den höheren Abzug.

Vorschlag:
- In Nr. 3 festhalten, dass die Restschuld durch die Bauart geschützt ist (keine Eingabe des Erlöses nach Schulden).
- Eine Restwertprobe ergänzen: Restwert = Bruttopreis aus dem Maßstab − Verkaufskosten − Σ ausstehender Stau.
- Rückzahlungspflichten aus Förderung in die Regel „Zahlung im Finanzplan, nie Abzug" aufnehmen.
- Den Preisstand des Abzugs festlegen (Stand am Stichtag) und die Probe darauf beziehen.

**4. [Hinweis · belegt] B.6 `MA-021`: „rund ein Sechstel der Förderung" gilt nur ohne Kappung und nur für den Baukostenanteil.**

19/119 = 16,0 % der Bruttokosten. Das trifft auf die Kostengruppen 200 bis 700 unterhalb der Bemessungsgrenze zu, nicht auf das Grundstück, das keine Vorsteuer trägt.

Liegen die Kosten über der Grenze, ist die Wirkung kleiner. Ein Beispiel mit 5.800 €/m² brutto und einer Grenze von 5.250 €/m²:
- Netto ergeben sich 4.874 €/m².
- Die Förderung sinkt um (5.250 − 4.874) / 5.250 = 7,2 %, nicht um 16 %.

Die Begründung der Ausnahme von der Vorsichtsregel bleibt richtig, die Größe ist zu pauschal.

Vorschlag: „bis zu rund einem Sechstel der Förderung auf die Baukosten, weniger, wenn die Bemessungsgrenze kappt".

**5. [Hinweis · begründete Einschätzung] Abschnitt 1 „Auftrag der Vorstudie": „Würden alle Wege gleich verteuert, bliebe ihr Abstand erhalten" gilt nur bei gleichem Eurobetrag, nicht bei gleichem Prozentsatz.**

Die bisherige Regel lautete „Aufwand +50 %, Nutzen −50 % für alle". Damit ändert sich der Abstand zweier Wege um 0,5 · Nutzenunterschied + 0,5 · Kostenunterschied.

Ein Beispiel: Eigenbau mit Kosten 600 und Nutzen 1.000, Kauf mit Kosten 400 und Nutzen 800. Im Basisfall liegen beide gleich (+400). Im alten ungünstigen Fall stehen −400 gegen −200. Die Neufassung je Weg (E.1) ist trotzdem die bessere Regel, nur die Begründung stimmt so nicht.

Vorschlag: „Würden alle Wege um denselben Betrag verteuert, bliebe ihr Abstand erhalten …", oder die Begründung auf „trifft die Unsicherheit dort, wo sie liegt" stützen.

## Nicht geprüft

- **Änderungen ohne Rechenbezug:** Rechtsinhalte in B.1 bis B.4 und C.1 (Fristen, Zinslauf nach § 233a AO, Kaufmannseigenschaft, Bindungsende) sowie Zuschnitt und Reihenfolge der Teilschritte gehören zu anderen Rollen.
- **Kombinierter Stressfall, kritischer Ausstiegsfaktor, Finanzierungslücke:** Der Bericht nennt keine Zahlen, nur Regeln. Rechnerisch geprüft sind nur Eindeutigkeit und Existenz (Befund 2).
- **Unveränderte Zahlen aus Runde 3:** Sie wurden nicht erneut gerechnet, außer dort, wo die Änderung von ihnen abhängt (Testfall, Variante Nachschuss).
- **Grobkalkulationsmodell:** Es ist eine eigene Vereinfachung, nicht die Spezifikation von 1a. Die Befunde 1 und 2 hängen in ihrer Richtung nicht an den gewählten Parametern, in der Höhe schon.
