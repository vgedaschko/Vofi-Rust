# Spezifikation – VOFI-Immobilienkalkulation

Das maßgebliche Entwicklungsdokument. Es beschreibt, was gebaut wird und warum, und wird laufend fortgeschrieben. Wer am Projekt arbeitet, liest es zuerst; was hier steht, gilt, bis es hier geändert wird. Wie es zu den übrigen Dokumenten steht, zeigt die Übersicht in `docs/README.md`. Leser: Entwicklung und Prüfer; der Auftraggeber erhält Entscheidungsbedarf im Gespräch und in `TASKS.md`.

**Stand:** 2026-11-18 · Konzeptphase, noch kein Code

## Wie dieses Dokument gepflegt wird

- **Erst die Spezifikation, dann die Umsetzung.** Soll etwas anders gebaut werden als hier beschrieben, wird zuerst dieser Text geändert und die Änderung im Entscheidungsprotokoll (`docs/entscheidungen.md`) begründet.
- **Jede Festlegung trägt einen Status:** **fest** (entschieden, Änderung nur mit Protokolleintrag) · **vorläufig** (Arbeitsstand, wird im jeweiligen Kapitel ausgearbeitet) · **offen** (noch zu klären, mit Zuständigkeit). Ruht eine Festlegung auf einer ungeklärten Annahme über Recht, Förderpraxis oder Methode, steht deren Kennung dabei (zum Beispiel `MA-001`); siehe Kapitel 8.
- **Prüfbefunde fließen ein, wenn sie tragen.** Nach jeder Prüfrunde wird geprüft, ob ein übernommener Befund eine Festlegung berührt; dann wird sie hier angepasst.
- **Annahmen dürfen fallen.** Eine frühere Festlegung zu ändern ist kein Fehler, solange Grund und Datum im Protokoll stehen und die betroffenen Kapitel nachgezogen sind.
- **Soll, nicht Ist.** Sobald ein Teil gebaut und abgenommen ist, beschreibt ihn die Anwendungsdokumentation; hier bleibt ein Verweis.
- **Kein Wunschzettel.** Hier steht nur, was beschlossen oder als Arbeitsstand gewollt ist. Ideen ohne Entscheidung gehören in `TASKS.md`.

## 1 Zweck und Rahmen

| Thema | Festlegung | Status |
|---|---|---|
| Zweck | Web-Anwendung zur Immobilien-Investitionsrechnung nach der VOFI-Methode (Vollständiger Finanzplan) mit Fördermodulen, Risikoanalyse, Projektübersicht und Mehrbenutzerbetrieb | fest |
| Nutzerkreis | Eigenes Unternehmen und Beratung für Kunden (Berichte, später Lesezugang). Kein Verkauf als Softwareprodukt | fest |
| Vorhabensarten | Ankauf Bestand · Neubau zur Vermietung · Sanierung im Bestand · Entwicklung mit Verkauf | fest |
| Nutzungsarten | Frei finanziertes Wohnen · geförderter Wohnungsbau · Gewerbe/Mixed-Use · Sonderimmobilien | fest |
| Investorensichten | Kapitalgesellschaft · Privatperson und vermögensverwaltende Personengesellschaft · steuerbefreite, kommunale und genossenschaftliche Unternehmen | fest |
| Steuerstatus | Eigenes Merkmal neben der Investorensicht: Die Rechtsform bestimmt nicht die Steuerpflicht (eine kommunale Wohnungs-GmbH ist steuerpflichtig, eine Vermietungsgenossenschaft nur unter Bedingungen befreit). Zu den Ausprägungen gehören auch die gewerblich geprägte Personengesellschaft, typisch die GmbH & Co. KG, und das Einzelunternehmen mit Betriebsvermögen; bei beiden ist der Verkaufsgewinn unabhängig von der Haltedauer steuerpflichtig (`ESTG-15`). Ob Anlaufverluste sofort verrechnet oder im Vorhaben vorgetragen werden, ist ein Merkmal je Vorhaben (`MA-016`) | fest |
| Regionaler Schwerpunkt | Deutschland, Förderlogik zuerst für Niedersachsen (NBank) und Bund (KfW, BAFA) | fest |
| Fachliche Grundlage | Lehrbuch-VOFI (Grob; Schulte/Ropeter), Branchenrichtlinien, geltendes Recht mit Quelle und Stand. Keine eigene Excel-Vorlage; die älteren Repositories `VoFi` und `NBank` werden nicht herangezogen | fest |
| Qualitätsanspruch | 9 von 10 nach den Maßstäben in `CLAUDE.md` | fest |
| Begründung des Eigenbaus | Eigener Bedarf in Kalkulation und Beratung. Eine bezifferte Wirtschaftlichkeitsrechnung gegenüber Kauf und Excel-Ausbau steht aus | offen – Vorstudie, braucht Mengengerüst des Auftraggebers |

