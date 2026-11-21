Rolle: Fachexperte Immobilienökonomie
Prüfobjekt: `docs/fachspezifikation-rechenkern.md`, Teil 1, eingefrorener Stand vom 2026-11-21. Vollständig gelesen: Kapitel 1 bis 6, 8, 10 und 11, 16 und 17 sowie Anhang A. Kapitel 7, 9 und 12 bis 15 habe ich nur dort gelesen, wohin Regeln meiner Rolle verweisen. Dazu: Spezifikation Kapitel 2 und 3, `MA-026` im Verzeichnis, die Katastereinträge `CO2KOSTAUFG-5A`, `GMODG-43`, `IIBV-28` und `KFW-297-298-MERKBLATT`, Quellnotizen 10 und 12, die Durchsicht an der Wesentlichkeitsschwelle sowie mein Bericht und die Sichtung der Runde 2. Der Referenzrechner lief mit 20 Fällen und 1.093 Prüfungen, alle bestanden, Rückgabewert 0. Meine Gegenrechnungen stehen in `research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/pruefrunde-fachspezifikation-3/fachexperte_gegenrechnung.py`.

Gesamturteil: Mit Auflagen tragfähig.
- **Was jetzt trägt:** Acht meiner zehn Befunde aus Runde 2 sind behoben, einer ist vertretbar anders entschieden. KfW-Tranche, Vorlauf, Übermiete und Gebietsverordnungen entsprechen jetzt Programm und Gesetz. Die Durchsicht an der Wesentlichkeitsschwelle ist fachlich überwiegend richtig gesetzt.
- **Was nicht trägt:** Eine Setzung mit hoher Wirkung steht weiter ohne Kennung: Der Mietpfad im Neubau unterstellt, dass die Vergleichsmiete mit der Erstvermietungsmiete wächst. Dazu kommen zwei Fehler, die aus der Durchsicht stammen. (1) Der kalkulatorische Zins H-25 ist laut R-3.4 ein einziger Wert für alle Tranchen; Formel, Beispiel und Anhang rechnen ihn noch je Tranchenart. (2) Die Spezifikation hält unter „Vollständigkeit je Vorhabensart“ (fest) fest, was V-11, V-12 und V-18 jetzt streichen.
- **Reststellen:** Der Text ist nach der Durchsicht nicht durchgehend gegengelesen worden. An rund fünfzehn Stellen stehen noch entfallene Regeln, Felder und Schalter.

Note: 8 von 10. Zur 9 fehlt:
- **im Dokument:** Befunde 1 bis 3. Das sind eine neue Modellannahme ohne neue Eingabe, eine Zahl und eine Formelzeile in R-5.12 und eine Abstimmung mit der Spezifikation.
- **Reststellen:** Befunde 4 und 5 mit einem Durchgang durch den Text, je etwa eine Stunde.
- **Nicht nötig:** Neue Regeln oder Eingaben braucht keiner dieser Befunde.

## Stand der Befunde aus Runde 2

| Nr. R2 | Thema | Stand | Wo |
|---|---|---|---|
| 1 | KfW-Tranche nach Merkblatt | **behoben** | R-5.19, KAT-15, E-35 bis E-38, `MA-040`, M-49, Kataster. Annuität 3 Mio. Euro zu 2,5 % über 408 Monate = 10.922,62 Euro, über 360 Monate 11.853,63 Euro nachgerechnet |
| 2 | § 5a CO2KostAufG, hälftige Teilung | **anders entschieden**, für die Teilung selbst vertretbar (0,06 %). Für die weiteren Vermieterkosten ist es nicht sauber belegt | V-12; siehe Befund 2 |
| 3 | Voreinstellung „Förderdarlehen: ja“ | **behoben** | Kennzeichen entfallen; übernommenes Darlehen immer mit Vorfälligkeit (R-5.16, V-03), also die vorsichtige Seite |
| 4 | Übermiete gegen NF-12, ohne Kennung | **behoben** | R-6.3 Zeile (2), `MA-038`, NF-12 in Kapitel 17 angeglichen |
| 5 | Vergleichsmiete des Neubaus | **teilweise behoben**: Die Bankseite ist mit E-65 gelöst. Der Mietpfad ist **offen** | R-5.12, E-65; Rest siehe Befund 1 |
| 6 | Vorlauf bis Baubeginn | **behoben** | E-23, H-35, R-11.2 (f_m ab Stichtag), R-6.7, R-5.11 (Förderentscheidung) |
| 7 | Kostengruppe 700 ohne Finanzierungskosten; Kostenstand der Kennwerte | **behoben** | R-1.1, H-30, E-25, Feldhilfe nach R-3.3 |
| 8 | Name „Darlehen zu Kaufpreis“ | **behoben** | E-61 entfallen, Nenner immer Kaufpreis oder Gesamtkosten (R-10.15) |
| 9 | Betriebskosten leerer Flächen | **anders entschieden und vertretbar**: 0,017 Prozentpunkte | V-15. Reststellen im Text siehe Befund 4 |
| 10 | Fortgeltung der Gebietsverordnungen, § 556f, Teilgebiete | **behoben** | R-6.18, `MA-039`, E-05 je Vorhaben, R-6.7 mit späterer Vermietung |

