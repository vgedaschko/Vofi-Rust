Rolle: Controller (Controlling des Wohnungsunternehmens)
Prüfobjekt: `docs/fachspezifikation-rechenkern.md` (Fassung nach der ersten Überarbeitung, vollständig gelesen) und Referenzrechner `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner/` (Kernmodule `grobkalkulation.py`, `proben.py`, `steuer.py` in den geprüften Teilen, `gegenrechnung.py`, `aenderungen-runde1.md`, `ursachen-runde1.json`, RF-16 und RF-20 in `rf_neu.py` gelesen; Lauf ausgeführt)
Gesamturteil: Trägt mit Auflagen. Die Rechnung stimmt: Drei eigene Stichproben treffen jeden Wert auf den Cent, auch im Neubau. Die Sperre bei verletzter Probe greift jetzt im Lauf, im Stressfall, in der Preissuche und in der Zielwertsuche, auch wenn nur eine einzige Stützstelle betroffen ist. Gegenüber Geschäftsführung und Revision lässt sich das Modell aber noch nicht ganz vertreten. Der neue Abweichungsmechanismus führt zwei Lockerungen als „strenger“, darunter eine, die den tragbaren Preis um 42.131 Euro hebt. Die Liste „Abweichungen vom Hausstandard“ lässt sich über Voreinstellungen und Katalogwerte umgehen. Die neuen Steuer- und Alternativproben rechnen die Steuer nicht nach. Und der Vergleich zweier Fassungen übersieht eine Änderung des Körperschaftsteuersatzes.
Note: **8 von 10** (Runde 1: 7). Die 9 ist nicht erreicht. Dafür fehlen die Befunde 1 bis 7. Sie sind im Dokument und im Referenzrechner zu beheben und brauchen keine Zuarbeit von außen. Befund 7 braucht zusätzlich das Freigabeblatt für den Auftraggeber.

## Befunde aus Runde 1

