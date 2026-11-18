Rolle: Fachexperte Immobilienökonomie
Prüfobjekt: `docs/fachspezifikation-rechenkern.md` (Teil 1, Entwurf zur Prüfrunde, Stand 2026-11-18), vollständig gelesen; dazu Spezifikation Kapitel 1 bis 4 und 8, `MA-017` und `MA-026`, Quellnotiz 10, Bericht Abschnitt 5 und Anhang D (Auszüge), Quellenkataster (Einträge der genannten Kennungen)

Gesamturteil: Mit Auflagen tragfähig. Der Aufbau des Finanzplans, die Lehrbuchansicht, die Unterlassensalternative und die Kennzahlen Endwertdifferenz, VOFI-Rendite und Gesamtkapitalrendite entsprechen Lehrbuch und Lexikon. Die Ertragsseite der Grobkalkulation bildet das Mietrecht aber an einer tragenden Stelle falsch ab: Erhöhungsziel ist die Marktmiete statt der ortsüblichen Vergleichsmiete, und die Kappungsgrenze wird als „vorsichtig“ bezeichnet, obwohl sie günstig gerechnet ist. Dazu kommen zwei gesetzliche Regeln, die das Dokument nur als Hinweis führt oder gar nicht kennt (anschaffungsnahe Herstellungskosten, Kündigungsrecht nach zehn Jahren), und die Neubau-Grobform rechnet die Baukosten über die Bauzeit ohne Preissteigerung.

Note: 7 von 10. Zur 9 fehlen:
- im Dokument zu beheben: Befunde 1 bis 4 und 7 bis 10 (Mietpfad auf die Vergleichsmiete mit vorsichtiger Kappung und Wartefrist, § 6 Abs. 1 Nr. 1a EStG als Regel, Vorfälligkeit höchstens bis zum Kündigungsrecht nach § 489 BGB, Baukosten mit Preissteigerung, Bezugsgrößen der Neubau-Kennzahlen, Begriffe);
- mit Arbeit am Kataster zu beheben: Befund 5 (Länderwerte für vier Länder) und der CO2-Bezug in Befund 6 (Modellannahme anlegen);
- Auskunft von außen braucht keiner der Befunde zwingend. Hausbank (Vorfälligkeit in der Praxis) und Steuerberater (die schon vorgeschlagenen Annahmen in Kapitel 17) bestätigen nur.

Was trägt (nachgeprüft, kein Befund):
- **Finanzplan und Lehrbuchansicht (R-4.1, R-4.7):** Die Gliederung in originäre und derivative Zahlungen, der Ausgleich je Periode und die Zuordnung der Konten zur einjährigen Reinvestition und Zwischenfinanzierung entsprechen dem Lehrbuch (Quellnotiz 11). Die Abbildung in R-4.7 ist vollständig, auch für Beitrag, Vorfälligkeit und einbehaltene Beträge.
- **Mietausfall als Erlösminderung (NF-13):** Er entspricht der gif- und ImmoWertV-Systematik (Sollmiete, dann Ausfall, dann Einzahlung). Dass `IIBV-29` nur als Voreinstellung der Quote dient, verhindert eine Doppelzählung.
- **Nettoanfangsrendite, Faktor und Schuldendienstdeckung (R-8.1, R-8.2, R-10.13, R-10.14, NF-30):** Die Bezugsbasen entsprechen der Spezifikation (Zeile „Restwert“) und der Bankpraxis. Ablösung, Vorfälligkeit und freie Tilgung gehören zu Recht nicht in den Kapitaldienst.
- **Gesamtkapitalrendite (R-10.11):** Die Formel entspricht dem Lexikoneintrag in Quellnotiz 10 (Z_S schon nach Steuern, Referenzzinsfuß aus der Alternative); zur Bezugsgröße im Neubau siehe Befund 9.
- **Restwert bei laufender Bindung (R-8.7, R-8.8):** Das ist mit `MA-017` stimmig (die Bindung läuft bei Rückzahlung fort), also keine Doppelzählung.
- **Kappungsformel (R-6.3):** Die Basis „Miete drei Jahre zuvor“ trifft § 558 Abs. 3 BGB.
- **Abschreibungssatz nach Fertigstellung (KAT-07):** Er trifft § 7 Abs. 4 EStG.
- **Private Veräußerung (R-7.11):** Steuerpflicht bei n = 10 ist nach § 23 EStG („nicht mehr als zehn Jahre“) richtig.

