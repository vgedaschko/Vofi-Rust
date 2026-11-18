# Notiz 15: Steuerrichtlinien und Urteile am Wortlaut

Zweck: Den Wortlaut der Verwaltungsanweisungen und Urteile beschaffen, die in Notiz 13 nur sekundär oder gar nicht gelesen waren, weil die amtlichen Steuerhandbücher des BMF (`esth.`, `gewsth.`, `ksth.`, `ao.bundesfinanzministerium.de`) ein Captcha zeigen. Das Captcha wurde nicht umgangen; gelesen wurde auf anderen, frei zugänglichen Wegen. Leser: Entwicklung (Fachspezifikation Rechenkern, Steuermodul), Pflege des Verzeichnisses der Modellannahmen, des Leitfadens für den Steuerberater und des Quellenkatasters. Stand: 2026-11-18.

Zur Belegqualität:

- **am Original:** amtliche Stelle (Bundesgesetzblatt, Gesetzestext beim Bund, BMF), heute im Volltext gelesen.
- **Wortlaut in Verlagswiedergabe:** vollständiger, wörtlicher Abdruck der Richtlinie, des Hinweises, des BMF-Schreibens oder des Urteils bei einem Verlag oder einer Volltextsammlung, heute gelesen. Wo eine zweite Wiedergabe denselben Text zeigt, steht „gegengeprüft“.
- **sekundär:** nur Zusammenfassung, Kommentar oder Suchauszug.
- **nicht erreicht:** mit Grund.

Hauptquellen dieser Notiz:

- **NWB-Datenbank** (`datenbank.nwb.de`): Richtlinien, Hinweise, BFH-Urteile und viele Verwaltungsanweisungen sind dort ohne Anmeldung im Volltext lesbar, mit Angabe der Fassung („VZ … aktuell“). Einzelne ältere BMF-Schreiben sind kostenpflichtig; die wurden nicht geöffnet.
- **steuerschroeder.de:** Abdruck der Richtlinien und Hinweise mit dem Vermerk „Text aus dem Amtlichen Einkommensteuer-Handbuch 2025“ bzw. „Gewerbesteuer-Handbuch 2024“.
- **haufe.de:** Abdruck der Hinweise 2024, teils nach einigen Absätzen abgeschnitten.

Abrufkopien liegen nur in `/tmp/claude-0/-home-user/eb745ffa-98ff-574d-96a9-6ae46d551680/scratchpad/quellen15/`, nicht im Repository.

## Ergebnis

Neun der zehn Steuerfragen sind am Wortlaut beantwortet; drei davon verschieben eine Voreinstellung.

1. **Erweiterte Kürzung und Verkaufsgewinn (`MA-030`): Die Verwaltung kürzt den Veräußerungsgewinn.** H 9.2 (3) GewStH: Veräußert ein Unternehmen, das die Voraussetzungen der erweiterten Kürzung erfüllt, Grundbesitz, „ist … auch der bei der Veräußerung erzielte Gewinn … zu kürzen“. Ausgenommen sind nur die Fälle des § 9 Nr. 1 Satz 5 Nr. 2 und Satz 6 GewStG. Die vorsichtige Voreinstellung „Verkaufsgewinn gewerbesteuerpflichtig“ widerspricht damit der Verwaltungsauffassung, sobald die Kürzung im Verkaufsjahr überhaupt zusteht. Ob sie zusteht, regelt BFH III R 1/23 (Notiz 13): Geht der letzte Grundbesitz vor dem 31.12., 23:59 Uhr über, entfällt die Kürzung ganz. Bei einem Übergang um 23:59 Uhr bleibt sie (BFH I R 89/03, jetzt im Volltext gelesen).
2. **Zuschuss für eine Mietbindung (`MA-031`) bei der Privatperson: Einnahme im Zuflussjahr, auf Antrag verteilbar, keine Minderung der Herstellungskosten.** R 21.5 Abs. 2 EStR nennt den Zuschuss „als Gegenleistung für eine Mietpreisbindung oder Nutzung durch einen bestimmten Personenkreis“ ausdrücklich und fügt an: „§ 11 Abs. 1 Satz 3 EStG ist zu beachten“. Das ist die gesetzliche Wahl, Einnahmen für eine Nutzungsüberlassung von mehr als fünf Jahren gleichmäßig zu verteilen. BFH IX R 60/02 schließt die Minderung der Herstellungskosten für solche Mittel aus.
3. **Zuschuss für eine Mietbindung im Betriebsvermögen: kein Wahlrecht nach R 6.5, eher passiver Rechnungsabgrenzungsposten.** R 6.5 Abs. 1 Satz 3 EStR: Ein Zuschuss liegt „in der Regel … nicht“ vor, „wenn ein unmittelbarer wirtschaftlicher Zusammenhang mit einer Leistung des Zuschussempfängers feststellbar ist“. H 5.6 EStH: Für Ertragszuschüsse ist „ggf. ein passiver Rechnungsabgrenzungsposten zu bilden“; Investitionszuschüsse sind „nicht passiv abzugrenzen“. Ausdrücklich zum Bindungszuschuss sagt keine Richtlinie etwas. Die Frage an den Steuerberater bleibt, wird aber eng.
4. **Marktübliches Damnum (`MA-032`): Die 5-%-Grenze steht im BMF-Schreiben vom 20.10.2003 (BStBl I S. 546), Rz. 15.** Das Schreiben vom 05.04.2005 (BStBl I S. 617) verweist nur darauf. Beide stehen in der Positivliste des BMF vom 20.03.2026, gelten also fort.
5. **Vorfälligkeitsentschädigung (`MA-032`): BMF vom 27.07.2015 im Wortlaut gelesen.** Sie ist beim Verkauf „keine nachträglichen Werbungskosten …, sondern Veräußerungskosten“ nach § 23 EStG. Die Voreinstellung ist damit Verwaltungsauffassung, keine Annahme mehr.
6. **Verlustvortrag ab 2028 (`MA-010`): am Bundesgesetzblatt bestätigt.** Art. 6 des Wachstumschancengesetzes ersetzt „70 Prozent“ durch „60 Prozent“, erstmals für den VZ 2028. Die Vorschrift tritt am 01.01.2028 in Kraft (Art. 35 Abs. 9). Die Annahme kann als geklärt geschlossen werden.
7. **Außenanlagen (`MA-023`):** R 21.1 Abs. 3 Satz 1 EStR rechnet von der Gartengestaltung nur die „lebende Umzäunung“ zum Gebäude. H 6.4 und H 7.1 EStH ordnen Gartenanlage, Hofbefestigung und Zufahrt als eigene Wirtschaftsgüter ein; die Umzäunung beim Mietwohngrundstück gehört dagegen „i. d. R.“ zum Gebäude. Außenanlagen zählen also überwiegend nicht zur Kostenbasis der Baukostenobergrenze.
8. **Befreite Genossenschaft im Verkaufsjahr (Steuerberater, Frage 5): beantwortet.** Die Veräußerung von Betriebsgrundstücken aus dem begünstigten Bereich ist ein begünstigtes Geschäft. „Einnahmen aus solchen Geschäften fallen deshalb nicht unter die 10 v. H.-Grenze“ (BMF vom 22.11.1991, Tz. 38 und 39, gelesen in der wortgleichen Verfügung der OFD Frankfurt). Das gilt nicht beim gewerblichen Grundstückshandel. R 5.9 KStR 2022 ist „unbesetzt“ und verweist über H 5.9 auf dieses Schreiben.
9. **Objektverkauf der GmbH & Co. KG (`MA-036`):** R 7.1 Abs. 3 GewStR und BFH IV R 3/05 im Wortlaut gelesen. Das Grundstück der nur gewerblich geprägten KG ist Anlagevermögen. Fällt die Veräußerung in eine Betriebsveräußerung oder -aufgabe, ist der Gewinn begünstigt und gehört nach § 7 Satz 2 GewStG nur zum Gewerbeertrag, soweit er nicht auf natürliche Personen entfällt. Offen bleibt der Einzelfall: Liegt bei einer geprägten KG, die nach dem Verkauf fortbesteht, eine Aufgabe vor?
10. **Mietrecht (nachrangig):** Zu `MA-007` begrenzt der BGH die Anrechnung der Drittmittel auf zwölf Jahre ab mittlerer Bezugsfertigkeit (VIII ZR 311/11). Zu `MA-018` nennt der BGH die „Erneuerung des Heizkessels“ als typische Endenergieeinsparung (VIII ZR 283/23, Rn. 31). Zu `MA-019` und `MA-025` wurde keine BGH-Entscheidung gefunden.

Nebenbefund: Notiz 13 nennt BFH I R 17/99 als Urteil, das „die Kürzung für einen Veräußerungsgewinn versagte“. Das trifft nicht zu. Das Urteil gewährt die Kürzung für den Gewinn aus der Auflösung einer § 6b-Rücklage und versagt sie nur für den Gewinnzuschlag nach § 6b Abs. 7 EStG.

## 1. R 21.5 EStR und H 21.5 EStH: Zuschüsse bei Vermietung (`MA-031`)

**Frage:** Ist ein Zuschuss, der eine Mietpreis- oder Belegungsbindung abgilt, Einnahme im Zuflussjahr? Darf verteilt werden? Wann mindert ein Zuschuss stattdessen die Herstellungskosten?

**Was der Text sagt:**

