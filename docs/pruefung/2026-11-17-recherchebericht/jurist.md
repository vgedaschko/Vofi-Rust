Rolle: Jurist (Immobilien- und Wohnungswirtschaftsrecht; Rechtsrisiken des Werkzeugs)
Prüfobjekt: `reports/VOFI Immobiliensoftware Marktrecherche.md` (Stand 17.11.2026), vollständig gelesen; Abgleich mit `research_notes/…/07` und `…/08`
Gesamturteil: Trägt mit Auflagen. Die geprüften Werte der Tabelle „Rechtsstand November 2026“ stimmen mit dem Gesetzestext überein. Die Mietrechtszeilen sind aber so stark verkürzt, dass eine 1:1-Übernahme in den Regelkatalog in Sanierungs- und Förderfällen zu überhöhten Mietpfaden führt. Außerdem fehlt ein Abschnitt zum rechtlichen Rahmen des Werkzeugs selbst: Rechts- und Steuerberatungsgrenze, Haftung, Beihilferecht, Nutzungsrechte, Datenschutz und Mitbestimmung. Dieser Rahmen muss vor dem Bau stehen, weil er Datenmodell, Berichte und Protokoll prägt.
Note: 6 von 10. Zur 9 fehlen (a) vollständige Tatbestände statt Stichworten in den Zeilen §§ 556d–559f BGB, MaBV und CO2KostAufG (Befunde 1–5), (b) ein Kapitel „Rechtlicher Rahmen des Werkzeugs“ mit den Punkten aus Befund 6–10 und einer Liste dessen, was ein zugelassener Anwalt und ein Steuerberater vor dem Einsatz bei Kunden verbindlich prüfen.

## Stichprobe am Gesetzestext (gesetze-im-internet.de, abgerufen 17.11.2026)

| Zeile im Bericht | Geprüfte Norm | Ergebnis |
|---|---|---|
| Körperschaftsteuer | § 23 Abs. 1 KStG | Wert stimmt (15 % bis 2027, dann 14/13/12/11, ab 2032 10 %) |
| Gewerbesteuer-Mindesthebesatz | § 16 Abs. 4 Satz 2, § 36 Abs. 5b GewStG | Wert stimmt (280 %, erstmals EZ 2027) |
| Sonderabschreibung | § 7b Abs. 1–3 EStG | Werte stimmen. Die Beihilfebindung nach Abs. 5 fehlt (Befund 8) |
| Kappungsgrenze | § 558 Abs. 3 BGB | Wert stimmt. Abs. 5 (Drittmittel) fehlt (Befund 2) |
| Mietpreisbremse | §§ 556d, 556e, 556f BGB | Werte stimmen, Ausnahmen unvollständig (Befund 3) |
| Index- und Staffelmiete | §§ 557a, 557b BGB | „Keine Obergrenze“ ist irreführend verkürzt (Befund 3) |
| Modernisierungsumlage | §§ 559, 559a, 559c BGB | 8 %, 3 €/2 € und Drittmittellogik stimmen. Der Erhaltungsabzug fehlt (Befund 2) |
| Heizungstausch | §§ 559e, 559f, 555b Nr. 1a BGB | Werte stimmen, Tatbestand verkürzt (Befund 1) |
| CO2-Kosten | §§ 5a, 5b, 5d, 8 CO2KostAufG | Werte stimmen, Neubau und Grenzen fehlen (Befund 5) |
| Heizungsrecht | §§ 42, 43, 71 GModG | Stimmt (Bio-Treppe 10/15/30/60 %, § 71 „weggefallen“) |
| Bauträgerraten | § 3 Abs. 1–2 MaBV, § 650v BGB | Ratenregel falsch wiedergegeben (Befund 4) |

## Befunde

