# Modellannahmen

Verzeichnis der Annahmen über Recht, Förderpraxis und Methode, die sich vor dem Bau nicht klären lassen und auf denen das Modell trotzdem rechnet. Leser: Auftraggeber, Entwicklung, Prüfer. Die Regeln dazu stehen in `docs/spezifikation.md`, Kapitel „Modellannahmen“.

**Diese Datei wird erzeugt.** Gepflegt wird `docs/modellannahmen/annahmen.toml`; danach `python3 scripts/modellannahmen.py` ausführen.

**Stand:** 36 offene Annahmen, davon 8 mit hohem Gewicht · 5 erledigt

## Offene Annahmen

| Kennung | Thema | Gewicht | Sichtbar | Umschaltbar | Klärung durch | Wiedervorlage |
|---|---|---|---|---|---|---|
| `MA-001` | Rechenweise der NBank-Renditeprüfung | hoch | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-004` | KfW-Darlehen als Ersatz für Eigenmittel bei der NBank | hoch | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-012` | Rendite bei mehreren Einlagen und Entnahmen | hoch | Kundenbericht | nein | Fachliteratur: Ropeter (1998), S. 186 ff. (`ROPETER-1998`); fachliche Freigabe durch den Auftraggeber | mit der Fachspezifikation des Rechenkerns (Phase 1) |
| `MA-014` | Streuungen und Korrelationen der Simulation | hoch | Kundenbericht | ja | Auftraggeber (eigene Erfahrungswerte); später Marktdaten | vor Stufe 2 (Simulation) |
| `MA-016` | Verrechnung von Anlaufverlusten | hoch | Kundenbericht | ja | Anwender je Vorhaben; im Zweifel Steuerberater des Investors | mit der Fachspezifikation des Steuermoduls (Phase 1) |
| `MA-026` | Rechengrundlage des Bankdarlehens | hoch | Kundenbericht | ja | Hausbank (13 Fragen in der Fachspezifikation des Rechenkerns, Kapitel 16); die Schwellen selbst (Beleihungsquote, Mindestdeckung, Mindesttilgung, kalkulatorischer Zins je Tranchenart, Bemessungszeitraum, Mindestansatz der Bewirtschaftung) sind Vorgaben des Hauses | mit den Vorgaben des Hauses vor dem Einsatz von Teilschritt 1a |
| `MA-030` | Gewerbesteuer auf den Verkaufsgewinn bei erweiterter Kürzung | hoch | Kundenbericht | ja | Steuerberater des Auftraggebers | mit der Antwort des Steuerberaters; spätestens vor dem Einsatz von Teilschritt 1a |
| `MA-031` | Steuerliche Einordnung des NBank-Zuschusses | hoch | Kundenbericht | ja | Steuerberater des Auftraggebers; zur Praxis der Bewilligung die NBank | mit der Antwort des Steuerberaters; spätestens vor dem Förderteil (1c) |
| `MA-007` | Dauer des Drittmittelabzugs bei Mieterhöhungen auf die Vergleichsmiete | mittel | Kundenbericht | ja | Anwalt (nur noch: gilt die Frist von zwölf Jahren beim Umlagesatz von 8 % fort?) | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-017` | Restwert bei laufender Bindung | mittel | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-032` | Finanzierungskosten und Vorfälligkeit in der Steuer | mittel | Anwendung | ja | Steuerberater des Auftraggebers | mit der Antwort des Steuerberaters; mit der Steuer in Grundform (Teil 2 der Fachspezifikation) |
| `MA-033` | Vorfälligkeitsentschädigung als Pauschale | mittel | Anwendung | nein | Hausbank | nach dem Gespräch mit der Hausbank; Zinsschadenrechnung mit der Vollkalkulation (Teil 2 der Fachspezifikation) |
| `MA-034` | Prolongation mit unverändertem Tilgungssatz | mittel | Anwendung | ja | Hausbank | nach dem Gespräch mit der Hausbank |
| `MA-036` | Objektverkauf der GmbH & Co. KG: laufender Gewinn oder Aufgabegewinn | mittel | Anwendung | ja | Steuerberater des Auftraggebers | mit der Antwort des Steuerberaters; mit der Steuer in Grundform (Teil 2 der Fachspezifikation) |
| `MA-037` | Kappungsspielraum bei unbekannter Mietenhistorie | mittel | Anwendung | ja | Anwender je Vorhaben (Mieterliste des Verkäufers) | mit der Mieterliste der Vollkalkulation Ankauf Bestand (1b-1) |
| `MA-039` | Fortgeltung der Gebietsverordnungen zu Kappungsgrenze und Mietpreisbremse | mittel | Anwendung | ja | Land als Verordnungsgeber; Beobachtung über den Katalog | mit jeder neuen Gebietsverordnung des Landes; spätestens 2029 |
| `MA-040` | Beginn der tilgungsfreien Jahre des KfW-Darlehens | mittel | Anwendung | ja | Hausbank; KfW | nach dem Gespräch mit der Hausbank; mit dem Lesen der Konditionenübersicht der KfW |
| `MA-002` | Tilgungsplan des NBank-Darlehens | gering | Anwendung | ja | NBank | nach dem Gespräch mit der NBank; im Einzelfall der Bewilligungsbescheid |
| `MA-003` | Zins des NBank-Darlehens ab dem 36. Jahr | gering | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-005` | Finanzierungskosten als zuwendungsfähige Kosten der NBank | gering | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-006` | Aufteilung bei teilgeförderten Vorhaben | gering | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-008` | Modernisierungsumlage für den Heizungstausch bei Staffelmiete | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-009` | Teilung der Bio-Brennstoffkosten im Neubau | gering | nur intern | nein | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-011` | Bagatellgrenze bei der Umsatzsteueroption | gering | Anwendung | ja | Steuerberater | vor Stufe 3 (Gewerbe) |
| `MA-013` | Rundung in Darlehensplänen | gering | nur intern | ja | Darlehensvertrag im Einzelfall | bei der ersten Parallelrechnung mit echten Darlehen (Abnahme Stufe 1) |
| `MA-015` | Modernisierungsumlage im Referenzfall IWU 2013 | gering | nur intern | nein | Fachliteratur (Endbericht im Volltext) | beim Anlegen des Abnahmetests (Phase 3) |
| `MA-018` | Ersatz eines Gaskessels als energetische Modernisierung | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-019` | Zinsverbilligte Darlehen bei der Umlage für den Heizungstausch | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-020` | Umlage für den Heizungstausch in der NBank-Bindung | gering | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-024` | Zeitlicher Anwendungsbereich des Wärmepumpen-Nachweises | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-025` | Modernisierungsumlage für den Glasfaseranschluss | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-027` | Rechenregel der VOFI-Amortisationsdauer | gering | Anwendung | ja | Fachliteratur (Grob, Einführung in die Investitionsrechnung) oder ein Hochschulskript, das die Regel wiedergibt | mit der Fachspezifikation des Kennzahlenblatts (Spezifikation Kapitel 3) |
| `MA-028` | Zuzurechnende Sollzinsen in der VOFI-Gesamtkapitalrentabilität | gering | Anwendung | nein | Fachliteratur: Grob, Einführung in die Investitionsrechnung, nach `SCHULTE-IMMOBILIENINVESTITION-2025` (S. 813) dort S. 140 f. | mit der Fachspezifikation des Kennzahlenblatts (Spezifikation Kapitel 3) |
| `MA-035` | CO2-Einstufung aus der Effizienzklasse | gering | Anwendung | nein | Anwender je Vorhaben (Heizkostenabrechnung des Verkäufers) | mit der Vollkalkulation Ankauf Bestand (1b-1) |
| `MA-038` | Rückführung einer Miete über der Vergleichsmiete | gering | Anwendung | ja | Auftraggeber (Erfahrung aus dem Bestand) | mit den Vorgaben des Hauses vor dem Einsatz von Teilschritt 1a |
| `MA-041` | Vermietung von Verein und Stiftung als Vermögensverwaltung | gering | Anwendung | nein | Steuerberater des Auftraggebers | mit der Antwort des Steuerberaters |

Nach Klärungsweg:

- **Anwalt:** `MA-008`, `MA-009`, `MA-018`, `MA-019`, `MA-024`, `MA-025`
- **Anwalt (nur noch: gilt die Frist von zwölf Jahren beim Umlagesatz von 8 % fort?):** `MA-007`
- **Anwender je Vorhaben (Heizkostenabrechnung des Verkäufers):** `MA-035`
- **Anwender je Vorhaben (Mieterliste des Verkäufers):** `MA-037`
- **Anwender je Vorhaben; im Zweifel Steuerberater des Investors:** `MA-016`
- **Auftraggeber (Erfahrung aus dem Bestand):** `MA-038`
- **Auftraggeber (eigene Erfahrungswerte); später Marktdaten:** `MA-014`
- **Darlehensvertrag im Einzelfall:** `MA-013`
- **Fachliteratur (Endbericht im Volltext):** `MA-015`
- **Fachliteratur (Grob, Einführung in die Investitionsrechnung) oder ein Hochschulskript, das die Regel wiedergibt:** `MA-027`
- **Fachliteratur: Grob, Einführung in die Investitionsrechnung, nach `SCHULTE-IMMOBILIENINVESTITION-2025` (S. 813) dort S. 140 f.:** `MA-028`
- **Fachliteratur: Ropeter (1998), S. 186 ff. (`ROPETER-1998`); fachliche Freigabe durch den Auftraggeber:** `MA-012`
- **Hausbank:** `MA-033`, `MA-034`
- **Hausbank (13 Fragen in der Fachspezifikation des Rechenkerns, Kapitel 16); die Schwellen selbst (Beleihungsquote, Mindestdeckung, Mindesttilgung, kalkulatorischer Zins je Tranchenart, Bemessungszeitraum, Mindestansatz der Bewirtschaftung) sind Vorgaben des Hauses:** `MA-026`
- **Hausbank; KfW:** `MA-040`
- **Land als Verordnungsgeber; Beobachtung über den Katalog:** `MA-039`
- **NBank:** `MA-001`, `MA-002`, `MA-003`, `MA-004`, `MA-005`, `MA-006`, `MA-017`, `MA-020`
- **Steuerberater:** `MA-011`
- **Steuerberater des Auftraggebers:** `MA-030`, `MA-032`, `MA-036`, `MA-041`
- **Steuerberater des Auftraggebers; zur Praxis der Bewilligung die NBank:** `MA-031`

## Einzelheiten

### MA-001 · Rechenweise der NBank-Renditeprüfung

- **Annahme:** Das Werkzeug weist die Eigenkapitalrendite für die Überkompensationsprüfung aus dem eigenen Finanzplan des Vorhabens aus und vergleicht sie mit dem 30-Jahres-Swapsatz zuzüglich 100 Basispunkten; Bewirtschaftungskosten, Mietsteigerung, Restwert und Betrachtungszeitraum folgen den Annahmen des Vorhabens.
- **Warum offen:** Die Richtlinie nennt Verfahren und Schwelle, die NBank veröffentlicht aber weder ihre Rechenannahmen noch ein Rechenblatt.
- **Andere Lesart:** Die NBank rechnet mit eigenen Pauschalen (etwa nach II. BV), ohne Restwert oder über einen festen Zeitraum; dann weicht ihre Rendite von der des Werkzeugs ab.
- **Grundlage:** Richtlinie Mietwohnraum 2026, Nummern 5.3.7 und 11.10. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`.
- **Wirkung (hoch):** Aussage, ob die Förderung als angemessen gilt oder gekürzt wird; trägt den Nutzen des Werkzeugs im Fördergeschäft.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, NBank-Renditeprüfung
- **Bemerkung:** Bis zur Klärung wird die Kennzahl als eigene Berechnung des Werkzeugs bezeichnet, nicht als Ergebnis der NBank-Prüfung.

### MA-002 · Tilgungsplan des NBank-Darlehens

- **Annahme:** Das zinslose Darlehen wird in gleichbleibenden Raten im Takt des Rechenrasters getilgt, im Monatsraster also monatlich.
- **Warum offen:** Beginn und Ende der Tilgung stehen in der Richtlinie: Beginn am Monatsersten nach der vollständigen Auszahlung, spätestens zwei Jahre nach dem Monat, der auf die Förderentscheidung folgt; Rückzahlung längstens 42 Jahre nach Bezugsfertigkeit; Aufschub des Beginns um bis zu fünf Jahre. Offen ist nur die Form der Raten: Die Modalitäten setzt die NBank fest. Nachtrag 2026-11-18: Auch die Produktinformation (Stand 05.11.2026) nennt keinen Tilgungssatz, nur die Rückzahlung nach längstens 42 Jahren. Eine ältere Produktinformation nach den Bestimmungen von 2024 nannte 1,25 % und ab dem Ende der zinslosen Zeit 2,50 %; sie gilt für die Richtlinie 2026 nicht.
- **Andere Lesart:** Jahresraten statt Monatsraten; steigende oder nach Vorgabe der NBank gestaffelte Raten.
- **Grundlage:** Richtlinie Mietwohnraum 2026, Nummer 5.3.5. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`.
- **Wirkung (gering):** Liquidität innerhalb des Jahres und laufender Beitrag; Endwert nur gering, weil das Darlehen 35 Jahre zinslos ist. Im geförderten Neubau des Referenzfalls: Tilgung ab Monat 23 in 500 Raten von 10.462,98 Euro; Kapitaldienst zu Bemessungskonditionen 151.713,24 Euro im Jahr.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank; im Einzelfall der Bewilligungsbescheid
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-5.11, R-11.14
- **Bemerkung:** Prüfrunde 1 zur Fachspezifikation des Rechenkerns (2026-11-18): Annahme auf Raten im Takt des Rasters umgestellt; der frühere Wortlaut nannte Jahresraten, der Kern rechnet im Monatsraster Monatsraten. Fragen an die NBank: Jahres- oder Monatsraten, Beginn mit Vollauszahlung oder Bezugsfertigkeit, Beginn der zinslosen Zeit. Richtlinie am 2026-11-18 gegen die Fragenliste gelesen (Quellnotiz 12): Beginn und Ende der Tilgung, Aufschub und zinslose Zeit sind Regel (Fachspezifikation R-5.11) und keine Annahme mehr; die Annahme betrifft nur noch die Form der Raten, Gewicht von mittel auf gering. Der Rechenkern setzt die Förderentscheidung in den Monat vor dem Baubeginn (Festlegung NF-65).

