# Modellannahmen

Verzeichnis der Annahmen über Recht, Förderpraxis und Methode, die sich vor dem Bau nicht klären lassen und auf denen das Modell trotzdem rechnet. Leser: Auftraggeber, Entwicklung, Prüfer. Die Regeln dazu stehen in `docs/spezifikation.md`, Kapitel „Modellannahmen“.

**Diese Datei wird erzeugt.** Gepflegt wird `docs/modellannahmen/annahmen.toml`; danach `python3 scripts/modellannahmen.py` ausführen.

**Stand:** 20 offene Annahmen, davon 5 mit hohem Gewicht · 0 erledigt

## Offene Annahmen

| Kennung | Thema | Gewicht | Sichtbar | Umschaltbar | Klärung durch | Wiedervorlage |
|---|---|---|---|---|---|---|
| `MA-001` | Rechenweise der NBank-Renditeprüfung | hoch | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-004` | KfW-Darlehen als Ersatz für Eigenmittel bei der NBank | hoch | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-012` | Rendite bei mehreren Einlagen und Entnahmen | hoch | Kundenbericht | nein | Fachliteratur (Grob im Original); fachliche Freigabe durch den Auftraggeber | mit der Fachspezifikation des Rechenkerns (Phase 1) |
| `MA-014` | Streuungen und Korrelationen der Simulation | hoch | Kundenbericht | ja | Auftraggeber (eigene Erfahrungswerte); später Marktdaten | vor Stufe 2 (Simulation) |
| `MA-016` | Verrechnung von Anlaufverlusten | hoch | Kundenbericht | ja | Anwender je Vorhaben; im Zweifel Steuerberater des Investors | mit der Fachspezifikation des Steuermoduls (Phase 1) |
| `MA-002` | Tilgungsplan des NBank-Darlehens | mittel | Anwendung | ja | NBank | nach dem Gespräch mit der NBank; im Einzelfall der Bewilligungsbescheid |
| `MA-005` | Finanzierungskosten als zuwendungsfähige Kosten der NBank | mittel | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-006` | Aufteilung bei teilgeförderten Vorhaben | mittel | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-007` | Dauer des Drittmittelabzugs bei Mieterhöhungen auf die Vergleichsmiete | mittel | Kundenbericht | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-010` | Verlustverrechnung ab 2028 | mittel | Anwendung | ja | Steuerberater; Bundesgesetzblatt | mit der nächsten vierteljährlichen Rechtsprüfung |
| `MA-017` | Restwert bei laufender Bindung | mittel | Kundenbericht | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-003` | Zins des NBank-Darlehens ab dem 36. Jahr | gering | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |
| `MA-008` | Modernisierungsumlage für den Heizungstausch bei Staffelmiete | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-009` | Teilung der Bio-Brennstoffkosten im Neubau | gering | nur intern | nein | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-011` | Bagatellgrenze bei der Umsatzsteueroption | gering | Anwendung | ja | Steuerberater | vor Stufe 3 (Gewerbe) |
| `MA-013` | Rundung in Darlehensplänen | gering | nur intern | ja | Darlehensvertrag im Einzelfall | bei der ersten Parallelrechnung mit echten Darlehen (Abnahme Stufe 1) |
| `MA-015` | Modernisierungsumlage im Referenzfall IWU 2013 | gering | nur intern | nein | Fachliteratur (Endbericht im Volltext) | beim Anlegen des Abnahmetests (Phase 3) |
| `MA-018` | Ersatz eines Gaskessels als energetische Modernisierung | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-019` | Zinsverbilligte Darlehen bei der Umlage für den Heizungstausch | gering | Anwendung | ja | Anwalt | mit der Rechtsprüfung vor dem Kundeneinsatz |
| `MA-020` | Umlage für den Heizungstausch in der NBank-Bindung | gering | Anwendung | ja | NBank | nach dem Gespräch mit der NBank |

Nach Klärungsweg:

- **Anwalt:** `MA-007`, `MA-008`, `MA-009`, `MA-018`, `MA-019`
- **Anwender je Vorhaben; im Zweifel Steuerberater des Investors:** `MA-016`
- **Auftraggeber (eigene Erfahrungswerte); später Marktdaten:** `MA-014`
- **Darlehensvertrag im Einzelfall:** `MA-013`
- **Fachliteratur (Endbericht im Volltext):** `MA-015`
- **Fachliteratur (Grob im Original); fachliche Freigabe durch den Auftraggeber:** `MA-012`
- **NBank:** `MA-001`, `MA-002`, `MA-003`, `MA-004`, `MA-005`, `MA-006`, `MA-017`, `MA-020`
- **Steuerberater:** `MA-011`
- **Steuerberater; Bundesgesetzblatt:** `MA-010`

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
- **Verwendet in:** Spezifikation Kapitel 4, Fördermodul

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
- **Verwendet in:** Spezifikation Kapitel 4, Fördermodul

### MA-005 · Finanzierungskosten als zuwendungsfähige Kosten der NBank

- **Annahme:** Finanzierungskosten einschließlich Bauzeitzinsen gehören nicht zu den zuwendungsfähigen Kosten und sind zusätzlich zu finanzieren.
- **Warum offen:** Die gelesenen Unterlagen grenzen die zuwendungsfähigen Kosten nicht abschließend ab.
- **Andere Lesart:** Finanzierungskosten sind ganz oder teilweise zuwendungsfähig.
- **Grundlage:** Richtlinie Mietwohnraum 2026; Bemessung nach Herstellungskosten. Angesetzt ist der ungünstigere Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`.
- **Wirkung (mittel):** Höhe von Darlehen und Zuschuss; Finanzierungslücke in der Bauphase.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Fördermodul

