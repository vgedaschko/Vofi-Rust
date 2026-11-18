Rolle: Grenzfälle
Prüfobjekt: `docs/fachspezifikation-rechenkern.md` (nach Prüfrunde 1: 167 Regeln, P-01 bis P-19, M-10 bis M-46) und Referenzrechner unter `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner/`. Gerechnet wurde mit einer unveränderten Kopie; `referenzfaelle.py` in der Kopie: 906 von 906 bestanden, 75 Sekunden.
Gesamturteil: Trägt mit Auflagen. Alle zehn Befunde aus Runde 1 sind behoben, einer mit kleinem Rest. 4.400 Zufallsfälle mit zulässigen Anwendereingaben liefen ohne Absturz und ohne Fehlalarm. An den neuen Regeln gibt es aber neue Lücken. Die wichtigste ist eine stille Falschrechnung: Endet die Zinsbindung vor dem Tilgungsbeginn, wird die Rate mit dem alten Zins gesetzt. Im Stressfall tilgt das Bankdarlehen dann gar nicht mehr, und die Deckung erscheint besser als im Basisfall. Daneben verletzt die 15-%-Regel die Monotonie der Preissuche, eine Voreinstellung von E-59 widerspricht dem Vorsichtsgrundsatz, und der Satz „Der Kern bricht nie ab“ gilt für die Suchen und für Katalog und Vorgaben nicht.
Note: 8 von 10. Zur 9 fehlen:
- im Dokument Befund 1 (Rate, wenn die Tilgung nach der Bindung beginnt) und Befund 2 (Sprung durch die 15-%-Regel in der Preissuche);
- im Dokument die Voreinstellung in Befund 3;
- die Grenzen der Vorgaben und der fehlenden Eingabefelder (Befund 6);
- die Regel zu E-60 = 0 (Befund 8);
- im Referenzrechner die Befunde 1, 4, 5 und 6, damit der Satz in Kapitel 14 auch für Suchen, Katalog und Vorgaben stimmt.

## Vorgehen

Skripte und Ausgaben liegen im Scratchpad unter `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs2-grenzfaelle/`:
- `h.py`: gemeinsame Hilfen; der Aufruf läuft über `kalkuliere`, ein Absturz wird als solcher gezählt;
- `runde1.py`: die Fälle aus Runde 1, Ausgabe `out_runde1.txt`;
- `neue.py`: NG-01 bis NG-31, Ausgabe `out_neue.txt`;
- `ziel.py`: Ausgabe `out_ziel.txt`, darin NG-22 im Stressfall, NG-24, NG-25, NG-33, NG-34, NG-35 und NG-36;
- `t4.py`: NG-32, Ausgabe `out_t4.txt`;
- `fuzz.py`, `fuzz2.py`, `fuzz3.py`: NG-38, Ausgabe `out_fuzz.txt`;
- Ausgabe `out_keine.txt`: NG-39.

Basis ist der Ankauf aus RF-11 ohne Investitionsstau (`ANKAUF` mit `stau_betrag = 0`) mit `VORGABEN` und `KATALOG`, beim Neubau `NEUBAU` mit `KATALOG_NEUBAU`. Alle Werte sind Annahmen der Beispiele.

Spalte „Art“: **D** heißt Lücke im Dokument, **R** Abweichung des Referenzrechners vom Dokument, **D + R** beides, **ok** keine Beanstandung.

## Befunde aus Runde 1

