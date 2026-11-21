Rolle: Grenzfälle
Prüfobjekt: `docs/fachspezifikation-rechenkern.md` (Teil 1, eingefrorener Stand vom 2026-11-21) und Referenzrechner unter `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner/`. Lauf `python3 referenzfaelle.py`: 20 Fälle, 1.093 von 1.093 Prüfungen bestanden, Rückgabewert 0, 61 Sekunden. Gerechnet wurde mit den Modulen des Referenzrechners, nur lesend eingebunden; am Prüfobjekt ist nichts geändert.
Gesamturteil: Trägt mit Auflagen. Alle zehn Befunde aus Runde 2 sind behoben, jeder ist mit dem damaligen Fall nachgerechnet. Die neuen Regeln zu Teilraten, Zwischenfinanzierung, Tilgung des Förderdarlehens, KfW-Anlaufjahren, Neubemessung im Stress, E-69 und E-70 halten an allen geprüften Rändern. Dazu liefen 2.040 Zufallsfälle ohne Absturz und ohne angeschlagene Probe. Es bleiben drei Lücken, die der Anwender nicht bemerkt. Am schwersten wiegt die Begründungspflicht nach R-3.2: Die Zielwertsuche prüft sie je Gitterwert statt einmal für den Ausgangsauftrag und liefert dadurch eine falsche Lösung. Die Haltedauertabelle prüft sie gar nicht.
Note: 8 von 10. Zur 9 fehlen im Referenzrechner Befund 1 (Begründungsprüfung in Zielwertsuche und Haltedauertabelle) und im Dokument und im Rechner die Befunde 2 (Scheinlösung am Rand des zulässigen Bereichs) und 3 (Katalogwerte ohne Bereich).

## Vorgehen

Skripte und Ausgaben liegen unter `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/pruefrunde-fachspezifikation-3/grenzfaelle/`. Jedes Skript lässt sich mit `PYTHONDONTWRITEBYTECODE=1 python3 <skript>.py` aus diesem Ordner aufrufen; die Ausgabe steht daneben in `out_<skript>.txt`.

| Skript | Inhalt |
|---|---|
| `h.py` | Hilfen. Bindet den Referenzrechner aus `../../referenzrechner` ein. Aufrufe laufen über `kalkuliere`; jeder Absturz wird als „ABSTURZ“ mit Datei und Zeile gezählt |
| `runde2.py`, `runde2_b2.py` | Befunde 1 bis 10 der Runde 2, neu gerechnet |
| `teilraten.py` | GF3-01 bis GF3-09: Teilraten, Zwischenfinanzierung, Tilgungsbeginn des Förderdarlehens, Haltedauer 42 |
| `kfw_stress.py` | GF3-10 bis GF3-17: KfW-Anlaufjahre, Neubemessung im Stress, Stresshöhen am Rand |
| `steuer_m20.py` | GF3-18 bis GF3-25: E-69, E-70, Aufträge, die feste Werte ändern |
| `preis_raender.py`, `preis_o_unter_u.py` | GF3-26 bis GF3-29: Preissuche an den Rändern und über dem Förderdeckel |
| `ziel_halte.py`, `ziel_rand.py`, `begruendung_suchen.py`, `begruendung_gitter.py` | GF3-30 bis GF3-33: Zielwertsuche, Haltedauertabelle, Begründungspflicht in den Suchen |
| `katalog_bereiche.py` | GF3-34: Katalogwerte außerhalb jedes sinnvollen Bereichs |
| `fuzz_neu.py`, `fuzz_ankauf.py`, `fuzz_preis.py` | GF3-35: Zufallsfälle (Saat und Zahl im Aufruf: `fuzz_neu.py 3 400`, `fuzz_neu.py 11 400`, `fuzz_ankauf.py 5 600`, `fuzz_ankauf.py 17 600`, `fuzz_preis.py 7 40`) |

Basis sind die Referenzobjekte aus `annahmen.py`: der Ankauf ohne Investitionsstau (`ANK`), der Neubau (`NB`), der geförderte Neubau mit 38 Jahren (`GEF` = RF-12 gefördert) und der Neubau mit 3 Mio. Euro KfW-Darlehen, 35 Jahre, ein tilgungsfreies Jahr (`KFWF`). Alle Werte sind Annahmen der Beispiele.