## 2 Funktionsumfang und Ausbaustufen

Grundlage ist der Recherchebericht (`reports/VOFI Immobiliensoftware Marktrecherche.md`). Pflichtumfang und Zuschnitt stehen dort in Abschnitt 5 und Anhang D; sie werden als Anforderungen hierher übernommen, sobald der Bericht die Prüfrunden bestanden hat und der Auftraggeber den Zuschnitt freigegeben hat.

| Thema | Festlegung | Status |
|---|---|---|
| Reihenfolge | Stufe 1 Wohnen in Niedersachsen (Neubau zur Vermietung, Ankauf Bestand; frei finanziert und gefördert) · Stufe 2 Sanierung im Bestand und Simulation · Stufe 3 Entwicklung mit Verkauf, Gewerbe · Stufe 4 Sonderimmobilien, Unternehmensebene | vorläufig – Umsatzsteueroption in Stufe 3: `MA-011` |
| Teilschritte der Stufe 1 | Vier Teilschritte: 1a Grobkalkulation für beide Vorhabensarten · 1b-1 Vollkalkulation Ankauf Bestand · 1b-2 Vollkalkulation Neubau · 1c Förderung in voller Tiefe mit Förderantrag, geteilt in einen Förderteil und einen Bestandsteil, der 1b-1 voraussetzt. Gremien- und Bankvorlage kommen mit dem zuerst gebauten Teilschritt der Vollkalkulation. Jeder Teilschritt ist für sich nutzbar und hat eine eigene Freigabe. Die Reihenfolge von 1b-1, 1b-2 und 1c richtet sich nach dem Mengengerüst: Ist der geförderte Neubau das Hauptgeschäft, rücken 1b-2 und der Förderteil von 1c nach vorn. Einzelheiten: Bericht, Abschnitt 5 und Anhang D | vorläufig – bis zur Freigabe des Zuschnitts durch den Auftraggeber |
| Erbbaurecht | In der Grobkalkulation ist der Erbbauzins eine eigene Eingabe mit Indexierung, ab der Vollkalkulation eine frei benennbare Position; das volle Modell folgt in Stufe 3 | vorläufig – Fachfrage an den Auftraggeber, ob es vorgezogen werden muss |
| Arbeitsablauf | Das Werkzeug trägt den Weg von der Grobkalkulation mit wenigen Eingaben über die Verfeinerung bis zur Gremien-, Bank- und Förderantragsunterlage. Eine frühe Phase mit wenigen Eingaben gehört in Stufe 1 | fest |
| Vollständigkeit je Vorhabensart | Eine Vorhabensart kommt erst in eine Stufe, wenn sie dort vollständig rechenbar ist (bei Ankauf Bestand also mit Bewirtschaftung, Instandhaltung, Kaufpreisaufteilung und CO2-Kosten nach `CO2KOSTAUFG-5` bis `CO2KOSTAUFG-5D`) | fest |
| Kennzahlen | VOFI-Kennzahlen und die international üblichen Größen nebeneinander; ein festes Kennzahlenblatt je Vorhabensart. Führende Entscheidungsgröße ist die Endwertdifferenz zur Unterlassensalternative, weil sie anders als die Rendite nicht davon abhängt, in welchem Monat Einlagen und Entnahmen fallen; die Rendite steht daneben (`MA-012`) | fest |
| Zielrendite und Schwellen | Zielrendite, Stresshöhen, Beleihungsquote, Mindestdeckung des Schuldendienstes und Warnschwellen sind Vorgaben des Hauses aus dem Katalog. Der kombinierte Stressfall rechnet mit ermäßigten Höhen und nur den Größen, die bei der Vorhabensart wirken. Im Projekt dürfen Stresshöhen nur verschärft werden; eine abweichende Zielrendite braucht eine Begründung und steht sichtbar auf dem Kennzahlenblatt | fest – Werte gibt der Auftraggeber frei |
| Entscheidungspunkte | Vor jeder Stufe eine Freigabe durch den Auftraggeber mit vorher benannten Abbruchkriterien. Der erste Freigabepunkt ist die Vorprüfung vor Beginn der Phase 2: Gespräch mit der NBank, Anwendergespräche, Herstellervorführungen und Katalogverantwortung müssen dann vorliegen. Die Schwellen der Vorprüfung gibt der Auftraggeber frei, bevor die Anwendergespräche beginnen: Bedarf allgemein (Mehrheit würde die Grobkalkulation statt Excel nutzen; sonst Abbruch), Bedarf, der nur den Eigenbau trägt (Mehrheit braucht Änderungsprotokoll, Arbeit mehrerer Personen oder Berichte und Zugang für Kunden; sonst Umsteuern auf den Vergleich von Kauf und Excel-Ausbau) und Mindestfallzahl (Vorschlag: Die Zeitersparnis über zehn Jahre deckt mindestens den Lizenzpreis des günstigsten vorgeführten Produkts) | fest (Schwellenwerte: Freigabe des Auftraggebers offen) |
| Erster Teilschritt | Der erste Teilschritt der Stufe 1 enthält nur, was für eine belegbare Grobkalkulation nötig ist: Änderungsprotokoll, Anmeldung, Projektzuweisung mit einfacher Rollenunterscheidung, benannter Arbeitsstand. Präsenzanzeige und das volle Rollenmodell mit Freigaben folgen im zweiten Teilschritt | fest |
| Grobkalkulation | Der höchste tragbare Kaufpreis ist der Preis, bei dem die VOFI-Rendite nach Steuern die Zielrendite erreicht – gerechnet mit dem Darlehen, das die Bank gibt. Das Bankdarlehen ist der kleinere Wert aus Beleihungsquote mal Wertansatz und dem Darlehen, dessen Schuldendienst die Mindestdeckung im ersten Jahr der Vollvermietung einhält (Rechengrundlage: `MA-026`); das nötige Eigenkapital wird ausgewiesen, das verfügbare Eigenkapital wirkt als freiwillige zweite Grenze, und das Blatt nennt, was bindet. Im geförderten Neubau ist das Bankdarlehen Restfinanzierung nach Förderdarlehen, Zuschuss und Eigenmitteln; die Kontrollsumme „Mittelherkunft gleich Mittelverwendung“ gilt immer. Zinsbindung ist Eingabe, der Anschlusszins Vorgabe des Hauses; der heutige Zins wird nicht still fortgeschrieben. Die Steuer in Kurzform rechnet bei Körperschaften mit dem Satz je Jahr aus dem Katalog und dem Kennzeichen „erweiterte Grundstückskürzung“ (`GEWSTG-9`), bei Personen und Personengesellschaften mit dem eingegebenen Steuersatz, bei gewerblichen Personengesellschaften und Einzelunternehmen mit Anrechnung der Gewerbesteuer (`ESTG-35`); lineare Abschreibung; der Verkaufsgewinn ist erfasst, wo der Steuerstatus es verlangt. Bei gebundenen Beständen pauschale Bindung. Das Ergebnis steht auch im kombinierten Stressfall. Zwei Fassungen lassen sich vergleichen; die Zielwertsuche geht auf die dafür gekennzeichneten Eingaben und meldet alle Lösungen oder „keine Lösung“. Bei Förderung ist der Bodenrichtwert Pflichteingabe, weil er die zuwendungsfähigen Grundstückskosten begrenzt | fest |

