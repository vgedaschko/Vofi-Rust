Rolle: Bank (Kreditprüfer einer finanzierenden Bank, wohnungswirtschaftliche Immobilienfinanzierung)
Prüfobjekt: `docs/fachspezifikation-rechenkern.md`, Stand 2026-11-18 – Kapitel 5 vollständig; aus Kapitel 3 die Eingaben und Vorgaben zur Finanzierung (E-45, E-46, E-59 bis E-61, E-64, H-02 bis H-07, H-10, H-11, H-18); R-4.5 (NF-06); R-10.14, R-10.15; R-11.2, R-11.3, R-11.7, R-11.8, R-11.12, R-11.14; Kapitel 13 (P-02, P-04, P-12); Kapitel 17 (vorgeschlagene Modellannahmen zu Vorfälligkeit und Prolongation, Punkt 8 der Widersprüche). Dazu Referenzrechner (`darlehen.py`, `grobkalkulation.py`, `kennzahlen.py`, `annahmen.py`) mit eigenen Fällen; `referenzfaelle.py` läuft durch (529 von 529 Prüfungen).

Gesamturteil: Mit Auflagen. Die Darlehensrechnung selbst (Prozentannuität mit Monatsrate, Zins auf die Vorperiode, Rundung je Rate, Zinsbindung ab Stichtag, Anschluss nicht still fortgeschrieben, Kontokorrentlinie null, Mittelherkunft gleich Mittelverwendung als Probe) erkennt ein Kreditprüfer sofort wieder und ist sauber nachrechenbar. Die Bemessung des Bankdarlehens und der Stressfall rechnen an vier Stellen günstiger, als eine Bank es tut: heutiger statt kalkulatorischer Zins, nur die Deckung im ersten Jahr, kein Zinsstress auf übernommene Darlehen, keine Bereitstellungszinsen. Dazu kommt ein Schalter in `MA-026`, dessen andere Lesart für die Deckung keiner Bankpraxis entspricht.

Note: 7 von 10. Zur 9 fehlt, und das lässt sich **im Dokument beheben**: (1) In (b) wird mit einem kalkulatorischen Zins als Vorgabe des Hauses gerechnet; vorsichtig voreingestellt ist der Anschlusszins (Befund 1). (2) Das Blatt zeigt die kleinste Deckung über die Haltedauer, mit Jahr und Meldung bei Unterschreiten (Befund 2). (3) `MA-026` wird in Beleihung und Deckung getrennt, und der Rang wird Merkmal je Darlehen (Befund 3). (4) E-59 und der Stressfall werden für übernommene Darlehen vervollständigt (Befund 4). (5) Die Restbindung der Vorfälligkeit wird nach `BGB-489` gekappt (Befund 5). (6) Bereitstellungszinsen werden in 1a wenigstens pauschal angesetzt oder als Modellannahme mit Meldung geführt (Befund 6). **Nur die Hausbank** kann beantworten, welche Lesart und welche Werte voreingestellt werden: Zinsansatz, Ertrag und Pauschalen, Rang, Wertansatz, Vorfälligkeit, Prolongation (Fragen am Ende). Ohne diese Antworten bleibt `MA-026` offen. Das hindert die 9 nicht, solange die vorsichtige Lesart voreingestellt und umschaltbar ist.

## Befunde

