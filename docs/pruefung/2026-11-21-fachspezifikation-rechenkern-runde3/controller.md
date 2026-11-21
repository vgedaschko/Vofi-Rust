Rolle: Controller (Controlling des Wohnungsunternehmens)
Prüfobjekt: `docs/fachspezifikation-rechenkern.md`, eingefrorene Fassung vom 2026-11-21. Das Dokument ist vollständig gelesen. Dazu der Referenzrechner: `grobkalkulation.py` in den Teilen Klassen, Abweichungen, Herkunft und Vergleich, `rf_rahmen.py` (Festschreibung), `aenderungen-runde2.md` (Abschnitt „Durchsicht und Nachtrag 2“), `ursachen-durchsicht.json` und die übrigen Ursachendateien. Der Lauf ist ausgeführt. Geprüft sind außerdem `docs/modellannahmen/annahmen.toml` und `docs/quellenkataster/quellen.toml`, beide per Skript.
Gesamturteil: Trägt mit Auflagen. Was ich stichprobenhaft nachgerechnet habe, stimmt. Die drei Klassen, die Begründungspflicht am tragbaren Preis und die Sperre bei einem fest gesetzten Wert sind in Text und Code gleich gebaut. Die Zählungen der Pflichteingaben, der 43 Werte und der fünf Lesarten stimmen.
Für Revision und Gremium bleiben vier Lücken:
- Die Liste der Abweichungen lässt sich umgehen, wenn der Auftrag die Voreinstellungen nicht mitführt.
- Die Festschreibung nach der Durchsicht erklärt 53 Sollwerte mit einem einzigen Sammelmuster. Das ist ein Rückfall hinter Runde 2.
- Zehn „feste Katalogwerte“ haben weder Quelle noch einen Verantwortlichen.
- Das Blatt sagt nicht, mit welchem Stand der Hauswerte gerechnet ist.

Dazu kommen rund 20 Reststellen aus der Zeit vor der Durchsicht, darunter eine falsche Zahl.
Note: **8 von 10** (Runde 2: 8). Zur 9 fehlen die Befunde 1 bis 5. Alle lassen sich im Dokument und im Referenzrechner beheben, ohne Zuarbeit von außen. Die Reststellen (Befunde 6 bis 8) sind ein halber Tag Gegenlesen.

## Befunde aus Runde 2

| Nr. | Befund Runde 2 | Stand | Nachweis |
|---|---|---|---|
| 1 | Zwei Lockerungen gelten als „strenger“ | **behoben** | Es gibt keine Richtung mehr. Maßstab ist der tragbare Preis (R-3.2 Nr. 5). H-25 wird gegen den aufgelösten Wert verglichen. H-09 ist fester Hauswert. RF-19: „fester kalkulatorischer Zins 1 %“ ergibt M-20 (+42.131 Euro). |
| 2 | Die Liste lässt sich über Voreinstellungen und Katalogwerte umgehen | **teilweise** | Die Regel ist behoben (R-3.1, R-3.2 Nr. 2): E-11 mit 3 % statt KAT-01 ergibt M-20 (+157.482 Euro). Durchgesetzt wird sie aber nur, wenn der Auftrag die Voreinstellung mitführt; sonst wird ohne Liste gerechnet (neuer Befund 1). |
| 3 | Die Proben rechnen die Steuer nicht nach | **behoben** | P-15 (e), P-16 mit den Sätzen des Auftrags und mit der Steuer, P-20 und P-21. Die Fehlerbilder in RF-16 verändern jetzt die Rechnung. Der Lauf meldet jedes Bild mit der genannten Probe. |
| 4 | Herkunft und Vergleich tragen keine Katalogänderung | **offen (teilweise)** | Eine Änderung der Körperschaftsteuer erscheint jetzt als abweichender Wert „KAT, steuer.kst_satz“ (RF-20). Es fehlen weiter: Quelle und Stand je Katalogwert und der Stand der Hauswerte (neuer Befund 4). Dem Vergleich fehlen Teile des Blatts (neuer Befund 9). |
| 5 | Die Warnschwellen haben keine Wirkung | **behoben** | R-10.25, M-48, Werte in A.4, zwei Fälle in RF-20 |
| 6 | Übernommenes Darlehen: Voreinstellung „Förderdarlehen: ja“ | **anders entschieden, vertretbar** | Das Kennzeichen ist entfallen. Es wird immer mit Vorfälligkeit gerechnet; das ist die vorsichtige Seite. Die Wirkung ist als V-03 benannt (+0,40 % des Preises, nur bei Verkauf vor dem Bindungsende). |
| 7 | Freigabeblatt fehlt | **bewusst außerhalb dieser Runde** | `TASKS.md` und R-3.4 sind jetzt stimmig. Die Grundlage im Dokument ist in drei Punkten noch nicht eindeutig: die Klasse von H-35, die Vervielfachung „je Investorensicht, Vorhabensart und Nutzungsart“ und der Stand der Hauswerte (neue Befunde 3 bis 5). |
| 8 | Sammelmuster heben die Ursachenpflicht auf | **mit Runde 2 behoben, mit der Durchsicht wieder offen** | `ursachen-runde2.json` hat 224 verankerte Muster, jedes trifft einen Wert. `ursachen-durchsicht.json` dagegen hat breite Muster (neuer Befund 2). |
| 9 | Zwei Kennzahlen mit demselben Namen | **behoben** | „Kapitaldienstreserve laut Finanzplan“ (R-10.21) und „Reserve nach Bemessung“ (R-10.24) |
| 10 | Einzelne Widersprüche | **behoben** | Kapitel 17 zu NF-12 mit `MA-038`. Die Zählung in R-3.6 stimmt (siehe unten). Tranchenschlüssel `Z-B6.BANK` und weitere in R-4.1. Die Summenregel gilt auch für Zeilen (R-12.5, R-12.7). |

