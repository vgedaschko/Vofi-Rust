# Modellannahmen

Verzeichnis der Annahmen über Recht, Förderpraxis und Methode, die sich vor dem Bau nicht klären lassen und auf denen das Modell trotzdem rechnet. Leser: Auftraggeber, Entwicklung, Prüfer. Die Regeln dazu stehen in `docs/spezifikation.md`, Kapitel „Modellannahmen“.

**Diese Datei wird erzeugt.** Gepflegt wird `docs/modellannahmen/annahmen.toml`; danach `python3 scripts/modellannahmen.py` ausführen.

**Stand:** 37 offene Annahmen, davon 8 mit hohem Gewicht · 0 erledigt

## Offene Annahmen

| Kennung | Thema | Gewicht | Sichtbar | Umschaltbar | Klärung durch | Wiedervorlage |
|---|---|---|---|---|---|---|
| `MA-001` | Rechenweise der NBank-Renditeprüfung | hoch | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-004` | KfW-Darlehen als Ersatz für Eigenmittel bei der NBank | hoch | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-012` | Rendite bei mehreren Einlagen und Entnahmen | hoch | Kundenbericht | nein | Fachliteratur: Ropeter (1998), S. 186 ff. (`ROPETER-1998`); fachliche Freigabe durch den Auftraggeber | mit der Fachspezifikation des Rechenkerns (Phase 1) |
| `MA-014` | Streuungen und Korrelationen der Simulation | hoch | Kundenbericht | ja | Auftraggeber (eigene Erfahrungswerte); später Marktdaten | vor Stufe 2 (Simulation) |
| `MA-016` | Verrechnung von Anlaufverlusten | hoch | Kundenbericht | ja | Anwender je Vorhaben; im Zweifel Steuerberater des Investors | mit der Fachspezifikation des Steuermoduls (Phase 1) |
| `MA-026` | Rechengrundlage des Bankdarlehens | hoch | Kundenbericht | ja | Hausbank (zehn Fragen in der Fachspezifikation des Rechenkerns, Kapitel 16); die Schwellen selbst (Beleihungsquote, Mindestdeckung, Mindesttilgung, kalkulatorischer Zins) sind Vorgaben des Hauses | mit den Vorgaben des Hauses vor dem Einsatz von Teilschritt 1a |
| `MA-030` | Gewerbesteuer auf den Verkaufsgewinn bei erweiterter Kürzung | hoch | Kundenbericht | ja | Steuerberater des Auftraggebers | mit der Antwort des Steuerberaters; spätestens vor dem Einsatz von Teilschritt 1a |
| `MA-031` | Steuerliche Einordnung des NBank-Zuschusses | hoch | Kundenbericht | ja | Steuerberater des Auftraggebers; zur Praxis der Bewilligung die NBank | mit der Antwort des Steuerberaters; spätestens vor dem Förderteil (1c) |
| `MA-002` | Tilgungsplan des NBank-Darlehens | mittel | Anwendung | ja | NBank | nach dem Gespräch mit der NBank; im Einzelfall der Bewilligungsbescheid |
| `MA-005` | Finanzierungskosten als zuwendungsfähige Kosten der NBank | mittel | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-006` | Aufteilung bei teilgeförderten Vorhaben | mittel | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-007` | Dauer des Drittmittelabzugs bei Mieterhöhungen auf die Vergleichsmiete | mittel | Kundenbericht | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-010` | Verlustverrechnung ab 2028 | mittel | Anwendung | ja | Projekt am Bundesgesetzblatt, Bestätigung durch den Steuerberater | mit der nächsten vierteljährlichen Rechtsprüfung |
| `MA-017` | Restwert bei laufender Bindung | mittel | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-022` | Leerstand beim Mieterwechsel und Sonderabschreibung | mittel | Anwendung | ja | Steuerberater | mit der Fachspezifikation des Steuermoduls (Phase 1) |
| `MA-023` | Kostenbasis der Baukostenobergrenze der Sonderabschreibung | mittel | Anwendung | ja | Steuerberater | mit der Fachspezifikation des Steuermoduls (Phase 1) |
| `MA-029` | Anknüpfung der De-minimis-Bindung der Sonderabschreibung | mittel | Anwendung | ja | Steuerberater | mit der Fachspezifikation des Steuermoduls (Phase 1) |
| `MA-032` | Finanzierungskosten und Vorfälligkeit in der Steuer | mittel | Anwendung | ja | Steuerberater des Auftraggebers | mit der Antwort des Steuerberaters; mit der Steuer in Grundform (Teil 2 der Fachspezifikation) |
| `MA-033` | Vorfälligkeitsentschädigung als Pauschale | mittel | Anwendung | nein | Hausbank | nach dem Gespräch mit der Hausbank; Zinsschadenrechnung mit der Vollkalkulation (Teil 2 der Fachspezifikation) |
| `MA-036` | Objektverkauf der GmbH & Co. KG: laufender Gewinn oder Aufgabegewinn | mittel | Anwendung | ja | Steuerberater des Auftraggebers | mit der Antwort des Steuerberaters; mit der Steuer in Grundform (Teil 2 der Fachspezifikation) |
| `MA-037` | Kappungsspielraum bei unbekannter Mietenhistorie | mittel | Anwendung | ja | Anwender je Vorhaben (Mieterliste des Verkäufers) | mit der Mieterliste der Vollkalkulation Ankauf Bestand (1b-1) |
| `MA-003` | Zins des NBank-Darlehens ab dem 36. Jahr | gering | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-008` | Modernisierungsumlage für den Heizungstausch bei Staffelmiete | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-009` | Teilung der Bio-Brennstoffkosten im Neubau | gering | nur intern | nein | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-011` | Bagatellgrenze bei der Umsatzsteueroption | gering | Anwendung | ja | Steuerberater | vor Stufe 3 (Gewerbe) |
| `MA-013` | Rundung in Darlehensplänen | gering | nur intern | ja | Darlehensvertrag im Einzelfall | bei der ersten Parallelrechnung mit echten Darlehen (Abnahme Stufe 1) |
| `MA-015` | Modernisierungsumlage im Referenzfall IWU 2013 | gering | nur intern | nein | Fachliteratur (Endbericht im Volltext) | beim Anlegen des Abnahmetests (Phase 3) |
| `MA-018` | Ersatz eines Gaskessels als energetische Modernisierung | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-019` | Zinsverbilligte Darlehen bei der Umlage für den Heizungstausch | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-020` | Umlage für den Heizungstausch in der NBank-Bindung | gering | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-021` | Nicht abziehbare Vorsteuer als zuwendungsfähige Kosten der NBank | gering | Anwendung | ja | NBank (nur noch Bestätigung) | nach dem Gespräch mit der NBank |
| `MA-024` | Zeitlicher Anwendungsbereich des Wärmepumpen-Nachweises | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-025` | Modernisierungsumlage für den Glasfaseranschluss | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-027` | Rechenregel der VOFI-Amortisationsdauer | gering | Anwendung | ja | Fachliteratur (Grob, Einführung in die Investitionsrechnung) oder ein Hochschulskript, das die Regel wiedergibt | mit der Fachspezifikation des Kennzahlenblatts (Spezifikation Kapitel 3) |
| `MA-028` | Zuzurechnende Sollzinsen in der VOFI-Gesamtkapitalrentabilität | gering | Anwendung | nein | Fachliteratur: Grob, Einführung in die Investitionsrechnung, nach `SCHULTE-IMMOBILIENINVESTITION-2025` (S. 813) dort S. 140 f. | mit der Fachspezifikation des Kennzahlenblatts (Spezifikation Kapitel 3) |
| `MA-034` | Prolongation mit unverändertem Tilgungssatz | gering | Anwendung | ja | Hausbank | nach dem Gespräch mit der Hausbank |
| `MA-035` | CO2-Einstufung aus der Effizienzklasse | gering | Anwendung | nein | Anwender je Vorhaben (Heizkostenabrechnung des Verkäufers) | mit der Vollkalkulation Ankauf Bestand (1b-1) |

