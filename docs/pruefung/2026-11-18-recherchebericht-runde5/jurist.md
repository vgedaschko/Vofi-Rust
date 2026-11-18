Rolle: Jurist (Immobilien- und Wohnungswirtschaftsrecht; Steuerrecht der Immobilie; Förder- und Beihilferecht; Rechtsrisiken des Werkzeugs)
Prüfobjekt: `reports/VOFI Immobiliensoftware Marktrecherche.md` und `docs/modellannahmen.md` (aus `annahmen.toml`), Fassung nach der vierten Überarbeitung. Es handelt sich um eine Änderungsprüfung der rechtlich erheblichen Stellen anhand von `bericht-aenderungen-seit-runde4.diff` und `annahmen-und-spezifikation-seit-runde4.diff`. Ganz gelesen habe ich Abschnitt 4 („Investorensicht und Steuerstatus“), Abschnitt 6 (NBank, Absatz zu den zuwendungsfähigen Kosten), Anhang B.1 (die Zeilen Modernisierungsumlage, Heizungstausch, Wärmepumpe), B.3 und B.5 ganz, B.6 die Zeilen `MA-019` bis `MA-026`, C.1 die Zeilen zu den Mietwohnungen, D.4 die Zeilen Ertragsteuern, De-minimis-Konto, Darlehen und Steuerstatus-Tabelle, dazu im Verzeichnis die Einträge `MA-019` und `MA-021` bis `MA-027` sowie im Kataster die Einträge `ESTG-35`, `ABSCHLAGSV-1`, `NI-ANBEST-P` und `AO-233A`. Runde 5, letzte Runde.

Gesamturteil: Trägt. Alle acht Punkte aus Runde 4 sind eingearbeitet. Die neue Zeile zu § 35 EStG gibt Faktor und beide Begrenzungen am Wortlaut richtig wieder. Die drei Ausnahmen von der Vorsichtsregel sind jetzt rechtlich begründet. Für `MA-021` habe ich zusätzlich einen Beleg der NBank gefunden, der die Voreinstellung stützt (Befund 5). Es bleiben sechs Befunde, alle mit wenigen Zeilen zu beheben:
- Der Kreis der an De-minimis Gebundenen ist nach dem Wortlaut des § 7b Abs. 5 EStG an die Person geknüpft, nicht an das Vorhaben. Damit ist er weiter, als B.3 ihn zieht (Befund 1).
- Das Rechenbeispiel zu § 35 übergeht den Gewerbesteuer-Freibetrag. Diesen Fehler habe ich in Runde 4 selbst vorgegeben (Befund 2).

Note: **9 von 10, die Note hält** (Runde 1: 6, Runde 2: 7, Runde 3: 9, Runde 4: 9).
- **Warum sie hält:** Die Rechtsaussagen der geänderten Teile stimmen am Gesetzestext. Die offenen Punkte sind gekennzeichnet und richtig zugeordnet. Die verbliebenen Befunde betreffen Randbereiche oder Rechenbeispiele, keine Grundregel. Nur Befund 1 kann ein Ergebnis kippen, und auch er nur bei einem bestimmten Investorentyp.
- **Was zur 10 fehlt:** die Befunde 1 bis 4 im Bericht und im Verzeichnis, Befund 5 im Verzeichnis und im Kataster. Außerdem die Lektüre der ANBest-P (Niedersachsen) und der Verwaltungsauffassung zu § 7b (BMF-Schreiben). Beide sind von hier aus nicht erreichbar.

## Stand der Runde-4-Punkte