### MA-003 · Zins des NBank-Darlehens ab dem 36. Jahr

- **Annahme:** Ab dem 36. Jahr wird das Darlehen mit dem Basiszinssatz zuzüglich 3 Prozentpunkten verzinst; den Basiszinssatz der fernen Jahre gibt der Anwender vor.
- **Warum offen:** Die Regel steht fest: zinslos bis zum Ablauf des 35. Jahres nach Bezugsfertigkeit, danach bis zu drei Prozentpunkte über dem dann gültigen Basiszinssatz, höchstens marktüblich; eine Festschreibung für die Restlaufzeit ist möglich. Offen ist ein künftiger Wert: der Basiszinssatz und der tatsächliche Aufschlag in den Jahren 36 bis 42.
- **Andere Lesart:** Geringerer Aufschlag oder Fortführung zinslos.
- **Grundlage:** Richtlinie Mietwohnraum 2026, Nummer 5.3.4; Basiszinssatz nach § 247 BGB. Angesetzt ist der ungünstigste zulässige Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `BGB-247`.
- **Wirkung (gering):** Zinsaufwand der Jahre 36 bis 42 auf die Restschuld.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 3, Zeithorizont; Fachspezifikation Rechenkern, R-5.8, R-5.11, R-11.14
- **Bemerkung:** Richtlinie am 2026-11-18 gegen die Fragenliste gelesen (Quellnotiz 12): Die Annahme betrifft einen künftigen Wert, nicht die Regel.

### MA-004 · KfW-Darlehen als Ersatz für Eigenmittel bei der NBank

- **Annahme:** Ein KfW-Darlehen zählt nicht als Eigenmittel; die geforderten 20 % sind aus Eigenkapital aufzubringen.
- **Warum offen:** Die Richtlinie verlangt Eigenmittel von mindestens 20 % der zuwendungsfähigen Kosten (Geld, Eigenleistungen, Wert des lastenfreien Grundstücks; mindestens die Hälfte Geld oder Grundstück) und kennt „als Ersatz der Eigenmittel anerkannte Fremdmittel“. Eine Anerkennung ist also möglich; unter welchen Voraussetzungen, steht nicht da.
- **Andere Lesart:** Die NBank erkennt ein KfW-Darlehen oder andere Fremdmittel ganz oder teilweise als Eigenmittelersatz an; sie stehen dann im Rang nach dem Förderdarlehen.
- **Grundlage:** Richtlinie Mietwohnraum 2026, Nummern 5.2.6, 11.4 und 11.5; Antragsvordruck mit eigener Zeile für KfW-Darlehen. Angesetzt ist der ungünstigere Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `NBANK-VORDRUCK-1011`.
- **Wirkung (hoch):** Eigenkapitalbedarf und damit Eigenkapitalrendite und Finanzierbarkeit des Vorhabens.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-5.12, R-11.14
- **Bemerkung:** Richtlinie am 2026-11-18 gegen die Fragenliste gelesen (Quellnotiz 12): Die Anerkennung von Fremdmitteln als Eigenmittelersatz ist nach Nummer 11.5 möglich; offen sind nur noch die Voraussetzungen. Die vorsichtige Voreinstellung bleibt bis zum Gespräch mit der NBank.

### MA-005 · Finanzierungskosten als zuwendungsfähige Kosten der NBank

- **Annahme:** Finanzierungskosten einschließlich Bauzeitzinsen gehören nicht zu den zuwendungsfähigen Kosten und sind zusätzlich zu finanzieren.
- **Warum offen:** Die Richtlinie nennt als Herstellungskosten die Kostengruppen 200 bis 700 nach DIN 276; die Finanzierung ist dort eine eigene Kostengruppe außerhalb dieser Spanne. Die Norm selbst ist nur im Inhaltsverzeichnis gesehen.
- **Andere Lesart:** Finanzierungskosten sind ganz oder teilweise zuwendungsfähig.
- **Grundlage:** Richtlinie Mietwohnraum 2026, Nummer 1.5; DIN 276 nur als Sekundärquelle. Angesetzt ist der ungünstigere Fall. Die Produktinformation (Stand 05.11.2026) nennt als zuwendungsfähig die Herstellungskosten der Kostengruppen 200 bis 700 und die Grundstückskosten der Kostengruppe 100; Finanzierungskosten nennt sie nicht. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `DIN-276`.
- **Wirkung (gering):** Höhe von Darlehen und Zuschuss; Finanzierungslücke in der Bauphase.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-11.2, R-11.14
- **Bemerkung:** Richtlinie am 2026-11-18 gegen die Fragenliste gelesen (Quellnotiz 12): durch die Kostengruppen weitgehend geklärt, Gewicht von mittel auf gering. Der Zuschlag der Kostengruppe 700 im Rechenkern enthält keine Finanzierungskosten (Fachspezifikation R-11.2).

### MA-006 · Aufteilung bei teilgeförderten Vorhaben

- **Annahme:** Kosten und Finanzierung werden innerhalb des Wohnens nach Wohnfläche auf geförderte Einkommensgruppen und frei finanzierte Wohnungen aufgeteilt, zwischen Wohnen und Gewerbe nach umbautem Raum; gemeinsame Erträge nach Wohnfläche. Einzeln zurechenbare Kosten werden nicht vorab zugeordnet.
- **Warum offen:** Der Schlüssel ergibt sich aus der Arbeitsmappe der NBank. Offen ist nur, ob einzeln zurechenbare Kosten vorab zugeordnet werden dürfen.
- **Andere Lesart:** Kosten, die sich einzelnen Wohnungen eindeutig zurechnen lassen, werden vorab zugeordnet; nur der Rest wird nach dem Schlüssel verteilt.
- **Grundlage:** NBank-Arbeitsmappe „Kosten-Finanzierungsaufteilung“, Blatt 1, Zeilen 11 bis 41 (gelesen 2026-11-18): Wohnflächenanteil mal Anteil des umbauten Raums. Quellen: `NBANK-KOSTEN-FINANZIERUNGSAUFTEILUNG`.
- **Wirkung (gering):** Zuwendungsfähige Kosten des geförderten Teils und damit Förderhöhe; Rendite je Teil.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Am 2026-11-18 nach Quellnotiz 13 genauer gefasst; Gewicht von mittel auf gering.

### MA-007 · Dauer des Drittmittelabzugs bei Mieterhöhungen auf die Vergleichsmiete

- **Annahme:** Fördermittel mindern Mieterhöhungen auf die ortsübliche Vergleichsmiete für zwölf Jahre ab der mittleren Bezugsfertigkeit der geförderten Maßnahme.
- **Warum offen:** Der Bundesgerichtshof begrenzt die Anrechnung auf zwölf Jahre und leitet die Frist aus dem damaligen Umlagesatz von 11 % ab. Ob sie beim heutigen Satz von 8 % unverändert gilt, ist nicht entschieden.
- **Andere Lesart:** Länger als zwölf Jahre, weil sich der Zuschuss beim Umlagesatz von 8 % später aufzehrt; im strengsten Fall über den gesamten Betrachtungszeitraum (frühere Voreinstellung).
- **Grundlage:** § 558 Abs. 5 in Verbindung mit § 559a BGB; BGH vom 13.06.2012, VIII ZR 311/11, Rn. 20 bis 27 (Wortlaut in nichtamtlicher Sammlung gelesen, Quellnotiz 15): zwölf Jahre ab mittlerer Bezugsfertigkeit; eine längere vertragliche Bindung verlängert die Anrechnung nicht. Die Voreinstellung folgt der Rechtsprechung und ist nicht mehr die strengste Lesart; als begründete Ausnahme von der Vorsichtsregel gekennzeichnet. Quellen: `BGB-558`, `BGB-559A`, `BGH-VIII-ZR-311-11`.
- **Wirkung (mittel):** Mietpfad geförderter Sanierungen nach der ersten Erhöhung; Endwert und Rendite.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Anwalt (nur noch: gilt die Frist von zwölf Jahren beim Umlagesatz von 8 % fort?) · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Kopplungen
- **Bemerkung:** Am 2026-11-18 nach Quellnotiz 15 von „gesamter Betrachtungszeitraum“ auf zwölf Jahre umgestellt.

### MA-008 · Modernisierungsumlage für den Heizungstausch bei Staffelmiete

- **Annahme:** Bei vereinbarter Staffelmiete ist während der Laufzeit der Staffeln keine Umlage für den Heizungstausch möglich.
- **Warum offen:** Der Ausschluss von Mieterhöhungen bei Staffelmiete nennt die neue Umlage für den Heizungstausch nicht ausdrücklich; ob er sie erfasst, ist offen.
- **Andere Lesart:** Die Umlage nach § 559e BGB ist neben der Staffelmiete zulässig.
- **Grundlage:** § 557a BGB und § 559e BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. Am Wortlaut gelesen (2026-11-18): § 557a Abs. 2 Satz 2 BGB schließt nur Erhöhungen „nach den §§ 558 bis 559b“ aus; § 559e liegt außerhalb, und § 559e Abs. 4 verweist nicht auf § 557a. Das spricht für die andere Lesart; die vorsichtige Voreinstellung bleibt bis zur Rechtsprüfung. Quellen: `BGB-557A`, `BGB-559E`.
- **Wirkung (gering):** Mieterlös nach Heizungstausch in Wohnungen mit Staffelmiete; gedeckelt auf 0,50 €/m² im Monat.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regel- und Förderkatalog

### MA-009 · Teilung der Bio-Brennstoffkosten im Neubau

- **Annahme:** Im Neubau werden keine Kosten eines Bio-Brennstoffanteils zwischen Vermieter und Mieter geteilt.
- **Warum offen:** Die Kostenteilung verweist für Neubauten auf die Regeln für neue fossile Heizungen; der Pflichtanteil an Bio-Brennstoff gilt aber nur in bestehenden Gebäuden.
- **Andere Lesart:** Die Teilung greift im Neubau auch für freiwillig bezogene Bio-Brennstoffe.
- **Grundlage:** § 5b CO2KostAufG und § 43 GModG. Quellen: `CO2KOSTAUFG-5B`, `GMODG-43`.
- **Wirkung (gering):** Nicht umlagefähige Betriebskosten im Neubau mit Gas- oder Ölheizung ab 2029.
- **Sichtbar:** nur intern · **Umschaltbar:** nein · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regel- und Förderkatalog

### MA-010 · Verlustverrechnung ab 2028

- **Annahme:** Verlustvorträge oberhalb von 1 Mio. € sind bis Veranlagungszeitraum 2027 zu 70 % und ab 2028 zu 60 % verrechenbar.
- **Warum offen:** Geklärt am Bundesgesetzblatt: Die Rückkehr auf 60 % ab dem Veranlagungszeitraum 2028 ist verkündetes Recht.
- **Andere Lesart:** Es bleibt auch ab 2028 bei 70 %.
- **Grundlage:** Wachstumschancengesetz, BGBl. 2024 I Nr. 108: Art. 6 ersetzt in § 10d Abs. 2 Satz 1 EStG „70 Prozent“ durch „60 Prozent“, erstmals für den Veranlagungszeitraum 2028; Art. 6 tritt am 01.01.2028 in Kraft (Art. 35 Abs. 9). Quellen: `ESTG-10D`, `BGBL-2024-I-108`.
- **Wirkung (mittel):** Steuerzahlungen von Vorhaben mit Anlaufverlusten ab 2028.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** geklärt am Bundesgesetzblatt · **Wiedervorlage:** mit der nächsten vierteljährlichen Rechtsprüfung
- **Status:** bestätigt, gesetzt am 2026-11-18, erledigt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regel- und Förderkatalog
- **Bemerkung:** Bestätigt am 2026-11-18 (Quellnotiz 15). Die Regel ist damit Festlegung im Katalog; eine Gesetzesänderung vor 2028 fängt die vierteljährliche Rechtsprüfung.

