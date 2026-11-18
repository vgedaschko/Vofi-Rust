Rolle: Grenzfälle
Prüfobjekt: `docs/fachspezifikation-rechenkern.md` (Teil 1, Stand 2026-11-18, Entwurf zur Prüfrunde) und Referenzrechner unter `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner/` (Kopie unverändert gerechnet; `referenzfaelle.py` in der Kopie: 529 von 529 bestanden)
Gesamturteil: Trägt mit Auflagen. Der Kern ist für die Mehrzahl der Ränder sauber definiert und reproduzierbar (Zins null, Eigenkapital null, Haltedauer 1 und 42, Bindung gleich Haltedauer, Investitionsstau im Verkaufsjahr, Milliarden und Cent, Tranchenreihenfolge). An vier Stellen erzeugen realistische Eingaben aber einen Absturz oder ein stilles Falschergebnis. Das verletzt die feste Festlegung „Randfälle haben definierte Ergebnisse statt Fehlern“ (Spezifikation Kapitel 3) und R-14 („Der Kern bricht nie mit einem Rechenfehler ab“): leerstehendes Objekt, Leerstand im Verkaufspreis, Zins plus Tilgung null, Preissuche über unzulässige Bereiche. Zwei Proben können einen Fehler nicht finden, oder sie schlagen fälschlich an.
Note: 7 von 10. Zur 9 fehlt: Befunde 1 bis 4 und 6 im Dokument regeln (je eine Regel oder eine Eingabegrenze), Befund 7 im Referenzrechner beheben, und der Referenzrechner muss die Eingabeprüfung (M-20) und die übrigen Meldungen tragen. Erst dann belegt er Kapitel 14; heute rechnen sechs unzulässige Eingaben ohne Meldung weiter, zwei stürzen ab.

## Vorgehen

Gerechnet wurde mit einer unveränderten Kopie des Referenzrechners. Die eigenen Skripte liegen im Scratchpad unter `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs1-grenzfaelle/`:
- `grenzfaelle.py`: GF-01 bis GF-45 und die Reproduzierbarkeit;
- `zusatz.py`: GF-19b, GF-44 im Detail, die Leerstand-Gegenrechnung, P-04 und der interne Zinsfuß;
- `p07_suche.py` und `p07_fall.py`: der Fehlalarm von P-07;
- `out1.txt` und `out2.txt`: die Ausgaben der Läufe.

Basis ist der Ankauf aus RF-11 (`annahmen.ANKAUF`, ohne Investitionsstau, wo nicht anders genannt) mit `annahmen.VORGABEN`. Alle Werte sind Annahmen der Beispiele.

Spalte „Art“: **D** heißt Lücke im Dokument, **R** Abweichung des Referenzrechners vom Dokument, **R-bek.** die im Dokument genannte fehlende Eingabeprüfung oder Meldung des Referenzrechners, **ok** keine Beanstandung.

## Gerechnete Fälle