1. [wichtig · belegt] **Zeile „Heizungstausch“ (§§ 559e, 559f BGB) und Fördermodul-Kopplungen.**
   - **Problem:** „10 % nach Abzug der Drittmittel“ lässt beide Voraussetzungen weg. Nach § 559e Abs. 1 Satz 1 gilt der 10-%-Satz nur, wenn die Maßnahme nach § 555b Nr. 1a dem Grunde nach zuschussfähig ist und der Vermieter Drittmittel tatsächlich in Anspruch genommen hat. Wird trotz Förderfähigkeit nicht gefördert, gilt nach Satz 2 nur § 559 mit 8 %. Bei § 559f fehlen die vier Ausnahmen vom Nachweis der Jahresarbeitszahl: Baujahr nach 1996, Standard der WSchV 1995, Standard nach § 38 GModG und Vorlauftemperatur bis 55 °C.
   - **Folge im Werkzeug:** Eine Regel „Heizung = 10 %“ ist für jeden ungeförderten Heizungstausch rechtswidrig. Eine Regel „Wärmepumpe ohne Nachweis = halbe Kosten“ unterschätzt die Miete bei jedem Gebäude ab 1997.
   - **Wirkung:** Der Betragsfehler bleibt meist klein, weil die Kappung von 0,50 €/m² in sechs Jahren (§ 559e Abs. 3, § 559 Abs. 3a Satz 3) häufig greift. Bei einer Wohnung mit 70 m² liegt die Grenze bei 420 € im Jahr.
   - **Offene Auslegungsfrage, nicht geklärt:** Wie werden zinsverbilligte Darlehen bei „abzüglich der in Anspruch genommenen Drittmittel“ angesetzt? Diese Frage gehört an den Anwalt.
   - **Vorschlag:** Die Zeile als Entscheidungsbaum führen: förderfähig ja/nein → Förderung genommen ja/nein → § 559e oder § 559. Dazu die Erhaltungspauschale von 15 % außer bei § 43-Anlagen, die Ausnahmen nach § 559f Abs. 1 Satz 2 als eigene Prüfmerkmale und die gemeinsame Grenze von 3 €/2 € (§ 559e Abs. 3 Satz 2).

2. [kritisch · belegt] **Zeilen „Modernisierungsumlage“ und „Kappungsgrenze“ sowie Abschnitt „Vier Kopplungen“: zwei Abzüge fehlen, die jeden geförderten Sanierungsfall verfälschen.**
   - **Fehlender Abzug 1, § 559 Abs. 2 BGB:** Kosten, die für Erhaltung ohnehin angefallen wären, gehören nicht zu den umlagefähigen Kosten. Der Bericht nennt das nur indirekt über die 15-%-Pauschale des § 559e.
   - **Fehlender Abzug 2, § 558 Abs. 5 BGB:** Drittmittel sind auch von jeder späteren Erhöhung auf die Vergleichsmiete abzuziehen. Der Wortlaut lautet: „im Falle des § 559a Absatz 1 mit 8 Prozent des Zuschusses“. Notiz 08 führt den Abzug als „neu“, im Bericht fehlt er ganz.
   - **Gegenrechnung:**

     | Größe | Wert |
     |---|---|
     | Wohnung | 70 m² |
     | Modernisierungskosten | 40.000 € |
     | Davon Erhaltungsanteil | 40 % |
     | Zuschuss | 12.000 € |
     | Umlage richtig: (40.000 − 16.000 − 12.000) × 8 % | 960 € im Jahr |
     | Umlage ohne Erhaltungsabzug: (40.000 − 12.000) × 8 %, unter der Kappung von 2.520 € | 2.240 € im Jahr |
     | Überhöhung der Umlage | 1.280 € im Jahr = 1,52 €/m² monatlich |
     | Zusätzlich: jede spätere Erhöhung auf die Vergleichsmiete zu hoch um 8 % × 12.000 € | 960 € im Jahr = 1,14 €/m² monatlich |

     Bei einer Sanierungsrechnung über 20 Jahre entscheidet das über die Vorteilhaftigkeit.
   - **Vorschlag:** Den Erhaltungsanteil als Pflichteingabe je Maßnahme führen (Schätzung zulässig; § 559c-Pauschale 30 % bis 10.000 € als Alternative). Den § 558-Abs.-5-Abzug als fünfte automatische Kopplung des Fördermoduls an den Mietpfad anlegen. Die Dauer dieses Abzugs (Rechtsprechung) ist nicht geprüft und vom Anwalt festzulegen.