### MA-011 · Bagatellgrenze bei der Umsatzsteueroption

- **Annahme:** Die Option zur Umsatzsteuer wird nur für Flächen angesetzt, deren Mieter ausschließlich vorsteuerunschädliche Umsätze ausführt; eine Bagatellgrenze wird nicht berücksichtigt.
- **Warum offen:** Das Gesetz kennt keine Bagatellgrenze; eine von der Verwaltung anerkannte Grenze von 5 % ist nur aus zweiter Hand bekannt.
- **Andere Lesart:** Vorsteuerschädliche Umsätze des Mieters bis 5 % sind unschädlich.
- **Grundlage:** § 9 Abs. 2 UStG. Angesetzt ist der ungünstigere Fall. Quellen: `USTG-9`, `USTAE-9-2`.
- **Wirkung (gering):** Vorsteuerabzug aus Bau- und Erwerbskosten bei gemischt genutzten Gewerbeflächen.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Steuerberater · **Wiedervorlage:** vor Stufe 3 (Gewerbe)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 2, Stufe 3

### MA-012 · Rendite bei mehreren Einlagen und Entnahmen

- **Annahme:** Einlagen und Entnahmen werden je Monat saldiert; Entnahmen werden zum Alternativzins nach Steuern auf das Ende des Planungszeitraums aufgezinst und dem Endwert zugerechnet, spätere Einlagen entsprechend dem eingesetzten Eigenkapital.
- **Warum offen:** Das Lehrbuch definiert die VOFI-Rendite nur für eine einzige Einlage zu Beginn. Für Nachschüsse und Ausschüttungen gibt es mehrere vertretbare Lesarten.
- **Andere Lesart:** Im nachgerechneten Testfall liefern die naheliegenden Lesarten 7,18 %, 7,25 %, 7,50 % und 7,88 %.
- **Grundlage:** Lehrbuchformel nach Grob und Kirchner; die gewählte Lesart bleibt in der Logik der ausdrücklichen Wiederanlage. Quellen: `KIRCHNER-IWU-2004`, `GROB-EINFUEHRUNG`.
- **Wirkung (hoch):** VOFI-Eigenkapitalrendite jedes Vorhabens mit Eigenkapitaleinsatz über die Bauzeit oder mit laufenden Ausschüttungen.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** nein · **Klärung durch:** Fachliteratur: Ropeter (1998), S. 186 ff. (`ROPETER-1998`); fachliche Freigabe durch den Auftraggeber · **Wiedervorlage:** mit der Fachspezifikation des Rechenkerns (Phase 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 3, Ausschüttungen und Nachschüsse
- **Bemerkung:** Die genaue Formel ist in Phase 1 festzulegen und finanzmathematisch nachzurechnen. Am Original bestätigt (`SCHULTE-IMMOBILIENINVESTITION-2025`, S. 816): Das Lehrbuch definiert die VOFI-Rendite nur für eine Einlage zu Beginn und gibt für mehrere Einlagen und Entnahmen keine Formel; die Formel des Projekts ist damit eine eigene Erweiterung. Rechnet die Unterlassensalternative mit zwei Zinssätzen, ist der Vergleichsfaktor neu zu fassen.

### MA-013 · Rundung in Darlehensplänen

- **Annahme:** Zins und Tilgung jeder Rate werden kaufmännisch auf Cent gerundet.
- **Warum offen:** Banken runden unterschiedlich; welche Regel gilt, steht im jeweiligen Darlehensvertrag.
- **Andere Lesart:** Abschneiden statt Runden oder Rundung nur des Gesamtbetrags der Rate.
- **Grundlage:** Gegenrechnung: kaufmännische Rundung und Abschneiden liegen bei einem Darlehen über 700.000 € zu 4 % nach zehn Jahren 0,60 € auseinander.
- **Wirkung (gering):** Restschuld im Cent-Bereich; Übereinstimmung mit dem Kontoauszug der Bank.
- **Sichtbar:** nur intern · **Umschaltbar:** ja · **Klärung durch:** Darlehensvertrag im Einzelfall · **Wiedervorlage:** bei der ersten Parallelrechnung mit echten Darlehen (Abnahme Stufe 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 3, Geldbeträge

### MA-014 · Streuungen und Korrelationen der Simulation

- **Annahme:** Voreingestellte Streuungen, Beharrungswerte und Korrelationen der Risikogrößen sind Schätzwerte des Werkzeugs; der Anwender kann sie überschreiben.
- **Warum offen:** Belastbare Marktquellen für Streuungen und Korrelationen deutscher Immobilienmärkte liegen nicht vor.
- **Andere Lesart:** Kalibrierung an eigenen Zeitreihen des Unternehmens oder an Marktdaten eines Anbieters.
- **Grundlage:** Fachliteratur zur Simulation in der Immobilienbewertung nennt Verfahren, aber keine deutschen Parameter.
- **Wirkung (hoch):** Bandbreite der Ergebnisse, Wahrscheinlichkeit, die Zielrendite zu verfehlen, schlechter Fall.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Auftraggeber (eigene Erfahrungswerte); später Marktdaten · **Wiedervorlage:** vor Stufe 2 (Simulation)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 5, Simulation

### MA-015 · Modernisierungsumlage im Referenzfall IWU 2013

- **Annahme:** Der Referenzfall rechnet mit einer Modernisierungsumlage von 11 % auf die Kosten abzüglich Zuschuss.
- **Warum offen:** Der Satz steht nicht in der gelesenen Tabelle; er ist daraus erschlossen, dass die Mietzeile damit exakt übereinstimmt.
- **Andere Lesart:** Eine andere Kombination aus Satz und Bemessungsgrundlage, die zufällig dieselbe Mietzeile ergibt.
- **Grundlage:** Endbericht des IWU von 2013, Anhang C; 11 % war der 2013 geltende gesetzliche Satz. Quellen: `IWU-2013-ENDBERICHT`.
- **Wirkung (gering):** Nur der Abnahmetest; kein Einfluss auf Kalkulationen.
- **Sichtbar:** nur intern · **Umschaltbar:** nein · **Klärung durch:** Fachliteratur (Endbericht im Volltext) · **Wiedervorlage:** beim Anlegen des Abnahmetests (Phase 3)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 3, Abnahmetests

### MA-016 · Verrechnung von Anlaufverlusten

- **Annahme:** Steuerliche Verluste des Vorhabens werden im Vorhaben vorgetragen und erst mit dessen späteren Gewinnen verrechnet. Das Modell nimmt damit an, dass der Investor im Verlustjahr keine anderen Gewinne derselben Steuerart im selben Steuersubjekt hat, mit denen er den Verlust verrechnen könnte.
- **Warum offen:** Ob ein Verlust sofort mit anderen Einkünften des Investors verrechnet werden kann, hängt von dessen übriger steuerlicher Lage ab, die das Werkzeug nicht kennt.
- **Andere Lesart:** Sofortige Verrechnung: Der Investor hat im selben Jahr genug andere Gewinne derselben Steuerart im selben Steuersubjekt (Körperschaft oder Organkreis, Betrieb, andere Einkünfte der Privatperson); die Steuerersparnis fließt im Verlustjahr zu. Das Vorhaben gilt dann als Teil eines größeren Steuersubjekts: Freibetrag und Abrundung der Gewerbesteuer und der Freibetrag der Hinzurechnung gelten als verbraucht. Bei der Personengesellschaft gilt die Lesart nur für die Einkommensteuer; ihr Fehlbetrag der Gewerbesteuer wird immer vorgetragen. Bei Kommanditisten gilt die sofortige Verrechnung nur, soweit kein negatives Kapitalkonto entsteht oder sich erhöht (§ 15a EStG); die Steuer in Kurzform prüft das nicht.
- **Grundlage:** Verlustabzug nach § 10d EStG; Gewerbeverlust nach § 10a GewStG. Voreingestellt ist der Vortrag, weil das Werkzeug die übrige steuerliche Lage des Investors nicht kennt. Welche Lesart das Vorhaben günstiger rechnet, hängt vom Fall ab: Meist ist es die sofortige Verrechnung; im Ankauf des Referenzfalls ergibt sie 4,523 % gegen 4,527 % mit Vortrag, weil der Freibetrag der Hinzurechnung bei ihr als verbraucht gilt. Quellen: `ESTG-10D`, `GEWSTG-10A`, `ESTG-15A`.
- **Wirkung (hoch):** Wert der beschleunigten Abschreibung und der Anlaufverluste im Neubau; Endwert und Rendite nach Steuern.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Anwender je Vorhaben; im Zweifel Steuerberater des Investors · **Wiedervorlage:** mit der Fachspezifikation des Steuermoduls (Phase 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 1, Steuerstatus; Fachspezifikation Rechenkern, R-7.5, R-7.6, Eingabe E-44
- **Bemerkung:** Aus Prüfrunde 3 (Fachexperte). Wird als Merkmal je Vorhaben geführt. Prüfrunde 1 zur Fachspezifikation des Rechenkerns (2026-11-18, Steuerberater): Annahme über andere Gewinne ausdrücklich genannt; bei der Personengesellschaft keine sofortige Erstattung der Gewerbesteuer. Die Kurzform verrechnet Vorträge unbeschränkt; ein Vortrag über dem Sockelbetrag löst einen Hinweis aus (MA-010). Prüfrunde 2 zur Fachspezifikation des Rechenkerns (2026-11-18), Steuerberater: Grenze des § 15a EStG bei Kommanditisten ergänzt; gerechnet wird sie erst in der Steuer in Grundform. Beim Einzelunternehmen rechnet die sofortige Verrechnung die Gewerbesteuer ohne Begrenzung auf die Einkommensteuer des Vorhabens an.

### MA-017 · Restwert bei laufender Bindung

- **Annahme:** Endet der Betrachtungszeitraum vor dem Ende der Bindung, löst der Verkäufer das zinslose Förderdarlehen ab und zahlt den Zuschuss anteilig zurück; der Verkaufswert wird aus der gebundenen Miete abgeleitet. Ein Käufer übernimmt Darlehen und Bindung nicht.
- **Warum offen:** Rückzahlung und Nachwirkung der Bindung stehen in der Richtlinie: Bei freiwilliger vollständiger Rückzahlung ist der Anteil des Zuschusses zurückzuzahlen, der auf die verbleibende Bindungsdauer entfällt, und die Bindungen wirken nach. Zur Übernahme von Darlehen und Bindung durch einen Käufer sagt die Richtlinie nichts. Nachtrag 2026-11-18 (Quellnotiz 13): Die Bindungen treffen kraft Gesetzes jeden Verfügungsberechtigten, also auch einen Käufer (§ 9 Abs. 1, § 10 NWoFG). Für den Eigentümer- und Schuldnerwechsel sieht die NBank eine Zustimmung gegen Entgelt vor (Entgeltkatalog Nr. 3: 0,5 % der Restschuld, 100 bis 1.500 Euro). Offen ist, unter welchen Voraussetzungen sie zustimmt und ob der Käufer das Darlehen zu unveränderten Bedingungen übernimmt.
- **Andere Lesart:** Der Käufer übernimmt Darlehen und Bindung; der Vorteil des zinslosen Darlehens geht dann in den Kaufpreis ein.
- **Grundlage:** Richtlinie Mietwohnraum 2026, Nummer 5.4.6. Angesetzt ist der ungünstigere Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `NWOFG-9`, `NWOFG-10`, `NBANK-ENTGELTKATALOG`.
- **Wirkung (mittel):** Restwert und Endwert geförderter Vorhaben mit Verkauf vor Bindungsende.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Spezifikation Kapitel 3, Restwert; Fachspezifikation Rechenkern, R-8.7, R-8.8, R-11.14
- **Bemerkung:** Aus Prüfrunde 3 (Fachexperte, Jurist). Richtlinie am 2026-11-18 gegen die Fragenliste gelesen (Quellnotiz 12): Rückzahlung des Zuschusses und Ende der Bindung sind geklärt; offen bleibt die Übernahme durch einen Käufer. Der Rechenkern rechnet die Rückzahlung zeitanteilig nach Perioden (Fachspezifikation R-8.7).

### MA-018 · Ersatz eines Gaskessels als energetische Modernisierung

- **Annahme:** Der Ersatz eines Gaskessels durch einen neuen Gas- oder Ölkessel gilt nicht als energetische Modernisierung; ohne Förderfähigkeit wird keine Modernisierungsumlage angesetzt.
- **Warum offen:** Ob der bloße Kesseltausch Endenergie nachhaltig einspart und damit die allgemeine Umlage eröffnet, ist eine Auslegungsfrage des Einzelfalls.
- **Andere Lesart:** Der Tausch gilt als energetische Modernisierung; dann ist die allgemeine Umlage von 8 % möglich.
- **Grundlage:** § 555b Nr. 1 und § 559 BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. BGH vom 26.03.2025, VIII ZR 283/23, Rn. 31 (Quellnotiz 15): Die Erneuerung des Heizkessels kann Endenergie einsparen; die Umlage setzt eine zum Zeitpunkt der Erklärung erwartbare, messbare und dauerhafte Einsparung voraus, und der Erhaltungsanteil ist abzuziehen. Die vorsichtige Voreinstellung bleibt, weil das Modell die Einsparung nicht prüfen kann; die andere Lesart wird als Eingabe „Einsparung nachgewiesen“ mit Erhaltungsanteil geführt. Quellen: `BGB-555B`, `BGB-559`, `BGH-VIII-ZR-283-23`.
- **Wirkung (gering):** Mieterlös nach Kesseltausch ohne Förderung.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regel- und Förderkatalog
- **Bemerkung:** Aus Prüfrunde 3 (Jurist).

### MA-019 · Zinsverbilligte Darlehen bei der Umlage für den Heizungstausch

- **Annahme:** Der Zinsvorteil eines zinsverbilligten Darlehens mindert die Umlage für den Heizungstausch in gleicher Weise wie bei der allgemeinen Modernisierungsumlage.
- **Warum offen:** Die Vorschrift zum Heizungstausch spricht vom Abzug der in Anspruch genommenen Drittmittel; wie ein Zinsvorteil dabei anzusetzen ist, regelt sie nicht ausdrücklich.
- **Andere Lesart:** Strenger: Das Darlehen wird wie ein Zuschuss mit seinem Nennbetrag von den Kosten abgezogen; dafür spricht der Wortlaut, der den Abzug an den Kosten ansetzt. Günstiger für den Vermieter: Nur Zuschüsse werden abgezogen; der Zinsvorteil bleibt unberücksichtigt.
- **Grundlage:** § 559e Abs. 1 in Verbindung mit § 559a BGB. Begründete Ausnahme von der Vorsichtsregel: Angesetzt ist nicht die strengste Lesart (Nennbetrag), sondern der Zinsvorteil. Dafür spricht die Systematik: § 559e Abs. 1 nimmt für die Drittmittel auf § 559a Bezug, und dessen Absatz 2 erfasst Darlehen über den Zinsvorteil; ein Darlehen ist zurückzuzahlen. Der Unterschied wirkt selten, weil meist die Kappung bindet. Quellen: `BGB-559E`, `BGB-559A`.
- **Wirkung (gering):** Mieterlös nach gefördertem Heizungstausch; gedeckelt auf 0,50 €/m² im Monat.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Kopplungen
- **Bemerkung:** Aus Prüfrunde 3 (Jurist); Lesart „Nennbetrag“ und Einordnung als Ausnahme von der Vorsichtsregel aus Prüfrunde 4 (Jurist); Bezeichnung in Prüfrunde 5 vereinheitlicht.

### MA-020 · Umlage für den Heizungstausch in der NBank-Bindung

- **Annahme:** Während der Mietbindung der NBank wird keine Umlage für den Heizungstausch angesetzt.
- **Warum offen:** Die Richtlinie lässt Mieterhöhungen in der Bindung nach bestimmten Vorschriften zu und nennt die neue Umlage für den Heizungstausch dabei nicht.
- **Andere Lesart:** Die Umlage ist auch in der Bindung zulässig, soweit die Höchstmiete eingehalten wird.
- **Grundlage:** Richtlinie Mietwohnraum 2026, Nummer 5.4.5. Angesetzt ist der für den Vermieter ungünstigere Fall. Am Wortlaut gelesen (2026-11-18): § 9 Abs. 1 Satz 3 NWoFG lässt Erhöhungen in den Grenzen der Förderentscheidung nach den allgemeinen mietrechtlichen Vorschriften zu, ohne Paragrafen aufzuzählen. Das Gesetz stützt die andere Lesart; die Höchstmiete begrenzt in jedem Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `BGB-559E`, `NWOFG-9`.
- **Wirkung (gering):** Mieterlös gebundener Wohnungen nach Heizungstausch.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus Prüfrunde 3 (Jurist).

### MA-021 · Nicht abziehbare Vorsteuer als zuwendungsfähige Kosten der NBank

- **Annahme:** Kann der Bauherr die Vorsteuer nicht abziehen, zählt die Umsatzsteuer zu den zuwendungsfähigen Kosten.
- **Warum offen:** Die Richtlinie regelt die Behandlung der Umsatzsteuer nicht ausdrücklich. Der Verwendungsnachweis der NBank setzt voraus, dass nicht abziehbare Umsatzsteuer zuwendungsfähig ist; eine ausdrückliche Bestätigung der NBank steht aus, und die ANBest-P, auf die die Richtlinie verweist, sind noch nicht gelesen.
- **Andere Lesart:** Zuwendungsfähig sind nur die Nettokosten; die Umsatzsteuer ist zusätzlich zu finanzieren.
- **Grundlage:** NBank, Vordruck 4009 „Einfacher Verwendungsnachweis“ (Stand Juli 2026), Nummer 5.4, vom Juristen am 18.11.2026 gelesen: Der Zuwendungsempfänger erklärt, dass die zuwendungsfähigen Ausgaben keine Umsatzsteuer enthalten, soweit sie nach § 15 UStG als Vorsteuer abziehbar ist. Das setzt voraus, dass nicht abziehbare Umsatzsteuer zuwendungsfähig ist. Die Richtlinie verweist in Nummer 12.5 für den Verwendungsnachweis auf Nummer 6 ANBest-P. Die Voreinstellung ist damit die am Text gestützte Lesart und keine Ausnahme von der Vorsichtsregel. Die andere Lesart senkte die Förderung auf die Baukosten um bis zu einem Sechstel (19/119 der Bruttokosten), weniger, wenn die Bemessungsgrenze kappt; die umsatzsteuerfreien Grundstückskosten berührt sie nicht. Quellen: `NBANK-VORDRUCK-4009`, `NBANK-RL-MIETWOHNRAUM-2026`, `NI-ANBEST-P`.
- **Wirkung (gering):** Höhe von Darlehen und Zuschuss; Finanzierungslücke.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** geklärt am Text des niedersächsischen Haushaltsrechts · **Wiedervorlage:** mit der nächsten vierteljährlichen Rechtsprüfung
- **Status:** bestätigt, gesetzt am 2026-11-18, erledigt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus der dritten Überarbeitung des Rechercheberichts; Größe der Wirkung und Klärungsweg nach Prüfrunde 4 (Finanzmathematiker, Jurist) berichtigt. Prüfrunde 5 (Jurist): Grundlage ist jetzt der Vordruck 4009; Gewicht von mittel auf gering gesetzt, die Einordnung als Ausnahme von der Vorsichtsregel entfällt. Bestätigt am 2026-11-18 durch VV Nr. 2.6 zu § 44 LHO und Nr. 6.4 ANBest-P (`NI-ANBEST-P`, Quellnotiz 13): Nur die nach § 15 UStG abziehbare Vorsteuer gehört nicht zu den zuwendungsfähigen Ausgaben. Die Bestätigung durch die NBank entfällt.

### MA-022 · Leerstand beim Mieterwechsel und Sonderabschreibung

- **Annahme:** Ein Leerstand zwischen zwei Mietverhältnissen schadet der Sonderabschreibung nicht, solange die Vermietungsabsicht fortbesteht. Schädlich bleiben Selbstnutzung, unentgeltliche Überlassung, vorübergehende Beherbergung und die Aufgabe der Vermietungsabsicht.
- **Warum offen:** Das Gesetz verlangt, dass die Wohnung der entgeltlichen Überlassung zu Wohnzwecken dient; ob das einen Leerstand beim Mieterwechsel einschließt, ergibt sich aus der Verwaltungsauffassung, die nicht gelesen ist.
- **Andere Lesart:** Jeder Leerstand im Nutzungszeitraum nach § 7b, dem Jahr der Anschaffung oder Herstellung und den neun folgenden Jahren, löst die rückwirkende Versagung der Sonderabschreibung aus.
- **Grundlage:** BMF-Schreiben vom 21.05.2025 zu § 7b EStG, Rn. 33: Eine Wohnung dient der entgeltlichen Überlassung auch, wenn sie vorübergehend leer steht, die Überlassung aber weiterhin vorgesehen ist und die Wohnung dafür bereitgehalten wird. Schädlich bleiben Selbstnutzung und unentgeltliche Überlassung (Rn. 32) sowie die vorübergehende Beherbergung (Rn. 36). Verwaltungsauffassung; die Finanzverwaltung ist daran gebunden. Quellen: `ESTG-7B`, `BMF-7B-2025`.
- **Wirkung (mittel):** Steuerzahlungen im Neubau mit Sonderabschreibung; Ergebnis im Stressfall Leerstand.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** geklärt am Anwendungsschreiben der Finanzverwaltung · **Wiedervorlage:** bei Neufassung des Anwendungsschreibens
- **Status:** bestätigt, gesetzt am 2026-11-18, erledigt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus Prüfrunde 3 (Jurist) und der dritten Überarbeitung des Rechercheberichts; schädliche Nutzungen und Begriff „Nutzungszeitraum“ aus Prüfrunde 4 (Jurist). Bestätigt am 2026-11-18 (Quellnotiz 13). Die Voreinstellung ist damit keine Ausnahme von der Vorsichtsregel mehr.

### MA-023 · Kostenbasis der Baukostenobergrenze der Sonderabschreibung

- **Annahme:** Die Baukostenobergrenze der Sonderabschreibung wird an den abschreibungsfähigen Anschaffungs- oder Herstellungskosten des Gebäudes gemessen: ohne Grund und Boden, ohne Erschließung außerhalb des Grundstücks, ohne Möblierung und ohne Finanzierungskosten, mit Hausanschlüssen und Baunebenkosten. Von den Außenanlagen zählt nur die Einfriedung des Wohngrundstücks; Gartenanlagen, Wege, Hofbefestigung und Zufahrten zählen nicht. Geteilt wird durch die Nutzfläche des ganzen Gebäudes einschließlich Nebenräumen und Garagen, wahlweise durch die Bruttogrundfläche. Beim Erwerb zählt der Gebäudeanteil des Kaufpreises nach der Kaufpreisaufteilung zuzüglich der anteiligen Erwerbsnebenkosten.
- **Warum offen:** Kostenbegriff, Flächenmaß und Außenanlagen sind durch die Verwaltungsauffassung geklärt. Im Modell liegt die Kostengruppe 500 meist nur als Summe vor: Sie zählt nicht zur Kostenbasis; Einfriedungen gibt der Anwender gesondert an.
- **Andere Lesart:** Die Kostengruppe 500 zählt ganz mit (strenger, ohne Stütze in der Verwaltungsauffassung).
- **Grundlage:** BMF-Schreiben vom 21.05.2025 zu § 7b EStG: abschreibungsfähige Kosten nach § 255 HGB (Rn. 38, 41), Grund und Boden und Erschließung außerhalb des Grundstücks zählen nicht, Hausanschlüsse zählen (Rn. 42, 43), Möblierung zählt nicht (Rn. 46), Kaufpreisaufteilung beim Erwerb (Rn. 47), Nutzfläche des ganzen Gebäudes oder Bruttogrundfläche nach DIN 277 (Rn. 49 bis 51); bei Überschreitung entfällt die Sonderabschreibung ganz (Rn. 48). Außenanlagen: Rn. 45 verweist auf R 21.1 Abs. 3 Satz 1 EStR – von der Gartengestaltung gehört nur die „lebende Umzäunung“ zum Gebäude, im Übrigen ist die Gartenanlage ein eigenes Wirtschaftsgut; die Umzäunung eines Mietwohngrundstücks gehört in der Regel zum Gebäude (H 6.4, H 7.1 EStH; Wortlaut in Verlagswiedergabe, Quellnotiz 15). Bis 2026-11-18 war bei Herstellung die Kostensumme der NBank-Förderung (Kostengruppen 200 bis 700) geteilt durch die Wohnfläche angesetzt; das war beim Kostenbegriff nahe am Ergebnis, beim Flächenmaß zu streng. Quellen: `ESTG-7B`, `BMF-7B-2025`, `ESTR-21-1`, `ESTH-6-4-7-1`.
- **Wirkung (gering):** Ob die Sonderabschreibung überhaupt gewährt wird; die Grenze ist eine Ausschlussgrenze.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** geklärt am Anwendungsschreiben der Finanzverwaltung und an den Einkommensteuer-Richtlinien · **Wiedervorlage:** bei Neufassung des Anwendungsschreibens
- **Status:** bestätigt, gesetzt am 2026-11-18, erledigt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus Prüfrunde 3 (Fachexperte) und der dritten Überarbeitung des Rechercheberichts; Ersterwerb aus Prüfrunde 4 (Jurist). Prüfrunde 5 (Jurist): beim Erwerb Gebäudeanteil statt Kaufpreis einschließlich Boden, ohne Marktwertdeckel. Offen bleibt, welche Gebäudekosten im Einzelnen zählen, etwa Außenanlagen. Am 2026-11-18 nach den Quellnotizen 13 und 15 neu gefasst und geschlossen. Die Wohnfläche bleibt Maßstab für den Deckel der Bemessungsgrundlage (BMF Rn. 59, 60), nicht für die Obergrenze.

### MA-024 · Zeitlicher Anwendungsbereich des Wärmepumpen-Nachweises

- **Annahme:** Für eine eingebaute Wärmepumpe ist der Nachweis der Jahresarbeitszahl erforderlich, außer in den Fällen des § 559f Abs. 1 Satz 2 Nr. 1 bis 4 BGB (Gebäude nach 1996 errichtet, nach der Wärmeschutzverordnung 1995 gebaut, nach einer Sanierung mindestens auf dem Stand des § 38 Gebäudemodernisierungsgesetz oder mit höchstens 55 °C Vorlauftemperatur beheizbar); ohne Nachweis wird nur die Hälfte der Kosten umgelegt. Im Neubau greift die Halbierung nicht.
- **Warum offen:** Eine Übergangsvorschrift zu §§ 559e, 559f BGB nennt die Inhaltsübersicht von Art. 229 EGBGB nicht; die Einzelvorschriften sind nicht gelesen. Ob ein Ausnahmefall vorliegt, gibt der Anwender je Vorhaben an.
- **Andere Lesart:** Die Vorschrift gilt nur für bestimmte Zeiträume; außerhalb ist die volle Umlage ohne Nachweis möglich.
- **Grundlage:** § 559f BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `BGB-559F`, `EGBGB-ART-229`.
- **Wirkung (gering):** Mieterlös nach Einbau einer Wärmepumpe.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus der dritten Überarbeitung des Rechercheberichts. Am 2026-11-18 nach Quellnotiz 13 um die gesetzlichen Ausnahmen ergänzt.

### MA-025 · Modernisierungsumlage für den Glasfaseranschluss

- **Annahme:** Für den erstmaligen Glasfaseranschluss wird keine Modernisierungsumlage angesetzt.
- **Warum offen:** Der Wortlaut steht in Spannung: § 559 Abs. 1 Satz 1 BGB nennt die Maßnahmen nach § 555b Nr. 1, 3, 4, 5 und 6, nicht Nr. 4a; Satz 2 regelt aber, wann die Erhöhung im Fall der Nr. 4a zulässig ist, und setzt ihre Umlage damit voraus.
- **Andere Lesart:** Nr. 4a ist umlagefähig, über Satz 2 oder weil der Anschluss den Gebrauchswert nach Nr. 4 erhöht: 8 % der Kosten, wenn der Mieter seinen Anbieter frei wählen kann und kein Bereitstellungsentgelt als Betriebskosten umgelegt wird oder wurde.
- **Grundlage:** § 555b Nr. 4a und § 559 Abs. 1 Satz 2 BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `BGB-555B`, `BGB-559`.
- **Wirkung (gering):** Mieterlös nach Glasfaserausbau.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus Prüfrunde 3 (Jurist); Grund und andere Lesart nach Prüfrunde 4 (Jurist) neu gefasst. Frage an den Anwalt: Ist Nr. 4a über § 559 Abs. 1 Satz 2 oder über Nr. 4 umlagefähig?

### MA-026 · Rechengrundlage des Bankdarlehens

- **Annahme:** Offen ist an der Rechnung der Bank fünferlei. (1) Beleihungsquote: Die Bank rechnet ihre Quote über alle Darlehen, auch über das Förderdarlehen der Grobförderung, obwohl es nach der Richtlinie im Rang nach den Bankmitteln steht, und über das durchgeleitete KfW-Darlehen; für ein übernommenes Darlehen ist der Rang Eingabe. (2) Kapitaldienst: Die Bank rechnet ihr eigenes Darlehen mit dem höheren aus Vertragszins und kalkulatorischem Zins. Darlehen anderer Geber mit fester Kondition (KfW, NBank, übernommene Darlehen) rechnet sie über den Bemessungszeitraum – eine Vorgabe des Hauses, voreingestellt die Zinsbindung des Bankdarlehens – mit dem zeitgewichteten Mittel aus Vertragszins bis zum Ende ihrer Zinsbindung und kalkulatorischem Zins danach; die Tilgung mindestens mit der Mindesttilgung. (3) Ertrag: Die Bank setzt den nachhaltigen Reinertrag an, beim Ankauf den kleineren aus Miete und Vergleichsmiete, mit Bewirtschaftungskosten mindestens in Höhe des Mindestansatzes. (4) Im Neubau gilt als nachhaltige Miete die Miete bei Bezug. (5) Wertansatz: Kaufpreis, beim Neubau die Gesamtkosten.
- **Warum offen:** Wie eine Bank Kapitaldienstfähigkeit und Beleihung im Einzelfall rechnet, ist nicht veröffentlicht und von Haus zu Haus verschieden: mit welchem Ertrag, ob vorrangige und geförderte Darlehen auf Quote und Deckung angerechnet werden und auf welchen Wert.
- **Andere Lesart:** (1) Die Bank rechnet ihre Quote nur über vor- und gleichrangige Darlehen; das Förderdarlehen belegt den Beleihungsraum dann nicht. (2) Die Bank rechnet mit den Vertragskonditionen. (3) Sie setzt Ertrag und Bewirtschaftung des Vorhabens an. (4) Sie rechnet auch die Darlehen anderer Geber durchgehend mit ihrem kalkulatorischen Zins. Diese vier sind umschaltbar; (1) bis (3) lassen das Bankdarlehen höher ausfallen, (4) niedriger. (5) Sie setzt im Neubau eine niedrigere nachhaltige Miete an (Eingabe). (6) Sie setzt einen Beleihungswert unter dem Kaufpreis an (Eingabe).
- **Grundlage:** Gegenrechnungen der Prüfrunden 4 und 5 zum Recherchebericht und der Prüfrunden 1 und 2 zur Fachspezifikation des Rechenkerns (Rollen Bank und Praktiker). Bewirtschaftungsansatz nach der Beleihungswertermittlungsverordnung. Rang des Förderdarlehens: Richtlinie Mietwohnraum 2026, Nummern 5.3.6 und 11.5; der Rang ist damit Regel, Annahme ist nur, ob die Bank ihre Quote trotzdem über alle Darlehen rechnet. Drei gekennzeichnete Ausnahmen von der Vorsichtsregel: der Bemessungszins fremder Tranchen (vorsichtiger wäre Lesart 4; sie ließ dem KfW-Darlehen keinen Bemessungsvorteil und erzeugte eine Klippe, wenn ein übernommenes Darlehen kurz vor dem Bankdarlehen aus der Bindung läuft), der Wertansatz (Kaufpreis statt eines niedrigeren Beleihungswerts) und die nachhaltige Miete im Neubau (der Kern kennt dort keinen Mietspiegelwert). Das Anschlussrisiko zeigt daneben die kleinste Deckung über die Haltedauer. Quellen: `BELWERTV-11`, `NBANK-RL-MIETWOHNRAUM-2026`.
- **Wirkung (hoch):** Höhe des Bankdarlehens und damit höchster tragbarer Preis, nötiges Eigenkapital und Rendite in der Grobkalkulation. Ankauf des Referenzfalls: Bankdarlehen 1.226.609,99 Euro; höchster tragbarer Preis 2.317.235 Euro gegen 2.359.366 Euro mit Vertragskonditionen (Lesart 2). Gebundener Bestand mit übernommenem Darlehen: Bankdarlehen 843.802,85 Euro mit dem Bemessungszins gegen 672.374,28 Euro nach Lesart 4. Neubau mit KfW-Darlehen von 3 Mio. Euro: tragbarer Grundstückspreis 1.197.094 Euro gegen 920.435 Euro nach Lesart 4 und 1.283.299 Euro nach Lesart 2. Im geförderten Neubau bleibt nach jeder Lesart kein Bankdarlehen, weil die Deckung bindet.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Hausbank (13 Fragen in der Fachspezifikation des Rechenkerns, Kapitel 16); die Schwellen selbst (Beleihungsquote, Mindestdeckung, Mindesttilgung, kalkulatorischer Zins je Tranchenart, Bemessungszeitraum, Mindestansatz der Bewirtschaftung) sind Vorgaben des Hauses · **Wiedervorlage:** mit den Vorgaben des Hauses vor dem Einsatz von Teilschritt 1a
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 2, Grobkalkulation; Fachspezifikation Rechenkern, R-5.12, R-5.19, R-10.24, R-11.8, R-11.14, R-11.15
- **Bemerkung:** Aus Prüfrunde 4 (Finanzmathematiker, Fachexperte, Praktiker). Prüfrunde 5: Bezug der Beleihungsquote auf die Summe aller Darlehen festgelegt, Gewicht von mittel auf hoch gesetzt, Wertansatz als Ausnahme von der Vorsichtsregel gekennzeichnet. Prüfrunde 1 zur Fachspezifikation des Rechenkerns (2026-11-18, Bank und Praktiker): neu geschnitten. Die Deckung über alle Darlehen ist jetzt Festlegung; der frühere Schalter verband Beleihungsraum und Deckung. Neu als vorsichtige Voreinstellung: kalkulatorischer Kapitaldienst und nachhaltiger Reinertrag; der Entwurf rechnete mit Vertragszins und dem Ertrag des Vorhabens. Prüfrunde 2 zur Fachspezifikation des Rechenkerns (2026-11-18) (Bank, Praktiker, Fachexperte): Der kalkulatorische Kapitaldienst für alle Tranchen ist durch den Bemessungszins je Tranche ersetzt; die frühere Voreinstellung bleibt als Lesart 4 umschaltbar. Die nachhaltige Miete im Neubau ist eigene Eingabe, ihre Voreinstellung Teil dieser Annahme. Am selben Tag aus der Richtlinie gelesen: Das Förderdarlehen ist nachrangig, und die vorrangigen Bankmittel sind mit mindestens 1 % zuzüglich ersparter Zinsen zu tilgen (Katalogwert, Regel).

### MA-027 · Rechenregel der VOFI-Amortisationsdauer

- **Annahme:** Die Amortisationsdauer endet mit der Periode, von der an das Vermögen aus der Investition bei gedachtem Verkauf zum Wertpfad, nach Verkaufskosten, Ablösung der Restschuld und Steuern, die Anlage des eingesetzten Eigenkapitals zur Unterlassensalternative dauerhaft erreicht oder übertrifft.
- **Warum offen:** Der Begriff ist belegt (Amortisationsdauer unter Berücksichtigung von Finanzierungskonditionen und steuerlichen Konsequenzen), die Rechenregel nach Grob liegt nicht am Original vor. Die zugänglichen Quellen beschreiben zwei verschiedene Regeln.
- **Andere Lesart:** Rückgewinnung des Eigenkapitals: die erste Periode, in der das Vermögen aus der Investition das eingesetzte Eigenkapital erreicht, ohne Vergleich mit der Unterlassensalternative. Diese Lesart amortisiert früher.
- **Grundlage:** Quellnotiz 10 (research_notes): Suchauszug aus dem Stichwort VOFI im Gabler Banklexikon; Beitrag der Dr. Klein Wowi Redaktion vom 06.04.2021, am Original gelesen. Voreingestellt ist die Lesart mit der längeren Amortisationsdauer. Sie rechnet mit dem Wertpfad je Periode, den der Bericht in Anhang A, Nr. 18 verlangt: Ohne Restwert vor dem Verkauf ergäbe die Kennzahl bei jedem fremdfinanzierten Bestand nur die Haltedauer (Finanzmathematiker, Prüfrunde 5). Im Testfall des Berichts ergibt die Voreinstellung bei angenommenem linearem Wertpfad drei Jahre, die andere Lesart zwei. Quellen: `GABLER-BANKLEXIKON-VOFI`, `DRKLEIN-VOFI-2021`, `GROB-EINFUEHRUNG`.
- **Wirkung (gering):** Ausgewiesene Amortisationsdauer auf dem Kennzahlenblatt; keine Wirkung auf Endwert, Rendite oder tragbaren Preis.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Fachliteratur (Grob, Einführung in die Investitionsrechnung) oder ein Hochschulskript, das die Regel wiedergibt · **Wiedervorlage:** mit der Fachspezifikation des Kennzahlenblatts (Spezifikation Kapitel 3)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 3, Lehrbuchkennzahlen
- **Bemerkung:** In Prüfrunde 5 neu gefasst: gedachter Verkauf zum Wertpfad und dauerhafte Überschreitung statt „ohne Restwert vor dem geplanten Verkauf“. Die Kennzahl steht damit erst mit dem Wertpfad ab der Vollkalkulation zur Verfügung. Die Gesamtkapitalrentabilität ist gelesen; ihre offene Einzelheit führt MA-028.

### MA-028 · Zuzurechnende Sollzinsen in der VOFI-Gesamtkapitalrentabilität

- **Annahme:** Der Anschaffungsauszahlung zuzurechnen ist die einfache Summe der Sollzinsen aller Darlehen, die die Anschaffungsauszahlung finanzieren, über den Betrachtungszeitraum; Zinsen auf den Kontokorrentkredit zählen nicht dazu.
- **Warum offen:** Formel und Referenzzinsfuß der Kennzahl sind am Lexikoneintrag gelesen. Der Eintrag sagt aber nicht, wie die zuzurechnenden Sollzinsen abgegrenzt sind: ob als einfache Summe, ob einschließlich der Zinsen auf einen Kontokorrentkredit und wie bei mehreren Tranchen und Sondertilgungen.
- **Andere Lesart:** Einschließlich der Kontokorrentzinsen oder mit aufgezinsten Sollzinsen; Kennzahl und Referenzzinsfuß fielen dann beide höher aus.
- **Grundlage:** Gabler Banklexikon, Stichwort VOFI-Gesamtkapitalrentabilität, als Bildschirmfoto gelesen am 18.11.2026 (Quellnotiz 10). Die Abgrenzung ändert die Entscheidung nicht: Die Sollzinsen gehen in Kennzahl und Referenzzinsfuß mit demselben Betrag ein, und die Kennzahl liegt genau dann über dem Referenzzinsfuß, wenn die Endwertdifferenz positiv ist. Im Testfall des Berichts ergibt die Voreinstellung 4,61 % gegen einen Referenzzinsfuß von 2,14 %. Quellen: `GABLER-BANKLEXIKON-GKR`.
- **Wirkung (gering):** Ausgewiesene VOFI-Gesamtkapitalrentabilität und ihr Referenzzinsfuß auf dem vollen Kennzahlenblatt; keine Wirkung auf Endwert, Eigenkapitalrendite, Endwertdifferenz oder tragbaren Preis.
- **Sichtbar:** Anwendung · **Umschaltbar:** nein · **Klärung durch:** Fachliteratur: Grob, Einführung in die Investitionsrechnung, nach `SCHULTE-IMMOBILIENINVESTITION-2025` (S. 813) dort S. 140 f. · **Wiedervorlage:** mit der Fachspezifikation des Kennzahlenblatts (Spezifikation Kapitel 3)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 3, Lehrbuchkennzahlen
- **Bemerkung:** Aus Prüfrunde 5 (Sichtung, Punkt 17). Im Bildschirmfoto ist der Wurzelexponent des Referenzzinsfußes nicht zu erkennen; nach dem Aufbau der Formel ist es wie bei der Kennzahl die n-te Wurzel.

### MA-029 · Anknüpfung der De-minimis-Bindung der Sonderabschreibung

- **Annahme:** Die De-minimis-Bindung der Sonderabschreibung gilt, wenn die Sonderabschreibung im Rahmen der Gewinnermittlung von Einkünften aus Land- und Forstwirtschaft, Gewerbebetrieb oder selbständiger Arbeit beansprucht wird: bei Körperschaften, gewerblich geprägten und gewerblichen Personengesellschaften und bei Kapitalgesellschaften als Gesellschafterinnen einer vermögensverwaltenden Personengesellschaft (je Beteiligtem). Die Privatperson, die die Wohnung im Privatvermögen vermietet, ist nicht gebunden, auch wenn sie daneben eine Praxis oder ein Gewerbe hat.
- **Warum offen:** Der Wortlaut des § 7b Abs. 5 Satz 2 EStG knüpft an die Person an; die Finanzverwaltung wendet die Bindung aber nur an, wenn die Sonderabschreibung in der Gewinnermittlung beansprucht wird. Ein Gericht könnte am Wortlaut anders entscheiden; praktisch ist das ohne Gewicht, weil die Verwaltung an ihr Schreiben gebunden ist.
- **Andere Lesart:** Wortlaut des § 7b Abs. 5 Satz 2 EStG: Gebunden ist jeder Anspruchsberechtigte mit solchen Einkünften, auch die Privatperson mit Praxis oder Gewerbe.
- **Grundlage:** BMF-Schreiben vom 21.05.2025 zu § 7b EStG, Rn. 83, 87, 107; Mitunternehmerschaften je Beteiligtem (Rn. 101 bis 104, 112). Körperschaften sind nach beiden Lesarten gebunden (§ 8 Abs. 2 KStG). Quellen: `ESTG-7B`, `KSTG-8`, `BMF-7B-2025`.
- **Wirkung (gering):** Ob die Sonderabschreibung eines Investors mit solchen Einkünften an der De-minimis-Höchstgrenze endet; Steuerzahlungen und Rendite nach Steuern im Neubau.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** geklärt am Anwendungsschreiben der Finanzverwaltung · **Wiedervorlage:** bei Neufassung des Anwendungsschreibens
- **Status:** bestätigt, gesetzt am 2026-11-18, erledigt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus Prüfrunde 5 (Jurist, Befund 1; Sichtung, Punkt 12). Am 2026-11-18 nach Quellnotiz 13 umgestellt: Bis dahin war die Anknüpfung an die Person voreingestellt (strengere Lesart des Wortlauts); die Verwaltungsauffassung ist die frühere „andere Lesart“. Die strengere Lesart bleibt umschaltbar.

### MA-030 · Gewerbesteuer auf den Verkaufsgewinn bei erweiterter Kürzung

- **Annahme:** Bei gesetztem Kennzeichen „erweiterte Grundstückskürzung“ unterliegt der Gewinn aus dem Verkauf des Objekts der Gewerbesteuer. Wird der gesamte Grundbesitz vor dem 31.12., 23:59 Uhr, übertragen, entfällt die erweiterte Kürzung für das ganze Verkaufsjahr, auch für den laufenden Ertrag; es bleibt die einfache Kürzung um die Grundsteuer, die die Steuer in Kurzform nicht rechnet. Geht der Grundbesitz zum 31.12., 23:59 Uhr, über (Eingabe „Übergang zum Jahresende“, voreingestellt nein), bleibt die Kürzung des laufenden Ertrags; der Verkaufsgewinn bleibt auch dann gewerbesteuerpflichtig.
- **Warum offen:** Dass die erweiterte Kürzung nicht zeitanteilig gewährt wird und bei Übergang vor dem Jahresende für das ganze Jahr entfällt, ist entschieden. Ob der Verkaufsgewinn bei einem Übergang zum 31.12., 23:59 Uhr, zum gekürzten Ertrag gehört, ist nicht am Original gelesen (BFH I R 89/03).
- **Andere Lesart:** Bei Übergang zum Jahresende gehört auch der Verkaufsgewinn zum gekürzten Ertrag und bleibt gewerbesteuerfrei. Umschaltbar; ohne die Eingabe „Übergang zum Jahresende“ wirkt die Lesart nicht.
- **Grundlage:** BFH vom 17.10.2024, III R 1/23; § 9 Nr. 1 Satz 1 und 2 GewStG. Angesetzt ist der ungünstigste Fall; die Voreinstellung ist keine Ausnahme von der Vorsichtsregel. Keine Annahme, sondern am Wortlaut belegt ist, dass Zinserträge nicht gekürzt werden. Quellen: `GEWSTG-9`, `GEWSTG-7`, `BFH-III-R-1-23`.
- **Wirkung (hoch):** Steuer im Verkaufsjahr, Endwert, Rendite und höchster tragbarer Preis bei Körperschaften und gewerblich geprägten Personengesellschaften mit Kennzeichen. Ankauf des Referenzfalls: Rendite 4,670 % in der Voreinstellung, 4,697 % mit Übergang zum Jahresende und 5,161 %, wenn dann auch der Verkaufsgewinn gekürzt wird; der Wegfall der Kürzung im Verkaufsjahr kostet 7.952,00 Euro Endwert, die Gewerbesteuer auf den Verkaufsgewinn 139.930,00 Euro.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Steuerberater des Auftraggebers · **Wiedervorlage:** mit der Antwort des Steuerberaters; spätestens vor dem Einsatz von Teilschritt 1a
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 1, Steuerstatus; Spezifikation Kapitel 2, Grobkalkulation; Fachspezifikation Rechenkern, R-7.8, R-7.14, R-9.5, Eingabe E-69
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Steuerberater, Befund 1). Der Entwurf hatte mit dem Kennzeichen den ganzen Gewerbeertrag freigestellt; das war eine nicht gekennzeichnete Ausnahme von der Vorsichtsregel. Prüfrunde 2 zur Fachspezifikation des Rechenkerns (2026-11-18) (Steuerberater, Hinweis 7) und Quellnotiz 13: Nach dem am 2026-11-18 am Original gelesenen Urteil BFH III R 1/23 ist der Wegfall der Kürzung im Verkaufsjahr Regel und jetzt Voreinstellung; die bisherige Voreinstellung (nur der Verkaufsgewinn gewerbesteuerpflichtig) gilt mit der neuen Eingabe „Übergang zum Jahresende“. Sollwerte der Referenzfälle mit Kennzeichen geändert (Differenzbericht aenderungen-runde2.md).

### MA-031 · Steuerliche Einordnung des NBank-Zuschusses

- **Annahme:** Der Zuschuss der Wohnraumförderung ist Gegenleistung für die Belegungs- und Mietbindung und wird über die Bindung verteilt versteuert. Ist das Kennzeichen der erweiterten Grundstückskürzung gesetzt, gilt er als Investitionszuschuss, der die Herstellungskosten mindert. Eine Rückzahlung beim Verkauf mindert das laufende Ergebnis, nicht den Verkaufsgewinn.
- **Warum offen:** Offen ist nur die Einordnung: Gegenleistung für die Bindung oder Investitionszuschuss. Die Folgen je Einordnung sind Regel und keine Annahme: Als Gegenleistung ist der Zuschuss im Betriebsvermögen abzugrenzen und bei der Privatperson Einnahme bei Zufluss, auf Wahl über die Bindung verteilbar; als Investitionszuschuss lässt die Verwaltung die Wahl zwischen Einnahme und Minderung der Herstellungskosten.
- **Andere Lesart:** Die jeweils andere Einordnung: ohne Kennzeichen Minderung der Herstellungskosten, mit Kennzeichen Verteilung über die Bindung. Dazu die sofortige Einnahme als Wahl des Investors; sie ist keine Lesart der Rechtslage, bleibt aber für die Sensitivität umschaltbar. Bei der Minderung mindert nur der Anteil des Zuschusses, der auf das Gebäude entfällt, die Abschreibungsgrundlage.
- **Grundlage:** Prüfrunde 2 zur Fachspezifikation (Steuerberater, Befunde 1, 2 und 4): § 5 Abs. 5 und § 11 Abs. 1 EStG am Original gelesen; die Verwaltungsanweisungen zu Zuschüssen sind nicht gelesen. Voreingestellt ist je Kennzeichen die ungünstigere der beiden Einordnungen, gemessen an der Endwertdifferenz, weil es im Referenzfall bei 5 % Zielrendite in keiner Lesart einen tragbaren Preis gibt. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `ESTG-5`, `ESTG-11`, `ESTG-7`.
- **Wirkung (hoch):** Steuer der Bauzeit und der Bindung, Eigenkapitalbedarf, Endwertdifferenz und Rendite im geförderten Neubau. Referenzfall mit 38 Jahren Haltedauer, ohne Kennzeichen: Rendite 3,956 % (verteilt, Voreinstellung) gegen 3,958 % (Minderung) und 3,559 % (sofortige Einnahme); Endwertdifferenz 5.656.209,72 Euro gegen 5.661.518,27 und 5.272.665,63 Euro. Mit Kennzeichen: 3,993 % (Minderung, Voreinstellung) gegen 4,001 % (verteilt) und 3,771 % (sofort).
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Steuerberater des Auftraggebers; zur Praxis der Bewilligung die NBank · **Wiedervorlage:** mit der Antwort des Steuerberaters; spätestens vor dem Förderteil (1c)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-7.3, R-7.4, R-7.19, R-11.14
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Steuerberater, Befund 6; Grenzfälle, Befund 9). Der Entwurf minderte die Abschreibungsgrundlage um den ganzen Zuschuss, auch um den Anteil, der auf das Grundstück entfällt. Übersteigt der Zuschuss die Kosten, auf die er entfällt, rechnet der Kern nicht (Meldung). Prüfrunde 2 zur Fachspezifikation des Rechenkerns (2026-11-18) (Steuerberater 1, 2 und 4; Praktiker 4): Annahme neu gefasst. Voreinstellung nicht mehr die sofortige Einnahme, sondern je Kennzeichen „verteilt“ oder „Minderung“; die Rückzahlung steht im laufenden Ergebnis; das Entgelt auf den Zuschuss folgt der Lesart des Zuschusses.

### MA-032 · Finanzierungskosten und Vorfälligkeit in der Steuer

- **Annahme:** Das Entgelt der NBank auf das Darlehen gilt als laufzeitbezogen und wird über die zinslose Zeit verteilt – im Betriebsvermögen durch Rechnungsabgrenzung, bei Privatperson, Verein und Stiftung als Vorauszahlung für mehr als fünf Jahre. Das Entgelt auf den Zuschuss folgt der Lesart des Zuschusses (MA-031). Ein Disagio der Privatperson gilt als marktüblich und ist im Jahr der Zahlung abziehbar. Die Vorfälligkeitsentschädigung von Privatperson, Verein und Stiftung beim Verkauf gilt als Veräußerungskosten: Sie mindert einen steuerpflichtigen Verkaufsgewinn und bleibt bei einem steuerfreien Verkauf ohne steuerliche Wirkung.
- **Warum offen:** Belegt ist, dass laufzeitbezogene Entgelte im Betriebsvermögen abzugrenzen sind und dass die Privatperson Ausgaben im Jahr der Zahlung abzieht, ein marktübliches Disagio eingeschlossen. Offen ist, ob die Entgelte der NBank laufzeitbezogen sind, wann ein Disagio marktüblich ist und wie die Vorfälligkeitsentschädigung der Privatperson beim Verkauf einzuordnen ist; das hängt an Verwaltungsauffassung und Rechtsprechung, die nicht gelesen sind.
- **Andere Lesart:** Die Entgelte der NBank sind im Jahr der Zahlung abziehbar (umschaltbar). Ein Disagio der Privatperson ist zu verteilen. Die Vorfälligkeitsentschädigung ist Werbungskosten aus Vermietung.
- **Grundlage:** Rechnungsabgrenzung nach § 5 Abs. 5 EStG und Verteilung von Vorauszahlungen nach § 11 Abs. 2 EStG, gelesen vom Steuerberater in den Prüfrunden 1 und 2; im Übrigen dessen Einschätzung. Angesetzt ist jeweils der ungünstigere Fall. Quellen: `ESTG-5`, `ESTG-11`, `ESTG-23`.
- **Wirkung (mittel):** Zeitpunkt des Abzugs und damit Steuer der ersten Jahre und des Verkaufsjahres. Geförderter Neubau des Referenzfalls: Endwert 9.477.900,38 Euro mit Verteilung der Entgelte gegen 9.478.243,94 Euro bei Abzug im Jahr der Zahlung, bei gleicher Rendite von 3,956 %. Bei der Privatperson mit steuerfreiem Verkauf mindert die Vorfälligkeitsentschädigung die Steuer nicht.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Steuerberater des Auftraggebers · **Wiedervorlage:** mit der Antwort des Steuerberaters; mit der Steuer in Grundform (Teil 2 der Fachspezifikation)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-7.2, R-7.11, R-7.15, R-7.17
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Steuerberater, Befund 5). Der Entwurf zog alle Finanzierungskosten im Jahr der Zahlung ab. Umschaltbar ist die Lesart zu den Entgelten; die beiden Punkte zur Privatperson sind fest gebaut und werden mit der Antwort des Steuerberaters überprüft. Prüfrunde 2 zur Fachspezifikation des Rechenkerns (2026-11-18) (Steuerberater 5): Laufzeitbezogene Entgelte werden auch bei der Privatperson verteilt (§ 11 Abs. 2 Satz 3 EStG); der Rundungsrest der Verteilung fällt ins Verkaufsjahr; das Entgelt auf den Zuschuss ist kein Entgelt für Schulden und folgt dem Zuschuss.

