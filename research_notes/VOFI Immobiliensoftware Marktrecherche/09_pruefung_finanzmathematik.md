# Prüfbericht Finanzmathematik zu `03_vofi_methodik_steuern_risiko.md` (Stand 17.11.2026)

```
Rolle: Prüfer Finanzmathematiker
Prüfobjekt: research_notes/VOFI Immobiliensoftware Marktrecherche/03_vofi_methodik_steuern_risiko.md
            (rechnerische Teile der Abschnitte 1, 2, 3, 4, 7; aus 5 und 6 nur Formeln und Kontrollsummen)
Gesamturteil: Trägt mit Auflagen. Tabellenaufbau und Rechenreihenfolge sind ohne Zirkelbezug umsetzbar, und
der Testfall S1 stimmt in allen ausgewiesenen Zahlen auf den Cent. Als Grundlage der Rechenkern-Spezifikation
fehlen aber die Behandlung von Entnahmen (führt zu falschen Kennzahlen), mehrere Periodenkonventionen und
die genauen Gültigkeitsbedingungen der Kapitalwert-Probe; der Monte-Carlo-Teil ist an vier Stellen zu pauschal.
```

Alle Gegenrechnungen: eigene Python-Skripte (exakte Bruchrechnung), außerhalb des Repos unter
`/tmp/claude-0/-home-user-Claude-Code/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/pruefung-finmath/`
(`s1_gegenrechnung.py`, `zusatzrechnungen.py`, `tabelle_md.py`). Zeilenangaben „Z.“ beziehen sich auf das Prüfobjekt.

## Befunde

**1. [kritisch · belegt] Abschnitt 1 Zeile B1 (Z. 58) gegen Formelsatz Abschnitt 2 (Z. 139–142) – Entnahmen sind in der Tabelle vorgesehen, in den Kennzahlen aber nicht.**
Die Tabelle erlaubt „− Entnahme (Ausschüttung)“, die Formeln EW^O = EK·Π(1 + h(1−s)), ΔEW = EW^I − EW^O und r_EK = (EW^I/EK₀)^(1/n) − 1 kennen nur Einlagen. Jede laufende Ausschüttung senkt dann EW^I, aber nicht EW^O; die Investition wird systematisch zu schlecht ausgewiesen.
Beleg: S1 mit 5.000 Entnahme in t = 1…5 → EW^I = 558.656,41. Nach den Formeln der Notiz: ΔEW = 129.861,36 und r_EK = 6,91 %. Richtig (Opportunität mit denselben Entnahmen): ΔEW = 155.571,23, also unverändert zu S1; r_EK mit zum Opportunitätssatz aufgezinsten Entnahmen 7,876 %, als interner Zins der EK-Reihe 8,01 %. Fehler: 25.709,87 beim ΔEW, rund ein Prozentpunkt bei der Rendite.
Vorschlag: Festlegen, dass der Opportunitäts-VOFI dieselbe Einlagen- und Entnahmenreihe erhält wie die Investition. Für die Rendite eine der beiden Lesarten verbindlich wählen und benennen: (a) Entnahmen zum Opportunitätssatz nach Steuern auf t = n aufzinsen und zum Endwert addieren, dann Wurzelformel; (b) r als Lösung von Σ EK_t·(1+r)^(n−t) = EW^I + Σ Entnahme_t·(1+r)^(n−t). Einen Testfall mit Entnahmen aufnehmen.