Nach Klärungsweg:

- **Anwalt:** `MA-007`, `MA-008`, `MA-009`, `MA-018`, `MA-019`, `MA-024`, `MA-025`
- **Anwender je Vorhaben (Heizkostenabrechnung des Verkäufers):** `MA-035`
- **Anwender je Vorhaben (Mieterliste des Verkäufers):** `MA-037`
- **Anwender je Vorhaben; im Zweifel Steuerberater des Investors:** `MA-016`
- **Auftraggeber (eigene Erfahrungswerte); später Marktdaten:** `MA-014`
- **Darlehensvertrag im Einzelfall:** `MA-013`
- **Fachliteratur (Endbericht im Volltext):** `MA-015`
- **Fachliteratur (Grob, Einführung in die Investitionsrechnung) oder ein Hochschulskript, das die Regel wiedergibt:** `MA-027`
- **Fachliteratur: Grob, Einführung in die Investitionsrechnung, nach `SCHULTE-IMMOBILIENINVESTITION-2025` (S. 813) dort S. 140 f.:** `MA-028`
- **Fachliteratur: Ropeter (1998), S. 186 ff. (`ROPETER-1998`); fachliche Freigabe durch den Auftraggeber:** `MA-012`
- **Hausbank:** `MA-033`, `MA-034`
- **Hausbank (zehn Fragen in der Fachspezifikation des Rechenkerns, Kapitel 16); die Schwellen selbst (Beleihungsquote, Mindestdeckung, Mindesttilgung, kalkulatorischer Zins) sind Vorgaben des Hauses:** `MA-026`
- **NBank:** `MA-001`, `MA-002`, `MA-003`, `MA-004`, `MA-005`, `MA-006`, `MA-017`, `MA-020`
- **NBank (nur noch Bestätigung):** `MA-021`
- **Projekt am Bundesgesetzblatt, Bestätigung durch den Steuerberater:** `MA-010`
- **Steuerberater:** `MA-011`, `MA-022`, `MA-023`, `MA-029`
- **Steuerberater des Auftraggebers:** `MA-030`, `MA-032`, `MA-036`
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

