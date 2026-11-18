Rolle: Fachexperte Immobilienökonomie
Prüfobjekt: `docs/fachspezifikation-rechenkern.md` nach der ersten Überarbeitung (Stand 2026-11-18). Vollständig gelesen: Kapitel 1 bis 11, 16, 17 und Anhang A. Kapitel 12 bis 15 nur, soweit Regeln dorthin verweisen. Dazu Spezifikation Kapitel 1 bis 4 und 8, `MA-035` und `MA-037`, die Katastereinträge der verwendeten Kennungen, mein Bericht aus Runde 1 und die Sichtung.

Gesamturteil: Mit Auflagen tragfähig. Alle zehn Befunde aus Runde 1 sind eingearbeitet, neun davon vollständig. Mietpfad, Wartefrist, Kappung, 15-%-Regel, Vorfälligkeit und Baupreissteigerung habe ich am Gesetzestext und mit zwei Mietpfaden von Hand nachgerechnet; sie stimmen auf vier Stellen. Offen bleiben drei Gruppen. (1) Die KfW-Tranche ist anders gebaut als das Programm: Laufzeitvarianten mit Annuität über die Restlaufzeit statt Tilgungssatz. (2) Die neue Fassung von § 5a CO2KostAufG wird nur zur Hälfte abgebildet. (3) Es gibt Setzungen ohne Modellannahme bzw. mit günstiger Voreinstellung: Vergleichsmiete im Neubau, Kennzeichen „Förderdarlehen“, Rückführung einer Übermiete. Dazu kommt ein Widerspruch zwischen R-6.3 und der Festlegungsliste.

Note: 8 von 10. Die 9 ist nicht erreicht. Es fehlt:
- **im Dokument:** Befunde 1 bis 6. Je eine Regel- oder Tabellenänderung, dazu der Referenzrechner. Neue Grundsatzfragen sind es nicht.
- **mit Arbeit am Kataster:** `KFW-297-298-MERKBLATT` um Laufzeitvarianten, Tilgungsform, Bereitstellungsprovision, Abruffrist und Vorfälligkeit ergänzen (Befund 1). `CO2KOSTAUFG-5A` um die hälftige Teilung der CO2-Kosten ergänzen (Befund 2).
- **von außen:** Hausbank oder KfW-Konditionenübersicht dazu, ab wann die tilgungsfreien Jahre zählen (Befund 1). Für die Note zwingend ist nur, dass die vorsichtige Lesart mit Kennung im Dokument steht.

## Befunde aus Runde 1

| Nr. R1 | Thema | Stand | Wo und wie | Rest |
|---|---|---|---|---|
| 1 | Mietpfad auf Vergleichsmiete, Wartefrist, Kappung gegen Miete drei Jahre zuvor | **behoben** | R-1.1 (Glossar), E-19, E-33, R-6.2, R-6.3, `MA-037`, KAT-08. Nachgerechnet, siehe unten | Widerspruch NF-12 gegen R-6.3, siehe Befund 4 |
| 2 | 15-%-Regel als Rechenregel | **behoben** | R-6.16, KAT-12, NF-46: Erhaltung und Modernisierung zusammen, netto, k ≤ Zeitraum, Schwelle auf Gebäudeanschaffungskosten. Beispiel RF-17 nachgerechnet | – |
| 3 | Vorfälligkeit höchstens bis zum Kündigungsrecht | **behoben** | R-5.16, KAT-13, `BGB-489` im Kataster. Restbindung = min(Bindungsende; t_voll + 126) − N. Beispiele 114, 66 und 0 Monate nachgerechnet; übernommenes Darlehen vorsichtig ab Stichtag | Voreinstellung „Förderdarlehen“ siehe Befund 3 |
| 4 | Baukosten ohne Preissteigerung | **behoben** | R-11.2: Rate_m mit f_m = (1 + H-14)^(m/12). Rate 1 = 7.540.000 / 18 x 1,03^(1/12) = 419.921,98 Euro nachgerechnet | – |
| 5 | Landeswerte HB, HH, SH, NRW | **Eingabe und Schlüssel tragen** (Werte bewusst offen) | E-03, E-04 (amtlicher Gemeindeschlüssel), R-3.5: Auflösung von KAT-01, KAT-04 (Hebesatz) und KAT-08 über Land und Gemeinde; Gültigkeitszeitraum je Katalogwert; Kapitel 16 „vor 1a-Abnahme“ | Teilgebiete einer Gemeinde, Fortgeltung der Verordnungen: Befund 10 |
| 6 | CO2-Kosten: Einstufung, Prognose, § 5a | **teilweise** | E-34 (Ausstoß aus der Heizkostenabrechnung), `MA-035` mit oberer Klassengrenze, H-29 als Preispfad: behoben | § 5a ist nur als „weitere Kosten je m²“ gefasst; die hälftige Teilung der CO2-Kosten fehlt (Befund 2) |
| 7 | Neubau: Kennwert 300/400, Stellplätze, Erstvermietung | **behoben** | E-25, H-30, R-11.2 (NF-54); E-27, R-6.15 (NF-45); H-28, R-6.7 (NF-42); dazu Bereitstellungszins R-5.18 | neue Lücken an der Nahtstelle: Befunde 6 und 7 |
| 8 | Instandhaltung nach Baualter | **behoben** | H-17 als Staffel, R-6.8. Stufenwechsel in RF-18 (Baujahr 1996) und RF-14 (Monat 283 und 403) nachgerechnet | – |
| 9 | Bezugsgrößen der Neubau-Kennzahlen, Symmetrie Ein- und Ausstieg | **behoben** | R-10.11: a_0 als abgezinste Investition der Investitionsphase; R-1.1 „Gesamtkosten“; R-10.13 „Anfangsrendite auf Gesamtkosten“; R-8.1 und R-10.13 mit derselben maßgeblichen Jahresmiete (RF-11: 12 x 11.220,00 x 0,985 = 132.620,40 Euro) | – |
| 10 | Begriffe | **behoben** | Glossar mit Nettokalt-, Ist-, Vergleichs-, Markt-, Neuvermietungs- und Sollmiete; H-11 „unbegrenzt“ als eigener Wert; „Darlehen zu Kaufpreis“; Erbbauzins mindert die maßgebliche Jahresmiete (R-6.11, R-8.1) | Bezeichnung bei abweichendem Wertansatz: Befund 8 |

