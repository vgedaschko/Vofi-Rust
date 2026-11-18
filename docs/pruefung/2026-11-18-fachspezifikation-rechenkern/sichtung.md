# Sichtung der Prüfrunde 1 – Fachspezifikation des Rechenkerns, Teil 1 (2026-11-18)

Prüfobjekt: `docs/fachspezifikation-rechenkern.md` (Entwurf, 148 Regeln) und der Referenzrechner unter `research_notes/…/skripte/referenzrechner/`.

Noten: Finanzmathematiker **8** · Fachexperte **7** · Praktiker **7** · Steuerberater **7** · Bank **7** · Controller **7** · Grenzfälle **7**. Befunde: 7 kritisch, 43 wichtig, 20 Hinweise (Zählung nach Kennzeichnung in den Berichten; einzelne Befunde ohne eigene Nummer sind unten mit aufgenommen).

Gesamtbild: Wo der Kern geregelt ist, rechnet er richtig – der Finanzmathematiker hat den Ankaufsfall, den Testfall und die Anschlussfinanzierung allein aus dem Text auf den Cent nachgebaut, der Controller drei Stichproben. Die Schwächen liegen an vier Stellen: Ränder (Abstürze und stille Falschergebnisse), Miete im Bestand, Bankensicht und Steuer rechnen an mehreren Stellen günstiger als die vorsichtige Lesart; und die Ordnung des Modells (Sperre bei verletzter Probe, versteckte Konstanten, Änderbarkeit der Vorgaben) ist noch nicht durchgehalten.

## Nachgeprüft

- **Mehrfach unabhängig gefunden:** fehlende Felder des übernommenen Darlehens (Finanzmathematiker 4, Bank 4, Praktiker 3, Controller 2); 15-%-Regel als Rechenregel (Fachexperte 2, Steuerberater 3); Vorfälligkeit ohne Kündigungsrecht nach zehn Jahren (Fachexperte 3, Bank 5, Grenzfälle 5, Praktiker); Bezug der Gesamtkapitalrendite beim Neubau (Finanzmathematiker 5, Fachexperte 9); Instandhaltung nach Baualter (Fachexperte 8, Praktiker 7); Änderbarkeit der Vorgaben (Controller 5, Praktiker 8); „Beleihungsauslauf" (Fachexperte 10, Bank 8); P-04 (Grenzfälle 6, Finanzmathematiker 8).
- **Am Gesetzestext gelesen (18.11.2026, laut Prüfberichten):** § 558 BGB (Fachexperte), § 489 und § 490 BGB (Bank), § 6 Abs. 1 Nr. 1a und § 7 Abs. 4 EStG (Fachexperte, Steuerberater), §§ 2, 7, 8, 9, 10a, 11 GewStG, §§ 5, 10d, 11, 15, 20, 23, 32d, 35, 51a EStG, §§ 5, 23 KStG (Steuerberater).
- **Rechnerisch belegt:** jede Zahl unten stammt aus einer Gegenrechnung der Prüfer; die Skripte sind unter `research_notes/…/skripte/pruefrunde-fachspezifikation-1/` gesichert (Finanzmathematiker und Steuerberater: Zahlen in den Berichten).
- **Eigene Festlegung zurückgenommen:** Das Kennzeichen „erweiterte Grundstückskürzung" für das Einzelunternehmen (Entscheidung vom selben Tag) ist nach dem Wortlaut von § 9 Nr. 1 Satz 2 GewStG falsch; siehe Punkt 36.

## Übernommen (erste Überarbeitung)

### A. Ordnung des Modells