| Nr. | Punkt aus Runde 4 | Stand | Fundstelle jetzt |
|---|---|---|---|
| 1 | § 35 EStG fehlt | behoben, Rest in Befund 2 und 3 | B.3 „Anrechnung der Gewerbesteuer auf die Einkommensteuer“; D.4 Ertragsteuern (Kurzform 1a) und Steuerstatus-Tabelle; B.5 Prüfliste des Steuerberaters (Ermäßigungshöchstbetrag); Kataster `ESTG-35` |
| 2 | Kennungen `MA-021` bis `MA-025` am Wirkort | behoben | `MA-021`: Abschnitt 6, C.1, D.4 „Grobförderung“. `MA-022`: B.3 „Rückabwicklung“. `MA-023`: B.3 „Kostengrenzen“, C.1. `MA-024`: B.1 „Wärmepumpe“. `MA-025`: B.1 „Modernisierungsumlage“. Die Zeile „Modernisierungsumlage“ sagt jetzt „Ob Nr. 4a damit umlagefähig ist, ist offen; angesetzt wird keine Umlage (`MA-025`)“ und widerspricht dem Verzeichnis nicht mehr |
| 3 | `MA-019`: Nennbetrag als andere Lesart, Abweichung kennzeichnen | behoben | Verzeichnis: „Strenger: … Nennbetrag“; Grundlage „Begründete Abweichung von der Vorsichtsregel“ mit der Systematik des § 559a Abs. 2 BGB und der Kappung. B.6 entsprechend |
| 4 | `MA-021`: ANBest-P als Grundlage, „bis zu einem Sechstel“ | behoben | Grund und Klärung verweisen auf die ANBest-P über RL Nr. 12.3.1. „bis zu einem Sechstel (19/119)“ ist richtig, 19/119 sind 15,97 %. Dass die Grundstückskosten nicht betroffen sind, ist ergänzt. Neuer Beleg in Befund 5 |
| 5 | `MA-025`: Grund der Offenheit | behoben | „Grund“ nennt die Spannung zwischen § 559 Abs. 1 Satz 1 und Satz 2 BGB, die andere Lesart beide Wege (Satz 2, Nr. 4). Die Frage an den Anwalt steht in der Bemerkung |
| 6 | Bemessungsgrundlage beim Ersterwerb | behoben in C.1; für § 7b neuer Befund 4 | C.1: Kaufpreis nebst Erwerbskosten, höchstens Marktwert, niedrigster Wert, niedrigerer Kaufpreis geht vor (RL Nr. 5.3.2.1, 5.3.2.4). Die Übertragung auf § 7b über `MA-023` geht zu weit |
| 7 | `MA-022`: schädliche Fälle, „Nutzungszeitraum“ | behoben | Die Annahme nennt Selbstnutzung, unentgeltliche Überlassung, Beherbergung und Aufgabe der Vermietungsabsicht als schädlich. Die andere Lesart sagt „Nutzungszeitraum nach § 7b“. Die Begründung stützt sich zuerst auf das Wort „dient“ |
| 8 | Randfälle § 8 Abs. 2 KStG, § 52 Abs. 15a EStG | behoben | B.3 „Beihilfebindung“ mit Genossenschaft und Vermietungsgenossenschaft nach Verlust der Befreiung; D.4 koppelt die De-minimis-Prüfung an den Wegfall der Befreiung; B.3 „Voraussetzungen“ mit dem Halbsatz zu § 4a. Beides ist am Wortlaut richtig |

## Zu den Prüffragen

**§ 35 EStG (Frage 1).** Die Zeile in B.3 gibt den Wortlaut von § 35 Abs. 1 Satz 1, 2 und 5 richtig wieder:
- Ermäßigungshöchstbetrag als die Steuer, die anteilig auf die gewerblichen Einkünfte entfällt;
- das Vierfache des Messbetrags beim Einzelunternehmen (Nr. 1) und des anteiligen Messbetrags beim Mitunternehmer (Nr. 2);
- Begrenzung auf die tatsächlich zu zahlende Gewerbesteuer.

Der Faktor 4 stimmt. Dass der Ermäßigungshöchstbetrag von den übrigen Einkünften abhängt, folgt aus der Formel in Satz 2 (positive gewerbliche Einkünfte geteilt durch die Summe aller positiven Einkünfte, mal geminderte tarifliche Steuer). Ihn wie den Steuersatz als Eingabe zu führen und dem Steuerberater zuzuweisen (D.4, B.5), ist richtig. Das ist eine Eingabe des Anwenders, keine Modellannahme. Falsch ist das Rechenbeispiel (Befund 2). Unvollständig sind die Kurzform in 1a und der Kreis der Begünstigten (Befund 3).