| Fall | Eingabe | erwartet nach Dokument | tatsächlich (Referenzrechner) | Art |
|---|---|---|---|---|
| GF-01 | Bankzins 0 %, Tilgung 2 % | R-14.1: Rate L x τ / p, rechnet | EW 2.732.055,55; r 8,041 %; L 1.560.000 nach (a); Proben bestanden | ok |
| GF-02 | Bankzins 0 %, Tilgung 0 % (E-45, H-04, E-64 zulassen beides) | definiertes Ergebnis | **Absturz** `DivisionByZero` in R-5.12 (b) | D + R → Befund 3 |
| GF-03 | Bankzins −0,5 % | M-20 (E-45: 0 bis 20) | rechnet still: r 8,262 % | R-bek. |
| GF-04 | Bankzins −2 % bei 2 % Tilgung | M-20 | **Absturz** `DivisionByZero` (i + τ = 0) | R-bek. / Befund 3 |
| GF-05 | Eigenkapital 0 (Quote 100 %, Nebenkosten 0, Deckung 1,0, Miete 20 €) | M-28, übrige Kennzahlen | r nicht definiert; EW = ΔEW 5.727.038,37; Proben bestanden | ok |
| GF-06 | Kaufpreis 0 | M-20 (E-10 > 0) | rechnet: EW 3.680.485,09, r nicht definiert | R-bek. |
| GF-07 | Ist- und Marktmiete 0 | M-20 (E-16 > 0) | rechnet: M-21, VK-Preis 0, EW 0,00, r −100 % | R-bek. |
| GF-08 | **Ist-Miete 0** (leerstehendes Objekt; E-15 ≥ 0 zulässig), Marktmiete 9,20, Anpassung 4 Jahre | Anpassung an die Marktmiete (R-6.3) | Miete bleibt in **allen 13 Jahren 0,00**; VK-Preis 0; EW 0,00; r −100 %; Proben bestanden | D → Befund 1 |
| GF-09 | Ist-Miete 0: tragbarer Preis | Preis oder M-32 | **M-31 „Suchbereich leer“** (Obergrenze 100 x Sollmiete Jahr 1 = 0) | D → Befund 1 |
| GF-10 | Leerstand 100 % (Mietausfall 1) | R-14.8: L = 0, M-21, Nachschüsse | wie beschrieben; aber **VK-Preis 3.326.730,48 wie voll vermietet**; r 0,592 % | D → Befund 2 |
| GF-11 | Ist-Miete über Marktmiete (11,00 gegen 9,20) | Pfad führt linear zurück | 11,00 / 10,596 / 10,286 / 10,072 / 9,958 / 10,158 | ok (B steigt mit Übermiete, Hinweis unten) |
| GF-12 | Pfad genau an der Kappungsgrenze (Ist 8,00, Markt 9,20, d = 3, ohne Steigerung) | min(Pfad; 8,00 x 1,15) gleichauf | 8,00 / 8,40 / 8,80 / 9,20 / 9,20 …, keine Mehrdeutigkeit | ok |
| GF-13 | Anpassungsdauer 0 | R-6.3 Satz 2: „Im Jahr 1 gilt die Ist-Miete“ | Jahr 1 = **9,20** (Marktmiete); RE_VJ 113.901,48 statt 103.035,24; L 1.560.000 statt 1.431.044,99 | D (Text gegen Formel) → Befund 8 |
| GF-14 | Beleihungsquote 0 % | L = 0, bindet (a) | L 0, bindet (a), Deckung „kein Kapitaldienst“; Proben bestanden | ok |
| GF-15 | Beleihungsquote 100 % | L = min(A, B, C) | L 1.431.044,99 nach (b) | ok |
| GF-16 | Mindestdeckung verfehlt schon das übernommene Darlehen (1,8 Mio., 3 %, 2 %) | L = 0, M-21 | L 0, M-21, bindet (a) und (b); Deckung 1,1448 | ok |
| GF-17 | übernommenes Darlehen 3,0 Mio. > Mittelbedarf | M-22 | M-22 | ok (E-59 nennt dieselbe Grenze als Eingabegrenze, also M-20; Kennung uneinheitlich) |
| GF-18 | übernommenes Darlehen = Mittelbedarf 2,64 Mio. | C = 0, EK 0, M-28 | so; EW = ΔEW 1.299.162,79 | ok |
| GF-19 | übernommenes Darlehen 2,0 Mio., Zielrendite 12 % | P* | 2.286.321 (Hebel bei kleinem EK) | ok |
| GF-19b | übernommenes Darlehen 2,0 Mio. zu 6 %, Verkaufsfaktor 4 | M-32 (Ziel bei keinem zulässigen Preis erreicht) | **Absturz** mit Meldung M-22: Die Suche liefert P* = 1.818.181, einen Preis im M-22-Bereich, und rechnet ihn | D + R → Befund 4 |
| GF-20 | Zuschuss > Baukosten (Neubau, Zuschussquote 80 %, Grundstück 5 Mio., Bau 2,6 Mio.) | R-7.3 Grundlage „Baukosten − Zuschüsse“ | Grundlage still auf 0 gesetzt; die übrigen 3,48 Mio. Zuschuss wirken steuerlich nirgends; P-08 besteht | D → Befund 9 |
| GF-21 | Verkaufsfaktor 0 | M-20 (E-47 > 0) | rechnet: EW 0,00, r −100 %, „Nachschussbedarf“ 610.943,61 (Ablösung im Verkaufsmonat) | R-bek. |
| GF-22 | Verlust in jedem Jahr (Mietausfall 60 %, Faktor 8) | R-7.5: Vortrag, verfällt | Steuer 0 in allen 12 Jahren, Vortrag 940.871,77 verfällt | ok |
| GF-23 | Verkaufsgewinn negativ (Faktor 10, n = 5), Körperschaft und Privat | R-7.5 / R-7.11 | KSt: g_v −857.179,13 im Vortrag; Privat: ohne Wirkung, 456,64 € Steuer auf Zinsen | ok |
| GF-24 | Steuersatz 0 % (Privat, Zinssatz 0) | rechnet | r 7,159 % | ok |
| GF-25 | Steuersatz 100 % | M-20 (E-42: 0 bis 60) | rechnet still: r 5,586 % | R-bek. |
| GF-26 | Haltedauer 1, Bindung 10 | R-14.5 | EW 938.499,02; VFE 126.170,42 = RF-14 | ok |
| GF-27 | Haltedauer 1, Bindung 40 (E-46 Höchstwert) | R-5.16 | VFE **546.738,49 = 39 % der Restschuld**; EW 517.930,95 | D → Befund 5 |
| GF-28 | Haltedauer 42 (Ankauf, Bindung 10) | rechnet | EW 9.074.902,49; r 4,916 %; Proben bestanden | ok |
| GF-29 | Bindung 15 bei Haltedauer 12; Bindung 12 bei Haltedauer 12 | VFE nur bei Bindung > N | 15/12: VFE 29.734,60; 12/12: VFE 0, kein M-24 | ok nach Dokument; Sache → Befund 5 |
| GF-30 | Tilgung 0 % (H-04 = 0) | endfällig wirkend | L 1.560.000 nach (a); Deckung 1,651 | ok |
| GF-31 | Tilgung 0 % mit H-07 „Restlaufzeit bleibt“ | definiertes Ergebnis | **Absturz** `DivisionByZero` (ln((i+τ)/τ)) | D + R → Befund 3 |
| GF-32 | Tilgung 100 % | rechnet | L 82.560,28; nach Monat 12 getilgt; Deckung 1,2218 | ok |
| GF-33 | Investitionsstau im Verkaufsjahr k = n = 12 (Erhaltung, Modernisierung) gegen k = 13 | Zahlung in N gegen Abzug | 171.091,31 jeweils; EW in allen drei Fällen 2.249.830,83 – in sich stimmig | ok |
| GF-34 | Zielrendite 30 % | P* oder M-32 | P* = 331.567 (kleiner Preis, starker Hebel) | ok |
| GF-35 | tragbarer Preis genau an der Obergrenze (Obergrenze = P* = 2.425.585) | P* = Obergrenze | **M-33 „Preis über der Obergrenze“**, kein Preis | D → Befund 10 |
| GF-36 | Zielwertsuche, zwei Lösungen in einer Rasterzelle: (x − 3)(x − 3,2) auf [0; 10] | R-11.10: nicht gefunden, Rasterweite genannt | Status „**keine Lösung: Ziel im ganzen Bereich erreicht**“ – sachlich falsch | D → Befund 10 |
| GF-37 | Kaufpreis 2,4 Mrd., Fläche 1,32 Mio. m² | rechnet exakt | EW 2.378.824.224,59; Proben bestanden | ok |
| GF-38 | Kaufpreis 2.400 €, 1,32 m², 1 Einheit | rechnet | EW 2.400,24; r 6,582 %; Proben bestanden | ok |
| GF-39 | interner Zinsfuß: −400.000, nach 12 Monaten +1; ebenso −100 / +1.200 | R-10.18: „Ein Wechsel: genau eine Lösung“ | **keine Lösung** bei gemeldetem Wechsel (Lösung unter −99 % bzw. über 1.000 %) | D → Befund 10 |
| GF-40 | Neubau, Bauzeit 60, Haltedauer 6; Stress +3 Monate | E-48 erfüllt; R-14.4 im Stress | Basis rechnet (r 1,299 %); Stress M-23; tragbarer Preis im Stress: **Absturz** (Meldung nicht abgefangen) | D + R → Befund 4 |
| GF-41 | Neubau, Bauzeit 0 | M-20 (E-26: 1 bis 60) | **Absturz** `DivisionByZero` | R-bek. |
| GF-42 | übernommenes Darlehen, Bindung endet vor Verkauf, Anschlusszins fehlt | M-24 | M-24 als `ValueError`, nicht als Meldung; bricht jede Suche ab | R (gering) |
| GF-43 | gebundener Bestand, Bindungsende im Verkaufsjahr (b = n = 12) gegen b = 11 | R-6.6: Jahr b + 1 gebunden | Miete J13 10,2540 gegen 10,6075; VK 2.923.629,12 gegen 3.024.403,92 | ok (vorsichtig) |
| GF-44 | Vollfinanzierung ohne Eigenkapital (Quote 100 %, Nebenkosten 0, Faktor 5): tragbarer Preis und Zielwertsuche | nicht geregelt | Preissuche wertet „Rendite nicht definiert“ als **erreicht**: P* = 3.826.767 mit EK 0 und **EW 0,50 €**; Zielwertsuche auf den Faktor wertet denselben Zustand als **verfehlt** | D + R → Befund 4 |
| GF-45 | Stichtag im Dezember, Schaltjahr, Monatsletzter | – | nicht rechenbar: Stichtag ist Monat und Jahr (E-02), Perioden sind p-tel Jahre (R-5.2) | nicht anwendbar in Teil 1 |
| GF-46 | Probe P-07: BGF 2.600,12 m², Kostenkennwert 2.901,89 €, Bauzeit 14, Haltedauer 36, Grobförderung B | P-07 besteht (Rückzahlung 8.138,35 nach R-8.7 richtig) | **P-07 meldet −0,01 €**; nach R-13.1 also M-10 und keine Ergebnisse | R → Befund 7 |
| GF-47 | Probe P-04: Einlage zum Stichtag um 100.000 € zu hoch (simulierter Fehler im Mittelabruf) | P-04 schlägt an (EK ≠ M − Ü − Z − L) | **P-01 bis P-12 bestehen alle**; EW 2.387.652,23 statt 2.374.377,18 | D → Befund 6 |
| GF-48 | Leerstand 2 %, 30 %, 50 %: Verkaufspreis auf Soll- gegen Ist-Miete (Faktor x (1 − Quote)) | – | 30 %: ΔEW **+594.615,05 gegen −147.102,15**, r 3,644 % gegen 0,861 %; 2 %: r 5,803 % gegen 5,618 % | D → Befund 2 |
| GF-49 | Reproduzierbarkeit: gleiche Eingabe zweimal; Tranchen in umgekehrter Folge; geförderter Neubau zweimal | identisch | identisch auf den Cent in jeder Periode (EW 2.311.811,84; 3.265.245,99) | ok |

