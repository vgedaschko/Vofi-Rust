# Fachspezifikation Rechenkern, Teil 1: allgemeiner Kern und Grobkalkulation

**Zweck:** Legt fest, wie der Rechenkern rechnet – so genau, dass ein Entwickler ohne Rückfrage implementieren und ein Finanzmathematiker jede Zahl nachrechnen kann. Teil 1 deckt den allgemeinen Kern (Zeit, Finanzplan, Darlehen, Steuer in Kurzform, Restwert, Unterlassensalternative, Kennzahlen, Rundung, Kontrollsummen) und die Grobkalkulation des Teilschritts 1a ab.
**Leser:** Entwicklung, Fachautoren des Fachhandbuchs, Prüfer. Der Auftraggeber liest das Dokument nicht; was er entscheiden muss, steht in Kapitel 16 und geht von dort nach `TASKS.md`.
**Stand:** 2026-11-18 · Entwurf zur Prüfrunde
**Geltung:** Konkretisiert `docs/spezifikation.md`, Kapitel 3 (und die Zeilen „Kennzahlen“, „Zielrendite und Schwellen“ und „Grobkalkulation“ in Kapitel 2). Bei Widerspruch gilt die Spezifikation. Der Recherchebericht (`reports/VOFI Immobiliensoftware Marktrecherche.md`, Anhang A und D) ist abgenommen und wird nicht fortgeschrieben; für den Rechenkern löst ihn dieses Dokument ab.

## Wie dieses Dokument zu lesen ist

- **Jede Regel hat eine Nummer** (`R-4.3`). Code und Tests verweisen auf diese Nummer. Eine Regel steht an genau einem Ort; andere Stellen verweisen.
- **Jede Zahl kommt aus dem Referenzrechner** unter `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner/` (Python, nur Standardbibliothek). `python3 referenzfaelle.py` rechnet 15 Referenzfälle mit 529 Prüfungen und endet nur dann mit Rückgabewert 0, wenn alle in ihrer Toleranz liegen; `python3 beispielwerte.py` druckt die übrigen Beispielzahlen. Der Referenzrechner ist kein Produktcode, sondern der Beleg, dass die Regeln eindeutig und rechenbar sind.
- **Rechts-, Förder- und Normangaben** stehen nur als Kennung des Quellenkatasters (`docs/quellenkataster.md`), zum Beispiel `GEWSTG-11`. Steuersätze, Fördersätze und Fristen sind Katalogwerte und in diesem Dokument nie Festwerte. Wo ein Beispiel einen Satz braucht, steht „Annahme“ dabei; die angenommenen Werte stehen gesammelt in `annahmen.py` des Referenzrechners.
- **Modellannahmen** tragen ihre Kennung (`MA-012`) an jeder Stelle, an der sie wirken (`docs/modellannahmen.md`).
- **Neue Festlegung** heißt: Spezifikation und Bericht lassen den Punkt offen, dieses Dokument entscheidet ihn. Jede neue Festlegung hat einen Satz Begründung und steht noch einmal in Kapitel 17.
- **Vorgaben des Hauses** (Zielrendite, Beleihungsquote und weitere) gibt der Auftraggeber frei. Alle Werte in den Beispielen sind Annahmen und keine Vorschläge.

Kennungen in diesem Dokument: `R-` Regel · `E-` Eingabe des Anwenders · `H-` Vorgabe des Hauses · `KAT-` Katalogwert · `P-` Kontrollsumme oder Probe · `M-` Meldung · `RF-` Referenzfall · `NF-` neue Festlegung.

## 1 Begriffe und Schreibweise

**R-1.1 Begriffe.** Das Werkzeug verwendet die Begriffe der linken Spalte. Die Lehrbuchbegriffe (`SCHULTE-IMMOBILIENINVESTITION-2025`) stehen im Fachhandbuch und in der Lehrbuchansicht (R-4.7).

| Begriff im Werkzeug | Lehrbuchbegriff | Bedeutung |
|---|---|---|
| Finanzplan | Vollständiger Finanzplan (VOFI) | Tabelle aller Zahlungen eines Vorhabens je Periode; jede Periode ist ausgeglichen |
| Endwert | Endvermögen | Guthaben abzüglich Kontokorrent am Ende des Planungszeitraums, nach Verkauf, Ablösung aller Darlehen und Steuern |
| Endwertdifferenz | Vermögensendwert | Endwert der Investition abzüglich Endwert der Unterlassensalternative |
| Unterlassensalternative | Unterlassungsalternative, Finanzinvestition | Anlage derselben Eigenkapitalbeträge am Kapitalmarkt statt in das Vorhaben |
| originäre Zahlung | direkte Zahlung | Zahlung des Objekts ohne Finanzierung und Steuern: Kauf, Bau, Miete, Bewirtschaftung, Maßnahmen, Zuschuss, Verkauf |
| derivative Zahlung | indirekte Zahlung | Zahlung aus Finanzierung, Geldanlage und Steuern |
| Geldanlage | Reinvestition | kurzfristige Anlage von Überschüssen |
| Kontokorrent | Zwischenfinanzierung | kurzfristiger Kredit für Fehlbeträge |
| Eigenkapital | Eigenmittel | Einlagen des Investors in das Vorhaben |
| Einlage, Entnahme, Nachschuss | – | Zahlung des Investors in das Vorhaben; Zahlung an den Investor; Einlage, die ein Fehlbetrag erzwingt (R-4.5) |
| VOFI-Rendite | VOFI-Eigenkapitalrentabilität | jährliche Rate, mit der das Eigenkapital auf den Endwert wächst (R-10.5) |
| Vergleichsrendite | VOFI-Rendite der Finanzinvestition | dieselbe Kennzahl für die Unterlassensalternative (R-10.8) |
| Reinertrag | Einnahmenüberschuss | Mieteinzahlungen nach Mietausfall abzüglich laufender Bewirtschaftung (R-6.12) |
| Restwert, Verkaufserlös | Veräußerungserlös | Erlös aus dem Verkauf am Ende der Haltedauer (Kapitel 8) |
| Zielrendite | – | Vorgabe des Hauses für die VOFI-Rendite nach Steuern, effektiver Jahreszins |
| Wertansatz | – | Wert, auf den die Bank ihre Beleihungsquote bezieht (R-5.12) |
| Kapitaldienst | – | Zins, planmäßige Tilgung und laufende Beiträge der Darlehen |

**R-1.2 Vorzeichen.** Im Finanzplan sind Zuflüsse des Vorhabens positiv und Abflüsse negativ. Eingaben und Zwischengrößen (Kosten, Zinsen, Tilgung, Steuer) werden als positive Beträge geführt und in der Summe mit ihrem Vorzeichen eingesetzt; eine negative Steuer ist eine Erstattung. Bestände (Guthaben, Kontokorrent, Restschuld) sind nie negativ. Der Bestandssaldo ist Guthaben − Kontokorrent − Summe der Restschulden.

**R-1.3 Bezeichner.** Formeln stehen als Textformeln. `x` ist das Malzeichen, `^` die Potenz, `min` und `max` das kleinste und das größte Glied, `runde(...)` die Rundung nach Kapitel 12.

| Zeichen | Bedeutung |
|---|---|
| p | Perioden je Jahr: 12 im Monatsraster, 1 im Jahresmodus |
| n | Haltedauer in Jahren; N = p x n ist die Zahl der Perioden |
| u, t | Periode oder Zeitpunkt 0 … N; j ist das Planjahr 1 … n |
| EW, EW_U, ΔEW | Endwert der Investition, der Unterlassensalternative, Endwertdifferenz |
| e_u, a_u | Einlage und Entnahme der Periode u nach Saldierung (R-10.3) |
| h, a_L, k | kurzfristiger Habenzins, langfristiger Anlagezins, Kontokorrentzins (effektiv je Jahr) |
| i, τ | nominaler Jahreszins und anfänglicher Tilgungssatz eines Darlehens |
| s_op(j), s_Z(j) | Grenzsteuersatz auf operative Erträge und auf Zinserträge im Planjahr j (R-7.14) |
| w(t) | Aufzinsungsfaktor von Zeitpunkt t auf N (R-10.4) |
| Z, D | Zähler und Nenner der Renditeformel (R-10.5) |
| r, r_U, z | VOFI-Rendite, Vergleichsrendite, Zielrendite |
| L, W, β, μ, M | Bankdarlehen, Wertansatz, Beleihungsquote, Mindestdeckung, Mittelbedarf (R-5.12) |

## 2 Zeit

**R-2.1 Zeitachse.** Der Stichtag ist Zeitpunkt 0: beim Ankauf der Übergang von Nutzen und Lasten, beim Neubau der Erwerb des Grundstücks. Periode u reicht von Zeitpunkt u − 1 bis Zeitpunkt u. Zahlungen einer Periode stehen an ihrem Ende, also am Zeitpunkt u; Zahlungen zum Stichtag stehen am Zeitpunkt 0.

**R-2.2 Raster.** Der Kern rechnet im Monatsraster (p = 12). Der Jahresmodus (p = 1) rechnet dieselben Regeln mit einer Periode je Jahr und dient dem Vergleich mit Lehrbuchfällen; er ist auf jeder Ausgabe als Jahresmodus bezeichnet. Beide Raster liefern für dasselbe Vorhaben verschiedene Ergebnisse, weil Zahlungen und Zinsen im Monatsraster früher fallen.
*Beispiel (RF-06, RF-14):* Der Testfall endet im Jahresmodus mit 584.366,28 Euro und im Monatsraster mit 585.918,72 Euro. Der Ankauf aus RF-11 endet im Jahresmodus mit 2.364.073,31 Euro, im Monatsraster mit 2.374.377,18 Euro; die VOFI-Rendite beträgt 5,123 % gegen 5,162 %.

**R-2.3 Verdichtung.** Die Jahresdarstellung des Monatsrasters summiert Zahlungen je Planjahr und zeigt Bestände zum Jahresende; der Stichtag ist eine eigene Spalte. Die Probe P-09 gilt für Zahlungen, nicht für Bestände.
*Beispiel (Testfall im Monatsraster):* Monat 1 hat 4.583,33 Euro Miete, 2.333,33 Euro Zins und 1.166,67 Euro Tilgung. Das Jahr 1 zeigt 54.999,96 Euro Miete (zwölfmal 4.583,33), 27.740,46 Euro Zins, 14.259,54 Euro Tilgung, 118,75 Euro Habenzins, 2.933,46 Euro Steuer und zum Jahresende 10.185,25 Euro Guthaben und 685.740,46 Euro Restschuld.

**R-2.4 Planjahr und Haltedauer.** Ein Planjahr sind p Perioden ab dem Stichtag; Planjahr j umfasst die Perioden (j − 1) x p + 1 bis j x p. Die Haltedauer n ist eine ganze Zahl von Jahren; verkauft wird am Zeitpunkt N = p x n. **Neue Festlegung (NF-01):** Die Grobkalkulation kennt die Haltedauer nur in ganzen Jahren; das genügt für das indikative Gebot und macht die Haltedauertabelle (R-11.13) möglich. Unterjährige Stichtage und Rumpfjahre regelt Teil 2.

**R-2.5 Konventionen je Zahlungsart.** Die Tabelle legt für jede Zahlungsart fest, wann gezahlt wird, in welchem Takt verzinst wird, auf welche Periode sich der Eingabewert bezieht und in welchem Monat die Zahlung steuerlich wirkt. **Neue Festlegung (NF-02):** Alle laufenden Zahlungen, auch die Miete, stehen am Periodenende. Das ist die vorsichtige und einheitliche Lesart und entspricht dem Lehrbuch; die andere Lesart (Miete zu Monatsbeginn) hebt den Endwert des Testfalls nach der Gegenrechnung in Quellnotiz 09 um rund 346 Euro. Die Fälligkeit der Miete ist im Kataster nicht verzeichnet (Kapitel 17, Katasterlücken).

| Zahlungsart | Zahlungszeitpunkt | Verzinsungstakt und Jahressatz | Basisperiode des Eingabewerts, Index | steuerliche Wirkung |
|---|---|---|---|---|
| Kaufpreis, Erwerbsnebenkosten, Grundstück | Zeitpunkt 0 | – | Betrag zum Stichtag | aktiviert; Abschreibung nach R-7.3 |
| Baukosten (Neubau) | Ende jedes Monats der Bauzeit, gleichmäßig (R-11.3) | – | Preisstand des Stichtags; in 1a nicht indexiert | aktiviert |
| Miete | Periodenende | – | Ankauf: Eingabewert gilt für Planjahr 1. Neubau: für das erste Vermietungsjahr. Index jährlich zu Jahresbeginn (R-6.1) | Planjahr der Zahlung |
| Bewirtschaftung, CO2-Kosten, Erbbauzins | Periodenende, je ein Zwölftel | – | Eingabewert gilt für Planjahr 1; Index jährlich nach Planjahr | Planjahr der Zahlung |
| Investitionsstau | letzter Monat des Jahres k; k = 0 zum Stichtag | – | Preisstand des Stichtags; Preisstand des Jahres k ist (1 + Baupreissteigerung)^k (R-6.10) | Erhaltung: Planjahr der Zahlung; Modernisierung: aktiviert |
| Darlehen: Zins, Tilgung, Beitrag | Periodenende | je Periode; nominaler Jahreszins geteilt durch p, auf die Restschuld der Vorperiode (R-5.2) | Zins der Zinsbindung, danach Anschlusszins (R-5.8) | Zins und Beitrag im Planjahr der Zahlung |
| Geldanlage, Kontokorrent | Zinsbuchung am Periodenende | je Periode; effektiver Jahreszins, konform umgerechnet (R-2.6), auf den Bestand der Vorperiode | – | Planjahr der Buchung |
| Unterlassensalternative | wie Geldanlage | wie Geldanlage (R-9.6) | – | Planjahr der Buchung |
| Zuschuss | mit dem Mittelabruf (R-11.3) | – | Betrag | mindert die Abschreibungsgrundlage (R-7.3) |
| Steuer | letzter Monat des Planjahres (R-2.7) | – | Satz des Kalenderjahres nach R-2.8 | – |
| Verkauf, Ablösung, Vorfälligkeit, Rückzahlung von Fördermitteln | Zeitpunkt N | – | Miete des Folgejahres (R-8.1) | letztes Planjahr |

**R-2.6 Nominale und effektive Jahressätze.** Darlehenszinsen sind nominale Jahressätze; der Periodenzins ist Restschuld x Jahreszins / p (R-5.3). Der Habenzins der Geldanlage, der Kontokorrentzins, die beiden Zinssätze der Unterlassensalternative und die Zielrendite sind effektive Jahressätze. Ein effektiver Jahressatz x wird konform umgerechnet: Periodensatz = (1 + x)^(1/p) − 1, auf zwölf Nachkommastellen gerundet (R-12.4). **Neue Festlegung (NF-03):** Die Spezifikation verlangt effektive Vergleichssätze; die konforme Umrechnung sorgt dafür, dass ein Guthaben im Monatsraster und im Jahresmodus denselben Jahresertrag bringt und die Unterlassensalternative vom Raster nicht abhängt. Darlehen folgen dem Vertrag und bleiben nominal; ihr Effektivzins wird ausgewiesen.
*Beispiel:* Aus 2 % effektiv wird der Monatssatz 0,001651581302, aus 8 % 0,006434030110. Ein Darlehen über 700.000 Euro zu nominal 4 % trägt im ersten Monat 2.333,33 Euro Zins; sein Effektivzins bei monatlicher Zahlung ist 4,0742 %. Die Unterlassensalternative des Testfalls endet im Jahresmodus mit 428.795,06 Euro und im Monatsraster mit 428.794,92 Euro; die 14 Cent stammen aus der Rundung der 120 Zinsbuchungen. Der Bericht (Anhang A.6) rechnete die Konten im Monatsraster mit einem Zwölftel des Jahressatzes; so gerechnet endet der Testfall mit 585.937,57 Euro statt 585.918,72 Euro (RF-06 führt beide Werte).

**R-2.7 Steuermonat.** Das Steuerjahr ist das Planjahr. Die Steuer eines Planjahres wird in seinem letzten Monat berechnet und gezahlt; eine Erstattung fließt im selben Monat. Vorauszahlungen und Abschlusszahlungen gibt es in der Kurzform nicht. **Neue Festlegung (NF-04)**, zusammen mit R-2.8: Das entspricht der sofortigen Besteuerung des Lehrbuchs und hält die Kurzform einfach; Kalenderjahr, Vorauszahlungen und Zahlungsverzug regelt die Steuer in Grundform (Teil 2).

**R-2.8 Kalenderjahr der Katalogsätze.** Planjahr j erhält die Sätze des Kalenderjahres Startjahr + j − 1; Startjahr ist das Kalenderjahr, in dem Planjahr 1 beginnt. Bei einem sinkenden Satz ist das die vorsichtige Zuordnung.
*Beispiel (RF-10, Annahme: Sätze nach `KSTG-23` und `SOLZG-4` im Stand des Berichts, Hebesatz 400 %):* Startjahr 2027. Planjahr 1 rechnet mit dem Satz für 2027, Planjahr 6 mit dem für 2032; 100.000 Euro Ergebnis kosten 29.825 Euro in Planjahr 1 und 24.550 Euro in Planjahr 6.

**R-2.9 Basisperiode der Indexierung.** Ein Eingabewert, der indexiert wird, gilt für das erste Jahr seiner Reihe und nicht für das Jahr davor. Indexstand im Jahr j ist Index_j = runde12(Index_(j−1) x (1 + Steigerung)) mit Index_1 = 1 (R-6.1). **Neue Festlegung (NF-05)** für die Zuordnung der Tabelle in R-2.5 (laufende Größen Planjahr 1, Maßnahmen Preisstand des Stichtags, Neubaumiete erstes Vermietungsjahr).
*Beispiel (RF-06):* Liest man den Reinertrag des Testfalls von 55.000 Euro als Wert des Vorjahres, steigt die Rendite von 7,876 % auf 8,028 % und der Endwert auf 588.484,91 Euro.

## 3 Eingaben

**R-3.1 Aufgelöster Rechenauftrag.** Der Rechenkern erhält einen vollständig aufgelösten Auftrag aus drei Quellen: Eingaben des Anwenders (`E-`), Vorgaben des Hauses (`H-`) und Katalogwerte (`KAT-`). Er liest selbst keinen Katalog und enthält keinen Satz, keine Schwelle und keine Frist als Festwert (`FAST-STANDARD`, `ICAEW-FMC`). Jeder Wert des Auftrags trägt Herkunft, bei Katalogwerten Kennung der Quelle und Stand, bei Annahmen die Kennung der Modellannahme. Eingaben, Rechnung und Ausgabe sind getrennt: Der Kern verändert keine Eingabe und gibt mit jedem Ergebnis den Auftrag, den Regelstand, die Version des Kerns und die Liste der Modellannahmen zurück, die gewirkt haben.

**R-3.2 Verschärfen und Lockern.** Vorgaben des Hauses sind im Vorhaben voreingestellt. Stresshöhen und Finanzierungsvorgaben (H-02 bis H-05, H-07) darf das Vorhaben nur verschärfen: niedrigere Beleihungsquote, höhere Mindestdeckung, höhere Tilgung, höherer Anschlussaufschlag, höhere Stresshöhen. Eine Lockerung, eine abweichende Zielrendite und ein Wertansatz der Bank über dem Kaufpreis, beim Neubau über den Gesamtkosten, brauchen eine Begründung als Text; der Kern rechnet damit und gibt die Meldung M-35 mit der Begründung für das Kennzahlenblatt zurück.

**R-3.3 Eingaben des Anwenders.** Geld in Euro mit zwei Nachkommastellen, Sätze als Prozent mit bis zu vier Nachkommastellen, Flächen in Quadratmetern mit zwei Nachkommastellen.

| Kennung | Eingabe | Einheit | zulässig | Voreinstellung | gilt für |
|---|---|---|---|---|---|
| E-01 | Vorhabensart | Auswahl | Ankauf Bestand, Neubau zur Vermietung | – | beide |
| E-02 | Stichtag | Monat, Jahr | ab dem laufenden Monat | Folgemonat | beide |
| E-10 | Kaufpreis | Euro | > 0 | – | Ankauf |
| E-11 | Erwerbsnebenkosten | % des Preises | 0 bis 20 | KAT-01 nach Land | beide |
| E-12 | Bodenanteil | % | 0 bis 100 | – | Ankauf |
| E-13 | Wohnfläche (`WOFLV-2`) | m² | > 0 | – | beide |
| E-14 | Zahl der Einheiten | Anzahl | ≥ 1 | – | beide |
| E-15 | Ist-Miete | Euro je m² und Monat | ≥ 0 | – | Ankauf |
| E-16 | Marktmiete; beim Neubau die Miete bei Bezug | Euro je m² und Monat | > 0 | – | beide |
| E-17 | Baujahr | Jahr | – | – | Ankauf |
| E-20 | Grundstückspreis | Euro | > 0 | – | Neubau |
| E-21 | Grundstücksfläche | m² | > 0 | – | Neubau |
| E-22 | Brutto-Grundfläche (`DIN-277`) | m² | > 0 | – | Neubau |
| E-25 | Kostenkennwert der Kostengruppen 200 bis 700 (`DIN-276`), brutto | Euro je m² Brutto-Grundfläche | > 0 | – | Neubau |
| E-26 | Bauzeit | Monate | 1 bis 60 | – | Neubau |
| E-28 | Mietenstufe | Auswahl | nach Katalog | – | Neubau mit Grobförderung |
| E-29 | Einkommensgruppe | Auswahl | nach Katalog | – | Neubau mit Grobförderung |
| E-30 | Bodenrichtwert | Euro je m² | > 0, Pflicht bei Förderung | – | Neubau mit Grobförderung |
| E-40 | Steuerstatus | Auswahl | R-7.1 | – | beide |
| E-41 | Kennzeichen erweiterte Grundstückskürzung (`GEWSTG-9`) | ja, nein | nur Status mit Gewerbesteuer | nein | beide |
| E-42 | Steuersatz des Investors einschließlich Zuschlagsteuern | % | 0 bis 60 | H-22 | Personen und Personengesellschaften |
| E-43 | Anteil natürlicher Personen am Gewinn | % | 0 bis 100 | 100 | gewerbliche Personengesellschaft |
| E-44 | Verlustverrechnung (`MA-016`) | Auswahl | Vortrag im Vorhaben, sofort | Vortrag | beide |
| E-45 | Zins des Bankdarlehens, nominal | % je Jahr | 0 bis 20 | – | beide |
| E-46 | Zinsbindung | Jahre | 1 bis 40 | KAT-02 | beide |
| E-47 | Verkaufsfaktor (Restwertfaktor) | Vielfaches der Jahresmiete | > 0 | – | beide |
| E-48 | Haltedauer | Jahre | 1 bis 42; beim Neubau mindestens Bauzeit plus ein Jahr (R-14.4) | H-19 | beide |
| E-50 | Investitionsstau | Euro oder Euro je m² | ≥ 0 | 0 | Ankauf |
| E-51 | Jahr der Ausführung | Jahr 0 bis n, oder später | ≥ 0 | 1 | Ankauf |
| E-52 | Kennzeichen Erhaltung oder Modernisierung | Auswahl | – | Erhaltung | Ankauf |
| E-53 | Anpassungsdauer der Ist-Miete an die Marktmiete | Jahre | 0 bis 20 | H-23 | Ankauf |
| E-54 | Effizienzklasse | Auswahl | nach Katalog | – | Ankauf |
| E-55 | Energieträger | Auswahl | nach Katalog | – | Ankauf |
| E-56 | gebundener Flächenanteil | % | 0 bis 100 | 0 | Ankauf |
| E-57 | Bindungsende | Jahr | nach dem Stichtag | – | Ankauf, gebunden |
| E-58 | gebundene Miete | Euro je m² und Monat | > 0 | Ist-Miete | Ankauf, gebunden |
| E-59 | übernommenes Darlehen: Restschuld, Zins, Tilgungssatz, Ende der Zinsbindung | Euro, %, %, Jahr | Restschuld ≤ Mittelbedarf | – | Ankauf, gebunden |
| E-60 | verfügbares Eigenkapital | Euro | ≥ 0 | leer | freiwillig |
| E-61 | Wertansatz der Bank mit Begründung | Euro | > 0 | Kaufpreis; Neubau: Gesamtkosten ohne Bauzeitzinsen | freiwillig |
| E-62 | Erbbauzins im ersten Jahr | Euro je Jahr | ≥ 0 | 0 | im Einzelfall |
| E-63 | Steigerung des Erbbauzinses | % je Jahr | −5 bis 15 | H-13 | im Einzelfall |
| E-64 | Tilgungssatz des Bankdarlehens | % je Jahr | ≥ H-04 | H-04 | beide |

