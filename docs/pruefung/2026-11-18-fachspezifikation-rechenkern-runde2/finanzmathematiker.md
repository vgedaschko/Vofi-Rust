```
Rolle: Prüfer Finanzmathematiker (Runde 2)
Prüfobjekt: docs/fachspezifikation-rechenkern.md (überarbeitet nach Prüfrunde 1) und Referenzrechner
            research_notes/…/skripte/referenzrechner/ (referenzfaelle.py, gegenrechnung.py)
Gesamturteil: Trägt, mit Auflagen. Alle zehn Befunde aus Runde 1 sind behoben. Den Ankaufsfall RF-11 habe ich
  in der neuen Fassung allein aus Text und Anhang A nachgebaut: Bankdarlehen, Mietpfad, Finanzplan,
  Alternative, Rendite, Endwertüberschuss, tragbarer Preis, Eigenkapitalgrenze, Stressfall, Deckung je Jahr,
  drei Anschlussregeln und vier Vorfälligkeitsfälle. Alles stimmt auf den Cent. Vier neue Mängel bleiben,
  keiner davon kritisch:
  - Der kalkulatorische Kapitaldienst des übernommenen Darlehens wendet einen Tilgungssatz, der sich auf den
    Nennbetrag bezieht, auf die Restschuld an. Er ist dadurch zu niedrig, entgegen der Vorsichtsregel.
  - Die Richtung „strenger“ ist bei den Bankvorgaben und bei H-07 nicht immer richtig.
  - In Kapitel 17 steht noch der alte Wortlaut zur Übermiete; die Formel in R-6.3 enthält die Rückführung nicht.
  - Der Zinsanstieg „bis zur Kreditzusage“ verändert das Darlehen nicht. Das ist nicht stimmig und
    unterschätzt das Eigenkapital im Stressfall.
Note: 8 von 10, knapp unter der 9. Zur 9 fehlen die Befunde 1 bis 4. Alle vier lassen sich im Dokument und im
  Referenzrechner beheben, ohne Auskunft von außen, mit etwa einem halben Tag Arbeit. Die Befunde 5 bis 10
  sind Hinweise.
```

Eigene Skripte, ohne Code des Referenzrechners gebaut, liegen unter `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs2-finmath/`:

| Skript | Inhalt |
|---|---|
| `rf11.py` | RF-11 nach R-2.x, R-4.3, R-5.3 bis R-5.16, R-6.1 bis R-6.16, R-7.2 bis R-7.8, R-7.16, R-8.1 bis R-8.6, R-9.1 bis R-9.7, R-10.3 bis R-10.14, R-11.2, R-11.3, R-11.8 |
| `preis.py`, `scan.py` | tragbarer Preis, Stressfall, P_EK, Knick, Monotonie |
| `extra.py`, `hebel.py` | Anschlussregeln, Neubemessung im Stress, Bankfall RF-19, Richtung „strenger“ |
| `s1b.py` | Testfall im Monatsraster, auch in der Rechenweise des Berichts |

Ich musste an zwei Stellen raten:
- Stressfall: „der Anschlusszins entsprechend“. Ich habe 4 % + 1 + 0,5 + 1 = 6,5 % angesetzt; damit trifft der Nachbau.
- Mietausfall im nachhaltigen Reinertrag: Siehe Befund 5. Für RF-11 ist das ohne Wirkung, im gebundenen Bestand nicht.

## Befunde aus Runde 1