**Grundlage für das Freigabeblatt (Auftrag Nr. 1).** Die Liste je Klasse ist vollständig, die Zählung stimmt:
- **27 Vorgaben:** H-01 mit drei Werten, H-06 mit acht, H-30 mit drei, dazu 13 einzelne Werte.
- **16 feste Hauswerte:** darunter H-17 mit drei Werten.
- **10 feste Katalogwerte:** H-10; H-20 mit zwei Werten; H-23; H-27; H-29 mit zwei; H-31, freie Zeit; H-37 mit zwei.
- dazu die Suchparameter H-21 und die fünf Lesarten.

Einen Wert als Voreinstellung nennt das Dokument nur bei H-09, H-11, H-25, H-26, H-32, H-33 und H-38. Alle übrigen Werte stehen nur als „Annahme der Beispiele, keine Vorschläge“ in A.4. Die Vorschläge muss also die Projektleitung setzen; das ist so beabsichtigt. Eindeutig ist die Grundlage erst nach den Befunden 3 bis 5.

## Eigene Nachrechnung

Die Skripte liegen unter `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/pruefrunde-fachspezifikation-3/controller/`:
- `kennungen.py`
- `ma_abgleich.py`
- `quellen_abgleich.py`
- `klassen_abgleich.py`
- `ursachen_reichweite.py`
- `voreinstellung_fehlt.py`
- `altzahlen.py`
- `beispiel_r32.py`

Ergebnisse:
- **Läufe:** `python3 referenzfaelle.py` besteht 1.093 von 1.093 Prüfungen und endet mit 0; `erwartete_werte.json` hat 490 Werte, wie R-15.2 sagt. `python3 beispielwerte.py` endet mit 0.
- **Zählungen gegen die Tabellen:**
  - Pflichteingaben: zwölf im Ankauf, vierzehn im Neubau.
  - Vorbelegte Felder: je sieben, wenn E-41 und E-42 als ein Feld zählen.
  - Masken je Fall nach R-3.6: alle Gesamtzahlen stimmen (19, 20, 21, 21, 31, 21, 25, 24).
  - Vorgaben je Klasse: 27, 16 und 10.
  - Freigabe: 43 Werte und fünf Lesarten.
  - Fragen nach außen: zehn, fünf und drei.
  - Vereinfachungen V-01 bis V-22; NF-01 bis NF-70 ohne Lücke.
  - Entfallene Eingabewerte: zwölf.
  - Herkunft im Auftrag: E 64, H 50, KAT 37, MA 5 stimmt mit dem Code überein.
  - Abweichungen: Die Klammerwerte in R-3.6 und die Zahl der verglichenen Größen stimmen nicht (Befunde 10 und 7).