3. [wichtig · belegt] **Zeilen „Mietpreisbremse“ und „Index- und Staffelmiete“.**
   - **Problem bei der Mietpreisbremse:** Es fehlen vier Regeln.
     - § 556e: Die Vormiete und Modernisierungen der letzten drei Jahre erhöhen die zulässige Miete.
     - § 556f Satz 2: Die erste Vermietung nach umfassender Modernisierung ist ausgenommen.
     - § 557a Abs. 4: Die Mietpreisbremse gilt für jede Mietstaffel.
     - § 557b: Bei Indexmiete ist eine Erhöhung nach § 558 ausgeschlossen. § 559/§ 559e gelten nur für nicht zu vertretende Maßnahmen oder Heizungsmaßnahmen nach § 555b Nr. 1a. Die Mietpreisbremse gilt nur für die Ausgangsmiete.
   - **Problem bei „keine betragsmäßige Obergrenze“:** Die Formulierung verleitet dazu, Index- oder Staffelpfad und Vergleichsmietenpfad zu kombinieren.
   - **Szenario Ankauf Bestand:** Vormiete 11,00 €/m², Vergleichsmiete 9,00 €/m². Das Werkzeug kappt die Neuvermietung auf 9,90 €/m², zulässig sind 11,00 €/m². Der Ankaufswert wird so unterschätzt.
   - **Szenario Indexmietvertrag:** Das Werkzeug addiert Index- und § 558-Erhöhungen. Der Mietpfad wird überschätzt.
   - **Vorschlag:** Mietvertragstyp (frei, Index, Staffel, gebunden) als Pflichtmerkmal je Einheit führen. Die zulässigen Erhöhungsarten je Typ als Matrix im Regelkatalog ablegen. Vormiete und Vormodernisierung als Eingabe aufnehmen. Gebundenen Wohnraum ausnehmen, weil er nach § 558 Abs. 2 Satz 2 aus der Vergleichsmiete fällt.

4. [wichtig · belegt] **Zeile „Bauträgerraten“ und Absatz „Vier Angaben … überholt“.**
   - **Problem:** „30 % … Rest in bis zu sieben Teilbeträgen aus 13 Vomhundertsätzen“ ist falsch. Nach § 3 Abs. 2 Satz 1 MaBV sind es höchstens sieben Teilbeträge insgesamt, die erste Rate eingeschlossen. Sie werden aus 13 Sätzen zusammengesetzt: Nr. 1 (30 % bzw. 20 %) plus zwölf Sätze auf die restliche Vertragssumme. Es fehlen außerdem die Fälligkeitsvoraussetzungen des § 3 Abs. 1, darunter ein Monat Wartezeit nach Bestätigung der Baugenehmigungsfreiheit.
   - **Rechtliche Wirkung:** § 650v BGB macht die MaBV zur zivilrechtlichen Obergrenze für Abschläge.
   - **Folge im Werkzeug:** Mit 30 % plus sieben Raten, also acht Zahlungen, setzt der Vertriebsplan Zahlungseingänge zu früh an. Bauzeitzinsen und Eigenkapitalbedarf werden zu niedrig ausgewiesen.
   - **Vorschlag:** Wortlaut übernehmen. Im Werkzeug höchstens sieben Ratenblöcke zulassen, gebildet aus den 13 Bausteinen, mit Umverteilung entfallender Leistungen (Abs. 2 Satz 3). Dazu eine Bürgschaftsvariante nach § 7 MaBV als Alternative.

5. [wichtig · belegt] **Zeile „CO2-Kosten“.**
   - **Problem:**
     - § 5b CO2KostAufG fehlt: Die hälftige Teilung gilt auch für Neubauten, die bis 31.12.2029 errichtet und erstmals genutzt werden, außer bei Bauantrag vor 13.05.2026. Damit betrifft sie Stufe 1, „Neubau zur Vermietung“.
     - Die Begrenzung auf höchstens 30 % Brennstoffanteil bei den Bio-Brennstoffkosten (§ 5a Abs. 3 Nr. 3) fehlt.
     - Die Härtefall-Rückausnahme des § 5d fehlt. Sie knüpft an Mietpreisbremsen-Gebiete und an eine Miete unter 85 % bzw. 70 % der Vergleichsmiete an.
   - **Folge im Werkzeug:** Ein Neubau mit Gas-Brennwertkessel wird ab 2028 ohne Vermieteranteil an CO2-Kosten und Netzentgelten gerechnet.
   - **Vorschlag:** Anwendungsbereich (Bestand nach § 5a, Neubau nach § 5b), die 30-%-Grenze und § 5d als Prüfmerkmale in den Regelsatz „GModG 2026“ aufnehmen, den Notiz 08 bereits empfiehlt.