1. **Verletzte Probe sperrt das Ergebnis** – im Lauf, in der Preissuche und in der Zielwertsuche. Schlägt eine Probe in einem Suchschritt an, endet die Suche mit Meldung und ohne Preis. Der Referenzrechner setzt das um; ein Referenzfall mit absichtlich verletzter Probe gehört dazu (Controller 1).
2. **Eingaben ergänzen:** Land und Gemeinde als Schlüssel für Grunderwerbsteuer, Hebesatz, Kappungsgrenze und Mietpreisbremse (Controller 2, Fachexperte 5); beim übernommenen Darlehen Anschlusszins, laufender Beitrag, Kennzeichen „Förderdarlehen", ursprünglicher Nennbetrag und Rang vor oder nach der Bank (Finanzmathematiker 4, Bank 4, Praktiker 3); Angebotspreis; Ist-Miete in der Form des Exposés (Jahresbetrag, Stellplätze, Leerstand); Bodenanteil mit Voreinstellung (Praktiker 8). Rückwirkende Stichtage sind zulässig (Controller 7). Die Zählung der Eingaben wird nachgezogen, auch für den Ankauf gebundener Bestände.
3. **Keine versteckten Konstanten:** Kappungszeitraum, Schwelle und Frist der 15-%-Regel, Suchgrenzen, Stützstellen, Staffeln der gebundenen Miete und das Startjahr werden Katalogwerte oder Vorgaben mit Kennung und Herkunft; im Referenzrechner sind Vorgaben des Hauses und Katalogwerte getrennt (Controller 3). KAT-02 wird Vorgabe des Hauses.
4. **Proben:** Steuerprobe (Fortschreibung der Verlustvorträge, Brücke vom Ergebnis zu den Zahlungen), Saldo- und Bestandsprobe der Unterlassensalternative, Proben für Zinsen, Index und Abschreibungstakt; P-04 so fassen, dass sie den Satz „Eigenkapital gleich Mittelbedarf abzüglich Überschüssen, Zuschüssen und Darlehen" wirklich sichert und Steuer und Tilgung der Bauzeit nennt; P-08 gilt für jeden Lauf; P-09 prüft unabhängig; alle Proben rechnen nach den Rundungsregeln des Kerns (Controller 4, Grenzfälle 6 und 7, Finanzmathematiker 7 und 8).
5. **Vorgaben des Hauses im Vorhaben:** Jede Vorgabe hat eine Richtung „strenger"; im Vorhaben ist nur die strengere Richtung frei. Eine Lockerung braucht eine Begründung, und jede Abweichung steht in einer Liste auf dem Kennzahlenblatt. Das gilt für alle Vorgaben, auch H-08 bis H-23 (Controller 5, Praktiker 8).
6. **Vergleich und eingefrorener Stand:** Der Vergleich zeigt alle Blattkennzahlen und die abweichenden Eingaben. Ein Stand speichert Eingaben, Vorgaben, Katalogstand und Kernversion; ein Vergleich über Kernversionen ist zulässig und gekennzeichnet (Controller 6).
7. **Darstellung:** Summen werden aus ungerundeten Werten gebildet; wo eine Spalte gerundeter Werte nicht zur gerundeten Summe addiert, weist die Ausgabe eine Rundungsdifferenz aus (Controller 8). Jede Zeile des Finanzplans hat eine stabile Kennung; die Verdichtung nach Geschäftsjahr ist für Teil 2 vorgemerkt (Controller 9).
8. **Kennzahlenblatt:** Endwert und Endwert der Unterlassensalternative; zum tragbaren Preis Faktor, Preis je Quadratmeter, Grundstückspreis je Quadratmeter und Abstand zum Angebotspreis (Controller 10, Praktiker 10).
9. **Meldungen** sagen, was geschehen ist und was der Bearbeiter tun kann; kein Verweis auf ein Feld, das es nicht gibt (Praktiker 9). Der Referenzrechner trägt die Eingabeprüfung und alle Meldungen; der Satz „Der Kern bricht nie ab" muss dann stimmen (Grenzfälle).
10. **Referenzfälle:** Alle Eingaben jedes Referenzfalls stehen im Dokument (Anhang), jedes Beispiel ist aus dem Text nachrechenbar (Finanzmathematiker 3). `--festschreiben` schreibt nur mit Differenzbericht (Controller 7). Unabhängig bestätigt sind bisher der Ankaufsfall, der Testfall im Jahresmodus und die Anschlussfinanzierung (Finanzmathematiker); für den geförderten Neubau, die Personengesellschaft und die Privatperson im vollen Plan und die Preissuche folgt nach dieser Überarbeitung eine Blindrechnung durch einen zweiten Bearbeiter, der den Referenzrechner nicht kennt.