**De-minimis-Bindung (Frage 3).** § 8 Abs. 2 KStG gilt für alle Steuerpflichtigen nach § 1 Abs. 1 Nr. 1 bis 3 KStG, also Kapitalgesellschaften, Genossenschaften und Versicherungsvereine. Das ist richtig übernommen, und die einmalige Definition in B.3 mit Verweisen aus Abschnitt 5, D.4 und B.5 ist sauber. Der Kreis ist aber zu eng gezogen (Befund 1).

**`MA-026` und `MA-027` (Frage 4).** Beide sind als Annahme erkennbar:
- `MA-026` steht in D.4 „Darlehen“ ausdrücklich als „Annahme über die Praxis der Bank“, außerdem in B.6, D.5 und in der Spezifikation, Kapitel 2. Rechtlich unkritisch: Wie eine Bank die Kapitaldienstfähigkeit eines gewerblichen Investors prüft, schreibt keine Norm vor. Die BelWertV regelt den Beleihungswert für die Pfandbriefdeckung, nicht die Kreditentscheidung. Dass `quellen` leer ist, ist deshalb richtig.
- `MA-027` hat keinen Rechtsgehalt und steht am Wirkort (Spezifikation, Kapitel 3).

**Die drei Ausnahmen (Frage 4).**
- `MA-019`: trägt. Die Begründung ist jetzt systematisch, nämlich § 559e Abs. 1 mit dem Verweis auf § 559a, dessen Abs. 2 Darlehen über den Zinsvorteil erfasst. Sie stellt nicht mehr auf die Folge ab.
- `MA-021`: trägt, und jetzt mit einem Textbeleg der NBank (Befund 5). Die Bruttolesart ist danach keine Ausnahme mehr, sondern die am Text gestützte Lesart.
- `MA-022`: trägt. Das Wortlautargument („dient“, Zweckbestimmung) steht vorn, und die schädlichen Fälle sind abgegrenzt.

**Kataster (Frage 5).** Siehe unten unter „Gelesene Normen“. Stand und Beleg der vier Einträge sind plausibel, drei davon habe ich heute an der Gesamtausgabe bestätigt. `NI-ANBEST-P` ist weiterhin nicht erreichbar.

## Befunde

1. [wichtig · begründete Einschätzung] **B.3 „Sonderabschreibung, Beihilfebindung“ und D.4 Steuerstatus „Privatperson oder vermögensverwaltende Personengesellschaft“ („Sonderabschreibung ohne De-minimis-Prüfung“): Der Kreis der Gebundenen ist zu eng gezogen.**
   - **Wortlaut:** § 7b Abs. 5 Satz 2 EStG wendet die De-minimis-Bindung für Bauanträge ab 2023 an „nur bei Anspruchsberechtigten mit Einkünften im Sinne der §§ 13, 15 und 18“. Der Satz knüpft an die Person des Anspruchsberechtigten an. Dass die Wohnung selbst zu diesen Einkünften gehören muss, sagt er nicht. B.3 schließt daraus („Gebunden sind damit …“), dass Privatpersonen und vermögensverwaltende Personengesellschaften nicht gebunden sind. Das ist die günstigere von zwei Lesarten und nicht gekennzeichnet.
   - **Szenario 1, persönliche Einkünfte:** Eine Ärztin mit Praxis (§ 18 EStG) oder ein Gesellschafter mit gewerblichen Beteiligungseinkünften (§ 15) baut privat Mietwohnungen. Nach dem Wortlaut ist sie „Anspruchsberechtigte mit Einkünften im Sinne des § 18“ und gebunden. Das Werkzeug rechnet die volle Sonderabschreibung ohne Prüfung.
   - **Szenario 1, Wirkung:** Bei 30 Wohnungen zu 70 m² und 4.000 €/m² Bemessungsgrundlage beträgt die Sonderabschreibung 420.000 € im Jahr. Bei 42 % Steuersatz ergibt das rund 176.000 € Steuervorteil im Jahr. Ein solcher Vorteil kann die De-minimis-Höchstgrenze des Katalogs (`EU-DE-MINIMIS-2023-2831`) binnen drei Jahren überschreiten. Dann entfällt die Sonderabschreibung, soweit die Grenze überschritten ist. Das ändert die Rendite im Neubau spürbar.
   - **Szenario 2, Körperschaft als Gesellschafterin:** Eine vermögensverwaltende KG hat eine GmbH als Gesellschafterin. Anspruchsberechtigt sind die Gesellschafter. Für den Anteil der GmbH gelten alle Einkünfte als gewerblich (§ 8 Abs. 2 KStG), und die Bindung greift nach beiden Lesarten. Die pauschale Freistellung der vermögensverwaltenden Personengesellschaft ist für diesen Anteil falsch.
   - **Vorschlag:**
     - In B.3 statt „Gebunden sind damit …“ schreiben: „Gebunden ist nach dem Wortlaut jeder Anspruchsberechtigte, der Einkünfte aus Land- und Forstwirtschaft, Gewerbebetrieb oder selbständiger Arbeit hat, auch aus anderen Quellen. Bei Personengesellschaften kommt es auf jeden Gesellschafter an; Körperschaften als Gesellschafter sind stets gebunden (§ 8 Abs. 2 KStG).“
     - Eine neue Annahme `MA-028` anlegen. Voreinstellung: gebunden, sobald der Investor solche Einkünfte hat, als Ja/Nein-Merkmal des Investors. Andere Lesart: gebunden nur, wenn die Wohnung zu diesen Einkünften gehört. Klärung durch den Steuerberater, Gewicht mittel. Ich nenne die Verwaltungsauffassung (BMF-Schreiben zu § 7b) nicht, weil ich sie nicht gelesen habe.
     - D.4 „Privatperson“: „De-minimis-Prüfung nach B.3, wenn der Investor das Merkmal trägt“.
   - **Zuständig:** Im Bericht und im Verzeichnis zu beheben; die Lesart bestätigt der Steuerberater.