## Stand der Befunde aus Runde 2

| Nr. | Befund Runde 2 | Stand | Beleg Runde 3 (`runde2.py`) |
|---|---|---|---|
| 1 | Rate nie zum Anschlusszins, wenn die Bindung vor dem Tilgungsbeginn endet | behoben | Bauzeit 24, Bindung 2, Stress: Monat 28 Zins 20.258,33 zu 6,5 %, Tilgung 6.233,34; Deckung 1,0884 gegen 1,2624 im Basisfall (wie R-5.10). Bindung 1 Jahr: Rate 23.375,00 Euro. KfW mit 5 tilgungsfreien Jahren bei 3 Jahren Bindung: erste Rate im Monat 70 zum Anschlusszins, Tilgung 3.604,65 Euro |
| 2 | 15-%-Regel macht die Preissuche sprunghaft | behoben | Ziel 3,71259 %: P* = 2.350.070 Euro mit M-34. Endwertüberschuss bei 2.350.070 Euro 0,88 Euro, bei 2.350.071 Euro −0,69 Euro; ab 2.350.090 Euro +10.536,50 Euro (`runde2_b2.py`) |
| 3 | Voreinstellung „Förderdarlehen: ja“ beim übernommenen Darlehen | anders entschieden und vertretbar | Kennzeichen entfallen, jeder Fall rechnet mit Entschädigung (benannte Vereinfachung). Ja, nein und leer ergeben gleich VFE 69.043,11 Euro und KD_Ü 15.000,00 Euro. Ein mitgegebener Schlüssel wird still übergangen; die Maske hat das Feld nicht mehr |
| 4 | M-24 bringt die Suchen zum Absturz | behoben | Preissuche: M-24. Haltedauertabelle: M-24 je Zeile. Zielwertsuche: „keine Suche: jeder Gitterwert endet mit M-24“ |
| 5 | Fehlende Katalogwerte ohne definiertes Ergebnis | behoben | Bayern mit dem Katalog Niedersachsen, fehlende Kappungsgrenze, fehlender Hebesatz: je M-47, auch in der Preissuche. Rest: Bereiche der Katalogwerte (Befund 3) |
| 6 | Eingabeprüfung lässt Vorgaben und Felder ungeprüft | behoben | E-58 = 0 und −1, H-18, H-11, H-09, H-25, H-29, H-17, H-06 negativ, leere Staffel, Rasterzahl 0, E-59 negativ, Bindung 0: je M-20, auch in der Preissuche |
| 7 | Proben sichern die Bemessung nicht | behoben | Mindestdeckung vergessen: P-12 sperrt. Fehlerbild „Rate ohne Anschluss“: P-20 sperrt in den Monaten 19 bis 22 |
| 8 | Tragbarer Preis ohne Eigenkapital | behoben | E-60 leer und E-60 = 0: M-41, Nebenangabe 1.569.899 Euro |
| 9 | Fehlalarm im Rundungsmodus „keine“ | behoben | Neubau „keine“: M-20. Ankauf im Jahresmodus „keine“: gerechnet, keine Probe schlägt an |
| 10 | Kündigungstermin im Jahresmodus; M-34 aus nicht bindender Grenze | behoben | Bindung 15, n = 10: 4.627,90 Euro im Monatsraster, 9.320,73 Euro im Jahresmodus. E-60 gleich dem Bedarf bei 2,0 Mio. Euro: Preis 2.000.000, bindend Eigenkapital, kein M-34 |

## Geprüfte Grenzfälle

Spalte „Art“: **ok** heißt keine Beanstandung; **D** heißt Lücke im Dokument, **R** heißt der Referenzrechner weicht vom Dokument ab.