| Nr. | Befund Runde 1 | Stand | Wo behoben, Beleg |
|---|---|---|---|
| 1 | Abschreibung im Monatsraster je Monat statt je Planjahr | behoben | R-7.3 bucht einmal am Ende des Planjahres, geprüft durch P-19 und P-08. RF-06 und RF-15 führen jetzt 585.918,65 Euro, Steuer im Jahr 1 2.933,48 Euro und Guthaben 10.185,23 Euro, wie in meiner Rechnung aus Runde 1. Die Angabe zum Bericht in R-2.6 habe ich nachgerechnet: Kontenzins nominal geteilt durch 12, ohne Rundung, Abschreibung je Jahr ergibt 585.937,57 Euro |
| 2 | Monotonie; R-11.4 und R-11.5 lieferten verschiedene Preise | behoben | R-11.4 hat jetzt eine einzige Definition. R-11.5 sucht nach und meldet Mehrfachwechsel mit M-34; die Monotonie ist eingeschränkt, R-11.10 ebenso. Nachgerechnet: Mit 5,000253 % ist das Ziel bis 2.317.188 Euro erreicht, von 189 bis 192 verfehlt, von 193 bis 196 erreicht und ab 197 verfehlt, genau wie in RF-20. Zum verbleibenden Rest siehe Befund 10 |
| 3 | Eingaben der Referenzfälle fehlten | behoben | Anhang A. RF-11 ließ sich bis auf die zwei Stellen oben aus Text und Anhang nachbauen. Die Zeile von RF-09 ist ergänzt (A.3); 1.527.777,74 Euro nachgerechnet |
| 4 | Übernommenes Darlehen: Anschlusszins und Rate fehlten | behoben, mit Rest | E-59 hat neun Werte. R-5.11 rechnet die Rate aus dem ursprünglichen Nennbetrag: 1.250,00 Euro im Monat, nachgerechnet. Rest: In R-3.6 heißt es „davon 28 ohne Voreinstellung“; richtig sind 21 (Befund 9). Neu ist die Bezugsbasis der kalkulatorischen Tilgung (Befund 1) |
| 5 | Gesamtkapitalrendite im Neubau mit dem Grundstück allein als a_0 | behoben | R-10.11: a_0 ist die abgezinste Investition der Investitionsphase; „g = r“ gilt nur noch bei einer Einlage zum Stichtag. Die 8.929.843,91 Euro sind plausibel (rund 9,5 Monate Abzinsung auf 7,72 Mio. Euro Baukosten), nicht auf den Cent nachgerechnet |
| 6 | Restlaufzeit bei „Restlaufzeit bleibt“ nicht ganzzahlig | behoben | R-5.9 rundet ab, mindestens eine Periode, mit Rückfall M-40. RF-08: 104.989 Euro, wie meine Zeile m = 18 aus Runde 1. RF-11: rechnerisch 210,13 Monate, abgerundet 210, Rate 6.622,11 Euro |
| 7 | Proben fangen Fehler nicht | behoben | P-08 läuft in jedem Lauf. Neu sind P-15 mit der Brücke, P-17 (Zins), P-18 (Index) und P-19 (Takt). P-11 ist als Identität bezeichnet (R-13.4). Die Brücke von P-15 habe ich algebraisch geprüft: Sie schließt in allen drei Lesarten von `MA-031` und mit der Vorfälligkeit der Privatperson |
| 8 | P-04 nannte Steuer und Tilgung nicht | behoben | P-04 hat drei Teile; Steuer und planmäßige Tilgung sind genannt. RF-12: 5.141.964,13 + 4.007.142,85 = 9.015.152,34 + 133.954,64 Euro, und 133.954,64 = 54.961,41 + 78.993,23 Euro |
| 9 | Geltungsbereich der Äquivalenz in R-10.6 Nr. 2 | behoben | „D > 0 und mindestens ein Zähler positiv“ steht in R-10.6 Nr. 2, P-11 und R-10.11 |
| 10 | Rundungslücken | behoben | (a) Boden: R-7.3 und R-12.3, Beispiel 637.239,625 → 637.239,63 nachgerechnet. (b) Bemessung immer kaufmännisch: R-5.12 und R-12.3. (c) R-10.9 nennt den Rechenmodus „ohne Rundung“. (d) runde(K / m) bei Zins null: R-5.4 und R-12.3 |

## Unabhängig nachgerechnet und bestätigt