- R 21.5 Abs. 1 Satz 1 und 2 regeln den Grundfall. Zuschüsse zur Finanzierung von Baumaßnahmen, die keine Mieterzuschüsse sind, „gehören grundsätzlich nicht zu den Einnahmen aus Vermietung und Verpachtung“. Bei Herstellungskosten sind die AfA „ab dem Jahr der Bewilligung … nach den um den Zuschuss verminderten Herstellungskosten zu bemessen“.
- R 21.5 Abs. 2 regelt die Ausnahme. „Abweichend von Absatz 1“ sind solche Zuschüsse „im Kalenderjahr des Zuflusses … Einnahmen aus Vermietung und Verpachtung, wenn sie eine Gegenleistung für die Gebrauchsüberlassung des Grundstücks darstellen (z. B. Zuschuss als Gegenleistung für eine Mietpreisbindung oder Nutzung durch einen bestimmten Personenkreis); § 11 Abs. 1 Satz 3 EStG ist zu beachten.“
- § 11 Abs. 1 Satz 3 EStG (am Original): „Der Steuerpflichtige kann Einnahmen, die auf einer Nutzungsüberlassung im Sinne des Absatzes 2 Satz 3 beruhen, insgesamt auf den Zeitraum gleichmäßig verteilen, für den die Vorauszahlung geleistet wird.“ Absatz 2 Satz 3 betrifft Vorauszahlungen für eine Nutzungsüberlassung „von mehr als fünf Jahren“.
- H 21.5, Stichwort „Zuschüsse“, nennt drei Fälle:
  - Ein Gemeindezuschuss für die Erhaltung des Gebäudes, „unabhängig von der Nutzung“ gewährt, mindert die Herstellungskosten (BFH IX R 104/86).
  - Ein Zuschuss für eine Tiefgarage „ohne Vereinbarung einer Mietpreisbindung oder Nutzung durch bestimmte Personen“ mindert die Herstellungskosten. Die Pflicht, die Garage der Öffentlichkeit gegen Entgelt zu öffnen, „ist keine Gegenleistung“ (BFH IV R 58/94).
  - „Öffentliche Fördermittel (Zuschüsse oder nicht rückzahlbare Darlehen), die ein Bauherr im Rahmen des sog. Dritten Förderungswegs für Belegungs- und Mietpreisbindungen erhält, sind im Zuflussjahr Einnahmen aus Vermietung und Verpachtung“ (BFH IX R 60/02).

**Fundstelle:**

- R 21.5 EStR, Fassung EStR 2012 i. d. F. vom 25.03.2013, laut NWB unverändert für VZ 2012 bis 2026: `https://datenbank.nwb.de/Dokument/443548_21___5/`. Gegengeprüft an `https://www.steuerschroeder.de/steuergesetze/estr/21.5` (Amtliches Einkommensteuer-Handbuch 2025).
- H 21.5 EStH 2024: `https://www.haufe.de/id/norm/einkommensteuer-richtlinien-amtliche-hinweise-2024-h-215-behandlung-von-zuschuessen-HI16802377_p21.5.html`. Gegengeprüft an `https://www.steuerschroeder.de/steuergesetze/esth/21.5` (Handbuch 2025).
- § 11 EStG: `gesetze-im-internet.de/estg/__11.html`.

**Belegqualität:** R 21.5 und H 21.5 im Wortlaut in Verlagswiedergabe, gegengeprüft. § 11 EStG am Original.

**Folge für `MA-031` (Privatperson):**

- Die Voreinstellung „Einnahme im Zuflussjahr“ ist die Regel der Verwaltung, keine bloße Annahme. Befund 1 der Prüfrunde 2 („in keinem Feld zwingend“) ist für die Privatperson damit widerlegt.
- Die Lesart „verteilt über die Bindung“ ist ein Wahlrecht des Steuerpflichtigen nach § 11 Abs. 1 Satz 3 EStG, auf das R 21.5 Abs. 2 ausdrücklich verweist. Sie ist keine konkurrierende Rechtsauffassung. Sie sollte als Eingabe „Verteilung nach § 11 Abs. 1 Satz 3 EStG beantragt“ geführt werden, voreingestellt nein, und nur bei einer Bindung von mehr als fünf Jahren wählbar sein.
- Die Lesart „Minderung der Herstellungskosten“ ist für einen Zuschuss, der an Belegungs- und Mietbindung geknüpft ist, nach IX R 60/02 ausgeschlossen. Sie gilt nur für einen Zuschuss ohne Bindung, etwa einen reinen Bau- oder Energiezuschuss. Für den NBank-Zuschuss sollte sie bei der Privatperson nicht mehr wählbar sein, oder nur mit Meldung.
- Vorschlag für den Wortlaut der Grundlage: „R 21.5 Abs. 2 EStR, H 21.5 EStH (‚Dritter Förderungsweg‘) und BFH vom 14.10.2003, IX R 60/02: Zuschüsse als Gegenleistung für eine Mietpreis- oder Belegungsbindung sind Einnahmen im Kalenderjahr des Zuflusses und mindern die Herstellungskosten nicht. Nach § 11 Abs. 1 Satz 3 EStG kann der Steuerpflichtige sie auf den Bindungszeitraum verteilen, wenn er mehr als fünf Jahre beträgt.“

**Frage an den Steuerberater:** geschärft. Bleiben sollen nur zwei Punkte. Erstens: Behandelt das Finanzamt den NBank-Zuschuss als Vorauszahlung im Sinne des § 11 Abs. 2 Satz 3 EStG, sodass die Verteilung möglich ist? Zweitens: Wie wird der Tilgungsnachlass behandelt? Er ist wirtschaftlich ein „nicht rückzahlbares Darlehen“ im Sinne von H 21.5; offen ist, ob er beim Erlass zufließt.

## 2. R 6.5 EStR und H 6.5 EStH: Zuschüsse im Betriebsvermögen (`MA-031`)

**Frage:** Gilt das Wahlrecht des Betriebsvermögens auch für Zuschüsse mit Gegenleistung (Bindung)? Gibt es eine Aussage zum passiven Rechnungsabgrenzungsposten?

**Was der Text sagt:**

- R 6.5 Abs. 1 (Begriff): „Ein Zuschuss ist ein Vermögensvorteil, den ein Zuschussgeber zur Förderung eines – zumindest auch – in seinem Interesse liegenden Zwecks dem Zuschussempfänger zuwendet. … In der Regel wird ein Zuschuss auch nicht vorliegen, wenn ein unmittelbarer wirtschaftlicher Zusammenhang mit einer Leistung des Zuschussempfängers feststellbar ist.“
- R 6.5 Abs. 2 (Wahlrecht) gilt für „Anlagegüter mit Zuschüssen aus öffentlichen oder privaten Mitteln“. Möglich ist entweder der Ansatz als Betriebseinnahme oder die erfolgsneutrale Behandlung mit Bewertung nur zu den selbst getragenen Kosten. Abs. 3 und 4 regeln nachträgliche und im Voraus gewährte Zuschüsse; für Letztere ist eine steuerfreie Rücklage möglich.
- H 6.5 verweist bei „Öffentliche Zuschüsse unter Auflage“ auf H 21.5 und bei „Rechnungsabgrenzungsposten“ auf H 5.6 (Investitionszuschüsse).
- H 6.5 bestätigt das Wahlrecht für Investitionszuschüsse (BFH IV R 56/01). Die Einnahmen-Überschuss-Rechnung muss es schon im Jahr der Bewilligung ausüben (BFH IV R 81/05).
- H 5.6 enthält drei Stichworte:
  - „Ertragszuschüsse: Für Ertragszuschüsse ist ggf. ein passiver Rechnungsabgrenzungsposten zu bilden“ (BFH IV R 96/82).
  - „Investitionszuschüsse: Soweit Zuschüsse zu Anschaffungs- oder Herstellungskosten eines Wirtschaftsgutes geleistet werden, sind sie nicht passiv abzugrenzen“ (BFH X R 23/89).
  - „Zinszuschuss: Der kapitalisiert ausgezahlte Zinszuschuss für die Aufnahme eines langjährigen Kapitalmarktdarlehens ist passiv abzugrenzen“ (BFH IV R 26/06).

**Fundstelle:**

- R 6.5 EStR: `https://datenbank.nwb.de/Dokument/443548_6___5/` (VZ 2012 bis 2026). Gegengeprüft an `https://www.steuerschroeder.de/steuergesetze/estr/6.5`.
- H 6.5 EStH: `https://www.steuerschroeder.de/steuergesetze/esth/6.5` (Handbuch 2025). Gegengeprüft an Haufe, H 6.5 2024, bis zum abgeschnittenen Stichwort „Wahlrecht“.
- H 5.6 EStH: `https://www.steuerschroeder.de/steuergesetze/esth/5.6` (Handbuch 2025). Gegengeprüft an `https://datenbank.nwb.de/Dokument/1077356_5___6/` (VZ 2025 bis 2026).

**Belegqualität:** Wortlaut in Verlagswiedergabe, gegengeprüft. Die BFH-Urteile in H 5.6 sind nicht selbst gelesen.

**Folge für `MA-031` (Betriebsvermögen):**