- **Annahme:** Das zinslose Darlehen wird in gleichbleibenden Raten so getilgt, dass es nach 42 Jahren zurückgezahlt ist. Die Raten fallen im Takt des Rechenrasters an, im Monatsraster also monatlich; Tilgung, zinslose Zeit und Bindung zählen ab dem Monat nach der Bauzeit.
- **Warum offen:** Die Richtlinie nennt nur die Höchstlaufzeit; den Tilgungsplan setzt die NBank im Einzelfall fest. Ein fester Tilgungssatz steht nicht mehr in der Richtlinie.
- **Andere Lesart:** Fester Tilgungssatz mit Restschuld am Ende oder schnellere Tilgung nach Vorgabe der NBank; Jahresraten statt Monatsraten; Beginn mit der Vollauszahlung statt mit der Bezugsfertigkeit.
- **Grundlage:** Richtlinie Mietwohnraum 2026: Rückzahlung binnen 42 Jahren. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`.
- **Wirkung (mittel):** Liquidität und Schuldendienstdeckung je Jahr; Endwert nur gering, weil das Darlehen 35 Jahre zinslos ist. Monatsraten statt Jahresraten ändern den Kapitaldienst des Jahres nicht, senken aber den laufenden Beitrag leicht, weil die Restschuld früher fällt. Im geförderten Neubau des Referenzfalls beträgt der Kapitaldienst des Förderdarlehens 150.431,28 Euro im ersten Jahr der Vollvermietung; er entscheidet mit darüber, dass kein Bankdarlehen bleibt.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank; im Einzelfall der Bewilligungsbescheid
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-5.11, R-11.14
- **Bemerkung:** Prüfrunde 1 zur Fachspezifikation des Rechenkerns (2026-11-18): Annahme auf Raten im Takt des Rasters umgestellt; der frühere Wortlaut nannte Jahresraten, der Kern rechnet im Monatsraster Monatsraten. Fragen an die NBank: Jahres- oder Monatsraten, Beginn mit Vollauszahlung oder Bezugsfertigkeit, Beginn der zinslosen Zeit.

### MA-003 · Zins des NBank-Darlehens ab dem 36. Jahr

- **Annahme:** Ab dem 36. Jahr wird das Darlehen mit dem Basiszinssatz zuzüglich 3 Prozentpunkten verzinst; den Basiszinssatz der fernen Jahre gibt der Anwender vor.
- **Warum offen:** Die Richtlinie nennt nur die Obergrenze „bis zu 3 Prozentpunkte über dem Basiszinssatz“; der tatsächliche Aufschlag wird erst dann festgelegt.
- **Andere Lesart:** Geringerer Aufschlag oder Fortführung zinslos.
- **Grundlage:** Richtlinie Mietwohnraum 2026; Basiszinssatz nach § 247 BGB. Angesetzt ist der ungünstigste zulässige Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `BGB-247`.
- **Wirkung (gering):** Zinsaufwand der Jahre 36 bis 42 auf die Restschuld.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 3, Zeithorizont

### MA-004 · KfW-Darlehen als Ersatz für Eigenmittel bei der NBank

- **Annahme:** Ein KfW-Darlehen zählt nicht als Eigenmittel; die geforderten 20 % sind aus Eigenkapital aufzubringen.
- **Warum offen:** Die Richtlinie erlaubt die Kombination mit anderen Fördermitteln, regelt aber nicht, ob sie auf die Eigenmittel angerechnet werden.
- **Andere Lesart:** Die NBank erkennt nachrangige Förderdarlehen ganz oder teilweise als Eigenmittelersatz an.
- **Grundlage:** Richtlinie Mietwohnraum 2026, Nummer 11.4; Antragsvordruck mit eigener Zeile für KfW-Darlehen. Angesetzt ist der ungünstigere Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `NBANK-VORDRUCK-1011`.
- **Wirkung (hoch):** Eigenkapitalbedarf und damit Eigenkapitalrendite und Finanzierbarkeit des Vorhabens.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Nummer 11.5 der Richtlinie spricht von „als Ersatz der Eigenmittel anerkannten Fremdmitteln“; das stützt die andere Lesart. Die vorsichtige Voreinstellung bleibt bis zum Gespräch mit der NBank.

### MA-005 · Finanzierungskosten als zuwendungsfähige Kosten der NBank

- **Annahme:** Finanzierungskosten einschließlich Bauzeitzinsen gehören nicht zu den zuwendungsfähigen Kosten und sind zusätzlich zu finanzieren.
- **Warum offen:** Die gelesenen Unterlagen grenzen die zuwendungsfähigen Kosten nicht abschließend ab.
- **Andere Lesart:** Finanzierungskosten sind ganz oder teilweise zuwendungsfähig.
- **Grundlage:** Richtlinie Mietwohnraum 2026; Bemessung nach Herstellungskosten. Angesetzt ist der ungünstigere Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`.
- **Wirkung (mittel):** Höhe von Darlehen und Zuschuss; Finanzierungslücke in der Bauphase.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage

### MA-006 · Aufteilung bei teilgeförderten Vorhaben

- **Annahme:** Kosten, Finanzierung und gemeinsame Erträge werden zwischen geförderten und frei finanzierten Wohnungen nach Wohnfläche aufgeteilt.
- **Warum offen:** Ob die NBank einen bestimmten Schlüssel verlangt, ist nicht geprüft; der Antragsvordruck wurde dafür nicht im Einzelnen gelesen.
- **Andere Lesart:** Aufteilung nach Wohnungszahl, nach tatsächlich zurechenbaren Kosten oder nach Vorgabe der NBank.
- **Grundlage:** Übliche Praxis der Kostenzuordnung; keine Fundstelle.
- **Wirkung (mittel):** Zuwendungsfähige Kosten des geförderten Teils und damit Förderhöhe; Rendite je Teil.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage

### MA-007 · Dauer des Drittmittelabzugs bei Mieterhöhungen auf die Vergleichsmiete

- **Annahme:** Fördermittel mindern Mieterhöhungen auf die ortsübliche Vergleichsmiete über den gesamten Betrachtungszeitraum.
- **Warum offen:** Das Gesetz nennt keine Dauer; Rechtsprechung dazu ist nicht geprüft.
- **Andere Lesart:** Der Abzug endet nach einer begrenzten Zeit, etwa mit dem Auslaufen des Förderzwecks oder nach einer von der Rechtsprechung gezogenen Frist.
- **Grundlage:** § 558 Abs. 5 in Verbindung mit § 559a BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `BGB-558`, `BGB-559A`.
- **Wirkung (mittel):** Mietpfad geförderter Sanierungen nach der ersten Erhöhung; Endwert und Rendite.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Kopplungen

### MA-008 · Modernisierungsumlage für den Heizungstausch bei Staffelmiete