1. **[wichtig · belegt] R-5.12 (b) und NF-09: Die Mindestdeckung rechnet mit dem heutigen Vertragszins. Das ist nicht die vorsichtige Lesart.**
   Eine Bank prüft die Kapitaldienstfähigkeit über die Zinsbindung hinaus. Sie rechnet deshalb in der Regel mit einem kalkulatorischen Zins und einer kalkulatorischen Tilgung (begründete Einschätzung; Höhe je Haus verschieden). NF-09 benennt das, stellt aber die günstigere Lesart voreingestellt ein. Das widerspricht der Konvention aus Spezifikation Kapitel 8, nach der die vorsichtige Lesart voreingestellt ist.
   Gegenrechnung RF-11 mit einem kalkulatorischen Zins gleich dem Anschlusszins (4 % + H-05 = 5 %, Tilgung 2 %), Referenzrechner mit eigenem Lauf:
   - Bankdarlehen 1.226.609,99 statt 1.431.044,99 Euro (−204.435 Euro, −14,3 %), Eigenkapital +204.435 Euro.
   - Höchster tragbarer Preis 2.383.411 statt 2.425.585 Euro (−42.174 Euro).

   Noch stärker wirkt der Ansatz bei übrigen Darlehen. Im gebundenen Bestand aus RF-11 geht das übernommene Darlehen mit 0,5 % in KD_Ü ein (12.500,04 Euro), obwohl seine Bindung im Jahr 8 endet. Mit seinem Anschlusszins von 3 % sind es 24.999,96 Euro. Dann sinkt B von 1.076.102,66 auf 867.770,66 Euro, und (b) bindet statt (a): Das Bankdarlehen wäre 192.229 Euro kleiner.
   *Vorschlag:* neue Vorgabe H-24 „Zins der Kapitaldienstrechnung“, Voreinstellung max(heutiger Zins; heutiger Zins + H-05). So entsteht keine neue Konstante. Tilgung max(E-64; H-04). Für übrige Darlehen gilt max(Vertragszins; eigener Anschlusszins), wenn ihre Bindung vor der des Bankdarlehens endet; ausgenommen ist das Förderdarlehen mit festen Konditionen (`MA-003` bleibt). Der Vertragszins wird andere Lesart in `MA-026` und ist umschaltbar. Kapitel 17, Zeile `MA-026`, entsprechend fassen.

2. **[wichtig · belegt] R-10.14, R-11.7, R-11.12, NF-35: Das Blatt zeigt im Basis- und im Stressfall nur die Deckung im ersten Jahr. Der Zinsstress wirkt aber erst nach der Bindung.**
   Das Dokument erkennt das selbst (Kapitel 17, Widersprüche Punkt 8), hat es aber nicht in die Regeln übernommen. Eigener Fall: RF-11-Ankauf mit Zins 3 %, Ist- gleich Marktmiete 8,50 Euro, Mietsteigerung 0,5 %.
   - Deckung im Stressfall: Jahr 1 1,263, Jahr 10 1,182, Jahr 11 1,092, Jahr 12 1,082.
   - Das Blatt zeigt 1,263. Tatsächlich unterschreitet der Fall ab Jahr 9 die Mindestdeckung von 1,2, ohne dass eine Meldung erscheint.

   Im geförderten Neubau aus RF-12 liegt die Deckung im Stressfall in den Planjahren 3 bis 5 unter 1 (0,963 / 0,961 / 0,978): Der Reinertrag deckt dort den Kapitaldienst nicht. Ein Kreditprüfer fragt genau danach („Kapitaldienstfähigkeit bei Prolongation“).
   Verschärfend wirkt NF-07. „Tilgungssatz bleibt“ ergibt im Beispiel aus R-5.9 die Anschlussrate 90.942 Euro, „Restlaufzeit bleibt“ 104.952 Euro. Für die Deckung ist die Voreinstellung damit nicht die strengste Regel (siehe Frage 9).
   *Vorschlag:* In R-11.12 kommt die kleinste Deckung über die Haltedauer ab dem ersten vollen Vermietungsjahr dazu, mit Planjahr, im Basis- und im Stressfall. Ebenso die Deckung im ersten Jahr nach dem Ende jeder Zinsbindung. Neue Meldungen: M-37 (Hinweis), wenn die Deckung in einem Jahr unter H-03 fällt; M-38 (Warnung), wenn sie unter 1 fällt, mit Nachschussbedarf. Gemischte Planjahre der Bauzeit (RF-12, Planjahr 2: 0,892) zählen nicht mit.