- **Beispiel in R-3.2:** Die Zeilen ohne festgeschriebenen Sollwert habe ich selbst gerechnet und alle getroffen.
  - Zinsbindung 5 statt 10 Jahre: −44.943,46 Euro Endwertdifferenz, −26.475 Euro Preis, −0,16 Prozentpunkte.
  - Mietsteigerung 2,5 %: +165.880,04 Euro, +97.715 Euro, +0,56 Prozentpunkte.
- **Kennungsabgleich (`kennungen.py`):**
  - Keine Kennung wird verwendet, ohne definiert zu sein.
  - 14 der 22 V-Kennungen stehen nur in der Liste und nicht an ihrer Regel. Die Regel sagt dort „benannte Vereinfachung, Kapitel 16“; nur R-6.11 und R-7.3 nennen die Nummer. Für Code und Tests, die nach CLAUDE.md die Kennung tragen sollen, ist das ein Hinweis, aber kein eigener Befund.
  - Wo entfallene Kennungen noch als geltend genannt sind, steht das in Befund 6.

## Befunde

1. **[wichtig · belegt] R-3.1, R-3.4, R-3.7, M-20. Ob die Liste „Abweichungen vom Hausstandard“ erscheint, hängt davon ab, was der Aufrufer liefert.**
   - *Widerspruch im Text:* R-3.4 sagt „Der Auftrag trägt den für das Vorhaben aufgelösten Wert“. R-3.2 braucht für die Liste aber den Wert des Hausstandards und den des Vorhabens nebeneinander. Nur mit beiden lässt sich auch erkennen, dass ein Vorhaben einen festen Wert ändert (M-20). R-3.1 verlangt das Mitführen nur für die Eingaben mit Voreinstellung. R-3.7 prüft nicht, ob es geschehen ist.
   - *Beleg (`voreinstellung_fehlt.py`):* Ankauf mit Erwerbsnebenkosten 3 % statt 10 %. Führt der Auftrag die Voreinstellung mit, endet der Lauf mit M-20. Fehlt sie (`voreinstellungen = None`, im Code ausdrücklich „die Eingaben sind der Hausstandard“), rechnet der Kern ohne Meldung und mit leerer Liste. Der tragbare Preis liegt dann um 157.482 Euro höher.
   - *Folge:* Ein Programmfehler in der Oberfläche oder ein Import ohne dieses Feld hebt den Schutz gegen Schönrechnen auf, und das Blatt sieht hauseinheitlich aus. Maßstab: ICAEW-FMC (kontrollierte Eingaben) und OWASP ASVS (serverseitige Prüfung, nicht beim Aufrufer).
   - *Vorschlag:*
     - In R-3.1 festlegen, dass der Auftrag für jede Vorgabe den Hauswert und gegebenenfalls den Vorhabenswert getrennt führt.
     - In R-3.7 als Schritt 3a ergänzen: Fehlt zu einer voreingestellten Eingabe die Voreinstellung mit Herkunft, gibt der Kern M-20 aus.
     - Katalog-Voreinstellungen wie E-11 aus KAT-01 und E-38 aus KAT-15 löst der Kern selbst aus dem Katalog des Auftrags auf. Er kennt diese Werte ohnehin.
     - Dazu ein Fall in RF-20.