### B. Miete, Erträge, Verkauf

11. **Mietpfad im Bestand nach `BGB-558`:** Ziel ist die ortsübliche Vergleichsmiete (eigene Eingabe), nicht die Marktmiete; Erhöhung frühestens fünfzehn Monate nach der letzten; Kappungsgrenze gegen die Miete drei Jahre zuvor. Ist die Mietenhistorie unbekannt, gilt die vorsichtige Lesart; welche das ist, wird als neue Modellannahme gefasst (`MA-037`). Leerstehende Flächen werden zur Neuvermietungsmiete vermietet, begrenzt durch die Mietpreisbremse, wo sie gilt; Ist-Miete null führt nicht mehr zu Miete null über die Haltedauer. Fluktuation ist eine Vorgabe des Hauses, voreingestellt null. Glossar: Ist-, Soll-, Nettokalt-, Vergleichs-, Neuvermietungs- und Marktmiete. Der Widerspruch bei Anpassungsdauer null wird aufgelöst (Fachexperte 1, Praktiker 5, Grenzfälle 1 und 8).
12. **Verkaufspreis:** Der Faktor bezieht sich auf die Miete nach strukturellem Leerstand; Einstieg und Ausstieg messen dieselbe Größe; der Erbbauzins mindert den Verkaufspreis nach Faktor (Grenzfälle 2, Fachexperte 9 und 10). Ändert die Festlegung NF-23.
13. **CO2-Kosten:** Einstufung nach Kilogramm CO2 je Quadratmeter (`CO2KOSTAUFG-5` ff.); die Ableitung aus der Effizienzklasse ist eine Näherung und wird Modellannahme (`MA-035`), der Preispfad Vorgabe des Hauses; die Vermieterkosten nach `CO2KOSTAUFG-5A` kommen hinzu (Fachexperte 6).
14. **Bewirtschaftung:** Instandhaltung nach Baualter gestaffelt, Voreinstellung nach `IIBV-28` (Fachexperte 8, Praktiker 7).
15. **Neubau in der Grobform:** Baukosten werden über die Bauzeit mit der Baupreissteigerung fortgeschrieben; der Kostenkennwert gilt für die Kostengruppen 300 und 400, die übrigen Gruppen kommen als Zuschläge aus den Vorgaben; Stellplätze; Erstvermietung mit Anlaufleerstand; Bereitstellungszinsen als Vorgabe (Fachexperte 4 und 7, Bank 6).
16. **Begriffe:** „Gesamtkosten" definieren; „ohne Linie" und „Linie null" trennen; „Beleihungsauslauf" heißt, solange der Kaufpreis im Nenner steht, „Darlehen zu Kaufpreis" (beim Neubau „Darlehen zu Gesamtkosten"); zusätzlich Restschuld zum Wert am Ende der Zinsbindung (Fachexperte 10, Bank 8).

### C. Darlehen und Bankensicht

