# Eigenes VOFI-Werkzeug: fachlich tragfähig, Wirtschaftlichkeit offen

Interne Entwicklungsunterlage zum Vorhaben Web-Werkzeug für die Immobilien-Investitionsrechnung nach der VOFI-Methode (Vollständiger Finanzplan). Rechts- und Förderangaben haben den Stand 17. und 18.11.2026, KfW-Zinsen den Stand 18.11.2026.

## Kernaussagen

1. **Der Eigenbau begründet sich aus dem eigenen Bedarf, nicht aus einer Marktlücke.** Gebraucht wird ein Werkzeug für die eigene Kalkulation und die Beratung, das Ankauf, Neubau, Sanierung und Entwicklung mit gepflegter Förderlogik in einem Rechenweg abbildet. Kein Anbieter weist das aus; der Vergleich beruht allerdings auf Herstellerangaben und ersetzt keine Vorführung.
2. **Der stärkste Nutzen hängt an einer Rechenweise, die nicht veröffentlicht ist.** Die NBank prüft die Förderhöhe im Mietwohnungsbau seit 01.07.2026 über eine Investitionsrechnung nach dem VOFI-Modell und misst die Eigenkapitalrendite am 30-Jahres-Swapsatz plus 100 Basispunkte. Mit welchen Annahmen sie rechnet, legt sie nicht offen.
3. **Der Rechenkern ist machbar; über das Ergebnis entscheiden die Konventionen.** Im nachgerechneten Testfall verschieben einzelne Festlegungen die Rendite um bis zu einen Prozentpunkt. Die Daueraufgabe ist der Regel- und Förderkatalog: 2026 haben sich Wohnraumförderung, Heizungsrecht, Modernisierungsumlage und Gewerbesteuer gleichzeitig geändert.
4. **Für den Fall des Eigenbaus wird Stufe 1 größer als zunächst geplant.** Eine Vorhabensart zählt erst, wenn sie vollständig rechenbar ist, und das Werkzeug muss von der Grobkalkulation bis zu Gremienvorlage, Bankvorlage und Förderantrag tragen. Stufe 1 (Wohnen in Niedersachsen) wird deshalb in drei Teilschritte geschnitten, den zweiten in zwei Teilen; jeder endet mit einem nutzbaren Ergebnis und einer eigenen Freigabe.
5. **Für den Fall des Eigenbaus trägt die Technikwahl.** Rechenkern und Server entstünden in der Programmiersprache Rust, die Oberfläche in TypeScript; dieselbe Rechenlogik liefe im Browser und auf dem Server. Mehrere Personen können ein Projekt gleichzeitig bearbeiten.

**Was dieser Bericht nicht leistet:** Er enthält keine Wirtschaftlichkeitsrechnung für das Vorhaben, keine Bestätigung des Bedarfs durch Anwender und keine verbindliche Rechtsprüfung. Die ersten beiden Lücken schließen die Vorprüfung und die Vorstudie (Abschnitt 1), die dritte Anwalt und Steuerberater (Abschnitt 7).

## Ihre Entscheidungen und nächsten Schritte

**Freigaben**

1. **Jetzt, mit der Abnahme des Berichts:** der Zuschnitt der Stufe 1 (Abschnitt 5). Damit beginnt die Fachspezifikation, Phase 1 des Entwicklungsplans.
2. **Vorprüfung, vor Beginn der Phase 2 (Architektur und Vorstudie):** Fortsetzung oder Abbruch nach den Kriterien in Abschnitt 1. Sie ist der erste Freigabepunkt.
3. **Mit dem Auftrag der Vorstudie:** die Schwellen der Abbruchkriterien für Aufwand und Nutzungsgrad und die Höhe des ungünstigen Falls (Abschnitt 1).
4. **Bauentscheidung, nach Phase 2:** bauen, kaufen oder lassen, auf Grundlage der Vorstudie.
5. **Mit der Freigabe von Teilschritt 1b:** die Höhe der Stressfälle als Vorgabe des Hauses (Abschnitt 3).

**Aufträge bis zur Vorprüfung**

6. **Gespräch mit der NBank** über die Rechenweise der Renditeprüfung (Bewirtschaftungskosten, Mietsteigerung, Restwert, Betrachtungszeitraum, Stichtag des Swapsatzes), den Tilgungsplan, die Anerkennung eines KfW-Darlehens als Eigenkapitalersatz, die Aufteilung bei teilgeförderten Vorhaben und die Frage, ob Finanzierungskosten und nicht abziehbare Vorsteuer zuwendungsfähig sind.
7. **Drei bis fünf Gespräche mit Anwendern oder Kunden:** Brauchen sie das Werkzeug und seine Berichte in dieser Form, was fehlt ihnen, und wie oft arbeiten mehrere Personen an einem Projekt, mit Freigaben oder Kundenzugang?
8. **Vorführungen von avestrategy, IGIS six und WOWICONTROL** anfordern. Die fünf bisher nicht untersuchten Anbieter (Abschnitt 2) recherchiert das Projekt bis zur Vorprüfung.
9. **Mengengerüst liefern:** Projekte pro Jahr, heutiger Zeitaufwand je Kalkulation, Zahl der Nutzer, Anteil geförderter Mietwohnungsbau, Beratungsmandate pro Jahr mit Honorarvolumen.
10. **Verantwortung für den Regel- und Förderkatalog benennen**, mit Vertretung.
11. **Zwei Fachfragen beantworten:** Kommt Erbbaurecht bei Ihren geförderten Neubauten häufig genug vor, um es in Stufe 1 vorzuziehen? Und steht beim Neubau die Frage „gefördert oder frei finanziert“ am Anfang der Kalkulation? Die Folgen stehen in Abschnitt 5.

**Weitere Aufträge**

12. **Anwalt und Steuerberater beauftragen** (Abschnitt 7): Datenschutz, Mitbestimmung und Nutzungsrechte vor dem ersten Teilschritt, Beratungsgrenzen und Haftung vor dem ersten Kundeneinsatz.
13. **Zustimmung der KfW** zum automatisierten Abruf der Zinsdaten einholen, bevor er im Betrieb genutzt wird (Abschnitt 6).
14. **Lehrbücher von Grob und Schulte/Ropeter** beschaffen oder bereitstellen; zwei Kennzahlen warten auf die Originaldefinition (Abschnitt 3).
15. **Zur Kenntnis:** Von Ihrer Vorgabe „echte Co-Editierung wie Google Sheets“ wird in einem Punkt abgewichen. Getrennt offline bearbeitete Kopien werden nicht nachträglich zusammengeführt; alles andere bleibt (Abschnitt 8). Sollte das Arbeiten ohne Netzverbindung fachlich nötig sein, bitte melden.

## 1 Entscheidungsreife: Vorprüfung und Vorstudie stehen vor der Bauentscheidung

Mit der Abnahme dieses Berichts beginnt die Fachspezifikation (Phase 1): Rechenkern, Datenmodell des Regel- und Förderkatalogs und der Umfang der Stufe 1 als prüfbare Anforderungen. Architektur, Gestaltung und Aufwandsschätzung (Phase 2) beginnen erst nach bestandener Vorprüfung, der Bau erst nach der Bauentscheidung. Endet das Vorhaben an einem dieser Punkte, bleibt die Fachspezifikation verwertbar: Rechenkonventionen, Referenzfälle und das Datenmodell des Katalogs dienen dann als Pflichtenheft für eine gekaufte Lösung oder als Bauplan für ein Excel-Modell.

Ein Befund kann gegen den Eigenbau sprechen. Der auf Dauer knappe Wert ist der **Regel- und Förderkatalog**: der datierte Bestand an Steuersätzen, Mietrechtsregeln und Förderkonditionen mit Quelle und Gültigkeit. Er ist von der Technik unabhängig und ließe sich auch für ein Excel-Modell oder ein zugekauftes System pflegen. Die aufwendigen Teile des Eigenbaus müssen sich deshalb aus ihrem eigenen Nutzen rechtfertigen: aus dem lückenlosen Änderungsprotokoll, der Arbeit mehrerer Personen an einem Projekt und den Berichten für Kunden. Ob dieser Nutzen besteht, fragen die Anwendergespräche ausdrücklich ab.

### Vier Wege, qualitativ eingeordnet

| Weg | Spricht dafür | Spricht dagegen | Vor der Entscheidung zu klären |
|---|---|---|---|
| Eigenbau | Alle vier Vorhabensarten und die Förderlogik in einem Rechenweg; Protokoll, Rollen und Kundenberichte nach eigenem Zuschnitt | Höchster Anfangsaufwand; Abhängigkeit von wenigen Fachleuten; dauerhafte Pflege von Software und Katalog | Vorstudie; Anwendergespräche |
| Kauf einer Suite, ergänzt um den eigenen Katalog | Sofort verfügbar; VOFI-Funktion vorhanden; Softwarepflege beim Anbieter | Auf Bestandshalter zugeschnitten, an Beratung und an das kaufmännische Bestandssystem (ERP) gekoppelt; Förderlogik, Simulation und Entwicklung mit Verkauf nicht ausgewiesen; Preise nicht öffentlich; Katalogpflege bleibt im Haus | Vorführungen: Was können die Produkte, zu welchem Preis, und dürfen sie in der Beratung für Dritte eingesetzt werden? |
| Ausbau von Excel (Modell nach den anerkannten Regeln des FAST-Standards, angebunden an den eigenen Katalog) | Vertraut; sichtbarer Rechenweg; von Banken akzeptiert; geringer Einstieg | Änderungsprotokoll, Rollen und gleichzeitiges Bearbeiten nur über Zusatzlösungen; Regeländerungen erreichen nur Dateien, die an den Katalog angebunden bleiben; Katalogpflege bleibt im Haus | Ob Protokoll, Rollen und Kundenzugang tatsächlich gebraucht werden |
| Nichtstun | Kein Aufwand | Die Regeländerungen von 2026 werden je Kalkulation von Hand nachgezogen; Rechenweg und Annahmen bleiben je Bearbeiter verschieden | Wie viele Vorhaben betroffen sind |

Die Vorabrechnung der NBank-Kennzahl spricht für keinen der vier Wege, solange die NBank ihre Rechenweise nicht offenlegt. Sie begründet das Gespräch mit der NBank.

### Freigabepunkte mit vorher benannten Abbruchkriterien

Freigegeben wird jeweils nur der nächste Schritt. Die Tabelle nennt die Punkte, an denen über Fortsetzung oder Abbruch entschieden wird; die fachliche Freigabe der Fachspezifikation und die Vorführung des technischen Fundaments führt der Entwicklungsplan.

| Freigabepunkt | Was dann vorliegt | Umsteuern oder Abbruch, wenn |
|---|---|---|
| Vorprüfung, vor Beginn der Phase 2 | Antwort der NBank; Anwendergespräche; Vorführungen der drei VOFI-Anbieter; Recherche zu den fünf weiteren Anbietern; benannte Katalogverantwortung; Mengengerüst einschließlich Beratungsgeschäft | ein Produkt den Bedarf der Stufe 1 einschließlich Förderlogik deckt (dann Kauf mit eigenem Katalog); die Gespräche den Bedarf nicht bestätigen; niemand die Katalogpflege übernimmt |
| Bauentscheidung, nach Phase 2 | Architekturentwurf mit Aufwandsschätzung; Vorstudie; Datenschutz und Mitbestimmung geklärt | die Vorstudie im ungünstigen Fall keinen Vorteil gegenüber Kauf oder Excel-Ausbau zeigt |
| Vor Teilschritt 1b, je Teil | Grobkalkulation im Einsatz; Referenzfälle laufen als automatische Tests | Grobkalkulationen weiter in Excel entstehen; ein Referenzfall außerhalb seiner festgelegten Toleranz liegt (Anhang A.6); der Aufwand die gesetzte Schwelle überschreitet |
| Vor Teilschritt 1c | Erste Gremien- und Bankvorlagen aus dem Werkzeug; Rechenweise der NBank geklärt, sonst bleibt es bei der Bezeichnung der Kennzahl nach Abschnitt 6 | Bank oder Gremium die Vorlagen nicht annehmen |
| Vor Stufe 2, 3 und 4 | Abnahme der vorigen Stufe durch Parallelrechnung echter Projekte gegen die bisherige Excel-Kalkulation; Katalog fristgerecht gepflegt; Fallzahlen für Sanierung, Entwicklung und Sonderimmobilien aus dem Mengengerüst | die Parallelrechnung Abweichungen zeigt, die keine benannte Konvention erklärt; der Katalog nicht aktuell gehalten wird; die Fallzahl den Ausbau nicht trägt |

Legt die NBank ihre Rechenweise nicht offen, entfällt das Vorhaben nicht. Die Kennzahl erscheint dann dauerhaft als eigene Rechnung, und die Vorstudie setzt den Nutzen aus dem Fördergeschäft entsprechend niedriger an.

Drei Risiken des Vorhabens liegen außerhalb der Technik. Die Nutzer bleiben bei Excel, wenn die erste Zahl dort schneller steht; dagegen stehen die Grobkalkulation im ersten Teilschritt, der sichtbare Rechenweg und der Excel-Export. Die Katalogpflege hängt an einer Person; sie braucht eine Vertretung und ein Vier-Augen-Verfahren. Und ein fehlerhafter Katalogwert kann in einen Kundenbericht gelangen; dazu Abschnitt 7.

### Auftrag der Vorstudie

Die Vorstudie entsteht in Phase 2, sobald Ihr Mengengerüst und die Aufwandsschätzung aus dem Architekturentwurf vorliegen. Damit der Vergleich fair ausfällt, gelten diese Vorgaben:

- **Varianten:** Eigenbau, Kauf mit eigenem Katalog und Excel-Ausbau mit eigenem Katalog; Nichtstun ist der Bezugsfall.
- **Zeitraum und Entscheidungsmaß:** zehn Jahre; gemessen wird die Endwertdifferenz jeder Variante gegenüber dem Bezugsfall, daneben die Amortisationsdauer.
- **Kosten je Variante:** Entwicklung und Fachspezifikation oder Lizenz und Einführung, dazu Betrieb und Softwarepflege. Die Katalogpflege wird in allen drei Varianten mit demselben Betrag angesetzt, weil sie überall anfällt.
- **Nutzen aus dem Mengengerüst:** Kalkulationen pro Jahr, Zeitersparnis gegenüber heute, Beitrag zum Beratungsgeschäft, Anteil des geförderten Mietwohnungsbaus in Niedersachsen.
- **Ungünstiger Fall:** Aufwand 50 % höher, Nutzen 50 % niedriger. Das ist ein Vorschlag; die Höhe geben Sie mit dem Auftrag frei.
- **Bereits angefallene Kosten:** Was bis zur Bauentscheidung für die Phasen 0 bis 2 ausgegeben ist, geht in keine Variante ein.

## 2 Markt: Vier Anbieter werben mit VOFI, keiner weist gepflegte Förderlogik aus

### Deutschland: VOFI steckt in Planungssuiten für Bestandshalter