### MA-006 · Aufteilung bei teilgeförderten Vorhaben

- **Annahme:** Kosten, Finanzierung und gemeinsame Erträge werden zwischen geförderten und frei finanzierten Wohnungen nach Wohnfläche aufgeteilt.
- **Warum offen:** Ob die NBank einen bestimmten Schlüssel verlangt, ist nicht geprüft; der Antragsvordruck wurde dafür nicht im Einzelnen gelesen.
- **Andere Lesart:** Aufteilung nach Wohnungszahl, nach tatsächlich zurechenbaren Kosten oder nach Vorgabe der NBank.
- **Grundlage:** Übliche Praxis der Kostenzuordnung; keine Fundstelle.
- **Wirkung (mittel):** Zuwendungsfähige Kosten des geförderten Teils und damit Förderhöhe; Rendite je Teil.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Fördermodul

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
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Steuerberater; Bundesgesetzblatt · **Wiedervorlage:** mit der nächsten vierteljährlichen Rechtsprüfung
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
- **Verwendet in:** Spezifikation Kapitel 4, Fördermodul
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
- **Andere Lesart:** Nur Zuschüsse werden abgezogen; der Zinsvorteil bleibt unberücksichtigt.
- **Grundlage:** § 559e Abs. 1 in Verbindung mit § 559a BGB. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `BGB-559E`, `BGB-559A`.
- **Wirkung (gering):** Mieterlös nach gefördertem Heizungstausch; gedeckelt auf 0,50 €/m² im Monat.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** Anwalt · **Wiedervorlage:** mit der Rechtsprüfung vor dem Kundeneinsatz
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Kopplungen
- **Bemerkung:** Aus Prüfrunde 3 (Jurist).

### MA-020 · Umlage für den Heizungstausch in der NBank-Bindung

- **Annahme:** Während der Mietbindung der NBank wird keine Umlage für den Heizungstausch angesetzt.
- **Warum offen:** Die Richtlinie lässt Mieterhöhungen in der Bindung nach bestimmten Vorschriften zu und nennt die neue Umlage für den Heizungstausch dabei nicht.
- **Andere Lesart:** Die Umlage ist auch in der Bindung zulässig, soweit die Höchstmiete eingehalten wird.
- **Grundlage:** Richtlinie Mietwohnraum 2026, Nummer 5.4.5. Angesetzt ist der für den Vermieter ungünstigere Fall. Quellen: `NBANK-RL-MIETWOHNRAUM-2026`, `BGB-559E`.
- **Wirkung (gering):** Mieterlös gebundener Wohnungen nach Heizungstausch.
- **Sichtbar:** Anwendung · **Umschaltbar:** ja · **Klärung durch:** NBank · **Wiedervorlage:** nach dem Gespräch mit der NBank
- **Status:** offen, gesetzt am 2026-11-18
- **Verwendet in:** Spezifikation Kapitel 4, Fördermodul
- **Bemerkung:** Aus Prüfrunde 3 (Jurist).