## Was trägt (nachgeprüft, kein Befund)

**Mietpfad am Gesetz:**
- **Ziel und Kappung:** § 558 Abs. 1 und 3 BGB verlangen Erhöhung „bis zur ortsüblichen Vergleichsmiete“, Wartefrist 15 Monate und Kappung „innerhalb von drei Jahren“. R-6.3 setzt das richtig um:
  - Die Bedingung m − 1 ≥ t_letzte + w lässt zwischen zwei Erhöhungen genau 15 unveränderte Monate.
  - Die Kappung läuft gegen Miete_(m − 36).
- **Vorsichtige Lesart von `MA-037`:** Sie ist die ungünstigste mögliche. Hat die letzte Erhöhung die Kappung ausgeschöpft, ist M_alt = Ist / (1 + κ), und vor dem Monat 37 besteht kein Spielraum.
- **„Planjahr 1 trägt immer die Ist-Miete“:** fachlich richtig und vorsichtig. Der Erwerber tritt erst mit dem Eigentum in das Mietverhältnis ein (§ 566 Abs. 1 BGB). Die erhöhte Miete schuldet der Mieter erst ab dem dritten Kalendermonat nach Zugang des Verlangens (§ 558b Abs. 1 BGB). Zwölf Monate liegen am sicheren Rand.
- **Neuvermietung:** Höchstens Vergleichsmiete x 1,10 nach § 556d Abs. 1 BGB. Die Vormiete (§ 556e) und die Ausnahmen (§ 556f) außer Ansatz zu lassen ist vorsichtig. RF-18 nachgerechnet: min(10,50; 9,20 x 1,10) = 10,12 Euro; 200 m² leer: 9.520,00 und 11.544,00 Euro.
- **Fluktuation:** Voreinstellung null ist vorsichtig. Der Wechselleerstand steckt in H-15. RF-18, Jahr 2: 0,95 x 8,50 + 0,05 x 10,3224 = 8,5911 Euro.
- **Gebundene Miete und Übergang:** Wartefrist ab dem letzten Bindungsschritt, Kappung gegen die gebundene Miete drei Jahre zuvor. Das entspricht § 558 Abs. 3. Die Ausnahme nach § 558 Abs. 4 (erloschene Fehlbelegungsabgabe) betrifft die Länder des Hauses praktisch nicht.

