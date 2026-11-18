# Spezifikation – VOFI-Immobilienkalkulation

Das maßgebliche Entwicklungsdokument. Es beschreibt, was gebaut wird und warum, und wird laufend fortgeschrieben. Wer am Projekt arbeitet, liest es zuerst; was hier steht, gilt, bis es hier geändert wird. Wie es zu den übrigen Dokumenten steht, zeigt die Übersicht in `docs/README.md`.

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
| Steuerstatus | Eigenes Merkmal neben der Investorensicht: Die Rechtsform bestimmt nicht die Steuerpflicht (eine kommunale Wohnungs-GmbH ist steuerpflichtig, eine Vermietungsgenossenschaft nur unter Bedingungen befreit) | fest |
| Regionaler Schwerpunkt | Deutschland, Förderlogik zuerst für Niedersachsen (NBank) und Bund (KfW, BAFA) | fest |
| Fachliche Grundlage | Lehrbuch-VOFI (Grob; Schulte/Ropeter), Branchenrichtlinien, geltendes Recht mit Quelle und Stand. Keine eigene Excel-Vorlage; die älteren Repositories `VoFi` und `NBank` werden nicht herangezogen | fest |
| Qualitätsanspruch | 9 von 10 nach den Maßstäben in `CLAUDE.md` | fest |
| Begründung des Eigenbaus | Eigener Bedarf in Kalkulation und Beratung. Eine bezifferte Wirtschaftlichkeitsrechnung gegenüber Kauf und Excel-Ausbau steht aus | offen – Vorstudie, braucht Mengengerüst des Auftraggebers |

## 2 Funktionsumfang und Ausbaustufen

Grundlage ist der Recherchebericht (`reports/VOFI Immobiliensoftware Marktrecherche.md`) in der nach Prüfrunde 1 überarbeiteten Fassung. Pflichtumfang und Zuschnitt der Stufen werden von dort übernommen, sobald die Überarbeitung die zweite Prüfrunde bestanden hat.

| Thema | Festlegung | Status |
|---|---|---|
| Reihenfolge | Stufe 1 Wohnen in Niedersachsen (Neubau zur Vermietung, Ankauf Bestand; frei finanziert und gefördert) · Stufe 2 Sanierung im Bestand und Simulation · Stufe 3 Entwicklung mit Verkauf, Gewerbe · Stufe 4 Sonderimmobilien, Unternehmensebene | vorläufig |
| Teilschritte der Stufe 1 | 1a Grobkalkulation für beide Vorhabensarten · 1b-1 Vollkalkulation Ankauf Bestand · 1b-2 Vollkalkulation Neubau · 1c Förderung in voller Tiefe, Vorlagen für Gremium, Bank und Förderantrag. Jeder Teilschritt ist für sich nutzbar und hat eine eigene Freigabe. Einzelheiten: Bericht, Abschnitt 5 und Anhang D | vorläufig – bis zur Freigabe des Zuschnitts durch den Auftraggeber |
| Erbbaurecht | In Stufe 1 nur als frei benennbare Kostenposition (Erbbauzins); das volle Modell folgt in Stufe 3 | vorläufig – Fachfrage an den Auftraggeber, ob es vorgezogen werden muss |
| Arbeitsablauf | Das Werkzeug trägt den Weg von der Grobkalkulation mit wenigen Eingaben über die Verfeinerung bis zur Gremien-, Bank- und Förderantragsunterlage. Eine frühe Phase mit wenigen Eingaben gehört in Stufe 1 | fest |
| Vollständigkeit je Vorhabensart | Eine Vorhabensart kommt erst in eine Stufe, wenn sie dort vollständig rechenbar ist (bei Ankauf Bestand also mit Bewirtschaftung, Instandhaltung, Kaufpreisaufteilung und CO2-Kosten) | fest |
| Kennzahlen | VOFI-Kennzahlen und die international üblichen Größen nebeneinander; ein festes Kennzahlenblatt je Vorhabensart; Zielrendite als Vergleichsmaß neben der Unterlassensalternative | vorläufig |
| Entscheidungspunkte | Vor jeder Stufe eine Freigabe durch den Auftraggeber mit vorher benannten Abbruchkriterien. Der erste Freigabepunkt ist die Vorprüfung vor Beginn der Phase 2: Gespräch mit der NBank, Anwendergespräche, Herstellervorführungen und Katalogverantwortung müssen dann vorliegen | fest |
| Erster Teilschritt | Der erste Teilschritt der Stufe 1 enthält nur, was für eine belegbare Grobkalkulation nötig ist: Änderungsprotokoll, Anmeldung, Projektzuweisung mit einfacher Rollenunterscheidung, benannter Arbeitsstand. Präsenzanzeige und das volle Rollenmodell mit Freigaben folgen im zweiten Teilschritt | fest |

## 3 Rechenkern

Die vollständige Fachspezifikation (Tabellenaufbau, Rechenreihenfolge, Formeln, Konventionen) entsteht als eigenes Kapitel aus dem Anhang des Berichts und den beiden finanzmathematischen Prüfberichten. Bis dahin gelten diese Leitlinien:

| Thema | Festlegung | Status |
|---|---|---|
| Methode | Periodenweise Tabellenrechnung mit expliziten Konten für Eigenkapital, jede Kredittranche, Kontokorrent, Geldanlage und Steuern; jede Periode schließt mit Finanzierungssaldo null | fest |
| Zeitraster | Intern monatlich; Jahresdarstellung als Verdichtung; zusätzlich ein Jahresmodus für den Vergleich mit Lehrbuchfällen | fest |
| Zeithorizont | Mindestens 42 Jahre abbildbar (Laufzeit der NBank-Darlehen), Bindungen von 35 Jahren vollständig | fest |
| Konventionen | Je Zahlungsart sind Basisperiode der Indexierung, Zahlungszeitpunkt, Steuermonat und Verzinsungstakt ausdrücklich festgelegt und dokumentiert | fest (Inhalt: vorläufig) |
| Geldbeträge | Exakte Dezimalrechnung. Je Zahlungsart ist eine Rundungsregel festgelegt; Darlehenspläne runden je Rate kaufmännisch auf Cent, je Darlehen umstellbar, damit Restschulden mit dem Kontoauszug übereinstimmen | fest (Regeln je Zahlungsart: vorläufig) – `MA-013` |
| Ausschüttungen und Nachschüsse | Die Unterlassensalternative erhält dieselbe Einlagen- und Entnahmenreihe wie die Investition. Einlagen und Entnahmen derselben Monatsperiode werden saldiert. Im Jahresmodus wird je Jahr saldiert. Vergleichssätze sind effektive Jahreszinsen. Die Renditeformel bei mehreren Einlagen über die Laufzeit ist eindeutig festzulegen; maßgeblich für Randfälle ist ihr Zähler, nicht der Endwert allein | fest / Formel: vorläufig – `MA-012` |
| Kontrollsummen | Ergebnisse erscheinen erst, wenn alle Kontrollsummen bestanden sind; die Proben berücksichtigen Zuschüsse, Tilgungszuschüsse, Disagio und kapitalisierte Zinsen | fest |
| Randfälle | Zinssatz null, Eigenkapital null, negativer Endwert und mehrdeutiger interner Zinsfuß haben definierte Ergebnisse statt Fehlern | fest |
| Nachvollziehbarkeit | Jede Ergebniszahl lässt sich bis zur Eingabe zurückverfolgen; jede Kalkulation speichert Regelstand und Version des Rechenkerns | fest |
| Abnahmetests | Zwei veröffentlichte Rechenbeispiele des IWU (2004, 2013) und der nachgerechnete Testfall mit Varianten laufen als automatische Tests, jeder mit benannter Toleranz (eigene Fälle auf den Cent; das IWU-Beispiel von 2013 ist nur auf rund 3,40 € nachvollziehbar); weitere Fälle für Verlustvortrag, steuerpflichtigen Verkauf und Monatsraster kommen hinzu | fest |
| Offene Lehrbuchdefinitionen | VOFI-Gesamtkapitalrendite und Amortisationsdauer nach Grob sind am Original zu beschaffen; bis dahin wird die Gesamtkapitalrendite nicht ausgewiesen | offen – Literatur beschaffen |

## 4 Regel- und Förderkatalog

| Thema | Festlegung | Status |
|---|---|---|
| Grundsatz | Steuersätze, Mietrechtsregeln, Förderkonditionen und Fristen sind datierte Daten mit Quelle und Gültigkeit, niemals fest im Programm | fest |
| Fördermodul | Baukasten aus Förderkomponenten (zinsverbilligtes Darlehen, Tilgungszuschuss, Einmalzuschuss, laufender Zuschuss, steuerliche Förderung, Bürgschaft) mit Bemessung, Auszahlungsplan, Bindungen, Voraussetzungen und Kumulierungsregeln; Programme werden konfiguriert, nicht programmiert | fest |
| Kopplungen | Förderung wirkt automatisch auf Miete (Bindungen, Abzug von Drittmitteln bei Modernisierungsumlage und Vergleichsmietenerhöhung), Finanzplan und Abschreibung | fest – Dauer des Abzugs: `MA-007` |
| Pflege | Redaktionell gepflegt mit benannter Verantwortung im Unternehmen; automatisiert höchstens bei Zinssätzen und nur mit Zustimmung der Quelle | fest / Verantwortung: offen – Auftraggeber |
| Rechtsstand | Laufende Gesetzgebung wird als Entwurfsstand geführt und kann je Kalkulation zugeschaltet werden | vorläufig |
| NBank-Renditeprüfung | Das Werkzeug weist die Eigenkapitalrendite für die Überkompensationsprüfung aus dem eigenen Finanzplan aus und bezeichnet sie als eigene Berechnung, bis die Rechenweise der NBank geklärt ist | vorläufig – `MA-001`; dazu `MA-002` bis `MA-006` zur NBank-Förderung |

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
| Beihilferecht | De-minimis-Konto je Unternehmensgruppe und Überkompensationsprüfung als Regelarten im Katalog | vorläufig |
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

1. Gespräch mit der NBank über die Rechenweise der Renditeprüfung.
2. Drei bis fünf Gespräche mit Anwendern oder Kunden.
3. Mengengerüst für die Wirtschaftlichkeitsrechnung (Projekte pro Jahr, heutiger Zeitaufwand, Zahl der Nutzer, Anteil geförderter Mietwohnungsbau).
4. Benennung der Verantwortung für die Pflege des Regel- und Förderkatalogs.
5. Durchsicht der Modellannahmen mit hohem Gewicht (`docs/modellannahmen.md`): Ist die jeweils vorsichtige Voreinstellung fachlich richtig gewählt?