**R-3.4 Vorgaben des Hauses.** Werte je Investorensicht und Nutzungsart aus dem Katalog; der Auftraggeber gibt sie frei (`TASKS.md`).

| Kennung | Vorgabe | Einheit | zulässig |
|---|---|---|---|
| H-01 | Zielrendite nach Steuern, effektiv | % je Jahr | > −100 |
| H-02 | Beleihungsquote | % des Wertansatzes | 0 bis 100 |
| H-03 | Mindestdeckung des Schuldendienstes | Verhältnis | ≥ 1 |
| H-04 | Mindesttilgung | % je Jahr | ≥ 0 |
| H-05 | Anschlusszins als Aufschlag auf den heutigen Zins | Prozentpunkte | ≥ 0 |
| H-06 | Stresshöhen, einzeln und kombiniert (R-11.8) | je Größe | ≥ 0 |
| H-07 | Regel für die Rate nach der Zinsbindung (R-5.9) | Auswahl | drei Regeln |
| H-08 | kurzfristiger Habenzins, effektiv | % je Jahr | ≥ 0 |
| H-09 | langfristiger Anlagezins der Unterlassensalternative, effektiv | % je Jahr | ≥ 0; Voreinstellung gleich H-08 |
| H-10 | Kontokorrentzins, effektiv | % je Jahr | ≥ H-08 |
| H-11 | Kontokorrentlinie | Euro | ≥ 0; Voreinstellung 0 |
| H-12 | Mietsteigerung | % je Jahr | −5 bis 15 |
| H-13 | Kostensteigerung | % je Jahr | −5 bis 15 |
| H-14 | Baupreissteigerung | % je Jahr | −5 bis 15 |
| H-15 | Mietausfallquote | % der Sollmiete | 0 bis 100 |
| H-16 | Verkaufskosten | % des Verkaufspreises | 0 bis 20 |
| H-17 | Bewirtschaftung: Verwaltung je Einheit, Instandhaltung je m², nicht umlagefähige Betriebskosten je m² und Jahr | Euro | ≥ 0 |
| H-18 | Vorfälligkeitssatz (R-5.16) | % der Restschuld je Jahr Restbindung | ≥ 0 |
| H-19 | Voreinstellung der Haltedauer | Jahre | 1 bis 42 |
| H-20 | Warnschwellen (Restwertanteil, Abstand der Faktoren) | je Kennzahl | – |
| H-21 | Suchbereiche und Raster der Zielwertsuche (R-11.10) | je Eingabe | – |
| H-22 | Voreinstellung des Steuersatzes der Personen; Satz auf Zinserträge | % | 0 bis 60 |
| H-23 | Voreinstellung der Anpassungsdauer | Jahre | 0 bis 20 |

Zu H-19: Das Lehrbuch empfiehlt einen Planungshorizont von zehn bis zwölf Jahren mit unterstelltem Verkauf, weil die Prognose mit der Entfernung ungenauer wird (`SCHULTE-IMMOBILIENINVESTITION-2025`). Zu H-17: Die Voreinstellungen stammen wahlweise aus `IIBV-26` und `IIBV-28` mit den Beträgen nach `IIBV-WERTE-2026`, aus `IMMOWERTV-ANLAGE-3` mit `IMMOWERTV-WERTE` oder sind eigene Werte des Hauses. Das Mietausfallwagnis dieser Regelwerke (`IIBV-29`) geht nicht als Kostenposition ein, sondern ist die Voreinstellung der Mietausfallquote H-15 (R-6.4).

**R-3.5 Katalogwerte.**

| Kennung | Katalogwert | Quelle |
|---|---|---|
| KAT-01 | Erwerbsnebenkosten je Land: Grunderwerbsteuer, Notar und Grundbuch, Makler | `GRESTG-11`, `NI-GREST-SATZ`; übrige Länder offen (`TASKS.md`) |
| KAT-02 | Voreinstellung der Zinsbindung | Vorgabe des Hauses |
| KAT-03 | Körperschaftsteuersatz je Kalenderjahr; Zuschlagsatz | `KSTG-23`, `SOLZG-4` |
| KAT-04 | Gewerbesteuer: Messzahl, Abrundung des Gewerbeertrags, Freibetrag, Hebesatz der Gemeinde | `GEWSTG-11`, `GEWSTG-16` |
| KAT-05 | Anrechnungsfaktor der Gewerbesteuer auf die Einkommensteuer | `ESTG-35` |
| KAT-06 | Frist des privaten Verkaufs | `ESTG-23` |
| KAT-07 | linearer Abschreibungssatz nach Baujahr oder Fertigstellung | `ESTG-7` |
| KAT-08 | Kappungsgrenze und ihr Zeitraum je Gemeinde | `BGB-558`, `NI-MIETERSCHUTZVO` |
| KAT-09 | CO2-Kosten des Vermieters je m² und Jahr nach Effizienzklasse und Energieträger, mit Steigerung | `CO2KOSTAUFG-5` bis `CO2KOSTAUFG-5D`, `CO2KOSTAUFG-ANLAGE` |
| KAT-10 | Grobförderung: Darlehens-, Zuschuss- und Eigenmittelquote nach Einkommensgruppe; Bemessungsgrenze; Eingangsmiete nach Mietenstufe; Steigerungsregel; Bindungsdauer; zinslose Zeit; Tilgungsdauer; Verwaltungskostenbeitrag; Entgelte | `NBANK-RL-MIETWOHNRAUM-2026`, `NBANK-PI-MIETWOHNUNGEN-MFH`; `MA-002`, `MA-003`, `MA-004`, `MA-005`, `MA-021` |
| KAT-11 | zulässige Steigerung gebundener Mieten bei übernommenen Bindungen | `NBANK-RL-MIETWOHNRAUM-2026` |

**R-3.6 Zahl der Eingaben.** Gezählt nach der Regel des Berichts (Anhang D.1; ohne Vorgaben des Hauses, ohne freiwillige Eingaben):

| Fall | Eingaben | Zahl |
|---|---|---|
| Ankauf | E-10 bis E-17 (8), E-40, E-41 oder E-42, E-45 bis E-48 (6) | 14 |
| Ankauf mit Pauschalen | dazu E-50 bis E-55 | 20 |
| Ankauf gebundener Bestände | dazu E-56, E-57 und die vier Werte von E-59 | 26 |
| Neubau | E-20 bis E-26, E-13, E-14, E-16 (8), dazu die sechs gemeinsamen | 14 |
| Neubau mit Grobförderung | dazu E-28 bis E-30 | 17 |
| gewerbliche Personengesellschaft, Einzelunternehmen mit Betriebsvermögen | je eine mehr (E-41 und E-42) | +1 |

Die 26 Eingaben beim Ankauf gebundener Bestände beantworten die offene Frage aus Prüfrunde 5 (`TASKS.md`); der Bericht nennt für diesen Fall keine Zahl.

**R-3.7 Eingabeprüfung.** Der Kern prüft den Auftrag vor der Rechnung gegen die zulässigen Bereiche. Eine Verletzung ist kein Programmfehler, sondern ein definiertes Ergebnis: Der Kern gibt eine Meldung mit Kennung und betroffener Eingabe zurück und keine Kennzahlen (Kapitel 14).

## 4 Aufbau des Finanzplans

**R-4.1 Konten und Zeilen.** Der Finanzplan führt je Periode die Zeilen der Tabelle. Bestände stehen am Periodenende.

| Block | Zeile | Inhalt |
|---|---|---|
| A originäre Zahlungen | Investition | Kaufpreis, Erwerbsnebenkosten, Grundstück, Baukosten, aktivierte Maßnahmen (−) |
| | Miete | Mieteinzahlung nach Mietausfall (+) |
| | Bewirtschaftung | laufende Kosten einschließlich CO2-Kosten und Erbbauzins (−) |
| | Erhaltung | Maßnahmen mit Kennzeichen Erhaltung (−) |
| | Zuschuss | Zuschüsse mit Geldfluss, brutto (+) |
| | Verkauf | Verkaufspreis abzüglich Verkaufskosten und ausstehendem Investitionsstau (+), nur in N |
| | Rückzahlung von Fördermitteln | (−), nur in N |
| B derivative Zahlungen | Eigenkapital | Einlage (+), Entnahme (−), Nachschuss (+) |
| | je Darlehen | Auszahlung (+), einbehaltener Betrag (−), Zins (−), Tilgung (−), laufender Beitrag (−), Ablösung (−) |
| | Vorfälligkeit | (−), nur in N |
| | einbehaltenes Entgelt auf Zuschüsse | (−) |
| | Geldanlage | Anlage (−), Auflösung (+), Habenzins (+) |
| | Kontokorrent | Aufnahme (+), Rückführung (−), Zins (−) |
| | Steuer | Zahlung (−) oder Erstattung (+) |
| Saldo | Finanzierungssaldo | Summe von A und B; in jeder Periode null (R-4.4) |
| C Bestände | Guthaben, Kontokorrent, Restschuld je Darlehen, Bestandssaldo | Bestandssaldo = Guthaben − Kontokorrent − Summe der Restschulden |
| Nebenrechnungen | Darlehenspläne, Abschreibungsplan, steuerliche Bemessung mit Verlustvortrag, Verkaufsrechnung, Unterlassensalternative | Kapitel 5, 7, 8, 9 |

**R-4.2 Kein Zirkelbezug.** Zinsen einer Periode hängen nur von Beständen am Ende der Vorperiode ab. Die Steuer hängt von Zahlungen und Zinsen der laufenden Periode ab, nicht vom Ausgleich. Der Ausgleich über Geldanlage und Kontokorrent wirkt erst auf die Zinsen der Folgeperiode. Damit lässt sich jede Periode in einem Durchgang rechnen (`SCHULTE-IMMOBILIENINVESTITION-2025`).

**R-4.3 Rechenreihenfolge je Periode.** Für u = 0 … N, in dieser Reihenfolge:

1. **Originäre Zahlungen** der Periode aus den Kapiteln 6 und 8 einstellen. In N kommen der Verkaufserlös nach R-8.5 und die Rückzahlung von Fördermitteln nach R-8.7 hinzu.
2. **Darlehen** nach Kapitel 5: Auszahlung und einbehaltener Betrag; ab u = 1 Zins und laufender Beitrag auf die Restschuld der Vorperiode; planmäßige Tilgung. In N wird nach der planmäßigen Rate jede Restschuld abgelöst (R-8.6). Für ein Darlehen mit freier Tilgung werden hier nur Zins und Beitrag gerechnet.
3. **Zinsen auf Bestände:** Habenzins = runde(Guthaben der Vorperiode x Periodensatz von h); Kontokorrentzins = runde(Kontokorrent der Vorperiode x Periodensatz von k). In u = 0 gibt es keine Zinsen.
4. **Vorfälligkeit** in N nach R-5.16.
5. **Steuerliche Nebenrechnung:** Das operative Ergebnis der Periode (R-7.2) und die Habenzinsen werden auf das Planjahr aufsummiert. Ist u das Ende eines Planjahres, wird die Jahressteuer nach Kapitel 7 berechnet und als Zahlung dieser Periode gebucht; in N gehört der Verkaufsgewinn dazu (R-7.4).
6. **Vorläufiger Saldo** = originäre Zahlungen + Auszahlungen der Darlehen − einbehaltene Beträge − Zins − Beitrag − Tilgung − Ablösung − Vorfälligkeit + Habenzins − Kontokorrentzins − Steuer.
7. **Freie Tilgung** (R-5.7): Tilgung = max(0, min(Restschuld, Guthaben − Kontokorrent der Vorperiode + vorläufiger Saldo + geplante Einlage − geplante Entnahme)). Der vorläufige Saldo sinkt um diese Tilgung.
8. **Eigenkapital:** geplante Einlagen und Entnahmen der Periode. Saldo = vorläufiger Saldo + Einlage − Entnahme.
9. **Ausgleich:** Netto = Guthaben − Kontokorrent der Vorperiode + Saldo. Ist Netto ≥ 0, ist das neue Guthaben Netto und der Kontokorrent null; sonst ist das Guthaben null und der Kontokorrent −Netto, höchstens die Linie (R-4.5). Anlage = Veränderung des Guthabens, Aufnahme = Veränderung des Kontokorrents.
10. **Bestände fortschreiben** und Kontrollsummen der Periode prüfen (Kapitel 13).

*Beispiel (RF-05, Testfall im Jahresmodus mit Rundung je Zahlung; Steuersatz 30 % als Annahme des Testfalls):*

| t | originär | Zins | Tilgung | Ablösung | Habenzins | Bemessung | Steuer | Anlage | Guthaben | Restschuld | Bestandssaldo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | −1.100.000,00 | – | – | – | – | – | – | 0,00 | 0,00 | 700.000,00 | −700.000,00 |
| 1 | 55.000,00 | 28.000,00 | 14.000,00 | – | 0,00 | 9.400,00 | 2.820,00 | 10.180,00 | 10.180,00 | 686.000,00 | −675.820,00 |
| 2 | 56.100,00 | 27.440,00 | 14.560,00 | – | 203,60 | 11.263,60 | 3.379,08 | 10.924,52 | 21.104,52 | 671.440,00 | −650.335,48 |
| 3 | 57.222,00 | 26.857,60 | 15.142,40 | – | 422,09 | 13.186,49 | 3.955,95 | 11.688,14 | 32.792,66 | 656.297,60 | −623.504,94 |
| 4 | 58.366,44 | 26.251,90 | 15.748,10 | – | 655,85 | 15.170,39 | 4.551,12 | 12.471,17 | 45.263,83 | 640.549,50 | −595.285,67 |
| 5 | 1.209.533,77 | 25.621,98 | 16.378,02 | 624.171,48 | 905,28 | 17.217,07 | 5.165,12 | 539.102,45 | 584.366,28 | 0,00 | 584.366,28 |

In t = 0 stehen den 1.100.000 Euro Investition 400.000 Euro Eigenkapital und 700.000 Euro Darlehen gegenüber. Jahr 2: Habenzins 2 % von 10.180,00 = 203,60; Bemessung 56.100,00 − 17.600,00 Abschreibung − 27.440,00 + 203,60 = 11.263,60; Steuer 3.379,08; Saldo 56.100,00 − 42.000,00 + 203,60 − 3.379,08 = 10.924,52.

**R-4.4 Finanzierungssaldo null.** In jeder Periode gilt: Saldo + Nachschuss − Anlage + Aufnahme = 0 (P-01). Der Finanzplan kennt keinen offenen Rest.

**R-4.5 Kontokorrentlinie und Nachschuss.** Übersteigt der Kontokorrent im Schritt 9 die Linie H-11, wird der übersteigende Betrag als Nachschuss gebucht: eine Einlage des Investors in derselben Periode. Der Nachschuss zählt als Einlage in der Renditeformel (R-10.3) und geht gespiegelt in die Unterlassensalternative ein (R-9.2). Ohne Linie (Lehrbuchfälle) ist der Kontokorrent unbegrenzt. **Neue Festlegung (NF-06):** Voreingestellt ist die Linie null, sodass jeder Fehlbetrag als Eigenkapitalbedarf sichtbar wird; ein Kontokorrent, den die Bank nicht zugesagt hat, würde den Eigenkapitalbedarf verdecken.
*Beispiel (RF-11):* Im Ankauf fällt im Jahr 2 der Investitionsstau von 127.308,00 Euro an. Das Guthaben reicht nicht; der Finanzplan bucht im Monat 24 einen Nachschuss von 91.529,75 Euro. *Beispiel (RF-06):* Im Testfall mit 380.000 Euro Eigenkapital und unbegrenztem Kontokorrent stehen 20.000,00 Euro Kontokorrent in t = 0, 10.940,00 in t = 1 und 770,64 in t = 2; der Endwert ist 561.526,16 Euro.

**R-4.6 Endwert.** Der Endwert ist der Bestandssaldo am Zeitpunkt N. Nach der Ablösung sind alle Restschulden null (P-02); der Endwert ist dann Guthaben − Kontokorrent. Er kann negativ sein (R-14.3).

**R-4.7 Lehrbuchansicht.** Im Jahresmodus lässt sich der Finanzplan in der Form des Lehrbuchs zeigen: Statt der Konten steht je Periode eine einjährige Reinvestition oder Zwischenfinanzierung, die in der Folgeperiode mit Zins zurückfließt. Die Ansicht ist eine andere Darstellung derselben Zahlen:

| Zeile der Lehrbuchansicht | aus dem Finanzplan |
|---|---|
| direkte Zahlungen (a_0, ü_t, R_n) | originäre Zahlungen |
| Eigenkapital | Einlage + Nachschuss − Entnahme |
| Kreditaufnahme | Auszahlung − einbehaltene Beträge |
| Zinsen Fremdkapital | −(Zins + Beitrag + Vorfälligkeit) |
| Tilgung | −(Tilgung + Ablösung) |
| Steuerzahlung | −Steuer |
| Reinvestition t | −Guthaben am Ende von t (für t < n) |
| Rückzahlung, Habenzinsen in t + 1 | Guthaben am Ende von t; Habenzins von t + 1 |
| Zwischenfinanzierung t | Kontokorrent am Ende von t (für t < n) |
| Rückzahlung, Sollzinsen in t + 1 | −Kontokorrent am Ende von t; −Kontokorrentzins von t + 1 |
| Endwert (Endvermögen) | Spaltensumme: null für t < n, Endwert für t = n |
| Kredit nach Tilgung | Restschuld |

*Beispiel (RF-03, Standardbeispiel mit Steuern, Tab. 5 des Lehrbuchs; ungerundet gerechnet, in ganzen Einheiten gezeigt):*

| t | direkte Zahlungen | Eigenkapital | Kredit | Zinsen | Tilgung | Steuer | Rückzahlung Zwischenfinanzierung | Sollzinsen | Zwischenfinanzierung | Saldo | Kredit nach Tilgung |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | −10.000 | 8.000 | 2.000 | – | – | – | – | – | – | 0 | 2.000 |
| 1 | 540 | – | – | −150 | −344 | −70 | – | – | 24 | 0 | 1.656 |
| 2 | 540 | – | – | −124 | −370 | −82 | −24 | −2 | 63 | 0 | 1.286 |
| 3 | 540 | – | – | −96 | −398 | −94 | −63 | −6 | 117 | 0 | 888 |
| 4 | 540 | – | – | −67 | −428 | −106 | −117 | −10 | 188 | 0 | 460 |
| 5 | 10.540 | – | – | −34 | −460 | −744 | −188 | −17 | – | 9.097 | 0 |

Der Referenzrechner trifft alle veröffentlichten Werte der Tabellen 3 bis 6 (RF-03).

## 5 Darlehen

**R-5.1 Tranche.** Jedes Darlehen ist eine Tranche mit eigenem Plan und eigener Restschuld. Merkmale: Nennbetrag; Tilgungsart (Prozentannuität, Laufzeitannuität, Ratentilgung, endfällig, freie Tilgung); nominaler Jahreszins; Tilgungssatz oder Laufzeit; Auszahlungsplan; einbehaltener Betrag; Beginn der Tilgung; Zinsbindung mit Anschlusszins und Anschlussregel; laufender Beitrag; Tilgungszuschuss; Rundungsart (`MA-013`); Kennzeichen „Bankdarlehen“ oder „übriges Darlehen“ für R-5.12. Die Grobkalkulation führt ein Bankdarlehen als Prozentannuität und höchstens zwei übrige Darlehen (übernommenes Darlehen, Förderdarlehen); der Kern selbst begrenzt die Zahl der Tranchen nicht.

**R-5.2 Zins.** Zins der Periode u = Restschuld am Ende von u − 1 x Jahreszins der Periode / p. Der Jahreszins ist nominal (R-2.6). Jede Periode zählt als ein p-tel Jahr; eine Zählung nach Kalendertagen gibt es in Teil 1 nicht.

**R-5.3 Rechenfolge und Rundung je Rate (`MA-013`).** Zins = runde(Restschuld x Jahreszins / p): erst multiplizieren, zuletzt teilen, dann auf Cent runden (R-12.5). Die Rate einer Annuität wird einmal gerundet und bleibt fest; Tilgung = Rate − Zins, ohne weitere Rundung. Voreingestellt ist kaufmännische Rundung; je Darlehen umstellbar auf Abschneiden oder auf keine Rundung, damit die Restschuld mit dem Kontoauszug der Bank übereinstimmt.
*Beispiel (RF-08):* 700.000 Euro zu 4 %, Monatsrate 3.500 Euro. Rate 1: Zins 2.333,33, Tilgung 1.166,67; Rate 2: Zins 2.329,44, Tilgung 1.170,56. Restschuld nach 120 Raten: 528.208,51 Euro bei kaufmännischer Rundung, 528.207,91 Euro bei Abschneiden, 528.208,56 Euro ohne Rundung.

**R-5.4 Annuität.** Prozentannuität (deutsche Bankpraxis): Rate = runde(Nennbetrag x (i + τ) / p), fest über die Zinsbindung. Laufzeitannuität (Lehrbuch): Rate = runde(K x i_p x q^m / (q^m − 1)) mit i_p = i / p, q = 1 + i_p und m Tilgungsperioden; die Potenz wird mit voller Rechengenauigkeit gebildet. Bei i = 0 ist die Rate K / m. In jeder Periode gilt Tilgung = min(Restschuld, max(0, Rate − Zins)); die letzte Rate einer Laufzeitannuität tilgt den Rest.
*Beispiel (RF-03, RF-04, RF-02):* 2.000 zu 7,5 % über fünf Jahre: Annuität 494; 21.869 zu 10 % über zehn Jahre: 3.559; 17.798,40 Euro zu 4 % über 25 Jahre: 1.139,31 Euro. Bei Zins null (R-14.1): 700.000 Euro über 20 Jahre, Rate 35.000,00 Euro.

**R-5.5 Ratentilgung.** Tilgung je Periode = runde(Nennbetrag / m); die letzte Rate tilgt den Rest. Zins nach R-5.2.
*Beispiel (RF-08):* 600.000 Euro zu 3 % über 20 Jahre im Jahresmodus: Tilgung 30.000,00; Zins 18.000,00 / 17.100,00 / 16.200,00; Restschuld nach fünf Jahren 450.000,00. 100.000 Euro in sieben Monatsraten: sechsmal 14.285,71, Schlussrate 14.285,74.