**Zwei Mietpfade von Hand nachgerechnet** (Vergleichsmiete 9,20 x 1,02^(j−1), κ = 15 %, w = 15, T = 36, d = 4):
- **RF-11, frei, vorsichtige Lesart:**

  | Monat | Ziel | Kappung | neue Miete |
  |---|---|---|---|
  | 37 | 8,50 + 1,2631 x 3/4 = 9,4473 | 8,50 x 1,15 = 9,7750 | 9,4473 |
  | 52 | 9,9584 | Miete_16 = 8,50 → 9,7750 | 9,7750 |
  | 67 bis 72 | – | Miete_31 bis Miete_36 = 8,50 | kein Spielraum |
  | 73 | 10,3607 | Miete_37 x 1,15 = 10,8644 | 10,3607 |
  | 88 | 10,5679 | Miete_52 x 1,15 = 11,2413 | 10,5679 |
  | 103 | 10,7793 | – | 10,7793 |
  | 118 | 10,9949 | 11,9148 | 10,9949 |
  | 133 | 11,4390 | – | 11,4390 |

  Alle sieben Stufen stimmen mit R-6.3 überein.
- **RF-11, gebundener Bestand** (40 % zu 6,80 Euro bis Ende Jahr 6): Stufe 1 ab Jahr 4 auf 6,80 x 1,0615 = 7,2182 Euro, Jahr 7 noch gebunden. Danach:

  | Monat | Ziel | Kappung | neue Miete |
  |---|---|---|---|
  | 85 | 7,2182 + (10,5679 − 7,2182)/4 = 8,0556 | 7,2182 x 1,15 = 8,3009 | 8,0556 |
  | 100 | 8,9987 | gebunden 8,3009 | 8,3009 |
  | 115 | – | Miete_79 = 7,2182 | keine Erhöhung |
  | 121 | – | Miete_85 x 1,15 = 9,2639 | 9,2640 |
  | 136 | – | Miete_100 x 1,15 = 9,5460 | 9,5461 |

  Stimmt mit R-6.6 überein.

**Weitere Regeln:**
- **15-%-Regel (R-6.16):** Sie trifft § 6 Abs. 1 Nr. 1a EStG (Runde 1 am Original gelesen). 424.360 / 1,19 = 356.605,04 > 297.000 Euro; Abschreibung Jahr 3: 39.600,00 + 8.487,20 Euro. Dass Erweiterungen (Satz 2, § 255 Abs. 2 HGB) im Kennzeichen „Modernisierung“ mitzählen, ist vorsichtig und in 1a hinnehmbar.
- **Vorfälligkeit (R-5.16):** Sie trifft § 489 Abs. 1 Nr. 2 BGB (heute erneut gelesen). Das KfW-Darlehen trägt zu Recht Vorfälligkeit: Das Merkblatt erlaubt außerplanmäßige Tilgung „nur gegen Zahlung einer Vorfälligkeitsentschädigung“, und nur die vollständige.
- **Verkaufsfaktor nach Leerstand (R-8.1):** Ein- und Ausstieg messen dieselbe Größe. Der Faktor auf die Miete nach strukturellem Leerstand ist eher vorsichtig, wenn der Anwender einen Marktfaktor auf die Ist-Nettokaltmiete einträgt. Die Trennung von Leerstand (wirkt auf den Preis) und Forderungsausfall (nur Zahlung) ist fachlich richtig, und die Summe bleibt die Voreinstellung nach `IIBV-29`.
- **Instandhaltung (R-6.8):** Stufen „unter 22, ab 22, ab 32 Jahren“ wie `IIBV-28`. Beim Neubau „volle Jahre seit Bezug“: RF-14, Monat 283 = Bezug 19 + 264.
- **Neubau-Grobform:**
  - Gesamtkosten ohne Bauzeitzinsen als Wertansatz, Eigenkapital zuerst, Bereitstellungszins 0,25 % je Monat nach freier Zeit: alles bankübliche Größenordnung.
  - Zuschläge 5 % (KG 200, 500, 600) und 20 % (KG 700) liegen im üblichen Rahmen.
  - Stellplätze getrennt mit Kennwert „BGF ohne Garage“.
  - Anlaufleerstand und Vollvermietungsjahr ab dem ersten Vermietungsmonat.
- **„Das KfW-Darlehen belegt den Beleihungsraum immer“:** fachlich richtig und vorsichtig. Das Merkblatt 297/298 lässt den Kredit nur über Finanzierungspartner laufen; die Hausbank trägt das Risiko und sichert ihn in aller Regel in derselben Grundschuld. Eine Modellannahme braucht es dafür nicht.
- **Kennzahlen:**
  - „Darlehen zu Kaufpreis“ beziehungsweise „zu Gesamtkosten“ (RF-12: 4.007.142,85 / 9.015.152,34 = 44,45 %).
  - Gesamtkapitalrendite mit der Investition der Investitionsphase als a_0.
  - Zinsdeckung (103.035,24 / 48.609,62 = 2,1196), Kapitaldienstreserve (103.035,24 − 1,2 x 73.596,60 = 14.719,32 Euro), Deckungsgrenzen (77,69 % und 23,86 %) und Kapitaldienst je Darlehen.

  Die Definitionen sind die bankübliche Fassung (ICR, Kapitaldienstreserve, Break-even-Mietausfall). Zur Bezeichnung siehe Befund 8, zu den Leerstandskosten Befund 9.