17. **KfW-Darlehen als eigene Tranche schon in der Grobkalkulation** (Neubau): Betrag bis zum Höchstbetrag je Wohneinheit, Zins, Tilgung, tilgungsfreie Anlaufjahre und Zinsbindung aus dem Katalog. Ohne sie fiel der tragbare Grundstückspreis im Fall des Praktikers um 538.626 Euro zu niedrig aus (Praktiker 1). Ändert Spezifikation Kapitel 2.
18. **Kapitaldienstfähigkeit vorsichtig:** kalkulatorischer Zins als Vorgabe des Hauses, voreingestellt der Anschlusszins und nie unter dem Vertragszins, für jede Tranche; kalkulatorische Mindesttilgung; nachhaltiger Ertrag (der kleinere aus Ist- und Vergleichsmiete) und Bewirtschaftung mindestens nach `BELWERTV-11`. Im Ankaufsfall sinkt das Bankdarlehen dadurch um 204.435 Euro (Bank 1 und 7).
19. **Deckung über die Haltedauer:** Das Blatt zeigt neben der Deckung im ersten Jahr die kleinste Deckung mit ihrem Jahr, im Basis- und im Stressfall; eigene Meldungen für „unter der Mindestdeckung" und „unter 1" (Bank 2).
20. **`MA-026` neu geschnitten:** Die Deckung rechnet immer über alle Darlehen – das ist Festlegung, keine Lesart mehr. Annahme bleibt, welche Darlehen den Beleihungsraum der Bank belegen: Das hängt am Rang; für übernommene Darlehen ist der Rang Eingabe, für das Förderdarlehen Annahme mit vorsichtiger Voreinstellung. Dazu Wertansatz und Ertragsansatz der Bank (Bank 3, Praktiker).
21. **Vorfälligkeit:** Die Restbindung endet spätestens am frühesten Kündigungstermin nach `BGB-489`; keine Vorfälligkeit für Förderdarlehen; Gewicht der Annahme mittel (Fachexperte 3, Bank 5, Grenzfälle 5).
22. **Stressfall:** Der Zinsstress trifft jede Tranche, deren Bindung vor dem Verkauf endet, auch das übernommene Darlehen; dazu Mehrkosten bei Investitionsstau und Baukosten und der Zinsanstieg bis zur Kreditzusage, mit Höhen aus den Vorgaben (Bank 4, Praktiker 6).
23. **Eigenkapitalgrenze:** Sie zählt die Einlage am Stichtag und alle Nachschüsse; der tragbare Preis darf nicht davon abhängen, in welchem Jahr dieselbe Maßnahme liegt (Praktiker 2).
24. **Ränder der Darlehensrechnung:** Zins und Tilgung null; Anschlussregel „Restlaufzeit bleibt" bei Tilgung null und bei nicht ganzzahliger Restlaufzeit; Tilgungssatz übernommener Darlehen bezogen auf den ursprünglichen Nennbetrag; Rundung der Rate bei Zins null (Grenzfälle 3, Finanzmathematiker 4, 6 und 10).
25. **Preissuche und Zielwertsuche:** Verhalten bei jeder Meldung, die in einem Suchschritt auftreten kann; ohne eingesetztes Eigenkapital gibt es keinen tragbaren Preis; Preis genau am Rand; mehrere Lösungen in einer Rasterzelle; Bereich des internen Zinsfußes. Weil die Abrundung des Gewerbeertrags die Monotonie bricht, ist der tragbare Preis der größte Preis, bis zu dem die Zielrendite für jeden kleineren Preis im Suchbereich erreicht ist; Nichtmonotonie wird gemeldet (Finanzmathematiker 2, Grenzfälle 4 und 10).
26. **Geförderter Neubau ohne Bankdarlehen:** Das Blatt zeigt die Deckung der übrigen Darlehen allein, die Reserve in Euro, den Reinertrag und die Miete je Quadratmeter, bei denen die Restfinanzierung möglich wäre, das Eigenkapital über dem Mindesteigenkapital und die Nachschüsse je Jahr. Voreinstellung der Haltedauer im geförderten Bau: Bindungsende plus ein Jahr, als Vorschlag an den Auftraggeber. Tilgungsfreie Anlaufjahre des Bankdarlehens sind für Teil 2 vorgemerkt (Praktiker 4, Bank 10).
27. **Kennzahlen aus Bankensicht** definieren: Zinsdeckung, Kapitaldienstreserve, Miete und Leerstand, bei denen die Deckung 1 erreicht, Kapitaldienst je Darlehen (Bank 9).
28. **Verlust beim Verkauf** erscheint als solcher, nicht nur als „Nachschussbedarf" (Grenzfälle 10).

### D. Steuer