## 3 Rechenkern

Die vollständige Fachspezifikation (Tabellenaufbau, Rechenreihenfolge, Formeln, Konventionen) entsteht als eigenes Kapitel aus dem Anhang des Berichts und den beiden finanzmathematischen Prüfberichten. Bis dahin gelten diese Leitlinien:

| Thema | Festlegung | Status |
|---|---|---|
| Methode | Periodenweise Tabellenrechnung mit expliziten Konten für Eigenkapital, jede Kredittranche, Kontokorrent, Geldanlage und Steuern; jede Periode schließt mit Finanzierungssaldo null | fest |
| Zeitraster | Intern monatlich; Jahresdarstellung als Verdichtung; zusätzlich ein Jahresmodus für den Vergleich mit Lehrbuchfällen | fest |
| Zeithorizont | Mindestens 42 Jahre abbildbar (Laufzeit der NBank-Darlehen nach `NBANK-RL-MIETWOHNRAUM-2026`), Bindungen von 35 Jahren vollständig | fest – Zins ab dem 36. Jahr: `MA-003` |
| Konventionen | Je Zahlungsart sind Basisperiode der Indexierung, Zahlungszeitpunkt, Steuermonat und Verzinsungstakt ausdrücklich festgelegt und dokumentiert | fest (Inhalt: vorläufig) |
| Geldbeträge | Exakte Dezimalrechnung. Je Zahlungsart ist eine Rundungsregel festgelegt; Darlehenspläne runden je Rate kaufmännisch auf Cent, je Darlehen umstellbar, damit Restschulden mit dem Kontoauszug übereinstimmen | fest (Regeln je Zahlungsart: vorläufig) – `MA-013` |
| Ausschüttungen und Nachschüsse | Die Unterlassensalternative erhält dieselbe Einlagen- und Entnahmenreihe wie die Investition. Einlagen und Entnahmen derselben Monatsperiode werden saldiert. Im Jahresmodus wird je Jahr saldiert. Vergleichssätze sind effektive Jahreszinsen. Die Renditeformel bei mehreren Einlagen über die Laufzeit ist eindeutig festzulegen; maßgeblich für Randfälle ist ihr Zähler, nicht der Endwert allein | fest / Formel: vorläufig – `MA-012` |
| Restwert | Der Verkaufserlös wird brutto geführt. Die Restschuld wird stets als Ablösung im Finanzplan gebucht, nie als Abzug vom Verkaufserlös; ein Investitionsstau mindert den Verkaufserlös nur, soweit er nicht als Maßnahme im Finanzplan steht. Eine Kontrollsumme sichert, dass beides den Endwert nur einmal mindert. Der Verkaufsfaktor bezieht sich auf die Jahresnettokaltmiete, die Nettoanfangsrendite auf den Reinertrag im Verhältnis zu Kaufpreis plus Erwerbsnebenkosten | fest – bei laufender Bindung: `MA-017` |
| Kontrollsummen | Ergebnisse erscheinen erst, wenn alle Kontrollsummen bestanden sind; die Proben berücksichtigen Zuschüsse, Tilgungszuschüsse, Disagio und kapitalisierte Zinsen | fest |
| Randfälle | Zinssatz null, Eigenkapital null, negativer Endwert und mehrdeutiger interner Zinsfuß haben definierte Ergebnisse statt Fehlern | fest |
| Nachvollziehbarkeit | Jede Ergebniszahl lässt sich bis zur Eingabe zurückverfolgen; jede Kalkulation speichert Regelstand und Version des Rechenkerns | fest |
| Abnahmetests | Zwei veröffentlichte Rechenbeispiele des IWU (`KIRCHNER-IWU-2004`, `IWU-2013-ENDBERICHT`) und der nachgerechnete Testfall mit Varianten laufen als automatische Tests, jeder mit benannter Toleranz (eigene Fälle auf den Cent; das IWU-Beispiel von 2013 ist nur auf rund 3,40 € nachvollziehbar); weitere Fälle für Verlustvortrag, steuerpflichtigen Verkauf und Monatsraster kommen hinzu | fest – Umlage im Fall von 2013: `MA-015` |
| Offene Lehrbuchdefinitionen | VOFI-Gesamtkapitalrendite und Amortisationsdauer nach Grob sind am Original zu beschaffen; bis dahin wird die Gesamtkapitalrendite nicht ausgewiesen | offen – Literatur beschaffen |