| Nr. | Befund Runde 1 | Stand | Regel | Nachweis in Runde 2 |
|---|---|---|---|---|
| 1 | Verletzte Probe sperrt das Ergebnis nicht | **behoben** | R-13.1, R-11.1, R-11.5, R-11.10, R-11.11, R-11.13; `_zielgroesse`, `tragbarer_preis`, `suche_eingabe`, `vergleiche` | Fehlerinjektion wiederholt, diesmal örtlich begrenzt (Skript `injektion.py`). Ein Euro Einlage zu viel nur bei Preisen von 2.317.200 bis 2.317.240 Euro, also nur in der Bisektion nahe P*: Preissuche endet mit M-10 und ohne Preis. Störung nur im Stressfall: Basisfall frei, Stressfall gesperrt (P-04), Preissuche im Stress mit M-10. Störung nur bei Verkaufsfaktor 19,06 in der Zielwertsuche: M-10. |
| 2 | Eingabeliste: Standort, übernommenes Darlehen | **behoben** | R-3.3 (E-03, E-04, E-59 mit neun Werten), R-3.6 | Zur Zählung in R-3.6 und zur Voreinstellung von E-59 siehe die neuen Befunde 6 und 10. |
| 3 | Versteckte Konstanten | **teilweise** | R-3.1, R-6.3 (T aus KAT-08), KAT-11, KAT-12, H-21, R-2.8 | Im Regeltext erledigt. Die Prüfung in RF-20 auf Zahlenliterale funktioniert: Ein eigener Lauf über alle Literale 2, 3, 12, 60, 80 und 1000 findet nur technische Stellen. Offen bleiben drei Punkte. (a) Voreinstellungen in der Eingabeklasse: `Grobeingabe.anpassungsdauer = 0` (laut Dokument H-23; 0 ist die günstigste Anpassung) und `stau_jahr = 0` (laut E-51 Jahr 1). (b) Katalogwerte stecken in Eingabeklassen: `Steuerparameter` mit KAT-03 bis KAT-06 und KAT-16 bis KAT-18 als Teil von `Grobeingabe` („E-40 bis E-44 mit den Steuerwerten des Katalogs“), `Foerderung` (KAT-10) ebenso. (c) Eine Herkunft mit Quelle und Stand je Wert, wie R-3.1 sie verlangt, gibt es nicht. Hinzu kommen die Zulässigkeitsgrenzen `GRENZEN` als globale Moduldaten ohne Kennung. RF-20 kann keine dieser Lücken erkennen, weil es nur Zahlenliterale sucht und nicht Voreinstellungen mit erlaubten Literalen oder die falsche Klasse. |
| 4 | Proben: Steuer, Alternative, P-09 | **teilweise** | P-09 (a, b), P-15, P-16, P-17 bis P-19, P-04 (a bis c) | P-04 (a) fängt den Ausgleichsposten, P-17 den still fortgeschriebenen Zins, P-15 einen falsch fortgeschriebenen Vortragsbestand. Die Steuer selbst rechnet keine Probe nach, und die Alternative wird mit ihren eigenen Sätzen geprüft (neuer Befund 3). |
| 5 | Änderbarkeit der Vorgaben im Vorhaben | **teilweise** | R-3.2, R-3.4, M-35, NF-39 | Richtung je Vorgabe, Begründungspflicht und Liste sind gebaut. Bei H-25 und H-09 kehrt sich die Richtung um, Voreinstellungen fehlen in der Liste, und E-11 kann unter KAT-01 gesenkt werden, ohne dass es in der Liste erscheint (neue Befunde 1 und 2). Abweichungen zwischen Dokument und Code: H-06 („strenger heißt höher“) und die Staffel H-17 („mit Begründung“) sind im Code gar nicht änderbar (M-20). |
| 6 | Vergleich zweier Fassungen, eingefrorener Stand | **teilweise** | R-11.11, NF-56 | Die Regel ist vollständig gefasst. Der Code vergleicht aber 22 Größen und nicht alle Größen des Blatts. Eine Änderung des Körperschaftsteuersatzes (Katalog) erscheint nicht unter den abweichenden Werten. Die Wirkung der Kernversion ist nur ein Kennzeichen, keine Rechnung (neuer Befund 4). |
| 7 | Sollwerte als Abnahmemaßstab | **teilweise** | R-15.2, R-15.6, E-02, `--festschreiben` | Erledigt sind die Festschreibung nur mit Differenzbericht, rückwirkende Stichtage und die Liste der offenen Bestätigungen. Blindrechnung, Tabellen- und Parallelrechnung stehen aus; das ist in `TASKS.md` und R-15.6 benannt. Der Differenzbericht erklärt die Werte aber gruppenweise, und Sammelmuster machen die Ursachenpflicht für ganze Fälle wirkungslos (neuer Befund 8). |
| 8 | Rundungsdifferenz bei Summen in vollen Euro | **behoben** | R-12.7, NF-58; `darstellung` | Regel und Umsetzung stimmen; Beispiel RF-18 mit 1 Euro Differenz. Zur Zeilensumme siehe neuen Befund 10. |
| 9 | Jahresscheiben, Zeilenkennungen | **behoben** | R-4.1 (Z-A1 bis Z-N2), R-2.3, Kapitel 16 (Geschäftsjahr in Teil 2) | Zur fehlenden Kennung je Tranche siehe neuen Befund 10. |
| 10 | Kennungen, Freigabeblatt, EW und EW_U | **teilweise** | MA-030 bis MA-037, KAT-02 → H-24, R-11.12 | Erledigt sind die Kennungen am Wirkort, KAT-02 und EW mit EW_U auf dem Blatt. Das Freigabeblatt gibt es nicht. R-3.4 behauptet, `TASKS.md` führe es, aber `TASKS.md` sagt „Ich bereite … vor“. Die Liste der Annahmen mit hohem Gewicht in `TASKS.md` nennt `MA-030` und `MA-031` nicht (neuer Befund 7). |