**2. [wichtig · belegt] Abschnitt 1, Rechenreihenfolge Schritte 4–7 (Z. 81–84) und Kontrollsummen Abschnitt 6 (Z. 327) – Kontokorrentzins fehlt in Steuer und Saldo; zwei Kontrollsummen stimmen so nicht.**
(a) Schritt 3 berechnet den KK-Zins, Schritt 4 (BMG) und Schritt 5 (vorläufiger Saldo) führen aber nur „Sollzinsen“, die in Schritt 2 als Kreditzinsen je Kredit k definiert sind. Wörtlich umgesetzt wird der KK-Zins weder gezahlt noch abgezogen. Beleg: S1 mit nur 380.000 EK (20.000 Kontokorrent in t = 0, 8 %): EW = 561.526,16 mit gebuchtem KK-Zins (1.600,00 / 875,20 / 61,65), EW = 563.365,88 bei wörtlicher Lesart – Abweichung 1.839,71.
(b) Schritt 7 löst die Kredite in t = n erst nach dem Ausgleich (Schritt 6) ab; die Ablösung ist aber eine Zahlung der Periode n und muss vor dem Ausgleich in den Saldo, sonst ist ein zweiter Ausgleich nötig. S1 rechnet es richtig (Ablösung 624.171,48 im Saldo von t = 5).
(c) „Σ Tilgungen = Kreditbetrag“ gilt nur ohne Disagio, ohne Tilgungszuschuss, ohne kapitalisierte Zinsen und nur inklusive Ablösung (S1: 75.828,52 laufend + 624.171,48 Ablösung = 700.000). Im Bauzeit-Beispiel aus Befund 8 ist Endschuld 7.161.427,58 bei 6.930.816,75 Auszahlung.
(d) „Bilanzidentität Bestandssaldo“ ist nicht definiert. In S1 geprüft und in jeder Periode erfüllt: Bestandssaldo_t − Bestandssaldo_(t−1) = Z_t + EK_t − Sollzinsen_t (inkl. KK) + Habenzinsen_t − Steuer_t.
Sonst ist die Reihenfolge widerspruchsfrei: Zinsen und Steuern hängen nur von Vorperiodenbeständen ab, mit Geldanlage und unbegrenztem Kontokorrent wird der Finanzierungssaldo immer null; eine dafür nötige Zeile fehlt nicht. Offen ist nur der Fall einer begrenzten Kontokorrentlinie (dann braucht es eine Zeile „Liquiditätslücke/EK-Nachschuss“).
Vorschlag: Schritte 4 und 5 um „− KK-Zins_t“ ergänzen; Ablösung vor den Ausgleich ziehen; Kontrollsumme (c) als „Auszahlungen + kapitalisierte Zinsen − Tilgungen − Zuschüsse − Ablösung = Restschuld“ fassen; (d) wie oben ausschreiben.

**3. [wichtig · belegt] Abschnitt 2 (Z. 144), Abschnitt 6 (Z. 327), zitiert auch Z. 131 – Beziehung ΔEW = KW·(1+i)^n: richtig, aber die Bedingungen sind unvollständig; als „automatischer Konsistenztest“ so nicht verwendbar.**
Nachgerechnet gilt sie exakt (Abweichung 0,0000), wenn zugleich: alle Zinssätze gleich sind (jeder Kredit, Kontokorrent, Geldanlage und Opportunität), kein Disagio/keine Gebühren, Steuer in der Periode der Entstehung gezahlt, sofortiger Verlustausgleich, ein einziger Steuersatz für Überschüsse und Zinsen, und der Kapitalwert auf die originäre Zahlungsfolge nach Steuern **ohne Zinsen** gerechnet wird: KW = Σ [Z_t − s·(steuerpfl. Überschuss_t − AfA_t)] / (1 + i(1−s))^t. Beleg (S1 mit allen Zinsen 4 %, s = 30 %): ΔEW/1,028^5 = 110.371,99 = KW; ohne Steuern 99.662,84 = KW.
Sie gilt nicht bei: unterschiedlichen Zinssätzen (Original-S1: 145.124,09 gegen 190.202,20, Abweichung −45.078,11); Verlustvortrag statt Sofortausgleich (Anlaufverlust-Variante: −973,20); abweichendem Steuersatz auf Zinsen (26,375 % statt 30 %: +144,00); zeitversetzter Steuerzahlung, Zinsschranke oder nur teilweise abziehbaren Zinsen; Monatsverzinsung mit Jahressteuer; Entnahmen ohne Spiegelung in der Opportunität (Befund 1). Zwei naheliegende Fehler: Vorsteuer-Zahlungen mit i(1−s) abzinsen (165.065,96 statt 110.371,99) und den Endwert statt der Endwertdifferenz abzinsen (510.371,99; das stimmt nur bei EK = 0 wie in L3).
Vorschlag: Die Probe als eigenen Testmodus mit genau dieser Bedingungsliste beschreiben und die KW-Formel dazuschreiben. Zusatzprobe aufnehmen: Unter diesen Bedingungen ist ΔEW unabhängig von der EK-Quote.