| Nr. | Befund Runde 1 | Stand | Beleg Runde 2 |
|---|---|---|---|
| 1 | Leerstehendes Objekt bekommt nie Miete | behoben | Ist-Miete 0 bei vermieteter Fläche: M-20 mit Hinweis auf E-31 (GF-08). Ganz leeres Objekt: Miete 10,12 ab Monat 4 (GF-08b); tragbarer Preis 2.354.808 € (GF-09) |
| 2 | Verkaufspreis ignoriert Leerstand | behoben | Leerstand 100 %: Verkaufspreis 0, M-42 (GF-10). Leerstand 30 %: 2.283.050,45 € statt 3.212.578,13 € (GF-48) |
| 3 | Division durch null bei Zins plus Tilgung null | behoben | Ohne Aufschlag: (b) unbegrenzt, (a) bindet (GF-02b). Mit Aufschlag: i_k 1 %, B 8.586.269,99 € (GF-02). „Restlaufzeit bleibt“ bei Tilgung null: M-40 (GF-31). Negativer Zins: M-20 (GF-03, GF-04) |
| 4 | Preissuche über unzulässige und undefinierte Bereiche | weitgehend behoben | GF-19b: U = 1.818.182 €, dort M-32. GF-44: M-41 mit Nebenangabe. GF-40: M-23 schon im Basisfall. Rest: Ohne Eigenkapital meldet die Zielwertsuche „Ziel an allen Rasterstellen erreicht“, ohne einen Hinweis wie M-41 (NG-37, in Befund 8) |
| 5 | Vorfälligkeit ohne Obergrenze | behoben | Bindung 40, Haltedauer 1: 114 Monate, 114.154,19 € (GF-27). Bindung 15, Haltedauer 12: keine Vorfälligkeit (GF-29). Jahresmodus: Hinweis in Befund 10 |
| 6 | P-04 kann keinen Fehler finden | behoben | 100.000 € Einlage zu viel: P-04 (a) und (c) melden, Ergebnis gesperrt (GF-47) |
| 7 | Fehlalarm P-07 um einen Cent | behoben | P-07 rechnet nach R-8.7 (RF-16). Der Runde-1-Fall rechnet wegen der neuen Baukostenregel einen anderen Zuschuss; keine Verletzung (GF-46) |
| 8 | Anpassungsdauer 0: Text gegen Formel | behoben | Jahr 1 Ist-Miete 8,50, erste Erhöhung Monat 37 (GF-13). RE_n kappt eine Ist-Miete über der Vergleichsmiete (GF-11) |
| 9 | Zuschuss über den Baukosten | behoben | Aufteilung auf Gebäude und Boden: Gebäudeanteil 2.661.776,66 € bei 3.327.220,83 € Baukosten. Drei Lesarten gerechnet (GF-20). Zuschuss über den Kosten: M-43 (RF-17) |
| 10 | Irreführende Ausgaben an den Rändern | behoben | P* an der Obergrenze gefunden (GF-35). „an allen Rasterstellen erreicht“ (GF-36). Interner Zinsfuß „Lösung außerhalb des Suchbereichs“ (GF-39). Fehlbetrag beim Verkauf 926.438,19 € mit M-42 (GF-21) |

Eingabeprüfung der Runde 1: GF-03, GF-04, GF-06, GF-07, GF-21, GF-25 und GF-41 enden jetzt alle mit M-20 und ohne Rechnung. GF-42: Der fehlende Anschlusszins des übernommenen Darlehens wird nach E-59 voreingestellt.

## Gerechnete Fälle

### Fälle aus Runde 1 (neu gerechnet)