| Gegenstand | Eigene Rechnung | Dokument |
|---|---|---|
| **RF-11 Basisfall, Monatsraster, Körperschaft** | RE_n 103.035,24; i_k 5 %, τ_k 2 %; A / B / C 1.560.000,00 / 1.226.609,99 / 2.640.000,00 (die geschlossene Form 1.226.610,00 verletzt μ mit 103.035,31); Eigenkapital 1.413.390,01; Nachschuss 72.484,81 im Monat 24; Rate 6.133,05; Restschuld nach 120 Monaten 925.579,91; neue Rate 5.399,22; Verkaufspreis 3.212.578,13; Ablösung 886.727,18; Verkaufsgewinn 999.589,46; Endwert 2.524.305,59; Alternative 1.770.603,63; ΔEW 753.701,96; r 4,5271 %; r_U 1,4831 %; w(0) 1,193164; w(24) 1,160122; EÜ −140.507,34 | alles gleich, auf den Cent |
| Mietpfad R-6.3 (RF-11, `MA-037` vorsichtig) | Erhöhungen in den Monaten 37 / 52 / 73 / 88 / 103 / 118 / 133 auf 9,4473 / 9,7750 / 10,3607 / 10,5679 / 10,7793 / 10,9949 / 11,4390. Ebenso die andere Lesart (13 / 28 / 43 / 58), die bekannte Historie (8,6250) und die Übermiete 11,00 (10,5960 / 10,2858 / 10,0723 / 9,9584 / 10,1575), diese aber nur nach dem Prosatext (Befund 3) | gleich |
| Deckung R-10.14 (RF-11) | Basis 1,400 / 1,3918 / **1,3835** (kleinste, Jahr 3) / … / 1,8116 / 2,0853 (Jahr 11). Stress 1,2354 / 1,2273 / **1,2191** / … / 1,5815 (Jahr 11) | gleich |
| Anschlussregeln (RF-11) | ΔEW und Deckung im Jahr 11: 753.701,96 und 2,0853 / 754.107,08 und 1,8358 / 754.381,58 und 1,7002 | gleich |
| **Tragbarer Preis** R-11.4 | P* = 2.317.235 Euro (r 5,000001 %, ein Euro darüber 4,999995 %); EÜ 0,35 Euro; Eigenkapital 1.322.348,51, insgesamt 1.395.253,65 Euro. Kein verfehlter Preis unter P* im Raster von 997 Euro. Im Bereich von 2,31 bis 2,325 Mio. Euro nur ein Wechsel, bei 2.317.236 Euro | gleich |
| Knick und Steigung | 8,3876 / 8,3164 / 8,2453 / 8,1492 / 8,0542 % um 1.887.092 Euro; zwischen 1,5 und 3,6 Mio. Euro streng fallend in Schritten von 100.000 Euro | gleich |
| Eigenkapitalgrenze R-11.6 | P_EK = 2.138.910 Euro: 1.126.191,01 + 73.808,50 = 1.199.999,51 Euro; einen Euro darüber 1.200.000,60 Euro | gleich |
| **Stressfall** R-11.8 | ΔEW 196.967,13; r 2,3619 %; EÜ −715.580,11; P*_Stress 1.978.674 Euro (EÜ 0,18 Euro) | gleich |
| Vorfälligkeit R-5.16 (RF-14, RF-19) | 1 / 120: 108.146,07, Endwert 1.071.298,15, r −24,204 %. 1 / 480: 114 Monate, 114.154,19. 5 / 240: 66 Monate, 60.008,94. 12 / 180: null. 5 / 120: 54.553,59 | gleich |
| Zielwertsuche R-11.10 | Vergleichsmiete 9,60 (bei 9,59: EÜ −405,72); Faktor 19,06; Investitionsstau bei 2,2 Mio. Euro 246.500 (bei 246.600: −29,04) | gleich |
| Bankfall RF-19 (Lesart 2) | L 1.560.000 nach (a); Deckung 1,3210, kleinste 1,3054; Stress 1,1480 und 1,0181 im Jahr 12 | gleich |
| Bausteine Neubau RF-12 | BK_0 7.540.000,00; Raten 419.921,98 / 420.957,62 / 437.879,56; Summe 7.719.152,34 (gleich in beiden Rechenfolgen). Bereitstellungszins 10.017,86 / 9.755,89. KfW-Grenze (b) 1.007.142,85. Entgelte 1.499,85 / 1.799,82. Rückzahlung 822.091,51. Zuschuss 1.743.830,47, Gebäudeanteil 1.543.830,47 | gleich |
| Steuerbeispiele R-7.8, R-7.16 | 17.407,50 + 1.400,00; 96.532,50 + 71.400,00 = 167.932,50; 97.932,50; 34.025,00. 31.925,00 nur ohne Erbbauzins (Befund 6) | gleich |
| Gebundener Bestand, Grenzen | A 1.060.000; KD_Ü 24.999,96; B 743.803,42 nur mit monatlich gerundetem Mietausfall (Befund 5) | gleich, bei der vom Referenzrechner gewählten Lesart |