2. [Hinweis · belegt] **B.3 „Anrechnung der Gewerbesteuer“ (Rechenbeispiel) und B.3 „Gewerbesteuer“: Der Freibetrag von 24.500 € fehlt. Das Beispiel stimmt deshalb für den Steuerstatus nicht, für den es geschrieben ist.**
   - **Wortlaut:** Nach § 11 Abs. 1 Satz 3 Nr. 1 GewStG wird der Gewerbeertrag „bei natürlichen Personen sowie bei Personengesellschaften um einen Freibetrag in Höhe von 24 500 Euro“ gekürzt, nachdem er auf volle 100 € abgerundet ist.
   - **Gegenrechnung:** Bei 100.000 € Gewerbeertrag beträgt der Messbetrag (100.000 − 24.500) × 3,5 % = 2.642,50 €, nicht 3.500 €.
     - Bei 400 % Hebesatz: Gewerbesteuer 10.570 €, Ermäßigung 4 × 2.642,50 = 10.570 €.
     - Bei 280 %: Gewerbesteuer 7.399 €, Ermäßigung auf 7.399 € begrenzt.
     - „Bis zu 14 Prozentpunkte“ gilt für den um den Freibetrag gekürzten Gewerbeertrag. Bezogen auf 100.000 € sind es 10,6 Punkte.
   - **Herkunft:** Diesen Fehler habe ich in Runde 4 selbst vorgegeben, weil ich mit der Rechnung der Körperschaft gerechnet habe. Er geht nicht auf die Überarbeitung zurück.
   - **Wirkung:** Die Aussage der Zeile bleibt richtig, die Zahlen stimmen nicht. Fehlt der Freibetrag im Katalog, ist die Gewerbesteuer kleinerer Personengesellschaften zu hoch. Bis 400 % Hebesatz gleicht § 35 das weitgehend aus, darüber nicht.
   - **Vorschlag:**
     - In B.3 „Gewerbesteuer“ ergänzen: „bei natürlichen Personen und Personengesellschaften Freibetrag 24.500 € (§ 11 Abs. 1 Satz 3 Nr. 1 GewStG)“.
     - Das Beispiel umstellen auf: „Bei 100.000 € Gewerbeertrag einer Personengesellschaft beträgt der Messbetrag nach Freibetrag 2.642,50 €: Die Ermäßigung erreicht bei 400 % die Gewerbesteuer von 10.570 € und ist bei 280 % auf 7.399 € begrenzt. Ohne die Anrechnung wäre die Steuerlast um bis zu 14 Prozentpunkte des gekürzten Gewerbeertrags zu hoch.“
     - In D.4, Zeile Personengesellschaft: „Gewerbesteuer mit Freibetrag, ohne oder mit erweiterter Kürzung“.
   - **Zuständig:** im Bericht zu beheben.