## Eigene Nachrechnung

Skripte im Scratchpad dieser Prüfung (`fs2-controller/`): `injektion.py`, `stichproben.py`, `vergleich.py`, `abweichung.py`.

- `python3 referenzfaelle.py`: 906 von 906 Prüfungen bestanden, Rückgabewert 0, 71 s. `gegenrechnung.py`: 16 von 16 bestanden.
- **Stichprobe 1, Neubau frei finanziert (RF-12)**, allein aus Text und Anhang A.6, ohne die Module des Referenzrechners:
  - Baukosten: BK_0 7.540.000,00; Raten 419.921,98 / 420.957,62 / 437.879,56; Baukosten 7.719.152,34; M 9.015.152,34.
  - Bemessung: Bewirtschaftung im ersten Vermietungsjahr 33.647,25; RE_n 336.600,00 (Mindestansatz 15 % bindet); B = L = 4.007.142,85; Eigenkapital als Ausgleichsposten 5.008.009,49.
  - Mittelabruf Monat 9: 323.492,21 Eigenkapital und 104.786,77 Bank; Monat 10: 349,29 Zins und 9.755,89 Bereitstellungszins.
  - Finanzierungskosten der Bauzeit: Bauzeitzinsen 54.961,41 und Bereitstellungszinsen 78.993,23, zusammen 133.954,64; Eigenkapital der Investitionsphase 5.141.964,13.
  - Monat 19: Rate 20.035,71, davon Zins 13.357,14.
  - Ergebnis: alle Werte wie R-11.2, R-11.3, R-5.10, R-5.18 und P-04.
- **Stichprobe 2, Neubau mit Grobförderung (RF-12)**:
  - Förderung: zuwendungsfähig 8.719.152,34; Förderdarlehen 5.231.491,40; Zuschuss und Mindesteigenkapital je 1.743.830,47; Entgelte 65.393,64; M 9.080.545,98.
  - Bemessung: RE_n 159.216,75; Kapitaldienst des Förderdarlehens 150.431,28; A 628.357,62; B −253.580,79; C 361.393,64; Eigenkapital als Ausgleichsposten 2.105.224,11.
  - Angaben ohne Bankdarlehen: Deckung der übrigen Darlehen 1,0584; Reserve −21.300,79; nötiger Reinertrag 210.874,61.
  - Ergebnis: alle Werte wie R-11.14 und R-11.15.
- **Stichprobe 3, Ankauf (RF-11)**:
  - Mietpfad nach R-6.3 mit `MA-037` vorsichtig: Erhöhungen in den Monaten 37 / 52 / 73 / 88 / 103 / 118 / 133 auf 9,4473 / 9,7750 / 10,3607 / 10,5679 / 10,7793 / 10,9949 / 11,4390.
  - Bankensicht: Kapitaldienst im Jahr 1 73.596,60; Zins im Jahr 1 48.609,62; Zinsdeckung 2,1196; Deckung 1,4000; Reserve 14.719,32.
  - Beim tragbaren Preis: Eigenkapital 1.322.348,51; Faktor 17,47; 1.755,48 Euro je m²; 282.765 Euro unter dem Angebotspreis.
  - Ergebnis: alle Werte wie im Dokument.
  - Für die vorsichtige Lesart ohne Mietenhistorie gibt die Formel in R-6.3 allein keine Miete vor dem Stichtag her. Nachrechenbar wird sie erst mit dem Satz „frühestens im Monat T + 1“. Ein Halbsatz „Miete_k = Ist / (1 + κ) für k ≤ 0“ würde die Formel schließen.
- **Fehlerinjektion in die Rechenlogik**, nicht in die Ausgabe (`injektion.py`):