Am Original gelesen (2026-11-18, gesetze-im-internet.de, ISO-8859-1):
- `BGB-558`: Abs. 1 bis 6, Fassung wie im Kataster. Bestätigt: Erhöhung „bis zur ortsüblichen Vergleichsmiete“, 15 Monate Wartefrist, Verlangen frühestens ein Jahr nach der letzten Erhöhung, 20 % beziehungsweise 15 % in drei Jahren.
- `ESTG-6`: Abs. 1 Nr. 1a. Bestätigt: Instandsetzung und Modernisierung binnen drei Jahren, Grenze 15 % der Gebäudeanschaffungskosten ohne Umsatzsteuer, ausgenommen jährlich übliche Erhaltung.
- `ESTG-7`: Abs. 4. Bestätigt: 3 % nach 31.12.2022, 2 % 1925 bis 2022, 2,5 % vor 1925.
- **§ 489 BGB, nicht im Kataster:** Abs. 1 Nr. 2: Kündigungsrecht „in jedem Fall nach Ablauf von zehn Jahren nach dem vollständigen Empfang“ mit sechs Monaten Frist. Für Befund 3 neu ins Kataster aufzunehmen (Kennung etwa `BGB-489`).

Befunde

1. [kritisch · belegt] **R-6.3, R-6.6, NF-12, NF-14, E-16 – Der Mietpfad im Bestand zielt auf die Marktmiete statt auf die ortsübliche Vergleichsmiete und ist günstiger gerechnet als angegeben.**
   (a) Zum Ziel: § 558 Abs. 1 BGB erlaubt beim Bestandsmieter die Erhöhung nur „bis zur ortsüblichen Vergleichsmiete“ (am Original gelesen). Der Bericht unterscheidet das selbst (Abschnitt 5, Nr. 5: Bestandsmieter auf die Vergleichsmiete, Neuvermietung auf die Marktmiete). Die Fachspezifikation kennt das Wort „Vergleichsmiete“ nicht. E-16 heißt „Marktmiete“, und R-6.6 führt nach Bindungsende mit Verweis auf `BGB-558` zur Marktmiete. Wer als Marktmiete die Angebotsmiete aus einem Portal einträgt, und das legt der Name nahe, überzeichnet in Hannover oder Hamburg die erreichbare Bestandsmiete erfahrungsgemäß deutlich (begründete Einschätzung zur Höhe). Das hebt Reinertrag, Verkaufspreis (Faktor auf die Sollmiete) und tragbaren Preis.
   (b) Zur Basis: R-6.3 setzt für j ≤ 3 die Ist-Miete als Basis der Kappung und nennt das „die vorsichtige Wahl“. Das stimmt nicht. Maßgeblich ist die Miete drei Jahre vor der Erhöhung, und die ist höchstens gleich der Ist-Miete. Wurde die Ist-Miete kurz vor dem Stichtag erhöht, ist der Spielraum kleiner als gerechnet. Die Ist-Miete als Basis ist damit die günstigste Annahme.
   (c) Zur Wartefrist: Der Pfad erhöht in jedem Planjahr; die Wartefrist von 15 Monaten erlaubt das nicht. Die Erhöhung schon zu Beginn von Jahr 2 setzt außerdem voraus, dass die letzte Erhöhung mindestens zwei Monate vor dem Stichtag lag.
   Vorschlag:
   - E-16 beim Ankauf als „ortsübliche Vergleichsmiete“ führen, beim Neubau als „Erstvermietungsmiete“; die Neuvermietungsmiete kommt mit der Fluktuation in 1b-1.
   - In R-6.6 das Ziel nach Bindungsende auf die Vergleichsmiete setzen.
   - Die Kappung für j ≤ 3 vorsichtig rechnen: Spielraum erst ab Jahr 4, oder eine Eingabe „Jahr der letzten Erhöhung“ mit Voreinstellung „unmittelbar vor dem Stichtag“.
   - Im Monatsraster Erhöhungsschritte frühestens alle 15 Monate setzen.
   - Bleibt NF-12 vereinfacht, braucht der Pfad eine Modellannahme mit der anderen Lesart; die jetzige Lesart ist nicht die vorsichtige.

