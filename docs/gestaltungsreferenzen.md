# Gestaltungsreferenzen

**Zweck:** Vorbilder für die Kernansichten des Werkzeugs, je Ansicht mit dem Muster, das wir übernehmen, und dem, was wir bewusst nicht übernehmen. Grundlage für die Festlegung „Vorgehen" in `docs/spezifikation.md`, Kapitel 6.
**Leser:** Entwicklung (Entwurf der Ansichten), Auftraggeber (Nachvollzug der Gestaltungsrichtung).
**Stand:** 2026-11-18
**Sammlung:** [VOFI Referenzen auf Mobbin](https://mobbin.com/collections/55475f2b-e821-4e46-934e-48b7a5ba6ab9/web/screens) – privat, nur für den Kontoinhaber und sein Team sichtbar. Jedes Vorbild trägt dort einen Kommentar mit derselben Einordnung wie hier.

Mobbin zeigt allgemeine Finanz-, Planungs- und Analyseanwendungen; Immobilien-Fachsoftware ist dort nicht vertreten. Die Vorbilder sind deshalb nach dem Muster gewählt, nicht nach der Branche. Bilder sind nicht eingebettet, weil die Bildadressen ablaufen; die Links führen auf die Mobbin-Seite des Bildschirms.

## 1 Projektübersicht

Muster: eine Datentabelle mit einer Zeile je Projekt, Status als farbiges Etikett in eigener Spalte, Verantwortliche als Namenskürzel, Beträge rechtsbündig. Darüber eine Filterleiste, deren aktive Filter als lesbarer Satz stehen („Status ist Planung oder In Bearbeitung"); die Spaltenauswahl liegt in einem eigenen Menü.

| Vorbild | Übernehmen | Nicht übernehmen |
|---|---|---|
| [Airtable – Projektliste mit Statusfilter](https://mobbin.com/screens/b3b21595-5794-4b20-bb85-ba48a59f12a1) | Filter als Satzbaustein mit Mehrfachauswahl der Status, Rücksetzen-Schaltfläche, Projektzahl in der Fußzeile | Bunte Statusfarben ohne feste Bedeutung; Datumsformat M/T/JJJJ |
| [Hex – Projektliste mit Spaltenauswahl](https://mobbin.com/screens/c19382a2-22c3-430e-b5f4-141f79f95891) | Spaltenauswahl mit Kontrollkästchen und „Zurücksetzen", Sortierung „zuletzt angesehen", Favoriten in der Seitenleiste | Leere Spalten bei unvollständigen Projekten ohne Kennzeichnung |
| [Apollo – Vorgangsliste mit Summenzeile und Seitenformular](https://mobbin.com/screens/c0181b7a-c4e6-4572-97ca-105acee05087) | Summenzeile unter der Betragsspalte; Neuanlage im Seitenpanel, ohne die Liste zu verlassen | Abgekürzte Beträge („4.33K") in einer Fachanwendung |

**Für unser Werkzeug heißt das:** Die Projektübersicht ist eine Tabelle, keine Kachelfläche. Spalten: Projekt, Vorhabensart, Arbeitsstand mit Freigabestatus, Verantwortlicher, Gesamtinvestition, EK-Rendite (VOFI), Stand der letzten Änderung; Filter nach Status, Vorhabensart und Verantwortlichem; Beträge voll ausgeschrieben im deutschen Format.

## 2 Eingabe von Annahmen

Muster: Annahmen in aufklappbaren Gruppen; der Gruppenkopf zeigt die Wirkung der Gruppe als Betrag. Je Zeile steht links die Bezeichnung mit einer Zeile Erläuterung, rechts das Eingabefeld mit Einheit im Feld. Verknüpfte Größen (Betrag und Anteil) stehen nebeneinander und rechnen sich gegenseitig um; geänderte Werte heben sich farblich vom Ausgangsstand ab.

| Vorbild | Übernehmen | Nicht übernehmen |
|---|---|---|
| [Zillow – Finanzierungsrechner](https://mobbin.com/screens/2066fe3c-4390-48de-8705-da6d9be19d06) | Gruppen mit Summe im Kopf („Property taxes 1.941 $"); Betrag und Prozent als gekoppeltes Feldpaar; Rechenweg sichtbar („1,67 % = 23.297 $/Jahr") | Lockere Formularabstände; Hinweistext unter jedem Feld |
| [Deputy – kompakte Zahlenliste](https://mobbin.com/screens/07fc7df7-32f1-4aee-8ace-c3d6881f94cf) | Zweispaltiges Raster: Bezeichnung links, Feld rechts, Einheit als Suffix im Feld | Felder über die volle Breite – bei Zahlen genügen 12 bis 16 Zeichen |
| [Sentry – nummerierte Einstellungsgruppen](https://mobbin.com/screens/7b1f2127-9f3d-451d-b9f6-32ffa2d02ecb) | Gruppe mit Überschrift und einem Satz Zweck; Bezeichnung mit Kurzerläuterung links, Feld rechts | Schrittnummern – Annahmen werden nicht in fester Reihenfolge abgearbeitet |
| [Neon – geänderte Zeile hervorgehoben](https://mobbin.com/screens/e4251f3b-8253-4662-bb95-08cbbfeee6e9) | Geänderte Werte farbig markiert, bis sie bestätigt sind; Einheit/Datentyp im Spaltenkopf | „Änderungen speichern / verwerfen" – bei uns wird jede Änderung sofort gespeichert und protokolliert |

**Für unser Werkzeug heißt das:** Ein Annahmenblatt mit Gruppen nach VOFI-Gliederung (Investition, Finanzierung, Bewirtschaftung, Steuern, Förderung), Einheit im Feld, Voreinstellung und Quelle per Tooltip. Ein Wert, der von der Voreinstellung oder vom freigegebenen Arbeitsstand abweicht, trägt eine Markierung am Feldrand und lässt sich einzeln zurücksetzen.

## 3 Finanzplan-Tabelle

Muster: Zeilenbezeichnungen in einer fixierten linken Spalte, Perioden als Spalten mit waagerechtem Bildlauf. Zeilen in aufklappbaren Gruppen mit Zwischensumme je Gruppe, Saldo- und Bestandszeilen grau unterlegt. Ein Umschalter Monat/Jahr über der Tabelle; eine senkrechte Linie trennt Ist- von Planwerten.

| Vorbild | Übernehmen | Nicht übernehmen |
|---|---|---|
| [Mercury – Cash-Flow-Analyse](https://mobbin.com/screens/f41ddda3-30cd-4bed-8730-9ab936b86a4c) | Fixierte Bezeichnungsspalte; Zeilen „Anfangsbestand" und „Bewegung" als unterlegte Gruppenköpfe; Umschalter „Monatlich" plus Jahreswahl; Diagramm Endbestand/Bewegung über der Tabelle | Monatsreiter als zusätzliche Navigation neben dem Bildlauf |
| [Causal – Modell mit Szenarien](https://mobbin.com/screens/c40c1200-8716-4dd1-892e-5e928acccec1) | Trennung Eingaben/Berechnungen als eigene Abschnitte; Gruppen mit Ordnersymbol; Mini-Verlaufslinie je Zeile; Formel als lesbare Bezüge („Inbound leads previous month") | Eingaben und Rechnung im selben Raster – bei uns nach FAST getrennt |
| [Monarch – Prognose über zehn Jahre](https://mobbin.com/screens/165858c6-39ad-450e-84ff-d4d952aa2616) | Umschalter „Monthly/Yearly" oben rechts; Gesamtzeilen als eigene, abgesetzte Blöcke; „Show 9 unbudgeted" für ausgeblendete Leerzeilen | Bildchen je Zeile; Zeilenhöhe zu groß für 40 Jahre |
| [YNAB – Einnahmen/Ausgaben](https://mobbin.com/screens/62817fae-ab1b-43cf-a15d-3d372afd32ca) | Mehrstufige Gruppen mit „Total …"-Zeilen; Spalten Durchschnitt und Summe am rechten Rand | Rot/Grün als Bereichsüberschrift; Emoji in Kategorienamen |
| [Fey – Kapitalflussrechnung](https://mobbin.com/screens/04db1121-595e-4723-90fb-061cc3bd25be) | Laufendes Jahr farbig abgesetzt; Veränderung zum Vorjahr als kleines Etikett beim Wert; Umschalter Quartal/Jahr | Dunkles Design; „Not Reported" statt Strich |
| [Xero – Liquiditätsvorschau](https://mobbin.com/screens/b8b8db5b-aec1-4b34-85ee-ae1e03102c5b) (ergänzend) | Umschalter Zusammenfassung/Tabelle; Kopfleiste Zufluss, Abfluss, Endbestand der Periode; aufklappbare Zeilen mit Einzelposten | Vollfarbige Kacheln „Suggested actions" |

**Für unser Werkzeug heißt das:** Die VOFI-Tabelle wird Eigenbau auf einer Tabellenbibliothek mit fixierter erster Spalte und virtualisiertem Bildlauf (42 Jahre × 12 Monate). Zeilenaufbau nach VOFI-Lehrbuch: Zahlungsreihe, Eigenkapital, Kredite, Geldanlage, Steuern, Finanzierungssaldo, Bestandsgrößen; Saldo- und Bestandszeilen unterlegt, Jahresumschaltung als Standard, Monat bei Bedarf.

## 4 Szenarien und Arbeitsstände

Muster: Der aktive Stand wird über eine Auswahl im Kopf der Arbeitsfläche gewählt und bleibt dort sichtbar. Versionen stehen in einer Tabelle mit Nummer, Zeitpunkt, Bearbeiter, Status und Kommentar; zwei Zeilen lassen sich zum Vergleich auswählen. Der Zahlenvergleich zweier Stände folgt dem Plan-Ist-Schema: Stand A, Stand B, Abweichung absolut, Abweichung in Prozent.

| Vorbild | Übernehmen | Nicht übernehmen |
|---|---|---|
| [Causal – Szenarioauswahl im Modellkopf](https://mobbin.com/screens/c40c1200-8716-4dd1-892e-5e928acccec1) | Szenario-Auswahl als Menü in der Werkzeugleiste mit Kennzeichnung des Standards; „Versions" daneben | Szenario und Version als zwei getrennte Konzepte ohne Erklärung |
| [Confluence – Versionstabelle](https://mobbin.com/screens/b405410d-7a2d-4bd6-b44d-4efa934e0dec) | Spalten Version, Datum, Geändert von, Status, Kommentar; Auswahl von genau zwei Versionen zum Vergleich; „Wiederherstellen" je Zeile mit Pflichtkommentar | Relative Zeitangaben („vor 6 Minuten") ohne absolutes Datum |
| [AWS – Plan-Ist-Tabelle mit Abweichung](https://mobbin.com/screens/d3ff9452-2c33-4222-b18f-c9df01dc7f33) | Spaltenfolge Ist, Plan, Abweichung absolut, Abweichung %; Strich statt Null bei fehlendem Wert; CSV-Download | Keine Hervorhebung wesentlicher Abweichungen |
| [Braintrust – Basis und Vergleich nebeneinander](https://mobbin.com/screens/da7f4d57-a8bd-4efd-b827-1dabf6d7ef30) | Zwei Spalten „Basis" und „Vergleich" mit je eigener Auswahl des Stands; Schalter „Diff" für die Unterschiedsansicht | Gleiche Gewichtung beider Seiten – bei uns ist der freigegebene Stand die Basis |

**Für unser Werkzeug heißt das:** Arbeitsstand-Auswahl dauerhaft im Kopf, mit Status (Entwurf, zur Prüfung, freigegeben). Der Vergleich zweier Stände ist eine Tabelle Basis | Vergleich | Δ | Δ % für Annahmen und Kennzahlen, mit Filter „nur Abweichungen"; freigegebene Stände sind schreibgeschützt.

## 5 Kennzahlenblatt und Auswertung

Muster: Wenige Kennzahlen als Liste, jede mit ihrem Vergleichsmaßstab direkt darunter oder daneben (Zielwert, Schwelle, Benchmark). Diagramme beantworten je eine Frage: Brücke vom Ausgangs- zum Endwert als Wasserfall, Verlauf über die Zeit gegen eine Vergleichslinie.

| Vorbild | Übernehmen | Nicht übernehmen |
|---|---|---|
| [Turo – Kennzahlen mit Schwellenwert](https://mobbin.com/screens/1a67ef81-40cd-44c8-b742-440dcb7e4fe1) | Je Kennzahl eine Zeile: Bezeichnung links, Wert rechts, Schwelle klein darunter („All-Star Host: 85 %"); aufklappbar für die Herleitung | Statusabzeichen und Tipps-Kachel |
| [Monarch – Rendite gegen Vergleichsindex](https://mobbin.com/screens/45b86e4e-2339-48f1-aeb7-15f7e7514a47) | Eigene Linie gegen Vergleichslinie im selben Diagramm; Nulllinie betont; Vergleichsgrößen als zuschaltbare Reiter | Grelle Akzentfarbe für die eigene Linie; Zeitraumschalter 1W–5Y (bei uns Haltedauer fest) |
| [Zoho CRM – Wasserfall mit Gesamtsäulen](https://mobbin.com/screens/56e5fd35-4d92-481f-aaca-3b02adf911ae) | Gesamtsäulen zwischen den Veränderungen, Wertbeschriftung an jeder Säule, Klammer „Gesamtdifferenz +150 %" über der Brücke | Farben Blau/Grün/Rot ohne IBCS-Semantik; Achse mit „k" statt ausgeschriebener Einheit |
| [Origin – Vermögensprognose](https://mobbin.com/screens/61bcb749-be67-42ae-8966-a231eaf49ed5) | Erläuterung eines Wendepunkts direkt am Datenpunkt; Kennzahl „heute" und „Endwert" über dem Diagramm | KI-Zusammenfassung; Achse ohne Tausendertrennung |

**Für unser Werkzeug heißt das:** Das Kennzahlenblatt ist eine Tabelle mit Spalten Kennzahl | Wert | Vergleichsmaß (Zielrendite, Unterlassensalternative) | Abweichung, keine Kachelreihe. Dazu höchstens drei Diagramme nach IBCS: Wasserfall vom Eigenkapitaleinsatz zum Endvermögen, Verlauf des Finanzierungssaldos, Bandbreite aus der Simulation.

## 6 Sensitivität und Was-wäre-wenn

Muster: Regler für die wenigen Treiber, der aktuelle Wert rechts neben der Bezeichnung, das Ergebnis oben und das Diagramm darunter aktualisieren sich sofort. Für zwei Treiber zugleich eine Matrix: Zeilen und Spalten sind die Stufen der beiden Treiber, die Zelle des Ausgangsfalls ist markiert, Werte sind nach Höhe eingefärbt.

| Vorbild | Übernehmen | Nicht übernehmen |
|---|---|---|
| [Claude – Zinseszinsrechner](https://mobbin.com/screens/025626bb-da23-4aaa-b892-83a399b2bc19) | Regler mit Wert rechtsbündig über der Spur; Ergebnisgrößen oben; Umschalter für die Periodizität; Diagramm reagiert sofort | Regler ohne Eingabefeld für genaue Werte |
| [Kiwi.com – Preismatrix zweier Daten](https://mobbin.com/screens/ea4bc778-0ba3-40c1-b552-ae18df885f79) | Zwei-Wege-Matrix mit Achsenbeschriftung oben und rechts; gewählte Zelle dunkel, Zeile und Spalte hell hinterlegt; günstige/ungünstige Werte farbig | Rot/Grün als einzige Unterscheidung (nicht farbenblind-sicher) |

**Für unser Werkzeug heißt das:** Sensitivität bekommt drei Werkzeuge: Regler für ±-Variation einzelner Treiber mit sofortiger Neuberechnung (Rechenkern im Browser), Zwei-Wege-Matrix (z. B. Zins × Miete) mit markiertem Basisfall und diskreter, farbenblind-tauglicher Abstufung, Tornado für die Rangfolge. Für das Tornadodiagramm gab Mobbin kein Vorbild (siehe Lücken).

## 7 Änderungsverlauf und Nachvollziehbarkeit

Muster: Ein Änderungsprotokoll als Tabelle mit festen Spalten Objekt, Feld, Zeitpunkt, alter Wert, neuer Wert, Person, gefiltert nach Zeitraum. Je Feld ist derselbe Verlauf aus dem Kontextmenü erreichbar. Die Herkunft einer Zahl wird über ein Kontextmenü „Untersuchen" am Wert geöffnet, nicht über eine eigene Seite.

| Vorbild | Übernehmen | Nicht übernehmen |
|---|---|---|
| [Pinterest – Änderungsverlauf des Kontos](https://mobbin.com/screens/7c8e8fec-1554-4b00-b0bb-d4a06b7cc589) | Spalten Objekt, Geändertes Feld, Zeitpunkt (mit Zeitzone), Vorher, Nachher, Benutzer; Zeitraumfilter oben; Seitenweise Anzeige | Technische Feldnamen („is_fdb") statt fachlicher Bezeichnung |
| [Zoom – Versionsverlauf einer Tabelle](https://mobbin.com/screens/681304f3-411a-41b5-a477-e523e844709c) | Änderungen je Person und Zeitpunkt gebündelt; „Vorher → Nachher" mit Pfeil; Spaltentyp-Symbol vor dem Feldnamen | Darstellung als Dialog über der Arbeitsfläche – bei uns Seitenpanel, damit die Tabelle sichtbar bleibt |
| [Causal – Kontextmenü am Wert mit „Comment" und „Inspect"](https://mobbin.com/screens/bcf6a262-169f-4562-aeac-43ccf67fa854) | Ein Kontextmenü je Zeile/Zelle mit Einheit wählen, Kommentieren und Untersuchen (Herkunft); Tastenkürzel im Menü | Ausrichtungs- und Sortieroptionen im selben Menü wie fachliche Funktionen |

**Für unser Werkzeug heißt das:** Jede Zahl der VOFI-Tabelle hat „Herkunft anzeigen": Seitenpanel mit Rechenweg (Formel in Worten, eingehende Annahmen mit Wert und Quelle) und darunter dem Änderungsverlauf der beteiligten Annahmen. Das projektweite Protokoll ist eine filterbare Tabelle nach Pinterest-Schema mit fachlichen Feldnamen und absolutem Zeitstempel. Personenbezogene Daten erscheinen dort nicht (Spezifikation, Kapitel 5).

## 8 Zusammenarbeit

Muster: Wer im Projekt ist, steht als Reihe von Namenskürzeln im Kopf; wer gerade an einer Stelle arbeitet, ist dort mit seinem Kürzel und einem farbigen Rahmen markiert. Kommentare hängen an einer Zelle oder einem Feld, öffnen sich als Faden im rechten Panel und lassen sich als erledigt abschließen. Freigaben laufen als sichtbarer Ablauf mit Status, Antragsteller, Prüfer und Pflichtkommentar.

| Vorbild | Übernehmen | Nicht übernehmen |
|---|---|---|
| [Canva – Kommentar an einer Tabellenzelle](https://mobbin.com/screens/979821d7-fca6-42bc-86b8-631a0a4c291c) | Kürzel des Bearbeiters an der Zelle; Kommentarfaden im rechten Panel mit Antworten und Haken „erledigt"; Rückfrage vor dem Löschen eines Fadens | Kreisdiagramm im Hintergrund; Löschen statt Archivieren – bei uns bleiben Fäden im Protokoll |
| [Microsoft Loop – Präsenz und Faden am Absatz](https://mobbin.com/screens/d5d348c9-8f9a-42a2-b643-5310c5f3fd0d) | Präsenz-Kürzel im Kopf und neben dem Eintrag in der Navigation; Faden am Element verankert, Zähler am Anker | Titelbild und Emojis |
| [Rows – Freigabedialog mit Rollen](https://mobbin.com/screens/7df349be-6228-4299-9fd2-1ae27f98cbd8) | Einladung mit Rollenwahl im Feld („Can edit"); Mitgliederliste mit Rolle und Status „Ausstehend"; Bestätigungsmeldung „Berechtigungen aktualisiert" | Freigabe per öffentlichem Link – für Bank- und Gremienunterlagen ausgeschlossen |
| [Aboard – Genehmigungsablauf](https://mobbin.com/screens/002ebeab-9460-41e8-bdbb-b76019b8f550) | Statusband „Ausstehend"; Ablauf mit Antragsteller (erledigt) und Prüfer (wartet); Ablehnen/Genehmigen mit Kommentar | Beleg-Vorschau als Hauptfläche |

**Für unser Werkzeug heißt das:** Präsenz im Projektkopf und an der bearbeiteten Zelle (nur Anzeige, keine Sperre – bei gleichzeitiger Eingabe gilt der spätere Wert). Kommentare an Annahmen und Tabellenzellen, abschließbar, nie gelöscht. Der Arbeitsstand wird über einen Ablauf Entwurf → zur Prüfung → freigegeben gebracht; der Prüfer genehmigt oder weist mit Pflichtkommentar zurück. Rollen nach Spezifikation: Verantwortlicher, Bearbeiter, Prüfer, Leser.

## 9 Berichte und Export

Muster: Ein Berichtsassistent mit drei Spalten: links die Seiten als Miniaturen (Deckblatt, Inhalt, Berichtsteile), in der Mitte die Einstellungen der gewählten Seite, rechts die maßstäbliche Vorschau. Ein zweiter Schritt legt Papierformat, Seitenzahlen und Kopfzeile fest.

| Vorbild | Übernehmen | Nicht übernehmen |
|---|---|---|
| [QuickBooks – Managementbericht erstellen](https://mobbin.com/screens/9e7af3f2-4437-4aad-abf1-17900dfae1dd) | Seitenleiste mit Miniaturen (Deckblatt, Inhaltsverzeichnis, Vorbemerkungen, Berichte und Diagramme); Vorlagenwahl; Deckblatt mit Firma, Berichtszeitraum, „Erstellt von/am"; Zeitraumwahl oben rechts | Vier frei wählbare Deckblattvorlagen – bei uns eine feste Hausvorlage je Empfänger (Gremium, Bank, Förderantrag) |
| [Xero – Berichtslayout bearbeiten](https://mobbin.com/screens/4ce3f2d0-84cd-4378-aaf1-7bbc322c652a) | Bericht als Seite auf grauem Grund; Abschnitte mit Überschrift, einem Satz Text und Tabelle untereinander; Werkzeugleiste für Abschnitt einfügen/verschieben; PDF-Knopf | Tabellenstil mit grauen Kästchen je Zeilenbezeichnung |
| [Craft – PDF-Vorschau mit Optionen](https://mobbin.com/screens/4db19b6a-476b-4f67-85c8-c14da1b98baa) | Optionen links (A4, Seitenzahlen, Dokumenttitel), Vorschau rechts, ein Knopf „Als PDF exportieren" | Wasserzeichen und „Stil verwenden" als Schalter |

**Für unser Werkzeug heißt das:** Berichte entstehen aus festen Vorlagen je Empfänger; der Anwender wählt Inhalte (Kennzahlenblatt, VOFI-Tabelle Jahreswerte, Annahmen, Sensitivität, Förderung) per Kontrollkästchen und sieht die Seite maßstäblich. Jede Seite trägt Arbeitsstand, Freigabestatus und Erstellungsdatum in der Fußzeile; Format A4, deutsche Zahlformate, Diagramme nach IBCS.

## 10 Kredit- und Tilgungsplan

Muster: Die Konditionen eines Darlehens stehen als Liste Bezeichnung | Wert (Darlehensart, Sollzins, effektiver Jahreszins, Zinsbindung, Tilgung); darunter folgt der Zahlungsplan mit Fälligkeiten. Eine Zahlungsregel wird in Worten angezeigt und mit den nächsten Fälligkeiten belegt.

| Vorbild | Übernehmen | Nicht übernehmen |
|---|---|---|
| [Zillow – Finanzierungsangebot](https://mobbin.com/screens/d9764dfc-e5e8-44ce-aaf9-880d88ebb467) | Konditionen als zweispaltige Liste (Darlehensart, Zinssatz, effektiver Jahreszins, Gebühren); Trennlinie zwischen Ergebnis- und Konditionsblock | Vertriebsknopf „Get pre-qualified"; Hinweisblock unter dem Dialog |
| [Mercury – wiederkehrende Zahlung](https://mobbin.com/screens/3383ccdd-1fe6-4969-9882-c55e95fd8dd3) | Zahlungsregel in Worten („monatlich zum 28."); die nächsten Fälligkeiten mit Wochentag; Hinweis bei Verschiebung („28.12. fällt auf ein Wochenende"); Laufzeitende | Erfolgsseite als Rahmen |
| [Zillow – Finanzierungsrechner](https://mobbin.com/screens/2066fe3c-4390-48de-8705-da6d9be19d06) (auch Ansicht 2) | Eingabe Kaufpreis, Eigenkapital als Betrag und Anteil, Darlehensprogramm, Zinssatz in einem Block | Rate als einzige Ergebnisgröße |

**Für unser Werkzeug heißt das:** Je Darlehen eine Konditionenkarte (Art, Nennbetrag, Auszahlung, Sollzins, Zinsbindung, anfängliche Tilgung, tilgungsfreie Jahre, Bereitstellungszins, Förderzuschuss) und darunter der Tilgungsplan als Tabelle Periode | Anfangsschuld | Zins | Tilgung | Rate | Restschuld, mit Jahressummen und Markierung des Zinsbindungsendes. Für die Plantabelle selbst gab Mobbin kein Vorbild (siehe Lücken).

## Gegenbeispiele

Nicht gespeichert; hier festgehalten, damit die Fehler nicht wiederholt werden.

| Beispiel | Fehler | Was wir stattdessen tun |
|---|---|---|
| [QuickBooks – Lead-Übersicht](https://mobbin.com/screens/325b5f2c-7903-4c73-a442-388ed62946ce) | Ringdiagramm für drei Kategorien mit Werten 1/0/1, daneben ein Balkendiagramm mit leeren Stufen und ein Prozentwert „0,00 %" – drei Kacheln, keine Aussage | Kleine Mengen als Zahl in der Tabelle; Diagramm nur, wenn es eine Frage beantwortet, mit der Aussage im Titel |
| [Zoho CRM – Startseite aus Kacheln](https://mobbin.com/screens/c069fad5-d6e2-4788-bf12-e77add0515fa) | Kachelwüste: vier Zahlenkacheln ohne Vergleichsmaß, darunter sechs gleich gewichtete Mini-Tabellen mit eigenem Menü und eigener Sortierung | Eine Hauptaussage je Ansicht; Kennzahlen mit Vergleichsmaß in einer Tabelle |
| [Rocket Money – Darlehensdetail](https://mobbin.com/screens/ec4485f4-f259-45c2-b26d-d47f161a1c48) | Ring „100 %" für ein einziges Darlehen, Flächendiagramm einer konstanten Linie – Dekoration ohne Information | Restschuldverlauf nur, wenn sich etwas bewegt; Einzelwerte als Zahl |
| [Behance – Zugriffsquellen](https://mobbin.com/screens/5404c3ce-e3fc-4f18-8ea3-570b94f9e267) | Dieselben Werte zweimal: als Balkenliste und als Ringdiagramm daneben | Eine Darstellung je Aussage |

## Lücken

Für diese Bausteine hat Mobbin nichts Brauchbares geliefert; die Referenz muss anders beschafft werden.

| Lücke | Woher die Referenz kommt |
|---|---|
| Berichte und Diagramme in Geschäftsberichtsqualität (Notation für Ist/Plan/Szenario, Wasserfall, Abweichungsdiagramme, Seitenraster) | IBCS-Standard (ibcs.com, frei verfügbare Fassung) mit den Beispielen zu Notation, Skalierung und Abweichungen; Geschäftsberichte großer Konzerne für Typografie und Raster |
| Tornadodiagramm und Bandbreiten-/Fächerdiagramm der Simulation | IBCS-Beispiele für Abweichungsbalken; Dokumentation gängiger Diagrammbibliotheken (Beispiele „tornado", „fan chart"); Lehrbuch-Darstellungen der Risikoanalyse |
| Tilgungsplan als Tabelle mit Zinsbindungsende und Anschlussfinanzierung | Tilgungspläne der Förderbanken (KfW, NBank) und Bankangebote; Handbücher der Immobilien-Fachsoftware |
| Datendichte Fachtabellen mit fixierten Spalten, Tastaturbedienung und Barrierefreiheit | Öffentliche Gestaltungssysteme für Fachanwendungen: IBM Carbon (Data table), SAP Fiori (Grid Table, Analytical Table), Atlassian Design System, GOV.UK Design System (Formulare, Fehlermeldungen); WAI-ARIA Authoring Practices (Grid-Muster) |
| Herkunft einer Zahl (Rechenweg, Abhängigkeiten) | Excel „Spur zum Vorgänger" und Formelauswertung als Bedienmuster; Dokumentation von Causal und vergleichbaren Modellierungswerkzeugen |
| Immobilienspezifische Ansichten (Flächen- und Mieterliste, Kostengliederung DIN 276, Förderprogramme) | Handbücher und Vorführungen der Fachsoftware aus der Marktrecherche (`reports/`); Formulare der Förderbanken |