| Eingebauter Fehler | Wirkung | Probe |
|---|---|---|
| Einlage +1 Euro nur nahe P*, nur im Stressfall, nur bei einem Faktor der Zielwertsuche | Suche ohne Ergebnis | **M-10** (P-04) |
| Verlustvortrag wird nie verbraucht | Endwert −32.243,29 | keine |
| Verbrauch protokolliert, aber nicht von der Bemessung abgezogen | Endwert −32.243,29 | keine |
| Zugang doppelt im Bestand | – | **P-15** |
| Steuersatz des falschen Kalenderjahres | Endwert −155,96 | keine |
| Alternative mit Anlagezins +0,5 Prozentpunkte | EW_U 1.840.956,50 statt 1.770.603,63 | keine |
| Alternative ohne Gewerbesteuer besteuert | EW_U 1.829.535,74 statt 1.770.603,63 | keine |
| Zins nach der Bindung still fortgeschrieben | – | **P-17** |
| Habenzins nominal / 12 statt konform | – | **P-17** |
| Tranche ohne Aufschlag H-05 aufgebaut | Endwert +13.910,82, im Stress +27.582,03 | keine |

## Befunde

1. **[kritisch · belegt] R-3.2, R-3.4 (H-25, H-09), M-35; Referenzrechner `vorgaben_im_vorhaben`. Zwei Lockerungen gelten als „strenger“ und brauchen weder Begründung noch Freigabe.**
   - *Ursache:* Ist die Vorgabe des Hauses eine Regel statt eines Werts, setzt der Code jede Abweichung als „strenger“. Das betrifft H-25 („Anschlusszins der Tranche“) und H-09 („gleich H-08“); im Code steht dafür der Wert `None`.
   - *Beleg H-25:* Ein fester kalkulatorischer Zins von 1 % wird ohne Begründung gerechnet und als „strenger“ geführt. Weil i_k = max(Vertragszins; H-25) gilt, rechnet die Bank damit faktisch zum Vertragszins. Das Bankdarlehen steigt von 1.226.609,99 auf 1.431.044,99 Euro, der tragbare Preis von 2.317.235 auf 2.359.366 Euro, also um 42.131 Euro.
   - *Beleg H-09:* Ein langfristiger Anlagezins von 0,5 % statt 2 % ist eine Lockerung, weil die Endwertdifferenz von 753.701,96 auf 966.697,17 Euro steigt. Er wird ebenfalls als „strenger“ geführt.
   - *Folge:* Das Blatt zeigt eine Lockerung als Verschärfung. Eine Gremienvorlage wirkt dadurch hauseinheitlich, ist es aber nicht. Das Dokument regelt nicht, wogegen bei Regelvorgaben verglichen wird. Maßstab: ICAEW-FMC (Eingaben nachvollziehbar und kontrolliert), Spezifikation Kapitel 2 „Zielrendite und Schwellen“ (**fest**).
   - *Vorschlag:* In R-3.2 festlegen, dass verglichen wird gegen den aufgelösten Wert des Hauses: bei H-25 je Tranche gegen den Anschlusszins, bei H-09 gegen H-08. Ein fester Satz unter dem Anschlusszins ist eine Lockerung. Dazu zwei Fälle in RF-19.

2. **[wichtig · belegt] R-3.4 („Voreinstellung … steht ohne Richtung in der Liste“), E-11 und KAT-01, M-35. Die Liste „Abweichungen vom Hausstandard“ lässt sich umgehen.**
   - *(a) Voreinstellungen:* Mit Anpassungsdauer 1 statt H-23 (4 Jahre) und Zinsbindung 5 statt H-24 (10 Jahre) bleibt die Liste leer, obwohl sich die Endwertdifferenz um −39.643 Euro ändert. Der Kern kennt die Voreinstellung nicht, weil die Eingabeklasse eigene Werte hat (`anpassungsdauer = 0`, `stau_jahr = 0`; siehe Runde-1-Befund 3).
   - *(b) Katalogwerte als Voreinstellung:* E-11 mit 3 % statt KAT-01 mit 10 % ergibt keine Meldung und keinen Listeneintrag. Der tragbare Preis steigt auf 2.474.717 Euro, also um 157.482 Euro. KAT-01 enthält die Grunderwerbsteuer, die sich nicht wegverhandeln lässt.
   - *Vorschlag:* Der Auftrag trägt zu jeder voreingestellten Eingabe den Wert der Voreinstellung und ihre Herkunft (H- oder KAT-Kennung). Jede Abweichung steht in der Liste. Erwerbsnebenkosten unter dem Grunderwerbsteuersatz des Landes sind eine Lockerung mit Begründungspflicht. Die Eingabeklassen bekommen keine fachlichen Voreinstellungen.

