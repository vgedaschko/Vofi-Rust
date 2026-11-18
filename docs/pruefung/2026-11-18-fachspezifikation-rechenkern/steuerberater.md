Rolle: Steuerberater (Immobilienmandanten aller Rechtsformen)
Prüfobjekt: `docs/fachspezifikation-rechenkern.md`, Stand 2026-11-18. Ganz gelesen: Kapitel 7. Dazu, soweit sie Steuern berühren: Kapitel 2 (R-2.5, R-2.7, R-2.8, NF-04), 3 (E-40 bis E-44, H-22, KAT-03 bis KAT-07), 6 (R-6.10, NF-15), 8, 9 (R-9.5), 10 (R-10.4, R-10.11, NF-28), 11 (R-11.14), 14 (M-36), 15 (RF-10, RF-13), 16 und 17. Gegengelesen: `steuer.py` des Referenzrechners, `MA-010`, `MA-016`, `MA-022`, `MA-023`, `MA-029`, Kataster zu den Steuerkennungen, Bericht Anhang B.5 und D.4.

Gesamturteil: Mit Auflagen tragfähig. Der Aufbau stimmt je Steuerstatus: Steuerart, Bemessung, Reihenfolge der Schritte, KSt-Staffel, Abrundung vor Freibetrag, § 35 EStG mit allen drei Begrenzungen und dem Anteil natürlicher Personen, getrennte Verlustvorträge, zwei Töpfe bei der Privatperson, Zehnjahresfrist. Alle Beispielzahlen in R-7.7 bis R-7.10 habe ich nachgerechnet; sie stimmen. Drei Stellen sind aber nicht vorsichtig, obwohl der Gesetzestext die vorsichtige Lösung schon trägt: die Reichweite der erweiterten Kürzung (NF-20), das Kennzeichen der Kürzung beim Einzelunternehmen und die 15-%-Regel. Dazu kommen zwei unvollständig gefasste Modellannahmen, nämlich Zuschüsse und Finanzierungskosten.

Note: **7 von 10.** Zur 9 fehlen:
- Befunde 1 bis 3: drei Korrekturen, die sich am Gesetzeswortlaut entscheiden lassen. Alle sind im Dokument behebbar, ohne den Steuerberater des Auftraggebers.
- Befunde 4 bis 7: vier Regeln enger fassen; das Dokument kann sie selbst entscheiden.
- Befund 10: der Kurzform-Hinweis als Meldung mit festem Inhalt.

Nur der Steuerberater des Auftraggebers kann bestätigen:
- ob die erweiterte Kürzung den Gewinn aus dem Verkauf des Grundbesitzes erfasst;
- wie der NBank-Zuschuss einzuordnen ist (Investitionszuschuss oder Gegenleistung für die Bindung);
- ob die Vorfälligkeitsentschädigung der Privatperson abziehbar ist;
- ob der Objektverkauf einer GmbH & Co. KG laufender Gewinn oder Aufgabegewinn ist (§ 7 Satz 2 GewStG);
- was der Verkauf in einer befreiten Vermietungsgenossenschaft auslöst.

Diese Punkte bleiben Modellannahmen mit vorsichtiger Voreinstellung. Erreicht das Dokument die vorsichtige Voreinstellung und die Befunde 1 bis 10, ist eine 9 erreichbar, auch bevor der Steuerberater antwortet.

## Befunde