- Das Wahlrecht nach R 6.5 Abs. 2 setzt einen Zuschuss im Sinne von Abs. 1 voraus. Ein Zuschuss, der eine Belegungs- und Mietbindung abgilt, steht in unmittelbarem wirtschaftlichem Zusammenhang mit einer Leistung des Empfängers, der Bindung. Er ist deshalb „in der Regel“ kein Zuschuss im Sinne von R 6.5.
- Er ist dann Entgelt für eine zeitraumbezogene Gegenleistung. Dafür sieht § 5 Abs. 5 Satz 1 Nr. 2 EStG einen passiven Rechnungsabgrenzungsposten vor, ebenso H 5.6 für Ertragszuschüsse und kapitalisierte Zinszuschüsse.
- Die Lesart „verteilt über die Bindung“ ist im Betriebsvermögen damit die am Text besser begründete. Die Minderung der Herstellungskosten (R 6.5 Abs. 2) passt nur zu einem reinen Investitionszuschuss.
- Das ist ein Schluss aus R 6.5 Abs. 1 Satz 3 und H 5.6. Ausdrücklich zum Bindungszuschuss äußert sich keine Richtlinie.
- Vorschlag: Im Betriebsvermögen „passiver Rechnungsabgrenzungsposten über die Bindungsdauer“ als begründete Voreinstellung führen. „Sofort“ und „Minderung der Herstellungskosten“ bleiben umschaltbar. Weil die Voreinstellung damit nicht mehr die ungünstigste ist, ist sie als begründete Ausnahme von der Vorsichtsregel zu kennzeichnen.

**Frage an den Steuerberater:** geschärft. „Bilden Sie für den NBank-Zuschuss und den Tilgungsnachlass in der Steuerbilanz der GmbH oder KG einen passiven Rechnungsabgrenzungsposten über die Bindungsdauer? Oder sehen Sie ihn als Investitionszuschuss mit Wahlrecht nach R 6.5?“

## 3. R 9.2 GewStR, H 9.2 GewStH und BFH I R 89/03: erweiterte Kürzung (`MA-030`)

**Frage:** Gehört der Gewinn aus dem Verkauf von Grundbesitz des Anlagevermögens zum gekürzten Ertrag? Was gilt bei einem Verkauf zum 31.12., 23:59 Uhr?

**Was der Text sagt:**

- R 9.2 Abs. 1 Satz 3 GewStR: „Die Voraussetzungen für die erweiterte Kürzung bei Grundstücksunternehmen müssen während des gesamten Erhebungszeitraums … vorliegen.“ Satz 4: Ob Grundbesitz zum Betriebsvermögen gehört, entscheidet sich „nicht … an einem bestimmten Stichtag“.
- H 9.2 (1), „Veräußerung des Grundbesitzes“: Der Verkauf des „einzigen und letzten Grundstücks“ während des Erhebungszeitraums „schließt die erhöhte Kürzung … für den Erhebungszeitraum aus“ (BFH vom 20.01.1982, BStBl II S. 478, und BFH vom 17.10.2024, BStBl 2025 II S. 158). Die Kürzung ist „jedoch zu gewähren, wenn das Unternehmen sein einziges Grundstück zum 31. Dezember, 23.59 Uhr, des Erhebungszeitraumes veräußert“ (BFH vom 11.08.2004, BStBl II S. 1080).
- H 9.2 (1), „Veräußerung eines Mitunternehmeranteils“: Dieser Gewinn wird nicht gekürzt; § 9 Nr. 1 Satz 6 GewStG hat insoweit klarstellende Bedeutung.
- H 9.2 (2), „Gewerblicher Grundstückshandel“: Er schließt die Kürzung aus. Beurteilt wird das nach dem Gesamtbild eines mehrjährigen Zeitraums. „Ein gelegentlicher Grundstücksverkauf stellt dagegen die ausschließliche Tätigkeit als Grundstücksverwaltungsgesellschaft nicht in Frage.“
- **H 9.2 (3), „Veräußerungsgewinne“:** „Veräußert ein Unternehmen, das die Voraussetzungen des § 9 Nr. 1 Satz 2 GewStG erfüllt, Grundbesitz, ist – vorbehaltlich des § 9 Nr. 1 Satz 5 Nr. 2 und Satz 6 GewStG – auch der bei der Veräußerung erzielte Gewinn gemäß § 9 Nr. 1 Satz 2 GewStG bei der Ermittlung des Gewerbeertrags zu kürzen (BFH vom 29.4.1987 – BStBl II S. 603).“
- H 9.2 (3), „Reinvestitionsrücklage“: Auch der Gewinn aus der Auflösung einer § 6b-Rücklage wird gekürzt, nicht aber der Gewinnzuschlag nach § 6b Abs. 7 EStG (BFH I R 17/99).
- § 9 Nr. 1 GewStG (am Original):
  - Satz 5 Nr. 2 schließt die Kürzung aus für stille Reserven aus Grundbesitz, der binnen drei Jahren vor der Aufdeckung unter dem Teilwert in den Betrieb gelangt ist.
  - Satz 6 schließt sie aus für den Teil des Gewerbeertrags, „der auf Veräußerungs- oder Aufgabegewinne im Sinne des § 7 Satz 2 Nr. 2 und 3 entfällt“, also auf den Mitunternehmeranteil und den Komplementäranteil der KGaA. Der Fall des § 7 Satz 2 Nr. 1, die Veräußerung oder Aufgabe des Betriebs, ist dort nicht genannt.
- BFH vom 11.08.2004, I R 89/03, Leitsatz: Die erweiterte Kürzung ist „unbeschadet des darin bestimmten Ausschließlichkeitsgebots zu gewähren, wenn das Unternehmen sein einziges Grundstück zum 31. Dezember, 23.59 Uhr, des Erhebungszeitraumes veräußert“.
  - Gründe II.2: Die Ausschließlichkeit sei „in zeitlicher Hinsicht um genau eine Minute unterschritten“. Das sei nicht erheblich, denn die Vereinbarung wirke „lediglich ‚technisch‘ …, ähnlich der sog. juristischen Sekunde“.
  - Zum Veräußerungsgewinn selbst sagt das Urteil nichts. Es überlässt die Berechnung dem Finanzamt (II.3).

**Fundstelle:**

- R 9.2 Abs. 1 GewStR: `https://www.steuerschroeder.de/steuergesetze/gewstr/9.2` (Gewerbesteuer-Handbuch 2024).
- H 9.2 (1) bis (4) GewStH: `https://datenbank.nwb.de/Dokument/1068784_9___2___1___/` bis `…_4___/` (Fassung VZ 2024 bis 2026). Gegengeprüft für H 9.2 (1) an Haufe, H 9.2 2024: `https://www.haufe.de/id/norm/gewerbesteuer-richtlinien-amtliche-hinweise-2024-h-92-kuerzung-bei-grundstuecksunternehmen-HI16827314_p9.2.html` (dort nach H 9.2 (1) abgeschnitten).
- BFH I R 89/03: `https://datenbank.nwb.de/Dokument/145695/` (BStBl 2004 II S. 1080).
- BFH I R 17/99: `https://datenbank.nwb.de/Dokument/97487/`, nur der Leitsatz gelesen.
- § 9 GewStG: `gesetze-im-internet.de/gewstg/__9.html`.

**Belegqualität:**

- R 9.2 Abs. 1, H 9.2 (1) und BFH I R 89/03: Wortlaut in Verlagswiedergabe, H 9.2 (1) gegengeprüft.
- H 9.2 (3): Wortlaut in Verlagswiedergabe, eine Wiedergabe. Die zweite (steuerschroeder) lieferte am 2026-11-18 wiederholt Fehler 500.
- § 9 GewStG am Original.
- BFH vom 29.04.1987 (BStBl II S. 603) nicht selbst gelesen, nur über H 9.2 (3).

**Folge für `MA-030`:**

- Die Kernfrage ist nach Verwaltungsauffassung beantwortet: Der Veräußerungsgewinn aus Grundbesitz gehört zum gekürzten Ertrag. Die heutige Voreinstellung „Verkaufsgewinn gewerbesteuerpflichtig, nur laufender Ertrag gekürzt“ hat danach keine Grundlage, solange die Kürzung im Verkaufsjahr überhaupt zusteht.
- Vorschlag für die Annahme, mit drei Fällen:
  1. Bleibt nach dem Verkauf weiterer Grundbesitz im Unternehmen, oder geht der letzte Grundbesitz zum 31.12., 23:59 Uhr, über: Der Verkaufsgewinn wird mitgekürzt (H 9.2 (3); BFH I R 89/03).
  2. Geht der letzte Grundbesitz früher über: Die erweiterte Kürzung entfällt für das ganze Jahr, für den laufenden Ertrag und für den Verkaufsgewinn; es bleibt die einfache Kürzung (BFH III R 1/23).
  3. Ausnahmen in jedem Fall: Anteile an Mitunternehmerschaften (§ 9 Nr. 1 Satz 6), Grundbesitz, der binnen drei Jahren unter dem Teilwert eingebracht wurde (Satz 5 Nr. 2), und gewerblicher Grundstückshandel (H 9.2 (2)).
- Der Fall 1 ist keine Ausnahme von der Vorsichtsregel mehr, sondern Verwaltungsauffassung. Die „andere Lesart“ wird zur strengeren: „Die Finanzverwaltung ändert H 9.2 (3), oder ein Gericht folgt ihr nicht.“
- Gewicht: hoch bleibt, weil die Weiche „Übergang vor oder nach 23:59 Uhr“ den ganzen Verkaufsgewinn betrifft.
- Die Eingabe „Übergang zum 31.12., 23:59 Uhr“ aus Notiz 13 wird damit tragend.

**Frage an den Steuerberater:** geschärft, nicht entfallen. „Nach H 9.2 (3) GewStH wird der Verkaufsgewinn mitgekürzt. Sehen Sie bei unseren Objektgesellschaften Risiken aus gewerblichem Grundstückshandel oder aus § 9 Nr. 1 Satz 5 Nr. 2 GewStG? Und vereinbaren Sie den Übergang in der Praxis zum 31.12., 23:59 Uhr?“