3. [Hinweis · belegt] **D.4 „Ertragsteuern“, Kurzform 1a („pauschaler Anrechnung …, also dem Vierfachen des Messbetrags, höchstens der Gewerbesteuer“): Drei Regeln fehlen, die die Kurzform auch ohne die übrigen Einkünfte abbilden kann.**
   - **Erstens die zweite Begrenzung.** Die Ermäßigung kann nicht höher sein als die Einkommensteuer auf die gewerblichen Einkünfte (§ 35 Abs. 1 Satz 1 und 2). Mit dem eingegebenen Steuersatz ist das in der Kurzform der Satz mal gewerblicher Gewinn des Jahres, nicht unter null. Einen Vortrag nicht ausgenutzter Ermäßigung sieht § 35 nicht vor. Szenario: Ein Jahr mit Einkommensteuer-Verlustvortrag, aber Gewerbeertrag nach Hinzurechnung. Wörtlich umgesetzt ergibt die Kurzform eine negative Einkommensteuer.
   - **Zweitens die Begünstigten.** § 35 ermäßigt nur die Einkommensteuer, also nur den Anteil natürlicher Personen. Bei einer GmbH & Co. KG mit einer GmbH als Kommanditistin gibt es für deren Anteil keine Anrechnung.
   - **Drittens der Abzug.** Die Gewerbesteuer ist keine Betriebsausgabe (§ 4 Abs. 5b EStG). Sie mindert also weder den Gewinn für die Einkommen- oder Körperschaftsteuer noch ihre eigene Bemessungsgrundlage. Bericht und Spezifikation sagen das nirgends. Für einen Rechenkern, der Steuern aus einem Ergebnis nach Kosten ableitet, ist es eine typische Fehlerquelle, auch bei der Körperschaft.
   - **Vorschlag:**
     - Kurzform: „… höchstens der Gewerbesteuer und der Einkommensteuer auf den gewerblichen Gewinn des Jahres (eingegebener Satz, nicht unter null), ohne Vortrag; nur für den Anteil natürlicher Personen“.
     - In B.3 „Gewerbesteuer“: „nicht als Betriebsausgabe abziehbar (§ 4 Abs. 5b EStG)“. Kataster `ESTG-4` um Abs. 5b ergänzen.
   - **Zuständig:** im Bericht zu beheben.

4. [Hinweis · begründete Einschätzung] **C.1 („Die Baukostenobergrenze der Sonderabschreibung folgt beim Ersterwerb derselben Grundlage“) und `MA-023` („beim Ersterwerb am Kaufpreis nebst Erwerbskosten, höchstens dem Marktwert“): Die Übertragung der NBank-Grundlage auf § 7b geht in zwei Punkten über das Gesetz hinaus.**
   - **Grund und Boden:** § 7b Abs. 2 Satz 2 und Abs. 3 messen die Anschaffungs- oder Herstellungskosten „der begünstigten Wohnung“. Grund und Boden ist ein eigenes Wirtschaftsgut und nicht abnutzbar. Bei der Herstellung lässt `MA-023` ihn deshalb zu Recht weg (Kostengruppen 200 bis 700 ohne 100). Beim Erwerb schließt die Annahme ihn über den ganzen Kaufpreis ein. Dieselben Worte würden so für Bau und Kauf verschieden gelesen.
   - **Szenario:** Eine Wohnung kostet 5.900 €/m² Kaufpreis mit Nebenkosten bei 20 % Bodenanteil. Der Gebäudeanteil liegt bei 4.720 €/m², unter der Grenze von 5.200 €/m². Die Voreinstellung versagt die Sonderabschreibung ganz, weil die Grenze eine Ausschlussgrenze ist. Das sind 20 % von 4.000 €/m² über vier Jahre, also 800 €/m² Abschreibung. „Vorsichtig“ ist diese Voreinstellung nur dem Anschein nach. Eine Lesart, die das Gesetz in diesem Punkt nicht trägt, sollte nicht Voreinstellung sein.
   - **Marktwertdeckel:** Er stammt aus RL Nr. 5.3.2.4 und hat in § 7b keine Grundlage. Für die Grenze zählen die tatsächlichen Anschaffungskosten. Ein Deckel lässt die Grenze seltener greifen und widerspricht damit sogar der Vorsichtsregel, die `MA-023` für sich beansprucht.
   - **Vorschlag:**
     - `MA-023` beim Erwerb: „Gebäudeanteil des Kaufpreises nach der Kaufpreisaufteilung (D.4) zuzüglich anteiliger Erwerbsnebenkosten, ohne Marktwertdeckel“.
     - Offen bleibt nur, welche Gebäudekosten zählen, etwa Außenanlagen. Dabei bleibt die weitere Summe Voreinstellung.
     - Den Satz in C.1 streichen oder ersetzen durch: „Die Baukostenobergrenze der Sonderabschreibung misst beim Erwerb den Gebäudeanteil (B.3, `MA-023`)“.
   - **Zuständig:** im Verzeichnis und im Bericht zu beheben; Bestätigung durch den Steuerberater mit der Fachspezifikation des Steuermoduls.