| Fall | Eingabe | erwartet nach Dokument | tatsächlich | Art |
|---|---|---|---|---|
| GF3-01 | gefördert, Bauzeit 1, 2, 3, 7, 13, 17, 18, 59, 60, je Basis und Stress (18 Läufe) | Teilraten nach aufgerundeten Anteilen H-37; Lücke über das Kontokorrent; Proben bestehen | Bauzeit 7: Teilraten ab Monat 1, 5, 7 und 11. Bauzeit 13: 1, 8, 11 und 17. Bauzeit 1: Rohbau und Innenputz beide ab Monat 2. Keine negative Restschuld, keine Probe | ok |
| GF3-02 | Vorlauf 12 bei Bauzeit 18; Vorlauf 60 bei Bauzeit 60, n = 38 und 42 | Termine um den Vorlauf verschoben | Tilgung ab Monat 35 bzw. 85, letzte Teilrate im Monat 34 bzw. 124; M-50 im zweiten Fall | ok |
| GF3-03 | Kontokorrentlinie 0, unbegrenzt, 500.000, 5 Mio. Euro (als Hauswert) | Zwischenfinanzierung bis zur Lücke über der Linie | höchster Stand 1.045.063,54 Euro in allen vier Läufen. Ab Linie 500.000 Euro kein Nachschuss mehr | ok |
| GF3-04 | Vorvermietung (Anlauf 0) | Teilrate 4 im Monat Bauende + 1 | Monat 19, Tilgung ab Monat 20 in 503 Raten | ok |
| GF3-05 | H-37 Rohbau = Innenputz = 1; Rohbau = Innenputz = 0,01 | zulässig (0 < Rohbau ≤ Innenputz ≤ 1) | 1/1: 90 % erst im Monat 19, Zwischenfinanzierung 4,88 Mio. Euro. 0,01: Zwischenfinanzierung 697.532 Euro | ok |
| GF3-06 | nur Darlehen; nur Zuschuss; Teilraten 100/0/0/0 und 0/0/0/100 | Aufteilung im Verhältnis, keiner über seinem offenen Betrag | gerechnet. 0/0/0/100: Zwischenfinanzierung 6,91 Mio. Euro zu 8 %, Rendite 3,492 %. Proben bestehen | ok |
| GF3-07 | gefördert mit 100.000 Euro KfW; gefördert mit Miete 12 Euro (Bankdarlehen nach (c)) | Reihenfolge EK, Förderung, KfW, Bank | gerechnet, Bank 361.393,64 Euro nach (c) | ok |
| GF3-08 | Tilgungsbeginn an der Frist: Bauzeit 19 bis 22; Frist 0, 1, 24, 600 Monate (Katalog) | T = min(letzte Teilrate + 1; Vorlauf + 1 + Frist) | Bauzeit 20: T = 25 = Frist. Bauzeit 21 und 22: T = 25 vor der letzten Teilrate; 501 und 502 Raten auf das noch nicht voll ausgezahlte Darlehen. Frist 600: T = 23 | ok |
| GF3-09 | Haltedauer 37, 42, 43; 42 mit Vorlauf 60 und Bauzeit 60 | 42 rechenbar, 43 M-20 | 42: Rendite 4,321 % (RF-14). 43: M-20. 42 mit 120 Monaten Bau: gerechnet | ok |
| GF3-10 | KfW 35 J./5 tilgungsfrei bei n = 3, 5, 6; 10 J./2 tilgungsfrei bei n = 3 | endfällig abgelöst, Vorfälligkeit, M-25 | n = 3: Tilgung 0, Ablösung 3 Mio. Euro, VFE 343.989,11 Euro (Bank und KfW), M-25. n = 6: erste Raten ab Monat 68 | ok |
| GF3-11 | KfW-Anlaufjahre über die Zinsbindung (Bindung 3 J., 5 tilgungsfreie Jahre) | erste Rate zum Anschlusszins (R-5.10) | Monat 70: Rate 16.104,65 Euro zu 5 %, tilgt | ok |
| GF3-12 | KfW 35/6 und 35/0 (nicht im Katalog) | M-20 | M-20 E-36 | ok |
| GF3-13 | KfW-Zins 0; KfW im Stress; KfW n = 42 mit 120 Monaten Bau | gerechnet | gerechnet; im Stress VFE 235.732,55 Euro | ok |
| GF3-14 | Stress-Neubemessung bis null: übernommenes Darlehen 1,3 Mio. Euro (Bindung 2 J., Anschluss nach E-45) | L_Stress = 0, M-21, Eigenkapital trägt den Rest | Basis L = 895,71 Euro. Stress: B = −68.496,80, L = 0, M-21, Eigenkapital 1.340.000,00 Euro, P-04 besteht | ok |
| GF3-15 | Zinsanstieg bis zur Zusage +5 und +20 Prozentpunkte | Neubemessung mit dem höheren Zins | L 715.522,49 bzw. 318.009,99 Euro. Kein Absturz, obwohl der Zins dann über der Eingabegrenze von E-45 liegt | ok |
| GF3-16 | Stress Leerstand +150 Pp.; Stress Verkaufsfaktor −100 % mit Preissuche | Leerstand höchstens 100 %; Verkaufspreis 0 | Miete 0, VK 0, M-29, M-42. Faktor 0: VK 0, Preissuche 681.568 Euro | ok |
| GF3-17 | Stress Bauzeit +200 Monate | M-23 vor dem Basisfall | M-23 | ok |
| GF3-18 | Körperschaft mit E-41, E-69 ja und nein, n = 1, 2, 10, 11, 12 | Verkaufsjahr nach R-7.8 Fall 1 oder 2 | gerechnet; n = 12: Steuer im Verkaufsjahr 261.999,86 gegen 114.103,86 Euro. Im Verlustjahr n = 1 kostet „ja“ 28,00 Euro Gewerbesteuer auf die Habenzinsen, die „nein“ mit dem Verlust verrechnet; unter der Schwelle | ok |
| GF3-19 | E-69 im geförderten Neubau, n = 36, 37, 38 (Bindungsende im Monat 438) | Rückzahlung nur bis zum Bindungsende | n = 36: Rückzahlung 24.911,86 Euro; n = 37, 38: null | ok |
| GF3-20 | E-69 = ja ohne E-41 | M-20 (Spalte „zulässig“: nur mit E-41) | still gerechnet, ohne Wirkung; steht als Abweichung in M-35 | R → Befund 4 |
| GF3-21 | E-69 = ja ohne Begründung | M-20 im Lauf und in der Preissuche | so | ok |
| GF3-22 | E-70 bei der Privatperson, Bindung 5, 6, 35 Jahre, n = 5, 6, 7, 38 | Bindung 5: M-20 („mehr als“ KAT-19); sonst verteilt, Rest im Verkaufsjahr | Bindung 5: M-20 in allen vier Läufen. Bindung 6, n = 5: Rückzahlung 726.596,03 Euro = 30/72 des Zuschusses | ok |
| GF3-23 | E-70 im Betriebsvermögen; KAT-19 fehlt | M-20; M-47 | so | ok |
| GF3-24 | Vorhaben ändert 15 feste Hauswerte, Katalogwerte und Lesarten (H-09, H-10, H-11, H-18, H-17, H-23, H-27, H-39, H-21, H-37, H-31, MA-026, MA-031, MA-038) und H-35 | M-20; H-35 ist nach R-3.4 „Vorgabe“ | alle M-20, auch H-35 („fester Katalogwert“ im Rechner) | R → Befund 4 |
| GF3-25 | H-38 „sofort“ und MA-036 über die Steuerparameter des Auftrags | M-20, wenn das Vorhaben es setzt | gerechnet, in der Liste als „Hauswert“ bzw. „Lesart des Hauses“; der Rechner kann Haus und Vorhaben hier nicht unterscheiden | R → Befund 4 |
| GF3-26 | Preissuche gefördert, Ziel 3 / 4 / 4,5 %, Verlauf über den Förderdeckel (P + ENK = 1 Mio. Euro) | monoton fallend | Endwertüberschuss fällt durchgehend, Knick bei 925.926 Euro; P* 2.118.474 / 1.166.209 / 643.944 Euro | ok |
| GF3-27 | Obergrenze unter der Untergrenze (übernommen 2 Mio. Euro, H-21 Faktor 5 bis 10,18) | M-31 („Obergrenze nicht über der Untergrenze“) | M-22 | R → Befund 4 |
| GF3-28 | H-21 Faktor 0,000001 (O = 0) und 0,00001 (O = 2); Rasterzahl 1, Fenster 0 | M-31; M-33; derselbe Preis | M-31; M-33; 2.407.109 Euro wie mit 40 Schritten | ok |
| GF3-29 | Zielrendite 1.000 %, −99,99 %, −100 % | M-32; M-33; M-20 | so | ok |
| GF3-30 | Zielwertsuche Kaufpreis 0 bis 5 Mio. Euro; mit übernommenem Darlehen 1,5 Mio. Euro; Zins −1 bis 10 % | eine Lösung | „2 Lösungen“: 1 Euro steigend und 2.407.109 Euro; 1.363.637 Euro steigend und 2.577.056 Euro; 0,000 % steigend und 4,069 % | D + R → Befund 2 |
| GF3-31 | Zielwertsuche Kaufpreis mit H-03 1,3 ohne Begründung, Ziel 2 % (am Ausgangsauftrag zulässig) | Begründung gilt für den Ausgangsauftrag (R-11.9); Lösung 3.086.928 Euro | „eine Lösung: 2.892.601 Euro“; 36 Gitterwerte mit M-20 | R → Befund 1 |
| GF3-32 | Haltedauertabelle mit H-12 2,5 % ohne Begründung | M-20 wie Lauf, Preis- und Zielwertsuche | Zahlen: 5,556 / 5,348 / 5,594 % statt M-20 | R → Befund 1 |
| GF3-33 | Haltedauer 40 bis 42 im Ankauf, Jahresmodus, Neubau mit Stress, Preissuche bei n = 42, Tabelle 1 bis 42 und 41 bis 43 | gerechnet; 43 M-20 | gerechnet; Neubau-Zeilen 1 und 2 M-23, Zeile 43 M-20; Preissuche 2.198.679 Euro in 3 Sekunden | ok |
| GF3-34 | 16 Katalogwerte außerhalb jedes sinnvollen Bereichs (KAT-03, -04, -07, -08, -10, -13, -14, -15) | Prüfung nach R-3.7 („kein Wert des Auftrags ohne geprüften Bereich“) | alle gerechnet außer Darlehensquote 150 % (M-22). Rückzahlungsfrist 0: Endwert 111,99 Mio. Euro, Rendite 10,971 %. Bindung 0: Absturz `KeyError` | D + R → Befund 3 |
| GF3-35 | 2.040 Zufallsfälle: 800 im Neubau (gefördert mit Teilratenmustern, KfW, Stress, Vorlauf, Bauzeit 1 bis 60, alle Steuerstatus, E-41/E-69/E-70), 1.200 im Ankauf (übernommenes Darlehen, gebundener Bestand, Neubemessung, beide Raster), 40 Preissuchen | nie Absturz, keine Probe, keine negative Restschuld oder Tilgung; P-14 | 1.854 Ergebnisse, 127 M-22, 19 M-23, 40 Preissuchen (11 Preis, 16 M-32, 12 M-46, 1 M-34). Kein Absturz, keine Probe, keine negative Größe, P-14 überall erfüllt | ok |