| Fall | Eingabe | erwartet nach Dokument | tatsächlich | Art |
|---|---|---|---|---|
| GF-02 | Zins 0, Tilgung 0, Mindesttilgung 0, Aufschlag 1 Pp. | i_k = 1 % | L 1.560.000 nach (a), B 8.586.269,99 | ok |
| GF-02b | dazu Aufschlag 0 | (b) unbegrenzt | b = None, L 1.560.000 nach (a), EW 2.676.362,28 | ok |
| GF-03, GF-04 | Zins −0,5 %, −2 % | M-20 | M-20 E-45 | ok |
| GF-06 | Kaufpreis 0 | M-20 | M-20 E-10 | ok |
| GF-07, GF-08 | Ist-Miete 0 bei vermieteter Fläche | M-20 (R-6.13) | M-20 E-15 mit Hinweis auf E-31 | ok |
| GF-08b | ganz leer, Markt 10,50, Bremse | Miete ab Monat 4 zu min(10,50; 9,20 x 1,10) | 0 / 0 / 0 / 10,12; L 930.929,99 | ok |
| GF-09 | ganz leer: tragbarer Preis | Preis | 2.354.808, r 5,000 % | ok |
| GF-10 | Leerstand 100 % | VK nach Leerstand, M-21, M-42 | VK 0; EW 0; FB 3.026,52; M-21, M-29, M-42 | ok |
| GF-48 | Leerstand 30 % | VK auf Miete nach Leerstand | VK 2.283.050,45; ΔEW −180.775,16 | ok |
| GF-13 | d = 0 | Jahr 1 Ist-Miete | M1 bis M13 8,50; M37 9,7631; RE_VJ 103.035,24 | ok |
| GF-11 | Ist 11,00 über VM 9,20 | Rückführung, RE_n mit min | 11,00 / 10,596 / … / 10,1575; RE_n 113.901,48 | ok |
| GF-19b | übernommen 2,0 Mio. zu 6 %, Faktor 4 | M-32 bei U | U 1.818.182, M-32 | ok |
| GF-44 | Vollfinanzierung ohne EK | M-41 mit Nebenangabe | M-41, Nebenangabe 3.752.336; Zielwertsuche „an allen Rasterstellen erreicht“ | ok / Rest in Befund 8 |
| GF-40 | Neubau, Bauzeit 60, n = 6 | M-23 vor dem Basisfall | M-23 in Basis, Stress und Preissuche | ok |
| GF-27 | n = 1, Bindung 40 | Restbindung 114 Monate | VFE 114.154,19 | ok |
| GF-29 | Bindung 15 / 12 bei n = 12 | keine VFE | VFE 0 in beiden | ok |
| GF-31 | Tilgung 0, „Restlaufzeit bleibt“ | M-40 | M-40, gerechnet | ok |
| GF-47 | Einlage +100.000 eingeschleust | P-04 | gesperrt, P-04 (a) und (c) je 100.000,00 | ok |
| GF-46 | Halber-Cent-Fall P-07 | keine Verletzung | nicht gesperrt | ok |
| GF-20 | Zuschuss 80 %, Grundstück 5 Mio., Bau 3,3 Mio. | Aufteilung, gerechnet | gerechnet; „sofort“ r 2,705 %, „verteilt“ 5,799 %, „Minderung“ 5,887 % | ok |
| GF-35 | Obergrenze genau P* | Preis gefunden | 2.317.235, kein M-33 | ok |
| GF-36 | (x − 3)(x − 3,2) | „an allen Rasterstellen“ | so, Rasterweite 0,25 | ok |
| GF-39 | IZF −400.000/+1; −100/+1.200 | „außerhalb des Suchbereichs“ | so | ok |
| GF-21 | Faktor 0; Faktor 4 nach 2 Jahren | M-20; Fehlbetrag mit M-42 | M-20; FB 926.438,19, M-25, M-29, M-38, M-42 | ok |
| GF-25 | Steuersatz 100 % | M-20 | M-20 E-42 | ok |
| GF-41 | Bauzeit 0 | M-20 | M-20 E-26 | ok |
| GF-42 | übernommen ohne Anschlusszins | Voreinstellung E-45 + H-05 | gerechnet | ok |

### Neue Fälle