## 4. R 7.1 Abs. 3 GewStR, H 7.1 (3) GewStH und BFH IV R 3/05 (`MA-036`)

**Frage:** Ist der Gewinn aus dem Verkauf des einzigen Objekts einer gewerblich geprägten GmbH & Co. KG ein begünstigter Aufgabegewinn nach § 7 Satz 2 GewStG?

**Was der Text sagt:**

- R 7.1 Abs. 3 GewStR:
  - Satz 1: Für die Gewerbesteuer sind „§ 16 Abs. 1 Satz 1 Nr. 1 Satz 1, Nr. 2, Nr. 3 und Abs. 3 Satz 1 EStG (Veräußerung oder Aufgabe des Betriebs)“ nicht anzuwenden.
  - Satz 2: „Betriebseinnahmen und Betriebsausgaben …, welche nicht mit der Unterhaltung eines laufenden Gewerbebetriebs zusammenhängen“, sind auszuscheiden.
  - Satz 4: Der Gewinn einer Mitunternehmerschaft aus Veräußerung oder Aufgabe „ist jedoch nur insoweit gewerbesteuerfrei, als er auf eine natürliche Person als unmittelbar beteiligten Mitunternehmer entfällt“.
- § 7 Satz 2 GewStG (am Original) sagt dasselbe für „des Betriebs oder eines Teilbetriebs einer Mitunternehmerschaft“.
- H 7.1 (3), „Veräußerungs- und Aufgabegewinne“:
  - Gewinne aus der Veräußerung oder Aufgabe eines Gewerbebetriebs „gehören vorbehaltlich der Anwendung des § 7 Satz 2 GewStG bei einer Personengesellschaft nicht zum Gewerbeertrag“.
  - Sie sind laufender Gewinn, soweit auf beiden Seiten dieselben Personen beteiligt sind.
  - „Eine GmbH & Co. KG, die ihren Geschäftsbereich veräußert und lediglich eine wesentliche Betriebsgrundlage zurückbehält, die sie fortan vermietet, bleibt gewerbesteuerpflichtig“ (BFH vom 17.03.2010, BStBl II S. 977).
  - Aus der Einkommensteuer gilt: Gewinne bei der Aufgabe sind laufender Gewinn, „soweit einzelne dem Betrieb gewidmete Wirtschaftsgüter im Rahmen der Aufgabe des Betriebs veräußert werden“ und dieselben Personen Veräußerer und Erwerber sind.
- BFH vom 14.12.2006, IV R 3/05 (BStBl 2007 II S. 777):
  - Leitsatz: „Ein Grundstück gehört nur dann zum Umlaufvermögen einer gewerblich geprägten Personengesellschaft, wenn bei der Gesellschaft die Voraussetzungen eines gewerblichen Grundstückshandels erfüllt sind.“
  - Gründe II.2: Ist die Gesellschaft „lediglich nach § 15 Abs. 3 Nr. 2 EStG kraft Rechtsform gewerblich“ tätig, hätte das Grundstück „nicht zum Umlaufvermögen … gehören können“. Weiter: „Wird es während des Bestehens des Betriebs veräußert, führt die Veräußerung zu einem laufenden Gewinn …. Findet die Veräußerung im Rahmen einer Betriebsveräußerung oder -aufgabe statt, ist der Gewinn nach §§ 16, 34 EStG begünstigt.“
  - Gründe II.1.a: Begünstigte Veräußerungs- und Aufgabegewinne nach §§ 16, 34 EStG sind aus dem Gewerbeertrag auszuscheiden.
  - Gründe II.1.b: Beim gewerblichen Grundstückshändler ist dagegen selbst der Verkauf des letzten Grundstücks laufender Gewinn.

**Fundstelle:**

- R 7.1 GewStR (i. d. F. vom 28.04.2010): `https://datenbank.nwb.de/Dokument/363299_7___1/`.
- H 7.1 (3) GewStH (VZ 2024 bis 2026): `https://datenbank.nwb.de/Dokument/1068784_7___1___3___/`.
- BFH IV R 3/05: `https://datenbank.nwb.de/Dokument/252516/`.
- § 7 GewStG: `gesetze-im-internet.de/gewstg/__7.html`.

**Belegqualität:** Wortlaut in Verlagswiedergabe, je eine Wiedergabe. Die steuerschroeder-Seiten zu R 7.1 Abs. 3 lieferten Fehler 500 oder Zeitüberschreitung. § 7 GewStG am Original.

**Folge für `MA-036`:**

- Beide Lesarten sind belegt: laufender Gewinn bei Verkauf während des Bestehens, begünstigter Gewinn bei Verkauf im Rahmen einer Aufgabe.
- Die Weiche ist eine Tatsachenfrage. Wird der Betrieb mit dem Verkauf eingestellt? Bleibt etwas zurück, das weiter vermietet wird (H 7.1 (3), BFH 17.03.2010)? Liegt gewerblicher Grundstückshandel vor (dann immer laufend)?
- Die vorsichtige Voreinstellung „laufender Gewinn“ bleibt richtig. Die andere Lesart sollte als Eingabe „Verkauf im Rahmen der Aufgabe des Betriebs (Gesellschaft wird eingestellt)“ geführt werden, mit dem Hinweis, dass bei gewerblichem Grundstückshandel immer laufender Gewinn vorliegt.
- Zusammenspiel mit `MA-030`: § 9 Nr. 1 Satz 6 GewStG nimmt nur § 7 Satz 2 Nr. 2 und 3 von der erweiterten Kürzung aus, nicht Nr. 1. Ein steuerpflichtiger Anteil am Aufgabegewinn, etwa der einer Komplementär-GmbH mit Vermögensanteil, fiele danach unter die Kürzung, wenn diese im Jahr zusteht. Das ist ein Schluss aus dem Wortlaut, nicht gelesen in Richtlinie oder Urteil.

**Frage an den Steuerberater:** geschärft. „Gilt der Verkauf des einzigen Objekts einer gewerblich geprägten KG als Aufgabe nach § 16 Abs. 3 EStG, wenn die KG danach nur noch den Erlös hält und liquidiert wird? Ab wann sehen Sie die Einstellung als vollzogen?“

## 5. KStR/KStH zu § 5 Abs. 1 Nr. 10 KStG und BMF vom 22.11.1991 (Steuerberater, Frage 5)

**Frage:** Zählt der Erlös aus dem Verkauf eines Objekts der befreiten Vermietungsgenossenschaft zu den Einnahmen aus nicht begünstigter Tätigkeit (10-%-Grenze)?

**Was der Text sagt:**

- Die Richtlinie trägt die Nummer **R 5.9 KStR 2022** („Vermietungsgenossenschaften und -vereine“, Fassung vom 13.04.2022). Sie ist „– unbesetzt –“.
- H 5.9 KStH (Fassung VZ 2026): „Zur Steuerbefreiung für Vermietungsgenossenschaften und -vereine … >BMF vom 22.11.1991 (BStBl I S. 1014) und die entsprechenden Erlasse der obersten Finanzbehörden der Länder.“ Notiz 13 hatte „R 5.9“ vermutet; das stimmt.
- BMF vom 22.11.1991, IV B 7 - S 2730 - 24/91, gelesen in der wortgleichen Verfügung der OFD Frankfurt vom 23.09.2013 (S 2730 A - 15 - St 53), die das Schreiben mit denselben Textziffern wiedergibt:
  - Tz. 32: Begriff und Höhe der Einnahmen „(Einnahmen einschließlich Umsatzsteuer) bestimmen sich nach den Grundsätzen über die steuerliche Gewinnermittlung“; die Bereiche werden „nach den gleichen Grundsätzen“ ermittelt.
  - Tz. 38: „Geschäfte, die zur Abwicklung der begünstigten Tätigkeiten notwendig sind und die im Rahmen der begünstigten Tätigkeiten erfolgen, sind ebenfalls begünstigt. Einnahmen aus solchen Geschäften fallen deshalb nicht unter die 10 v. H.-Grenze.“
  - Tz. 39: Zu den begünstigten Geschäften gehört „die Veräußerung von Betriebsgrundstücken oder von Teilen von Betriebsgrundstücken aus dem begünstigten Bereich. Der Verkauf von bebauten oder unbebauten Grundstücken ist aber nicht begünstigt, wenn der Grundstückshandel gewerblichen Charakter annimmt“.
  - Tz. 42: Nicht begünstigt ist der Verkauf von Wirtschaftsgütern „aus dem nicht begünstigten steuerpflichtigen Gewerbebetrieb“.
  - Zusatz der OFD: Das BMF-Schreiben stand 2012 nicht in der Positivliste. Die **Positivliste vom 20.03.2026** (BStBl 2026 I S. 394, Anlage 1, lfd. Nr. 1167) führt es wieder, und H 5.9 KStH verweist darauf. Es gilt also.
- Der Kommentar Herrmann/Heuer/Raupach (§ 5 KStG Anm. 202, 204; Stand der Kommentierung Mai 2015) gibt dasselbe wieder. Er stellt den Einnahmebegriff auf Bruttoeinnahmen ab und zitiert dazu Rz. 32 ff. und 37 des Schreibens.

**Fundstelle:**