3. **[wichtig · belegt] R-13.3 (P-15, P-16), R-13.4; `proben.py`. Die neuen Proben stimmen Bestände ab, rechnen aber die Steuer nicht nach.**
   - *Was R-13.4 behauptet:* P-15 rechne „Rechenregeln unabhängig nach: Steuer“.
   - *Was die Proben tatsächlich prüfen:* P-15 prüft nur, ob das Steuerprotokoll in sich stimmt (Fortschreibung, Summe der Arten, Buchung) und schlägt die Brücke vom Ergebnis zu den Zahlungen. P-16 rechnet die Zinsen der Alternative mit den Sätzen, die in ihrer eigenen Zeile stehen, und prüft ihre Steuer nicht.
   - *Beleg (Injektion):* Vier Logikfehler bleiben ohne Probe: Vortrag nie verbraucht oder nicht abgezogen (Endwert −32.243,29 Euro), Steuersatz des falschen Kalenderjahres (−155,96 Euro), Alternative mit falschem Anlagezins (EW_U +70.352,87 Euro) und Alternative mit falschem Steuerstatus (EW_U +58.932,11 Euro). Die letzten beiden treffen unmittelbar die führende Kennzahl ΔEW.
   - *Eine weitere Lücke:* Eine Tranche, die ohne H-05 aufgebaut ist, fällt keiner Probe auf.
   - *Woran es liegt:* Die Fehlerbilder in RF-16 verändern nur die Ausgabe (`protokoll[3]["vv"] += 1000`), nicht die Rechnung. Sie zeigen deshalb nur, dass die Probe Widersprüche im Protokoll erkennt.
   - *Vorschlag:*
     - P-15 (e): Steuer je Art und Jahr = runde(Satz des Kalenderjahres aus dem Auftrag x max(0; Bemessung − Verbrauch)) mit Verbrauch = min(Vortrag; positive Bemessung).
     - P-16 mit den Sätzen H-08, H-09 und H-10 aus dem Auftrag und mit nachgerechneter Steuer der Alternative.
     - Eine Auftragsprobe: Zins jeder Tranche nach der Bindung = E-45 + H-05, im Stressfall zuzüglich der Stresshöhe; beim übernommenen Darlehen der sechste Wert von E-59.
     - Die Fehlerbilder als Fehler in der Rechnung einbauen.
     - R-13.4 auf das berichtigen, was die Proben wirklich fangen.