**R-5.6 Endfällig.** Keine laufende Tilgung; Zins nach R-5.2. Getilgt wird am Ende der Laufzeit oder mit der Ablösung in N.
*Beispiel (RF-08):* 500.000 Euro zu 3,5 %: Monatszins 1.458,33 Euro, Ablösung 500.000,00 Euro.

**R-5.7 Freie Tilgung.** Der ganze Überschuss der Periode tilgt (R-4.3, Schritt 7); der Rest wird in N abgelöst. Solange Restschuld besteht, bleibt das Guthaben null. Ein Finanzplan führt höchstens eine Tranche mit freier Tilgung. Die Tilgungsart stammt aus dem Lehrbuch und steht ab der Vollkalkulation zur Wahl; in der Grobkalkulation dient sie nur dem Referenzfall.
*Beispiel (RF-04):* Bürogebäude, Kredit 21.869 zu 10 %: Tilgung 1.010 / 1.060 / 1.113 in den Jahren 1 bis 3, Kreditstand 20.859 / 19.799 / 18.686, Rückzahlung im zehnten Jahr 10.737, Endvermögen 31.567. Die freie Tilgung ist die beste der drei Kreditvarianten des Lehrbuchs (endfällig 30.179, Annuität 31.400).

**R-5.8 Zinsbindung und Anschlusszins.** Die Zinsbindung zählt in Perioden ab dem Stichtag (**neue Festlegung NF-08**: früheres Ende ist die vorsichtige Lesart beim Neubau). Bis zu ihrem Ende gilt der vereinbarte Zins, danach der Anschlusszins. Für das Bankdarlehen ist der Anschlusszins der heutige Zins zuzüglich des Aufschlags H-05; für ein übriges Darlehen ist er Eingabe (E-59) oder Katalogwert (`MA-003` für das Förderdarlehen). Der heutige Zins wird nie still fortgeschrieben: Fehlt ein Anschlusszins, obwohl die Haltedauer über die Bindung hinausreicht, rechnet der Kern nicht und gibt M-24 zurück.

**R-5.9 Rate nach der Zinsbindung.** In der ersten Periode nach der Bindung wird die Rate einer Prozentannuität neu gesetzt. **Neue Festlegung (NF-07):** Voreingestellt ist „Tilgungssatz bleibt“: neue Rate = runde(Restschuld am Bindungsende x (Anschlusszins + Tilgungssatz der Anschlussfinanzierung) / p); der Tilgungssatz der Anschlussfinanzierung ist der anfängliche, mindestens H-04. Das ist die übliche Prolongation. Die beiden anderen Regeln sind über H-07 wählbar: „Rate bleibt“ (die bisherige Rate, mindestens der neue Zins) und „Restlaufzeit bleibt“ (Laufzeitannuität über die rechnerische Restlaufzeit ln((i + τ) / τ) / ln(1 + i / p) Perioden abzüglich der vergangenen). Ratentilgung und endfällige Darlehen ändern nur den Zins.
*Beispiel (RF-08, Jahresmodus, ungerundet):* 1.496.000 Euro zu 4 % und 2 %, Bindung zehn Jahre, danach 6 %. Rate ab Jahr 11: 90.942 Euro (Tilgungssatz bleibt), 89.760 Euro (Rate bleibt), 104.952 Euro (Restlaufzeit bleibt). Die Regel wirkt wenig auf den Endwert und stark auf die Schuldendienstdeckung. *Beispiel (RF-11):* Rate bis Monat 120: 7.155,22 Euro; Restschuld 1.079.843,92 Euro; Rate ab Monat 121 bei 5 % und 2 %: 6.299,09 Euro.

**R-5.10 Auszahlung und Beginn der Tilgung.** Ein Darlehen wird nach seinem Auszahlungsplan ausgezahlt (R-11.3). Bis zum Beginn der Tilgung fallen nur Zins und Beitrag auf den ausgezahlten Betrag an; beim Neubau beginnt die Tilgung im Monat nach der Bauzeit. Die Rate der Prozentannuität bezieht sich auf den Nennbetrag.
*Beispiel (RF-12):* Bankdarlehen 4.781.894,99 Euro, erste Auszahlung im Monat 7, Bauzeit 18 Monate. Zinsen der Bauzeit zusammen 83.180,59 Euro. Monat 19: Rate 23.909,47 Euro, davon Zins 15.939,65 und Tilgung 7.969,82.

**R-5.11 Übrige Darlehen.** Ein übernommenes Darlehen gilt als am Stichtag in Höhe seiner Restschuld ausgezahlt; der Kaufpreis steht in voller Höhe als Investition. Es läuft als Prozentannuität mit seinem Zins, seinem Tilgungssatz und seiner eigenen Zinsbindung weiter. Das Förderdarlehen der Grobförderung läuft als Ratentilgung über die Tilgungsdauer des Katalogs ab dem Monat nach der Bauzeit (`MA-002`), zinslos für die zinslose Zeit ab demselben Monat und danach zum Zins nach `MA-003`, mit laufendem Beitrag (R-5.13) und einbehaltenem Entgelt (R-5.14). **Neue Festlegung (NF-11):** Raten und Beiträge übriger Darlehen fallen im Takt des Rasters an, im Monatsraster also monatlich mit einem Zwölftel; `MA-002` nennt Jahresraten. Bei einem zinslosen Darlehen ändert das nur die Liquidität innerhalb des Jahres.
*Beispiel (RF-11):* Übernommenes Darlehen 500.000 Euro zu 0,5 % und 2 % Tilgung: Kapitaldienst im ersten Jahr 12.500,04 Euro. *Beispiel (RF-08, Jahresmodus; Werte nach Bericht Anhang C.1 als Annahme):* Förderdarlehen 2.320.000 Euro, Entgelt 1 % = 23.200,00 Euro einbehalten, Beitrag 0,5 % = 11.600,00 Euro im ersten Jahr, Rate 55.238,10 Euro; Restschuld nach 35 Jahren 386.666,50 Euro, ein Sechstel des Darlehens; Zins im 36. Jahr bei angenommenen 5 %: 19.333,33 Euro.

**R-5.12 Höhe des Bankdarlehens (`MA-026`).** Das Bankdarlehen ist der kleinste von drei Werten und nie negativ:

    L = max(0; abrunden_Cent(min(A; B; C)))

- **(a) Beleihungsquote:** A = β x W − Ü. W ist der Wertansatz: der Kaufpreis, beim Neubau die Gesamtkosten ohne Bauzeitzinsen (R-11.2), überschreibbar durch E-61. Ü ist die Summe der übrigen Darlehen.
- **(b) Mindestdeckung:** B ist das größte Darlehen, mit dem der Reinertrag im ersten Jahr der Vollvermietung den Kapitaldienst aller Darlehen mit der Mindestdeckung deckt: RE_VJ ≥ μ x (KD_Ü + p x runde(B x (i + τ) / p)). Geschlossen: B = (RE_VJ / μ − KD_Ü) / (i + τ), auf Cent abgerundet und um einzelne Cent gesenkt, bis die Ungleichung mit der gerundeten Rate gilt. KD_Ü ist der Kapitaldienst der übrigen Darlehen in zwölf Monaten ab Tilgungsbeginn (Zins, Tilgung, Beitrag). Gerechnet wird mit dem heutigen Zins i und dem Tilgungssatz τ des Vorhabens (E-64).
- **(c) Restfinanzierung:** C = M − Ü − Zuschüsse − Mindesteigenkapital. M ist der Mittelbedarf nach R-11.2. Ein Mindesteigenkapital gibt nur die Förderung vor (`MA-004`); sonst ist es null.

Das Eigenkapital ist der Ausgleichsposten: EK = M − Ü − Zuschüsse − L (P-04). Das Ergebnis nennt die bindende Grenze; bei Gleichstand alle gleichauf liegenden. Ist B ≤ 0, trägt der Reinertrag nach der Mindestdeckung kein Bankdarlehen, weil er schon für die übrigen Darlehen nicht reicht oder nicht positiv ist: L = 0 und Meldung M-21. Ist C < 0, übersteigen die übrigen Mittel den Bedarf: keine Rechnung, Meldung M-22 (R-14.7). Die andere Lesart von `MA-026` ist umschaltbar: Dann zählen Ü in (a) und KD_Ü in (b) nicht mit. **Neue Festlegung (NF-09)** sind die Rundung zur sicheren Seite und der Ansatz von heutigem Zins und Tilgungssatz in (b); eine Bank, die mit einem kalkulatorischen Zins rechnet, ergäbe ein kleineres Darlehen (Frage an die Hausbank, Kapitel 16).

*Beispiele (RF-09; Zins 4 %, Tilgung 2 %, Mindestdeckung 1,2 als Annahme; Werte des Berichts, Anhang D.4):*

| Fall | A | B | C | Bankdarlehen | bindet | Eigenkapital |
|---|---|---|---|---|---|---|
| Ankauf 2,6 Mio. Euro, Reinertrag 107.712 Euro, Quote 65 % | 1.690.000 | 1.496.000 | 2.782.000 | 1.496.000 | (b) | 1.286.000 |
| Ankauf 2,2 Mio. Euro, sonst gleich | 1.430.000 | 1.496.000 | 2.354.000 | 1.430.000 | (a) | 924.000 |
| Ankauf 2,0 Mio. Euro, Nebenkosten 0,2 Mio., übernommenes Darlehen 1,0 Mio. | 300.000 | 1.527.778 | 1.200.000 | 300.000 | (a) | 900.000 |
| derselbe Ankauf, andere Lesart von `MA-026` | 1.300.000 | 1.944.444 | 1.200.000 | 1.200.000 | (c) | 0 |
| Neubau 10 Mio., Förderdarlehen 5,4 Mio., Zuschuss 1,8 Mio., Mindesteigenkapital 1,8 Mio., Quote 65 %, Reinertrag 400.000 | 1.100.000 | 2.962.698 | 1.000.000 | 1.000.000 | (c) | 1.800.000 |
| derselbe Neubau, Quote 60 % | 600.000 | 2.962.698 | 1.000.000 | 600.000 | (a) | 2.200.000 |
| derselbe Neubau, Quote 65 %, Reinertrag 200.000 | 1.100.000 | 184.920,58 | 1.000.000 | 184.920,58 | (b) | 2.615.079,42 |
| derselbe Neubau, Reinertrag 180.000 | 1.100.000 | negativ | 1.000.000 | 0 mit M-21 | (b) | 2.800.000 |

Der Kapitaldienst des Förderdarlehens im Beispiel ist 155.571,43 Euro; erst über 186.685,71 Euro Reinertrag bleibt nach (b) etwas für die Bank. Die Grenzen (a) und (b) des ersten Beispiels treffen sich beim Kaufpreis 2.301.538,46 Euro (Knick, R-11.5). Im Monatsraster wirkt die Rundung der Rate: Bei 107.712,37 Euro Reinertrag ergibt die geschlossene Form 1.496.005,14 Euro; gewährt werden 1.496.004,99 Euro mit 89.760,24 Euro Kapitaldienst und einer Deckung von 1,200001.

**R-5.13 Laufende Beiträge.** Ein laufender Beitrag (Verwaltungskostenbeitrag) ist runde(Restschuld der Vorperiode x Beitragssatz / p). Er ist Finanzierungskosten: Er zählt zum Kapitaldienst (R-10.14), mindert das operative Ergebnis (R-7.2) und steht in der Bestandsprobe (P-03).

**R-5.14 Einbehaltene Beträge.** Ein Disagio oder Bearbeitungsentgelt wird bei der ersten Auszahlung einbehalten: Die Restschuld steigt um die volle Auszahlung, der Geldzufluss ist um den einbehaltenen Betrag kleiner. Das Entgelt auf einen Zuschuss wird von dessen erster Auszahlung einbehalten; der Zuschuss steht brutto als originäre Zahlung, das Entgelt als eigener Abfluss. Einbehaltene Beträge gehören zur Mittelverwendung (R-11.2).
*Beispiel (RF-08):* Disagio 3 % auf 700.000 Euro: Restschuld 700.000,00, Zufluss 679.000,00 Euro. *Beispiel (RF-12):* Förderdarlehen 5.124.000 Euro und Zuschuss 1.708.000 Euro: einbehalten 51.240,00 + 12.810,00 = 64.050,00 Euro.

**R-5.15 Tilgungszuschuss.** Ein Tilgungszuschuss mindert die Restschuld ohne Geldfluss. Er steht nicht im Finanzierungssaldo, aber in der Kreditprobe (P-02) und in der Bestandsprobe (P-03). Die Grobkalkulation nutzt ihn nicht; der Kern führt ihn für die KfW-Darlehen des Teils 2.
*Beispiel (RF-08):* Testfall mit 21.000 Euro Disagio, 35.000 Euro Tilgungszuschuss im dritten Jahr und 100.000 Euro Zuschuss: Alle Kontrollsummen schließen mit null.

**R-5.16 Ablösung und Vorfälligkeit.** In N wird nach der planmäßigen Rate jede Restschuld abgelöst (R-8.6). Reicht die Zinsbindung eines Darlehens über N hinaus, fällt eine Vorfälligkeitsentschädigung an: runde(abgelöste Restschuld x H-18 x Restbindung in Jahren), als Finanzierungskosten in N. Für Förderdarlehen fällt keine an. **Neue Festlegung (NF-10):** Die Pauschale ersetzt in Teil 1 die Zinsschadenrechnung der Bank; sie ist eine Annahme über die Bankpraxis (Vorschlag einer Modellannahme, Kapitel 17). Der Kern gibt den Hinweis M-25 zurück, wenn die Bindung über die Haltedauer reicht.
*Beispiel (RF-08; Satz 1 % je Jahr als Annahme):* Testfall mit zehn Jahren Zinsbindung, Verkauf nach fünf: 624.171,48 x 1 % x 5 = 31.208,57 Euro; Endwert 562.520,28 statt 584.366,28 Euro. *Beispiel (RF-14):* Ankauf mit Verkauf nach einem Jahr: 126.170,42 Euro bei neun Jahren Restbindung.

**R-5.17 Kontokorrent.** Der Kontokorrent ist keine Tranche, sondern das Ausgleichskonto für Fehlbeträge (R-4.3, Schritt 9) mit effektivem Jahreszins H-10 (R-2.6) und der Linie H-11 (R-4.5). Er hat keinen Tilgungsplan: Jeder Überschuss führt ihn zurück, bevor Guthaben entsteht. Sein Zins mindert das operative Ergebnis und steht im Periodensaldo.
*Beispiel (RF-06):* Ohne den Kontokorrentzins in Steuer und Saldo läge der Endwert der Variante mit 380.000 Euro Eigenkapital um 1.839,71 Euro zu hoch (Bericht, Abschnitt 3).

## 6 Erträge und laufende Auszahlungen der Grobkalkulation

**R-6.1 Indexreihe.** Index_1 = 1; Index_j = runde12(Index_(j−1) x (1 + Steigerung)). Jede Größe hat ihre eigene Steigerung: Mieten H-12, Kosten H-13, Baupreise H-14, CO2-Kosten KAT-09, Erbbauzins E-63. Der Schritt fällt zu Beginn jedes Jahres der Reihe.

**R-6.2 Marktmiete.** Marktmiete_j = E-16 x Index_j (Mieten), in Euro je Quadratmeter und Monat, ungerundet geführt.

**R-6.3 Anpassungspfad.** Die Ist-Miete nähert sich der Marktmiete über die Anpassungsdauer d (E-53) linear und höchstens mit der Kappungsgrenze κ (KAT-08):

    Pfad_j  = Ist + (Marktmiete_j − Ist) x min(1; (j − 1) / d)        (bei d = 0: Marktmiete_j)
    Miete_j = min(Pfad_j; Basis_j x (1 + κ)),   Basis_j = Miete_(j−3) für j > 3, sonst Ist

Im Jahr 1 gilt die Ist-Miete, im Jahr d + 1 ist die Marktmiete erreicht, wenn die Kappung nicht bindet. Liegt die Ist-Miete über der Marktmiete, führt derselbe Pfad sie linear zurück; die Kappung wirkt nur nach oben. **Neue Festlegung (NF-12):** Der einfache Pfad ersetzt in 1a die Mieterliste; Wartefristen und Einzelmieten regelt die Vollkalkulation. Für die ersten drei Jahre ist die Miete vor dem Stichtag unbekannt; die Ist-Miete als Basis ist die vorsichtige Wahl.
*Beispiel (RF-11; Mietsteigerung 2 %, Kappung 15 % in drei Jahren als Annahme):* Ist-Miete 8,50 Euro, Marktmiete 9,20 Euro, Anpassung über vier Jahre. Miete je Quadratmeter in den Jahren 1 bis 6: 8,5000 / 8,7210 / 9,0358 / 9,4473 / 9,9584 / 10,1575. Jahr 2: Marktmiete 9,384; Pfad 8,50 + 0,884 x 1/4 = 8,7210. Ab Jahr 5 gilt die Marktmiete.

**R-6.4 Sollmiete, Mietausfall, Mieteinzahlung.** Sollmiete der Periode = runde(Wohnfläche x Miete_j x 12 / p). Mieteinzahlung = runde(Sollmiete x (1 − Mietausfallquote)). **Neue Festlegung (NF-13):** Der erwartete Mietausfall aus Leerstand und Forderungsverlust mindert den Erlös und ist keine Kostenposition; ein pauschales Mietausfallwagnis als Kosten wäre eine kalkulatorische Größe ohne Zahlung (`SCHULTE-IMMOBILIENINVESTITION-2025`). Fluktuation mit Leerstandsdauer regelt die Vollkalkulation.
*Beispiel (RF-11; Mietausfall 2 % als Annahme):* 1.320 m² x 8,50 Euro = 11.220,00 Euro Sollmiete im Monat; Einzahlung 10.995,60 Euro; im Jahr 1 zusammen 131.947,20 Euro.

**R-6.5 Gebundene Miete.** Für den gebundenen Flächenanteil φ gilt die gebundene Miete: unverändert für die festen Jahre, danach je Schritt um höchstens die zulässige Steigerung σ erhöht, nie über der Marktmiete:

    Stufe_j = 0 für j ≤ feste Jahre, sonst (j − feste Jahre − 1) div Schrittjahre + 1
    gebundene Miete_j = min(Ausgangsmiete x (1 + σ)^Stufe_j; Marktmiete_j)

Miete_j des Vorhabens = φ x gebundene Miete_j + (1 − φ) x freie Miete_j. Feste Jahre, Schrittjahre und σ sind Katalogwerte (KAT-10, KAT-11). Bei übernommenen Bindungen zählt der erste Schritt ab dem Stichtag, weil die letzte Erhöhung unbekannt ist (vorsichtige Lesart; Teil von **NF-14**).
*Beispiel (RF-12; Werte nach Bericht Anhang C.1 als Annahme: drei Jahre fest, dann 6,15 % je drei Jahre):* Eingangsmiete 8,20 Euro: 8,2000 in den Vermietungsjahren 1 bis 3, 8,7043 in 4 bis 6, 9,2396 ab Jahr 7.

**R-6.6 Miete nach dem Ende der Bindung.** Endet die Bindung nach dem Jahr b, gilt im Jahr b + 1 noch die letzte gebundene Miete; von dort führt der Anpassungspfad nach R-6.3 zur Marktmiete, mit der letzten gebundenen Miete als Ausgang (`BGB-558`). **Neue Festlegung (NF-14).**
*Beispiel (RF-11):* 40 % der Fläche gebunden zu 6,80 Euro bis Ende Jahr 6, Rest wie oben. Miete des Vorhabens in den Jahren 1 bis 10: 7,8200 / 7,9526 / 8,1415 / 8,5557 / 8,8623 / 8,9818 / 9,1037 / 9,5630 / 9,7879 / 9,9173. Jahr 1: 0,4 x 6,80 + 0,6 x 8,50 = 7,82. Jahr 4: 0,4 x 7,2182 + 0,6 x 9,4473 = 8,5557.

**R-6.7 Neubau.** Die Miete fließt ab dem Monat nach der Bauzeit in voller Höhe; eine Erstvermietungskurve regelt Teil 2. Vermietungsjahr v umfasst zwölf Monate ab Bezug; die eingegebene Miete gilt für v = 1 und steigt mit dem Mietindex. Mit Grobförderung gilt R-6.5 mit der Eingangsmiete des Katalogs für den geförderten Flächenanteil (voreingestellt die ganze Fläche); die Bindung beginnt mit der Bezugsfertigkeit.

**R-6.8 Bewirtschaftung.** Jahresbetrag_j = (Verwaltung je Einheit x Einheiten + Instandhaltung je m² x Wohnfläche + nicht umlagefähige Betriebskosten je m² x Wohnfläche) x Index_j (Kosten). Zahlung je Periode = runde(Jahresbetrag_j / p). j ist das Planjahr; die Eingabewerte haben den Preisstand des Planjahres 1. Beim Neubau beginnen die Zahlungen mit dem Bezug, zum Preisstand ihres Planjahres. Die Instandhaltungspauschale deckt die laufende Instandhaltung, nicht den Investitionsstau (R-6.10).
*Beispiel (RF-11; 350 Euro je Einheit, 14 und 2 Euro je m² als Annahme):* 20 x 350 + 1.320 x 14 + 1.320 x 2 = 28.120 Euro im Jahr 1, im Monat 2.343,33 Euro.

**R-6.9 CO2-Kosten.** Zahlung je Periode = runde(CO2-Kosten des Vermieters je m² x Wohnfläche x Index_j (CO2) / p). Der Wert je Quadratmeter und seine Steigerung kommen aufgelöst aus KAT-09; der Kern rechnet das Stufenmodell in 1a nicht selbst.
*Beispiel (RF-11; 0,60 Euro je m² und Jahr, plus 5 % je Jahr als Annahme):* 792 Euro im Jahr 1, 66,00 Euro im Monat; Bewirtschaftung und CO2-Kosten zusammen 2.409,33 Euro im Monat und 28.911,96 Euro im Jahr 1.

**R-6.10 Investitionsstau.** Eine Maßnahme hat einen Betrag zum Preisstand des Stichtags (E-50), ein Jahr der Ausführung k (E-51) und das Kennzeichen Erhaltung oder Modernisierung (E-52). Zahlung = runde(Betrag x (1 + Baupreissteigerung)^k) im letzten Monat des Jahres k; für k = 0 zum Stichtag als Teil des Mittelbedarfs. Erhaltung mindert das operative Ergebnis im Jahr der Zahlung; Modernisierung wird aktiviert und ab dem Folgejahr mit dem Satz des Gebäudes abgeschrieben (R-7.3). Liegt k nach dem Verkauf, mindert die Maßnahme den Verkaufserlös (R-8.4). Eine Mietwirkung der Modernisierung gibt es in 1a nicht. **Neue Festlegung (NF-15).** Die Prüfung auf anschaffungsnahe Herstellungskosten (`ESTG-6`) gehört zur Steuer in Grundform; übersteigen Erhaltungsmaßnahmen der ersten drei Jahre 15 % der Gebäudeanschaffungskosten, gibt der Kern den Hinweis M-36 zurück.
*Beispiel (RF-11; Baupreissteigerung 3 % als Annahme):* 120.000 Euro, Jahr 2, Erhaltung: Zahlung 120.000 x 1,0609 = 127.308,00 Euro im Monat 24.