**4. [wichtig · belegt] Abschnitt 3 Kennzahlenkatalog (Z. 191, 193), Abschnitt 2 (Z. 147), Abschnitt 7 (Z. 381) – DSCR im Exit-Jahr, LTV und Amortisationsdauer sind mit den beschriebenen Eingaben nicht eindeutig bzw. nicht berechenbar.**
(a) DSCR = NOI/(Zins + Tilgung), „periodisch, Minimum“: Zählt die Ablösung in t = n als Tilgung, fällt der DSCR in S1 von 1,4175 auf 0,0894. Das Minimum und damit P(DSCR_min < Covenant) wären in jedem Lauf verletzt. Laufende Werte S1: 1,3095 / 1,3357 / 1,3624 / 1,3897 / 1,4175.
(b) LTV „laufend“ und die Amortisationsdauer („bei fiktiver Veräußerung in t“) brauchen einen Wert- bzw. Netto-Liquidationserlös je Periode. Den gibt es weder in der Zeilenstruktur noch in S1 (nur Verkauf in t = 5).
(c) Die Amortisationsdauer wird mit „bzw.“ in zwei Lesarten angeboten, die verschiedene Ergebnisse liefern. Beleg (Annahme des Prüfers: Netto-Liquidationserlös linear von 1,00 auf 1,15 Mio.): Bestandssaldo inkl. Liquidation in t = 2: 409.664,52 – deckt das EK (400.000), aber nicht den Opportunitätsendwert (411.278,40). Lesart „EK gedeckt“ → 2 Jahre, Lesart „Opportunität erreicht“ → 3 Jahre.
Vorschlag: Sondertilgungen/Ablösung bei Exit und Umschuldung aus dem DSCR-Nenner ausnehmen; einen Wertpfad (Marktwert, Verkaufskosten, ggf. Vorfälligkeit und Steuer je Periode) als eigene Nebenrechnung festlegen; eine Amortisations-Lesart als Standard wählen (die Grob-Definition ist ungeprüft, siehe „Nicht geprüft“).

**5. [wichtig · belegt] Abschnitt 4 (Z. 211, 223, 227, 228) gegen S1 (Z. 94) – Periodenzuordnung an vier Stellen nicht eindeutig.**
(a) Indexstart: Miete_t = Miete₀·Π(1+g_τ) lässt offen, ob der Eingabewert die Miete des ersten Jahres ist. S1 rechnet Jahr 1 = 55.000 und Jahr t = 55.000·1,02^(t−1). Liest man 55.000 als Miete₀ (Jahr 1 = 56.100): EW = 588.484,91 statt 584.366,28 (+4.118,62), r_EK 8,03 % statt 7,88 %.
(b) Jahres- gegen Monatsraster: Die Notiz empfiehlt den Monatskern, S1 ist ein Jahresfall. S1 im Monatsraster (Annahmen des Prüfers: Miete/12 nachschüssig, Rate 3.500, Zins i/12, Habenzins h/12, Steuer am Jahresende): EW = 585.937,57 (+1.571,29), Ablösung 622.651,19 statt 624.171,48. Der Satz in Z. 223 („sonst entstehen Abweichungen zur Lehrbuch-Jahresrechnung“) ist missverständlich: Die Abweichung entsteht durch das Monatsraster selbst, nicht durch die Art der Aggregation.
(c) Vorschüssige Miete und Steuerzeitpunkt: Wie eine vorschüssige Zahlung auf einen Zeitpunkt gelegt wird (Monatsanfang = Ende des Vormonats) und in welchem Monat die Jahressteuer fließt, steht nicht da. Wirkung in S1: vorschüssig +346,47 gegenüber nachschüssig; Steuer monatlich statt am Jahresende rund −134.
(d) Opportunität: Die Formel verzinst jährlich. Rechnet der Kern die Geldanlage monatlich mit h/12 (effektiv 2,0184 %), muss die Opportunität gleich rechnen: 429.067,98 statt 428.795,05 (273 Differenz, die sonst im ΔEW landet).
Dazu: Die Kontrollsumme „Summe Monatswerte = Jahreswert“ (Z. 327) gilt nur für Stromgrößen; Bestände sind der Dezemberstand. Bei Schwellenwert-Klauseln fehlt der Zustand „Indexstand bei letzter Anpassung“.
Vorschlag: Je Zahlungsart festlegen: Basisperiode der Indexierung, Zeitpunkt (Periodenanfang/-ende), Zahlungsmonat der Steuer, Verzinsungstakt – und denselben Takt für Investition und Opportunität. n in den Renditeformeln als Monate/12 definieren.