29. **Erweiterte Kürzung:** Sie kürzt nur die Erträge aus Verwaltung und Nutzung des eigenen Grundbesitzes (`GEWSTG-9`); Zinserträge bleiben gewerbesteuerpflichtig, auch in der Unterlassensalternative. Für den Verkaufsgewinn ist die Lage offen: neue Modellannahme `MA-030`, voreingestellt „gewerbesteuerpflichtig" (Steuerberater 1). Ändert NF-20.
30. **Steuerstatus:** Das Kennzeichen gibt es bei der Körperschaft und bei der gewerblich geprägten Personengesellschaft, nicht beim Einzelunternehmen und nicht bei der originär gewerblichen Personengesellschaft; der Status Personengesellschaft wird geteilt (Steuerberater 2). Ändert Spezifikation Kapitel 1 und 2.
31. **15-%-Regel** (`ESTG-6`): Rechenregel statt Hinweis; Erhaltung und Modernisierung zusammen, ohne Umsatzsteuer, in den ersten drei Jahren; bei Überschreitung Herstellungskosten (Fachexperte 2, Steuerberater 3).
32. **Hinzurechnung** nach `GEWSTG-8` als Formelzeile mit Freibetrag aus dem Katalog; damit entfällt der Widerspruch zu NF-19 (Steuerberater 4).
33. **Finanzierungskosten:** im Betriebsvermögen laufzeitbezogene Entgelte verteilt (`ESTG-5`); bei der Privatperson ist die Vorfälligkeitsentschädigung beim Verkauf Veräußerungskosten. Die Modellannahme (`MA-032`) beschränkt sich auf das, was offen bleibt (Steuerberater 5).
34. **NBank-Zuschuss steuerlich:** drei Lesarten (Minderung der Abschreibungsgrundlage, sofortige Einnahme, Einnahme verteilt über die Bindung); voreingestellt ist die Lesart mit dem niedrigsten Endwert, die andere umschaltbar; Gewicht hoch (`MA-031`). Der Anteil des Zuschusses, der auf den Boden entfällt, mindert die Abschreibungsgrundlage des Gebäudes nicht. Übersteigt der Zuschuss die Kosten, gibt es eine Meldung (Steuerberater 6, Grenzfälle 9).
35. **Verlustverrechnung:** Bei der Personengesellschaft gibt es keine sofortige Erstattung der Gewerbesteuer; der Fehlbetrag wird vorgetragen (`GEWSTG-10A`). `MA-016` nennt die Annahme über andere Gewinne ausdrücklich (Steuerberater 7).
36. **Weitere Steuerstatus und Meldungen:** steuerpflichtige Körperschaft ohne Gewerbesteuer (Verein, Stiftung); bei der befreiten Genossenschaft Meldung zur 10-%-Grenze im Verkaufsjahr (`KSTG-5`); Objektverkauf der GmbH & Co. KG als laufender Gewinn oder Aufgabegewinn als Modellannahme `MA-036` (Steuerberater 8).
37. **Privatperson:** steuerpflichtiger Verkaufsgewinn wird mit Vermietungsverlust und Verlustvortrag verrechnet (`ESTG-10D`); die Frist läuft nach den Vertragsdaten (Steuerberater 9).
38. **Hinweis zur Kurzform** als Meldung mit festem Wortlaut im Annahmenblatt (Textvorschlag im Bericht des Steuerberaters), einmal und an dieser Stelle (Steuerberater 10).
39. **Abschreibung im Monatsraster:** Buchung je Planjahr wie in R-7.3; die Sollwerte des Testfalls im Monatsraster und die Gegenrechnung werden berichtigt (585.918,65 Euro; Steuer im ersten Jahr 2.933,48 Euro). Rundungsregel für Bodenwert und Abschreibungsgrundlage (Finanzmathematiker 1 und 10).

### E. Kennzahlen