1. **[kritisch · belegt (Zinsen) / begründete Einschätzung (Verkaufsgewinn)]**
   - **Fundstelle:** R-7.8 (NF-20), R-9.5, R-7.14, Kapitel 17 erste neue Modellannahme.
   - **Problem:** Das Kennzeichen „erweiterte Kürzung" stellt den ganzen Gewerbeertrag frei, Habenzinsen und Verkaufsgewinn eingeschlossen. Das ist ausdrücklich eine Ausnahme von der Vorsichtsregel (Spezifikation Kapitel 8, fest). Als Begründung steht nur „Wortlaut des Berichts". Das ist keine Aussage über die Rechtslage und trägt die Ausnahme nicht.
   - **Beleg Zinsen:** § 9 Nr. 1 Satz 2 GewStG (gelesen 2026-11-18) kürzt nur „um den Teil des Gewerbeertrags, der auf die Verwaltung und Nutzung des eigenen Grundbesitzes entfällt". Daneben eigenes Kapitalvermögen zu verwalten, ist nur unschädlich, wird aber nicht gekürzt. Zinsen aus der Geldanlage bleiben deshalb nach dem Wortlaut gewerbesteuerpflichtig. Das ist keine offene Frage, sondern eine Rechenregel.
   - **Beleg Verkaufsgewinn:** Hier ist die Lage nicht eindeutig. Dafür spricht, dass der Verkauf zur Nutzung des Grundbesitzes gehören kann. Dagegen spricht:
     - Der Wortlaut verlangt, dass das Unternehmen im Erhebungszeitraum „ausschließlich" Grundbesitz verwaltet. Wer zum Verkaufsstichtag N seinen einzigen Grundbesitz veräußert, hält danach keinen mehr; nach der mir bekannten, hier nicht am Original gelesenen Rechtsprechung kann das die Kürzung im Verkaufsjahr gefährden.
     - Satz 5 Nr. 2 sperrt die Kürzung, soweit stille Reserven aus Grundbesitz aufgedeckt werden, der binnen drei Jahren unter dem Teilwert eingebracht wurde.
     - Satz 6 schließt sie für Veräußerungsgewinne nach § 7 Satz 2 Nr. 2 und 3 aus.
   - **Wirkung:** im Ankauf RF-11 155.680 € Gewerbesteuer. Sie schlägt unmittelbar auf den höchsten tragbaren Preis (R-11.4) durch.
   - **Vorschlag:**
     - (a) Habenzinsen werden unter der Kürzung immer der Gewerbesteuer unterworfen, als Regel und nicht als Annahme; in der Unterlassensalternative (R-9.5) ebenso. Sie verwaltet nur Kapital und hätte keinen Anspruch auf die Kürzung. Die heutige Lesart rechnet sie zwar „günstiger", aber gegen das Gesetz.
     - (b) Für den Verkaufsgewinn die Modellannahme mit vorsichtiger Voreinstellung führen: Verkaufsgewinn gewerbesteuerpflichtig, umschaltbar, Gewicht hoch, Klärung durch den Steuerberater.
     - (c) R-7.14 entsprechend anpassen: Bei gesetzter Kürzung gilt g = 0 nur für s_op, nicht für s_Z.