## Befunde

1. [wichtig · begründete Einschätzung] **R-6.7, R-2.5 (Zeile Miete), R-6.6: Der Mietpfad im Neubau ruht auf einer Modellannahme ohne Kennung.**
   - **Was der Kern rechnet:** „Die Vergleichsmiete des Neubaus ist E-16 x Mietindex“, und die frei finanzierte Fläche folgt ihr mit d = 0 alle 15 Monate. Damit unterstellt der Kern eine von zwei Außenweltlagen:
     - Es ist eine Indexmiete vereinbart (`BGB-557B`, im Kataster). Dann folgt die Miete dem Verbraucherpreisindex, und der Mietspiegel spielt keine Rolle.
     - Oder der Mietspiegel steht für dieses Objekt auf der Höhe der Erstvermietungsmiete.
   - **Was in der Praxis vorkommt** (begründete Einschätzung): Liegt die Erstvermietungsmiete über dem Mietspiegelwert der Neubauklasse und ist keine Index- oder Staffelmiete vereinbart, lässt `BGB-558` keine Erhöhung zu, bis der Mietspiegel die Miete einholt. Danach hängt die Miete dauerhaft am niedrigeren Mietspiegelpfad.
   - **Wirkung im Neubau des Referenzfalls** (RF-12, Faktor 24, Verkauf nach 15 Jahren; maßgebliche Jahresmiete am Verkaufsstichtag nach Leerstand 12 x 2.000 m² x Miete x 0,985):
     - Liegt der Mietspiegelwert 5 % unter E-16, liegen die Miete am Verkaufsstichtag und damit der Verkaufspreis rund 5 % tiefer. Das sind rund 0,6 Mio. Euro oder fast 7 % der Gesamtkosten von 9,0 Mio. Euro.
     - Bei 18 % Abstand bleibt die Miete etwa elf Jahre bei 16,50 Euro. Der Verkaufspreis liegt dann rund 2,3 Mio. Euro tiefer.
     - Beide Fälle liegen weit über der Schwelle von 1 % der Gesamtkosten.
   - **Zuordnung:** Das ist eine Annahme über Vertragsform und Markt, die sich als falsch herausstellen kann (Spezifikation Kapitel 8). `MA-026` deckt nur die nachhaltige Miete der Bank.
   - **Vorschlag ohne neue Eingabe:**
     - Neue Modellannahme, Gewicht hoch: „Im Neubau folgt die Miete dem Mietindex wie eine Indexmiete.“ Andere Lesart: Vergleichsmietenverfahren mit E-65 als Vergleichsmiete im ersten Vermietungsjahr. E-65 ist die nachhaltige Miete, die schon heute eine Mietspiegelgröße vertritt.
     - Die andere Lesart wird Lesart des Hauses (R-3.4). Kennung an R-6.7, R-2.5 und Spezifikation „Grobkalkulation“.
     - Die Feldhilfe zu E-16 nennt die Vertragsform.
   - **Abgrenzung:** Welche Lesart die vorsichtige ist, entscheidet das Haus mit der Freigabe. Beim gegenwärtigen Text gewinnt still die günstige.