49 Fälle gerechnet, GF-45 war nicht rechenbar. 19 Fälle tragen die Befunde 1 bis 10. In 7 Fällen fehlt die Eingabeprüfung des Referenzrechners, die das Dokument selbst nennt. Diese 7 sind keine Befunde am Dokument, entwerten aber den Beleg für R-3.7 und M-20.

## Befunde

1. **[kritisch · belegt] R-6.3, R-11.5, R-10.13 – Ein leerstehendes Objekt bekommt nie Miete.**
   - Problem: E-15 erlaubt die Ist-Miete 0. Die Kappung rechnet Miete_j = min(Pfad_j; Basis_j x (1 + κ)) mit Basis = Ist = 0 in den Jahren 1 bis 3 und danach Basis = Miete_(j−3) = 0.
   - Beleg: Die Miete bleibt über die ganze Haltedauer null, der Verkaufspreis ist 0, der Endwert 0,00, die Rendite −100 % (GF-08). Die Preissuche meldet M-31, weil die Obergrenze 100 x Sollmiete Jahr 1 = 0 ist (GF-09). Der Einstiegsfaktor teilt durch null; der Referenzrechner fängt das stillschweigend ab. Dokument und Referenzrechner stimmen überein; die Lücke liegt in der Regel. Das betrifft einen häufigen Ankaufsfall: Leerstand, Entmietung, Revitalisierung.
   - Vorschlag: Die Kappung gilt nur für bestehende Mietverhältnisse. Leere Fläche wird zur Marktmiete neu vermietet; Mietpreisbremse und Erstvermietungsdauer kommen in Teil 2. Alternativ E-15 > 0 verlangen und Leerstand als eigene Eingabe führen. Die Suchobergrenze auf die Marktmiete beziehen und für Sollmiete 0 eine Regel für R-10.13 angeben.