- R 5.9 KStR: `https://datenbank.nwb.de/Dokument/883112_5___9/`.
- H 5.9 KStH: `https://datenbank.nwb.de/Dokument/1102750_5___9/`.
- OFD Frankfurt vom 23.09.2013: `https://datenbank.nwb.de/Dokument/480060/`.
- Positivliste vom 20.03.2026: `https://datenbank.nwb.de/Dokument/1090883/`.
- HHR-Auszug: `https://www.steuerberater-center.de/media/KStG_005_302_02-2021_Anm0183-0209.pdf`.
- Das BMF-Schreiben selbst steht bei NWB unter `…/Dokument/83622/`, ist dort aber kostenpflichtig und wurde nicht geöffnet.

**Belegqualität:**

- R 5.9, H 5.9 und Positivliste: Wortlaut in Verlagswiedergabe.
- BMF vom 22.11.1991: Wortlaut der Tz. 32 bis 42 in einer amtlichen Wiedergabe (OFD-Verfügung) über den Verlag, gegengeprüft am Kommentar HHR (sekundär). Das Schreiben selbst im BStBl ist nicht erreicht.

**Folge:** Die Frage an den Steuerberater entfällt in der bisherigen Form.

- Der Verkauf eines Objekts der Genossenschaft aus dem begünstigten Bereich ist begünstigtes Geschäft. Der Erlös zählt nicht zu den Einnahmen aus nicht begünstigter Tätigkeit.
- Als Einnahme im begünstigten Bereich erhöht er sogar den Nenner der 10-%-Prüfung.
- Zu modellieren ist nur die Ausnahme: gewerblicher Grundstückshandel. Er ist bei einem einzelnen Verkauf nicht zu erwarten, wird aber als Meldung vorgesehen, wenn die Genossenschaft in kurzer Folge mehrere Objekte verkauft.
- Rest-Frage, falls der Steuerberater Zeit hat: „Werten Sie Verkäufe unserer Genossenschaft als gewerblichen Grundstückshandel, und ab wie vielen Objekten?“

## 6. BMF vom 27.07.2015: Schuldzinsen und Vorfälligkeitsentschädigung nach Verkauf (`MA-032`)

**Was der Text sagt:**

- Nr. 1.1, Schuldzinsen nach Verkauf: Sie bleiben nachträgliche Werbungskosten, „wenn und soweit die Verbindlichkeiten nicht durch den Veräußerungserlös hätten getilgt werden können (sog. Grundsatz des Vorrangs der Schuldentilgung)“. Das gilt auch beim nicht steuerbaren Verkauf (BFH IX R 45/13).
- Nr. 2, Vorfälligkeitsentschädigung: Der Zusammenhang mit der Vermietung wird „im Zuge der Veräußerung überlagert bzw. von einem neuen, durch die Veräußerung ausgelösten Veranlassungszusammenhang ersetzt“. Sie ist deshalb „keine nachträglichen Werbungskosten bei den Einkünften aus Vermietung und Verpachtung, sondern Veräußerungskosten bei der Ermittlung der Einkünfte i. S. d. § 23 Absatz 3 i. V. m. § 23 Absatz 1 Satz 1 Nummer 1 EStG“. Die ältere Rechtsprechung, die beim Erwerb eines neuen Mietobjekts ausnahmsweise Werbungskosten zuließ (BFH IX R 5/94), „ist … überholt“. Sie gilt letztmals bei Kaufverträgen vor dem 27.07.2015.
- Nr. 3: Für Schuldzinsen nach Aufgabe der Einkünfteerzielungsabsicht vor dem Verkauf gibt es keinen Abzug.
- Das Schreiben ersetzt die Schreiben vom 28.03.2013 und 15.01.2014. Es steht in der Positivliste vom 20.03.2026 (Anlage 1, lfd. Nr. 788).

**Fundstelle:** BMF vom 27.07.2015, IV C 1 - S 2211/11/10001, DOK 2015/0644430, BStBl I 2015 S. 581: `https://datenbank.nwb.de/Dokument/545773/`. Die Fundstelle im BStBl ist an der Positivliste gegengeprüft.

**Belegqualität:** Wortlaut in Verlagswiedergabe, vollständig, eine Wiedergabe. Das PDF beim BMF ist nicht gefunden (vermutete Adressen lieferten 404); das EStH, Anhang 30 IV, hat ein Captcha.

**Folge für `MA-032`:**

- Der Teil „Vorfälligkeitsentschädigung der Privatperson“ ist Verwaltungsauffassung und kann aus der Annahme herausgenommen werden. Grundlage: „BMF vom 27.07.2015 (BStBl I S. 581), Nr. 2.“
- Neu für den Kern: Schuldzinsen auf einen nach dem Verkauf verbleibenden, durch den Erlös nicht tilgbaren Darlehensrest bleiben Werbungskosten, auch beim steuerfreien Verkauf. Für die Haltedauer bis zum Verkauf ist das ohne Wirkung; es betrifft nur Rechnungen über den Verkauf hinaus. Kein Handlungsbedarf, solange der Kern mit dem Verkauf endet.

**Frage an den Steuerberater:** Der Teil zur Vorfälligkeit entfällt. Es bleibt nur die Frage zum NBank-Bearbeitungsentgelt.

## 7. Marktübliches Damnum (`MA-032`, Hausbank H10)

**Frage:** Welches BMF-Schreiben enthält die 5-%-Grenze?

**Was der Text sagt:**

- BMF vom 20.10.2003, IV C 3 - S 2253 a - 48/03 (BStBl I 2003 S. 546; „Bauherren- und Fondserlass“), Rz. 15:
  - Damnum, Disagio, Bearbeitungs- und Auszahlungsgebühren sind abziehbar, „soweit unter Berücksichtigung der jährlichen Zinsbelastung die marktüblichen Beträge nicht überschritten werden. Der über die marktüblichen Beträge hinausgehende Teil ist auf den Zinsfestschreibungszeitraum oder bei dessen Fehlen auf die Laufzeit des Darlehens zu verteilen.“
  - „Aus Vereinfachungsgründen kann von der Marktüblichkeit ausgegangen werden, wenn für ein Darlehen mit einem Zinsfestschreibungszeitraum von mindestens 5 Jahren ein Damnum in Höhe von bis zu 5 v. H. vereinbart worden ist.“
  - Weiter: Ist das Damnum höchstens drei Monate vor Auszahlung eines ins Gewicht fallenden Teils (mindestens 30 %) geleistet, wird ein wirtschaftlich vernünftiger Grund angenommen.
- Rz. 22 desselben Schreibens: Gebühren für die Vermittlung der Finanzierung sind „in Höhe der marktüblichen Konditionen“ abziehbar, „erfahrungsgemäß … insgesamt 2 v. H. des jeweils vermittelten Darlehens“.
- BMF vom 05.04.2005, IV A 3 - S 2259 - 7/05 (BStBl I 2005 S. 617), regelt die Anwendung des neuen § 11 Abs. 2 Satz 3 EStG. Zum Damnum: Es wird nicht beanstandet, die Neuregelung nicht auf ein Damnum anzuwenden, das vor dem 01.01.2006 abgeflossen ist; „die Abziehbarkeit nach Maßgabe der bisherigen Verwaltungspraxis (Rz. 15 des BMF-Schreibens v. 20.10.2003, BStBl 2003 I S. 546) bleibt damit im Ergebnis erhalten“. Die Grenze selbst steht also nur im Schreiben von 2003.
- Beide Schreiben stehen in der Positivliste vom 20.03.2026 (Anlage 1, lfd. Nr. 943 und 969).

**Fundstelle:**

- BMF vom 20.10.2003: `https://datenbank.nwb.de/Dokument/88184/`. Gegengeprüft an der wortgleichen Verfügung der OFD München/Nürnberg vom 10.12.2003, `https://datenbank.nwb.de/Dokument/125776/`.
- BMF vom 05.04.2005: `https://datenbank.nwb.de/Dokument/161868/`.

**Belegqualität:** Wortlaut in Verlagswiedergabe, gegengeprüft.

**Folge für `MA-032`:**

- Die Teilannahme „Disagio der Privatperson marktüblich“ wird zu einer Prüfregel: Bis 5 % bei mindestens fünf Jahren Zinsbindung wird sofort abgezogen. Darüber wird der übersteigende Teil auf die Zinsbindung verteilt, ohne Bindung auf die Laufzeit.
- Für die Bearbeitungsentgelte der NBank liefert Rz. 15 einen Anhalt: Auch „Bearbeitungs- und Auszahlungsgebühren“ fallen unter dieselbe Marktüblichkeitsprüfung. Das betrifft die Privatperson, nicht die Abgrenzung im Betriebsvermögen.
- Kataster: Der Eintrag `BMF-DAMNUM-2005` aus Notiz 13 trägt falsch. Vorschlag: `BMF-BAUHERREN-2003` neu, `BMF-EURLUMSG-2005` nur als Anwendungsschreiben.

**Frage an die Hausbank (H10):** bleibt, unverändert Hauspraxis. Die steuerliche Grenze ist aber jetzt belegt.

## 8. R 21.1 Abs. 3 EStR: Außenanlagen (`MA-023`)

**Was der Text sagt:**