3. **[wichtig · belegt] R-5.12, `MA-026`: Ein Schalter verbindet zwei verschiedene Fragen. Seine andere Lesart für (b) ist nicht bankfähig.**
   Die andere Lesart lässt Ü in (a) und KD_Ü in (b) zugleich weg. Für (a) ist das eine echte Frage des Rangs: Ein Förderdarlehen im Nachrang zur Bank belegt deren Beleihungsraum nicht. Für (b) dagegen zählt jede Bank, die ich kenne, den gesamten Kapitaldienst, weil er aus demselben Reinertrag fließt (begründete Einschätzung).
   Gegenrechnung RF-12 gefördert mit der anderen Lesart:
   - Bankdarlehen 360.050 Euro.
   - Gesamtdeckung im ersten vollen Vermietungsjahr 0,881, in den Planjahren 3 bis 10 durchgehend unter 1,02 (0,881 bis 1,015).
   - Nachschussbedarf 87.934,88 Euro.

   Die Lesart erzeugt also eine Finanzierung, deren Kapitaldienst der Ertrag nicht trägt.
   *Vorschlag:* `MA-026` teilen. `MA-026a` regelt den Beleihungsraum: (a) über alle Darlehen oder nur über die vorrangigen und das eigene. Dazu kommt als Merkmal je Tranche „Rang vor oder nach dem Bankdarlehen“; ein übernommenes Darlehen ist vorrangig voreingestellt, das Förderdarlehen gleichrangig angerechnet, bis die Hausbank antwortet. `MA-026b` regelt die Deckung über alle Darlehen. Schaltet der Anwender sie trotzdem um, erscheint die Gesamtdeckung mit M-38. R-10.15 weist den Auslauf einmal für das Bankdarlehen mit den vorrangigen Darlehen aus und einmal für alle Darlehen.

4. **[wichtig · belegt] E-59, R-5.8, R-3.6, R-11.8: Das übernommene Darlehen ist unvollständig beschrieben und vom Zinsstress ausgenommen.**
   - R-5.8 verlangt den Anschlusszins übriger Darlehen als „Eingabe (E-59)“. E-59 nennt aber nur vier Werte (Restschuld, Zins, Tilgungssatz, Ende der Zinsbindung), und R-3.6 zählt vier.
   - Der Referenzrechner führt sechs Werte (`anschluss_zins`, `beitrag_satz`; `grobkalkulation.py`, Zeile 122). Nach dem Wortlaut müsste der Kern beim gebundenen Bestand mit Haltedauer über der Bindung M-24 melden.
   - Im Stressfall erhält nur das Bankdarlehen den Aufschlag auf den Anschlusszins (`grobkalkulation.py`, Zeile 367). R-11.8 sagt dazu nichts.

   Im gebundenen Bestand aus RF-11 ist der Sprung des übernommenen Darlehens von 0,5 % auf 3 % im Jahr 9 das größte Zinsänderungsrisiko: Die Deckung fällt im Basisfall von 1,512 auf 1,394, im Stressfall von 1,394 auf 1,287, ohne Stressaufschlag auf dieses Darlehen.
   *Vorschlag:* E-59 um den Anschlusszins ergänzen, Voreinstellung heutiger Zins des Bankdarlehens + H-05; der Beitragssatz entfällt oder wird ausdrücklich geführt. R-3.6 auf 27 Eingaben ändern. In R-11.8 festlegen, dass der Aufschlag auf jedes Darlehen mit marktabhängigem Anschluss wirkt; ausgenommen bleibt das Förderdarlehen, weil `MA-003` dort schon den ungünstigsten Satz ansetzt.

5. **[wichtig · belegt] R-5.16, NF-10 und vorgeschlagene Modellannahme „Vorfälligkeitsentschädigung“: Die Restbindung wird nicht gesetzlich gekappt, und das Gewicht „gering“ ist zu niedrig.**
   `BGB-489` Abs. 1 Nr. 2 (am Original gelesen am 2026-11-18, gesetze-im-internet.de, Fassung vom Lesetag) gibt dem Darlehensnehmer „in jedem Fall nach Ablauf von zehn Jahren nach dem vollständigen Empfang“ ein Kündigungsrecht mit sechs Monaten Frist. Danach fällt keine Entschädigung mehr an.
   E-46 lässt eine Zinsbindung bis 40 Jahre zu. Bei 20 Jahren Bindung und Verkauf nach 5 Jahren setzt R-5.16 15 Jahre Restbindung an; rechtlich trägt das Darlehen höchstens rund 5,5 Jahre Entschädigung. Die Pauschale ist damit etwa 2,7-mal zu hoch.
   Die Rechtsgrundlage der Entschädigung beim Verkauf ist `BGB-490` Abs. 2: Kündigung bei berechtigtem Interesse, ausdrücklich bei „anderweitiger Verwertung“ des beliehenen Objekts (am Original gelesen am selben Tag). Beide Paragrafen fehlen im Kataster; Kapitel 17 nennt die Lücke.
   Zum Gewicht: In RF-08 beträgt die Entschädigung 31.208,57 Euro und mindert den Endwert nach Steuern um 21.846 Euro (3,7 %); in RF-14 sind es 126.170,42 Euro. Der tatsächliche Zinsschaden hängt vom Zinsniveau beim Verkauf ab und kann null sein oder über der Pauschale liegen.
   *Vorschlag:* Restbindung = min(Bindungsende; 10 Jahre nach Vollauszahlung + 6 Monate) − N. `BGB-489` und `BGB-490` ins Kataster aufnehmen. Gewicht der Annahme mittel; als andere Lesart die Zinsschadenrechnung nennen, mit dem Hinweis, dass sie bei gestiegenen Zinsen gegen null geht.