### MA-033 · Vorfälligkeitsentschädigung als Pauschale

- **Annahme:** Wird vor dem Ende der Zinsbindung verkauft, beträgt die Vorfälligkeitsentschädigung Restschuld mal Satz des Hauses mal Restbindung in Jahren. Die Restbindung endet spätestens mit dem gesetzlichen Kündigungsrecht des Darlehensnehmers. Für das NBank-Darlehen fällt keine Entschädigung an. Für das KfW-Darlehen fällt sie an wie für das Bankdarlehen, mit der Pauschale des Hauses; Teilrückzahlungen sind ausgeschlossen.
- **Warum offen:** Die Bank berechnet ihren Zinsschaden aus dem Vertragszins, dem Wiederanlagezins am Tag der Ablösung, ersparten Kosten und Sondertilgungsrechten. Das Zinsniveau beim Verkauf ist heute nicht bekannt.
- **Andere Lesart:** Zinsschadenrechnung der Bank: Die Entschädigung kann null sein, wenn das Zinsniveau beim Verkauf über dem Vertragszins liegt, oder über der Pauschale, wenn es darunter liegt.
- **Grundlage:** Anspruch der Bank nach § 490 Abs. 2 BGB und Kündigungsrecht nach zehn Jahren nach § 489 Abs. 1 Nr. 2 BGB, gelesen in der Prüfrunde (Bank, Fachexperte). Die Höhe der Pauschale ist Vorgabe des Hauses. Beim übernommenen Darlehen zählt die Frist des Kündigungsrechts ab dem Stichtag, weil das Datum des Empfangs keine Eingabe ist; das ist die längste Restbindung. KfW-Merkblatt 297/298 (Stand 07/2026), Abschnitt Tilgung: außerplanmäßige Tilgung nur vollständig und nur gegen Vorfälligkeitsentschädigung. Quellen: `BGB-489`, `BGB-490`, `KFW-297-298-MERKBLATT`.
- **Wirkung (mittel):** Endwert und Rendite bei Verkauf vor dem Ende einer Zinsbindung; Haltedauertabelle und Stressfälle mit kurzer Haltedauer. Ankauf des Referenzfalls mit Verkauf nach einem Jahr: 108.146,07 Euro bei 1.201.623,01 Euro Restschuld. Bei 40 Jahren Zinsbindung begrenzt das Kündigungsrecht die Restbindung auf 114 Monate: 114.154,19 Euro statt einer Pauschale über 39 Jahre. Neubau mit KfW-Darlehen, Verkauf nach acht Jahren bei zehn Jahren Zinsbindung: 35.411,17 Euro für das Bankdarlehen und 52.203,65 Euro für das KfW-Darlehen.
- **Sichtbar:** Anwendung · **Umschaltbar:** nein · **Klärung durch:** Hausbank · **Wiedervorlage:** nach dem Gespräch mit der Hausbank; Zinsschadenrechnung mit der Vollkalkulation (Teil 2 der Fachspezifikation)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-5.16, Vorgabe H-18
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Bank, Befund 5; Fachexperte, Befund 3; Grenzfälle, Befund 5): Kappung am Kündigungsrecht ergänzt, Gewicht von gering auf mittel gesetzt. Nicht umschaltbar, weil die andere Lesart das Zinsniveau beim Verkauf als Eingabe braucht; der Satz ist als Vorgabe des Hauses veränderbar. Prüfrunde 2 zur Fachspezifikation des Rechenkerns (2026-11-18) und Quellnotiz 13: Wortlaut berichtigt – nur das NBank-Darlehen bleibt ohne Entschädigung; das KfW-Darlehen trägt sie wie das Bankdarlehen. Der Rechenkern rechnete das schon so; neu ist der Beleg. Im Jahresmodus wird der Kündigungstermin auf ganze Perioden aufgerundet.