**Setzungen der Überarbeitung (Kapitel 17).**
- *„Zielgröße der Suche ist der Endwertüberschuss“* ist richtig. Bei D > 0 gilt EÜ ≥ 0 genau dann, wenn r ≥ z, weil (1 + r)^n = Z / D ist; ist Z ≤ 0, ist EÜ < 0 und r = −100 %. Bei D = 0 bleibt EÜ = Z definiert. Preissuche und Zielwertsuche haben damit ein Kriterium.
- *„Restlaufzeit wird abgerundet“* ist eindeutig. Für die Deckung ist das vorsichtig. Für die Endwertdifferenz ist es die günstigere Rundung, weil schneller getilgt wird; ein Fehler ist das nicht, weil „Restlaufzeit bleibt“ nicht voreingestellt ist. Folgerichtig wird es erst durch Befund 2.
- *„Maßstab sind Endwertdifferenz und Rendite, nicht der Endwert“* ist im Fall des Zuschusses richtig: Die sofortige Einnahme hat die niedrigste ΔEW und die niedrigste Rendite, den höchsten Endwert. Eindeutig ist die Setzung aber nicht, siehe Befund 8.
- *„Die Hinzurechnung gehört zum gekürzten Ertrag“* ist in sich folgerichtig: Formel R-7.8, R-7.16, Tabelle R-7.14 mit g_op = 0. Es ist aber die günstigere Lesart, ohne Kennung, siehe Befund 7.

## Befunde

**1. [wichtig · belegt] R-5.12 (b), „Kalkulatorischer Kapitaldienst KD_Ü“, mit E-59 und R-5.11: Beim übernommenen Darlehen ist die kalkulatorische Tilgung zu niedrig. Die Bank gibt dadurch zu viel Darlehen, gegen die Vorsichtsregel.**

- KD_Ü = p x runde(Schuld x (i_k + τ_k) / p). Der Referenzrechner setzt für „Schuld“ die Restschuld ein, für τ_k den Tilgungssatz der Tranche.
- Nach E-59 bezieht sich dieser Tilgungssatz aber auf den ursprünglichen Nennbetrag (R-5.11). Damit sind zwei verschiedene Bezugsgrößen gemischt.
- Gebundener Bestand (RF-11), Restschuld 500.000 Euro, Nennbetrag 600.000 Euro, τ 2 %, i_k 3 %:

| Lesart | kalkulatorische Tilgung je Jahr | KD_Ü | B = Bankdarlehen |
|---|---|---|---|
| heute: 2 % auf die Restschuld | 10.000 | 24.999,96 | 743.803,42 |
| Tilgung wie im Vertrag, auf die Restschuld umgerechnet (2,4 %) | 12.000 | 27.000,00 | 715.231,42 |
| Schuld = Nennbetrag | 12.000 | 30.000,00 | 672.374,28 |

- Die vertragliche Tilgung beträgt im ersten Jahr schon rund 12.500 Euro; die Rate von 1.250 Euro im Monat enthält nur rund 210 Euro Zins.
- Die Rechnung setzt also eine kleinere Tilgung an, als der Vertrag vorschreibt. Das Bankdarlehen liegt um 28.572 Euro zu hoch, gemessen an der folgerichtigen Lesart.

Vorschlag:
- In R-5.12: „Für das übernommene Darlehen ist τ_k = max(Tilgungssatz x Nennbetrag / Restschuld; H-04), angewandt auf die Restschuld zum Stichtag.“
- Das Wort „Schuld“ in der Formel ausdrücklich als Restschuld zum Stichtag bezeichnen.
- Werte des gebundenen Bestands und von R-11.11 neu festschreiben.

**2. [wichtig · belegt] R-3.2 und NF-39 gegen R-3.4 (H-02, H-03, H-04, H-07, H-25) und R-5.9: Die Richtung „strenger“ ist für die Finanzierungsvorgaben eine Eigenschaft des Falls und nicht der Vorgabe. Bei H-07 widerspricht sie dem Dokument selbst.**

- R-3.2 definiert „strenger“ als die Richtung, in der der tragbare Preis sinkt.
- H-07: Die Spalte nennt „Restlaufzeit bleibt“ als strenger. Nach R-5.9 hat aber gerade diese Regel die höchste Endwertdifferenz (754.381,58 gegen 753.701,96 Euro). Nachgerechnet steigt auch der tragbare Preis: 2.317.632 gegen 2.317.235 Euro, bei „Rate bleibt“ 2.317.477 Euro.
  - Der Bearbeiter kann also ohne Begründung auf die Regel wechseln, die das Vorhaben am günstigsten rechnet.
  - Strenger ist sie nur bei der Deckung im Jahr nach dem Anschluss.