6. **[wichtig · belegt (Rechnung), Satz als Annahme] R-5.10, R-11.3, R-15.6: In 1a fehlen Bereitstellungszinsen ganz. Benannt ist das nur als Thema für Teil 2, nicht als Vereinfachung mit Wirkung.**
   „Eigenkapital zuerst“ (NF-33) verlängert gerade die Zeit, in der das zugesagte Bankdarlehen nicht abgerufen ist. RF-12 frei finanziert: 4.781.894,99 Euro, abgerufen von Monat 7 bis 18.
   Mit angenommenen 0,25 % je Monat auf den nicht abgerufenen Betrag (marktüblich nach meiner Einschätzung, weder im Kataster noch im Katalog) ergeben sich:
   - 152.800 Euro ohne bereitstellungsfreie Zeit,
   - 81.071 Euro bei 6 Monaten,
   - 21.992 Euro bei 12 Monaten.

   Zum Vergleich: Die Zinsen der Bauzeit betragen 83.180,59 Euro. Das nötige Eigenkapital ist damit um bis zu 3,7 % zu niedrig.
   *Vorschlag:* Vorgaben H-25 „Bereitstellungszins je Monat“ und H-26 „bereitstellungsfreie Zeit“, gerechnet auf Zusage minus Auszahlungen bis zum Vorperiodenende, Finanzierungskosten wie Bauzeitzinsen. Der Mittelabruf ist schon monatlich, der Aufwand also klein. Andernfalls eine Modellannahme „keine Bereitstellungszinsen in 1a“ mit Gewicht mittel und einem Hinweis auf dem Blatt beim Neubau.

7. **[wichtig · belegt] R-5.12 (b) mit R-6.3 und R-6.12: Der Reinertrag der Deckung ist kein nachhaltiger Ertrag im Sinne der Bank.**
   (a) Beim Ankauf zählt die Ist-Miete des Jahres 1, auch wenn sie über der Marktmiete liegt (R-6.3 lässt das zu). Gegenrechnung RF-11 mit Ist-Miete 10,00 statt 8,50 Euro bei 9,20 Euro Marktmiete: B 1.754.445 statt 1.581.965 Euro, wenn die Marktmiete angesetzt wird (+172.480 Euro, +10,9 %).
   (b) Die Bewirtschaftung folgt den Pauschalen des Vorhabens (H-17). Im Neubau aus RF-12 frei finanziert machen Bewirtschaftung und Mietausfall 13,06 % der Sollmiete aus. `BELWERTV-11` (im Kataster, am Original gelesen am 2026-11-18) setzt für den Beleihungswert mindestens 15 % des Rohertrags an. Mit 15 % sinkt das Bankdarlehen dort, wo (b) bindet, von 4.781.894,99 auf 4.675.000 Euro (−106.895 Euro).

   *Vorschlag:* als Lesart in `MA-026` (vorsichtig voreingestellt, umschaltbar). Miete in (b) = min(Ist; Marktmiete) je m². Bewirtschaftung in (b) = max(Kosten des Vorhabens; H-27 x Rohertrag), H-27 voreingestellt mit dem Wert aus `BELWERTV-11`. Für die Vorhabensrechnung selbst bleibt alles wie bisher.

