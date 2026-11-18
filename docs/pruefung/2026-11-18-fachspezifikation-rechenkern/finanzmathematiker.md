```
Rolle: Prüfer Finanzmathematiker
Prüfobjekt: docs/fachspezifikation-rechenkern.md (Teil 1, Stand 2026-11-18, Entwurf zur Prüfrunde) und
            Referenzrechner research_notes/…/skripte/referenzrechner/ (Lauf referenzfaelle.py)
Gesamturteil: Trägt, mit Auflagen. Der Kern ist eindeutig genug, dass ich die Grobkalkulation Ankauf (RF-11)
  allein aus dem Text auf den Cent nachbauen konnte, einschließlich tragbarem Preis, Stressfall und
  Vergleichsrendite. Die Fallen aus den fünf Prüfrunden zum Bericht sind geregelt. Es gibt aber vier
  Mängel: Die Sollwerte des Testfalls im Monatsraster widersprechen R-7.3 um 7 Cent. Die Preisgleichung ist
  wegen der 100-Euro-Abrundung der Gewerbesteuer nicht streng monoton, und R-11.4 und R-11.5 liefern dann
  verschiedene Preise. Die Eingaben der Referenzfälle fehlen im Dokument. Beim übernommenen Darlehen fehlt
  das Eingabefeld für den Anschlusszins.
Note: 8 von 10. Zur 9 fehlen die Befunde 1 bis 4. Alle vier lassen sich im Dokument und im Referenzrechner
  beheben, ohne Auskunft von außen, mit rund einem halben Tag Arbeit. Die Befunde 5 bis 10 sind Hinweise.
```

Eigene Skripte, ohne Code des Referenzrechners gebaut, liegen unter `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs1-finmath/`:

| Skript | Inhalt |
|---|---|
| `s1.py` | Testfall S1 nach R-2.x, R-4.3, R-5.3, R-7.13 und R-9.3, im Jahresmodus und im Monatsraster |
| `darl.py` | Zinsbindung kürzer als Haltedauer: drei Anschlussregeln, Rundungsarten |
| `grob.py`, `preis.py` | RF-11 vollständig, mit Bemessung nach R-5.12, Steuer der Körperschaft, Unterlassensalternative, Vergleichsfaktor, Preissuche und Stressfall |
| `mono.py`, `knick2.py` | Monotonie von r(P) in Schritten von einem Euro |
| `eig.py` | Eigenschaften 3 und 6 der Renditeformel im Monatsraster |

Eingabewerte, die das Dokument nicht nennt, habe ich aus Bericht A.6 (Testfall) und `annahmen.py` (RF-11) genommen. Siehe Befund 3.

## Unabhängig nachgerechnet und bestätigt