**6. [wichtig · belegt] Abschnitt 1, Testfall S1 (Z. 93–105), L1–L4 (Z. 35–39, 107) und Abschnitt 6 (Z. 330) – S1 stimmt vollständig; als Regressionstest fehlen vier Angaben, und L1–L4 taugen nicht als Golden-Master-Tests.**
S1: Alle Tabellenwerte (t = 0…5, einschließlich Ablösung) und alle Ergebniszahlen bestätigt (EW 584.366,28; EW^O 428.795,05; ΔEW 155.571,23; r_EK 7,876 %; Opportunität 1,40 %). Finanzierungssaldo in jeder Periode null, Kontokorrent nie beansprucht. Vollständige Tabelle im Anhang.
Für den eindeutigen Nachbau fehlen: (1) Rundungsregel – die Tabelle ist mit voller Genauigkeit gerechnet und nur in der Anzeige gerundet (Reinertrag Jahr 5 = 59.533,7688). Bei Cent-Rundung jeder Zahlung weichen drei Zwischenwerte um einen Cent ab (Guthaben t = 4: 45.263,83 statt 45.263,84; Geldanlage t = 4 und t = 5); der Endwert bleibt gleich. (2) Jahresmodus als ausdrückliche Annahme für alle Zahlungen, nicht nur für das Darlehen (siehe Befund 5b). (3) Opportunitätszins = Habenzins 2 % und Steuersatz 30 % auf Opportunitätszinsen stehen nur in der Ergebniszeile, nicht in den Annahmen. (4) Keine Vorfälligkeitsentschädigung bei Ablösung; „sofortige Verrechnung“ meint Zahlung der Steuer in derselben Periode (in S1 gibt es keinen Verlust, an dem man es sonst ablesen könnte).
S1 prüft nicht: Kontokorrent, negative BMG/Erstattung, Verlustvortrag, Raten- und Endtilgung, steuerpflichtigen Veräußerungsgewinn, Disagio, gestaffelte Einlagen, Entnahmen, Monatsraster.
L1–L4: Die Eckwerte sind in sich stimmig – L1: 5.000·1,025^5 = 5.657,04; 10.079 − 5.657 = 4.422; r_EK = 15,05 %. L2: (2.852,08/2.100)^(1/4) − 1 = 7,953 %; nur n = 4 passt (n = 3: 10,74 %, n = 5: 6,31 %). L3: Zins 1.000 = 10 % von 10.000; wegen EK = 0 ist keine EK-Rendite definiert. L4: 1,5 % < 2 % → unvorteilhaft, folgerichtig. Ob 10.079 und 2.100 selbst stimmen, ist ohne Zahlungsreihen nicht prüfbar. Damit lassen sich aus L1–L4 nur drei Formelproben bauen (EW^O, ΔEW, Wurzelformel), keine Tabellenprüfung – anders als Z. 330 es vorsieht.
Vorschlag: Die vier Angaben in S1 ergänzen; S2–S5 für die nicht abgedeckten Fälle bauen (Vorschläge: Kontokorrent-Variante mit 380.000 EK, Anlaufverlust, Entnahmen, Einheitszins-Fall für die KW-Probe – Werte dazu liegen in den Skripten vor); L1–L4 erst nach Beschaffung der Originaltabellen als Tests führen.

**7. [wichtig · belegt] Abschnitt 1 Kreditformeln (Z. 89), Abschnitt 2 (Z. 142, 143), Abschnitt 3 (Z. 184) – Randfälle und eine nicht eindeutige Kennzahl.**
(a) r_EK = (EW/EK₀)^(1/n) − 1 ist für EW ≤ 0 und für EK₀ = 0 nicht definiert. EW < 0 tritt bei hohem Fremdkapitalanteil in schlechten Simulationsläufen auf; Mittelwert und Konvergenzkriterium von E[r_EK] (Z. 380) wären dann nicht berechenbar. EK₀ = 0 ist genau der Literaturfall L3.
(b) Annuitätenformel A = K₀·i·(1+i)^N/((1+i)^N − 1): bei i = 0 Division durch null (richtig: K₀/N = 35.000 bei 700.000/20 Jahre); bei sehr kleinen Sätzen numerisch instabil (i = 10⁻¹²: 34.996,89; i = 10⁻¹⁵: 31.525,20). Relevant für zinslose oder zinsverbilligte Förderdarlehen (ob konkrete Programme 0 % haben, ist hier ungeprüft).
(c) Interner Zins: „Mehrdeutigkeit abfangen“ ohne Regel. Bei Entnahmen/Nachschüssen und im Monatsraster der Projektentwicklung sind mehrere Vorzeichenwechsel der Normalfall.
(d) VOFI-Gesamtkapitalrentabilität: Die verbale Rekonstruktion lässt offen, womit die Fremdkapitalbeträge auf t = n bezogen werden. Drei Lesarten für S1: 4,61 % (unverzinst addiert), 4,69 % (mit Habenzins nach Steuern aufgezinst), 4,76 % (Fremdkapital mit Sollzins nach Steuern aufgezinst). Die Notiz weist die Unsicherheit selbst aus; die Kennzahl ist bis zur Klärung nicht testbar.
Vorschlag: (a) r_EK = −100 % bei EW ≤ 0, „nicht definiert“ bei EK₀ = 0, in der Simulation Quantile statt Mittelwert der Rendite und ΔEW als Hauptgröße; (b) Sonderfall i = 0 und stabile Auswertung für kleine i; (c) Vorzeichenwechsel zählen, bei mehr als einem alle Nullstellen im Suchbereich melden und auf die VOFI-Rendite verweisen; (d) Probe für jede GK-Definition: bei 100 % EK muss r_GK = r_EK gelten.