| Fall | Eingabe | erwartet nach Dokument | tatsächlich | Art |
|---|---|---|---|---|
| NG-01 | Ist 11,00 > VM 9,20, Fluktuation 10 %, Bremse | Neuvermietung höchstens 10,32; Rückführung | Jahr 1 bis 4: 11,00 / 10,5686 / 10,3114 / 10,1925 | ok |
| NG-02 | Vergleichsmiete 0 bei vermieteter Fläche; ganz leer ohne VM | M-20 | M-20 E-19 in beiden | ok |
| NG-03 | Wartefrist am Rand: n = 3 und 4 (MA-037 vorsichtig), n = 1 und 2 (andere Lesart) | erste Erhöhung Monat 37 bzw. 13 | n = 3 keine, n = 4 ab M37 (9,4473), VK 2.653.219,32; n = 1 keine, n = 2 ab M13 | ok |
| NG-04 | Kappung genau erreicht (8,00 x 1,15 = 9,20 = VM) | eindeutig | eine Erhöhung M13 auf 9,2000 | ok |
| NG-05 | ganz leer und Leerstand 100 % | Einzahlung 0, M-31 in der Suche | EW 0, M-21/M-29/M-42; Suche M-31 | ok |
| NG-06 | Fluktuation 100 %, mit und ohne Bremse | ganze Fläche ab Jahr 2 zur Neuvermietungsmiete | M13 10,3224 bzw. 10,7100 | ok |
| NG-07 | 200 m² leer: Bremse greift (10,50) / greift nicht (9,80) / aus | min(Markt; VM x 1,1) | 10,12 / 9,80 / 10,50 | ok |
| NG-08 | 40 % gebunden, Bindungsende Jahr 1 / 12 / 13 / 50 | Jahr b + 1 letzte gebundene Miete, dann R-6.3 | b = 1: 6,80 bis M36, M37 7,82; b ≥ 12 gleich | ok |
| NG-09 | gebundene Miete E-58 = 0 und = −1 | M-20 (E-58 > 0); Einzahlung nie negativ (R-6.4) | beide gerechnet; bei −1: Sollmiete −1.320,00, Einzahlung **−1.293,60 €** je Monat | R → Befund 6 |
| NG-10 | H-25 fest 2 % unter Vertragszins 4 % | i_k = max = 4 % | L 1.431.044,99 = Lesart 2 | ok |
| NG-11 | Mindesttilgung 0, Tilgung 0, Zins 4 % | τ_k = 0 | B 1.717.253,99; (a) bindet | ok |
| NG-12 | RE_n negativ (Leerstand 80 %), auch bei i_k + τ_k = 0 | B ≤ 0, L 0, M-21 | so, in beiden Fällen | ok |
| NG-13 | KfW = Höchstbetrag; einen Cent darüber | gerechnet; M-20 | so | ok |
| NG-14 | KfW tilgungsfrei 20 > n = 15; tilgungsfrei 12 > Zinsbindung 10 | Rate nach R-5.9 zum Anschlusszins | n = 15: endfällig abgelöst. tf 12: Monat 163 Zins 12.500,00, **Tilgung 0,00**; nie getilgt | D + R → Befund 1 |
| NG-15 | KfW 3 Mio. + Grobförderung B | M-22; Suche ab kleinstem zulässigem Preis | M-22; Suche U 3.643.155, M-32 | ok |
| NG-16 | Bindung 15, n = 10 und 11; Monatsraster und Jahresmodus | Restbindung bis 126 Monate | Monat: n = 10 VFE 4.627,90, n = 11 null. **Jahresmodus n = 10: null** | D → Befund 10 |
| NG-17 | Bindung 5, n = 3 und 5 | 2 Jahre VFE; keine | 22.971,07; 0 | ok |
| NG-18 | übernommen, Bindung 20, n = 5, Kennzeichen ja / nein / leer | leer = „ja“ (E-59) | leer wirkt wie „nein“: VFE 62.689,54 statt 45.023,21; KD_Ü 24.999,96 statt 15.000; L 869.467,71 statt 1.012.324,28 | D + R → Befund 3 |
| NG-19 | Bauzeit 1; Bauzeit 60 bei n = 5 | gerechnet; M-23 | so | ok |
| NG-20 | Baupreissteigerung −5 % | Raten sinken | BK 7.241.735,38 < 7.540.000 | ok |
| NG-21 | gefördert ohne Bankdarlehen | kein Bereitstellungszins | 0,00 | ok |
| NG-22 | Neubau, Zinsbindung 1 Jahr (Tilgung ab Monat 19); dazu Bauzeit 24, Bindung 2 Jahre im Stressfall | Rate zum Anschlusszins: L x (5 % + 2 %) / 12 | Basis: Rate 20.035,71 statt 23.375,00, Tilgung halbiert. **Stress: Tilgung 0,00 €**, Deckung 1,3212 gegen 1,2624 im Basisfall. Keine Probe meldet | D + R → Befund 1 |
| NG-23 | EK-Grenze mit Fehlbetrag (Faktor 4, n = 2) | Fehlbetrag zählt zum Bedarf (R-10.17) | Bedarf 2.135.393,20 = 1.208.955,01 + 926.438,19 | ok |
| NG-24 | E-60 genau = Bedarf bei 2,0 Mio. | P_EK = 2.000.000 | 2.000.000, bindend EK; aber **M-34** aus der Renditegrenze 2.407.109 | R → Befund 10 |
| NG-25 | E-60 = 0, Vollfinanzierung, Ziel 5 %, 8 %, 10 % | kein tragbarer Preis ohne EK (R-14.2, M-41) | **Preis 1.639.636 €, bindend EK, EK 0, Rendite nicht definiert, keine Meldung** | D + R → Befund 8 |
| NG-26 | Ziel −50 % / 30 % | M-33; Preis oder M-32 | M-33; P* 321.691 (Hebel) | ok |
| NG-27 | Probe verletzt nur über 2,2 Mio. (eingeschleust) | M-10 ohne Preis | M-10 | ok |
| NG-28 | 15-%-Regel genau an der Schwelle (netto 297.000,00) und 2 Cent darüber | „übersteigt“: nicht aktiviert / aktiviert | so, M-36 nur darüber | ok |
| NG-29 | 400.000 im Jahr 3 und im Jahr 4 | aktiviert / sofort | so | ok |
| NG-30 | Zuschussquote 100 % bei Darlehensquote 60 % | M-22 | M-22 | ok |
| NG-31 | Land Bayern mit Katalog Niedersachsen; Kappungsgrenze fehlt; Hebesatz fehlt | Meldung, keine Rechnung | Bayern: **still gerechnet**. Kappung fehlt: **Absturz** `TypeError` (`erhoehungspfad`). Hebesatz fehlt: **Absturz** | D + R → Befund 5 |
| NG-32 | Erhaltung 336.000 € im Jahr 1, Ziel 3,71259 % | P* nach R-11.4 = 2.350.070 | Suche **2.357.457**, ohne M-34; zwischen 2.350.071 und 2.350.089 verfehlt, ab 2.350.090 Sprung um +10.565,68 € EÜ | D + R → Befund 2 |
| NG-33 | Grobförderung ohne Zins nach der zinslosen Zeit, n = 38 | M-24 (R-14.11), auch in Suchen | `kalkuliere`: M-24. **Preissuche, Zielwertsuche und Haltedauertabelle: Absturz** `ValueError` | R → Befund 4 |
| NG-34 | Vorgaben außerhalb von R-3.4: H-18 −1 %, H-11 −100.000, H-09 −50 %, H-29 −500, H-17 −2.000, H-06 Leerstand −50 Pp., H-17 Staffel leer, H-21 Suchraster 0 | M-20 | alle gerechnet. Stress mit H-06 −50 Pp.: **r 12,992 %**, VK 3.720.905,81. Staffel leer: **Absturz** `IndexError`. Suchraster 0: **Absturz** `ZeroDivisionError` | D + R → Befund 6 |
| NG-35 | E-59 Anschlusszins −5 %, Beitrag −1 %; Bindung 0 Jahre | M-20 | gerechnet: Zins −1.944,88, Beitrag −388,98 je Monat | D + R → Befund 6 |
| NG-36 | eingeschleust: Mindestdeckung in R-5.12 vergessen | P-12 schlägt an (R-13.4: „P-04 und P-12 sichern die Bemessung“) | L 1.471.932,00 statt 1.226.609,99; **keine Probe**, nur Hinweis M-38 | D → Befund 7 |
| NG-37 | Zielwertsuche Faktor ohne Eigenkapital (GF-44) | gleiches Kriterium wie Preissuche | „Ziel an allen Rasterstellen erreicht“, kein Hinweis auf fehlendes EK | D → Befund 8 |
| NG-38 | 4.400 Zufallsfälle mit zulässigen Anwendereingaben: Ankauf und Neubau, alle Steuerstatus, Lesarten MA-016, MA-026, MA-030, MA-031, MA-032, MA-036, MA-037, Stress, beide Raster | nie Absturz, kein Fehlalarm | 4.300 Ergebnisse, 99 M-22, 1 M-23; **kein Absturz, keine verletzte Probe** | ok |
| NG-39 | Neubau im Rundungsmodus „keine“ | Toleranz 1E-30 (R-13.2) oder M-20 | **gesperrt: P-04 meldet −1E-53** | D + R → Befund 9 |