## 4 Regel- und Förderkatalog

| Thema | Festlegung | Status |
|---|---|---|
| Grundsatz | Steuersätze, Mietrechtsregeln, Förderkonditionen und Fristen sind datierte Daten mit Quelle und Gültigkeit, niemals fest im Programm | fest |
| Fördermodul | Baukasten aus Förderkomponenten (zinsverbilligtes Darlehen, Tilgungszuschuss, Einmalzuschuss, laufender Zuschuss, steuerliche Förderung, Bürgschaft) mit Bemessung, Auszahlungsplan, Bindungen, Voraussetzungen und Kumulierungsregeln; Programme werden konfiguriert, nicht programmiert | fest |
| Kopplungen | Förderung wirkt automatisch auf Miete (Bindungen, Abzug von Drittmitteln bei Modernisierungsumlage nach `BGB-559A` und Vergleichsmietenerhöhung nach `BGB-558`), Finanzplan und Abschreibung | fest – Dauer des Abzugs: `MA-007`; zinsverbilligte Darlehen beim Heizungstausch: `MA-019` |
| Pflege | Redaktionell gepflegt mit benannter Verantwortung im Unternehmen; automatisiert höchstens bei Zinssätzen und nur mit Zustimmung der Quelle | fest / Verantwortung: offen – Auftraggeber |
| Rechtsstand | Laufende Gesetzgebung wird als Entwurfsstand geführt und kann je Kalkulation zugeschaltet werden | vorläufig |
| NBank-Renditeprüfung | Das Werkzeug weist die Eigenkapitalrendite für die Überkompensationsprüfung aus dem eigenen Finanzplan aus und bezeichnet sie als eigene Berechnung, bis die Rechenweise der NBank geklärt ist | vorläufig – `MA-001` |
| Regeln auf ungeklärter Grundlage | Ruht eine Regel des Katalogs auf einer Modellannahme, trägt der Katalogeintrag deren Kennung, und die Voreinstellung folgt Kapitel 8. Derzeit betrifft das: NBank-Förderung `MA-002`, `MA-003`, `MA-004`, `MA-005`, `MA-006`, `MA-017`, `MA-020`, `MA-021`; Mietrecht `MA-007`, `MA-008`, `MA-018`, `MA-019`, `MA-025`; Betriebskosten und Heizung `MA-009`, `MA-024`; Steuern `MA-010`, `MA-016`, `MA-022`, `MA-023`; Finanzierung `MA-026`. Inhalt, andere Lesart und Klärungsweg stehen nur im Verzeichnis (`docs/modellannahmen.md`) | fest |

