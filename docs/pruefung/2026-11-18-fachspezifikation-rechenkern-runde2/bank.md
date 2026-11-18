Rolle: Bank (Kreditprüfer einer finanzierenden Bank, wohnungswirtschaftliche Immobilienfinanzierung)
Prüfobjekt: `docs/fachspezifikation-rechenkern.md`, Fassung nach der ersten Überarbeitung (2026-11-18). Geprüft wurden Kapitel 5 vollständig; aus Kapitel 3 E-45, E-46, E-59 bis E-61, E-64, H-02 bis H-07, H-18, H-24, H-25, H-31, KAT-13 bis KAT-15; aus Kapitel 10 R-10.14, R-10.15 und R-10.20 bis R-10.23; aus Kapitel 11 R-11.2, R-11.3, R-11.6 bis R-11.8, R-11.12, R-11.14 und R-11.15; dazu Kapitel 13 und 16, `MA-026`, `MA-033`, `MA-034` und Anhang A.4 bis A.6. Den Referenzrechner habe ich unverändert benutzt: `referenzfaelle.py` besteht (906 von 906 Prüfungen), dazu ein eigenes Skript mit 20 Fällen.

Gesamturteil: Mit Auflagen. Die Bemessung des Bankdarlehens erkennt ein Kreditprüfer jetzt wieder. Sie rechnet kalkulatorischen Zins und Mindesttilgung je Tranche, den nachhaltigen Reinertrag mit dem Mindestansatz für die Bewirtschaftung, die Deckung über alle Darlehen, den Beleihungsraum nach Rang, die kleinste Deckung über die Haltedauer und die Kennzahlen aus Bankensicht. Die zehn Befunde aus Runde 1 sind bis auf einen Teil von Befund 10 behoben. Doppelt vorsichtig wird nirgends gerechnet. Offen sind drei Stellen, an denen das Werkzeug günstiger rechnet als eine Bank: die Voreinstellung „Förderdarlehen: ja“ beim übernommenen Darlehen, der Zinsanstieg bis zur Kreditzusage ohne neue Bemessung und die Prolongationsregel, die über „Deckung unter 1“ entscheidet.

Note: 8 von 10. Zur 9 fehlen drei Änderungen, die **im Dokument** möglich sind (Befunde 1 bis 3):
1. Beim übernommenen Darlehen ist „Förderdarlehen: nein“ voreingestellt, wie es der Referenzrechner schon tut.
2. Der Stressfall bemisst das Darlehen mit dem Zinsanstieg bis zur Zusage neu, oder er weist die Lücke beim Eigenkapital aus.
3. Die Deckung nach der Zinsbindung wird zusätzlich mit der strengsten Anschlussregel geprüft, und die Richtung von H-07 wird berichtigt.

Die Befunde 4 bis 8 sind Hinweise. **Nur die Hausbank** kann klären, welche Werte und Lesarten voreingestellt werden. Das hindert die 9 nicht, solange die vorsichtige Lesart voreingestellt ist. Kapitel 16 deckt `MA-026`, `MA-033` und `MA-034` ab; drei Fragen sollten ergänzt werden (Befund 8).

## Befunde aus Runde 1