39 neue Fälle, 15 davon tragen Befunde (NG-09, 14, 16, 18, 22, 24, 25, 31, 32, 33, 34, 35, 36, 37, 39).

## Befunde

1. **[kritisch · belegt] R-5.9, R-5.10, R-5.19 – Endet die Zinsbindung vor dem Tilgungsbeginn, wird die Rate nie zum Anschlusszins gesetzt.**
   - Problem: R-5.9 setzt die Rate „in der ersten Periode nach der Bindung“ neu. Beginnt die Tilgung erst später (Bauzeit, im Stressfall verlängert, oder tilgungsfreie Anlaufjahre des KfW-Darlehens), gibt es zu diesem Zeitpunkt keine Rate. Das Dokument sagt nicht, welcher Zins in die erste Rate nach R-5.4 eingeht. Der Referenzrechner bildet sie mit dem Vertragszins, verzinst aber zum Anschlusszins.
   - Beleg (NG-22): Neubau mit Bauzeit 24 und Zinsbindung 2 Jahren. Im Basisfall beginnt die Tilgung in Monat 25, die Rate ist richtig. Im Stressfall (Bauzeit + 3) ist die Rate 21.705,36 €, der Zins zu 6,5 % ebenso: Die Tilgung ist null über die ganze Haltedauer. Die Deckung im ersten Jahr ist im Stressfall 1,3212, im Basisfall 1,2624; der Stress verbessert die Kennzahl, auf die die Bank schaut. Mit einem Jahr Zinsbindung halbiert sich schon im Basisfall die Tilgung (3.339,28 statt 6.678,57 €). KfW mit 12 tilgungsfreien Jahren bei 10 Jahren Bindung wird nie getilgt (NG-14). Keine Probe meldet es (Befund 7).
   - Vorschlag: In R-5.4 und R-5.9 festlegen: Die erste Rate einer Prozentannuität wird mit dem Zins der Periode des Tilgungsbeginns gebildet; liegt sie nach der Bindung, gilt die Anschlussregel H-07 ab dort. Eine Ratenprobe ergänzen: Zins + Tilgung = Rate, außer in der Schlussrate.