5. [Hinweis · belegt] **`MA-021`, Grundlage, und B.6, Zeile `MA-021`: Ein Text der NBank stützt die Voreinstellung. Das Verzeichnis führt sie noch als ungelesene „übliche Regel“ und als Ausnahme von der Vorsichtsregel.**
   - **Fund:** NBank, Vordruck 4009 „Einfacher Verwendungsnachweis“, Stand Juli 2026, verlinkt auf der Programmseite „Mietwohnungen in Mehrfamilienhäusern (Allgemeine Mietwohnraumförderung)“. Er ist ein XFA-Formular, den Text habe ich aus dem Formular ausgelesen. Nr. 5.4 lautet: „Ich/Wir erkläre(n), dass in den zuwendungsfähigen Ausgaben keine Umsatzsteuerbestandteile enthalten sind, soweit diese gemäß § 15 Umsatzsteuergesetz (UStG) als Vorsteuer abziehbar sind.“
   - **Folgerung:** Die Erklärung setzt voraus, dass nicht abziehbare Umsatzsteuer zuwendungsfähig ist. Sie entspricht der üblichen Regel der ANBest-P, auf die RL Nr. 12.5 für den Verwendungsnachweis ausdrücklich verweist (Nummer 6 ANBest-P).
   - **Vorschlag:**
     - Grundlage: „NBank, Vordruck 4009, Nr. 5.4: nur abziehbare Vorsteuer ist aus den zuwendungsfähigen Ausgaben herauszunehmen; RL Nr. 12.5 mit Nummer 6 ANBest-P“.
     - Den Satz „Ausnahme von der Vorsichtsregel“ streichen. Die Voreinstellung ist die am Text gestützte Lesart, und die Abweichung entfällt.
     - Gewicht von mittel auf gering setzen. Bestätigung im Gespräch mit der NBank, Status bleibt bis dahin offen.
     - Ins Kataster `NBANK-VORDR-4009` aufnehmen (am Original gelesen am 18.11.2026, Stand Juli 2026). Die B.6-Zeile und die Liste der Ausnahmen in `TASKS.md` und in der Durchsicht durch den Auftraggeber entsprechend anpassen.
   - **Zuständig:** Verzeichnis und Kataster; die Bestätigung gibt die NBank.