Gezielt geprüft sind 290 Läufe in 35 Gruppen, dazu 2.040 Zufallsfälle. Fünf Gruppen tragen Befunde.

## Befunde

1. **[kritisch · belegt] R-11.1, R-11.9, R-3.2 Nr. 5; `grobkalkulation.py`, `suche_eingabe` und `haltedauer_tabelle`: Die Begründungspflicht wirkt in der Zielwertsuche je Gitterwert und in der Haltedauertabelle gar nicht.**
   - Problem: Das Dokument sagt: „Die Suchen selbst (R-11.4, R-11.9, R-11.13) prüfen die Begründungen einmal vorab“ (R-11.1). Zur Zielwertsuche heißt es: „Die Begründungspflicht … gilt für den Auftrag, von dem die Suche ausgeht, nicht für die Werte, die sie durchläuft“ (R-11.9).
     - Der Rechner prüft in der Zielwertsuche an jedem Gitterwert. Ein Gitterwert, an dem dieselbe Abweichung die Rendite hebt, endet mit M-20 und zählt als „verfehlt“.
     - Die Haltedauertabelle ruft `rechne_grob` mit `_begruendung=False` auf und prüft nie.
   - Beleg, Zielwertsuche (`begruendung_gitter.py`): Ankauf, Zielrendite 2 %, Mindestdeckung 1,3 statt 1,2 als Abweichung ohne Begründung (wie RF-19). Am Ausgangsauftrag mit 2,4 Mio. Euro ist das zulässig; gerechnet wird mit Rendite 4,910 % und M-35. Die Zielwertsuche auf den Kaufpreis von 1 bis 8 Mio. Euro liefert „eine Lösung: 2.892.601 Euro“. Ab 2.892.602 Euro enden 36 Gitterwerte mit M-20. Mit Begründung liefert dieselbe Suche 3.086.928 Euro. Die ausgegebene Lösung liegt um 194.327 Euro oder 6,3 % zu tief, und nichts sagt dem Anwender, warum.
   - Beleg, Haltedauertabelle (`begruendung_suchen.py`): Ankauf mit Mietsteigerung 2,5 % ohne Begründung. Lauf, Stressfall, Preissuche, Zielwertsuche und Vergleich enden mit M-20. Die Haltedauertabelle zeigt für die Jahre 10 bis 12 Renditen von 5,556 / 5,348 / 5,594 % statt 5,008 / 4,842 / 5,042 %.
   - Vorschlag: `suche_eingabe` und `haltedauer_tabelle` prüfen wie `tragbarer_preis` einmal vorab am Ausgangsauftrag (`pruefe_begruendungen`) und rechnen die Gitterwerte und Zeilen dann mit `_begruendung=False`. RF-20 bekommt für beide einen Fall: die Abweichung oben mit Ziel 2 % und die Haltedauertabelle mit M-20.