**Neue Festlegungen NF-39 bis NF-58:** Fachlich üblich und tragfähig sind NF-39, 40, 42, 43, 44, 45, 46, 52, 53, 54, 55 und 57. NF-41 ist zu ändern (Befund 1). NF-47 bis NF-51 und NF-56, NF-58 liegen außerhalb meiner Rolle (Steuer, Darstellung). Zur Setzungsliste in Kapitel 17:
- Nr. 3 trägt für Planjahr 1. Den Neubau zeigt Befund 5, die Fortgeltung von KAT-08 Befund 10.
- Nr. 4 trägt.
- Nr. 7 ist rechnerisch plausibel, ruht aber auf der KfW-Abbildung aus Befund 1.

## Befunde

1. [wichtig · belegt] **R-5.19, KAT-15, NF-41, A.4 (KAT-15), Spezifikation Kapitel 2 „Teilschritte“: Die KfW-Tranche entspricht nicht den Programmbedingungen.**
   - **Programmbedingungen** (`KFW-297-298-MERKBLATT`, Stand 07/2026, gültig ab 30.07.2026, heute am Original gelesen):
     - Abschnitt „Laufzeit und Zinsbindung“: Es gibt Laufzeitvarianten, nämlich endfällig bis 10 Jahre; bis 10 Jahre mit 1 bis 2 Tilgungsfreijahren; bis 25 Jahre mit 1 bis 3; bis 35 Jahre mit 1 bis 5. Die Zinsbindung läuft über die ganze Laufzeit oder 10 Jahre.
     - Abschnitt „Tilgung“: Nach den tilgungsfreien Jahren „wird der Kredit monatlich in Annuitäten zurückgezahlt“. Das ist eine Laufzeitannuität über die Restlaufzeit.
     - Einen Tilgungssatz kennt das Programm nicht. Der Kern rechnet dagegen eine Prozentannuität mit „Tilgungssatz aus KAT-15“.
   - **Gegenrechnung** (3.000.000 Euro zu 2,5 %, RF-12): Kern 11.250,00 Euro je Monat. Nach Programm:

     | Variante (Laufzeit / Tilgungsfreijahre) | Monatsrate |
     |---|---|
     | 35 / 1 | 10.922,62 Euro |
     | 35 / 5 | 11.853,63 Euro |
     | 25 / 3 | 14.785,20 Euro |
     | 10 / 2 | 34.511,53 Euro |

     Kapitaldienst, Deckung nach R-10.14 und Restschuld am Ende der Zinsbindung (R-10.15) hängen an der Variante. Die Richtung ist je Variante verschieden, die Abweichung reicht bis zum Dreifachen.
   - **Zählbeginn der tilgungsfreien Jahre:** Der Kern zählt sie „ab dem Monat nach der Bauzeit“, die Zinsbindung „ab dem Stichtag“. Das Merkblatt bindet den Zins an den Tag der Zusage. Dass die Anlaufjahre erst nach der Bauzeit beginnen, steht dort nicht; das ist eine ungeklärte Lesart ohne Kennung. Sie ist die günstige: In RF-12 beginnt die Tilgung im Monat 31 statt im Monat 13, und die Deckung im ersten Vollvermietungsjahr zeigt nur drei Tilgungsraten (R-10.23: 90.000 Euro).
   - **Weiteres aus dem Merkblatt:**
     - Höchstbetrag 100.000 Euro je Wohneinheit, mit QNG 150.000 Euro. KAT-15 führt nur einen Wert.
     - Bereitstellungsprovision 0,15 % je Monat ab dem 13. Monat nach Zusage.
     - Abruffrist 12 Monate, verlängerbar um bis zu 24 Monate; E-26 lässt dagegen 60 Monate Bauzeit zu.
     - Im Kataster belegt `verwendet_fuer` nur den Höchstbetrag. Tilgungsfreie Jahre, Laufzeit und Zinsbindung stehen ohne Katasterbeleg in KAT-15.
   - **Vorschlag:**
     - KAT-15 als Liste der Laufzeitvarianten (Laufzeit, Spanne der Tilgungsfreijahre, Zinsbindung) und Höchstbetrag je Förderstufe führen; E-35 um die Auswahl von Variante und Förderstufe ergänzen.
     - Tilgung als Laufzeitannuität über Laufzeit minus Tilgungsfreijahre; R-5.4 kann das schon.
     - Zählbeginn als neue Modellannahme, vorsichtig ab dem Stichtag (Zusage), andere Lesart ab Bezugsfertigkeit, Frage an die Hausbank.
     - Meldung, wenn die Bauzeit die Abruffrist übersteigt. Die Bereitstellungsprovision rechnen (R-5.18 hat die Form) oder ihr Fehlen in NF-41 als günstige Ausnahme begründen.
     - Spezifikation Kapitel 2: „Tilgung“ durch „Laufzeitvariante“ ersetzen. Kataster ergänzen.