2. **[kritisch · begründete Einschätzung, Gegenrechnung belegt] R-8.1 (NF-23), R-14.8 – Der Verkaufspreis ignoriert Leerstand.**
   - Problem: Der Faktor wirkt auf die Sollmiete vor Mietausfall. Bei 100 % Leerstand verkauft das Modell zum Preis des voll vermieteten Objekts (3.326.730,48 €, GF-10). RF-14 führt genau diesen Fall als bestanden, ohne das zu bemerken. Der Stressfall hebt den Mietausfall um 2 Prozentpunkte, der Restwert bleibt davon unberührt.
   - Beleg: Bei 30 % strukturellem Leerstand kippt die Entscheidung. Die Endwertdifferenz ist +594.615,05 € mit dem Faktor auf der Sollmiete und −147.102,15 € mit dem Faktor auf der Mieteinzahlung (GF-48). Die Spezifikation (Kapitel 3, „Restwert“, fest) nennt die Jahresnettokaltmiete; ein Käufer bezahlt die erzielte Miete, nicht die Sollmiete einer leeren Fläche.
   - Vorschlag: Mietausfall in Leerstand (wirkt auf den Restwert) und Forderungsausfall (wirkt nicht) trennen; Bezug des Faktors ist die Sollmiete abzüglich Leerstand. Andernfalls die Wahl als Modellannahme mit der anderen Lesart führen; nach Kapitel 8 der Spezifikation ist die vorsichtige Lesart voreinzustellen.