| Gegenstand | Eigene Rechnung | Dokument |
|---|---|---|
| Testfall, Jahresmodus mit Rundung je Zahlung (R-4.3) | Endwert 584.366,28; Alternative 428.795,06; Endwertdifferenz 155.571,22; Rendite 7,8760 %; Sollzinsen 134.171,48 | gleich (R-4.3, R-12.3) |
| Testfall, Unterlassensalternative im Monatsraster | 428.794,92; ungerundet 428.795,0530 = 400.000 x 1,014^5 | gleich. NF-03 hält: Die Alternative hängt nicht vom Raster ab |
| Testfall, Monatsraster, Jahr 1 | Zins 27.740,46; Restschuld 685.740,46; Habenzins 118,75 | gleich. Steuer, Guthaben und Endwert weichen ab: Befund 1 |
| Periodensätze (R-2.6) | 0,001651581302; 0,006434030110; Effektivzins 4,0742 % | gleich |
| Renditeformel (R-10.5) | D = 448.628,86; r = 7,2461 %; Endwertüberschuss 63.919,08; andere Lesarten 68.101,945 und 71.817,145 | gleich (Rundung der Darstellung siehe Befund 10) |
| Gesamtkapitalrendite (R-10.11) | Z_S 93.920,04; g = 4,614 %; k = 2,138 % | gleich |
| Amortisation (R-10.12) | 354.180,00 / 409.664,52 / 466.495,06 gegen 405.600,00 / 411.278,40 / 417.036,30; Voreinstellung 3 Jahre, andere Lesart 2 Jahre | gleich |
| Restwertanteil Testfall | 89,98 % | gleich |
| Rundung je Rate (R-5.3) | 528.208,51 / 528.207,91 / 528.208,56 | gleich |
| Anschluss RF-08 (R-5.9) | Restschuld nach 10 Jahren 1.136.777,27; Raten 90.942,18 / 89.760 / 104.952,48 | gleich. Mehrdeutigkeit bei der Restlaufzeit: Befund 6 |
| Anschluss RF-11 im Monatsraster | Rate 7.155,22; Restschuld nach 120 Monaten 1.079.843,92; neue Rate 6.299,09 | gleich |
| Bankdarlehen (R-5.12, NF-09) | RF-11: B geschlossen 1.431.045,00; die gerundete Rate verletzt μ (103.035,31 > 103.035,24); gewährt 1.431.044,99. Neubau mit 200.000 Euro Reinertrag: 184.920,58. RF-12: 4.781.894,99 (Reinertrag 344.296,50). Die Cent-Suche endet, weil runde(B x c) monoton ist; das Ergebnis ist das größte zulässige B | gleich |
| **RF-11 Basisfall, Monatsraster, Körperschaft** | Reinertrag 103.035,24; A / B / C 1.560.000 / 1.431.044,99 / 2.640.000; Eigenkapital 1.208.955,01; Nachschuss im Monat 24: 91.529,75; Verkaufspreis 3.326.730,48; Endwert 2.374.377,18; Alternative 1.548.770,72; Endwertdifferenz 825.606,46; r 5,1617 %; r_U 1,4832 %; w(0) 1,193164; w(24) 1,160122; Deckung 1,200001; Endwertüberschuss 43.445,29 | alles gleich, auf den Cent |
| RF-11 Stressfall (NF-35) | Endwert 1.900.792,30; Endwertdifferenz 342.583,38; r 3,1778 %; Deckung 1,1471; Endwertüberschuss −444.360,24 | gleich |
| **Tragbarer Preis** (R-11.4) | Basis 2.425.585 (r = 5,0000053 %, bei einem Euro mehr 4,9999985 %); Darlehen nach (b); Eigenkapital 1.237.098,51; Endwertüberschuss 1,44. Stress 2.128.948; Darlehen nach (a) 1.383.816,20; Deckung 1,1863 | gleich |
| Steuer (R-7.7 bis R-7.10, R-7.14) | 29.825 / 15.825; 4.438,24 + 4.200 (2028 mit 14 %); ganze Tabelle der Personengesellschaft; 12.863,75 und 131,88; Grenzsätze 29,825 % und 42 % | gleich |
| Übrige Beispiele | Gewerbesteuer auf den Verkaufsgewinn 155.680; Steuer auf den Verkaufsgewinn 272.999,11 (Restwertanteil 82,94 %); Förderdarlehen 55.238,10 / 386.666,50 / 19.333,33; Rückzahlung 805.200; Investitionsstau 134.391,64 / 52.190,93 / 80.634,98; gebundene Miete 8,2000 / 8,7043 / 9,2396; Mittelabruf RF-12; interner Zinsfuß 100 % und 200 % | gleich |

**Äquivalenz „r > r_U genau dann, wenn ΔEW > 0“ (R-10.6 Nr. 2, P-11).** Die Aussage stimmt, wenn mindestens ein Zähler positiv und D > 0 ist. Dann gilt Z − Z_U = ΔEW als Identität, bei gleichem D und gleichem n. Ein Gegenbeispiel gibt es nur außerhalb dieser Bedingung (Befund 9). Weil es eine Identität ist, prüft P-11 nur, ob die Umsetzung in sich stimmig ist (Befund 7).

**Fallen aus den Runden 4 und 5:**

| Falle | Geregelt in |
|---|---|
| Freibetrag der Gewerbesteuer | R-7.8, R-7.9 |
| Bezug der Beleihungsquote und Untergrenze null | R-5.12 mit `MA-026`, M-21 |
| Wertpfad der Amortisation, dauerhaftes Erreichen, Spiegelung | R-10.12 |
| Probe des Investitionsstaus in Anteilen | P-06 |
| Alternativzins des Testfalls | R-4.3, R-10.4 |
| Rate nach der Zinsbindung | NF-07 |
| Suchbereich und Raster der Zielwertsuche | R-11.10 |
| Hinzurechnung als benannte Vereinfachung | R-7.1 |

## Befunde