2. [wichtig · belegt] **R-6.10, NF-15, M-36 – Anschaffungsnahe Herstellungskosten sind gesetzliche Regel, nicht Hinweis, und der Auslöser ist falsch gefasst.**
   - Nach § 6 Abs. 1 Nr. 1a EStG (am Original gelesen) gehören Instandsetzungs- und Modernisierungsaufwendungen binnen drei Jahren nach Anschaffung zu den Herstellungskosten, wenn sie ohne Umsatzsteuer 15 % der Gebäudeanschaffungskosten übersteigen.
   - Die Kurzform lässt Erhaltung trotzdem sofort abziehen und meldet nur M-36. Der Auslöser zählt nur Erhaltungsmaßnahmen und brutto. Das Gesetz zählt Erhaltung und Modernisierung zusammen, netto.
   - Gerade beim Ankauf mit Investitionsstau, dem Kernfall der Pauschalen, wird die Grenze häufig überschritten. Der Sofortabzug rechnet die Rendite nach Steuern dann zu gut. Das widerspricht der Vorsichtsregel und dem Grundsatz „keine stille Lesart“.
   - Die Regel ist mit den vorhandenen Eingaben (E-50 bis E-52, Abschreibungsgrundlage nach R-7.3) in einer Zeile rechenbar.
   - Vorschlag: In R-6.10 als Rechenregel fassen. Summe aller Maßnahmen mit k ≤ 3, netto (Kennzeichen oder Umsatzsteuersatz aus dem Katalog), gegen 15 % der Gebäudeanschaffungskosten. Bei Überschreiten werden die Erhaltungsmaßnahmen dieser Jahre aktiviert und wie Modernisierung abgeschrieben. M-36 meldet dann, dass aktiviert wurde. NF-15 entsprechend ändern.

3. [wichtig · belegt] **R-5.16, NF-10 – Die Vorfälligkeitsentschädigung übersieht das gesetzliche Kündigungsrecht nach zehn Jahren.**
   - § 489 Abs. 1 Nr. 2 BGB (am Original gelesen; nicht im Kataster) erlaubt dem Darlehensnehmer bei gebundenem Sollzins die Kündigung „in jedem Fall nach Ablauf von zehn Jahren nach dem vollständigen Empfang“ mit sechs Monaten Frist.
   - R-5.16 rechnet die Pauschale über die ganze Restbindung, und E-46 lässt Bindungen bis 40 Jahre zu.
   - Szenario: Ankauf mit 20 Jahren Zinsbindung, Verkauf nach 12 Jahren. R-5.16 setzt 8 Jahre x H-18 x Restschuld an, rechtlich ist keine Entschädigung geschuldet.
   - Szenario: Verkauf nach 5 Jahren. Angesetzt werden 15 Jahre statt höchstens rund 5,5 Jahre bis zum frühesten Kündigungstermin.
   - Das verzerrt die Haltedauertabelle (R-11.13) und die Wahl der Zinsbindung, also genau die Entscheidung, die das Werkzeug stützen soll.
   - Vorschlag: Restbindung für die Pauschale = min(Bindungsende; Monat der vollständigen Auszahlung + 120 + 6) − N, nicht unter null. Gilt für Bankdarlehen und übernommene Darlehen (E-59, Beginn mit der letzten Zinsvereinbarung, § 489 Abs. 1 Nr. 2 Halbsatz 2). `BGB-489` ins Kataster aufnehmen. M-25 nur auslösen, wenn tatsächlich Vorfälligkeit anfällt.

4. [wichtig · belegt] **R-2.5 (Zeile Baukosten), R-11.2, R-11.3 – Die Baukosten laufen über die Bauzeit ohne Preissteigerung.**
   - Der Kostenkennwert hat den Preisstand des Stichtags und ist „in 1a nicht indexiert“, obwohl H-14 Baupreissteigerung vorhanden ist. DIN 276 verlangt für jede Kostenermittlung die Angabe des Kostenstands. Ein Kennwert zum heutigen Preisstand ist auf die Ausführung fortzuschreiben (Praxis der BKI-Kennwerte, begründete Einschätzung).
   - Gegenrechnung RF-12: 7.540.000 Euro in 18 gleichen Monatsraten, monatlich mit 3 % je Jahr fortgeschrieben: 179.152 Euro oder 2,38 % mehr. Bei 36 Monaten Bauzeit gut das Doppelte.
   - Der Fehler liegt auf der günstigen Seite und steckt im Basisfall. Der Stressaufschlag von 5 % (R-11.8) wird so zur Hälfte verbraucht.
   - Vorschlag: Monatsrate m = runde(Rate zum Stichtag x (1 + H-14)^(m / 12)). Alternativ die Eingabe „Kostenstand des Kennwerts“ und fortschreiben bis zur Rate. In R-2.5 und R-11.3 nachtragen, P-04 bleibt unverändert.