3. **[kritisch · belegt] R-5.12 (b), R-5.9 – Division durch null bei Zins plus Tilgung null.**
   - Problem: B = (RE/μ − KD_Ü) / (i + τ) ist bei i = 0 und τ = 0 nicht definiert. Beides ist zulässig: E-45 ab 0, H-04 ≥ 0, E-64 ≥ H-04. Ebenso ist ln((i + τ)/τ) der Regel „Restlaufzeit bleibt“ bei τ = 0 nicht definiert.
   - Beleg: Der Referenzrechner bricht in beiden Fällen ab (GF-02, GF-31; ebenso GF-04 mit negativem Zins). Das verstößt gegen die feste Festlegung „Randfälle“ der Spezifikation und gegen den Eingangssatz von Kapitel 14. R-14.1 behandelt nur i = 0 mit τ > 0.
   - Vorschlag: In R-5.12 festlegen: Bei i + τ = 0 ist der Kapitaldienst des Bankdarlehens null, und B ist unbegrenzt, wenn RE_VJ ≥ μ x KD_Ü (dann binden a oder c); sonst ist B = 0 mit M-21. Für H-07 „Restlaufzeit bleibt“ τ > 0 verlangen (M-20) oder bei τ = 0 auf „Tilgungssatz bleibt“ zurückfallen, mit Hinweis.