| Nr. | Befund Runde 1 | Stand | Regel | Anmerkung |
|---|---|---|---|---|
| 1 | Mindestdeckung mit heutigem Vertragszins | behoben | R-5.12 (b), H-25, NF-09 | je Tranche max(Vertragszins; H-25), voreingestellt der Anschlusszins; τ_k = max(τ; H-04). Ankauf nachgerechnet: B = 103.035,24 / 1,2 / 7 % = 1.226.610,00; gerundete Rate 7.155,23 x 12 = 85.862,76 > 85.862,70, also 1.226.609,99 Euro wie im Dokument |
| 2 | nur Deckung im ersten Jahr | behoben | R-10.14, M-38, M-39, NF-30 | kleinste Deckung mit Planjahr, Deckung nach jeder Zinsbindung, Basis- und Stressfall; gemischte Bauzeitjahre zählen nicht. Grenze siehe Befund 3 |
| 3 | `MA-026` verband Beleihungsraum und Deckung | behoben | R-5.12 (a), (b), `MA-026`, E-59 | Die Deckung über alle Darlehen ist Festlegung, der Rang ein Merkmal je Tranche. Der Teilvorschlag, R-10.15 zweifach auszuweisen (vorrangige und alle Darlehen), ist nicht übernommen; das genügt für 1a |
| 4 | übernommenes Darlehen unvollständig, ohne Stress | behoben | E-59 (neun Werte), R-3.6 (34), R-5.8, R-11.8 | Anschlusszins voreingestellt E-45 + H-05; Stress auf jede Tranche mit Bindungsende vor dem Verkauf (nachgerechnet: 15.772,22 Euro Zins im Jahr 9 zu 4 %). Neue Lücke beim Kennzeichen Förderdarlehen: Befund 1 |
| 5 | Vorfälligkeit ohne Kappung nach `BGB-489` | behoben | R-5.16, KAT-13, `MA-033` (mittel) | Restbindung = min(Bindungsende; t_voll + 120 + 6 Monate) − N; `BGB-489` und `BGB-490` stehen im Kataster. Nachgerechnet: 1.201.623,01 x 1 % x 9,5 = 114.154,19 Euro |
| 6 | keine Bereitstellungszinsen | behoben | R-5.18, H-31, NF-40, R-10.17 | Nachgerechnet: 4.007.142,85 x 0,25 % = 10.017,86; Monat 10 (4.007.142,85 − 104.786,77) x 0,25 % = 9.755,89 Euro; 78.993,23 + 54.961,41 = 133.954,64 Euro (P-04) |
| 7 | Ertrag nicht nachhaltig | behoben (Neubau: Befund 6) | R-5.12 (b), KAT-14 | min(Miete; Vergleichsmiete) je Teilfläche, Abzug = max(Bewirtschaftung + Ausfall; 15 % des Rohertrags) |
| 8 | „Beleihungsauslauf“ mit Kaufpreis im Nenner | behoben | R-10.15, NF-52 | „Darlehen zu Kaufpreis“ und Restschuld zum Wert am Ende der Zinsbindung, auch im Stressfall |
| 9 | Bankkennzahlen fehlen | behoben | R-10.20 bis R-10.23, NF-53 | Nachgerechnet für RF-11: 103.035,24 − 1,2 x 73.596,60 = 14.719,32 Euro; 102.508,56 / 131.947,20 = 77,69 % |
| 10 | geförderter Neubau: nur „kein Bankdarlehen“ | teilweise | R-11.15, NF-57 | Deckung der übrigen Darlehen, Reserve, nötiger Reinertrag und nötige Miete sind da (nachgerechnet: 1,2 x (150.431,28 + 25.297,56) = 210.874,61 Euro). Es fehlen der Verlauf zur Mindestdeckung und der freie Beleihungsraum (Befund 5) |

**Doppelte Vorsicht (Prüfauftrag 2):** Ich habe keine gefunden.
- Der kalkulatorische Zins wirkt nur in der Bemessung. Der Stressfall übernimmt das Darlehen des Basisfalls und stresst die tatsächlichen Konditionen; die Deckung auf dem Blatt rechnet mit Vertragskonditionen (R-10.14).
- Die nachhaltige Miete ist eine Frage der Höhe, das Mietausfallwagnis eine Frage der Menge. Das ist die Systematik der `BELWERTV-11`. Der Mindestansatz von 15 % wird als Maximum gebildet, nicht zum Ausfall hinzugezählt.
- Im geförderten Neubau ist RE_n gleich dem Reinertrag des Vorhabens (159.216,75 Euro); dort greift weder der Mindestansatz noch die Vergleichsmiete.
- Der Stress „Zinsanstieg bis zur Zusage“ hebt den Anschlusszins des Bankdarlehens rechnerisch mit, auf zusammen +1,5 Prozentpunkte. Das folgt aus der Definition „heutiger Zins + H-05“ und ist keine Doppelzählung.

