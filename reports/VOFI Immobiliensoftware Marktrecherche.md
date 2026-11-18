# Eigenes VOFI-Werkzeug: fachlich tragfähig, Wirtschaftlichkeit offen

Interne Entwicklungsunterlage zum Vorhaben Web-Werkzeug für die Immobilien-Investitionsrechnung nach der VOFI-Methode (Vollständiger Finanzplan). Rechts- und Förderangaben haben den Stand 17.11.2026, KfW-Zinsen den Stand 18.11.2026.

## Kernaussagen

1. **Der Eigenbau begründet sich aus dem eigenen Bedarf, nicht aus einer Marktlücke.** Gebraucht wird ein Werkzeug für die eigene Kalkulation und die Beratung, das Ankauf, Neubau, Sanierung und Entwicklung mit gepflegter Förderlogik in einem Rechenweg abbildet. Kein Anbieter weist das aus; der Vergleich beruht allerdings auf Herstellerangaben und ersetzt keine Vorführung.
2. **Der stärkste Nutzen hängt an einer Rechenweise, die nicht veröffentlicht ist.** Die NBank prüft die Förderhöhe im Mietwohnungsbau seit 01.07.2026 über eine Investitionsrechnung nach dem VOFI-Modell und misst die Eigenkapitalrendite am 30-Jahres-Swapsatz plus 100 Basispunkte. Mit welchen Annahmen sie rechnet, legt sie nicht offen.
3. **Der Rechenkern ist machbar; über das Ergebnis entscheiden die Konventionen, nicht die Formel.** Im nachgerechneten Testfall verschieben einzelne Festlegungen die Rendite um bis zu einen Prozentpunkt. Die Daueraufgabe ist der Regel- und Förderkatalog: 2026 haben sich Wohnraumförderung, Heizungsrecht, Modernisierungsumlage und Gewerbesteuer gleichzeitig geändert.
4. **Stufe 1 wird größer als zunächst geplant.** Eine Vorhabensart zählt erst, wenn sie vollständig rechenbar ist, und das Werkzeug muss vom ersten Überschlag bis zur Gremien-, Bank- und Förderantragsunterlage tragen. Stufe 1 (Wohnen in Niedersachsen) wird deshalb in drei Teilschritte mit je eigenem Ergebnis und eigener Freigabe geschnitten.
5. **Die Technikwahl trägt.** Rechenkern und Server in Rust, Oberfläche in TypeScript; dieselbe Rechenlogik läuft im Browser und auf dem Server. Gleichzeitiges Bearbeiten mit Anzeige, wer wo arbeitet, wird umgesetzt.

**Was dieser Bericht nicht leistet:** Er enthält keine Wirtschaftlichkeitsrechnung für das Vorhaben, keine Bestätigung des Bedarfs durch Anwender und keine verbindliche Rechtsprüfung.

## Ihre Entscheidungen und nächsten Schritte

1. **Gespräch mit der NBank** über die Rechenweise der Renditeprüfung (Bewirtschaftungskosten, Mietsteigerung, Restwert, Betrachtungszeitraum, Stichtag des Swapsatzes) sowie über Tilgungsplan und Anerkennung eines KfW-Darlehens als Eigenkapitalersatz.
2. **Drei bis fünf Gespräche mit Anwendern oder Kunden**, ob sie das Werkzeug und seine Berichte in dieser Form brauchen und was ihnen fehlt.
3. **Vorführungen von avestrategy, IGIS six und WOWICONTROL** anfordern, bevor über den Eigenbau entschieden wird.
4. **Mengengerüst liefern** für die Vorstudie zur Wirtschaftlichkeit: Projekte pro Jahr, heutiger Zeitaufwand je Kalkulation, Zahl der Nutzer, Anteil geförderter Mietwohnungsbau.
5. **Verantwortung für den Regel- und Förderkatalog benennen**, mit Vertretung.
6. **Anwalt und Steuerberater beauftragen** mit den Punkten aus Abschnitt 7; Datenschutz und Mitbestimmung vor der Spezifikation des Änderungsprotokolls klären.
7. **Zur Kenntnis:** Von Ihrer Vorgabe „echte Co-Editierung wie Google Sheets“ wird in einem Punkt abgewichen. Getrennt offline bearbeitete Kopien werden nicht nachträglich zusammengeführt; alles andere bleibt (Abschnitt 8). Sollte das Arbeiten ohne Netzverbindung fachlich nötig sein, bitte melden.