**R-6.11 Erbbauzins.** Zahlung je Periode = runde(Erbbauzins im ersten Jahr x Index_j (Erbbauzins) / p), ab dem Stichtag, auch in der Bauzeit; sie zählt zur Bewirtschaftung. Was beim Erbbaurecht in Stufe 1 fehlt, nennt der Bericht (Anhang D.1).

**R-6.12 Reinertrag.** Reinertrag einer Zeitspanne = Mieteinzahlungen − Bewirtschaftung nach R-6.8, R-6.9 und R-6.11. Maßnahmen nach R-6.10, Zinsen, Tilgung und Steuern gehören nicht dazu. Der Reinertrag im ersten Jahr der Vollvermietung (RE_VJ) ist beim Ankauf der des Planjahres 1, beim Neubau der der zwölf Monate nach der Bauzeit.
*Beispiel (RF-11):* 131.947,20 − 28.911,96 = 103.035,24 Euro.

## 7 Steuer in Kurzform

**R-7.1 Steuerstatus.** Die Kurzform rechnet je Planjahr eine Steuerzahlung nach dem Steuerstatus des Vorhabens (E-40):

| Status | Regel | Quellen der Katalogwerte |
|---|---|---|
| voll steuerpflichtige Körperschaft | R-7.7, R-7.8 | `KSTG-23`, `SOLZG-4`, `GEWSTG-11`, `GEWSTG-16`, `GEWSTG-9` |
| gewerbliche oder gewerblich geprägte Personengesellschaft (`ESTG-15`) | R-7.9 | dazu `ESTG-35` |
| Einzelunternehmen mit Betriebsvermögen | R-7.9 mit Anteil 100 % | wie zuvor |
| Privatperson, vermögensverwaltende Personengesellschaft | R-7.10, R-7.11 | `ESTG-23` |
| befreite Körperschaft (`KSTG-5`) | R-7.12 | – |
| Lehrbuch | R-7.13, nur Referenzfälle | – |

Die Kurzform ist eine benannte Vereinfachung gegenüber der Steuer in Grundform (Teil 2). Sie rechnet ohne Hinzurechnungen der Gewerbesteuer (`GEWSTG-8`), ohne Begrenzung der Verlustverrechnung (`ESTG-10D`, `GEWSTG-10A`, `MA-010`), ohne Zinsschranke, ohne Sonderabschreibung und mit dem Planjahr als Steuerjahr (R-2.7). Das Ergebnis führt den Hinweis, dass die Steuer in Kurzform gerechnet ist.

**R-7.2 Bemessung.** Drei Größen je Planjahr:

- **operatives Ergebnis** e_op = Mieteinzahlungen − Bewirtschaftung − Erhaltungsmaßnahmen − Abschreibung − Zinsen der Darlehen − Kontokorrentzinsen − laufende Beiträge − einbehaltene Beträge − Vorfälligkeit;
- **Habenzinsen** z_h der Geldanlage;
- **Verkaufsgewinn** g_v im letzten Planjahr (R-7.4).

Zuschüsse sind kein Ertrag; sie mindern die Abschreibungsgrundlage (R-7.3). Die Gewerbesteuer ist keine Betriebsausgabe und mindert weder das Ergebnis noch ihre eigene Bemessung (`ESTG-4-5B`). **Neue Festlegung (NF-16):** Finanzierungskosten einschließlich der einbehaltenen Entgelte, eines Disagios, der Zinsen der Bauzeit und der Vorfälligkeit sind in der Kurzform im Jahr der Zahlung abziehbar; Zahlungen zum Stichtag zählen zum Planjahr 1. Ob sie zu verteilen oder zu aktivieren wären, klärt die Grundform (Vorschlag einer Modellannahme, Kapitel 17).

**R-7.3 Abschreibung.** Linear mit dem Satz KAT-07, beim Ankauf nach dem Baujahr E-17. Abschreibungsgrundlage beim Ankauf: (Kaufpreis + Erwerbsnebenkosten) x (1 − Bodenanteil) − Zuschüsse; beim Neubau: Baukosten − Zuschüsse, das Grundstück mit seinen Nebenkosten ist Boden. Abschreibung des Planjahres j = runde(Grundlage x Satz x Nutzungsmonate im Planjahr / 12), höchstens der Rest der Grundlage; gebucht am Ende des Planjahres. Beim Ankauf läuft die Nutzung ab dem Stichtag, beim Neubau ab dem Monat nach der Bauzeit. Eine aktivierte Maßnahme (R-6.10) wird ab dem Jahr nach ihrer Zahlung mit demselben Satz abgeschrieben. **Neue Festlegung (NF-17);** dass Zuschüsse die Abschreibungsgrundlage mindern, folgt der Kopplung „Förderung wirkt auf die Abschreibung“ der Spezifikation (Kapitel 4) und ist als Modellannahme vorgeschlagen (Kapitel 17).
*Beispiel (RF-11; 2 % als Annahme):* (2.400.000 + 240.000) x 75 % = 1.980.000 Euro Grundlage, 39.600,00 Euro je Jahr. *Beispiel (RF-12; 3 % als Annahme):* Baukosten 7.540.000 Euro, Bezug nach 18 Monaten: Planjahr 2 trägt sechs Monate, 113.100,00 Euro. *Beispiel (RF-14):* Über 42 Jahre endet die Abschreibung im Planjahr 35; danach ist die Grundlage aufgebraucht.

**R-7.4 Verkaufsgewinn.** g_v = gebuchter Verkaufserlös (R-8.5) − Restbuchwert − Rückzahlung von Fördermitteln. Restbuchwert = Boden + Abschreibungsgrundlage − Summe der Abschreibungen, je einschließlich aktivierter Maßnahmen (P-08). Ob g_v besteuert wird, regelt der Steuerstatus.
*Beispiel (RF-11):* Erlös 3.276.829,52 Euro, Restbuchwert 2.640.000 − 12 x 39.600 = 2.164.800,00 Euro, Verkaufsgewinn 1.112.029,52 Euro. *Beispiel (RF-10):* Im Testfall ergäbe ein steuerpflichtiger Verkauf 138.000 Euro Gewinn, 41.400 Euro Steuer und einen Endwert von 542.966,28 Euro.

**R-7.5 Verlustvortrag (`MA-016`, Voreinstellung).** Ein negatives Jahresergebnis wird nicht erstattet, sondern erhöht den Verlustvortrag des Vorhabens; ein positives wird bis zur Höhe des Vortrags verrechnet, nur der Rest wird besteuert. Die Kurzform verrechnet Vorträge unbeschränkt und ohne Rücktrag. Einkommen- oder Körperschaftsteuer und Gewerbesteuer führen getrennte Vorträge. Ein Vortrag, der am Ende der Haltedauer übrig ist, verfällt für das Vorhaben. **Neue Festlegung (NF-18)** für die unbeschränkte Verrechnung.
*Beispiel (RF-10, RF-15; Testfall mit 20.000 und 30.000 Euro Reinertrag in den ersten beiden Jahren, Steuersatz 30 % als Annahme):* Mit Vortrag fällt in keinem der fünf Jahre Steuer an, 4.254,31 Euro Vortrag bleiben ungenutzt, Endwert 533.745,69 Euro.

**R-7.6 Sofortige Verrechnung (`MA-016`, andere Lesart).** Der Verlust mindert im selben Jahr die Steuer des Investors auf andere Einkünfte; die Steuer ist dann linear im Ergebnis und kann negativ sein. Das Vorhaben gilt als Teil eines größeren Steuersubjekts: Freibetrag und Abrundung des Gewerbeertrags gelten als verbraucht, und die Anrechnung nach R-7.9 wirkt mit ihrem Grenzsatz. **Neue Festlegung (NF-19).**
*Beispiel (derselbe Fall):* Steuer −7.680,00 / −4.855,68 / 3.286,68 / 4.054,76 / 4.865,45 Euro, Endwert 537.232,83 Euro; die Lesart hebt den Endwert um 3.487,14 Euro. *Beispiel (RF-13):* Im Ankauf hebt sie die VOFI-Rendite von 5,162 % auf 5,260 %.

**R-7.7 Körperschaft.** Einkommen = e_op + z_h + g_v. Körperschaftsteuer mit Zuschlag = runde(Satz des Kalenderjahres x (1 + Zuschlagsatz) x Einkommen nach Verlustvortrag). Dazu die Gewerbesteuer nach R-7.8.
*Beispiel (RF-10; Katalogstand des Berichts, Hebesatz 400 % als Annahme):* 100.000 Euro im Planjahr 2027: 15.825,00 Euro Körperschaftsteuer mit Zuschlag und 14.000,00 Euro Gewerbesteuer, zusammen 29.825,00 Euro; mit erweiterter Kürzung 15.825,00 Euro. Nach −50.000 Euro im ersten Jahr und +80.049 Euro im zweiten: 4.438,24 + 4.200,00 = 8.638,24 Euro.

**R-7.8 Gewerbesteuer.** Gewerbeertrag = Gewinn nach gewerbesteuerlichem Verlustvortrag, auf volle 100 Euro abgerundet, bei Personenunternehmen um den Freibetrag gekürzt, nicht unter null (`GEWSTG-11`). Messbetrag = runde(Gewerbeertrag x Messzahl); Gewerbesteuer = runde(Messbetrag x Hebesatz). Ist das Kennzeichen „erweiterte Grundstückskürzung“ (E-41) gesetzt, ist die Gewerbesteuer null und die Anrechnung entfällt. **Neue Festlegung (NF-20):** In der Kurzform erfasst das Kennzeichen den ganzen Gewerbeertrag des Vorhabens einschließlich der Habenzinsen und des Verkaufsgewinns, nach dem Wortlaut des Berichts („mit dem die Gewerbesteuer entfällt“). Ob Zinsen und Verkaufsgewinn tatsächlich begünstigt sind, ist nicht am Original geklärt; das ist eine Ausnahme von der Vorsichtsregel und als Modellannahme vorgeschlagen (Kapitel 17). Im Ankauf aus RF-11 macht die Gewerbesteuer auf den Verkaufsgewinn 155.680 Euro aus.

**R-7.9 Gewerbliche Personengesellschaft und Einzelunternehmen.** Gewinn = e_op + z_h + g_v. Einkommensteuer = runde(E-42 x Gewinn nach Verlustvortrag). Gewerbesteuer nach R-7.8 mit Freibetrag. Anrechnung (`ESTG-35`) = min(Anteil x Anrechnungsfaktor x Messbetrag; Anteil x Gewerbesteuer; Anteil x Einkommensteuer des Jahres); Steuer = Einkommensteuer + Gewerbesteuer − Anrechnung. Einen Vortrag der Anrechnung gibt es nicht. Der Anteil ist E-43, der Anteil natürlicher Personen am Gewinn; beim Einzelunternehmen ist er 100 %. **Neue Festlegung (NF-21):** Ein Anteil als Eingabe genügt in der Kurzform; der Steuersatz E-42 ist dann der gewogene Satz aller Gesellschafter.
*Beispiel (RF-10; Steuersatz 42 %, Katalogstand des Berichts als Annahme):* 100.000 Euro Gewinn: Gewerbeertrag 75.500 Euro, Messbetrag 2.642,50 Euro.

| Hebesatz | Gewerbesteuer | Anrechnung | Steuer gesamt |
|---|---|---|---|
| 400 % | 10.570,00 | 10.570,00 | 42.000,00 |
| 280 % | 7.399,00 | 7.399,00 | 42.000,00 |
| 480 % | 12.684,00 | 10.570,00 | 44.114,00 |
| 400 %, Anteil natürlicher Personen 50 % | 10.570,00 | 5.285,00 | 47.285,00 |
| 400 %, Steuersatz 8 % | 10.570,00 | 8.000,00 | 10.570,00 |

Bis zu einem Hebesatz von 400 % gleicht die Anrechnung die Gewerbesteuer aus; das Kennzeichen der Kürzung ändert dann nichts (RF-13: Endwert in beiden Fällen 2.125.644,23 Euro). Bei 440 % sinkt der Endwert auf 2.107.852,32 Euro, bei 60 % natürlichen Personen auf 2.036.713,03 Euro.

**R-7.10 Privatperson.** Zwei getrennte Töpfe: Steuer auf Vermietung = runde(E-42 x e_op nach Verlustvortrag); Steuer auf Zinsen = runde(Satz auf Zinserträge x z_h). Ein Vermietungsverlust mindert die Steuer auf Zinsen nicht. Der Satz auf Zinserträge ist H-22; seine gesetzliche Grundlage fehlt im Kataster (Kapitel 17). **Neue Festlegung (NF-22).**
*Beispiel (RF-10; 42 % und 26,375 % als Annahme):* 30.000 Euro Vermietung und 1.000 Euro Zinsen: 12.600,00 + 263,75 = 12.863,75 Euro. Bei −10.000 Euro Vermietung und 500 Euro Zinsen: 131,88 Euro.

**R-7.11 Privater Verkauf.** Der Verkaufsgewinn ist steuerpflichtig, wenn die Haltedauer n die Frist KAT-06 nicht überschreitet (`ESTG-23`); dann Steuer = runde(E-42 x g_v) für g_v > 0. Ein negativer Verkaufsgewinn bleibt unberücksichtigt (vorsichtige Lesart). Der Buchwert nach R-7.4 enthält die abgezogenen Abschreibungen.
*Beispiel (RF-13; Frist zehn Jahre als Katalogstand):* Verkauf nach zehn Jahren: 380.346,24 Euro Steuer auf den Gewinn; nach elf Jahren keine. Die VOFI-Rendite je Haltedauer 9 bis 12 Jahre ist 3,997 / 4,133 / 5,982 / 5,949 %; der Sprung liegt zwischen Jahr 10 und 11.

**R-7.12 Befreite Körperschaft.** Steuer null in jedem Jahr. Die Grenze nicht begünstigter Einnahmen (`KSTG-5`) prüft die Kurzform nicht.

**R-7.13 Lehrbuchsteuer.** Ein Satz auf e_op, z_h und, je nach Fall, g_v; wahlweise sofortige Verrechnung oder Vortrag; getrennter Satz auf Zinsen möglich. Nur für Referenzfälle im Jahresmodus.
*Beispiel (RF-03):* Standardbeispiel mit 50 %: Steuer 70 / 82 / 94 / 106 / 744.

**R-7.14 Grenzsteuersätze für Kennzahlen.** Der Vergleichsfaktor (R-10.4) und die Gesamtkapitalrendite (R-10.11) brauchen je Planjahr einen Satz:

| Status | s_op(j) | s_Z(j) |
|---|---|---|
| Körperschaft | Körperschaftsteuersatz(j) x (1 + Zuschlag) + g | wie s_op |
| gewerbliche Personengesellschaft, Einzelunternehmen | E-42 + g − Anteil x Messzahl x min(Anrechnungsfaktor; Hebesatz) | wie s_op |
| Privatperson | E-42 | Satz auf Zinserträge |
| befreit | 0 | 0 |
| Lehrbuch | Satz | Satz auf Zinsen |

mit g = Messzahl x Hebesatz, bei gesetztem Kennzeichen g = 0 und ohne Anrechnungsglied. Freibetrag, Abrundung und Verlustvortrag bleiben außer Betracht.
*Beispiel (RF-13):* Körperschaft ohne Kürzung im Jahr 2027: 15,825 % + 14 % = 29,825 %; Personengesellschaft bei 400 %: 42 % + 14 % − 14 % = 42 %.

## 8 Restwert und Verkauf

**R-8.1 Verkaufsfaktor.** Verkaufspreis = runde(Verkaufsfaktor x Jahressollmiete des Folgejahres). Die Jahressollmiete des Folgejahres ist die Summe der Sollmieten der zwölf Monate nach dem Verkaufsstichtag nach R-6.4, vor Mietausfall. Das Ergebnis ist der Kaufpreis des Käufers ohne dessen Erwerbsnebenkosten. **Neue Festlegung (NF-23)** für die Sollmiete vor Mietausfall als Bezug; die Spezifikation nennt die Jahresnettokaltmiete. In 1a ist der Faktor der einzige Maßstab.
*Beispiel (RF-11):* Miete im Jahr 13: 11,6678 Euro je m², Sollmiete 15.401,53 Euro im Monat und 184.818,36 Euro im Jahr; Faktor 18: Verkaufspreis 3.326.730,48 Euro.

**R-8.2 Nettoanfangsrendite.** Verkaufspreis = runde(Reinertrag des Folgejahres / Nettoanfangsrendite / (1 + Erwerbsnebenkosten des Käufers)). Der Reinertrag folgt R-6.12; das Ergebnis vor der Division durch (1 + Nebenkosten) ist der Kaufpreis einschließlich der Nebenkosten des Käufers. Der Maßstab steht ab der Vollkalkulation zur Wahl; das Eingabefeld weist die Bezugsbasis aus.
*Beispiel (Bericht Anhang D.4):* 100.000 Euro Jahresmiete, 20 % nicht umlagefähige Kosten. Faktor 22,2: 2.220.000,00 Euro. Nettoanfangsrendite 4,5 %: 1.777.777,78 Euro einschließlich und bei 7 % Nebenkosten 1.661.474,56 Euro ohne Nebenkosten des Käufers.

**R-8.3 Verkaufskosten.** Verkaufskosten = runde(Verkaufspreis x H-16).
*Beispiel (RF-11; 1,5 % als Annahme):* 49.900,96 Euro.

**R-8.4 Ausstehender Investitionsstau.** Eine Maßnahme, die am Verkaufsstichtag noch aussteht (k > n), mindert den Verkaufserlös um runde(Betrag x ausstehender Anteil x (1 + Baupreissteigerung)^n), also zum Preisstand des Stichtags und nicht des Planjahres. Was bis zum Stichtag ausgeführt ist, steht als Zahlung im Finanzplan (R-6.10). In 1a ist eine Maßnahme ganz ausgeführt oder ganz ausstehend; die Probe P-06 läuft in Anteilen.
*Beispiel (RF-14, Bericht Anhang A Nr. 3):* 100.000 Euro, geplant für Jahr 12, Verkauf in Jahr 10, 3 %: Abzug 134.391,64 Euro, nicht 142.576,09 Euro. Würden 40 % in Jahr 9 ausgeführt, stünden 52.190,93 Euro im Finanzplan und 80.634,98 Euro im Abzug; die Anteile ergeben 100 %, die Eurobeträge keinen der beiden Preisstände.

**R-8.5 Gebuchter Verkaufserlös.** Im Finanzplan steht in N: Verkaufserlös = Verkaufspreis − Verkaufskosten − ausstehender Investitionsstau (P-05). Ein Schuldenfeld hat der Restwert nicht: Der Erlös wird nie nach Schulden eingegeben oder gebucht.
*Beispiel (RF-11):* 3.326.730,48 − 49.900,96 = 3.276.829,52 Euro. *Beispiel (RF-05):* Wird im Testfall der Erlös nach Schulden gebucht und die Restschuld zusätzlich abgelöst, fällt der Endwert auf −39.805,20 Euro; die Kreditprobe bemerkt nichts, die Restwertprobe meldet −624.171,48 Euro.

**R-8.6 Ablösung.** Jede Restschuld wird in N als Zahlung im Finanzplan abgelöst, nach der planmäßigen Rate und vor dem Ausgleich. Übernimmt der Käufer ein Darlehen, werden der Verkaufserlös in voller Höhe und die Restschuld als Ablösung gebucht.
*Beispiel (RF-11):* Ablösung des Bankdarlehens 1.034.515,79 Euro im Monat 144.

**R-8.7 Rückzahlung von Fördermitteln (`MA-017`).** Wird vor dem Ende der Bindung verkauft, ist der Zuschuss anteilig zurückzuzahlen: Rückzahlung = runde(Zuschuss x verbleibende Bindungsperioden / Bindungsperioden). Die Bindung beginnt mit der Bezugsfertigkeit. Die Rückzahlung ist eine Zahlung im Finanzplan in N, nie ein Abzug vom Verkaufserlös (P-07); sie mindert den Verkaufsgewinn (R-7.4).
*Beispiel (RF-12; Bindung 35 Jahre als Katalogstand):* Zuschuss 1.708.000 Euro, Bezug nach 18 Monaten, Verkauf nach 240 Monaten: 198 von 420 Monaten verbleiben, Rückzahlung 805.200,00 Euro. Nach 42 Jahren (RF-14) ist sie null.

**R-8.8 Restwert bei laufender Bindung (`MA-017`).** Läuft die Bindung am Verkaufsstichtag noch, folgt der Verkaufspreis aus der gebundenen Miete des Folgejahres (R-6.5), und das Förderdarlehen wird wie jedes Darlehen abgelöst. Die andere Lesart (der Käufer übernimmt Darlehen und Bindung) ist in Teil 1 nicht gebaut; sie kommt mit dem Bestandsteil der Förderung.
*Beispiel (RF-12):* Verkauf nach 20 Jahren bei gebundener Miete: Verkaufspreis 6.757.038,72 Euro, Ablösung des Förderdarlehens 2.866.999,26 Euro.

**R-8.9 Reihenfolge am Verkaufsstichtag.** In N laufen die Schritte der Periode wie in jeder anderen (R-4.3): laufende Zahlungen des letzten Monats, planmäßige Rate, dann Ablösung, Vorfälligkeit, Verkaufserlös, Rückzahlung, Steuer des letzten Planjahres einschließlich Verkaufsgewinn, Ausgleich. Der Endwert enthält damit alle Steuern.

## 9 Unterlassensalternative

**R-9.1 Eigener Finanzplan mit zwei Zinssätzen.** Die Unterlassensalternative wird als eigener Finanzplan gerechnet, nicht mit einer Formel. Sie führt drei Konten: die langfristige Anlage zum Anlagezins a_L (H-09), das Wiederanlagekonto zum kurzfristigen Habenzins h (H-08) und einen Kontokorrent zum Satz k (H-10). Der kurzfristige Satz ist derselbe wie der der Geldanlage der Investition. Voreingestellt ist a_L = h.
*Beispiel (RF-03, RF-04):* Standardbeispiel mit Steuern: Die Ein-Satz-Formel 8.000 x (1 + 5 % x 0,5)^5 ergibt 9.051,27, der Finanzplan mit 5 % und 4,5 % ergibt 9.046,02 wie das Lehrbuch. Im Fallbeispiel liegt die Formel mit 30.848,38 um 404,15 Tausend Euro oder 1,33 % über dem Finanzplan (30.444,24).

**R-9.2 Spiegelung.** Die Alternative erhält in jeder Periode dieselbe Einlage e_u und dieselbe Entnahme a_u wie die Investition, nach Saldierung (R-10.3) und einschließlich der Nachschüsse (P-10).
*Beispiel (RF-06):* Bei 5.000 Euro Entnahme je Jahr bleibt die Endwertdifferenz des Testfalls 155.571,23 Euro. Ohne Spiegelung fiele sie auf 129.861,36 Euro und die Rendite auf 6,91 %.

**R-9.3 Rechenreihenfolge je Periode.** (1) Zinsen auf die Bestände der Vorperiode: runde(langfristige Anlage x Periodensatz von a_L), runde(Wiederanlagekonto x Periodensatz von h), runde(Kontokorrent x Periodensatz von k). (2) Am Ende eines Planjahres die Steuer nach R-9.5. (3) Einlage: zuerst Rückführung eines Kontokorrents, der Rest in die langfristige Anlage. (4) Ausgleich: Wiederanlagekonto − Kontokorrent + Zinsen − Kontokorrentzins − Steuer − Entnahme; ist das Ergebnis negativ, gilt R-9.4.