2. [wichtig · belegt] **R-6.9, R-6.8, KAT-09, `MA-035`: Die hälftige Teilung der CO2-Kosten nach § 5a CO2KostAufG fehlt; die „weiteren Kosten je m²“ sind kein Katalogwert.**
   - **Gesetzeslage** (§ 5a CO2KostAufG, heute am Original gelesen): Abs. 3 Nr. 2 lässt Vermieter und Mieter bei einer Heizung nach § 43 Abs. 1 GModG ab dem 1. Januar 2028 die CO2-Kosten jeweils hälftig tragen, „in Abweichung von § 5 Absatz 2“. Dazu kommen nach Nr. 1 die Gasnetzentgelte ab 2028 und nach Nr. 3 ab 2029 der Pflichtanteil des Brennstoffs, höchstens 30 %.
   - **Was der Kern rechnet:** immer das Stufenmodell nach § 5. § 5a erscheint nur als pauschaler Betrag je m² aus dem Katalog, in A.4 null.
   - **Szenario:** Ankauf mit 2026 eingebauter Gasheizung und 14 kg CO2 je m². Das Stufenmodell gibt einen kleinen Vermieteranteil; nach § 5a sind es ab 2028 50 % der CO2-Kosten und die halben Netzentgelte. Der Kern rechnet die Bewirtschaftung zu günstig, und zwar über die ganze Haltedauer.
   - Netzentgelte und Biobrennstoffkosten hängen am Verbrauch des Objekts und am Netzbetreiber. Ein landesweiter Katalogwert je m² ist dafür die falsche Form.
   - § 5b (Neubau mit solcher Heizung, Bauantrag ab dem 13.05.2026) ist mit „E-34 = 0“ still ausgeschlossen.
   - **Vorschlag:**
     - Eingabe „Heizung nach § 43 GModG, Einbaujahr“ (ja/nein).
     - Bei ja: Vermieteranteil der CO2-Kosten 50 % ab dem Kalenderjahr 2028 (Katalogwert mit Gültigkeit) und Netzentgelte und Biobrennstoffanteil als Eingabe in Euro je Jahr, mit H-13 indexiert.
     - Beim Neubau Energieträger abfragen und § 5b anwenden oder fossile Heizung in 1a ausdrücklich ausschließen (Meldung).
     - `CO2KOSTAUFG-5A` im Kataster um die CO2-Teilung ergänzen; dort fehlt sie in `verwendet_fuer`.

3. [wichtig · belegt] **E-59 (Voreinstellung „Förderdarlehen: ja“) und der Satz nach der Eingabetabelle in R-3.3: Die Voreinstellung ist die günstige, nicht die vorsichtige.**
   - **Wirkung von „Förderdarlehen = ja“:**
     - Das übernommene Darlehen geht in R-5.12 mit dem vertraglichen statt mit dem kalkulatorischen Kapitaldienst in KD_Ü ein. Das gibt mehr Bankdarlehen.
     - Nach R-5.16 fällt keine Vorfälligkeit an.
   - **Gegenrechnung:** RF-19 nennt selbst 33.080,71 Euro mit und 46.182,48 Euro ohne Kennzeichen.
   - Der Text sagt dagegen: „Die Voreinstellungen von E-59 sind die vorsichtigen.“ Ein frei finanziertes Bestandsdarlehen, das der Bearbeiter ohne Blick auf das Kennzeichen erfasst, wird so als Förderdarlehen gerechnet.
   - **Vorschlag:** Voreinstellung „nein“ oder Pflichtfeld ohne Voreinstellung; den Satz nach der Tabelle berichtigen.