**8. [wichtig · belegt] Abschnitt 4 (Z. 224–226) – Bauzeitzinsen: Die sequentielle Monatsfortschreibung beseitigt nicht jede Zirkularität; Faustformel und logistische Kurve sind ungenau angegeben.**
(a) Die Fortschreibung „Zinsen auf Vorperiodenstand“ löst Zins auf Zins. Sobald aber EK oder Kreditlinie als Quote der Gesamtkosten **einschließlich** Bauzeitzinsen festgelegt sind (LTC, „Equity first“), bleibt ein Fixpunkt: Gesamtkosten → EK → Zeitpunkt der Kreditabrufe → Zinsen → Gesamtkosten. Beleg (10 Mio. Kosten linear über 24 Monate, 5 %, EK 30 % zuerst): ein Durchlauf mit EK = 3,0 Mio. ergibt Zinsen 235.370 und LTC 70,69 %; der Fixpunkt liegt bei EK 3.069.183,25, Zinsen 230.610,83, LTC 70,00 % (6 Iterationen).
(b) Faustformel „Kosten·i·Bauzeit·0,5“: passt nur bei voller Kreditfinanzierung von Beginn an (exakt 494.134 linear, 492.407 kubische S-Kurve gegen 500.000). Bei „Equity first“ sind es 230.611 – weniger als die Hälfte; auch auf den Kreditanteil bezogen (350.000) liegt sie 50 % zu hoch.
(c) Logistische S-Kurve: Die angegebene Funktion erfüllt F(0) = 0, F(1) = 1 nicht (k = 10, τ₀ = 0,5: F(0) = 0,0067, F(1) = 0,9933 → nur 98,66 % der Kosten verteilt). Die Normierung wird erwähnt, aber nicht angegeben. Die kubische Form 3τ² − 2τ³ und die Beta-Verteilungsfunktion sind in Ordnung.
Vorschlag: Festlegen, welche Größe Eingabe ist (EK-Betrag oder Quote) und bei Quote eine Fixpunkt-Iteration mit Abbruchschranke vorsehen; Faustformel auf „kreditfinanzierte Kosten × mittlere Inanspruchnahme“ umformulieren; Normierung (F(τ) − F(0))/(F(1) − F(0)) ausschreiben.

**9. [wichtig · belegt] Abschnitt 7, Tabelle der Inputs und Korrelationen (Z. 369–379) – Verteilungen und Zeitstruktur an drei Stellen zu pauschal.**
(a) „Normal“ für die Exit-Rendite: Der Verkaufspreis hängt von 1/Rendite ab; für eine unbeschränkte Normalverteilung existiert dessen Erwartungswert nicht. Beleg: μ = 4,5 %, σ = 1,5 %: in 200.000 Ziehungen 272 negative Renditen, größter Faktor 93.293; der mittlere Faktor schwankt über 20 Seeds mit je 10.000 Läufen zwischen 18,0 und 29,4 (deterministisch 22,2). Schon bei σ = 1,0 % liegt der Mittelwert mit 23,4–23,7 rund 6 % über dem Basisfall.
(b) Simulationsmittel ≠ Basisfall: Bei schiefen Verteilungen und der Kehrwert-Beziehung weicht der Mittelwert systematisch vom deterministischen Fall ab (PERT 3,5/4,5/6,5 %: mittlerer Faktor 21,73 gegen 22,22 am Modus). Das gehört in die Spezifikation, sonst wird es als Rechenfehler gemeldet.
(c) „Normal oder PERT p. a.“ für Mietwachstum und Inflation ohne Aussage zur Abhängigkeit über die Jahre: Unabhängige Jahresziehungen mitteln sich weg. Beleg (g ~ N(2 %; 1,5 %), 10 Jahre): Streuung des Mietniveaus 5,7 % bei unabhängigen Ziehungen, 11,6 % bei AR(1) mit 0,7, 18,2 % bei einer Ziehung für alle Jahre. Das Risiko wird je nach Wahl um den Faktor drei unterschiedlich ausgewiesen; die Notiz nennt AR(1) nur als Alternative.
(d) Korrelationen: Nicht gesagt wird, welches Maß der Nutzer eingibt. Bei der Gauß-Copula ist der Parameter die Korrelation der Normalvariablen, nicht die Rangkorrelation (für Spearman 0,5 braucht es 0,5176) und nicht die lineare Korrelation der Randverteilungen (zwei Lognormal-Größen mit σ = 1: 0,38 statt 0,5; bei −0,5 nur −0,23). Cholesky braucht eine positiv definite Matrix; bei nur semidefiniter Matrix scheitert die Standardzerlegung. Gesucht ist die nächstgelegene Korrelationsmatrix (Einheitsdiagonale), und die Korrektur muss dem Nutzer angezeigt werden. Eine statische Matrix reicht nicht für Zeitreihen (Zinsprozess gegen Jahresgrößen): korreliert werden müssen die Störgrößen je Periode.
Vorschlag: Exit-Rendite und andere Nenner-Größen nur beschränkt (PERT, gestutzt, Lognormal); Standard für Wachstumsgrößen AR(1) mit einstellbarer Persistenz; Rangkorrelation als Eingabemaß mit Umrechnung; im Bericht Basisfall, Mittelwert und Median nebeneinander ausweisen. Die übrigen Angaben (Dreieck/PERT-Formeln, Vasicek/CIR, Vorzeichen der Korrelationen) sind rechnerisch in Ordnung; PERT-Erwartungswert per Simulation bestätigt (4,665 % gegen Formel 4,667 %).