**1. [wichtig · belegt] R-7.3 gegen R-2.2, R-2.3, R-2.6, R-10.6 Nr. 6, RF-06, RF-15 und `rf_testfall.py` Zeile 41 sowie `gegenrechnung.py` (`testfall_monat`): Die Sollwerte des Testfalls im Monatsraster folgen nicht der Abschreibungsregel des Dokuments.**

- R-7.3 regelt: Abschreibung des Planjahres = runde(Grundlage x Satz x Nutzungsmonate / 12), gebucht am Ende des Planjahres. Im Testfall sind das 17.600,00 Euro je Jahr.
- Der Referenzrechner bucht dagegen je Monat runde(17.600 / 12) = 1.466,67 Euro. Das ergibt 17.600,04 Euro je Jahr und 88.000,20 Euro statt 88.000,00 Euro über fünf Jahre. Den Buchwert führt er trotzdem mit 1.100.000 − 5 x 17.600.
- Die „unabhängige“ Gegenrechnung RF-15 rechnet `c(D(17600) / 12) * 12` und hat damit denselben Fehler. Sie bestätigt also nur die Lesart des Autors, nicht den Text.

Gegenrechnung nach R-7.3 (`s1.py`):

| Größe | nach R-7.3 | Dokument |
|---|---|---|
| Bemessung Jahr 1 | 9.778,25 | – |
| Steuer Jahr 1 | 2.933,48 | 2.933,46 |
| Guthaben Ende Jahr 1 | 10.185,23 | 10.185,25 |
| Endwert | 585.918,65 | 585.918,72 |
| Endwertdifferenz | 157.123,73 | 157.123,80 |

Mit 17.600,04 Euro je Jahr trifft mein Nachbau die Werte des Dokuments auf den Cent; die Ursache ist damit belegt.

Folgen:
- Ein Rust-Kern, der R-7.3 richtig umsetzt, fällt durch RF-06 und RF-15, obwohl die Toleranz „exakt“ ist.
- Keine Probe bemerkt den Fehler: P-08 läuft nur in der Grobkalkulation, nicht für die Testfall-Pläne (Befund 7).

Vorschlag:
- `s1_monat` und `testfall_monat` auf eine Buchung je Planjahr umstellen und die Werte neu festschreiben.
- Die Beispiele in R-2.2, R-2.3, R-2.6, R-10.6 Nr. 6 und R-15.3 nachziehen.
- Die Angabe zum Bericht in R-2.6 prüfen. Die 585.937,57 Euro des Berichts sind nicht nachgerechnet; ich weiß nicht, mit welcher Abschreibung sie entstanden sind.

**2. [wichtig · belegt] R-11.4 gegen R-11.5, R-11.10 und NF-34: Die Rendite fällt mit dem Preis nicht streng. Die beiden Definitionen des tragbaren Preises können verschiedene Preise ergeben.**

- R-11.5 behauptet: „Die Rendite fällt mit dem Preis streng“. R-11.10 behauptet: „mehrere Lösungen treten in 1a nur über die Prüffunktion auf“.
- Der Gewerbeertrag wird auf volle 100 Euro abgerundet (R-7.8). Steigt der Preis, steigt die Abschreibung; fällt der Gewerbeertrag dabei unter eine Hunderterschwelle, sinkt die Gewerbesteuer in einem Schritt um 14 Euro.
- RF-11 (`mono.py`): Von P = 2.425.541 auf 2.425.542 Euro steigt der Endwert um 14,12 Euro, das Eigenkapital nur um 1,10 Euro. Die Rendite steigt um 4,5E-7. Das entspricht etwa sieben Euro Preis.
- Mit einer Zielrendite von 5,002762 % statt 5 % (`knick2.py`) wechselt das Vorzeichen dreimal: bei 2.425.537/538, bei 2.425.541/542 und bei 2.425.545/546. R-11.4 („größter Preis mit r ≥ z“) ergibt dann 2.425.545 Euro, R-11.5 („kleinster Wechsel von erreicht nach verfehlt“) 2.425.537 Euro.
- Die Stützstellen liegen rund 336.000 Euro auseinander. M-34 kann solche Mehrfachlösungen deshalb nie melden.
- Wirtschaftlich geht es um wenige Euro. Aber das Dokument gibt zwei Lesarten vor, und die Zusicherung „ein Preis auf jedem Rechner“ hängt davon ab, welche man baut. Verletzt ist der Anspruch des Dokuments „eine Lesart“ (Zweck, Absatz 1).

