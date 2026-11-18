Rolle: Controller (Controlling des Wohnungsunternehmens)
Prüfobjekt: `docs/fachspezifikation-rechenkern.md` (Teil 1, Stand 2026-11-18, vollständig gelesen) und Referenzrechner `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner/` (alle Module gelesen außer den `rf_*.py` im Einzelnen; Lauf ausgeführt)
Gesamturteil: Trägt mit Auflagen. Die Rechnung ist nachvollziehbar und stimmt: Der Lauf besteht mit Rückgabewert 0 (529 von 529), drei eigene Stichproben treffen jeden Wert auf den Cent, und die Ordnung aus Eingabe, Vorgabe des Hauses und Katalogwert ist sauber angelegt. Gegenüber Geschäftsführung, Bank und Revision lässt sich das Modell aber noch nicht vertreten: Die Kontrollsummen sperren die Preissuche nicht, die Eingabeliste hat Lücken bei Standort und übernommenem Darlehen, einzelne Fristen stehen fest im Regeltext und im Code, und zwei Abstimmungen fehlen (Steuer, Unterlassensalternative).
Note: 7 von 10. Zur 9 fehlen die Befunde 1 bis 6. Sie sind fast alle im Dokument zu beheben, die Befunde 1, 3 und 4 zusätzlich im Referenzrechner. Befund 7 betrifft die Abnahme des Referenzrechners und braucht Zuarbeit außerhalb des Dokuments (Excel-Gegenrechnung, Parallelrechnung echter Projekte).

## Eigene Nachrechnung

- `python3 referenzfaelle.py`: 15 Fälle, 529 Prüfungen, alle bestanden, Rückgabewert 0, Laufzeit 17 s.
- Stichprobe 1, RF-11 Ankauf (eigenes Skript ohne Module des Referenzrechners): Mietpfad 8,5000 / 8,7210 / 9,0358 / 9,4473 / 9,9584 / 10,1575; Reinertrag 103.035,24; B = 1.431.044,99 mit Rate 7.155,22 und Deckung 1,2000008; Eigenkapital 1.208.955,01; Miete im Jahr 13 11,6678; Verkaufspreis 3.326.730,48; Verkaufskosten 49.900,96; Restbuchwert 2.164.800,00; Verkaufsgewinn 1.112.029,52; Steuer darauf 117.319,11 + 155.680,00 = 272.999,11. Alle Werte wie im Dokument (R-6.3, R-6.12, R-5.12, R-8.1 bis R-8.5, R-7.4, R-10.16).
- Stichprobe 2, RF-10 Personengesellschaft, Tabelle R-7.9: alle fünf Zeilen getroffen (Gewerbeertrag 75.500, Messbetrag 2.642,50, Steuer 42.000,00 / 42.000,00 / 44.114,00 / 47.285,00 / 10.570,00).
- Stichprobe 3, RF-12 Grobförderung (R-11.14, R-8.7): zuwendungsfähig 8.540.000; Förderdarlehen 5.124.000,00; Zuschuss und Mindesteigenkapital je 1.708.000,00; Entgelte 64.050,00; Mittelbedarf 8.900.050,00; A = 619.400,00; C = 360.050,00; Rückzahlung nach 240 Monaten 805.200,00. Alle Werte getroffen.
- Fehlerinjektion und Rundungsvergleich: Skript `gating.py` im Scratchpad (Befunde 1 und 8).

## Befunde