### MA-034 · Prolongation mit unverändertem Tilgungssatz

- **Annahme:** Nach dem Ende der Zinsbindung setzt die Bank die Rate neu aus der Restschuld, dem Anschlusszins und dem anfänglichen Tilgungssatz, mindestens der Mindesttilgung des Hauses. Für die KfW-Tranche ist die Anschlusskondition festgelegt: Prolongationsangebot ohne Zinsverbilligung aus Bundesmitteln. Anschlusszins also Marktzins nach H-05, nicht Programmzins.
- **Warum offen:** Wie prolongiert wird, vereinbaren Bank und Darlehensnehmer erst am Ende der Zinsbindung.
- **Andere Lesart:** Die bisherige Rate bleibt; oder die Restlaufzeit bleibt, und die Rate wird als Annuität über die verbleibende Laufzeit neu gerechnet. Beide sind als Vorgabe des Hauses wählbar.
- **Grundlage:** Übliche Praxis nach Einschätzung der Prüfer; für die KfW-Tranche das KfW-Merkblatt 297/298, Abschnitt Zinssatz. Die drei Regeln lassen sich nicht für jede Größe in dieselbe Reihenfolge bringen: Der unveränderte Tilgungssatz ergibt die niedrigste Rate und damit die höchste Deckung nach der Zinsbindung, aber die niedrigste Endwertdifferenz und den niedrigsten tragbaren Preis. Nach der Rangfolge der Vorsicht (tragbarer Preis vor Endwertdifferenz vor Rendite) ist er die vorsichtige Lesart. Damit er keine Unterdeckung verbirgt, weist das Blatt die kleinste Deckung zusätzlich nach der Regel mit der niedrigsten Deckung aus und meldet danach. Quellen: `KFW-297-298-MERKBLATT`.
- **Wirkung (mittel):** Rate, Restschuld und Deckung nach der Zinsbindung; Endwert nur gering. Ankauf des Referenzfalls: tragbarer Preis 2.317.235 Euro (Tilgungssatz bleibt) gegen 2.317.477 Euro (Rate bleibt) und 2.317.632 Euro (Restlaufzeit bleibt); Endwertdifferenz 753.701,96 Euro gegen 754.107,08 und 754.381,58 Euro; Deckung im Jahr 11 2,0853 gegen 1,8358 und 1,7002. Bei 3 % Zins und 0,5 % Mietsteigerung mit Vertragskonditionen: kleinste Deckung 1,3054 laut Finanzplan, 1,1975 nach der ungünstigsten Regel; im Stressfall 1,0181 gegen 0,8966.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Hausbank · **Wiedervorlage:** nach dem Gespräch mit der Hausbank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-5.8, R-5.9, R-10.14, Vorgabe H-07
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Bank, Frage 9; Controller, Befund 10). Die Regel „Restlaufzeit bleibt“ rundet die Restlaufzeit auf ganze Perioden ab und fällt ohne Tilgung auf den unveränderten Tilgungssatz zurück (Meldung). Prüfrunde 2 zur Fachspezifikation des Rechenkerns (2026-11-18) (Bank, Befund 3): Gewicht von gering auf mittel; Ausweis der kleinsten Deckung nach der ungünstigsten Anschlussregel. Quellnotiz 13: Anschlusskondition der KfW-Tranche aus dem Merkblatt belegt; der Rechenkern rechnete den Anschluss der KfW-Tranche schon mit dem Marktzins.