## 1 Entscheidungsreife: Der Bericht klärt, was zu bauen wäre – nicht, ob es sich rechnet

### Kosten und Nutzen des Vorhabens sind nicht beziffert

Der Bericht beantwortet drei Fragen: was ein Werkzeug für die eigene Kalkulation und die Beratung können muss, wie der Rechenweg prüffähig wird und welche Rechts- und Förderregeln es mit welchem Stand führen muss. Er beantwortet nicht, ob der Eigenbau wirtschaftlich ist. Auf der Kostenseite fehlen der Aufwand für Entwicklung und Fachspezifikation, die dauerhafte Pflege des Regel- und Förderkatalogs und der Betrieb. Auf der Nutzenseite fehlen die Zahl der Kalkulationen pro Jahr, die Zeitersparnis gegenüber heute, der Beitrag zum Beratungsgeschäft und der Anteil des geförderten Mietwohnungsbaus in Niedersachsen, an dem der stärkste Nutzen hängt. Diese Rechnung entsteht als eigene Vorstudie, sobald Ihr Mengengerüst und eine Aufwandsschätzung aus dem Architekturentwurf vorliegen. Sie vergleicht den Eigenbau mit den Alternativen und enthält einen ungünstigen Fall.

Ein Befund gehört vor diese Rechnung, weil er gegen den Eigenbau sprechen kann. Der auf Dauer knappe Wert ist der **Regel- und Förderkatalog**: der datierte Bestand an Steuersätzen, Mietrechtsregeln und Förderkonditionen mit Quelle und Gültigkeit. Er ist von der Technik unabhängig und ließe sich auch für ein Excel-Modell oder ein zugekauftes System pflegen. Die aufwendigen Teile des Eigenbaus müssen sich deshalb aus ihrem eigenen Nutzen rechtfertigen: aus dem lückenlosen Änderungsprotokoll, der Arbeit mehrerer Personen an einem Projekt und den Berichten für Kunden.

### Vier Wege, qualitativ eingeordnet

| Weg | Spricht dafür | Spricht dagegen | Vor der Entscheidung zu klären |
|---|---|---|---|
| Eigenbau | Alle vier Vorhabensarten und die Förderlogik in einem Rechenweg; Protokoll, Rollen und Kundenberichte nach eigenem Zuschnitt | Höchster Anfangsaufwand; Abhängigkeit von wenigen Fachleuten; dauerhafte Pflege von Software und Katalog | Vorstudie Wirtschaftlichkeit; Anwendergespräche |
| Kauf einer Suite, ergänzt um den eigenen Katalog | Sofort verfügbar; VOFI-Funktion vorhanden; Softwarepflege beim Anbieter | Auf Bestandshalter zugeschnitten, an Beratung und ERP-System gekoppelt; Förderlogik, Simulation und Entwicklung mit Verkauf nicht ausgewiesen; Preise nicht öffentlich | Vorführungen: Was können die Produkte über die Werbung hinaus, zu welchem Preis, und dürfen sie in der Beratung für Dritte eingesetzt werden? |
| Ausbau von Excel (Modell nach FAST-Standard mit eigenem Katalog) | Vertraut; sichtbarer Rechenweg; von Banken akzeptiert; geringer Einstieg | Änderungsprotokoll, Rollen und gleichzeitiges Bearbeiten nur über Zusatzlösungen; jede Regeländerung muss in jede Datei getragen werden | Ob Protokoll, Rollen und Kundenzugang tatsächlich gebraucht werden |
| Nichtstun | Kein Aufwand | Die NBank prüft mit einer Rechnung, die im Haus vorab niemand nachbildet; die Regeländerungen von 2026 werden von Hand nachgezogen | Wie viele Vorhaben betroffen sind |

Die Tabelle ordnet ein, sie bewertet nicht in Euro. Dass die Wettbewerber die genannten Funktionen nicht ausweisen, heißt nicht, dass sie fehlen; deshalb stehen die Vorführungen vor der Entscheidung und nicht danach.

### Freigabe je Schritt, mit vorher benannten Abbruchkriterien