Vorschlag:
- R-11.5 als die maßgebliche Definition festlegen. R-11.4 und P-14 verweisen darauf.
- Den Monotoniesatz einschränken: „fällt streng bis auf Rundungsstufen der Steuer (Gewerbeertrag auf 100 Euro, bis etwa 14 Euro Steuer je Stufe); Mehrfachwechsel innerhalb weniger Euro sind möglich und werden nicht gemeldet.“
- Dasselbe in R-11.10 für die Zielwertsuche.

**3. [wichtig · belegt] R-15.1 („Jeder Referenzfall nennt Eingaben“) gegen R-15.3, Kopf des Dokuments und R-5.12: Die Eingaben der Referenzfälle stehen nicht im Dokument. Den Testfall S1 kann man aus dem Text allein nicht nachbauen.**

Der Kopf sagt, das Dokument löse den Bericht für den Rechenkern ab. Trotzdem fehlen:

| Fall | Was fehlt | Wo es steht |
|---|---|---|
| Testfall S1 | Kaufpreis und Nebenkosten, Eigenkapital, Zins und Tilgung, Reinertrag mit Steigerung, Abschreibung, Habenzins, Kontokorrentzins, Verkaufserlös, Lehrbuchsteuer mit sofortiger Verrechnung | nur Bericht A.6; ich musste sie dort holen |
| RF-11 und RF-12 | Kostensteigerung 2 %, Kontokorrentzins 8 %, Startjahr 2027, Staffel des Körperschaftsteuersatzes, Neubaumiete 16,50 Euro, Kostenkennwert 2.900 Euro, Abschreibungssatz und weitere | nur `annahmen.py` |
| RF-09, dritte Zeile der Tabelle in R-5.12 | Reinertrag und Kapitaldienst des übernommenen Darlehens | nirgends ausgewiesen; B = 1.527.778 und 1.944.444 folgen nur mit 140.000 Euro Reinertrag und 2,5 % Kapitaldienst. „Sonst gleich“ (107.712 Euro) ergäbe einen negativen Kapitaldienst |

Vorschlag: In Kapitel 15 je Referenzfall eine Eingabetabelle aufnehmen, mit Herkunft (Bericht, Lehrbuch, Annahme). Alternativ ein Anhang „Eingaben der Referenzfälle“, aus `annahmen.py` erzeugt. Die Zeile von RF-09 ergänzen.

**4. [wichtig · belegt] E-59, R-5.8, R-5.11 und R-3.6: Beim übernommenen Darlehen fehlen Anschlusszins und Rate als Eingabe.**

- R-5.8 sagt, der Anschlusszins eines übrigen Darlehens sei „Eingabe (E-59)“. E-59 kennt aber nur Restschuld, Zins, Tilgungssatz und Ende der Zinsbindung.
- Folge: Endet die Bindung des übernommenen Darlehens vor dem Verkauf, kann der Kern nur M-24 melden. Die Grobkalkulation gebundener Bestände ist dann nicht rechenbar.
- Der Referenzrechner liest `anschluss_zins` als zusätzliches Feld (`_tranche_uebernommen`). Er weicht damit vom Dokument ab, und die Zählung „26 Eingaben“ (R-3.6) stimmt nicht.
- Zweite Lücke: Nach R-5.11 ist die Rate = Restschuld zum Stichtag x (Zins + Tilgungssatz). Die vertragliche Rate bezieht sich aber auf den ursprünglichen Nennbetrag. Gibt der Anwender den Tilgungssatz aus dem Vertrag ein, wird die Rate zu klein. Kapitaldienst KD_Ü und die Grenze (b) fallen dann zu günstig aus, also gegen die Vorsichtsregel (Spezifikation Kapitel 8).

Vorschlag:
- E-59 um den Anschlusszins ergänzen (Voreinstellung: heutiger Zins + H-05) und um die Rate laut Kontoauszug. Die Rate ersetzt den Tilgungssatz oder wird aus ihm abgeleitet, mit ausdrücklichem Bezug.
- R-3.6 nachzählen.

**5. [Hinweis · begründete Einschätzung] R-10.11: Für den Neubau ergibt „a_0 = Anschaffungsauszahlung zum Stichtag“ eine sinnlose Gesamtkapitalrendite. Auch „ohne Fremdkapital ist g = r“ gilt nur eingeschränkt.**