2. **[wichtig · belegt] R-11.4, R-11.5, R-6.16 – Die 15-%-Regel macht das Ziel im Preis sprunghaft; die Preissuche verfehlt dann die eigene Definition, ohne M-34.**
   - Problem: Die Schwelle der anschaffungsnahen Herstellungskosten hängt vom Kaufpreis ab. Unter dem Schwellenpreis wird die Erhaltung aktiviert, darüber sofort abgezogen. Der Endwertüberschuss springt deshalb am Schwellenpreis nach oben. R-11.5 kennt als Ursache der Nichtmonotonie nur die Abrundung des Gewerbeertrags („wenige Euro“). Die Liste „Vom Preis hängen ab“ in R-11.4 nennt die Aktivierung nicht.
   - Beleg (NG-32): Erhaltung 336.000 € im Jahr 1, Zielrendite 3,71259 %. Das Ziel ist bis 2.350.070 € erreicht, von 2.350.071 bis 2.350.089 € verfehlt, ab 2.350.090 € springt EÜ um 10.565,68 € und ist bis 2.357.457 € wieder erreicht. Die Suche liefert 2.357.457 € statt 2.350.070 € nach R-11.4, ohne M-34. P-14 besteht, weil sie nur P* + 1 prüft.
   - Vorschlag: Den Schwellenpreis aus R-6.16 geschlossen berechnen, als Stützstelle mit beiden Nachbarpreisen auswerten und bei einem Wechsel M-34 melden. In R-11.4 und R-11.5 die Aktivierung als preisabhängige Größe und als zweite Ursache der Nichtmonotonie nennen.
3. **[wichtig · belegt] R-3.3 E-59, R-5.12, R-5.16 – Die Voreinstellung „Förderdarlehen: ja“ ist nicht die vorsichtige; der Referenzrechner setzt „nein“.**
   - Problem: Das Dokument nennt die Voreinstellungen von E-59 „die vorsichtigen“. Das Kennzeichen „ja“ streicht aber die Vorfälligkeit und setzt den vertraglichen statt des kalkulatorischen Kapitaldienstes an. Beides ist günstiger. Der Referenzrechner nimmt ohne Angabe „nein“ (`ue.get("foerderdarlehen", False)`).
   - Beleg (NG-18): Restschuld 500.000 €, Bindung 20 Jahre, n = 5. Mit „ja“ sind es 45.023,21 € Vorfälligkeit, 15.000 € KD_Ü und 1.012.324,28 € Bankdarlehen. Mit „nein“ oder ohne Angabe sind es 62.689,54 €, 24.999,96 € und 869.467,71 €. Dokument und Referenzrechner rechnen dieselbe Eingabe also verschieden.
   - Vorschlag: Voreinstellung „nein“; „ja“ nur mit Bescheid und dann in der Liste der Abweichungen.
4. **[wichtig · belegt] Kapitel 14, R-14.11, R-11.5, R-11.10, R-11.13 – M-24 bringt Preissuche, Zielwertsuche und Haltedauertabelle zum Absturz.**
   - Problem: `kalkuliere` fängt das M-24 der Tranche ab (es wird dort als `ValueError` ausgelöst). `tragbarer_preis`, `suche_eingabe` und `haltedauer_tabelle` fangen nur `Meldung`.
   - Beleg (NG-33): Grobförderung ohne Zins nach der zinslosen Zeit, n = 38. Der Einzellauf endet mit M-24, die drei Suchen brechen mit `ValueError` ab. Der Eingangssatz von Kapitel 14 („endet nie mit einem Rechenfehler“) gilt damit nicht. RF-20 prüft M-24 nur über `kalkuliere`.
   - Vorschlag: M-24 als `Meldung` auslösen und für jede Suche einen Referenzfall mit M-24 aufnehmen.
