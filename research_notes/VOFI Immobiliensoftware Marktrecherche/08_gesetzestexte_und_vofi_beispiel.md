# Verifikation der Steuer- und Mietrechtsparameter am Gesetzestext (Stand 17.11.2026) und vollständiges VOFI-Testbeispiel (IWU)

**Methode.** Alle Werte wurden am 17.11.2026 direkt auf www.gesetze-im-internet.de gelesen (konsolidierte Gesamtfassungen und Einzelnormseiten, per Direktabruf). Die IWU-Beispiele stammen aus zwei von www.iwu.de heruntergeladenen PDF. Diese Notiz ersetzt nicht die Dateien 03 und 06, sondern prüft deren als "unverifiziert", "(FW)" oder "Gaps" markierte Parameter.

**Statusangaben in den Tabellen.**
- **bestätigt** = Wert im Gesetzeswortlaut gelesen, deckt sich mit der früheren Notiz.
- **korrigiert (alt → neu)** = frühere Notiz weicht vom gelesenen Wortlaut ab.
- **neu** = in den früheren Notizen nicht oder nur ohne Wortlaut enthalten.
- **nicht verifizierbar** = im abrufbaren Text nicht enthalten oder Quelle gesperrt.

**Nicht erreichbar in dieser Sitzung:** www.destatis.de, www.bafin.de, www.bundesbank.de, www.recht.bund.de, dserver.bundestag.de (Netzwerksperre); www.bundesfinanzministerium.de lieferte nur eine Bot-Schutzseite (HTTP 503). Indexstände (VPI), BaFin-Mindestkapitalisierungszinssätze, BGBl.-Originale und BMF-Schreiben konnten daher nicht gelesen werden.

**Standangaben der gelesenen Fassungen (Kopfzeile "Stand" bzw. Vollzitat der jeweiligen Gesamtausgabe):**

| Gesetz / VO | "Stand" laut gesetze-im-internet.de | Hinweis |
|---|---|---|
| KStG | zuletzt geändert durch Art. 30 G v. 4.2.2026 I Nr. 33 | |
| SolzG 1995 | zuletzt geändert durch Art. 4 G v. 23.12.2024 I Nr. 449 | |
| EStG | zuletzt geändert durch Art. 1 G v. 15.10.2026 I Nr. 307 (Gesetz zur Einführung eines antragslosen Kindergeldes) | kein § 6f enthalten |
| EStDV | zuletzt geändert durch Art. 2 V v. 19.12.2025 I Nr. 372 | |
| GewStG | zuletzt geändert durch Art. 8 G v. 29.6.2026 I Nr. 197 (Neuntes Gesetz zur Änderung von Vorschriften im Steuerberatungsrecht sowie im Steuerrecht) | |
| AO | zuletzt geändert durch Art. 6 G v. 22.10.2026 I Nr. 320 | |
| UStG | zuletzt geändert durch Art. 5 G v. 29.6.2026 I Nr. 197 | |
| GrEStG | zuletzt geändert durch Art. 9 G v. 29.6.2026 I Nr. 197 | Seitenhinweis: mittelbare Änderung durch Art. 10 desselben Gesetzes "textlich nachgewiesen, dokumentarisch noch nicht abschließend bearbeitet" |
| BGB | zuletzt geändert durch Art. 6 G v. 23.7.2026 I Nr. 226 | |
| EGBGB | zuletzt geändert durch Art. 16 G v. 22.10.2026 I Nr. 321 | |
| GEG, jetzt "Gebäudemodernisierungsgesetz (GModG)" | zuletzt geändert durch Art. 4 G v. 23.7.2026 I Nr. 226 | Titel der Seite: "GModG" |
| CO2KostAufG | geändert durch Art. 5 G v. 23.7.2026 I Nr. 226 | Seitenhinweis: Änderung "mWv 29.7.2026 textlich nachgewiesen, dokumentarisch noch nicht abschließend bearbeitet" |
| II. BV | zuletzt geändert durch Art. 78 Abs. 2 G v. 23.11.2007 I 2614 | seit 2007 unverändert |
| ImmoWertV 2021 | Vollzitat "vom 14. Juli 2021 (BGBl. I S. 2805)", keine Änderung ausgewiesen | |
| BelWertV | zuletzt geändert durch Art. 5 V v. 4.10.2022 I 1614 | |
| PfandBG | zuletzt geändert durch Art. 23 G v. 25.3.2026 I Nr. 81 | |
| MaBV | zuletzt geändert durch Art. 2 V v. 28.7.2026 I Nr. 229 | |
| WoFlV | Vollzitat "vom 25. November 2003 (BGBl. I S. 2346)", keine Änderung ausgewiesen | |