## 5 Technik

Technische Entscheidungen trifft Claude; hier stehen sie mit ihrer geschäftlichen Begründung.

| Thema | Festlegung | Begründung | Status |
|---|---|---|---|
| Rechenkern | Rust, läuft unverändert auf dem Server und als WebAssembly im Browser | Eine Rechenlogik statt zwei; Bildschirm und Bericht können nicht voneinander abweichen | fest |
| Server | Rust, bewusst schlank (Anmeldung, Änderungsprotokoll, Verteilung, Exporte) | Notfalls in anderer Technik ersetzbar, ohne den Rechenkern anzufassen | fest |
| Oberfläche | TypeScript mit gepflegten Bibliotheken für Tabellen, Diagramme und Formulare | Ausgereifte Bausteine statt Eigenbau; größerer Pool an Entwicklern | fest |
| Zusammenarbeit | Gleichzeitiges Bearbeiten mit sofortiger Verteilung jeder Änderung und Anzeige, wer wo arbeitet. Ändern zwei Personen im selben Moment dasselbe Feld, gilt der spätere Wert; beide Eingaben stehen im Protokoll. Kein Zusammenführen offline bearbeiteter Kopien | Das Änderungsprotokoll, das Controlling und Revision brauchen, fällt als Nebenprodukt an; die Bausteine der aufwändigeren Variante sind unreif und binden an kleine Fremdteams | fest (ersetzt die ursprüngliche Vorgabe, siehe Protokoll) |
| Änderungsprotokoll | Jede Änderung an Annahmen mit Person, Zeit, altem und neuem Wert; Grundlage für Rückgängig, benannte Arbeitsstände und Freigaben | Nachweisbarkeit; später nicht nachrüstbar | fest |
| Rollen | Rolle je Projektmitgliedschaft (Verantwortlicher, Bearbeiter, Prüfer, Leser; später lesender Kunde); Rechte werden auf dem Server durchgesetzt | Projektzuweisung an Mitarbeiter; Kundenzugang ohne Umbau | fest |
| Mandantentrennung | Jede Tabelle trägt von Beginn an ein Mandantenkennzeichen | Kundenzugänge später ohne Umbau der Datenhaltung | fest |
| Datenhaltung und Betrieb | Eine Anwendung, eine PostgreSQL-Datenbank, Betrieb in der EU | Geringe Betriebskosten, kein Anbieterzwang | fest / Anbieter: offen |
| Personenbezogene Daten | Mieternamen und Einkommensangaben gehören nicht in das unveränderliche Änderungsprotokoll; Lösch- und Auskunftspflichten werden vor dessen Spezifikation geklärt | Datenschutz und Mitbestimmung prägen die Architektur | offen – vor Spezifikation des Protokolls |
| Simulation | Zufallsstartwert, Generator und Version werden je Lauf gespeichert; Server und Browser verwenden dieselben mathematischen Funktionen. Voreingestellte Streuungen und Korrelationen sind Schätzwerte (`MA-014`) | Wiederholbare Ergebnisse | fest |
| Excel | Import von Beginn an; Export mit Annahmenblatt und Versionsstempel, ab dem zweiten Teilschritt der Stufe 1 mit Summen- und Saldoformeln, sodass Bank und Gremium nachrechnen können | Banken und Gremien arbeiten mit Excel | fest |