- H-02, H-03, H-04 und H-25: Ein kleineres Darlehen senkt den tragbaren Preis nur bei positivem Hebel, also wenn der Darlehenszins nach Steuern unter der Zielrendite liegt. Gegenbeispiele aus RF-11 (`hebel.py`):

| Fall | P* mit μ = 1,2 | P* mit μ = 1,3 („strenger“) | Unterschied |
|---|---|---|---|
| Zielrendite 2 %, Zins 4 % | 2.973.391 | 2.983.619 | +10.228 |
| Zielrendite 2 %, Zins 6 % | 2.858.254 | 2.877.470 | +19.216 |
| Zielrendite 5 % (Haus), Zins 8 % | 2.055.449 | 2.056.155 | +706 |

  - Eine niedrige Zielrendite ist bei befreiten Körperschaften und im geförderten Bau zu erwarten (R-11.14, Kapitel 16).
  - Dort lockert die als „strenger“ freigegebene Richtung das Vorhaben ohne Begründung.

Vorschlag:
- Für die Vorgaben, die das Bankdarlehen bemessen (H-02, H-03, H-04, H-25), festlegen: „strenger heißt kleineres Darlehen“, ausdrücklich als Ausnahme von R-3.2 mit der Begründung „Bankensicht“.
- Für H-07 die Spalte auf „Voreinstellung“ setzen, also mit Begründung, oder auf „Tilgungssatz bleibt“ als strengste Regel für ΔEW und Preis.
- Alternativ prüft der Kern jede Abweichung, indem er den tragbaren Preis mit beiden Werten rechnet. Das kostet zwei Preissuchen je Abweichung.

**3. [wichtig · belegt] Kapitel 17, Zeile NF-12, und die Formel in R-6.3 gegen den Text und das Beispiel von R-6.3: Für die Miete über der Vergleichsmiete gibt es noch den alten Wortlaut, und die Formel rechnet die Rückführung nicht.**

- Die Tabelle in Kapitel 17 sagt: „Miete über der Vergleichsmiete bleibt stehen, bis die Vergleichsmiete sie einholt.“
- R-6.3 sagt das Gegenteil, im Absatz „Ist-Miete über der Vergleichsmiete“: Die Miete wird über d Jahre auf die Vergleichsmiete zurückgeführt. Das Beispiel zeigt 11,00 / 10,5960 / 10,2858 / 10,0723 / 9,9584 Euro.
- Der Formelblock von R-6.3 kennt nur Erhöhungen: „neu … > Miete_(m−1); … sonst Miete_m = Miete_(m−1)“.
- Ein Entwickler, der die Formel oder die Tabelle umsetzt, lässt die Miete bei 11,00 Euro stehen. Das ist die günstigere Lesart, und RF-18 fällt dann durch.

Vorschlag:
- In den Formelblock aufnehmen: „Ist m der erste Monat eines Planjahres j ≥ 2 und Ziel_m < Miete_(m−1), dann Miete_m = max(Ziel_m; Vergleichsmiete_j); t_letzte bleibt unverändert.“
- Prüfen, ob eine Senkung t_letzte setzt. Nach dem Beispiel tut sie es nicht: Die Erhöhung im Jahr 6 auf 10,1575 Euro wirkt sofort.
- NF-12 in Kapitel 17 an R-6.3 angleichen.

**4. [wichtig · belegt] R-11.8 und NF-35, „Zins des Bankdarlehens (Zinsanstieg bis zur Kreditzusage)“, gegen „Das Bankdarlehen wird nicht neu bemessen“: Der Stressfall beschreibt keinen stimmigen Zustand und weist zu wenig Eigenkapital aus.**

- Begründet ist NF-35 so: „Die Bank bemisst ihr Darlehen heute aus den Basisannahmen; der Stress trifft das Vorhaben danach.“
- Ein Zinsanstieg *bis zur Zusage* liegt aber vor der Bemessung. Die Bank rechnet dann mit i_k = max(4,5 %; 5,5 %), und B fällt auf 1.144.835,99 Euro.
- RF-11 (`extra.py`):