2. **[wichtig · belegt] R-11.10: Ein Wechsel an der Grenze des zulässigen Bereichs wird als Lösung ausgegeben.**
   - Problem: Nach R-11.10 gilt das Ziel an einem Gitterwert mit Eingabemeldung als verfehlt. Liegt neben einem solchen Gitterwert ein zulässiger, an dem das Ziel erreicht ist, entsteht ein Wechsel „verfehlt → erreicht“. Das Verfahren verfeinert ihn und meldet ihn als Lösung mit der Richtung „steigend“. Die Zahl der unzulässigen Werte steht nur als Zählung daneben; die Meldung, die dort gilt, steht nicht dabei. Text und Rechner stimmen überein; der Fehler liegt in der Regel.
   - Beleg (`ziel_halte.py`, `ziel_rand.py`):
     - Kaufpreis 0 bis 5 Mio. Euro: „2 Lösungen“, nämlich 1 Euro steigend und 2.407.109 Euro fallend. Die Preissuche nennt für dieselben Eingaben 2.407.109 Euro.
     - Mit 1,5 Mio. Euro übernommenem Darlehen: „2 Lösungen“, nämlich 1.363.637 Euro steigend und 2.577.056 Euro fallend. 21 Gitterwerte enden mit M-22; 1.363.637 Euro ist nur der kleinste Preis, bei dem die übrigen Mittel den Bedarf nicht übersteigen.
     - Zins von −1 bis 10 %: 0,000 % steigend und 4,069 % fallend.
     - Der Suchbereich je Eingabe ist ein fester Katalogwert (H-21). Für Kaufpreis und Zins nennt Anhang A.4 keinen Bereich; ein Bereich ab null ist naheliegend.
   - Vorschlag: In R-11.10 festlegen, dass ein Wechsel zwischen einem Gitterwert mit Eingabemeldung und einem zulässigen keine Lösung ist. Er erscheint als „Rand des zulässigen Bereichs bei x, Meldung M-..“. Für Kaufpreis und Grundstückspreis beginnt der Bereich wie in R-11.5 beim kleinsten zulässigen Preis. Dazu ein Fall in RF-20.