**KfW-Tranche (Prüfauftrag 3):**
- Rang: „belegt den Beleihungsraum immer“ entspricht der Praxis. Das durchgeleitete Darlehen liegt im Obligo der Hausbank und in ihrer Grundschuld.
- Bemessung: Kalkulatorisch zählt die volle Tilgung ohne Anlaufjahre (τ_k). Nachgerechnet: B = (336.600 / 1,2 − 210.000) / 7 % = 1.007.142,85 Euro.
- Deckung: Die Anlaufjahre wirken nur auf die Deckung des ersten Jahres (2,356; Befund 7). Die kleinste Deckung fängt das Ende der Zinsbindung auf: 1,7726 im Jahr 11, im Stress 1,3485.
- Zinsbindungsende und Anschlusszins nach R-5.8 sind sauber geregelt.

**Vorfälligkeit, Bereitstellung, Prolongation, Rate aus dem Nennbetrag (Prüfauftrag 4):**
- R-5.16, R-5.18 und R-5.11 sind richtig und nachgerechnet; die Rate aus dem Nennbetrag ergibt 600.000 x 2,5 % / 12 = 1.250,00 Euro.
- R-5.9 rundet die Restlaufzeit ab und fällt bei Tilgung null auf „Tilgungssatz bleibt“ mit M-40 zurück; das ist richtig.
- Nachgerechnet: 1.136.777,27 Euro zu 6 % über 18 Jahre ergeben die Rate 104.989 Euro.
- Problem ist nicht die Rechnung, sondern die Wirkung der Voreinstellung auf die Meldungen (Befund 3).

## Befunde

1. **[wichtig · belegt] E-59, Voreinstellungsspalte und Satz unter der Tabelle („Die Voreinstellungen von E-59 sind die vorsichtigen“), mit R-5.12 und R-5.16: „Kennzeichen Förderdarlehen: ja“ ist die günstigere Voreinstellung, nicht die vorsichtige. Der Referenzrechner stellt sie umgekehrt ein.**
   Das Kennzeichen wirkt zweifach zugunsten des Vorhabens:
   - Ein Förderdarlehen, dessen Bindung nicht vor der des Bankdarlehens endet, geht mit dem vertraglichen statt dem kalkulatorischen Kapitaldienst in KD_Ü ein (R-5.12).
   - Es zahlt keine Vorfälligkeit (R-5.16).

   Eigene Fälle zum gebundenen Bestand (RF-11, übernommene Bindung zwölf statt acht Jahre):
   - Mit „ja“ beträgt KD_Ü 15.000,00 Euro, das Bankdarlehen 886.660,00 Euro.
   - Mit „nein“ beträgt KD_Ü 24.999,96 Euro, das Bankdarlehen 743.803,42 Euro. Der Unterschied ist 142.856,58 Euro oder 19 %.
   - Vorfälligkeit nach fünf Jahren: 33.080,71 statt 46.182,48 Euro (R-5.16, Beispiel).

   Für ein übernommenes Annuitätendarlehen einer Geschäftsbank des Verkäufers ist „ja“ schlicht falsch, und der Bearbeiter merkt es nicht. Der Referenzrechner setzt `ue.get("foerderdarlehen", False)` (`grobkalkulation.py`, Zeile 510), also „nein“. Spezifikation und Referenzrechner widersprechen sich damit; RF-11 setzt das Kennzeichen ausdrücklich.
   *Vorschlag:* Voreinstellung „nein“ wie im Referenzrechner. Wer „ja“ setzt, belegt es mit dem Bewilligungsbescheid; das Kennzeichen steht dann in der Liste der Abweichungen oder im Annahmenblatt. Die Zählung in R-3.6 („dazu 6“) bleibt.