Freigegeben wird jeweils nur der nächste Schritt. Wo ein Kriterium eine Schwelle braucht (Aufwand, Nutzungsgrad), setzen Sie sie mit der Vorstudie; der Bericht nennt keine, weil er sie nicht belegen könnte.

| Entscheidungspunkt | Was dann vorliegt | Umsteuern oder Abbruch, wenn |
|---|---|---|
| Vor Beginn | Antwort der NBank; Anwendergespräche; Vorführungen der Wettbewerber; Vorstudie Wirtschaftlichkeit; benannte Katalogverantwortung | ein Produkt den Bedarf der Stufe 1 einschließlich Förderlogik deckt (dann Kauf mit eigenem Katalog); die Vorstudie unter vorsichtigen Annahmen keinen Vorteil gegenüber Kauf oder Excel-Ausbau zeigt; die Gespräche den Bedarf nicht bestätigen; niemand die Katalogpflege übernimmt |
| Vor Teilschritt 1b | Grobkalkulation im Einsatz; Referenzfälle laufen als automatische Tests | Vorprüfungen weiter in Excel entstehen; die Referenzfälle nicht auf den Cent stimmen; der Aufwand die in der Vorstudie gesetzte Schwelle überschreitet |
| Vor Teilschritt 1c | Erste Gremien- und Bankvorlagen aus dem Werkzeug; Rechenweise der NBank geklärt oder Bezeichnung der Kennzahl entschieden | Bank oder Gremium die Vorlagen nicht annehmen |
| Vor Stufe 2, 3 und 4 | Nutzungsbilanz der vorigen Stufe; Katalog fristgerecht gepflegt; Fallzahlen für Sanierung, Entwicklung und Sonderimmobilien aus dem Mengengerüst; vor dem ersten Kundeneinsatz die Rechtsprüfung nach Abschnitt 7 | der Katalog nicht aktuell gehalten wird; die Fallzahl den Ausbau nicht trägt |

Legt die NBank ihre Rechenweise nicht offen, entfällt das Vorhaben nicht. Die Kennzahl erscheint dann dauerhaft als eigene Rechnung, und die Vorstudie setzt den Nutzen aus dem Fördergeschäft entsprechend niedriger an.

Vier Risiken des Vorhabens liegen außerhalb der Technik. Die Nutzer bleiben bei Excel, wenn die erste Zahl dort schneller steht; dagegen stehen die Grobkalkulation im ersten Teilschritt, der sichtbare Rechenweg und der Excel-Export. Die Katalogpflege hängt an einer Person; sie braucht eine Vertretung und ein Vier-Augen-Verfahren. Ein fehlerhafter Katalogwert gelangt in einen Kundenbericht; dazu Abschnitt 7. Und die Verbindung von Rust, Finanzmathematik und Immobilienwissen ist selten; ein kleines Team hängt an einzelnen Personen.

## 2 Markt: Vier Anbieter werben mit VOFI, keiner weist gepflegte Förderlogik aus

### Deutschland: VOFI steckt in Planungssuiten für Bestandshalter