- R 21.1 Abs. 3 Satz 1: „Kosten für die gärtnerische Gestaltung der Grundstücksfläche bei einem Wohngebäude gehören nur zu den Herstellungskosten des Gebäudes, soweit diese Kosten für das Anpflanzen von Hecken, Büschen und Bäumen an den Grundstücksgrenzen (‚lebende Umzäunung‘) entstanden sind.“
- Satz 2: „Im Übrigen bildet die bepflanzte Gartenanlage ein selbständiges Wirtschaftsgut.“
- Satz 3: Gartenanlagen, die Mieter mitbenutzen dürfen, und Vorgärten werden auf „regelmäßig 10 Jahre“ abgeschrieben.
- BMF vom 21.05.2025 zu § 7b, Rn. 45 (Notiz 13, am Original): „Für die Aufwendungen für Außenanlagen gilt R 21.1 Absatz 3 Satz 1 EStR.“
- Ergänzend H 6.4 und H 7.1 EStH (Handbuch 2025):
  - „Die zu einem Gebäude gehörende Gartenanlage ist ein selbständiges Wirtschaftsgut“ (BFH IX R 18/91).
  - Die Umzäunung eines Mietwohngrundstücks kann im Nutzungszusammenhang mit dem Gebäude stehen und gehört „daher i. d. R. zu den Gebäudeherstellungskosten“ (BFH VIII R 121/73).
  - „Hofbefestigungen und Straßenzufahrt stehen i. d. R. mit einem Betriebsgebäude in keinem einheitlichen Nutzungs- und Funktionszusammenhang“ (BFH III R 161/81).
  - H 7.1 führt Außenanlagen bei Betriebsgrundstücken als eigene unbewegliche Wirtschaftsgüter, „nicht aber Umzäunungen bei Wohngebäuden“.

**Fundstelle:**

- R 21.1 EStR: `https://www.steuerschroeder.de/steuergesetze/estr/21.1` (Handbuch 2025). Gegengeprüft an `https://datenbank.nwb.de/Dokument/443548_21___1/` (VZ 2012 bis 2026) und an Haufe, EStR 2008, R 21.1 (Satz 1 wortgleich).
- H 6.4 und H 7.1: `…/steuergesetze/esth/6.4` und `…/esth/7.1`.

**Belegqualität:** R 21.1 Abs. 3 im Wortlaut in Verlagswiedergabe, gegengeprüft. H 6.4 und H 7.1: Wortlaut in Verlagswiedergabe, eine Wiedergabe.

**Folge für `MA-023`:**

- Der letzte offene Punkt ist geklärt. Zur Kostenbasis der Baukostenobergrenze zählen von den Außenanlagen nur die Einfriedung des Wohngrundstücks (Zaun, lebende Umzäunung) und Erdarbeiten, die zum Gebäude gehören.
- Gartenanlagen, Wege, Hofbefestigung und Zufahrten zählen nicht; sie sind eigene Wirtschaftsgüter.
- In Kostengruppen nach DIN 276 heißt das: KG 500 grundsätzlich nicht, mit Ausnahme der Einfriedungen. Die vorsichtige Zwischenlösung „Außenanlagen zählen mit“ aus Notiz 13 kann entfallen.
- Weil KG 500 im Kern meist als Summe vorliegt, sollte die Annahme lauten: „KG 500 zählt nicht zur Kostenbasis; Einfriedungen sind als Eingabe zurechenbar.“ Gewicht: gering.

**Frage an den Steuerberater:** entfällt.

## 9. § 10d Abs. 2 EStG ab 2028 (`MA-010`)

**Was der Text sagt:**

- Wachstumschancengesetz vom 27.03.2024, BGBl. 2024 I Nr. 108:
  - Art. 2 Nr. 4 ersetzt in § 10d Abs. 2 Satz 1 „60 Prozent“ durch „70 Prozent“; § 52 Abs. 18b Satz 3 gilt ab VZ 2024.
  - **Art. 6 Nr. 1** ersetzt „70 Prozent“ durch „60 Prozent“.
  - Art. 6 Nr. 2 fügt an § 52 Abs. 18b an: „§ 10d Absatz 2 Satz 1 in der Fassung des Artikels 6 … ist erstmals für den Veranlagungszeitraum 2028 anzuwenden.“
  - Art. 35 Abs. 9: „Artikel 6 tritt am 1. Januar 2028 in Kraft.“ Art. 2 trat mit Wirkung vom 01.01.2024 in Kraft (Abs. 4).
- gesetze-im-internet.de zeigt heute 70 %, weil Art. 6 noch nicht in Kraft ist.
- Der Regierungsentwurf des Jahressteuergesetzes 2026 (BR-Drs. 447/26 vom 14.08.2026) ändert § 10d Abs. 2 nicht; geprüft per Volltextsuche.

**Fundstelle:** `https://www.recht.bund.de/bgbl/1/2024/108/VO.html`, PDF `…/regelungstext.pdf`, S. 7, 12, 36.

**Belegqualität:** am Original.

**Folge für `MA-010`:**

- Die Annahme ist geklärt. Die 60 % ab VZ 2028 sind geltendes, verkündetes Recht und keine Modellannahme mehr.
- Vorschlag: Status „erledigt am 2026-11-18“. Die Regel wandert als Festlegung in den Katalog, mit Kennung `BGBL-2024-I-108` und dem Vermerk „Gesetzesänderung vor 2028 möglich; vierteljährliche Rechtsprüfung“.
- Nicht geprüft ist, ob ein anderes Gesetz von 2025 oder 2026 außer dem JStG-Entwurf Art. 6 aufhebt. Das gehört in die vierteljährliche Rechtsprüfung, nicht in die Annahme.

**Frage an den Steuerberater:** entfällt.

## 10. BFH vom 14.10.2003, IX R 60/02 (BStBl II 2004 S. 14)

**Was der Text sagt:**

- Leitsatz: „Öffentliche Fördermittel (Zuschüsse oder nicht rückzahlbare Darlehen), die ein Bauherr zur Förderung von Mietwohnraum im Rahmen des sog. Dritten Förderungswegs für Belegungs- und Mietpreisbindungen erhält, sind als Einnahmen aus Vermietung und Verpachtung im Kalenderjahr des Zuflusses zu versteuern.“
- II.1: „Unerheblich ist dabei, ob der Mieter selbst oder ein Dritter die Gegenleistung erbringt“, sofern ein „unmittelbarer rechtlicher und wirtschaftlicher Zusammenhang“ besteht, „wie dies z. B. bei einer Mietpreisbindung oder einem Belegungsrecht der Fall ist“.
- II.2.a: Die Mittel sind Ausgleich „für den darin liegenden Verzicht auf eine günstigere Vermietung“. Sie sind nach § 11 Abs. 1 EStG „im Jahr des Zuflusses zu erfassen …, und zwar unabhängig davon, ob als sog. leistungsfreies Darlehen oder als Zuschuss“.
- II.2.b: Die Zuschüsse „mindern … nicht die Herstellungskosten“. Sie dienen „nicht dazu, ein Objekt zu errichten, sondern bilden die Gegenleistung … für die vertraglich eingegangenen Bindungen“. Die Bindungen sind „zeitlich begrenzt und decken sich nicht mit der Nutzungsdauer“.
- Das Urteil erging vor Einführung von § 11 Abs. 1 Satz 3 EStG (Gesetz vom 09.12.2004). Zur Verteilung sagt es deshalb nichts; diese Lücke schließt R 21.5 Abs. 2 mit dem Verweis auf § 11 Abs. 1 Satz 3.

**Fundstelle:** `https://datenbank.nwb.de/Dokument/122750/`. Gegengeprüft für Leitsatz und Kernsatz an Haufe, „Mieteinnahmen-ABC / Öffentliche Fördermittel für Belegungs- und Mietpreisbindung“.

**Belegqualität:** Wortlaut in Verlagswiedergabe, vollständig. Gegenprüfung nur für Leitsatz und Kernsatz.

**Folge:** wie Abschnitt 1. Die Lesart „Minderung der Herstellungskosten“ ist für den Bindungszuschuss bei der Privatperson ausgeschlossen.

## 11. Mietrecht: Rechtsprechung des BGH (nachrangig)

### `MA-007` Dauer des Drittmittelabzugs

**Was der Text sagt:** BGH vom 13.06.2012, VIII ZR 311/11.

- Rn. 20: Der Senat hält es „für geboten, die gesetzliche Anrechnungspflicht in verfassungskonformer Auslegung … auf einen bestimmten Zeitraum zu begrenzen“, und „für sachgerecht, diesen Zeitraum mit zwölf Jahren, beginnend ab der mittleren Bezugsfertigkeit des geförderten Objekts, zu bemessen (Senatsurteil vom 25. Februar 2004 - VIII ZR 116/03)“.
- Rn. 22 leitet die zwölf Jahre so her: Die Kürzung um 11 % des Förderbetrags zehrt den Zuschuss „nach etwas über neun Jahren“ auf; mit „angemessener Verzinsung“ ergeben sich zwölf Jahre.
- Rn. 24 bis 27: Eine längere vertragliche Bindung im Fördervertrag (dort 20 Jahre) verlängert die gesetzliche Anrechnung nicht.

**Fundstelle:** `https://gesetze.co/urteile/VIII_ZR_311-11`. Volltext mit Randnummern. Die „KI-Orientierungssätze“ der Seite sind nicht amtlich und wurden nicht verwendet.

**Belegqualität:** Wortlaut in Verlagswiedergabe (nichtamtliche Sammlung), eine Wiedergabe. Die Entscheidungsdatenbank des BGH war nicht erreichbar (siehe unten).

**Folge für `MA-007`:**