4. [wichtig · belegt] **R-6.3 gegen NF-12 (Kapitel 17), Rückführung einer Übermiete ohne Modellannahme.**
   - **Widerspruch:** R-6.3 führt eine Ist-Miete über der Vergleichsmiete ab Planjahr 2 linear über d Jahre zurück. Beispiel 11,00 / 10,5960 / 10,2858 Euro, nachgerechnet: 11 + (9,384 − 11) x 1/4 = 10,596. Die Festlegungsliste sagt zu NF-12: „Miete über der Vergleichsmiete bleibt stehen, bis die Vergleichsmiete sie einholt.“ Das ist die andere Lesart.
   - **Fehlende Kennung:** Rechtlich sinkt die Miete eines laufenden Vertrags nicht. Die Rückführung ist eine Annahme über Mieterwechsel und Durchsetzbarkeit, also eine Modellannahme nach Spezifikation Kapitel 8, und sie steht ohne Kennung.
   - **Vorschlag:**
     - Kapitel 17 an R-6.3 angleichen. Die Rückführung ist die vorsichtige Lesart und sollte bleiben; die Bank rechnet ohnehin mit min(Miete; Vergleichsmiete).
     - Neue Modellannahme: Übermiete wird über d Jahre zurückgeführt; andere Lesart: sie bleibt stehen, bis die Vergleichsmiete sie einholt, und sinkt nur über die Fluktuation. Gewicht mittel, umschaltbar. Kennung an R-6.3, NF-12 und Spezifikation Kapitel 4.

5. [wichtig · begründete Einschätzung] **R-6.7, R-5.12 (Neubau): Die Vergleichsmiete des Neubaus ist die Erstvermietungsmiete mal Index, ohne Eingabe und ohne Modellannahme.**
   - Die Spezifikation (Kapitel 2, „Grobkalkulation“, fest) verlangt für die Bank den „kleineren Wert aus Miete und ortsüblicher Vergleichsmiete“. Im Neubau setzt R-6.7 beides gleich. Damit entfällt der Abschlag der Bank auf eine Erstvermietungsmiete über dem Mietspiegel ganz (RF-12: Rohertrag_n = 396.000 = 2.000 x 16,50 x 12).
   - Außerdem steigt die Miete nach dem Bezug alle 15 Monate mit dem Mietindex. § 558 erlaubt das nur bis zur Vergleichsmiete. Liegt die Neubaumiete über dem Mietspiegelwert, was im Neubau verbreitet ist (begründete Einschätzung), sind über Jahre keine Erhöhungen durchsetzbar.
   - Ob die Vergleichsmiete eines Neubaus der Erstvermietungsmiete entspricht, ist eine Annahme über den Markt, die sich als falsch herausstellen kann. Eine Kennung fehlt; Anhang A.6 führt keine Vergleichsmiete.
   - **Vorschlag:** E-19 auch beim Neubau (Mietspiegel, Neubauklasse), voreingestellt E-16, mit neuer Modellannahme „Vergleichsmiete des Neubaus gleich Erstvermietungsmiete“. Vorsichtige Lesart: ein Abschlag als Vorgabe des Hauses oder der Mietspiegelwert. Die Bank rechnet dann mit min(Miete; E-19).

6. [wichtig · begründete Einschätzung] **R-2.1, R-11.2, R-11.3 (Neubau): Zwischen Grundstückserwerb und Baubeginn gibt es keinen Vorlauf.**
   - Der Stichtag ist der Grundstückserwerb, und die erste Baurate fällt im Monat 1. Zwischen Erwerb und Baubeginn liegen in der Praxis Planung, Genehmigung und Vergabe, oft sechs bis achtzehn Monate (begründete Einschätzung).
   - Die Grobform rechnet diese Zeit nicht. Ohne sie fehlen:
     - die Baupreissteigerung des Vorlaufs: bei zwölf Monaten und 3 % rund 231.575 Euro auf die Baukosten von RF-12;
     - das im Grundstück gebundene Eigenkapital des Vorlaufs;
     - der spätere Mietbeginn.
   - Alle drei Wirkungen liegen auf der günstigen Seite und treffen das indikative Grundstücksgebot. Der Bearbeiter kann es nicht nachbilden: Setzt er den Stichtag auf den Baubeginn, fallen Grundstückszahlung und Preisstand von E-25 falsch.
   - **Vorschlag:** Eingabe „Vorlauf bis Baubeginn“ in Monaten, Voreinstellung als Vorgabe des Hauses. Die Bauzeit beginnt danach, f_m zählt ab dem Stichtag. Der Stressfall verlängert wahlweise den Vorlauf. Die Haltedauerprüfung (R-14.4) und KfW-Abruffrist (Befund 1) zählen mit.