| Größe | Stressfall wie im Dokument | mit neu bemessenem Darlehen |
|---|---|---|
| Bankdarlehen | 1.226.609,99 | 1.144.835,99 |
| Eigenkapital der Investitionsphase | 1.413.390,01 | 1.495.164,01 (+81.774,00, +5,8 %) |
| VOFI-Rendite | 2,362 % | 2,404 % |
| ΔEW | 196.967,13 | 216.856,20 |

- Das Blatt zeigt das nötige Eigenkapital im Stressfall (R-11.7) um 81.774 Euro zu niedrig.
- Rendite und Deckung fallen in der Rechnung des Dokuments zwar ungünstiger aus, aber nur, weil der Hebel im Stress negativ ist; bei positivem Hebel kehrt sich das um.

Vorschlag:
- L_Stress = min(L_Basis(P); L(P) aus R-5.12 mit dem Zins nach Zusage), sonst unverändert.
- Oder die Größe umbenennen in „Zinsanstieg nach der Zusage bis zur Auszahlung“. Das gibt es bei festem Zins nicht; deshalb trägt nur die erste Lösung.
- P-04 (a) im Stressfall mit diesem L.

**5. [Hinweis · belegt] R-5.12, „Nachhaltiger Reinertrag“: „Mietausfall auf den Rohertrag_n“ und „Bewirtschaftung“ sind nicht auf den Cent bestimmt. Bei der Toleranz „exakt“ fällt eine wortgetreue Umsetzung durch.**

- Der Referenzrechner rechnet den Mietausfall als Summe über die Monate von Roh_m − runde(Roh_m x 0,98).
- Liest man „Mietausfall auf den Rohertrag_n“ als Satz x Jahresrohertrag, ergibt sich im gebundenen Bestand:

| Größe | Referenzrechner | Satz x Jahresrohertrag |
|---|---|---|
| Mietausfall | 2.477,40 | 2.477,38 |
| RE_n | 92.479,44 | 92.479,46 |
| B | 743.803,42 | 743.803,66 |

- Ebenso offen ist, ob „Bewirtschaftung“ die Summe der Monatszahlungen (28.911,96 Euro) oder der Jahresbetrag (28.912,00 Euro) ist.

Vorschlag: „Mietausfall = Summe über die zwölf Monate von (Roh_m − runde(Roh_m x (1 − H-15 − H-27))); Bewirtschaftung = Summe der Zahlungen nach R-6.8, R-6.9 dieser Monate.“

**6. [Hinweis · belegt] R-7.16, Beispiel „Bei sofortiger Verrechnung und 60.000 Euro Entgelten: Hinzurechnung 15.000 Euro, Steuer 31.925,00 Euro“: Der Erbbauzins des ersten Beispiels fehlt, ohne dass es dasteht.**

- Mit den 40.000 Euro Erbbauzins wären es 25 % x (60.000 + 20.000) = 20.000 Euro Hinzurechnung und 32.625,00 Euro Steuer.
- Der Referenzrechner rechnet ohne Pacht (`rf_neu.py`, Zeile 130).

Vorschlag: „… und 60.000 Euro Entgelten ohne Erbbauzins“.

**7. [Hinweis · begründete Einschätzung] R-7.8 und R-7.16, NF-47 („Hinzurechnung gehört zum gekürzten Ertrag“): Das ist die günstigere Lesart, ohne Kennung im Verzeichnis und ohne Beleg im Kataster.**

- Die andere Lesart wäre: Die Hinzurechnung bleibt neben dem gekürzten Ertrag gewerbesteuerpflichtig. Sie rechnet ungünstiger.
- Ob die Verwaltung die Hinzurechnungen auf den Grundbesitz der Kürzung zuordnet, habe ich nicht am Original geprüft. Das gehört zum Steuerberater.
- Rechnerisch ist die Setzung folgerichtig umgesetzt: R-7.14 setzt g_op = 0, und s_FK bei sofortiger Verrechnung gilt nur ohne Kennzeichen.
- Wirkung in RF-11: null, weil die Entgelte unter dem Freibetrag bleiben. Wirkung entsteht erst ab etwa 200.000 Euro Entgelten im Jahr, also bei rund 5 Mio. Euro Darlehen.