2. [wichtig · belegt] **Spezifikation Kapitel 2, Zeile „Vollständigkeit je Vorhabensart“ (fest), gegen V-11, V-12 und V-18; dazu ist die Zahl in V-12 zu niedrig.**
   - **Widerspruch zur Spezifikation:** Die Zeile verlangt für den Ankauf Bestand „Bewirtschaftung, Instandhaltung, Kaufpreisaufteilung und CO2-Kosten nach `CO2KOSTAUFG-5` bis `CO2KOSTAUFG-5D`“. Die Fachspezifikation streicht dagegen dreierlei:
     - § 5a bis § 5d (R-6.9, V-12);
     - die CO2-Kosten ohne Angabe von E-34 (V-11);
     - den Bodenanteil als Eingabe außer bei steuerfreiem Verkauf (V-18).
   - Die Zeile „Wesentlichkeit“ ist ebenfalls fest. Zwei feste Zeilen widersprechen sich also. Nach `CLAUDE.md` ist das sofort zu beheben, nicht zu umgehen.
   - **Zahl in V-12:** V-12 nennt „0,06 % / 0,009 Prozentpunkte“ für die hälftige Teilung *und* die weiteren Vermieterkosten (früher E-66, E-67). Die Durchsicht hat aber getrennt gemessen:
     - die Teilung allein: 0,06 %;
     - die weiteren Kosten mit 2.000 Euro im Jahr: **−0,83 % / −0,103 Prozentpunkte**. Die Durchsicht nennt das selbst „Grenzfall: knapp an der Schwelle“ (Zeile E-67).
   - **2.000 Euro sind eher niedrig:** Nach `GMODG-43` (Kataster: Brennstoffpfad 10 / 15 / 30 / 60 % ab 2029 / 2030 / 2035 / 2040) wachsen diese Kosten über die Haltedauer. Für das Referenzobjekt habe ich halbe Netzentgelte und Mehrkosten des Bioanteils überschlagen. Es ergeben sich rund 2.850 Euro im Jahr bei 15 % und rund 4.280 Euro bei 30 % Bioanteil. Die Preise sind Annahmen, nicht gelesen, und stehen im Skript.
   - **Kein Ausweg über eine Eingabe:** H-17, und damit auch die nicht umlagefähigen Betriebskosten, ist fester Hauswert. Für ein Objekt mit einer Heizung nach § 43 GModG gibt es also keinen Weg, diese Kosten anzusetzen.
   - **Einordnung:** Typisch ist der Fall 2027 noch nicht. Mit jedem nach dem GModG eingebauten Gaskessel wird er häufiger.
   - **Vorschlag:**
     - Die Spezifikationszeile auf „CO2-Kosten nach `CO2KOSTAUFG-5`; § 5a bis § 5d als benannte Vereinfachung“ und „Kaufpreisaufteilung, wo sie wirkt“ fassen, mit Eintrag im Entscheidungsprotokoll.
     - V-12 in zwei Zeilen teilen: Teilung 0,06 %; weitere Kosten −0,83 % / −0,103 Prozentpunkte je 2.000 Euro, steigend mit dem Bioanteil. „Klärt im Einzelfall“ nennt den Bearbeiter.
     - Den dritten Wert von H-17 (nicht umlagefähige Betriebskosten) als Vorgabe der Klasse (a) führen. Das wäre im Vorhaben mit Begründung änderbar und bräuchte kein neues Feld in der Grundmaske.
     - Im Kataster `CO2KOSTAUFG-5A` den Verweis auf die entfallenen E-66 und E-67 berichtigen (Befund 5).