4. **[wichtig · belegt] R-11.5, R-11.10, R-14.4 – Die Preissuche ist über unzulässige und undefinierte Bereiche nicht geregelt.** Das Dokument sagt nur, M-22-Preise „gelten als unterhalb des zulässigen Bereichs“. Der Referenzrechner wertet sie als „erreicht“; bei einem Vorhaben, das die Zielrendite bei keinem zulässigen Preis erreicht, meldet die Suche deshalb P* = 1.818.181 im M-22-Bereich und stürzt beim Nachrechnen ab, statt M-32 zu melden (GF-19b). Die Suche wertet auch „Rendite nicht definiert“ (M-28) als „erreicht“; ausgewiesen wird dann ein tragbarer Preis von 3.826.767 €, bei dem kein Eigenkapital eingesetzt ist und der Endwert 0,50 € beträgt; P-14 ist dort nicht auswertbar (GF-44). Die Zielwertsuche nach R-11.10 wertet denselben Zustand als „verfehlt“. M-23 im Stressfall (E-48 erfüllt, Bauzeit + 3 Monate nicht) bricht die Preissuche ab (GF-40), und das Dokument sagt nicht, ob der Basisfall dann auf dem Blatt steht. Vorschlag: Zuerst den kleinsten zulässigen Preis bestimmen und erst ab dort suchen. Für D = 0 in beiden Suchen dasselbe Kriterium festlegen, etwa Endwertüberschuss oder ΔEW ≥ 0 statt der Rendite. E-48 mit der Bauzeit des Stressfalls prüfen.
5. **[wichtig · begründete Einschätzung] R-5.16 (NF-10) – Vorfälligkeit ohne Obergrenze.** Haltedauer 1 und Bindung 40 Jahre ergeben 546.738,49 € Vorfälligkeit, 39 % der Restschuld (GF-27). Bei Bindung 15 und Verkauf nach 12 Jahren setzt das Modell 29.734,60 € an (GF-29). Nach meiner Kenntnis (ungeprüft, aus dem Gedächtnis; das Kataster hat dazu keinen Eintrag, Kapitel 17 nennt die Lücke) kann der Darlehensnehmer nach § 489 Abs. 1 Nr. 2 BGB zehn Jahre nach vollständigem Empfang mit sechs Monaten Frist kündigen. Dann fiele hier keine Entschädigung an, und die Restbindung wäre höchstens bis zu diesem Termin zu rechnen. Vorschlag: Restbindung = max(0; min(Bindungsende; frühestes gesetzliches Kündigungsdatum) − N) mit dem Kündigungsrecht als Katalogwert und Quelle. Bis zur Klärung als Modellannahme führen; die Liste in Kapitel 17 enthält die Vorfälligkeit bereits, aber nicht diese Obergrenze.
6. **[wichtig · belegt] R-13.3 P-04 – Die Probe kann keinen Fehler finden.** Weil die Verwendungsseite „Guthaben abzüglich Kontokorrent am Ende der Phase“ enthält, ist P-04 die aufsummierte P-01 und bei bestandener P-01 immer erfüllt. Eine um 100.000 € zu hohe Einlage zum Stichtag lässt P-01 bis P-12 bestehen, und der Endwert verschiebt sich (GF-47). P-12 prüft das Eigenkapital aus der Formel R-5.12, nicht das gebuchte. Damit sichert keine Probe den Satz „Das Eigenkapital ist der Ausgleichsposten EK = M − Ü − Zuschüsse − L (P-04)“. P-11 ist aus demselben Grund konstruktionsbedingt immer erfüllt; als Prüfung der Umsetzung ist das in Ordnung, sollte aber so benannt sein. Vorschlag: P-04 als „gebuchte Einlagen der Investitionsphase ohne Nachschüsse für Bauzeitzinsen = M − Ü − Zuschüsse − L“ fassen; dazu beim Ankauf Guthaben und Kontokorrent nach dem Stichtag gleich null.
7. **[wichtig · belegt] Referenzrechner `grobkalkulation.py`, P-07 – Fehlalarm um einen Cent.** Mit BGF 2.600,12 m², Kostenkennwert 2.901,89 €, Bauzeit 14 Monaten, Haltedauer 36 Jahren und Grobförderung B meldet P-07 −0,01 €. Nach R-13.1 erschiene dann M-10 statt eines Ergebnisses (GF-46). Die Rückzahlung selbst ist nach R-8.7 richtig (8.138,35 €). Die Probe rechnet aber Zuschuss x (v / b) mit vorgezogener Division, entgegen R-12.5; sie trifft genau die halben Cent. Das ist eine Abweichung des Referenzrechners. Für das Dokument folgt daraus: R-13.2 verlangt Abweichung null, also müssen die Proben nach denselben Rundungsregeln wie die Rechnung nachrechnen. Vorschlag: P-07 mit der Formel aus R-8.7 nachrechnen und den Satz in R-13.2 ergänzen.
8. **[wichtig · belegt] R-6.3 – Text und Formel widersprechen sich bei der Anpassungsdauer 0.** Der Text sagt „Im Jahr 1 gilt die Ist-Miete“, die Formel „bei d = 0: Marktmiete_j“, also auch in Jahr 1. Der Referenzrechner folgt der Formel: Die Miete in Jahr 1 ist 9,20 statt 8,50 €, RE_VJ 113.901,48 statt 103.035,24 €, das Bankdarlehen 1.560.000 nach (a) statt 1.431.044,99 € nach (b) (GF-13). Eine Erhöhung bestehender Mieten am Übergabetag ist mietrechtlich nicht möglich; die Wartefrist regelt erst die Vollkalkulation (NF-12). d = 0 ist zulässig (E-53, H-23). Vorschlag: Pfad_1 = Ist für jedes d; d = 0 heißt dann Marktmiete ab Jahr 2, mit Kappung. Ebenso klären, ob RE_VJ eine Ist-Miete über der Marktmiete ungekürzt ansetzt (GF-11 hebt B); vorsichtig wäre min(Ist; Markt).
9. **[Hinweis · belegt] R-7.3, R-11.14 – Zuschuss über den Baukosten.** Die zuwendungsfähigen Kosten umfassen das Grundstück, R-7.3 zieht den ganzen Zuschuss von den Baukosten ab. Übersteigt der Zuschuss die Baukosten, setzt der Referenzrechner die Grundlage still auf null (GF-20: 6,08 Mio. € Zuschuss gegen 2,6 Mio. € Baukosten). Die übrigen 3,48 Mio. € mindern weder Boden noch Abschreibung und sind damit steuerfrei. Das ist günstig für das Vorhaben und widerspricht der Vorsichtsregel. P-08 besteht. Vorschlag: Den Zuschuss im Verhältnis der zuwendungsfähigen Bau- und Grundstückskosten auf Gebäude und Boden aufteilen (gehört zur vorgeschlagenen Modellannahme „Zuschüsse in der Steuer“, Kapitel 17) und eine negative Grundlage ausdrücklich ausschließen.
10. **[Hinweis · belegt] R-11.5, R-11.10, R-10.18, R-14.3 – An den Rändern führt die Ausgabe in die Irre.** Die vier Fälle:
    - (a) P* genau an der Obergrenze ergibt M-33 „Preis über der Obergrenze“ und keinen Preis, obwohl P* im Bereich liegt (GF-35). Vorschlag: zusätzlich Obergrenze + 1 auswerten.
    - (b) Zwei Lösungen in einer Rasterzelle ergeben den Status „Ziel im ganzen Bereich erreicht“, der sachlich falsch ist (GF-36). Vorschlag: „an allen Rasterstellen erreicht, Rasterweite x“.
    - (c) Beim internen Zinsfuß meldet die Suche einen Vorzeichenwechsel, findet aber keine Lösung, wenn diese außerhalb von −99 % bis 1.000 % liegt (GF-39). Vorschlag: „Lösung außerhalb des Suchbereichs“ als eigenes Ergebnis.
    - (d) Mit der voreingestellten Linie null (NF-06) kann der Endwert nie negativ werden. Ein Verlust beim Verkauf wird Nachschuss in N und erscheint als „Nachschussbedarf“ (R-10.17), beim Verkaufsfaktor 0 etwa 610.943,61 € (GF-21). R-14.3 und R-14.13 sollten das sagen, und der Nachschussbedarf sollte Nachschüsse in N gesondert ausweisen.