### MA-035 · CO2-Einstufung aus der Effizienzklasse

- **Annahme:** Ist der CO2-Ausstoß des Gebäudes nicht eingegeben, leitet der Katalog ihn aus Effizienzklasse und Energieträger ab und setzt den Ausstoß an der oberen Grenze der Klasse an.
- **Warum offen:** Der Anteil des Vermieters an den CO2-Kosten richtet sich nach dem Ausstoß in Kilogramm CO2 je Quadratmeter und Jahr. Die Effizienzklasse des Energieausweises beruht auf dem Energiebedarf oder -verbrauch und nicht auf dem Ausstoß; die Umrechnung über den Energieträger ist eine Näherung.
- **Andere Lesart:** Der tatsächliche Ausstoß aus der Heizkostenabrechnung; er ist als Eingabe vorgesehen und geht der Näherung vor.
- **Grundlage:** Stufen nach der Anlage zum Kohlendioxidkostenaufteilungsgesetz. Angesetzt ist der ungünstigere Fall innerhalb der Klasse. Quellen: `CO2KOSTAUFG-5`, `CO2KOSTAUFG-ANLAGE`.
- **Wirkung (gering):** Laufende Kosten des Vermieters im Bestand. Im Ankauf des Referenzfalls (30 kg je m², Vermieteranteil 40 %, 50 Euro je Tonne als Annahmen) 792 Euro im ersten Jahr bei 134.640 Euro Jahresmiete.
- **Sichtbar:** Anwendung · **Umschaltbar:** nein · **Klärung durch:** Anwender je Vorhaben (Heizkostenabrechnung des Verkäufers) · **Wiedervorlage:** mit der Vollkalkulation Ankauf Bestand (1b-1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-6.9, Eingabe E-34, Katalogwert KAT-09
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Fachexperte, Befund 6). Nicht umschaltbar: Die andere Lesart ist die Eingabe des Ausstoßes. Der CO2-Preis ist keine Modellannahme, sondern eine Vorgabe des Hauses.