4. **[wichtig · belegt] R-3.1, R-11.11; `vergleiche`, `Grobeingabe.steuer`, `Grobeingabe.foerderung`. Herkunft und Vergleich tragen eine Katalogänderung nicht.**
   - *Beleg:* Fassung A mit dem Katalogstand von A.4 (Körperschaftsteuer sinkend), Fassung B mit 15 % in allen Jahren. Die Endwertdifferenz ändert sich um −56.063,35 Euro, die Liste der abweichenden Werte bleibt leer, weil `kst_satz` vom Vergleich ausgenommen ist. Ein Hebesatz von 440 % statt 400 % (KAT-04, Wert der Gemeinde) erscheint als Herkunft „E“.
   - *Folge:* Gerade nach einer Gesetzesänderung, dem häufigsten Grund für einen Vergleich zweier Stände, kann das Controlling die Abweichung nicht erklären.
   - *Was im Vergleich fehlt:* Der Code vergleicht 22 Größen. R-11.11 verlangt alle Größen des Blatts nach R-11.12. Es fehlen die Spalte des Stressfalls, der tragbare Preis mit seinen Angaben, die Deckung nach jeder Zinsbindung, die Deckungsgrenzen, der Kapitaldienst je Darlehen, die Nachschüsse je Planjahr sowie die Meldungen und die Annahmen, die gewirkt haben. Die Wirkung der Kernversion ist nur ein Kennzeichen (`versionsgleich`).
   - *Vorschlag:* Steuer- und Fördersätze gehören als Tabellen in die Klasse des Katalogs (Satz je Kalenderjahr als vergleichbare Daten, nicht als Funktion). Herkunft, Quelle und Stand gehören an jeden Wert. Der Vergleich deckt das ganze Blatt beider Fälle ab. Dazu ein Referenzfall „gleiche Eingaben, anderer Katalogstand“.

5. **[wichtig · belegt] H-20, R-10.13, R-10.16, R-14.13. Die Warnschwellen, die einzigen Plausibilitätsgrenzen des Modells, haben keine Wirkung.**
   - *Beleg:* R-10.13 und R-10.16 verweisen auf H-20. Es fehlen eine Meldung in R-14.13, ein Wert in Anhang A.4 und ein Referenzfall. `Vorgaben.warnschwelle_restwertanteil` wird nirgends gelesen.
   - *Folge:* Ein Vorhaben mit 95 % Restwertanteil oder einem Ausstiegsfaktor über dem Einstiegsfaktor geht ohne Hinweis ins Gremium. Maßstab: FAST und ICAEW-FMC (Plausibilisierung der Ausgabe), Rolle Controller (Plausibilitätsgrenzen).
   - *Vorschlag:* M-47 „Warnschwelle überschritten“ mit Kennzahl, Wert und Schwelle für den Restwertanteil und den Abstand Ausstiegs- minus Einstiegsfaktor. Dazu Werte in A.4 und ein Fall in RF-20. Zu erwägen sind weitere Schwellen: Mietsteigerung über der Kostensteigerung und Ausstiegsfaktor über dem Marktfaktor des Katalogs.

6. **[wichtig · belegt] R-3.3 (E-59, Satz unter der Tabelle), R-5.16, R-5.12. Die Voreinstellung „Förderdarlehen: ja“ des übernommenen Darlehens ist nicht vorsichtig, und Dokument und Code widersprechen sich.**
   - *Widerspruch:* Das Dokument nennt die Voreinstellungen von E-59 „die vorsichtigen“. Mit dem Kennzeichen entfällt aber die Vorfälligkeit: Im gebundenen Bestand mit Verkauf nach fünf Jahren sind es 33.080,71 statt 46.182,48 Euro (Beispiel in R-5.16). Außerdem geht das Darlehen mit seinem vertraglichen statt dem kalkulatorischen Kapitaldienst in KD_Ü ein, was das Bankdarlehen erhöht.
   - *Code:* Er setzt `foerderdarlehen` voreingestellt auf `False`, also auf die vorsichtige Lesart.
   - *Vorschlag:* Voreinstellung „nein“, wie im Code. Das Kennzeichen setzt der Bearbeiter nur mit Bescheid. Spezifikation Kapitel 8, „Vorsicht“ (**fest**).