3. **[wichtig · belegt] R-3.5, R-3.7, Kapitel 14: Katalogwerte haben keinen zulässigen Bereich. Unplausible Werte rechnen still falsch oder bringen den Kern zum Absturz.**
   - Problem: R-3.7 sagt: „Es gibt keinen Wert des Auftrags ohne geprüften Bereich.“ R-3.5 nennt für die Katalogwerte aber keinen Bereich, und `pruefe_eingaben` prüft sie nur auf Vorhandensein (M-47). Ausnahme sind die Teilraten von KAT-10 (Summe eins).
   - Beleg (`katalog_bereiche.py`), 16 Fälle, 15 davon still gerechnet:
     - Rückzahlungsfrist des Förderdarlehens 0 Jahre: Laufzeit −4, Rate −1.307.872,85 Euro, die Tilgung ist negativ, die Schuld wächst ohne Auszahlung. Endwert 111.989.789,61 Euro, Rendite 10,971 % statt 3,956 %. P-02, P-03 und P-20 bestehen, weil sie die negative Rate aus denselben Merkmalen nachrechnen.
     - Bindung der Förderung 0 Jahre: Absturz `KeyError: 18` in `ertrag.py`, `mieten_neubau`, über `kalkuliere`. Das widerspricht dem Eingangssatz von Kapitel 14.
     - Weiter still gerechnet: Hebesatz −400 % (Rendite 6,431 %), Körperschaftsteuer 150 %, Kappungsgrenze −15 %, Abschreibungssatz 200 % und −2 %, Mindestansatz der Bewirtschaftung 150 %, Sperrfrist −120 Monate, negative Bereitstellungsprovision, negativer Verwaltungskostenbeitrag, KfW-Zinsbindung 0.
   - Katalogwerte pflegt das Haus mit Quelle. Ein Tippfehler im Katalog fällt dem Bearbeiter nicht auf, weil er die Werte nicht sieht.
   - Vorschlag: In R-3.5 eine Spalte „zulässig“ je KAT-Wert aufnehmen. Sätze liegen zwischen 0 und 100 %. Fristen, Laufzeiten und Bindungen sind ganze Zahlen ≥ 1, wo sie Divisor oder Laufzeit sind. Der Hebesatz ist ≥ 0. Prüfen in R-3.7 Schritt 2, Verletzung als M-47 mit dem Zusatz „Katalogwert außerhalb seines Bereichs“. P-20 um „Rate ≥ 0 und planmäßige Tilgung ≥ 0“ ergänzen; das kostet nichts. Ein Fall in RF-20.