**10. [wichtig · belegt für a und b, begründete Einschätzung für c und d] Abschnitt 7, Sampling und Konvergenz (Z. 380), Abschnitt 6 (Z. 328) – Laufzahlen widersprechen dem eigenen Kriterium; Fehlerformel passt nicht zu LHS/Sobol; „fester Seed“ reicht nicht.**
(a) „Für Mittelwerte reichen oft 1.000–5.000“ gegen „Halbbreite des 95-%-Intervalls für E[r_EK] < 5 Basispunkte“: nötig sind N ≥ (1,96·σ/0,0005)², also 6.147 Läufe bei σ(r_EK) = 2 Prozentpunkten, 13.830 bei 3, 38.416 bei 5. Mit 1.000 Läufen und σ = 3 Punkten beträgt die Halbbreite 18,6 Basispunkte. Die Angabe „≥ 10.000 für das 5-%-Quantil“ ist dagegen haltbar (Standardfehler 0,021·σ).
(b) σ/√N gilt nur für einfache Zufallsstichproben. Bei LHS überschätzt die Formel den Fehler stark (Testfunktion mit 5 Inputs, N = 1.000: Formel 4,8 Basispunkte, beobachtet 0,5), bei Sobol ist sie nicht anwendbar. Ein darauf gestütztes Abbruchkriterium rechnet ein Vielfaches zu lange.
(c) Sobol-Folgen dürfen nicht in aufeinanderfolgende „Batches“ zerlegt werden (Stabilitätsprüfung über Batches), und das Umsortieren nach Iman-Conover zerstört ihre Gleichverteilung im Verbund. Mit Bernoulli-Ereignissen je Mietvertrag und Jahr wächst die Dimension stark, der Vorteil von Sobol schwindet.
(d) Reproduzierbarkeit: Derselbe Seed liefert nur dann dieselben Zahlen, wenn auch Zufallsgenerator samt Version, Reihenfolge der Ziehungen und Aufteilung auf parallele Stränge feststehen. Der Rechenkern soll auf dem Server und als WebAssembly im Browser laufen; Potenz-, Exponential- und Logarithmusfunktionen können sich dort in den letzten Stellen unterscheiden.
Vorschlag: Fehler über unabhängige Wiederholungen schätzen (z. B. 20 unabhängig gemischte LHS- oder Sobol-Sätze, Streuung der Satzmittel); LHS mit Iman-Conover oder Sobol mit Copula kombinieren, nicht über Kreuz; Zufallszahlen je Lauf aus (Seed, Laufnummer) ableiten, Generator und Version im Ergebnis speichern; für Server und Browser dieselbe Implementierung der mathematischen Funktionen verwenden und Gleichheit an S1 und einem Simulationslauf testen.

## Nicht geprüft