6. [kritisch · begründete Einschätzung] **Fehlendes Thema: Grenze zur Rechts- und Steuerberatung (RDG, StBerG).**
   - **Problem:** Der Bericht plant die Steuerrechnung in drei Perspektiven für Kunden, außerdem Prüfungen wie „rückwirkende 15-%-Prüfung“, „Warnprüfung der Unschädlichkeitsgrenzen“, „10-%-Grenze als laufende Prüfung“ und die Eignung für § 7b. Hinzu kommen mietrechtlich „zulässige“ Mietpfade und die Befüllung von Förderformularen. Zur Abgrenzung sagt er nichts.
   - **Rechtslage, am Text geprüft:**
     - Hilfeleistung in Steuersachen ist jede Tätigkeit in fremden Angelegenheiten, „sobald sie eine rechtliche Prüfung des Einzelfalls erfordert“ (§ 2 Abs. 2 StBerG).
     - Sie ist geschäftsmäßig nur Befugten erlaubt (§§ 2 Abs. 1, 5 Abs. 1 StBerG), auch unentgeltlich.
     - Für Rechtsdienstleistungen gilt dieselbe Schwelle (§ 2 Abs. 1 RDG). § 5 RDG erlaubt sie als Nebenleistung und nennt die Fördermittelberatung ausdrücklich (§ 5 Abs. 2 Nr. 3). Förderaussagen sind damit eher gedeckt.
     - Eine gleichwertige allgemeine Nebenleistungsausnahme habe ich im StBerG nicht gefunden (§ 4 StBerG nicht vollständig gelesen).
   - **Szenario:** Ein Kundenbericht stellt fest „Sonderabschreibung § 7b nutzbar, 15-%-Grenze überschritten, Verkauf nach zehn Jahren steuerfrei“. Das ist eine steuerliche Prüfung des konkreten Falls.
   - **Mögliche Folgen, nicht im Einzelnen geprüft:** Bußgeld, Unterlassungsanspruch der Steuerberaterkammer (§ 5 Abs. 3 StBerG), Nichtigkeit der Honorarabrede.
   - **Vorschlag:** In Kundenberichten Steuer- und Mietrechtsparameter als **vom Kunden oder seinem Steuerberater vorgegebene Annahmen** führen. Dazu gehören Grenzsteuersatz, AfA-Wahl, „§ 7b: angenommen ja/nein“ und „Mietpfad: unterstellt“. Das Werkzeug rechnet die Folgen, es bescheinigt keine Zulässigkeit. Prüfmeldungen wie die 15-%-Grenze bleiben interne Plausibilitätshinweise oder lauten „mit Steuerberater klären“. Abgrenzung und Formulierungen vor Markteinsatz von Anwalt und Steuerberater freigeben lassen.