- Die Annahme „über den gesamten Betrachtungszeitraum“ ist strenger als die Rechtsprechung. Vorschlag für die Voreinstellung: Abzug für zwölf Jahre ab mittlerer Bezugsfertigkeit der geförderten Maßnahme.
- Neue andere Lesart: länger, weil der BGH die zwölf Jahre aus dem damaligen Umlagesatz von 11 % abgeleitet hat. Bei heute 8 % zehrt sich der Zuschuss erst nach rund 12,5 Jahren auf, mit Verzinsung entsprechend später. Diese Umrechnung ist eine eigene Überlegung, nicht vom BGH entschieden.
- Gewicht: mittel bleibt. Klärung durch: Anwalt, nur noch zur Frage, ob die Zwölf-Jahres-Frist bei 8 % fortgilt.

### `MA-018` Gaskesseltausch

**Was der Text sagt:** BGH vom 26.03.2025, VIII ZR 283/23 (ECLI:DE:BGH:2025:260325UVIIIZR283.23.0).

- Leitsatz: Die Erhöhung nach § 559 Abs. 1 a. F. i. V. m. § 555b Nr. 1 BGB setzt voraus, dass „zum (ex ante-)Zeitpunkt der Abgabe der Mieterhöhungserklärung eine (allein) durch die erfolgte bauliche Veränderung hervorgerufene messbare und dauerhafte Einsparung von Endenergie zu erwarten ist“. Dabei „kann auch auf anerkannte Pauschalwerte zurückgegriffen werden“.
- Rn. 31: Eine Einsparung liegt nach der Vorstellung des Gesetzgebers auch vor, wenn die Nutzenergie „mit größerer Effizienz (beispielsweise durch Erneuerung des Heizkessels oder die Verringerung der Wärmverluste zwischen Heizkessel und Heizkörpern)“ bereitgestellt wird.
- Der entschiedene Fall betraf den Ersatz von Gasthermen in den Wohnungen durch eine Gaszentralheizung.

**Fundstelle:** Urteilsabschrift als PDF beim RWS Verlag: `https://www.rws-verlag.de/fileadmin/Volltexte-4/viii_zr_283-23.pdf`.

**Belegqualität:** Wortlaut des amtlichen Urteils in Verlagswiedergabe, eine Wiedergabe.

**Folge für `MA-018`:**

- Die Voreinstellung „Kesseltausch ist keine energetische Modernisierung“ ist strenger als der BGH. Nach VIII ZR 283/23 kann die Erneuerung eines Heizkessels energetische Modernisierung sein, wenn eine messbare, dauerhafte Endenergieeinsparung zu erwarten ist.
- Beim Ersatz eines alten durch einen neuen Gaskessel kommt hinzu, dass der Erhaltungsanteil abzuziehen ist (§ 559 Abs. 2 BGB; nicht Gegenstand dieses Urteils).
- Vorschlag: Die Voreinstellung bleibt vorsichtig, weil das Modell die Einsparung nicht prüfen kann. Die Grundlage wird ergänzt: „BGH VIII ZR 283/23, Rn. 31: Kesselerneuerung kann Endenergie einsparen; Umlage nur mit Nachweis einer messbaren Einsparung und nach Abzug des Erhaltungsanteils.“
- Die andere Lesart wird zur Eingabe „Einsparung nachgewiesen“ mit Erhaltungsanteil.

### `MA-019` und `MA-025`

Zum Zinsvorteil bei § 559e BGB (`MA-019`) und zur Glasfaser nach § 555b Nr. 4a BGB (`MA-025`) wurde in einer Websuche keine Entscheidung des BGH gefunden. Beide Vorschriften sind jung (2024 und 2021). Eine Suche in der Entscheidungsdatenbank des BGH war nicht möglich. Die Annahmen bleiben unverändert.

## Vorschläge

### (a) Modellannahmen

| Kennung | Vorschlag |
|---|---|
| `MA-010` | Als geklärt schließen. Die 60 % ab VZ 2028 sind verkündetes Recht (BGBl. 2024 I Nr. 108, Art. 6 und Art. 35 Abs. 9) und werden Festlegung im Katalog. |
| `MA-023` | Offenen Rest schließen: Außenanlagen (KG 500) zählen nicht zur Kostenbasis, Einfriedungen des Wohngrundstücks schon (R 21.1 Abs. 3 Satz 1 EStR; H 6.4, H 7.1 EStH). Gewicht gering. |
| `MA-030` | Annahme neu fassen, drei Fälle wie in Abschnitt 3: Verkaufsgewinn mitgekürzt bei weiterem Grundbesitz oder Übergang zum 31.12., 23:59 Uhr; Wegfall der Kürzung im ganzen Jahr bei früherem Übergang des letzten Grundbesitzes; Ausnahmen nach § 9 Nr. 1 Satz 5 Nr. 2 und Satz 6 GewStG und beim gewerblichen Grundstückshandel. Die bisherige Voreinstellung wird zur „anderen Lesart“. Grundlage: H 9.2 (1) und (3) GewStH, BFH I R 89/03, BFH III R 1/23. Gewicht bleibt hoch. Der Referenzfall „Ankauf“ ist neu zu rechnen, weil die bisher vorsichtige Lesart wegfällt. |
| `MA-031` | Nach Rechtsform trennen. **Privatperson:** Einnahme im Zuflussjahr (R 21.5 Abs. 2, H 21.5, BFH IX R 60/02); Verteilung als Antrag nach § 11 Abs. 1 Satz 3 EStG, wenn die Bindung länger als fünf Jahre dauert; „Minderung der Herstellungskosten“ nicht wählbar. **Betriebsvermögen:** passiver Rechnungsabgrenzungsposten über die Bindung als begründete Voreinstellung (R 6.5 Abs. 1 Satz 3, H 5.6 „Ertragszuschüsse“), „sofort“ und „Minderung“ umschaltbar. Befund 1 der Prüfrunde 2 ist für die Privatperson widerlegt, für das Betriebsvermögen bestätigt. |
| `MA-032` | Vorfälligkeit der Privatperson aus der Annahme nehmen; sie ist Verwaltungsauffassung (BMF vom 27.07.2015, Nr. 2). Disagio der Privatperson als Prüfregel: bis 5 % bei mindestens fünf Jahren Zinsbindung sofort, darüber Verteilung des Mehrbetrags (BMF vom 20.10.2003, Rz. 15). Offen bleibt nur das NBank-Entgelt. |
| `MA-036` | Grundlage ergänzen: R 7.1 Abs. 3 Satz 4 GewStR, H 7.1 (3) GewStH, BFH IV R 3/05 (II.2). Die Voreinstellung bleibt. Die andere Lesart wird zur Eingabe „Verkauf im Rahmen der Aufgabe“, mit Meldung bei gewerblichem Grundstückshandel. |
| `MA-007` | Voreinstellung auf zwölf Jahre ab mittlerer Bezugsfertigkeit umstellen (BGH VIII ZR 311/11, Rn. 20 bis 22). Andere Lesart: länger wegen 8 % statt 11 %. Klärung durch: Anwalt, eingeschränkt auf diese Frage. |
| `MA-018` | Grundlage um BGH VIII ZR 283/23, Rn. 31, ergänzen. Die Voreinstellung bleibt; die andere Lesart wird zur Eingabe „Einsparung nachgewiesen“ mit Erhaltungsanteil. |

### (b) Leitfaden für den Steuerberater

- **Entfällt:**
  - Frage 5 (Genossenschaft, 10-%-Grenze): beantwortet durch BMF vom 22.11.1991, Tz. 38 und 39.
  - Teil „Vorfälligkeit“ aus Frage 3: beantwortet durch BMF vom 27.07.2015.
  - Bestätigung zu `MA-010`.
  - Frage nach Außenanlagen (`MA-023`).
- **Geschärft:**
  - Frage 1 (`MA-030`): „Sehen Sie Risiken aus gewerblichem Grundstückshandel oder § 9 Nr. 1 Satz 5 Nr. 2 GewStG, und vereinbaren Sie den Übergang zum 31.12., 23:59 Uhr?“
  - Frage 2 (`MA-031`): „Behandeln Sie den NBank-Zuschuss bei der Privatperson als Vorauszahlung nach § 11 Abs. 2 Satz 3 EStG, sodass die Verteilung möglich ist? Bilden Sie in der Steuerbilanz einen passiven Rechnungsabgrenzungsposten? Wann fließt der Tilgungsnachlass zu?“
  - Frage 3, Rest: NBank-Bearbeitungsentgelt laufzeitbezogen?
  - Frage 4 (`MA-036`): „Ist der Verkauf des einzigen Objekts der geprägten KG mit anschließender Liquidation eine Aufgabe nach § 16 Abs. 3 EStG?“

### (c) Quellenkataster

Vorschläge für Einträge. Die Kennungen folgen Notiz 13; Spalte „Gelesen“ mit Belegqualität.