- Im Neubau fällt zum Stichtag nur das Grundstück an. In RF-12 sind das 1.296.000 Euro von 8.836.000 Euro.
- Der Zähler Z − D + Z_S + a_0 enthält dann Einlagen und Darlehen für rund 7,5 Mio. Euro Baukosten, der Nenner nicht. g wird um ein Vielfaches überhöht.
- Die Kennzahl steht ab der Vollkalkulation auf dem Blatt, also auch für 1b-2.
- „g = r ohne Fremdkapital“ gilt nur, wenn D = a_0, also bei einer einzigen Einlage zum Stichtag. Mit Nachschüssen (Investitionsstau im Jahr 2) gilt es nicht.

Vorschlag:
- a_0 als die auf den Stichtag abgezinsten Investitionsauszahlungen der Investitionsphase festlegen, mit demselben Faktor w wie D.
- Den Satz zu g = r auf „bei einer Einlage zum Stichtag und ohne Fremdkapital“ einschränken. Gehört zu `MA-028`.

**6. [Hinweis · belegt] R-5.9, Regel „Restlaufzeit bleibt“, und R-5.4: Die Zahl der Perioden ist nicht ganzzahlig. Das Dokument sagt nicht, wie damit umzugehen ist.**

- ln(3) / ln(1,04) − 10 = 18,011 Perioden.
- R-5.4 setzt m Tilgungsperioden mit „letzter Rate“ voraus, also eine ganze Zahl.

| m | Rate |
|---|---|
| 18,011 (reell) | 104.952 (Wert des Dokuments; der Referenzrechner rechnet reell) |
| 18 | 104.989 |
| 19 | 101.879 |

- Wie die Bruchperiode am Ende getilgt wird, ist offen.

Vorschlag: „m reell; Rate mit reellem m; die Tilgung folgt R-5.4, Restschuld nach der letzten vollen Periode in der Folgeperiode“. Oder m aufrunden. In jedem Fall ausdrücklich.

**7. [Hinweis · belegt] Kapitel 13: Welche Fehler keine Probe fängt.**

- P-01, P-02, P-03 und P-09 prüfen die Buchführung, nicht die Rechenregeln. Unbemerkt blieben:
  - Zins auf den Bestand der laufenden statt der Vorperiode;
  - falscher Zins nach der Zinsbindung;
  - falscher Index;
  - falsche Steuer;
  - Abschreibung im falschen Takt (Befund 1).
- P-11 ist nach R-10.6 eine algebraische Identität. Sie schlägt nur an, wenn Z und Z_U mit verschiedenem w oder D gerechnet werden.
- P-08 läuft im Referenzrechner nur in `grobkalkulation.py`. In den Testfall-Plänen hätte P-08 gemeldet: Summe der Abschreibungen 88.000,20 gegen einen Buchwert auf Basis von 88.000,00.

Vorschlag:
- P-08 für jeden Plan.
- Eine Zinsprobe neu: je Tranche und Periode Zins = runde(Restschuld_(u−1) x Satz_u / p), Habenzins und Kontokorrentzins ebenso, als unabhängige Neuberechnung.
- Eine Bemessungsprobe neu: Summe der Bemessungen über die Haltedauer = originäre Zahlungen ohne Investition − Abschreibungen − Finanzierungskosten + Habenzinsen + Verkaufsgewinn (Verkaufspreis − Buchwert).
- Bei P-11 vermerken, dass sie nur die Konsistenz prüft.

**8. [Hinweis · belegt] P-04 (R-13.3) gegen `grobkalkulation.py`, Zeilen 425 bis 436: Die Formel nennt nicht alle Glieder, die der Referenzrechner verwendet.**

- Der Referenzrechner fasst unter „laufende Zahlungen der Bauzeit“ Kosten − Miete + Steuer + Tilgung zusammen. Das Dokument nennt Steuer und Tilgung nicht.
- Bei sofortiger Verrechnung (E-44) erstattet der Kern im Neubau im Planjahr 1 Steuer, also in der Bauzeit. Nach dem Wortlaut schlösse P-04 dann nicht.

Vorschlag: „laufende Zahlungen der Bauzeit = Bewirtschaftung, Erbbauzins und Erhaltung − Mieteinzahlungen + Steuer + planmäßige Tilgung übriger Darlehen“ ausschreiben.

