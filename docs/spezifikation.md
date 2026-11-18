# Spezifikation – VOFI-Immobilienkalkulation

Das maßgebliche Entwicklungsdokument. Es beschreibt, was gebaut wird und warum, und wird laufend fortgeschrieben. Wer am Projekt arbeitet, liest es zuerst; was hier steht, gilt, bis es hier geändert wird.

**Stand:** 2026-11-18 · Konzeptphase, noch kein Code

## Wie dieses Dokument gepflegt wird

- **Erst die Spezifikation, dann die Umsetzung.** Soll etwas anders gebaut werden als hier beschrieben, wird zuerst dieser Text geändert und die Änderung im Entscheidungsprotokoll (`docs/entscheidungen.md`) begründet.
- **Jede Festlegung trägt einen Status:** **fest** (entschieden, Änderung nur mit Protokolleintrag) · **vorläufig** (Arbeitsstand, wird im jeweiligen Kapitel ausgearbeitet) · **offen** (noch zu klären, mit Zuständigkeit).
- **Prüfbefunde fließen ein, wenn sie tragen.** Nach jeder Prüfrunde wird geprüft, ob ein übernommener Befund eine Festlegung berührt; dann wird sie hier angepasst.
- **Annahmen dürfen fallen.** Eine frühere Festlegung zu ändern ist kein Fehler, solange Grund und Datum im Protokoll stehen und die betroffenen Kapitel nachgezogen sind.
- **Kein Wunschzettel.** Hier steht nur, was beschlossen oder als Arbeitsstand gewollt ist. Ideen ohne Entscheidung gehören in `TASKS.md`.

## 1 Zweck und Rahmen

| Thema | Festlegung | Status |
|---|---|---|
| Zweck | Web-Anwendung zur Immobilien-Investitionsrechnung nach der VOFI-Methode (Vollständiger Finanzplan) mit Fördermodulen, Risikoanalyse, Projektübersicht und Mehrbenutzerbetrieb | fest |
| Nutzerkreis | Eigenes Unternehmen und Beratung für Kunden (Berichte, später Lesezugang). Kein Verkauf als Softwareprodukt | fest |
| Vorhabensarten | Ankauf Bestand · Neubau zur Vermietung · Sanierung im Bestand · Entwicklung mit Verkauf | fest |
| Nutzungsarten | Frei finanziertes Wohnen · geförderter Wohnungsbau · Gewerbe/Mixed-Use · Sonderimmobilien | fest |
| Investorensichten | Kapitalgesellschaft · Privatperson und vermögensverwaltende Personengesellschaft · steuerbefreite, kommunale und genossenschaftliche Unternehmen | fest |
| Regionaler Schwerpunkt | Deutschland, Förderlogik zuerst für Niedersachsen (NBank) und Bund (KfW, BAFA) | fest |
| Fachliche Grundlage | Lehrbuch-VOFI (Grob; Schulte/Ropeter), Branchenrichtlinien, geltendes Recht mit Quelle und Stand. Keine eigene Excel-Vorlage; die älteren Repositories `VoFi` und `NBank` werden nicht herangezogen | fest |
| Qualitätsanspruch | 9 von 10 nach den Maßstäben in `CLAUDE.md` | fest |
| Begründung des Eigenbaus | Eigener Bedarf in Kalkulation und Beratung. Eine bezifferte Wirtschaftlichkeitsrechnung gegenüber Kauf und Excel-Ausbau steht aus | offen – Vorstudie, braucht Mengengerüst des Auftraggebers |

## 2 Funktionsumfang und Ausbaustufen

Grundlage ist der Recherchebericht (`reports/VOFI Immobiliensoftware Marktrecherche.md`) in der nach Prüfrunde 1 überarbeiteten Fassung. Pflichtumfang und Zuschnitt der Stufen werden von dort übernommen, sobald die Überarbeitung die zweite Prüfrunde bestanden hat.

| Thema | Festlegung | Status |
|---|---|---|
| Reihenfolge | Stufe 1 Wohnen in Niedersachsen (Neubau zur Vermietung, Ankauf Bestand; frei finanziert und gefördert) · Stufe 2 Sanierung im Bestand und Simulation · Stufe 3 Entwicklung mit Verkauf, Gewerbe · Stufe 4 Sonderimmobilien, Unternehmensebene | vorläufig |
| Arbeitsablauf | Das Werkzeug trägt den Weg von der Grobkalkulation mit wenigen Eingaben über die Verfeinerung bis zur Gremien-, Bank- und Förderantragsunterlage. Eine frühe Phase mit wenigen Eingaben gehört in Stufe 1 | fest |
| Vollständigkeit je Vorhabensart | Eine Vorhabensart kommt erst in eine Stufe, wenn sie dort vollständig rechenbar ist (bei Ankauf Bestand also mit Bewirtschaftung, Instandhaltung, Kaufpreisaufteilung und CO2-Kosten) | fest |
| Kennzahlen | VOFI-Kennzahlen und die international üblichen Größen nebeneinander; ein festes Kennzahlenblatt je Vorhabensart; Zielrendite als Vergleichsmaß neben der Unterlassensalternative | vorläufig |
| Entscheidungspunkte | Vor jeder Stufe eine Freigabe durch den Auftraggeber mit vorher benannten Abbruchkriterien | fest |

## 3 Rechenkern