3. [wichtig · belegt] **H-25 „ein Wert für alle Tranchen“ (R-3.4, V-07) gegen R-5.12 und Anhang A.4; eine Beispielzahl ist falsch, V-06 stimmt nicht allgemein.**
   - **Formel:** R-5.12, Bemessungszins: `i_kalk = max(Vertragszins; H-25 der Tranchenart)`. Eine Tranchenart von H-25 gibt es nicht mehr.
   - **Beispielzahl:** R-5.12, Satz nach der Tabelle zum Bemessungszins: „Mit einem festen kalkulatorischen Zins von 4 % für übernommene Darlehen (H-25) sind es bei acht Jahren 826.660,00 Euro.“
     - Die Zahl gilt nur, wenn die Bank weiter mit 7 % rechnet und allein die fremde Tranche mit 4 %. Gegenrechnung: i_B = 1,2 %, KD_Ü = 19.200,00 Euro, (92.479,44 / 1,2 − 19.200) / 7 % = 826.660,00 Euro.
     - Mit einem Wert für alle Tranchen, wie R-3.4 ihn festlegt und wie der Referenzrechner ihn umsetzt (`kalk_zins` in `grobkalkulation.py`), ist i_k = max(4 %; 4 %) = 4 %. Das Darlehen ist dann (77.066,20 − 19.200) / 6 % = **964.436,66 Euro**.
   - **V-06:** „Lesart 2 ergibt sich auf den Cent über H-25 in Höhe des Vertragszinses“. Das gilt im Ankauf ohne fremde Tranche und beim KfW-Darlehen mit gleicher Bindung. Es gilt nicht für ein übernommenes Darlehen mit kürzerer Bindung:
     - Nach Lesart 2 sind es 1.034.436,66 Euro, wie in R-5.12 genannt;
     - mit H-25 = 4 % sind es 964.436,66 Euro, weil i_kalk = max(0,5 %; 4 %) den Zins der fremden Tranche nach ihrer Bindung anhebt.
   - **Weitere Reststellen:**
     - Anhang A.4, Zeile „H-25 bis H-28: kalkulatorischer Zins für jede Tranchenart …“;
     - `MA-026` im Verzeichnis. Dort steht noch „für ein übernommenes Darlehen ist der Rang Eingabe“, „Diese vier sind umschaltbar“, „(6) Beleihungswert … (Eingabe)“ und „kalkulatorischer Zins je Tranchenart“, entgegen der eigenen Bemerkung zur Durchsicht.
   - **Folge:** Ein Entwickler, der nach R-5.12 baut, bildet vier H-25-Werte. Ein Prüfer, der den Satz nachrechnet, findet 138 Tsd. Euro Unterschied zum Referenzrechner.
   - **Vorschlag:**
     - „der Tranchenart“ streichen.
     - Den Satz auf 964.436,66 Euro berichtigen und aus dem Referenzrechner belegen.
     - V-06 auf „im Ankauf ohne fremde Tranche deckungsgleich; mit fremder Tranche kürzerer Bindung höher“ fassen, mit Zahl.
     - A.4 und `MA-026` nachziehen.

4. [Hinweis · belegt] **R-6.7, R-10.22, R-5.12, Anhang A.4: Die entfallene Regel R-6.17 wird weiter angewendet.**
   - R-6.7: „bis dahin ist die ganze Fläche leer und trägt die Betriebskosten leerstehender Flächen (R-6.17)“.
   - R-10.22: „Die Bewirtschaftung enthält die Betriebskosten leerstehender Flächen, soweit sie in dieses Jahr fallen (R-6.17)“.
   - R-5.12: „Bewirtschaftung_n = … nach R-6.8, R-6.9 und R-6.17“.
   - A.4: „H-36 … Betriebskosten leerstehender Flächen 0 Euro, in den bezeichneten Fällen 30 Euro“.
   - R-6.17 und H-36 sind aber entfallen (V-15, NF-60 zurückgenommen). Ein Entwickler muss raten, ob R-6.7 und R-10.22 einen Betrag rechnen.
   - **Vorschlag:** In R-6.7 den Halbsatz streichen oder auf V-15 verweisen; in R-10.22 den Satz streichen; R-5.12 und A.4 bereinigen.

5. [Hinweis · belegt] **Weitere Reststellen der Durchsicht, je ein Satz zu ändern.**
   - **R-6.16:** „das Eingabefeld E-52 sagt das“. E-52 ist entfallen; gemeint ist die Feldhilfe zu E-50.
   - **NF-07 (Kapitel 17):** „zwei weitere Regeln wählbar“. Sie sind nicht mehr wählbar (R-5.9, V-01).
   - **Kapitel 16, „Was Teil 2 regelt“, Zeile KfW:** Die „Bereitstellungsprovision“ ist dort Teil 2. R-5.19, NF-41 und die Spezifikation rechnen sie aber schon in 1a, und die Durchsicht (Zeile 448) hat sie behalten.
   - **R-5.19 und Kapitel 17, Widersprüche Nr. 10:** Beide sagen, die Spezifikationszeile „Teilschritte der Stufe 1“ nenne noch „Tilgung“. Sie nennt bereits „Laufzeitvariante … statt eines Tilgungssatzes“.
   - **R-5.19:** Der Satz nach der Liste führt den Zählbeginn der Anlaufjahre noch als „Frage nach außen“. Kapitel 16, Einleitung der Hausbankfragen, sagt dagegen „nicht mehr gefragt“; V-08 nennt als Klärung „Zusage der KfW über die Hausbank“. Das ist auf eine Aussage zu bringen.
   - **Anhang A.6:** E-05 „im Gebiet (Voreinstellung)“. Im Neubau ist E-05 keine Eingabe (R-6.18 Nr. 3).
   - **Kataster `CO2KOSTAUFG-5A`, `verwendet_fuer`:** Dort steht noch „Eingabe E-66“ und „Eingabe E-67“.
   - **R-11.14 („Nach Lesart (1) … stiege A“), R-5.19 (`MA-040`, „Zahlen der anderen Lesart … führt der Referenzrechner nicht mehr“) und die MA-Tabelle in Kapitel 17:** Diese Zahlen kann niemand mehr nachrechnen. Das widerspricht „Jede Zahl kommt aus dem Referenzrechner“. Sie sind als „Stand vor der Durchsicht, nicht nachrechenbar“ zu kennzeichnen oder zu streichen.