5. **[wichtig · belegt] R-3.1, R-3.5, R-3.7 – Fehlende Katalogwerte haben kein definiertes Ergebnis.**
   - Problem: Für KAT-01 und KAT-08 sind die übrigen Länder ausdrücklich offen. Das Dokument regelt nicht, was geschieht, wenn Land oder Gemeinde keinen Katalogwert haben. Die Eingabeprüfung prüft nur, dass das Land nicht leer ist, nicht „Länder des Katalogs“ (E-03).
   - Beleg (NG-31): Land „Bayern“ mit dem Katalog Niedersachsen wird still gerechnet. Eine fehlende Kappungsgrenze oder ein fehlender Hebesatz führt zum Absturz mit `TypeError`.
   - Vorschlag: In R-3.7 eine Vollständigkeitsprüfung des aufgelösten Katalogs festlegen, je KAT-Wert, der im Lauf gebraucht wird, mit eigener Meldung („Katalogwert fehlt“: Kennung, Land, Gemeinde, keine Rechnung). Dazu E-03 und E-04 gegen die Liste der Katalogeinträge prüfen. Ob für Gemeinden außerhalb einer Landesverordnung die gesetzlichen Grundwerte (`BGB-558`) gelten, als Katalogregel mit Quelle festlegen; ungeprüft, nicht am Original gelesen.
6. **[wichtig · belegt] R-3.4, R-3.7, R-3.3 – Die Eingabeprüfung lässt Vorgaben und einzelne Felder ungeprüft.**
   - Ungeprüft und gerechnet werden:
     - E-58 = 0 und −1, mit negativer Mieteinzahlung (NG-09); das widerspricht R-6.4 („nicht unter null“).
     - Anschlusszins und Beitrag von E-59 negativ (NG-35); für beide nennt das Dokument keinen Bereich.
     - H-06 negativ (NG-34): Ein Stress von −50 Pp. Leerstand hebt die Rendite auf 12,992 %.
     - H-09, H-11, H-17, H-18, H-25 und H-29 außerhalb ihres Bereichs.
   - Abstürze: H-21 hat im Dokument keinen zulässigen Bereich; Suchraster 0 stürzt ab. Eine leere Staffel H-17 stürzt ebenfalls ab.
   - Vorschlag: In R-3.7 jede Vorgabe und jeden Wert von E-59 prüfen. H-21 bekommt Bereiche: Raster ≥ 1, Fenster ≥ 0, Obergrenze > 0, IZF-Untergrenze > −100 %. H-17 verlangt mindestens eine Stufe ab Alter 0. RF-20 um je einen Fall ergänzen.
7. **[wichtig · belegt] R-13.3 P-12, R-13.4 – Die Proben sichern die Bemessung nicht.**
   - Problem: R-13.4 sagt „P-04 und P-12 sichern die Bemessung“. P-12 vergleicht L aber mit denselben A, B, C, die die Bemessung errechnet hat.
   - Beleg (NG-36): Wird in R-5.12 die Mindestdeckung vergessen, steigt das Bankdarlehen um 245.322,01 € auf 1.471.932,00 €, und keine Probe meldet es. Ebenso bleibt Befund 1 (Tilgung null) ohne Meldung, weil keine Probe die Rate prüft.
   - Vorschlag: P-12 unabhängig rechnen. Die Deckungsungleichung mit dem gebuchten L und den kalkulatorischen Konditionen aus dem Auftrag prüfen, dazu (a) aus β, W und Ü_B, und bindet (b), dass L + 1 Cent sie verletzt. Eine Ratenprobe ergänzen (Befund 1). R-13.4 entsprechend fassen.
8. **[wichtig · belegt] R-11.6, R-14.2, R-11.10 – Ein tragbarer Preis ohne Eigenkapital entsteht über die Eigenkapitalgrenze.**
   - Problem: R-11.5 prüft D = 0 nur bei P*, R-11.6 nimmt dann min(P*; P_EK).
   - Beleg (NG-25): Mit E-60 = 0 und Vollfinanzierung liefert die Suche 1.639.636 € als tragbaren Preis, bindend „Eigenkapital“, bei EK 0, D 0 und nicht definierter Rendite, ohne Meldung. R-14.2 sagt dagegen „ohne eingesetztes Eigenkapital kein tragbarer Preis (M-41)“. Ähnlich meldet die Zielwertsuche ohne Eigenkapital „Ziel an allen Rasterstellen erreicht“, ohne Hinweis (NG-37).
   - Vorschlag: Die Prüfung D = 0 auf den Preis min(P*; P_EK) beziehen (M-41). Bei E-60 = 0 das Ergebnis „ohne Eigenkapital“ nennen. In R-11.10 einen Hinweis für Gitterwerte ohne Einlage festlegen.