7. **[wichtig · begründete Einschätzung] R-3.4, Kapitel 16, `TASKS.md` („Wartet auf Nutzer“). Die Vorgaben sind für eine Freigabe durch die Geschäftsführung so noch nicht handhabbar, und das Freigabeblatt fehlt.**
   - *Widersprüche:* R-3.4 sagt „`TASKS.md` führt sie als Freigabeblatt“; `TASKS.md` sagt „Ich bereite … vor“. Die Liste der Annahmen mit hohem Gewicht in `TASKS.md` nennt sechs, das Verzeichnis führt acht: `MA-030` und `MA-031` fehlen. Nach Spezifikation Kapitel 8 dürfen sie vor dem Kundeneinsatz nicht ohne ausdrückliche Freigabe offen sein.
   - *Was rund 60 Einzelwerte für eine Freigabe schwer macht:* Sie sind von sehr unterschiedlicher Art. Eine Geschäftsführung gibt etwa 15 geschäftspolitische Werte frei: H-01 bis H-06, H-12 bis H-16, H-25 und H-27. Die übrigen Werte gibt das Controlling frei (Pauschalen, CO2-Preis, Zuschläge) oder die Entwicklung (H-20, H-21, `GRENZEN`).
   - *Was für ein Freigabeblatt fehlt:*
     - je Wert Vorschlag, Herkunft des Vorschlags (Regelwerk, Marktbericht, Hauspraxis) und Wirkung auf den tragbaren Preis des Referenzobjekts; RF-19 liefert die Einzelwirkungen schon;
     - eine Kennung des Vorgabenstands mit „gültig ab“, „freigegeben von“ und Datum; die Klasse `Vorgaben` hat kein solches Feld, und der eingefrorene Stand nach R-11.11 kann es deshalb nicht festhalten;
     - eine Entscheidung, welche Werte nach Investorensicht und Nutzungsart unterschieden werden (R-3.4 sagt „je Investorensicht und Nutzungsart“, sonst vervielfacht sich die Liste);
     - wer eine Lockerung freigibt und in welchem Turnus die Werte überprüft werden.
   - *Vorschlag:* Freigabeblatt in drei Teilen (Geschäftsführung, Controlling, Technik) mit den genannten Spalten. Den Satz in R-3.4 berichtigen. `MA-030` und `MA-031` in `TASKS.md` aufnehmen.

8. **[wichtig · belegt] R-15.2, `ursachen-runde1.json`, `aenderungen-runde1.md`. Der Differenzbericht erklärt Gruppen, nicht Werte; Sammelmuster heben die Ursachenpflicht für ganze Fälle auf.**
   - *Sammelmuster:* `^RF-12\|`, `^RF-13\|`, `^RF-14\|`, `^RF-11\|Basisfall: ` und `^RF-1[6-9]\||^RF-20\|` erfassen jede künftige Änderung dieser Fälle mit einem festen Satz. Eine unbeabsichtigte Änderung, etwa durch einen Programmfehler in RF-12, bekäme also die Ursache „Folge von R-11.2, R-6.7, R-6.8, R-5.18 …“, und der Rückgabewert 2 tritt nicht ein.
   - *Gruppenweise Erklärung:* 26 der 145 geänderten Werte tragen den Satz „wie RF-11 Basisfall: R-6.3, R-8.1, R-5.12“. Welcher Teil der Änderung der Endwertdifferenz von 825.606,46 auf 753.701,96 Euro aus welcher Regel stammt, zeigt der Bericht nicht. Meine Stichproben bestätigen die neuen Werte, nicht die Zuordnung.
   - *Gegenrechnung:* Sie ist von den Modulen unabhängig, nicht vom Verfasser. Sie deckt 16 von 441 Werten ab, keinen davon aus dem Neubau, der Preissuche, dem Stressfall oder dem Fall ohne Bankdarlehen. Meine Stichproben 1 und 2 schließen davon den Neubau und den Fall ohne Bankdarlehen in der Bemessung; der Finanzplan des Neubaus bleibt offen.
   - *Vorschlag:* Ursachen nur je Wertname oder engem Muster; ein Muster, das einen ganzen Fall erfasst, ist unzulässig. Bei mehreren Ursachen die Brücke rechnen: den alten Stand mit Regel 1, dann 1 und 2 und so weiter, je Schritt die Wirkung auf ΔEW, Rendite und tragbaren Preis. Das ist dieselbe Abweichungsbrücke, die R-11.11 für Teil 2 vormerkt; sie lohnt sich schon für die Festschreibung.