5. [wichtig · belegt] **R-3.5, KAT-01 und KAT-08 – Die Länderwerte fehlen für vier der fünf Länder, entgegen einer festen Festlegung.**
   - Spezifikation Kapitel 1, „Regionaler Schwerpunkt“ (fest): Für alle fünf Länder führt der Katalog von Anfang an Grunderwerbsteuersatz, Gebiete mit Mietpreisbremse und abgesenkter Kappungsgrenze.
   - KAT-01 nennt „übrige Länder offen“, KAT-08 nur `NI-MIETERSCHUTZVO`.
   - Im Kataster gibt es keinen Eintrag für die Verordnungen und Steuersätze von Hamburg, Bremen, Schleswig-Holstein und Nordrhein-Westfalen (Suche nach Kappung, Mietpreisbremse, GrESt). Auch `NI-GREST-SATZ` und `NI-MIETERSCHUTZVO` sind nur sekundär oder nicht geprüft.
   - Ein Ankauf in Hamburg oder Köln ist damit in 1a nicht belegbar rechenbar.
   - Vorschlag: Je Land Grunderwerbsteuersatz und Kappungsgrenzenverordnung (mit Geltungsdauer, § 558 Abs. 3 Satz 3: höchstens fünf Jahre) ins Kataster aufnehmen und am Original lesen. KAT-08 je Gemeinde mit Gültigkeitszeitraum führen, weil eine auslaufende Verordnung innerhalb der Haltedauer die Kappung von 15 % auf 20 % ändert. Ob ein Land derzeit eine Verordnung hat, ist dabei am Original zu prüfen, nicht aus dem Gedächtnis.

6. [wichtig · begründete Einschätzung] **R-6.9, KAT-09, E-54, E-55 – Die CO2-Kosten vermischen Recht, Prognose und Näherung, ohne Modellannahme.**
   - Das Stufenmodell nach `CO2KOSTAUFG-5` und Anlage stuft nach kg CO2 je m² und Jahr ein (Kataster: am Original gelesen). Die Fachspezifikation fragt Effizienzklasse und Energieträger ab. Die Effizienzklasse beruht auf dem Endenergiebedarf, nicht auf dem CO2-Ausstoß.
   - Die Zuordnung Klasse und Träger zu kg CO2 und dann zum Vermieteranteil ist eine Näherung. Die „Steigerung“ in KAT-09 ist eine Preisprognose für CO2, kein Katalogwert mit Quelle.
   - Beides kann sich als falsch erweisen und gehört nach Spezifikation Kapitel 8 in eine Modellannahme beziehungsweise eine Vorgabe des Hauses.
   - Außerdem fehlen die übrigen nicht umlagefähigen Vermieterkosten nach `CO2KOSTAUFG-5A` (Gasnetzentgelte, Bio-Brennstoffanteil). Die Spezifikation verlangt beim Ankauf die CO2-Kosten „nach `CO2KOSTAUFG-5` bis `CO2KOSTAUFG-5D`“, also einschließlich 5a und 5b.
   - Vorschlag: Freiwillige Eingabe „CO2-Ausstoß kg je m² und Jahr“ (aus der Heizkostenabrechnung, die der Vermieter ohnehin hat), sonst Näherung aus Klasse und Träger mit neuer Modellannahme und vorsichtiger Voreinstellung (obere Klassengrenze). CO2-Preispfad als Vorgabe des Hauses, H-24. Kosten nach 5a als eigene Zeile oder ausdrücklich nach 1b-1 verweisen. 5b (Neubau mit fossiler Heizung) in R-6.7 erwähnen oder ausschließen.