1. **[kritisch · belegt] R-13.1, R-11.5, R-11.10; Referenzrechner `grobkalkulation.py` (`rechne_grob`, Zeilen 414 bis 448, `_rendite_minus_ziel`, `suche_eingabe`). Eine verletzte Kontrollsumme sperrt das Ergebnis nicht.** R-13.1 und die Spezifikation (Kapitel 3, Kontrollsummen, **fest**) sagen: keine Ergebnisse ohne bestandene Proben. Im Referenzrechner werden die Kennzahlen aber vor den Proben gebildet und auch bei Befunden zurückgegeben. Preissuche, Zielwertsuche und Haltedauertabelle lesen die Rendite, ohne `befunde` anzusehen.
   - *Beleg:* P-04 künstlich verletzt. Der Lauf liefert trotzdem eine Rendite von 5,1617 %, und `tragbarer_preis` gibt unverändert 2.425.585 Euro aus.
   - *Lücke im Dokument:* Es regelt nicht, was geschieht, wenn eine Probe an einer der rund 60 Stützstellen der Suche verletzt ist. Im Normalfall sind alle 61 Läufe ohne Befund; ein Gebot dürfte im Fehlerfall aber nicht entstehen.
   - *Vorschlag:* R-11.5 und R-11.10 ergänzen: Jeder Lauf der Suche durchläuft Kapitel 13. Ein Befund an einer Stützstelle bricht die Suche mit M-10 ab und nennt Stützstelle und Probe. Im Referenzrechner `kennzahlen` erst nach leerer Befundliste setzen und dafür einen eigenen Test anlegen (Fehlerbild wie bei P-05).

2. **[wichtig · belegt] R-3.3, E-11, KAT-01, KAT-04, KAT-08, E-59, R-5.8. Die Eingabeliste ist an zwei Stellen unvollständig.**
   - *(a) Der Standort fehlt.* KAT-01 gilt „nach Land“, der Hebesatz in KAT-04 und die Kappungsgrenze in KAT-08 gelten „je Gemeinde“. Es gibt aber keine Eingabe für Land und Gemeinde. Damit lässt sich nicht zurückverfolgen, warum ein Vorhaben mit 400 % Hebesatz und 15 % Kappung gerechnet wurde. Bei fünf Ländern im Schwerpunkt ist das der häufigste Rückfragepunkt der Revision.
   - *(b) Beim übernommenen Darlehen fehlen zwei Werte.* R-5.8 nennt den Anschlusszins eines übrigen Darlehens „Eingabe (E-59)“. E-59 führt aber nur Restschuld, Zins, Tilgungssatz und Ende der Zinsbindung, und R-3.6 zählt „die vier Werte von E-59“. Der Referenzrechner verlangt zusätzlich `anschluss_zins` und `beitrag_satz` (`_tranche_uebernommen`). Fehlt der Anschlusszins, endet der Lauf mit M-24, also ist die Angabe Pflicht.
   - *Vorschlag:* E-03 „Gemeinde (amtlicher Gemeindeschlüssel)“ als Pflichteingabe aufnehmen, aus der KAT-01, KAT-04 und KAT-08 aufgelöst werden. E-59 um Anschlusszins (Pflicht, wenn die Haltedauer über die Bindung reicht) und laufenden Beitrag erweitern; R-3.6 nachziehen (Ankauf gebundener Bestände: 27 oder 28 statt 26).