40. **Gesamtkapitalrendite:** Bezugsgröße beim Neubau ist die gesamte Investition, nicht nur das Grundstück; der Satz „ohne Fremdkapital gleich der Eigenkapitalrendite" wird auf seinen Geltungsbereich beschränkt (Finanzmathematiker 5, Fachexperte 9).
41. **Renditeformel:** Der Geltungsbereich der Äquivalenz mit der Endwertdifferenz wird genau gefasst (eingezahltes Eigenkapital vorhanden, nicht beide Zähler kleiner oder gleich null) (Finanzmathematiker 9).
42. **Rundungsbeispiele** berichtigen (Finanzmathematiker 10).

### F. Verzeichnisse und Spezifikation

43. **Neue Modellannahmen** ins Verzeichnis, mit Kennung am Wirkort im Dokument: `MA-030` Gewerbesteuer auf den Verkaufsgewinn bei erweiterter Kürzung (hoch) · `MA-031` steuerliche Einordnung des Zuschusses (hoch) · `MA-032` Finanzierungskosten und Vorfälligkeit steuerlich (mittel) · `MA-033` Vorfälligkeitsentschädigung als Pauschale (mittel) · `MA-034` Prolongation mit unverändertem Tilgungssatz (gering) · `MA-035` CO2-Einstufung aus der Effizienzklasse (gering) · `MA-036` Objektverkauf der GmbH & Co. KG (mittel) · `MA-037` Kappungsspielraum bei unbekannter Mietenhistorie (mittel). `MA-026`, `MA-016` und `MA-002` (Monatsraten statt Jahresraten) werden angepasst.
44. **Quellenkataster:** `BGB-489`, `BGB-490`, `ESTG-5`, `ESTG-11`, `ESTG-20`, `ESTG-32D`, `ESTG-51A`, `GEWSTG-2`, `GEWSTG-3` neu, soweit noch nicht vorhanden; Lesedatum 18.11.2026 für die in den Prüfberichten als gelesen genannten Normen; Notiz zu `GEWSTG-36` prüfen (Wortlaut von § 9 Nr. 1 Satz 1 GewStG).
45. **Spezifikation** (`docs/spezifikation.md`) und Entscheidungsprotokoll: Steuerstatus (Punkt 30), Grobkalkulation (Punkte 17, 18, 19, 23, 25), Restwert (Punkt 12), Regionaler Schwerpunkt (Land und Gemeinde als Eingabe), Zielrendite und Schwellen (Punkt 5), Kennzahlen (Punkt 16).

## Nicht in dieser Überarbeitung

- **Landeswerte für Bremen, Hamburg, Schleswig-Holstein, Nordrhein-Westfalen** (Fachexperte 5): Die Eingabe und der Katalogschlüssel kommen jetzt (Punkt 2); die Werte selbst sind am Landesrecht zu lesen und stehen als Aufgabe in `TASKS.md`.
- **Excel-Blindrechnung und Parallelrechnung echter Projekte** (Controller 7): braucht Kalkulationen des Auftraggebers; in `TASKS.md` unter „Wartet auf Nutzer". Die Blindrechnung durch einen zweiten Bearbeiter folgt nach der Überarbeitung.
- **Verdichtung nach Geschäftsjahr, tilgungsfreie Anlaufjahre des Bankdarlehens, Disagio:** Teil 2.

## Fragen nach außen

- **Hausbank:** zehn Fragen der Rolle Bank (Rang und Beleihungsraum, Wertansatz, kalkulatorischer Zins, Ertragsansatz, Deckung, Restfinanzierung neben dem Förderdarlehen, Bereitstellungszinsen, Vorfälligkeit, Prolongation, Entgelte).
- **Steuerberater des Auftraggebers:** Kürzung auf den Verkaufsgewinn; Einordnung des NBank-Zuschusses; Vorfälligkeitsentschädigung der Privatperson; Objektverkauf der GmbH & Co. KG; Verkauf in der befreiten Genossenschaft.
- **Auftraggeber:** Werte der Vorgaben des Hauses; Fehlbetrag als Nachschuss oder Kontokorrentlinie; Haltedauer und Zielrendite im geförderten Bau; Kalkulationen für die Parallelrechnung.