9. **[Hinweis · belegt] R-13.2, R-12.2 – Fehlalarm im Rundungsmodus „keine“.**
   - Problem: P-04, P-06, P-07 und P-18 vergleichen exakt und ohne die Toleranz von 1E-30 aus R-13.2.
   - Beleg (NG-39): Der Neubau im Modus „keine“ ist gesperrt, P-04 meldet −1E-53 €. Der Modus ist nach R-12.2 für den Lehrbuchvergleich im Jahresmodus gedacht, der Kern lehnt ihn beim Neubau aber nicht ab. Den in der Aufgabe gesuchten Cent-Fehlalarm wie P-07 in Runde 1 gibt es im Modus „Cent“ nicht mehr (NG-38).
   - Vorschlag: Toleranz in allen Proben nach R-13.2; „keine“ außerhalb des Jahresmodus als M-20.
10. **[Hinweis · belegt] R-5.16, R-11.5 – Zwei kleine Unstimmigkeiten.**
    - (a) Jahresmodus (NG-16): Der Kündigungstermin von 126 Monaten wird auf 10 Perioden abgerundet. Bei Bindung 15 und n = 10 setzt der Jahresmodus keine Vorfälligkeit an, das Monatsraster 4.627,90 €. Das ist entgegen der Vorsichtsregel. Vorschlag: im Jahresmodus aufrunden, oder ganze Perioden ab dem ersten vollen Monat, und so festlegen.
    - (b) NG-24: Bindet das Eigenkapital (2.000.000 €), trägt das Ergebnis trotzdem M-34 aus der Renditegrenze bei 2.407.109 €. Vorschlag: M-34 nur für die bindende Grenze ausgeben.

## Am Dokument bestätigt (keine Befunde)

- Mietpfad nach `BGB-558`:
  - Ist-Miete über der Vergleichsmiete, mit und ohne Fluktuation;
  - Kappung genau erreicht;
  - Wartefrist am Rand der Haltedauer in beiden Lesarten von `MA-037`;
  - Mietpreisbremse greift, greift nicht, ist aus;
  - Fluktuation 100 %;
  - Bindungsende im ersten Jahr, im Verkaufsjahr, danach.
  Alles rechnet nach R-6.3, R-6.6, R-6.13 und R-6.14.
- Kalkulatorischer Kapitaldienst: H-25 unter dem Vertragszins, Mindesttilgung null, Reinertrag negativ, jeweils nach R-5.12.
- KfW-Höchstbetrag auf den Cent; Überfinanzierung mit KfW und Förderung ergibt M-22; die Suche beginnt beim kleinsten zulässigen Preis.
- Neubau: Bauzeit 1 und Bauzeit über der Haltedauer (M-23); negative Baupreissteigerung; kein Bereitstellungszins ohne Bankdarlehen.
- 15-%-Regel: genau an der Schwelle nicht aktiviert, 2 Cent darüber aktiviert; Jahr 3 aktiviert, Jahr 4 nicht.
- Eingeschleuste Probenverletzung mitten in der Suche: M-10 ohne Preis.
- 4.400 Zufallsfälle mit zulässigen Anwendereingaben: kein Absturz und kein Fehlalarm im Modus „Cent“. Der Satz „Der Kern bricht nie ab“ gilt damit für die Eingaben des Anwenders im Einzellauf; die Ausnahmen betreffen Suchen, Katalog und Vorgaben (Befunde 4 bis 6).

## Nicht geprüft

- Datumsränder (Monatsletzter, Schaltjahr) und Stichtag im Dezember (R-2.8): In Teil 1 nicht anwendbar, der Stichtag ist ein Monat.
- Vergleich zweier Fassungen (R-11.11) und Darstellung (R-12.7): nur über die Referenzfälle, nicht gesondert angegriffen.
- Zufallsfälle für Preissuche und Zielwertsuche: Sie laufen je mehrere Sekunden; geprüft sind die gezielten Fälle NG-23 bis NG-27, NG-32 und NG-33.
- Rechtsgrundlagen (`BGB-489`, `BGB-558`, `ESTG-6`, KfW-Konditionen): nicht am Original gelesen. Ob tilgungsfreie Jahre über der Zinsbindung beim KfW-Darlehen vorkommen, ist ungeprüft; Befund 1 trägt auch ohne diesen Fall, über das Bankdarlehen im Stressfall.