## 6 Gestaltung und Bedienung

| Thema | Festlegung | Status |
|---|---|---|
| Vorgehen | Vor jedem Entwurf Vorbilder aus guten Finanz- und Tabellenanwendungen sichten und das Muster benennen, dem der Entwurf folgt | fest |
| Wettbewerb | Die prägenden Ansichten (Finanzplan-Tabelle, Eingabe der Annahmen, Kennzahlenblatt mit Bericht) entstehen im Design-Wettbewerb: mindestens fünf Entwürfe in zugewiesenen, verschiedenen Richtungen, mit echten Zahlen, verdeckt bewertet; der Auftraggeber entscheidet unter den besten | fest |
| Werkzeug und Prüfung | Jede Gestaltungsarbeit beginnt mit dem Skill `frontend-design`. Jede Änderung an Oberflächendateien durchläuft vor dem Stopp die Gestaltungsprüfung am gerenderten Ergebnis (Designkritik, Barrierefreiheit); ein Hook hält den Stopp einmal auf und nennt, was fehlt | fest |
| Bausteine | Gepflegte Bibliotheken für Standardelemente; Eigenbau nur für das Fachliche (VOFI-Tabelle, Förderlogik) | fest |
| Auftreten | Produkt, Kundenberichte und Exporte ohne Hinweisflut; Hinweise nur bei fachlicher, technischer oder rechtlicher Bedeutung, einmal und an der Stelle, an der sie gebraucht werden | fest |
| Berichte und Diagramme | Nach IBCS; deutsche Zahl- und Datumsformate | fest |
| Gestaltungssystem | Farben, Typografie, Raster, Bausteinbibliothek | offen – mit dem ersten Oberflächenentwurf |

## 7 Rechtlicher Rahmen des Werkzeugs

Vor dem Einsatz bei Kunden mit Anwalt und Steuerberater zu klären; bis dahin sind diese Punkte Planungsannahmen.

| Thema | Arbeitsstand | Status |
|---|---|---|
| Abgrenzung zur Rechts- und Steuerberatung | Kundenberichte stellen Rechenergebnisse unter benannten Annahmen dar und ersetzen keine Einzelfallprüfung; wo die Grenze liegt, klärt der Anwalt | offen – Anwalt |
| Haftung | Aussagen in Kundenberichten sind so zu fassen, dass sie nicht als Zusicherung verstanden werden; Haftungsregelung im Beratungsvertrag | offen – Anwalt |
| Beihilferecht | De-minimis-Konto je Unternehmensgruppe (`EU-DE-MINIMIS-2023-2831`) und Überkompensationsprüfung als Regelarten im Katalog | vorläufig |
| Nutzungsrechte | Lizenzen für Normen, Kostenkennwerte und fremde Datenquellen vor deren Einbindung klären | offen |
| Mitbestimmung | Änderungsprotokoll und Präsenzanzeige können mitbestimmungspflichtig sein | offen – Auftraggeber |