2. **[wichtig · belegt] R-15.2; `ursachen-durchsicht.json`, `aenderungen-runde2.md` (Abschnitt „Durchsicht“). Die Festschreibung nach der Durchsicht erklärt Gruppen, nicht einzelne Werte. Das ist ein Rückfall gegenüber Runde 2.**
   - *Was R-15.2 verlangt:* „Die Ursache wird je Wert unter seinem vollen Namen angegeben.“
   - *Was die Datei tut:* Keines der 18 Muster ist ein voller Wertname (`ursachen_reichweite.py`). Das Muster `[Ss]tressfall|Stressgroessen einzeln|Basis und Stress|Bankfall \(Zins 3 %` trifft 53 der 490 Sollwerte in vier Fällen. Davon hat die Durchsicht 32 geändert. Der Ursachensatz verbindet zwei verschiedene Ursachen: „Stressgröße Instandhaltung entfallen“ und „H-25 statt Lesart 2“.
   - *Folge:* Eine unbeabsichtigte Änderung irgendeines Stresswerts wäre in dieser Festschreibung ohne Fehler durchgegangen. Ob die 32 Werte allein aus dem Wegfall der Instandhaltung folgen, lässt sich nicht nachprüfen. Die Leitgrößen sind plausibel: Der Preis im Stressfall steigt um +0,67 %, wie V-22 sagt.
   - *Warum die Sperre nicht greift:* `schreibe_fest` lehnt nur Muster ab, die einen ganzen Fall treffen. Ein Muster, das quer über vier Fälle 53 Werte trifft, besteht diese Probe.
   - *Weitere Lücken:*
     - Die geänderten Sollwerte im Code stehen nur von Hand im Bericht. Eine Zeile lautet „RF-16, RF-19, RF-20: Tests zu … | entfallen“, ohne einzelne Werte; eine Datei nach Art von `im-code-*.json` gibt es nicht.
     - Die Basisdateien der Differenzberichte (441 und 526 Werte) sind nicht abgelegt.
   - *Vorschlag:*
     - Die Ursachen der Durchsicht je Wert mit verankertem vollem Namen neu erzeugen, wie in `ursachen-runde2.json`.
     - `schreibe_fest` lehnt künftig jedes Muster ab, das mehr als einen Wert trifft.
     - Eine Datei `im-code-durchsicht.json` anlegen.
     - Die Basisstände neben den Berichten ablegen.
     - R-15.2 nennt den Abschnitt „Durchsicht“ und `ursachen-durchsicht.json`.

3. **[wichtig · belegt] R-3.2 Nr. 1 (c), R-3.4 (Klasse „fester Katalogwert“), `docs/quellenkataster/quellen.toml`. Zehn Werte mit Wirkung auf das Ergebnis haben weder Quelle noch Verantwortlichen.**
   - *Definition:* „Fester Katalogwert: Wert mit Quelle im Katalog, ohne Freigabeentscheidung des Hauses.“
   - *Beleg:* Für H-10, H-20, H-21, H-23, H-27, H-31 (freie Zeit) und H-37 gibt es keinen Eintrag im Kataster (`quellen_abgleich.py`, Suche nach Begriff und Kennung). H-29 hat für den Preis `BEHG`, für die Steigerung keine Quelle. Es sind Annahmen des Hauses oder der Bank, keine Normwerte:
     - Forderungsausfall 0,5 % (H-27): −0,57 % Preis bei 1,5 %.
     - Bereitstellungsfreie Zeit (H-31): Neubau +0,60 % der Gesamtkosten, +7,26 % des tragbaren Grundstückspreises bei 12 statt 6 Monaten (Durchsicht, Zeile H-31). Sie ist zugleich Frage 7 an die Hausbank.
     - Anpassungsdauer (H-23), Kontokorrentzins (H-10), Bauabschnitte (H-37).
   - *Folge:* Fragt die Bank „Woher kommen 0,5 % Forderungsausfall?“, hat niemand den Wert freigegeben, und eine Quelle gibt es nicht. Nach R-3.2 darf ihn kein Vorhaben ändern und keine Geschäftsführung freigeben. Maßstab: CLAUDE.md, Abschnitt Quellen („keine … Angabe ohne Eintrag im Kataster“), FAST („keine versteckten Konstanten“), Rolle Controller (Rückverfolgung jeder Zahl).
   - *Vorschlag:* Je Wert eine der beiden Lösungen:
     - Eine Katasterkennung, auch der Art „Kondition der Hausbank, Stand“ oder „Statistik, Stand“.
     - Oder Umstufung zum festen Hauswert auf dem Controlling-Teil des Freigabeblatts. Für H-23, H-27, H-31 (freie Zeit) und H-10 ist das der passende Ort.
     - Für H-20 und H-21 reicht die Kennung „Festlegung der Entwicklung“ mit NF-Nummer.