7. [wichtig · begründete Einschätzung] **E-25, NF-38, R-6.7 – Die Neubau-Grobform hat drei fachliche Lücken, die das indikative Grundstücksgebot nach oben verschieben.**
   (a) Kostenkennwert: Ein einziger Kennwert „Kostengruppen 200 bis 700 je m² BGF“ ist unüblich. Die gängigen Kennwerte (BKI) werden für die Kostengruppen 300 und 400 je m² BGF veröffentlicht; 200, 500, 600 und vor allem 700 (Baunebenkosten, üblich ein Fünftel bis ein Viertel von 300 und 400) kommen getrennt oder als Zuschlag hinzu. Wer den veröffentlichten Kennwert einträgt, unterschlägt rund ein Viertel der Kosten. Vorschlag: E-25 als Kennwert 300 und 400 je m² BGF, dazu Zuschläge für 200, 500, 600 in Euro oder Prozent und 700 in Prozent von 300 und 400 als Vorgabe des Hauses. Die Summe bleibt die Bemessung nach R-11.14.
   (b) Stellplätze: Tiefgaragen- und Stellplatzkosten stecken je nach Lesart im BGF-Kennwert, ihre Erlöse fehlen. Beide Regelwerke für H-17 führen eigene Stellplatzwerte (`IMMOWERTV-ANLAGE-3`, Quellnotiz 10). Vorschlag: In 1a mindestens Anzahl, Kosten und Miete je Stellplatz, oder ausdrücklich „BGF ohne Garage“ festlegen und M-Hinweis. Der Bericht legt Nebenerlöse zwar in 1b, die Kosten aber nicht.
   (c) Erstvermietung: Die volle Miete ab dem Monat nach der Bauzeit ist die günstigste Lesart. Vorschlag: Vorgabe des Hauses „Leerstandsmonate bei Erstvermietung“ mit Voreinstellung über null; sie wirkt nicht auf RE_VJ für die Bank, aber auf den Finanzplan.

8. [Hinweis · belegt] **R-6.8, H-17 – Die Instandhaltung wird über die ganze Haltedauer altersunabhängig gerechnet.**
   - H-17 nennt `IIBV-28` als Quelle der Voreinstellung. Dessen Pauschale steigt nach Gebäudealter (Kataster: 7,10 / 9,00 / 11,50 Euro je m² als Basis). Beim Neubau über 42 Jahre (RF-14) und beim Ankauf eines Gebäudes kurz vor der Altersschwelle bleibt die Stufe unberücksichtigt.
   - Die Instandhaltung ist zugleich die einzige Kostengröße im Stresstest.
   - Vorschlag: Instandhaltung je m² je Altersstufe aus dem Katalog, Stufe nach Baujahr (E-17) beziehungsweise Fertigstellung und Planjahr. Bei eigenen Werten des Hauses gilt ein fester Satz.

9. [Hinweis · begründete Einschätzung] **R-10.11, R-10.13, NF-23, NF-28 – Bezugsgrößen der Kennzahlen im Neubau und beim Ausstieg sind unscharf.**
   (a) R-10.11 setzt a_0 als „Anschaffungsauszahlung zum Stichtag“. Beim Neubau ist das nur der Grundstückskauf; die Gesamtkapitalrendite wäre dann grob überzeichnet. a_0 für die Investitionsphase festlegen, etwa die Investitionsauszahlungen bis zum Ende der Bauzeit auf den Stichtag abgezinst mit w nach R-10.4, und `MA-028` ergänzen.
   (b) R-10.13 nimmt im Neubau beim Faktor „Gesamtkosten ohne Bauzeitzinsen“, bei der Nettoanfangsrendite nur „Gesamtkosten“, und „Gesamtkosten“ steht in keinem Glossar. Definieren (Grundstück, Nebenkosten, Kostengruppen 200 bis 700, mit oder ohne Bauzeitzinsen und Entgelte) und die Neubaugröße als „Anfangsrendite auf Gesamtkosten“ bezeichnen, wie in der Projektentwicklung üblich.
   (c) NF-23: Der Ausstieg nimmt die Sollmiete der zwölf Monate nach dem Verkauf. Der Mietindex springt nach R-6.1 genau am Verkaufsstichtag, der Einstieg (Planjahr 1, Index 1) dagegen nicht. In RF-11 macht der eine Indexschritt 65.230 Euro des Verkaufspreises aus (3.326.730,48 gegen 3.261.500,47 Euro bei Miete des Jahres 12). Der Vergleich von Einstiegs- und Ausstiegsfaktor in der Warnschwelle H-20 misst damit nicht gleich. Vorschlag: Ausstieg auf die am Verkaufsstichtag geltende Miete mal zwölf, symmetrisch zum Einstieg, oder die Asymmetrie in NF-23 begründen und beim Faktorvergleich bereinigen.