8. **[wichtig · begründete Einschätzung] R-10.15: „Beleihungsauslauf“ ist für eine Bank der Bezug auf den Beleihungswert, hier steht der Kaufpreis im Nenner.**
   Ein Kreditprüfer liest 59,63 % (RF-11) als Auslauf auf den Beleihungswert. Dieser liegt nach BelWertV in der Regel unter dem Kaufpreis (`BELWERTV-4`, `BELWERTV-12` verwenden den Begriff in diesem Sinn), der tatsächliche Auslauf also höher. Die Ausnahme von der Vorsichtsregel ist in `MA-026` sauber begründet, nur der Kennzahlname auf dem Blatt verdeckt sie.
   Außerdem zeigt die Kennzahl nur den Stand zum Stichtag. Die Bank fragt beim Anschluss nach Restschuld zu Wert.
   *Vorschlag:* Umbenennen in „Darlehen zu Kaufpreis“ (Neubau: „zu Gesamtkosten“). „Beleihungsauslauf“ erst ab der Vollkalkulation mit Beleihungswert verwenden. Zusätzlich die Restschuld aller Darlehen am Ende der Zinsbindung zum Verkaufspreis nach R-8.1 in diesem Jahr ausweisen; das kostet nur eine Bewertung mehr.

9. **[Hinweis · belegt] R-10.14, R-11.12: Kennzahlen, die eine Bankvorlage braucht und die der Kern schon in 1a liefern kann, sind nicht definiert.**
   Im Dokument fehlen (Suche nach „Zinsdeckung“ ohne Treffer):
   - die Zinsdeckung: Reinertrag / (Zinsen + laufende Beiträge), je Planjahr;
   - die Kapitaldienstreserve in Euro: Reinertrag − H-03 x Kapitaldienst;
   - die Break-even-Miete oder der Break-even-Leerstand bei Deckung 1,0;
   - der Kapitaldienst je Darlehen im ersten vollen Jahr.

   Die Gremien- und Bankvorlage kommt erst mit 1b. Die Definitionen gehören aber in den Kern, damit 1a und 1b dieselben Zahlen zeigen.
   *Vorschlag:* als R-10.20 bis R-10.22 aufnehmen; die Break-even-Miete über die vorhandene Zielwertsuche (R-11.10) mit der Zielgröße Deckung.

10. **[Hinweis · belegt] R-11.14 mit M-21: Im geförderten Neubau sagt das Blatt nur „kein Bankdarlehen“. Die Bank wüsste gern, wie weit es fehlt.**
    Mit den Zahlen aus RF-12 sieht eine Bank den Fall so: Das NBank-Darlehen kostet 1/42 Tilgung (2,38 %) plus 0,5 % Beitrag, zusammen rund 2,9 % im Jahr. Das ist echter Kapitaldienst, der in die Kapitaldienstfähigkeit gehört.
    - Gesamtdeckung ohne Bankdarlehen: 1,0118.
    - Kapitaldienstreserve: 149.080,50 − 1,2 x 147.340,45 = −27.728 Euro.
    - Für die Restfinanzierung von 360.050 Euro wären 202.731 Euro Reinertrag nötig, also eine Eingangsmiete um 10,50 statt 8,20 Euro je m², die die Bindung nicht zulässt.

    Die Deckung steigt mit den Mietstufen auf 1,21 im Planjahr 11 und 1,51 im Planjahr 20. Die übliche Bankantwort darauf wäre ein Darlehen mit tilgungsfreien Anlaufjahren oder Eigenkapital, nicht null.
    *Vorschlag:* M-21 führt die Gesamtdeckung ohne Bankdarlehen, die Kapitaldienstreserve und den nötigen Reinertrag für die Restfinanzierung mit. Tilgungsfreie Anlaufjahre des Bankdarlehens sind in Teil 2 vorzumerken; R-5.10 kann sie schon heute über „Beginn der Tilgung“. Frage 6 an die Hausbank.

## Fragen an die Hausbank (für `MA-026`, Vorfälligkeit, Prolongation)