7. [wichtig · begründete Einschätzung] **Fehlendes Thema: Haftung für Rechenergebnisse und Förderaussagen gegenüber Kunden.**
   - **Problem:** Der Bericht empfiehlt, die NBank-Renditekennzahl „vorab auszuweisen“, und formuliert „rechnerisch ausfinanziert“. KfW-Zinsen sollen tagesaktuell automatisch einfließen. Im Kundenbericht kann eine solche Aussage als Auskunft mit Einstandswillen gelesen werden, etwa „Überkompensationsprüfung bestanden“ oder „Zins 1,83 %“. Die NBank-Annahmen sind laut Bericht selbst unveröffentlicht.
   - **Rechtsrahmen:** Haftungsbegrenzungen in AGB sind für grobe Fahrlässigkeit und Personenschäden unwirksam (§ 309 Nr. 7 BGB, am Text geprüft). Ein bloßer Haftungsausschluss im Bericht schützt daher wenig.
   - **Zusätzliches Risiko, nicht geprüft:** Fließen Werkzeugzahlen in einen Förderantrag, sind sie subventionserheblich (§ 264 StGB).
   - **Vorschlag:** Vor dem Kundeneinsatz drei Dinge regeln.
     - Beratungs-AGB mit Haftungsbegrenzung für leichte Fahrlässigkeit, Höchstbetrag und Verjährung, abgestimmt auf eine Vermögensschadenhaftpflicht.
     - Berichtssprache: „Ergebnis unter den ausgewiesenen Annahmen“, „Kennzahl nach eigener Rechnung, keine Aussage über die Bewilligung“.
     - Ein Satz Stand-Hinweis an der Förderkondition, wie in `CLAUDE.md` vorgesehen, statt pauschaler Vorbehalte.

8. [wichtig · belegt] **Fehlendes Thema: Beihilferecht als Regelart des Fördermoduls.**
   - **Problem:** Der Bericht kennzeichnet nur KfW 266 als De-minimis-Beihilfe. Am Text belegt ist zusätzlich § 7b Abs. 5 EStG: Die Sonderabschreibung wird nur gewährt, soweit die De-minimis-VO (EU) 2023/2831 eingehalten ist, im neuen Fenster für Anspruchsberechtigte mit Einkünften nach §§ 13, 15, 18 EStG. Das trifft die Kapitalgesellschaft, die Investorenperspektive der Stufe 1. Die NBank-Förderung beruht auf dem DAWI-Freistellungsbeschluss (EU) 2025/2630 (RL Nr. 1.2, Notiz 07). Die „Renditekennzahl“ ist die Überkompensationskontrolle dieses Beschlusses und mehr als eine Bankkennzahl.
   - **Szenario:** Eine GmbH mit 40 Wohnungen hat 11,2 Mio. € Bemessungsgrundlage und damit 560.000 € Sonder-AfA im Jahr. Der Beihilfewert kann die De-minimis-Schwelle (laut KfW-Merkblatt 300.000 € in drei Jahren) zusammen mit KfW 266 überschreiten. Die Berechnungsmethode des Beihilfewerts ist nicht geprüft. Das Werkzeug würde einen Steuervorteil einrechnen, der nicht gewährt wird.
   - **Vorschlag:** Je Förderkomponente ein Beihilferegime führen (keine Beihilfe, De-minimis, AGVO-Artikel, DAWI). Dazu ein De-minimis-Konto je Unternehmensgruppe über drei Jahre und eine Warnung bei Überschreitung. Die Wertermittlung (Subventionsäquivalent) mit dem Steuerberater festlegen. Notiz 04 hat das Schema bereits skizziert, der Bericht übernimmt es nicht.

9. [wichtig · begründete Einschätzung] **Fehlendes Thema: Nutzungsrechte an eingebundenen Inhalten.**
   - **Problem:** Gesetze und Verordnungen sind frei (§ 5 Abs. 1 UrhG). Die anderen Quellen sind es nicht ohne Weiteres.
     - DIN 276/277 sind private Normwerke; auf sie verwiesen zu werden macht sie nicht frei (§ 5 Abs. 3 UrhG).
     - Die BKI-Kennwerte sind ein kommerzielles Datenwerk. Ihr Einbau in Software und Kundenberichte braucht eine Lizenz.
     - Die gif-Richtlinie MF-G ist ein Verbandswerk.
     - Systematisch abgerufene KfW-Zinsdaten können als Datenbank geschützt sein (§ 87b Abs. 1 Satz 2 UrhG: wiederholte, systematische Entnahme). Der Bericht verlangt hier bereits die Zustimmung der KfW, das ist richtig.
     - Für die Destatis-Indizes ist die Lizenz nicht geprüft.
   - **Vorschlag:** Vor dem Bau des Kostenmoduls eine Rechteliste führen: Quelle, Lizenzgeber, erlaubte Nutzung intern und in Kundenberichten, Kosten.
     - Bei DIN die Kostengruppen-Gliederung mit Nummern und Kurzbezeichnungen von der Wiedergabe des Normtextes trennen und die Lizenz bei DIN Media klären.
     - BKI nur nach Lizenzvertrag einbinden, der die Ausgabe in Kundenberichten abdeckt.
     - Die Lizenzen der Open-Source-Bausteine in dieselbe Liste aufnehmen.