4. **[Hinweis · belegt] R-3.2 Nr. 1, R-3.3, R-3.4, R-14.13: Vier Stellen, an denen Rechner und Text auseinanderlaufen.**
   - (a) H-35 ist nach R-3.4 „Vorgabe; Voreinstellung von E-23“ und zählt zu den 27 freizugebenden Vorgaben. Im Rechner steht H-35 unter `FESTE_KATALOGWERTE`, und eine Abweichung im Vorhaben endet mit M-20 (GF3-24). Die Wirkung ist gering, weil E-23 dasselbe leistet. Vorschlag: `vorlauf` nach `KENNUNG_VORGABE` verschieben, oder R-3.4 ändern und die Zählung „27 Vorgaben“ anpassen.
   - (b) E-69 ist nach R-3.3 „nur mit Kennzeichen E-41“ zulässig. Ohne E-41 rechnet der Rechner still ohne Wirkung und führt E-69 in M-35 als Abweichung (GF3-20). Vorschlag: M-20 in `pruefe_eingaben` wie bei E-41 und E-70.
   - (c) H-38 (Hauswert) und die Lesart von `MA-036` stehen in den Steuerparametern der Eingabe (`Steuerparameter.verlust`, `.aufgabegewinn`). Ändert ein Vorhaben sie dort, rechnet der Kern ohne M-20 und führt sie als „Hauswert“ oder „Lesart des Hauses“ (GF3-25). Das widerspricht R-3.2 Nr. 1 und der Trennung der drei Datenklassen in R-3.1. Dasselbe gilt für die Katalogwerte KAT-03 bis KAT-06 in diesem Objekt. Vorschlag: Hauswerte, Lesarten und Katalogwerte aus `Steuerparameter` in `Vorgaben` und `Katalog` verlegen, damit `abweichungen` sie erreicht.
   - (d) M-31 nennt als Auslöser auch „Obergrenze nicht über der Untergrenze“. Liegt O unter dem kleinsten zulässigen Preis, meldet der Rechner M-22 (GF3-27: übernommenes Darlehen 2 Mio. Euro, H-21 Faktor 5 bis 10,18, O unter U = 1.818.182 Euro; ab Faktor 10,2 mit O = 1.820.461 Euro wird gesucht). Das kommt nur mit sehr hohem übernommenem Darlehen vor. Vorschlag: In `_tragbarer_preis` erst U bestimmen und bei O ≤ U M-31 melden, oder die Tabelle in R-14.13 auf „keine Miete“ beschränken.