6. [Hinweis · begründete Einschätzung] **D.4 Steuerstatus-Tabelle („Verkaufsgewinn steuerpflichtig“ bei Körperschaft und gewerblicher Personengesellschaft) und B.5: Ob der Verkaufsgewinn der Gewerbesteuer unterliegt, ist nicht geregelt.**
   - **Problem:** Mit dem neuen Steuerstatus wird die Frage erheblich, und sie hängt am Gestaltungsfall:
     - Nach § 7 Satz 2 GewStG gehört der Gewinn aus der Veräußerung des Betriebs oder eines Mitunternehmeranteils zum Gewerbeertrag, „soweit er nicht auf eine natürliche Person als unmittelbar beteiligter Mitunternehmer entfällt“.
     - Der Verkauf der Immobilie aus dem fortbestehenden Betrieb ist dagegen laufender Gewinn.
     - Bei erweiterter Kürzung kommt es darauf an, ob der Verkaufsgewinn auf die „Verwaltung und Nutzung des eigenen Grundbesitzes“ entfällt (§ 9 Nr. 1 Satz 2 GewStG).
   - **Wirkung:** Bei 400 % Hebesatz bis zu 14 % des Verkaufsgewinns, bei natürlichen Personen teils über § 35 ausgeglichen. Bei langen Haltedauern ist der Restwert der größte Einzelposten des Endwerts.
   - **Vorschlag:** In D.4 ergänzen: „Gewerbesteuer auf den Verkaufsgewinn je Steuerstatus nach Vorgabe des Steuerberaters; voreingestellt steuerpflichtig, bei erweiterter Kürzung nicht“. Die Voreinstellung „nicht“ ist eine Annahme und braucht eine Kennung, oder es wird vorsichtig ebenfalls „steuerpflichtig“ voreingestellt. In B.5 den Punkt für den Steuerberater aufnehmen.
   - **Zuständig:** Steuerberater; im Bericht nur Zeile und Prüfauftrag.

**Ohne Befund geprüft** (Wortlaut stimmt mit dem Prüfobjekt überein):
- § 35 Abs. 1 bis 4 EStG: Faktor, beide Begrenzungen, gesonderte Feststellung bei Mitunternehmerschaften, Anteil nach dem allgemeinen Gewinnverteilungsschlüssel ohne Vorabgewinne.
- § 7b Abs. 1 bis 5 EStG in den Zeilen B.3 „Voraussetzungen“, „Kostengrenzen“ und „Rückabwicklung“.
- § 52 Abs. 15a Satz 1 bis 3 EStG. Die Einschränkung auf §§ 13, 15, 18 gilt nach Satz 3 nur für Bauanträge ab 2023. Die ältere Fassung läuft mit dem Veranlagungszeitraum 2026 aus, deshalb ist das für die Planung ohne Belang.
- § 8 Abs. 2 und § 1 Abs. 1 KStG.
- § 233a Abs. 2 und 2a AO in Verbindung mit § 7b Abs. 4 Satz 4 EStG.
- § 1 AbschlagsV.
- RL Mietwohnraum 2026, Nr. 12.3.1 und 12.5 (ANBest-P als Anlage 2 zu VV Nr. 5.1 zu § 44 LHO; Verwendungsnachweis nach Nummer 6 ANBest-P).

## Gelesene Normen mit Lesedatum (zum Nachtragen im Kataster)

Abgerufen am **18.11.2026** von gesetze-im-internet.de über curl (ISO-8859-1). Die Stände der Gesamtausgaben habe ich am Kopf der jeweiligen Gesamtausgabe abgelesen.

