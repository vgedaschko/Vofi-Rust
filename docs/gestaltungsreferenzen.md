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

**Für unser Werkzeug heißt das:** Die VOFI-Tabelle wird Eigenbau auf einer Tabellenbibliothek mit fixierter erster Spalte und virtualisiertem Bildlauf (42 Jahre × 12 Monate). Zeilenaufbau nach VOFI-Lehrbuch: Zahlungsreihe, Eigenkapital, Kredite, Geldanlage, Steuern, Finanzierungssaldo, Bestandsgrößen; Saldo- und Bestandszeilen unterlegt, Jahresumschaltung als Standard, Monat bei Bedarf.

(In Arbeit – Abschnitte 4 bis 10 folgen.)