4. **[wichtig · belegt] R-3.2 Nr. 1 und Nr. 3, R-3.4, R-11.11, R-11.12. Das Blatt sagt nicht, mit welchem Stand der Hauswerte und des Katalogs gerechnet ist.**
   - *Was fehlt:* Feste Hauswerte ändert man „mit Name und Datum“ (R-3.2). Einen Vorgabenstand mit Kennung, „gültig ab“ und „freigegeben von“ führen aber weder der Auftrag (R-3.1) noch der eingefrorene Stand (R-11.11) noch das Blatt (R-11.12 nennt nur „Standkennung, Regelstand und Version des Kerns“). Auch die Klasse `Vorgaben` hat dafür kein Feld; das war schon Runde 2, Befund 7.
   - *Ungleich behandelt:* R-3.2 Nr. 3 zeigt eine umgeschaltete Lesart und H-38 „sofort“ auf dem Blatt. Andere Hauswerte, die das Haus von ihrer genannten Voreinstellung wegstellt, zeigt es nicht, und der Code (`vorgaben_im_vorhaben`) ebenso wenig:
     - H-11 Linie „unbegrenzt“ statt null; nach NF-06 verdeckt das den Eigenkapitalbedarf.
     - H-26 Fluktuation über null.
     - H-32 und H-33, etwa ein Mindestansatz von 10 % statt KAT-14. Nach R-5.12 bindet dann im Neubau der Reinertrag des Vorhabens, und das Darlehen steigt.
   - *Folge:* Zwei Gremienvorlagen mit verschiedenen Hausständen sehen gleich aus. Den Unterschied zeigt erst ein Vergleich mit Auftragsdaten. Maßstab: Rolle Controller (welche Version beschlossen wurde) und OWASP ASVS (lückenloses Änderungsprotokoll).
   - *Vorschlag:*
     - Je eine Kennung für Vorgaben- und Katalogstand (gültig ab, freigegeben von, am) im Auftrag, im eingefrorenen Stand und im Kopf des Blatts.
     - R-3.2 Nr. 3 auf jeden Hauswert mit Voreinstellung ausdehnen, oder das Wort „Voreinstellung“ bei Hauswerten durch „Vorschlag für die Freigabe“ ersetzen.

5. **[wichtig · belegt] R-3.4, Durchsicht Zeile 228, `grobkalkulation.py` (`FESTE_KATALOGWERTE`). Die Klassen sind an drei Stellen widersprüchlich, und die Grundlage des Freigabeblatts ist nicht eindeutig.**
   - *H-35:* Das Dokument führt H-35 als „Vorgabe; Voreinstellung von E-23“ unter den 27 Werten für die Geschäftsführung, ebenso die Durchsicht („vier Voreinstellungen … Vorlauf“). Der Referenzrechner führt `"vorlauf": "H-35"` als festen Katalogwert (`klassen_abgleich.py`). Was soll die Geschäftsführung also freigeben?
   - *Wortlaut aus der Zeit vor der Durchsicht:*
     - NF-40 und R-5.18: „Satz und freie Zeit sind Vorgaben des Hauses“. Gilt jetzt: Hauswert und Katalogwert.
     - NF-06: „Kontokorrentlinie als Vorgabe“. Gilt jetzt: H-11 fester Hauswert.
     - NF-44: „Fluktuation als Vorgabe“. Gilt jetzt: H-26 fester Hauswert.
     - R-3.4 zu H-33: „deshalb ist der Wert Vorgabe und nicht Katalogwert“. Gilt jetzt: fester Hauswert.
   - *Vervielfachung:* Der Kopf von R-3.4 sagt „Werte je Investorensicht, Vorhabensart und Nutzungsart“. Die Zahl 43 vervielfacht aber nur H-01 (drei Werte); H-19 „je Nutzungsart“ zählt einmal. Je nachdem, wie man den Kopfsatz liest, sind es 43 oder ein Vielfaches. Diese Frage war schon in Runde 2 gestellt (Befund 7).
   - *Vorschlag:* H-35 im Code zur Vorgabe machen, oder im Dokument zum Katalogwert (dann 26 statt 27). Die vier Stellen auf die Klasse nachziehen. Im Kopf von R-3.4 festlegen, dass in 1a nur H-01 nach Vorhabensart und Förderung unterschieden wird und alle anderen Werte einmal je Haus gelten.