*Beispiel (RF-03, Tab. 6 des Lehrbuchs: 8.000 zu 5 %, Wiederanlage 4,5 %, Steuersatz 50 %):*

| t | Zins langfristig | Zins Wiederanlage | Steuer | langfristige Anlage | Wiederanlagekonto |
|---|---|---|---|---|---|
| 0 | – | – | – | 8.000 | 0 |
| 1 | 400 | 0 | 200 | 8.000 | 200 |
| 2 | 400 | 9 | 205 | 8.000 | 405 |
| 3 | 400 | 18 | 209 | 8.000 | 614 |
| 4 | 400 | 28 | 214 | 8.000 | 827 |
| 5 | 400 | 37 | 219 | 8.000 | 1.046 |

Endwert 9.046 (genau 9.046,02), Vergleichsrendite 2,49 %.

**R-9.4 Entnahmen und Fehlbeträge.** Entnahmen und Steuern werden zuerst vom Wiederanlagekonto bedient, dann durch Auflösung der langfristigen Anlage zum Nennwert, zuletzt über den Kontokorrent. **Neue Festlegung (NF-24):** Die Reihenfolge schont die höher verzinste Anlage am längsten und rechnet die Alternative damit eher zu gut als zu schlecht; für die Investition ist das die vorsichtige Wahl.
*Beispiel (RF-07; Testfall mit a_L = 3 % und h = 2 %):* Eine Entnahme von 40.000 Euro im Jahr 4 übersteigt das Wiederanlagekonto (25.554,45 Euro am Ende von Jahr 3); der Rest kommt aus der langfristigen Anlage. Die Endwertdifferenz steigt dadurch von 141.173,70 auf 141.213,52 Euro, weil die Alternative den höheren Zins verliert.

**R-9.5 Steuern.** Die Alternative wird mit demselben Steuerstatus und denselben Parametern besteuert wie die Investition, mit eigenem Verlustvortrag. Ihre Zinserträge sind Habenzinsen z_h, ihre Kontokorrentzinsen operativer Aufwand. Das gesetzte Kennzeichen der erweiterten Kürzung gilt auch für sie (NF-20); das rechnet die Alternative günstiger und die Investition vorsichtiger.
*Beispiel (RF-11):* Körperschaft, zwölf Jahre, Einlagen 1.208.955,01 Euro zum Stichtag und 91.529,75 Euro im Monat 24: Endwert der Alternative 1.548.770,72 Euro, Vergleichsrendite 1,483 %.

**R-9.6 Takt und Rundung.** Die Alternative rechnet im selben Raster wie die Investition, mit konformen Periodensätzen (R-2.6) und Rundung je Zinsbuchung (R-12.3).

**R-9.7 Endwert.** EW_U = langfristige Anlage + Wiederanlagekonto − Kontokorrent am Zeitpunkt N. Sind beide Sätze gleich und gibt es nur eine Einlage, entspricht das der Aufzinsung mit dem Zins nach Steuern.
*Beispiel (RF-05):* 400.000 x 1,014^5 = 428.795,05 Euro; der Finanzplan ergibt ungerundet denselben Wert und mit Rundung je Zinsbuchung 428.795,06 Euro. Mit a_L = 3 %: 443.192,58 Euro (RF-07, RF-15).

## 10 Kennzahlen

Kennzahlen werden mit voller Rechengenauigkeit gebildet und nur für die Darstellung gerundet (R-12.6).

**R-10.1 Endwert.** EW nach R-4.6, EW_U nach R-9.7.

**R-10.2 Endwertdifferenz.** ΔEW = EW − EW_U. Sie ist die führende Entscheidungsgröße: Das Vorhaben ist gegenüber der Unterlassensalternative vorteilhaft, wenn ΔEW > 0. Sind beide Zinssätze der Alternative gleich, fließen Einlagen in das Guthaben und werden Entnahmen aus ihm bedient, hängt ΔEW nicht davon ab, wann Einlagen und Entnahmen fallen (R-10.6, Eigenschaften 4 und 5).
*Beispiel:* Testfall 155.571,23 Euro (RF-05); Ankauf 825.606,46 Euro (RF-11); Lehrbuch, Standardbeispiel 61,57 ohne und 50,53 mit Steuern (RF-03).

**R-10.3 Saldierung.** Einlagen, Nachschüsse und Entnahmen derselben Periode werden saldiert: s_u = Einlage + Nachschuss − Entnahme; e_u = max(s_u; 0), a_u = max(−s_u; 0). Im Monatsraster wird je Monat saldiert, im Jahresmodus je Jahr.
*Beispiel (RF-06):* Nachschuss und Entnahme von je 50.000 Euro im Jahr 2 ändern weder Endwert noch Rendite (7,876 %); unsaldiert ergäbe dieselbe Zahlungsreihe 7,246 %.

**R-10.4 Vergleichsfaktor.** Der Aufzinsungsfaktor einer Periode ist der kurzfristige Habenzins nach Steuern:

    f_u  = runde12((1 + h x (1 − s_Z(j)))^(1/p)),   j = Planjahr der Periode u
    w(t) = f_(t+1) x f_(t+2) x … x f_N,   w(N) = 1

w(t) zinst einen Betrag von t auf N auf; 1 / w(0) x w(t) zinst ihn von t auf 0 ab. s_Z(j) ist der Grenzsteuersatz auf Zinserträge nach R-7.14.
*Beispiel (RF-05; h = 2 %, Steuersatz 30 %):* f = 1,014 in jedem Jahr; w(0) = 1,014^5 = 1,071988, w(2) = 1,042591. *Beispiel (RF-11):* Körperschaft mit sinkendem Satz, Monatsraster: w(0) = 1,193164, w(24) = 1,160122.

**R-10.5 VOFI-Eigenkapitalrendite (`MA-012`).**

    Z = EW + Summe über u von a_u x w(u)                (Zähler: Endwert zuzüglich aufgezinster Entnahmen)
    D = Summe über u von e_u x w(u) / w(0)              (Nenner: auf den Stichtag abgezinste Einlagen)
    r = (Z / D)^(1/n) − 1

Mit einer einzigen Einlage zum Stichtag und ohne Entnahmen ist das die Lehrbuchformel r = (EW / EK)^(1/n) − 1 (`GABLER-BANKLEXIKON-VOFI`, `SCHULTE-IMMOBILIENINVESTITION-2025`). Für mehrere Einlagen und Entnahmen gibt das Lehrbuch keine Formel; die Erweiterung ist eine eigene Festlegung des Projekts und in Berichten als solche bezeichnet. **Neue Festlegung (NF-25)** sind der Vergleichsfaktor nach R-10.4 und die Vergleichsrendite nach R-10.8; sie machen die im Bericht empfohlene Formel mit der Unterlassensalternative aus zwei Zinssätzen verträglich.
*Beispiel (RF-06, Nachschuss 50.000 Euro im Jahr 2):* Z = 636.495,82; D = 400.000 + 50.000 x 1,042591 / 1,071988 = 448.628,86; r = (636.495,82 / 448.628,86)^(1/5) − 1 = 7,246 %. *Beispiel (Entnahmen 5.000 Euro je Jahr):* Z = 558.656,41 + 25.709,87 = 584.366,28; r = 7,876 % wie im Testfall.

**R-10.6 Eigenschaften und Grenzen der Renditeformel (`MA-012`).** Jede Eigenschaft ist im Referenzrechner an Zahlen geprüft (RF-06, RF-07).

1. **Lehrbuch als Sonderfall.** Bei einer Einlage zum Stichtag gilt die Lehrbuchformel. Standardbeispiel: 5,08 % gegen 4,95 % der Finanzinvestition.
2. **Gleiche Entscheidung wie die Endwertdifferenz.** r > r_U genau dann, wenn ΔEW > 0 – für jede Einlagen- und Entnahmenreihe, jeden Steuerstatus, beide Raster und beliebige zwei Zinssätze der Alternative. Der Grund: Rendite und Vergleichsrendite haben denselben Nenner und dieselben aufgezinsten Entnahmen im Zähler; ihre Zähler unterscheiden sich genau um ΔEW (P-11). Testfall mit a_L = 3 %: ΔEW 141.173,70 Euro, r 7,876 % gegen r_U 2,072 %; mit Nachschuss 140.108,93 Euro, 7,246 % gegen 2,044 %. Verlustfall (Verkauf zu 950.000 Euro, Nachschuss): ΔEW −44.428,77 Euro, r −0,547 % gegen r_U 1,400 %.
3. **Entnahmen aus Guthaben ändern die Rendite nicht.** Eine Entnahme aus der Geldanlage senkt den Endwert um genau den Betrag, um den der Zähler sie aufzinst. Im Jahresmodus gilt das exakt (7,876 % mit und ohne Entnahmen). Im Monatsraster gilt es bis auf die Wirkung der jährlichen Steuerzahlung: Eine Entnahme von 10.000 Euro im Monat 30 ändert die Rendite des Testfalls um weniger als 0,001 Prozentpunkte und die Endwertdifferenz um 3 Cent.
4. **Grenze: Entnahmen über Kontokorrent.** Muss eine Entnahme über den Kontokorrent finanziert werden, sinkt die Rendite, weil der Kontokorrent mehr kostet als der Vergleichsfaktor ansetzt: 8,123 % ohne und 8,089 % mit Entnahmen in der Variante mit 380.000 Euro Eigenkapital. Solange ein Verlustvortrag die Habenzinsen steuerfrei stellt, gilt Eigenschaft 3 ebenfalls nur näherungsweise: In einem Testfall mit Anlaufverlust ändert eine Entnahme von 5.000 Euro die Endwertdifferenz um 0,43 Euro; die Rendite bleibt bei 6,9327 %.
5. **Grenze: zwei verschiedene Zinssätze der Alternative.** Die Endwertdifferenz ist nur bei gleichen Sätzen vom Zeitpunkt der Entnahmen unabhängig. Bei a_L = 3 % und h = 2 % hebt eine Entnahme, die in der Alternative langfristige Anlage auflöst, die Endwertdifferenz (R-9.4: von 141.173,70 auf 141.213,52 Euro).
6. **Grenze: Die Rendite hängt vom Zeitpunkt später Einlagen ab.** Eine Einlage nach dem Stichtag verwässert die Rendite zum Vergleichsfaktor hin, und eine spätere Entnahme hebt das nicht auf. Im Jahresmodus: Nachschuss im Jahr 2 und Entnahme im Jahr 3 ergeben 7,246 % statt 7,876 %, bei unveränderter Endwertdifferenz. Im Monatsraster: Nachschuss und Entnahme von je 50.000 Euro im Monat 13 lassen die Rendite bei 7,933 %; fällt die Entnahme einen Monat später, sind es 7,291 %, elf Monate später ebenfalls 7,291 %. Die Endwertdifferenz bleibt bis auf Rundung gleich (157.123,80 gegen 157.123,77 Euro). Der Abstand zur Zielrendite kann damit durch einen Monat Verschiebung kippen; Jahresmodus und Monatsraster können für dasselbe Vorhaben verschiedene Renditen zeigen.

**Entscheidung zu Eigenschaft 6 (neue Festlegung NF-26):** Die Abhängigkeit wird hingenommen und nicht durch eine Verrechnung von Rückführungen gegen frühere Einlagen beseitigt. Gründe: Die Endwertdifferenz führt und ist davon nicht betroffen. Eine Formel dieser Bauart, die gegen beides unempfindlich ist, gibt es nicht (Prüfrunde 3, Finanzmathematiker). Die naheliegende Alternative, der Barwert der Netto-Eigenkapitalreihe als Nenner, glättet die Verschiebung (7,866 %), hebt aber die Rendite bei Entnahmen aus dem Guthaben auf 8,240 % und hat einen Nenner, der gegen null gehen kann. In der Grobkalkulation tritt der Fall nicht auf, weil sie keine geplanten Entnahmen kennt. Treffen in einer Rechnung Einlagen nach dem Stichtag und Entnahmen zusammen, gibt der Kern den Hinweis M-27 zurück.

**Andere Lesarten (`MA-012`).** Für den Nachschuss von 50.000 Euro im Jahr 2: Summe der Einlagen als Nenner 7,18 %; interner Zins der Eigenkapitalreihe 7,50 %; Nachschuss wie eine negative Entnahme aufgezinst 7,88 %; Formel nach R-10.5: 7,25 %. Die Endwertdifferenz ist in allen Fällen dieselbe. Offen bleibt der Vergleich mit dem Lösungsansatz bei `ROPETER-1998`, auf den das Lehrbuch verweist.

**R-10.7 Randfälle der Rendite.** Ist D = 0 (keine Einlage), ist die Rendite nicht definiert und wird so ausgewiesen (M-28). Ist Z ≤ 0, beträgt sie −100 % (M-29). Maßgeblich ist der Zähler, nicht der Endwert: Mit Entnahmen kann Z positiv sein, obwohl EW negativ ist.
*Beispiel (RF-07):* EW −10.000 Euro, aufgezinste Entnahmen 50.000 Euro, Eigenkapital 400.000 Euro, fünf Jahre: (40.000 / 400.000)^(1/5) − 1 = −36,9 %. *Beispiel (RF-14):* Testfall ohne Eigenkapital: Rendite nicht definiert, Endwert und Endwertdifferenz 63.947,36 Euro. Testfall mit Verkauf zu 500.000 Euro: Endwert −65.633,72 Euro, Rendite −100 %.

**R-10.8 Vergleichsrendite und Abstand zur Zielrendite.** Vergleichsrendite r_U = (Z_U / D)^(1/n) − 1 mit Z_U = EW_U + Summe von a_u x w(u): dieselbe Formel, angewandt auf den Endwert der Unterlassensalternative. Bei gleichen Sätzen und einer Einlage ist r_U der kurzfristige Habenzins nach Steuern. Abstand zur Zielrendite = r − z in Prozentpunkten; z ist H-01, ein effektiver Jahreszins nach Steuern.
*Beispiel (RF-11; Zielrendite 5 % als Annahme):* r = 5,162 %, r_U = 1,483 %, Abstand +0,162 Prozentpunkte; im kombinierten Stressfall 3,178 % und −1,822 Prozentpunkte.

**R-10.9 Endwertüberschuss.** EÜ = Z − D x (1 + z)^n: der Betrag in Euro zum Zeitpunkt N, um den der Zähler der Renditeformel den Wert übertrifft, den er bei genau der Zielrendite hätte. EÜ hat dasselbe Vorzeichen wie der Abstand zur Zielrendite und ist beim höchsten tragbaren Preis null, bis auf die Auflösung der Preissuche von einem Euro (in RF-11: 1,44 Euro). **Neue Festlegung (NF-27):** Der Bericht beschreibt die Größe als „Endwert zuzüglich der aufgezinsten Entnahmen, abzüglich der mit der Zielrendite aufgezinsten Einlagen“. Bei einer Einlage zum Stichtag ist das dasselbe. Bei späteren Einlagen wären zwei Lesarten möglich, die zur Rendite im Widerspruch stehen können; gewählt ist die Fassung, die mit Rendite und tragbarem Preis nie in Widerspruch gerät. EÜ teilt die Grenze aus R-10.6, Eigenschaft 6.
*Beispiel (RF-07):* Testfall: 584.366,28 − 400.000 x 1,05^5 = 73.853,66 Euro. Mit Nachschuss im Jahr 2 und Entnahme im Jahr 3: 63.919,08 Euro. Die anderen Lesarten ergäben 68.101,94 Euro (jede Einlage ab ihrem Zeitpunkt mit der Zielrendite aufgezinst) und 71.817,14 Euro (Einlagen und Entnahmen mit der Zielrendite aufgezinst). *Beispiel (RF-11):* Ankauf 43.445,29 Euro, im Stressfall −444.360,24 Euro.

**R-10.10 Laufzeit.** n in den Formeln ist N / p, die Haltedauer in Jahren.

**R-10.11 VOFI-Gesamtkapitalrendite und Referenzzinsfuß (`GABLER-BANKLEXIKON-GKR`, `MA-028`).**

    g = ((Z − D + Z_S + a_0) / a_0)^(1/n) − 1
    k = ((Z_U − D + Z_S + a_0) / a_0)^(1/n) − 1

a_0 ist die Anschaffungsauszahlung zum Stichtag, Z_S die Summe der Sollzinsen aller Darlehen ohne Kontokorrent, je Planjahr um den Grenzsteuersatz entlastet: Z_S = Summe über j von Zinsen_j x (1 − s_op(j)). Mit einer Einlage und einem Steuersatz ist das die Formel des Lexikons mit EW für Z und EK für D. g > k genau dann, wenn ΔEW > 0. Ohne Fremdkapital ist g = r. Ist a_0 ≤ 0, ist die Kennzahl nicht definiert; ist der Zähler ≤ 0, beträgt sie −100 %. Die Kennzahl steht ab der Vollkalkulation auf dem vollen Blatt. **Neue Festlegung (NF-28)** sind die Erweiterung auf Z und D, der Referenzzinsfuß aus dem Finanzplan der Alternative und die Entlastung je Jahr.
*Beispiel (RF-05):* Z_S = 134.171,48 x 0,7 = 93.920,04 Euro; g = ((584.366,28 − 400.000 + 93.920,04 + 1.100.000) / 1.100.000)^(1/5) − 1 = 4,61 %; k = 2,14 %.

**R-10.12 Amortisationsdauer (`MA-027`).** Voraussetzung ist ein Wertpfad: der Verkaufserlös nach R-8.5 bei gedachtem Verkauf am Ende jedes Jahres t. Vermögen_t = Guthaben_t − Kontokorrent_t + Verkaufserlös_t − Restschulden_t − Vorfälligkeit_t − Rückzahlung von Fördermitteln_t − Steuer auf den gedachten Verkauf_t. Vergleich_t ist der Bestand der Unterlassensalternative am Ende von t (R-9.3), mit denselben Einlagen und Entnahmen. Die Amortisationsdauer ist das kleinste t*, für das Vermögen_t ≥ Vergleich_t für alle t von t* bis n gilt; gibt es keines, lautet das Ergebnis „im Planungszeitraum nicht erreicht“. Die andere Lesart (erstes t mit Vermögen_t ≥ Summe der Einlagen) ist umschaltbar. Die Kennzahl steht ab der Vollkalkulation zur Verfügung, weil die Grobkalkulation keinen Wertpfad führt. **Neue Festlegung (NF-29)** ist die Spiegelung der Einlagen und Entnahmen in der Vergleichsgröße.
*Beispiel (RF-05; Wertpfad der Nachrechnung: Verkaufserlös linear von 1,00 auf 1,15 Mio. Euro):* Vermögen bei gedachtem Verkauf in den Jahren 1 bis 3: 354.180,00 / 409.664,52 / 466.495,06 Euro; Alternative 405.600,00 / 411.278,40 / 417.036,30 Euro; Eigenkapital 400.000 Euro. Voreinstellung: drei Jahre; andere Lesart: zwei Jahre.

**R-10.13 Anfangsrendite und Faktor.** Bezug ist das erste Jahr der Vollvermietung (`GIF-KENNZAHLENKATALOG`; im Kataster nur als Sekundärquelle belegt, Kapitel 17).

    Einstiegsfaktor      = Kaufpreis / Jahressollmiete            (Neubau: Gesamtkosten ohne Bauzeitzinsen)
    Bruttoanfangsrendite = Jahressollmiete / Kaufpreis
    Nettoanfangsrendite  = Reinertrag / (Kaufpreis + Erwerbsnebenkosten)   (Neubau: / Gesamtkosten)
    Ausstiegsfaktor      = Verkaufspreis / Jahressollmiete des Folgejahres = E-47

Einstiegs- und Ausstiegsfaktor stehen nebeneinander auf dem Blatt; liegt der Ausstiegsfaktor über dem Einstiegsfaktor, greift die Warnschwelle H-20.
*Beispiel (RF-11):* 2.400.000 / 134.640 = 17,83; Bruttoanfangsrendite 5,61 %; Nettoanfangsrendite 103.035,24 / 2.640.000 = 3,90 %; Ausstiegsfaktor 18,00.

**R-10.14 Schuldendienstdeckung.** Deckung einer Zeitspanne = Reinertrag / Kapitaldienst. Kapitaldienst = Zinsen + planmäßige Tilgung + laufende Beiträge aller Darlehen. Nicht zum Kapitaldienst gehören Ablösung, Vorfälligkeit, freie Tilgung und der Kontokorrent. Ohne Kapitaldienst ist die Kennzahl nicht definiert und wird als „kein Kapitaldienst“ ausgewiesen. Auf dem Blatt der Grobkalkulation steht die Deckung im ersten Jahr der Vollvermietung; der Kern rechnet sie für jedes Planjahr. **Neue Festlegung (NF-30)** für die Abgrenzung.
*Beispiel (RF-05):* Testfall 1,3095 / 1,3357 / 1,3624 / 1,3897 / 1,4175; mit der Ablösung im Nenner fiele sie im Verkaufsjahr auf 0,09. *Beispiel (RF-11):* Im Basisfall 1,200 im Jahr 1, steigend auf 1,582 im Jahr 10 und 1,833 nach dem Anschluss; im kombinierten Stressfall 1,147 im Jahr 1 und 1,442 im Jahr 11.

**R-10.15 Beleihungsauslauf.** Beleihungsauslauf = (Bankdarlehen + übrige Darlehen) / Wertansatz, zum Stichtag, beim Neubau zum Ende der Bauzeit.
*Beispiel (RF-11):* 1.431.044,99 / 2.400.000 = 59,63 %; beim tragbaren Preis im Stressfall bindet die Quote und der Auslauf ist 65,00 %.

**R-10.16 Restwertanteil.** Restwertanteil = Restwertbeitrag / EW mit Restwertbeitrag = Verkaufserlös − Ablösung − Vorfälligkeit − Rückzahlung von Fördermitteln − Steuer auf den Verkaufsgewinn. Die Steuer auf den Verkaufsgewinn ist die Steuer des letzten Planjahres abzüglich der Steuer, die ohne Verkaufsgewinn anfiele. Bei EW ≤ 0 ist die Kennzahl nicht definiert. Sie kann über 100 % liegen, wenn der laufende Betrieb Geld gekostet hat. Die Warnschwelle ist H-20. **Neue Festlegung (NF-31).**
*Beispiel (RF-05):* (1.150.000 − 624.171,48) / 584.366,28 = 89,98 %. *Beispiel (RF-11):* (3.276.829,52 − 1.034.515,79 − 272.999,11) / 2.374.377,18 = 82,94 %.

**R-10.17 Eigenkapital und Nachschussbedarf.** Nötiges Eigenkapital = Summe der Einlagen der Investitionsphase (Zeitpunkt 0 bis Ende der Bauzeit) einschließlich der Nachschüsse für Zinsen und Beiträge der Bauzeit. Nachschussbedarf = Summe der Nachschüsse nach der Investitionsphase.
*Beispiel (RF-11):* 1.208.955,01 Euro Eigenkapital, 91.529,75 Euro Nachschussbedarf. *Beispiel (RF-12):* 4.137.285,60 Euro, davon 83.180,59 Euro für Zinsen der Bauzeit.