- **Annahme:** Bei vereinbarter Staffelmiete ist während der Laufzeit der Staffeln keine Umlage für den Heizungstausch möglich.
- **Warum offen:** Der Ausschluss von Mieterhöhungen bei Staffelmiete nennt die neue Umlage für den Heizungstausch nicht ausdrücklich; ob er sie erfasst, ist offen.
- **Andere Lesart:** Die Umlage nach § 559e BGB ist neben der Staffelmiete zulässig.
- **Grundlage:** § 557a BGB und § 559e BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `BGB-557A`, `BGB-559E`.
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
- **Warum offen:** Der veröffentlichte Gesetzestext zeigt nur die heute geltende Fassung mit 70 %; die künftig geltende Fassung ist am Bundesgesetzblatt noch nicht gelesen.
- **Andere Lesart:** Es bleibt auch ab 2028 bei 70 %.
- **Grundlage:** § 10d EStG in der geltenden Fassung; die Befristung bis 2027 ist nur aus zweiter Hand belegt. Angesetzt ist der ungünstigere Fall. Quellen: `ESTG-10D`.
- **Wirkung (mittel):** Steuerzahlungen von Vorhaben mit Anlaufverlusten ab 2028.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Projekt am Bundesgesetzblatt, Bestätigung durch den Steuerberater · **Wiedervorlage:** mit der nächsten vierteljährlichen Rechtsprüfung
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regel- und Förderkatalog

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
- **Andere Lesart:** Sofortige Verrechnung: Der Investor hat im selben Jahr genug andere Gewinne derselben Steuerart im selben Steuersubjekt (Körperschaft oder Organkreis, Betrieb, andere Einkünfte der Privatperson); die Steuerersparnis fließt im Verlustjahr zu. Das Vorhaben gilt dann als Teil eines größeren Steuersubjekts: Freibetrag und Abrundung der Gewerbesteuer und der Freibetrag der Hinzurechnung gelten als verbraucht. Bei der Personengesellschaft gilt die Lesart nur für die Einkommensteuer; ihr Fehlbetrag der Gewerbesteuer wird immer vorgetragen.
- **Grundlage:** Verlustabzug nach § 10d EStG; Gewerbeverlust nach § 10a GewStG. Voreingestellt ist der Vortrag, weil das Werkzeug die übrige steuerliche Lage des Investors nicht kennt. Welche Lesart das Vorhaben günstiger rechnet, hängt vom Fall ab: Meist ist es die sofortige Verrechnung; im Ankauf des Referenzfalls ergibt sie 4,523 % gegen 4,527 % mit Vortrag, weil der Freibetrag der Hinzurechnung bei ihr als verbraucht gilt. Quellen: `ESTG-10D`, `GEWSTG-10A`.
- **Wirkung (hoch):** Wert der beschleunigten Abschreibung und der Anlaufverluste im Neubau; Endwert und Rendite nach Steuern.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Anwender je Vorhaben; im Zweifel Steuerberater des Investors · **Wiedervorlage:** mit der Fachspezifikation des Steuermoduls (Phase 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 1, Steuerstatus; Fachspezifikation Rechenkern, R-7.5, R-7.6, Eingabe E-44
- **Bemerkung:** Aus Prüfrunde 3 (Fachexperte). Wird als Merkmal je Vorhaben geführt. Prüfrunde 1 zur Fachspezifikation des Rechenkerns (2026-11-18, Steuerberater): Annahme über andere Gewinne ausdrücklich genannt; bei der Personengesellschaft keine sofortige Erstattung der Gewerbesteuer. Die Kurzform verrechnet Vorträge unbeschränkt; ein Vortrag über dem Sockelbetrag löst einen Hinweis aus (MA-010).

### MA-017 · Restwert bei laufender Bindung

- **Annahme:** Endet der Betrachtungszeitraum vor dem Ende der Bindung, wird der Verkaufswert aus der gebundenen Miete abgeleitet und das zinslose Förderdarlehen beim Verkauf abgelöst; ein anteilig zurückzuzahlender Zuschuss wird angesetzt.
- **Warum offen:** Ob ein Käufer Darlehen und Bindung übernehmen kann und zu welchen Bedingungen, ist mit der NBank nicht geklärt.
- **Andere Lesart:** Der Käufer übernimmt Darlehen und Bindung; der Vorteil des zinslosen Darlehens geht dann in den Kaufpreis ein.
- **Grundlage:** Richtlinie Mietwohnraum 2026: Bindung läuft bei vorzeitiger Rückzahlung fort, Zuschuss anteilig zurückzuzahlen. Angesetzt ist der ungünstigere Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`.
- **Wirkung (mittel):** Restwert und Endwert geförderter Vorhaben mit Verkauf vor Bindungsende.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Spezifikation Kapitel 3, Restwert
- **Bemerkung:** Aus Prüfrunde 3 (Fachexperte, Jurist).

### MA-018 · Ersatz eines Gaskessels als energetische Modernisierung

- **Annahme:** Der Ersatz eines Gaskessels durch einen neuen Gas- oder Ölkessel gilt nicht als energetische Modernisierung; ohne Förderfähigkeit wird keine Modernisierungsumlage angesetzt.
- **Warum offen:** Ob der bloße Kesseltausch Endenergie nachhaltig einspart und damit die allgemeine Umlage eröffnet, ist eine Auslegungsfrage des Einzelfalls.
- **Andere Lesart:** Der Tausch gilt als energetische Modernisierung; dann ist die allgemeine Umlage von 8 % möglich.
- **Grundlage:** § 555b Nr. 1 und § 559 BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `BGB-555B`, `BGB-559`.
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
- **Grundlage:** Richtlinie Mietwohnraum 2026, Nummer 5.4.5. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `BGB-559E`.
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
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank (nur noch Bestätigung) · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus der dritten Überarbeitung des Rechercheberichts; Größe der Wirkung und Klärungsweg nach Prüfrunde 4 (Finanzmathematiker, Jurist) berichtigt. Prüfrunde 5 (Jurist): Grundlage ist jetzt der Vordruck 4009; Gewicht von mittel auf gering gesetzt, die Einordnung als Ausnahme von der Vorsichtsregel entfällt.

### MA-022 · Leerstand beim Mieterwechsel und Sonderabschreibung

- **Annahme:** Ein Leerstand zwischen zwei Mietverhältnissen schadet der Sonderabschreibung nicht, solange die Vermietungsabsicht fortbesteht. Schädlich bleiben Selbstnutzung, unentgeltliche Überlassung, vorübergehende Beherbergung und die Aufgabe der Vermietungsabsicht.
- **Warum offen:** Das Gesetz verlangt, dass die Wohnung der entgeltlichen Überlassung zu Wohnzwecken dient; ob das einen Leerstand beim Mieterwechsel einschließt, ergibt sich aus der Verwaltungsauffassung, die nicht gelesen ist.
- **Andere Lesart:** Jeder Leerstand im Nutzungszeitraum nach § 7b, dem Jahr der Anschaffung oder Herstellung und den neun folgenden Jahren, löst die rückwirkende Versagung der Sonderabschreibung aus.
- **Grundlage:** § 7b Abs. 2 und 4 EStG: Das Gesetz stellt darauf ab, ob die Wohnung der entgeltlichen Überlassung zu Wohnzwecken dient, also auf ihre Zweckbestimmung (Einschätzung des Juristen am Wortlaut, Prüfrunden 3 und 4). Ausnahme von der Vorsichtsregel: Die ungünstige Lesart striche bei jedem Leerstandsstress die gesamte Sonderabschreibung und machte den Stressfall unbrauchbar. Quellen: `ESTG-7B`.
- **Wirkung (mittel):** Steuerzahlungen im Neubau mit Sonderabschreibung; Ergebnis im Stressfall Leerstand.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Steuerberater · **Wiedervorlage:** mit der Fachspezifikation des Steuermoduls (Phase 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus Prüfrunde 3 (Jurist) und der dritten Überarbeitung des Rechercheberichts; schädliche Nutzungen und Begriff „Nutzungszeitraum“ aus Prüfrunde 4 (Jurist).

### MA-023 · Kostenbasis der Baukostenobergrenze der Sonderabschreibung

- **Annahme:** Die Baukostenobergrenze der Sonderabschreibung wird bei Herstellung an derselben Kostensumme gemessen wie die Förderung der NBank, den Kostengruppen 200 bis 700. Beim Erwerb zählt der Gebäudeanteil des Kaufpreises nach der Kaufpreisaufteilung zuzüglich der anteiligen Erwerbsnebenkosten, ohne den Marktwertdeckel der NBank.
- **Warum offen:** Welche Kosten in die Grenze des § 7b EStG einzurechnen sind, beantwortet das Gesetz nicht nach Kostengruppen. Für die Anschaffung ist keine Kostensumme bestimmt; Kostengruppen gibt es beim Kauf vom Bauträger nicht.
- **Andere Lesart:** Strenger beim Erwerb: der Kaufpreis einschließlich Boden nebst Erwerbskosten; die Grenze würde häufiger überschritten. Enger bei Herstellung: eine Kostensumme ohne Außenanlagen oder Baunebenkosten; die Grenze würde seltener überschritten.
- **Grundlage:** § 7b Abs. 2 und 3 EStG messen die Anschaffungs- oder Herstellungskosten der begünstigten Wohnung. Bei Herstellung ist die weitere Kostensumme und damit der ungünstigere Fall angesetzt (Richtlinie Mietwohnraum 2026, Nummern 1.5 und 5.3.2). Beim Erwerb gilt eine begründete Ausnahme von der Vorsichtsregel: Angesetzt ist nicht die strengste Lesart, sondern der Gebäudeanteil (Einschätzung des Juristen am Wortlaut, Prüfrunde 5): Grund und Boden ist ein eigenes, nicht abnutzbares Wirtschaftsgut und zählt auch bei der Herstellung nicht mit (Kostengruppe 100); dieselben Worte würden sonst für Bau und Kauf verschieden gelesen. Der Marktwertdeckel der NBank beim Ersterwerb stammt aus den Nummern 5.3.2.1 und 5.3.2.4 der Richtlinie und hat in § 7b keine Grundlage; ohne ihn greift die Grenze eher. Quellen: `ESTG-7B`, `NBANK-RL-MIETWOHNRAUM-2026`.
- **Wirkung (mittel):** Ob die Sonderabschreibung überhaupt gewährt wird; die Grenze ist eine Ausschlussgrenze.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Steuerberater · **Wiedervorlage:** mit der Fachspezifikation des Steuermoduls (Phase 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus Prüfrunde 3 (Fachexperte) und der dritten Überarbeitung des Rechercheberichts; Ersterwerb aus Prüfrunde 4 (Jurist). Prüfrunde 5 (Jurist): beim Erwerb Gebäudeanteil statt Kaufpreis einschließlich Boden, ohne Marktwertdeckel. Offen bleibt, welche Gebäudekosten im Einzelnen zählen, etwa Außenanlagen.

### MA-024 · Zeitlicher Anwendungsbereich des Wärmepumpen-Nachweises

- **Annahme:** Für jede im Betrachtungszeitraum eingebaute Wärmepumpe ist der Nachweis der Jahresarbeitszahl erforderlich; ohne ihn wird nur die Hälfte der Kosten umgelegt.
- **Warum offen:** Für welche Einbauzeitpunkte und Mietverhältnisse die Vorschrift gilt, ist am Übergangsrecht nicht geprüft.
- **Andere Lesart:** Die Vorschrift gilt nur für bestimmte Zeiträume; außerhalb ist die volle Umlage ohne Nachweis möglich.
- **Grundlage:** § 559f BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `BGB-559F`.
- **Wirkung (gering):** Mieterlös nach Einbau einer Wärmepumpe.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus der dritten Überarbeitung des Rechercheberichts.

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

- **Annahme:** Offen ist an der Rechnung der Bank viererlei; voreingestellt ist jeweils die vorsichtige Lesart, außer beim Wertansatz. (1) Beleihungsraum: Das Förderdarlehen der Grobförderung und ein KfW-Darlehen belegen den Beleihungsraum der Bank; für ein übernommenes Darlehen ist der Rang Eingabe. (2) Kapitaldienst: Die Bank rechnet die Kapitaldienstfähigkeit kalkulatorisch, je Darlehen mit dem höheren Zins aus Vertragszins und kalkulatorischem Zins (Vorgabe des Hauses, voreingestellt der Anschlusszins) und mindestens der Mindesttilgung. (3) Ertrag: Sie setzt den nachhaltigen Reinertrag an, den kleineren Wert aus Miete und ortsüblicher Vergleichsmiete, mit Bewirtschaftungskosten mindestens nach dem Katalog. (4) Wertansatz ist der Kaufpreis, beim Neubau die Gesamtkosten, nicht ein eigener Beleihungswert. Keine Annahme, sondern Festlegung ist, dass die Mindestdeckung immer über den Kapitaldienst aller Darlehen rechnet.
- **Warum offen:** Wie eine Bank Kapitaldienstfähigkeit und Beleihung im Einzelfall rechnet, ist nicht veröffentlicht und von Haus zu Haus verschieden: mit welchem Ertrag, ob vorrangige und geförderte Darlehen auf Quote und Deckung angerechnet werden und auf welchen Wert.
- **Andere Lesart:** (1) Das Förderdarlehen steht im Nachrang und belegt den Beleihungsraum nicht. (2) Die Bank rechnet mit den Vertragskonditionen. (3) Sie setzt Ertrag und Bewirtschaftung des Vorhabens an. Alle drei sind umschaltbar und lassen das Bankdarlehen höher ausfallen. (4) Die Bank setzt einen Beleihungswert unter dem Kaufpreis an; dann fällt das Darlehen niedriger aus.
- **Grundlage:** Gegenrechnungen der Prüfrunden 4 und 5 zum Recherchebericht und der Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Rolle Bank). Bewirtschaftungsansatz nach der Beleihungswertermittlungsverordnung. Begründete Ausnahme von der Vorsichtsregel beim Wertansatz: Voreingestellt ist der Kaufpreis, beim Neubau die Gesamtkosten ohne Bauzeitzinsen, obwohl ein eigener Wert der Bank darunter liegen kann. Die Grobkalkulation kennt keinen Beleihungswert; die Ausnahme wirkt höchstens bis zum Darlehen nach Mindestdeckung, das aus dem Ertrag und nicht aus dem Gebot folgt. Der Wert ist als „Wertansatz der Bank“ überschreibbar, über dem Kaufpreis nur mit Begründung, und das Blatt zeigt, welche Grenze das Darlehen bestimmt. Quellen: `BELWERTV-11`.
- **Wirkung (hoch):** Höhe des Bankdarlehens und damit höchster tragbarer Preis, nötiges Eigenkapital und Rendite in der Grobkalkulation. Ankauf des Referenzfalls: Bankdarlehen 1.226.609,99 Euro kalkulatorisch gegen 1.431.044,99 Euro mit Vertragskonditionen; höchster tragbarer Preis 2.317.235 Euro gegen 2.359.366 Euro. Bei einer Ist-Miete über der Vergleichsmiete 1.355.969,99 Euro gegen 1.560.000,00 Euro mit dem Ertrag des Vorhabens. Neubau mit KfW-Darlehen: tragbarer Grundstückspreis 924.244 Euro gegen 1.286.380 Euro mit Vertragskonditionen. Im geförderten Neubau des Referenzfalls bleibt in jeder Lesart des Beleihungsraums kein Bankdarlehen, weil die Deckung bindet.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Hausbank (zehn Fragen in der Fachspezifikation des Rechenkerns, Kapitel 16); die Schwellen selbst (Beleihungsquote, Mindestdeckung, Mindesttilgung, kalkulatorischer Zins) sind Vorgaben des Hauses · **Wiedervorlage:** mit den Vorgaben des Hauses vor dem Einsatz von Teilschritt 1a
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 2, Grobkalkulation; Fachspezifikation Rechenkern, R-5.12, R-5.19, R-11.14, R-11.15
- **Bemerkung:** Aus Prüfrunde 4 (Finanzmathematiker, Fachexperte, Praktiker). Prüfrunde 5: Bezug der Beleihungsquote auf die Summe aller Darlehen festgelegt, Gewicht von mittel auf hoch gesetzt, Wertansatz als Ausnahme von der Vorsichtsregel gekennzeichnet. Prüfrunde 1 zur Fachspezifikation des Rechenkerns (2026-11-18, Bank und Praktiker): neu geschnitten. Die Deckung über alle Darlehen ist jetzt Festlegung; der frühere Schalter verband Beleihungsraum und Deckung. Neu als vorsichtige Voreinstellung: kalkulatorischer Kapitaldienst und nachhaltiger Reinertrag; der Entwurf rechnete mit Vertragszins und dem Ertrag des Vorhabens.

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

- **Annahme:** Die De-minimis-Bindung der Sonderabschreibung knüpft an die Person an: Gebunden ist jeder Anspruchsberechtigte, der Einkünfte aus Land- und Forstwirtschaft, Gewerbebetrieb oder selbständiger Arbeit hat, auch wenn die Wohnung nicht zu diesen Einkünften gehört. Das gilt auch für die Privatperson mit Praxis oder Gewerbe und für die Kapitalgesellschaft als Gesellschafterin einer vermögensverwaltenden Personengesellschaft. Das Merkmal wird am Investor geführt, bei Personengesellschaften je Gesellschafter.
- **Warum offen:** § 7b Abs. 5 Satz 2 EStG wendet die Bindung an „nur bei Anspruchsberechtigten mit Einkünften im Sinne der §§ 13, 15 und 18“. Der Satz knüpft an die Person an und sagt nicht, dass die Wohnung selbst zu diesen Einkünften gehören muss. Die Verwaltungsauffassung dazu ist nicht gelesen.
- **Andere Lesart:** Gebunden ist nur, wessen Wohnung zu diesen Einkünften gehört. Privatpersonen und vermögensverwaltende Personengesellschaften wären dann auch frei, wenn der Investor daneben eine Praxis oder ein Gewerbe hat; die Sonderabschreibung liefe bei ihnen ohne De-minimis-Prüfung.
- **Grundlage:** § 7b Abs. 5 Satz 2 EStG, Einschätzung des Juristen am Wortlaut (Prüfrunde 5). Körperschaften nach § 1 Abs. 1 Nr. 1 bis 3 KStG sind nach beiden Lesarten gebunden, weil alle ihre Einkünfte als gewerblich gelten (§ 8 Abs. 2 KStG), auch für ihren Anteil an einer vermögensverwaltenden Personengesellschaft. Angesetzt ist die weitere Bindung und damit der ungünstigere Fall. Quellen: `ESTG-7B`, `KSTG-8`.
- **Wirkung (mittel):** Ob die Sonderabschreibung eines Investors mit solchen Einkünften an der De-minimis-Höchstgrenze endet; Steuerzahlungen und Rendite nach Steuern im Neubau.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Steuerberater · **Wiedervorlage:** mit der Fachspezifikation des Steuermoduls (Phase 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage
- **Bemerkung:** Aus Prüfrunde 5 (Jurist, Befund 1; Sichtung, Punkt 12).

### MA-030 · Gewerbesteuer auf den Verkaufsgewinn bei erweiterter Kürzung

- **Annahme:** Bei gesetztem Kennzeichen „erweiterte Grundstückskürzung“ unterliegt der Gewinn aus dem Verkauf des Objekts der Gewerbesteuer. Gekürzt wird nur der laufende Ertrag aus Verwaltung und Nutzung des Grundbesitzes.
- **Warum offen:** Das Gesetz kürzt um den Teil des Gewerbeertrags, der auf die Verwaltung und Nutzung des eigenen Grundbesitzes entfällt. Ob der Gewinn aus dem Verkauf des Objekts dazu gehört, sagt der Wortlaut nicht; es hängt von Rechtsprechung und vom Einzelfall ab, etwa davon, ob der Verkauf Teil der Vermögensverwaltung ist.
- **Andere Lesart:** Der Verkaufsgewinn gehört zum gekürzten Ertrag und bleibt gewerbesteuerfrei.
- **Grundlage:** Wortlaut von § 9 Nr. 1 Satz 2 GewStG, gelesen vom Steuerberater in der Prüfrunde; Rechtsprechung zur Kürzung im Veräußerungsjahr nicht gelesen. Angesetzt ist der ungünstigere Fall. Keine Annahme, sondern am Wortlaut belegt ist, dass Zinserträge nicht gekürzt werden. Quellen: `GEWSTG-9`, `GEWSTG-7`.
- **Wirkung (hoch):** Steuer im Verkaufsjahr, Endwert, Rendite und höchster tragbarer Preis bei Körperschaften und gewerblich geprägten Personengesellschaften mit Kennzeichen. Ankauf des Referenzfalls: Rendite 4,697 % gegen 5,161 % in der anderen Lesart; Steuer auf den Verkaufsgewinn 245.386,69 Euro gegen 105.456,69 Euro, also 139.930,00 Euro mehr.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Steuerberater des Auftraggebers · **Wiedervorlage:** mit der Antwort des Steuerberaters; spätestens vor dem Einsatz von Teilschritt 1a
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 1, Steuerstatus; Spezifikation Kapitel 2, Grobkalkulation; Fachspezifikation Rechenkern, R-7.8, R-7.14, R-7.17
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Steuerberater, Befund 1). Der Entwurf hatte mit dem Kennzeichen den ganzen Gewerbeertrag freigestellt; das war eine nicht gekennzeichnete Ausnahme von der Vorsichtsregel.

### MA-031 · Steuerliche Einordnung des NBank-Zuschusses

- **Annahme:** Der Zuschuss der Wohnraumförderung ist im Jahr des Zuflusses steuerpflichtige Einnahme; Abschreibungsgrundlage und Boden bleiben ungemindert, eine Rückzahlung beim Verkauf mindert den Verkaufsgewinn.
- **Warum offen:** Für Investitionszuschüsse lässt die Verwaltung im Betriebsvermögen ein Wahlrecht zwischen Einnahme und Minderung der Herstellungskosten zu; ein Zuschuss, der an eine langjährige Belegungs- und Mietbindung geknüpft ist, kann auch als Entgelt für die Bindung gelten und wäre dann über die Bindung zu verteilen. Welche Einordnung für den Zuschuss der NBank gilt, ist nicht geklärt.
- **Andere Lesart:** Einnahme, verteilt über die Dauer der Bindung; oder Minderung der Herstellungskosten, wobei nur der Anteil des Zuschusses, der auf das Gebäude entfällt, die Abschreibungsgrundlage mindert. Beide Lesarten sind gebaut und umschaltbar.
- **Grundlage:** Einschätzung des Steuerberaters in der Prüfrunde; die Verwaltungsanweisungen zu Zuschüssen sind nicht gelesen. Voreingestellt ist die Lesart mit der niedrigsten Endwertdifferenz und Rendite. Ihr Endwert ist der höchste der drei, weil die frühe Steuer als Nachschuss das eingesetzte Eigenkapital erhöht; der Endwert ist deshalb nicht der Maßstab. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `ESTG-11`, `ESTG-7`.
- **Wirkung (hoch):** Steuer der Bauzeit und der Bindung, Eigenkapitalbedarf, Endwertdifferenz und Rendite im geförderten Neubau. Referenzfall mit 38 Jahren Haltedauer: Rendite 3,558 % bei sofortiger Einnahme gegen 3,973 % (verteilt) und 3,974 % (Minderung); Endwertdifferenz 5.305.318,55 Euro gegen 5.700.811,35 und 5.706.360,57 Euro; Eigenkapital der Investitionsphase 2.444.791,88 Euro gegen 2.121.717,82 Euro bei Verteilung. Mit 20 Jahren: 1,675 % gegen 2,137 %.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Steuerberater des Auftraggebers; zur Praxis der Bewilligung die NBank · **Wiedervorlage:** mit der Antwort des Steuerberaters; spätestens vor dem Förderteil (1c)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-7.3, R-7.4, R-7.19, R-11.14
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Steuerberater, Befund 6; Grenzfälle, Befund 9). Der Entwurf minderte die Abschreibungsgrundlage um den ganzen Zuschuss, auch um den Anteil, der auf das Grundstück entfällt. Übersteigt der Zuschuss die Kosten, auf die er entfällt, rechnet der Kern nicht (Meldung).

### MA-032 · Finanzierungskosten und Vorfälligkeit in der Steuer

- **Annahme:** Die Entgelte der NBank auf Darlehen und Zuschuss gelten als laufzeitbezogen und werden im Betriebsvermögen über die Zinsbindung verteilt. Ein Disagio der Privatperson gilt als marktüblich und ist im Jahr der Zahlung abziehbar. Die Vorfälligkeitsentschädigung der Privatperson beim Verkauf gilt als Veräußerungskosten: Sie mindert nur einen steuerpflichtigen Verkaufsgewinn und nicht die Einkünfte aus Vermietung.
- **Warum offen:** Belegt ist, dass laufzeitbezogene Entgelte im Betriebsvermögen abzugrenzen sind und dass die Privatperson Ausgaben im Jahr der Zahlung abzieht, ein marktübliches Disagio eingeschlossen. Offen ist, ob die Entgelte der NBank laufzeitbezogen sind, wann ein Disagio marktüblich ist und wie die Vorfälligkeitsentschädigung der Privatperson beim Verkauf einzuordnen ist; das hängt an Verwaltungsauffassung und Rechtsprechung, die nicht gelesen sind.
- **Andere Lesart:** Entgelte der NBank sind im Jahr der Zahlung abziehbar (umschaltbar). Ein Disagio der Privatperson ist zu verteilen. Die Vorfälligkeitsentschädigung der Privatperson ist Werbungskosten aus Vermietung.
- **Grundlage:** Rechnungsabgrenzung nach § 5 Abs. 5 EStG und Abflussprinzip nach § 11 Abs. 2 EStG, gelesen vom Steuerberater in der Prüfrunde; im Übrigen dessen Einschätzung. Angesetzt ist jeweils der ungünstigere Fall. Quellen: `ESTG-5`, `ESTG-11`, `ESTG-23`.
- **Wirkung (mittel):** Zeitpunkt des Abzugs und damit Steuer der ersten Jahre und des Verkaufsjahres. Geförderter Neubau des Referenzfalls: Rendite 3,558 % mit Verteilung der Entgelte gegen 3,573 % bei Abzug im Jahr der Zahlung; Endwertdifferenz 5.305.318,55 Euro gegen 5.321.983,34 Euro. Bei der Privatperson mit steuerfreiem Verkauf mindert die Vorfälligkeitsentschädigung keine Steuer.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Steuerberater des Auftraggebers · **Wiedervorlage:** mit der Antwort des Steuerberaters; mit der Steuer in Grundform (Teil 2 der Fachspezifikation)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-7.2, R-7.11, R-7.15
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Steuerberater, Befund 5). Der Entwurf zog alle Finanzierungskosten im Jahr der Zahlung ab. Umschaltbar ist die Lesart zu den Entgelten; die beiden Punkte zur Privatperson sind fest gebaut und werden mit der Antwort des Steuerberaters überprüft.

### MA-033 · Vorfälligkeitsentschädigung als Pauschale

- **Annahme:** Wird vor dem Ende der Zinsbindung verkauft, beträgt die Vorfälligkeitsentschädigung Restschuld mal Satz des Hauses mal Restbindung in Jahren. Die Restbindung endet spätestens mit dem gesetzlichen Kündigungsrecht des Darlehensnehmers; für Förderdarlehen fällt keine Entschädigung an.
- **Warum offen:** Die Bank berechnet ihren Zinsschaden aus dem Vertragszins, dem Wiederanlagezins am Tag der Ablösung, ersparten Kosten und Sondertilgungsrechten. Das Zinsniveau beim Verkauf ist heute nicht bekannt.
- **Andere Lesart:** Zinsschadenrechnung der Bank: Die Entschädigung kann null sein, wenn das Zinsniveau beim Verkauf über dem Vertragszins liegt, oder über der Pauschale, wenn es darunter liegt.
- **Grundlage:** Anspruch der Bank nach § 490 Abs. 2 BGB und Kündigungsrecht nach zehn Jahren nach § 489 Abs. 1 Nr. 2 BGB, gelesen in der Prüfrunde (Bank, Fachexperte). Die Höhe der Pauschale ist Vorgabe des Hauses. Beim übernommenen Darlehen zählt die Frist des Kündigungsrechts ab dem Stichtag, weil das Datum des Empfangs keine Eingabe ist; das ist die längste Restbindung. Quellen: `BGB-489`, `BGB-490`.
- **Wirkung (mittel):** Endwert und Rendite bei Verkauf vor dem Ende einer Zinsbindung; Haltedauertabelle und Stressfälle mit kurzer Haltedauer. Ankauf des Referenzfalls mit Verkauf nach einem Jahr: 108.146,07 Euro bei 1.201.623,01 Euro Restschuld. Bei 40 Jahren Zinsbindung begrenzt das Kündigungsrecht die Restbindung auf 114 Monate: 114.154,19 Euro statt einer Pauschale über 39 Jahre.
- **Sichtbar:** Anwendung · **Umschaltbar:** nein · **Klärung durch:** Hausbank · **Wiedervorlage:** nach dem Gespräch mit der Hausbank; Zinsschadenrechnung mit der Vollkalkulation (Teil 2 der Fachspezifikation)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-5.16, Vorgabe H-18
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Bank, Befund 5; Fachexperte, Befund 3; Grenzfälle, Befund 5): Kappung am Kündigungsrecht ergänzt, Gewicht von gering auf mittel gesetzt. Nicht umschaltbar, weil die andere Lesart das Zinsniveau beim Verkauf als Eingabe braucht; der Satz ist als Vorgabe des Hauses veränderbar.

### MA-034 · Prolongation mit unverändertem Tilgungssatz

- **Annahme:** Nach dem Ende der Zinsbindung setzt die Bank die Rate neu aus der Restschuld, dem Anschlusszins und dem anfänglichen Tilgungssatz, mindestens der Mindesttilgung des Hauses.
- **Warum offen:** Wie prolongiert wird, vereinbaren Bank und Darlehensnehmer erst am Ende der Zinsbindung.
- **Andere Lesart:** Die bisherige Rate bleibt; oder die Restlaufzeit bleibt, und die Rate wird als Annuität über die verbleibende Laufzeit neu gerechnet. Beide sind als Vorgabe des Hauses wählbar.
- **Grundlage:** Übliche Praxis nach Einschätzung der Prüfer. Begründete Ausnahme von der Vorsichtsregel: Die drei Regeln lassen sich nicht in eine feste Reihenfolge bringen. Der unveränderte Tilgungssatz ergibt die niedrigste Rate und damit die höchste Deckung nach der Zinsbindung, aber die niedrigste Endwertdifferenz. Für die Endwertdifferenz ist die Voreinstellung die vorsichtige Lesart, für die Deckung nicht; deshalb weist das Blatt die Deckung nach jeder Zinsbindung eigens aus.
- **Wirkung (gering):** Rate, Restschuld und Deckung nach der Zinsbindung; Endwert nur gering. Ankauf des Referenzfalls, Endwertdifferenz und Deckung im Jahr 11: Tilgungssatz bleibt 753.701,96 Euro und 2,0853; Rate bleibt 754.107,08 Euro und 1,8358; Restlaufzeit bleibt 754.381,58 Euro und 1,7002.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Hausbank · **Wiedervorlage:** nach dem Gespräch mit der Hausbank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage; Fachspezifikation Rechenkern, R-5.9, Vorgabe H-07
- **Bemerkung:** Aus Prüfrunde 1 zur Fachspezifikation des Rechenkerns (Bank, Frage 9; Controller, Befund 10). Die Regel „Restlaufzeit bleibt“ rundet die Restlaufzeit auf ganze Perioden ab und fällt ohne Tilgung auf den unveränderten Tilgungssatz zurück (Meldung).

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