| Kennung | Titel | Fundstelle | Stand | Gelesen |
|---|---|---|---|---|
| `ESTR-21-5` | R 21.5 EStR und H 21.5 EStH: Behandlung von Zuschüssen | NWB 443548_21___5; steuerschroeder estr/21.5, esth/21.5; Haufe H 21.5 2024 | EStR 2012 i. d. F. 25.03.2013 (VZ 2012–2026); EStH 2024/Handbuch 2025 | Wortlaut in Verlagswiedergabe, gegengeprüft, 2026-11-18 |
| `ESTR-6-5` | R 6.5 EStR und H 6.5 EStH: Zuschüsse für Anlagegüter | NWB 443548_6___5; steuerschroeder estr/6.5, esth/6.5 | wie oben | Wortlaut in Verlagswiedergabe, gegengeprüft, 2026-11-18 |
| `ESTH-5-6` (neu) | H 5.6 EStH: Rechnungsabgrenzung (Ertrags-, Investitions-, Zinszuschüsse) | steuerschroeder esth/5.6; NWB 1077356_5___6 | Handbuch 2025; NWB VZ 2025–2026 | Wortlaut in Verlagswiedergabe, gegengeprüft, 2026-11-18 |
| `ESTR-21-1` (neu) | R 21.1 Abs. 3 EStR: Gartenanlagen und lebende Umzäunung | steuerschroeder estr/21.1; NWB 443548_21___1 | EStR 2012 (VZ 2012–2026) | Wortlaut in Verlagswiedergabe, gegengeprüft, 2026-11-18 |
| `ESTH-6-4-7-1` (neu) | H 6.4 und H 7.1 EStH: Außenanlagen, Gartenanlage, Umzäunung | steuerschroeder esth/6.4, esth/7.1 | Handbuch 2025 | Wortlaut in Verlagswiedergabe, 2026-11-18 |
| `GEWSTR-9-2` (neu) | R 9.2 GewStR und H 9.2 GewStH: Kürzung bei Grundstücksunternehmen | steuerschroeder gewstr/9.2; NWB 1068784_9___2___1___ bis _4___; Haufe H 9.2 2024 | GewStR 2009; GewStH VZ 2024–2026 | Wortlaut in Verlagswiedergabe, H 9.2 (1) gegengeprüft, H 9.2 (3) eine Wiedergabe, 2026-11-18 |
| `GEWSTR-7-1` | R 7.1 GewStR und H 7.1 GewStH: Gewerbeertrag | NWB 363299_7___1; NWB 1068784_7___1___3___ | GewStR i. d. F. 28.04.2010; GewStH VZ 2024–2026 | Wortlaut in Verlagswiedergabe, 2026-11-18 |
| `KSTR-5-9` | R 5.9 KStR (unbesetzt) und H 5.9 KStH: Vermietungsgenossenschaften | NWB 883112_5___9; NWB 1102750_5___9 | KStR 2022 (13.04.2022); KStH VZ 2026 | Wortlaut in Verlagswiedergabe, 2026-11-18 |
| `BMF-VERMGEN-1991` (neu) | BMF-Schreiben: Steuerbefreiung für Vermietungsgenossenschaften und -vereine | BStBl I 1991 S. 1014; GZ IV B 7 - S 2730 - 24/91; gelesen als OFD Frankfurt vom 23.09.2013, S 2730 A - 15 - St 53 (NWB 480060) | 22.11.1991; in Positivliste 2026 | Tz. 1 bis 51 im Wortlaut der OFD-Wiedergabe, 2026-11-18; BStBl-Fassung nicht erreicht |
| `BMF-SCHULDZINSEN-2015` | BMF-Schreiben: Schuldzinsen und Vorfälligkeitsentschädigung nach Veräußerung des Mietobjekts | BStBl I 2015 S. 581; GZ IV C 1 - S 2211/11/10001, DOK 2015/0644430; NWB 545773 | 27.07.2015; in Positivliste 2026 | Wortlaut in Verlagswiedergabe, ganz, 2026-11-18 |
| `BMF-BAUHERREN-2003` (neu, ersetzt `BMF-DAMNUM-2005`) | BMF-Schreiben: Gesamtobjekte, Modelle mit einem Kapitalanleger, Fonds (Rz. 15: Damnum) | BStBl I 2003 S. 546; GZ IV C 3 - S 2253 a - 48/03; NWB 88184 | 20.10.2003; in Positivliste 2026 | Rz. 15 und 22 im Wortlaut, gegengeprüft an OFD München/Nürnberg vom 10.12.2003, 2026-11-18 |
| `BMF-EURLUMSG-2005` (neu) | BMF-Schreiben: Anwendung von § 11 Abs. 1 Satz 3, Abs. 2 Satz 3 EStG, Damnum | BStBl I 2005 S. 617; GZ IV A 3 - S 2259 - 7/05; NWB 161868 | 05.04.2005; in Positivliste 2026 | Wortlaut in Verlagswiedergabe, ganz, 2026-11-18 |
| `BMF-POSITIVLISTE-2026` (neu) | BMF-Schreiben: Anwendung von BMF-Schreiben (Positivliste) | BStBl I 2026 S. 394; GZ IV A 2 - O 2000/00079/006/001; NWB 1090883 | 20.03.2026 (Stand 19.03.2026) | Einträge lfd. Nr. 776, 788, 943, 969, 1167 gelesen, 2026-11-18 |
| `BGBL-2024-I-108` (neu) | Wachstumschancengesetz, Art. 2 Nr. 4, Art. 6, Art. 35 Abs. 4 und 9 | recht.bund.de, BGBl. 2024 I Nr. 108 | 27.03.2024 | am Original, 2026-11-18 |
| `BFH-IX-R-60-02` | BFH, Urteil: Fördermittel im Dritten Förderungsweg als Einnahmen im Zuflussjahr | BStBl II 2004 S. 14; NWB 122750 | 14.10.2003 | Wortlaut in Verlagswiedergabe, ganz, 2026-11-18 |
| `BFH-I-R-89-03` (neu) | BFH, Urteil: erweiterte Kürzung bei Veräußerung zum 31.12., 23:59 Uhr | BStBl II 2004 S. 1080; NWB 145695 | 11.08.2004 | Wortlaut in Verlagswiedergabe, ganz, 2026-11-18 |
| `BFH-I-R-17-99` (neu) | BFH, Urteil: erweiterte Kürzung und § 6b-Rücklage | BStBl II 2001 S. 251; NWB 97487 | 15.03.2000 | Leitsatz, 2026-11-18 |
| `BFH-IV-R-3-05` | BFH, Urteil: Grundstück der gewerblich geprägten Personengesellschaft als Anlagevermögen; Anteilsveräußerung bei Grundstückshandel | BStBl II 2007 S. 777; NWB 252516 | 14.12.2006 | Wortlaut in Verlagswiedergabe, ganz, 2026-11-18 |
| `BGH-VIII-ZR-311-11` (neu) | BGH, Urteil: Anrechnung von Drittmitteln auf zwölf Jahre begrenzt | gesetze.co/urteile/VIII_ZR_311-11 | 13.06.2012 | Wortlaut in nichtamtlicher Sammlung, Rn. 15 bis 27, 2026-11-18 |
| `BGH-VIII-ZR-283-23` (neu) | BGH, Urteil: energetische Modernisierung, Endenergieeinsparung ex ante | ECLI:DE:BGH:2025:260325UVIIIZR283.23.0; Abschrift bei rws-verlag.de | 26.03.2025 | Leitsatz, Rn. 1, 2, 31, 32, 2026-11-18 |

Lesedaten zu bestehenden Einträgen:

- `ESTG-11`: Abs. 1 Satz 3 und Abs. 2 Satz 3 und 4 am 2026-11-18 erneut gelesen.
- `GEWSTG-9`: Nr. 1 Satz 5 Nr. 2 und Satz 6 am 2026-11-18 gelesen.
- `GEWSTG-7`: Satz 2 am 2026-11-18 gelesen.
- `ESTG-10D`: Abs. 2 erneut gelesen (70 %, geltende Fassung).

## Nicht erreicht

- **Amtliche Steuerhandbücher des BMF:** nicht aufgerufen (Captcha, vom Proxy abgewiesen). Alle Richtlinien und Hinweise sind deshalb nur in Verlagswiedergabe gelesen, nicht am Original.
- **BMF-Schreiben vom 22.11.1991 im BStBl:** Bei NWB kostenpflichtig, nicht geöffnet. Gelesen ist die wortgleiche Verfügung der OFD Frankfurt vom 23.09.2013. Ob sie in jeder Ziffer mit dem BStBl-Text übereinstimmt, ist nicht geprüft; Tz.-Zählung und Bezug sind identisch.
- **BMF-PDFs vom 27.07.2015, 20.10.2003, 05.04.2005:** Auf bundesfinanzministerium.de nicht gefunden; vermutete Adressen lieferten 404. Gelesen bei NWB.
- **steuerschroeder.de:** Einzelne Seiten (H 9.2 (1) bis (3), R 7.1 Abs. 3, KStR) lieferten wiederholt Fehler 500 oder Zeitüberschreitung. Für H 9.2 (3) und R 7.1 Abs. 3 fehlt daher die zweite Wiedergabe.
- **lexetius.com, dejure.org:** Im Netz der Sitzung nicht erreichbar (Verbindung zurückgesetzt oder Name nicht auflösbar). **anwalt24.de** zeigt eine Cloudflare-Prüfung, die nicht umgangen wurde.
- **juris.bundesgerichtshof.de:** per `curl` 403, per WebFetch nicht auflösbar. Die BGH-Urteile sind deshalb nur aus nichtamtlicher Sammlung und Verlagsabschrift gelesen. Soll das nachgeholt werden, muss der Host in den Netzeinstellungen der Sitzung freigegeben werden.
- **BFH vom 29.04.1987 (BStBl II S. 603)**, Grundlage von H 9.2 (3): nicht selbst gelesen.
- **BFH X R 22/13** (Notiz 13, Grundstückshändler) und die BFH-Urteile, die H 5.6 nennt: nicht gelesen, für die Fragen dieser Notiz nicht tragend.
- **Rechtsprechung zu `MA-019` und `MA-025`:** keine BGH-Entscheidung gefunden. Nur Websuche, keine Suche in der BGH-Datenbank.
- **Spätere Änderungen von Art. 6 Wachstumschancengesetz:** Nur der Regierungsentwurf zum JStG 2026 ist durchsucht, nicht alle Gesetze von 2025 und 2026.