**R-10.18 Interner Zinsfuß.** Der interne Zinsfuß der Eigenkapitalreihe (−e_u, +a_u, in N zuzüglich EW) ist jeder effektive Jahressatz x mit Summe über u von Zahlung_u x (1 + x)^(−u/p) = 0. Der Kern zählt die Vorzeichenwechsel der Reihe. Kein Wechsel: keine Lösung. Ein Wechsel: genau eine Lösung. Mehr als ein Wechsel: Der Kern sucht alle Lösungen zwischen −99 % und +1.000 % auf einem Raster von 2.000 Schritten mit Bisektion an jedem Vorzeichenwechsel, meldet alle (M-26) und verweist auf die VOFI-Rendite. Der interne Zinsfuß ist eine Nebenangabe und nie Entscheidungsgröße.
*Beispiel (RF-05):* Eigenkapitalreihe des Testfalls: 7,876 %, gleich der VOFI-Rendite. *Beispiel (RF-14, Lehrbuch):* −1.000 / +5.000 / −6.000: zwei Wechsel, Lösungen 100 % und 200 %.

**R-10.19 Kapitalwert.** Der Kapitalwert ist in Teil 1 keine Kennzahl des Blatts; er dient der Probe P-13 und dem Plausibilitätstest R-15.4.

## 11 Grobkalkulation

**R-11.1 Ablauf.** Eine Grobkalkulation läuft in dieser Reihenfolge: (1) Eingabeprüfung (R-3.7); (2) Ertragsreihen nach Kapitel 6; (3) Bemessung nach R-11.2 mit dem Bankdarlehen nach R-5.12; (4) Mittelabruf nach R-11.3; (5) Abschreibungsplan (R-7.3) und Verkauf (Kapitel 8); (6) Finanzplan (Kapitel 4) und Unterlassensalternative (Kapitel 9); (7) Kontrollsummen (Kapitel 13); (8) Kennzahlen (Kapitel 10) und Blatt (R-11.12). Dasselbe läuft für den kombinierten Stressfall (R-11.8). Der höchste tragbare Preis (R-11.4) wiederholt die Schritte 2 bis 8 für andere Preise.

**R-11.2 Bemessung.** Vor dem Finanzplan stehen fest: Erwerbsnebenkosten = runde(Preis x E-11); Baukosten = runde(Brutto-Grundfläche x Kostenkennwert); Reinertrag im ersten Jahr der Vollvermietung (R-6.12); übrige Darlehen und ihr Kapitaldienst; Zuschüsse und Mindesteigenkapital (R-11.14); der Mittelbedarf M = Preis + Erwerbsnebenkosten + Baukosten + Investitionsstau zum Stichtag + einbehaltene Entgelte; der Wertansatz W. **Neue Festlegung (NF-32):** Beim Neubau enthalten Mittelbedarf und Wertansatz die Zinsen und Beiträge der Bauzeit nicht; diese trägt das Eigenkapital als Nachschuss im Monat ihrer Fälligkeit. Das vermeidet den Zirkelbezug zwischen Darlehenshöhe und Bauzeitzinsen und ist die vorsichtige Lesart; die Einstellung einer Eigenkapitalquote auf die Gesamtkosten einschließlich Bauzeitzinsen regelt Teil 2.
*Beispiel (RF-11):* M = 2.400.000 + 240.000 = 2.640.000 Euro; A = 1.560.000, B = 1.431.044,99, C = 2.640.000; Bankdarlehen 1.431.044,99 Euro, es bindet (b); Eigenkapital 1.208.955,01 Euro.

**R-11.3 Mittelabruf.** Der Bedarf jedes Monats der Investitionsphase wird in fester Reihenfolge gedeckt: zuerst das Eigenkapital bis zu seinem Betrag nach R-5.12, dann Förderdarlehen und Zuschuss im Verhältnis ihrer Beträge, zuletzt das Bankdarlehen. Beim ersten Abruf der Fördermittel erhöhen die einbehaltenen Entgelte den Bedarf. Beim Ankauf fällt der ganze Bedarf zum Stichtag an; ein übernommenes Darlehen gilt als zum Stichtag ausgezahlt. Beim Neubau fallen Grundstück und Nebenkosten zum Stichtag an und die Baukosten in gleichen Monatsraten über die Bauzeit; die letzte Rate nimmt den Rundungsrest. Zinsen und Beiträge der Bauzeit werden über den Ausgleich des Finanzplans zu Nachschüssen (R-4.5). **Neue Festlegung (NF-33):** „Eigenkapital zuerst“ ist die übliche Auflage der Banken; der gleichmäßige Mittelabfluss ist die Standardkurve der Grobkalkulation, die Kurve nach Bauablauf und die Auszahlung der Förderung nach Baufortschritt regelt Teil 2.
*Beispiel (RF-12, Neubau frei finanziert):* Stichtag: 1.296.000,00 Euro aus Eigenkapital. Monate 1 bis 6: je 418.888,89 Euro aus Eigenkapital. Monat 7: 244.771,67 Euro Eigenkapital und 174.117,22 Euro Bankdarlehen. Monat 8: 418.888,89 Euro Bankdarlehen, dazu 580,39 Euro Zins als Nachschuss. Mittelherkunft der Investitionsphase: 4.137.285,60 Euro Eigenkapital und 4.781.894,99 Euro Bankdarlehen; Mittelverwendung: 8.836.000,00 Euro Investition und 83.180,59 Euro Finanzierungskosten (P-04).

**R-11.4 Höchster tragbarer Preis.** Gesucht ist der Kaufpreis, beim Neubau der Grundstückspreis, bei dem die VOFI-Rendite nach Steuern die Zielrendite erreicht:

    r(P) = z,   gerechnet mit L(P) nach R-5.12 und allen übrigen Eingaben unverändert

Vom Preis hängen ab: Erwerbsnebenkosten, Mittelbedarf, Wertansatz, Bankdarlehen, Eigenkapital, Abschreibung und Buchwert; bei Förderung die zuwendungsfähigen Grundstückskosten. Mieten, Kosten und Verkaufspreis hängen nicht vom Preis ab. Der höchste tragbare Preis P* ist der größte Preis in vollen Euro mit r(P*) ≥ z.

**R-11.5 Lösungsverfahren, Eindeutigkeit, Knick.** Suchbereich ist 1 Euro bis H-21 x Jahressollmiete des ersten Jahres der Vollvermietung (Voreinstellung im Referenzrechner: das Hundertfache). Der Kern wertet r(P) − z an 41 gleichmäßig verteilten Stützstellen aus und verfeinert jeden Vorzeichenwechsel durch ganzzahlige Bisektion bis auf einen Euro (R-11.10). Ausgegeben wird der kleinste Preis, an dem das Vorzeichen von „erreicht“ nach „verfehlt“ wechselt; gibt es weitere Wechsel, meldet der Kern sie (M-34). Ist die Zielrendite schon bei einem Euro verfehlt, gibt es keinen tragbaren Preis (M-32); ist sie an der Obergrenze noch erreicht, meldet der Kern das (M-33). Preise, bei denen R-5.12 die Meldung M-22 ergibt, gelten als unterhalb des zulässigen Bereichs. **Neue Festlegung (NF-34):** Die ganzzahlige Suche liefert auf jedem Rechner denselben Preis.
Die Rendite fällt mit dem Preis streng: Der Endwert fällt, und das Eigenkapital steigt. L(P) ist stetig und hat Knicke, wo die bindende Grenze wechselt; am Knick ist die Rendite stetig, und ihre Steigung ist auf beiden Seiten negativ (Prüfrunde 5, Finanzmathematiker). Der Kern verlässt sich darauf nicht, sondern sucht mit dem Raster.
*Beispiel (RF-11):* P* = 2.425.585 Euro; dort ist r = 5,000 %, einen Euro darüber liegt r unter 5 % (P-14); es gibt genau einen Vorzeichenwechsel. Der Knick zwischen (a) und (b) liegt bei 1.431.044,99 / 0,65 = 2.201.607,68 Euro: Die Rendite beträgt 6,7042 / 6,6408 / 6,5775 / 6,4983 / 6,4199 % bei −20.000 / −10.000 / 0 / +10.000 / +20.000 Euro um den Knick; die Steigung ist −6,33 Basispunkte je 10.000 Euro links und −7,92 rechts. Zwischen 1,5 und 3,6 Mio. Euro fällt die Rendite in jedem Schritt von 100.000 Euro.

**R-11.6 Eigenkapital als zweite Grenze.** Ist das verfügbare Eigenkapital E-60 angegeben, ist P_EK der größte Preis in vollen Euro, bei dem das nötige Eigenkapital (R-10.17) E-60 nicht übersteigt; gesucht wird wie in R-11.5. Der höchste tragbare Preis ist dann min(P*; P_EK). Der Eigenkapitalbedarf steigt streng mit dem Preis; P_EK ist eindeutig.
*Beispiel (RF-11):* Mit 900.000 Euro verfügbarem Eigenkapital ist P_EK = 2.000.000 Euro (2.200.000 Mittelbedarf, 1.300.000 Darlehen nach der Beleihungsquote); es bindet das Eigenkapital, nicht die Rendite.

**R-11.7 Ausgabe.** Zum höchsten tragbaren Preis weist das Blatt aus: den Preis; die bindende Grenze (Rendite oder Eigenkapital); das nötige Eigenkapital; welche der drei Grenzen aus R-5.12 das Darlehen bestimmt; die Schuldendienstdeckung; alles im Basisfall und im kombinierten Stressfall. Nebenangabe ist der Preis, bis zu dem die Beleihungsquote das Darlehen bestimmt (der Knick B / β); er ist keine Preisgrenze.
*Beispiel (RF-11):* Basisfall 2.425.585 Euro, Rendite bindet, Darlehen 1.431.044,99 Euro nach (b), Eigenkapital 1.237.098,51 Euro. Stressfall 2.128.948 Euro, Rendite bindet, Darlehen nach (a), Deckung im Stressfall 1,1863.

**R-11.8 Kombinierter Stressfall.** Der kombinierte Stressfall ändert gleichzeitig die Größen der Tabelle um die ermäßigten Höhen H-06; eine Größe, die beim Vorhaben nicht wirkt, entfällt.

| Größe | Änderung | wirkt bei |
|---|---|---|
| Anschlusszins | Aufschlag in Prozentpunkten | Haltedauer über der Zinsbindung |
| Mietausfallquote | Aufschlag in Prozentpunkten | immer |
| Mietsteigerung | Abschlag in Prozentpunkten | immer |
| Instandhaltungskosten | Aufschlag in % | immer |
| Verkaufsfaktor | Abschlag in % | immer |
| Baukosten | Aufschlag in % | Neubau |
| Bauzeit | Verlängerung in Monaten | Neubau |

Das Bankdarlehen wird nicht neu bemessen: Es gilt das Darlehen, das R-5.12 beim selben Preis aus den Basisannahmen ergibt. Förderdarlehen und Zuschuss bleiben ebenfalls auf dem Stand des Basisfalls; Mehrkosten trägt das Eigenkapital. Ausgewiesen werden alle Kennzahlen des Blatts im Stressfall, darunter die Schuldendienstdeckung. Der tragbare Preis im Stressfall löst r_Stress(P) = z mit L_Basis(P). **Neue Festlegung (NF-35):** Die Bank bemisst ihr Darlehen heute aus den Basisannahmen; der Stress trifft das Vorhaben danach.
*Beispiel (RF-11; Höhen als Annahme: Anschlusszins +1 Prozentpunkt, Mietausfall +2 Prozentpunkte, Mietsteigerung −0,5 Prozentpunkte, Instandhaltung +10 %, Verkaufsfaktor −10 %):* Endwert 1.900.792,30 statt 2.374.377,18 Euro, Endwertdifferenz 342.583,38 statt 825.606,46 Euro, Rendite 3,178 % statt 5,162 %, Deckung 1,1471 statt 1,2000, Bankdarlehen unverändert 1.431.044,99 Euro. *Beispiel (RF-12; dazu Baukosten +5 %, Bauzeit +3 Monate):* Eigenkapital 4.524.360,81 statt 4.137.285,60 Euro, Rendite 3,048 % statt 5,307 %.

**R-11.9 Zielwertsuche: zulässige Eingaben.** Die Zielwertsuche sucht den Wert einer Eingabe, bei dem die VOFI-Rendite die Zielrendite erreicht, wahlweise bei dem die Endwertdifferenz null ist. Zugelassen und so gekennzeichnet sind: Kaufpreis, Grundstückspreis, Marktmiete, Ist-Miete, Investitionsstau, Verkaufsfaktor, Zins des Bankdarlehens, Kostenkennwert. Nicht zugelassen sind Auswahlfelder (Steuerstatus, Verlustverrechnung), ganzzahlige Zeitgrößen (Haltedauer, Zinsbindung, Bauzeit) und alle Vorgaben des Hauses; der Kern gibt dafür M-30 zurück. **Neue Festlegung (NF-36).** Suchbereich, Auflösung und Rasterzahl je Eingabe sind H-21; Vorschlag der Auflösung: Preise 1 Euro, Mieten 0,01 Euro je m², Faktoren 0,01, Zinsen 0,001 Prozentpunkte, Investitionsstau 100 Euro.

**R-11.10 Zielwertsuche: Verfahren.** Gesucht wird auf dem Gitter der Auflösung im Bereich [u; o]. Der Kern wertet die Zielfunktion f an den Rasterstellen aus (f ≥ 0 heißt „Ziel erreicht“), verfeinert jeden Vorzeichenwechsel zwischen zwei Rasterstellen durch ganzzahlige Bisektion und gibt zu jedem Wechsel den letzten Gitterwert aus, bei dem das Ziel noch erreicht ist, mit der Richtung des Wechsels. Ergebnis: „eine Lösung“, „k Lösungen“ mit allen Werten, „keine Lösung: Ziel im ganzen Bereich erreicht“ oder „keine Lösung: Ziel im ganzen Bereich verfehlt“; dazu Bereich und Rasterweite. Zwei Lösungen, die näher beieinander liegen als die Rasterweite, findet das Verfahren nicht; die Ausgabe nennt deshalb die Rasterweite („Lösungen im Bereich [u; o] bei Rasterweite x“).
*Beispiel (RF-11):* Nötige Marktmiete bei 2,6 Mio. Euro Kaufpreis: 9,96 Euro je m² (Bereich 6 bis 20 Euro). Tragbarer Investitionsstau bei 2,4 Mio. Euro: 147.600 Euro. Kritischer Verkaufsfaktor: 17,69. Bereich 6 bis 9 Euro: „keine Lösung: Ziel im ganzen Bereich verfehlt“. Für die nicht monotone Prüffunktion (x − 3) x (x − 7) meldet das Verfahren beide Lösungen, 3,00 und 7,00. Die Eingaben der Grobkalkulation wirken alle monoton; mehrere Lösungen treten in 1a nur über die Prüffunktion auf.

**R-11.11 Vergleich zweier Fassungen.** Zwei Fassungen sind zwei vollständige Aufträge, die unabhängig voneinander gerechnet werden. Der Vergleich stellt je Kennzahl des Blatts Wert A, Wert B und die Differenz B − A nebeneinander; Renditen und Quoten in Prozentpunkten. Er setzt voraus, dass beide Fassungen alle Kontrollsummen bestehen und mit derselben Version des Kerns gerechnet sind; unterschiedliche Regelstände werden ausgewiesen.
*Beispiel (RF-11):* Ankauf frei gegen denselben Ankauf mit 40 % gebundener Fläche und übernommenem Darlehen: Endwertdifferenz 825.606,46 gegen 601.639,51 Euro, Differenz −223.966,95 Euro. *Beispiel (RF-12):* Neubau frei finanziert gegen gefördert, je 20 Jahre: Differenz der Endwertdifferenz −5.249.273,41 Euro.

**R-11.12 Verkürztes Kennzahlenblatt.** Das Blatt der Grobkalkulation zeigt im Basisfall und im kombinierten Stressfall: Endwertdifferenz (R-10.2); VOFI-Rendite, Vergleichsrendite, Abstand zur Zielrendite (R-10.5, R-10.8); Endwertüberschuss (R-10.9); Restwertanteil (R-10.16); Einstiegs- und Ausstiegsfaktor, Brutto- und Nettoanfangsrendite (R-10.13); Beleihungsauslauf (R-10.15); Schuldendienstdeckung im ersten Jahr der Vollvermietung (R-10.14); nötiges Eigenkapital und Nachschussbedarf (R-10.17); den höchsten tragbaren Preis mit bindender Grenze (R-11.7). Dazu: die Meldungen des Laufs; Abweichungen von den Vorgaben des Hauses mit Begründung (R-3.2); die Kennungen der Modellannahmen, die gewirkt haben; Standkennung, Regelstand und Version des Kerns. Das Blatt erscheint nur, wenn alle Kontrollsummen bestanden sind (R-13.1).

**R-11.13 Haltedauertabelle.** Statt einer Zielwertsuche auf die Haltedauer rechnet der Kern die Grobkalkulation für jede Haltedauer eines Bereichs und zeigt Endwert, Endwertdifferenz und Rendite je Jahr.
*Beispiel (RF-11):* Haltedauer 8 bis 13 Jahre: 4,768 / 4,970 / 5,111 / 5,142 / 5,162 / 5,173 %. Bei der Privatperson springt die Rendite zwischen Jahr 10 und 11 (R-7.11).

**R-11.14 Grobförderung im Neubau.** Die Grobförderung der NBank ist eine Näherung und im Ergebnis so gekennzeichnet. Aus den Katalogwerten KAT-10 und den Eingaben E-28 bis E-30:

    zuwendungsfähige Kosten = min(Baukosten; Bemessungsgrenze x Wohnfläche)
                            + min(Grundstückspreis + Erwerbsnebenkosten; Bodenrichtwert x Grundstücksfläche)
    Förderdarlehen       = runde(Darlehensquote x zuwendungsfähige Kosten)
    Zuschuss             = runde(Zuschussquote x zuwendungsfähige Kosten)
    Mindesteigenkapital  = runde(Eigenmittelquote x zuwendungsfähige Kosten)
    einbehaltene Entgelte = runde(Förderdarlehen x Entgeltsatz) + runde(Zuschuss x Entgeltsatz)

Es gelten `MA-021` (Kosten einschließlich nicht abziehbarer Vorsteuer), `MA-005` (keine Finanzierungskosten), `MA-004` (Eigenmittel aus Eigenkapital), `MA-002` und `MA-003` (R-5.11), `MA-017` (R-8.7, R-8.8) und `MA-026` (R-5.12). Miete nach R-6.5 und R-6.7. **Neue Festlegung (NF-38):** Der Kostenkennwert E-25 umfasst die Kostengruppen 200 bis 700; Grundstückskosten sind Preis und Erwerbsnebenkosten; der Zuschuss mindert die Abschreibungsgrundlage des Gebäudes; zinslose Zeit, Tilgung und Bindung zählen ab dem Monat nach der Bauzeit.
*Beispiel (RF-12; Werte nach Bericht Anhang C.1 für Einkommensgruppe B als Annahme, Bodenrichtwert 400 Euro je m²):* Baukosten 7.540.000 Euro unter der Bemessungsgrenze; Grundstück 1.296.000 Euro, begrenzt auf 2.500 m² x 400 Euro = 1.000.000 Euro; zuwendungsfähig 8.540.000 Euro. Förderdarlehen 5.124.000,00, Zuschuss 1.708.000,00, Mindesteigenkapital 1.708.000,00, Entgelte 64.050,00 Euro; Mittelbedarf 8.900.050,00 Euro. Reinertrag bei 8,20 Euro Eingangsmiete 149.080,50 Euro; Kapitaldienst des Förderdarlehens 147.340,45 Euro. Grenzen: A = 619.400,00, B negativ, C = 360.050,00; Bankdarlehen null mit Meldung M-21; Eigenkapital 2.084.407,23 Euro einschließlich 16.357,23 Euro Beiträge der Bauzeit; Deckung 1,0118. Verkauf nach 20 Jahren: Endwert 3.265.245,99 Euro, Endwertdifferenz 463.572,57 Euro, Rendite 2,273 %. Nach der anderen Lesart von `MA-026` gäbe die Bank die Restfinanzierung von 360.050,00 Euro.

## 12 Rundung und Genauigkeit

**R-12.1 Dezimalrechnung.** Geldbeträge sind exakte Dezimalzahlen mit zwei Nachkommastellen; Gleitkommazahlen kommen im Rechenkern nicht vor. Zwischengrößen werden mit mindestens 28 gültigen Dezimalstellen geführt. Die Regeln dieses Kapitels sind so gefasst, dass jedes Ergebnis in Cent von der Stellenzahl darüber nicht abhängt: Jede Größe, die in einen Geldbetrag eingeht, ist ein exaktes Produkt oder wird vorher nach R-12.4 gerundet.

**R-12.2 Rundungsmodi.** Im Modus „Cent“ (Produkt) gelten die Regeln R-12.3 bis R-12.5. Im Modus „keine“ (Lehrbuchvergleich im Jahresmodus) wird nichts gerundet; verglichen wird der gerundete Wert mit dem veröffentlichten.

**R-12.3 Rundung je Zahlungsart.** Kaufmännisch heißt: auf Cent, ab der Hälfte von null weg.

| Zahlungsart | Regel |
|---|---|
| Darlehen | Zins und Beitrag je Rate kaufmännisch; die Rate einer Annuität einmal kaufmännisch; je Darlehen umstellbar (`MA-013`, R-5.3) |
| Darlehenshöhe nach R-5.12 | auf Cent abgerundet, zur sicheren Seite |
| Geldanlage, Kontokorrent, Unterlassensalternative | je Zinsbuchung kaufmännisch |
| Mieten, Bewirtschaftung, CO2-Kosten, Erbbauzins | je Zahlung kaufmännisch; der Index bleibt ungerundet im Sinn von R-12.4 |
| Investition, Maßnahmen, Erwerbsnebenkosten, Baukosten | je Zahlung kaufmännisch; Monatsraten der Baukosten kaufmännisch, die letzte nimmt den Rest |
| Abschreibung | je Planjahr kaufmännisch |
| Steuer in Kurzform | je Steuerart und Planjahr kaufmännisch; Gewerbeertrag vorher auf volle 100 Euro abgerundet (`GEWSTG-11`) |
| Verkaufspreis, Verkaufskosten, Abzüge, Rückzahlungen | je Betrag kaufmännisch |
| Preise der Preissuche | volle Euro (R-11.5) |

*Beispiel (RF-05, RF-06):* Der Endwert des Testfalls bleibt mit Rundung je Zahlung bei 584.366,28 Euro (ungerundet 584.366,2816); das Guthaben im Jahr 4 ist 45.263,83 statt 45.263,84 Euro, die Endwertdifferenz 155.571,22 statt 155.571,23 Euro. In der Variante Nachschuss verschiebt die Rundung den Endwert auf 636.495,81 Euro. Diese Werte sind als Sollwerte der Tests festgeschrieben.

**R-12.4 Sätze, Faktoren, Indexstände.** Abgeleitete Periodensätze (R-2.6), Vergleichsfaktoren (R-10.4) und Indexstände (R-6.1) werden kaufmännisch auf zwölf Nachkommastellen gerundet und dann als exakte Dezimalzahl verwendet. Wurzeln werden dafür mit mindestens 20 gültigen Nachkommastellen gebildet. Eingegebene Sätze werden nicht gerundet. **Neue Festlegung (NF-37):** Der Bericht verlangt, den Index ungerundet fortzuschreiben; zwölf Stellen ändern keinen Cent (bei 10 Mio. Euro weniger als ein Tausendstel Cent je Zahlung) und machen das Ergebnis auf jedem Rechner gleich.