Der deutschsprachige Markt zerfällt in Segmente, die sich kaum überlappen: Planungssuiten der Wohnungswirtschaft, Plattformen institutioneller Investoren, Bauträger-Werkzeuge, Rechner für Privatanleger und Formulare der Förderbanken. **Vier Angebote nennen den Vollständigen Finanzplan ausdrücklich.** avestrategy führt ein Spezialmodul „Immo-VoFi“ und bietet daneben die Discounted-Cashflow-Rechnung (DCF) ([avestrategy Spezialmodule](https://avestrategy.com/software/spezialmodule/); [avestrategy Portfoliomanagement](https://avestrategy.com/software/leistungspaket-portfoliomanagement/)). IGIS six wirbt mit „workflowbasierten dynamischen Investitionsrechnungen (VoFi und DCF)“ ([IGIS six Detailblatt 05/2025](https://igissix.de/wp-content/uploads/2025/07/05_2025_igis_six_detailblatt_investitionsrendite_web.pdf)). WOWICONTROL rechnet „auf Basis der VoFi-Methode“ im Kontext der Unternehmensplanung ([Dr. Klein Wowi](https://www.drklein-wowi.de/unternehmenssteuerung)). Das frei verfügbare RentalCal-Werkzeug des IWU ist eine VOFI-Webanwendung für Bestandsinvestitionen kleiner Vermieter ([ERES 2018](https://ideas.repec.org/p/arz/wpaper/eres2018_225.html)).

Die drei kommerziellen Lösungen werden von Beratungshäusern vertrieben, sind an die kaufmännischen Bestandssysteme gekoppelt und nennen keine Preise; Haufe etwa verweist für Controlling und Portfoliomanagement auf avestrategy ([Haufe Real Estate](https://realestate.haufe.de/schnittstellen/avestrategy)). Institutionelle Plattformen wie bison.box und immopac arbeiten mit DCF-Logik, Entwickler-Werkzeuge wie Alasco steuern Baukosten und Liquidität ([Planon](https://planonsoftware.com/us/news/planon-acquires-real-estate-software-company-control-it/); [immopac](https://www.immopac.ch/produkte/); [Alasco](https://www.alasco.com/financial-management-software-real-estate-construction)).

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

„–“ bedeutet: vom Anbieter nicht ausgewiesen. Weitere Quellen: [mevivoECO](https://www.wowiconsult.eu/software/mevivoeco); [control.IT](https://www.controlit.eu/bison-box/). Nicht untersucht sind Reasult, PROBIS, Corporate Planner, PlaCoM und evoreal; das Projekt holt diese Recherche bis zur Vorprüfung nach.

### International: Vorbild für Bedienung und Berichte; die VOFI-Methode führt dort kein Werkzeug

Die ARGUS-Familie der Altus Group deckt mietvertragsgenauen DCF, Residualwert, Szenarien und Sensitivitäten ab ([ARGUS Developer](https://www.altusgroup.com/solutions/argus-developer)). Eine eingebaute Monte-Carlo-Simulation, also die Rechnung mit vielen Zufallsläufen statt eines einzelnen Falls, ist die Ausnahme ([ReadyMedia](https://content.readymedia.com.au/article/navigating-market-uncertainty-with-confidence-the-new-tool-empowering-property-developers); [A.CRE](https://www.adventuresincre.com/apartment-acquisition-model-with-monte-carlo-simulation-module/)). Gleichzeitiges Bearbeiten eines Rechenmodells weist kein immobilienspezifisches Werkzeug aus; am weitesten geht Dealpath mit Modellversionen, Pflichtfreigaben und einem Protokoll, wer wann was geändert hat ([Dealpath](https://www.dealpath.com/deal-execution/)).

### Folgen für das eigene Werkzeug: Förderlogik, sichtbarer Rechenweg, zwei Kennzahlenwelten

Förderlogik bietet der Markt kaum. Nur mevivoECO berücksichtigt Fördermittel in der Wirtschaftlichkeitsrechnung von Sanierungsvarianten; die soziale Wohnraumförderung mit Bewilligungsmiete, Bindungsdauer und Zuschuss weist kein Anbieter aus. Die NBank liefert Formulare, kein Rechenwerk: den Förderantrag (Vordruck 1011, Stand Juli 2026) und eine Excel-Datei „Kosten-Finanzierungsaufteilung“. Ihre Investitionsrechnung „nach dem Modell des vollständigen Finanzplans“ veröffentlicht sie nicht ([NBank Vordruck 1011](https://www.nbank.de/medien/nb-media/Downloads/Formulare-zur-Antragstellung/F%C3%B6rderantrag-Mietwohnungen-Vordruck-1011.pdf); [RL Mietwohnraum 2026, Nr. 5.3.7 und 11.10](https://www.nbank.de/medien/nb-media/Downloads/Rechtliche-Grundlagen/Richtlinien/Richtlinie-F%C3%B6rderung-von-Mietwohnraum-%28RL-Mietwohnraum-2026%29.pdf)).

Excel bleibt der Maßstab für Nachvollziehbarkeit. In einer Studie der HfWU mit dem Softwarehaus Reasult nutzten 2020 **88 % der Projektentwickler Excel im Kerngeschäft**; eine zweite Quelle nennt für dieselbe Studie 96 % ([Cash-Online](https://www.cash-online.de/a/projektentwickler-excel-datei-statt-digitalisierung-551691/); [Agicap](https://agicap.com/de/artikel/projektentwicklung-immobilien/)). Der Grund für dieses Vertrauen ist der sichtbare Rechenweg ([MRI Software](https://mrisoftware.com/uk/?p=25532)). ARGUS trifft umgekehrt der Vorwurf der „Black Box“, weshalb viele Anwender dort nur einen Teil modellieren und in Excel weiterrechnen ([G2](https://www.g2.com/products/argus-enterprise); [A.CRE](https://www.adventuresincre.com/ms-excel-alternative-to-argus-dcf/)). Das eigene Werkzeug muss deshalb jeden Rechenschritt zeigen und nach Excel ausgeben können.

Die VOFI-Methode allein überzeugt nicht jeden Leser. Selbst das IWU diskutierte 2023 für sein Werkzeug „Kapitalwert statt VoFI?“ ([IWU 10/2023](https://iwu.de/fileadmin/publikationen/vortrag/2023-10-12_Enseling_Wirtschaftlichkeitsberechnungen_AP5.pdf)). **Empfehlung:** VOFI-Kennzahlen und die international üblichen Größen (Kapitalwert, interner Zinsfuß, Eigenkapitalvervielfacher) stehen nebeneinander auf demselben Blatt.

## 3 Rechenkern: Die Konventionen entscheiden über das Ergebnis, nicht die Formel

### Die Methode: jede Zahlung auf einem Konto, jede Periode ausgeglichen

Der VOFI rechnet periodenweise in einer Tabelle ([Gabler Banklexikon](https://www.gabler-banklexikon.de/definition/vofi-62370)). Unter der Zahlungsfolge der Investition stehen getrennte Zeilen für Eigenkapital, jeden Kredit, Kontokorrent, Geldanlage und Steuern. Jede Periode wird auf einen Finanzierungssaldo von null ausgeglichen, und der **Endwert** ist der Bestand am Ende des Planungszeitraums ([FernUni Hagen](https://www.fernuni-hagen.de/controlling/docs/probekapitel_innovationscontrolling.pdf); [Kirchner, IWU 2004, S. 16–18](https://www.iwu.de/fileadmin/publikationen/wohnen/2004_IWU_Kirchner_Investitionsrechnungen-in-der-Wohnungswirtschaft-Wohnungswirtschaftliche-Theorie-I.pdf)). Die VOFI-Rendite ist die jährliche Verzinsung, mit der das Eigenkapital auf diesen Endwert wächst. Entscheidungsmaß ist die Endwertdifferenz zur **Unterlassensalternative**, der Anlage desselben Eigenkapitals am Kapitalmarkt nach Steuern ([Gabler Banklexikon](https://www.gabler-banklexikon.de/definition/vofi-eigenkapitalrentibilitaet-62371)). Die Lehrbücher sprechen von Eigenmitteln; dieser Bericht sagt durchgehend Eigenkapital.

Der Aufbau ist ohne Zirkelbezug umsetzbar, weil Zinsen und Steuern nur von den Beständen der Vorperiode abhängen. Der Kern rechnet intern monatlich, weil Bauphase, Mittelabfluss und Bauzeitzinsen unterjährig wirken, und verdichtet für die Darstellung auf Jahre. Er bildet mindestens 42 Jahre ab, die Laufzeit der NBank-Darlehen.

### Drei nachgerechnete Referenzfälle sichern den Kern ab

Drei Rechnungen stehen als automatische Abnahmetests bereit, jede mit festgelegter Toleranz (Anhang A.6). Das Lehrbeispiel von Kirchner mit drei Perioden prüft das Tabellenschema. Das wohnungswirtschaftliche Beispiel des IWU von 2013, ein Mehrfamilienhaus über 25 Jahre mit Annuitätendarlehen und KfW-Zuschuss, prüft die lange Laufzeit; es lässt sich bis auf Rundungsdifferenzen von höchstens 3,40 Euro nachrechnen, weil die Quelle volle Euro ausweist ([IWU-Endbericht 2013, Anhang C, S. 51](https://www.iwu.de/fileadmin/user_upload/dateien/energie/sonstiges/Endbericht_Akteursbezogene_Wirtschaftlichkeit.pdf)). Beide rechnen ohne Steuern und prüfen damit nur die Rechenlogik.

Die Steuerzeile deckt ein eigens konstruierter **Testfall** ab, auf den sich die folgende Tabelle bezieht: Ankauf für 1,1 Mio. Euro, 400.000 Euro Eigenkapital, Annuitätendarlehen zu 4 %, Steuersatz 30 %, fünf Jahre, VOFI-Rendite 7,88 %. Seine Werte und alle Varianten sind in zwei voneinander unabhängigen Gegenrechnungen auf den Cent bestätigt.

### Sieben Festlegungen bewegen das Ergebnis messbar

Das Lehrbuch lässt offen, was eine Software festlegen muss. Die Tabelle zeigt, was im Testfall und seinen Varianten geschieht, wenn eine Festlegung fehlt oder anders getroffen wird; die exakten Referenzwerte stehen in Anhang A.6.

| Festlegung | Wirkung |
|---|---|
| Die Unterlassensalternative erhält dieselben Einlagen und Entnahmen wie die Investition | Ohne diese Spiegelung fällt bei 5.000 Euro Entnahme je Jahr die Endwertdifferenz um 25.710 Euro und die Rendite um knapp einen Prozentpunkt zu niedrig aus |
| Eine Renditeformel für beliebige Einlagen und Entnahmen | Bei einem Nachschuss von 50.000 Euro im zweiten Jahr liegen vier naheliegende Lesarten um 0,7 Prozentpunkte auseinander, bei gleicher Endwertdifferenz |
| Einlagen und Entnahmen derselben Periode werden saldiert | Fallen ein Nachschuss und eine Entnahme von je 50.000 Euro in dasselbe Jahr, weicht die unsaldierte Rechnung um 0,63 Prozentpunkte ab, obwohl sich am Zahlungsstrom nichts ändert |
| Der Eingabewert der Miete ist die Miete des ersten Jahres | Als Vorjahreswert gelesen steigt die Rendite um 0,15 Prozentpunkte |
| Der Kontokorrentzins geht in Steuer und Periodensaldo ein | In der Variante mit Kontokorrent weicht der Endwert sonst um 1.840 Euro ab |
| Monatsraster mit ausgewiesenem Jahresmodus | Das Monatsraster allein ergibt 1.571 Euro mehr Endwert; Lehrbuchvergleiche brauchen den Jahresmodus |
| Der Schuldendienstdeckungsgrad nimmt die Ablösung der Restschuld aus | Sonst fällt er im Verkaufsjahr von 1,42 auf 0,09 und meldet einen Bruch der Kreditauflage |

**Empfehlung zur Renditeformel:** Einlagen werden zum Alternativzins nach Steuern auf den Beginn abgezinst, Entnahmen auf das Ende aufgezinst und dem Endwert zugerechnet. Diese Form bleibt in der VOFI-Logik der ausdrücklichen Wiederanlage und ist für jede Einlagenreihe definiert; im Neubau fließt das Eigenkapital über viele Monate. Sie liegt genau dann über dem effektiven Jahreszins der Alternative, wenn die Endwertdifferenz positiv ist. Die Spezifikation führt die Formel bis zur Übernahme als offen; Formel, Saldierung und Randfälle stehen in Anhang A, Nr. 12 bis 15.

Vier weitere Vorgaben prägen den Kern, weil sie im Fördergeschäft der Normalfall sind (Anhang A, Nr. 10, 16, 22, 23 und 26). Das NBank-Darlehen ist 35 Jahre zinslos, trägt danach Zins und folgt einem von der NBank festgesetzten Tilgungsplan; es braucht eine eigene Darlehensart, weil die übliche Annuitätenformel bei einem Zinssatz von exakt null versagt. Tilgungszuschüsse senken die Restschuld, ohne dass Geld fließt, und die NBank behält ihr Bearbeitungsentgelt bei der Auszahlung ein; Kontrollsummen, die das nicht kennen, schlagen bei richtig gerechneten Förderdarlehen an. Ist das Eigenkapital als Quote der Gesamtkosten einschließlich Bauzeitzinsen vorgegeben, stellt der Kern die Quote in mehreren Durchläufen ein. Und jede Zahlungsart hat eine Rundungsregel; Darlehen runden je Rate kaufmännisch auf Cent, damit Restschulden mit dem Kontoauszug übereinstimmen.

Zwei Lehrbuchkennzahlen bleiben vorerst draußen: die VOFI-Gesamtkapitalrendite und die Amortisationsdauer. Für beide liefern mehrere Lesarten verschiedene Werte (Anhang A, Nr. 18 und 19). Ausgewiesen werden sie erst, wenn die Definitionen nach Grob am Original beschafft sind.

### Die Regeln guter Tabellenmodelle werden zu Bauregeln der Software

Der FAST-Standard und der Financial Modelling Code des ICAEW verlangen, Eingaben, Rechnung und Ausgabe zu trennen und nichts Veränderliches in Formeln einzubetten ([FAST Standard](http://www.fast-standard.org/wp-content/uploads/2015/03/FASTStandard_02a.pdf); [ICAEW](https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx)). Für das Werkzeug heißt das: Steuersätze, Fördersätze und Fristen stehen im Regel- und Förderkatalog und nie im Programm. Jede Ergebniszahl lässt sich bis zur Eingabe zurückverfolgen. Ergebnisse erscheinen erst, wenn alle Kontrollsummen bestanden sind. Und jede Kalkulation speichert, mit welchem Regelstand und welcher Version des Rechenkerns sie entstanden ist; ARGUS-Nutzer kritisieren Aktualisierungen, die Ergebnisse unangekündigt verändern ([Capterra](https://www.capterra.com/p/276457/ARGUS-Enterprise/reviews/)).

### Kennzahlen: ein festes Blatt je Vorhabensart, gemessen auch an der Zielrendite

Die Unterlassensalternative ist eine nahezu risikolose Anlage. Ein Projekt, das sie knapp schlägt, hat eine positive Endwertdifferenz und verdient trotzdem keine Risikoprämie. **Empfehlung:** Die Zielrendite des Investors ist Pflichteingabe. Sie bezieht sich auf das Eigenkapital nach Steuern, ist ein effektiver Jahreszins und wird mit der VOFI-Rendite verglichen. Der Abstand zu ihr steht neben der Endwertdifferenz, und die kritischen Werte (etwa der höchste tragbare Kaufpreis) werden gegen beide Maßstäbe berechnet.

Das Kennzahlenblatt ist je Vorhabensart festgelegt. Es zeigt drei Fälle nebeneinander: den Basisfall, den kombinierten Stressfall, in dem alle Stressgrößen zugleich eintreten, und den ungünstigsten einzelnen Stressfall mit Namen. Die Kennzahlen stehen in vier Gruppen:

- **Rendite:** VOFI-Rendite, Endwertdifferenz, Abstand zur Zielrendite, Kapitalwert, interner Zinsfuß auf das Eigenkapital, Eigenkapitalvervielfacher, Anteil des Restwerts am Endwert.
- **Kapitalbedarf:** Gesamtinvestition, Eigenkapitaleinsatz, höchster Eigenkapitalbedarf mit Zeitpunkt, Nachschussbedarf und Finanzierungslücke, also der Teil der Gesamtinvestition, den Eigenkapital, Darlehen und Förderung nicht decken.
- **Finanzierung:** kleinster Schuldendienstdeckungsgrad und höchster Beleihungsauslauf, jeweils mit Jahr.
- **Objekt:** Anfangsrendite brutto und netto, Einstiegsfaktor und Ausstiegsfaktor nebeneinander, Break-even-Miete.

Der Restwertanteil und das Faktorenpaar stehen auf dem Blatt, weil ein Ausstieg zu einem höheren Faktor als beim Einstieg die Rendite am leichtesten schönt. Jede Kennzahl trägt eine dokumentierte Definition, die Anfangsrenditen und Faktoren nach dem Kennzahlenkatalog der gif, der Eigenkapitalvervielfacher nach INREV ([gif Kennzahlenkatalog](https://kennzahlenkatalog.gif-ev.com/); [INREV](https://www.inrev.org/definitions/EN/all)). Die Grobkalkulation im ersten Teilschritt zeigt ein reduziertes Blatt ohne die Gruppe Finanzierung und ohne Stressfälle; beides folgt mit Teilschritt 1b.

### Risikoanalyse: feste Stressfälle zuerst, Simulation in Stufe 2

Die Literatur empfiehlt ein gestuftes Vorgehen aus Sensitivität, Szenario und Simulation ([CUREM, Nöldeke 2008](https://www.curem.uzh.ch/static/abschlussarbeiten/2008/Noeldeke_Johannes_Masterthesis_2008.pdf)). Stufe 1 liefert Sensitivitäten, die Rangfolge der Einflussgrößen als Tornado-Diagramm, kritische Werte und einen festen Satz von Stressfällen für Anschlusszins, Baukosten, Bauzeit, Leerstand, Verkaufsfaktor, Mietsteigerung und Instandhaltungskosten, einzeln und kombiniert. Die Stresshöhen sind Katalogwerte, die Sie als Vorgabe des Hauses mit der Freigabe von Teilschritt 1b festlegen; im Projekt lassen sie sich verschärfen, aber nicht abschwächen. Am empfindlichsten reagieren die Ergebnisse auf den langfristigen Diskontsatz und die Verkaufsrendite ([Hoesli/Jani/Bender 2006](https://ideas.repec.org/a/eme/jpifpp/14635780610655076.html)).

Die Simulation in Stufe 2 wertet alle Risikofaktoren mit ihren Abhängigkeiten gleichzeitig aus und liefert eine Verteilung statt eines Punktwerts ([Gleißner](https://werner-gleissner.de/site/publikationen/WernerGleissner_Integrierte-Risiko-und-Portfoliomanagementsysteme-in-der-Immobilienwirtschaft.pdf)). Für die Eingabe genügen drei Werte (schlechtester, wahrscheinlichster, bester), aus denen eine Verteilung gebildet wird, die den wahrscheinlichsten Wert stärker gewichtet (PERT-Verteilung); die einfachere Dreiecksverteilung überschätzt die Streuung, in einer neueren Studie um 55 % ([French/Gabrielli](https://centaur.reading.ac.uk/27304/1/0703.pdf); [Heriot-Watt University](https://researchportal.hw.ac.uk/en/publications/beyond-normal-and-triangular-beta-distributions-for-monte-carlo-d/)). Drei Vorgaben verhindern falsche Sicherheit (Anhang A.7): Die Verkaufsrendite wird nur aus beschränkten Verteilungen gezogen. Mietsteigerung und Inflation brauchen eine Annahme über ihre Beharrung von Jahr zu Jahr. Und Hauptgrößen sind Endwertdifferenz, Median und Quantile neben dem Basisfall. Die Zahl der Rechenläufe folgt aus einem Genauigkeitsziel für das 5-%-Quantil, die Schwelle, die nur in einem von zwanzig Läufen unterschritten wird. Je nach Streuung braucht es dafür rund 27.000 bis 172.000 Läufe; solche Läufe rechnet der Server. Streuungen und Abhängigkeiten für deutsche Märkte setzt der Anwender; belastbare Marktquellen dafür liegen nicht vor.

## 4 Fachlicher Umfang: Pflichtbausteine von der Grobkalkulation bis zum Förderantrag

### Der Arbeitsablauf bestimmt den Umfang: Grobkalkulation, Vollkalkulation, Vorlagen

Ein Vorhaben wird erst grob kalkuliert, dann vollständig, und geht am Ende als Vorlage an Gremium, Bank und Förderstelle. Trägt das Werkzeug eine dieser Strecken nicht, entsteht die Kalkulation in Excel und wird erst später übertragen; Protokoll und Arbeitsstände fehlen dann für die wichtigste Strecke.

In der **Grobkalkulation** liegen wenige Angaben vor: beim Ankauf Kaufpreis, Wohnfläche, Mieten und Baujahr, beim Neubau Grundstückspreis, Brutto-Grundfläche und ein Kostenkennwert. Arbeitsziel ist eine erste VOFI-Rendite und der höchste tragbare Kaufpreis bei Zielrendite mit rund 15 Eingaben; alles Übrige kommt als gekennzeichnete Voreinstellung aus dem Regel- und Förderkatalog. Beim Ankauf gehören drei Pauschalen dazu, weil sie den tragbaren Kaufpreis unmittelbar bewegen: der Investitionsstau, die Anpassung der Ist-Miete an die Marktmiete und die CO2-Kosten. Beim Neubau gehört die Förderung der NBank als Näherung dazu. In der **Vollkalkulation** ersetzt der Anwender Voreinstellungen schrittweise durch eigene Werte, bis zur dritten Gliederungsebene der DIN 276 und zur Mieterliste je Einheit, ohne dass frühere Werte verloren gehen. Am Ende stehen die **Vorlagen**: Gremienvorlage, Bankvorlage und Förderantrag, jeweils bezogen auf einen benannten, freigegebenen Arbeitsstand.

Die vier Vorhabensarten teilen sich ein Datenmodell, aber nicht den Pflichtumfang. Anhang D nennt zu jedem Baustein, was Pflicht ist und ab welchem Teilschritt oder welcher Stufe er vorhanden sein muss. **Pflicht** heißt: Ohne den Baustein ist eine Vorhabensart der Stufe nicht vollständig rechenbar oder nicht vorlagefähig. **Differenzierung** heißt: Ausbau über die Pflicht hinaus, der das Werkzeug von Excel und den Produkten am Markt abhebt. Mit Stufenangabe ist er eingeplant, ohne Stufenangabe nur vorgemerkt.

### Warum Baupreisindex, Brutto-Kennzeichen, Restwertbezug und Übergabe an die Unternehmensplanung Pflicht sind

Die Baupreise für Wohngebäude lagen im August 2026 um **5,5 % über dem Vorjahr**, die Instandhaltungspreise um 6,0 %; eine vom Verbraucherpreisindex getrennte Fortschreibung ist deshalb zwingend ([Destatis, Pressemitteilung Nr. 360 vom 09.10.2026](https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/10/PD26_360_61261.html)). Wer zehn Millionen Euro Baukosten im Wohnungsbau versehentlich netto erfasst, unterschätzt den Kapitalbedarf um 1,9 Millionen Euro, weil die Vorsteuer dort nicht abziehbar ist.

Beim Restwert entscheidet die Bezugsbasis. Ein Verkaufsfaktor bezieht sich auf die Jahresnettokaltmiete. Eine Nettoanfangsrendite bezieht sich auf den Reinertrag, also die Miete nach nicht umlagefähigen Kosten, im Verhältnis zum Kaufpreis einschließlich der Erwerbsnebenkosten. Wer den Faktor auf den Reinertrag anwendet, unterschätzt den Restwert bei 20 % nicht umlagefähigen Kosten um ein Fünftel; wer die Nettoanfangsrendite auf die Miete anwendet, überschätzt ihn um mindestens ein Viertel. Beide Eingaben weisen deshalb ihre Bezugsbasis aus (Anhang D.4).

Im genossenschaftlichen und kommunalen Umfeld ist die integrierte Planung aus Plan-Bilanz, Plan-GuV und Plan-Kapitalflussrechnung Gegenstand der Verbandsprüfung ([VNW-Schulungsunterlage 09/2026](https://fs.evenito.com/render/f1b7385d-5dd6-47d3-b107-6e2b21d0eda0)). Pflicht für das Werkzeug ist die Übergabe der Projektwirkungen in Jahresscheiben; die eigene Planbilanz ist Differenzierung in Stufe 4.

### Jede Vorhabensart hat eigene Pflichten und eigene Entscheidungsgrößen

| Vorhabensart | Was nur hier gilt | Entscheidungsgrößen | Stufe |
|---|---|---|---|
| Ankauf Bestand | Mieterliste mit Ist-Mieten und fortwirkenden Drittmitteln; Kaufpreisaufteilung; übernommene Darlehen; Maßnahmenplan mit Investitionsstau, Mietminderung, Leerzug und Umzugskosten; Modernisierungsumlage mit den zwingenden Abzügen; CO2-Kosten ab dem ersten Jahr. Mittelabfluss und Bauzeitzinsen entfallen | VOFI-Rendite, Anfangsrendite und Faktor, höchster tragbarer Kaufpreis, Schuldendienstdeckung | 1 |
| Neubau zur Vermietung | Kostenstände; Mittelabfluss; Bauzeitzinsen; Erstvermietung; Abschreibungswahl; Förderung im Zahlungsstrom | zusätzlich Rendite auf die Kosten, höchster Eigenkapitalbedarf, höchster tragbarer Grundstückspreis | 1 |
| Sanierung im Bestand | Differenzrechnung gegen den Fall ohne Maßnahme, der die unvermeidbare Instandhaltung, die CO2-Kosten der alten Heizung und den Heizungstausch bei Ausfall enthält; Bauabschnitte; Umlage mit Drittmitteln aus dem Fördermodul | Vorteil gegenüber dem Fall ohne Maßnahme; Mietwirkung je Wohnung | 2 |
| Entwicklung mit Verkauf | Vertriebsplan; Bauträgerraten mit Fälligkeit nach Art des Käufers und Sicherheitseinbehalt (Anhang B.4); Residualwert vorwärts und rückwärts; Verkauf an einen Investor vor Fertigstellung (Forward Deal); Finanzierungskaskade mit Vorverkaufsquote als Auszahlungsbedingung; Prüfung auf gewerblichen Grundstückshandel; monatliche Tabelle als Hauptsicht | Marge auf Kosten und auf Erlös, höchster Eigen- und Fremdkapitalbedarf, Break-even-Verkaufspreis, interner Zinsfuß von Projekt und Eigenkapital | 3 |

Banken bilden in ihren Cashflow-Modellen „nahezu sämtliche Mietvertragsbestimmungen“ ab; das macht die vertragsgenaue Gewerbemodellierung in Stufe 3 zur Pflicht ([Immobilien & Finanzierung](https://www.kreditwesen.de/sites/default/files/content/articledownloads/2015/09/lak_12_10_334-336.pdf)).

### Investorensicht und Steuerstatus sind getrennte Merkmale

Die Rechtsform bestimmt nicht die Steuerpflicht. Eine kommunale Wohnungs-GmbH ist in der Regel voll körperschaft- und gewerbesteuerpflichtig. Befreit sind nur Genossenschaften und Vereine, und auch sie nur, solange ihre nicht begünstigten Einnahmen 10 % der Gesamteinnahmen nicht übersteigen ([§ 5 Abs. 1 Nr. 10 KStG](https://www.gesetze-im-internet.de/kstg_1977/__5.html)). Das Werkzeug führt deshalb zwei Merkmale. Die **Investorensicht** (Kapitalgesellschaft; Privatperson und vermögensverwaltende Personengesellschaft; steuerbefreite, kommunale und genossenschaftliche Unternehmen) steuert Berichtsform und Kennzahlen. Der **Steuerstatus** steuert die Steuerrechnung:

| Steuerstatus | Was die Steuerrechnung braucht |
|---|---|
| Voll steuerpflichtige Körperschaft, ohne oder mit erweiterter Grundstückskürzung | Körperschaftsteuer-Staffel bis 2032; Gewerbesteuer mit Hinzurechnung; bei erweiterter Kürzung die Prüfung der Unschädlichkeitsgrenzen; getrennte Verlustvorträge für Körperschaft- und Gewerbesteuer |
| Privatperson oder vermögensverwaltende Personengesellschaft | Persönlicher Grenzsteuersatz als Eingabe; Zehnjahresfrist beim Verkauf |
| Befreite Vermietungsgenossenschaft oder befreiter Verein | Steuersatz null; die 10-%-Grenze wirkt wie eine Klippe und läuft als Prüfung in jeder Periode mit |
| Gemeinnützig (Wohngemeinnützigkeit) | Voraussetzungen als Prüfung bei Mietbeginn; die Steuerfolgen gibt der Steuerberater vor |

Für jeden steuerpflichtigen Status gelten die Abschreibungswahl und die rückwirkende 15-%-Prüfung anschaffungsnaher Herstellungskosten. Welche Abschreibung zulässig ist, hängt an Vorhabensart, Nutzung je Gebäudeteil und Vermögenszugehörigkeit. Die degressive Abschreibung und die Sonderabschreibung gibt es nur bei Herstellung oder bei Anschaffung bis zum Ende des Fertigstellungsjahres, beim Ankauf älterer Bestände also nicht (Abschnitt 6).

Zwei Einschränkungen gelten für jeden Steuerstatus. Bei der Entwicklung mit Verkauf kann gewerblicher Grundstückshandel vorliegen; dann gelten andere Regeln (Gewerbesteuer, keine Zehnjahresfrist, keine erweiterte Kürzung). Das Werkzeug warnt, die Abgrenzung trifft der Steuerberater. Und in Kundenberichten sind Steuerparameter Annahmen, die der Kunde oder sein Steuerberater vorgibt (Abschnitt 7).

## 5 Stufenplan: Stufe 1 in drei Teilschritten, jeder mit nutzbarem Ergebnis

Der Plan folgt drei Regeln. Eine Vorhabensart steht erst in einer Stufe, wenn sie dort vollständig rechenbar ist. Grundlagen, die später nur teuer nachzurüsten sind, entstehen zuerst: Änderungsprotokoll, Regel- und Förderkatalog und das Mandantenkennzeichen, das die Daten nach Kunden trennt. Und regulatorisch schwierige Felder folgen erst, wenn der Kern durch Referenzfälle abgesichert ist. Der Plan legt Inhalt und Reihenfolge fest; Aufwand und Termine beziffert der Architekturentwurf in Phase 2.

### Der Zielkonflikt: Vollständigkeit macht Stufe 1 größer

Ein gewöhnlicher Ankauf mit Gasheizung und geplanter Strangsanierung ist nur rechenbar, wenn Kaufpreisaufteilung, Bewirtschaftung, Maßnahmenplan, Modernisierungsumlage und CO2-Kosten vorhanden sind. Ein geförderter Neubau ist nur vorlagefähig, wenn Arbeitsstände, Gremien- und Bankvorlage, Liquiditätsplan und Förderantrag dazukommen. Stufe 1 enthält deshalb deutlich mehr als ein Rechenwerk für Wohnen mit Förderung. Der Preis ist ein späteres erstes Gesamtergebnis und mehr gebundener Aufwand, bevor der Nutzen belegt ist.

Gelöst wird das durch den Zuschnitt in Teilschritte. Jeder endet mit einem Ergebnis, das im Alltag trägt, und wird einzeln freigegeben. Teilschritt 1b ist dafür in zwei Teile geschnitten, 1b-1 für den Ankauf und 1b-2 für den Neubau, die je für sich vorlagefähig sind. Zurückgestellt ist nur, was keine Vorhabensart der Stufe 1 unvollständig lässt: Simulation, die Kopplung der Modernisierungsumlage an das Fördermodul, vertragsgenaues Gewerbe und die Unternehmenshierarchie. Die Bausteine im Einzelnen stehen in Anhang D.

| Teilschritt | Fachlicher Inhalt | Zusammenarbeit und Nachweis | Was der Anwender danach kann |
|---|---|---|---|
| 1a Grobkalkulation | Ankauf Bestand und Neubau zur Vermietung mit Kennwerten und Voreinstellungen aus dem Katalog; beim Ankauf Pauschalen für Investitionsstau, Anpassung der Ist- an die Marktmiete und CO2-Kosten; Grobförderung der NBank als Voreinstellung; Zielrendite, kritische Werte, reduziertes Kennzahlenblatt ohne Kreditkennzahlen; Excel-Import verdichteter Werte | Änderungsprotokoll; Anmeldung; Projektzuweisung mit einfacher Rollenunterscheidung; sofortige Verteilung jeder Änderung; benannter, eingefrorener Arbeitsstand | Ein Exposé oder ein Grundstück in Minuten grob kalkulieren, frei finanziert oder gefördert, den höchsten tragbaren Preis nennen und den Stand festhalten, auf dem ein Gebot beruht |
| 1b-1 Vollkalkulation Ankauf Bestand | Mieterliste und Mietpfad nach Mietvertragsart; Bewirtschaftung; Maßnahmenplan mit Mietminderung, Leerzug und Umzugskosten; CO2-Kosten; Modernisierungsumlage mit den zwingenden Abzügen und der Heizungskappung; Darlehen in voller Tiefe mit Kreditkennzahlen; Steuer in Grundform; Varianten, Sensitivitäten, Stressfälle; Gremien- und Bankvorlage | Volles Rollenmodell; Arbeitsstände mit Status und Freigabe durch die Rolle Prüfer; Präsenzanzeige; Excel-Export mit Summen- und Saldoformeln | Einen frei finanzierten Ankauf vollständig rechnen und mit freigegebenem Stand vor Gremium und Bank bringen |
| 1b-2 Vollkalkulation Neubau | Kosten bis zur dritten Ebene der DIN 276 mit Kostenständen bis zum Kostenvoranschlag; Mittelabfluss und Bauzeitzinsen; Erstvermietung; Abschreibungswahl und Sonderabschreibung; monatlicher Liquiditätsplan der Bauphase | wie 1b-1 | Einen frei finanzierten Neubau vollständig rechnen und vorlegen |
| 1c Förderung Niedersachsen | Fördermodul mit NBank-Hauptprogramm, NBank-Zuschuss für energetisch hochwertigen Neubau, KfW 297/298 und 296; Bindungen mit Mietpfad in und nach der Bindung; Ankauf von Beständen mit laufenden Bindungen und übernommenen Förderdarlehen, Verlängerung auslaufender Bindungen als Variante; Beihilfekennzeichen; Förderantrag; Kostenanschlag und Kostenfeststellung; Jahresscheiben für die Unternehmensplanung | Förderantrag nur aus einem freigegebenen Arbeitsstand | Ein gefördertes Vorhaben rechnen, den Förderantrag ausgeben und die Eigenkapitalrendite vorab mit eigenen Annahmen an der Schwelle der NBank messen |

**Steuer in Grundform.** Dazu gehören je Steuerstatus die laufende Ertragsteuer mit Abschreibungsplan, Verlustvortrag und 15-%-Prüfung, für die Körperschaft die Gewerbesteuer mit Hinzurechnung und erweiterter Grundstückskürzung, für die Privatperson die Zehnjahresfrist und für die befreite Genossenschaft die 10-%-Prüfung. Ohne die erweiterte Kürzung wäre die Zahl in der Gremienvorlage einer Kapitalgesellschaft um die Gewerbesteuer falsch. Zinsschranke, Umsatzsteueroption und gewerblicher Grundstückshandel gehören nicht zur Grundform und folgen in Stufe 3.

**Erbbaurecht.** Hier ist die Vollständigkeit bewusst eingeschränkt. In Stufe 1 ist der Erbbauzins eine frei benennbare Position mit Index. Nicht abgebildet sind der Restwert bei endlicher Laufzeit, die Entschädigung bei Heimfall oder Zeitablauf, der fehlende Bodenanteil bei Kaufpreisaufteilung und Abschreibung und die Behandlung bei den zuwendungsfähigen Kosten der NBank. Ein Vorhaben auf Erbbaugrund ist in Stufe 1 deshalb nur näherungsweise rechenbar; das volle Modell folgt in Stufe 3. Vergeben Gemeinden Grundstücke für Ihre geförderten Neubauten häufig im Erbbaurecht, wird das Modell in Teilschritt 1c vorgezogen. Das ist die erste Fachfrage im Kopfteil.

**Grobförderung in 1a.** Sie steht im ersten Teilschritt, weil Eingangsmiete, zinsloses Darlehen und Zuschuss Kapitalbedarf und Rendite eines Neubaus in Niedersachsen grundlegend ändern. Steht die Frage „gefördert oder frei finanziert“ bei Ihnen nicht am Anfang der Kalkulation, rückt die Grobförderung nach 1c und Teilschritt 1a wird kleiner. Das ist die zweite Fachfrage. Vorlagefähig wird ein gefördertes Vorhaben in jedem Fall erst mit 1c.

**Zusammenarbeit in 1a.** Der erste Teilschritt enthält nur, was eine belegbare Grobkalkulation braucht. Das Änderungsprotokoll gehört dazu, weil es die Form ist, in der das System jede Eingabe speichert; ein späterer Umbau wäre teurer als der sofortige Einbau. Präsenzanzeige und volles Rollenmodell folgen in 1b, nach der ersten Prüfung, ob das Werkzeug genutzt wird. Die Prüfrunde hatte vorgeschlagen, auch die sofortige Verteilung von Änderungen an alle geöffneten Bildschirme zu verschieben. Das wird nicht umgesetzt: Die Verteilung ist derselbe Mechanismus wie das Speichern über das Änderungsprotokoll und kostet kaum Mehraufwand.

Das technische Fundament legt Phase 3 des Entwicklungsplans: Rechenkern mit festgeschriebenen Konventionen, Kontrollsummen und Referenztests, Katalog mit dem Regelstand je Kalkulation und Änderungsprotokoll. Die Teilschritte der Stufe 1 bilden Phase 4. Sie endet mit einer Parallelrechnung echter Projekte gegen die bisherige Excel-Kalkulation.

### Stufen 2 bis 4

| Stufe | Fachlicher Umfang | Technik und Betrieb | Begründung |
|---|---|---|---|
| 2 Sanierung und Simulation | Sanierung im Bestand als Differenzrechnung nach Abschnitt 4; Modernisierungsumlage mit Drittmitteln aus dem Fördermodul, vereinfachtem Verfahren und Sperrfristen; Vergleich von Heizungsvarianten; KfW 261, BAFA-Einzelmaßnahmen, KfW 458, NBank-Modernisierung; Prüfung der Kumulierungsgrenzen | Simulation mit Bandbreiteneingabe; lange Rechenläufe auf dem Server | Die Sanierung trägt die meisten Rechtsänderungen von 2026; die Simulation setzt einen stabilen, getesteten Kern voraus |
| 3 Entwicklung und Gewerbe | Entwicklung mit Verkauf nach Abschnitt 4; Gewerbe und gemischte Nutzung vertragsgenau mit Umsatzsteueroption und Vorsteuerberichtigung; Zinsschranke mit ihren Ausnahmen; volles Erbbaurechtsmodell; Förderprogramme für Nichtwohngebäude und Umnutzung; Vergleich Verkaufen oder Halten | Monatliche Hauptsicht; Kreditauflagen mit Schwellen und Ampel; weitergehender Excel-Export | Eigene Regelwerke; baut auf den Kosten- und Finanzierungsbausteinen der Stufen 1 und 2 auf |
| 4 Sonderimmobilien und Unternehmensebene | Pacht- und Betreibermodell; Hierarchie vom Unternehmen bis zur Einheit mit Plan-GuV und Planbilanz; Förderung weiterer Länder | Lesende Kundenzugänge; Schnittstellen zu ERP-Systemen | Kleinste Fallzahlen, höchster Spezialisierungsgrad; Länderförderung erst nach Prüfung der jeweiligen Richtlinien |

Die Voraussetzung der Simulation, ein auf Server und Browser gleich rechnender Kern, entsteht schon in Stufe 1.

## 6 Regel- und Förderkatalog: Die Regeln von 2026 gehören vollständig hinein

Der Katalog führt jede Regel als datierten Wert mit Quelle und Gültigkeit. Anhang B listet die Parameter des Steuer-, Miet- und Bewertungsrechts mit Fundstelle und Fassung, Anhang C die Förderkonditionen mit Stand. Dieser Abschnitt nennt, was daraus für den Bau folgt.

### Mietrecht: Die Mietvertragsart steuert, welche Erhöhung zulässig ist

Die Erhöhungswege des BGB schließen einander teilweise aus. Ein Werkzeug, das Indexanpassung, Erhöhung auf die Vergleichsmiete und Modernisierungsumlage addiert, überzeichnet den Mietpfad. Die Mietvertragsart ist deshalb Pflichtmerkmal jeder Einheit.

| Mietvertragsart | Erhöhung auf die Vergleichsmiete | Modernisierungsumlage | Mietpreisbremse |
|---|---|---|---|
| Frei vereinbart | Zulässig nach 15 Monaten Wartefrist; Kappungsgrenze 20 % oder 15 % in drei Jahren; Drittmittel werden abgezogen ([§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html)) | Zulässig ([§ 559](https://www.gesetze-im-internet.de/bgb/__559.html), [§ 559e BGB](https://www.gesetze-im-internet.de/bgb/__559e.html)) | Bei Mietbeginn; Vormiete und Ausnahmen beachten ([§ 556d](https://www.gesetze-im-internet.de/bgb/__556d.html), [§ 556e](https://www.gesetze-im-internet.de/bgb/__556e.html), [§ 556f BGB](https://www.gesetze-im-internet.de/bgb/__556f.html)) |
| Staffelmiete | Ausgeschlossen | Ausgeschlossen; für die Umlage nach Heizungstausch ist das offen (Abschnitt 7) | Für jede Staffel ([§ 557a BGB](https://www.gesetze-im-internet.de/bgb/__557a.html)) |
| Indexmiete | Ausgeschlossen | Nur bei Maßnahmen, die der Vermieter nicht zu vertreten hat, und beim Heizungstausch | Nur für die Ausgangsmiete ([§ 557b BGB](https://www.gesetze-im-internet.de/bgb/__557b.html)) |
| Gebunden (NBank) | Drei Jahre keine Erhöhung; danach nach BGB, höchstens 6,15 % in drei Jahren, auch bei Neuvermietung; Staffel- und Indexmiete unzulässig | Innerhalb derselben Grenze | Entfällt; es gilt die Eingangsmiete der Förderzusage ([RL Mietwohnraum 2026, Nr. 5.4.4 und 5.4.5](https://www.nbank.de/medien/nb-media/Downloads/Rechtliche-Grundlagen/Richtlinien/Richtlinie-F%C3%B6rderung-von-Mietwohnraum-%28RL-Mietwohnraum-2026%29.pdf)) |

Fünf Regeln verfälschen den Mietpfad am stärksten, wenn sie fehlen.

1. **Erhaltungsanteil und Zuschüsse** gehören nicht zu den umlagefähigen Kosten (§ 559 Abs. 2, § 559a Abs. 1 BGB). Bei einer Wohnung mit 70 Quadratmetern, 40.000 Euro Modernisierungskosten, 40 % Erhaltungsanteil und 12.000 Euro Zuschuss sind 960 Euro Umlage im Jahr zulässig; ohne den Abzug des Erhaltungsanteils wären es 2.240 Euro, also 1,52 Euro je Quadratmeter und Monat zu viel.
2. **Drittmittel mindern auch spätere Erhöhungen auf die Vergleichsmiete**, ein Zuschuss mit 8 % seines Betrags im Jahr (§ 558 Abs. 5 BGB); im Beispiel sind das weitere 960 Euro. Beim Ankauf wirken so auch Drittmittel aus Modernisierungen des Verkäufers fort. Wie lange der Abzug gilt, sagt das Gesetz nicht; bis zur Klärung rechnet das Werkzeug ihn unbefristet (Abschnitt 7).
3. **Beim Heizungstausch hängt die Umlage an der Förderfähigkeit.** Ist die Maßnahme dem Grunde nach förderfähig und gefördert, sind 10 % der Kosten abzüglich der Drittmittel umlagefähig; ist sie förderfähig, aber nicht gefördert, 8 %. Ist sie nicht förderfähig, gibt es eine Umlage nur, wenn der Einbau zugleich Endenergie einspart oder vom Vermieter nicht zu vertreten ist (§ 559e Abs. 1, § 559 Abs. 1 BGB). Für Heizungen gilt stets die Kappung von 0,50 Euro je Quadratmeter und Monat. Jede Maßnahme trägt deshalb als Pflichtfeld die Nummer des § 555b BGB, unter die sie fällt.
4. **Bei der Neuvermietung darf die Vormiete vereinbart werden**, auch wenn sie über der Grenze der Mietpreisbremse liegt (§ 556e BGB); wer das übersieht, unterschätzt den Wert eines Ankaufs.
5. **Die Miete einer geförderten Wohnung folgt drei Lagen.** In der Bindung gilt die Obergrenze der Förderzusage auch bei Neuvermietung; ein Mieterwechsel führt nicht zur Marktmiete. Nach der Bindung steigt die Miete des Bestandsmieters nur über die Vergleichsmiete mit Kappungsgrenze. Bei Neuvermietung nach der Bindung gilt die Marktmiete, begrenzt durch die Mietpreisbremse, wo eine Landesverordnung besteht; für Wohnungen, die nach dem 01.10.2014 erstmals genutzt und vermietet wurden, entfällt auch diese Grenze (§ 556f BGB). Der geförderte Neubau nähert sich der Marktmiete nach Bindungsende also über die Fluktuation; ohne diese Regel wäre sein Restwert unterschätzt.

### Steuern: Zwei Regeln wirken als Schwelle

Die degressive Abschreibung von 5 % steht nur zu, wenn der Steuerpflichtige das Wohngebäude selbst herstellt oder bis zum Ende des Fertigstellungsjahres anschafft ([§ 7 Abs. 5a EStG](https://www.gesetze-im-internet.de/estg/__7.html)). Das Werkzeug bietet sie beim Ankauf älterer Bestände nicht an. Bei einem Gebäudeanteil von 800.000 Euro aus dem Baujahr 1970 sind 16.000 Euro im Jahr abziehbar; mit der degressiven Abschreibung wären es im ersten Jahr 40.000 Euro, und die Rendite des Ankaufs wäre zu hoch ausgewiesen.

Die Sonderabschreibung für den Mietwohnungsneubau hat eine Baukostenobergrenze, die als Ausschlussgrenze wirkt: Liegen die Kosten darüber, entfällt die Sonderabschreibung ganz. Sie wird außerdem rückwirkend gestrichen, wenn nachträgliche Kosten die Grenze binnen drei Jahren überschreiten oder die Wohnung in den ersten zehn Jahren nicht durchgehend vermietet oder steuerfrei verkauft wird ([§ 7b EStG](https://www.gesetze-im-internet.de/estg/__7b.html)). Jede Variante und jeder Stressfall prüft die Grenze deshalb neu: Ein Baukostenstress von 10 % auf 4.900 Euro je Quadratmeter überschreitet die Grenze von 5.200 Euro und streicht die gesamte Sonderabschreibung.

Die Zinsschranke folgt in Stufe 3. Für sie gilt die berichtigte Rechenregel in Anhang B.3; ob sie überhaupt greift, hängt an der Freigrenze, an der Konzernzugehörigkeit und am Eigenkapitalvergleich.

### Heizung und CO2-Kosten: ein neuer Kostenblock beim Vermieter, auch im Neubau

Das Gebäudeenergiegesetz heißt seit 29.07.2026 Gebäudemodernisierungsgesetz (GModG); die 65-%-Regel für neue Heizungen ist entfallen. Wer seither in ein bestehendes Gebäude eine Gas-, Öl- oder Flüssiggasheizung einbaut, muss ab 2029 einen steigenden Pflichtanteil an Bio-Brennstoffen einsetzen. Solarthermie, eine Lüftungsanlage mit Wärmerückgewinnung oder eine Wärmepumpen-Hybridheizung erfüllen die Pflicht ebenfalls ([§ 43 GModG](https://www.gesetze-im-internet.de/geg/__43.html)). Zugleich trägt der Vermieter bei solchen Heizungen ab 2028 die Hälfte der CO2-Kosten und der Gasnetzentgelte und ab 2029 die Hälfte der Kosten des Pflichtanteils ([§ 5a CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/__5a.html)). Fällt die alte Heizung irreparabel aus, können sich Pflicht und Kostenteilung um zwölf Monate verschieben.

**Die Kostenteilung gilt entsprechend für Neubauten**, die bis 31.12.2029 errichtet werden, sofern der Bauantrag ab dem 13.05.2026 gestellt wurde ([§ 5b CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/__5b.html)). Der Pflichtanteil selbst gilt nur für bestehende Gebäude. Im Neubau sind nach dem Wortlaut deshalb Netzentgelte und CO2-Kosten zu teilen, während die Teilung der Bio-Brennstoffkosten keinen Gegenstand hat; diese Auslegung prüft der Anwalt (Abschnitt 7). Die Härtefallregel greift für professionelle Vermieter nicht, weil sie höchstens sechs vermietete Wohnungen voraussetzt. Im Finanzplan ist das eine eigene Auszahlungszeile, die Stufe 1 beim Ankauf wie beim Neubau braucht. Stufen, Fristen und Fundstellen stehen in Anhang B.2.

### Überholte Angaben und laufende Gesetzgebung

Drei Angaben, die in der Praxis noch kursieren, sind überholt. Der Mindesthebesatz der Gewerbesteuer beträgt ab 2027 280 % statt 200 %; die Untergrenze der Belastung steigt rechnerisch von 7,0 % auf 9,8 %. Die pauschale Erhaltungskürzung von 15 % beim Heizungstausch gilt für neue Gas- und Ölheizungen gerade nicht. Und die Makler- und Bauträgerverordnung erlaubt höchstens sieben Teilbeträge insgesamt, die erste Rate eingeschlossen (Anhang B.4). Eine vierte Angabe ist zu prüfen: Die Bagatellgrenze von 5 % bei der Umsatzsteueroption steht nicht im Gesetz. Ob die Finanzverwaltung sie anerkennt, ist am Umsatzsteuer-Anwendungserlass nachzulesen; bis dahin führt der Katalog sie als ungeprüfte Verwaltungsauffassung.

Drei laufende Vorhaben würden Ergebnisse ändern und werden im Katalog als Entwurfsstand geführt, der je Kalkulation zugeschaltet werden kann: eine Regel zur Kaufpreisaufteilung (§ 6f EStG) aus dem Jahressteuergesetz 2026, ein „Mietrecht II“ zu Indexmiete und Möblierungszuschlag und die bis 01.12.2026 angekündigte Grüngas- und Grünheizölquote ([§ 42a GModG](https://www.gesetze-im-internet.de/geg/__42a.html)). Keines der drei steht in den gelesenen Gesetzesfassungen. Die Gesetzesdatenbank des Bundes zeigt zudem nur die geltende Fassung. Bereits verkündete Änderungen mit späterem Inkrafttreten sind am Bundesgesetzblatt zu prüfen; das betrifft die Grenze des Verlustvortrags ab 2028 (Anhang B.3).

### Das Fördermodul: Fachleute richten Programme ohne Programmierung ein

**Empfehlung:** Das Fördermodul ist ein Baukasten. Ein Programm besteht aus allgemeinen Angaben (Geber, Rechtsgrundlage, Antragsweg, Zielgruppe) und einer oder mehreren Förderkomponenten: zinsverbilligtes Darlehen, Tilgungszuschuss, Einmalzuschuss, laufender Zuschuss, steuerliche Förderung, Bürgschaft. Jede Komponente trägt eine Bemessungsregel mit Deckel, Zuschläge, einen Auszahlungsplan, Gebühren und ein Beihilfekennzeichen.

Drei Regelarten kommen hinzu, die Excel-Modelle selten abbilden. Bindungen erzeugen einen eigenen Mietpfad je gebundener Einheit. Voraussetzungen sind prüfbare Regeln mit Nachweis und Frist. Kumulierungsregeln wirken über Programme hinweg als Ausschluss, Sperrfrist, gemeinsame Höchstquote oder Kostenabgrenzung. Jede Fassung der Konditionen hat ein Gültig-ab-Datum, ein auslösendes Ereignis (Antrag, Zusage, Bauantrag, Baubeginn) und eine Quelle.

Sechs Kopplungen stellt das Modul selbst her, weil hier die teuersten Fehler entstehen. Zuschüsse mindern die Kostenbasis der Modernisierungsumlage, Zinsvorteile den Erhöhungsbetrag, gerechnet auf den Ursprungsbetrag des Darlehens ([§ 559a BGB](https://www.gesetze-im-internet.de/bgb/__559a.html)). Dieselben Drittmittel mindern spätere Erhöhungen auf die Vergleichsmiete. Bindungen ersetzen den Marktmietpfad nach den drei Lagen der fünften Mietregel. Der Tilgungszuschuss der KfW fließt nicht als Geld zu; er wird zwei, vier und fünf Jahre nach der Zusage auf die zuletzt fälligen Raten angerechnet und ist im Finanzplan eine Sondertilgung. Die Kumulierungsgrenze von 60 % in der Bundesförderung für effiziente Gebäude zählt Zuschüsse und Tilgungszuschüsse, nicht aber Zinsverbilligungen. Und die Eigenkapitalrendite wird an der Schwelle der NBank gemessen.

### NBank: Darlehen und Zuschuss decken höchstens 80 % der zuwendungsfähigen Kosten

Die niedersächsische Förderung zeigt, warum das Modul nicht auf ein Fördermuster festgelegt sein darf. Bis 30.06.2026 galt ein Darlehen über 75 % der Gesamtkosten mit 30 % Tilgungsnachlass. Seit 01.07.2026 gilt die Verbindung aus einem 35 Jahre zinslosen Darlehen und einem Zuschuss, der Tilgungsnachlass ist entfallen, und die Bemessungsgrenze der Herstellungskosten stieg zwischen 01.07. und 01.10.2026 von 4.800 auf 5.250 Euro je Quadratmeter.

Darlehen und Zuschuss ergeben in allen drei Einkommensgruppen zusammen höchstens **80 % der zuwendungsfähigen Kosten**; mindestens 20 % Eigenkapital sind Voraussetzung (die Richtlinie spricht von Eigenmitteln). Ausfinanziert ist das Vorhaben damit nicht. Zuwendungsfähig sind die Herstellungskosten der Kostengruppen 200 bis 700 und das Grundstück höchstens zum Bodenrichtwert (RL Nr. 1.5 und 5.3.2). Zusätzlich zu finanzieren sind deshalb Grundstückskosten über dem Bodenrichtwert, Kosten über der Bemessungsgrenze und die Entgelte der NBank von rechnerisch 0,70 % bis 0,775 % der zuwendungsfähigen Kosten. Finanzierungskosten einschließlich Bauzeitzinsen (Kostengruppe 800) sind nach diesem Wortlaut ebenfalls nicht zuwendungsfähig; die Bestätigung der NBank steht aus und gehört in das Gespräch. Die Auszahlung in vier Raten nach Baufortschritt erfordert eine Zwischenfinanzierung. Andere Fördermittel dürfen daneben genutzt werden (RL Nr. 11.4).

Die Eigenkapitalrendite, an der die NBank die Angemessenheit misst, weist das Werkzeug vorab aus. Solange die NBank ihre Rechenweise nicht bestätigt hat, trägt die Kennzahl die Bezeichnung „Eigenkapitalrendite (VOFI) gegenüber 30-Jahres-Swapsatz plus 100 Basispunkte, eigene Annahmen“. Eine falsch benannte Behördenkennzahl schadet im Beratungsgeschäft mehr als gar keine.

Für Bestände mit auslaufenden Bindungen bietet die NBank zwei weitere Programme, die Verlängerung auslaufender Bindungen und den Erwerb von Bindungen (Anhang C.1). Die Verlängerung ist beim Ankauf gebundener Bestände die naheliegende Variante zum Auslaufenlassen und gehört deshalb in Teilschritt 1c.

### Pflege: redaktionell, mit benannter Verantwortung

Strukturiert und tagesaktuell liegen nur die KfW-Zinsen vor: Die Website der KfW lädt sie aus einer Datei, die für 42 Programme Laufzeit, tilgungsfreie Jahre, Zinsbindung, Soll- und Effektivzins liefert. Diese Quelle ist nicht dokumentiert und ohne zugesicherte Stabilität; vor einer Nutzung im Betrieb ist die Zustimmung der KfW einzuholen ([KfW-Zinsdatensatz](https://www.kfw.de/zinsen/alle.rates)). Höchstbeträge, Sätze und Bindungen veröffentlicht kein Geber strukturiert; sie stehen in datierten PDF-Dokumenten. Die Förderdatenbank des Bundes meldet über einen Nachrichtenkanal geänderte Programme ohne Konditionen und taugt damit als Änderungsmelder ([foerderdatenbank.de](https://www.foerderdatenbank.de/FDB/DE/Service/RSS/rss.html)). **Empfehlung:** ein redaktionell gepflegter Katalog mit benannter Verantwortung und Vertretung im Unternehmen, automatisiert höchstens bei den Zinsen.

## 7 Rechtlicher Rahmen des Werkzeugs: Datenschutz vor dem ersten Teilschritt, Beratungsgrenzen vor dem ersten Kundeneinsatz

Das Werkzeug rechnet Steuern, zulässige Mieten und Förderung für Dritte und hält fest, wer wann was geändert hat. Daraus folgen fünf Rechtsfragen, die Datenmodell, Berichte und Protokoll prägen. Die Einschätzungen stützen sich auf den Wortlaut der genannten Vorschriften und bleiben Planungsannahmen, bis Anwalt und Steuerberater sie geprüft haben. Jede Frage hat einen Zeitpunkt, zu dem sie geklärt sein muss.

| Thema | Worum es geht | Planungsannahme für den Bau | Geklärt |
|---|---|---|---|
| Grenze zur Rechts- und Steuerberatung | Hilfeleistung in Steuersachen und Rechtsdienstleistung beginnen, sobald eine Tätigkeit in fremden Angelegenheiten „eine rechtliche Prüfung des Einzelfalls erfordert“, und sind Befugten vorbehalten ([§ 2 StBerG](https://www.gesetze-im-internet.de/stberg/__2.html); [§ 2 RDG](https://www.gesetze-im-internet.de/rdg/__2.html)). Als Nebenleistung zu einer anderen Tätigkeit sind beide erlaubt. Für die Fördermittelberatung sagt das Gesetz das ausdrücklich ([§ 5 Abs. 2 Nr. 3 RDG](https://www.gesetze-im-internet.de/rdg/__5.html)); bei Steuerfragen entscheiden Inhalt, Umfang und Zusammenhang mit der Haupttätigkeit ([§ 4e StBerG](https://www.gesetze-im-internet.de/stberg/__4e.html)) | Kundenberichte führen Steuer- und Mietrechtsparameter als Annahmen, die der Kunde oder sein Steuerberater vorgibt (Grenzsteuersatz, Abschreibungswahl, „Sonderabschreibung angenommen“). Das Werkzeug rechnet die Folgen und bescheinigt keine Zulässigkeit. Prüfmeldungen wie die 15-%-Grenze bleiben interne Hinweise | vor dem ersten Kundeneinsatz |
| Haftung für Rechenergebnisse und Förderaussagen | Eine Rendite- oder Förderaussage im Kundenbericht kann als Auskunft gelesen werden, für die das Haus einsteht. Haftungsausschlüsse in Geschäftsbedingungen greifen bei grober Fahrlässigkeit nicht: gegenüber Verbrauchern nach [§ 309 Nr. 7 BGB](https://www.gesetze-im-internet.de/bgb/__309.html), gegenüber Unternehmern über die Inhaltskontrolle nach [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html) ([§ 310 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__310.html)). Wer in einem Förderantrag für sich oder einen anderen unrichtige Angaben macht, kann sich schon bei Leichtfertigkeit strafbar machen ([§ 264 Abs. 1 und 5 StGB](https://www.gesetze-im-internet.de/stgb/__264.html)); ob die Wohnraumförderung unter die Vorschrift fällt, ist offen | Berichte sprechen von „Ergebnis unter den ausgewiesenen Annahmen“ und bei der NBank-Kennzahl von einer eigenen Rechnung ohne Aussage über die Bewilligung. Jede Förderkondition trägt ihr Stand-Datum. Der Förderantrag entsteht nur aus einem freigegebenen Arbeitsstand. Die Haftung regelt der Beratungsvertrag, abgestimmt auf die Vermögensschadenhaftpflicht | vor dem ersten Kundeneinsatz |
| Beihilferecht | Die Sonderabschreibung für den Mietwohnungsneubau wird Unternehmen mit Gewinneinkünften nur gewährt, soweit die De-minimis-Verordnung (EU) 2023/2831 eingehalten ist ([§ 7b Abs. 5 EStG](https://www.gesetze-im-internet.de/estg/__7b.html)); auch KfW 266 ist eine De-minimis-Beihilfe. Die NBank-Förderung stützt sich auf den Freistellungsbeschluss (EU) 2025/2630 für Leistungen der Daseinsvorsorge; ihre Renditeprüfung ist dessen Kontrolle gegen Überkompensation | Jede Förderkomponente trägt ein Beihilfekennzeichen (keine Beihilfe, De-minimis, Gruppenfreistellung, Daseinsvorsorge). Ein De-minimis-Konto je Unternehmensgruppe über drei Jahre warnt bei Überschreitung, sonst rechnet das Werkzeug einen Steuervorteil ein, der nicht gewährt wird | vor dem ersten Kundeneinsatz |
| Nutzungsrechte an eingebundenen Inhalten | Gesetze und Verordnungen sind frei. Private Normen wie DIN 276 und DIN 277 bleiben geschützt, auch wenn Gesetze auf sie verweisen ([§ 5 UrhG](https://www.gesetze-im-internet.de/urhg/__5.html)). Die Kostenkennwerte des BKI sind ein kommerzielles Datenwerk, die Mietflächenrichtlinie der gif ein Verbandswerk. Der wiederholte, systematische Abruf der KfW-Zinsdaten kann Rechte des Datenbankherstellers berühren ([§ 87b UrhG](https://www.gesetze-im-internet.de/urhg/__87b.html)) | Eine Rechteliste nennt je Quelle Lizenzgeber, erlaubte Nutzung intern und in Kundenberichten und Kosten. Bei DIN wird die Gliederung mit Nummern und Kurzbezeichnungen getrennt vom Normtext behandelt. BKI-Werte kommen nur mit einer Lizenz hinein, die Kundenberichte abdeckt; KfW-Zinsen nur mit Zustimmung der KfW | vor dem ersten Teilschritt, weil schon die Grobkalkulation die Gliederung der DIN 276 nutzt |
| Datenschutz und Mitbestimmung | Ein Protokoll mit Person, Zeitpunkt, altem und neuem Wert und eine Anzeige, wer gerade wo arbeitet, sind geeignet, Verhalten und Leistung von Beschäftigten zu überwachen; besteht ein Betriebsrat, bestimmt er mit ([§ 87 Abs. 1 Nr. 6 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html)). Mieterlisten und Einkommensgruppen sind personenbezogene Daten; ein unveränderliches Protokoll, das sie enthält, kollidiert mit Löschpflichten | Einheiten werden über Kennungen geführt statt über Mieternamen; die Einkommensgruppe ist ein Merkmal der Einheit. Das Protokoll enthält keine personenbezogenen Mieterdaten und hat ein Aufbewahrungs- und Zugriffskonzept. Mitarbeiter werden informiert oder eine Betriebsvereinbarung geschlossen | vor dem ersten Teilschritt |

„Vor dem ersten Teilschritt“ heißt: in Phase 2, bevor der Architekturentwurf das Änderungsprotokoll festlegt; das Ergebnis liegt zur Bauentscheidung vor. Bis zum ersten Kundeneinsatz rechnet das Werkzeug intern mit den Planungsannahmen und den vorsichtigen Voreinstellungen aus Anhang B.

**Vor dem ersten Teilschritt zu prüfen, durch den Anwalt**

- das Datenschutzkonzept (Auftragsverarbeitung, Folgenabschätzung, Lösch- und Auskunftspflichten, Rolle des Hauses bei Kundenzugängen);
- die Mitbestimmung bei Änderungsprotokoll und Präsenzanzeige;
- die Lizenzlage für DIN, BKI, gif, KfW-Zinsdaten und Destatis-Indizes.

**Vor dem ersten Kundeneinsatz zu prüfen, durch den Anwalt**

- die Abgrenzung von Werkzeug und Kundenbericht zur Rechts- und Steuerberatung, mit freigegebenen Formulierungen für Berichte; gemeinsam mit dem Steuerberater, wie weit die Nebenleistung nach § 4e StBerG steuerliche Aussagen in einer Investitions- und Förderberatung trägt;
- Beratungsvertrag und Haftungsbegrenzung gegenüber Verbrauchern und Unternehmern; der Sorgfaltsmaßstab für Zahlen, die in Förderanträge eingehen, und die Anwendbarkeit des § 264 StGB auf die Wohnraumförderung;
- die Auslegungsfragen des Miet- und Heizungsrechts: der Ansatz zinsverbilligter Darlehen beim Heizungstausch nach § 559e Abs. 1 BGB; die Dauer des Drittmittelabzugs nach § 558 Abs. 5 BGB; die Geltung des Staffelmieten-Ausschlusses für § 559e BGB; die Umlage eines nicht förderfähigen Heizungstauschs als energetische Modernisierung nach § 555b Nr. 1 BGB; der zeitliche Anwendungsbereich des § 559f BGB; die Teilung der Bio-Brennstoffkosten im Neubau nach § 5b CO2KostAufG.

**Vor dem ersten Kundeneinsatz zu prüfen, durch den Steuerberater**

- die Ermittlung des Beihilfewerts der Sonderabschreibung und die Führung des De-minimis-Kontos;
- die Abgrenzung des gewerblichen Grundstückshandels und seine Folgen je Steuerstatus;
- der Steuerstatus kommunaler und gemeinnütziger Wohnungsunternehmen und die Verlustverrechnung ab 2028;
- bei der Zinsschranke die Einordnung von Konzernzugehörigkeit und Eigenkapitalvergleich;
- bei der Umsatzsteuer die Bagatellgrenze von 5 % nach Verwaltungsauffassung und die Behandlung von Stellplätzen als Nebenleistung zur Wohnung.

## 8 Technik und Zusammenarbeit: eine Rechenlogik an zwei Orten, gleichzeitiges Bearbeiten über den Server

### Rechenkern und Server in Rust, Oberfläche in TypeScript

Das Werkzeug braucht dieselbe Rechen- und Prüflogik an zwei Orten. Im Browser soll jede Eingabe sofort das Ergebnis zeigen; auf dem Server müssen dieselben Zahlen für Freigabe, Export, Simulation und Protokoll verbindlich entstehen. In der Programmiersprache Rust wird der Kern einmal geschrieben. Er läuft auf dem Server und, übersetzt in WebAssembly, im Browser des Anwenders; WebAssembly ist ein Format, in dem derselbe Programmcode im Webbrowser läuft. Das spart die Pflege zweier Rechenwerke und verhindert, dass Bildschirm und Bericht voneinander abweichen, solange beide dieselben Rechenbausteine nutzen. Vergleichbare Produkte gehen denselben Weg, etwa die Tabellenkalkulationen Quadratic und IronCalc ([Quadratic](https://quadratichq.com/technology); [IronCalc](https://github.com/ironcalc/IronCalc)). Die Oberfläche entsteht in TypeScript, der verbreiteten Sprache für Web-Oberflächen, weil es dort ausgereifte Bausteine für Tabellen, Diagramme und Formulare und mehr Entwickler gibt.

Ein eigener Probelauf mit einem vereinfachten Rechenmodell stützt die Wahl: Derselbe Programmcode lieferte auf dem Server und im Browser bis auf die letzte Stelle gleiche Ergebnisse, sofern die mathematischen Funktionen aus demselben Baustein stammen; im Browser erreichte der Kern 50 bis 75 % der Servergeschwindigkeit. Geldbeträge werden exakt dezimal geführt; der dafür verbreitete Baustein rechnet mit rund 28 Stellen und damit ohne Rundungsfehler der Zahldarstellung ([rust_decimal](https://crates.io/crates/rust_decimal)). Dass Restschulden auf den Cent mit dem Kontoauszug der Bank übereinstimmen, folgt erst aus den festgelegten Rundungsregeln (Anhang A, Nr. 10).

Die Entscheidung hat ihren Preis. Fachleute, die Rust, Finanzmathematik und Immobilienwissen verbinden, sind selten. Der Baukasten hat Lücken: Bausteine für den internen Zinsfuß und für die Zählung der Zinstage nach Bankenkonvention sind kaum verbreitet und werden selbst geschrieben, ein Baustein für die Rechteprüfung wurde am 22.10.2026 von seinen Entwicklern eingestellt, und viele zentrale Bausteine gelten nach Angabe ihrer Entwickler noch nicht als ausgereift, sodass jede neue Fassung Nacharbeit verlangen kann ([xirr](https://crates.io/crates/xirr); [Oso](https://github.com/osohq/oso); [axum](https://crates.io/crates/axum)). Und die Organisation hinter den WebAssembly-Werkzeugen wurde 2025 aufgelöst; die Kernwerkzeuge erscheinen unter neuer Trägerschaft weiter, zuletzt am 30.10.2026 ([Rust-Blog](https://github.com/rust-lang/blog.rust-lang.org/blob/main/content/inside-rust/sunsetting-the-rustwasm-github-org.md); [wasm-bindgen](https://crates.io/crates/wasm-bindgen)).

Drei Leitplanken begrenzen diese Risiken. Der Rechenkern bleibt klein, fachlich gegliedert und vollständig durch die Referenzfälle abgesichert. Der Server bleibt schlank (Anmeldung, Änderungsprotokoll, Verteilung, Exporte), sodass er notfalls in anderer Technik ersetzbar wäre, ohne den Kern anzutasten. Und es wird keine allgemeine Formelmaschine gebaut: IronCalc gilt nach knapp drei Jahren Entwicklung noch nicht als fertig (Version 0.9); ein Kern für ein festes Fachmodell ist deutlich kleiner, weil Modell und Rechenregeln feststehen.

### Zusammenarbeit: gleichzeitiges Bearbeiten bleibt, das Zusammenführen von Offline-Kopien entfällt

Sie hatten „echte Co-Editierung wie Google Sheets“ gewählt. Der Kern dieser Vorgabe wird umgesetzt: Mehrere Personen bearbeiten dasselbe Projekt gleichzeitig, jede Eingabe erscheint sofort bei allen, und ab Teilschritt 1b zeigt eine Präsenzanzeige, wer gerade in welchem Feld arbeitet. **Abgewichen wird in einem Punkt:** Kopien, die ohne Verbindung getrennt bearbeitet wurden, werden nicht nachträglich zusammengeführt. Bearbeiten setzt eine Verbindung zum Server voraus.

Das Verfahren, hier **servergeführte Zusammenarbeit** genannt, folgt dem Muster der Gestaltungssoftware Figma und der Projektsoftware Linear. Jede Eingabe geht als einzelne Änderung an den Server. Der Server prüft Berechtigung und Plausibilität, schreibt die Änderung in ein fortlaufendes Protokoll und verteilt sie an alle geöffneten Bildschirme ([Figma](https://madebyevan.com/figma/how-figmas-multiplayer-technology-works/); [Linear-Analyse](https://github.com/wzhudev/reverse-linear-sync-engine)). Ändern zwei Personen im selben Moment dasselbe Feld, gilt der spätere Wert. Beide sehen ihn sofort, beide Eingaben stehen im Protokoll, und die Änderung lässt sich zurücknehmen.

Vier geschäftliche Gründe tragen die Abweichung. Der Nutzen des Zusammenführens ist gering, weil das Modell aus Zahlenfeldern und Listen besteht und nicht aus Fließtext. Das Änderungsprotokoll, das Controlling und Revision brauchen, fällt beim servergeführten Verfahren als Nebenprodukt an; es ist zugleich Prüfpfad und Grundlage für Rückgängig und benannte Arbeitsstände. Die Technik für das Zusammenführen speichert Änderungen dagegen als Datenpakete, die ein Mensch nicht lesen kann, und bräuchte ein zweites Protokoll. Rechte lassen sich beim servergeführten Verfahren vor jeder Änderung prüfen und beim Zusammenführen erst danach. Und das Risiko wäre höher: Der am besten passende Baustein stammt von einem kleinen Team und erschien in gut fünf Monaten in rund neun neuen Fassungen, der verbreitetste gilt seinen Entwicklern noch nicht als ausgereift, und ein dritter beschreibt seine Rust-Schnittstelle selbst als „low level and not well documented“ ([Loro](https://github.com/loro-dev/loro); [yrs](https://crates.io/crates/yrs); [Automerge](https://github.com/automerge/automerge)). Fertige Dienste wie Zero sind auf andere Servertechnik zugeschnitten oder nur als Cloud-Dienst zu haben, was den eigenen Server in der EU unterläuft ([Zero](https://github.com/rocicorp/mono)).

Die Option bleibt offen: Für wenige Freitextfelder wie Kommentare lässt sich später gezielt ein Baustein für gemeinsames Schreiben einbetten, ohne den Aufbau zu ändern.

### Weitere Festlegungen zu Rollen, Anmeldung, Export, Simulation und Betrieb

| Festlegung | Begründung | Offen |
|---|---|---|
| Rolle je Projektmitgliedschaft: Verantwortlicher, Bearbeiter, Prüfer, Leser, später lesender Kunde. Teilschritt 1a unterscheidet nur Bearbeiter und Leser; das volle Modell mit Freigaben folgt in 1b | Projektzuweisung an Mitarbeiter; Kundenzugang ohne Umbau | – |
| Anmeldung mit dem vorhandenen Firmenkonto über den verbreiteten Standard OIDC ([openidconnect](https://crates.io/crates/openidconnect)) | Keine eigenen Passwörter; Sperrung an einer Stelle | – |
| Jede Tabelle der Datenbank trägt von Beginn an ein Mandantenkennzeichen | Kundenzugänge später ohne Umbau der Datenhaltung | – |
| Für die Tabellenoberfläche der Baustein AG Grid Enterprise: Bereichsauswahl, Kopieren aus Excel und Excel-Export sind enthalten; 999 US-Dollar je Entwickler als unbefristete Lizenz ([AG Grid](https://www.ag-grid.com/license-pricing/)) | Ausgereifter Standardbaustein statt Eigenbau | Lizenzbedingungen für den Betrieb gegenüber externen Kunden |
| Excel-Export mit Annahmenblatt und Versionsstempel, ab Teilschritt 1b mit Summen- und Saldoformeln in der VOFI-Tabelle ([rust_xlsxwriter](https://crates.io/crates/rust_xlsxwriter)) | Banken und Gremien rechnen Zeilen und Spalten nach; ein vollständig in Excel nachrechenbarer Export ist ein eigenes Teilprojekt | – |
| Simulation: Vorschau im Browser, Läufe für Berichte auf dem Server | Die Genauigkeit der Quantile verlangt mehr Läufe, als der Browser zügig rechnet (Anhang A.7) | Die Grenze wird am fertigen Modell gemessen, bevor Antwortzeiten zugesagt werden |
| Eine Anwendung mit einer PostgreSQL-Datenbank (einer verbreiteten freien Datenbank), Betrieb in der EU | Geringe Betriebskosten, kein Anbieterzwang | Wahl des Anbieters; Auftragsverarbeitung |

## 9 Belastbarkeit: Recht und Förderung überwiegend am Original geprüft, Markt nach Herstellerangaben, Bedarf nicht mit Anwendern bestätigt

| Belegstufe | Umfang |
|---|---|
| Am Original geprüft (Stand 17. und 18.11.2026) | Förderkonditionen von KfW, BAFA und NBank an Merkblättern, Richtlinien und Produktinformationen; Steuer-, Miet- und Bewertungsrecht am Gesetzestext auf gesetze-im-internet.de; Rechenschema, Kennzahlenformeln und Testfall durch zwei unabhängige Gegenrechnungen; zwei veröffentlichte Rechenbeispiele des IWU; Stand der Softwarebausteine an den Paketverzeichnissen |
| Herstellerangaben und Sekundärquellen | Funktionsumfang der Wettbewerbsprodukte, wie von den Anbietern beworben, ohne Vorführung und ohne unabhängige Nutzerbewertungen der deutschen Fachlösungen; Marktstudien und Fachliteratur zu Risikoverfahren; Leistungswerte der Technik aus einem Probelauf an einem vereinfachten Modell |
| Fachliche Folgerung, nicht bestätigt | Einstufung in Pflicht und Differenzierung, Zuschnitt der Stufen und Teilschritte; das Arbeitsziel von rund 15 Eingaben für die Grobkalkulation; die Einschätzungen zum rechtlichen Rahmen in Abschnitt 7 und die Voreinstellungen für offene Auslegungsfragen |
| Nicht recherchiert | Erbbaurecht (übliche Erbbauzinsen, Wertsicherung, Entschädigung); Verwaltungsauffassung, Rechtsprechung und Landesrecht; die Anbieter Reasult, PROBIS, Corporate Planner, PlaCoM und evoreal |

**Offen vor der Umsetzung**

| Punkt | Zuständig |
|---|---|
| Rechenweise der Renditeprüfung; Tilgungsplan des Darlehens; Anerkennung eines KfW-Darlehens als Eigenkapitalersatz; ob nicht abziehbare Vorsteuer und Finanzierungskosten zu den zuwendungsfähigen Kosten zählen; Aufteilung bei teilgeförderten Vorhaben | Auftraggeber im Gespräch mit der NBank |
| Häufigkeit von Erbbaurecht im geförderten Neubau; Stellenwert der Frage „gefördert oder frei finanziert“ am Anfang der Neubaukalkulation | Auftraggeber (Fachfragen) |
| Zustimmung der KfW zum automatisierten Abruf der Zinsen | Auftraggeber |
| Werte, die im Gesetzestext nicht stehen und am Original nachzuziehen sind: Grunderwerbsteuersatz Niedersachsen (5,0 % nach Sekundärangabe); ab 01.01.2026 indexierte Beträge der II. Berechnungsverordnung; fortgeschriebene Bewirtschaftungskosten der ImmoWertV für 2026; aktuelle Mindestkapitalisierungszinssätze der BaFin; Einkommensgrenzen der niedersächsischen Wohnraumförderung in Euro; in Niedersachsen geltende Verordnungen zu Mietpreisbremse und Kappungsgrenze | Katalogverantwortung |
| Abgleich der BAFA-Richtlinie mit der amtlichen Fassung BAnz AT 27.08.2026 B1 | Katalogverantwortung |
| Stand von Jahressteuergesetz 2026, Mietrecht II und Grüngasquote; verkündete Änderungen mit späterem Inkrafttreten am Bundesgesetzblatt, zuerst die Grenze des Verlustvortrags ab 2028 | Katalogverantwortung, vierteljährlich |
| Lehrbuchdefinitionen von Gesamtkapitalrendite und Amortisationsdauer nach Grob | Entwicklung; Auftraggeber stellt Exemplare bereit, wo nötig |
| Rechtsfragen nach Abschnitt 7 | Anwalt, Steuerberater |
| Funktionen der Wettbewerber über die Werbung hinaus | Auftraggeber über Vorführungen der drei VOFI-Anbieter; Entwicklung über die Recherche zu den fünf weiteren Anbietern; beides bis zur Vorprüfung |
| Marktübliche Werte für Kreditauflagen, Betreiberimmobilien, Streuungen und Abhängigkeiten | Anwender setzt sie; keine belastbaren Quellen |

## Anhang A: Vorgaben an den Rechenkern

Die Vorgaben gehen in die Spezifikation des Rechenkerns ein. Alle Zahlen beziehen sich, wenn nicht anders gesagt, auf den Testfall aus Abschnitt 3 (Jahresraster, Zahlungen am Periodenende, Habenzins 2 %, Kontokorrentzins 8 %, Verkauf im fünften Jahr).

### A.1 Tabellenaufbau und Rechenreihenfolge

1. Zinsen und Steuern einer Periode hängen nur von den Beständen der Vorperiode ab; Geldanlage und Kontokorrent gleichen den Saldo aus. So entsteht kein Zirkelbezug.
2. Der Kontokorrentzins geht in die Steuerbemessung und in den Periodensaldo ein. In der Variante mit 380.000 Euro Eigenkapital beträgt der Endwert 561.526,16 Euro; ohne den Zins läge er um 1.839,71 Euro daneben.
3. Die Ablösung der Restschuld im letzten Jahr ist eine Zahlung dieser Periode und steht vor dem Ausgleich.
4. Steuern laufen über eine eigene Nebenrechnung mit Abschreibungsplan und Verlustvortrag. Der Steuersatz auf Zinserträge ist getrennt vom Satz auf Mietüberschüsse einstellbar.
5. Für eine begrenzte Kontokorrentlinie führt die Tabelle eine Zeile für Liquiditätslücke oder Eigenkapitalnachschuss.

### A.2 Konventionen je Zahlungsart

6. Festgeschrieben werden je Zahlungsart: die Basisperiode der Indexierung, der Zahlungszeitpunkt am Periodenanfang oder -ende, der Zahlungsmonat der Steuer und der Verzinsungstakt. Wird der Eingabewert der Miete als Vorjahreswert gelesen, steigt die Rendite von 7,876 % auf 8,028 %.
7. Investition und Unterlassensalternative werden im selben Takt verzinst. Die Laufzeit geht als Monate geteilt durch zwölf in die Renditeformel ein.
8. Das Monatsraster verändert das Ergebnis gegenüber der Jahresrechnung von sich aus (Endwert 585.937,57 Euro, also 1.571,29 Euro mehr). Für Lehrbuchvergleiche gibt es einen ausgewiesenen Jahresmodus.
9. Die Probe „Summe der Monatswerte gleich Jahreswert“ gilt für Zahlungen, nicht für Bestände. Wertsicherungsklauseln mit Schwelle führen den Indexstand der letzten Anpassung als Zustand mit.
10. Rundung ist je Kontoart festgelegt: Darlehenskonten runden wie die Bank auf Cent je Rate, Steuerbeträge nach den jeweiligen Vorschriften, Kennzahlen bleiben ungerundet. Beispiel: 700.000 Euro zu 4 %, Monatsrate 3.500 Euro, zehn Jahre; die Restschuld beträgt bei voller Genauigkeit 528.208,56 Euro, bei Cent-Rundung je Rate 528.208,51 Euro. Die exakte Dezimalrechnung verhindert Rundungsfehler der Zahldarstellung; die Übereinstimmung mit Bank- und Steuerbescheiden folgt erst aus diesen Regeln. Potenzen und Wurzeln (Rendite, Monatszins aus Jahreszins) bleiben gerundete Größen.

### A.3 Kennzahlen

11. Die Unterlassensalternative erhält dieselbe Einlagen- und Entnahmenreihe wie die Investition. Bei 5.000 Euro Entnahme je Jahr beträgt der Endwert 558.656,41 Euro; ohne Spiegelung ergäbe sich eine Endwertdifferenz von 129.861,36 Euro statt 155.571,23 Euro und eine Rendite von 6,91 %.
12. Empfohlene Renditeformel für beliebige Einlagen und Entnahmen: r = ((EW + Σ Entnahme_t · q^(N−t)) / (Σ Einlage_t · q^(−t)))^(1/n) − 1. Dabei ist EW der Endwert, q = 1 + h · (1 − s) der Aufzinsungsfaktor je Periode aus Alternativzins h und Steuersatz s (im Monatsraster h geteilt durch zwölf), t die Periode der Zahlung, N die Zahl der Perioden und n die Laufzeit in Jahren. r liegt genau dann über dem Alternativzins, wenn die Endwertdifferenz positiv ist.
13. Im Testfall mit Entnahmen liefert die Formel unverändert 7,876 %, weil die Investition dort ihr Guthaben selbst zum Alternativzins anlegt. In der Variante mit Kontokorrent sinkt die Rendite mit Entnahmen von 8,12 % auf 8,09 %, weil die Entnahmen über den teureren Kontokorrent finanziert werden.
14. Bei einem Nachschuss von 50.000 Euro im zweiten Jahr (Endwert 636.495,82 Euro) ergeben vier Lesarten 7,18 % (Summe der Einlagen als Nenner), 7,25 % (empfohlene Formel), 7,50 % (interner Zins der Eigenkapitalreihe) und 7,88 % (Nachschuss wie eine negative Entnahme aufgezinst). Die Endwertdifferenz ist in allen Fällen 155.571,23 Euro.
15. Randfälle haben definierte Ergebnisse: Bei einem Endwert von null oder darunter beträgt die Rendite minus 100 %; bei Eigenkapital von null ist sie nicht definiert. Bei einem Zinssatz von exakt null tritt an die Stelle der Annuitätenformel die gleichmäßige Tilgung.
16. Das NBank-Darlehen ist eine eigene Darlehensart: zinslos, mit Verwaltungskostenbeitrag auf die Restschuld und einem von der NBank festgesetzten Tilgungsplan.
17. Der Schuldendienstdeckungsgrad nimmt Ablösung und Umschuldung aus dem Nenner aus. Sonst fällt er im Verkaufsjahr von 1,42 auf 0,09.
18. Beleihungsauslauf und Amortisationsdauer setzen einen Wertpfad je Periode voraus (Marktwert, Verkaufskosten, Vorfälligkeit, Steuer), der als eigene Nebenrechnung geführt wird. Für die Amortisationsdauer ist eine Lesart zu wählen; „Eigenkapital gedeckt“ und „Alternative erreicht“ liefern im Beispiel zwei gegenüber drei Jahren.
19. Die VOFI-Gesamtkapitalrendite wird nicht ausgewiesen, bis die Originalformel beschafft ist; drei Lesarten ergeben 4,61 %, 4,69 % und 4,76 %.
20. Der interne Zinsfuß ist bei mehreren Vorzeichenwechseln mehrdeutig. Das Werkzeug zählt die Wechsel, meldet alle Lösungen und verweist auf die VOFI-Rendite.

### A.4 Kontrollsummen

21. Jede Periode schließt mit einem Finanzierungssaldo von null. Ergebnisse erscheinen erst, wenn alle Kontrollsummen bestanden sind.
22. Je Kredit gilt: Auszahlungen zuzüglich einbehaltenem Disagio und kapitalisierten Zinsen, abzüglich Tilgungen, Tilgungszuschüssen und Ablösung, ergeben die Restschuld. Die einfache Probe „Summe der Tilgungen gleich Darlehensbetrag“ versagt bei Disagio, Tilgungszuschuss und kapitalisierten Bauzeitzinsen.
23. Für den Bestandssaldo (Guthaben abzüglich Kontokorrent und Restschulden) gilt in jeder Periode: Veränderung gleich originäre Zahlung, zuzüglich Einlagen, abzüglich Entnahmen, abzüglich Sollzinsen einschließlich Kontokorrent- und kapitalisierter Zinsen, zuzüglich Habenzinsen, abzüglich Steuer, zuzüglich Zuschüssen ohne Geldfluss (Tilgungszuschuss, Teilschulderlass), abzüglich einbehaltenem Disagio. Ohne die beiden letzten Glieder meldet die Probe bei einem Tilgungszuschuss von 35.000 Euro eine Abweichung von genau 35.000 Euro und bei 3 % Disagio auf 700.000 Euro eine von 21.000 Euro, obwohl richtig gerechnet wurde.
24. Die Probe „abgezinste Endwertdifferenz gleich Kapitalwert“ läuft als eigener Testmodus. Sie gilt exakt nur, wenn zugleich alle Zinssätze gleich sind (Kredite, Kontokorrent, Geldanlage, Alternative), keine Gebühren anfallen, die Steuer in der Entstehungsperiode gezahlt und Verluste sofort ausgeglichen werden, ein einziger Steuersatz gilt und der Kapitalwert auf die Zahlungsfolge nach Steuern ohne Zinsen gerechnet wird. Kapitalwert und Endwertdifferenz werden mit demselben Satz abgezinst, dem Zins nach Steuern. Mit einheitlich 4 % Zins ergeben beide Wege 110.371,99 Euro; mit den getrennten Zinssätzen des Testfalls weichen sie um 45.078,11 Euro voneinander ab.

### A.5 Bauphase

25. Der Mittelabfluss folgt einer Kurve, die bei null beginnt und bei 100 % endet; die kumulierte Kostenkurve wird üblicherweise als S-Kurve modelliert ([Lang, Leseprobe Mittelabfluss](https://www.k3kostencontrolling.de/media/files/expertknowledge/leseprobe_mittelabfluss.pdf)).
26. Ist das Eigenkapital als Quote der Gesamtkosten einschließlich Bauzeitzinsen vorgegeben, stellt der Kern die Quote in mehreren Durchläufen ein. Beispiel mit 10 Mio. Euro Kosten, linear über 24 Monate, 5 % Zins, 30 % Eigenkapital zuerst eingesetzt, Zins auf den Stand des Vormonats kapitalisiert: Ein einfacher Durchlauf ergibt 235.370 Euro Zinsen und 70,69 % Fremdkapital; nach sechs Durchläufen stehen 3.069.183 Euro Eigenkapital, 230.611 Euro Zinsen und 70,00 %.
27. Die Faustformel „Kosten mal Zins mal Bauzeit mal ein halb“ ergibt im selben Beispiel 500.000 Euro. Sie trifft nur bei voller Kreditfinanzierung von Beginn an (494.134 Euro); wird das Eigenkapital zuerst eingesetzt, liegt sie um das 2,17-Fache zu hoch und taugt nicht als Plausibilitätsmaß.

### A.6 Referenz- und Testfälle

28. Kirchner (IWU 2004, S. 16–18): 1.000 Euro Eigenkapital, Sollzins 7,5 %, Habenzins 5,0 %, drei Perioden; Endwert 1.322,48 Euro, VOFI-Rendite 9,76 %.
29. IWU 2013 (Anhang C, S. 51): Endwert 153.032 Euro, VOFI-Rendite 3,11 %; gerechnet mit der 2013 geltenden Modernisierungsumlage von 11 %.
30. Testfall: Endwert 584.366,28 Euro, Endwertdifferenz 155.571,23 Euro, VOFI-Rendite 7,876 %; dazu die Varianten mit Kontokorrent, Entnahmen und einheitlichem Zins.
31. Zu ergänzen sind Fälle für Nachschuss, Tilgungszuschuss, Disagio, Anlaufverluste mit Verlustvortrag, steuerpflichtigen Verkauf und das Monatsraster.

### A.7 Simulation

32. Hauptgrößen sind Endwertdifferenz, Median und Quantile. Der Mittelwert der Rendite eignet sich nicht, weil bei hohem Fremdkapitalanteil negative Endwerte auftreten.
33. Die Verkaufsrendite wird nur aus beschränkten Verteilungen gezogen, weil der Verkaufspreis von ihrem Kehrwert abhängt. Bei 4,5 % Erwartungswert und 1,5 Punkten Streuung einer Normalverteilung entstehen negative Renditen, und der mittlere Verkaufsfaktor schwankt je nach Zufallsstart zwischen 18,0 und 29,4 bei einem Basiswert von 22,2.
34. Mietsteigerung und Inflation folgen einem Prozess mit einstellbarer Beharrung. Die Streuung des Mietniveaus nach zehn Jahren beträgt bei unabhängigen Jahresziehungen 5,7 %, bei mittlerer Beharrung 11,6 % und bei einer Ziehung für alle Jahre rund 18 %.
35. Der Anwender gibt Rangkorrelationen ein, die das Werkzeug umrechnet. Unzulässige Korrelationsmatrizen werden auf die nächstgelegene zulässige korrigiert; die Korrektur wird angezeigt ([Iman-Conover-Verfahren](https://arxiv.org/pdf/1508.02749)).
36. Der Bericht zeigt Basisfall, Mittelwert und Median nebeneinander sowie die Wahrscheinlichkeit, die Zielrendite zu verfehlen; bei schiefen Verteilungen weicht der Mittelwert systematisch vom Basisfall ab.
37. Die Zahl der Läufe folgt aus dem Genauigkeitsziel der Hauptgrößen; für das 5-%-Quantil sind mindestens rund 10.000 Läufe nötig. Zur Einordnung: Soll der Mittelwert der Rendite bei einfacher Zufallsziehung mit 95 % Sicherheit auf fünf Basispunkte genau sein, braucht es 6.147 Läufe bei zwei Prozentpunkten Streuung, 13.830 bei drei und 38.416 bei fünf. Mit 1.000 Läufen und drei Punkten Streuung beträgt die halbe Breite dieses Vertrauensbereichs 18,6 Basispunkte, der Standardfehler 9,5. Bei geschichteter Ziehung gilt diese Formel nicht; dort wird der Fehler über unabhängige Wiederholungen geschätzt.
38. Für die Wiederholbarkeit eines Laufs werden Zufallsstartwert, Zufallsgenerator und dessen Version gespeichert. Server und Browser verwenden dieselben mathematischen Funktionen.
39. Als Bedienmuster dienen die Bandbreite direkt im Eingabefeld für Einsteiger und eine Ansicht mit Verteilungstyp und Korrelationen für Experten ([Causal](https://docs.causal.app/formulas/values-with-uncertainty); [Lumivero @RISK](https://lumivero.com/products/atrisk/)).

## Anhang B: Rechtsstand 17.11.2026 – Parameter für den Regel- und Förderkatalog

Alle Zeilen geben, wenn nicht anders vermerkt, den Gesetzestext auf gesetze-im-internet.de wieder, gelesen am 17.11.2026. Die Spalte „Fassung“ nennt das Datum der letzten dort ausgewiesenen Änderung. Verwaltungsauffassung, Rechtsprechung und Landesrecht sind nicht enthalten.

### B.1 Mietrecht (BGB, Fassung 23.07.2026)

| Regel | Inhalt | Fundstelle |
|---|---|---|
| Erhöhung auf die Vergleichsmiete | Die Miete muss 15 Monate unverändert sein; das Verlangen ist frühestens ein Jahr nach der letzten Erhöhung möglich; Modernisierungsumlagen und Betriebskostenanpassungen zählen dabei nicht. Die Vergleichsmiete wird aus den Entgelten der letzten sechs Jahre gebildet; Wohnraum mit gesetzlich oder durch Förderzusage festgelegter Miete bleibt außen vor | [§ 558 Abs. 1 und 2](https://www.gesetze-im-internet.de/bgb/__558.html) |
| Kappungsgrenze | 20 % in drei Jahren; 15 % in Gebieten, die das Land per Verordnung für jeweils höchstens fünf Jahre bestimmt. Sie gilt nicht, soweit mit dem Wegfall der Bindung eine Ausgleichszahlung des Mieters entfallen ist, bis zu deren Höhe | [§ 558 Abs. 3 und 4](https://www.gesetze-im-internet.de/bgb/__558.html) |
| Drittmittel bei der Vergleichsmiete | Vom Jahresbetrag der Erhöhung sind Drittmittel abzuziehen, ein Zuschuss mit 8 % seines Betrags. Wie lange der Abzug gilt, sagt das Gesetz nicht | [§ 558 Abs. 5](https://www.gesetze-im-internet.de/bgb/__558.html) |
| Mietpreisbremse | Miete bei Mietbeginn höchstens 10 % über der Vergleichsmiete; nur in Gebieten mit Landesverordnung; Verordnungen gelten längstens bis 31.12.2029 | [§ 556d](https://www.gesetze-im-internet.de/bgb/__556d.html) |
| Vormiete und Vormodernisierung | Die Vormiete darf vereinbart werden; Mietminderungen und Erhöhungen aus dem letzten Jahr des Vormietverhältnisses bleiben außer Betracht. Modernisierungen der letzten drei Jahre erhöhen die zulässige Miete um den Betrag einer Modernisierungsumlage | [§ 556e](https://www.gesetze-im-internet.de/bgb/__556e.html) |
| Ausnahmen von der Mietpreisbremse | Wohnungen, die nach dem 01.10.2014 erstmals genutzt und vermietet werden; die erste Vermietung nach umfassender Modernisierung | [§ 556f](https://www.gesetze-im-internet.de/bgb/__556f.html) |
| Staffelmiete | Jede Staffel gilt mindestens ein Jahr. Erhöhungen nach §§ 558 bis 559b sind ausgeschlossen; § 559e nennt der Wortlaut nicht. Die Mietpreisbremse gilt für jede Staffel. Eine betragsmäßige Obergrenze der Staffeln enthält das Gesetz nicht | [§ 557a](https://www.gesetze-im-internet.de/bgb/__557a.html) |
| Indexmiete | Die Miete folgt dem Verbraucherpreisindex und bleibt jeweils mindestens ein Jahr unverändert. Die Erhöhung auf die Vergleichsmiete ist ausgeschlossen. Eine Modernisierungsumlage ist nur zulässig bei Maßnahmen, die der Vermieter nicht zu vertreten hat, und beim Heizungstausch. Die Mietpreisbremse gilt nur für die Ausgangsmiete. Eine betragsmäßige Obergrenze der Indexanpassung enthält das Gesetz nicht | [§ 557b](https://www.gesetze-im-internet.de/bgb/__557b.html) |
| Modernisierungsumlage | 8 % der für die Wohnung aufgewendeten Kosten im Jahr. Kosten, die für Erhaltung ohnehin angefallen wären, gehören nicht dazu und sind notfalls zu schätzen | [§ 559 Abs. 1 und 2](https://www.gesetze-im-internet.de/bgb/__559.html) |
| Kappung der Umlage | 3 €/m² monatlich innerhalb von sechs Jahren; 2 €/m², wenn die Miete vorher unter 7 €/m² lag; für Heizungsmaßnahmen 0,50 €/m² innerhalb dieser Grenzen | [§ 559 Abs. 3a](https://www.gesetze-im-internet.de/bgb/__559.html) |
| Drittmittel bei der Umlage | Zuschüsse mindern die Kostenbasis. Bei zinsverbilligten Darlehen sinkt der Erhöhungsbetrag um die jährliche Zinsermäßigung, gerechnet auf den Ursprungsbetrag gegen den Marktzins erstrangiger Hypotheken bei Abschluss der Maßnahme. Mittel der Förderbanken von Bund und Ländern gelten als öffentliche Mittel | [§ 559a](https://www.gesetze-im-internet.de/bgb/__559a.html) |
| Vereinfachtes Verfahren | Bis 10.000 € Kosten je Wohnung; 30 % pauschaler Erhaltungsabzug; kein Abzug des Zinsvorteils. Kosten früherer Umlagen der letzten fünf Jahre mindern die 10.000 €. Danach fünf Jahre keine weitere Modernisierungsumlage, außer bei gesetzlicher Pflicht oder Beschluss der Wohnungseigentümer | [§ 559c](https://www.gesetze-im-internet.de/bgb/__559c.html) |
| Heizungstausch | 10 % der Kosten abzüglich der in Anspruch genommenen Drittmittel, wenn die Maßnahme dem Grunde nach zuschussfähig ist und Drittmittel genutzt wurden; ohne Förderung 8 % nach § 559. Der Erhaltungsanteil beträgt pauschal 15 %, nicht aber bei Gas-, Öl- und Flüssiggasheizungen nach § 43 GModG. Kappung 0,50 €/m² in sechs Jahren, zusammen mit anderen Umlagen höchstens 3 € oder 2 € | [§ 559e](https://www.gesetze-im-internet.de/bgb/__559e.html); [§ 555b Nr. 1a](https://www.gesetze-im-internet.de/bgb/__555b.html) |
| Wärmepumpe | Die vollen Kosten sind nur ansetzbar, wenn ein Fachunternehmer eine Jahresarbeitszahl von mindestens 2,5 nachweist; sonst die Hälfte. Der Nachweis entfällt bei Gebäuden, die nach 1996 errichtet wurden, die den Wärmeschutz der Verordnung vom 16.08.1994 einhalten, die nach einer Sanierung § 38 GModG entsprechen oder die mit höchstens 55 °C Vorlauftemperatur beheizbar sind | [§ 559f](https://www.gesetze-im-internet.de/bgb/__559f.html) |

### B.2 Heizung und CO2-Kosten (GModG und CO2KostAufG, Fassung 23.07.2026)

| Regel | Inhalt | Fundstelle |
|---|---|---|
| Heizungsrecht | Gebäudemodernisierungsgesetz (GModG), bis 28.07.2026 Gebäudeenergiegesetz. Die 65-%-Regel ist entfallen; der Eigentümer wählt unter mehreren Heizungsarten | [§ 42 GModG](https://www.gesetze-im-internet.de/geg/__42.html) |
| Pflichtanteil Bio-Brennstoff | Für nach dem 29.07.2026 in bestehende Gebäude eingebaute Gas-, Öl- und Flüssiggasheizungen: 10 % ab 2029, 15 % ab 2030, 30 % ab 2035, 60 % ab 2040 | [§ 43 GModG](https://www.gesetze-im-internet.de/geg/__43.html) |
| CO2-Kosten Wohnen | Zehn Stufen nach Ausstoß je Quadratmeter; Vermieteranteil von 0 % (unter 12 kg) bis 95 % (ab 52 kg) | [Anlage](https://www.gesetze-im-internet.de/co2kostaufg/anlage.html), [§ 5 CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/__5.html) |
| CO2-Kosten Nichtwohngebäude | Der Mieter trägt höchstens die Hälfte | [§ 8 CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/__8.html) |
| Neue Gas-, Öl- oder Flüssiggasheizung im Bestand | Vermieter und Mieter tragen je die Hälfte der Gasnetzentgelte und der CO2-Kosten ab 01.01.2028 und der Kosten des Pflichtanteils an Bio-Brennstoff ab 01.01.2029, dies für höchstens 30 % des verbrauchten Brennstoffs | [§ 5a CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/__5a.html) |
| Dieselbe Teilung im Neubau | Für Gebäude, die bis 31.12.2029 neu errichtet und erstmals genutzt werden; nicht bei Bauantrag vor dem 13.05.2026 | [§ 5b CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/__5b.html) |
| Härtefall | Es bleibt beim Stufenmodell, wenn zugleich gilt: kein angespannter Wohnungsmarkt, Miete unter 85 % der Vergleichsmiete, höchstens sechs vermietete Wohnungen, Effizienzklasse G oder H, persönliche Härte. In angespannten Märkten nur in zwei Fallgruppen und bei einer Miete unter 70 % | [§ 5d CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/__5d.html) |

### B.3 Steuern

| Regel | Inhalt | Fundstelle | Fassung |
|---|---|---|---|
| Körperschaftsteuer | 15 % bis Veranlagungszeitraum 2027; 14 % (2028), 13 % (2029), 12 % (2030), 11 % (2031), 10 % ab 2032; Solidaritätszuschlag 5,5 % der Steuer | [§ 23 KStG](https://www.gesetze-im-internet.de/kstg_1977/__23.html); [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html) | 04.02.2026 |
| Gewerbesteuer | Messzahl 3,5 %; Mindesthebesatz 280 %, erstmals für den Erhebungszeitraum 2027; Hinzurechnung eines Viertels der Finanzierungsentgelte über 200.000 € | [§ 11](https://www.gesetze-im-internet.de/gewstg/__11.html), [§ 16](https://www.gesetze-im-internet.de/gewstg/__16.html), [§ 36](https://www.gesetze-im-internet.de/gewstg/__36.html), [§ 8 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html) | 29.06.2026 |
| Erweiterte Grundstückskürzung | Auf Antrag; unschädlich sind Stromeinnahmen bis 20 % und sonstige Mieterleistungen bis 5 % der Einnahmen aus der Gebrauchsüberlassung | [§ 9 Nr. 1 GewStG](https://www.gesetze-im-internet.de/gewstg/__9.html) | 29.06.2026 |
| Zinsschranke | Freigrenze unter 3 Mio. € Nettozinsaufwand; sonst Abzug bis 30 % des verrechenbaren EBITDA; EBITDA-Vortrag fünf Jahre, Zinsvortrag unbefristet | [§ 4h EStG](https://www.gesetze-im-internet.de/estg/__4h.html); [§ 8a KStG](https://www.gesetze-im-internet.de/kstg_1977/__8a.html) | 15.10.2026 |
| Verlustvortrag | 1 Mio. € unbeschränkt, darüber 70 % (Einkommen- und Körperschaftsteuer) oder 60 % (Gewerbesteuer). Eine Rückkehr von 70 % auf 60 % ab 2028 ist im geltenden Text nicht ablesbar | [§ 10d EStG](https://www.gesetze-im-internet.de/estg/__10d.html); [§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html) | 15.10.2026 |
| Gebäudeabschreibung | Linear 3 % (Fertigstellung nach 31.12.2022), 2 % (1925–2022), 2,5 % (vor 1925); degressiv 5 % vom Restwert für Wohngebäude mit Baubeginn oder Kaufvertrag nach 30.09.2023 und vor 01.10.2029 | [§ 7 EStG](https://www.gesetze-im-internet.de/estg/__7.html) | 15.10.2026 |
| Sonderabschreibung Mietwohnungsneubau | Bis 5 % jährlich in vier Jahren; Bauantrag vor 01.10.2029; Effizienzhaus 40 mit Qualitätssiegel Nachhaltiges Gebäude; Baukostenobergrenze 5.200 €/m², Bemessungsgrundlage höchstens 4.000 €/m²; zehn Jahre Vermietung zu Wohnzwecken | [§ 7b Abs. 1 bis 4 EStG](https://www.gesetze-im-internet.de/estg/__7b.html) | 15.10.2026 |
| Sonderabschreibung, Beihilfebindung | Für Anspruchsberechtigte mit Einkünften aus Land- und Forstwirtschaft, Gewerbebetrieb oder selbständiger Arbeit nur, soweit die De-minimis-Verordnung (EU) 2023/2831 eingehalten und nachgewiesen ist | [§ 7b Abs. 5 EStG](https://www.gesetze-im-internet.de/estg/__7b.html) | 15.10.2026 |
| Sanierungsgebiet, Denkmal | Acht Jahre bis 9 %, vier Jahre bis 7 %; nur soweit nicht durch Zuschüsse gedeckt | [§ 7h](https://www.gesetze-im-internet.de/estg/__7h.html), [§ 7i EStG](https://www.gesetze-im-internet.de/estg/__7i.html) | 15.10.2026 |
| Anschaffungsnahe Herstellungskosten | Instandsetzung über 15 % der Gebäude-Anschaffungskosten (netto) binnen drei Jahren | [§ 6 Abs. 1 Nr. 1a EStG](https://www.gesetze-im-internet.de/estg/__6.html) | 15.10.2026 |
| Privater Verkauf | Steuerpflicht bei höchstens zehn Jahren Haltedauer; abgezogene Abschreibungen mindern die Anschaffungskosten | [§ 23 EStG](https://www.gesetze-im-internet.de/estg/__23.html) | 15.10.2026 |
| Vermietungsgenossenschaft | Die Befreiung entfällt bei über 10 % sonstiger Einnahmen; 30 % bei Mieterstrom | [§ 5 Abs. 1 Nr. 10 KStG](https://www.gesetze-im-internet.de/kstg_1977/__5.html) | 04.02.2026 |
| Wohngemeinnützigkeit | Vergünstigte Überlassung an Hilfebedürftige; Bezüge höchstens das Fünf- oder Sechsfache des Regelsatzes; Prüfung bei Mietbeginn | [§ 52 Abs. 2 Satz 1 Nr. 27 AO](https://www.gesetze-im-internet.de/ao_1977/__52.html) | 22.10.2026 |
| Umsatzsteuer | Vermietung steuerfrei; Option nur, soweit der Mieter ausschließlich vorsteuerunschädliche Umsätze ausführt; Berichtigungszeitraum der Vorsteuer zehn Jahre, je Jahr ein Zehntel | [§ 4 Nr. 12](https://www.gesetze-im-internet.de/ustg_1980/__4.html), [§ 9](https://www.gesetze-im-internet.de/ustg_1980/__9.html), [§ 15a UStG](https://www.gesetze-im-internet.de/ustg_1980/__15a.html) | 29.06.2026 |
| Grunderwerbsteuer | Bundessatz 3,5 %; die Ländersätze beruhen auf Landesrecht | [§ 11 GrEStG](https://www.gesetze-im-internet.de/grestg_1983/__11.html) | 29.06.2026 |

### B.4 Bewirtschaftung, Bewertung und Bauträgerraten

| Regel | Inhalt | Fundstelle | Fassung |
|---|---|---|---|
| Kostenmiete: Beträge der Verordnung, Preisstand 2002 | Verwaltung höchstens 230 € je Wohnung; Instandhaltung höchstens 7,10 / 9,00 / 11,50 €/m² nach Alter des Gebäudes; Mietausfallwagnis höchstens 2 %; Anpassung alle drei Jahre nach dem Verbraucherpreisindex. Diese Beträge sind nicht die heute anzusetzenden | [§ 26](https://www.gesetze-im-internet.de/bvo_2/__26.html), [§ 28](https://www.gesetze-im-internet.de/bvo_2/__28.html), [§ 29 II. BV](https://www.gesetze-im-internet.de/bvo_2/__29.html) | 23.11.2007 |
| Kostenmiete: anzusetzende Beträge seit 01.01.2026 | Verwaltung 372,46 € je Wohnung; Instandhaltung 11,50 / 14,58 / 18,62 €/m². Die Beträge stehen nicht im Verordnungstext; sie stammen aus einer Sekundärquelle und passen rechnerisch zu den Beträgen der Verordnung | [Haufe](https://www.haufe.de/immobilien/verwaltung/erhoehung-der-kostenmiete-bei-sozialwohnungen_258_392374.html) | am Original nachzuziehen |
| Bewirtschaftungskosten in der Wertermittlung | Werte der Verordnung für 2021: Verwaltung 298 € je Wohnung, Instandhaltung 11,70 €/m², Mietausfallwagnis 2 %; Gewerbe: Verwaltung 3 %, Mietausfallwagnis 4 % des Rohertrags. Jährliche Fortschreibung nach dem Verbraucherpreisindex; die Werte für 2026 stehen nicht in der Verordnung. Ein Liegenschaftszins darf nur mit diesen Modellansätzen kombiniert werden | [Anlage 3 ImmoWertV](https://www.gesetze-im-internet.de/immowertv_2022/anlage_3.html); [IVD](https://ivd.net/wp-content/uploads/2025/12/2026_Liegenschaftszinsaetze_.pdf) | 14.07.2021 |
| Beleihungswert | Mindestens 15 % Bewirtschaftungskosten; Korridor des Kapitalisierungszinses Wohnen 3,5–5,5 %, Gewerbe 4,5–6,5 %; den jeweils geltenden Mindestsatz gibt die BaFin bekannt; Pfandbriefdeckung bis 60 % | [§ 11](https://www.gesetze-im-internet.de/belwertv/__11.html), [§ 12 BelWertV](https://www.gesetze-im-internet.de/belwertv/__12.html); [§ 14 PfandBG](https://www.gesetze-im-internet.de/pfandbg/__14.html) | 04.10.2022; 25.03.2026 |
| Bauträgerraten: Zahl und Höhe | Höchstens sieben Teilbeträge insgesamt, entsprechend dem Bauablauf. Sie werden aus 13 Vomhundertsätzen zusammengesetzt: 30 % der Vertragssumme nach Beginn der Erdarbeiten (Erbbaurecht 20 %) und zwölf Sätze auf die restliche Vertragssumme, von 40 % nach Rohbaufertigstellung bis 5 % nach vollständiger Fertigstellung. Entfallende Leistungen werden anteilig auf die übrigen Raten verteilt | [§ 3 Abs. 2 MaBV](https://www.gesetze-im-internet.de/gewo_34cdv/__3.html) | 28.07.2026 |
| Bauträgerraten: Voraussetzungen | Zahlungen erst, wenn der Vertrag wirksam, die Vormerkung eingetragen, die Lastenfreistellung gesichert und die Baugenehmigung erteilt ist; bei genehmigungsfreien Vorhaben einen Monat nach Zugang der Bestätigung, dass gebaut werden darf. Ersatzweise Sicherheitsleistung. Abschlagszahlungen kann der Bauträger nur in diesem Rahmen verlangen | [§ 3 Abs. 1](https://www.gesetze-im-internet.de/gewo_34cdv/__3.html), [§ 7 MaBV](https://www.gesetze-im-internet.de/gewo_34cdv/__7.html); [§ 650v BGB](https://www.gesetze-im-internet.de/bgb/__650v.html) | 28.07.2026; 23.07.2026 |

## Anhang C: Förderkonditionen mit Stand und Quelle

Quellen der NBank-Zeilen: [RL Mietwohnraum 2026](https://www.nbank.de/medien/nb-media/Downloads/Rechtliche-Grundlagen/Richtlinien/Richtlinie-F%C3%B6rderung-von-Mietwohnraum-%28RL-Mietwohnraum-2026%29.pdf), Runderlass vom 25.06.2026, in Kraft seit 01.07.2026, und die jeweilige Produktinformation. KfW-Zinsen: [Zinsdatensatz](https://www.kfw.de/zinsen/alle.rates), gültig ab 18.11.2026.

### C.1 NBank (Niedersachsen)

| Programm und Gegenstand | Konditionen | Stand und Quelle |
|---|---|---|
| Mietwohnungen in Mehrfamilienhäusern: Förderhöhe | Darlehen bis 40 / 60 / 70 % und Zuschuss bis 40 / 20 / 10 % der zuwendungsfähigen Kosten (Einkommensgruppen A / B / C); Eigenkapital mindestens 20 % | Richtlinie Nr. 5.2.6 und 5.3.3 |
| Mietwohnungen: Darlehen | Zins 0 % für 35 Jahre, danach bis Basiszins plus 3 Prozentpunkte; Rückzahlung binnen 42 Jahren; Verwaltungskostenbeitrag 0,5 % jährlich auf die Restschuld | Richtlinie Nr. 5.3.4, 5.3.5, 12.7 |
| Mietwohnungen: Entgelt und Auszahlung | Entgelt 1 % des Darlehens und 0,75 % des Zuschusses; Auszahlung 30 / 30 / 30 / 10 % nach Baufortschritt | Richtlinie Nr. 5.5.3, 12.7 |
| Mietwohnungen: Bemessungsgrenze | Herstellungskosten bis 5.250 €/m² (Mietenstufe I–III) oder 5.460 €/m² (IV–VII) seit 01.10.2026; halbjährlich indexiert | [Produktinformation](https://www.nbank.de/medien/nb-media/Downloads/Programminformation/Produktinformationen/Produktinformation-Mietwohnungen-in-Mehrfamilienh%C3%A4usern-%28NB-AuE-EE%29.pdf), Stand 05.11.2026 |
| Mietwohnungen: Miete und Bindung | Eingangsmiete 6,50 / 7,90 / 8,70 €/m² (I–III) oder 6,80 / 8,20 / 9,00 €/m² (IV–VII); drei Jahre fest, danach höchstens 6,15 % in drei Jahren; bis 0,30 €/m² Zuschlag ab Effizienzhaus 40; Bindung 35 Jahre | Produktinformation, Stand 05.11.2026 |
| Energetisch hochwertiger Neubau | Reiner Zuschuss bis 50 / 40 / 30 %, höchstens 90.000 / 75.000 / 60.000 € je Wohneinheit; mindestens Effizienzhaus 40; nicht mit dem Hauptprogramm kumulierbar | [Produktinformation](https://www.nbank.de/medien/nb-media/Downloads/Programminformation/Produktinformationen/Produktinformation-Energetisch-hochwertiger-Mietwohnungsneubau-in-Mehrfamilienh%C3%A4usern.pdf), Stand 10.07.2026 |
| Klimagerechte Modernisierung | Zuschuss je Wohnung nach Sprung der Effizienzklasse: 25 / 20 / 10 % bei zwei Klassen bis 40 / 35 / 25 % ab fünf Klassen; Höchstbeträge 9.000 bis 31.000 €; Bindung 25 Jahre | [Produktinformation](https://www.nbank.de/medien/nb-media/Downloads/Programminformation/Produktinformationen/Produktinformation-Modernisierung-von-Mietwohnraum.pdf), Stand 10.07.2026 |

Als Orientierung für die Einkommensgruppen nennt der Rechner der NBank 31.586 Euro Bruttojahreseinkommen für eine Person in der Basisstufe ([NBank Einkommensermittlung](https://www.nbank.de/F%C3%B6rderprogramme/Einkommensermittlung.html)).

### C.2 KfW und BAFA (Bund)

| Programm und Gegenstand | Konditionen | Stand und Quelle |
|---|---|---|
| KfW 261 BEG Wohngebäude: Förderung | Kredit 150.000 € je Wohneinheit; Tilgungszuschuss Effizienzhaus 40 EE 10 %, 55 EE 5 %, 70 und 85 EE 0 %; plus 5 Punkte Nachhaltigkeitsklasse, plus 10 schlechtestes Gebäude, plus 15 serielle Sanierung (bei Effizienzhaus 70 plus 5); öffentliche Zuschüsse zusammen höchstens 60 % | [Merkblatt](https://www.kfw.de/PDF/Download-Center/F%C3%B6rderprogramme-%28Inlandsf%C3%B6rderung%29/PDF-Dokumente/6000004854_M_261.pdf), Stand 09/2026, gültig ab 24.09.2026 |
| KfW 261: Zins | Sollzins 3,01 % (Laufzeit 10 Jahre) bis 3,65 % (30 Jahre) | Zinsdatensatz |
| KfW 297/298 Klimafreundlicher Neubau: Förderung | 100.000 € je Wohneinheit, mit Qualitätssiegel Nachhaltiges Gebäude 150.000 €; Stufe Effizienzhaus 55 mit 100.000 €, befristet längstens bis 31.12.2026 | [Merkblatt](https://www.kfw.de/PDF/Download-Center/F%C3%B6rderprogramme-%28Inlandsf%C3%B6rderung%29/PDF-Dokumente/6000005051_M_297_298.pdf), Stand 07/2026, gültig ab 30.07.2026 |
| KfW 297/298: Zins | Stufe Effizienzhaus 40: 1,83 % (Laufzeit 10 Jahre) bis 2,79 % (35 Jahre); Stufe Effizienzhaus 55 ab 1,00 % | Zinsdatensatz |
| KfW 296 Neubau im Niedrigpreissegment | 100.000 € je Wohneinheit; Sollzins 0,01 % (Laufzeit 10 Jahre) bis 1,45 % (35 Jahre) | [Merkblatt](https://www.kfw.de/PDF/Download-Center/F%C3%B6rderprogramme-%28Inlandsf%C3%B6rderung%29/PDF-Dokumente/6000005195_M_296.pdf), Stand 06/2026; Zinsdatensatz |
| KfW 458 Heizungsförderung: Sätze | 30 % Grundförderung; 16 % Klimageschwindigkeitsbonus, ab 01.02.2027 halbjährlich um 4 Punkte sinkend; Einkommensbonus bis 40 %; Obergrenze 70 %, für Selbstnutzer mit Einkommen bis 30.000 € 80 % | [Merkblatt](https://www.kfw.de/PDF/Download-Center/F%C3%B6rderprogramme-%28Inlandsf%C3%B6rderung%29/PDF-Dokumente/6000005131_M_458.pdf), Stand 09/2026, gültig ab 24.09.2026 |
| KfW 458: förderfähige Kosten | 28.000 € (erste Wohneinheit), 15.000 € (zweite bis sechste), 8.000 € (weitere) | wie vor |
| KfW 266 Gewerbe zu Wohnen | Zuschuss 30 % auf höchstens 100.000 € je entstehender Wohneinheit; Antrag bis 31.12.2026; De-minimis-Beihilfe | [Merkblatt](https://www.kfw.de/PDF/Download-Center/F%C3%B6rderprogramme-%28Inlandsf%C3%B6rderung%29/PDF-Dokumente/6000005303_M_266.pdf), Stand 07/2026 |
| BAFA BEG Einzelmaßnahmen: Sätze und Kosten | 15 % für Gebäudehülle und Anlagentechnik; förderfähige Ausgaben je Kalenderjahr 30.000 € (erste Wohneinheit), 15.000 € (zweite bis sechste), 8.000 € (ab siebter) | [Richtlinie vom 17.07.2026](https://www.energiewechsel.de/KAENEF/Redaktion/DE/PDF-Anlagen/BEG/beg-richtlinien-juli-2026/20260720-beg-einzelmassnahmen.pdf?__blob=publicationFile&v=5); [BAFA-Merkblatt](https://www.bafa.de/SharedDocs/Downloads/DE/Energie/beg_merkblatt_allgemein_antragstellung_neu.pdf?__blob=publicationFile&v=17), Version 1.14 vom 19.10.2026 |
| BAFA BEG Einzelmaßnahmen: Sanierungsfahrplan und Kumulierung | Mit Sanierungsfahrplan förderfähige Ausgaben 60.000 / 30.000 / 15.000 €; Bonus von 5 Punkten nur auf den Teil oberhalb der Grenze ohne Fahrplan; Kumulierung höchstens 60 %, für Kommunen 90 % | wie vor |