## 8 Modellannahmen

Manches lässt sich vor dem Bau nicht klären: eine Bank legt ihre Rechenweise nicht offen, ein Gesetz lässt eine Frage offen, ein Lehrbuch definiert einen Fall nicht. Das Modell muss trotzdem rechnen. Damit solche Setzungen nicht unsichtbar im Programm verschwinden, gilt diese Konvention.

**Was eine Modellannahme ist.** Eine Annahme über die Außenwelt – Recht, Förderpraxis, Bankpraxis, Methode –, die sich als falsch herausstellen kann und auf der ein Ergebnis beruht. Sie ist zu unterscheiden von der Festlegung (wir entscheiden, wie wir bauen; steht in dieser Spezifikation), von der Eingabe des Anwenders (seine Annahme zum Vorhaben, etwa die Mietsteigerung) und von der ungeprüften Quelle (der Wert steht fest, wurde aber noch nicht am Original gelesen; steht im Quellenkataster).

| Regel | Inhalt | Status |
|---|---|---|
| Verzeichnis | Jede Modellannahme steht mit Kennung `MA-000` im Verzeichnis `docs/modellannahmen.md` (Daten: `docs/modellannahmen/annahmen.toml`): was angenommen wird, warum es offen ist, die andere Lesart, Grundlage mit Quellenkennungen, Gewicht und Wirkung, wer klären kann, Wiedervorlage | fest |
| Kennzeichnung | Wo eine Annahme wirkt, steht ihre Kennung: in Spezifikation und Fachhandbuch an der betroffenen Regel, im Regel- und Förderkatalog am Datensatz, im Code an der umsetzenden Stelle und an den Tests, die von ihr abhängen. Eine Kennung, die im Verzeichnis fehlt, lässt die Prüfung scheitern | fest |
| Vorsicht | Voreingestellt ist die Lesart, die das Vorhaben ungünstiger rechnet. Ausnahmen werden im Verzeichnis begründet | fest |
| Umschaltbar | Annahmen mit hohem oder mittlerem Gewicht werden nach Möglichkeit als Einstellung gebaut, sodass die andere Lesart ohne Programmänderung gewählt und in der Sensitivität gegenübergestellt werden kann | fest |
| Mitgeführt im Ergebnis | Der Rechenkern gibt mit jedem Ergebnis die Liste der Annahmen zurück, die in dieser Kalkulation tatsächlich gewirkt haben. Angezeigt wird nur, was gewirkt hat | fest |
| Sichtbarkeit | Drei Stufen: **Kundenbericht** – steht im Annahmenblatt des Berichts, einmal, in einem Satz, mit der Wirkung; **Anwendung** – am betroffenen Ergebnis abrufbar und in internen Berichten; **nur intern** – in den Entwicklungsunterlagen. Annahmen mit hohem Gewicht sind nie nur intern. Das Annahmenblatt ist der eine Ort für solche Hinweise; sie werden nicht über den Bericht verstreut | fest |
| Auflösung | Wird eine Annahme geklärt, erhält sie den Status bestätigt (mit Quelle im Quellenkataster) oder widerlegt. Bei widerlegt werden Spezifikation, Katalog und Code geändert, das Entscheidungsprotokoll ergänzt und die Änderungshistorie nennt, welche Ergebnisse sich ändern. Kennungen bleiben bestehen und werden nie neu vergeben | fest |
| Wiedervorlage | Offene Annahmen werden an jedem Freigabepunkt durchgesehen; vor dem Kundeneinsatz darf keine Annahme mit hohem Gewicht ohne ausdrückliche Freigabe des Auftraggebers offen sein | fest |

## 9 Offene Punkte beim Auftraggeber

Offene Punkte beim Auftraggeber führt allein `TASKS.md` im Abschnitt „Wartet auf Nutzer“. Hier steht nur, welche Festlegung an welcher Antwort hängt: Zeilen mit dem Status „vorläufig“ oder „offen“ nennen die Frage, von der sie abhängen.