Quellen der Standangaben: jeweilige Gesamtausgabe, z. B. [KStG](https://www.gesetze-im-internet.de/kstg_1977/index.html), [EStG](https://www.gesetze-im-internet.de/estg/index.html), [BGB](https://www.gesetze-im-internet.de/bgb/index.html), [GModG](https://www.gesetze-im-internet.de/geg/index.html); Titel der Änderungsgesetze 2026 aus dem [Aktualitätendienst](https://www.gesetze-im-internet.de/aktuDienst.html).

---

## 1. Körperschaftsteuer: Tarif, SolZ, Zinsschranke, § 8c KStG, Mindestbesteuerung

### Takeaway
Der Stufentarif des § 23 KStG (15 % bis VZ 2027, dann 14/13/12/11 %, ab VZ 2032 10 %), der SolZ von 5,5 % und die Zinsschranke (Freigrenze unter 3 Mio. €, 30 % verrechenbares EBITDA, EBITDA-Vortrag 5 Jahre, Zinsvortrag unbefristet) stehen wörtlich im geltenden Text. Der Verlustvortrag ist im veröffentlichten § 10d Abs. 2 EStG mit 70 % begrenzt; die Rückkehr auf 60 % ab VZ 2028 ist dort nicht ablesbar.

### Cited Findings

**KStG / SolzG**

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| KSt-Satz bis VZ 2027 | 15 % | [§ 23 Abs. 1 Nr. 1 KStG](https://www.gesetze-im-internet.de/kstg_1977/__23.html) | "Veranlagungszeiträume bis 2027 15 Prozent" | bestätigt |
| KSt-Satz VZ 2028 | 14 % | § 23 Abs. 1 Nr. 2 | "den Veranlagungszeitraum 2028 14 Prozent" | bestätigt |
| KSt-Satz VZ 2029 | 13 % | § 23 Abs. 1 Nr. 3 | "den Veranlagungszeitraum 2029 13 Prozent" | bestätigt |
| KSt-Satz VZ 2030 | 12 % | § 23 Abs. 1 Nr. 4 | "den Veranlagungszeitraum 2030 12 Prozent" | bestätigt |
| KSt-Satz VZ 2031 | 11 % | § 23 Abs. 1 Nr. 5 | "den Veranlagungszeitraum 2031 11 Prozent" | bestätigt |
| KSt-Satz ab VZ 2032 | 10 % | § 23 Abs. 1 Nr. 6 | "Veranlagungszeiträume ab 2032 10 Prozent des zu versteuernden Einkommens" | bestätigt |
| SolZ-Satz | 5,5 % der Bemessungsgrundlage | [§ 4 Satz 1 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html) | "Der Solidaritätszuschlag beträgt 5,5 Prozent der Bemessungsgrundlage." | bestätigt (war FW) |
| SolZ-Bemessungsgrundlage bei Körperschaften | festgesetzte KSt | [§ 3 Abs. 1 Nr. 1 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) | "nach der ... festgesetzten Körperschaftsteuer" | bestätigt |
| SolZ-Freigrenze | gilt nur für einkommensteuerpflichtige Personen | § 3 Abs. 3 SolzG | "ist von einkommensteuerpflichtigen Personen nur zu erheben, wenn ..." | neu (für Körperschaften keine Freigrenze im Text) |
| Zinsschranke bei Körperschaften | maßgebliches Einkommen statt maßgeblicher Gewinn; alle Einkünfte = ein Betrieb | [§ 8a Abs. 1 KStG](https://www.gesetze-im-internet.de/kstg_1977/__8a.html) | "dass anstelle des maßgeblichen Gewinns das maßgebliche Einkommen tritt" | bestätigt |
| Eigenkapital-Escape bei Körperschaften | nur, wenn Gesellschafter-Fremdfinanzierung (Beteiligung mind. 1/4) höchstens 10 % des Nettozinsaufwands | § 8a Abs. 3 KStG | "insgesamt nicht mehr als 10 Prozent der die Zinserträge übersteigenden Zinsaufwendungen" | neu |
| Schädlicher Beteiligungserwerb | mehr als 50 % innerhalb von 5 Jahren an einen Erwerber: Verluste vollständig nicht abziehbar | [§ 8c Abs. 1 Satz 1 KStG](https://www.gesetze-im-internet.de/kstg_1977/__8c.html) | "Werden innerhalb von fünf Jahren ... mehr als 50 Prozent ... übertragen ... vollständig nicht mehr abziehbar" | bestätigt (war FW) |
| Konzernklausel | 100-%-Beteiligungsfälle unschädlich | § 8c Abs. 1 Satz 4 | "zu 100 Prozent mittelbar oder unmittelbar beteiligt" | bestätigt |
| Stille-Reserven-Klausel | Verlust bleibt abziehbar, soweit er die im Inland steuerpflichtigen stillen Reserven nicht übersteigt | § 8c Abs. 1 Satz 5–8 | "soweit er die gesamten ... stillen Reserven des Betriebsvermögens ... nicht übersteigt" | bestätigt |
| Sanierungsklausel | Beteiligungserwerb zur Sanierung unbeachtlich | § 8c Abs. 1a | "Beteiligungserwerb zum Zweck der Sanierung ... unbeachtlich" | neu |
| Zinsvortrag und § 8c | §§ 8c, 8d gelten für den Zinsvortrag entsprechend | § 8a Abs. 1 Satz 3 KStG | "Die §§ 8c und 8d gelten für den Zinsvortrag ... entsprechend" | neu |

**§ 4h und § 10d EStG** (§ 8a Abs. 1 KStG verweist für Körperschaften auf § 4h EStG und nennt § 10d EStG bei der Definition des maßgeblichen Einkommens; die allgemeine Verweisung des § 8 Abs. 1 KStG wurde nicht gesondert gelesen)

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Grundregel | Zinsaufwand abziehbar bis Zinsertrag, darüber bis zum verrechenbaren EBITDA | [§ 4h Abs. 1 Satz 1 EStG](https://www.gesetze-im-internet.de/estg/__4h.html) | "abziehbar in Höhe des Zinsertrags, darüber hinaus nur bis zur Höhe des verrechenbaren EBITDA" | bestätigt |
| Verrechenbares EBITDA | 30 % des um Zinsaufwand und Abschreibungen (§ 6 Abs. 2, 2a, § 7) erhöhten und um Zinserträge verminderten maßgeblichen Gewinns | § 4h Abs. 1 Satz 2 | "Das verrechenbare EBITDA ist 30 Prozent des ..." | bestätigt |
| EBITDA-Vortrag | 5 Wirtschaftsjahre; entsteht nicht, wenn Zinsaufwand ≤ Zinsertrag oder Abs. 2 greift | § 4h Abs. 1 Satz 3 | "in die folgenden fünf Wirtschaftsjahre vorzutragen (EBITDA-Vortrag)" | bestätigt (war FW) |
| Verbrauchsreihenfolge | EBITDA-Vorträge in zeitlicher Reihenfolge | § 4h Abs. 1 Satz 4 | "mindern die EBITDA-Vorträge in ihrer zeitlichen Reihenfolge" | neu |
| Zinsvortrag | zeitlich unbegrenzt; erhöht Zinsaufwand der Folgejahre, nicht den Gewinn | § 4h Abs. 1 Satz 5–6 | "in die folgenden Wirtschaftsjahre vorzutragen (Zinsvortrag)" | bestätigt (war FW) |
| Freigrenze | Nettozinsaufwand unter 3 Mio. € | § 4h Abs. 2 Satz 1 Buchst. a | "weniger als drei Millionen Euro betragen" | bestätigt (Freigrenze, kein Freibetrag) |
| Freigrenze und Zinsvortrag | Ausnahmen des Abs. 2 gelten nicht, soweit Zinsaufwand durch Zinsvortrag erhöht ist | § 4h Abs. 1 Satz 7 | "Absatz 2 findet keine Anwendung, soweit Zinsaufwendungen aufgrund eines Zinsvortrags erhöht wurden" | neu |
| Stand-alone-Ausnahme | keine nahestehende Person i. S. d. § 1 Abs. 2 AStG und keine ausländische Betriebsstätte | § 4h Abs. 2 Satz 1 Buchst. b | "keiner Person im Sinne des § 1 Absatz 2 ... des Außensteuergesetzes nahesteht" | bestätigt |
| Eigenkapital-Escape | EK-Quote des Betriebs ≥ Konzernquote; Toleranz 2 Prozentpunkte | § 4h Abs. 2 Satz 1 Buchst. c | "Unterschreiten ... um bis zu zwei Prozentpunkte ist unschädlich" | neu |
| Untergang der Vorträge | bei Aufgabe oder Übertragung des Betriebs | § 4h Abs. 5 | "gehen ein nicht verbrauchter EBITDA-Vortrag und ein nicht verbrauchter Zinsvortrag unter" | neu |
| Verlustrücktrag | bis 1 Mio. € (2 Mio. € bei Zusammenveranlagung), in den unmittelbar vorangegangenen und den zweiten vorangegangenen VZ | [§ 10d Abs. 1 Satz 1–2 EStG](https://www.gesetze-im-internet.de/estg/__10d.html) | "bis zu einem Betrag von 1 000 000 Euro ... des zweiten dem Veranlagungszeitraum vorangegangenen Veranlagungszeitraums" | bestätigt (war FW) |
| Verlustvortrag Sockel | 1 Mio. € unbeschränkt (2 Mio. € bei Zusammenveranlagung) | § 10d Abs. 2 Satz 1–2 | "bis zu einem Gesamtbetrag der Einkünfte von 1 Million Euro unbeschränkt" | bestätigt |
| Verlustvortrag oberhalb Sockel (ESt/KSt) | 70 % des übersteigenden Gesamtbetrags der Einkünfte | § 10d Abs. 2 Satz 1 | "darüber hinaus bis zu 70 Prozent des 1 Million Euro übersteigenden Gesamtbetrags" | bestätigt für die geltende Fassung |
| Anwendungsbeginn 70 % | erstmals VZ 2024 | [§ 52 Abs. 18b Satz 3 EStG](https://www.gesetze-im-internet.de/estg/__52.html) | "§ 10d Absatz 2 in der Fassung des Artikels 2 des Gesetzes vom 27. März 2024 ... erstmals für den Veranlagungszeitraum 2024" | bestätigt |
| Rückkehr auf 60 % ab VZ 2028 | – | – | im konsolidierten Text nicht enthalten | nicht verifizierbar |
| Gewerbeverlust (Vergleich) | 1 Mio. € Sockel, darüber 60 % | [§ 10a Satz 1–2 GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html) | "Der 1 Million Euro übersteigende maßgebende Gewerbeertrag ist bis zu 60 Prozent ... zu kürzen" | bestätigt |

### Inferences
- Kombinierte Belastung KSt + SolZ je VZ (Rechenwert aus den bestätigten Sätzen): 2027 15,825 %; 2028 14,77 %; 2029 13,715 %; 2030 12,66 %; 2031 11,605 %; ab 2032 10,55 %.
- Im Rechenkern müssen ESt/KSt (70 %) und GewSt (60 %) getrennte Mindestbesteuerungsquoten führen.
- Weil die Freigrenze nicht gilt, soweit ein Zinsvortrag den Zinsaufwand erhöht (§ 4h Abs. 1 Satz 7), genügt eine einfache "< 3 Mio. €"-Prüfung nicht; der vorgetragene Teil ist getrennt zu behandeln.

### Gaps
- Die Befristung der 70-%-Quote auf VZ 2024–2027 und die Rückkehr auf 60 % ab VZ 2028 (so die frühere Notiz 03 nach Sekundärquellen) steht nicht im konsolidierten Text; sie beruht auf einem erst künftig in Kraft tretenden Änderungsartikel. BGBl. 2024 I Nr. 108 war nicht abrufbar (recht.bund.de gesperrt).
- BMF-Anwendungsschreiben zur Zinsschranke (März 2025) nicht abrufbar.

---

## 2. Gewerbesteuer: Messzahl, Hinzurechnungen, erweiterte Grundstückskürzung, Mindesthebesatz

### Takeaway
Steuermesszahl 3,5 %, Hinzurechnung von einem Viertel der Finanzierungsentgelte über 200.000 € und die Unschädlichkeitsgrenzen der erweiterten Kürzung (Strom 20 %, sonstige Mieterleistungen 5 %) sind bestätigt. Der Mindesthebesatz ist geändert: der Text nennt 280 %, erstmals für den Erhebungszeitraum 2027.

### Cited Findings

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Steuermesszahl | 3,5 % | [§ 11 Abs. 2 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) | "Die Steuermesszahl für den Gewerbeertrag beträgt 3,5 Prozent." | bestätigt (war FW) |
| Rundung, Freibetrag | Gewerbeertrag auf volle 100 € abrunden; Freibetrag 24.500 € (natürliche Personen, Personengesellschaften), 5.000 € (u. a. bestimmte befreite Körperschaften, jPdöR); Kapitalgesellschaften nicht genannt | § 11 Abs. 1 Satz 3 | "um einen Freibetrag in Höhe von 24 500 Euro" | neu |
| Hinzurechnung Finanzierungsanteile | ein Viertel der Summe aus a) bis f), soweit die Summe 200.000 € übersteigt | [§ 8 Nr. 1 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html) | "Ein Viertel der Summe aus ... soweit die Summe den Betrag von 200 000 Euro übersteigt" | bestätigt |
| darin: Entgelte für Schulden | 100 % (effektiv 25 %) | § 8 Nr. 1 Buchst. a | "Entgelten für Schulden" | bestätigt |
| darin: Renten, dauernde Lasten, Gewinnanteile stiller Gesellschafter | 100 % (effektiv 25 %) | § 8 Nr. 1 Buchst. b, c | – | neu |
| darin: Mieten/Leasing bewegliche Wirtschaftsgüter | ein Fünftel (effektiv 5 %) | § 8 Nr. 1 Buchst. d | "einem Fünftel der Miet- und Pachtzinsen" | bestätigt |
| darin: Mieten/Pachten unbewegliche Wirtschaftsgüter | die Hälfte (effektiv 12,5 %) | § 8 Nr. 1 Buchst. e | "der Hälfte der Miet- und Pachtzinsen ... der unbeweglichen Wirtschaftsgüter" | bestätigt |
| darin: Rechteüberlassung | ein Viertel (effektiv 6,25 %) | § 8 Nr. 1 Buchst. f | "einem Viertel der Aufwendungen für die zeitlich befristete Überlassung von Rechten" | neu |
| Einfache Grundbesitzkürzung | als Betriebsausgabe erfasste Grundsteuer | [§ 9 Nr. 1 Satz 1 GewStG](https://www.gesetze-im-internet.de/gewstg/__9.html) | "die im Erhebungszeitraum als Betriebsausgabe erfasste Grundsteuer" | neu (ab EZ 2025, § 36 Abs. 4b) |
| Erweiterte Kürzung | auf Antrag Kürzung um den Teil des Gewerbeertrags aus Verwaltung und Nutzung eigenen Grundbesitzes | § 9 Nr. 1 Satz 2 | "Unternehmen, die ausschließlich eigenen Grundbesitz oder neben eigenem Grundbesitz eigenes Kapitalvermögen verwalten und nutzen" | bestätigt |
| Erlaubte Nebentätigkeiten | Betreuung von Wohnungsbauten; Errichtung und Veräußerung von EFH, ZFH, ETW | § 9 Nr. 1 Satz 2 | "oder daneben Wohnungsbauten betreuen oder Einfamilienhäuser ... errichten und veräußern" | bestätigt |
| Teileigentum | unschädlich, wenn Gebäude zu mehr als 66 2/3 % Wohnzwecken dient | § 9 Nr. 1 Satz 3 Buchst. a | "zu mehr als 66 2/3 Prozent Wohnzwecken dient" | neu |
| Unschädliche Stromeinnahmen | höchstens 20 % der Einnahmen aus Gebrauchsüberlassung des Grundbesitzes (EE-Anlagen, Ladestationen); EE-Strom nicht an Letztverbraucher außer Mieter | § 9 Nr. 1 Satz 3 Buchst. b | "nicht höher als 20 Prozent der Einnahmen aus der Gebrauchsüberlassung des Grundbesitzes" | bestätigt |
| Unschädliche sonstige Mieter-Einnahmen | höchstens 5 % der Einnahmen aus Gebrauchsüberlassung | § 9 Nr. 1 Satz 3 Buchst. c | "aus unmittelbaren Vertragsbeziehungen mit den Mietern ... nicht höher als 5 Prozent" | bestätigt |
| Ausschlüsse | Grundbesitz dient Gewerbebetrieb eines Gesellschafters; Sondervergütungen; Veräußerungsgewinne nach § 7 Satz 2 Nr. 2, 3 | § 9 Nr. 1 Satz 5–6 | "wenn der Grundbesitz ganz oder zum Teil dem Gewerbebetrieb eines Gesellschafters oder Genossen dient" | neu |
| Mindesthebesatz | 280 %, wenn die Gemeinde keinen höheren bestimmt | [§ 16 Abs. 4 Satz 2 GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html) | "Er beträgt 280 Prozent, wenn die Gemeinde nicht einen höheren Hebesatz bestimmt hat." | korrigiert (200 % → 280 %) |
| Anwendungsbeginn 280 % | erstmals Erhebungszeitraum 2027 | [§ 36 Abs. 5b GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html) | "§ 16 Absatz 4 Satz 2 in der Fassung des Artikels 7 des Gesetzes vom 29. Juni 2026 (BGBl. 2026 I Nr. 197) ist erstmals für den Erhebungszeitraum 2027 anzuwenden" | neu (frühere Notiz: "Status unbekannt") |

### Inferences
- Effektive GewSt = 3,5 % × Hebesatz; Untergrenze ab EZ 2027 damit 9,8 % (280 %), bis EZ 2026 nach der Vorfassung 7,0 % (200 %; die Vorfassung ist auf der Seite nicht mehr abgebildet).
- Die Unschädlichkeitsgrenzen 20 % und 5 % beziehen sich auf die Einnahmen aus der Gebrauchsüberlassung des Grundbesitzes im Wirtschaftsjahr, nicht auf die Gesamterträge. Der Rechenkern braucht diese Bezugsgröße als eigene Zeile.

### Gaps
- Der bis EZ 2026 geltende Mindesthebesatz von 200 % wurde nicht im Wortlaut gelesen (nur die Neufassung ist veröffentlicht).

---

## 3. Einkommensteuer für private Investoren und Personengesellschaften

### Takeaway
Alle abgefragten AfA- und Fristenparameter sind im geltenden Text bestätigt, einschließlich der Fenster "vor dem 1. Oktober 2029" für § 7 Abs. 5a und § 7b. Einen § 6f EStG gibt es in der veröffentlichten Fassung (Stand 15.10.2026) nicht.

### Cited Findings

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Lineare AfA Wirtschaftsgebäude | 3 % (Betriebsvermögen, nicht Wohnzwecke, Bauantrag nach 31.3.1985) | [§ 7 Abs. 4 Satz 1 Nr. 1 EStG](https://www.gesetze-im-internet.de/estg/__7.html) | "jährlich 3 Prozent" | bestätigt (war FW) |
| Lineare AfA, Fertigstellung nach 31.12.2022 | 3 % | § 7 Abs. 4 Satz 1 Nr. 2 Buchst. a | "nach dem 31. Dezember 2022 fertiggestellt worden sind, jährlich 3 Prozent" | bestätigt |
| Lineare AfA, Fertigstellung 1.1.1925 bis 31.12.2022 | 2 % | § 7 Abs. 4 Satz 1 Nr. 2 Buchst. b | "vor dem 1. Januar 2023 und nach dem 31. Dezember 1924 ... jährlich 2 Prozent" | bestätigt |
| Lineare AfA, Fertigstellung vor 1.1.1925 | 2,5 % | § 7 Abs. 4 Satz 1 Nr. 2 Buchst. c | "vor dem 1. Januar 1925 fertiggestellt worden sind, jährlich 2,5 Prozent" | bestätigt |
| Kürzere tatsächliche Nutzungsdauer | zulässig bei weniger als 33 Jahren (Nr. 1, Nr. 2a), 50 Jahren (Nr. 2b), 40 Jahren (Nr. 2c) | § 7 Abs. 4 Satz 2 | "so können anstelle der Absetzungen nach Satz 1 die der tatsächlichen Nutzungsdauer entsprechenden Absetzungen ... vorgenommen werden" | bestätigt (war FW) |
| Zeitanteilige AfA im Erstjahr | monatsgenau | § 7 Abs. 1 Satz 4 | "um jeweils ein Zwölftel für jeden vollen Monat, der dem Monat der Anschaffung oder Herstellung vorangeht" | neu |
| Degressive Gebäude-AfA | 5 % vom jeweiligen Restwert | § 7 Abs. 5a Satz 4 | "nach einem unveränderlichen Prozentsatz in Höhe von 5 Prozent vom jeweiligen Buchwert (Restwert)" | bestätigt |
| Voraussetzungen degressive AfA | Wohnzwecke; Belegenheit EU/EWR; selbst hergestellt oder bis Ende des Fertigstellungsjahres angeschafft; nur anstelle der AfA nach Abs. 4 Nr. 2 Buchst. a | § 7 Abs. 5a Satz 1 | "soweit sie Wohnzwecken dienen und vom Steuerpflichtigen hergestellt oder bis zum Ende des Jahres der Fertigstellung angeschafft worden sind" | bestätigt |
| Zeitfenster degressive AfA | Herstellungsbeginn oder Kaufvertrag nach 30.9.2023 und vor 1.10.2029 | § 7 Abs. 5a Satz 1 | "nach dem 30. September 2023 und vor dem 1. Oktober 2029" | bestätigt (Wortlaut: "vor dem 1. Oktober 2029") |
| Herstellungsbeginn | Datum der Baubeginnsanzeige | § 7 Abs. 5a Satz 2–3 | "Als Beginn der Herstellung gilt das Datum in der ... Baubeginnsanzeige" | neu |
| Erstjahr, AfaA, Wechsel | zeitanteilig; keine AfaA; Wechsel zur linearen AfA zulässig, dann Restwert und Restnutzungsdauer | § 7 Abs. 5a Satz 5–8 | "Der Übergang ... zur Absetzung für Abnutzung in gleichen Jahresbeträgen ist zulässig" | neu |
| Sonder-AfA Mietwohnungsneubau | bis 5 % p. a. im Jahr der Anschaffung/Herstellung und den 3 Folgejahren, neben AfA nach § 7 Abs. 4 oder 5a | [§ 7b Abs. 1 EStG](https://www.gesetze-im-internet.de/estg/__7b.html) | "bis zu jährlich 5 Prozent der Bemessungsgrundlage neben der Absetzung für Abnutzung nach § 7 Absatz 4 oder 5a" | bestätigt |
| § 7b Zeitfenster | Bauantrag/Bauanzeige nach 31.8.2018 und vor 1.1.2022 oder nach 31.12.2022 und vor 1.10.2029 | § 7b Abs. 2 Satz 1 Nr. 1 | "nach dem 31. Dezember 2022 und vor dem 1. Oktober 2029" | bestätigt |
| § 7b Effizienzanforderung (neues Fenster) | "Effizienzhaus 40" mit Nachhaltigkeits-Klasse, Nachweis durch QNG | § 7b Abs. 2 Satz 1 Nr. 2 | "Kriterien eines „Effizienzhaus 40“ mit Nachhaltigkeits-Klasse erfüllt und dies durch Qualitätssiegel Nachhaltiges Gebäude nachgewiesen wird" | bestätigt |
| § 7b Vermietungsbindung | Jahr der Anschaffung/Herstellung und 9 Folgejahre entgeltliche Überlassung zu Wohnzwecken | § 7b Abs. 2 Satz 1 Nr. 3 | "in den folgenden neun Jahren der entgeltlichen Überlassung zu Wohnzwecken dient" | bestätigt (war FW) |
| § 7b Baukostenobergrenze | 3.000 €/m² Wohnfläche (altes Fenster), 5.200 €/m² (neues Fenster) | § 7b Abs. 2 Satz 2 | "5 200 Euro je Quadratmeter Wohnfläche nicht übersteigen" | bestätigt |
| § 7b Bemessungsgrundlage | max. 2.000 €/m² (alt), max. 4.000 €/m² (neu) | § 7b Abs. 3 | "maximal 4 000 Euro je Quadratmeter Wohnfläche" | bestätigt |
| § 7b Rückgängigmachung | bei Nutzungsänderung oder steuerfreier Veräußerung in 10 Jahren; bei Überschreiten der Obergrenze durch nachträgliche Kosten innerhalb der ersten 3 Jahre nach Ablauf des Jahres der Anschaffung/Herstellung | § 7b Abs. 4 | "innerhalb der ersten drei Jahre nach Ablauf des Jahres der Anschaffung oder Herstellung" | bestätigt |
| § 7b Beihilferecht | De-minimis-VO (EU) 2023/2831; im neuen Fenster nur bei Einkünften nach §§ 13, 15, 18 | § 7b Abs. 5 | "soweit die Voraussetzungen der Verordnung (EU) 2023/2831 eingehalten sind" | bestätigt (frühere Notiz: unklar) |
| § 7b alte Fassung | letztmals VZ 2026 | § 52 Abs. 15a EStG | "letztmalig für den Veranlagungszeitraum 2026" | neu |
| Sanierungsgebiet | bis 9 % im Jahr der Herstellung und 7 Folgejahren, dann bis 7 % in 4 Jahren; nur soweit nicht durch Zuschüsse gedeckt; nicht bei Neubau | [§ 7h Abs. 1, 1a EStG](https://www.gesetze-im-internet.de/estg/__7h.html) | "in den folgenden sieben Jahren jeweils bis zu 9 Prozent und in den folgenden vier Jahren jeweils bis zu 7 Prozent" | bestätigt (war FW) |
| Baudenkmal | wie § 7h: 8 × bis 9 %, 4 × bis 7 %; nur soweit nicht durch Zuschüsse aus öffentlichen Kassen gedeckt | [§ 7i Abs. 1 EStG](https://www.gesetze-im-internet.de/estg/__7i.html) | "jeweils bis zu 9 Prozent und in den folgenden vier Jahren jeweils bis zu 7 Prozent" | bestätigt (war FW) |
| Anschaffungsnahe Herstellungskosten | Instandsetzung/Modernisierung innerhalb von 3 Jahren nach Anschaffung über 15 % der Gebäude-Anschaffungskosten (netto); ohne Erweiterungen und jährlich übliche Erhaltungsarbeiten | [§ 6 Abs. 1 Nr. 1a EStG](https://www.gesetze-im-internet.de/estg/__6.html) | "innerhalb von drei Jahren nach der Anschaffung ... ohne die Umsatzsteuer 15 Prozent der Anschaffungskosten des Gebäudes übersteigen" | bestätigt |
| Verteilung größeren Erhaltungsaufwands | gleichmäßig auf 2 bis 5 Jahre; Gebäude nicht im Betriebsvermögen, überwiegend Wohnzwecke | [§ 82b Abs. 1 EStDV](https://www.gesetze-im-internet.de/estdv_1955/__82b.html) | "auf zwei bis fünf Jahre gleichmäßig verteilen" | bestätigt |
| Restbetrag bei Veräußerung | im Veräußerungsjahr Werbungskosten | § 82b Abs. 2 EStDV | "im Jahr der Veräußerung als Werbungskosten abzusetzen" | neu |
| Spekulationsfrist Grundstücke | nicht mehr als 10 Jahre zwischen Anschaffung und Veräußerung | [§ 23 Abs. 1 Satz 1 Nr. 1 EStG](https://www.gesetze-im-internet.de/estg/__23.html) | "nicht mehr als zehn Jahre beträgt" | bestätigt (war FW) |
| Gewinnermittlung § 23 | Anschaffungs-/Herstellungskosten mindern sich um abgezogene AfA, erhöhte Absetzungen, Sonderabschreibungen | § 23 Abs. 3 Satz 4 | "mindern sich um Absetzungen für Abnutzung, erhöhte Absetzungen und Sonderabschreibungen" | bestätigt (war FW) |
| Freigrenze § 23 | Gesamtgewinn im Kalenderjahr unter 1.000 € | § 23 Abs. 3 Satz 5 | "weniger als 1 000 Euro betragen hat" | bestätigt (war FW ohne Betrag) |
| Verbilligte Vermietung, Aufteilung | Entgelt unter 50 % der ortsüblichen Marktmiete: Aufteilung in entgeltlichen und unentgeltlichen Teil | [§ 21 Abs. 2 Satz 1 EStG](https://www.gesetze-im-internet.de/estg/__21.html) | "weniger als 50 Prozent der ortsüblichen Marktmiete" | bestätigt |
| Verbilligte Vermietung, Vollentgeltlichkeit | ab 66 % der ortsüblichen Miete bei auf Dauer angelegter Vermietung | § 21 Abs. 2 Satz 2 | "mindestens 66 Prozent der ortsüblichen Miete, gilt die Wohnungsvermietung als entgeltlich" | bestätigt |
| § 6f EStG (Kaufpreisaufteilung) | nicht vorhanden | [Einzelnorm-URL liefert HTTP 404](https://www.gesetze-im-internet.de/estg/__6f.html); auf § 6e folgt § 7 | Volltextsuche im EStG und in der EStDV nach "Kaufpreisaufteilung": kein Treffer | nicht in Kraft laut veröffentlichtem Text |

### Inferences
- Zwischen 50 % und unter 66 % der ortsüblichen Miete enthält der Gesetzestext keine ausdrückliche Rechtsfolge; die frühere Notiz nennt dafür die Totalüberschussprognose (Verwaltungsauffassung, hier nicht verifiziert).
- § 7b ist im neuen Fenster für Überschusseinkünfte (private Vermieter) nicht beihilferechtlich begrenzt, für Gewinneinkünfte gilt die De-minimis-Grenze.
- § 7h/7i und § 7b verwenden unterschiedliche Kürzungslogiken für Zuschüsse; im Rechenkern muss die Förderung je AfA-Art getrennt von der Bemessungsgrundlage abgezogen werden.

### Gaps
- Status des JStG 2026 (§ 6f EStG-E): gesetze-im-internet.de zeigt den Stand 15.10.2026. Ob das Gesetz danach beschlossen oder verkündet wurde, ist hier nicht feststellbar (Bundestag, BGBl. und BMF nicht abrufbar).
- Drei-Objekt-Grenze und Totalüberschussprognose sind Rechtsprechung bzw. Verwaltungsauffassung, nicht Gesetzestext; nicht geprüft.

---

## 4. Steuerbefreite: Vermietungsgenossenschaften und Wohngemeinnützigkeit

### Takeaway
Die 10-%-Grenze für nicht begünstigte Einnahmen (30 % bei Mieterstrom) und die Einkommensgrenzen der Wohngemeinnützigkeit (Fünf- bzw. Sechsfaches des Regelsatzes, maßgeblich bei Mietbeginn) stehen im Text.

### Cited Findings

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Begünstigte Tätigkeit | Wohnungen herstellen oder erwerben und Mitgliedern per Miet- oder Nutzungsvertrag überlassen; dazu Gemeinschaftsanlagen und Folgeeinrichtungen | [§ 5 Abs. 1 Nr. 10 Satz 1 KStG](https://www.gesetze-im-internet.de/kstg_1977/__5.html) | "Genossenschaften sowie Vereine, soweit sie ... Wohnungen herstellen oder erwerben und sie den Mitgliedern ... überlassen" | bestätigt |
| Unschädlichkeitsgrenze | Einnahmen aus anderen Tätigkeiten höchstens 10 % der gesamten Einnahmen, sonst Befreiung ausgeschlossen | § 5 Abs. 1 Nr. 10 Satz 2 | "10 Prozent der gesamten Einnahmen übersteigen" | bestätigt |
| Erhöhte Grenze Strom | 30 % für Mieterstrom und Gemeinschaftliche Gebäudeversorgung, wenn die 10 % nur durch diese Einnahmen überschritten werden | § 5 Abs. 1 Nr. 10 Satz 3–4 | "erhöht sich die Grenze des Satzes 2 für diese Einnahmen auf 30 Prozent" | neu |
| Investierende Mitglieder | zählen nicht als Mitglieder | § 5 Abs. 1 Nr. 10 Satz 5 | "sind keine Mitglieder im Sinne des Satzes 1" | neu |
| Unterbringung Wohnungsloser | Verträge mit jPdöR oder gemeinnützigen Mitgliedern begünstigt | § 5 Abs. 1 Nr. 10 Satz 6–7 | "Verträge zur vorübergehenden Unterbringung von Wohnungslosen" | neu |
| Wohngemeinnützigkeit | vergünstigte Wohnraumüberlassung an Personen i. S. d. § 53 AO | [§ 52 Abs. 2 Satz 1 Nr. 27 AO](https://www.gesetze-im-internet.de/ao_1977/__52.html) | "die Förderung wohngemeinnütziger Zwecke; dies ist die vergünstigte Wohnraumüberlassung an Personen im Sinne des § 53" | bestätigt |
| Einkommensgrenze | Bezüge höchstens das Fünffache des Regelsatzes (§ 28 SGB XII); Alleinstehende und Alleinerziehende das Sechsfache | § 52 Abs. 2 Satz 1 Nr. 27 AO | "nicht höher sein dürfen als das Fünffache des Regelsatzes ... tritt an die Stelle des Fünffachen das Sechsfache" | bestätigt (frühere Notiz: Grenzen nicht verifiziert) |
| Zeitpunkt der Prüfung | Beginn des Mietverhältnisses | § 52 Abs. 2 Satz 1 Nr. 27 AO | "Die Hilfebedürftigkeit muss zu Beginn des jeweiligen Mietverhältnisses vorliegen." | bestätigt |
| Allgemeine Grenze (Vergleich) | Vierfaches bzw. Fünffaches des Regelsatzes; Bezüge aller Haushaltsangehörigen | [§ 53 Nr. 2 AO](https://www.gesetze-im-internet.de/ao_1977/__53.html) | "das Vierfache des Regelsatzes der Sozialhilfe" | neu |

### Inferences
- "Vergünstigt" ist im Gesetz nicht beziffert; ein Mindestabstand zur Marktmiete ergibt sich nicht aus § 52 AO.

### Gaps
- AEAO zu § 52 Abs. 2 Nr. 27 AO (Auslegung "vergünstigt", Mittelverwendung, Rücklagen) nicht abrufbar.
- Kommunale Wohnungsgesellschaften: keine eigene Befreiungsnorm gelesen; die Aussage der früheren Notiz bleibt ungeprüft.

---

## 5. Umsatzsteuer

### Takeaway
Steuerfreiheit der Vermietung, Option nur bei vorsteuerunschädlicher Verwendung durch den Mieter und der zehnjährige Berichtigungszeitraum für Grundstücke sind bestätigt.

### Cited Findings

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Steuerbefreiung | Vermietung und Verpachtung von Grundstücken | [§ 4 Nr. 12 Satz 1 Buchst. a UStG](https://www.gesetze-im-internet.de/ustg_1980/__4.html) | "die Vermietung und die Verpachtung von Grundstücken" | bestätigt |
| Ausnahmen (steuerpflichtig) | kurzfristige Beherbergung, Fahrzeugstellplätze, kurzfristige Campingplatzvermietung, Betriebsvorrichtungen | § 4 Nr. 12 Satz 2 | "Nicht befreit sind ... die Vermietung von Plätzen für das Abstellen von Fahrzeugen" | bestätigt |
| Option | möglich bei Umsatz an anderen Unternehmer für dessen Unternehmen | [§ 9 Abs. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__9.html) | "als steuerpflichtig behandeln, wenn der Umsatz an einen anderen Unternehmer für dessen Unternehmen ausgeführt wird" | bestätigt |
| Optionsbeschränkung Vermietung | nur soweit der Mieter das Grundstück ausschließlich für vorsteuerunschädliche Umsätze verwendet; Nachweispflicht des Vermieters | § 9 Abs. 2 | "ausschließlich für Umsätze verwendet oder zu verwenden beabsichtigt, die den Vorsteuerabzug nicht ausschließen" | bestätigt |
| Option bei Grundstückslieferung | nur im notariell zu beurkundenden Vertrag | § 9 Abs. 3 Satz 2 | "nur in dem ... notariell zu beurkundenden Vertrag erklärt werden" | neu |
| Berichtigungszeitraum | 10 Jahre bei Grundstücken einschließlich wesentlicher Bestandteile und Gebäuden auf fremdem Boden (sonst 5) | [§ 15a Abs. 1 Satz 2 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15a.html) | "tritt an die Stelle des Zeitraums von fünf Jahren ein Zeitraum von zehn Jahren" | bestätigt |
| Berichtigungsbetrag | je Kalenderjahr ein Zehntel der Vorsteuer | § 15a Abs. 5 Satz 1 | "in den Fällen des Satzes 2 von einem Zehntel" | bestätigt |
| Veräußerung im Zeitraum | Änderung der Verhältnisse; Berichtigung, als wäre bis Fristende entsprechend verwendet worden | § 15a Abs. 8–9 | "so vorzunehmen, als wäre das Wirtschaftsgut ... weiterhin für das Unternehmen verwendet worden" | neu |
| Geschäftsveräußerung | Zeitraum läuft beim Erwerber weiter | § 15a Abs. 10 | "wird der ... maßgebliche Berichtigungszeitraum nicht unterbrochen" | neu |
| Regelsteuersatz | 19 % | [§ 12 Abs. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__12.html) | "19 Prozent der Bemessungsgrundlage" | bestätigt |

### Inferences
- Die Ausschließlichkeit in § 9 Abs. 2 steht ohne Bagatellgrenze im Gesetz; eine Toleranz (in der Praxis 5 %) wäre Verwaltungsauffassung und ist hier nicht belegt.

### Gaps
- UStAE (Abschnitte 9.2, 15a) nicht abrufbar; Bagatellgrenzen des § 44 UStDV nicht geprüft.

---

## 6. Mietrecht (BGB)

### Takeaway
Kappungsgrenze 20 %/15 %, Mietpreisbremse (Verordnungen bis längstens 31.12.2029), 8-%-Umlage mit 3 €/2 €-Kappung und der Drittmittelabzug nach § 559a sind bestätigt. Für die Indexmiete steht keine Obergrenze im Text. § 559e ist auf das GModG umgestellt, und es gibt einen § 559f: ohne Nachweis einer Jahresarbeitszahl von mindestens 2,5 darf bei Wärmepumpen nur die Hälfte der Kosten umgelegt werden.

### Cited Findings

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Wartefrist Vergleichsmietenerhöhung | Miete 15 Monate unverändert; Verlangen frühestens 1 Jahr nach letzter Erhöhung; §§ 559–560 zählen nicht | [§ 558 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__558.html) | "seit 15 Monaten unverändert" | bestätigt |
| Vergleichsmiete | übliche Entgelte der letzten 6 Jahre | § 558 Abs. 2 | "in den letzten sechs Jahren vereinbart oder ... geändert" | bestätigt |
| Kappungsgrenze | 20 % in 3 Jahren; 15 % in per Landesverordnung bestimmten Gebieten (VO jeweils höchstens 5 Jahre) | § 558 Abs. 3 | "nicht um mehr als 20 vom Hundert erhöhen (Kappungsgrenze) ... beträgt 15 vom Hundert" | bestätigt |
| Drittmittel bei § 558 | vom Jahresbetrag abzuziehen; Zuschüsse mit 8 % | § 558 Abs. 5 | "sind Drittmittel im Sinne des § 559a abzuziehen, im Falle des § 559a Absatz 1 mit 8 Prozent des Zuschusses" | neu |
| Mietpreisbremse | Miete bei Mietbeginn höchstens 10 % über ortsüblicher Vergleichsmiete | [§ 556d Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__556d.html) | "höchstens um 10 Prozent übersteigen" | bestätigt |
| Geltungsende | Landesverordnungen müssen spätestens mit Ablauf des 31.12.2029 außer Kraft treten | § 556d Abs. 2 Satz 4 | "muss spätestens mit Ablauf des 31. Dezember 2029 außer Kraft treten" | bestätigt |
| Ausnahme Neubau | Wohnung nach 1.10.2014 erstmals genutzt und vermietet; erste Vermietung nach umfassender Modernisierung | [§ 556f BGB](https://www.gesetze-im-internet.de/bgb/__556f.html) | "die nach dem 1. Oktober 2014 erstmals genutzt und vermietet wird" | bestätigt (Stichtag unverändert) |
| Vormiete, Modernisierungszuschlag | Vormiete darf vereinbart werden; Modernisierung der letzten 3 Jahre erhöht die zulässige Miete um den § 559-Betrag | [§ 556e BGB](https://www.gesetze-im-internet.de/bgb/__556e.html) | "bis zur Höhe der Vormiete" | neu |
| Staffelmiete | jede Staffel mind. 1 Jahr; in Geldbetrag auszuweisen; §§ 558–559b ausgeschlossen; Mietpreisbremse gilt je Staffel; Kündigungsausschluss höchstens 4 Jahre | [§ 557a BGB](https://www.gesetze-im-internet.de/bgb/__557a.html) | "Die §§ 556d bis 556g sind auf jede Mietstaffel anzuwenden." | bestätigt; keine betragsmäßige Obergrenze im Text |
| Indexmiete | Bindung an den Verbraucherpreisindex; mind. 1 Jahr unverändert; § 558 ausgeschlossen; § 559/§ 559e nur bei nicht zu vertretenden Maßnahmen oder Maßnahme nach § 555b Nr. 1a | [§ 557b Abs. 1–2 BGB](https://www.gesetze-im-internet.de/bgb/__557b.html) | "Eine Erhöhung nach § 558 ist ausgeschlossen." | bestätigt |
| Indexmiete, Kappung | keine Obergrenze der Indexanpassung im Text; Mietpreisbremse nur für die Ausgangsmiete | § 557b Abs. 4 | "Die §§ 556d bis 556g sind nur auf die Ausgangsmiete einer Indexmietvereinbarung anzuwenden." | bestätigt (Stand 23.7.2026: kein Deckel) |
| Modernisierungsumlage | 8 % der für die Wohnung aufgewendeten Kosten p. a. (Maßnahmen nach § 555b Nr. 1, 3, 4, 5, 6) | [§ 559 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__559.html) | "die jährliche Miete um 8 Prozent der für die Wohnung aufgewendeten Kosten erhöhen" | bestätigt |
| Abzug Erhaltungsaufwand | nicht umlagefähig; ggf. Schätzung; Abnutzungsgrad zu berücksichtigen | § 559 Abs. 2 | "Kosten, die für Erhaltungsmaßnahmen erforderlich gewesen wären, gehören nicht zu den aufgewendeten Kosten" | bestätigt (war FW) |
| Kappung | 3 €/m² Wohnfläche monatlich in 6 Jahren; 2 €/m², wenn Miete vorher unter 7 €/m² | § 559 Abs. 3a Satz 1–2 | "nicht um mehr als 3 Euro je Quadratmeter Wohnfläche ... weniger als 7 Euro ... nicht um mehr als 2 Euro" | bestätigt (war FW) |
| Kappung Heizungstausch | 0,50 €/m² in 6 Jahren, wenn die Heizungsmaßnahme zugleich § 555b Nr. 1 oder 1a erfüllt; 3 €/2 € bleiben Gesamtgrenze | § 559 Abs. 3a Satz 3 | "um nicht mehr als 0,50 Euro je Quadratmeter Wohnfläche innerhalb von sechs Jahren" | bestätigt |
| Härteeinwand | Abwägung; entfällt bei allgemein üblichem Zustand oder nicht zu vertretenden Maßnahmen (Rückausnahme Heizungseinbau) | § 559 Abs. 4 | "eine Härte bedeuten würde" | neu |
| Drittmittel: Zuschüsse | vom Mieter, von Dritten für ihn oder aus öffentlichen Haushalten gedeckte Kosten gehören nicht zu den aufgewendeten Kosten | [§ 559a Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__559a.html) | "oder die mit Zuschüssen aus öffentlichen Haushalten gedeckt werden, gehören nicht zu den aufgewendeten Kosten im Sinne des § 559" | bestätigt (war FW) |
| Drittmittel: zinsverbilligte Darlehen | Erhöhungsbetrag sinkt um den Jahresbetrag der Zinsermäßigung = (marktüblicher Zins − ermäßigter Zins) × Ursprungsbetrag des Darlehens | § 559a Abs. 2 Satz 1–2 | "verringert sich der Erhöhungsbetrag nach § 559 um den Jahresbetrag der Zinsermäßigung ... für den Ursprungsbetrag des Darlehens" | bestätigt (war FW ohne Formel) |
| Maßgeblicher Marktzins | erstrangige Hypotheken bei Beendigung der Maßnahme | § 559a Abs. 2 Satz 3 | "der marktübliche Zinssatz für erstrangige Hypotheken zum Zeitpunkt der Beendigung der Modernisierungsmaßnahmen" | neu |
| Laufende Zuschüsse/Darlehen | Erhöhungsbetrag sinkt um den Jahresbetrag | § 559a Abs. 2 Satz 4 | "zur Deckung von laufenden Aufwendungen ... um den Jahresbetrag des Zuschusses oder Darlehens" | neu |
| Gleichstellung | Mieterdarlehen, Mietvorauszahlung; Mittel der Förderinstitute von Bund und Ländern gelten als öffentliche Mittel | § 559a Abs. 3 | "Mittel der Finanzierungsinstitute des Bundes oder eines Landes gelten als Mittel aus öffentlichen Haushalten." | neu |
| Aufteilung | nach Verhältnis der je Wohnung aufgewendeten Kosten, wenn nicht zuordenbar | § 559a Abs. 4 | "nach dem Verhältnis der für die einzelnen Wohnungen aufgewendeten Kosten aufzuteilen" | neu |
| Vereinfachtes Verfahren | bis 10.000 € je Wohnung; 30 % Pauschalabzug für Erhaltung; § 559a Abs. 2 Satz 1–3 (Zinsvorteil) nicht anzuwenden; 5 Jahre Sperre für § 559/§ 559e | [§ 559c BGB](https://www.gesetze-im-internet.de/bgb/__559c.html) | "werden pauschal 30 Prozent der nach Satz 1 geltend gemachten Kosten abgezogen" | bestätigt (war FW) |
| Heizungsumlage | 10 % der Kosten abzüglich in Anspruch genommener Drittmittel, wenn Maßnahme nach § 555b Nr. 1a dem Grunde nach förderfähig ist und Drittmittel genutzt wurden; ohne Förderung trotz Förderfähigkeit: § 559 | [§ 559e Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__559e.html) | "um 10 Prozent der für die Wohnung aufgewendeten Kosten abzüglich der in Anspruch genommenen Drittmittel" | bestätigt, Wortlaut jetzt gelesen |
| § 559e Erhaltungspauschale | 15 % pauschal; gilt nicht für Kosten einer Heizungsanlage nach § 43 GModG (Gas, Heizöl, Flüssiggas) | § 559e Abs. 2 | "Dies gilt nicht, soweit Kosten durch den Einbau einer Heizungsanlage im Sinne des § 43 des Gebäudemodernisierungsgesetzes entstanden sind." | korrigiert (Sekundärquelle: "15 % bei neuen Gas-/Ölheizungen" → Pauschale gilt dort gerade nicht) |
| § 559e Kappung | 0,50 €/m² monatlich in 6 Jahren; zusammen mit § 559 höchstens 3 €/2 € | § 559e Abs. 3 | "um nicht mehr als 0,50 Euro je Quadratmeter Wohnfläche innerhalb von sechs Jahren" | bestätigt |
| § 559f Wärmepumpe | Umlage nach § 559 oder § 559e in voller Höhe nur mit Nachweis einer Jahresarbeitszahl von mindestens 2,5 | [§ 559f Abs. 1 Satz 1 BGB](https://www.gesetze-im-internet.de/bgb/__559f.html) | "nur verlangen, wenn er den Nachweis erbracht hat, dass die Jahresarbeitszahl der Wärmepumpe bei mindestens 2,5 liegt" | neu (frühere Notiz: Wortlaut unbestätigt) |
| § 559f Ausnahmen vom Nachweis | Gebäude nach 1996 errichtet; Standard WSchV 1994; nach Sanierung mind. § 38 GModG; Vorlauftemperatur höchstens 55 °C | § 559f Abs. 1 Satz 2 | "mit einer Vorlauftemperatur beheizt werden kann, die nicht mehr als 55 Grad Celsius ... beträgt" | neu |
| § 559f Rechtsfolge ohne Nachweis | nur die Hälfte der aufgewendeten Kosten ansetzbar | § 559f Abs. 2 | "nur die Hälfte der für die Wohnung aufgewendeten Kosten zugrunde legen" | neu |
| § 559f Nachweisart | Fachunternehmer; VDI 4650 Blatt 1 oder vergleichbar; in der Regel vor Inbetriebnahme | § 559f Abs. 1 Satz 3–4 | "muss von einem Fachunternehmer erbracht werden" | neu |
| Modernisierungstatbestand Heizung | Einbau einer Heizungsanlage i. S. d. § 42 GModG | [§ 555b Nr. 1a BGB](https://www.gesetze-im-internet.de/bgb/__555b.html) | "eine Heizungsanlage im Sinne des § 42 des Gebäudemodernisierungsgesetzes" | neu |

### Inferences
- Rechenregel Umlage mit Förderung: umlagefähige Kosten = Kosten der Wohnung − Erhaltungsanteil − Zuschüsse (§ 559a Abs. 1); Jahreserhöhung = 8 % davon − Jahresbetrag der Zinsverbilligung (§ 559a Abs. 2); danach Kappung nach § 559 Abs. 3a. Zuschüsse mindern also die Basis, Zinsvorteile den Erhöhungsbetrag.
- Der Zinsvorteil wird auf den Ursprungsbetrag des Darlehens gerechnet, nicht auf die Restschuld; der Abzug ist damit über die Zeit konstant, solange die Verbilligung läuft (das Gesetz nennt kein Ende; die Dauer der Zinsbindung ist als Annahme zu führen).
- § 559e Abs. 1 verweist auf § 555b Nr. 1a und damit auf alle Optionen des § 42 Abs. 2 GModG, einschließlich Gas- und Ölheizungen. Für diese entfällt nach Abs. 2 Satz 2 nur die 15-%-Pauschale, sodass dort der tatsächliche Erhaltungsanteil nach § 559 Abs. 2 abzuziehen ist (Lesart des Wortlauts, keine Kommentarmeinung geprüft).
- Im vereinfachten Verfahren entfällt nur der Zinsvorteilsabzug; Zuschüsse (§ 559a Abs. 1) und laufende Zuschüsse (Abs. 2 Satz 4) bleiben abzugspflichtig.

### Gaps
- "Mietrecht II" (Indexmietdeckel, Möblierung, Kurzzeitmiete): im BGB mit Stand 23.7.2026 nicht enthalten. Ob danach ein Gesetz beschlossen oder verkündet wurde, ist hier nicht feststellbar.
- Im EGBGB (Art. 229) fand sich bei der Volltextsuche keine Übergangsvorschrift, die § 559e oder § 559f nennt; der zeitliche Anwendungsbereich des § 559f (Maßnahmenbeginn oder Ankündigung) ist damit offen.
- Welche Landesverordnungen zu § 556d und § 558 Abs. 3 gelten, ist Landesrecht und nicht geprüft.

---

## 7. II. Berechnungsverordnung §§ 26, 28, 29

### Takeaway
Im Verordnungstext stehen nur die Basisbeträge mit Preisstand 2002 (z. B. 230 € Verwaltung je Wohnung; 7,10/9,00/11,50 €/m² Instandhaltung) und die Indexregel (alle drei Jahre zum 1. Januar, VPI Oktober zu Oktober). Die aktuell anzusetzenden Beträge sind indexierte Werte, die nicht im Gesetzestext stehen.

### Cited Findings

| Parameter | Wert im Verordnungstext | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Verwaltungskosten Wohnung | höchstens 230 € jährlich je Wohnung (bei Eigenheimen je Wohngebäude) | [§ 26 Abs. 2 II. BV](https://www.gesetze-im-internet.de/bvo_2/__26.html) | "höchstens mit 230 Euro jährlich je Wohnung" | bestätigt (Basisbetrag) |
| Verwaltungskosten Garage/Stellplatz | höchstens 30 € jährlich | § 26 Abs. 3 | "höchstens mit 30 Euro jährlich je Garagen- oder Einstellplatz" | bestätigt (Basisbetrag) |
| Indexregel | Anpassung am 1.1.2005 und am 1.1. jedes dritten Folgejahres um die Veränderung des VPI Deutschland, Oktober vor der Anpassung gegenüber Oktober vor der letzten Anpassung; erste Anpassung Oktober 2004 gegenüber Oktober 2001 | § 26 Abs. 4 | "verändern sich am 1. Januar 2005 und am 1. Januar eines jeden darauf folgenden dritten Jahres um den Prozentsatz ..." | bestätigt |
| Instandhaltung, Bezugsfertigkeit unter 22 Jahre | höchstens 7,10 €/m² Wohnfläche p. a. | [§ 28 Abs. 2 Nr. 1 II. BV](https://www.gesetze-im-internet.de/bvo_2/__28.html) | "weniger als 22 Jahre zurückliegt, höchstens 7,10 Euro" | bestätigt (Basisbetrag) |
| Instandhaltung, mind. 22 Jahre | höchstens 9 €/m² | § 28 Abs. 2 Nr. 2 | "mindestens 22 Jahre zurückliegt, höchstens 9 Euro" | bestätigt (Basisbetrag) |
| Instandhaltung, mind. 32 Jahre | höchstens 11,50 €/m² | § 28 Abs. 2 Nr. 3 | "mindestens 32 Jahre zurückliegt, höchstens 11,50 Euro" | bestätigt (Basisbetrag) |
| Abschlag gewerbliche Wärmelieferung | −0,20 €/m² | § 28 Abs. 2 Satz 2 | "um 0,20 Euro" | neu |
| Zuschlag Aufzug | +1 €/m² | § 28 Abs. 2 Satz 3 | "um 1 Euro" | neu |
| Abschlag Kleinreparaturen durch Mieter | −1,05 €/m² | § 28 Abs. 3 | "verringern sich die Sätze nach Absatz 2 um 1,05 Euro" | neu |
| Schönheitsreparaturen durch Vermieter | höchstens 8,50 €/m² zusätzlich | § 28 Abs. 4 | "höchstens mit 8,50 Euro je Quadratmeter Wohnfläche im Jahr" | neu |
| Instandhaltung Garage/Stellplatz | höchstens 68 € jährlich inkl. Schönheitsreparaturen | § 28 Abs. 5 | "höchstens 68 Euro jährlich" | neu |
| Indexierung § 28 | Beträge der Abs. 2 bis 5 wie § 26 Abs. 4 | § 28 Abs. 5a | "verändern sich entsprechend § 26 Abs. 4" | bestätigt |
| Mietausfallwagnis | höchstens 2 % der Erträge i. S. d. § 31 Abs. 1 Satz 1; nicht indexiert | [§ 29 Satz 3 II. BV](https://www.gesetze-im-internet.de/bvo_2/__29.html) | "höchstens mit 2 vom Hundert der Erträge" | bestätigt |
| Abschreibung (Kostenmiete) | soll 1 % der Baukosten nicht übersteigen; Sonderabschreibungen für Anlagen (z. B. Sammelheizung 3 %, Aufzug 2 %) | [§ 25 II. BV](https://www.gesetze-im-internet.de/bvo_2/__25.html) | "soll bei Gebäuden 1 vom Hundert der Baukosten ... nicht übersteigen" | neu |
| Indexierte Werte ab 1.1.2026 (11,50 / 14,58 / 18,62 €/m²; Verwaltung 372,46 €) | nicht im Verordnungstext | frühere Notiz 06 (Haufe) | – | nicht verifizierbar (VPI bei destatis.de nicht abrufbar) |

### Inferences
- Anpassungstermine nach der Dreijahresregel: 1.1.2005, 2008, 2011, 2014, 2017, 2020, 2023, 2026; nächste Anpassung 1.1.2029 mit VPI Oktober 2028 gegenüber Oktober 2025.
- Plausibilitätsprüfung der Sekundärwerte: 372,46 / 230 = 1,6194. Derselbe Faktor ergibt 7,10 → 11,50; 9,00 → 14,57 (Sekundärquelle 14,58, Differenz durch kettenweise Rundung); 11,50 → 18,62. Die veröffentlichten Werte sind also in sich konsistent mit den Basisbeträgen, der Faktor selbst ist nicht geprüft.
- Für das Tool: Basisbeträge und Indexregel als Gesetzesparameter, die jeweils gültigen Beträge als datierte Stammdaten mit Quellenvermerk führen.

### Gaps
- VPI-Zeitreihe (Oktoberwerte) und amtliche oder verbandliche Veröffentlichung der Beträge ab 1.1.2026 nicht abrufbar.

---

## 8. CO2KostAufG, ImmoWertV Anlage 3, BelWertV, PfandBG, MaBV, WoFlV

### Takeaway
Die Stufentabelle des CO2KostAufG, die Modellansätze der ImmoWertV (gesetzliche Werte für 2021 plus Basiswerte und jährliche Indexregel), die 15-%-Mindestbewirtschaftungskosten und die seit 2022 dynamischen Mindestkapitalisierungszinssätze der BelWertV, die 60-%-Grenze des PfandBG, die MaBV-Raten und die WoFlV-Anrechnung sind am Text bestätigt. Neu im CO2KostAufG sind §§ 5a bis 5d: bei Gas-, Öl- und Flüssiggasheizungen nach § 43 GModG trägt der Vermieter ab 2028 die Hälfte von Gasnetzentgelten und CO2-Kosten und ab 2029 die Hälfte der Kosten des Pflicht-Biobrennstoffanteils.

### Cited Findings

**CO2KostAufG – Anlage (zu den §§ 5 bis 7)**, [Quelle](https://www.gesetze-im-internet.de/co2kostaufg/anlage.html), Status: bestätigt (frühere Notiz: Tabelle nicht verifiziert)

| kg CO2 je m² Wohnfläche und Jahr | Anteil Mieter | Anteil Vermieter |
|---|---|---|
| < 12 | 100 % | 0 % |
| 12 bis < 17 | 90 % | 10 % |
| 17 bis < 22 | 80 % | 20 % |
| 22 bis < 27 | 70 % | 30 % |
| 27 bis < 32 | 60 % | 40 % |
| 32 bis < 37 | 50 % | 50 % |
| 37 bis < 42 | 40 % | 60 % |
| 42 bis < 47 | 30 % | 70 % |
| 47 bis < 52 | 20 % | 80 % |
| ≥ 52 | 5 % | 95 % |

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Einstufung | spezifischer Ausstoß auf eine Nachkommastelle gerundet; bei unterjähriger Abrechnung Tabellenwerte anteilig kürzen | [§ 5 Abs. 1 CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/__5.html) | "auf die erste Nachkommastelle zu runden" | neu |
| Nichtwohngebäude | Mieter höchstens 50 % | [§ 8 Abs. 1](https://www.gesetze-im-internet.de/co2kostaufg/__8.html) | "mehr als 50 Prozent der Kohlendioxidkosten ... unwirksam" | bestätigt |
| Stufenmodell Nichtwohngebäude | im Text nur als Ankündigung für 2025 | § 8 Abs. 4 | "wird im Jahr 2025 von einem Stufenmodell für Nichtwohngebäude abgelöst werden" | neu (weiter hälftige Teilung im Text) |
| Hälftige Kostenteilung bei § 43-Heizung (Bestand) | Vermieter und Mieter je zur Hälfte: Gasnetzentgelte ab 1.1.2028; CO2-Kosten ab 1.1.2028 (abweichend von der Stufentabelle); Kosten des Pflicht-Biobrennstoffs ab 1.1.2029 für höchstens 30 % Anteil am Gesamtbrennstoff | [§ 5a Abs. 3 CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/__5a.html) | "Vermieter und Mieter tragen jeweils hälftig ..." | neu (frühere Notiz: Wortlaut nicht verifiziert) |
| Neubau | § 5a entsprechend für bis 31.12.2029 neu errichtete und erstmals genutzte Gebäude; nicht bei Bauantrag vor 13.5.2026 | § 5b | "bis zum Ablauf des 31. Dezember 2029 neu errichtet und erstmals genutzt" | neu |
| Härtefall Vermieter | nur Stufentabelle statt Hälfte, wenn kumulativ: kein angespannter Markt, Miete unter 85 % der Vergleichsmiete, höchstens 6 vermietete Wohnungen, Effizienzklasse G oder H, persönliche Härte; in angespannten Märkten nur in den Fällen des Abs. 2 Nr. 3 und 4 (Wärmepumpe technisch unmöglich und kein Fernwärmenetz; WEG-Beschlusslage) und bei Miete unter 70 % | § 5d Abs. 1 | "die vereinbarte Miete weniger als 85 Prozent der ortsüblichen Vergleichsmiete ... beträgt" | neu |
| Evaluierung | 2036 | § 5c | "werden im Jahr 2036 ... evaluiert" | neu |

**ImmoWertV 2021 – Anlage 3 (zu § 12 Abs. 5 Satz 2), Modellansätze für Bewirtschaftungskosten**, [Quelle](https://www.gesetze-im-internet.de/immowertv_2022/anlage_3.html)

| Parameter | Wert für 2021 (Verordnungstext) | Basiswert (Verordnungstext, Nr. III) | Status |
|---|---|---|---|
| Verwaltung je Wohnung bzw. je Wohngebäude bei EFH/ZFH | 298 € p. a. | 230 € | bestätigt |
| Verwaltung je Eigentumswohnung | 357 € p. a. | 275 € | bestätigt |
| Verwaltung je Garage/Stellplatz | 39 € p. a. | 30 € | bestätigt |
| Instandhaltung je m² Wohnfläche (Schönheitsreparaturen beim Mieter) | 11,70 € p. a. | 9,00 € | bestätigt |
| Instandhaltung je Garage/Stellplatz | 88 € p. a. | 68 € | bestätigt |
| Mietausfallwagnis Wohnen | 2 % des marktüblich erzielbaren Rohertrags | – | bestätigt |
| Verwaltung Gewerbe | 3 % des Rohertrags | – | bestätigt |
| Instandhaltung Gewerbe | 100 % (Büro, Praxen, Geschäfte), 50 % (SB-Märkte u. ä.), 30 % (Lager, Logistik, Produktion) des Wohn-Ansatzes, jeweils wenn Vermieter "Dach und Fach" trägt | – | bestätigt |
| Mietausfallwagnis Gewerbe | 4 % des Rohertrags | – | bestätigt |
| Indexregel (Nr. III) | jährlich; Basiswerte × VPI Oktober des Jahres vor dem Stichtag / VPI Oktober 2001; Instandhaltung je m² auf eine Nachkommastelle, übrige Werte kaufmännisch auf volle Euro | – | bestätigt |
| Werte für 2026/2027 | nicht im Verordnungstext | – | nicht verifizierbar (VPI nicht abrufbar) |

Wortlaut Indexregel: "Die Anpassung der Werte nach den Nummern I.1 und I.2 erfolgt jährlich auf der Grundlage der in Satz 3 genannten Basiswerte mit dem Prozentsatz, um den sich der ... Verbraucherpreisindex für Deutschland für den Monat Oktober 2001 gegenüber demjenigen für den Monat Oktober des Jahres, das dem Stichtag der Ermittlung des Liegenschaftszinssatzes vorausgeht, erhöht oder verringert hat."

**BelWertV / PfandBG**

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Mindest-Bewirtschaftungskosten | 15 % des Rohertrags (Summe Verwaltung, Instandhaltung, Mietausfallwagnis); tatsächliche Kosten dürfen nicht unterschritten werden | [§ 11 Abs. 2 Satz 3–4 BelWertV](https://www.gesetze-im-internet.de/belwertv/__11.html) | "Die Mindesthöhe für den Abzug der in den Absätzen 3 bis 5 genannten Kosten insgesamt beträgt 15 Prozent des Rohertrags." | bestätigt (war FW) |
| Einzelansätze Verwaltung | Wohnen: Beträge der Anlage 3 ImmoWertV; Gewerbe: 1 % des Jahresrohertrags | [Anlage 1 BelWertV](https://www.gesetze-im-internet.de/belwertv/anlage_1.html) | "die in Anlage 3 ... der Immobilienwertermittlungsverordnung in der jeweils geltenden Fassung genannten Beträge" | neu |
| Einzelansätze Instandhaltung | 0,8 % (Lager, Produktion, einfache Gewerbeobjekte, SB-Märkte), 0,5 % (Wohngebäude, Gewerbe mittlerer Standard), 0,4 % (hochwertige Büro-/Handelsobjekte) der Herstellungskosten je m² ohne Baunebenkosten und Außenanlagen | Anlage 1 | "Wohngebäude und gewerbliche Gebäude mit mittlerem Standard: 0,5 Prozent" | neu |
| Einzelansätze Mietausfallwagnis | Wohnen 2 %, Gewerbe 4 % | Anlage 1 | "Wohnungsbau: 2 Prozent ... Gewerbliche Objekte: 4 Prozent" | neu |
| Modernisierungsrisiko | 0,2 % / 0,5 % / 0,75 % der Herstellungskosten (gering/mittel/hoch) | § 11 Abs. 7, Anlage 1 | "Hohes Modernisierungsrisiko ... 0,75 Prozent" | bestätigt (war FW ohne Sätze) |
| Kapitalisierungszins, Regel | Wohnen mind. 3 Prozentpunkte, Gewerbe mind. 4 Prozentpunkte über der Rendite 30-jähriger Bundesanleihen (auf eine Nachkommastelle gerundet), zuzüglich Aufschläge nach Anlage 3 | [§ 12 Abs. 4 Satz 1 BelWertV](https://www.gesetze-im-internet.de/belwertv/__12.html) | "bei wohnwirtschaftlicher Nutzung mindestens 3 Prozentpunkte, bei gewerblicher Nutzung mindestens 4 Prozentpunkte über der ... Rendite 30-jähriger Bundesanleihen" | neu |
| Kapitalisierungszins, Korridor | Wohnen mind. 3,5 % und höchstens 5,5 %; Gewerbe mind. 4,5 % und höchstens 6,5 % | § 12 Abs. 4 Satz 3 | "mindestens 3,5 Prozent und höchstens 5,5 Prozent ... mindestens 4,5 Prozent und höchstens 6,5 Prozent" | neu |
| Anpassungsmechanik | Prüfung am 30.11.; Änderung zum 1.1. des Folgejahres bei Abweichung von mind. 0,5 Prozentpunkten; BaFin veröffentlicht | § 12 Abs. 4 Satz 2, 4 | "mindestens 0,5 Prozentpunkte höher oder niedriger" | neu |
| Erstklassige Objekte | Unterschreitung um höchstens 0,5 Prozentpunkte (Wohnen, Handel, Büro, Lager/Logistik) | § 12 Abs. 5 | "um höchstens 0,5 Prozentpunkte unterschritten werden" | neu |
| Aufschläge nach Nutzungsart | +0,5 Prozentpunkte (u. a. Hotels, Kliniken, Pflegeheime, Einkaufszentren, Lager/Logistik, Parkhäuser); +1,0 Prozentpunkte (Produktionsimmobilien) | [Anlage 3 BelWertV](https://www.gesetze-im-internet.de/belwertv/anlage_3.html) | "Produktionsimmobilien: 1,0 Prozentpunkte" | bestätigt (frühere Notiz ohne Sätze) |
| Maximale Nutzungsdauer | Wohnhäuser 80 Jahre; Geschäfts-/Bürohäuser 60; u. a. Hotels, Pflegeheime, Logistik 40; Fachmärkte, Freizeit 30 | Anlage 2 BelWertV | "Wohnhäuser: 80 Jahre" | neu |
| Vervielfältiger | V = (q^n − 1) / (q^n · z) | § 12 Abs. 1 | "V = (qn – 1) / (qn · z)" | neu |
| Verfahrenswahl | Ertragswert maßgeblich und Obergrenze; Sonderprüfung, wenn Sachwert mehr als 20 % darunter | [§ 4 Abs. 1 BelWertV](https://www.gesetze-im-internet.de/belwertv/__4.html) | "Maßgeblich ... ist regelmäßig der Ertragswert, der nicht überschritten werden darf" | neu |
| Aktuell gültiger Mindestzins 2026/2027 | nicht im Verordnungstext (BaFin-Bekanntgabe) | – | – | nicht verifizierbar (bafin.de gesperrt) |
| Beleihungsgrenze Pfandbriefdeckung | erste 60 % des Beleihungswerts | [§ 14 PfandBG](https://www.gesetze-im-internet.de/pfandbg/__14.html) | "nur bis zur Höhe der ersten 60 Prozent des ... Beleihungswert[s] zur Deckung benutzt werden" | bestätigt (war FW) |

**MaBV § 3 Abs. 2** ([Quelle](https://www.gesetze-im-internet.de/gewo_34cdv/__3.html); Kurzname der Seite "gewo_34cdv"), Status: bestätigt, Einzelsätze jetzt vollständig

Der Text kennt 13 Vomhundertsätze, aus denen "bis zu sieben Teilbeträge" zusammengesetzt werden können ("Die Teilbeträge können aus den nachfolgenden Vomhundertsätzen zusammengesetzt werden"). Feste sieben Raten gibt es nicht.

| Nr. | Bauabschnitt | Satz | Bezugsgröße | umgerechnet auf Vertragssumme (Eigentum) |
|---|---|---|---|---|
| 1 | nach Beginn der Erdarbeiten | 30 % (Erbbaurecht: 20 %) | Vertragssumme | 30,0 % |
| 2a | Rohbaufertigstellung einschließlich Zimmererarbeiten | 40 % | restliche Vertragssumme | 28,0 % |
| 2b | Dachflächen und Dachrinnen | 8 % | Rest | 5,6 % |
| 2c | Rohinstallation Heizung | 3 % | Rest | 2,1 % |
| 2d | Rohinstallation Sanitär | 3 % | Rest | 2,1 % |
| 2e | Rohinstallation Elektro | 3 % | Rest | 2,1 % |
| 2f | Fenstereinbau einschließlich Verglasung | 10 % | Rest | 7,0 % |
| 2g | Innenputz, ausgenommen Beiputzarbeiten | 6 % | Rest | 4,2 % |
| 2h | Estrich | 3 % | Rest | 2,1 % |
| 2i | Fliesenarbeiten im Sanitärbereich | 4 % | Rest | 2,8 % |
| 2j | Bezugsfertigkeit, Zug um Zug gegen Besitzübergabe | 12 % | Rest | 8,4 % |
| 2k | Fassadenarbeiten | 3 % | Rest | 2,1 % |
| 2l | vollständige Fertigstellung | 5 % | Rest | 3,5 % |

Die Sätze 2a bis 2l summieren sich auf 100 % der restlichen Vertragssumme. Die letzte Spalte ist eine eigene Umrechnung (Rest = 70 %), kein Verordnungstext. Weitere Regeln im Text: entfallende Leistungen werden anteilig auf die übrigen Raten verteilt (Abs. 2 Satz 3); bei Altbauten kann der Teilbetrag für schon erbrachte Leistungen sofort entgegengenommen werden (Satz 4); Voraussetzungen nach Abs. 1 sind u. a. Rechtswirksamkeit des Vertrags, Vormerkung, gesicherte Lastenfreistellung und Baugenehmigung; Freistellung von §§ 3 ff. bei Sicherheitsleistung nach § 7.

**WoFlV**

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Lichte Höhe mind. 2 m | vollständig | [§ 4 Nr. 1 WoFlV](https://www.gesetze-im-internet.de/woflv/__4.html) | "mit einer lichten Höhe von mindestens zwei Metern sind vollständig" | bestätigt |
| Lichte Höhe 1 m bis unter 2 m | zur Hälfte | § 4 Nr. 2 | "mindestens einem Meter und weniger als zwei Metern sind zur Hälfte" | bestätigt |
| Unbeheizbare Wintergärten, Schwimmbäder u. ä. | zur Hälfte | § 4 Nr. 3 | "sind zur Hälfte" | bestätigt |
| Balkone, Loggien, Dachgärten, Terrassen | in der Regel ein Viertel, höchstens die Hälfte | § 4 Nr. 4 | "in der Regel zu einem Viertel, höchstens jedoch zur Hälfte" | bestätigt |
| Nicht zur Wohnfläche | Zubehörräume (Keller, Abstellräume außerhalb der Wohnung, Waschküchen, Boden-, Trocken-, Heizungsräume, Garagen), bauordnungswidrige Räume, Geschäftsräume | [§ 2 Abs. 3 WoFlV](https://www.gesetze-im-internet.de/woflv/__2.html) | "Zur Wohnfläche gehören nicht die Grundflächen folgender Räume" | bestätigt |
| Messregel | lichte Maße zwischen den Bauteilen ab Vorderkante der Bekleidung; Schornsteine, Pfeiler u. ä. bleiben außer Betracht, wenn höher als 1,50 m und Grundfläche über 0,1 m² | [§ 3 WoFlV](https://www.gesetze-im-internet.de/woflv/__3.html) | "nach den lichten Maßen zwischen den Bauteilen" | neu |

### Inferences
- §§ 5a/5b CO2KostAufG verändern die Betriebskostenrechnung für Bestände mit ab dem 30.7.2026 eingebauten fossilen Heizungen: ab 2028 fällt beim Vermieter ein nicht umlagefähiger Kostenblock an (halbe Gasnetzentgelte, halbe CO2-Kosten unabhängig von der Effizienzstufe, ab 2029 halbe Bio-Brennstoffkosten). Das gehört als eigene Auszahlungszeile in den Finanzplan.
- BelWertV: Für den Wohnungsbau ist der Mindestkapitalisierungszins = min(max(Rendite 30-jähriger Bundesanleihen gerundet + 3,0; 3,5); 5,5) Prozent, mit Anpassung nur in Schritten ab 0,5 Prozentpunkten zum Jahreswechsel. Ohne die BaFin-Bekanntgabe ist der aktuell geltende Wert nicht sicher bestimmbar; als datierten Stammdatenwert führen.
- BelWertV-Verwaltungskosten Wohnen und ImmoWertV-Ansätze hängen am selben VPI-Index wie die II. BV; ein zentraler Indexbaustein (VPI Oktober, Basis Oktober 2001) deckt alle drei Regelwerke ab, mit unterschiedlichem Rhythmus (ImmoWertV jährlich, II. BV dreijährlich) und unterschiedlicher Rundung.

### Gaps
- Aktuelle BaFin-Mindestkapitalisierungszinssätze und Bundesbank-Rendite nicht abrufbar.
- ImmoWertV-Werte für 2026/2027 nicht berechenbar ohne VPI.
- Im CO2KostAufG wurden §§ 6, 7 und 9 (Begrenzung der Umlagefähigkeit, Abrechnung, Beschränkungen bei energetischen Verbesserungen) nicht im Detail ausgewertet.

---

## 9. Grunderwerbsteuer (Bundessatz)

### Takeaway
Der bundesgesetzliche Satz beträgt 3,5 %; abweichende Ländersätze beruhen auf Landesrecht und wurden auftragsgemäß nicht geprüft.

### Cited Findings

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Steuersatz | 3,5 % | [§ 11 Abs. 1 GrEStG](https://www.gesetze-im-internet.de/grestg_1983/__11.html) | "Die Steuer beträgt 3,5 vom Hundert." | bestätigt |
| Rundung | auf volle Euro abrunden | § 11 Abs. 2 | "auf volle Euro nach unten abzurunden" | neu |

### Inferences
- Im Tool: Bundessatz als Rückfallwert, Ländersätze als datierte Stammdaten.

### Gaps
- Ländersätze (BB, HE, MV, NI, RP, ST laut früherer Notiz unverifiziert) bleiben offen. Die durch Art. 9 und 10 G v. 29.6.2026 bewirkten Änderungen des GrEStG wurden inhaltlich nicht ausgewertet.

---

## 10. Gebäudeenergiegesetz / Gebäudemodernisierungsgesetz: Heizungsanforderungen

### Takeaway
Die 65-%-Regel steht nicht mehr im veröffentlichten Text. Die Seite /geg/ zeigt das "Gebäudemodernisierungsgesetz (GModG)" mit Stand "Zuletzt geändert durch Art. 4 G v. 23.7.2026 I Nr. 226"; §§ 71 bis 73 sind "(weggefallen)". An die Stelle tritt in §§ 42 bis 46 ein Optionenkatalog mit einer Bio-Brennstoff-Treppe für neu eingebaute Gas-, Öl- und Flüssiggasheizungen (10 % ab 2029, 15 % ab 2030, 30 % ab 2035, 60 % ab 2040).

### Cited Findings

| Parameter | Wert | Fundstelle | Wortlaut (Auszug) | Status |
|---|---|---|---|---|
| Gesetzestitel | "Gesetz zur Einsparung von Energie und zur Modernisierung der Wärmeversorgung in Gebäuden (Gebäudemodernisierungsgesetz - GModG)" vom 8.8.2020 | [Gesamtausgabe](https://www.gesetze-im-internet.de/geg/index.html) | Vollzitat: "Gebäudemodernisierungsgesetz vom 8. August 2020 (BGBl. I S. 1728), das zuletzt durch Artikel 4 des Gesetzes vom 23. Juli 2026 (BGBl. 2026 I Nr. 226) geändert worden ist" | bestätigt |
| Änderungsgesetz | "Gesetz zur Änderung des Gebäudeenergiegesetzes, zur Änderung des Gebäude-Elektromobilitätsinfrastruktur-Gesetzes und zur Änderung weiterer Vorschriften im Wärmebereich vom 23. Juli 2026", BGBl. 2026 I Nr. 226 | [Aktualitätendienst](https://www.gesetze-im-internet.de/aktuDienst.html) | – | bestätigt |
| 65-%-Regel | im Text nicht mehr vorhanden: Volltextsuche "65 Prozent" ohne Treffer; §§ 71, 72, 73 "(weggefallen)"; keine §§ 71a ff. | Gesamtausgabe | "§ 71 (weggefallen)" | bestätigt |
| Grundsatz Heizungstausch | Eigentümer wählt aus zehn Optionen (u. a. Gas-/Öl-/Flüssiggasheizung, Wärmepumpe, Solarthermie, Biomasse/Wasserstoff, Hybridheizungen, KWK, Stromdirektheizung, Wärmenetzanschluss, "andere innovative Heizungslösung"); Maßgaben der §§ 43–46 sind zu beachten | [§ 42 GModG](https://www.gesetze-im-internet.de/geg/__42.html) | "Wird eine Heizungsanlage in einem bestehenden Gebäude oder Gebäudenetz ersetzt ..." | neu (Wortlaut) |
| Bio-Brennstoff-Treppe | für nach dem 29.7.2026 in Bestandsgebäude neu eingebaute Gas-, Heizöl-, Flüssiggasheizungen: ab 1.1.2029 mind. 10 %, ab 1.1.2030 mind. 15 %, ab 1.1.2035 mind. 30 %, ab 1.1.2040 mind. 60 % der Wärme aus Biomethan, Bioöl, biogenem Flüssiggas oder Wasserstoff (grün, blau, orange, türkis) | [§ 43 Abs. 1 GModG](https://www.gesetze-im-internet.de/geg/__43.html) | "ab dem 1. Januar 2029 mindestens 10 Prozent, ab dem 1. Januar 2030 mindestens 15 Prozent, ab dem 1. Januar 2035 mindestens 30 Prozent und ab dem 1. Januar 2040 mindestens 60 Prozent" | bestätigt (Stufen jetzt am Text) |
| Ersatzerfüllung Solarthermie | 2029–2034 erfüllt bei mind. 0,04 m² Aperturfläche je m² Nutzfläche (bis 2 Wohnungen) bzw. 0,03 m² (mehr als 2 Wohnungen) | § 43 Abs. 3 | "mindestens 0,03 Quadratmetern Aperturfläche je Quadratmeter Nutzfläche" | neu |
| Ersatzerfüllung Lüftung mit WRG | 2029–2034 erfüllt bei Wärmerückgewinnungsgrad mind. 73 %, Leistungszahl mind. 10, Versorgung der gesamten Gebäudefläche | § 43 Abs. 4 | "mindestens 73 Prozent" | neu |
| Wärmepumpen-Hybrid | Pflicht gilt als erfüllt bei Wärmepumpenleistung mind. 30 % (bivalent parallel/teilparallel) bzw. 40 % (bivalent alternativ) der Spitzenlast | § 43 Abs. 5 | "mindestens 30 Prozent oder bei bivalent alternativem Betrieb mindestens 40 Prozent" | neu |
| Havarie | bei irreparablem Ausfall 12 Monate Aufschub | § 43 Abs. 7 | "erst nach Ablauf von zwölf Monaten ab dem Einbau" | neu |
| Verpflichteter | Eigentümer, sonst Betreiber | § 43 Abs. 1, 6 | "durch den Betreiber der Heizungsanlage zu erfüllen" | neu |
| Grüngas-/Grünheizölquote | eigenes Gesetz, von der Bundesregierung bis 1.12.2026 vorzulegen; Inverkehrbringer sollen ab 2045 vollständig klimaneutrale Brennstoffe liefern | [§ 42a GModG](https://www.gesetze-im-internet.de/geg/__42a.html) | "In einem bis zum 1. Dezember 2026 durch die Bundesregierung vorzulegenden Gesetz wird eine Grüngas-/Grünheizölquote eingeführt." | neu |
| Neubau | Niedrigstenergiegebäude; "Maßgaben der §§ 42 bis 45 entsprechend" einzuhalten | [§ 10 Abs. 2 Nr. 3 GModG](https://www.gesetze-im-internet.de/geg/__10.html) | "die Maßgaben der §§ 42 bis 45 entsprechend eingehalten werden" | neu |
| Stromdirektheizung | Neubau nur bei 45 % besserem Wärmeschutz (§ 10 Abs. 4); Bestand nur bei 30 % besserem Wärmeschutz (§ 46); Ausnahme selbstgenutzte Gebäude bis 2 Wohnungen | [§ 46 GModG](https://www.gesetze-im-internet.de/geg/__46.html) | "um mindestens 30 Prozent unterschreitet" | neu |

### Inferences
- Für die Investitionsrechnung ersetzt ein Brennstoffkostenpfad (steigender Pflichtanteil teurerer Bio-Brennstoffe 2029/2030/2035/2040) die frühere Investitionspflicht. Zusammen mit § 5a CO2KostAufG (hälftige Vermieterbeteiligung) und § 559e Abs. 2 Satz 2 BGB (keine 15-%-Pauschale bei § 43-Anlagen) entsteht ein zusammenhängendes Regelpaket, das im Tool als ein datierter Regelsatz "GModG 2026" abgebildet werden sollte.
- § 42a kündigt ein weiteres Gesetz bis 1.12.2026 an; die Brennstoffpreisannahmen ab 2029 stehen damit unter Gesetzgebungsvorbehalt.

### Gaps
- Übergangsvorschriften für vor dem 30.7.2026 eingebaute oder beauftragte Anlagen (§§ 110 ff. GModG) nicht ausgewertet.
- Angaben der früheren Notiz zu EPBD-Umsetzung und Inkrafttreten weiterer Teile nicht geprüft.

---

## 11. VOFI-Testbeispiele aus IWU-Veröffentlichungen

### Takeaway
Zwei vollständig nachrechenbare Beispiele liegen vor. Das Lehrbeispiel von Kirchner (2004) umfasst 3 Perioden ohne Darlehen und Steuern (Endvermögen 1.322,48 € bzw. 1.249,76 €; VOFI-Rentabilität 9,76 % bzw. 7,71 %). Das wohnungswirtschaftliche Beispiel aus dem IWU-Endbericht 2013 (vermietetes Mehrfamilienhaus, 25 Jahre, Annuitätendarlehen, KfW-Zuschuss, keine Steuern) endet mit einem Endwert von 153.032 € und einer VOFI-Rendite von 3,11 %; die abgelesene Tabelle wurde nachgerechnet und stimmt bis auf Rundung (höchstens 3,4 €).

### Cited Findings

**Testfall A – Kirchner (2004), Lehrbeispiel**

Quelle: Joachim Kirchner, "Investitionsrechnungen in der Wohnungswirtschaft", Skript zur Vorlesung Wohnungswirtschaftliche Theorie I vom 28.1.2004, Institut Wohnen und Umwelt, Abschnitte 3.1.1 und 3.1.2, S. 14–18 (VOFI-Tabelle S. 17, Renditeformel S. 18) — [IWU-PDF](https://www.iwu.de/fileadmin/publikationen/wohnen/2004_IWU_Kirchner_Investitionsrechnungen-in-der-Wohnungswirtschaft-Wohnungswirtschaftliche-Theorie-I.pdf)

Eingaben (S. 14, 17):
- Eigenmittel M0 = 1.000 € in t = 0; keine weiteren Basiszahlungen.
- Sollzins 7,5 %, Habenzins 5,0 %, konstant; Ergänzungsfinanzierung und -investition jeweils einperiodig, beliebig teilbar.
- Projekt A: −1.100 / 400 / 0 / 1.000 (t = 0..3). Projekt B: −900 / 600 / 450 / 0.
- Rekursion (S. 16): C_t = M_t + Ü_t + (1 + p_t) · C_(t−1), mit Habenzins bei positivem, Sollzins bei negativem Saldo; C_0 = M_0 + Ü_0.
- VOFI-Rentabilität (S. 18): r = (C_T / M_0)^(1/T) − 1.

Vollständiger Finanzplan Projekt A (S. 17):

| t | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Basiszahlung M | 1.000,00 | 0,00 | 0,00 | 0,00 |
| Projekt A | −1.100,00 | 400,00 | 0,00 | 1.000,00 |
| Ergänzungsfinanzierung (Aufnahme / Rückzahlung mit Zins) | 100,00 | −107,50 | | |
| Ergänzungsinvestition 1 | | −292,50 | 307,13 | |
| Ergänzungsinvestition 2 | | | −307,13 | 322,48 |
| Endvermögen | 0,00 | 0,00 | 0,00 | 1.322,48 |

Vollständiger Finanzplan Projekt B (S. 17):

| t | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Basiszahlung M | 1.000,00 | 0,00 | 0,00 | 0,00 |
| Projekt B | −900,00 | 600,00 | 450,00 | 0,00 |
| Ergänzungsinvestition 0 | −100,00 | 105,00 | | |
| Ergänzungsinvestition 1 | | −705,00 | 740,25 | |
| Ergänzungsinvestition 2 | | | −1.190,25 | 1.249,76 |
| Endvermögen | 0,00 | 0,00 | 0,00 | 1.249,76 |

Ergebnisse (S. 18): VOFI-Rentabilität A = 9,76 %; B = 7,71 %; Variante A mit Eigenkapital 900 statt 1.000: 10,19 %.

Kontrollvariante (S. 22, einheitlicher Kalkulationszins 7,5 % für Soll und Haben): Endvermögen A = 1.338,02 €, B = 1.301,35 €.

Hinweise zur Quelle: In der Tabelle zu Projekt B (S. 17) ist die Ergänzungsinvestition in t = 2 ohne Minuszeichen gedruckt ("1.190,25"); auf S. 22 steht für Projekt A "−313,44" statt −314,44. Beides sind Druckfehler; die Endwerte sind rechnerisch konsistent (eigene Nachrechnung: A 1.322,48125; B 1.249,7625; A mit EK 900: Endwert 1.203,96).

**Testfall B – IWU (2013), vermietetes Mehrfamilienhaus "MFH68 – KfW 100"**

Quelle: Andreas Enseling, Eberhard Hinz, Martin Vaché, "Akteursbezogene Wirtschaftlichkeitsberechnungen von Energieeffizienzmaßnahmen im Bestand – Berechnungen mit dem Vollständigen Finanzplan", Endbericht im Auftrag des HMUELV, Institut Wohnen und Umwelt, Darmstadt, 31.07.2013 — [IWU-PDF](https://www.iwu.de/fileadmin/user_upload/dateien/energie/sonstiges/Endbericht_Akteursbezogene_Wirtschaftlichkeit.pdf). Fundstellen: Annahmen Vermietung S. 24–25 (Tabelle 16 auf S. 25); Mieterhöhungen Tabelle 17, S. 26; Ergebnis Tabelle 19, S. 27; vollständiger Finanzplan "MFH68-KfW 100 - Energetische Modernisierungsinvestition – Vermietung (Referenzfall/Gesamtgebäude)", Anhang C, S. 51 (Tabelle als Bild, hier abgelesen); Modellgebäude Tabelle 3, S. 10; KfW-Zuschuss Tabelle 6, S. 18; Zinsannahmen S. 17.

Eingaben:

| Eingabe | Wert | Fundstelle im Bericht |
|---|---|---|
| Gebäude | MFH, Baualtersklasse 1958–1968, 782 m² Wohnfläche, 12 Wohneinheiten | Tabelle 3, S. 10 |
| Betrachtungszeitraum | 25 Jahre, kein Restwert | Tabelle 16, S. 25; S. 17 |
| Anfangsauszahlung (energiebedingte Mehrkosten nach Kopplungsprinzip) | 88.992 € (114 €/m²) | Anhang C, S. 51; Tabelle 17 |
| Vollkosten der Maßnahmen | 201.142 € (257 €/m²) | Hausdatenblatt, Anhang A |
| KfW-Investitionszuschuss | 25.143 €, Zufluss in t = 1 (12,5 % für KfW 100, max. 9.375 € je WE) | Anhang C; Tabelle 6, S. 18 |
| Eigenkapital / Fremdkapital | 71.194 € / 17.798 € (80 % / 20 % der Anfangsauszahlung) | Anhang C; S. 25 |
| Darlehen | Annuitätendarlehen, 25 Jahre, 4,0 % nominal, jährlich nachschüssig, vollständig getilgt | S. 25, S. 17 |
| Habenzins Anschlussinvestition / Sollzins Zwischenfinanzierung | 3,0 % / 6,0 % | Tabelle 16; S. 17 |
| Miete im Ausgangszustand = Vergleichsmiete unsaniert | 5,50 €/m² monatlich | Tabelle 16 |
| Vergleichsmiete saniert | 5,79 €/m² monatlich (Zuschlag 0,29 €/m²) | Tabelle 16; S. 24 |
| Steigerung der Vergleichsmieten | 1,0 % p. a. | Tabelle 16 |
| Mietausfallwagnis | 2 % | Tabelle 16 |
| Mieterhöhung nach § 559 BGB mit Abzug der Förderung | 0,75 €/m² monatlich | Tabelle 17, S. 26 |
| Steuern | nicht betrachtet | S. 25 ("Steuerliche Gesichtspunkte werden nicht betrachtet") |
| Ergebnis | Endwert 153.032 €; VOFI-Rendite (Kapitalrentabilität EK) 3,11 % | Anhang C, S. 51; Tabelle 19, S. 27 |

Zeilenstruktur der Originaltabelle: Direkte Zahlungen (Anfangsauszahlung, zusätzliche Mieteinnahmen, Restwert, KfW-Zuschuss); Indirekte Zahlungen (Eigenkapital, Fremdkapital, Zinsen Fremdkapital, Tilgung, FK-KfW, Zinsen KfW, Tilgung KfW, Steuerzahlung, Sollzinsen Zwischenfinanzierung, Rückzahlung Zwischenfinanzierung, Zwischenfinanzierung, Habenzinsen Anschlussinvestition, Rückzahlung Anschlussinvestition, Reinvestition); Endwert; VOFI-Rendite. Die Zeilen Restwert, FK-KfW, Zinsen KfW, Tilgung KfW, Steuerzahlung und alle Zwischenfinanzierungszeilen sind in diesem Fall leer.

t = 0: Anfangsauszahlung −88.992; Eigenkapital +71.194; Fremdkapital +17.798.

Periodentabelle t = 1..25 (Beträge in Euro, wie veröffentlicht gerundet; abgelesen aus Anhang C, S. 51):

| t | Zusätzliche Mieteinnahmen | KfW-Zuschuss | Zinsen Fremdkapital | Tilgung | Habenzinsen Anschlussinvestition | Rückzahlung Anschlussinvestition | Reinvestition | Endwert |
|---|---|---|---|---|---|---|---|---|
| 1 | 6.883 | 25.143 | −712 | −427 |  |  | −30.886 |  |
| 2 | 6.377 |  | −695 | −444 | 927 | 30.886 | −37.051 |  |
| 3 | 5.866 |  | −677 | −462 | 1.112 | 37.051 | −42.889 |  |
| 4 | 5.350 |  | −659 | −481 | 1.287 | 42.889 | −48.387 |  |
| 5 | 4.829 |  | −639 | −500 | 1.452 | 48.387 | −53.529 |  |
| 6 | 4.303 |  | −619 | −520 | 1.606 | 53.529 | −58.298 |  |
| 7 | 3.771 |  | −599 | −541 | 1.749 | 58.298 | −62.679 |  |
| 8 | 3.234 |  | −577 | −562 | 1.880 | 62.679 | −66.654 |  |
| 9 | 2.888 |  | −554 | −585 | 2.000 | 66.654 | −70.403 |  |
| 10 | 2.917 |  | −531 | −608 | 2.112 | 70.403 | −74.292 |  |
| 11 | 2.946 |  | −507 | −633 | 2.229 | 74.292 | −78.327 |  |
| 12 | 2.975 |  | −481 | −658 | 2.350 | 78.327 | −82.513 |  |
| 13 | 3.005 |  | −455 | −684 | 2.475 | 82.513 | −86.855 |  |
| 14 | 3.035 |  | −428 | −712 | 2.606 | 86.855 | −91.356 |  |
| 15 | 3.066 |  | −399 | −740 | 2.741 | 91.356 | −96.023 |  |
| 16 | 3.096 |  | −370 | −770 | 2.881 | 96.023 | −100.861 |  |
| 17 | 3.127 |  | −339 | −800 | 3.026 | 100.861 | −105.874 |  |
| 18 | 3.158 |  | −307 | −832 | 3.176 | 105.874 | −111.070 |  |
| 19 | 3.190 |  | −274 | −866 | 3.332 | 111.070 | −116.453 |  |
| 20 | 3.222 |  | −239 | −900 | 3.494 | 116.453 | −122.029 |  |
| 21 | 3.254 |  | −203 | −936 | 3.661 | 122.029 | −127.805 |  |
| 22 | 3.287 |  | −166 | −974 | 3.834 | 127.805 | −133.786 |  |
| 23 | 3.320 |  | −126 | −1.013 | 4.014 | 133.786 | −139.980 |  |
| 24 | 3.353 |  | −86 | −1.053 | 4.199 | 139.980 | −146.393 |  |
| 25 | 3.386 |  | −44 | −1.095 | 4.392 | 146.393 |  | 153.032 |

Endwert in t = 25: 153.032 € (= 146.393 + 4.392 + 3.386 − 44 − 1.095). VOFI-Rendite = (153.032 / 71.194)^(1/25) − 1 = 3,11 %.

Dieselben Daten als CSV:

```csv
t,zusaetzliche_mieteinnahmen,kfw_zuschuss,zinsen_fk,tilgung,habenzinsen,rueckzahlung_anschlussinvestition,reinvestition,endwert
0,0,0,0,0,0,0,0,
# t=0: anfangsauszahlung=-88992; eigenkapital=71194; fremdkapital=17798
1,6883,25143,-712,-427,0,0,-30886,
2,6377,0,-695,-444,927,30886,-37051,
3,5866,0,-677,-462,1112,37051,-42889,
4,5350,0,-659,-481,1287,42889,-48387,
5,4829,0,-639,-500,1452,48387,-53529,
6,4303,0,-619,-520,1606,53529,-58298,
7,3771,0,-599,-541,1749,58298,-62679,
8,3234,0,-577,-562,1880,62679,-66654,
9,2888,0,-554,-585,2000,66654,-70403,
10,2917,0,-531,-608,2112,70403,-74292,
11,2946,0,-507,-633,2229,74292,-78327,
12,2975,0,-481,-658,2350,78327,-82513,
13,3005,0,-455,-684,2475,82513,-86855,
14,3035,0,-428,-712,2606,86855,-91356,
15,3066,0,-399,-740,2741,91356,-96023,
16,3096,0,-370,-770,2881,96023,-100861,
17,3127,0,-339,-800,3026,100861,-105874,
18,3158,0,-307,-832,3176,105874,-111070,
19,3190,0,-274,-866,3332,111070,-116453,
20,3222,0,-239,-900,3494,116453,-122029,
21,3254,0,-203,-936,3661,122029,-127805,
22,3287,0,-166,-974,3834,127805,-133786,
23,3320,0,-126,-1013,4014,133786,-139980,
24,3353,0,-86,-1053,4199,139980,-146393,
25,3386,0,-44,-1095,4392,146393,0,153032
```

### Inferences
- **Mietreihe ist aus den Berichtsannahmen exakt reproduzierbar (eigene Nachrechnung, alle 25 Werte ohne Abweichung):** Mieterhöhung Δm = 11 % × (88.992 − 25.143) / 12 / 782 = 0,7484 €/m² monatlich (im Bericht gerundet 0,75); zusätzliche Mieteinnahme_t = [max(5,50 + Δm; 5,79 × 1,01^(t−1)) − 5,50 × 1,01^(t−1)] × 782 × 12 × 0,98. Bis Jahr 8 schmilzt der Mehrertrag ab, weil die Vergleichsrechnung ohne Modernisierung der Vergleichsmiete folgt; ab Jahr 9 bleibt der Zuschlag 0,29 €/m², mit 1 % p. a. wachsend. Der Umlagesatz von 11 % ist im Bericht nicht als Zahl gelesen worden, sondern ergibt sich aus der exakten Reproduktion; er entsprach dem damaligen § 559 BGB.
- Der Zuschuss ist 12,5 % der Vollkosten (0,125 × 201.142 = 25.142,75), wird aber vollständig von den umlagefähigen Mehrkosten abgezogen. Das entspricht der Logik des § 559a Abs. 1 BGB.
- Darlehenszeilen sind reproduzierbar: Annuität = 17.798,40 × 0,04 / (1 − 1,04^−25) = 1.139,31 € p. a.; Zins und Tilgung stimmen in allen 25 Jahren auf den Euro (eine Abweichung von 1 € in Jahr 22).
- Rekursion: Reinvestition_t = Reinvestition_(t−1) × 1,03 + Miete_t + Zuschuss_t − Zins_t − Tilgung_t. Mit ungerundeten Darlehenswerten ergibt die Nachrechnung einen Endwert von 153.028,94 € (veröffentlicht 153.032 €; Abweichung 3,06 €, weil die Mietreihe nur gerundet vorliegt) und 3,108 %.
- Empfohlene Toleranzen für den automatisierten Test: Zins/Tilgung ±1 €, Salden ±4 €, Endwert ±4 €, Rendite ±0,005 Prozentpunkte. Rechnet der Test die Mietreihe aus den Annahmen mit voller Genauigkeit, sollten die Abweichungen kleiner werden; das wurde nicht geprüft.
- Der Testfall B rechnet eine Zusatzinvestition (Differenzbetrachtung "mit/ohne Modernisierung"), kein Gesamtobjekt mit Kaufpreis und Restwert, und nutzt weder Steuerzeile noch Sollzins-Zweig. Für Steuern, Zwischenfinanzierung und Exit sind eigene synthetische Testfälle nötig; der Sollzins-Zweig ist durch Testfall A (Projekt A, t = 0) abgedeckt.
- Der Parameterstand ist historisch (11 % Umlage, keine Kappungsgrenze); heute gelten 8 % und 3 €/2 € je m² (Abschnitt 6). Der Fall eignet sich als Regressionstest für die Rechenlogik, nicht als Abbild des geltenden Rechts.

### Gaps
- Die weiteren Finanzpläne in Anhang C (S. 47–54: EFH48 und MFH68, Selbstnutzer und Vermietung, je vier Standards) wurden nicht abgelesen; der zweite Plan auf S. 51 (MFH68 – KfW 70, VOFI-Rendite 3,08 %) stünde als zusätzlicher Testfall bereit.
- Kirchner (2004) enthält ab S. 28 ein zweites, wohnungswirtschaftliches Beispiel (48 Wohnungen, frei finanziert gegenüber gefördert, Planungshorizont 50 Jahre, mit Steuern, II. BV und Restwert). Es wurde nicht ausgewertet; ob es als VOFI oder mit Barwertverfahren gerechnet ist, wurde nicht geprüft.
- Ein IWU-Dokument mit vollständiger VOFI-Tabelle einschließlich Steuerzeile wurde nicht gefunden; Die zwei heruntergeladenen IWU-Vortragsfoliensätze (RentalCal 2.0 von 2021, Wirtschaftlichkeitsberechnungen von 10/2023) enthalten in der Textebene keine VOFI-Periodentabelle; weitere RentalCal-Dokumente wurden nicht durchsucht.
- Die IWU-Tabelle liegt nur als Bild mit geringer Auflösung vor; alle Ziffern wurden visuell abgelesen und über die Rekursion gegengeprüft, eine einzelne Fehlablesung im Bereich ±1 € ist dennoch nicht ausgeschlossen.