### MA-036 · Objektverkauf der GmbH & Co. KG: laufender Gewinn oder Aufgabegewinn

- **Annahme:** Der Gewinn aus dem Verkauf des Objekts ist bei der Personengesellschaft laufender Gewinn und gehört in voller Höhe zum Gewerbeertrag; die Gewerbesteuer wird bei natürlichen Personen angerechnet.
- **Warum offen:** Hält die Gesellschaft nur dieses Objekt, kann der Verkauf die Aufgabe des Betriebs sein. Der Aufgabegewinn gehört nur insoweit zum Gewerbeertrag, als er nicht auf natürliche Personen als unmittelbar beteiligte Gesellschafter entfällt. Welcher Fall vorliegt, hängt vom Einzelfall und von der Rechtsprechung ab.
- **Andere Lesart:** Aufgabegewinn: Der Anteil des Verkaufsgewinns, der auf natürliche Personen entfällt, bleibt gewerbesteuerfrei. Umschaltbar.
- **Grundlage:** Wortlaut von § 7 Satz 2 GewStG; Einordnung als Einschätzung des Steuerberaters in der Prüfrunde. Voreingestellt ist der laufende Gewinn: Bis zu einem Hebesatz in Höhe des Anrechnungsfaktors ist das wegen der Anrechnung nahezu neutral, darüber die ungünstigere Lesart. Tarifermäßigungen für Aufgabegewinne rechnet die Kurzform nicht. Quellen: `GEWSTG-7`, `ESTG-35`, `ESTG-15`.
- **Wirkung (mittel):** Steuer im Verkaufsjahr bei Personengesellschaften mit natürlichen Personen als Gesellschaftern. Ankauf des Referenzfalls bei 440 % Hebesatz und 60 % natürlichen Personen: Rendite 3,324 % als laufender Gewinn gegen 3,487 % als Aufgabegewinn.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Steuerberater des Auftraggebers · **Wiedervorlage:** mit der Antwort des Steuerberaters; mit der Steuer in Grundform (Teil 2 der Fachspezifikation)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 1, Steuerstatus; Fachspezifikation Rechenkern, R-7.18
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Steuerberater, Befund 8).