**9. [Hinweis · belegt] R-10.6 Nr. 2: „für jede Einlagen- und Entnahmenreihe“ ist zu weit gefasst.**

- Sind beide Zähler ≤ 0, sind r = r_U = −100 %, obwohl ΔEW ≠ 0 sein kann. Das ist erreichbar, wenn Entnahmen die Einlagen früh übersteigen.
- Beispiel: Die Alternative gerät in den Kontokorrent. Bei 100 Euro Einlage, 1.000 Euro Entnahme in Jahr 1, 8 % Kontokorrentzins und 30 % Steuer ist Z_U ≈ −1.117 + 1.057 < 0.
- Bei D = 0 ist r nicht definiert, ΔEW aber schon (RF-14: 63.947,36 Euro).
- P-11 nennt die erste Ausnahme, R-10.6 nicht.

Vorschlag: In R-10.6 Nr. 2 „sofern D > 0 und mindestens ein Zähler positiv ist“ ergänzen.

**10. [Hinweis · belegt] Kapitel 12: Kleine Rundungslücken.**

- (a) Für die Abschreibungsgrundlage und den Bodenwert fehlt eine Rundungsregel. Der Referenzrechner rundet den Boden auf Cent und rechnet die Grundlage als Differenz. Bei P* = 2.425.585 sind das 667.035,875 Euro Boden, gerundet 667.035,88. Das kann einen Cent Abschreibung kippen.
- (b) Die Cent-Suche für B (NF-09) setzt kaufmännische Rundung der Rate voraus. Bei einem Bankdarlehen mit umgestellter Rundung (`MA-013`, „Abschneiden“ oder „keine“) ist nicht gesagt, welche Rate gilt.
- (c) R-10.9 nennt 68.101,94 und 71.817,14 Euro. Mit dem gerundeten Endwert 585.086,02 sind es genau 68.101,945 und 71.817,145, kaufmännisch nach R-12.7 also ,95. Die Beispiele von RF-07 sind offenbar ungerundet gerechnet. Der Rechenmodus sollte dabei stehen.
- (d) Laufzeitannuität bei i = 0: Ob K / m gerundet wird, steht nicht da (R-5.4, R-14.1).

Vorschlag: Je ein Halbsatz in R-12.3, R-5.12 und R-10.9.

## Zu den Prüfaufträgen im Einzelnen

**1. Eindeutigkeit.**
- Drei Fälle allein aus dem Text nachgebaut:
  - Testfall S1 in beiden Rastern;
  - Zinsbindung kürzer als Haltedauer (RF-08 im Jahresmodus, RF-11 im Monatsraster);
  - Grobkalkulation mit tragbarem Preis (RF-11, Basisfall und Stressfall).
- Ich musste raten bei:
  - den Eingaben (Befund 3);
  - der Restlaufzeit (Befund 6);
  - den Vorträgen und der 100-Euro-Abrundung der Steuer der Alternative bei Körperschaften. R-9.5 („dieselben Parameter, eigener Verlustvortrag“) reicht hier, mein Nachbau trifft den Wert;
  - der Rundung des Bodenwerts (Befund 10a).
- Alles Übrige war eindeutig.

**2. Zeit und Zins.**
- Konforme Umrechnung, nominaler Darlehenszins und Zahlungszeitpunkte am Periodenende sind eindeutig und im Nachbau bestätigt.
- Die Alternative ist in beiden Rastern gleich, ungerundet auf 1E-4 Euro.
- Die Investition unterscheidet sich zwischen den Rastern, wie R-2.2 sagt.
- Der Vergleichsfaktor setzt den Zins nach Steuern monatlich an, das Konto versteuert jährlich. Die Abweichung ist in Eigenschaft 3 offen benannt; bestätigt sind 2 Cent bei einer Entnahme im Monat 30.

**3. Darlehen.**
- Alle Tilgungsarten der Beispiele stimmen, ebenso die drei Rundungsarten, Prolongation, Bankdarlehen als kleinster von drei Werten mit Untergrenze null, Mindestdeckung mit gerundeter Rate und Disagio.
- Offen sind Befund 4 und Befund 6.
- Die Vorfälligkeit (NF-10) ist eine Pauschale. Rechnerisch ist sie eindeutig; die Restbindung ist in ganzen Jahren, weil Haltedauer und Bindung ganzzahlig sind.