6. [Hinweis · belegt] **R-5.11, NF-65: Die Begründung zur Förderentscheidung stimmt nicht mit der Richtlinie überein.**
   - NF-65 sagt, die Richtlinie „nennt aber keinen Abstand“ zwischen Förderentscheidung und Baubeginn. Quellnotiz 12 hält aus `NBANK-RL-MIETWOHNRAUM-2026` (Nr. 4.2, 5.4.7) fest: Baubeginn spätestens vier Monate nach der Förderentscheidung.
   - Die Setzung „Monat vor dem Baubeginn“ bleibt zulässig. Sie ist aber die günstige Lesart: Bei einer früheren Entscheidung beginnt die Tilgung des zinslosen Darlehens früher.
   - **Wirkung:** im Referenzfall null, weil die letzte Teilrate den Tilgungsbeginn bestimmt (Monat 23 vor Monat 25); im Stressfall höchstens drei Monate früher. Das liegt unter der Schwelle.
   - **Vorschlag:** Die Begründung auf „frühestens am Tag der Entscheidung, spätestens vier Monate vor Baubeginn; gesetzt ist der späteste Monat (günstig, unter der Schwelle)“ fassen.

7. [Hinweis · begründete Einschätzung] **R-3.4, Zu H-17: Was die Instandhaltungsstaffel umfasst, ist nicht festgelegt.**
   - `IIBV-28` (Kataster, am 18.11.2026 gelesen; Quellnotiz 10) kennt Zu- und Abschläge zur Grundpauschale. Darunter sind ein Aufzug mit +1,00 Euro je m² und die Schönheitsreparaturen, wenn der Vermieter sie trägt, mit höchstens 8,50 Euro je m², beides Basisbeträge.
   - Das Kataster vermerkt, dass diese Zuschläge „im Katalog noch fehlen“. R-3.4 sagt nicht, ob die freigegebene Staffel sie enthält.
   - **Warum das zählt:** Für die Freigabe ist das kein Randthema. Die Schönheitsreparaturen sind rund das 8,5-Fache der Variation „Betriebskosten +1 Euro je m²“ (−0,54 %). Grob überschlagen bewegen sie den Preis um 4 bis 5 % (begründete Einschätzung). Ob der Vermieter sie trägt, hängt an der Wirksamkeit der Klauseln im Bestand.
   - **Vorschlag ohne neue Eingabe:** Im Satz „Zu H-17“ festlegen, dass die Staffel die Kosten der Wohnungsinstandsetzung bei Mieterwechsel und die Schönheitsreparaturen enthält oder nicht. Diese Frage gehört auf das Freigabeblatt. Einen Aufzugszuschlag nicht einbauen: Er liegt unter der Schwelle (≈ −0,5 %), als Vereinfachung benennen.

8. [Hinweis · begründete Einschätzung] **R-3.2 Nr. 1 (c), R-3.4: Die Klasse „fester Katalogwert“ ist für Werte ohne Quelle vergeben.**
   - Definiert ist sie als „Wert mit Quelle im Katalog, ohne Freigabeentscheidung des Hauses“. H-10, H-23 und H-37 haben aber keine Rechts- oder Normquelle:
     - H-10 ist der Kontokorrentzins, eine Bankkondition;
     - H-23 ist die Anpassungsdauer, also die Mietpolitik des Hauses;
     - H-37 sind die Bauabschnitte, eine Setzung nach NF-64.
   - Bei H-27 belegt `IIBV-29` nur die Summe mit H-15, nicht den Teil.
   - Weil die Freigabeentscheidung fehlt, setzt niemand verantwortlich diese Werte.
   - **Wirkung:** klein, H-23 +0,13 %. Der Befund betrifft die Verantwortung für den Wert, nicht die Zahl.
   - **Vorschlag:** H-10, H-23 und H-37 als feste Hauswerte führen, H-27 ebenso oder mit Quelle. Dann stehen sie auf dem Freigabeblatt.