3. **[wichtig · belegt] R-6.3, R-6.5, M-36 (R-6.10); Referenzrechner `ertrag.py` (`kappung_jahre=3`, `fest_jahre=3`, `schritt_jahre=3`), `grobkalkulation.py` (`geb_fest_jahre: int = 3`, `geb_schritt_jahre: int = 3`, `startjahr: int = 2027`, `suchobergrenze_faktor = D(100)`). Versteckte Konstanten (Verstoß gegen FAST und ICAEW sowie gegen R-3.1 und die eigene Leseregel, Zeile 12: „Fristen … nie Festwerte“).**
   - *Im Regeltext:*
     - R-6.3 schreibt den Kappungszeitraum fest: „Basis_j = Miete_(j−3)“. KAT-08 führt den Zeitraum aber als Katalogwert („Kappungsgrenze und ihr Zeitraum“).
     - M-36 nennt „ersten drei Jahre“ und „15 %“ als Festwerte zu `ESTG-6`, ohne Katalogkennung.
     - R-10.18 legt −99 % bis +1.000 % und 2.000 Schritte fest, ohne NF-Kennzeichnung.
     - R-11.5 setzt 41 Stützstellen, obwohl H-21 das Raster als Vorgabe führt.
   - *Im Code:* `anpassungspfad` wird nie mit einem Zeitraum aus dem Auftrag aufgerufen. Der Wert 3 ist dort fest verdrahtet. Feste Jahre und Schrittjahre der übernommenen Bindung im Ankauf sind Voreinstellungen der Eingabeklasse, obwohl KAT-11 nur die Steigerung führt.
   - *Herkunft im Code:* Die Klasse `Vorgaben` mischt Werte des Hauses mit Katalogwerten (`kappung` = KAT-08, `afa_satz` = KAT-07) ohne Herkunftsangabe. R-3.1 verlangt die Herkunft je Wert.
   - *Vorschlag:* R-6.3 mit `κ_Jahre` aus KAT-08 schreiben. KAT-11 um „feste Jahre, Schrittjahre“ ergänzen. M-36 auf KAT-12 (`ESTG-6`: Zeitraum, Quote) umstellen. Rasterzahl und Bereich der Suchen als H-21 mit Voreinstellung führen, die Grenzen des internen Zinsfußes als NF kennzeichnen. Im Referenzrechner alle Werte über den Auftrag führen, ohne Voreinstellungen in den Eingabeklassen, mit einem Feld `herkunft` (E/H/KAT) je Wert. Ein Test soll sicherstellen, dass `grep` auf Zahlenliterale in den Kernmodulen leer bleibt, bis auf eine Liste erlaubter technischer Konstanten.

4. **[wichtig · belegt] Kapitel 13, R-13.3; Referenzrechner `proben.py`, `rechne_alternative`. Zwei Abstimmungen fehlen, eine ist zu schwach.**
   - *(a) Es gibt keine Steuerprobe.* Steuer, Verlustvortrag und Anrechnung sind die fehleranfälligsten Nebenrechnungen. Keine Probe stimmt sie ab: Fortschreibung des Vortrags (Anfang + Verlust − Verrechnung = Ende, je Steuerart), die Steuer je Jahr gleich der Summe der Steuerarten abzüglich Anrechnung, und die Ergebnis-Zahlungs-Brücke über die Laufzeit (Summe e_op + g_v = Summe der originären und derivativen Zahlungen ohne Eigenkapital und Steuer, zuzüglich Summe der Abschreibungen, abzüglich Investition, zuzüglich Buchwertabgang).
   - *(b) Die Unterlassensalternative hat keine eigene Saldo- und Bestandsprobe.* Sie ist ein eigener Finanzplan mit drei Konten (R-9.1), wird aber nur über P-10 und P-11 geprüft. Ein Buchungsfehler in R-9.4 bliebe unbemerkt und würde die führende Kennzahl ΔEW verfälschen.
   - *(c) P-09 ist im Code eine Selbstbestätigung.* `verdichte` summiert dieselben Zeilen, die P-09 nachsummiert, und das nur für vier Größen. Es fehlt die Jahresbestandsprobe, die ein Prüfer tatsächlich macht: Bestand am Jahresende = Bestand am Vorjahresende + Jahresflüsse.
   - *Spezifikation:* Sie verlangt Kontrollsummen für „Steuern“ ausdrücklich nicht. Das Methodenkapitel führt aber explizite Konten für Steuern; Befund 4a ist deshalb die fehlende Abstimmung dieses Kontos.
   - *Vorschlag:* P-15 Steuerprobe und P-16 Probe der Alternative (Saldo und Bestand je Periode) aufnehmen. P-09 als Jahresbestandsprobe für alle Zeilen der Jahresdarstellung fassen.