Der deutschsprachige Markt zerfällt in Segmente, die sich kaum überlappen: Planungs- und Portfoliosuiten der Wohnungswirtschaft, institutionelle Asset-Management-Plattformen, ERP-Systeme ohne eigene Investitionsrechnung, Bauträger-Werkzeuge, Rechner für Privatanleger und Formulare der Förderbanken. **Vier Angebote nennen den Vollständigen Finanzplan ausdrücklich.** avestrategy führt ein Spezialmodul „Immo-VoFi“ und bietet daneben die Discounted-Cashflow-Rechnung (DCF) ([avestrategy Spezialmodule](https://avestrategy.com/software/spezialmodule/); [avestrategy Portfoliomanagement](https://avestrategy.com/software/leistungspaket-portfoliomanagement/)). IGIS six wirbt mit „workflowbasierten dynamischen Investitionsrechnungen (VoFi und DCF)“ ([IGIS six Detailblatt 05/2025](https://igissix.de/wp-content/uploads/2025/07/05_2025_igis_six_detailblatt_investitionsrendite_web.pdf)). WOWICONTROL rechnet „auf Basis der VoFi-Methode“ im Kontext der Unternehmensplanung ([Dr. Klein Wowi](https://www.drklein-wowi.de/unternehmenssteuerung)). Das frei verfügbare RentalCal-Werkzeug des IWU ist eine VOFI-Webanwendung für Bestandsinvestitionen kleiner Vermieter ([ERES 2018](https://ideas.repec.org/p/arz/wpaper/eres2018_225.html)).

Die drei kommerziellen Lösungen werden von Beratungshäusern vertrieben, sind an ERP-Systeme gekoppelt und nennen keine Preise. Die ERP-Hersteller lösen das Thema über Partner; Haufe verweist für Controlling und Portfoliomanagement auf avestrategy ([Haufe Real Estate](https://realestate.haufe.de/schnittstellen/avestrategy)). Institutionelle Plattformen wie bison.box und immopac arbeiten mit Planungs- und DCF-Logik, nicht mit VOFI ([Planon](https://planonsoftware.com/us/news/planon-acquires-real-estate-software-company-control-it/); [immopac](https://www.immopac.ch/produkte/)). Entwickler-Werkzeuge wie Alasco steuern Baukosten und Liquidität, rechnen aber keine Investition über die Haltedauer ([Alasco](https://www.alasco.com/financial-management-software-real-estate-construction)).

| Produkt (Anbieter) | Zielgruppe | VOFI | Fördermittel | Simulation | Preis |
|---|---|---|---|---|---|
| avestrategy (BBT) | Wohnungsunternehmen, Genossenschaften | ja, Modul „Immo-VoFi“; zusätzlich DCF | – | – | nicht öffentlich |
| IGIS six (iwb) | Wohnungsunternehmen | ja, neben DCF | – | – | nicht öffentlich |
| WOWICONTROL (Dr. Klein Wowi) | Wohnungsunternehmen, Genossenschaften | ja | – | – | nicht öffentlich |
| mevivoECO (wowiconsult) | Wohnungsunternehmen, Banken | – | ja, in der Sanierungsrechnung | – | nicht öffentlich |
| bison.box (control.IT/Planon) | Asset- und Fondsmanager | – | – | – | nicht öffentlich |
| immopac | Institutionelle Investoren | – (DCF) | – | offen („Szenarien und Simulationen“) | nicht öffentlich |
| Alasco | Projektentwickler | – | – | – | nicht öffentlich |
| RentalCal (IWU) | Klein- und Privatvermieter | ja | – | – | kostenlos |
| ARGUS-Familie (Altus Group) | Investoren, Bewerter, Entwickler | – (DCF, Residualwert) | – | nur EstateMaster | nicht öffentlich |

„–“ bedeutet: vom Anbieter nicht ausgewiesen. Weitere Quellen: [mevivoECO](https://www.wowiconsult.eu/software/mevivoeco); [control.IT](https://www.controlit.eu/bison-box/). Nicht untersucht wurden unter anderem Reasult, PROBIS, Corporate Planner, PlaCoM und evoreal.

### International: Maßstab für Bedienung und Berichte, nicht für die Methode

Die ARGUS-Familie der Altus Group deckt mietvertragsgenauen DCF, Residualwert, Szenarien und Sensitivitäten ab ([ARGUS Developer](https://www.altusgroup.com/solutions/argus-developer); [Altus Release 03/2026](https://www.altusgroup.com/product-releases/argus-intelligence-release-mar26/)). Kein untersuchtes internationales Werkzeug weist die VOFI-Methode aus. Eine eingebaute Monte-Carlo-Simulation, also die Rechnung mit vielen Zufallsläufen statt eines einzelnen Falls, ist die Ausnahme: Ausgewiesen ist sie für ARGUS EstateMaster und für ein Excel-Modell von A.CRE ([ReadyMedia](https://content.readymedia.com.au/article/navigating-market-uncertainty-with-confidence-the-new-tool-empowering-property-developers); [A.CRE](https://www.adventuresincre.com/apartment-acquisition-model-with-monte-carlo-simulation-module/)). Gleichzeitiges Bearbeiten eines Rechenmodells weist kein immobilienspezifisches Werkzeug aus. Am weitesten geht Dealpath mit Modellversionen, Pflichtfreigaben und einem Protokoll, wer wann was geändert hat; Dealpath rechnet aber selbst nicht ([Dealpath](https://www.dealpath.com/deal-execution/)).

### Drei Lehren für das eigene Werkzeug

Die erste Lehre betrifft die Förderung. Nur mevivoECO berücksichtigt Fördermittel in der Wirtschaftlichkeitsrechnung von Sanierungsvarianten; die soziale Wohnraumförderung mit Bewilligungsmiete, Bindungsdauer und Zuschuss weist kein Anbieter aus. Die NBank liefert Formulare, kein Rechenwerk: den Förderantrag (Vordruck 1011, Stand Juli 2026) und eine Excel-Datei „Kosten-Finanzierungsaufteilung“. Ihre Investitionsrechnung „nach dem Modell des vollständigen Finanzplans“ veröffentlicht sie nicht ([NBank Vordruck 1011](https://www.nbank.de/medien/nb-media/Downloads/Formulare-zur-Antragstellung/F%C3%B6rderantrag-Mietwohnungen-Vordruck-1011.pdf); [RL Mietwohnraum 2026, Nr. 5.3.7 und 11.10](https://www.nbank.de/medien/nb-media/Downloads/Rechtliche-Grundlagen/Richtlinien/Richtlinie-F%C3%B6rderung-von-Mietwohnraum-%28RL-Mietwohnraum-2026%29.pdf)).

Die zweite Lehre betrifft Excel. In einer Studie der HfWU mit dem Softwarehaus Reasult nutzten 2020 **88 % der Projektentwickler Excel im Kerngeschäft**; eine zweite Quelle nennt für dieselbe Studie 96 % ([Cash-Online](https://www.cash-online.de/a/projektentwickler-excel-datei-statt-digitalisierung-551691/); [Agicap](https://agicap.com/de/artikel/projektentwicklung-immobilien/)). Der Grund für dieses Vertrauen ist der sichtbare Rechenweg ([MRI Software](https://mrisoftware.com/uk/?p=25532)). Die wiederkehrende Kritik an ARGUS zeigt die Kehrseite geschlossener Systeme: steile Lernkurve, hoher Preis und der Vorwurf der „Black Box“, weshalb viele Anwender nur bis zum Nettobetriebsergebnis in ARGUS modellieren und in Excel weiterrechnen ([G2](https://www.g2.com/products/argus-enterprise); [A.CRE](https://www.adventuresincre.com/ms-excel-alternative-to-argus-dcf/)). Das eigene Werkzeug muss deshalb jeden Rechenschritt zeigen und nach Excel ausgeben können.

Die dritte Lehre betrifft die Vermittlung. Selbst das IWU diskutierte 2023 für sein Werkzeug „Kapitalwert statt VoFI?“ ([IWU 10/2023](https://iwu.de/fileadmin/publikationen/vortrag/2023-10-12_Enseling_Wirtschaftlichkeitsberechnungen_AP5.pdf)). **Empfehlung:** VOFI-Kennzahlen und die international üblichen Größen (Kapitalwert, interner Zinsfuß, Eigenkapitalvervielfacher) stehen nebeneinander auf demselben Blatt.

## 3 Rechenkern: Die Konventionen entscheiden über das Ergebnis, nicht die Formel

### Die Methode: jede Zahlung auf einem Konto, jede Periode ausgeglichen

Der VOFI ist kein Formelverfahren, sondern eine periodenweise Tabellenrechnung ([Gabler Banklexikon](https://www.gabler-banklexikon.de/definition/vofi-62370)). Unter der Zahlungsfolge der Investition stehen getrennte Zeilen für Eigenkapital, jeden Kredit, Kontokorrent, Geldanlage und Steuern. Jede Periode wird auf einen Finanzierungssaldo von null ausgeglichen, und der **Endwert** ist der Bestand am Ende des Planungszeitraums ([FernUni Hagen](https://www.fernuni-hagen.de/controlling/docs/probekapitel_innovationscontrolling.pdf); [Kirchner, IWU 2004, S. 16–18](https://www.iwu.de/fileadmin/publikationen/wohnen/2004_IWU_Kirchner_Investitionsrechnungen-in-der-Wohnungswirtschaft-Wohnungswirtschaftliche-Theorie-I.pdf)). Die VOFI-Rendite ist die jährliche Verzinsung, mit der das Eigenkapital auf diesen Endwert wächst. Entscheidungsmaß ist die Endwertdifferenz zur **Unterlassensalternative**, der Anlage desselben Eigenkapitals am Kapitalmarkt nach Steuern ([Gabler Banklexikon](https://www.gabler-banklexikon.de/definition/vofi-eigenkapitalrentibilitaet-62371)). Die Lehrbücher sprechen von Eigenmitteln; dieser Bericht sagt durchgehend Eigenkapital.

Der Aufbau ist ohne Zirkelbezug umsetzbar, weil Zinsen und Steuern nur von den Beständen der Vorperiode abhängen. Der Kern rechnet intern monatlich, weil Bauphase, Mittelabfluss und Bauzeitzinsen unterjährig wirken, und verdichtet für die Darstellung auf Jahre. Er bildet mindestens 42 Jahre ab, die Laufzeit der NBank-Darlehen.

### Drei nachgerechnete Referenzfälle sichern den Kern ab

Drei Rechnungen stehen als automatische Abnahmetests bereit. Das Lehrbeispiel von Kirchner (1.000 Euro Eigenkapital, Sollzins 7,5 %, Habenzins 5,0 %, drei Perioden) endet mit **1.322,48 Euro Endwert und 9,76 % VOFI-Rendite**. Das wohnungswirtschaftliche Beispiel des IWU von 2013 (Mehrfamilienhaus mit zwölf Wohnungen, 25 Jahre, Annuitätendarlehen zu 4 %, KfW-Zuschuss 25.143 Euro) endet mit **153.032 Euro Endwert und 3,11 % VOFI-Rendite** und ist bis auf Rundungsdifferenzen von höchstens 3,40 Euro reproduzierbar ([IWU-Endbericht 2013, Anhang C, S. 51](https://www.iwu.de/fileadmin/user_upload/dateien/energie/sonstiges/Endbericht_Akteursbezogene_Wirtschaftlichkeit.pdf)). Beide rechnen ohne Steuern; sie prüfen die Rechenlogik, nicht das geltende Recht.

Die Steuerzeile deckt ein eigens konstruierter **Testfall** ab, auf den sich alle folgenden Zahlen beziehen: Ankauf für 1,1 Mio. Euro, 400.000 Euro Eigenkapital, Annuitätendarlehen zu 4 %, Steuersatz 30 %, fünf Jahre. Er endet mit **584.366,28 Euro Endwert, 155.571,23 Euro Endwertdifferenz und 7,876 % VOFI-Rendite**. Diese Werte und alle Varianten sind in zwei voneinander unabhängigen Gegenrechnungen auf den Cent bestätigt.

### Sieben Festlegungen bewegen das Ergebnis messbar

Das Lehrbuch lässt offen, was eine Software festlegen muss. Die Tabelle zeigt, was im Testfall geschieht, wenn eine Festlegung fehlt oder anders getroffen wird.

| Festlegung | Wirkung im Testfall |
|---|---|
| Die Unterlassensalternative erhält dieselben Einlagen und Entnahmen wie die Investition | Ohne diese Spiegelung fällt bei 5.000 Euro Entnahme je Jahr die Endwertdifferenz um 25.710 Euro zu niedrig aus, die Rendite mit 6,91 % statt 7,88 % |
| Eine Renditeformel für beliebige Einlagen und Entnahmen | Bei einem Nachschuss von 50.000 Euro im zweiten Jahr liefern vier naheliegende Lesarten 7,18 % bis 7,88 % bei gleicher Endwertdifferenz |
| Der Eingabewert der Miete ist die Miete des ersten Jahres | Als Vorjahreswert gelesen steigt die Rendite von 7,88 % auf 8,03 % |
| Der Kontokorrentzins geht in Steuer und Periodensaldo ein | Sonst weicht der Endwert um 1.840 Euro ab |
| Monatsraster mit ausgewiesenem Jahresmodus | Das Monatsraster allein ergibt 1.571 Euro mehr Endwert; Lehrbuchvergleiche brauchen den Jahresmodus |
| Der Schuldendienstdeckungsgrad nimmt die Ablösung der Restschuld aus | Sonst fällt er im Verkaufsjahr von 1,42 auf 0,09 und meldet einen Bruch der Kreditauflage |
| Die Probe „abgezinste Endwertdifferenz gleich Kapitalwert“ läuft nur als Testmodus | Sie gilt exakt nur bei einheitlichem Zins; mit getrennten Soll- und Habenzinsen weichen beide Größen um 45.078 Euro ab |

**Empfehlung zur Renditeformel:** Einlagen werden zum Alternativzins nach Steuern auf den Beginn abgezinst, Entnahmen auf das Ende aufgezinst und dem Endwert zugerechnet. Diese Form bleibt in der VOFI-Logik der ausdrücklichen Wiederanlage und ist für jede Einlagenreihe definiert; im Neubau fließt das Eigenkapital über viele Monate. Sie liegt genau dann über dem Alternativzins, wenn die Endwertdifferenz positiv ist. Im Testfall liefert sie 7,88 %, im Beispiel mit Nachschuss 7,25 %. Die Spezifikation führt die Formel bis zur Übernahme als offen.

Vier weitere Punkte prägen den Kern, weil sie im Fördergeschäft der Normalfall sind. Das NBank-Darlehen ist 35 Jahre zinslos; die übliche Annuitätenformel teilt bei einem Zinssatz von exakt null durch null, und der Tilgungsplan wird ohnehin von der NBank festgesetzt. Es braucht deshalb eine eigene Darlehensart. Ein Tilgungszuschuss senkt die Restschuld, ohne dass Geld fließt; Kontrollsummen, die das nicht kennen, schlagen bei richtig gerechneten Förderdarlehen an. Ist das Eigenkapital als Quote der Gesamtkosten einschließlich Bauzeitzinsen vorgegeben, muss der Kern die Quote in mehreren Durchläufen einstellen; ein einfacher Durchlauf verfehlt sie im Beispiel mit 70,69 % statt 70,00 % Fremdkapital. Und Darlehenspläne runden wie die Bank auf Cent je Rate, damit Restschulden mit dem Kontoauszug übereinstimmen. Anhang A führt alle Vorgaben mit Zahlen, Annahmen und Testfällen.

Zwei Lehrbuchkennzahlen bleiben vorerst draußen. Für die VOFI-Gesamtkapitalrendite ergeben drei Lesarten 4,61 %, 4,69 % und 4,76 %, für die Amortisationsdauer zwei Lesarten zwei gegenüber drei Jahren. Beide werden erst ausgewiesen, wenn die Definitionen nach Grob am Original beschafft sind.

### Die Regeln guter Tabellenmodelle werden zu Bauregeln der Software

Der FAST-Standard und der Financial Modelling Code des ICAEW laufen auf wenige Prinzipien hinaus: Eingaben, Rechnung und Ausgabe trennen, jede Berechnung nur einmal ausführen, nichts Veränderliches in Formeln einbetten ([FAST Standard](http://www.fast-standard.org/wp-content/uploads/2015/03/FASTStandard_02a.pdf); [ICAEW](https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx)). Für das Werkzeug heißt das: Annahmen sind ein eigener, versionierter Datensatz. Steuersätze, Fördersätze und Fristen stehen im Regel- und Förderkatalog und nie im Programm. Jede Ergebniszahl lässt sich bis zur Eingabe zurückverfolgen. Ergebnisse erscheinen erst, wenn alle Kontrollsummen bestanden sind. Und jede Kalkulation speichert, mit welchem Regelstand und welcher Version des Rechenkerns sie entstanden ist; ARGUS-Nutzer kritisieren ausdrücklich Aktualisierungen, die Ergebnisse unangekündigt verändern ([Capterra](https://www.capterra.com/p/276457/ARGUS-Enterprise/reviews/)).

### Kennzahlen: ein festes Blatt je Vorhabensart, gemessen auch an der Zielrendite

Die Unterlassensalternative ist eine nahezu risikolose Anlage. Ein Projekt, das sie knapp schlägt, hat eine positive Endwertdifferenz und verdient trotzdem keine Risikoprämie. **Empfehlung:** Die Zielrendite des Investors ist Pflichteingabe. Der Abstand zu ihr steht neben der Endwertdifferenz, und die kritischen Werte (etwa der höchste tragbare Kaufpreis) werden gegen beide Maßstäbe berechnet.

Das Kennzahlenblatt ist je Vorhabensart festgelegt und zeigt Basisfall und Stressfall nebeneinander. Es enthält vier Gruppen. Rendite: VOFI-Rendite, Endwertdifferenz, Abstand zur Zielrendite, Kapitalwert, interner Zinsfuß auf das Eigenkapital, Eigenkapitalvervielfacher. Kapitalbedarf: Eigenkapitaleinsatz, höchster Eigenkapitalbedarf mit Zeitpunkt, Nachschussbedarf. Finanzierung: kleinster Schuldendienstdeckungsgrad und höchster Beleihungsauslauf, jeweils mit Jahr. Objekt: Anfangsrendite brutto und netto, Kaufpreisfaktor, Break-even-Miete. Jede Kennzahl trägt eine dokumentierte Definition; für Anfangsrenditen gilt der Kennzahlenkatalog der gif, für den Eigenkapitalvervielfacher die Definition von INREV ([gif Kennzahlenkatalog](https://kennzahlenkatalog.gif-ev.com/); [INREV](https://www.inrev.org/definitions/EN/all)).

### Risikoanalyse: feste Stressfälle zuerst, Simulation in Stufe 2

Die Literatur empfiehlt ein gestuftes Vorgehen aus Sensitivität, Szenario und Simulation, weil die ersten beiden keine Eintrittswahrscheinlichkeiten kennen ([CUREM, Nöldeke 2008](https://www.curem.uzh.ch/static/abschlussarbeiten/2008/Noeldeke_Johannes_Masterthesis_2008.pdf)). Stufe 1 liefert Sensitivitäten, die Rangfolge der Einflussgrößen als Tornado-Diagramm, kritische Werte und einen festen Satz von Stressfällen für Anschlusszins, Baukosten, Bauzeit, Leerstand und Verkaufsfaktor. Die Höhe der Stressfälle ist eine Vorgabe des Hauses und wird mit der Freigabe des zweiten Teilschritts festgelegt. Am empfindlichsten reagieren die Ergebnisse auf den langfristigen Diskontsatz und die Verkaufsrendite ([Hoesli/Jani/Bender 2006](https://ideas.repec.org/a/eme/jpifpp/14635780610655076.html)).

Die Simulation wertet alle Risikofaktoren einschließlich ihrer Abhängigkeiten gleichzeitig aus und liefert eine Verteilung statt eines Punktwerts ([Gleißner](https://werner-gleissner.de/site/publikationen/WernerGleissner_Integrierte-Risiko-und-Portfoliomanagementsysteme-in-der-Immobilienwirtschaft.pdf)). Der VOFI eignet sich dafür, weil Liquiditätsengpass, Verlustvortrag oder Auflagenbruch in jedem Lauf durchgerechnet werden. Für die Eingabe genügen drei Werte (schlechtester, wahrscheinlichster, bester), aus denen eine PERT-Verteilung gebildet wird; die einfachere Dreiecksverteilung überschätzt die Streuung, in einer neueren Studie um 55 % ([French/Gabrielli](https://centaur.reading.ac.uk/27304/1/0703.pdf); [Heriot-Watt University](https://researchportal.hw.ac.uk/en/publications/beyond-normal-and-triangular-beta-distributions-for-monte-carlo-d/)).

Drei Vorgaben verhindern, dass die Simulation falsche Sicherheit erzeugt. Die Verkaufsrendite wird nur aus beschränkten Verteilungen gezogen; unbeschränkt schwankt der mittlere Verkaufsfaktor je nach Zufallsstart zwischen 18,0 und 29,4 bei einem Basiswert von 22,2. Mietsteigerung und Inflation brauchen eine Annahme über ihre Beharrung von Jahr zu Jahr; voneinander unabhängige Jahresziehungen weisen das Risiko des Mietniveaus nach zehn Jahren mit 5,7 % aus, bei mittlerer Beharrung sind es 11,6 %. Und Hauptgrößen des Berichts sind Endwertdifferenz, Median und Quantile neben dem Basisfall, nicht der Mittelwert der Rendite. Streuungen und Abhängigkeiten für deutsche Märkte setzt der Anwender; belastbare Marktquellen dafür liegen nicht vor.

## 4 Fachlicher Umfang: Pflichtbausteine vom ersten Überschlag bis zur Antragsunterlage