**R-12.5 Reihenfolge der Rechenschritte.** Erst alle Multiplikationen, dann die Division, zuletzt die Rundung: Zins = runde(Restschuld x Satz / p), nicht Restschuld x runde(Satz / p). Summen werden aus gerundeten Einzelbeträgen gebildet, nie selbst gerundet; der Jahreswert ist die Summe der Monatswerte (P-09).

**R-12.6 Kennzahlen.** Renditen, Faktoren, Quoten und Deckungen werden nicht gerundet weitergerechnet. Potenzen und Wurzeln der Kennzahlen werden mit der vollen Rechengenauigkeit gebildet.

**R-12.7 Darstellung.** Geldbeträge mit zwei Nachkommastellen oder in vollen Euro, Renditen mit zwei, in Prüfunterlagen mit drei Nachkommastellen, Faktoren und Deckungen mit zwei, jeweils kaufmännisch gerundet, im deutschen Zahlformat. Die Darstellung wirkt nie auf die Rechnung zurück.

## 13 Kontrollsummen und Proben

**R-13.1 Grundsatz.** Der Kern gibt Kennzahlen und Blatt nur zurück, wenn alle Kontrollsummen des Laufs bestanden sind. Sonst gibt er die Meldung M-10 mit der Liste der verletzten Proben zurück: Kennung, Periode oder Objekt, Abweichung. Eine verletzte Probe ist ein Fehler des Kerns oder des Auftrags, nie ein Ergebnis.

**R-13.2 Toleranz.** Im Rundungsmodus „Cent“ gelten P-01 bis P-10 und P-12 exakt, mit Abweichung null. Im Modus „keine“ gilt eine Rechentoleranz von 1E-30.

**R-13.3 Liste der Proben.**

| Kennung | Probe | Formel |
|---|---|---|
| P-01 | Finanzierungssaldo | je Periode: Saldo + Nachschuss − Anlage + Aufnahme = 0 (R-4.4) |
| P-02 | Kreditprobe | je Darlehen und Periode: Summe der Auszahlungen + kapitalisierte Zinsen − Tilgungen − Tilgungszuschüsse − Ablösung = Restschuld; nach der Ablösung ist jede Restschuld null. Einbehaltene Beträge mindern den Zufluss, nicht die Schuld; kapitalisierte Zinsen gibt es erst in Teil 2 |
| P-03 | Bestandsprobe | je Periode: Veränderung des Bestandssaldos = originäre Zahlungen + Einlagen + Nachschüsse − Entnahmen − Finanzierungskosten + Habenzinsen − Steuer + Tilgungszuschüsse − einbehaltene Beträge; Finanzierungskosten sind Zinsen, Kontokorrentzinsen, Beiträge und Vorfälligkeit |
| P-04 | Mittelherkunft gleich Mittelverwendung | über die Investitionsphase: Eigenkapital + Auszahlungen der Darlehen + Zuschüsse = Investition + Erhaltung zum Stichtag + einbehaltene Beträge + Finanzierungskosten abzüglich Habenzinsen + laufende Zahlungen der Bauzeit + Guthaben abzüglich Kontokorrent am Ende der Phase |
| P-05 | Restwertprobe | gebuchter Verkaufserlös = Preis aus dem Maßstab − Verkaufskosten − ausstehender Investitionsstau (R-8.5) |
| P-06 | Investitionsstau | je Maßnahme: gezahlter Anteil + abgezogener Anteil = 100 % |
| P-07 | Zuschussprobe | je Zuschuss: erhalten − zurückgezahlt = Betrag, der nach der Rückzahlungsregel verbleibt (R-8.7) |
| P-08 | Abschreibungsprobe | Summe der Abschreibungen ≤ Abschreibungsgrundlage; Restbuchwert = Boden + Grundlage − Summe der Abschreibungen |
| P-09 | Verdichtung | Summe der Periodenwerte = Jahreswert, für Zahlungen (R-2.3) |
| P-10 | Spiegelprobe | Einlagen und Entnahmen der Unterlassensalternative = saldierte Reihe der Investition, je Periode (R-9.2) |
| P-11 | Renditeprobe | r > r_U genau dann, wenn ΔEW > 0, sofern mindestens einer der beiden Zähler positiv ist; sonst sind beide Renditen −100 % (R-10.6, R-10.7) |
| P-12 | Bankdarlehen | 0 ≤ L ≤ max(0; min(A; B; C)); Eigenkapital ≥ Mindesteigenkapital (R-5.12) |
| P-13 | Kapitalwertprobe, nur Testmodus | abgezinste Endwertdifferenz = Kapitalwert der Zahlungsreihe nach Steuern ohne Zinsen. Gilt nur, wenn alle Zinssätze gleich sind, keine Gebühren anfallen, die Steuer im Entstehungsjahr gezahlt und Verluste sofort verrechnet werden und ein einziger Steuersatz gilt; abgezinst wird mit dem Zins nach Steuern |
| P-14 | Preisprobe | r(P*) ≥ z und r(P* + 1 Euro) < z (R-11.4) |

*Beispiele.* P-03 im Testfall, Jahr 1: −675.820,00 − (−700.000,00) = 24.180,00 = 55.000,00 − 28.000,00 + 0,00 − 2.820,00. P-05 erkennt die doppelt gezählte Restschuld (R-8.5). P-07 in RF-12: 1.708.000,00 − 805.200,00 = 902.800,00 Euro verbleiben. P-08 in RF-11: 660.000 + 1.980.000 − 475.200 = 2.164.800 Euro. P-13 (RF-06): Bei einheitlich 4 % sind Kapitalwert und abgezinste Endwertdifferenz je 110.371,99 Euro; im Testfall mit getrennten Sätzen stehen 190.202,20 gegen 145.124,09 Euro, und die Probe darf dort nicht laufen. Ohne die Glieder für Tilgungszuschuss und einbehaltene Beträge meldete P-03 bei richtig gerechneten Förderdarlehen Abweichungen (RF-08).

**R-13.4 Verhalten bei Verletzung.** Der Kern rechnet den Lauf zu Ende, sammelt alle Verletzungen und gibt sie gemeinsam zurück. Die Oberfläche zeigt statt der Ergebnisse die Meldung mit der ersten verletzten Probe; die vollständige Liste geht in das Protokoll. In den Referenzfällen laufen die Proben in jedem gerechneten Finanzplan ohne Verletzung; das Fehlerbild zu P-05 ist ein eigener Test.

## 14 Randfälle und Meldungen

Jeder Randfall hat ein definiertes Ergebnis: einen Wert, den Status „nicht definiert“ oder eine Meldung. Der Kern bricht nie mit einem Rechenfehler ab.

**R-14.1 Zinssatz null.** Bei i = 0 ist die Laufzeitannuität K / m (R-5.4) und die Prozentannuität Nennbetrag x τ / p; Zinsbuchungen sind null. Bei h = 0 und a_L = 0 ist der Endwert der Unterlassensalternative die Summe der Einlagen abzüglich der Entnahmen, die Vergleichsrendite null. Ein sehr kleiner Zins ist kein Randfall: Die Annuitätenformel wird in Dezimalrechnung ausgewertet und bleibt stabil.
*Beispiel (RF-08, RF-14):* 700.000 Euro zinslos über 20 Jahre: Rate 35.000,00 Euro; als Prozentannuität mit 2 %: 1.166,67 Euro im Monat; zu 0,01 % über 20 Jahre: Rate 35.036,76 Euro, Restschuld am Ende null. Testfall mit allen Zinssätzen null: Endwert der Alternative 400.000,00 Euro, Vergleichsrendite 0,000 %, Endwert 676.755,55 Euro.

**R-14.2 Eigenkapital null.** Ohne Einlage ist die Rendite nicht definiert (M-28); Endwert, Endwertdifferenz und alle übrigen Kennzahlen werden ausgewiesen. Der Endwert der Unterlassensalternative ist null. Das Lehrbuch nennt die Rendite in diesem Fall „unendlich“; das Werkzeug weist keine Zahl aus.
*Beispiel (RF-14):* Testfall ohne Eigenkapital, Kontokorrent unbegrenzt: Endwert 63.947,36 Euro, Rendite nicht definiert.

**R-14.3 Negativer Endwert.** Der Endwert kann negativ sein; dann ist die Endwertdifferenz entsprechend negativ. Die Rendite folgt R-10.7: −100 %, wenn der Zähler nicht positiv ist. Der Restwertanteil ist nicht definiert. Alle Kontrollsummen gelten unverändert.
*Beispiel (RF-14):* Testfall mit Verkauf zu 500.000 Euro: Endwert −65.633,72 Euro, Rendite −100 %.

**R-14.4 Haltedauer endet vor der Vollvermietung.** Beim Neubau muss die Haltedauer mindestens bis zum Ende des ersten Jahres der Vollvermietung reichen: N ≥ Bauzeit + p, im Stressfall mit der verlängerten Bauzeit. Sonst gibt es keinen Reinertrag für R-5.12 und keinen Verkauf eines vermieteten Objekts: Meldung M-23, keine Kennzahlen.
*Beispiel (RF-14):* Bauzeit 18 Monate, Haltedauer 2 Jahre: M-23. Haltedauer 3 Jahre: gerechnet, Endwert 4.599.296,28 Euro.

**R-14.5 Verkauf im ersten Jahr.** n = 1 ist zulässig. Die Steuer des einzigen Planjahres enthält den Verkaufsgewinn; reicht die Zinsbindung über das Jahr, fällt Vorfälligkeit an (R-5.16).
*Beispiel (RF-14):* Ankauf mit Verkauf nach einem Jahr: Endwert 938.499,02 Euro, Rendite −22,371 %, Vorfälligkeit 126.170,42 Euro.

**R-14.6 Maßnahme nach dem Verkauf.** Liegt das Jahr der Ausführung nach der Haltedauer, wird die Maßnahme nicht gezahlt, sondern vom Verkaufserlös abgezogen (R-8.4).

**R-14.7 Überfinanzierung.** Übersteigen übrige Darlehen, Zuschüsse und Mindesteigenkapital den Mittelbedarf (C < 0 in R-5.12), rechnet der Kern nicht: Meldung M-22.
*Beispiel (RF-14):* Übernommenes Darlehen 3,0 Mio. Euro bei 2,64 Mio. Euro Mittelbedarf: M-22.

**R-14.8 Kein Ertrag, kein Kapitaldienst.** Bei einer Mietausfallquote von 100 % ist der Reinertrag negativ; das Bankdarlehen ist null, es bindet (b), und der Kern meldet M-21. Die Schuldendienstdeckung ist ohne Kapitaldienst nicht definiert. Die laufenden Kosten werden zu Nachschüssen.
*Beispiel (RF-14):* Ankauf mit 100 % Mietausfall: Bankdarlehen 0,00 Euro, Nachschussbedarf 514.035,60 Euro, alle Kontrollsummen bestanden.

**R-14.9 Kein tragbarer Preis.** Erreicht die Rendite die Zielrendite bei keinem Preis des Suchbereichs: M-32. Erreicht sie sie im ganzen Suchbereich: M-33 mit der Obergrenze.
*Beispiel (RF-14):* Investitionsstau von 6 Mio. Euro zum Stichtag: M-32. Zielrendite −50 %: M-33.

**R-14.10 Interner Zinsfuß.** Nach R-10.18: keine Lösung ohne Vorzeichenwechsel, alle Lösungen bei mehreren.

**R-14.11 Langer Zeitraum.** Der Kern rechnet 42 Jahre im Monatsraster (504 Perioden). Ist die Abschreibungsgrundlage aufgebraucht, ist die Abschreibung null. Nach dem Ende der Bindung fällt keine Rückzahlung des Zuschusses an. Nach der zinslosen Zeit trägt das Förderdarlehen den Zins nach `MA-003`.
*Beispiel (RF-14, geförderter Neubau über 42 Jahre):* letzte Abschreibung im Planjahr 35; erster Zins auf das Förderdarlehen im Planjahr 37 (zinslose Zeit 35 Jahre ab dem Monat nach der Bauzeit); Ablösung des Förderdarlehens am Ende 182.998,38 Euro; Rückzahlung des Zuschusses null; Endwert 13.486.156,44 Euro, Rendite 4,548 %; alle Kontrollsummen bestanden.

**R-14.12 Jahresmodus und Monatsraster.** Beide Raster sind für jedes Vorhaben rechenbar und liefern verschiedene Werte (R-2.2). Sollwerte der Tests gelten je Raster.

**R-14.13 Meldungen.**

| Kennung | Art | Auslöser | Folge |
|---|---|---|---|
| M-10 | Fehler | eine Kontrollsumme ist verletzt (R-13.1) | keine Ergebnisse |
| M-20 | Eingabe | Wert außerhalb des zulässigen Bereichs (R-3.7) | keine Ergebnisse |
| M-21 | Hinweis | Reinertrag trägt nach der Mindestdeckung kein Bankdarlehen (B ≤ 0), etwa weil er den Kapitaldienst der übrigen Darlehen nicht deckt; Bankdarlehen null (R-5.12) | Ergebnis mit Hinweis auf dem Blatt |
| M-22 | Eingabe | übrige Darlehen, Zuschüsse und Mindesteigenkapital übersteigen den Mittelbedarf | keine Ergebnisse |
| M-23 | Eingabe | Haltedauer endet vor dem Ende des ersten Jahres der Vollvermietung | keine Ergebnisse |
| M-24 | Eingabe | Anschlusszins fehlt, obwohl die Haltedauer über die Zinsbindung reicht (R-5.8) | keine Ergebnisse |
| M-25 | Hinweis | Zinsbindung reicht über die Haltedauer; Vorfälligkeit angesetzt (R-5.16) | Ergebnis mit Hinweis |
| M-26 | Hinweis | interner Zinsfuß mehrdeutig; alle Lösungen genannt (R-10.18) | Ergebnis mit Hinweis |
| M-27 | Hinweis | Einlagen nach dem Stichtag und Entnahmen treffen zusammen; die Rendite hängt von ihrem Zeitpunkt ab (R-10.6) | Ergebnis mit Hinweis |
| M-28 | Status | Rendite nicht definiert: keine Einlage (R-10.7) | übrige Kennzahlen gültig |
| M-29 | Status | Rendite −100 %: Zähler nicht positiv (R-10.7) | übrige Kennzahlen gültig |
| M-30 | Eingabe | Zielwertsuche auf eine nicht zugelassene Eingabe (R-11.9) | keine Suche |
| M-31 | Eingabe | Suchbereich leer | keine Suche |
| M-32 | Ergebnis | kein tragbarer Preis: Ziel im ganzen Suchbereich verfehlt | Blatt ohne Preis |
| M-33 | Ergebnis | Ziel im ganzen Suchbereich erreicht; Preis über der Obergrenze | Blatt ohne Preis |
| M-34 | Hinweis | mehrere Lösungen der Preisgleichung; alle genannt (R-11.5) | Ergebnis mit Hinweis |
| M-35 | Hinweis | Vorgabe des Hauses gelockert, abweichende Zielrendite oder Wertansatz über dem Kaufpreis; mit Begründung (R-3.2) | steht auf dem Blatt |
| M-36 | Hinweis | Erhaltungsmaßnahmen der ersten drei Jahre über 15 % der Gebäudeanschaffungskosten; in der Kurzform nicht geprüft (R-6.10) | Ergebnis mit Hinweis |

Im Referenzrechner sind M-21, M-22, M-23, M-24, M-30, M-32, M-33 und M-34 gebaut und geprüft; die übrigen sind Vorgaben an den Kern.

## 15 Referenzfälle

**R-15.1 Grundsatz.** Jeder Referenzfall nennt Eingaben, erwartete Werte und Toleranz. Veröffentlichte Werte (Lehrbuch, IWU, Bericht) stehen als Sollwert im Code des Referenzrechners; verglichen wird mit der Genauigkeit der Quelle. Eigene Fälle stimmen im Rundungsmodus „Cent“ auf den Cent. Renditen stimmen auf die ausgewiesenen Nachkommastellen. Die Fälle werden als automatische Tests des Rechenkerns übernommen; der Kern in Rust muss dieselben Werte liefern.

**R-15.2 Festschreibung eigener Fälle.** Die Sollwerte der eigenen Fälle stehen in `erwartete_werte.json` (207 Werte, festgeschrieben am 2026-11-18 aus dem Referenzrechner). Sie ändern sich nur mit einer Regeländerung in diesem Dokument; `--festschreiben` schreibt sie neu. Damit sie nicht nur sich selbst bestätigen, rechnet `gegenrechnung.py` vier Fälle ohne die Module des Referenzrechners nach (RF-15) und trifft sie auf den Cent.

**R-15.3 Liste.**

| Fall | Inhalt | prüft | Sollwerte (Auswahl) | Toleranz |
|---|---|---|---|---|
| RF-01 | Kirchner, drei Perioden, Projekt A und B (`KIRCHNER-IWU-2004`) | Geldanlage, Kontokorrent, Lehrbuchrendite | Endwert 1.322,48 und 1.249,76 Euro; Rendite 9,76 % und 7,71 %; mit 900 Euro Eigenkapital 1.203,96 Euro und 10,19 % | 0,01 Euro |
| RF-02 | IWU 2013, Mehrfamilienhaus, 25 Jahre (`IWU-2013-ENDBERICHT`, `MA-015`) | lange Laufzeit, Laufzeitannuität, Zuschuss | Endwert 153.032 Euro; Rendite 3,11 %; Mietreihe, Zins, Tilgung, Reinvestition je Jahr | 3,40 Euro je veröffentlichtem Wert; Mietreihe 0,50 Euro, Zins und Tilgung 1 Euro |
| RF-03 | Schulte, Standardbeispiel, vier Finanzpläne (`SCHULTE-IMMOBILIENINVESTITION-2025`) | Finanzplan mit und ohne Steuern, Zwischenfinanzierung, Unterlassensalternative mit zwei Sätzen, Lehrbuchansicht | Endvermögen 10.250 / 10.188 / 9.097 / 9.046; Renditen 5,08 / 4,95 / 2,60 / 2,49 % | jeder veröffentlichte Wert nach Rundung; genaue Werte 0,01 |
| RF-04 | Schulte, Fallbeispiel Bürogebäude | endfällig, Annuität, freie Tilgung, steuerpflichtiger Verkauf | Endvermögen 30.179 / 31.400 / 31.567; Finanzinvestition 30.445; Renditen 3,27 / 3,68 / 3,74 / 3,36 % | Immobilienpläne nach Rundung; Finanzinvestition eine Einheit |
| RF-05 | Testfall (Bericht Anhang A.6) | Rechenreihenfolge, Kennzahlen, Rundung, Restwertprobe | Endwert 584.366,28; Endwertdifferenz 155.571,23; Rendite 7,876 %; Gesamtkapitalrendite 4,61 % gegen 2,14 %; Amortisation 3 Jahre | 0,01 Euro; mit Rundung exakt |
| RF-06 | Varianten des Testfalls | Entnahmen, Kontokorrent, Nachschuss, Saldierung, Basisperiode, Monatsraster, Kapitalwertprobe | 558.656,41 / 561.526,16 / 636.495,82 / 585.086,02 Euro; Renditen 8,123 / 7,246 / 8,028 %; Monatsraster 585.918,72 Euro | 0,01 Euro; mit Rundung exakt |
| RF-07 | mehrere Einlagen und Entnahmen | Eigenschaften der Renditeformel, zwei Sätze, Endwertüberschuss, Monatsverschiebung | siehe R-10.6 und R-10.9 | 0,01 Euro; drei Nachkommastellen |
| RF-08 | Darlehensarten | jede Tilgungsart, Rundung je Rate, Anschluss, Förderdarlehen, Disagio, Tilgungszuschuss, Vorfälligkeit | 528.208,51 / 528.207,91 / 528.208,56 Euro; Raten 90.942 / 89.760 / 104.952 Euro | exakt; Anschluss 1,50 Euro gegen die Gegenrechnung der Prüfrunde 5 |
| RF-09 | Regel des Bankdarlehens | drei bindende Grenzen, Null mit Meldung, andere Lesart `MA-026` | Tabelle in R-5.12 | exakt |
| RF-10 | Steuer in Kurzform je Steuerstatus | Sätze je Jahr, Kürzung, Freibetrag, Anrechnung, privater Verkauf, Verlustvortrag gegen sofort | Tabelle in R-7.9; 29.825 / 15.825 Euro | exakt |
| RF-11 | Grobkalkulation Ankauf | ganzer Ablauf, Stressfall, tragbarer Preis, Zielwertsuche, gebundener Bestand, Vergleich, Haltedauertabelle | Endwert 2.374.377,18 Euro; Rendite 5,162 %; tragbarer Preis 2.425.585 und 2.128.948 Euro | exakt |
| RF-12 | Grobkalkulation Neubau, frei und mit Grobförderung | Mittelabruf, Bauzeitzinsen, Förderdarlehen mit Entgelt und Beitrag, Zuschuss mit Rückzahlung | Endwert 8.956.483,75 Euro; tragbarer Grundstückspreis 1.393.742 Euro; gefördert 3.265.245,99 Euro | exakt |
| RF-13 | Ankauf je Steuerstatus | derselbe Fall mit zehn Ausprägungen: Körperschaft ohne und mit Kürzung und mit sofortiger Verlustverrechnung; Personengesellschaft bei 400 % und 440 % Hebesatz, mit 60 % natürlichen Personen, mit Kürzung; Einzelunternehmen; Privatperson; befreit | Renditen 5,162 / 5,883 / 5,260 / 4,188 / 4,114 / 3,816 / 4,188 / 4,114 / 5,949 / 6,399 % | exakt |
| RF-14 | Randfälle | Kapitel 14 | siehe dort | exakt |
| RF-15 | Gegenrechnung ohne die Module des Referenzrechners | Testfall im Monatsraster, Alternative mit zwei Sätzen, Anlaufverlust, Ankauf Basisfall | 585.918,72 / 443.192,58 / 533.745,69 und 537.232,83 / 2.374.377,18 Euro | exakt |

Zu RF-02: Mit der Mietreihe aus den Annahmen des Berichts endet die Nachrechnung bei 153.031,71 Euro, 29 Cent unter dem veröffentlichten Wert; die größte Abweichung einer Zeile beträgt 0,61 Euro. Mit der veröffentlichten, auf Euro gerundeten Mietreihe sind es 153.028,94 Euro. Die Toleranz von 3,40 Euro der Spezifikation deckt beide Rechenwege; für den ersten genügte ein Euro (Vorschlag in Kapitel 17). Zu RF-04: Die Buchtabelle der Finanzinvestition ist in sich um eine Einheit unstimmig (Quellnotiz 11); gerechnet sind 30.444,24. Für die freie Tilgung gilt Tab. 11 des Lehrbuchs (31.567), nicht die Zusammenfassung in Tab. 15.

**R-15.4 Plausibilitätstest Steuerparadoxon.** Im Standardbeispiel des Lehrbuchs ist der Kapitalwert vor Steuern negativ (−43) und nach Steuern positiv (+8). Der Test rechnet beide Werte mit der Kapitalwertfunktion des Kerns und prüft Vorzeichen und Betrag (RF-03). Er sichert, dass Abschreibung und Zinsabzug in der richtigen Richtung wirken.