Die vollständige Fachspezifikation (Tabellenaufbau, Rechenreihenfolge, Formeln, Konventionen) entsteht als eigenes Kapitel aus dem Anhang des Berichts und den beiden finanzmathematischen Prüfberichten. Bis dahin gelten diese Leitlinien:

| Thema | Festlegung | Status |
|---|---|---|
| Methode | Periodenweise Tabellenrechnung mit expliziten Konten für Eigenkapital, jede Kredittranche, Kontokorrent, Geldanlage und Steuern; jede Periode schließt mit Finanzierungssaldo null | fest |
| Zeitraster | Intern monatlich; Jahresdarstellung als Verdichtung; zusätzlich ein Jahresmodus für den Vergleich mit Lehrbuchfällen | fest |
| Zeithorizont | Mindestens 42 Jahre abbildbar (Laufzeit der NBank-Darlehen), Bindungen von 35 Jahren vollständig | fest |
| Konventionen | Je Zahlungsart sind Basisperiode der Indexierung, Zahlungszeitpunkt, Steuermonat und Verzinsungstakt ausdrücklich festgelegt und dokumentiert | fest (Inhalt: vorläufig) |
| Geldbeträge | Exakte Dezimalrechnung; Darlehenspläne mit banküblicher Rundung auf Cent je Rate, damit Restschulden mit dem Kontoauszug übereinstimmen | fest |
| Ausschüttungen und Nachschüsse | Die Unterlassensalternative erhält dieselbe Einlagen- und Entnahmenreihe wie die Investition. Die Renditeformel bei mehreren Einlagen über die Laufzeit ist eindeutig festzulegen | fest / Formel: offen |
| Kontrollsummen | Ergebnisse erscheinen erst, wenn alle Kontrollsummen bestanden sind; die Proben berücksichtigen Zuschüsse, Tilgungszuschüsse, Disagio und kapitalisierte Zinsen | fest |
| Randfälle | Zinssatz null, Eigenkapital null, negativer Endwert und mehrdeutiger interner Zinsfuß haben definierte Ergebnisse statt Fehlern | fest |
| Nachvollziehbarkeit | Jede Ergebniszahl lässt sich bis zur Eingabe zurückverfolgen; jede Kalkulation speichert Regelstand und Version des Rechenkerns | fest |
| Abnahmetests | Zwei veröffentlichte Rechenbeispiele des IWU (2004, 2013) und der nachgerechnete Testfall mit Varianten laufen als automatische Tests; weitere Fälle für Verlustvortrag, steuerpflichtigen Verkauf und Monatsraster kommen hinzu | fest |
| Offene Lehrbuchdefinitionen | VOFI-Gesamtkapitalrendite und Amortisationsdauer nach Grob sind am Original zu beschaffen; bis dahin wird die Gesamtkapitalrendite nicht ausgewiesen | offen – Literatur beschaffen |

## 4 Regel- und Förderkatalog

| Thema | Festlegung | Status |
|---|---|---|
| Grundsatz | Steuersätze, Mietrechtsregeln, Förderkonditionen und Fristen sind datierte Daten mit Quelle und Gültigkeit, niemals fest im Programm | fest |
| Fördermodul | Baukasten aus Förderkomponenten (zinsverbilligtes Darlehen, Tilgungszuschuss, Einmalzuschuss, laufender Zuschuss, steuerliche Förderung, Bürgschaft) mit Bemessung, Auszahlungsplan, Bindungen, Voraussetzungen und Kumulierungsregeln; Programme werden konfiguriert, nicht programmiert | fest |
| Kopplungen | Förderung wirkt automatisch auf Miete (Bindungen, Abzug von Drittmitteln bei Modernisierungsumlage und Vergleichsmietenerhöhung), Finanzplan und Abschreibung | fest |
| Pflege | Redaktionell gepflegt mit benannter Verantwortung im Unternehmen; automatisiert höchstens bei Zinssätzen und nur mit Zustimmung der Quelle | fest / Verantwortung: offen – Auftraggeber |
| Rechtsstand | Laufende Gesetzgebung wird als Entwurfsstand geführt und kann je Kalkulation zugeschaltet werden | vorläufig |
| NBank-Renditeprüfung | Das Werkzeug weist die Eigenkapitalrendite im Sinne der Überkompensationsprüfung aus, sobald die Rechenweise der NBank geklärt ist | offen – Auftraggeber fragt NBank |

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
| Simulation | Zufallsstartwert, Generator und Version werden je Lauf gespeichert; Server und Browser verwenden dieselben mathematischen Funktionen | Wiederholbare Ergebnisse | fest |
| Excel | Import von Beginn an; Export zunächst als Werte mit Annahmenblatt und Versionsstempel | Banken und Gremien arbeiten mit Excel | vorläufig – Praktiker verlangt nachrechenbaren Export früher |

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

## 8 Offene Punkte beim Auftraggeber

1. Gespräch mit der NBank über die Rechenweise der Renditeprüfung.
2. Drei bis fünf Gespräche mit Anwendern oder Kunden.
3. Mengengerüst für die Wirtschaftlichkeitsrechnung (Projekte pro Jahr, heutiger Zeitaufwand, Zahl der Nutzer, Anteil geförderter Mietwohnungsbau).
4. Benennung der Verantwortung für die Pflege des Regel- und Förderkatalogs.