5. **[wichtig · begründete Einschätzung] R-3.2, R-3.4, M-35, R-11.12. Wer im Vorhaben welche Vorgabe ändern darf und was davon sichtbar wird, ist nur für einen Teil geregelt.**
   - *Was geregelt ist:* R-3.2 erlaubt für H-02 bis H-05 und H-07 nur Verschärfungen; Lockerungen, Zielrendite und Wertansatz meldet M-35 auf dem Blatt.
   - *Was offen bleibt:* Ob H-08 bis H-23 im Vorhaben änderbar sind, regelt das Dokument nicht. Das betrifft gerade die Größen, die den tragbaren Preis am stärksten treiben: Mietsteigerung, Kostensteigerung, Mietausfall, Bewirtschaftungspauschalen, Verkaufskosten, Habenzins.
   - *Szenario:* Ein Bearbeiter hebt im Vorhaben die Mietsteigerung H-12 von 2 % auf 2,5 % an. Der tragbare Preis steigt, aber weder M-35 noch das Blatt zeigen es; die Gremienvorlage wirkt hauseinheitlich, ist es aber nicht. Die Spezifikation verlangt Vergleichbarkeit der Projekte (Kapitel 2, Kennzahlen: festes Blatt je Vorhabensart).
   - *Was zu H-07 fehlt:* Was bei der Auswahl H-07 „verschärfen“ heißt, ist nicht definiert.
   - *Vorschlag:* In R-3.4 eine Spalte „im Vorhaben änderbar: nein / nur verschärfen (Richtung) / frei mit Begründung“. Jede Abweichung von einem H-Wert erscheint auf dem Blatt in einer Zeile „Abweichungen vom Hausstandard“ mit altem und neuem Wert und Begründung, nicht nur die Lockerungen. Für H-07 die Rangfolge der drei Regeln nach Deckung festlegen. Die Rechte (Spezifikation Kapitel 5: Bearbeiter, Prüfer, Verantwortlicher) gehören in die Architektur; der Kern muss die Abweichungsliste zurückgeben.

6. **[wichtig · belegt] R-11.11, R-3.1, Spezifikation Kapitel 3 „Nachvollziehbarkeit“ (fest); Referenzrechner `vergleiche`. Der Vergleich zweier Fassungen und der eingefrorene Stand tragen eine Abstimmung über Versionen hinweg nicht.**
   - *(a) Der Vergleich ist zu schmal.* Der Code vergleicht 6 Kennzahlen, R-11.11 verlangt alle Kennzahlen des Blatts (rund 17). Es gibt auch keine Gegenüberstellung der Eingaben, die sich unterscheiden. Das ist die erste Frage des Controllings: Was wurde geändert, und was hat es bewirkt?
   - *(b) Ein Vergleich über Kernversionen hinweg ist ausgeschlossen.* R-11.11 setzt dieselbe Version des Kerns voraus. Eine im Gremium beschlossene Fassung vom Frühjahr lässt sich damit nach einem Kern-Update nicht mehr mit der heutigen vergleichen. Wie der beschlossene Stand eingefroren und wiedergegeben wird, regelt das Dokument nicht: gespeichertes Ergebnis oder Neuberechnung mit alter Version.
   - *Vorschlag:* R-11.11 um die Liste der abweichenden Auftragswerte (Kennung, A, B) ergänzen. Festlegen: Eine beschlossene Fassung speichert den aufgelösten Auftrag, das Ergebnis und die Kernversion unveränderlich. Ein Vergleich mit anderer Kernversion ist zulässig und weist die Versionswirkung gesondert aus, gerechnet als derselbe Auftrag unter beiden Versionen. Eine Abweichungsbrücke mit schrittweisem Austausch der Eingaben kann für Teil 2 vorgemerkt werden.