Vorschlag: Als Modellannahme führen (Gewicht gering bis mittel), mit Quelle aus der Verwaltungsauffassung, oder die vorsichtige Lesart voreinstellen.

**8. [Hinweis · begründete Einschätzung] Kapitel 17, Setzung 1, und „Wie dieses Dokument zu lesen ist“ (Maßstab der Vorsicht): Endwertdifferenz, Rendite und tragbarer Preis können verschiedene Lesarten als die ungünstigere ausweisen. Eine Rangfolge fehlt.**

- Beispiel: Lesart Y hat 100 Einlage und wächst 10 Jahre mit 5 %. Lesart X legt zusätzlich 100 ein, die mit 3 % wachsen. Die Alternative bringt 1,5 % nach Steuern.

| Lesart | ΔEW | Rendite |
|---|---|---|
| Y | 46,84 | 5,00 % |
| X | 65,17 | 4,04 % |

- Nach ΔEW ist Y vorsichtiger, nach der Rendite X.
- Solche Fälle entstehen, wo eine Lesart Nachschüsse verschiebt: `MA-016`, `MA-031`, `MA-032`.

Vorschlag: Rangfolge festlegen, zum Beispiel „maßgeblich ist der tragbare Preis, wo er gerechnet wird, sonst die Endwertdifferenz (R-10.2); die Rendite nur bei Gleichstand“. Weichen die Größen ab, steht das im Verzeichnis bei der Annahme.

**9. [Hinweis · belegt] Kleine Unstimmigkeiten.**

- (a) R-3.6: Für den Ankauf gebundener Bestände ergibt die Tabelle 34 Felder, davon 4 + 3 + 6 = 13 mit Voreinstellung. Ohne Voreinstellung sind es also 21, nicht 28. Außerdem fehlen E-44 und E-64 in der Zählung, obwohl beide für „beide“ gelten und eine Voreinstellung haben.
- (b) R-10.2 und R-15.3 nennen für den Testfall ΔEW 155.571,23 Euro neben dem Endwert 584.366,28 Euro. Mit Rundung je Zahlung ist die Differenz 584.366,28 − 428.795,06 = 155.571,22 Euro, so steht es auch in `erwartete_werte.json`. 155.571,23 Euro ist der ungerundete Wert. Den Modus dazuschreiben.
- (c) R-15.6: Die Zeile „Prüfrunde 1, Finanzmathematiker … der Ankauf ist auf dem Stand des Entwurfs bestätigt“ kann jetzt nachgezogen werden. Bestätigt ist der Stand nach der Überarbeitung, siehe die Tabelle oben.

**10. [Hinweis · begründete Einschätzung] R-11.4 gegen R-11.5 und NF-34 („R-11.4 und R-11.5 beschreiben jetzt dieselbe Größe“): Das gilt nur so weit, wie Stützstellen und Fenster reichen.**

- R-11.4 verlangt, dass das Ziel bei jedem kleineren Preis erreicht ist. R-11.5 sichert das nur für die 40 Stützstellen, die in RF-11 rund 446.000 Euro auseinanderliegen, und für das Fenster von 20 Euro.
- Eine Delle zwischen zwei Stützstellen, mehr als 20 Euro unter dem Fund, bliebe unentdeckt. Die Kernumsetzung lieferte dann einen anderen Preis als die Definition.
- In RF-11 tritt das nicht auf; ich habe ein Raster von 997 Euro geprüft.
- Mögliche Auslöser sind Sprünge, zum Beispiel das Umschalten der Aktivierung nach R-6.16, das bei rund 864.000 Euro Kaufpreis liegt.

Vorschlag: In R-11.4 „im Sinn des Verfahrens nach R-11.5“ ergänzen, oder bekannte Sprungstellen (Schwelle nach R-6.16) als zusätzliche Stützstellen aufnehmen.

## Nahtstellen und alter Wortlaut

Gesucht habe ich nach alten Werten (2.425.585; 43.445; 1.208.955; 1.431.044,99 als Basisdarlehen; 825.606), nach „streng“, „Folgejahr“ und „bleibt stehen“.

Gefunden:
- NF-12 (Befund 3);
- H-07 (Befund 2).

