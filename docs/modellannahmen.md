# Modellannahmen

Verzeichnis der Annahmen über Recht, Förderpraxis und Methode, die sich vor dem Bau nicht klären lassen und auf denen das Modell trotzdem rechnet. Leser: Auftraggeber, Entwicklung, Prüfer. Die Regeln dazu stehen in `docs/spezifikation.md`, Kapitel „Modellannahmen“.

**Diese Datei wird erzeugt.** Gepflegt wird `docs/modellannahmen/annahmen.toml`; danach `python3 scripts/modellannahmen.py` ausführen.

**Stand:** 29 offene Annahmen, davon 6 mit hohem Gewicht · 0 erledigt

## Offene Annahmen

| Kennung | Thema | Gewicht | Sichtbar | Umschaltbar | Klärung durch | Wiedervorlage |
|---|---|---|---|---|---|---|
| `MA-001` | Rechenweise der NBank-Renditeprüfung | hoch | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-004` | KfW-Darlehen als Ersatz für Eigenmittel bei der NBank | hoch | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-012` | Rendite bei mehreren Einlagen und Entnahmen | hoch | Kundenbericht | nein | Fachliteratur (Grob im Original); fachliche Freigabe durch den Auftraggeber | mit der Fachspezifikation des Rechenkerns (Phase 1) |
| `MA-014` | Streuungen und Korrelationen der Simulation | hoch | Kundenbericht | ja | Auftraggeber (eigene Erfahrungswerte); später Marktdaten | vor Stufe 2 (Simulation) |
| `MA-016` | Verrechnung von Anlaufverlusten | hoch | Kundenbericht | ja | Anwender je Vorhaben; im Zweifel Steuerberater des Investors | mit der Fachspezifikation des Steuermoduls (Phase 1) |
| `MA-026` | Rechengrundlage des Bankdarlehens | hoch | Kundenbericht | ja | Hausbank; die Schwellen selbst (Beleihungsquote, Mindestdeckung, Mindesttilgung) sind Vorgaben des Hauses | mit den Vorgaben des Hauses vor dem Einsatz von Teilschritt 1a |
| `MA-002` | Tilgungsplan des NBank-Darlehens | mittel | Anwendung | ja | NBank | nach dem Gespräch mit der NBank; im Einzelfall der Bewilligungsbescheid |
| `MA-005` | Finanzierungskosten als zuwendungsfähige Kosten der NBank | mittel | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-006` | Aufteilung bei teilgeförderten Vorhaben | mittel | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-007` | Dauer des Drittmittelabzugs bei Mieterhöhungen auf die Vergleichsmiete | mittel | Kundenbericht | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-010` | Verlustverrechnung ab 2028 | mittel | Anwendung | ja | Projekt am Bundesgesetzblatt, Bestätigung durch den Steuerberater | mit der nächsten vierteljährlichen Rechtsprüfung |
| `MA-017` | Restwert bei laufender Bindung | mittel | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-022` | Leerstand beim Mieterwechsel und Sonderabschreibung | mittel | Anwendung | ja | Steuerberater | mit der Fachspezifikation des Steuermoduls (Phase 1) |
| `MA-023` | Kostenbasis der Baukostenobergrenze der Sonderabschreibung | mittel | Anwendung | ja | Steuerberater | mit der Fachspezifikation des Steuermoduls (Phase 1) |
| `MA-029` | Anknüpfung der De-minimis-Bindung der Sonderabschreibung | mittel | Anwendung | ja | Steuerberater | mit der Fachspezifikation des Steuermoduls (Phase 1) |
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
| `MA-028` | Zuzurechnende Sollzinsen in der VOFI-Gesamtkapitalrentabilität | gering | Anwendung | nein | Fachliteratur (Grob, Einführung in die Investitionsrechnung) | mit der Fachspezifikation des Kennzahlenblatts (Spezifikation Kapitel 3) |

Nach Klärungsweg:

- **Anwalt:** `MA-007`, `MA-008`, `MA-009`, `MA-018`, `MA-019`, `MA-024`, `MA-025`
- **Anwender je Vorhaben; im Zweifel Steuerberater des Investors:** `MA-016`
- **Auftraggeber (eigene Erfahrungswerte); später Marktdaten:** `MA-014`
- **Darlehensvertrag im Einzelfall:** `MA-013`
- **Fachliteratur (Endbericht im Volltext):** `MA-015`
- **Fachliteratur (Grob im Original); fachliche Freigabe durch den Auftraggeber:** `MA-012`
- **Fachliteratur (Grob, Einführung in die Investitionsrechnung):** `MA-028`
- **Fachliteratur (Grob, Einführung in die Investitionsrechnung) oder ein Hochschulskript, das die Regel wiedergibt:** `MA-027`
- **Hausbank; die Schwellen selbst (Beleihungsquote, Mindestdeckung, Mindesttilgung) sind Vorgaben des Hauses:** `MA-026`
- **NBank:** `MA-001`, `MA-002`, `MA-003`, `MA-004`, `MA-005`, `MA-006`, `MA-017`, `MA-020`
- **NBank (nur noch Bestätigung):** `MA-021`
- **Projekt am Bundesgesetzblatt, Bestätigung durch den Steuerberater:** `MA-010`
- **Steuerberater:** `MA-011`, `MA-022`, `MA-023`, `MA-029`

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