7. **[wichtig · begründete Einschätzung] R-15.2, R-15.3, LIESMICH „Woher die Sollwerte stammen“. Die Sollwerte reichen als Abnahmemaßstab für die Rust-Implementierung nicht aus.**
   - *Woher die Sollwerte stammen:* 207 Sollwerte bestätigen nur, dass der Referenzrechner mit sich selbst übereinstimmt. `gegenrechnung.py` stammt vom selben Verfasser mit derselben Lesart der Regeln, deckt nur Testfall und Ankauf als Körperschaft ab und schützt damit vor Programmierfehlern, nicht vor Auslegungsfehlern.
   - *Was unabhängig ungeprüft bleibt:* der ganze Neubau (Mittelabruf, Bauzeitzinsen als Nachschuss, Grobförderung im Finanzplan), die Preissuche und der Stressfall, Personengesellschaft und Privatperson im vollen Finanzplan (RF-13), gebundene Miete und übernommenes Darlehen. Meine drei Stichproben bestätigen nur Bausteine davon (Bemessung, Steuertabelle), keine vollen Pläne.
   - *Weitere Lücken:* `--festschreiben` überschreibt alle Sollwerte ohne Differenzbericht. Und E-02 lässt nur Stichtage „ab dem laufenden Monat“ zu; damit sind Parallelrechnungen abgeschlossener Projekte und spätere Nachkalkulationen ausgeschlossen.
   - *Vorschlag:*
     - Eine Excel-Gegenrechnung von RF-11 und RF-12 (gefördert) im Monatsraster. Sie soll von einer Person aufgebaut werden, die nur das Dokument kennt, nicht den Code; Abweichungen werden je Regel geklärt.
     - Eine Parallelrechnung von zwei bis drei echten Vorhaben des Hauses gegen dessen bisherige Excel- und Bankrechnung, mit erklärter Differenz.
     - Ein echter Tilgungsplan einer Bank gegen R-5.3 (`MA-013`).
     - `--festschreiben` soll die geänderten Sollwerte mit alter und neuer Zahl und der auslösenden Regel ausgeben und den Lauf protokollieren.
     - E-02 für Nachrechnungen auch rückwirkend zulassen; die Sperre gehört in die Oberfläche der Neuanlage.
   - Die Punkte gehören in `TASKS.md` (Auftraggeber: Projektauswahl und Excel-Rechnungen) und in R-15.

8. **[wichtig · belegt] R-12.7, R-2.3; Spezifikation Kapitel 5 „Excel“ (Export mit Summen- und Saldoformeln). Für Summen gerundeter Darstellungswerte gibt es keine Regel.** R-12.7 erlaubt die Darstellung „in vollen Euro“, regelt aber nicht, wie Spaltensummen dann zu den Zeilen passen.
   - *Beleg (RF-11, Jahresdarstellung in vollen Euro):* Die Miete ergibt in der Summe 1.881.048,96, also 1.881.049 Euro. Die Summe der gerundeten Jahreswerte ist 1.881.050, ein Euro mehr; bei der Steuer ebenso 349.828 gegen 349.827.
   - *Folge:* In einer Bankvorlage mit Summenformeln stimmt die Summe dann nicht mit der Anzeige überein. Genau das prüft das Controlling vor jeder Gremienvorlage.
   - *Weiterer Punkt:* R-2.3 zeigt eine Jahresmiete von 54.999,96 statt 55.000 Euro als Folge der Monatsrundung. Das ist regelkonform, verdient aber einen Satz im Fachhandbuch.
   - *Vorschlag:* R-12.7 ergänzen: Export und Bericht führen Cent-Werte und runden nur im Zahlformat. Summen werden aus den ungerundeten Werten gebildet, und die Anzeige in vollen Euro weist Rundungsdifferenzen einmal aus, als Fußnote nach Geschäftsberichtsbrauch. Alternativ wird die gerundete Summe gezeigt und die Differenz auf die größte Zeile verteilt; das wäre zu entscheiden und festzulegen. P-09 erstreckt sich dann auf den Export.