6. **[Hinweis · belegt] Reststellen: Entfallene Regeln, Kennungen und Schalter werden als geltend genannt (Zeilen der Fassung vom 2026-11-21; `kennungen.py`).**
   - **R-6.17 (entfallen)** als geltender Bezug:
     - Z. 489 (R-5.12: „Bewirtschaftung_n … nach R-6.8, R-6.9 und R-6.17“);
     - Z. 635 (R-6.7: „trägt die Betriebskosten leerstehender Flächen (R-6.17)“);
     - Z. 1023 (R-10.22: „Die Bewirtschaftung enthält die Betriebskosten leerstehender Flächen …“).
   - **H-36 (entfallen):** A.4, Z. 1734: „Betriebskosten leerstehender Flächen 0 Euro, in den bezeichneten Fällen 30 Euro“.
   - **E-52 (entfallen):** Z. 667 (R-6.16): „das Eingabefeld E-52 sagt das“.
   - **H-25 je Tranchenart (entfallen, V-07):** Z. 499 („H-25 der Tranchenart“), Z. 527 („4 % für übernommene Darlehen (H-25)“; dazu Befund 7) und A.4, Z. 1732 („kalkulatorischer Zins für jede Tranchenart“).
   - **Schalter, die es nicht mehr gibt:**
     - NF-07 „zwei weitere Regeln wählbar“;
     - NF-15 „Modernisierung aktiviert“ (V-13);
     - A.5, Fall RF-13: „Lesarten von `MA-030` … wie bezeichnet“;
     - R-10.12: „Die andere Lesart ist umschaltbar“ (`MA-027`);
     - R-5.3: Rundung „je Darlehen umstellbar“ (`MA-013`). Das ist ein Schalter je Vorhaben ohne E- oder H-Kennung, der in keiner Liste erscheint. Für 1a sollte dort stehen „Darlehensbaustein; in der Grobkalkulation kaufmännisch“.
   - **Sonstige:**
     - A.6: E-05 „im Gebiet (Voreinstellung)“, obwohl E-05 im Neubau keine Eingabe ist;
     - R-11.14, Z. 1145: „Ausprägung von H-01 (R-3.3)“ statt R-3.4;
     - Kapitel 17: Die Legende der Spalte „Stand“ kennt „Durchsicht“ nicht, die Tabelle verwendet es;
     - Kataster: `CO2KOSTAUFG-5A`, „verwendet für“, nennt noch „Eingabe E-66“ und „E-67“.
   - *Vorschlag:* Die Stellen nachziehen. Dazu `kennungen.py` als festen Test neben RF-20 führen: Er meldet jede Nennung einer entfallenen Kennung außerhalb ihrer Entfall-Zeile und der Liste V-01 bis V-22.

7. **[Hinweis · belegt] Zahlen aus altem Stand ohne Kennzeichnung oder ohne Beleg im Referenzrechner.**
   - *Falsch:* R-5.12, Z. 527: „Mit einem festen kalkulatorischen Zins von 4 % … 826.660,00 Euro“. Mit H-25 als einem Wert für alle Tranchen rechnet der Referenzrechner 964.436,66 Euro (`altzahlen.py`).
   - *Veraltet:* R-11.11 und R-11.12 nennen „36 Größen“, der Sollwert ist 35, weil „Darlehen zu Wertansatz“ entfallen ist. R-11.11 zählt „Begründungen“ zu den abweichenden Werten, der Sollwert nicht.
   - *Skript druckt veraltete Literale:* `beispielwerte.py`, Z. 214 druckt den „KfW-Vorteil“ als Differenz fest eingetragener Zahlen: 221.477 und 409.454 Euro. Das Dokument nennt 217.668 und 406.373 Euro (Kapitel 17, Setzung 10).
   - *Nicht als Sollwert geführt, aber nachrechenbar:* 1.034.436,66, 2.425.000,00 und 1.283.299 Euro aus der früheren Lesart 2. Ich treffe alle drei mit H-25 = 0 %.
   - *V-06 nur eingeschränkt richtig:* „ein fester Satz in Höhe des Vertragszinses ergibt dasselbe … auf den Cent“ gilt nur ohne fremde Tranche mit niedrigerem Zins. Im gebundenen Bestand ergeben 4 % ein Darlehen von 964.436,66 statt 1.034.436,66 Euro und einen Preis von 2.269.324 statt 2.271.869 Euro. Das sind −0,11 %, also unter der Schwelle. Gleich auf den Cent ist nur H-25 = 0 %.
   - *Vorschlag:* Z. 527 berichtigen. „35“ setzen. Die Literale in `beispielwerte.py` durch die Rechnung ersetzen. V-06 und R-5.12, Z. 515, auf „H-25 = 0 %“ fassen. Die drei Werte der Lesart 2 als Sollwerte mit H-25 = 0 % festschreiben.