### MA-037 · Kappungsspielraum bei unbekannter Mietenhistorie

- **Annahme:** Ist die Mietenhistorie nicht eingegeben, gilt die letzte Mieterhöhung als zum Stichtag erfolgt und die Kappungsgrenze als ausgeschöpft: Die erste Erhöhung fällt frühestens nach der Wartefrist und frühestens einen Monat nach Ablauf des Kappungszeitraums ab dem Stichtag.
- **Warum offen:** Wartefrist und Kappungsgrenze hängen davon ab, wann und um wie viel die Miete in den Jahren vor dem Ankauf erhöht wurde. Das Exposé nennt das in der Regel nicht; die Mieterliste liegt erst zur Vollkalkulation vor.
- **Andere Lesart:** Die letzte Erhöhung liegt mindestens den Kappungszeitraum zurück: Die Wartefrist ist abgelaufen, und die Kappungsgrenze steht voll zur Verfügung. Umschaltbar; mit eingegebener Mietenhistorie entfällt die Annahme.
- **Grundlage:** Wartefrist und Kappungsgrenze nach § 558 BGB, gelesen vom Fachexperten in der Prüfrunde; Werte je Gemeinde aus dem Katalog. Angesetzt ist der ungünstigere Fall. Quellen: `BGB-558`.
- **Wirkung (mittel):** Mietpfad der ersten Jahre im Bestand, Reinertrag, Verkaufspreis und höchster tragbarer Preis. Ankauf des Referenzfalls: höchster tragbarer Preis 2.317.235 Euro gegen 2.322.775 Euro in der anderen Lesart; dort steigt die Miete schon im Monat 13 statt im Monat 37.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Anwender je Vorhaben (Mieterliste des Verkäufers) · **Wiedervorlage:** mit der Mieterliste der Vollkalkulation Ankauf Bestand (1b-1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 2, Grobkalkulation; Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-6.3, Eingabe E-33
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Fachexperte, Befund 1; Praktiker, Befund 5). Der Entwurf führte die Miete linear zur Marktmiete und prüfte nur die Kappung gegen die Miete drei Jahre zuvor.

### MA-038 · Rückführung einer Miete über der Vergleichsmiete

- **Annahme:** Liegt die Ist-Miete über der ortsüblichen Vergleichsmiete, wird sie ab dem zweiten Planjahr über die Anpassungsdauer linear auf die Vergleichsmiete zurückgeführt; danach folgt sie der Vergleichsmiete.
- **Warum offen:** Das Gesetz senkt keine vereinbarte Miete. Ob eine Miete über der Vergleichsmiete hält, hängt von Mieterwechseln, von der Durchsetzbarkeit und vom Markt ab.
- **Andere Lesart:** Die Miete bleibt stehen, bis die Vergleichsmiete sie eingeholt hat. Umschaltbar.
- **Grundlage:** Einschätzung der Prüfer in Prüfrunde 2 zur Fachspezifikation (Fachexperte 4, Finanzmathematiker 3). Angesetzt ist die Lesart mit dem niedrigeren tragbaren Preis. Quellen: `BGB-558`.
- **Wirkung (gering):** Mieteinzahlungen, Verkaufspreis und tragbarer Preis, wenn die Ist-Miete über der Vergleichsmiete liegt. Referenzfall mit 11,00 Euro Ist-Miete gegen 9,20 Euro Vergleichsmiete: tragbarer Preis 2.424.974 Euro gegen 2.470.976 Euro, wenn die Miete stehen bleibt; Endwertdifferenz 831.335,64 Euro gegen 905.596,44 Euro.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Auftraggeber (Erfahrung aus dem Bestand) · **Wiedervorlage:** mit den Vorgaben des Hauses vor dem Einsatz von Teilschritt 1a
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 2, Grobkalkulation; Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-6.3
- **Bemerkung:** Aus Prüfrunde 2 zur Fachspezifikation des Rechenkerns (Sichtung, Punkt 14). In der Kapitaldienstrechnung der Bank zählt eine Miete über der Vergleichsmiete ohnehin nicht (MA-026).

### MA-039 · Fortgeltung der Gebietsverordnungen zu Kappungsgrenze und Mietpreisbremse

- **Annahme:** Gilt am Stichtag eine Verordnung zur abgesenkten Kappungsgrenze oder zur Mietpreisbremse, gilt sie nach ihrem Ablauf mit einer Folgeverordnung fort; das Geltungsende ist Katalogwert.
- **Warum offen:** Die Verordnungen sind befristet; ob das Land sie verlängert, ist eine Entscheidung der Zukunft. Das Gesetz lässt Verordnungen zur Mietpreisbremse spätestens Ende 2029 enden und begrenzt Kappungsverordnungen auf höchstens fünf Jahre.
- **Andere Lesart:** Die Verordnung endet mit ihrem Geltungsende; danach gilt die gesetzliche Kappungsgrenze, und die Mietpreisbremse entfällt. Umschaltbar.
- **Grundlage:** § 556d Abs. 2 und § 558 Abs. 3 BGB, gelesen in Prüfrunde 2 zur Fachspezifikation (Fachexperte 10). Angesetzt ist die Lesart mit dem niedrigeren tragbaren Preis. Vorsichtig ist sie nur, wo am Stichtag eine Verordnung gilt. Quellen: `BGB-556D`, `BGB-558`.
- **Wirkung (mittel):** Mietpfad nach dem Geltungsende, Verkaufspreis und tragbarer Preis. Ankauf des Referenzfalls: tragbarer Preis 2.317.235 Euro gegen 2.319.295 Euro ohne Fortgeltung; Endwertdifferenz 753.701,96 Euro gegen 757.210,62 Euro. Bei längerer Haltedauer und größerem Abstand zur Vergleichsmiete wächst die Wirkung.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Land als Verordnungsgeber; Beobachtung über den Katalog · **Wiedervorlage:** mit jeder neuen Gebietsverordnung des Landes; spätestens 2029
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 2, Grobkalkulation; Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-6.3, R-6.13, R-6.18
- **Bemerkung:** Aus Prüfrunde 2 zur Fachspezifikation des Rechenkerns (Sichtung, Punkt 17). Die Ausnahme der Mietpreisbremse für die Wohnung nach BGB-556F gilt dauerhaft; „liegt im Gebiet“ ist je Vorhaben überschreibbar. Das Geltungsende der niedersächsischen Verordnungen im Referenzkatalog ist eine Annahme und noch am Verordnungstext zu lesen.

### MA-040 · Beginn der tilgungsfreien Jahre des KfW-Darlehens

- **Annahme:** Die tilgungsfreien Anlaufjahre und die Laufzeit des KfW-Darlehens zählen ab dem ersten Abruf.
- **Warum offen:** Das Merkblatt nennt Laufzeitvarianten mit tilgungsfreien Anlaufjahren, sagt aber nicht, ob sie ab der Zusage, ab dem ersten Abruf oder ab der Bezugsfertigkeit zählen; die Konditionenübersicht der KfW ist nicht gelesen.
- **Andere Lesart:** Die Anlaufjahre zählen ab der Bezugsfertigkeit; die Tilgung beginnt dann später. Umschaltbar. Zählten sie ab der Zusage, begänne die Tilgung noch früher.
- **Grundlage:** KfW-Merkblatt 297/298, gelesen in Prüfrunde 2 zur Fachspezifikation (Fachexperte 1). Vorsichtig ist die Voreinstellung für die Deckung, weil die Tilgung früher beginnt. Nach der Rangfolge der Vorsicht ist sie es nicht: Der tragbare Grundstückspreis des Referenzfalls liegt mit ihr um 1.447 Euro höher. Die Voreinstellung ist deshalb als Ausnahme gekennzeichnet; sie folgt der Sichtung der Prüfrunde 2. Quellen: `KFW-297-298-MERKBLATT`.
- **Wirkung (mittel):** Tilgungsbeginn, Deckung der ersten Jahre und Bemessung des Bankdarlehens im Neubau mit KfW-Darlehen. Referenzfall: Tilgung ab Monat 20 gegen Monat 31; Deckung im ersten Jahr der Vollvermietung 1,3857 gegen 1,6583; tragbarer Grundstückspreis 1.197.094 Euro gegen 1.195.647 Euro.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Hausbank; KfW · **Wiedervorlage:** nach dem Gespräch mit der Hausbank; mit dem Lesen der Konditionenübersicht der KfW
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 2, Grobkalkulation; Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-5.10, R-5.19
- **Bemerkung:** Aus Prüfrunde 2 zur Fachspezifikation des Rechenkerns (Sichtung, Punkt 8). Der Zins des KfW-Darlehens ist Eingabe; der Katalogwert ist Platzhalter, solange die Konditionenübersicht nicht im Kataster gelesen ist.

### MA-041 · Vermietung von Verein und Stiftung als Vermögensverwaltung

- **Annahme:** Die Vermietung des Wohnungsbestands eines Vereins oder einer Stiftung ist Vermögensverwaltung: Es fällt keine Gewerbesteuer an, die Einkünfte werden nach dem Zahlungsprinzip ermittelt, und der Verkauf nach Ablauf der Frist für private Veräußerungsgeschäfte ist steuerfrei.
- **Warum offen:** Vereine und Stiftungen sind nicht kraft Rechtsform gewerblich. Ob ihre Vermietung im Einzelfall die Grenze zum wirtschaftlichen Geschäftsbetrieb oder zum Gewerbebetrieb überschreitet, hängt von Umfang und Zusatzleistungen ab.
- **Andere Lesart:** Die Vermietung ist gewerblich; dann gilt die Besteuerung der Körperschaft mit Gewerbesteuer. Nicht umschaltbar: Der Bearbeiter wählt in diesem Fall den Steuerstatus „Körperschaft“.
- **Grundlage:** § 1 Abs. 1 und § 8 Abs. 2 KStG, gelesen in Prüfrunde 2 zur Fachspezifikation (Steuerberater 3); im Übrigen dessen Einschätzung. Die Voreinstellung ist die günstigere Lesart; sie ist die Regel für den Steuerstatus, den der Bearbeiter gewählt hat, und der Steuerstatus ist seine Angabe. Der Freibetrag nach § 24 KStG ist vorsichtig nicht gerechnet. Quellen: `KSTG-1`, `KSTG-8`, `KSTG-24`.
- **Wirkung (gering):** Steuer, Endwert und Rendite beim Steuerstatus „Verein und Stiftung“. Ankauf des Referenzfalls: Rendite 5,520 % gegen 4,527 % bei Besteuerung als Körperschaft mit Gewerbesteuer.
- **Sichtbar:** Anwendung · **Umschaltbar:** nein · **Klärung durch:** Steuerberater des Auftraggebers · **Wiedervorlage:** mit der Antwort des Steuerberaters
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 2, Grobkalkulation; Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-7.1, R-7.17, R-9.5
- **Bemerkung:** Aus Prüfrunde 2 zur Fachspezifikation des Rechenkerns (Sichtung, Punkt 20). Die Fassung nach Prüfrunde 1 besteuerte den Verkaufsgewinn unabhängig von der Haltedauer und verteilte Entgelte wie im Betriebsvermögen.