5. **[Hinweis · belegt] R-6.7, R-10.22, R-11.14, Anhang A.4: Verweise auf Entfallenes.**
   - R-6.7 („trägt die Betriebskosten leerstehender Flächen (R-6.17)“) und R-10.22 („Die Bewirtschaftung enthält die Betriebskosten leerstehender Flächen …“) verweisen auf R-6.17, die entfallen ist.
   - Anhang A.4, Zeile H-32 bis H-37, nennt noch „Betriebskosten leerstehender Flächen 0 Euro, in den bezeichneten Fällen 30 Euro je m²“ (H-36 entfallen).
   - Das Beispiel in R-11.14 nennt eine Zahl nach Lesart (1) von `MA-026` („A stiege auf 5.859.849,02 Euro“). Diese Lesart rechnet der Referenzrechner nicht mehr, und die Zahl ist in ihm nicht zu finden; das widerspricht dem Satz in `LIESMICH.md`, jede Zahl des Dokuments komme aus den Skripten.
   - Vorschlag: Die beiden Verweise streichen, A.4 bereinigen und die Zahl in R-11.14 wie in R-5.19 als „Stand vor der Durchsicht“ kennzeichnen oder streichen.

## Am Dokument bestätigt (keine Befunde)

- **Teilraten und Zwischenfinanzierung (R-11.3):**
  - Bauzeiten 1 bis 60 Monate, auch solche, die nicht durch die Abschnitte teilbar sind; Vorlauf 0 bis 60; Anlauf 0.
  - Teilratenmuster bis 0/0/0/100 und Kontokorrentlinie 0 bis unbegrenzt.
  - Jede Lücke wird nachgeholt, das Kontokorrent kehrt auf null zurück, P-04 besteht.
- **Tilgung des Förderdarlehens (R-5.11):** Die Frist von 24 Monaten greift genau ab Bauzeit 20. Danach läuft die Tilgung auf das noch nicht voll ausgezahlte Darlehen ohne negative Restschuld. Haltedauer 42 und Bauende im Monat 120 sind rechenbar.
- **KfW (R-5.10, R-5.19):** Anlaufjahre über Haltedauer und Zinsbindung, Varianten außerhalb des Katalogs (M-20), Zins 0.
- **Stress (R-11.8):** Neubemessung bis auf null mit M-21 und höherem Eigenkapital. Der Leerstand ist bei 100 % gedeckelt, Faktor −100 % ergibt Verkaufspreis 0, eine überlange Bauzeit führt zu M-23.
- **E-69 und E-70 (R-7.8, R-7.19):** Verkauf im ersten Jahr, am Ende der Zinsbindung und am Bindungsende der Förderung. Bei einer Bindung von genau fünf Jahren endet E-70 mit M-20 („mehr als“). Die Begründungspflicht für E-69 gilt im Lauf und in der Preissuche.
- **Preissuche:** Ränder (O = 0, O = 2, Raster 1 ohne Fenster, Ziele 1.000 % und −99,99 %) und der monotone Verlauf über den Förderdeckel. P-14 hält in allen 40 Zufallssuchen.

## Nicht geprüft

- Vergleich zweier Fassungen (R-11.11) und Abweichungsliste mit Wirkung im Stressfall (R-3.2 Nr. 4) wurden nur über die Referenzfälle geprüft und nicht gesondert angegriffen.
- Zufallsfälle für die Zielwertsuche und die Haltedauertabelle fehlen; geprüft sind dort nur die gezielten Fälle GF3-30 bis GF3-33.
- Rechtsgrundlagen (`NBANK-RL-MIETWOHNRAUM-2026`, `KFW-297-298-MERKBLATT`, `GEWSTG-9`, `ESTG-11`): nicht am Original gelesen; geprüft ist nur, ob Text und Rechner einander entsprechen.