8. **[Hinweis · belegt] `docs/modellannahmen.md` (Daten in `annahmen.toml`) weicht vom Dokument ab (`ma_abgleich.py`).**
   - *Gewicht von `MA-032`:* R-7.15 („`MA-032`, Gewicht mittel“) und die Tabelle in Kapitel 17 sagen „mittel“, das Verzeichnis sagt „gering“.
   - *„Umschaltbar: ja“:* Das Verzeichnis führt das für `MA-002`, `MA-003`, `MA-005`, `MA-013`, `MA-017` und `MA-027`, dazu für `MA-001` und `MA-004` (Teil 2). Das Dokument kennt in 1a nur die fünf Lesarten des Hauses und H-38. Wer das Freigabeblatt aus dem Verzeichnis zieht, findet mehr Schalter, als der Kern hat.
   - *Vorschlag:* Das Gewicht angleichen. Das Feld `umschaltbar` dreiwertig machen: „Lesart des Hauses in 1a“, „vorgemerkt für Teil 2“, „nein“.

9. **[Hinweis · belegt] R-11.11 gegen R-11.12 und R-11.7; `vergleiche`, `BLATTGROESSEN`, `PREISGROESSEN`. Der Vergleich zweier Fassungen deckt das Blatt noch nicht ganz ab.**
   - *Was dem Vergleich fehlt:*
     - der Faktor auf die Ist-Miete im Basis- und im Stressfall;
     - der höchste Stand der Zwischenfinanzierung;
     - die Liste der Abweichungen vom Hausstandard;
     - beim tragbaren Preis das nötige Eigenkapital, der Eigenkapitalbedarf insgesamt, die Grenze des Darlehens und die beiden Deckungen nach R-11.7.
   - *Kernversion:* Ihre Wirkung ist weiter nur ein Kennzeichen (`versionsgleich`), keine Rechnung desselben Auftrags unter beiden Versionen, wie R-11.11 sie beschreibt.
   - *Folge:* Steigt bei gleichem Preis das nötige Eigenkapital, zeigt der Vergleich das nicht.
   - *Vorschlag:* `BLATTGROESSEN` und `PREISGROESSEN` aus der Liste in R-11.12 und R-11.7 ableiten, statt sie getrennt zu führen. In R-11.11 sagen, dass der Referenzrechner nur eine Version kennt und die Versionsrechnung Sache des Produkts ist.

10. **[Hinweis · belegt] R-3.6: Die Klammerwerte folgen einer anderen Zählregel als der Satz darüber.**
    - *Der Satz:* „In Klammern die Felder ohne Voreinstellung.“
    - *Die Zählung:* Gezählt sind tatsächlich die Felder, die man im Fall tippen muss. E-31, E-50, E-56 und E-35 haben die Voreinstellung 0 und sind als „zu tippen“ mitgezählt. Nach dem Satz wären es 13 (leere Fläche), 12 (Investitionsstau), 17 (gebundener Bestand) und 15 (KfW) statt 14, 13, 19 und 16.
    - *Und:* „Je sieben vorbelegte Felder“ stimmt nur, wenn E-41 und E-42 als ein Feld zählen.
    - *Vorschlag:* Den Satz auf „davon im Fall zu tippen; eine Voreinstellung 0 zählt mit, wenn der Fall den Wert verlangt“ ändern. E-41 und E-42 als „ein Feld je Steuerstatus“ bezeichnen.

## Nicht geprüft

- Fachliche Richtigkeit der Steuer-, Förder- und Bankregeln und der Katalogwerte: Das ist Sache der Rollen Steuerberater, Fachexperte und Bank. Keine Quelle am Original gelesen.
- Keine eigene Fehlerinjektion in die Rechnung wie in Runde 2. Befund 3 aus Runde 2 ist am Lauf der Fehlerbilder in RF-16 beurteilt.
- Die 32 Stresswerte der Durchsicht sind nicht einzeln nachgerechnet, nur die Leitgrößen gegen V-22.
- Der Code des Referenzrechners außerhalb der genannten Teile, die Blindrechnung und `wesentlichkeit.py` nicht Zeile für Zeile; `docs/entscheidungen.md` nur auf die Einträge vom 2026-11-21.