10. [Hinweis · belegt] **R-1.1, R-4.5, R-10.15, R-6.11 – Begriffe, die ein Entwickler oder Fachautor falsch lesen kann.**
    - Ist-Miete, Marktmiete, Sollmiete und Nettokaltmiete fehlen im Glossar. Es ist nirgends gesagt, dass alle Mieteingaben Nettokaltmieten ohne Betriebskostenvorauszahlung sind, obwohl die Spezifikation den Faktor auf die Jahresnettokaltmiete bezieht.
    - R-4.5 sagt „Ohne Linie (Lehrbuchfälle) ist der Kontokorrent unbegrenzt“ und „Voreingestellt ist die Linie null“. „Ohne Linie“ und „Linie null“ bedeuten dort das Gegenteil. Vorschlag: „unbegrenzt“ als eigener Wert von H-11.
    - „Beleihungsauslauf“ (R-10.15) bezeichnet in der Bankpraxis das Darlehen im Verhältnis zum Beleihungswert. Mit dem Kaufpreis als Wertansatz (`MA-026`) ist es ein Darlehens-Kaufpreis-Verhältnis (LTV). Vorschlag: „Fremdkapitalquote auf den Wertansatz“, oder die Bezeichnung erst, wenn ein Beleihungswert eingegeben ist.
    - Beim Erbbaurecht (R-6.11) mindert der Erbbauzins den Reinertrag, nicht aber den Verkaufspreis nach Faktor (R-8.1). Der Ausstieg wird überzeichnet, wenn der Anwender den Faktor nicht selbst senkt. Vorschlag: Hinweis an E-47, sobald E-62 > 0. Die Restlaufzeit des Erbbaurechts gehört in das volle Modell (Spezifikation, „Erbbaurecht“, vorläufig).

Zu den 38 neuen Festlegungen im Überblick:
- **Zu ändern:** NF-12 und NF-14 (Befund 1), NF-15 (Befund 2), NF-10 (Befund 3), NF-38 (Befund 7).
- **Zu präzisieren:** NF-23 und NF-28 (Befund 9).
- **Modellannahme statt Festlegung:** CO2-Zuordnung in R-6.9 (Befund 6). Bleibt NF-12 vereinfacht, gilt das auch für den Mietpfad.
- **Fachlich üblich und tragfähig:** NF-02, NF-06, NF-07 (mit der vorgeschlagenen Annahme), NF-13, NF-30, NF-31, NF-32, NF-33 und NF-35. NF-32 ist für das Eigenkapital vorsichtig. Eigenkapital zuerst (NF-33) entspricht der Bankauflage.
- **Steuerfestlegungen NF-16 bis NF-22:** Fachlich nur so weit gesehen, wie sie meine Rolle berühren. Die vorgeschlagenen Modellannahmen in Kapitel 17 decken sie.

Fehlende Eingaben und Vorgaben: Vergleichsmiete statt Marktmiete und Jahr der letzten Erhöhung (Befund 1), Netto-Kennzeichen für Maßnahmen (Befund 2), CO2-Ausstoß und CO2-Preispfad (Befund 6), Zuschläge der Kostengruppen, Stellplätze und Erstvermietungsleerstand (Befund 7), Instandhaltung je Altersstufe (Befund 8). Überflüssige Eingaben habe ich nicht gefunden.

Nicht geprüft:
- **Rechengenauigkeit und Referenzrechner:** Das prüft eine andere Rolle; ich habe nur die beiden Gegenrechnungen in Befund 4 und 9 selbst gerechnet.
- **Steuerlogik im Einzelnen (Kapitel 7):** Gewerbesteuer, Anrechnung und Verlustvortrag gehören zu Steuerberater und Finanzmathematiker.
- **NBank-Grobförderung (R-11.14):** Nur gegen den Bericht Anhang D geprüft, nicht gegen `NBANK-RL-MIETWOHNRAUM-2026` am Original.
- **DIN 276 und 277 und der gif-Kennzahlenkatalog:** Nicht am Original, weil nicht frei zugänglich (Kataster: nur Sekundärquelle). Die Aussagen zu den Kostengruppen in Befund 7 sind deshalb begründete Einschätzung.
- **Länderverordnungen für Befund 5:** Nicht gesucht, weil nicht meine Aufgabe; ich habe nur festgestellt, dass sie im Kataster fehlen.
