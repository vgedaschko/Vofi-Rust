# Fachliche Anforderungen ("branchentypische Fähigkeiten") an ein professionelles Immobilien-Investitionsrechnungstool für den deutschen Markt (Stand: 17. November 2026)

**Lesehinweise für den Report-Writer**

- **Verifikationsgrad:** In dieser Sitzung war der Direktabruf von Webseiten (WebFetch) für alle getesteten Hosts gesperrt (u. a. gesetze-im-internet.de, haufe.de, buzer.de, vdiv.de, gleisslutz.com, haus-und-grund-muenchen.de). Alle Belege stammen daher aus Suchtreffer-Auszügen, nicht aus vollständig gelesenen Dokumenten. Zahlen mit Rechtswirkung (II. BV, BGB, GModG, BelWertV) sollten vor Übernahme in Produkt-Stammdaten am Originaltext gegengeprüft werden.
- **Kennzeichnung:** `(V)` = durch Suchtreffer in dieser Sitzung belegt. `(FW)` = Fachwissen des Researchers; die verlinkte Primärquelle ist der Ort, an dem es nachprüfbar ist, wurde aber nicht abgerufen.
- **Einstufung:** `[M]` = Muss für ein professionelles Tool, `[D]` = Differenzierungsmerkmal. Die Quellen treffen diese Einstufung fast nie selbst; sie ist eine Folgerung des Researchers und steht deshalb jeweils unter "Inferences".
- **Abgrenzung:** Steuern, VOFI-Methodik, Förderprogramme im Detail und Softwaremarkt werden von anderen Researchern abgedeckt und sind hier nur an den Schnittstellen erwähnt.

---

## 1. Kostenseite: DIN 276, Erwerbs- und Baunebenkosten, Bauzeitfinanzierung, Baupreisindex, Kostenkennwerte, Mittelabfluss, Flächen (DIN 277, WoFlV, gif)

### Takeaway
Kostengliederung nach DIN 276:2018-12 (KG 100–800, inkl. der seit 2018 eigenständigen KG 800 Finanzierung) und eine saubere Flächenlogik (WoFlV für Wohnen/Förderung, MF-GIF 2023 für Gewerbe, DIN 277 für Kostenkennwerte) sind die Grundstruktur, die Banken, Förderbanken und Planer erwarten. Die Baupreisdynamik ist 2026 wieder hoch (+5,5 % ggü. Vorjahr im August 2026), eine explizite, vom VPI getrennte Baupreisindexierung ist deshalb Pflicht.