2. **[wichtig · belegt] R-11.8, Zeile „Zins des Bankdarlehens (Zinsanstieg bis zur Kreditzusage)“, mit NF-35: Steigt der Zins vor der Zusage, bemisst die Bank mit dem höheren Zins. Der Stressfall behält das Darlehen des Basisfalls und zeigt deshalb ein Darlehen, das die Bank nach ihrer eigenen Regel nicht gäbe.**
   NF-35 begründet „Die Bank bemisst ihr Darlehen heute aus den Basisannahmen“. Für die Größe „bis zur Kreditzusage“ trägt das nicht: Vor der Zusage ist nichts bemessen. Eigener Lauf RF-11 mit E-45 + 0,5 Prozentpunkte in R-5.12:
   - i_k = 5,5 %, B = 85.862,70 / 7,5 % = 1.144.835,99 statt 1.226.609,99 Euro.
   - Das Darlehen ist also 81.774,00 Euro kleiner, das nötige Eigenkapital 5,8 % höher.

   Der Stressfall zeigt stattdessen die Deckung 1,2354 im Jahr 1. Das Darlehen des Basisfalls hat bei 5,5 % und 2 % eine kalkulatorische Deckung von 85.862,70 x 1,2 / (1.226.609,99 x 7,5 %) = 1,12 und liegt damit unter H-03. Der Engpass, den eine Bank in diesem Fall meldet, ist Eigenkapital, nicht Deckung. Er steht nicht auf dem Blatt und nicht im tragbaren Preis des Stressfalls.
   *Vorschlag:* Im Stressfall wird L einmal mit E-45 + Zusageaufschlag nach R-5.12 neu bemessen. Alle übrigen Stressgrößen bleiben auf L_Basis, wie NF-35 es will. Die Differenz trägt das Eigenkapital (R-11.3: Ausgleichsposten mit L_Zusage), und P-04 prüft gegen L_Zusage. Wenn das nicht gewollt ist, weist das Blatt wenigstens „Eigenkapitallücke bei Zinsanstieg bis zur Zusage“ in Euro aus. Frage an die Hausbank: Gilt eine Zinssicherung (Forward, Zusage mit Festzins)? Dann entfällt die Größe.

3. **[wichtig · belegt] R-5.9, `MA-034` (Gewicht gering), H-07 und R-3.2: Die voreingestellte Prolongationsregel entscheidet, ob „Deckung unter 1“ gemeldet wird. Die Spalte „strenger heißt“ von H-07 widerspricht R-3.2.**
   Fall aus RF-19 (Zins 3 %, Ist- gleich Vergleichsmiete 8,50 Euro, Mietsteigerung 0,5 %), eigener Lauf:

   | Regel nach der Bindung | kalkulatorisch, Stress: kleinste Deckung | Meldung | Vertragskonditionen (Lesart 2), Basis | Lesart 2, Stress |
   |---|---|---|---|---|
   | Tilgungssatz bleibt (Voreinstellung) | 1,1098 (Jahr 12) | M-38 | 1,3054, keine Meldung | 1,0181, M-38 |
   | Rate bleibt | 1,1516 | M-38 | 1,3054 | 1,0564, M-38 |
   | Restlaufzeit bleibt | 0,9774 | **M-39** | 1,1975, **M-38** | 0,8966, **M-39** |

   Mit der Voreinstellung erfährt der Bearbeiter nicht, dass der Reinertrag bei einer Prolongation über die Restlaufzeit den Kapitaldienst nicht deckt. Genau so prüft eine Bank beim Anschluss, wenn die Gesamtlaufzeit begrenzt ist.
   - `MA-034` begründet die Ausnahme damit, dass die Deckung nach jeder Zinsbindung auf dem Blatt steht. Sie steht dort aber nur zur günstigsten Regel. Das Gewicht „gering“ passt nicht zu einer Wirkung, die die Meldung von M-38 auf M-39 hebt.
   - H-07 nennt „Restlaufzeit bleibt“ die strengere Richtung. Nach R-3.2 ist strenger die Richtung, in der Preis oder Endwertdifferenz sinken. „Restlaufzeit bleibt“ hebt die Endwertdifferenz aber von 753.701,96 auf 754.381,58 Euro (R-5.9) und wäre damit eine Lockerung, die keine Begründung braucht.

   *Vorschlag:* Die Voreinstellung für die Endwertdifferenz bleibt. Zusätzlich rechnet der Kern die Deckung im ersten Jahr nach jeder Zinsbindung und die kleinste Deckung danach auch mit „Restlaufzeit bleibt“ (ein Nebenlauf nur der Tranchen, ohne Steuer). M-38 und M-39 prüfen den kleineren der beiden Werte und nennen die Regel. Das Gewicht von `MA-034` wird mittel. In H-07 heißt die Spalte für die Deckung „Restlaufzeit bleibt“ und für die Endwertdifferenz „Tilgungssatz bleibt“, oder R-3.2 erhält für H-07 eine ausdrückliche Ausnahme.