9. **[Hinweis · belegt] R-10.14, R-10.21, R-11.15, R-11.12. Zwei Kennzahlen mit demselben Namen und zwei Werten auf demselben Blatt.**
   - *Beleg (RF-12 gefördert):* Die Kapitaldienstreserve ist −21.113,95 Euro nach R-10.21 (Reinertrag des Vorhabens, tatsächlicher Kapitaldienst) und −21.300,79 Euro nach R-11.15 (nachhaltiger Reinertrag, kalkulatorischer Kapitaldienst der übrigen Darlehen). Die Deckung ist 1,0595 gegen 1,0584. Beide stehen nach R-11.12 auf dem Blatt.
   - *Folge:* Die Bank fragt, welche gilt. Maßstab: einheitliche Kennzahldefinition (Rolle Controller, IBCS „einheitliche Notation“).
   - *Vorschlag:* Unterschiedliche Namen, etwa „Kapitaldienstreserve laut Finanzplan“ und „Reserve in der Bankrechnung“. R-11.15 verweist auf R-10.21 und nennt den Unterschied in einem Satz.

10. **[Hinweis · belegt] Einzelne Widersprüche und Lücken nach der Überarbeitung.**
    - *Kapitel 17, NF-12, gegen R-6.3:* Kapitel 17 sagt „Miete über der Vergleichsmiete bleibt stehen, bis die Vergleichsmiete sie einholt“. R-6.3 und RF-18 führen sie dagegen linear zurück (11,00 / 10,5960 / … / 9,9584 Euro).
    - *R-3.6, Zählung:* „davon 28 ohne Voreinstellung“ für den gebundenen Bestand stimmt nicht. Bei 34 Feldern mit 7 + 6 voreingestellten sind es 21. E-01, E-02, E-44 und E-64 sind Pflichtfelder der Maske und in keiner Zeile gezählt.
    - *R-4.1:* Z-B4 bis Z-B10 und Z-C3 „je Darlehen“ haben keinen Schlüssel für die Tranche. Für die spätere Kontenzuordnung (Zinsaufwand je Darlehen) braucht es eine Kennung der Form `Z-B6.<Tranche>`. Die Unterlassensalternative und das Steuerprotokoll haben keine Zeilenkennungen.
    - *R-12.7:* Die Regel gilt für Spalten. Die Zeilensummen der Jahresdarstellung (Summe über die Haltedauer) brauchen dieselbe Regel.
    - *Vorschlag:* Kapitel 17 berichtigen, die Zählung nachziehen, Tranchenschlüssel und Zeilensummen ergänzen.

## Nicht geprüft

- Die übrigen Referenzfall-Module (`rf_lehrbuch.py`, `rf_testfall.py`, `rf_bausteine.py`, `rf_grob.py`) und den Rest von `rf_neu.py` außer RF-16 und dem Literaltest in RF-20 nicht Zeile für Zeile; `beispielwerte.py` nicht ausgeführt. Die 441 Sollwerte nur über den Gesamtlauf, die Gegenrechnung und drei eigene Stichproben.
- Den Finanzplan des Neubaus über die Bauzeit hinaus (Endwert, Rendite, Steuer) nicht selbst nachgerechnet, nur Bemessung, Mittelabruf und Finanzierungskosten der Bauzeit.
- Fachliche Richtigkeit von Steuer-, Förder- und Bankregeln und die Katalogwerte: Rollen Steuerberater, Fachexperte und Bank. Keine Quelle am Original gelesen.
- `docs/entscheidungen.md` und `docs/quellenkataster.md` nicht abgeglichen; `docs/modellannahmen.md` nur auf Kennungen, Gewicht und Status (37 Einträge, alle offen).