- Steuerrecht, Gesetzeszitate, Sätze und Fristen (Abschnitt 5) – anderer Prüfer. Rechnerisch aufgefallen ist nur: Der Formelsatz verwendet einen einzigen Satz s für Mietüberschüsse, Habenzinsen und Opportunität; ob das je Investorentyp zutrifft, ist Steuerfrage. Rechnerisch muss der Zinssteuersatz getrennt einstellbar sein (Wirkung siehe Befund 3).
- Originalformeln und -tabellen von Grob, Schulte/Ropeter, Gabler (VOFI-Gesamtkapitalrentabilität, Amortisationsdauer, Zahlungsreihen zu L1–L4): kein Zugriff; ob die Rekonstruktionen dem Lehrbuch entsprechen, ist ungeprüft.
- Die zitierten Quellenaussagen in Abschnitt 7 (z. B. Konvergenzrate Iman-Conover, 55 % breitere Bandbreite der Dreiecksverteilung, 42 % LHS-Anteil) und alle Marktdefinitionen in Abschnitt 3 (gif, INREV) wurden nicht an den Quellen geprüft.
- Kalibrierung: Ob die in den Gegenrechnungen angenommenen Streuungen (σ der Rendite, der Exit-Rendite, des Mietwachstums) marktgerecht sind, ist nicht geprüft; sie dienen nur als Rechenbeispiel.
- Abweichungen zwischen Server- und Browser-Rechnung (Befund 10d) konnten mangels Code nicht gemessen werden.

---

## Anhang: Gegenrechnung Testfall S1 (bestätigt, als automatischer Test verwendbar)

**Eingaben.** Jahresraster, alle Zahlungen am Periodenende, n = 5. Kaufpreis 1.000.000 + Erwerbsnebenkosten 100.000 in t = 0. Eigenkapital 400.000 in t = 0, keine Entnahmen. Annuitätendarlehen 700.000, Zins 4 % auf die Restschuld des Vorjahres, Anfangstilgung 2 %, Annuität 42.000 jährlich nachschüssig, kein Disagio, Ablösung der Restschuld in t = 5 nach der regulären Rate, keine Vorfälligkeitsentschädigung. Reinertrag (voll steuerpflichtig, zahlungsgleich) Jahr 1: 55.000, Jahr t: 55.000·1,02^(t−1). AfA 2 % × 80 % × 1.100.000 = 17.600 je Jahr (t = 1…5). Steuersatz 30 % auf BMG = Reinertrag − AfA − Sollzins − KK-Zins + Habenzins; Steuer wird in derselben Periode gezahlt, negative BMG würde sofort erstattet (kommt nicht vor). Geldanlage 2 % auf das Guthaben des Vorjahres, Kontokorrent 8 % auf den Stand des Vorjahres. Verkauf in t = 5 zu 1.150.000 netto, Veräußerungsgewinn steuerfrei. Opportunität: 400.000 zu 2 % mit 30 % Steuer, jährlich.

**Rundung.** Gerechnet mit voller Genauigkeit, gerundet nur für die Anzeige (kaufmännisch auf Cent). Vorzeichen: + Zufluss, − Abfluss; Bestände ohne Vorzeichenumkehr; Bestandssaldo = Guthaben − Kontokorrent − Restschuld.

| t | Originäre Zahlung | davon Reinertrag (steuerpfl.) | Eigenkapital | Kreditaufnahme | Sollzins | Tilgung | Ablösung | Habenzins | AfA | steuerl. BMG | Steuer | Geldanlage (− Anlage) | Finanzierungssaldo | Guthaben | Kontokorrent | Restschuld | Bestandssaldo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | -1.100.000,00 | 0,00 | 400.000,00 | 700.000,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 700.000,00 | -700.000,00 |
| 1 | 55.000,00 | 55.000,00 | 0,00 | 0,00 | -28.000,00 | -14.000,00 | 0,00 | 0,00 | 17.600,00 | 9.400,00 | -2.820,00 | -10.180,00 | 0,00 | 10.180,00 | 0,00 | 686.000,00 | -675.820,00 |
| 2 | 56.100,00 | 56.100,00 | 0,00 | 0,00 | -27.440,00 | -14.560,00 | 0,00 | 203,60 | 17.600,00 | 11.263,60 | -3.379,08 | -10.924,52 | 0,00 | 21.104,52 | 0,00 | 671.440,00 | -650.335,48 |
| 3 | 57.222,00 | 57.222,00 | 0,00 | 0,00 | -26.857,60 | -15.142,40 | 0,00 | 422,09 | 17.600,00 | 13.186,49 | -3.955,95 | -11.688,14 | 0,00 | 32.792,66 | 0,00 | 656.297,60 | -623.504,94 |
| 4 | 58.366,44 | 58.366,44 | 0,00 | 0,00 | -26.251,90 | -15.748,10 | 0,00 | 655,85 | 17.600,00 | 15.170,39 | -4.551,12 | -12.471,18 | 0,00 | 45.263,84 | 0,00 | 640.549,50 | -595.285,66 |
| 5 | 1.209.533,77 | 59.533,77 | 0,00 | 0,00 | -25.621,98 | -16.378,02 | -624.171,48 | 905,28 | 17.600,00 | 17.217,07 | -5.165,12 | -539.102,44 | 0,00 | 584.366,28 | 0,00 | 0,00 | 584.366,28 |