7. [Hinweis · begründete Einschätzung] **R-1.1 „Gesamtkosten“, H-30, R-11.2: Die Abgrenzung des Zuschlags für die Kostengruppe 700 zu den Finanzierungskosten fehlt.**
   - Die Kostengruppe 700 der DIN 276 enthält nach meiner Kenntnis eine Untergruppe Finanzierungskosten (begründete Einschätzung; DIN nicht frei zugänglich, im Kataster nur sekundär).
   - Der Kern rechnet Bauzeitzinsen und Bereitstellungszinsen selbst und nimmt sie aus den Gesamtkosten heraus. Übernimmt das Haus für H-30 einen Erfahrungswert „KG 700 gesamt“, zählt die Finanzierung doppelt. Das wirkt vorsichtig, verzerrt aber Wertansatz und „Darlehen zu Gesamtkosten“.
   - **Vorschlag:** In R-1.1 und H-30 „Kostengruppe 700 ohne Finanzierungskosten“ schreiben.
   - Dazu in der Hilfe zu E-25: Veröffentlichte Kennwerte haben einen eigenen Kostenstand und Bundesdurchschnitt; sie sind auf den Stichtag und regional fortzuschreiben, bevor sie als „Preisstand des Stichtags“ eingetragen werden.

8. [Hinweis · belegt] **R-1.1, R-10.15 gegen Spezifikation Kapitel 2 „Kennzahlen“: Der Name „Darlehen zu Kaufpreis“ stimmt nicht bei abweichendem Wertansatz.**
   - Die Spezifikation (fest) definiert „das Verhältnis der Darlehen zum Kaufpreis“. R-1.1 und R-10.15 teilen durch den Wertansatz, und der ist mit E-61 überschreibbar.
   - Gibt der Bearbeiter 2,6 Mio. Euro Wertansatz bei 2,4 Mio. Euro Kaufpreis ein (RF-19), sinkt die Kennzahl und behält den Namen „zu Kaufpreis“.
   - **Vorschlag:** Nenner immer Kaufpreis beziehungsweise Gesamtkosten, wie in der Spezifikation; bei gesetztem E-61 zusätzlich „Darlehen zu Wertansatz“ ausweisen.

9. [Hinweis · begründete Einschätzung] **R-6.7, R-6.13, R-10.22: Die Betriebskosten leerer Flächen trägt niemand.**
   - Die Bewirtschaftung enthält nur nicht umlagefähige Betriebskosten. Während des Anlaufleerstands steht der Neubau ganz leer, und der Eigentümer trägt die umlagefähigen Betriebskosten selbst, etwa Grundsteuer, Versicherung und Grundversorgung der Heizung. Dasselbe gilt für eine leere Fläche nach E-31.
   - Für den strukturellen Leerstand deckt die Pauschale das ab (`IIBV-29` umfasst den Leerstand), für den ausdrücklich modellierten Leerstand nicht.
   - Die Kennzahl „Mietausfall bei Deckung 1“ (R-10.22) überschätzt deshalb die Reserve. Bankenübliche Break-even-Rechnungen setzen Leerstandskosten an.
   - Größenordnung RF-12: drei Monate x 2.000 m² x geschätzt 2,50 Euro je m², rund 15.000 Euro; klein, aber systematisch günstig.
   - **Vorschlag:** Umlagefähige Betriebskosten je m² als Vorgabe; sie fallen auf jede leere Fläche (Anlaufleerstand, E-31) an. In R-10.22 im Zähler die Leerstandskosten mitführen.

10. [Hinweis · belegt] **KAT-08 mit R-3.5 (Satz nach der Tabelle), R-6.7, E-04, Setzung Nr. 3: Die Fortgeltung der Gebietsverordnungen ist eine Annahme, und § 556f ist verkürzt.**
    - **Fortgeltung:** § 556d Abs. 2 BGB (heute gelesen) lässt Verordnungen „spätestens mit Ablauf des 31. Dezember 2029“ enden. § 558 Abs. 3 Satz 3 begrenzt Kappungsverordnungen auf höchstens fünf Jahre. Den Stand des Stichtags über zwölf oder 42 Jahre fortzuschreiben, ist eine Annahme über künftiges Landesrecht. Vorsichtig ist sie nur, wo am Stichtag eine Verordnung gilt; wo keine gilt, ist sie neutral. Sie gehört nach Kapitel 8 mit Kennung ins Verzeichnis.
    - **§ 556f Satz 1:** Er nimmt jede Wohnung aus, „die nach dem 1. Oktober 2014 erstmals genutzt und vermietet wird“, also auch jede spätere Neuvermietung. R-6.7 sagt nur „für die Erstvermietung“. Für die Fluktuation im Neubau ist offen, ob R-6.14 dort überhaupt gilt („Bestandsfläche“).
    - **Teilgebiete:** Beide Verordnungsermächtigungen erlauben „Teile einer Gemeinde“. E-04 als Gemeindeschlüssel reicht dafür nicht.
    - **Vorschlag:**
      - Modellannahme „Gebietsverordnungen gelten über die Haltedauer fort“.
      - R-6.7 und R-6.14 auf den Wortlaut von § 556f bringen.
      - KAT-08 um ein Kennzeichen „Teilgebiet“ mit Abfrage ergänzen.