2. **[wichtig · belegt am Wortlaut, Ergänzung begründete Einschätzung]**
   - **Fundstelle:** E-41 („nur Status mit Gewerbesteuer"), R-7.9, RF-13 („Personengesellschaft … mit Kürzung"). Dazu Spezifikation Kapitel 2, Zeile „Grobkalkulation" (fest): Das Kennzeichen gelte „für jeden Steuerstatus mit Gewerbesteuer: … gewerbliche Personengesellschaften und Einzelunternehmen".
   - **Problem:** Die erweiterte Kürzung steht nur Unternehmen zu, die „ausschließlich eigenen Grundbesitz … verwalten und nutzen" (§ 9 Nr. 1 Satz 2 GewStG). Damit scheiden aus:
     - die originär gewerbliche Personengesellschaft, deren Gewerbebetrieb gerade aus einer anderen Tätigkeit folgt (§ 15 Abs. 3 Nr. 1 EStG, gelesen: die gewerbliche Tätigkeit macht die ganze Tätigkeit zum Gewerbebetrieb);
     - das Einzelunternehmen, bei dem die Immobilie im Betriebsvermögen eines laufenden Gewerbes liegt.

     Ein Einzelunternehmer, der nur eigenen Grundbesitz verwaltet, ist nach allgemeiner Abgrenzung gar nicht gewerblich, sondern erzielt Einkünfte aus Vermietung. Gewerblich geprägt kann nur eine Personengesellschaft sein. Für das Einzelunternehmen gibt es damit praktisch keinen Fall, in dem das Kennzeichen zutrifft.
   - **Szenario:** Ein Bearbeiter setzt für einen Handwerksunternehmer mit Mietshaus im Betriebsvermögen das Kennzeichen. Die Gewerbesteuer entfällt, und der tragbare Preis steigt bei Hebesatz über 400 % zu Unrecht.
   - **Vorschlag:**
     - Steuerstatus der Personengesellschaft teilen in „gewerblich geprägt (`ESTG-15` Abs. 3 Nr. 2)" mit Kennzeichen und „originär gewerblich" ohne Kennzeichen.
     - Beim Einzelunternehmen E-41 sperren.
     - Spezifikation Kapitel 2 vorher ändern und in `docs/entscheidungen.md` begründen. Die Begründung im Bericht D.4 („damit 1a und 1b denselben Fall gleich rechnen") gilt dann nur für die geprägte Gesellschaft.

3. **[wichtig · belegt]**
   - **Fundstelle:** R-6.10 (NF-15), E-52 (Voreinstellung „Erhaltung"), M-36.
   - **Problem:** Die Kurzform zieht Erhaltung im Jahr der Zahlung ab und gibt über der 15-%-Grenze nur einen Hinweis. Die Regel ist eindeutig und mit den vorhandenen Eingaben rechenbar. Nach § 6 Abs. 1 Nr. 1a EStG (gelesen) sind Instandsetzungs- und Modernisierungsaufwendungen binnen drei Jahren nach der Anschaffung Herstellungskosten, wenn sie ohne Umsatzsteuer 15 % der Anschaffungskosten des Gebäudes übersteigen. Für Vermietungseinkünfte gilt das über § 9 Abs. 5 Satz 2 EStG (nicht gesondert gelesen). Die Voreinstellung ist also die günstige Lesart, und ein Ergebnis über der Grenze ist schlicht falsch. M-36 ist zudem in sich widersprüchlich: „in der Kurzform nicht geprüft", aber durch die Prüfung ausgelöst.
   - **Szenario:** RF-11 mit 320.000 € Erhaltung im Jahr 2. Grenze 15 % × 1.980.000 = 297.000 €. Die Kurzform zieht 320.000 € sofort ab statt sie über 50 Jahre mit 2 % abzuschreiben.
   - **Vorschlag:** In der Kurzform automatisch aktivieren, wenn k ≤ 3 und Summe(E-50 je Maßnahme mit k ≤ 3) / (1 + USt-Satz aus dem Katalog) > 15 % × Abschreibungsgrundlage des Gebäudes vor Zuschüssen. Die Beträge sind brutto; die Grenze ist netto gemessen. M-36 wird dann zur Meldung „als anschaffungsnahe Herstellungskosten behandelt". Laufende Instandhaltung (R-6.8) zählt nach Satz 2 nicht mit; das ist bereits so getrennt.

4. **[wichtig · belegt]**
   - **Fundstelle:** R-7.1, letzter Absatz („ohne Hinzurechnungen"), R-7.8, NF-19.
   - **Problem:** Die Auslassung ist benannt, aber weder ihre Richtung noch ihre Schwelle. Der Bericht (D.4) begründete sie noch mit „wirkt erst, wenn die Hinzurechnungsposten zusammen 200.000 Euro übersteigen"; diese Begründung ist im Dokument verloren gegangen. Nach § 8 Nr. 1 GewStG (gelesen) wird ein Viertel der Summe aus Entgelten für Schulden und der Hälfte der Pacht für Grundbesitz hinzugerechnet, „soweit die Summe den Betrag von 200 000 Euro übersteigt". Der Erbbauzins (R-6.11) gehört nach der Kataster-Notiz zu `GEWSTG-8` dazu.
   - **Szenario:** Eine kommunale Wohnungs-GmbH ohne Kürzung mit großem Bestand hat den Freibetrag schon verbraucht. Dieselbe Logik legt NF-19 für den Freibetrag der Gewerbesteuer zugrunde. Dann kostet jeder Euro Zins 25 % × 3,5 % × Hebesatz, bei 400 % also 3,5 %. RF-11 mit rund 57.000 € Zins im Jahr 1 gibt rund 2.000 € Gewerbesteuer im Jahr. Die Kurzform rechnet das Vorhaben also günstiger; die Hinzurechnung fehlt gegen die Vorsichtsregel.
   - **Vorschlag:** Die eine Zeile in die Kurzform aufnehmen: Hinzurechnung = 25 % × max(0; Zinsen + Beiträge + Entgelte + ½ Erbbauzins − Freibetrag (KAT-04)). Im Modus „sofort" gilt der Freibetrag als verbraucht, wie in NF-19. Dann fällt „Hinzurechnungen" aus der Liste der Auslassungen in R-7.1 und Kapitel 16.

5. **[wichtig · belegt (Disagio, Bilanzierung) / begründete Einschätzung (Vorfälligkeit)]**
   - **Fundstelle:** R-7.2 (NF-16), dritte neue Modellannahme in Kapitel 17.
   - **Problem:** Die vorgeschlagene Annahme fasst Fragen zusammen, die das Gesetz zum Teil schon entscheidet:
     - **Privatperson, Disagio:** marktübliches Disagio im Jahr der Zahlung abziehbar (§ 11 Abs. 2 Satz 4 EStG, gelesen). Bauzeitzinsen sind vorweggenommene Werbungskosten. NF-16 stimmt hier.
     - **Betriebsvermögen, Disagio:** § 11 lässt die Gewinnermittlung unberührt (Abs. 2 Satz 6). Ein Disagio ist dort aktiver Rechnungsabgrenzungsposten (§ 5 Abs. 5 Satz 1 Nr. 1 EStG, gelesen) und über die Zinsbindung zu verteilen. Laufzeitbezogene Entgelte ebenso. NF-16 ist hier nicht vorsichtig.
     - **Privatperson, Vorfälligkeitsentschädigung beim Verkauf:** nach mir bekannter BFH-Rechtsprechung (nicht am Original gelesen) keine Werbungskosten bei Vermietung, sondern Veräußerungskosten. Bei Verkauf nach Ablauf der Frist sind sie gar nicht abziehbar. Das Dokument zieht sie in e_op mit E-42 ab, also zu günstig, wenn n > Frist und die Zinsbindung über die Haltedauer reicht.
   - **Vorschlag:**
     - Für die Status mit Betriebsvermögen Disagio und laufzeitbezogene Entgelte linear über die Zinsbindung verteilen. Das ist eine Regel, keine Annahme.
     - Bei der Privatperson die Vorfälligkeit in den Verkaufstopf von R-7.11 legen: abziehbar nur, wenn der Verkauf steuerpflichtig ist.
     - Die Modellannahme auf das Offene beschränken: ob NBank-Entgelte laufzeitbezogen oder einmalig sind, die Marktüblichkeit des Disagios und die Vorfälligkeit der Privatperson. Gewicht gering bis mittel, wie vorgeschlagen.

6. **[wichtig · begründete Einschätzung]**
   - **Fundstelle:** R-7.3 (NF-17), R-11.14 (NF-38), zweite neue Modellannahme in Kapitel 17.
   - **Problem 1, andere Lesart:** Als andere Lesart steht nur „sofort steuerpflichtiger Ertrag". Die praktisch wichtige zweite Lesart fehlt: Ein Zuschuss, der Gegenleistung für Miet- und Belegungsbindung ist, ist Einnahme aus der Nutzungsüberlassung. Bei der Privatperson ist er nach § 11 Abs. 1 Satz 3 EStG (gelesen) auf die Bindungsdauer verteilbar, im Betriebsvermögen über einen passiven Rechnungsabgrenzungsposten (§ 5 Abs. 5 Satz 1 Nr. 2 EStG, gelesen). Die Einkommensteuer-Richtlinien unterscheiden nach meiner Kenntnis genau so; sie stehen nicht auf gesetze-im-internet.de und sind nicht gelesen. Ein Indiz für die Gegenleistung liefert das Dokument selbst: die zeitanteilige Rückzahlung bei vorzeitigem Verkauf (R-8.7, `MA-017`).
   - **Problem 2, Vorsicht und Gewicht:** Die Voreinstellung ist die günstigere Lesart, ist aber nicht als Ausnahme von der Vorsichtsregel gekennzeichnet. Gewicht mittel ist zu niedrig. In RF-12 geht es um 1.708.000 €; als Ertrag im Zuflussjahr wären das bei rund 30 % gut 500.000 € Steuer.
   - **Problem 3, Zuordnung:** Der Zuschuss bemisst sich auch auf die Grundstückskosten. In RF-12 sind 1,0 von 8,54 Mio. € zuwendungsfähiger Kosten Boden. Er mindert nach R-7.3 aber vollständig die Abschreibungsgrundlage des Gebäudes. Richtig wäre die Aufteilung im Verhältnis der zuwendungsfähigen Kosten; der Bodenanteil mindert die Anschaffungskosten des Bodens. Die heutige Rechnung ist vorsichtig, aber falsch zugeordnet; die Summe im Restbuchwert bleibt gleich.
   - **Vorschlag:** Die Annahme mit drei Lesarten führen: Minderung der Herstellungskosten, Einnahme über die Bindung verteilt, Einnahme sofort. Die Ausnahme von der Vorsicht begründen: Bei einem Investitionszuschuss im Betriebsvermögen ist die Minderung als Wahlrecht üblich. Gewicht hoch, Klärung durch den Steuerberater am Bewilligungsbescheid. Den Zuschuss nach Kostenanteilen auf Gebäude und Boden verteilen.

7. **[wichtig · begründete Einschätzung, § 10a belegt]**
   - **Fundstelle:** R-7.6 (NF-19), `MA-016`.
   - **Problem:** „Sofort" heißt im Dokument: Die Steuer ist linear im Ergebnis, ein Verlust bringt im selben Jahr eine Erstattung zum Grenzsatz. Steuerlich setzt das voraus, dass der Investor im selben Jahr genug positive Einkünfte derselben Steuerart hat, gegen die der Verlust läuft. Bei Einkommen- und Körperschaftsteuer ist das als Annahme über die übrige Lage vertretbar und in R-7.6 erkennbar benannt. Bei der Gewerbesteuer ist es für die Personengesellschaft falsch. Die Gewerbesteuer ist eine Objektsteuer je Betrieb. Der Fehlbetrag bleibt bei der Mitunternehmerschaft und wird nur mit deren künftigen Gewerbeerträgen verrechnet (§ 10a Satz 1, 4 und 5 GewStG, gelesen). Er mindert keine Gewerbesteuer der Gesellschafter.
   - **Szenario:** Die Objekt-GmbH & Co. KG hat kein anderes Geschäft. Mit „sofort" erhält sie eine Gewerbesteuer-„Erstattung", die es nicht gibt. Für Kommanditisten begrenzt zudem § 15a EStG die sofortige Verrechnung, soweit ein negatives Kapitalkonto entsteht (nicht gelesen, ungeprüft).
   - **Vorschlag:** Im Modus „sofort" bei der Personengesellschaft die Gewerbesteuer weiter mit Vortrag rechnen; nur Einkommensteuer und Anrechnung laufen linear. Bei Körperschaft und Einzelunternehmen im Text von `MA-016` ausdrücklich sagen: Die Lesart unterstellt weitere Gewinne in derselben Körperschaft beziehungsweise demselben Betrieb, oder eine Organschaft. Einen Hinweis zu § 15a in das Kataster aufnehmen (Grundform).

8. **[wichtig · begründete Einschätzung, Wortlaut belegt]**
   - **Fundstelle:** R-7.1 (befreite Körperschaft `KSTG-5`), R-7.12.
   - **Problem 1, Verkaufsjahr:** Nach § 5 Abs. 1 Nr. 10 Satz 2 KStG (gelesen) ist die Befreiung der Vermietungsgenossenschaft ausgeschlossen, wenn die Einnahmen aus nicht begünstigten Tätigkeiten 10 % der gesamten Einnahmen übersteigen. Begünstigt ist nur die Überlassung an Mitglieder. Der Verkaufserlös des Objekts (RF-11: 3,3 Mio. € gegen 0,13 Mio. € Jahresmiete) ist nach meiner Einschätzung keine begünstigte Einnahme. Die Kurzform rechnet ausgerechnet das Verkaufsjahr steuerfrei, in dem die Klippe am sichersten greift. Die Folgen hängen an § 13 KStG und § 3 Nr. 15 GewStG, beide nicht ausgewertet.
   - **Problem 2, fehlender Status:** Für steuerpflichtige Körperschaften ohne Gewerbebetrieb fehlt ein Status. Verein und Stiftung sind nach § 2 Abs. 3 GewStG (gelesen) nur mit wirtschaftlichem Geschäftsbetrieb gewerbesteuerpflichtig; Vermietung ist Vermögensverwaltung. Sie liefen heute unter „voll steuerpflichtige Körperschaft" mit Gewerbesteuer. Das ist vorsichtig, aber der Verkaufsgewinn wäre bei ihnen nur innerhalb der Frist steuerpflichtig.
   - **Vorschlag:**
     - R-7.12 um eine Meldung ergänzen: „Verkauf in befreiter Genossenschaft: Befreiung im Verkaufsjahr vom Steuerberater zu prüfen". Das ist dieselbe Gewichtsklasse wie `MA-017` und kein stilles Steuerfrei.
     - In Kapitel 16 den Status „Körperschaft ohne Gewerbesteuer (Verein, Stiftung)" für die Grundform vormerken.

9. **[Hinweis · belegt]**
   - **Fundstelle:** R-7.11, R-7.5.
   - **Problem:** Bei der Privatperson wird der steuerpflichtige Verkaufsgewinn ohne Verlustvortrag und ohne den Vermietungsverlust desselben Jahres besteuert; der Vortrag „verfällt". § 23 Abs. 3 Satz 7 EStG (gelesen) beschränkt aber nur Verluste aus privaten Veräußerungsgeschäften. Der Vortrag aus Vermietung mindert nach § 10d Abs. 2 EStG (gelesen) den Gesamtbetrag der Einkünfte, zu dem der Gewinn nach § 23 gehört. Die Rechnung ist damit zu vorsichtig und widerspricht der Fiktion „Vortrag im Vorhaben". Der Betrag ist meist klein.
   - **Vorschlag:** Im Verkaufsjahr gilt g_v + e_op als Bemessung des Vermietungstopfs, wenn der Verkauf steuerpflichtig ist. Einen Satz in R-7.11 ergänzen: Die Frist läuft nach den Vertragsdaten, nicht nach dem Übergang von Nutzen und Lasten. Die Rechnung mit ganzen Jahren (n ≤ Frist heißt pflichtig) ist dafür vorsichtig genug; der Anwender braucht den Hinweis für die Verkaufsplanung.

10. **[wichtig · belegt am Dokument]**
    - **Fundstelle:** R-7.1, letzter Satz („Das Ergebnis führt den Hinweis …"), Meldungsliste R-14.13, Kapitel 17 „Quellenkataster".
    - **Problem 1, Meldung:** Der Kurzform-Hinweis hat keine Kennung und keinen Wortlaut. Es bleibt offen, was der Bearbeiter erfährt. Spezifikation Kapitel 7 verlangt die Abgrenzung zur Steuerberatung; die Sichtbarkeitsregel in Kapitel 8 verlangt einen Satz am einen Ort. Ohne festen Text wird der Hinweis entweder Hinweisflut oder fehlt.
    - **Problem 2, Kataster:** Die Lücke „Satz auf Zinserträge" ist richtig erkannt. Es fehlen weitere Einträge für Normen, auf denen die Kurzform tatsächlich ruht.
    - **Vorschlag:** Eine Meldung M-37 „Steuer in Kurzform" mit festem Text, einmal im Annahmenblatt, etwa so:

      > „Die Steuer ist vereinfacht gerechnet: ohne Mindestbesteuerung, Zinsschranke, Sonderabschreibung und Reinvestitionsrücklage; das Kennzeichen der erweiterten Kürzung ist ungeprüft übernommen. Sie ersetzt keine steuerliche Prüfung des Einzelfalls."

      Die Liste kürzt sich, sobald die Befunde 1, 3 und 4 umgesetzt sind. Die Unschädlichkeitsgrenzen nach § 9 Nr. 1 Satz 3 und 5 GewStG (Strom, Mieterleistungen, Betriebsaufspaltung) prüft der Anwender selbst; das gehört in den Satz zum Kennzeichen. Dazu diese Normen ins Kataster aufnehmen, jeweils am 2026-11-18 gelesen:

      | Kennung | Inhalt |
      |---|---|
      | `ESTG-32D` | 25 % Abgeltungsteuer, Kirchensteuerformel |
      | `ESTG-20` | Abs. 9: Sparer-Pauschbetrag 1.000/2.000 €, Abzug tatsächlicher Werbungskosten ausgeschlossen; Abs. 8: Subsidiarität |
      | `ESTG-11` | Disagio, Verteilung von Einnahmen |
      | `ESTG-5` | Abs. 5: Rechnungsabgrenzung |
      | `ESTG-51A` | Abs. 2 Satz 3: § 35 gilt nicht für die Bemessung der Kirchensteuer |
      | `GEWSTG-2` | Abs. 2 und 3 |
      | `GEWSTG-3` | Nr. 15 |

      Aus § 20 Abs. 9 folgen zwei Konsequenzen:
      - Bei der Privatperson sind Kontokorrentzinsen der Unterlassensalternative nicht abziehbar; R-9.5 behandelt sie heute als operativen Aufwand.
      - Der Pauschbetrag ist in der Kurzform nicht angesetzt. Das ist in Ordnung, weil es beide Seiten gleich trifft, sollte aber als Satz in R-7.10 stehen.

## Ohne Befund geprüft (bestätigt)

- R-7.7: KSt-Staffel nach `KSTG-23` (gelesen: 15 % bis 2027, 14/13/12/11 %, ab 2032 10 %). RF-10 stimmt: 29.825 € (2027) und 24.550 € (2032). Das Folgejahr des Verlustbeispiels ist 2028: 30.049 × 14,77 % = 4.438,24 €, Gewerbesteuer 30.000 × 14 % = 4.200 €.
- R-7.8: Abrundung vor Freibetrag, Freibetrag 24.500 € nur für natürliche Personen und Personengesellschaften (§ 11 Abs. 1 Satz 3 GewStG, gelesen), Messzahl 3,5 %. Getrennter gewerbesteuerlicher Vortrag, gekürzt vor Abrundung und Freibetrag (`steuer.py`, Zeilen 123 und 139). Das stimmt mit § 10a Satz 1 überein.
- R-7.9: Alle fünf Zeilen der Tabelle nachgerechnet und richtig. Die drei Begrenzungen entsprechen § 35 Abs. 1 Satz 1, 2 und 5 und Abs. 2 Satz 2 EStG (gelesen). Kein Vortrag ist richtig. Den Ermäßigungshöchstbetrag mit der Einkommensteuer auf den Gewinn des Vorhabens zu nähern, ist für die Kurzform vertretbar; die Abhängigkeit von den übrigen Einkünften gehört als Modellannahme mit Gewicht gering in die Grundform. Kleinigkeit ohne Befundrang: E-42 schließt Zuschlagsteuern ein, die Anrechnung mindert aber nur die Einkommensteuer, und für die Kirchensteuer gilt § 35 nicht (§ 51a Abs. 2 Satz 3 EStG). In der Grundform trennen.
- `ESTG-4-5B`: Die Gewerbesteuer ist keine Betriebsausgabe; richtig umgesetzt.
- R-7.10: Zwei Töpfe sind richtig. Vermietungsverluste mindern abgeltend besteuerte Kapitalerträge nicht. Das Beispiel stimmt (12.863,75 € und 131,88 €).
- R-7.11: Frist „nicht mehr als zehn Jahre" nach § 23 Abs. 1 Satz 1 Nr. 1 EStG (gelesen); bei n = 10 pflichtig, bei n = 11 frei, also vorsichtig. Der Buchwert nach Abschreibungen entspricht § 23 Abs. 3 Satz 4. Ein negativer Verkaufsgewinn bleibt unberücksichtigt; das ist nach Satz 7 vorsichtig und vertretbar.
- R-7.3: Linear mit dem Satz nach Fertigstellung (§ 7 Abs. 4 Satz 1 Nr. 2 EStG, gelesen: 3 % nach dem 31.12.2022). Bemessung aus der Kaufpreisaufteilung einschließlich anteiliger Nebenkosten, Erwerb ab Übergang von Nutzen und Lasten. Randbemerkung: Nach § 7 Abs. 1 Satz 4 zählt der Monat der Fertigstellung voll. RF-12 rechnet erst ab dem Monat nach der Bauzeit (6 statt 7 Monate im Planjahr 2). Das ist vorsichtig und klein; in Teil 2 mit dem echten Fertigstellungsmonat regeln.
- R-7.5 und `MA-016`: Vortrag als Voreinstellung ist die vorsichtige Lesart. Den unbeschränkten Vortrag ohne Mindestbesteuerung (`ESTG-10D` gelesen: Sockel 1 Mio. €, darüber 70 %; `GEWSTG-10A` gelesen: 60 %) halte ich für die Kurzform mit linearer Abschreibung für vertretbar. Vorträge über 1 Mio. € entstehen hier kaum. Bitte die Richtung (günstiger) in R-7.1 nennen. Der Kern sollte einen Hinweis zurückgeben, wenn im Verkaufsjahr ein Vortrag gegen einen Gewinn über 1 Mio. € verrechnet wird; in RF-11 liegt der Verkaufsgewinn bei 1,11 Mio. €.
- R-7.4 und Gewerbesteuer auf den Verkaufsgewinn bei der Personengesellschaft: Die Kurzform behandelt den Objektverkauf als laufenden, gewerbesteuerpflichtigen Gewinn mit Anrechnung. Nach § 7 Satz 2 GewStG (gelesen) wäre ein Aufgabegewinn beim Anteil natürlicher Personen frei. Bis 400 % Hebesatz ist das neutral, darüber vorsichtig. Das ist vertretbar, sollte aber wegen der Kataster-Notiz zu `GEWSTG-7` als Modellannahme mit Gewicht mittel geführt werden („Objektverkauf ist laufender Gewinn"; andere Lesart: Betriebsaufgabe).
- NF-04 und R-2.8: Planjahr als Steuerjahr, Satz des Kalenderjahres, in dem das Planjahr beginnt. Bei sinkender KSt ist das vorsichtig; Zahlung am Ende des Planjahres entspricht dem Lehrbuch. Vertretbar.
- R-9.5: Gleicher Steuerstatus und eigener Vortrag für die Alternative sind richtig. Zur Kürzung siehe Befund 1, zur Privatperson Befund 10.
- R-10.11 und NF-28: Die Entlastung der Sollzinsen mit s_op ist innerhalb der Kurzform folgerichtig. Ohne Hinzurechnung ist s_op für Zinsen leicht zu hoch; mit Befund 4 wird es s_op − 25 % × g, sobald der Hinzurechnungsfreibetrag überschritten ist. Kein eigener Befund, weil die Kennzahl erst ab der Vollkalkulation erscheint.
- Was die Kurzform schweigend voraussetzt und vertretbar ausklammert: Verkauf als Asset Deal (kein § 8c KStG); keine Reinvestitionsrücklage nach § 6b EStG (vorsichtig); umsatzsteuerfreie Wohnraumvermietung mit Bruttokosten (für Gewerbe und Mixed-Use nicht tragfähig; UStG nicht gelesen); kein gewerblicher Grundstückshandel bei der Privatperson (Rechtsprechung, Kataster `ESTG-23`). Den gewerblichen Grundstückshandel und die Umsatzsteuer sollte die Meldung aus Befund 10 nicht aufzählen. Sie gehören an die Eingabe des Steuerstatus und der Nutzungsart.

## Am Original gelesene Normen

Alle am 2026-11-18 von gesetze-im-internet.de abgerufen (`curl`, ISO-8859-1), in der dort veröffentlichten Fassung. Die Standangabe der Seiten habe ich nicht gesondert ausgewertet; die Fassungsdaten des Katasters (EStG 15.10.2026, GewStG 29.06.2026, KStG 04.02.2026) habe ich nicht widerlegt.

| Kennung | Norm | Gelesen |
|---|---|---|
| `GEWSTG-9` | § 9 GewStG | Nr. 1 Satz 1 bis 6 |
| `GEWSTG-7` | § 7 GewStG | Satz 1 bis 4 |
| `GEWSTG-8` | § 8 GewStG | Nr. 1 mit Freibetrag 200.000 € |
| `GEWSTG-10A` | § 10a GewStG | Satz 1 bis 5 |
| `GEWSTG-11` | § 11 GewStG | Abs. 1 und 2 |
| neu | § 2 GewStG | Abs. 2 und 3 |
| neu | § 3 GewStG | Nr. 15 aufgerufen, ohne Fundtext ausgewertet |
| `ESTG-35` | § 35 EStG | Abs. 1 und Abs. 2 Satz 1 und 2 |
| `ESTG-23` | § 23 EStG | ganz |
| `ESTG-7` | § 7 EStG | Abs. 1 Satz 4, Abs. 4 Satz 1, Abs. 5a Satz 1 |
| `ESTG-6` | § 6 EStG | Abs. 1 Nr. 1a |
| `ESTG-10D` | § 10d EStG | Abs. 2 |
| `ESTG-15` | § 15 EStG | Abs. 3 Nr. 1 |
| neu | § 32d EStG | Abs. 1 |
| neu | § 20 EStG | Abs. 8 und 9 |
| neu | § 11 EStG | ganz |
| neu | § 5 EStG | Abs. 5 |
| neu | § 51a EStG | Abs. 2 Satz 3 |
| `KSTG-23` | § 23 KStG | ganz |
| `KSTG-5` | § 5 KStG | Abs. 1 Nr. 9 Satz 1 und 2, Nr. 10 Satz 1 bis 7 |

Weitere Feststellungen:
- `ESTG-4-5B`, `ESTG-9` und `KSTG-8` habe ich nur abgerufen, nicht inhaltlich ausgewertet.
- Abweichung zum Kataster, zur Nachprüfung: Die veröffentlichte Fassung von § 9 Nr. 1 Satz 1 GewStG lautet jetzt „die im Erhebungszeitraum als Betriebsausgabe erfasste Grundsteuer für zum Betriebsvermögen des Unternehmers gehörenden Grundbesitz". Das ist nicht mehr der Prozentsatz vom Grundsteuerwert. Die Kataster-Notiz zu `GEWSTG-36` („einfache Grundbesitzkürzung ab 2025") ist daraufhin zu prüfen. Für die Kurzform folgenlos, weil sie die einfache Kürzung nicht rechnet; das ist vorsichtig.

Nicht gelesen und deshalb nur als Einschätzung verwendet:
- Rechtsprechung zur erweiterten Kürzung im Veräußerungsjahr, zur Vorfälligkeitsentschädigung der Privatperson und zur Betriebsaufgabe der Objekt-KG;
- EStR R 6.5 und R 21.5 (Zuschüsse);
- § 15a EStG, § 13 KStG, § 9 Abs. 5 EStG, UStG.

## Nicht geprüft

- Die Rechengenauigkeit des ganzen Finanzplans und der Kennzahlen. Das prüft der Finanzmathematiker; ich habe nur die Steuerbeispiele in R-7.7 bis R-7.10 und R-7.8 (155.680 €) nachgerechnet.
- `referenzfaelle.py` habe ich nicht ausgeführt; RF-13 und die Renditen habe ich nicht nachgerechnet.
- Abschreibungswahl, Sonderabschreibung (`MA-022`, `MA-023`, `MA-029`) und Zinsschranke. Sie wirken erst in Teil 2; die Annahmen habe ich nur auf Folgerichtigkeit mit der Kurzform gelesen.
- Gemeinnützigkeit nach §§ 51 ff. AO und die Wohngemeinnützigkeit (Bericht D.4, fünfte Zeile). Nicht gelesen; die Kurzform fasst sie unter „befreit".