### Cited Findings
- (V) Die aktuelle Fassung ist DIN 276:2018-12 "Kosten im Bauwesen", erschienen im Dezember 2018. Ein Entwurf oder eine Neufassung 2025/2026 war in der Recherche nicht auffindbar — [bauprofessor.de, Meldung 01.12.2018](https://www.bauprofessor.de/news/neue-din-276-kosten-im-bauwesen/); [DIN, Inhaltsverzeichnis DIN 276:2018-12](https://www.din.de/de/mitwirken/normenausschuesse/nabau/veroeffentlichungen/wdc-beuth:din21:293154016/toc-2873248/download)
- (V) KG 800 "Finanzierung" ist mit der Ausgabe 2018-12 neu als eigene Hauptgruppe eingeführt worden (vorher KG 760 innerhalb der Baunebenkosten). Sie umfasst Kosten der Finanzierung bis zum Beginn der Nutzung, z. B. Zinsen, Bürgschaften, Notarkosten der Finanzierung — [bauprofessor.de, Kostengruppe Finanzierung](https://www.bauprofessor.de/kostengruppe-finanzierung-in-din-276/)
- (FW) Hauptgruppen: 100 Grundstück, 200 Vorbereitende Maßnahmen, 300 Bauwerk – Baukonstruktionen, 400 Bauwerk – Technische Anlagen, 500 Außenanlagen und Freiflächen, 600 Ausstattung und Kunstwerke, 700 Baunebenkosten, 800 Finanzierung — nachprüfbar bei [bauprofessor.de, Kostengruppen nach DIN 276](https://www.bauprofessor.de/kostengruppen-nach-din-276/)
- (V) Stufen der Kostenermittlung nach DIN 276:2018-12: Kostenrahmen, Kostenschätzung, Kostenberechnung, Kostenvoranschlag (neu 2018), Kostenanschlag, Kostenfeststellung. Die Kostenberechnung muss bis zur 3. Gliederungsebene vorliegen — [baunetzwissen.de, DIN 276](https://www.baunetzwissen.de/controlling-und-management/fachwissen/kosten-und-vertraege/din-276--kosten-im-bauwesen-8441183); [forum-verlag.com, DIN 276 neu](https://forum-verlag.com/fachwissen/bau-und-gebaeudemanagement/din-276-neu-kostengruppen-und-kostenplanung-sind-besonders-betroffen/)
- (V) Die HOAI 2021 verweist für anrechenbare Kosten weiterhin auf DIN 276-1:2008-12. Honorarermittlung (KG 700) und Kostengliederung des Projekts laufen also potenziell auf unterschiedlichen Normfassungen — [datadrivenaec.com, DIN 276 Kostengruppen und HOAI-Bezug](https://datadrivenaec.com/insights/din-276-kostengruppen-uebersicht)
- (V) BKI-Kostenkennwerte werden auf Basis der Kostengruppen 300+400 nach DIN 276 veröffentlicht — [BKI Flyer 2025 (Architektenkammer Sachsen)](https://www.aksachsen.org/fileadmin/Image_Archive/Berufspolitik/BKI/BKI_Flyer_2025.pdf)
- (V) Baupreisindex Destatis: Preise für den Neubau konventionell gefertigter Wohngebäude im August 2026 +5,5 % ggü. August 2025 und +1,0 % ggü. Mai 2026; Rohbau +5,4 %, Ausbau +5,7 %; Instandhaltung von Wohngebäuden (ohne Schönheitsreparaturen) +6,0 %. Pressemitteilung Nr. 360 vom 9. Oktober 2026 — [Destatis PD26_360](https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/10/PD26_360_61261.html)
- (V) Verlauf 2026: +3,3 % (Februar), +5,0 % (Mai, korrigierte Meldung), +5,5 % (August); Indexstand Wohngebäude August 2026 laut Drittauswertung 141,7 (2021 = 100). Erhebung quartalsweise (Feb/Mai/Aug/Nov); nächster Berichtsmonat November 2026, Veröffentlichung Januar 2027 — [Destatis, Korrektur Mai 2026](https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/07/PD26_241_61261.html); [statistiken-aktuell.de](https://statistiken-aktuell.de/baupreise-august-2026-datenmonitor/)
- (V) Regionale Abweichung ist erheblich: Berlin +6,9 % (Neubau Wohngebäude, August 2026) — [Amt für Statistik Berlin-Brandenburg](https://www.statistik-berlin-brandenburg.de/archiv/m-i-4-vj)
- (V) Förderseitige Kostenprüfung: Seit dem Förderjahr 2023 obliegt die Gesamtkostenprüfung für den geförderten Mietwohnungsneubau in NRW der NRW.BANK; es gibt eine Hilfestellung zu Baukosten für 2025 — [NRW.BANK, Hilfestellung Baukosten WRF 2025](https://www.nrwbank.de/.galleries/downloads/Presse/publikationen-wohnungsmarktbeobachtung/aktuelle-ergebnisse/Hilfestellung-fuer-Kommunen-Baukosten-WRF-2025.pdf)
- (V) Wohnflächenverordnung: Balkone, Loggien, Dachgärten und Terrassen werden in der Regel zu 25 %, höchstens zu 50 % angerechnet. Die WoFlV ist im geförderten Wohnungsbau verbindlich; fehlt im frei finanzierten Bereich eine Vereinbarung, gilt im Zweifel ebenfalls die WoFlV. DIN 277 erfasst Außenbereiche als eigene Kategorie ohne prozentuale Kürzung — [Schwäbisch Hall, Wohnflächenberechnung](https://www.schwaebisch-hall.de/wohnen-und-leben/bauen-und-modernisieren/neubau-anbau/wohnflaechenberechnung.html); [ImmoScout24, Wohnfläche](https://www.immobilienscout24.de/wissen/verkaufen/wohnflaeche.html)
- (V) gif-Mietflächen: Im Februar 2023 hat die gif die "MF-GIF 2023" (Richtlinie zur Berechnung der Mietfläche für Gebäude) veröffentlicht; sie löst MFG 2017 und MF/G 2012 ab. Gliederung: MF-GIF-0 (keine Mietfläche), MF-GIF-1 (exklusiv genutzte Mietfläche), MF-GIF-2 (gemeinschaftlich genutzte Mietfläche). Die Richtlinie ist als eigenständiges Regelwerk nutzbar; der Mietvertrag sollte ausdrücklich auf sie verweisen — [McDermott Will & Emery, Die neue MF-GIF 2023](https://www.mcdermottlaw.com/de/insights/real-estate-update-die-neue-mf-gif-2023/)
- (V) Die ältere MF/W (Wohnraum, 2012) hat sich laut Kanzleieinschätzung im Wohnungsmarkt nicht als ortsüblich durchgesetzt — [GÖRG, Flächenberechnung bei Mietobjekten (2013)](https://www.goerg.de/de/aktuelles/veroeffentlichungen/01-05-2013/flaechenberechnung-bei-mietobjekten-die-neuen-gif-richtlinien)
- (V) Kaufnebenkosten werden in Renditerechnungen von Privatanlegern häufig nicht vollständig in die Investitionssumme einbezogen (als typischer Fehler benannt) — [baufi24.de, Rendite berechnen](https://www.baufi24.de/rendite-berechnen-immobilie/)

### Inferences
Anforderungskatalog Kostenseite (Einstufung = Folgerung des Researchers):

| Fähigkeit | Einstufung | Begründung |
|---|---|---|
| Kostengliederung DIN 276:2018-12, mind. 1. Ebene (KG 100–800), aufklappbar bis 2./3. Ebene | [M] | Norm ist Verkehrssprache zwischen Planer, Bank und Förderbank |
| Versionierung der Kostenstände nach Ermittlungsstufe (Rahmen → Schätzung → Berechnung → Anschlag → Feststellung) mit Soll-Ist-Vergleich | [M] für Neubau/Sanierung/Developer | Stufenlogik ist normiert; Nachkalkulation baut darauf auf |
| KG 800 Bauzeitfinanzierung endogen aus Mittelabfluss × Zins rechnen (nicht als Pauschale), inkl. Bereitstellungszinsen | [M] | VOFI-Logik verlangt periodengenaue Finanzierung; Pauschalen sind die häufigste Fehlerquelle |
| Erwerbsnebenkosten als eigene Blöcke: Grunderwerbsteuer (Satz je Bundesland, Stammdatentabelle), Notar/Grundbuch, Makler, Due Diligence | [M] | Standardumfang jeder Ankaufskalkulation |
| Getrennte Indexreihen: Baupreisindex (Destatis, quartalsweise) ≠ VPI ≠ Mietentwicklung | [M] | 2026: Baupreise +5,5 %, deutlich über VPI-Niveau |
| Baupreisfortschreibung vom Kostenstand auf den Vergabe-/Bauzeitmittelpunkt | [M] für Neubau/Sanierung | Kostenstand und Zahlungszeitpunkt fallen auseinander |
| Mittelabflussplanung nach Bauablauf (S-Kurve oder gewerkeweise, monatlich/quartalsweise) | [M] | Voraussetzung für Bauzeitzinsen und Liquiditätsplanung |
| Position "Unvorhergesehenes" und Risikozuschläge je KG, getrennt ausgewiesen | [M] | Banken und Gremien fragen explizit danach |
| Kennwert-Plausibilisierung (€/m² BGF, €/m² Wfl., KG 300+400) gegen BKI-Bandbreiten | [D] | BKI-Daten sind lizenzpflichtig; Import/Benchmark ist Mehrwert |
| Automatischer Destatis-Abruf (GENESIS-API) für Baupreisindex und VPI | [D] | Aktualität ohne Pflegeaufwand |
| Flächenmodell mit mehreren parallelen Flächenarten je Einheit (BGF/NUF nach DIN 277, Wohnfläche nach WoFlV, Mietfläche nach MF-GIF) und Kennzahl Flächeneffizienz | [M] | Kosten hängen an BGF, Erlöse an Wohn-/Mietfläche |
| Brutto/Netto-Schalter je Kostenposition in Abhängigkeit von Vorsteuerabzug (Option nach § 9 UStG bei Gewerbe) | [M] bei Gewerbe/Mixed-Use | Schnittstelle zum Steuer-Researcher |

- Weil die HOAI auf die 2008er Fassung verweist, sollte das Tool die Honorarermittlung nicht "nebenbei" aus der 2018er Gliederung ableiten, sondern KG 700 als Eingabe oder Prozentsatz führen.
- Die 25-%-Balkonregel der WoFlV wirkt direkt auf die Mieterlöse; bei geförderten Wohnungen ist die WoFlV-Fläche zugleich Bemessungsgrundlage der Bewilligungsmiete.

### Gaps
- Ob für DIN 276 eine Überarbeitung in Arbeit ist, konnte nicht geklärt werden; ein Forentreffer nannte eine "DIN 276:2022", die nicht belegbar ist und vermutlich falsch ist.
- Aktuelle Fassung von DIN 277 (nach Kenntnis des Researchers DIN 277:2021-08) wurde in den Suchtreffern nicht bestätigt.
- Aktuelle Grunderwerbsteuersätze je Bundesland, GNotKG-Faustwerte und Maklerprovisionen wurden nicht recherchiert (Steuer-Researcher).
- Keine Quelle zu marktüblichen Zuschlägen für Unvorhergesehenes oder zu typischen S-Kurven-Parametern gefunden.
- BKI-Kennwerte selbst (Zahlenwerte) sind kostenpflichtig und nicht ermittelt.

---

## 2. Ertragsseite Wohnen: Mietrecht (§§ 556d ff., 557–559e BGB), Betriebskosten, CO2-Kostenaufteilung, Kostenmiete nach II. BV, Bindungen

### Takeaway
Die Mietentwicklung im Wohnen ist kein frei wählbarer Prozentsatz, sondern ein regelgebundener Pfad (Kappungsgrenze, Mietpreisbremse bis 31.12.2029, Modernisierungsumlage mit Kappung und Drittmittelabzug, Bindungen). 2026 ist das Mietrecht in Bewegung (GModG seit 29.07.2026 in Kraft, "Mietrecht II" im Verfahren bzw. möglicherweise im Herbst beschlossen), weshalb alle Regeln als datierte, pflegbare Parameter und nicht als Code-Konstanten abgebildet werden müssen.

### Cited Findings
**Mietpreisbremse und Kappungsgrenze**
- (V) Die Mietpreisbremse (§§ 556d ff. BGB) wurde vom Bundestag bis 31.12.2029 verlängert (Beschluss Sommer 2025); sie wäre sonst Ende 2025 ausgelaufen — [LTO](https://www.lto.de/recht/nachrichten/n/bundestag-verlaengert-mietpreisbremse-bis-2029); [Bundesregierung](https://www.bundesregierung.de/breg-de/bundesregierung/bundeskanzleramt/verlaengerung-mietpreisbremse-2350648)
- (V) Sie gilt nur, wo das Land per Rechtsverordnung einen angespannten Wohnungsmarkt ausweist; die Länder können verlängern, müssen aber nicht (Beispiel: Berlin bis Ende 2029). Der Geltungsbereich ist also je Gemeinde und mit Ablaufdatum zu führen — [immowelt Ratgeber](https://www.immowelt.de/ratgeber/mieten/mietpreisbremse); [berlin.de](https://www.berlin.de/aktuelles/10014766-958090-rent-cap-extended-until-2029.html)
- (V) Ausgenommen sind Wohnungen, die nach dem 1.10.2014 erstmals genutzt und vermietet wurden, sowie umfassend modernisierte Wohnungen — [Haufe, Mietpreisbremse](https://www.haufe.de/immobilien/wirtschaft-politik/mietpreisbremse-in-baden-wuerttemberg_84342_321932.html)
- (V) Kappungsgrenze § 558 Abs. 3 BGB: Mieterhöhung bis zur ortsüblichen Vergleichsmiete um höchstens 20 % in drei Jahren; die Länder können für Gemeinden mit angespanntem Markt per Verordnung (max. fünf Jahre Laufzeit) auf 15 % absenken — [Sächsische Staatsregierung, Medienservice](https://www.medienservice.sachsen.de/medien/news/1087981/download_pdf)

**Mietrecht II (Indexmiete, Möblierung, Kurzzeitmiete) – Status unsicher**
- (V) Regierungsentwurf am 29.04.2026 im Kabinett beschlossen, BT-Drs. 21/6807, erste Lesung am 09.07.2026, danach Ausschussberatung — [beck-aktuell, 29.04.2026](https://www.beck-aktuell.de/heute-im-recht/rechtspolitik-gesetzgebung/mieterschutz-indexmieten-kurzzeitvermietung-2026-04-29); [immocentrio.de](https://immocentrio.de/ratgeber/mietrechtsreform-2026)
- (V) Entwurfsinhalte: Begrenzung von Indexmieterhöhungen in angespannten Märkten (Schwelle je nach Quelle 3 % mit hälftiger Anrechnung darüber oder 3,5 %), mit Ausnahmen u. a. für Neubau und umfassende Modernisierung; Möblierungszuschlag muss offengelegt werden, Vermutung der Angemessenheit bis 10 % der Nettokaltmiete (andere Quellen: 5 % bzw. alternativ 1 % des Zeitwerts der Möbel); Kurzzeitmietverträge max. sechs Monate — [immowelt, Mietrechtsreform 2026](https://www.immowelt.de/ratgeber/mieten/mietrechtsreform-2026); [KPMG Law](https://kpmg-law.de/mietrechtsreform-2026-setzt-engere-rahmenbedingungen-fuer-vermieter/); [Taylor Wessing, Referentenentwurf Mietrecht II](https://www.taylorwessing.com/de/insights-and-events/insights/2026/02/referentenentwurf-mietrecht-ii)
- (V, widersprüchlich) Zwei Überschriften deuten darauf hin, dass der Bundestag im Herbst 2026 eine Fassung beschlossen hat, die Möblierungszuschläge deckelt, aber auf die Indexmieten-Deckelung verzichtet. Inhalt, Datum und Inkrafttreten konnten nicht geprüft werden — [boerse-express, "Bundestag beschließt Deckelung für Möblierungszuschläge"](https://www.boerse-express.com/news/articles/mietrecht-bundestag-beschliesst-deckelung-fuer-moeblierungszuschlaege-928990); [VDIV, "Mietrecht reformiert: keine Deckelung von Indexmieten, neue Regeln für möbliertes Wohnen"](https://vdiv.de/news-details/mietrecht-reformiert-keine-deckelung-von-indexmieten-neue-regeln-fuer-moebliertes-wohnen); dagegen "noch nicht abgeschlossen": [immowelt](https://www.immowelt.de/ratgeber/mieten/mietrechtsreform-2026)

**Modernisierungsumlage**
- (V) § 559 BGB: jährliche Mieterhöhung um 8 % der aufgewendeten Modernisierungskosten; Kappung 3 €/m² Wohnfläche innerhalb von sechs Jahren — [reduco.ai, Modernisierungsumlage 2026](https://reduco.ai/blog/modernisierungsumlage-energetische-sanierung)
- (FW) Bei einer Ausgangsmiete unter 7 €/m² beträgt die Kappung 2 €/m² in sechs Jahren (§ 559 Abs. 3a BGB); Erhaltungsaufwand ist vorab abzuziehen (§ 559 Abs. 2); Drittmittel wie Zuschüsse und Zinsvorteile aus Förderdarlehen mindern die umlagefähigen Kosten (§ 559a); vereinfachtes Verfahren bis 10.000 € je Wohnung mit 30 % Pauschalabzug (§ 559c) — nachprüfbar bei [gesetze-im-internet.de, § 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html)
- (V) § 559e BGB (seit 2024, Heizungstausch): 10 % Umlagesatz bei Inanspruchnahme öffentlicher Förderung, Pflichtabzug der Förderung, pauschal 15 % Erhaltungsanteil, eigene Kappung 0,50 €/m² monatlich innerhalb von sechs Jahren — [lexetius.com, § 559e BGB](https://lexetius.com/BGB/559e/mieterhohung-nach-einbau-oder-aufstellung-einer-heizungsanlage); [reduco.ai](https://reduco.ai/blog/modernisierungsumlage-energetische-sanierung)
- (V) Mit dem Gebäudemodernisierungsgesetz (in Kraft 29.07.2026) wurden § 555b und § 559e BGB geändert und ein § 559f BGB neu eingefügt; Details des neuen Wortlauts waren nicht abrufbar. Sekundärquellen nennen: Kappung 0,50 €/m² bleibt; 15 % Erhaltungspauschale bei neuen Gas-/Ölheizungen — [Haufe, Synopse GEG/GModG Art. 6 Änderung BGB](https://www.haufe.de/id/beitrag/synopse-geg-gmodg-art-6-aenderung-des-buergerlichen-gesetzbuches-HI17231871.html); [energie-experten.org](https://www.energie-experten.org/energie-sparen/energieberatung/gebaeudemodernisierungsgesetz)

**CO2-Kosten und neue Kostenteilung bei fossilen Heizungen**
- (V) CO2KostAufG: Zehn-Stufen-Modell für Wohngebäude seit 2023; je höher der CO2-Ausstoß je m² Wohnfläche, desto höher der Vermieteranteil; ab 52 kg CO2/m²/Jahr trägt der Vermieter 95 %. Bei Nichtwohngebäuden gilt hälftige Teilung (50:50) — [ista, CO2-Preis 2026](https://www.ista.com/de/blog/heizen-abrechnen/die-heizkosten-steigen-was-der-co2-preis-2026-fuer-mieter-und-vermieter-bedeutet/); [cleanthinking.de, 11.10.2026](https://www.cleanthinking.de/?p=1073785)
- (V) CO2-Preis nach BEHG 2026: Preiskorridor 55–65 €/t. Für 2027 hat das Kabinett laut einer Quelle am 12.08.2026 die Beibehaltung des Korridors beschlossen (Gesetzgebungsstand nicht geprüft); ab 2028 soll der EU-ETS 2 den Preis bestimmen — [ema-energiewelt.de](https://ema-energiewelt.de/wissen/co2-preis-2027-behg-novelle-korridor-55-65-euro); [42watt.de](https://42watt.de/magazin/co2-steuer)
- (V) GModG-Mieterschutz: Bei nach Inkrafttreten neu eingebauten Gas-/Ölheizungen trägt der Vermieter ab 01.01.2028 die Hälfte der CO2-Kosten und der Gasnetzentgelte, ab 2029 zusätzlich die Hälfte der Mehrkosten des vorgeschriebenen Bio-Brennstoffanteils (gedeckelt auf einen Bioanteil von 30 %). Gilt nur für Wohnraummietverhältnisse; bei Wärmepumpe entfällt die Beteiligung — [energie-experten.org](https://www.energie-experten.org/energie-sparen/energieberatung/gebaeudemodernisierungsgesetz); [vermieterwelt.de](https://www.vermieterwelt.de/beitraege/heizungsgesetz/); [Haufe, CO2-Kosten: Vermieter zahlen deutlich mehr](https://www.haufe.de/immobilien/wirtschaft-politik/co2-preis-inwiefern-muessen-sich-vermieter-beteiligen_84342_525922.html)

**Kostenmiete und II. Berechnungsverordnung (Stand 01.01.2026, gültig bis zur nächsten Anpassung 01.01.2029)**
- (V) Die Pauschalen nach §§ 26, 28 II. BV werden alle drei Jahre nach dem Verbraucherpreisindex angepasst (§ 26 Abs. 4, § 28 Abs. 5a); Anpassung zum 01.01.2026 um +8,37 % (VPI Oktober 2025 ggü. Oktober 2022) — [Haufe, Verwaltungskostenpauschale 2026](https://www.haufe.de/immobilien/verwaltung/erhoehung-der-kostenmiete-bei-sozialwohnungen_258_392374.html); [Haus & Grund Düsseldorf](https://hausundgrundddf.de/pauschalen-im-oeffentlich-gefoerderten-wohnungsbau/)
- (V) Verwaltungskostenpauschale ab 01.01.2026: 372,46 € je Wohnung und Jahr (zuvor 343,69 €; einzelne Quellen nennen 372,45 €); 445,32 € je Eigentumswohnung/Kaufeigentumswohnung; 48,58 € je Garage/Einstellplatz (einzelne Quellen 48,57 €) — [Haus + Grund München, 05.12.2025](https://www.haus-und-grund-muenchen.de/presse/mieterhoehung-bei-sozialwohnungen-zum-112026/); [Haus & Grund Rheinland Westfalen, Infoblatt 11/2025](https://www.hausundgrund-verband.de/fileadmin/root/media/downloads/2025/Infoblatt_Mietanpassung_112025.pdf)
- (V) Instandhaltungskostenpauschale ab 01.01.2026 je m² Wohnfläche und Jahr: 11,50 € (Bezugsfertigkeit weniger als 22 Jahre zurück), 14,58 € (mind. 22 Jahre), 18,62 € (mind. 32 Jahre). Die Altersgrenzen wandern jährlich (2026 betroffen: Bezugsfertigkeitsjahrgänge 1994 und 2004) — [Haus & Grund Düsseldorf](https://hausundgrundddf.de/pauschalen-im-oeffentlich-gefoerderten-wohnungsbau/); [Haufe](https://www.haufe.de/immobilien/verwaltung/erhoehung-der-kostenmiete-bei-sozialwohnungen_258_392374.html)
- (V) Achtung Verwechslungsgefahr: Die nicht indexierten Basiswerte der Verordnung (Stand 2002) lauten 7,10 / 9,00 / 11,50 €/m²; der Basiswert der ältesten Klasse (11,50 €) ist zufällig identisch mit dem indexierten 2026er-Wert der jüngsten Klasse. Ratgeberseiten zitieren teils die Basiswerte als aktuell — [Dr. Klein, Instandhaltungsrücklage](https://www.drklein.de/instandhaltungsruecklage.html); [gesetze-im-internet.de, § 28 II. BV](https://www.gesetze-im-internet.de/bvo_2/__28.html)
- (V) Mietausfallwagnis: höchstens 2 % der Erträge (§ 29 II. BV); rechnerisch werden 2,04 % auf die übrigen laufenden Aufwendungen angesetzt. Laufende Aufwendungen = Kapitalkosten (§ 19) + Bewirtschaftungskosten (§ 24: Abschreibung, Verwaltung, Betriebskosten, Instandhaltung, Mietausfallwagnis). Der Vermieter darf höchstens die Kostenmiete verlangen, die durch eine Wirtschaftlichkeitsberechnung zu ermitteln ist — [gesetze-im-internet.de, § 29 II. BV](https://www.gesetze-im-internet.de/bvo_2/__29.html); [Kreis Viersen, FAQ Wirtschaftlichkeitsberechnung](https://www.kreis-viersen.de/system/files/dokumente/FAQs%20zum%20Thema%20Wirtschaftlichkeitsberechnung.pdf); [Berliner Mieterverein](https://www.berliner-mieterverein.de/?p=1359)

**Wärmelieferung / Contracting**
- (V) § 556c BGB i. V. m. WärmeLV: Umstellung auf gewerbliche Wärmelieferung ist als Betriebskosten nur umlegbar bei Effizienzverbesserung und Kostenneutralität (Wärmelieferkosten nicht höher als bisherige Eigenversorgungskosten); Ankündigung drei Monate vorher. Laut BFW wird die Kostenneutralität beim Heizungstausch im vermieteten Bestand nur in etwa 17 % der Fälle erreicht. Das BMWE-Eckpunktepapier zum Wärmenetzpaket (26.08.2026) kündigt eine "modifizierte Kostenneutralität" an (noch kein geltendes Recht) — [Rödl & Partner, 25.06.2026](https://www.roedl.com/insights/nebenkosten-umlage-umstellung-waermeversorgung/); [BFW-Stellungnahme 08.05.2026](https://www.bfw-bund.de/wp-content/uploads/2026/05/260508_BFW_Stellungnahme_Contracting_WaermeLV.pdf); [BMWE-Eckpunkte Wärmenetzpaket (via vedec)](https://vedec.kbit.de/wp-content/uploads/2026/08/20260826_Eckpunkte-Wärmenetzpaket_BMWE.pdf)

### Inferences
| Fähigkeit | Einstufung | Begründung |
|---|---|---|
| Mietmodell je Einheit oder Einheitengruppe: Ist-Miete, Marktmiete, ortsübliche Vergleichsmiete (Mietspiegel), Vertragsart (Standard/Staffel/Index), letzter Erhöhungszeitpunkt | [M] | Ohne Trennung Bestands- vs. Neuvertragsmiete sind Kappungsregeln nicht rechenbar |
| Regel-Engine: § 558 (20 %/15 % in drei Jahren, Deckel ortsübliche Vergleichsmiete, 15 Monate Wartefrist) mit Kennzeichen "angespannter Markt" je Gemeinde und Ablaufdatum der Landesverordnung | [M] | Kernregel für buy & hold Wohnen |
| Mietpreisbremse bei Wiedervermietung (Vergleichsmiete + 10 %, Vormiete, Ausnahmen Neubau nach 01.10.2014 und umfassende Modernisierung), Gültigkeit bis 31.12.2029 plus Szenario "Verlängerung/Auslaufen" | [M] | Bestimmt den Mietsprung bei Fluktuation |
| Fluktuationsmodell (Quote p. a., Leerstandsdauer, Wiedervermietungskosten, Mietsprung auf zulässige Neuvertragsmiete) | [M] | Hebel der Mietentwicklung im Bestand |
| Modernisierungsumlage-Rechner: Kosten − Erhaltungsanteil − Drittmittel (§ 559a) → 8 % → Kappung 3 €/2 €; Heizungspfad § 559e/§ 559f getrennt; anschließende Sperrwirkung für § 558 | [M] für Sanierung | Größter Einzelhebel und größte Fehlerquelle der Sanierungsrechnung |
| Verknüpfung Fördermittel ↔ Umlage: Zuschüsse und Zinsvorteile mindern automatisch die umlagefähigen Kosten; Tool verhindert Doppelansatz | [M] | Explizit als typischer Fehler im Briefing genannt; rechtlich zwingend |
| Warmmietenneutralitäts-Check (Umlage vs. rechnerische Heizkostenersparnis) je Wohnung | [D] | Für kommunale/genossenschaftliche Unternehmen politisch zentral |
| CO2-Kostenmodul: Verbrauch × Emissionsfaktor × CO2-Preispfad → Stufe → Vermieteranteil als nicht umlagefähige Kosten; Sonderregel 50 % für neue fossile Heizungen ab 2028 inkl. Netzentgelte | [M] für Bestand mit fossiler Wärme | Seit 2023 liquiditätswirksam; ab 2028 deutlich verschärft |
| Trennung umlagefähige / nicht umlagefähige Bewirtschaftungskosten, Leerstandskosten (nicht umlegbare Betriebskosten im Leerstand) | [M] | Standard in jeder Bank- und Gremienvorlage |
| Kostenmieten-Modul nach II. BV: Wirtschaftlichkeitsberechnung (Gesamtkosten, Finanzierungsmittel, laufende Aufwendungen), Pauschalen als datierte Stammdaten (01.01.2026: 372,46 € / 11,50–14,58–18,62 €/m² / 2 %) mit automatischem Alterswechsel der Instandhaltungsklasse | [M] für geförderten Altbestand (1. Förderweg) und Antragsunterlagen; sonst [D] | Pflichtformat für preisgebundenen Bestand |
| Bindungsmodell: Bewilligungsmiete, zulässige Steigerung laut Förderbescheid, Bindungsdauer, Belegungsbindung, Auslauf der Bindung mit Übergang ins Vergleichsmietensystem (inkl. Kappungsgrenze nach Bindungsende) | [M] für geförderten Wohnungsbau | Bindungsauslauf ist der zentrale Werttreiber geförderter Objekte |
| Möblierungszuschlag als eigene, gedeckelte Erlöskomponente | [M] für Mikro-/Studentenwohnen, sobald Mietrecht II gilt | Regulatorisches Risiko dieser Assetklasse |
| Gemeindescharfe Stammdaten (Mietpreisbremse, Kappungsgrenze, Mietspiegel) als gepflegter Datendienst | [D] | Hoher Pflegeaufwand, hoher Nutzen |

- Weil § 559e/§ 559f, CO2-Kostenteilung, Mietrecht II und BEHG-Preispfad 2026 gleichzeitig in Bewegung sind, ist ein "Rechtsstand-Datum" je Kalkulation (welche Regelversion wurde gerechnet) ein sinnvolles Prüf- und Dokumentationsmerkmal.
- Die GModG-Kostenteilung verändert die Wirtschaftlichkeit "Gasheizung ersetzen durch Gasheizung" gegenüber "Wärmepumpe" strukturell; ein Variantenvergleich Heizungstechnik gehört in jedes Sanierungsszenario.

### Gaps
- Der genaue Wortlaut von § 559e (neu) und § 559f BGB nach GModG (BGBl. 2026 I Nr. 226) konnte nicht abgerufen werden; Umlagesatz, Förderabzug und Kappung für Wärmepumpen nach § 559f sind unbestätigt.
- Status von Mietrecht II zum 17.11.2026 (beschlossen? Bundesrat? Inkrafttreten? Indexdeckel ja/nein? Möblierungszuschlag 5 % oder 10 %?) ist offen; maßgeblich wären bundestag.de (Drs. 21/6807, Beschlussempfehlung) und das BGBl.
- Ob das vereinfachte Verfahren § 559c (10.000 €) angehoben wurde, ist ungeklärt.
- Für die II.-BV-Zuschläge 2026 (Aufzug, Abschläge Kleinreparaturen, Zuschlag Schönheitsreparaturen, Garageninstandhaltung) fand sich nur ein Einzelwert (13,76 €/m² bei vom Vermieter getragenen Schönheitsreparaturen laut Haus + Grund München, Zuordnung unklar); die amtliche Tabelle wurde nicht gefunden.
- Die vollständige Stufentabelle des CO2KostAufG und der Wortlaut der GModG-Änderungen daran wurden nicht verifiziert.
- Länderspezifische Regelungen des geförderten Wohnungsbaus (Bewilligungsmieten, Bindungsdauern, zulässige Mietsteigerungen je Land) wurden nicht erhoben (Förder-Researcher).
- Übliche Ansätze für Fluktuation und Leerstand je Markt: keine belastbare Quelle recherchiert.

---

## 3. Ertragsseite Gewerbe: Mietvertragsdaten, Anschlussvermietung, WALT, Umsatzmiete, Nebenkosten, rent-roll-basierte Modellierung

### Takeaway
Gewerbe wird mietvertragsscharf (Rent Roll) und nicht flächenpauschal gerechnet: Laufzeit, Optionen, Indexklausel, mietfreie Zeiten und Incentives je Vertrag sowie Annahmen zur Anschlussvermietung je Fläche. Belastbare deutsche Marktquellen zu konkreten Parametern (Wiedervermietungswahrscheinlichkeit, Leerstandsdauer) waren in der Recherche kaum auffindbar; die Parameter müssen frei eingebbar sein.

### Cited Findings
- (V) Cashflow-Modelle für gewerbliche Immobilienfinanzierungen bilden "nahezu sämtliche Mietvertragsbestimmungen" ab, etwa Indexanpassung, Mietgarantien und mietfreie Zeiten — [Zeitschrift Immobilien & Finanzierung (kreditwesen.de)](https://www.kreditwesen.de/sites/default/files/content/articledownloads/2015/09/lak_12_10_334-336.pdf)
- (V) Bei Objekten mit mehreren Mietern wird die Vertragslaufzeit als WALT (gewichtete durchschnittliche Restlaufzeit) gemessen; ein hoher WALT erhöht die Planbarkeit der Erträge und senkt das wahrgenommene Risiko — [JLL, Tenant Retention as Value Driver](https://www.jll.com/de-de/insights/tenant-retention-as-value-driver)
- (V) Incentives: Drei bis sechs mietfreie Monate oder vergleichbare Zugeständnisse sind bei Neuabschlüssen marktüblich und unmittelbar liquiditätsbelastend — [JLL](https://www.jll.com/de-de/insights/tenant-retention-as-value-driver)
- (V) Mietvertragslaufzeiten am Gewerbeimmobilienmarkt verkürzen sich seit Jahren deutlich — [Immobilien & Finanzierung (kreditwesen.de)](https://kreditwesen.de/sites/default/files/content/articledownloads/2017/48/lak_17_23_830-832.pdf)
- (V) CO2-Kosten: Bei Nichtwohngebäuden werden die CO2-Kosten hälftig zwischen Vermieter und Mieter geteilt (kein Stufenmodell); die GModG-Mieterschutzregeln gelten nur für Wohnraum, bei Gewerbemietern bleiben Betriebskosten voll umlegbar — [cleanthinking.de](https://www.cleanthinking.de/?p=1073785); [energie-experten.org](https://www.energie-experten.org/energie-sparen/energieberatung/gebaeudemodernisierungsgesetz)
- (V) Bewertungsmodell-Ansätze Gewerbe nach ImmoWertV Anlage 3: Verwaltungskosten 3 % und Mietausfallwagnis 4 % des marktüblich erzielbaren Rohertrags bei reiner und gemischter gewerblicher Nutzung — [gesetze-im-internet.de, ImmoWertV Anlage 3](https://www.gesetze-im-internet.de/immowertv_2022/anlage_3.html)
- (V) Mietfläche: MF-GIF 2023 unterscheidet exklusive (MF-GIF-1) und anteilige Gemeinschaftsflächen (MF-GIF-2) — [McDermott](https://www.mcdermottlaw.com/de/insights/real-estate-update-die-neue-mf-gif-2023/)
- (V) Mieterausfall als Finanzierungsauslöser: Cash-Management-Auslöser in Kreditverträgen knüpfen neben DSCR und Debt Yield auch an den Verlust eines Großmieters an (US-Quelle) — [rets.ai, Loan Covenants](https://rets.ai/glossary/loan-covenants)

### Inferences
| Fähigkeit | Einstufung | Begründung |
|---|---|---|
| Rent Roll je Mietvertrag: Mieter, Fläche(n) nach MF-GIF, Nutzungsart, Miete €/m², Beginn/Ende, Sonderkündigungsrechte (Break), Verlängerungsoptionen (Anzahl, Dauer, Mietkonditionen), Sicherheiten | [M] für Gewerbe/Mixed-Use | Banken-Cashflow-Modelle bilden nahezu alle Vertragsbestimmungen ab |
| Indexklauseln: Bezug VPI, Schwellenwert (Punkte/Prozent), Weitergabequote (z. B. 80 %/100 %), Karenzzeit, automatische vs. Verlangens-Anpassung; alternativ Staffelmiete | [M] | Standardvertragslogik; Schwellen erzeugen sprunghafte Cashflows |
| Mietfreie Zeiten, Ausbaukostenzuschüsse (TI), Maklerkosten/Vermietungsprovision als zahlungswirksame Positionen zum Vertragsbeginn; optional effektive Miete (Net Effective Rent) | [M] | 3–6 Monate mietfrei sind marktüblich und liquiditätswirksam |
| Anschlussvermietung je Fläche: Verlängerungswahrscheinlichkeit, Leerstandsdauer, Marktmiete + Marktmietwachstum, Neuvertrags-Incentives, Leerstandskosten; wahrscheinlichkeitsgewichtet oder als Szenario | [M] | Kern der ARGUS-artigen Modellierung |
| WALT/WAULT (bis Break und bis Vertragsende), Mietauslaufprofil, Mieterkonzentration, Over-/Underrent ggü. Marktmiete | [M] | Standardkennzahlen in Investment Memo und Bankenunterlage |
| Umsatzmiete (Mindestmiete + Prozentsatz vom Umsatz über Schwelle) | [M] bei Einzelhandel/Hotel, sonst [D] | Typisch für Handel und Hybridpachten |
| Nebenkostenmodell: umlegbar/nicht umlegbar je Vertrag (Double-/Triple-Net), Verwaltungskostenumlage, Instandhaltungsobergrenzen ("Dach und Fach") | [M] | Bestimmt den NOI |
| USt-Option je Mietvertrag (Vorsteuerschlüssel für CapEx und Betriebskosten) | [M] | Schnittstelle Steuer |
| Import Rent Roll (Excel/CSV) und Stichtags-Snapshots | [D] | Praxisnutzen bei Ankaufsprüfung |
| Monatliche Periodizität im Gewerbe-Cashflow | [D] (Quartal/Jahr = [M]) | Mietfreie Zeiten und Indexsprünge sind unterjährig |

- Bei Mixed-Use müssen Wohn- und Gewerbelogik im selben Objekt nebeneinander laufen (unterschiedliche Mieterhöhungsregeln, CO2-Aufteilung, USt, Bewirtschaftungskostenansätze).

### Gaps
- Keine belastbare deutsche Quelle zu typischen Indexschwellen, Wiedervermietungswahrscheinlichkeiten, Leerstandsdauern oder TI-Höhen gefunden; die gif-Richtlinien zu Renditedefinitionen und zur DCF-Standardisierung wurden in den Treffern nicht sichtbar.
- Funktionsumfang von ARGUS Enterprise als Referenz wurde hier nicht recherchiert (Softwaremarkt-Researcher).
- Aktuelle Rechtslage zur Schriftform bei Gewerbemietverträgen (§ 550/§ 578 BGB nach Bürokratieentlastungsgesetz IV, Textform) wurde nur in einem unsicheren Anwaltsbeitrag angesprochen und ist nicht verifiziert.

---

## 4. Sonderimmobilien: Pflege, Hotel, studentisches Wohnen/Serviced Apartments, betreutes Wohnen

### Takeaway
Sonderimmobilien werden über den Betreiber gerechnet: Der Immobilien-Cashflow ist eine Pacht, deren Nachhaltigkeit sich aus der Betriebsrechnung des Betreibers ergibt (Pflege: Investitionskostensatz und EBITDAR; Hotel: Umsatz/GOP und Pachtquote; Mikroapartments: Auslastung und All-in-Miete). Marktübliche Schwellenwerte (z. B. Pachtdeckung) konnten in dieser Recherche nicht belegt werden.

### Cited Findings
**Pflege**
- (V) § 82 SGB XI reglementiert die Finanzierung: Pflegevergütung, Unterkunft/Verpflegung und Investitionskosten sind getrennt zu berechnen und auszuweisen. Betriebsnotwendige Investitionsaufwendungen einschließlich Miete, Pacht und Erbbauzins können den Bewohnern gesondert berechnet werden, soweit sie nicht durch öffentliche Förderung gedeckt sind (§ 82 Abs. 2–4) — [gesetze-im-internet.de, § 82 SGB XI](https://www.gesetze-im-internet.de/sgb_11/__82.html); [IREBS-Pflegestudie (kreditwesen.de)](https://www.kreditwesen.de/sites/default/files/flipbook/insert/64856/pflegestudie_irebs_S21.pdf)
- (V) Bewertungsstandard der Banken: HypZert-Fachgruppe Sozialimmobilien, "Bewertung von Pflegeheimen", 6. Auflage (Inhaltsverzeichnis vom 07.07.2026). Ein Pflegeheim als Betreiberimmobilie "wird durch den Betrieb der Einrichtung und die Faktoren, die diesen Betrieb beeinflussen, bedingt" — [HypZert, Inhaltsverzeichnis](https://www.hypzert.de/sites/default/files/shop-table-of-contents/20260707_Bewertung-von-Pflegeheimen-6-Auflage_Inhalt_FG-Sozialimmobilien.pdf)
- (V) Praxishinweise für Pachtverträge: Pacht möglichst indexiert; Instandhaltungspflicht des Eigentümers auf "Dach und Fach" beschränkt — [Stiftung Warentest](https://www.test.de/Pflegeapartments-als-Geldanlage-Wie-riskant-ist-der-Kauf-einer-Pflegeimmobilie-5562373-5562379/)
- (V) Pflegeimmobilien stellen rund 54 % des Transaktionsvolumens im Healthcare-Investmentmarkt (Colliers, Stand der Publikation 2021) — [Colliers, Healthcare-Immobilien Buyers Guide](https://www.colliers.de/wp-content/uploads/2024/01/21_10_healthcare_immobilien_buyers_guide.pdf)

**Hotel**
- (V) Pachtvertrag: Laufzeit typischerweise 15–30 Jahre, fixe Pacht, Betreiber erhält meist ein schlüsselfertiges, mit FF&E ausgestattetes Objekt. Managementvertrag: Trennung von Eigentum und Betrieb, Vergütung des Betreibers u. a. als Prozentsatz des GOP; das Betriebsrisiko liegt beim Eigentümer — [Horwath HTL, Pachtvertrag vs. Managementvertrag](https://horwathhtl.com/wp-content/uploads/2025/02/HorwathHTL_Pachtvertrag-vs-Managementvertrag_Deutsch.pdf)
- (V) Trend weg vom reinen Pachtvertrag hin zu Management- und Hybridverträgen; das Risiko verschiebt sich damit zum Investor — [TU Wien, Diplomarbeit Beilein 2012](https://repositum.tuwien.at/bitstream/20.500.12708/12877/2/Beilein%20Gregor%20-%202012%20-%20Vertragliche%20Gestaltungsmoeglichkeiten%20von%20Eigentuemer-...pdf)
- (V) Pachtquote/Pachtdeckung: Ein Wert von 1,0 würde bedeuten, dass der gesamte Betriebsgewinn in die Pacht fließt und nichts für die FF&E-Reserve und das unternehmerische Risiko bleibt — [Taylor Wessing, Interview Hotelmietverträge im Wandel (09/2025)](https://www.taylorwessing.com/zh-hant/insights-and-events/insights/2025/09/interview-hotelmietvertraege-im-wandel)
- (V) Aus Bankensicht sind Managementverträge transparenter als klassische Pachtverträge, was die Risikoanalyse erleichtert — [Immobilien & Finanzierung (kreditwesen.de)](https://www.kreditwesen.de/sites/default/files/content/articledownloads/2015/09/lak_12_19_714-716.pdf)
- (V) BelWertV: Für Hotels, Kliniken, Logistik u. a. gelten erhöhte Mindestkapitalisierungszinssätze (siehe Abschnitt 6) — [Haufe, BelWertV-Novelle](https://www.haufe.de/immobilien/investment/wertermittlungsportale-immobilienbewertung-per-knopfdruck_256_501422.html)

**Studentisches Wohnen / Mikroapartments**
- (V) Initiative Micro-Living/bulwiengesa: rund 26.700 Einheiten in 123 Apartmenthäusern ausgewertet, durchschnittliche Auslastung 95 % (Report 2. Hj. 2024); ein neuerer Bericht nennt 95,6 % bei 128 Objekten/28.300 Einheiten — [Initiative Micro-Living Report 2. Hj. 2024 (konii)](https://konii.de/wp-content/uploads/2025/01/Initiative-Micro-Living_Report_2.HJ_24.pdf); [konii.de](https://www.konii.de/?p=216166)
- (V) MLP/IW-Studentenwohnreport 2026: qualitätsbereinigte Mieten im 1. Hj. 2026 durchschnittlich +2,6 % über Vorjahr; Studierendenzahl WS 2025/26: 2,88 Mio. — [boerse-express](https://www.boerse-express.com/news/articles/studentisches-wohnen-54-des-einkommens-fuer-miete-notstand-waechst-928578)
- (V) Renditeaufschlag studentisches Wohnen ggü. klassischen Mehrfamilienhäusern (Spitzenrendite 3,46 %): 94 Basispunkte (Newmark, 2026) — [konii.de](https://www.konii.de/?p=216003)
- (V) Regulatorisches Risiko: Möblierte Mikroapartments stehen wegen der Mietrechtsreform (Möblierungszuschlag, Kurzzeitvermietung) unter politischem Risiko — [REFIRE](https://www.refire-online.com/investment/furnished-but-exposed-german-micro-apartments-face-political-risk/)

### Inferences
| Fähigkeit | Einstufung | Begründung |
|---|---|---|
| Pachtvertragsmodell (Fixpacht, Indexierung, Laufzeit/Optionen, Instandhaltungsaufteilung "Dach und Fach", FF&E-Verantwortung) | [M] für Sonderimmobilien | Grundform aller Betreiberimmobilien |
| Betreiber-Schattenrechnung Pflege: Plätze, Auslastung, Pflegegradmix, Investitionskostensatz €/Platz/Tag, Umsatz, EBITDAR, Pacht → Pachtdeckung (EBITDAR/Pacht) und Pachtquote (Pacht/Umsatz) | [D] (Pachtdeckung als Eingabefeld/Kennzahl: [M]) | Nachhaltigkeit der Pacht ist der Kern der Bank-Bewertung; volle Betreiberrechnung ist Spezialistenfunktion |
| Plausibilisierung Pacht gegen refinanzierbaren Investitionskostensatz (I-Kosten × Plätze × Belegungstage) | [D] | Pacht ist über § 82 SGB XI faktisch gedeckelt |
| Hotel: Zimmerzahl, Auslastung, ADR → RevPAR → Umsatz → GOP; Fixpacht / Umsatzpacht / Hybrid (Mindestpacht + Umsatzanteil) / Managementvertrag (Base + Incentive Fee, Eigentümer trägt Ergebnis); FF&E-Reserve in % vom Umsatz | [D]; Hybridpacht-Formel [M], wenn Hotel im Zielumfang | Vertragsvielfalt, Risikoübergang auf Investor |
| Mikro-/Studentenapartments: All-in-Miete zerlegt in Nettokaltmiete, Möblierungszuschlag, Betriebskosten-/Servicepauschale; Auslastung, Semester-Fluktuation, Möbel-Reinvestitionszyklus, Betreiber-/Managementfee | [M] für diese Nutzungsart | Zerlegung wird durch Mietrecht II rechtlich relevant |
| Betreutes Wohnen: Wohnmiete (reguläres Mietrecht) + Betreuungspauschale getrennt; ggf. Generalmietvertrag mit Betreiber | [M] für diese Nutzungsart | Mischform aus Wohnen und Betreibermodell |
| Betreiberbonität/Drittverwendungsfähigkeit als qualitatives Risikofeld und Szenario "Betreiberausfall" (Pachtausfall, Neuverpachtung zu Marktpacht, Umbaukosten) | [D] | Größtes Einzelrisiko bei Single-Tenant-Betreiberobjekten |
| Erhöhte Bewertungsabschläge der Bank (BelWertV-Mindestzinssätze, höhere Bewirtschaftungskosten) je Nutzungsart als Stammdaten | [D] | Erklärt niedrigere Beleihungsausläufe |

### Gaps
- Keine Quelle mit bezifferten Marktstandards gefunden für: Pachtdeckung/EBITDAR-Coverage bei Pflegeheimen, Pachtquote in % vom Umsatz, übliche Investitionskostensätze, FF&E-Reserve in % (Hotel), Management-Fee-Sätze, Betreiberkosten bei Mikroapartments. Diese Werte stehen vermutlich im HypZert-Leitfaden (kostenpflichtig) und in Berichten von CBRE/Savills/Horwath.
- Landesrechtliche Vorgaben zu Investitionskosten (z. B. APG DVO NRW) und Heimbauvorschriften (Einzelzimmerquoten) wurden nicht recherchiert, sind aber für die Pflegekalkulation maßgeblich.
- Betreutes Wohnen/Service-Wohnen: keine spezifischen Quellen gefunden.

---

## 5. Bewirtschaftung: Instandhaltung, CapEx, Verwaltung, ESG/CRREM, GEG/GModG, EPBD, EU-Taxonomie, energetische Kennwerte

### Takeaway
Zum Stand November 2026 ist die 65-%-EE-Regel für neue Heizungen aufgehoben: Das Gebäudemodernisierungsgesetz (GModG) ist am 29.07.2026 in Kraft getreten und ersetzt sie durch eine Bio-Brennstoff-Treppe ab 2029 plus Kostenteilung zulasten des Vermieters. Die EPBD-Umsetzungsteile folgen erst Anfang 2027; für die Kalkulation heißt das: CO2- und Brennstoffkostenpfade sowie CapEx-Fahrpläne werden wichtiger als eine starre Technikvorgabe.

### Cited Findings
**GEG → GModG (Status 2026)**
- (V) Der Bundestag hat das Gebäudemodernisierungsgesetz am 10.07.2026 beschlossen (laut einer Quelle 322 zu 272 Stimmen); verkündet am 28.07.2026 (BGBl. 2026 I Nr. 226); seit 29.07.2026 heißt das GEG offiziell Gebäudemodernisierungsgesetz. Die 65-%-Regel für neu eingebaute Heizungen ist aufgehoben, die Beratungspflicht bei fossilen Heizungen entfallen — [Gleiss Lutz, Überblick GModG](https://www.gleisslutz.com/de/know-how/ueberblick-ueber-das-neue-gebaeudemodernisierungsgesetz); [Bundesregierung, FAQ](https://www.bundesregierung.de/breg-de/service/fragen-und-anworten/neues-gebaeudemodernisierungsgesetz-2430284); [baulinks.de](https://www.baulinks.de/webplugin/2026/1006.php4)
- (V) "Bio-Treppe": Neue Gas-/Ölheizungen müssen ab 01.01.2029 mindestens 10 % klimafreundliche Brennstoffe (Biomethan, Bioöl, Wasserstoff) nutzen, steigend auf 30 % ab 2035 und 60 % ab 2040; eine Quelle nennt zusätzlich eine Stufe 15 % ab 2030 — [energie-experten.org](https://www.energie-experten.org/energie-sparen/energieberatung/gebaeudemodernisierungsgesetz); [Wikipedia, Gebäudemodernisierungsgesetz](https://de.wikipedia.org/wiki/Geb%C3%A4udemodernisierungsgesetz); [cleanthinking.de](https://www.cleanthinking.de/gebaeudemodernisierungsgesetz/)
- (V) Kanzleibewertung: "Mehr Flexibilität und Eigenverantwortung, aber weniger Klimaschutz?" — [CMS](https://cms.law/en/deu/legal-updates/neues-gebaeudemodernisierungsgesetz-mehr-flexibilitaet-und-eigenverantwortung-aber-weniger-klimaschutz)

**EPBD**
- (V) Die Umsetzungsfrist der EPBD (29.05.2026) wurde von Deutschland (und laut einer Meldung von allen Mitgliedstaaten) verfehlt; ein Vertragsverletzungsverfahren ist möglich bzw. laut einer Quelle bereits eingeleitet. Das GModG ist das Umsetzungsgesetz; die EPBD-Umsetzungsteile treten laut einer Quelle erst rund sechs Monate nach Verkündung in Kraft (Ende Januar 2027) — [Haufe, EPBD-Verzug](https://www.haufe.de/immobilien/wirtschaft-politik/energieeffienz-in-gebaeuden-fahrplan-der-bundesregierung_84342_520684.html); [immowelt](https://www.immowelt.de/ratgeber/news/eu-gebaeuderichtlinie-wird-umgesetzt-das-kommt-jetzt-auf-eigentuemer-zu); [konii.de](https://www.konii.de/?p=209926)
- (V) Mindestvorgaben für die Gesamtenergieeffizienz (MEPS) gelten nur für Nichtwohngebäude: Bis 2033 müssen die 26 % der Nichtwohngebäude mit der schlechtesten Effizienz erfasst (saniert) sein. Für Wohngebäude gibt es keinen gebäudescharfen Sanierungszwang, sondern einen nationalen Durchschnittspfad (Portfolioansatz). Der nationale Gebäuderenovierungsplan ist bis 31.12.2026 der EU-Kommission vorzulegen — [reduco.ai, EPBD-Novelle](https://reduco.ai/blog/epbd-novelle-2024-eigentuemer-pflichten); [GÖRG, 30.09.2025](https://www.goerg.de/de/aktuelles/veroeffentlichungen/30-09-2025/regulatorischer-wandel-im-gebaeudesektor-nationale-umsetzung-der-eu-gebaeuderichtlinie); [ZIA-Positionspapier 03/2026](https://zia-deutschland.de/wp-content/uploads/2026/03/ZIA-Positionspapier_praxistaugliche-EPBD-Umsetzung.pdf)

**EU-Taxonomie und CRREM**
- (V) Taxonomie-Kriterien (Klimaschutz): Erwerb/Eigentum von Bestandsgebäuden erfordert Energieausweisklasse A oder Zugehörigkeit zu den besten 15 % des nationalen Bestands; Renovierung erfordert mindestens 30 % Primärenergieeinsparung — [Predium](https://predium.de/resource/taxonomie-konform-wirtschaften-stranded-assets-vermeiden-eu-taxonomie-einfach-erklart); [reduco.ai, Stranded Assets](https://reduco.ai/blog/stranded-assets-immobilien-vermeiden)
- (V) Die Kriterien sind 2026 in Überarbeitung: Der vdp hat am 28.04.2026 zum Entwurf eines delegierten Rechtsakts zu den Aktivitäten 7.1, 7.2 und 7.7 Stellung genommen (u. a. Übergangsregel mit 60 % Effizienzsteigerung bei 7.7; Kritik am Ausschluss von EE-Effizienzgewinnen bei 7.2) — [vdp-Pressemitteilung 28.04.2026](https://www.pfandbrief.de/wp-content/uploads/2026/04/20260428_vdp_PM_Kritik-Taxonomie_vdp-Stellungnahme_DE.pdf)
- (V) CRREM: Pfade je Land und Nutzungsart (acht Hauptnutzungstypen); laut Sekundärquelle heißt der Stranding-Zeitpunkt seit Juli 2025 "CRREM Misalignment Year" = erstes Jahr, in dem die CO2- oder Energieintensität des Gebäudes sein 1,5-°C-Budget überschreitet — [reduco.ai, ESG-Benchmarking](https://reduco.ai/blog/immobilienwirtschaft/esg-benchmarking-immobilien-methoden)

**Instandhaltung und Verwaltung**
- (V) Peterssche Formel: Herstellungskosten je m² × 1,5 ÷ 80 = jährliche Instandhaltungsrücklage je m² (Annahme: in 80 Jahren fällt das 1,5-Fache der reinen Herstellungskosten ohne Grundstück an); bei WEG wird mit Faktor 0,7 für das Gemeinschaftseigentum gerechnet. Bei Altbauten sind die Herstellungskosten oft unbekannt, die Formel ist dort kaum anwendbar; Faustregel alternativ 1–1,5 % des Gebäudewerts p. a. — [Dr. Klein](https://www.drklein.de/instandhaltungsruecklage.html); [Interhyp](https://www.interhyp.de/ratgeber/lexikon/instandhaltungsruecklage.html)
- (V) Normierte Ansätze: II. BV 2026 (11,50 / 14,58 / 18,62 €/m²; Verwaltung 372,46 €/WE) für preisgebundenen Wohnraum; ImmoWertV Anlage 3 als Bewertungsmodellansatz (siehe Abschnitt 6) — [Haufe](https://www.haufe.de/immobilien/verwaltung/erhoehung-der-kostenmiete-bei-sozialwohnungen_258_392374.html)
- (V) Preisindex Instandhaltung von Wohngebäuden: +6,0 % ggü. Vorjahr (August 2026) — [Destatis](https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/10/PD26_360_61261.html)
- (V) Typische Bauteil-Lebensdauern aus Ratgeberquellen (nicht normiert): Dach ca. 50 Jahre, Dachdämmung ca. 40 Jahre, Parkett ca. 50 Jahre, Kunststoffboden 15–20 Jahre — [Homeday](https://www.homeday.de/de/immobilienwissen/instandhaltungskosten-haus/)

**Energieerzeugung im Objekt**
- (V) Gemeinschaftliche Gebäudeversorgung (§ 42b EnWG, seit Solarpaket I, Mai 2024): auf ein Gebäude samt Nebenanlagen beschränkt, viertelstündliche Messung erforderlich, Preis frei vereinbar, kein Mieterstromzuschlag; Kopplungsverbot mit dem Mietvertrag gilt. Klassischer Mieterstrom: Zuschlag laut Sekundärquelle ca. 1,6–2,6 ct/kWh. Energy Sharing (§ 42c EnWG) über das öffentliche Netz ist laut mehreren Quellen ab 01.06.2026 nutzbar. Die GGV wird 2026 in der Praxis noch wenig genutzt — [Rödl & Partner, 24.09.2026](https://www.roedl.com/insights/energy-sharing-mieterstrom-einbindung-erzeugungsanlagen/); [ema-energiewelt.de](https://ema-energiewelt.de/wissen/mieterstrom-energiegemeinschaft-2026); [rewis.io, § 42b EnWG](https://rewis.io/gesetze/enwg/p/42b-enwg/)

### Inferences
| Fähigkeit | Einstufung | Begründung |
|---|---|---|
| Instandhaltung wahlweise pauschal (€/m², % der Herstellungskosten, Peters, II. BV, ImmoWertV) oder als bauteilbezogener Maßnahmenplan mit Zyklen und Preisindexierung | Pauschale [M]; Bauteil-Lebenszyklusplan [D] | Pauschalen sind Standard; Bauteilplanung trennt Profi- von Einfachtools |
| CapEx-Plan mit Abgrenzung Instandhaltung / Modernisierung (umlagefähig) / aktivierungspflichtig, je Maßnahme mit Zeitpunkt, Kosten, Förderung, Mietwirkung, Energieeffekt | [M] für Sanierung/Bestand | Verbindet Kosten-, Miet-, Steuer- und Förderlogik |
| Energetischer Steckbrief je Gebäude: Endenergie, Primärenergie (kWh/m²a), Energieträger, Effizienzklasse, CO2-Emissionen vor/nach Maßnahme | [M] | Eingangsgröße für CO2-Kostenaufteilung, Förderfähigkeit, Taxonomie, Bankfragen |
| Preispfade CO2 (BEHG-Korridor 2026/27, ETS 2 ab 2028 als Szenario) und Energieträgerpreise; Bio-Treppe als Brennstoffkostenaufschlag ab 2029 | [M] für Bestand mit fossiler Wärme | Seit GModG ist die fossile Heizung zulässig, aber mit steigenden laufenden Vermieterkosten |
| Heizungs-Variantenvergleich (fossil mit Bio-Treppe und 50-%-Vermieteranteil vs. Wärmepumpe/Fernwärme mit Förderung und § 559e/f-Umlage) | [D] | Neue Entscheidungssituation 2026 |
| CRREM-Abgleich (Stranding/Misalignment Year) je Objekt und im Portfolio | [D] | Von institutionellen Investoren und Banken zunehmend erwartet; Datenlizenz/Tool-Import nötig |
| EU-Taxonomie-Check (Top 15 %/EPC A; −30 % Primärenergie) als Kennzeichen | [D] | Relevant für Fonds, Banken, CSRD-pflichtige Unternehmen; Kriterien 2026 in Revision |
| MEPS-Risikoflag für Nichtwohngebäude (schlechteste 16 %/26 %) mit CapEx-Pflichtzeitpunkt | [D] | Erst mit EPBD-Umsetzung 2027 konkret |
| PV/Mieterstrom/GGV-Modul: Ertrag kWh, Eigenverbrauchsquote, Mieterstrompreis, Einspeisevergütung, Zuschlag, Betriebskosten | [D] | Quartiers- und Neubauprojekte; zusätzliche Erlösquelle |
| Verwaltungskosten als €/Einheit (Wohnen) bzw. % der Miete (Gewerbe), indexiert | [M] | Standard |

### Gaps
- Wortlaut GModG: Die genauen Stufen der Bio-Treppe (15 % ab 2030 ja/nein), Anforderungen an Neubauten, Übergangsfristen und das genaue Inkrafttreten der EPBD-Teile sind nur aus Sekundärquellen belegt, die sich teils widersprechen.
- EPBD-Zwischenziel "16 % der schlechtesten Nichtwohngebäude bis 2030" und Wohngebäude-Durchschnittspfad (−16 % Primärenergie bis 2030, −20 bis −22 % bis 2035) sind dem Researcher bekannt, wurden aber in den Treffern nicht bestätigt; ebenso die neue Energieausweis-Skala A–G und Solarpflichten.
- Aktuelle CRREM-Pfadversion und Lizenzbedingungen wurden nicht an der Primärquelle (crrem.org) geprüft.
- EEG-Vergütungssätze und Mieterstromzuschlag 2026 in amtlicher Höhe (Bundesnetzagentur) wurden nicht ermittelt.
- Normierte Nutzungsdauertabellen (BNB/BBSR "Nutzungsdauern von Bauteilen", VDI 2067) wurden in der Suche nicht gefunden.
- Keine Quelle zu einer rechtlichen Definition der Warmmietenneutralität gefunden (ist ein politisches/unternehmerisches Ziel, kein gesetzlicher Maßstab).

---

## 6. Exit/Restwert: Verkaufsfaktor, ewige Rente, ImmoWertV-Ertragswert, BelWertV-Beleihungswert, Verkaufskosten

### Takeaway
Der Restwert dominiert den Endwert eines VOFI; das Tool braucht mehrere parallele Wertsichten: Investoren-Exit (Faktor/Exit-Yield auf die Miete des Folgejahres), Verkehrswert-Plausibilisierung nach ImmoWertV 2021 (Liegenschaftszins, Bewirtschaftungskosten nach Anlage 3, Restnutzungsdauer) und den konservativeren Beleihungswert nach BelWertV, an dem die Bank den Beleihungsauslauf misst.

### Cited Findings
- (V) ImmoWertV Anlage 3 (Modellansätze Bewirtschaftungskosten), Ausgangswerte: Verwaltungskosten 298 € je Wohnung; Instandhaltungskosten 11,70 €/m² Wohnfläche; Mietausfallwagnis 2 % des Rohertrags bei Wohnnutzung; bei gewerblicher Nutzung Verwaltung 3 % und Mietausfallwagnis 4 % des marktüblich erzielbaren Rohertrags — [gesetze-im-internet.de, ImmoWertV Anlage 3](https://www.gesetze-im-internet.de/immowertv_2022/anlage_3.html); [reduco.ai, Ertragswertverfahren](https://reduco.ai/blog/immobilienverkauf/ertragswertverfahren-immobilie)
- (V) Die Werte für Wohnnutzung werden jährlich nach dem Verbraucherpreisindex fortgeschrieben (Anlage 3 Nr. III; Bezug: VPI Oktober des Vorjahres ggü. Oktober 2001). Fortgeschriebene Werte ab 01.01.2025: 359 € je Wohnung, 429 € je Eigentumswohnung, 47 € je Garage/Stellplatz; Instandhaltung 14,00 €/m² — [steuerschroeder.de](https://www.steuerschroeder.de/blog/bewertung-von-immobilien-bewirtschaftungskosten); [Oberer Gutachterausschuss Brandenburg, BewKo 2025](https://gutachterausschuss.brandenburg.de/sixcms/media.php/9/BewKo_2025.pdf)
- (V) Für 2026: VPI Oktober 2025 = 123,0 und Oktober 2001 = 77,1 (2020 = 100). Daraus ergibt sich ein Faktor von rund 1,595 und rechnerisch ca. 367 € je Wohnung, ca. 439 € je Eigentumswohnung, ca. 48 € je Garage und ca. 14,40 €/m² Instandhaltung. Diese 2026er-Werte sind eine Berechnung aus den Indexständen, keine veröffentlichte Tabelle — [steuerschroeder.de](https://www.steuerschroeder.de/blog/bewertung-von-immobilien-bewirtschaftungskosten)
- (V) Gutachterausschüsse und IVD leiten Liegenschaftszinssätze 2026 modellkonform mit Gesamtnutzungsdauer, Restnutzungsdauer und Bewirtschaftungskosten nach den Anlagen 1–3 ImmoWertV 2021 ab; Liegenschaftszinssätze dürfen nur mit denselben Modellansätzen angewendet werden — [IVD, Liegenschaftszinssätze 2026](https://ivd.net/wp-content/uploads/2025/12/2026_Liegenschaftszinsaetze_.pdf); [Gutachterausschuss Berlin](https://www.berlin.de/gutachterausschuss/_assets/amarktinformationen/adaten-zur-wertermittlung/05-02-010-2600.pdf)
- (V) BelWertV-Novelle (Teil der Pfandbriefrechtlichen Änderungsverordnung), in Kraft seit 08.10.2022: dynamisches Modell für Mindestkapitalisierungszinssätze auf Basis der Rendite 30-jähriger Bundesanleihen (§ 12 Abs. 4); erstmals statistische Bewertungsverfahren für Ein-/Zweifamilienhäuser und Eigentumswohnungen zugelassen — [Haufe, BelWertV-Novelle](https://www.haufe.de/immobilien/investment/wertermittlungsportale-immobilienbewertung-per-knopfdruck_256_501422.html); [Staiber, GuG 2/2022 (HfWU)](https://www.hfwu.de/fileadmin/user_upload/FWR/Personalprofiles_FWR/staiber.markus/Veroeffentlichungen/GuG_2_2022_Staiber_BelWertV_fv.pdf)
- (V, unsicher) Laut einer Fachseite wurden die Mindestkapitalisierungszinssätze zum 01.01.2024 auf 5,5 % (wohnwirtschaftlich) und 6,5 % (gewerblich) angehoben (zuvor 5,1 % bzw. 6,1 %); für bestimmte Nutzungsarten (Warenhäuser, SB-/Fachmärkte, Hotels, Kliniken, Lager/Logistik) gelten höhere Mindestsätze, für Produktionsimmobilien 7 %. Nicht gegen die amtliche Fassung geprüft; Werte für 2026 unbekannt — [HypZert-Meldungen](https://www.hypzert.de/en/node/1974?page=6); [gesetze-im-internet.de, BelWertV Anlage 3](https://www.gesetze-im-internet.de/belwertv/anlage_3.html)
- (FW) Bewirtschaftungskosten im Beleihungswert: Mindestansatz 15 % des Rohertrags, zusätzlich ggf. Modernisierungsrisiko (§ 11 BelWertV); Beleihungsgrenze für Pfandbriefdeckung 60 % des Beleihungswerts (§ 14 PfandBG) — nachprüfbar bei [gesetze-im-internet.de, § 11 BelWertV](https://www.gesetze-im-internet.de/belwertv/__11.html)
- (V) BelWertV: Bei vermieteten Eigentumswohnungen und Ein-/Zweifamilienhäusern ist eine vermietungsbedingte Wertminderung nachvollziehbar abzuziehen — [kreditwesen.de, Immobilien & Finanzierung 12/2022](https://www.kreditwesen.de/sites/default/files/flipbook/insert/84554/if_12-2022_dsd_wuensche_fischer_S2.pdf)
- (V) Für die steuerliche Bewertung nach BewG gelten seit 01.01.2026 neue Bewirtschaftungskostenwerte, die auf denselben indexierten Ansätzen beruhen (nicht mit ImmoWertV-Verkehrswert verwechseln) — [steuerschroeder.de](https://www.steuerschroeder.de/blog/bewertung-von-immobilien-bewirtschaftungskosten)

### Inferences
| Fähigkeit | Einstufung | Begründung |
|---|---|---|
| Exit über Verkaufsfaktor bzw. Exit-Yield auf die nachhaltige Miete des Jahres n+1; Angabe brutto/netto; Abzug Verkaufskosten (Makler, Beratung, ggf. Vorfälligkeitsentschädigung) und Restschuld | [M] | Standard-Endwertlogik |
| Alternative Restwertmethoden wählbar: ewige Rente (mit Wachstumsrate), Ertragswert mit endlicher Restnutzungsdauer und Bodenwert, Sachwert/Bodenwert als Untergrenze | [M] (mind. zwei Methoden); volle Auswahl [D] | Wohnungswirtschaft denkt in Restnutzungsdauer, Investoren in Exit-Yield |
| Abgezinster Instandhaltungsstau und CapEx-Bedarf (auch ESG-CapEx) im Exit berücksichtigen | [M] | Sonst systematisch überhöhte Restwerte |
| Ertragswert nach ImmoWertV 2021 als Nebenrechnung mit Anlage-3-Ansätzen (jährlich fortgeschriebene Stammdaten) und Liegenschaftszins | [D] | Plausibilisierung gegen Gutachterausschuss-Daten; kein Ersatz für Gutachten |
| Beleihungswert-Schätzung nach BelWertV (Mindestkapitalisierungszins, mind. 15 % Bewirtschaftungskosten, nachhaltige Miete) → Beleihungsauslauf und Realkreditanteil (60 %) | [D] | Erklärt Finanzierungsstruktur und Marge aus Banksicht; für Berater mit Bankdialog sehr nützlich |
| Wertentwicklungspfad je Jahr (Marktwert, LTV-Verlauf) statt nur Exit-Zeitpunkt | [M] | Voraussetzung für LTV-Covenant-Test und Anschlussfinanzierung |
| Sensitivität Exit-Faktor × Mietwachstum × Zins | [M] | Restwert ist der stärkste Ergebnistreiber |

- Modellkonformität ist ein unterschätzter Punkt: Ein vom Gutachterausschuss veröffentlichter Liegenschaftszins darf nur mit den zugehörigen Anlage-3-Bewirtschaftungskosten kombiniert werden; ein Tool sollte bei der Ertragswert-Nebenrechnung nicht die tatsächlichen Bewirtschaftungskosten einsetzen.

### Gaps
- Amtlich veröffentlichte ImmoWertV-Anlage-3-Werte für 2026 wurden nicht gefunden (nur rechnerisch aus VPI ableitbar).
- Aktuelle BelWertV-Mindestkapitalisierungszinssätze für 2026 und die genauen Aufschläge je Nutzungsart sind nicht verifiziert; der Mindestansatz 15 % und die 60-%-Grenze wurden in den Treffern nicht bestätigt.
- Keine Quelle zu marktüblichen Verkaufskosten (Prozentansätze) recherchiert.
- Aktuelle Marktrenditen/Faktoren je Assetklasse 2026 (bulwiengesa, JLL, vdp-Index) wurden nicht erhoben.

---

## 7. Developer/Bauträger: Residualwert, Vertrieb, MaBV-Raten, Forward Deal/Funding, Projektfinanzierung, Marge, Erbbaurecht

### Takeaway
Die Developer-Rechnung ist eine zeitlich kurze, liquiditätsgetriebene Kalkulation: Erlöse nach Vertriebsplan und MaBV-Ratenlogik bzw. Forward-Struktur, Kosten nach Bauablauf, mehrschichtige Finanzierung, Ergebnisgrößen Trading Profit, Marge auf Kosten/Erlös und Projekt-IRR; das Residualwertverfahren ist die Umkehrrechnung zum maximal tragbaren Grundstückspreis.

### Cited Findings
- (V) Residualwertverfahren: erwarteter Verkehrswert/Erlös des fertigen Projekts abzüglich aller Projektkosten (Bau, Planung, Nebenkosten, Finanzierung) und einer Entwicklermarge ergibt den tragbaren Grundstückspreis — [immoportal.com, Residualwertverfahren](https://www.immoportal.com/glossar/residualwertverfahren-extraktionsverfahren)
- (V) Als Beispielgröße nennt eine englischsprachige Quelle eine Zielmarge von 20 % auf die Gesamtentwicklungskosten (Return on Cost); eine deutsche Quelle mit Marktstandard wurde nicht gefunden — [A.CRE, Residual Land Value](https://www.adventuresincre.com/glossary/residual-land-value-analysis/)
- (V) MaBV § 3 Abs. 2: Der Bauträger darf Zahlungen nur in höchstens sieben Teilbeträgen nach Bauablauf entgegennehmen; erste Rate 30 % der Vertragssumme (bei Erbbaurecht 20 %) nach Beginn der Erdarbeiten; die übrigen Raten sind Vomhundertsätze der restlichen Vertragssumme, letzte Rate 5 % nach vollständiger Fertigstellung. Voraussetzungen nach § 3 Abs. 1 (u. a. Auflassungsvormerkung, Lastenfreistellung, Baugenehmigung) müssen vor jeder Entgegennahme erfüllt sein — [lexetius.com, § 3 MaBV](https://lexetius.com/MaBV/3); [bauprofessor.de, Abschlagszahlungen Bauträgervertrag](https://www.bauprofessor.de/abschlagszahlungen-bautraegervertrag/)
- (FW) Vollständiger Katalog der Bausteine (Anteile an der Restsumme nach der Grundstücksrate): 40 % Rohbaufertigstellung einschl. Zimmererarbeiten; 8 % Dachflächen/Dachrinnen; je 3 % Rohinstallation Heizung, Sanitär, Elektro; 10 % Fenstereinbau einschl. Verglasung; 6 % Innenputz; 3 % Estrich; 4 % Fliesen im Sanitärbereich; 12 % Bezugsfertigkeit Zug um Zug gegen Besitzübergabe; 3 % Fassadenarbeiten; 5 % vollständige Fertigstellung — nachprüfbar bei [lexetius.com, § 3 MaBV](https://lexetius.com/MaBV/3)
- (V) Alternative § 7 MaBV: Mit einer Bürgschaft nach § 7 darf der Bauträger Zahlungen auch abweichend von § 3 Abs. 2 entgegennehmen — [BGH, Urteil vom 09.12.2010, VII ZR 206/09 (rewis.io)](https://rewis.io/urteile/urteil/qva-09-12-2010-vii-zr-20609/)
- (V) Forward Deal: keine finanzielle Beteiligung des Käufers an der Entwicklung (Kaufpreis bei Fertigstellung); in der Regel als Asset Deal strukturiert. Forward Funding: Endinvestor steigt früh ein und finanziert nach Baufortschritt — [Heuking, Projektentwicklung: Transaktionen im Bestand und Forward Deals](https://www.hlc.com/de/publications/projektentwicklung-transaktionen-im-bestand-und-forward-deals); [TU Wien, Hafez 2019](https://repositum.tuwien.at/bitstream/20.500.12708/7646/2/Hafez%20Nadja%20-%202019%20-%20Finanzierung%20von%20Immobilien-Projektentwicklungen%20durch...pdf)
- (V) Eigenkapital: Für Projektentwicklungen wird ein Eigenkapitalanteil von rund 20 % erwartet, abhängig von der Vorvermietung (ältere Fachquelle); Mezzanine-Kapital ist nachrangig und wird von Banken häufig wirtschaftlich wie Eigenkapital behandelt (Equity- vs. Debt-Mezzanine) — [Immobilien & Finanzierung (kreditwesen.de)](https://www.kreditwesen.de/sites/default/files/content/articledownloads/2015/09/lak_07_19_679-681_0.pdf); [Immobilien & Finanzierung (kreditwesen.de)](https://kreditwesen.de/sites/default/files/content/articledownloads/2015/09/lak_13_19_698-699.pdf)
- (V) Marktumfeld 2026: Banken finanzieren Projektentwicklungen selektiv ("Wer noch Kredit bekommt"); Refinanzierbarkeit gilt als neue Core-Qualität — [private banking magazin](https://www.private-banking-magazin.de/immobilien-zwischen-risikodisziplin-und-renditedruck-projektentwicklung/); [cash-online](https://www.cash-online.de/a/refinanzierbarkeit-ist-die-neue-core-qualitaet-717126/)
- (V) Baupreisrisiko 2026: +5,5 % p. a. (siehe Abschnitt 1) — [Destatis](https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/10/PD26_360_61261.html)

### Inferences
| Fähigkeit | Einstufung | Begründung |
|---|---|---|
| Vertriebsplan: Einheitenliste mit Preisen (€/m², Stellplätze), Abverkaufsgeschwindigkeit (Einheiten/Monat), Vorverkaufsstand, Preisstaffelung; Erlöszufluss = Verkaufszeitpunkt × MaBV-Bautenstand | [M] für Bauträger | MaBV koppelt Liquidität an Bauablauf und Vertrieb |
| MaBV-Ratenplan-Generator (7 Raten aus 13 Bausteinen, 30 %/20 % Grundstücksrate) verknüpft mit Bauzeitenplan; Alternative § 7-Bürgschaft (Avalprovision) | [M] für Bauträger | Gesetzlich zwingende Zahlungslogik |
| Globalverkauf: Forward Deal (Einmalzahlung bei Übergabe, volle Zwischenfinanzierung) vs. Forward Funding (Kaufpreisraten nach Baufortschritt, Verzinsung der Abschläge) als Varianten | [M] für Developer | Finanzierungsbedarf und Marge unterscheiden sich fundamental |
| Residualwertrechner (rückwärts: max. Grundstückspreis bei Zielmarge; vorwärts: Marge bei gegebenem Preis), inkl. Erwerbsnebenkosten und Finanzierung des Grundstücks | [M] für Developer | Standard-Ankaufsentscheidung |
| Finanzierungskaskade: Eigenkapital → Mezzanine/Nachrang (PIK-Zins, Kicker) → Senior-Bauzeitkredit (Inanspruchnahme nach Baufortschritt, Rückführung aus Kaufpreisraten) → Avale; Auszahlungsvoraussetzungen wie Vorverkaufs-/Vorvermietungsquote als Bedingung | [M]; Mezz-Kicker/Waterfall zwischen JV-Partnern [D] | Mehrschichtige Finanzierung ist Regelfall |
| Kennzahlen: Trading Profit absolut, Marge auf Gesamtkosten (GIK) und auf Erlös (GDV), Projekt-IRR und Eigenkapital-IRR, Equity Multiple, Peak Equity/Peak Debt, LTC, Break-even-Verkaufspreis und -Vermietungsstand | [M] | Erwartete Entscheidungsgrößen von Gremien und Banken |
| Bauabschnitte/Phasen mit eigener Kosten-, Vertriebs- und Finanzierungslogik | [M] bei Quartier/größeren Projekten | Realität großer Entwicklungen |
| Erbbaurecht: Erbbauzins (% vom Bodenwert), Wertsicherungsklausel (VPI, Anpassungsintervall), Laufzeit/Heimfall/Entschädigung; reduzierte MaBV-Grundstücksrate (20 %) | [M] für kommunale/kirchliche Grundstücke; sonst [D] | Wachsende Bedeutung der Konzeptvergabe im Erbbaurecht |
| Gewährleistungsrückstellung, Vertriebskosten, Sonderwunsch-Erlöse, Bauzeitverzug-Szenario (Zinsmehrkosten, Vertragsstrafen) | [D] | Risikotiefe |
| Umsatzsteuer/Grunderwerbsteuer-Besonderheiten des Bauträgers und § 13b UStG | Schnittstelle | Steuer-Researcher |

- Der Übergang "Developer baut und behält" (Neubau zur Vermietung) sollte ohne Modellbruch möglich sein: gleiche Kostenseite, anderes Erlösmodul; Vergleich "Verkaufen vs. Halten" ist eine naheliegende Beratungsleistung [D].

### Gaps
- Keine deutsche Quelle mit Marktstandard für Developer-Margen (häufig genannte 15–20 % auf Kosten sind nicht belegt), Vorverkaufs-/Vorvermietungsauflagen der Banken oder aktuelle Mezzanine-Konditionen gefunden; die bulwiengesa-Projektentwicklerstudie (Methodik: [PE-Studie 2019](https://archiv.bulwiengesa.de/sites/default/files/pe-studie_2019_methodik.pdf)) wurde nicht inhaltlich ausgewertet.
- Der MaBV-Ratenkatalog ist nur in den Eckwerten (7 Raten, 30 %/20 %, 5 % Schlussrate) durch Suchtreffer bestätigt; die Einzelprozentsätze stammen aus Fachwissen.
- Zum Erbbaurecht (übliche Erbbauzinssätze, Wertsicherung nach § 9a ErbbauRG) wurde nichts recherchiert.
- §§ 650u/650v BGB (Bauträgervertrag) und Sicherheiten nach § 650m BGB wurden nicht vertieft.

---

## 8. Finanzierung aus Bankensicht: Darlehensarten, Anschlussfinanzierung, Covenants, Kapitaldienstfähigkeit, Derivate, Bausparen

### Takeaway
Banken prüfen cashflow- und covenantbasiert: LTV/LTC, DSCR, ICR und zunehmend Debt Yield, getestet über die gesamte Laufzeit inklusive Refinanzierungszeitpunkt. Ein professionelles Tool muss jede Darlehenstranche periodengenau abbilden und das Anschlussfinanzierungsrisiko explizit rechnen; konkrete marktübliche Schwellenwerte für Deutschland ließen sich in der Recherche nicht belegen.

### Cited Findings
- (V) Immobilienbezogene Financial Covenants in deutschen Kreditverträgen: Loan to Value, Loan to Cost, Interest Cover Ratio, Debt Service Coverage Ratio — [Latham & Watkins, Immobilienfinanzierungen](https://www.lw.com/de/people/admin/upload/SiteAttachments/Immobilienfinanzierungen–Welche-Rechtsthemen-Unternehmen-präsent-haben-sollten.pdf)
- (V) Covenants werden oft zweistufig ("soft"/"hard") vereinbart. LTV = Darlehen/Marktwert, typischerweise jährlich getestet; Rechtsfolgen meist Sondertilgung, Cash Trap (Ansparen auf Reservekonto) oder Cash Sweep (Zwangstilgung), seltener Fälligstellung. Rechenbeispiele: 50 Mio. € Darlehen bei 80 Mio. € Marktwert = 62,5 % LTV; 1.500 T€ Cashflow bei 750 T€ Zins und 500 T€ Tilgung = ICR 200 %, DSCR 120 % — [TH Aschaffenburg, Vorlesung Immobilieninvestition und -finanzierung (Mühlfried), 2025](https://moodle.th-ab.de/pluginfile.php/501651/mod_resource/content/0/20250710%20IIF%20-%20M%C3%BChlfried.pdf)
- (V) Bewertungsbasis und Berechnungsmethodik der Covenants müssen im Kreditvertrag klar definiert sein; bei Verletzung sind Waiver, Covenant Holiday, Teilrückzahlung oder Nachschuss von Eigenkapital üblich — [Immobilien & Finanzierung (kreditwesen.de)](https://www.kreditwesen.de/sites/default/files/content/articledownloads/2015/07/lak_14_22_814-815.pdf); [CMS, Immobilienfinanzierungen](https://cms.law/de/deu/legal-updates/immobilienfinanzierungen-in-zeiten-von-corona)
- (V) Marktlage 2026: "Cash-Flow-Ära"; Fälligkeitswelle (Maturity Wall) von geschätzt 82 Mrd. € in Deutschland 2026; konservativere Beleihungsausläufe und klar definierte Covenants — [KPMG, Schlüsselthemen Immobilienmarkt 2026](https://klardenker.kpmg.de/financialservices-hub/ein-weiteres-jahr-in-der-cash-flow-aera-steht-bevor-schluesselthemen-fuer-den-deutschen-immobilienmarkt-2026/); [EY, Die Maturity Wall rollt weiter](https://www.ey.com/de_de/insights/tax-law-magazine/die-maturity-wall-rollt-weiter)
- (V) Debt Yield (NOI/Darlehen) wird als Maß nachhaltiger Kapitaldienstfähigkeit bei Refinanzierungen herangezogen; eine US-Analyse 2026 nennt Spannen von 7–10 % und bezeichnet ihn als oft strengere Grenze als den DSCR (nicht auf Deutschland übertragbar) — [cash-online](https://www.cash-online.de/a/refinanzierbarkeit-ist-die-neue-core-qualitaet-717126/); [CommercialIQ](https://commercialiq.lovable.app/insights/dscr-what-lenders-actually-want-2026)
- (V) Anschlussfinanzierung: Nach Ende der Zinsbindung wird die Restschuld zum dann gültigen Zins fortgeführt; das Zinsänderungsrisiko ist von Beginn an einzuplanen — [transparent-beraten.de](https://www.transparent-beraten.de/kapitalanlage/immobilien/finanzierung)
- (V) Beleihungswert als Bezugsgröße der Bank: siehe Abschnitt 6 (BelWertV, dynamische Mindestkapitalisierungszinssätze seit 08.10.2022) — [Haufe](https://www.haufe.de/immobilien/investment/wertermittlungsportale-immobilienbewertung-per-knopfdruck_256_501422.html)

### Inferences
| Fähigkeit | Einstufung | Begründung |
|---|---|---|
| Beliebig viele Darlehenstranchen je Projekt: Annuität, Tilgungsdarlehen, endfällig, tilgungsfreie Anlaufjahre, Förderdarlehen mit Tilgungszuschuss; Zinsbindung ≠ Laufzeit; unterjährige Zahlweise | [M] | Realität jeder Wohnungswirtschafts- und Projektfinanzierung |
| Anschlussfinanzierung je Tranche mit eigenem Anschlusszins (Szenario/Forward-Kurve), Warnung wenn Zinsbindungsende im Betrachtungszeitraum ohne Anschlussannahme | [M] | Im Briefing als typischer Fehler genannt; Maturity Wall 2026 |
| Auszahlung nach Baufortschritt, Bereitstellungszinsen (zinsfreie Zeit, Satz), Disagio, Bearbeitungs-/Strukturierungsgebühren, Avalprovisionen | [M] | Bauzeitfinanzierung |
| Forward-Darlehen (Zinsaufschlag je Vorlaufmonat) als Sicherungsvariante | [D] | Vergleichsrechnung |
| Sondertilgungsrechte, Vorfälligkeitsentschädigung beim Exit vor Zinsbindungsende | [M] (VFE mind. als Eingabe) | Exit-Szenarien sonst verzerrt |
| Covenant-Monitor je Periode: LTV (auf Marktwertpfad), LTC, DSCR, ICR, Debt Yield, mit Soft-/Hard-Schwellen, Ampel und Headroom; Cash-Trap/Cash-Sweep-Mechanik | Kennzahlen [M]; Mechanik [D] | Bankenstandard |
| Kapitaldienstfähigkeit/Kapitaldienstgrenze je Objekt und Unternehmen, Stresstest Zins +x bp / Miete −y % | [M] | Kernfrage jeder Kreditentscheidung |
| Zinsderivate vereinfacht: Swap (variabel → fix), Cap (Prämie, Strike) | [D] | Nur bei variabler Finanzierung (Developer, Gewerbe) relevant |
| Bausparen/Bausparvorfinanzierung als Zinssicherungsinstrument (Ansparphase, Zuteilung, Bauspardarlehen) | [D] | Nischenanforderung der Wohnungswirtschaft |
| Banken-Sicht: Beleihungswert, Beleihungsauslauf, Realkredit-/Blankoanteil | [D] | Siehe Abschnitt 6 |
| Sicherheitenspiegel (Grundschulden, Rang) und Darlehensspiegel über das Portfolio | [D] | Unternehmensebene |

### Gaps
- Keine belastbare Quelle zu marktüblichen Covenant-Schwellen in Deutschland 2026 (z. B. LTV-Obergrenzen, DSCR-/ICR-Mindestwerte, Debt-Yield-Untergrenzen) gefunden; naheliegende Quellen wären das BF.Quartalsbarometer (bulwiengesa, [Q4/2025](https://bulwiengesa.de/sites/default/files/2025-12/bf.qb_q4_2025_extern.pdf), nicht ausgewertet), vdp und JLL-Finanzierungsreports.
- Zu Bausparen in der Wohnungswirtschaft, Forward-Darlehen-Aufschlägen und Bereitstellungszins-Usancen wurde keine Quelle recherchiert.
- Regulatorische Treiber aus Banksicht (CRR III, MaRisk, ESG-Datenanforderungen der Banken an Kreditnehmer) wurden nicht vertieft.
- Aktuelles Zinsniveau 2026 (Bauzinsen, Swapsätze) wurde nicht erhoben.

---

## 9. Quartiers-, Portfolio- und Unternehmensebene: Aggregation, Bauabschnitte, Energieversorgung, integrierte Unternehmensplanung

### Takeaway
Wohnungsunternehmen denken nicht nur in Einzelprojekten: Der GdW-Prüfungsverband-Kontext beschreibt die integrierte Gesamtplanung aus Plan-Bilanz, Plan-GuV und Plan-Kapitalflussrechnung als höchste Entwicklungsstufe, gespeist aus Teilplänen (Investition, Finanzierung, Mieterlöse, Abschreibung, Instandhaltung). Ein Projekt-VOFI sollte deshalb seine Wirkungen als Jahresscheiben in diese Unternehmensplanung übergeben können; eine vollintegrierte Planbilanz im Tool selbst ist Differenzierung, die Übergabefähigkeit ist Pflicht.

### Cited Findings
- (V) Schulungsunterlage aus dem GdW-Verbandsumfeld (VNW, September 2026) zur Prüfung der Unternehmensplanung: Unterscheidung strategische/operative Planung; die integrierte Gesamtplanung mit Plan-Bilanz, Plan-GuV und Plan-Kapitalflussrechnung wird als am höchsten entwickelte Stufe eingeordnet; Basis sind konsistente Teilpläne (Investitions-, Finanzierungs-, Mieterlös-, Abschreibungs-, Instandhaltungs-, Personalplanung). Verweis auf Berichtspflichten gegenüber dem Aufsichtsrat (§ 90 Abs. 1 Nr. 1 AktG; GdW-Mustersatzung für Wohnungsgenossenschaften § 23 Abs. 3) — [Schulungsunterlage "Prüfung der Unternehmensplanung" (evenito)](https://fs.evenito.com/render/f1b7385d-5dd6-47d3-b107-6e2b21d0eda0)
- (V) Portfolio- und Investitionsplanung landeseigener Wohnungsunternehmen (Berlin, Schulungsmaterial 2023 der Wohnraumversorgung Berlin): Schritte Investitionsplanung → Einteilung in Jahresscheiben → Planbilanz/Plan-GuV — [berlin.de, WVB-Schulungsmaterial Investitionsplanung 2023](https://berlin.de/sen/wohnen/_assets/wvb/wvb_schulungsmaterial_2023-investitionsplanung.pdf)
- (V) Die Verordnung über die Gliederung des Jahresabschlusses von Wohnungsunternehmen (JAbschlWUV) wurde im Juli 2023 neu gefasst; Planbilanz und Plan-GuV orientieren sich an dieser Gliederung — [Haufe, Erläuterungen zur Rechnungslegung der Wohnungsunternehmen, Vorwort 4. Aufl.](https://www.haufe.de/id/beitrag/vorwort-zur-4-auflage-der-erlaeuterungen-zur-rechnungslegung-der-wohnungsunternehmen-HI10365116.html)
- (V) Wohnungswirtschaftliche Lehrbuchpraxis: Investitionsrechnung (Kapitalwert, interner Zinsfuß) am Beispiel einer Modernisierungsmaßnahme einschließlich Liquiditätsbetrachtung — [HTW Berlin, Inhaltsverzeichnis Lehrbuch](https://sisis.rz.htw-berlin.de/inh2007/12358129.pdf)
- (V) Unternehmenssteuerung in Wohnungsgenossenschaften wird als Steuerung "in komplexen Märkten" mit Kennzahlensystemen diskutiert — [Universität Münster, IfG-Vortrag Schnake](https://www.wiwi.uni-muenster.de/ifg/sites/ifg/files/downloads/pw/presenations/schnake_unternehmensteuerung_in_komplexen_maerkten.pdf)
- (V) Quartiers-Energieversorgung, rechtliche Leitplanken: gemeinschaftliche Gebäudeversorgung nur je Gebäude (§ 42b EnWG), Energy Sharing über das öffentliche Netz (§ 42c EnWG) seit 2026; Wärmelieferung/Contracting nur bei Kostenneutralität umlegbar (§ 556c BGB, Reform angekündigt) — [Rödl & Partner, Energy Sharing/Mieterstrom](https://www.roedl.com/insights/energy-sharing-mieterstrom-einbindung-erzeugungsanlagen/); [Rödl & Partner, Umstellung Wärmeversorgung](https://www.roedl.com/insights/nebenkosten-umlage-umstellung-waermeversorgung/)
- (V) EPBD-Logik für Wohngebäude ist ein Portfolio-/Durchschnittsansatz, kein Einzelgebäudezwang; das stützt portfolioweite Sanierungsfahrpläne — [reduco.ai, EPBD Wohngebäude Portfolioansatz](https://reduco.ai/blog/immobilienwirtschaft/epbd-wohngebaeude-portfolio-ansatz-2030)
- (V) Portfoliorisiko Refinanzierung: Fälligkeitswelle 2026 (ca. 82 Mrd. €) — [KPMG](https://klardenker.kpmg.de/financialservices-hub/ein-weiteres-jahr-in-der-cash-flow-aera-steht-bevor-schluesselthemen-fuer-den-deutschen-immobilienmarkt-2026/)

### Inferences
| Fähigkeit | Einstufung | Begründung |
|---|---|---|
| Hierarchie Unternehmen → Portfolio/Quartier → Projekt → Bauabschnitt → Gebäude → Einheit(engruppe) mit Aggregation aller Cashflows und Kennzahlen | [M] | Quartierssanierung und Portfolioankäufe sind sonst nicht abbildbar |
| Bauabschnitte mit zeitlichem Versatz, gemeinsamen Kosten (Erschließung, Tiefgarage, Energiezentrale) und Umlageschlüsseln | [M] für Quartier | Kostenallokation bestimmt Einzelwirtschaftlichkeit |
| Quersubventionierung sichtbar machen: Deckungsbeitrag je Gebäude/Nutzungsart (frei finanziert ↔ gefördert ↔ Gewerbe) und Gesamtergebnis | [M] für Mixed-Use/Quartier, kommunale Unternehmen | Gremien fragen nach Einzel- und Gesamtwirtschaftlichkeit |
| Jahresscheiben-Export je Projekt: Investitionen (aktivierungsfähig/Aufwand), Zugänge Anlagevermögen, Abschreibungen, Zuschüsse, Darlehensaufnahme/Tilgung/Zins, Mieterlöse, Instandhaltung → für Wirtschafts- und Finanzplan | [M] für Wohnungsunternehmen | Teilpläne speisen die Unternehmensplanung |
| Integrierte Plan-GuV/Planbilanz/Plan-Kapitalflussrechnung nach HGB/JAbschlWUV im Tool (Projekt-Delta und "Unternehmen mit/ohne Maßnahme") | [D] | Von Prüfungsverband als höchste Stufe beschrieben; ersetzt aber kein ERP-Planungsmodul (Aareon/SAP etc.) |
| Unternehmens-Kennzahlenwirkung: Eigenkapitalquote, Verschuldungsgrad, Zinsdeckung, Kapitaldienstdeckung, Tilgungskraft, Instandhaltung €/m² vor/nach Projekt | [D] | Aufsichtsrats- und Bankensicht |
| Portfoliokennzahlen: Ø-Miete, Leerstand, Fluktuation, WALT, NOI-Rendite, LTV, DSCR, CO2-Intensität, CRREM-Status, Fälligkeitsprofil Darlehen/Bindungen | [M] (Basis), ESG-Teil [D] | Reporting-Standard |
| Energiezentrale/Wärmenetz als eigenes Teilprojekt: Investition, Förderung, Wärmepreis (Grund-/Arbeitspreis), Contracting-Variante vs. Eigenbetrieb, Kostenneutralitätsprüfung § 556c | [D] | Typisch für energetische Quartierssanierung |
| PV/Mieterstrom/GGV je Gebäude, Aggregation im Quartier | [D] | Siehe Abschnitt 5 |
| Portfoliopriorisierung (Ranking von Maßnahmen nach Kapitalwert/CO2-Vermeidungskosten unter Budgetrestriktion) | [D] | Strategische Beratung |

- Zur Leitfrage "Erwarten Wohnungsunternehmen, Aufsichtsräte und Banken eine integrierte Planbilanz?": Die Quellen belegen, dass eine integrierte Unternehmensplanung als Best Practice gilt und geprüft wird. Sie belegen nicht, dass diese aus dem Investitionsrechnungstool selbst kommen muss. Folgerung: Pflicht ist eine saubere, HGB-nahe Übergabe der Projektwirkungen (Jahresscheiben); eine eigene integrierte Planrechnung ist ein starkes Differenzierungsmerkmal für kleinere Unternehmen ohne ERP-Planungsmodul und für Berater.

### Gaps
- Keine GdW-Arbeitshilfe mit konkreten Vorgaben zur Investitionsrechnung oder zum Aufbau des Wirtschaftsplans gefunden (GdW-Arbeitshilfen sind überwiegend kostenpflichtig).
- Keine Primärquelle, ob Banken bei Wohnungsunternehmen standardmäßig eine Mehrjahres-Planbilanz verlangen; plausibel, aber unbelegt.
- Kommunalrechtliche Vorgaben (Eigenbetriebsverordnungen, Wirtschaftsplanpflicht nach Gemeindeordnung, mittelfristige Finanzplanung über fünf Jahre) wurden nicht recherchiert.
- Wärmenetz-Wirtschaftlichkeit (BEW-Förderung, AVBFernwärmeV-Preisgleitklauseln, kommunale Wärmeplanung) wurde nicht recherchiert.

---

## 10. Erwartete Outputs: Gremienvorlage, Bankenunterlage, Förder-Wirtschaftlichkeitsberechnung, Soll-Ist, Szenarien, Kennzahlen, Liquidität

### Takeaway
Förderbanken verlangen eigene Wirtschaftlichkeitsberechnungs-Formulare je Bundesland (z. B. NBank, Thüringer Aufbaubank), die inhaltlich der II.-BV-Struktur folgen (Gesamtkosten, Finanzierungsplan, Aufwendungen/Erträge). Ein Tool muss diese Sichten aus demselben Datenmodell erzeugen können; daneben erwarten Gremien und Banken standardisierte Kennzahlen-, Cashflow- und Szenarioberichte.

### Cited Findings
- (V) Die NBank (Niedersachsen) stellt ein eigenes Formular "Wirtschaftlichkeitsberechnung" für die Antragstellung bereit und veröffentlicht die II. BV als Rechtsgrundlage — [NBank, Formular Wirtschaftlichkeitsberechnung](https://www.nbank.de/medien/nb-media/Downloads/Formulare-zur-Antragstellung/Wirtschaftlichkeitsberechnung.pdf); [NBank, II. BV](https://NBank.de/medien/nb-media/Downloads/Rechtliche-Grundlagen/Sonstige-rechtliche-Grundlagen/II.-BV-Zweite-Berechnungsverordnung.pdf)
- (V) Die Thüringer Aufbaubank verwendet einen "Erfassungsbogen Objektwirtschaftlichkeitsberechnung", der "der ersten Einschätzung der Tragfähigkeit im Rahmen der sozialen Mietwohnraumförderung" dient — [TAB, Erfassungsbogen](https://dokumente.aufbaubank.de/862739-TAB_Erfassungsbogen_Objektwirtschaftlichkeitsberechnung.pdf)
- (V) NRW: Die Wohnraumförderbestimmungen (WFB) regeln Vordrucke und Vertragsmuster; die NRW.BANK prüft seit Förderjahr 2023 die Gesamtkosten im Mietwohnungsneubau — [recht.nrw.de, WFB](https://recht.nrw.de/lrmb/verwaltungsvorschrift/17022020-wohnraumfoerderungsbestimmungen-wfb-runderlass-des-ministeriums/); [NRW.BANK, Hilfestellung Baukosten](https://www.nrwbank.de/.galleries/downloads/Presse/publikationen-wohnungsmarktbeobachtung/aktuelle-ergebnisse/Hilfestellung-fuer-Kommunen-Baukosten-WRF-2025.pdf)
- (V) Struktur der Wirtschaftlichkeitsberechnung im preisgebundenen Wohnungsbau: laufende Aufwendungen = Kapitalkosten + Bewirtschaftungskosten; Ergebnis ist die Kostenmiete — [Kreis Viersen, FAQ Wirtschaftlichkeitsberechnung](https://www.kreis-viersen.de/system/files/dokumente/FAQs%20zum%20Thema%20Wirtschaftlichkeitsberechnung.pdf)
- (V) Banksicht: Kreditverträge erfordern laufende Covenant-Berechnung auf klar definierter Bewertungs- und Berechnungsbasis (Reporting-Pflicht des Kreditnehmers) — [Immobilien & Finanzierung (kreditwesen.de)](https://www.kreditwesen.de/sites/default/files/content/articledownloads/2015/07/lak_14_22_814-815.pdf)
- (V) Gremiensicht Wohnungsunternehmen: Vorstand/Geschäftsführung berichtet dem Aufsichtsrat über die Unternehmensplanung (§ 90 AktG analog, GdW-Mustersatzung) — [Schulungsunterlage Prüfung der Unternehmensplanung](https://fs.evenito.com/render/f1b7385d-5dd6-47d3-b107-6e2b21d0eda0)
- (V) DIN 276 sieht die Kostenfeststellung als letzte Stufe vor; Soll-Ist-Vergleiche knüpfen an die Stufen an — [baunetzwissen.de](https://www.baunetzwissen.de/controlling-und-management/fachwissen/kosten-und-vertraege/din-276--kosten-im-bauwesen-8441183)

### Inferences
| Output | Einstufung | Inhalt |
|---|---|---|
| Kennzahlen-Cockpit (eine Seite) | [M] | VOFI-Endwert und VOFI-Eigenkapitalrendite, IRR (Projekt/EK), Kapitalwert, Anfangsrendite brutto/netto, Faktor, Cash-on-Cash, Amortisation, DSCR/ICR/LTV min/Ø, Peak Equity, Break-even-Miete |
| Mehrjahres-Cashflow-Tabelle (10 Jahre Standard, bis 30+ Jahre für Wohnungswirtschaft/Förderbindung) mit Jahres- und unterjähriger Sicht | [M] | VOFI-Tableau: Einzahlungen, Auszahlungen, Finanzierung, Steuern, Reinvestition, Bestandsgrößen |
| Liquiditätsplanung Bauphase (monatlich) | [M] für Neubau/Sanierung/Developer | Mittelabfluss, Mittelzufluss (Darlehen, Zuschüsse, Kaufpreisraten), Liquiditätsreserve |
| Szenariovergleich (Base/Best/Worst und frei definierbare Varianten nebeneinander) | [M] | Sanierungstiefe, Fördervariante, Finanzierungsstruktur, Halten vs. Verkaufen |
| Sensitivitätsmatrix (zweidimensional, z. B. Miete × Baukosten, Zins × Exit-Faktor) und Tornado-Diagramm | [M]; Monte-Carlo [D] | Standardfrage jedes Gremiums |
| Investitionsvorlage/Investment Memo (PDF/Word, anpassbares Layout, Kommentarfelder, Annahmenverzeichnis) | [M] | Entscheidungsvorlage Aufsichtsrat/Investment Committee |
| Bankenunterlage: Objekt-/Projektsteckbrief, Kosten nach DIN 276, Finanzierungsplan (Mittelherkunft/-verwendung), Mieterliste, Kapitaldienstrechnung, Covenant-Verlauf, Stressfälle | [M] | Kreditantrag |
| Wirtschaftlichkeitsberechnung im II.-BV-Format und Befüllung länderspezifischer Förderformulare | II.-BV-Struktur [M] für geförderten Wohnungsbau; länderspezifische Formular-Exporte [D] | 16 Länder mit eigenen Vordrucken sind Pflegeaufwand |
| Soll-Ist-Vergleich/Nachkalkulation (Kosten je KG, Termine, Mieten, Finanzierung), Forecast-Fortschreibung | [M] für Projektsteuerung; [D] für reine Ankaufstools | Lernschleife und Projektcontrolling |
| Annahmen- und Änderungsprotokoll (Versionierung, Audit Trail, Vier-Augen-Freigabe) | [M] | Revisionssicherheit ggü. Excel ist ein Hauptkaufargument |
| Excel-Export mit nachvollziehbaren Werten (ideal: Formeln) | [M] | Banken und Prüfer rechnen nach |
| Mandantenfähige Berater-Reports (White-Label), mehrsprachig (DE/EN) | [D] | Beratungsgeschäft, internationale Investoren |
| ESG-Bericht (Energiekennwerte vor/nach, CO2-Pfad, Taxonomie-/CRREM-Status) | [D] | Zunehmend von Banken abgefragt |

### Gaps
- Konkrete Formularanforderungen der KfW (z. B. für Kommunal-/Unternehmensprogramme) und der einzelnen Landesförderbanken (IBB, L-Bank, BayernLabo, IFB Hamburg, IB.SH, WIBank, SAB, ILB, ISB u. a.) wurden nicht einzeln geprüft; NRW.BANK- und IBB-Formulare waren in den Treffern nicht direkt sichtbar. Nach Kenntnis des Researchers verlangt die KfW bei wohnwirtschaftlichen Programmen in der Regel keine eigene Wirtschaftlichkeitsberechnung nach festem Format, sondern technische Nachweise über Energieeffizienz-Experten; unbelegt.
- Kein veröffentlichter Standard für den Aufbau eines Investment Memos oder einer Aufsichtsratsvorlage in der Wohnungswirtschaft gefunden.
- Keine Quelle, die den üblichen Betrachtungszeitraum (10 Jahre institutionell vs. 20–30+ Jahre Wohnungswirtschaft) belegt.

---

## 11. Typische Fehler und Fallstricke, die gute Software verhindern sollte

### Takeaway
Die meisten Fehler entstehen an Schnittstellen zwischen Regelwerken (Förderung ↔ Umlage, Preisbindung ↔ Vergleichsmiete, nominal ↔ real, brutto ↔ netto) und durch veraltete oder verwechselte Pauschalen. Ein Tool verhindert sie durch datierte Stammdaten, Regelprüfungen mit Warnhinweisen und erzwungene Annahmen (z. B. Anschlusszins).

### Cited Findings
- (V) Kaufnebenkosten werden bei Renditeberechnungen häufig nicht vollständig im eingesetzten Kapital berücksichtigt — [baufi24.de](https://www.baufi24.de/rendite-berechnen-immobilie/)
- (V) Das Zinsänderungsrisiko nach Ablauf der Zinsbindung wird oft nicht von Anfang an eingeplant — [transparent-beraten.de](https://www.transparent-beraten.de/kapitalanlage/immobilien/finanzierung)
- (V) Veraltete Pauschalen: Ratgeberseiten zitieren 2026 noch die nicht indexierten II.-BV-Basiswerte (7,10/9,00/11,50 €/m²) als geltend, während ab 01.01.2026 11,50/14,58/18,62 €/m² gelten — [Dr. Klein](https://www.drklein.de/instandhaltungsruecklage.html) vs. [Haus & Grund Düsseldorf](https://hausundgrundddf.de/pauschalen-im-oeffentlich-gefoerderten-wohnungsbau/)
- (V) Regelwerksverwechslung: Die ab 2026 geltenden BewG-Bewirtschaftungskosten (Steuerbewertung) dürfen nicht mit ImmoWertV-Modellansätzen oder tatsächlichen Kosten verwechselt werden; die ImmoWertV-Ausgangswerte von 2021 (298 €/11,70 €) sind "eingefroren" und ohne Fortschreibung nicht aktuell — [reduco.ai, Ertragswertverfahren](https://reduco.ai/blog/immobilienverkauf/ertragswertverfahren-immobilie); [steuerschroeder.de](https://www.steuerschroeder.de/blog/bewertung-von-immobilien-bewirtschaftungskosten)
- (V) Fördermittel und Umlage: Bei der Heizungsumlage (§ 559e BGB) sind Fördermittel zwingend vor der Umlage abzuziehen; die 3-€-Kappung gilt für § 559, § 559e hat eine eigene 0,50-€-Kappung — [reduco.ai](https://reduco.ai/blog/modernisierungsumlage-energetische-sanierung)
- (V) Flächenfehler: Wird nach DIN 277 statt WoFlV gerechnet, gehen Balkone zu 100 % statt in der Regel 25 % ein; ohne Vereinbarung gilt im Zweifel die WoFlV — [Schwäbisch Hall](https://www.schwaebisch-hall.de/wohnen-und-leben/bauen-und-modernisieren/neubau-anbau/wohnflaechenberechnung.html)
- (V) Normversionsfehler: HOAI verweist auf DIN 276-1:2008-12, die Kostenplanung läuft auf DIN 276:2018-12 — [datadrivenaec.com](https://datadrivenaec.com/insights/din-276-kostengruppen-uebersicht)
- (V) Contracting-Annahme: Wärmelieferkosten sind nur bei Kostenneutralität umlegbar; diese wird beim Heizungstausch im Bestand laut BFW nur in ca. 17 % der Fälle erreicht — [BFW-Stellungnahme](https://www.bfw-bund.de/wp-content/uploads/2026/05/260508_BFW_Stellungnahme_Contracting_WaermeLV.pdf)
- (V) Covenant-Definitionen: Bewertungsbasis und Berechnungsmethodik müssen eindeutig definiert sein, sonst sind Kennzahlen nicht vergleichbar — [Immobilien & Finanzierung (kreditwesen.de)](https://www.kreditwesen.de/sites/default/files/content/articledownloads/2015/07/lak_14_22_814-815.pdf)
- (V) Regulatorische Stichtage: Quellen aus dem Frühjahr 2026, die das GEG 2024 mit 65-%-Regel als geltend beschreiben, sind seit 29.07.2026 überholt — [Bundesregierung, FAQ GModG](https://www.bundesregierung.de/breg-de/service/fragen-und-anworten/neues-gebaeudemodernisierungsgesetz-2430284)

### Inferences
Prüfregeln ("Guardrails"), die ein professionelles Tool implementieren sollte (Einstufung durchgehend [M], soweit nicht anders vermerkt):

1. **Nominal/real:** Ein Preisbasisjahr; jede Reihe (Miete, Kosten, Bau, Zins, Diskontsatz) ist eindeutig als nominal gekennzeichnet; Warnung bei Mietsteigerung > VPI-Annahme über lange Zeiträume oder bei realem Diskontsatz auf nominale Cashflows.
2. **Brutto/Netto:** Vorsteuerabzug je Nutzungsanteil; Wohnen brutto, optierendes Gewerbe netto; bei Mixed-Use Vorsteuerschlüssel; Warnung bei Nettokosten für Wohnanteile.
3. **Anschlussfinanzierung:** Kein Rechnen über das Zinsbindungsende hinaus ohne explizite Anschlussannahme; Restschuld zum Exit wird automatisch abgelöst (inkl. VFE-Hinweis).
4. **Mietpfad-Plausibilität Wohnen:** Bestandsmieten dürfen den Pfad aus § 558 (20 %/15 % in drei Jahren, Deckel Vergleichsmiete) nicht überschreiten; Neuvertragsmieten im Geltungsbereich der Mietpreisbremse nicht > Vergleichsmiete + 10 % (Ausnahmen prüfen); gebundene Wohnungen nicht über Bewilligungs-/Kostenmiete.
5. **Förderung ↔ Umlage:** Zuschüsse/Zinsvorteile mindern automatisch die Umlagebasis (§ 559a, § 559e); kein gleichzeitiger voller Ansatz von Förderung und Umlage; Kappungsgrenzen 3 €/2 €/0,50 € werden je Wohnung geprüft.
6. **Erhaltungsanteil:** Modernisierungskosten werden vor Umlage um ersparte Instandhaltung gekürzt; derselbe Betrag darf nicht zusätzlich im Instandhaltungsplan stehen (Doppelzählung in umgekehrter Richtung).
7. **Bauzeitzinsen:** aus dem Mittelabfluss gerechnet, nicht zusätzlich als Pauschale in KG 800 (Doppelzählung) und nicht vergessen.
8. **Flächenkonsistenz:** Mieterlöse auf Wohn-/Mietfläche, Kosten auf BGF; Plausibilitätsprüfung des Verhältnisses Wohnfläche/BGF.
9. **Leerstand in der Anlaufphase:** Erstvermietungskurve bei Neubau; Sanierungsleerstand und Mietausfall während der Bauzeit; Umzugsmanagementkosten.
10. **Nicht umlagefähige Kosten:** CO2-Vermieteranteil, Verwaltung, Instandhaltung, Leerstands-Betriebskosten werden nicht vergessen; ab 2028 50-%-Regel bei neuen fossilen Heizungen.
11. **Restwert:** Exit-Faktor nicht auf eine nicht nachhaltige Miete (Overrent, auslaufende Verträge) anwenden; CapEx-Stau abziehen; Warnung, wenn der Restwertanteil am Endwert einen Schwellenwert überschreitet.
12. **Bindungsauslauf:** Kein sofortiger Sprung auf Marktmiete nach Bindungsende (Kappungsgrenze gilt).
13. **Datierte Stammdaten:** II. BV, ImmoWertV Anlage 3, CO2-Preise, GrESt-Sätze, Mietpreisbremsen-Gebiete mit Gültigkeit-von/bis; Kalkulation speichert den verwendeten Rechtsstand.
14. **Indexmieten/Gewerbeindex:** Schwellenlogik statt linearer Fortschreibung; Indexmiete und Modernisierungsumlage schließen sich weitgehend aus (§ 557b BGB) [Hinweisfunktion, D].
15. **Steuer-/Rechtsform-Konsistenz** (Schnittstelle Steuer-Researcher): keine Ertragsteuern bei steuerbefreiten Vermietungsgenossenschaften; erweiterte Kürzung; AfA-Basis ohne Grund und Boden.
16. **Zirkularität:** Bauzeitzinsen ↔ Finanzierungsbedarf ↔ Gesamtkosten sauber iterativ lösen (in Excel häufige Fehlerquelle).

### Gaps
- Es wurde keine systematische Fachquelle (Lehrbuch, Verbandsleitfaden, Prüfungsfeststellungen) zu typischen Fehlern in Immobilien-Investitionsrechnungen gefunden; die Liste beruht überwiegend auf Folgerungen aus den Regelwerken und Praxiswissen des Researchers.
- Die Lehrbücher Schulte ("Immobilienökonomie"), Brauer und Gondring konnten nicht eingesehen werden; ihre Fehlerkataloge und Musterrechnungen fehlen.
- Die im Briefing genannte Vermischung nominal/real ist in den gefundenen Quellen nicht ausdrücklich behandelt.

---

## 12. Synthese: Anforderungsmatrix nach Projekttyp, Nutzungsart und Investorenperspektive

### Takeaway
Über alle vier Projekttypen hinweg ist ein gemeinsamer Kern Pflicht (DIN-276-Kosten, Flächenmodell, einheiten- bzw. vertragsscharfes Mietmodell, Tranchenfinanzierung, Restwert, Szenarien/Sensitivitäten, Berichte); die Differenzierung entsteht durch die Tiefe der Regelwerke (Mietrecht, II. BV, MaBV, Betreibermodelle), gepflegte Stammdaten mit Rechtsstand und die Anbindung an Unternehmensplanung und ESG.

### Cited Findings
- (V) Regelwerke mit datierten Kernparametern, die das Tool als Stammdaten führen muss (Stand 17.11.2026): II. BV-Pauschalen ab 01.01.2026 — [Haufe](https://www.haufe.de/immobilien/verwaltung/erhoehung-der-kostenmiete-bei-sozialwohnungen_258_392374.html); Mietpreisbremse bis 31.12.2029 — [LTO](https://www.lto.de/recht/nachrichten/n/bundestag-verlaengert-mietpreisbremse-bis-2029); GModG in Kraft seit 29.07.2026 — [Bundesregierung](https://www.bundesregierung.de/breg-de/service/fragen-und-anworten/neues-gebaeudemodernisierungsgesetz-2430284); CO2-Preiskorridor 55–65 €/t 2026 — [ista](https://www.ista.com/de/blog/heizen-abrechnen/die-heizkosten-steigen-was-der-co2-preis-2026-fuer-mieter-und-vermieter-bedeutet/); Baupreisindex +5,5 % (08/2026) — [Destatis](https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/10/PD26_360_61261.html); MF-GIF 2023 — [McDermott](https://www.mcdermottlaw.com/de/insights/real-estate-update-die-neue-mf-gif-2023/); DIN 276:2018-12 — [bauprofessor.de](https://www.bauprofessor.de/kostengruppe-finanzierung-in-din-276/)
- (V) Integrierte Unternehmensplanung (Plan-Bilanz, Plan-GuV, Plan-Kapitalflussrechnung) ist im genossenschaftlichen/kommunalen Umfeld Prüfungs- und Aufsichtsratsthema — [Schulungsunterlage Prüfung der Unternehmensplanung](https://fs.evenito.com/render/f1b7385d-5dd6-47d3-b107-6e2b21d0eda0)
- (V) Förderbanken arbeiten mit eigenen Wirtschaftlichkeitsberechnungs-Formularen — [NBank](https://www.nbank.de/medien/nb-media/Downloads/Formulare-zur-Antragstellung/Wirtschaftlichkeitsberechnung.pdf); [TAB](https://dokumente.aufbaubank.de/862739-TAB_Erfassungsbogen_Objektwirtschaftlichkeitsberechnung.pdf)

### Inferences
**A. Nach Projekttyp** (M = Muss, D = Differenzierung; Details in den Abschnitten 1–11)

| Baustein | (1) Ankauf Bestand | (2) Neubau zur Vermietung | (3) Sanierung/Quartier | (4) Developer/Bauträger |
|---|---|---|---|---|
| Kaufpreis + Erwerbsnebenkosten, Kaufpreisaufteilung Boden/Gebäude | M | M (Grundstück) | – (Bestand) / M bei Zukauf | M |
| DIN-276-Kosten, Kostenstände, Baupreisindex | D (nur CapEx) | M | M | M |
| Mittelabfluss, Bauzeitzinsen, Bereitstellungszinsen | – | M | M | M |
| Mietmodell Bestand (Ist-/Markt-/Vergleichsmiete, Fluktuation, § 558) | M | – | M | – |
| Erstvermietung/Anlaufkurve | – | M | M (nach Leerzug) | D (bei Globalverkauf mit Vermietungsgarantie) |
| Modernisierungsumlage §§ 559–559f, Drittmittelabzug, Warmmietenneutralität | D (bei geplanter Aufwertung) | – | M | – |
| Energetik vor/nach, CO2-Kosten, Heizungsvarianten | M (Risiko-CapEx) | D | M | D |
| Förderung (Zuschuss, Darlehen, Tilgungszuschuss) im Zahlungsstrom | D | M | M | D |
| Sanierungsleerstand, Umzugsmanagement, Bauabschnitte | – | D | M | M (Abschnitte) |
| Vertriebsplan, MaBV-Raten, Forward Deal/Funding | – | – | – | M |
| Residualwert | D | D | – | M |
| Exit/Restwert, Wertpfad, LTV | M | M | M | M (= Verkaufserlös) |
| Kennzahlen | IRR, VOFI-Rendite, Faktor, DSCR | + Rendite auf Kosten, Kostenmiete | + Delta-Betrachtung mit/ohne Maßnahme | Marge, Trading Profit, Projekt-/EK-IRR, Peak Equity |
| Soll-Ist/Nachkalkulation | D | M | M | M |
| Aggregation Gebäude → Quartier, Energiezentrale | D (Portfolioankauf: M) | D | M | D |

Für Typ (3) ist die **Differenzinvestitionsrechnung** ("mit Maßnahme" vs. "ohne Maßnahme/Instandhaltung-only", ggf. vs. "Abriss/Neubau") die fachlich prägende Besonderheit [M]; für die energetische Quartierssanierung kommen gebäudeübergreifende Maßnahmen (Wärmenetz, PV), Abschnittsbildung und Quersubventionierung hinzu.

**B. Nach Nutzungsart**

| Baustein | Frei finanziertes Wohnen | Geförderter/sozialer Wohnungsbau | Gewerbe/Mixed-Use | Sonderimmobilien |
|---|---|---|---|---|
| Fläche | WoFlV (M) | WoFlV (M, zwingend) | MF-GIF 2023 (M) | Plätze/Zimmer/Apartments + Fläche (M) |
| Erlöslogik | Vergleichsmiete, Kappung, Mietpreisbremse, Staffel/Index (M) | Bewilligungs-/Kostenmiete, Bindungsdauer, Belegung, Bindungsauslauf (M) | Rent Roll, Index mit Schwelle, Incentives, Anschlussvermietung, WALT (M) | Pacht (fix/Umsatz/hybrid), Auslastung, Betreiberrechnung (M/D) |
| Bewirtschaftung | frei, Benchmarks (M) | II.-BV-Pauschalen 2026 (M) | % der Miete, NK-Umlagegrad, Triple-Net (M) | Dach und Fach, FF&E (M) |
| CO2-Kosten | Stufenmodell + 50-%-Regel neue fossile Heizung ab 2028 (M) | wie Wohnen (M) | 50:50, voll umlegbare BK (M) | je Vertragslage (D) |
| USt | keine Option | keine Option | Option, Vorsteuerschlüssel (M) | nutzungsabhängig (M, Steuer-Schnittstelle) |
| Bank-/Bewertungssicht | ImmoWertV/BelWertV Wohnen (D) | Förderbank-WB-Formular (M/D) | BelWertV Gewerbe, Covenants (M) | erhöhte Mindestzinssätze, HypZert-Leitfäden (D) |
| Typische Kennzahlen | €/m² Wfl., Faktor, Leerstand, Fluktuation | Kostenmiete, Förderbarwert, Eigenkapitalverzinsung | NOI, WALT, Net Initial Yield, Over-/Underrent | Pachtdeckung, Pachtquote, RevPAR, Auslastung, €/Platz |

**C. Nach Investorenperspektive** (fachliche Seite; steuerliche Details beim Steuer-Researcher)

| Perspektive | Prägende fachliche Anforderungen |
|---|---|
| Kapitalgesellschaft / institutioneller Investor | IRR/Equity-Multiple-Sicht, 10-Jahres-DCF, Covenants, Exit-Yield, Rent Roll, ESG/CRREM/Taxonomie, Investment Memo (DE/EN) |
| Privatperson / Personengesellschaft | Nach-Steuer-Liquidität, Kapitaldienstfähigkeit, Zinsbindung und Anschlussrisiko, einfache Eingabe, Sondertilgung, Beraterreport |
| Steuerbefreite / kommunale / genossenschaftliche Unternehmen | Langfristhorizont (30+ Jahre), Kostenmiete/Bindungen, Warmmietenneutralität, Sozialverträglichkeit der Umlage, Instandhaltungsstrategie, Wirkung auf Wirtschaftsplan/Plan-GuV/Planbilanz, Aufsichtsratsvorlage, Förderbankformulare, Quartiersaggregation |

**D. Top-Differenzierungsmerkmale gegenüber Excel und einfachen Rechnern (Folgerung)**
1. Gepflegter, datierter Regel- und Stammdatendienst (Mietrecht je Gemeinde, II. BV, ImmoWertV Anlage 3, CO2-Pfad, Baupreisindex) mit dokumentiertem Rechtsstand je Kalkulation.
2. Automatische Kopplung Förderung ↔ Modernisierungsumlage ↔ Kappungsgrenzen ↔ Warmmietenneutralität.
3. Ein Datenmodell für alle vier Projekttypen, inklusive Wechsel "Verkaufen vs. Halten" und Differenzrechnung "mit/ohne Maßnahme".
4. Bankensicht in einem Klick (Beleihungswert-Schätzung, Covenant-Verlauf, Stressfälle).
5. Übergabe an bzw. Integration der Unternehmensplanung (Jahresscheiben, Plan-GuV/Bilanz).
6. Betreibermodelle für Sonderimmobilien mit Schattenrechnung.
7. Quartiersaggregation mit Energiezentrale, PV/Mieterstrom und CO2-Pfad.

### Gaps
- Die Matrix ist eine Synthese des Researchers; keine einzelne Quelle bestätigt die Einstufung Muss/Differenzierung. Eine Validierung über Anwenderinterviews (Wohnungsunternehmen, Banken, Projektentwickler) oder über den Funktionsvergleich etablierter Software (anderer Researcher) wäre nötig.
- Rechtsstand-Risiken zum 17.11.2026, die vor Produktentscheidungen am Originaltext zu prüfen sind: (a) Wortlaut GModG inkl. § 559e/§ 559f BGB und geändertes CO2KostAufG; (b) Status Mietrecht II (BT-Drs. 21/6807); (c) BEHG-Preis 2027 und Start ETS 2; (d) Inkrafttreten der EPBD-Teile (voraussichtlich Anfang 2027) und Nationaler Gebäuderenovierungsplan (fällig 31.12.2026); (e) Revision der EU-Taxonomie-Kriterien 7.1/7.2/7.7; (f) angekündigte Reform § 556c BGB/WärmeLV.
- Für einen Direktabruf der Primärquellen müssten folgende Hosts in den Netzwerkeinstellungen der Sitzung freigegeben werden: www.gesetze-im-internet.de, www.haufe.de, www.buzer.de, vdiv.de, www.gleisslutz.com, www.haus-und-grund-muenchen.de.