9. **[Hinweis · begründete Einschätzung] R-2.3, R-2.7, R-2.8 (NF-04). Jahresscheiben für die Unternehmensplanung und die Buchhaltung sind nicht angelegt, aber auch nicht verbaut.**
   - *Was fehlt:* Die Jahresdarstellung verdichtet nur nach Planjahr. Beginnt das Vorhaben im Juli, decken sich Planjahr und Geschäftsjahr nicht, und auch die Steuer fällt im Planjahr an. Für die Übergabe in die Unternehmensplanung (GuV-Jahre, Liquidität je Geschäftsjahr) wird eine Verdichtung nach Kalender- oder Geschäftsjahr gebraucht. Gebraucht wird außerdem eine Zuordnung der Zeilen aus R-4.1 zu Konten: Mieterlöse, Bewirtschaftung, Abschreibung, Zinsaufwand, Ertragsteuern, Buchwert, Restschuld.
   - *Warum es nicht verbaut ist:* Das Monatsraster liefert alle Daten dafür.
   - *Vorschlag:* In R-2.3 eine zweite Verdichtung „nach Geschäftsjahr (Beginnmonat als Vorgabe des Hauses)“ als reine Darstellung festlegen. In R-4.1 jeder Zeile eine stabile Zeilenkennung geben, auf die sich später eine Kontenzuordnung stützt. Den Steuermonat nach Kalenderjahr für Teil 2 vormerken (steht dort schon).

10. **[Hinweis · belegt] Kapitel 17, R-7.8, R-7.3, R-7.2, R-5.16, R-5.9; `TASKS.md` „Wartet auf Nutzer“; KAT-02. Einige Kennungen und Verweise passen noch nicht zusammen.**
    - *Annahmen ohne Kennung:* Die fünf vorgeschlagenen Modellannahmen haben am Wirkort noch keine Kennung, darunter die Reichweite der erweiterten Kürzung mit hohem Gewicht. Sie ist eine Ausnahme von der Vorsichtsregel und macht im Ankauf 155.680 Euro aus (eigene Stichprobe bestätigt).
    - *Vorgaben des Hauses:* `TASKS.md` führt sieben Werte, das Dokument 23 Kennungen. Hinter diesen 23 stehen rund 45 freizugebende Einzelwerte, etwa sieben Stresshöhen einzeln und kombiniert, drei Pauschalen, Suchbereiche je Eingabe und zwei Sätze in H-22.
    - *KAT-02:* Es ist als Katalogwert geführt, die Quelle lautet aber „Vorgabe des Hauses“. Das ist eine Vermischung der Herkunftsarten.
    - *R-11.12:* Endwert und Endwert der Unterlassensalternative fehlen auf dem Blatt, obwohl sich ΔEW nur aus beiden abstimmen lässt.
    - *Vorschlag:*
      - Die fünf Annahmen als `MA-030` bis `MA-034` eintragen und die Kennungen in die Regeln setzen.
      - KAT-02 in H-24 umbenennen.
      - Für den Auftraggeber in `TASKS.md` ein Freigabeblatt mit allen Einzelwerten, Einheit und Vorschlag anlegen; dabei H-22 in zwei Kennungen teilen.
      - EW und EW_U auf das Blatt nehmen.

## Nicht geprüft

- Die Referenzfall-Module `rf_*.py` habe ich nur stichprobenhaft gelesen, nicht Zeile für Zeile gegen R-15.3; `beispielwerte.py` habe ich nicht ausgeführt. Die Sollwerte habe ich über drei eigene Stichproben und den Gesamtlauf abgesichert.
- Fachliche Richtigkeit der Steuer-, Förder- und Bankregeln: Das gehört zu den Rollen Steuerberater, Fachexperte und Bank. Am Original habe ich keine Quelle gelesen.
- Die Finanzmathematik der Renditeformel (R-10.5 bis R-10.9) habe ich nur auf Nachvollziehbarkeit geprüft, nicht auf Herleitung.
- Den Abgleich mit `docs/entscheidungen.md` und `docs/quellenkataster.md` habe ich nicht vorgenommen; Kataster-Kennungen habe ich nicht auf Existenz geprüft.