## Am Original gelesen (2026-11-18)

Gesetze: gesetze-im-internet.de, per curl, ISO-8859-1. Die Fassungsangabe der Seiten habe ich nicht ausgewertet; die Inhalte stimmen mit den Katastereinträgen „Fassung 23.07.2026“ überein.

| Kennung | gelesen | Ergebnis |
|---|---|---|
| `BGB-558` | Abs. 1 bis 6 | wie Kataster. Bestätigt Wartefrist 15 Monate, Verlangen frühestens ein Jahr nach der letzten Erhöhung, Kappung 20 % bzw. 15 % in drei Jahren, Verordnung höchstens fünf Jahre, Drittmittel Abs. 5 |
| `BGB-556D` | Abs. 1 und 2 | Aufschlag 10 %; Verordnungen enden spätestens am 31.12.2029 |
| `BGB-556E` | Abs. 1 und 2 | Vormiete und Vormodernisierung |
| `BGB-556F` | – | dauerhafte Ausnahme für Wohnungen, die nach dem 01.10.2014 erstmals genutzt und vermietet werden; erste Vermietung nach umfassender Modernisierung |
| `BGB-489` | Abs. 1 Nr. 1 und 2 | wie Kataster |
| § 558b BGB | Abs. 1 | nicht im Kataster: erhöhte Miete ab Beginn des dritten Kalendermonats nach Zugang. Für die Begründung „Planjahr 1 mit Ist-Miete“ ins Kataster aufnehmen (etwa `BGB-558B`) |
| § 566 BGB | Abs. 1 | nicht im Kataster: Eintritt des Erwerbers mit dem Eigentum; Aufnahme wie zuvor (etwa `BGB-566`) |
| `CO2KOSTAUFG-5` | Abs. 1 bis 3 | wie Kataster |
| `CO2KOSTAUFG-5A` | Abs. 1 bis 4 | Abweichung: Das Kataster nennt in `verwendet_fuer` nur Netzentgelte, „CO2-Kosten ab 2028“ und Bio-Brennstoff. Dass die CO2-Kosten abweichend vom Stufenmodell hälftig geteilt werden (Abs. 3 Nr. 2), fehlt dort und im Dokument (Befund 2) |
| `CO2KOSTAUFG-5B` | – | wie Kataster |
| `KFW-297-298-MERKBLATT` | Seiten 4 bis 6, kfw.de | Stand 07/2026, gültig ab 30.07.2026, wie Kataster. Belegt die Laufzeitvarianten, Annuität monatlich nach den Tilgungsfreijahren, Höchstbeträge 100.000 / 150.000 Euro, Bereitstellungsprovision 0,15 % je Monat ab dem 13. Monat, Abruffrist 12 + 24 Monate, Vorfälligkeit nur bei vollständiger Rückzahlung. Kataster in `verwendet_fuer` ergänzen (Befund 1) |

## Nicht geprüft

- **Kapitel 7 (Steuer) und NF-47 bis NF-51:** Rolle Steuerberater.
- **Kapitel 12 bis 15 (Rundung, Proben, Randfälle, Referenzfälle):** nur so weit, wie Regeln dorthin verweisen; Rolle Finanzmathematiker, Controller, Grenzfälle. Den Referenzrechner habe ich nicht laufen lassen, nur die genannten Zahlen von Hand nachgerechnet.
- **NBank-Grobförderung (R-11.14, KAT-10):** nicht am Original `NBANK-RL-MIETWOHNRAUM-2026`.
- **DIN 276 und 277, gif-Kennzahlenkatalog:** nicht frei zugänglich. Befund 7 ist deshalb Einschätzung.
- **Landeswerte für HB, HH, SH, NRW:** bewusst nicht Teil dieser Runde.
- **KfW-Konditionenübersicht** (Zinssätze, ob die Laufzeit ab der Zusage zählt): Host laut Kataster gesperrt, nicht versucht.
- **Wahl der Tilgungsvariante beim KfW-Darlehen:** nicht entschieden, nur die Form des Programms belegt.