**4. Kennzahlen.**
- Die Äquivalenz gilt als Identität. Ein Gegenbeispiel gibt es nur außerhalb des Definitionsbereichs (Befund 9).
- Endwertüberschuss und tragbarer Preis passen zusammen: 1,44 Euro.
- Die Gesamtkapitalrendite stimmt für den Ankauf. Für den Neubau ist sie falsch definiert (Befund 5).
- Die Amortisation stimmt.
- Interner Zinsfuß: Die Vorzeichenregel ist richtig angewandt. Eine einzige Lösung kann unter −99 % liegen und wird dann als „keine Lösung“ gemeldet. Das ist bedeutungslos, weil die Kennzahl nur Nebenangabe ist.

**5. Grobkalkulation.**
- Die Lösung, der Knick und der Stressfall mit dem Darlehen des Basisfalls sind bestätigt.
- Eindeutigkeit und Monotonie siehe Befund 2.
- P_EK zählt Nachschüsse nach der Investitionsphase nicht zum verfügbaren Eigenkapital. Das ist vertretbar, weil das Blatt den Nachschussbedarf daneben ausweist. Schärfer wäre eine Umschaltung.

**6. Rundung und Proben.** Siehe Befunde 7, 8 und 10. NF-37 ist für die Wiederholbarkeit richtig begründet. „Ändern keinen Cent“ gilt nur fast immer, weil auch ein kleiner Unterschied eine halbe Cent-Grenze kippen kann. Das ist unschädlich, weil die zwölf Stellen festgelegt sind.

**7. Referenzrechner.**
- `python3 referenzfaelle.py` läuft durch: 15 Fälle, 529 Prüfungen, 529 bestanden, Rückgabewert 0.
- Stichproben an vier Modulen:

| Modul | Befund |
|---|---|
| `grobkalkulation.py` (Abschreibung, P-04, übernommenes Darlehen) | Abschreibung richtig nach R-7.3; P-04 umfassender als das Dokument (Befund 8); Anschlusszins als zusätzliches Feld (Befund 4) |
| `rf_testfall.py` | weicht von R-7.3 ab (Befund 1) |
| `kennzahlen.py` | setzt R-10.4, R-10.5, R-10.9 und R-10.11 wortgetreu um |
| `proben.py` | P-11 ist eine Identität; P-08 nicht für jeden Plan (Befund 7) |

- Belastbarkeit der 207 festgeschriebenen Werte: Die Werte von RF-11 im Basis- und Stressfall, den tragbaren Preis und die Kennzahlen des Testfalls im Jahresmodus habe ich unabhängig getroffen, ebenso die Beispiele der Kapitel 5, 7 und 10 aus der Tabelle oben.
- Nicht zu halten sind die Werte des Testfalls im Monatsraster, die über `s1_monat` entstehen (Befund 1).
- RF-15 ist keine unabhängige Gegenrechnung, weil sie dieselbe Lesart übernimmt. Künftig sollte sie aus dem Text allein entstehen, von jemandem, der den Referenzrechner nicht kennt.
- RF-12 (Neubau gefördert und frei, Bauzeitzinsen) und RF-13 (zehn Steuerstatus) habe ich nicht als ganzen Plan nachgebaut. Diese Werte sind nur so belastbar wie der Referenzrechner.

## Nicht geprüft

- **RF-12 und RF-14 als vollständige Finanzpläne:** nur Bemessung, Mittelabruf und Rate nachgerechnet, nicht Endwert und Rendite. Grund: Zeit; Vorrang hatten die drei verlangten Fälle.
- **RF-13 je Steuerstatus über den ganzen Plan:** nur die Steuerformeln einzeln.
- **RF-01 bis RF-04 (Lehrbuch, IWU):** in früheren Runden bestätigt, hier nicht erneut gerechnet.
- **Rechtsinhalte der Steuer:** Reichweite der erweiterten Kürzung, Zuschüsse und Finanzierungskosten in der Steuer gehören zum Juristen und Steuerberater. Rechnerisch habe ich sie nur so geprüft, wie sie geschrieben sind.
- **Meldungen, die der Referenzrechner nicht baut (M-25 bis M-29, M-35, M-36), und die Eingabeprüfung:** nicht ausgeführt.
- **Zielwertsuche auf Miete, Investitionsstau und Faktor (R-11.10):** Werte nicht nachgerechnet.
- **Quellen:** keine am Original gelesen.