10. [wichtig · begründete Einschätzung] **Datenschutz und Mitbestimmung sind „vor Betriebsaufnahme“ verschoben, prägen aber die Architektur.**
    - **Problem:** Der Bericht nennt das Änderungsprotokoll mit Person, Zeitpunkt, altem und neuem Wert „Speicherformat des Systems“ und „nicht nachrüstbar“, dazu eine Präsenzanzeige. Das ist eine technische Einrichtung, die das Verhalten und die Leistung der Beschäftigten auswerten kann. Besteht ein Betriebsrat, greift die Mitbestimmung (§ 87 Abs. 1 Nr. 6 BetrVG, am Text geprüft). Weitere personenbezogene Daten:
      - Mieterlisten je Vertrag (Gewerbe) mit Namen;
      - Einkommensgruppen A/B/C je geförderter Einheit, also Einkommensdaten von Mietern;
      - Kundenzugänge, die eine Rollenklärung verlangen (Auftragsverarbeitung oder eigene Verantwortung).
    - **Konflikt:** Ein „lückenloses“ und unveränderliches Protokoll widerspricht Löschpflichten, wenn es Mieterdaten enthält.
    - **Vorschlag:** Datenschutz durch Technikgestaltung jetzt festlegen.
      - Einheiten über Kennungen statt Mieternamen führen.
      - Einkommensgruppe nur als Kategorie der Einheit speichern.
      - Protokoll ohne personenbezogene Mieterdaten, mit Aufbewahrungs- und Zugriffskonzept.
      - Betriebsvereinbarung oder Mitarbeiterinformation zum Protokoll und zur Präsenzanzeige.
      - Klären, ob eine Datenschutz-Folgenabschätzung nötig ist, und AV-Verträge mit dem Hoster schließen.
    - Die Festlegung gehört vor die Spezifikation des Protokolls, nicht vor die Betriebsaufnahme.

**Vor Markteinsatz verbindlich durch einen zugelassenen Anwalt (bei 6 und 8 zusätzlich durch einen Steuerberater) zu prüfen:**
- die Abgrenzung von Bericht und Werkzeug zu RDG und StBerG (Befund 6);
- Beratungs-AGB und Haftungsbegrenzung (7);
- die Auslegung von § 559e Abs. 1 bei Darlehen und die Dauer des § 558-Abs.-5-Abzugs (1, 2);
- die Beihilfewertermittlung für § 7b (8);
- die Lizenzlage für DIN, BKI und KfW-Daten (9);
- Datenschutzkonzept und Mitbestimmung (10).

Nicht geprüft:
- **Abruf:** WebFetch konnte gesetze-im-internet.de nicht auflösen. Die Normen habe ich deshalb über den Proxy direkt geladen und gelesen.
- **Nicht nachgeprüfte Normen:** Zeilen zu §§ 4h, 6, 7, 7h, 7i, 10d, 23 EStG, §§ 8, 9, 10a GewStG, § 5 KStG, § 52 AO, UStG, GrEStG, II. BV, BelWertV und PfandBG. Notiz 08 führt sie als bestätigt.
- **Spalte „Fassung“:** Die Änderungsdaten habe ich nicht gegen die Gesamtausgaben geprüft.
- **Nicht abgerufen:** Landesrecht (Niedersächsische Mieterschutzverordnung, Grunderwerbsteuersatz), EGBGB-Übergangsrecht zu §§ 559e/559f, Übergangsvorschriften des GModG (§§ 110 ff.), Rechtsprechung zu § 558 Abs. 5 BGB, DSGVO-Text, De-minimis-VO-Text.
- **Fördertabelle:** Die Förderkonditionen (KfW, NBank, BAFA) habe ich nicht nachgeprüft; sie liegen außerhalb des Schwerpunkts dieser Rolle.