| Nr. | Frage | bisherige Voreinstellung des Werkzeugs |
|---|---|---|
| 1 | Bezieht die Bank ihre Beleihungsgrenze auf alle Darlehen oder nur auf vorrangige und das eigene? Welchen Rang verlangt die NBank für ihr Darlehen: Gleichrang, Nachrang, Rangrücktritt? | alle Darlehen, ohne Rang (`MA-026`) |
| 2 | Auf welchen Wert bezieht sich die Quote: Kaufpreis oder Gesamtkosten, Marktwert oder Beleihungswert? Mit welchem üblichen Abstand des Beleihungswerts zum Kaufpreis bei Wohnanlagen, und wie hoch ist die Quote auf diesen Wert? | Kaufpreis, beim Neubau Gesamtkosten ohne Bauzeitzinsen; Quote H-02 |
| 3 | Rechnet die Kapitaldienstfähigkeit mit dem Vertragszins oder mit einem kalkulatorischen Zins (Höhe, Regel) und einer kalkulatorischen Tilgung? Gilt das auch für übernommene Bestandsdarlehen mit niedrigem Zins und kurzer Restbindung? | heutiger Vertragszins und Tilgungssatz des Vorhabens; übernommene Darlehen mit ihrem Vertragszins (NF-09) |
| 4 | Welchen Ertrag setzt die Bank an: Vertragsmiete oder nachhaltige Miete? Mit eigenen Bewirtschaftungspauschalen und Mietausfallwagnis, etwa mindestens 15 % wie im Beleihungswert? | Ist-Miete des ersten Jahres nach Mietausfall H-15, Kosten nach H-17 |
| 5 | Wird die Deckung über den Kapitaldienst aller Darlehen gerechnet, mit welcher Mindestdeckung, und nur im ersten Jahr oder auch über die Laufzeit und beim Anschluss? Gibt es zusätzlich eine Auflage zur Zinsdeckung? | alle Darlehen, erstes Jahr der Vollvermietung, Mindestdeckung H-03; keine Zinsdeckung |
| 6 | Finanziert die Bank neben einem zinslosen NBank-Darlehen (42 Jahre, Beitrag 0,5 %) eine Restfinanzierung, wenn die Gesamtdeckung im ersten Jahr bei etwa 1,0 liegt und mit den gebundenen Mietstufen steigt? Bietet sie dafür tilgungsfreie Anlaufjahre an? | kein Bankdarlehen (M-21), Rest aus Eigenkapital |
| 7 | Welche Bereitstellungszinsen gelten (Satz je Monat, bereitstellungsfreie Zeit)? Zahlt die Bank nach Baufortschritt aus, und verlangt sie, dass das Eigenkapital zuerst eingesetzt wird? | keine Bereitstellungszinsen; Eigenkapital zuerst; gleichmäßiger Abruf (NF-33) |
| 8 | Wie berechnet die Bank die Vorfälligkeitsentschädigung beim Verkauf, und welche Größenordnung je Jahr Restbindung ist bei heutigem Zinsniveau üblich? Rechnet sie bei Bindungen über zehn Jahre nur bis zum Kündigungsrecht nach § 489 BGB? | Pauschale H-18 x Restschuld x Restbindung, ohne Kappung (NF-10) |
| 9 | Wie wird nach der Zinsbindung prolongiert: anfänglicher Tilgungssatz auf die Restschuld, Rate bleibt oder Restlaufzeit bleibt? Mit welchem Aufschlag gegenüber Neugeschäft, mit Forward-Möglichkeit, und prüft die Bank die Kapitaldienstfähigkeit beim Anschluss neu? | Tilgungssatz bleibt (NF-07); Anschlusszins heutiger Zins + H-05 |
| 10 | Rechnet die Bank Disagio oder Bearbeitungsentgelt auf das eigene Darlehen? | keines beim Bankdarlehen in 1a (R-5.14 nur für Fördermittel genutzt) |

## Nicht geprüft

- Kapitel 6 bis 9 und 12 sowie die Steuer, außer wo sie Reinertrag und Kapitaldienst berühren; Kapitel 14 nur zu M-21, M-22, M-24, M-25.
- Bankpraxis lässt sich nicht an einer veröffentlichten Quelle prüfen. Kalkulatorischer Zins, Pauschalen, Rang und Bereitstellungszinssatz sind meine Einschätzung aus der Rolle und als solche gekennzeichnet; der Satz von 0,25 % je Monat in Befund 6 ist eine Annahme.
- Am Original gelesen habe ich nur `BGB-489` und `BGB-490` (gesetze-im-internet.de, 2026-11-18; beide fehlen im Kataster). `BELWERTV-11` habe ich aus dem Kataster übernommen und nicht neu gelesen.
- Konditionen der NBank (Laufzeit, Beitrag, Rang) habe ich nicht am Original geprüft; ich habe mit den Annahmen aus `annahmen.py` gerechnet.
- Rust-Code gibt es noch nicht.
- Eigene Rechnungen: Skripte `f1.py` bis `f4.py` unter `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/fs1-bank/`. Sie verwenden die Module des Referenzrechners unverändert; der Fall mit kalkulatorischem Zins legt nur eine Hülle um `bankdarlehen()`.