Gesammelt, unter der Schwelle und kein Befund:
- **V-03, V-14 und V-17:** Sie berühren in ihrem Sonderfall 0,1 Prozentpunkte (+0,141 / −0,109 / +0,103). Sie sind aber vorsichtig gewählt, durch H-13 gut genähert oder vom Haus einmal zu stellen. Vertretbar.
- **E-34 ohne Angabe:** Die freiwillige E-34 mit Voreinstellung 0 ist die günstige Voreinstellung (V-11, 0,37 %).
- **R-6.18 Nr. 2:** „Auf den Euro dasselbe“ gilt nur ohne Mietenhistorie. Mit E-33 wirkt die Kappung von 20 % schon vor dem Geltungsende.
- **Degressive Abschreibung im Neubau:** fehlt, vorsichtig; Rolle Steuerberater.

## Was fachlich trägt (nachgeprüft, kein Befund)

- **Lehrbuchbegriffe und Methode:** Das Glossar (R-1.1) und die Lehrbuchansicht (R-4.7) bilden Grob und Schulte richtig ab: Endvermögen, Vermögensendwert, direkte und indirekte Zahlungen, Unterlassungsalternative. Die Trennung von strukturellem Leerstand und Forderungsausfall mit Wirkung auf den Verkaufspreis ist fachlich richtig.
- **Miete im Bestand:** Mietpfad, Kappung gegen die Miete drei Jahre zuvor und Planjahr 1 mit Ist-Miete gelten unverändert. Neu richtig sind die Rückführung einer Übermiete als `MA-038` und § 556f dauerhaft für den Neubau.
- **Finanzierung:**
  - Bemessung (a) bis (c) mit nachhaltiger Miete, Mindestansatz und Bemessungszins.
  - Die KfW-Tranche entspricht dem Merkblatt.
  - Das Förderdarlehen folgt der Richtlinie: Tilgung ab dem Monat nach der letzten Teilrate, spätestens nach der Frist, Ende 42 Jahre nach Bezugsfertigkeit, zinslos 35 Jahre; Nr. 5.3.4 und 5.3.5 nach Quellnotiz 12.
  - Bereitstellungszins und Vorfälligkeit bis zum Kündigungsrecht sind bankübliche Grobform.
- **Förderung in Grobform:** Zuwendungsfähige Kosten mit Begrenzung auf den Bodenrichtwert, Teilraten 30 / 30 / 30 / 10, Eigenmittel 20 % und Rückzahlung des Zuschusses anteilig zur Restbindung entsprechen der Richtlinie nach Quellnotiz 12. Die Haltedauer „Bindungsende plus ein Jahr“ ist fachlich sinnvoll; nachgerechnet: Bindung von Monat 19 bis 438, 420 Monate, Rückzahlung nach 240 Monaten 198 / 420.
- **Restwert:** Faktor auf die maßgebliche Jahresmiete nach Leerstand und Erbbauzins, Ein- und Ausstieg symmetrisch, Warnschwelle für den Faktorabstand. Das ist für eine Grobkalkulation richtig und vollständig genug.
- **Zuschnitt gegen den Bauablauf der Spezifikation** (Kapitel 2, „Teilschritte“, fest): 1a enthält beide Vorhabensarten, das KfW-Darlehen in Grobform und die NBank-Grobförderung. Mieterliste, Modernisierungsumlage, Kosten nach Kostengruppen und die volle Förderung liegen in Teil 2 bei 1b-1, 1b-2 und 1c. Das passt zur festgelegten Folge.

## Am Original gelesen

In dieser Runde nichts Neues am Original. Verwendet habe ich die Kataster- und Quellnotizstände vom 18.11.2026 (`NBANK-RL-MIETWOHNRAUM-2026` nach Quellnotiz 12, `IIBV-28`, `GMODG-43`, `CO2KOSTAUFG-5A`).

## Nicht geprüft

- **Kapitel 7 (Steuer), 9 (Unterlassensalternative) und 12 bis 15:** außerhalb meiner Rolle (Steuerberater, Finanzmathematiker, Controller, Grenzfälle), nur an den Verweisstellen gelesen.
- **Die Preise für Netzentgelte und Biogas in Befund 2:** Das sind Annahmen. Weder BNetzA noch Marktberichte habe ich gelesen.
- **Das Mietspiegelgefälle im Neubau (Befund 1)** ist eine Einschätzung aus der Praxis. Mietspiegel einzelner Gemeinden habe ich nicht ausgewertet.
- **Landeswerte HB, HH, SH, NRW:** wie in Runde 2 bewusst ausgenommen.