4. **[Hinweis · belegt] R-10.21 und R-11.15, auf demselben Blatt (R-11.12): zwei verschiedene „Kapitaldienstreserven“.**
   Im geförderten Neubau steht −21.113,95 Euro nach R-10.21 (Reinertrag des Vorhabens, tatsächlicher Kapitaldienst) neben −21.300,79 Euro nach R-11.15 (RE_n, kalkulatorischer Kapitaldienst). Weichen Ertrag oder Konditionen stärker ab, liegen die beiden Werte weit auseinander. Ein Kreditprüfer fragt dann, welcher gilt.
   *Vorschlag:* Den Wert nach R-11.15 „Reserve nach Bankansatz“ nennen und die Größe in R-10.21 „Kapitaldienstreserve (Ist)“.

5. **[Hinweis · belegt] R-11.15: Für ein Gespräch über eine Restfinanzierung fehlen zwei Angaben, die die Bank zuerst sucht: wann die Deckung trägt und ob Sicherheit vorhanden ist.**
   Eigener Lauf RF-12 gefördert:
   - Die Deckung der übrigen Darlehen steigt mit den gebundenen Mietstufen. Sie erreicht 1,2 im Basisfall im Planjahr 9 (1,2244) und im Stressfall im Planjahr 12 (1,2672); bis zum Planjahr 11 liegt sie bei 1,1999.
   - Der Beleihungsraum A = 628.357,62 Euro übersteigt die Restfinanzierung C = 361.393,64 Euro. Die Sicherheit ist also da; es fehlt nur der Kapitaldienst.

   Mit diesen beiden Zahlen kann die Bank ein Darlehen mit tilgungsfreien Anlaufjahren oder eine Stundung anbieten. Ohne sie bleibt nur das Eigenkapital.
   *Vorschlag:* R-11.15 ergänzen um (a) Deckung der übrigen Darlehen je Planjahr, Basis und Stress, mit dem ersten Planjahr ≥ H-03 und ≥ 1; (b) freien Beleihungsraum A − C. Beides liegt im Kern schon vor.

6. **[Hinweis · begründete Einschätzung] R-5.12 (b), „nachhaltiger Reinertrag“, beim Neubau: Der Vergleich mit der Vergleichsmiete läuft dort ins Leere.**
   E-19 gilt nur beim Ankauf. Im Referenzrechner ist beim Neubau die Vergleichsmiete gleich der Marktmiete bei Bezug (`ertrag.py`, Zeile 165): Gerechnet wird mit 16,50 Euro als „nachhaltig“. Eine Bank setzt beim Neubau die nachhaltig erzielbare Miete an, die oft unter der Erstvermietungsmiete liegt. Die Spezifikation (Kapitel 2) verspricht den kleineren Wert für beide Vorhabensarten.
   *Vorschlag:* Beim Neubau eine freiwillige Eingabe „nachhaltige Miete der Bank“, voreingestellt E-16. Alternativ ein Satz in R-5.12, dass der Vergleich beim Neubau entfällt. Frage 4 an die Hausbank auf den Neubau ausdehnen.