- **Annahme:** Das zinslose Darlehen wird in gleichbleibenden Jahresraten so getilgt, dass es nach 42 Jahren ab Vollauszahlung zurückgezahlt ist.
- **Warum offen:** Die Richtlinie nennt nur die Höchstlaufzeit; den Tilgungsplan setzt die NBank im Einzelfall fest. Ein fester Tilgungssatz steht nicht mehr in der Richtlinie.
- **Andere Lesart:** Fester Tilgungssatz mit Restschuld am Ende oder schnellere Tilgung nach Vorgabe der NBank.
- **Grundlage:** Richtlinie Mietwohnraum 2026: Rückzahlung binnen 42 Jahren. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`.
- **Wirkung (mittel):** Liquidität und Schuldendienstdeckung je Jahr; Endwert nur gering, weil das Darlehen 35 Jahre zinslos ist.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank; im Einzelfall der Bewilligungsbescheid
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regeln auf ungeklärter Grundlage

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
- **Sichtbar:** Kundenbericht · **Umschaltbar:** nein · **Klärung durch:** Fachliteratur (Grob im Original); fachliche Freigabe durch den Auftraggeber · **Wiedervorlage:** mit der Fachspezifikation des Rechenkerns (Phase 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 3, Ausschüttungen und Nachschüsse
- **Bemerkung:** Die genaue Formel ist in Phase 1 festzulegen und finanzmathematisch nachzurechnen.

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

- **Annahme:** Steuerliche Verluste des Vorhabens werden im Vorhaben vorgetragen und erst mit dessen späteren Gewinnen verrechnet.
- **Warum offen:** Ob ein Verlust sofort mit anderen Einkünften des Investors verrechnet werden kann, hängt von dessen übriger steuerlicher Lage ab, die das Werkzeug nicht kennt.
- **Andere Lesart:** Sofortige Verrechnung mit anderen Einkünften des Investors; die Steuerersparnis fließt dann im Verlustjahr zu.
- **Grundlage:** Verlustabzug nach § 10d EStG. Angesetzt ist der ungünstigere Fall. Quellen: `ESTG-10D`.
- **Wirkung (hoch):** Wert der beschleunigten Abschreibung und der Anlaufverluste im Neubau; Endwert und Rendite nach Steuern.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Anwender je Vorhaben; im Zweifel Steuerberater des Investors · **Wiedervorlage:** mit der Fachspezifikation des Steuermoduls (Phase 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 1, Steuerstatus
- **Bemerkung:** Aus Prüfrunde 3 (Fachexperte). Wird als Merkmal je Vorhaben geführt.

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
- **Grundlage:** NBank, Vordruck 4009 „Einfacher Verwendungsnachweis“ (Stand Juli 2026), Nummer 5.4, vom Juristen am 18.11.2026 gelesen: Der Zuwendungsempfänger erklärt, dass die zuwendungsfähigen Ausgaben keine Umsatzsteuer enthalten, soweit sie nach § 15 UStG als Vorsteuer abziehbar ist. Das setzt voraus, dass nicht abziehbare Umsatzsteuer zuwendungsfähig ist. Die Richtlinie verweist in Nummer 12.5 für den Verwendungsnachweis auf Nummer 6 ANBest-P. Die Voreinstellung ist damit die am Text gestützte Lesart und keine Ausnahme von der Vorsichtsregel. Die andere Lesart senkte die Förderung auf die Baukosten um bis zu einem Sechstel (19/119 der Bruttokosten), weniger, wenn die Bemessungsgrenze kappt; die umsatzsteuerfreien Grundstückskosten berührt sie nicht. Quellen: `NBANK-VORDR-4009`, `NBANK-RL-MIETWOHNRAUM-2026`, `NI-ANBEST-P`.
- **Wirkung (gering):** Höhe von Darlehen und Zuschuss; Finanzierungslücke.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank (nur noch Bestätigung) · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regel- und Förderkatalog
- **Bemerkung:** Aus der dritten Überarbeitung des Rechercheberichts; Größe der Wirkung und Klärungsweg nach Prüfrunde 4 (Finanzmathematiker, Jurist) berichtigt. Prüfrunde 5 (Jurist): Grundlage ist jetzt der Vordruck 4009; Gewicht von mittel auf gering gesetzt, die Einordnung als Ausnahme von der Vorsichtsregel entfällt.

### MA-022 · Leerstand beim Mieterwechsel und Sonderabschreibung

- **Annahme:** Ein Leerstand zwischen zwei Mietverhältnissen schadet der Sonderabschreibung nicht, solange die Vermietungsabsicht fortbesteht. Schädlich bleiben Selbstnutzung, unentgeltliche Überlassung, vorübergehende Beherbergung und die Aufgabe der Vermietungsabsicht.
- **Warum offen:** Das Gesetz verlangt, dass die Wohnung der entgeltlichen Überlassung zu Wohnzwecken dient; ob das einen Leerstand beim Mieterwechsel einschließt, ergibt sich aus der Verwaltungsauffassung, die nicht gelesen ist.
- **Andere Lesart:** Jeder Leerstand im Nutzungszeitraum nach § 7b, dem Jahr der Anschaffung oder Herstellung und den neun folgenden Jahren, löst die rückwirkende Versagung der Sonderabschreibung aus.
- **Grundlage:** § 7b Abs. 2 und 4 EStG: Das Gesetz stellt darauf ab, ob die Wohnung der entgeltlichen Überlassung zu Wohnzwecken dient, also auf ihre Zweckbestimmung (Einschätzung des Juristen am Wortlaut, Prüfrunden 3 und 4). Ausnahme von der Vorsichtsregel: Die ungünstige Lesart striche bei jedem Leerstandsstress die gesamte Sonderabschreibung und machte den Stressfall unbrauchbar. Quellen: `ESTG-7B`.
- **Wirkung (mittel):** Steuerzahlungen im Neubau mit Sonderabschreibung; Ergebnis im Stressfall Leerstand.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Steuerberater · **Wiedervorlage:** mit der Fachspezifikation des Steuermoduls (Phase 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regel- und Förderkatalog
- **Bemerkung:** Aus Prüfrunde 3 (Jurist) und der dritten Überarbeitung des Rechercheberichts; schädliche Nutzungen und Begriff „Nutzungszeitraum“ aus Prüfrunde 4 (Jurist).

### MA-023 · Kostenbasis der Baukostenobergrenze der Sonderabschreibung

- **Annahme:** Die Baukostenobergrenze der Sonderabschreibung wird bei Herstellung an derselben Kostensumme gemessen wie die Förderung der NBank, den Kostengruppen 200 bis 700. Beim Erwerb zählt der Gebäudeanteil des Kaufpreises nach der Kaufpreisaufteilung zuzüglich der anteiligen Erwerbsnebenkosten, ohne den Marktwertdeckel der NBank.
- **Warum offen:** Welche Kosten in die Grenze des § 7b EStG einzurechnen sind, beantwortet das Gesetz nicht nach Kostengruppen. Für die Anschaffung ist keine Kostensumme bestimmt; Kostengruppen gibt es beim Kauf vom Bauträger nicht.
- **Andere Lesart:** Strenger beim Erwerb: der Kaufpreis einschließlich Boden nebst Erwerbskosten; die Grenze würde häufiger überschritten. Enger bei Herstellung: eine Kostensumme ohne Außenanlagen oder Baunebenkosten; die Grenze würde seltener überschritten.
- **Grundlage:** § 7b Abs. 2 und 3 EStG messen die Anschaffungs- oder Herstellungskosten der begünstigten Wohnung. Bei Herstellung ist die weitere Kostensumme und damit der ungünstigere Fall angesetzt (Richtlinie Mietwohnraum 2026, Nummern 1.5 und 5.3.2). Beim Erwerb ist nicht die strengste Lesart angesetzt, sondern der Gebäudeanteil (Einschätzung des Juristen am Wortlaut, Prüfrunde 5): Grund und Boden ist ein eigenes, nicht abnutzbares Wirtschaftsgut und zählt auch bei der Herstellung nicht mit (Kostengruppe 100); dieselben Worte würden sonst für Bau und Kauf verschieden gelesen. Der Marktwertdeckel der NBank beim Ersterwerb stammt aus den Nummern 5.3.2.1 und 5.3.2.4 der Richtlinie und hat in § 7b keine Grundlage; ohne ihn greift die Grenze eher. Quellen: `ESTG-7B`, `NBANK-RL-MIETWOHNRAUM-2026`.
- **Wirkung (mittel):** Ob die Sonderabschreibung überhaupt gewährt wird; die Grenze ist eine Ausschlussgrenze.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Steuerberater · **Wiedervorlage:** mit der Fachspezifikation des Steuermoduls (Phase 1)
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regel- und Förderkatalog
- **Bemerkung:** Aus Prüfrunde 3 (Fachexperte) und der dritten Überarbeitung des Rechercheberichts; Ersterwerb aus Prüfrunde 4 (Jurist). Prüfrunde 5 (Jurist): beim Erwerb Gebäudeanteil statt Kaufpreis einschließlich Boden, ohne Marktwertdeckel. Offen bleibt, welche Gebäudekosten im Einzelnen zählen, etwa Außenanlagen.

### MA-024 · Zeitlicher Anwendungsbereich des Wärmepumpen-Nachweises

- **Annahme:** Für jede im Betrachtungszeitraum eingebaute Wärmepumpe ist der Nachweis der Jahresarbeitszahl erforderlich; ohne ihn wird nur die Hälfte der Kosten umgelegt.
- **Warum offen:** Für welche Einbauzeitpunkte und Mietverhältnisse die Vorschrift gilt, ist am Übergangsrecht nicht geprüft.
- **Andere Lesart:** Die Vorschrift gilt nur für bestimmte Zeiträume; außerhalb ist die volle Umlage ohne Nachweis möglich.
- **Grundlage:** § 559f BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `BGB-559F`.
- **Wirkung (gering):** Mieterlös nach Einbau einer Wärmepumpe.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regel- und Förderkatalog
- **Bemerkung:** Aus der dritten Überarbeitung des Rechercheberichts.

### MA-025 · Modernisierungsumlage für den Glasfaseranschluss

- **Annahme:** Für den erstmaligen Glasfaseranschluss wird keine Modernisierungsumlage angesetzt.
- **Warum offen:** Der Wortlaut steht in Spannung: § 559 Abs. 1 Satz 1 BGB nennt die Maßnahmen nach § 555b Nr. 1, 3, 4, 5 und 6, nicht Nr. 4a; Satz 2 regelt aber, wann die Erhöhung im Fall der Nr. 4a zulässig ist, und setzt ihre Umlage damit voraus.
- **Andere Lesart:** Nr. 4a ist umlagefähig, über Satz 2 oder weil der Anschluss den Gebrauchswert nach Nr. 4 erhöht: 8 % der Kosten, wenn der Mieter seinen Anbieter frei wählen kann und kein Bereitstellungsentgelt als Betriebskosten umgelegt wird oder wurde.
- **Grundlage:** § 555b Nr. 4a und § 559 Abs. 1 Satz 2 BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `BGB-555B`, `BGB-559`.
- **Wirkung (gering):** Mieterlös nach Glasfaserausbau.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Regel- und Förderkatalog
- **Bemerkung:** Aus Prüfrunde 3 (Jurist); Grund und andere Lesart nach Prüfrunde 4 (Jurist) neu gefasst. Frage an den Anwalt: Ist Nr. 4a über § 559 Abs. 1 Satz 2 oder über Nr. 4 umlagefähig?

### MA-026 · Rechengrundlage des Bankdarlehens

- **Annahme:** Die Bank rechnet über alle Darlehen: Die Beleihungsquote begrenzt die Summe aller Darlehen gegen den Wertansatz, und die Mindestdeckung rechnet aus dem Reinertrag im ersten Jahr der Vollvermietung gegen den Kapitaldienst aller Darlehen einschließlich eines Förderdarlehens oder übernommenen Darlehens. Wertansatz ist der Kaufpreis, beim Neubau die Gesamtkosten, nicht ein eigener Beleihungswert.
- **Warum offen:** Wie eine Bank Kapitaldienstfähigkeit und Beleihung im Einzelfall rechnet, ist nicht veröffentlicht und von Haus zu Haus verschieden: mit welchem Ertrag, ob vorrangige und geförderte Darlehen auf Quote und Deckung angerechnet werden und auf welchen Wert.
- **Andere Lesart:** Die Bank rechnet Beleihungsquote und Mindestdeckung nur für ihr eigenes Darlehen; dann fällt das Bankdarlehen neben einem Förderdarlehen oder übernommenen Darlehen höher aus. Oder sie setzt einen eigenen Wert an, etwa einen Beleihungswert unter dem Kaufpreis; dann fällt es niedriger aus.
- **Grundlage:** Gegenrechnungen der Prüfrunden 4 und 5 (Finanzmathematiker, Fachexperte, Praktiker). Bei Beleihungsquote und Mindestdeckung ist der ungünstigere Fall angesetzt; die andere Lesart ist umschaltbar. Begründete Ausnahme von der Vorsichtsregel beim Wertansatz: Voreingestellt ist der Kaufpreis, beim Neubau die Gesamtkosten, obwohl ein eigener Wert der Bank darunter liegen kann. Die Grobkalkulation kennt keinen Beleihungswert; die Ausnahme wirkt höchstens bis zum Darlehen nach Mindestdeckung, das aus dem Ertrag und nicht aus dem Gebot folgt. Der Wert ist als „Wertansatz der Bank“ überschreibbar, über dem Kaufpreis nur mit Begründung, und das Blatt zeigt, welche Grenze das Darlehen bestimmt.
- **Wirkung (hoch):** Höhe des Bankdarlehens und damit höchster tragbarer Preis, nötiges Eigenkapital und Rendite in der Grobkalkulation. Im geförderten Neubau und beim Ankauf gebundener Bestände entscheidet die Lesart über das Eigenkapital: im Beispiel des Berichts (Anhang D.4) über bis zu 1 Mio. Euro bei 10 Mio. Euro Gesamtkosten.
- **Sichtbar:** Kundenbericht · **Umschaltbar:** ja · **Klärung durch:** Hausbank; die Schwellen selbst (Beleihungsquote, Mindestdeckung, Mindesttilgung) sind Vorgaben des Hauses · **Wiedervorlage:** mit den Vorgaben des Hauses vor dem Einsatz von Teilschritt 1a
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 2, Grobkalkulation
- **Bemerkung:** Aus Prüfrunde 4 (Finanzmathematiker, Fachexperte, Praktiker). Prüfrunde 5: Bezug der Beleihungsquote auf die Summe aller Darlehen festgelegt, Gewicht von mittel auf hoch gesetzt, Wertansatz als Ausnahme von der Vorsichtsregel gekennzeichnet. Weitere Frage an die Hausbank: Rechnet sie den Reinertrag der Deckung mit eigenen Bewirtschaftungspauschalen statt mit den Kosten des Vorhabens?

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
- **Sichtbar:** Anwendung · **Umschaltbar:** nein · **Klärung durch:** Fachliteratur (Grob, Einführung in die Investitionsrechnung) · **Wiedervorlage:** mit der Fachspezifikation des Kennzahlenblatts (Spezifikation Kapitel 3)
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