Ohne Widerspruch:
- Kapitel 5 gegen Kapitel 11: Mittelabruf, KfW-Tranche, Bemessung, Stress.
- Kapitel 6 gegen Kapitel 8: maßgebliche Jahresmiete, Leerstand nur im Verkaufspreis, Erbbauzins.
- Kapitel 7 gegen Kapitel 9: Kennzeichen wirkt nicht in der Alternative; Kontokorrentzinsen als Entgelte; s_Z mit Gewerbesteuer.
- Regeltext gegen Anhang A: bis auf H-07.
- Spezifikation, Zeilen „Grobkalkulation“, „Restwert“ und „Kennzahlen“: stimmen mit R-5.12, R-8.1, R-10.14 und R-11.4.

## Referenzrechner und Gegenrechnung

- `python3 referenzfaelle.py`: 20 Fälle, 906 Prüfungen, 906 bestanden, Rückgabewert 0, 72 Sekunden.
- `python3 gegenrechnung.py`: 16 Prüfungen, 16 bestanden.
- `gegenrechnung.py` importiert nur `json`, `os` und `decimal`. Vom Code des Referenzrechners ist sie also unabhängig, von seiner Lesart nicht, weil sie vom selben Verfasser stammt. R-15.6 sagt das selbst richtig.
- Mein Nachbau ist die erste Rechnung eines zweiten Lesers für die neue Fassung. Er trifft alle zehn Ankaufswerte der Gegenrechnung und die Testfallwerte.

Belastbar, weil von mir unabhängig getroffen:
- RF-05, RF-06 und RF-07 im Testfall, in beiden Rastern;
- RF-08 (Anschlussregeln, Raten);
- RF-09 (Tabelle);
- RF-11 im Basis- und Stressfall, mit tragbarem Preis, P_EK, Deckungen, Anschlussregeln und Zielwertsuche;
- die Vorfälligkeitsfälle aus RF-14 und RF-19, der Bankfall aus RF-19, die Nichtmonotonie aus RF-20;
- die Bausteine des Neubaus aus RF-12;
- die Steuerbeispiele aus R-7.8 und R-7.16.

Nur so belastbar wie der Referenzrechner:
- RF-12 als ganzer Plan: frei, mit KfW-Darlehen, gefördert über 38 Jahre;
- RF-13 (14 Steuerstatus);
- RF-17 im vollen Plan: drei Lesarten des Zuschusses, Personengesellschaft, Privatperson;
- RF-18, außer den Mietpfaden;
- der gebundene Bestand über die Bemessung hinaus.

Der gebundene Bestand ändert sich mit Befund 1 ohnehin.

## Was zur 9 fehlt

- **Im Dokument:** Befunde 1 bis 4, dazu 5 und 6, weil sonst die Toleranz „exakt“ an der Lesart hängt.
- **Im Referenzrechner:**
  - τ_k des übernommenen Darlehens (Befund 1);
  - Senkung der Miete im Formelweg (Befund 3);
  - Neubemessung im Stressfall (Befund 4);
  - Festschreibung mit Differenzbericht.
- **Von außen:**
  - die Blindrechnung von RF-12, RF-13 und RF-17 durch einen zweiten Bearbeiter, wie in R-15.6 geplant;
  - der Tilgungsplan einer Bank gegen R-5.3;
  - die Antwort der Hausbank zur kalkulatorischen Tilgung übernommener Darlehen (Kapitel 16, Frage 3).

## Nicht geprüft

- **RF-12, RF-13 und RF-17 als ganze Finanzpläne:** nur Bausteine gerechnet. Grund: Zeit. Vorrang hatten der verlangte Ankaufsfall und die neu gefassten Regeln.
- **RF-11 im Jahresmodus** (2.514.395,05 Euro): Mein Nachbau rechnet nur im Monatsraster.
- **Gesamtkapitalrendite und Amortisation im neuen Stand** (R-10.11, R-10.12), R-11.15 (Ergebnis ohne Bankdarlehen) und R-11.11 (Vergleich): nicht nachgerechnet.
- **Meldungen und Eingabeprüfung:** nur dort ausgelöst, wo mein Nachbau sie berührt.
- **Rechtsinhalte:** Kürzung samt Hinzurechnung (NF-47), Zuschuss (`MA-031`) und Kündigungsrecht (`BGB-489`) gehören zum Steuerberater und zum Juristen. Gerechnet habe ich sie so, wie sie geschrieben sind. Keine Quelle am Original gelesen.