| Kennung | Norm | Gelesen | Vorgefundene Fassung | Abgleich mit dem Kataster |
|---|---|---|---|---|
| `ESTG-35` | § 35 EStG | Abs. 1 bis 4 | EStG zuletzt geändert durch Art. 1 G v. 15.10.2026 I Nr. 307 | Stand stimmt. Im Vermerk „Abs. 1 und 2“ auf „Abs. 1 bis 4 (Runde 5)“ erweitern |
| `ESTG-7B` | § 7b EStG | Abs. 1 bis 5 | wie oben | stimmt |
| `ESTG-52` | § 52 EStG | nur Abs. 15a | wie oben | stimmt |
| `ESTG-4` | § 4 EStG | nur Abs. 5b | wie oben | neu zu vermerken (Befund 3) |
| `KSTG-8`, `KSTG-1` (falls geführt) | § 8 Abs. 2, § 1 Abs. 1 KStG | – | – | `KSTG-8` stimmt (04.02.2026 laut Kataster; Stand heute nicht erneut abgelesen) |
| `GEWSTG-11` | § 11 GewStG | Abs. 1 bis 3 | – | Im Vermerk den Freibetrag nach Abs. 1 Satz 3 nachtragen (Befund 2) |
| `GEWSTG-7` (neu, falls nicht geführt) | § 7 GewStG | Satz 1 bis 4 | – | Befund 6 |
| `GEWSTG-9` | § 9 GewStG | nur Nr. 1 Satz 2 | – | stimmt |
| `AO-233A` | § 233a AO | Abs. 2 und 2a erneut | AO zuletzt geändert durch Art. 6 G v. 22.10.2026 I Nr. 320 | Stand 22.10.2026 stimmt |
| `ABSCHLAGSV-1` | § 1 AbschlagsV | ganz | zuletzt geändert durch Art. 4 G v. 28.4.2017 (BGBl. I S. 969) | Fassung 28.04.2017 stimmt |
| `NBANK-RL-MIETWOHNRAUM-2026` | RL Mietwohnraum 2026 (PDF von www.nbank.de) | Nr. 12.3.1, 12.4.1, 12.5 erneut; Volltextsuche „Umsatzsteuer“, „Vorsteuer“, „ANBest“ | Nds. MBl. 2026 Nr. 319 vom 1. Juli 2026 | stimmt |
| neu: `NBANK-VORDR-4009` | NBank, Vordruck 4009 „Einfacher Verwendungsnachweis“ (www.nbank.de, Downloads/Formulare-Verwendungsnachweis) | Nr. 5.4 | „Stand: Juli 2026“ (Formularkopf), PDF erstellt 22.07.2026 | neu anzulegen (Befund 5) |
| `NI-ANBEST-P` | VV zu § 44 LHO mit ANBest-P (Nds.) | nicht gelesen | – | bleibt „nicht geprüft“. Auf www.nbank.de nicht verlinkt gefunden; voris und das Landesportal mf.niedersachsen.de lehnt der Proxy ab (403) |

Die Normen des Mietrechts (§§ 555b, 559, 559a, 559e, 559f BGB) habe ich abgerufen, aber nicht erneut ganz gelesen. Die Zeilen in B.1 sind gegenüber Runde 4 nur um die Kennungen ergänzt, das Runde-4-Ergebnis gilt fort.

## Vor Markteinsatz verbindlich zu prüfen (Ergänzung zu B.5)

- **Steuerberater:**
  - Kreis der De-minimis-Gebundenen bei Privatpersonen mit Einkünften nach §§ 13, 15, 18 und bei vermögensverwaltenden Gesellschaften mit Körperschaften als Gesellschaftern (Befund 1);
  - Gebäudeanteil als Maß der Baukostenobergrenze beim Erwerb (4);
  - Gewerbesteuer auf den Verkaufsgewinn je Steuerstatus (6).
- **NBank:** Bestätigung der Bruttolesart (Befund 5). Nach dem Vordruck 4009 ist das eine Formsache.
- **Anwalt:** Gegenüber Runde 4 nichts Neues (`MA-019`, `MA-024`, `MA-025` wie dort).

Im Bericht und im Verzeichnis zu erledigen, ohne Auslegungsfrage, sind die Befunde 2, 3 und 5 sowie die Katalogzeile zu Befund 6.

## Nicht geprüft

- ANBest-P und VV zu § 44 LHO (Niedersachsen): nicht erreichbar (Proxy 403 bei voris und mf.niedersachsen.de; auf nbank.de nicht verlinkt). Ersatzweise der Vordruck 4009 (Befund 5).
- Verwaltungsauffassung (BMF-Schreiben zu §§ 7b und 35 EStG), Rechtsprechung zur erweiterten Kürzung beim Verkauf und zu § 7 Satz 2 GewStG. Die Befunde 1, 4 und 6 sind deshalb Einschätzungen am Wortlaut.
- Unionsrecht (De-minimis-VO (EU) 2023/2831): Höchstbetrag und Ermittlung des Beihilfewerts nicht erneut gelesen. Die Wirkungsrechnung in Befund 1 nennt deshalb keinen Betrag der Grenze.
- Teile des Berichts ohne Rechtsgehalt sowie Zeilen, die gegenüber Runde 4 unverändert sind. Das Runde-4-Ergebnis gilt fort.
- Bundesgesetzblatt (`MA-010`): in dieser Runde nicht versucht.