Zeilenprobe: Originäre Zahlung + Eigenkapital + Kreditaufnahme + Sollzins + Tilgung + Ablösung + Habenzins + Steuer + Geldanlage = Finanzierungssaldo = 0 (AfA und BMG sind keine Zahlungen).

**Ungerundete Werte (vier Nachkommastellen) für Tests mit enger Toleranz**

| t | Reinertrag | Sollzins | Tilgung | Ablösung | Habenzins | BMG | Steuer | Guthaben | Restschuld | Bestandssaldo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 55.000,0000 | 28.000,0000 | 14.000,0000 | 0,0000 | 0,0000 | 9.400,0000 | 2.820,0000 | 10.180,0000 | 686.000,0000 | -675.820,0000 |
| 2 | 56.100,0000 | 27.440,0000 | 14.560,0000 | 0,0000 | 203,6000 | 11.263,6000 | 3.379,0800 | 21.104,5200 | 671.440,0000 | -650.335,4800 |
| 3 | 57.222,0000 | 26.857,6000 | 15.142,4000 | 0,0000 | 422,0904 | 13.186,4904 | 3.955,9471 | 32.792,6633 | 656.297,6000 | -623.504,9367 |
| 4 | 58.366,4400 | 26.251,9040 | 15.748,0960 | 0,0000 | 655,8533 | 15.170,3893 | 4.551,1168 | 45.263,8398 | 640.549,5040 | -595.285,6642 |
| 5 | 59.533,7688 | 25.621,9802 | 16.378,0198 | 624.171,4842 | 905,2768 | 17.217,0654 | 5.165,1196 | 584.366,2816 | 0,0000 | 584.366,2816 |

**Kennzahlen und Summen**

| Größe | Wert |
|---|---|
| Endwert EW^I (Bestandssaldo t = 5) | 584.366,28 (ungerundet 584.366,2816) |
| Endwert der Opportunität 400.000 · 1,014^5 | 428.795,05 (ungerundet 428.795,0530) |
| Endwertdifferenz ΔEW | 155.571,23 (ungerundet 155.571,2285) |
| VOFI-Eigenkapitalrentabilität | 7,8760 % |
| Rendite der Opportunität | 1,4000 % |
| Endwert je Euro Eigenkapital (EW/EK) | 1,4609 |
| Σ Sollzinsen / Σ laufende Tilgung / Ablösung | 134.171,48 / 75.828,52 / 624.171,48 |
| Σ Steuern / Σ Habenzinsen | 19.871,26 / 2.186,82 |
| DSCR t = 1…5 (Reinertrag / Annuität 42.000, ohne Ablösung) | 1,3095 / 1,3357 / 1,3624 / 1,3897 / 1,4175 |
| ICR t = 1…5 (Reinertrag / Sollzins) | 1,9643 / 2,0445 / 2,1306 / 2,2233 / 2,3235 |
| Interner Zins der originären Zahlungsfolge vor Steuern | 5,9984 % |
| Interner Zins der EK-Reihe bei Vollausschüttung statt Wiederanlage (−400.000; 10.180,00; 10.782,00; 11.392,68; 12.012,08; 538.468,75) | 8,1702 % |

**Abweichungen bei Cent-Rundung jeder einzelnen Zahlung** (falls der Rechenkern so rundet): Geldanlage t = 4: −12.471,17; Guthaben t = 4: 45.263,83; Bestandssaldo t = 4: −595.285,67; Geldanlage t = 5: −539.102,45. Alle übrigen Werte und der Endwert 584.366,28 sind gleich.

**Zusatzwerte aus den Befunden (Varianten von S1, nur die geänderte Annahme genannt)**

| Variante | Endwert | Bemerkung |
|---|---|---|
| Entnahme 5.000 in t = 1…5 | 558.656,41 | ΔEW richtig 155.571,23 (Opportunität mit gleichen Entnahmen) |
| Eigenkapital 380.000 (Kontokorrent 20.000 in t = 0) | 561.526,16 | KK-Stände 20.000,00 / 10.940,00 / 770,64 / 0; KK-Zinsen 1.600,00 / 875,20 / 61,65 |
| Reinertrag Jahr 1 = 56.100 (Index ab t = 0) | 588.484,91 | r_EK 8,0277 % |
| Alle Zinssätze 4 %, Steuersatz 30 % | 585.939,00 | ΔEW/1,028^5 = Kapitalwert nach Steuern = 110.371,99 |
| Alle Zinssätze 4 %, ohne Steuern | 607.916,24 | ΔEW/1,04^5 = Kapitalwert = 99.662,84 |