**R-15.5 Plausibilitätstest Hebelwirkung.** Liegt die Rendite des Objekts unter dem Kreditzins, steigt die VOFI-Rendite mit dem Eigenkapital (negativer Hebel); liegt sie darüber, fällt sie (positiver Hebel). Der Test prüft beide Richtungen. Standardbeispiel des Lehrbuchs, negativer Hebel: −0,83 / 1,72 / 3,14 / 4,04 / 4,67 / 5,08 / 5,21 / 5,31 % für 3.000 bis 10.000 Eigenkapital (RF-03). Testfall, positiver Hebel: 9,407 / 7,876 / 6,914 / 6,253 % für 300.000 bis 600.000 Euro Eigenkapital bei entsprechend kleinerem Darlehen (RF-05).

**R-15.6 Noch fehlende Fälle.** Für Teil 2 vorgemerkt: KfW-Darlehen mit Tilgungszuschuss im Finanzplan des Neubaus, Auszahlung nach Baufortschritt mit Bereitstellungszinsen, Steuer in Grundform mit Sonderabschreibung, Mieterliste. Das zweite wohnungswirtschaftliche Beispiel bei Kirchner (48 Wohnungen, 50 Jahre) und der zweite Finanzplan des IWU (KfW 70) sind nicht ausgewertet (Quellnotiz 08).

## 16 Offene Punkte

### Was Teil 2 regelt

| Thema | Inhalt | Teilschritt |
|---|---|---|
| Steuer in Grundform | Kalenderjahr, Vorauszahlungen, Abschreibungsplan je Gebäudeteil, Abschreibungswahl, Sonderabschreibung mit De-minimis-Prüfung (`MA-022`, `MA-023`, `MA-029`), Begrenzung der Verlustverrechnung (`MA-010`), Hinzurechnungen, anschaffungsnahe Herstellungskosten, Prüfungen der Befreiung | 1b |
| Neubau | Kosten nach `DIN-276` mit Kostenständen, Mittelabfluss nach Bauablauf, Bauzeitzinsen mit Eigenkapitalquote auf die Gesamtkosten, Bereitstellungszinsen, kapitalisierte Zinsen, Erstvermietung, Liquiditätsplan | 1b-2 |
| KfW | Neubaudarlehen mit Konditionen aus dem Katalog, Tilgungszuschuss, tilgungsfreie Anlaufjahre | 1b-2 |
| NBank in voller Tiefe | Fördermodul, Auszahlung nach Baufortschritt, Entgeltaufrechnung, Renditeprüfung (`MA-001`), Teilförderung (`MA-006`), Antragssicht | 1c |
| Mieterliste und Mietrecht | Miete je Einheit und Vertragsart, Wartefrist, Mietpreisbremse, Modernisierungsumlage, Leerstand mit Fluktuation | 1b-1 |
| Darlehen in voller Tiefe | beliebig viele Tranchen, Zahlungsrhythmus je Tranche, Zinstage, Zinsschadenrechnung der Vorfälligkeit, Kreditkennzahlen je Periode | 1b |
| Kennzahlen des vollen Blatts | Wertpfad, Amortisationsdauer, Gesamtkapitalrendite auf dem Blatt, Kapitalwert, Eigenkapitalvervielfacher, kritische Werte | 1b |
| Risiko | Einzelstressfälle, Sensitivität, Tornado-Diagramm; Simulation mit Prozessdefinition | 1b; Stufe 2 |
| Restwert | Nettoanfangsrendite und Ertragswert als Maßstab; Übernahme von Darlehen und Bindung durch den Käufer (`MA-017`) | 1b; 1c |
| Entnahmen | geplante Ausschüttungen; danach die Entscheidung zu R-10.6, Eigenschaft 6, überprüfen. Kandidat, noch nicht untersucht: Entnahmen zuerst gegen noch nicht zurückgeführte Nachschüsse verrechnen | 1b |

### Wer was klären kann

| Frage | Wer | Regel |
|---|---|---|
| Werte der Vorgaben des Hauses H-01 bis H-23, darunter neu gegenüber der bisherigen Liste: Habenzins kurz und lang, Kontokorrentzins und -linie, Steigerungen, Mietausfallquote, Verkaufskosten, Bewirtschaftungspauschalen, Vorfälligkeitssatz, Voreinstellung der Haltedauer, Anpassungsdauer, Suchbereiche | Auftraggeber | R-3.4 |
| Soll ein Fehlbetrag als Nachschuss aus Eigenkapital erscheinen (Linie null) oder rechnet das Haus mit einer Kontokorrentlinie? | Auftraggeber | R-4.5 |
| Steht „gefördert oder frei finanziert“ am Anfang der Kalkulation? Davon hängt ab, ob R-11.14 in 1a bleibt | Auftraggeber | R-11.14 |
| Begrenzt die Beleihungsquote alle Darlehen, rechnet die Deckung das Förderdarlehen mit, welcher Wertansatz gilt? Zusätzlich: Rechnet die Bank die Kapitaldienstfähigkeit mit dem Vertragszins oder mit einem kalkulatorischen Zins und einer kalkulatorischen Tilgung? Mit eigenen Bewirtschaftungspauschalen? | Hausbank | R-5.12, `MA-026` |
| Wie berechnet die Bank die Vorfälligkeitsentschädigung; welche Prolongation ist üblich (Tilgungssatz, Rate, Restlaufzeit)? | Hausbank | R-5.16, R-5.9 |
| Tilgungsplan des Förderdarlehens: Jahres- oder Monatsraten, Beginn mit Vollauszahlung oder Bezugsfertigkeit; ab wann zählt die zinslose Zeit? | NBank | R-5.11, `MA-002` |
| Wird das Entgelt auf den Zuschuss gegen die erste Rate des Darlehens aufgerechnet? | NBank | R-5.14 |
| Rückzahlung des Zuschusses beim Verkauf: zeitanteilig nach Monaten? Übernahme von Darlehen und Bindung durch den Käufer? | NBank | R-8.7, `MA-017` |
| Mit der vorsichtigen Lesart von `MA-026` und der Tilgung nach `MA-002` bleibt im geförderten Neubau des Referenzfalls kein Bankdarlehen (R-11.14). Entspricht das der Praxis? | NBank, Hausbank | R-5.12 |
| Erfasst die erweiterte Kürzung in der Praxis des Investors Habenzinsen und Verkaufsgewinn? Gewerbesteuer auf den Verkaufsgewinn je Steuerstatus | Steuerberater | R-7.8 |
| Zuschüsse: Minderung der Abschreibungsgrundlage oder Ertrag? Behandlung der Rückzahlung | Steuerberater | R-7.3, R-7.4 |
| Finanzierungskosten in der Kurzform sofort abziehbar (Entgelte, Disagio, Bauzeitzinsen, Vorfälligkeit)? | Steuerberater | R-7.2 |
| Steuersatz auf Zinserträge je Steuerstatus; Besteuerung der Unterlassensalternative bei erweiterter Kürzung | Steuerberater | R-7.10, R-9.5 |
| Lösungsansatz für mehrere Einlagen und Entnahmen bei `ROPETER-1998`; Abgrenzung der Sollzinsen und Amortisationsregel bei `GROB-EINFUEHRUNG` | Fachliteratur | `MA-012`, `MA-027`, `MA-028` |

## 17 Vorschlagsliste

Dieses Dokument ändert keine andere Datei. Die folgenden Punkte sind Vorschläge an die Projektsteuerung.

### Neue Festlegungen dieses Dokuments

| Nr. | Regel | Festlegung |
|---|---|---|
| NF-01 | R-2.4 | Haltedauer in ganzen Jahren; Planjahr sind zwölf Monate ab dem Stichtag |
| NF-02 | R-2.5 | alle laufenden Zahlungen am Periodenende, auch die Miete |
| NF-03 | R-2.6 | Darlehenszins nominal; Konten, Unterlassensalternative und Zielrendite effektiv, konform umgerechnet |
| NF-04 | R-2.7, R-2.8 | Steuerjahr ist das Planjahr, Zahlung im letzten Monat; Sätze des Kalenderjahres Startjahr + j − 1 |
| NF-05 | R-2.9 | Basisperioden je Zahlungsart |
| NF-06 | R-4.5 | Kontokorrentlinie als Vorgabe, Voreinstellung null; Fehlbetrag wird Nachschuss derselben Periode |
| NF-07 | R-5.9 | nach der Zinsbindung bleibt der Tilgungssatz; zwei weitere Regeln wählbar |
| NF-08 | R-5.8 | Zinsbindung zählt ab dem Stichtag |
| NF-09 | R-5.12 | Mindestdeckung mit gerundeter Rate zur sicheren Seite; heutiger Zins und Tilgungssatz des Vorhabens |
| NF-10 | R-5.16 | Vorfälligkeit pauschal aus Restschuld, Satz und Restbindung; nicht für Förderdarlehen |
| NF-11 | R-5.11 | Raten übriger Darlehen im Takt des Rasters |
| NF-12 | R-6.3 | linearer Anpassungspfad mit Kappung gegen die Miete drei Jahre zuvor |
| NF-13 | R-6.4 | Mietausfall als Erlösminderung |
| NF-14 | R-6.5, R-6.6 | gebundene Miete in Stufen, nie über der Marktmiete; danach Anpassungspfad |
| NF-15 | R-6.10 | Investitionsstau: Zahlung im letzten Monat des Jahres zum Preisstand des Jahres; Erhaltung abziehbar, Modernisierung aktiviert |
| NF-16 | R-7.2 | Finanzierungskosten in der Kurzform im Jahr der Zahlung abziehbar |
| NF-17 | R-7.3 | Abschreibung je Planjahr, zeitanteilig; Zuschüsse mindern die Grundlage |
| NF-18 | R-7.5 | Kurzform verrechnet Verlustvorträge unbeschränkt; getrennte Vorträge |
| NF-19 | R-7.6 | sofortige Verrechnung ist linear; Freibetrag und Abrundung gelten als verbraucht |
| NF-20 | R-7.8 | Kennzeichen der erweiterten Kürzung erfasst in der Kurzform den ganzen Gewerbeertrag |
| NF-21 | R-7.9 | Anteil natürlicher Personen als Eingabe |
| NF-22 | R-7.10, R-7.11 | Privatperson mit zwei Töpfen; negativer Verkaufsgewinn bleibt unberücksichtigt |
| NF-23 | R-8.1 | Verkaufsfaktor bezieht sich auf die Sollmiete der zwölf Monate nach dem Stichtag |
| NF-24 | R-9.4 | Reihenfolge der Entnahmen in der Unterlassensalternative |
| NF-25 | R-10.4, R-10.5, R-10.8 | Vergleichsfaktor aus dem kurzfristigen Habenzins nach Steuern; Vergleichsrendite mit derselben Formel |
| NF-26 | R-10.6 | Zeitpunktabhängigkeit der Rendite wird hingenommen |
| NF-27 | R-10.9 | Endwertüberschuss = Z − D x (1 + z)^n |
| NF-28 | R-10.11 | Gesamtkapitalrendite mit Z, D, Z_U und Entlastung je Jahr |
| NF-29 | R-10.12 | Amortisationsdauer mit gespiegelter Vergleichsgröße |
| NF-30 | R-10.14 | Abgrenzung von Reinertrag und Kapitaldienst |
| NF-31 | R-10.16 | Restwertanteil aus dem Restwertbeitrag |
| NF-32 | R-11.2 | Neubau: Mittelbedarf und Wertansatz ohne Bauzeitzinsen; diese trägt das Eigenkapital |
| NF-33 | R-11.3 | Mittelabruf: Eigenkapital, dann Fördermittel im Verhältnis, dann Bankdarlehen; Baukosten gleichmäßig |
| NF-34 | R-11.5 | Preis in vollen Euro, ganzzahlige Suche, Suchbereich |
| NF-35 | R-11.8 | Stressfall mit Darlehen und Fördermitteln des Basisfalls beim selben Preis |
| NF-36 | R-11.9 | Liste der suchbaren Eingaben mit Auflösung |
| NF-37 | R-12.4 | zwölf Nachkommastellen für Sätze, Faktoren und Indexstände |
| NF-38 | R-11.14 | Abgrenzungen der Grobförderung |

### Widersprüche und Lücken in Spezifikation, Bericht und Verzeichnissen

Gefolgt wurde in jedem Fall der Spezifikation.

1. **Monatsraster des Testfalls.** Der Bericht (Anhang A.6) nennt 585.937,57 Euro und rechnet die Konten mit einem Zwölftel des Jahressatzes; die Spezifikation verlangt effektive Vergleichssätze. Nach R-2.6 sind es 585.918,72 Euro. RF-06 führt beide Werte.
2. **Vergleichszins der Rendite.** Der Bericht (Anhang A.3 Nr. 12) vergleicht mit q^(N/n) − 1 aus einem Zinssatz; die Spezifikation rechnet die Unterlassensalternative mit zwei Sätzen. Ersetzt durch die Vergleichsrendite (R-10.8).
3. **Endwertüberschuss.** Die Beschreibung im Bericht (Abschnitt 3) lässt bei späteren Einlagen zwei Lesarten zu, die der Rendite widersprechen können (R-10.9: 68.101,94 und 71.817,14 gegen 63.919,08 Euro).
4. **Endwertdifferenz und Zeitpunkt.** Spezifikation Kapitel 2, Zeile „Kennzahlen“, begründet die führende Rolle der Endwertdifferenz damit, dass sie nicht vom Monat der Einlagen und Entnahmen abhängt. Das gilt exakt nur bei gleichen Zinssätzen der Alternative und Entnahmen aus Guthaben (R-10.6, Eigenschaften 4 und 5).
5. **Zwei oder drei Grenzen.** Spezifikation Kapitel 2, Zeile „Grobkalkulation“, nennt im zweiten Satz den „kleineren Wert“ aus zwei Grenzen und im vierten die Restfinanzierung als dritte. Gemeint ist der kleinste von drei Werten (R-5.12).
6. **Jahresraten des Förderdarlehens.** `MA-002` nennt gleichbleibende Jahresraten; der Kern rechnet im Monatsraster Monatsraten (R-5.11). Der Kapitaldienst im Beispiel des Berichts (155.571 Euro auf 5,4 Mio. Euro) ist jährlich gerechnet; monatlich ist der Beitrag etwas kleiner.
7. **Index ungerundet.** Der Bericht (Anhang A.2 Nr. 10) schreibt den Index ungerundet fort; R-12.4 rundet auf zwölf Stellen, damit das Ergebnis auf jedem Rechner gleich ist.
8. **Deckung im Stressfall.** Das Blatt der Grobkalkulation zeigt die Deckung im ersten Jahr der Vollvermietung. Den erhöhten Anschlusszins des Stressfalls zeigt diese Zahl nicht, weil er erst nach der Zinsbindung wirkt. Vorschlag: im Stressfall zusätzlich die kleinste Deckung über die Haltedauer mit ihrem Jahr.
9. **Zahl der Eingaben.** Der Bericht zählt den Ankauf gebundener Bestände nicht aus; es sind 26 (R-3.6).
10. **Kennzahlen der gif.** `GIF-KENNZAHLENKATALOG` ist im Kataster nur als Sekundärquelle geführt; R-10.13 folgt der Spezifikation (Zeile „Restwert“) und der üblichen Fassung.

### Änderungen an `docs/spezifikation.md`

| Stelle | Vorschlag |
|---|---|
| Kapitel 3, Kopfsatz | Verweis auf dieses Dokument als Fachspezifikation, Teil 1; die Leitlinien bleiben als Zusammenfassung |
| Kapitel 3, „Konventionen“ und „Geldbeträge“ | Status „fest“; Inhalt nach Kapitel 2 und 12 dieses Dokuments |
| Kapitel 3, „Ausschüttungen und Nachschüsse“ | Formel fest nach R-10.3 bis R-10.9; „Vergleichssätze“ benennen: Habenzins, Anlagezins, Kontokorrentzins, Zielrendite effektiv; Darlehenszins nominal |
| Kapitel 3, „Unterlassensalternative“ | Reihenfolge bei Entnahmen (R-9.4) und Steuerstatus der Alternative (R-9.5) ergänzen |
| Kapitel 3, „Lehrbuchkennzahlen“ | Status „fest“ für Gesamtkapitalrendite und Amortisationsregel nach R-10.11 und R-10.12; Amortisationsdauer ab der Vollkalkulation |
| Kapitel 3, „Kontrollsummen“ | Liste P-01 bis P-14 |
| Kapitel 3, „Abnahmetests“ | Referenzfälle RF-01 bis RF-15; für IWU 2013 zusätzlich die Mietreihe aus den Annahmen mit einem Euro Toleranz |
| Kapitel 2, „Kennzahlen“ | Begründung der Endwertdifferenz präzisieren (Punkt 4 oben) |
| Kapitel 2, „Grobkalkulation“ | „kleinster von drei Werten“; Wertansatz und Mittelbedarf beim Neubau ohne Bauzeitzinsen; Stressfall mit dem Darlehen des Basisfalls beim selben Preis; Preis in vollen Euro |
| Kapitel 2, „Zielrendite und Schwellen“ | Liste der Vorgaben des Hauses um H-08 bis H-23 ergänzen |

Dazu: das Dokument in `docs/README.md` (Teil A) und in der Tabelle „Pflichtlektüre“ von `CLAUDE.md` eintragen; `skripte/LIESMICH.md` um den Ordner `referenzrechner/` ergänzen.

### Modellannahmen

| Kennung | Vorschlag |
|---|---|
| `MA-012` | Annahme neu fassen nach R-10.3 bis R-10.8: Vergleichsfaktor ist der kurzfristige Habenzins nach Steuern; verglichen wird mit der Vergleichsrendite der Unterlassensalternative. Andere Lesarten mit den Zahlen aus R-10.6. Umschaltbar bleibt „nein“. Status offen bis `ROPETER-1998` gelesen ist; Wirkort zusätzlich: dieses Dokument, R-10.5 bis R-10.9 |
| `MA-013` | ergänzen: Rate einmal gerundet, Tilgung als Differenz (R-5.3) |
| `MA-002` | ergänzen: Raten im Takt des Rasters; Tilgung und zinslose Zeit ab dem Monat nach der Bauzeit (R-5.11) |
| `MA-016` | ergänzen: Fassung der anderen Lesart nach R-7.6; Wirkung im Ankauf 5,162 % gegen 5,260 % |
| `MA-017` | ergänzen: zeitanteilige Rückzahlung nach Monaten (R-8.7); Übernahme durch den Käufer in Teil 1 nicht gebaut |
| `MA-026` | ergänzen: Kapitaldienst in (b) mit heutigem Zins und Tilgungssatz; Frage nach kalkulatorischem Zins; Befund zum geförderten Neubau (R-11.14) |
| `MA-027` | ergänzen: gespiegelte Vergleichsgröße; Kennzahl ab der Vollkalkulation |
| `MA-028` | ergänzen: Erweiterung auf mehrere Einlagen und Entlastung je Jahr (R-10.11) |
| neu | **Reichweite der erweiterten Kürzung in der Kurzform.** Annahme: Das Kennzeichen lässt die Gewerbesteuer auf den ganzen Gewerbeertrag des Vorhabens entfallen, auch auf Habenzinsen und Verkaufsgewinn. Andere Lesart: Zinsen und Verkaufsgewinn bleiben gewerbesteuerpflichtig. Ausnahme von der Vorsichtsregel, begründet mit dem Wortlaut des Berichts. Gewicht hoch (im Ankauf 155.680 Euro Gewerbesteuer auf den Verkaufsgewinn). Klärung: Steuerberater. Wirkt in R-7.8, R-7.14, R-9.5 |
| neu | **Zuschüsse in der Steuer.** Annahme: Zuschüsse mindern die Abschreibungsgrundlage; eine Rückzahlung erhöht den Buchwert. Andere Lesart: sofort steuerpflichtiger Ertrag. Gewicht mittel. Klärung: Steuerberater. Wirkt in R-7.2 bis R-7.4 |
| neu | **Finanzierungskosten in der Kurzform.** Annahme: Entgelte, Disagio, Zinsen der Bauzeit und Vorfälligkeit sind im Jahr der Zahlung abziehbar. Andere Lesart: Verteilung oder Aktivierung. Gewicht gering bis mittel. Klärung: Steuerberater. Wirkt in R-7.2 |
| neu | **Vorfälligkeitsentschädigung.** Annahme: Pauschale aus Restschuld, Satz des Hauses und Restbindung. Andere Lesart: Zinsschadenrechnung der Bank. Gewicht gering. Klärung: Hausbank. Wirkt in R-5.16 |
| neu | **Prolongation nach der Zinsbindung.** Annahme: Die Bank setzt die Rate aus der Restschuld mit Anschlusszins und unverändertem Tilgungssatz neu. Andere Lesarten: Rate bleibt; Restlaufzeit bleibt. Gewicht gering für den Endwert, mittel für die Deckung. Klärung: Hausbank. Wirkt in R-5.9 |

### Quellenkataster

Lücken, die beim Ausformulieren aufgefallen sind; ohne Eintrag darf der Katalog die Werte nicht führen:

- gesetzliche Grundlage des Steuersatzes auf Zinserträge der Privatperson (H-22, R-7.10);
- Fälligkeit der Miete (R-2.5);
- Darlehensrecht zur vorzeitigen Rückzahlung und Vorfälligkeitsentschädigung (R-5.16);
- Regeln zur Angabe des Effektivzinses, falls das Werkzeug den Effektivzins eines Darlehens ausweist (R-2.6);
- steuerliche Behandlung von Zuschüssen und von Finanzierungskosten (R-7.2, R-7.3);
- `GIF-KENNZAHLENKATALOG` am Original (R-10.13);
- `ROPETER-1998`, `GROB-EINFUEHRUNG` (`MA-012`, `MA-027`, `MA-028`).

### Punkte für `TASKS.md`

- Vorgaben des Hauses: Liste H-01 bis H-23 statt der bisherigen sieben Werte (R-3.4) – wartet auf Nutzer.
- Fachfrage: Fehlbeträge als Nachschuss aus Eigenkapital oder Kontokorrentlinie des Hauses (R-4.5) – wartet auf Nutzer.
- Gespräch mit der Hausbank um drei Fragen ergänzen: kalkulatorischer Zins in der Kapitaldienstrechnung, Vorfälligkeit, Prolongation.
- Gespräch mit der NBank um vier Fragen ergänzen (Tabelle in Kapitel 16), darunter der Befund, dass im Referenzfall kein Bankdarlehen bleibt.
- Steuerberater: vier Fragen der Kurzform (Tabelle in Kapitel 16).
- Erledigt mit diesem Dokument: die Punkte „Fachspezifikation: offene Punkte aus Prüfrunde 3“ (außer Prozessdefinition der Simulation, die zu Stufe 2 gehört), „Fachspezifikation Rechenkern (aus Quellnotiz 11)“, „Fachspezifikation Finanzierung (aus Prüfrunde 5)“; aus „Fachspezifikation Steuern“ sind die Rechenregeln der Kurzform gefasst, die Rechtsfragen stehen als vorgeschlagene Modellannahmen aus, die De-minimis-Bindung (`MA-029`) und das Zuschussentgelt in der Kreditprobe bleiben für Teil 2.
- Prüfrunde zu diesem Dokument ansetzen (Finanzmathematiker, Fachexperte, Praktiker, Controller, Grenzfälle).
- Teil 2 der Fachspezifikation beauftragen (Tabelle in Kapitel 16).