## Am Dokument bestätigt (keine Befunde)

- Zins null, Eigenkapital null, Beleihungsquote 0 und 100 %, Tilgung 0 und 100 %, Haltedauer 1 und 42, Bindung gleich Haltedauer (keine Vorfälligkeit, kein M-24), Verlust in jedem Jahr, negativer Verkaufsgewinn je Steuerstatus, gebundene Miete mit Bindungsende im Verkaufsjahr: Alle haben ein definiertes Ergebnis, und alle Proben bestehen.
- Gleichstand an Schwellen: Kappung genau erreicht (GF-12), gleichauf liegende Grenzen in R-5.12 (GF-05: (a) und (c)), private Veräußerungsfrist bei n = Frist (steuerpflichtig, vorsichtig nach R-7.11). Keine Mehrdeutigkeit.
- Ein Investitionsstau im Verkaufsjahr gezahlt, aktiviert oder vom Erlös abgezogen ergibt denselben Endwert (GF-33). R-6.10 und R-8.4 sind stimmig.
- Reproduzierbarkeit: dieselbe Eingabe ergibt zweimal und bei umgekehrter Tranchenfolge Periode für Periode denselben Cent (GF-49). Milliarden und Cent rechnen exakt (GF-37, GF-38).

## Nicht geprüft

- Datumsränder (Monatsletzter, Schaltjahr): In Teil 1 nicht anwendbar, weil der Stichtag ein Monat ist und Perioden p-tel Jahre sind (R-5.2). Gehört zu Teil 2 (Zinstage).
- R-2.8 bei Stichtag im Dezember: Elf Monate von Planjahr 1 tragen den Satz des Vorjahres. Das Dokument nennt das nur für sinkende Sätze vorsichtig. Der Referenzrechner kennt keinen Stichtagsmonat; nicht nachgerechnet.
- M-25 bis M-29, M-31 als Meldung der Grobkalkulation, M-35 und M-36 sowie die Eingabeprüfung M-20: Sie fehlen im Referenzrechner, wie das Dokument sagt. Geprüft habe ich nur, was ohne sie geschieht (Tabelle, „R-bek.“).
- Lehrbuchmodus ohne Rundung (Toleranz 1E-30), Gesamtkapitalrendite und Amortisationsdauer an den Rändern: nicht gesondert gerechnet.
- Rechtsgrundlagen (§ 489 BGB, Wartefrist nach § 558 BGB): nicht am Original gelesen; in Befund 5 und 8 als ungeprüft gekennzeichnet.