7. **[Hinweis · belegt] Nahtstellen KfW-Tranche und Deckung: R-5.12 (a) gegen `MA-026` (1); R-10.14 gegen Referenzrechner.**
   - R-5.12 nennt „KfW belegt den Raum immer“ eine Festlegung. `MA-026` (1) und Frage 1 führen den KfW-Raum als Teil der Annahme, die andere Lesart (1) erwähnt ihn aber nicht. Eines davon muss gelten. Ich empfehle die Festlegung, weil das Darlehen im Obligo der Hausbank liegt; dann kommt KfW aus `MA-026` (1) heraus.
   - Die Deckung im ersten Jahr der Vollvermietung beträgt im KfW-Fall 2,356. Darin stecken nur drei Tilgungsraten der KfW (R-10.23: 90.000,00 Euro). Mit voller Tilgung sind es 1,849 im Planjahr 4. Die kleinste Deckung fängt das auf, die erste Zeile des Blatts überzeichnet aber. Vorschlag: zusätzlich „Deckung im ersten Jahr mit vollem Kapitaldienst aller Tranchen“, wenn eine Tranche tilgungsfreie Anlaufjahre hat.
   - R-10.14 verlangt die Deckung „nach dem Ende jeder Zinsbindung“. `_blatt` nimmt das Förderdarlehen aus. Im geförderten Fall fällt die Deckung nach dem Ende der zinslosen Zeit von 2,214 auf 1,900. Text oder Rechner angleichen.

8. **[Hinweis · begründete Einschätzung] Kapitel 16, Fragen an die Hausbank: `MA-026`, `MA-033` und `MA-034` sind abgedeckt (Fragen 1 bis 4 je Teil von `MA-026`, Frage 8 und Frage 9). Drei Fragen fehlen.**
   - Neu: „Sichern Sie den Zins vor der Zusage (Forward, Festzinszusage), und bemessen Sie bei gestiegenem Zins neu?“ Die Antwort klärt Befund 2.
   - Frage 1 ergänzen: „Behandeln Sie ein durchgeleitetes KfW-Darlehen als eigenes Obligo im Beleihungsraum, mit oder ohne Haftungsfreistellung?“
   - Frage 4 ergänzen: „Welche Miete setzen Sie beim Neubau an: die Erstvermietungsmiete oder eine nachhaltige Miete?“ Die Antwort klärt Befund 6.
   - Frage 8 ergänzen: „Entfällt die Vorfälligkeit, wenn der Käufer das Darlehen übernimmt oder ein Pfandtausch möglich ist?“
   - Frage 9 so stellen, dass die Antwort zwischen den drei Regeln von H-07 wählt, und fragen, ob die Gesamtlaufzeit beim Anschluss begrenzt wird. Die Antwort klärt Befund 3.

## Nicht geprüft

- Kapitel 6 bis 9 und 12 sowie die Steuer, außer wo sie Reinertrag, Kapitaldienst und Eigenkapital berühren. Kapitel 14 nur zu M-21, M-22, M-24, M-25, M-38 bis M-40.
- Bankpraxis lässt sich nicht an einer veröffentlichten Quelle prüfen. Rang des KfW-Darlehens, Zinssicherung vor der Zusage, nachhaltige Miete beim Neubau und Prolongation über die Restlaufzeit sind meine Einschätzung aus der Rolle.
- Keine Quelle neu am Original gelesen. `BGB-489`, `BGB-490` und `BELWERTV-11` habe ich gegen das Kataster abgeglichen (Einträge vorhanden, am Original gelesen am 2026-11-18).
- Die Werte in KAT-15 (KfW-Konditionen) und H-31 (Bereitstellungszins) sind Annahmen des Dokuments; ich habe sie nicht geprüft.
- Den tragbaren Preis unter den drei Anschlussregeln habe ich nicht neu gesucht; die Richtung folgt aus den Endwertdifferenzen in R-5.9.
- Rust-Code gibt es noch nicht.
- Eigene Rechnungen: `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs2-bank/b1.py`, aufgerufen mit dem Ordner des Referenzrechners als Argument. Das Skript benutzt dessen Module unverändert und ändert nur Eingaben und Vorgaben.
