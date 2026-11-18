# Notiz 11: Schulte et al., „Immobilieninvestition" – Auswertung am Original

Zweck: Den Immobilien-VOFI am Lehrbuchtext klären (Zeilenaufbau, Kennzahlen, Musterrechnung) und mit dem Projektstand abgleichen. Leser: Fachspezifikation Rechenkern (Spezifikation Kapitel 3), Pflege von Quellenkataster und Modellannahmen. Stand: 2026-11-18.

Seitenangaben „S." sind Buchseiten. „Projekt" meint Spezifikation Kapitel 3 und Anhang A des Rechercheberichts. Eigene Rechnungen sind als solche bezeichnet; sie stehen im Skript `skripte/schulte_musterrechnung.py`.

## Quelle

| Merkmal | Angabe | Woher |
|---|---|---|
| Verfasser | „Karl-Werner Schulte et al."; die Mitverfasser nennt das PDF nicht | Kolumnentitel der geraden Seiten |
| Kapitel | „4 Immobilieninvestition". Das PDF enthält daraus die Abschnitte 4 „Einführung in die Investitionsrechnung für Immobilieninvestitionen", 5 „Fazit" und 6 „Literatur"; die Abschnitte 1 bis 3 (Anlageformen und Entscheidungskriterien, vgl. S. 787) fehlen | Kolumnentitel der ungeraden Seiten, Überschriften |
| Seiten | 787–838 (52 PDF-Seiten) | Seitenzahlen |
| Sammelwerk | „Immobilienökonomie"; als Urheber führt das PDF Karl-Werner Schulte, Stephan Bone-Winkel und Wolfgang Schäfers (nach der Vorauflage im Literaturverzeichnis, S. 837, die Herausgeber). Die Bandzählung „I" steht nicht im PDF; der Auftraggeber nennt das Werk „Immobilienökonomie I" | Metadaten des PDF |
| Verlag, Jahr | © 2025 Walter de Gruyter GmbH, Berlin/Boston; DOI 10.1515/9783111704906; PDF erzeugt am 17.03.2026 | Metadaten des PDF |
| Auflage | nicht erkennbar. Das Literaturverzeichnis führt „Immobilienökonomie I: Betriebswirtschaftliche Grundlagen" von 2015 als zitierte Quelle (S. 837); das gelesene Kapitel ist also jünger. Inhaltlich reicht es bis mindestens Juli 2025 (S. 792) | Text |
| Gelesen | vollständig am 18.11.2026; die Tabellen 7 bis 14 sind Rasterbilder im Querformat und wurden vergrößert gelesen | – |

Das PDF liegt nicht im Repository und gehört dort nicht hin.

## Ergebnis

1. **Zeilenaufbau geklärt.** Das Kapitel zeigt den Immobilien-VOFI vollständig in acht Tabellen (S. 812–829). Er ist einfacher als die Rekonstruktion in Notiz 03: Es gibt kein Guthaben- und kein Kontokorrentkonto mit Bestandszeile, sondern je Periode eine einjährige „Reinvestition" oder „Zwischenfinanzierung", die in der Folgeperiode mit Zins zurückfließt. Rechnerisch ist das dasselbe wie ein Konto, das auf den Stand der Vorperiode verzinst wird. Die Vorgaben A.1 Nr. 1 bis 4 des Berichts sind damit am Original bestätigt.
2. **Kennzahlen nur zum Teil.** Belegt sind Endvermögen, Vermögensendwert (im Projekt: Endwertdifferenz), VOFI-Rendite auf das Eigenkapital und der Vergleich mit der Unterlassungsalternative, die als eigener VOFI gerechnet wird (S. 810–815). Die Gesamtkapitalrentabilität wird nur an Grob (2015), S. 140 f. verwiesen (S. 813). Die Amortisationsdauer erscheint nur als Kästchen in einer Übersicht (S. 799). Für mehrere Eigenkapitaleinlagen und für Entnahmen gibt das Kapitel ausdrücklich keine Formel und verweist auf Ropeter (1998), S. 186 ff. (S. 816).
3. **Musterrechnungen nachgebaut.** Das Standardbeispiel (fünf Jahre; vier Finanzpläne) trifft alle Buchwerte. Das Fallbeispiel Bürogebäude (zehn Jahre; drei Kreditvarianten und Finanzinvestition) trifft alle Werte der drei Immobilienpläne; die Finanzinvestition weicht in sechs Zellen um je eine Einheit ab (Endvermögen 30.444 statt 30.445 Tausend Euro). Insgesamt 50 von 53 Prüfungen; Einzelheiten unter „Musterrechnungen".
4. **Wichtigste Abweichung zum Projekt:** Die Unterlassungsalternative des Buchs hat zwei Zinssätze – einen langfristigen für das angelegte Eigenkapital und einen kurzfristigen für die Wiederanlage der Zinsen. Die Projektformel EK × (1 + h × (1 − s))^n kennt nur einen Satz und liegt im Fallbeispiel um 404 Tausend Euro (1,3 %) über dem Buchwert.
5. **Modellannahmen:** `MA-012` teilweise geklärt (das Lehrbuch bestätigt, dass es keine Formel gibt), `MA-027` und `MA-028` gar nicht.

## Gliederung des Kapitels

| Abschnitt | Inhalt | S. |
|---|---|---|
| 4.1 | Anforderungskatalog: absolute und relative Vorteilhaftigkeit (4.1.1), Besonderheiten der Immobilie (4.1.2) | 787–789 |
| 4.2.1 | Datenbasis, direkte Zahlungen: Investitionsausgabe a_0, laufende Einnahmen e_t, laufende Ausgaben a_t, Überschüsse ü_t, Veräußerungserlös R_n | 789–795 |
| 4.2.2 | Indirekte Zahlungen: Verwendung von Überschüssen, Ausgleich von Fehlbeträgen, Steuern | 795–797 |
| 4.3.1 | Typologie der Verfahren (klassisch statisch, klassisch dynamisch, modern) | 797–799 |
| 4.3.2 | Klassische Methoden: statisch und dynamisch, Kalkulationszinsfuß, Kapitalwert, Standardbeispiel, interner Zinsfuß, Steuern im Standardmodell, Steuerparadoxon | 798–810 |
| 4.3.3 | Moderne Methoden: Basiskonzept VOFI, Endvermögen, Erläuterung des Standardbeispiels (Tab. 3, 4), VOFI-Rentabilität, Steuern (Tab. 5, 6), Fallbeispiel Bürogebäude (Tab. 7–15) | 810–830 |
| 4.4 | Kritische Würdigung | 821, 830 |
| 5 | Fazit | 830–831 |
| 6 | Literatur | 831–838 |

## Zeilenaufbau des VOFI

### Hauptplan (Tab. 3 und 5, S. 812 und 818)

| Block | Zeile | Vorzeichen und Inhalt |
|---|---|---|
| Direkte Zahlungen | a_0 | Investitionsausgabe in t_0, negativ |
| | ü_t | Einnahmenüberschuss je Periode t_1 bis t_n |
| | R_n | Veräußerungserlös in t_n, brutto |
| Indirekte Zahlungen | Eigenkapital | Einlage in t_0, positiv |
| | Fremdkapital (Fallbeispiel: „Kreditaufnahme") | Auszahlung des Kredits in t_0, positiv |
| | Zinsen FK | negativ; Sollzins auf den Kreditstand am Ende der Vorperiode |
| | Tilgung | negativ |
| | Steuerzahlung | nur im Plan mit Steuern; aus der Nebenrechnung |
| | Reinvestition t_k | Anlage des Überschusses der Periode k, negativ |
| | Habenzinsen | Zins der Anlage, eine Periode später |
| | Rückzahlung | Rückfluss der Anlage, eine Periode später |
| | Zwischenfinanzierung t_k / Sollzinsen / Rückzahlung | dieselben drei Zeilen mit umgekehrtem Vorzeichen, wenn die Periode k mit einem Fehlbetrag schließt (Tab. 5, 9) |
| Saldo | „Endwert" (Fallbeispiel: „Endvermögen") | in t_0 bis t_(n−1) null, in t_n das Endvermögen |
| Nachrichtlich | Kredit nach Tilgung (Fallbeispiel: „Kreditbetrag") | einzige Bestandszeile |
| | Annuität; Sollzinssatz langfristig; Sollzinssatz Zwischenfinanzierung; Guthabenzinsen langfristig; Guthabenzinsen kurzfristig | Parameter je Periode |

Die drei Zeilen Reinvestition/Zins/Rückzahlung wiederholen sich für jede Periode k = 1 bis n − 1; der Plan wächst also mit der Laufzeit um drei Zeilen je Jahr. Eine Zeile für Guthabenstand, Kontokorrentstand oder Bestandssaldo gibt es nicht. Im Fallbeispiel steht die Steuerzahlung zwischen Zinsen und Tilgung (S. 822); im Annuitätenfall trägt der Block weiter den Namen „Reinvestition", führt aber Zwischenfinanzierungen mit „Sollzins 11 %" (S. 824).

### Nebenrechnungen (Tab. 5, S. 818; Tab. 8, S. 823)

| Nebenrechnung | Zeilen |
|---|---|
| Finanzierungsplan (nur Fallbeispiel) | Kreditaufnahme · Kreditzinsen · Kredittilgung · Kreditstand PE |
| Abschreibungsplan | AfA-Satz · AfA-Grundlage (Gebäudewert) · AfA-Betrag · Buchwert (beginnt mit der ganzen Investitionsausgabe einschließlich Grundstück) |
| Steuerliche Nebenrechnung | Mieteinnahmen · − Abschreibungen · + Haben-/Sollzinsen der kurzfristigen Anlage oder Zwischenfinanzierung · − Sollzinsen des Kredits · + Veräußerungserlös · − Restbuchwert · = Ergebnis vor Steuer · × Steuersatz · = Steuerzahlung |

Im Fallbeispiel weist die Nebenrechnung zusätzlich die Zeile „Steuerpflichtiger Veräußerungsgewinn" aus (S. 823).

### Rechenreihenfolge je Periode (S. 811, 817–819)

1. Direkte Zahlungen der Periode einstellen (ü_t, in t_n zusätzlich R_n).
2. Kapitaldienst: Zinsen = Sollzinssatz × Kredit am Ende der Vorperiode; Tilgung = Annuität − Zinsen (S. 811).
3. Rückfluss der Anlage oder Rückzahlung der Zwischenfinanzierung aus der Vorperiode samt Zins (S. 811).
4. Steuerliche Nebenrechnung in dieser Reihenfolge: Einnahmenüberschuss übertragen, Abschreibung aus dem Abschreibungsplan, Sollzinsen aus dem VOFI, Guthabenzinsen aus der Zwischenanlage, im Verkaufsjahr Verkaufserlös abzüglich Restbuchwert; Bemessungsgrundlage × Steuersatz = Steuerzahlung (S. 817, 819).
5. Steuerzahlung als indirekte Zahlung in den VOFI; ein negatives Ergebnis führt zu einer Erstattung (S. 819).
6. Der Zahlungssaldo der Periode wird für ein Jahr angelegt oder zwischenfinanziert; in t_n ist er das Endvermögen (S. 811–812).

Zins und Steuer hängen damit nur von Beständen der Vorperiode und von Zahlungen der laufenden Periode ab; einen Zirkelbezug gibt es nicht.

### Konventionen

| Thema | Regel im Kapitel | S. |
|---|---|---|
| Zahlungszeitpunkt | Alle Zahlungen fallen am Jahresende an; a_0 in t_0. Das Kapitel rechnet nur in Jahren | 789, 819 |
| Steuerzahlung | Am Ende des Jahres, für das sie berechnet ist („sofortige Besteuerung"); keine Voraus- und Abschlusszahlungen | 807 |
| Verluste | Sofortiger Ausgleich mit anderen Einkünften, also Erstattung; Verlustvortrag ausgeklammert | 807 |
| Steuersatz | Ein pauschaler, konstanter Ertragsteuersatz auf eine einheitliche Bemessungsgrundlage; Freibeträge gelten als ausgeschöpft | 807 |
| Abschreibung | Linear auf den Gebäudeanteil; die erste Abschreibung ist eine volle Jahresabschreibung am Ende des ersten Jahres | 807, 817 |
| Reinvestition | Überschüsse werden je ein Jahr zum kurzfristigen Guthabenzins angelegt. Genannte Alternativen: Finanzanlage, Investition ins Objekt, andere Objekte, Kredittilgung | 796, 811 |
| Fehlbeträge | Einjährige Zwischenfinanzierung zu einem eigenen, höheren Sollzins (9 % im Standardbeispiel, 11 % im Fallbeispiel) | 818, 824 |
| Veräußerung | Verkaufserlös brutto als direkte Zahlung in t_n; die Restschuld wird in derselben Periode als Tilgung gezahlt; der Gewinn (Erlös − Restbuchwert) geht in die Steuerrechnung des Verkaufsjahrs. Verkaufskosten kommen nicht vor | 811, 817, 822–823 |
| Kreditarten | Annuitätendarlehen mit Volltilgung über die Laufzeit; endfälliger Kredit; „Kredit mit freier Tilgung", bei dem der ganze Periodenüberschuss tilgt und der Rest am Ende abgelöst wird | 811, 821, 826 |
| Rundung | Ausgewiesen sind ganze Geldeinheiten; gerechnet ist ungerundet (eigene Feststellung: nur so treffen die Zwischenwerte) | 812, 818 |
| Unterlassungsalternative | Eigener VOFI „Finanzinvestition": Eigenkapital zum langfristigen Guthabenzins angelegt, Zinsen jährlich ausgezahlt und zum kurzfristigen Satz wiederangelegt, Rückzahlung in t_n; mit Steuern auf alle Zinsen. Bei voller Fremdfinanzierung ist ihr Endvermögen null | 810, 813–814, 820 |

## Kennzahlen

| Kennzahl | Definition und Formel | S. |
|---|---|---|
| Endvermögen K_N | Saldo des VOFI in t_n; Entscheidung: vorteilhaft, wenn K_N der Investition über K_N der Unterlassungsalternative liegt | 810 |
| Vermögensendwert | ΔK_N = K_N(Investition) − K_N(Unterlassung); das Projekt nennt diese Größe Endwertdifferenz | 810–811 |
| VOFI-Rendite (Eigenkapital) | r_VOFI = (K_N / EK_0)^(1/N) − 1; verglichen wird mit der VOFI-Rendite der Finanzinvestition | 813–815 |
| VOFI-Rendite nach Steuern | dieselbe Formel mit dem Endvermögen nach Steuern | 819 |
| VOFI-Gesamtkapitalrentabilität | nicht behandelt; Verweis auf Grob (2015), S. 140 f. Welche Sollzinsen zuzurechnen sind, sagt das Kapitel nicht | 813 |
| VOFI-Amortisationsdauer, „Entnahme" | nur als VOFI-Kennzahlen in der Typologie genannt, ohne Definition oder Rechenregel. Die Pay-off-Methode ist als klassisches Verfahren aufgezählt und ausdrücklich nicht behandelt | 799, 800–801 |
| Kalkulationszinsfuß | KZF = (i_H × EK + i_S × FK) / (EK + FK) bei Mischfinanzierung | 800 |
| Kapitalwert | C_0 = Summe über t von ü_t × (1 + i)^(−t) + R_n × (1 + i)^(−n) − a_0 | 801 |
| Interner Zinsfuß | Zins r mit C_0(r) = 0; bei mehreren Vorzeichenwechseln mehrdeutig (Beispiel −1.000, +5.000, −6.000 mit 100 % und 200 %) | 803–805 |
| Kapitalwert nach Steuern (Standardmodell) | i_s = (1 − s) × i; C_0s = Summe von [ü_t − s × (ü_t − AfA_t)] × (1 + i_s)^(−t) + [R_n − s × (R_n − RBW_n)] × (1 + i_s)^(−n) − a_0 | 806 |
| Statische Anfangsrendite | Jahresnettomiete / Investitionssumme | 798, 804 |
| Annuität | Fremdkapital × i × (1 + i)^n / ((1 + i)^n − 1) | 821 |

**Mehrere Einlagen und Entnahmen (S. 816).** Das Kapitel nennt drei Problemfälle der VOFI-Rendite:

- Eigenkapital null: Die Formel liefert kein Ergebnis; eine voll fremdfinanzierte Investition mit positivem Ergebnis habe „immer eine unendliche Rendite".
- Eigenkapital zu mehr als einem Zeitpunkt (Projektentwicklung, Kaufpreis in Tranchen, Fondsanteile mit verteilter Einzahlung): Das Endvermögen lässt sich rechnen, die Rendite nicht. Wörtlich: „Weitere Eigenkapitaleinsätze (EK_1 bis EK_n) können zwar im VOFI abgebildet, nicht jedoch von der VOFI-Renditeformel verarbeitet werden" (S. 816). Für einen „praxisorientierten Lösungsansatz" verweist das Kapitel auf Ropeter (1998), S. 186 ff.
- Entnahmen: Der VOFI lässt sich rechnen, der Erfolg ist dann aber nicht mehr allein am Endvermögen zu messen; der ökonomische Gehalt einer so errechneten Rendite sei „äußerst problematisch".

Eine Aussage dazu, ob die Unterlassungsalternative dieselben Einlagen und Entnahmen erhält, enthält das Kapitel nicht.

## Musterrechnungen

### Standardbeispiel (S. 802, 808, 811–820)

Eingangsdaten:

| Größe | Wert | S. |
|---|---|---|
| Investitionsausgabe a_0 in t_0 | 10.000 GE | 802 |
| Einnahmenüberschuss ü_t, t_1 bis t_5 | 540 GE je Jahr | 802 |
| Veräußerungserlös R_5 | 10.000 GE (keine Wertsteigerung) | 802, 811 |
| Eigenkapital / Kredit | 8.000 / 2.000 GE | 802 |
| Kredit | Annuitätendarlehen über fünf Jahre zu 7,5 %, Kapitaldienst 494 | 811–812 |
| Reinvestition | je ein Jahr zu 4,5 % | 811 |
| Zwischenfinanzierung | 9,0 % | 812, 818 |
| Finanzinvestition | 8.000 GE zu 5,0 % (langfristig), Wiederanlage der Zinsen zu 4,5 % | 813–814 |
| Steuersatz | 50 %, auch auf Zinsen; Veräußerungsgewinn steuerpflichtig | 808, 817 |
| Abschreibung | Gebäudewert 5.000 GE, linear über 20 Jahre, 250 GE je Jahr; Restbuchwert in t_5 8.750 | 808, 817–818 |

Ergebnisse und Prüfpunkte (Buchwerte; die Nachrechnung trifft alle):

| Plan | Prüfpunkte je Jahr | Endvermögen | VOFI-Rendite | S. |
|---|---|---|---|---|
| Klassisch, ohne Steuern | Kalkulationszinsfuß 5,5 % | Kapitalwert −43 | interner Zinsfuß 5,4 % | 802, 804 |
| Klassisch, mit Steuern | i_s 2,75 %; ü nach Steuern 395; Netto-Veräußerungserlös 9.375 | Kapitalwert +8 | interner Zinsfuß 2,77 % | 808, 810 |
| Tab. 3 Immobilie ohne Steuern | Kredit nach Tilgung 1.656 / 1.286 / 888 / 460 / 0; Reinvestition 46 / 93 / 143 / 195 | 10.250 | 5,08 % | 812, 815 |
| Tab. 4 Finanzinvestition ohne Steuern | Reinvestition 400 / 818 / 1.255 / 1.711 | 10.188 | 4,95 % | 813–815 |
| Tab. 5 Immobilie mit Steuern | Steuerzahlung 70 / 82 / 94 / 106 / 744; Zwischenfinanzierung 24 / 63 / 117 / 188 | 9.097 | 2,60 % | 817–819 |
| Tab. 6 Finanzinvestition mit Steuern | Steuerzahlung 200 / 205 / 209 / 214 / 219; Reinvestition 200 / 405 / 614 / 827 | 9.046 | 2,49 % | 819–820 |

Das Buch zieht daraus: Nach Kapitalwert und internem Zinsfuß wäre die Investition zu unterlassen, nach dem Endvermögen ist sie vorzuziehen, weil der VOFI Kapitalkosten und Wiederanlage genauer erfasst (S. 813). Eigene Rechnung: Der Vermögensendwert beträgt 61,57 GE ohne und 50,53 GE mit Steuern; die Endvermögen in voller Genauigkeit sind 10.249,85 / 10.188,28 / 9.096,56 / 9.046,02 GE.

### Fallbeispiel Bürogebäude (S. 819–830)

Eingangsdaten nach den Tabellen, Beträge in Tausend Euro:

| Größe | Wert | S. |
|---|---|---|
| Investitionsausgabe in t_0 | 43.738 | 822 |
| Netto-Mieteinnahmen, nachschüssig, t_1 bis t_10 | 3.606 je Jahr | 819, 822 |
| Veräußerungserlös in t_10 | 43.738 (keine Wertsteigerung) | 819, 822 |
| Eigenkapital / Kredit | je 21.869 (50 % / 50 %) | 819, 822 |
| Sollzins des Kredits | 10 %, für alle Kreditvarianten | 819 |
| Kreditvarianten | endfällig · Annuitätendarlehen über zehn Jahre, Annuität 3.559 · freie Tilgung | 821 |
| Reinvestition | je ein Jahr zu 5 % | 821 |
| Zwischenfinanzierung | 11 % (nur aus den Tabellen ersichtlich) | 824 |
| Abschreibung | Gebäudeanteil 15.000, 4 %, also 600 je Jahr; Restbuchwert in t_10 37.738 | 819, 823 |
| Steuern | Betriebsvermögen, Ertragsteuersatz 50 %; Veräußerungsgewinn 6.000 steuerpflichtig | 821, 823 |
| Finanzinvestition | 21.869 zu 7 % über zehn Jahre (1.531 je Jahr), Wiederanlage zu 5 % | 819, 828 |

Ergebnisse (Tab. 15, S. 830) und Nachrechnung:

| Alternative | Endvermögen Buch | Nachrechnung | VOFI-Rendite Buch | Nachrechnung | Prüfpunkte |
|---|---|---|---|---|---|
| Endfälliger Kredit | 30.179 | 30.179,37 | 3,27 % | 3,273 % | Steuerzahlung, Reinvestition und Ergebnis vor Steuer je Jahr treffen (S. 822–823) |
| Annuitätendarlehen | 31.400 | 31.400,46 | 3,68 % | 3,684 % | Zinsen, Kreditstand, Steuerzahlung, Zwischenfinanzierung je Jahr treffen (S. 824–825) |
| Freie Tilgung | 31.576 (Tab. 15), 31.567 (Tab. 11) | 31.567,01 | 3,74 % | 3,739 % | Tilgung, Kreditstand, Steuerzahlung je Jahr treffen (S. 826–827) |
| Finanzinvestition | 30.445 | 30.444,24 | 3,36 % | 3,364 % | sechs Zellen weichen um je 1 ab (S. 828–829) |

Weitere Prüfpunkte je Jahr (Buchwerte, von der Nachrechnung getroffen):

- Endfälliger Kredit, Reinvestition t_1 bis t_9: 1.010 / 2.044 / 3.105 / 4.192 / 5.307 / 6.449 / 7.620 / 8.820 / 10.050 (S. 822).
- Annuitätendarlehen, Zwischenfinanzierung t_1 bis t_9: 363 / 814 / 1.365 / 2.030 / 2.823 / 3.760 / 4.858 / 6.139 / 7.624 (S. 824).
- Freie Tilgung, Kreditstand t_1 bis t_10: 20.859 / 19.799 / 18.686 / 17.518 / 16.291 / 15.002 / 13.649 / 12.229 / 10.737 / 0 (S. 826).

Das Buch folgert: Die Immobilie ist mit endfälligem Kredit unvorteilhaft, mit Annuitätendarlehen und mit freier Tilgung der Finanzinvestition überlegen; die freie Tilgung ist optimal (S. 821).

### Abweichungen der Nachrechnung und Unstimmigkeiten im Kapitel

- **Tab. 13/14 (S. 828–829), einzige Abweichung der Nachrechnung.** Mit 7 % auf 21.869 ergeben sich Steuerzahlung t_2 785 statt 784, Reinvestition t_4, t_5, t_6 und t_9 je um 1 niedriger und ein Endvermögen von 30.444 statt 30.445; die Rendite stimmt. Vermutung: Die Tabelle ist mit einem nicht gerundeten Zinsertrag gerechnet und zusätzlich in sich um eine Einheit unstimmig. Eine Suche über alle Zinserträge, die gerundet 1.531 ergeben, findet keinen, der alle Zellen trifft; im besten Fall (1.530,92 bis 1.530,98) bleibt die Steuerzahlung t_2 abweichend. Der Grund: Eine Steuerzahlung von 784 in t_2 verlangt bei 50 % Steuer und 5 % Wiederanlage einen Zinsertrag unter 1.530,74, das Endvermögen 30.445 einen über 1.530,87. Nichts wurde angepasst.
- **Tab. 15 (S. 830):** Endvermögen bei freier Tilgung 31.576; Tab. 11 (S. 826) und die Nachrechnung ergeben 31.567. Zahlendreher in der Zusammenfassung; die Rendite ist davon nicht berührt.
- **Fließtext S. 819 gegen Tabellen:** Der Text nennt 44.800.000 Euro Kaufpreis und 3.700.000 Euro Mieteinnahmen; alle Tabellen und die Annuitätenrechnung auf S. 821 rechnen mit 43.738 und 3.606 Tausend Euro. Der Referenzfall folgt den Tabellen.
- **Zwischenfinanzierungssatz im Fallbeispiel:** Der Text nennt nur 10 % Sollzins und 5 % Anlagezins; die 11 % stehen nur in den Tabellen (S. 824, 826, 828). Tab. 7 weist in derselben Zeile 10 % aus (S. 822), ohne Folge, weil dort keine Zwischenfinanzierung anfällt.
- **Rentenbarwertfaktor (S. 802, 804):** Die abgedruckten Brüche sind verdruckt; die Ergebnisse (−43 und 5,4 %) folgen aus der üblichen Form des Faktors und aus der Summenformel auf S. 801.
- **Abb. 12 (S. 815):** Die Kurve der VOFI-Rendite über dem Eigenkapitaleinsatz lässt sich bei niedrigem Eigenkapital nur mit 10 % Zwischenfinanzierungssatz treffen (abgelesen etwa −4,6 % bei 2.500 und −1,9 % bei 3.000; mit 9 % wie in Tab. 3 wären es −3,08 % und −0,83 %). Nur aus dem Diagramm abgelesen, daher kein Prüfpunkt.

## Abgleich mit dem Projekt

### Anhang A des Berichts

| Vorgabe | Befund | S. |
|---|---|---|
| A.1 Nr. 1: Zinsen und Steuern hängen nur von Beständen der Vorperiode ab; Geldanlage und Kontokorrent gleichen aus | **bestätigt** in der Sache. Darstellung **abweichend**: einjährige Anlagen und Zwischenfinanzierungen statt Konten, keine Bestandszeilen außer dem Kreditstand | 811–812, 818 |
| A.1 Nr. 2: Kontokorrentzins in Steuerbemessung und Periodensaldo | **bestätigt**: Sollzinsen der Zwischenfinanzierung stehen im VOFI und in der Nebenrechnung | 818, 825 |
| A.1 Nr. 3: Ablösung der Restschuld als Zahlung der letzten Periode; Verkaufserlös vor Schulden | **bestätigt** (Tilgung 21.869 in t_10 bei endfälligem Kredit, 10.737 bei freier Tilgung; R_n brutto). Verkaufskosten, Fördermittel, Investitionsstau: **nicht behandelt** | 822, 826 |
| A.1 Nr. 4: Steuern über Nebenrechnung mit Abschreibungsplan und Verlustvortrag; getrennter Satz auf Zinserträge | Nebenrechnung und Abschreibungsplan **bestätigt**. **Abweichend:** Verlustvortrag ausgeklammert, ein Satz für alles – als Vereinfachung, die sich ausdrücklich an die reale Lage anpassen lasse | 807, 817–818 |
| A.1 Nr. 5: begrenzte Kontokorrentlinie | **nicht behandelt** | – |
| A.2 Nr. 6: Konventionen je Zahlungsart; Eingabewert der Miete gilt für das erste Jahr | Jahresende für alle Zahlungen, Steuer im Jahr der Entstehung, volle erste Jahresabschreibung: **bestätigt** für den Jahresmodus. Indexierung, Basisperiode der Miete: **nicht behandelt** (Überschüsse sind in beiden Beispielen konstant) | 789, 807 |
| A.2 Nr. 7: Investition und Unterlassensalternative im selben Takt | **bestätigt** (beide jährlich, gleicher kurzfristiger Anlagezins) | 812, 814 |
| A.2 Nr. 8: Jahresmodus für Lehrbuchvergleiche | **bestätigt**: Das Kapitel rechnet nur jährlich | 789 |
| A.2 Nr. 10: Rundungsregeln (`MA-013`) | **nicht behandelt**. Die Tabellen zeigen gerundete Werte einer ungerundeten Rechnung; der Referenzfall muss ungerundet rechnen und gerundet vergleichen | 812 |
| A.3 Nr. 11: Unterlassensalternative mit derselben Einlagen- und Entnahmenreihe | **nicht behandelt** (nur eine Einlage in t_0) | 816 |
| A.3 Nr. 12: Renditeformel; Vergleich mit dem effektiven Jahreszins der Alternative | Grundformel **bestätigt**. Erweiterung auf mehrere Einlagen und Entnahmen: **nicht behandelt**, als ungelöst benannt. **Abweichend:** Die Alternative hat zwei Zinssätze; ihr Vergleichszins ist die VOFI-Rendite der Finanzinvestition (4,95 %), nicht h × (1 − s) aus einem Satz | 813–816 |
| A.3 Nr. 13, 14: Saldierung, Lesarten bei Nachschuss | **nicht behandelt** | 816 |
| A.3 Nr. 15: Randfälle (Eigenkapital null: Rendite nicht definiert) | **bestätigt** für Eigenkapital null; negativer Zähler **nicht behandelt** | 816 |
| A.3 Nr. 18: Amortisationsdauer (`MA-027`) | **nicht behandelt** | 799 |
| A.3 Nr. 19: Gesamtkapitalrendite (`MA-028`) | **nicht behandelt**; Fundstelle bei Grob genannt | 813 |
| A.3 Nr. 20: mehrdeutiger interner Zinsfuß | **bestätigt** | 804–805 |
| A.4 Nr. 21: Finanzierungssaldo null je Periode | **bestätigt** (Saldozeile null in t_0 bis t_(n−1)) | 812 |
| A.4 Nr. 22: Kreditprobe | im einfachen Fall erfüllt (Summe der Tilgungen gleich Kredit); Disagio, Zuschüsse, kapitalisierte Zinsen **nicht behandelt** | 823–827 |
| A.4 Nr. 24: abgezinste Endwertdifferenz gleich Kapitalwert nur bei einheitlichem Zins | **bestätigt** im Ergebnis: Mit getrennten Sätzen widersprechen sich Kapitalwert (−43) und Endvermögen (10.250 gegen 10.188). Eigene Probe: Setzt man im Standardbeispiel alle Sätze auf 5,5 %, ist die abgezinste Differenz der Endvermögen −42,70 und gleich dem Kapitalwert | 802, 813 |
| A.5 Nr. 25, 27: Mittelabfluss; Faustformel für Bauzeitzinsen | Das Kapitel nennt die Praxisannahme „50 % des Finanzierungsvolumens" und empfiehlt stattdessen einen idealtypischen Kostenverlauf – **bestätigt** in der Richtung, ohne Rechnung. Bauzeitzinsen gehören zur Investitionsausgabe | 790–791 |
| A.6: Referenzfälle | zwei neue Fälle, siehe Vorschläge | – |
| A.1 Nr. 3 (Einzelheiten), A.3 Nr. 16, 17, A.4 Nr. 23, A.5 Nr. 26, A.7 | **nicht behandelt** (Förderdarlehen, Deckungsgrad, Bestandsprobe, Eigenkapitalquote, Simulation); zur Risikoanalyse nur der Verweis auf ein anderes Kapitel des Werks | 821 |

### Spezifikation Kapitel 3 (und Kapitel 2, Kennzahlen)

| Festlegung | Befund | S. |
|---|---|---|
| Methode: Tabellenrechnung mit Konten für Eigenkapital, jede Kredittranche, Kontokorrent, Geldanlage, Steuern; Saldo null | **bestätigt** in der Sache; das Buch führt statt der Konten einjährige Anlagen und Zwischenfinanzierungen und nur den Kreditstand als Bestand | 812, 818 |
| Zeitraster: Jahresmodus für Lehrbuchfälle | **bestätigt** | 789 |
| Zeithorizont mindestens 42 Jahre | **abweichende Empfehlung**, kein Widerspruch: Das Kapitel rät zu 10 bis 12 Jahren mit unterstelltem Verkauf, weil die Prognose mit der Entfernung ungenauer wird | 794 |
| Ausschüttungen und Nachschüsse (`MA-012`) | **nicht behandelt**; Problem benannt | 816 |
| Restwert: Erlös brutto, Restschuld als Ablösung im Finanzplan | **bestätigt** | 822 |
| Randfälle: Eigenkapital null | **bestätigt** (kein Ergebnis) | 816 |
| Lehrbuchkennzahlen: Eigenkapitalrendite | **bestätigt** am Original; Gesamtkapitalrendite und Amortisationsdauer **nicht behandelt** | 813–815 |
| Kapitel 2, Kennzahlen: Endwertdifferenz führt, Rendite daneben | **bestätigt**: Das Endvermögen ist das Entscheidungskriterium, die Rendite seine „Transformation" in eine Kennziffer | 810, 813 |
| Kapitel 2, Zielrendite als zweiter Maßstab | **berührt**: Das Kapitel hält es für theoretisch besser, Risiken über Sensitivitätsanalysen abzubilden als über einen Zuschlag auf die Kapitalkosten. Das Projekt tut beides | 791 |

### Modellannahmen

- **`MA-012` (Rendite bei mehreren Einlagen und Entnahmen): teilweise geklärt.** Geklärt ist das „Warum offen": Die Lehrbuchformel gilt nur für eine Einlage in t_0, und das Kapitel sagt ausdrücklich, dass weitere Einlagen nicht verarbeitet werden und eine Rendite bei Entnahmen ökonomisch fragwürdig ist (S. 816). Keine der vier Lesarten des Projekts wird gestützt oder verworfen. Gestützt wird die Entscheidung, die Endwertdifferenz führen zu lassen. Der Klärungsweg ist jetzt genauer: Ropeter (1998), S. 186 ff. Neu zu beachten: Der Aufzinsungsfaktor q der Projektformel setzt einen einzigen Alternativzins voraus; die Alternative des Buchs hat zwei Sätze.
- **`MA-027` (Amortisationsdauer): gar nicht geklärt.** Das Kapitel nennt die VOFI-Amortisationsdauer nur in der Typologie (S. 799) und behandelt auch die klassische Pay-off-Methode nicht (S. 801). Es stützt keine Lesart.
- **`MA-028` (zuzurechnende Sollzinsen der Gesamtkapitalrentabilität): gar nicht geklärt.** Das Kapitel verweist auf Grob (2015), S. 140 f. (S. 813) und nennt damit die Fundstelle. Der Satz auf S. 815, der interne Zinsfuß sei „in der hier dargestellten Ausprägung" eine Gesamtkapitalrendite, betrifft den klassischen internen Zinsfuß, nicht die VOFI-Kennzahl.
- **`MA-013` (Rundung in Darlehensplänen): nicht berührt.**

## Was das Kapitel sonst für den Rechenkern hergibt

- **Begriffe.** Endvermögen (Projekt: Endwert), Vermögensendwert (Endwertdifferenz), Unterlassungsalternative (Unterlassensalternative), direkte und indirekte Zahlungen (originär und derivativ), Reinvestition und Zwischenfinanzierung (Geldanlage und Kontokorrent) (S. 789, 810–812).
- **Investitionsausgabe.** Bestandteile: Kaufpreis, Grunderwerbsteuer, Besichtigung, Makler, Notar und Grundbuch, Finanzierungsbeschaffung, Zinsen für Vor- und Zwischenfinanzierung. Anschaffungsausgabe und steuerliche Anschaffungskosten können auseinanderfallen; die Aufteilung auf Grund und Gebäude trägt die Abschreibung (S. 789–790).
- **Anschlussfinanzierung und Alternativanlage.** Reicht der Planungszeitraum über die Zinsbindung oder die Laufzeit der Alternativanlage hinaus, braucht es eine Annahme; genannt werden Durchschnitte der letzten zehn Jahre oder die Fortschreibung des bisherigen Satzes. Opportunitätskosten des Eigenkapitals sind die entgangenen Habenzinsen einer langfristigen Alternativanlage, etwa einer Bundesanleihe (S. 791). Das deckt sich mit der Projektregel, den Anschlusszins nicht still fortzuschreiben, nur insoweit, als eine ausdrückliche Annahme verlangt ist.
- **Mietausfall.** Erwartete Ausfälle aus Leerstand werden direkt von den Mieterträgen abgesetzt und nicht als pauschales Mietausfallwagnis in die Kosten genommen, weil dieses eine kalkulatorische Größe ist (S. 793).
- **Laufende Ausgaben.** Verwaltungskosten und regelmäßige Instandhaltung mit Index fortschreiben; unregelmäßige Instandsetzung und Verbesserung zum wahrscheinlichen Zeitpunkt ansetzen (S. 793).
- **Veräußerungserlös.** Fortschreibung vergangener Preisentwicklungen gilt als unzuverlässig; Alternative ist der prognostizierte Verkehrswert. Warnung, der Investor könne sich über den Restwert „reich" rechnen (S. 795) – stützt Restwertanteil und Faktorenpaar auf dem Kennzahlenblatt.
- **Steuern in den klassischen Verfahren.** Vier Varianten (Basis-, Zins-, Standardmodell, Bruttomethode; Tab. 2, S. 806); das Steuerparadoxon am Standardbeispiel (Kapitalwert −43 vor, +8 nach Steuern, S. 808–809). Eigene Nachrechnung der Kurve in Abb. 11: Nulldurchgang knapp unter 40 %, Höchstwert rund 13 bei 70 %, null bei 100 %.
- **Betriebs- und Privatvermögen** als Stellgröße der Besteuerung (S. 807–808). Die dort genannten Einzelregeln (Freibetrag bei Kreditzinsen in der Gewerbesteuer, Frist für den steuerfreien Verkauf) sind Lehrbuchvereinfachungen und keine Quelle für den Katalog; dafür gilt das Kataster. Dasselbe gilt für die mietrechtlichen Angaben auf S. 792 und die Nebenkostensätze auf S. 790.
- **Hebelwirkung.** Die VOFI-Rendite steigt im Standardbeispiel mit dem Eigenkapitaleinsatz, weil die Gesamtkapitalrendite unter dem Sollzins liegt (negativer Leverage-Effekt, S. 815). Taugt als Plausibilitätsprüfung für die Sensitivität „Eigenkapitalanteil".
- **Risiko.** Kein eigener Abschnitt; Verweis auf das Kapitel zum Risikomanagement desselben Werks und der Hinweis, dass Simulationen mit Zufallsverteilungen möglich sind (S. 821, 830).
- **DCF.** Brutto- (WACC) und Nettomethode (Flow to Equity) als Varianten der Kapitalwertmethode (S. 803) – deckt die zweite Kennzahlenwelt des Projekts begrifflich ab.

## Vorschläge

### Spezifikation und Bericht

1. **Unterlassensalternative als eigener Finanzplan mit zwei Zinssätzen** (Anlagezins für das Eigenkapital, Wiederanlagezins für die Erträge), voreingestellt beide gleich. Betrifft Spezifikation Kapitel 3 „Ausschüttungen und Nachschüsse" und Bericht A.3 Nr. 11 und 12 (Definition von q). Wirkung laut eigener Rechnung: Die Ein-Satz-Formel liegt im Standardbeispiel um 21,97 GE (ohne Steuern) und 5,24 GE (mit Steuern), im Fallbeispiel um 404,15 Tausend Euro über dem Endvermögen der Finanzinvestition.
2. **Bericht Abschnitt 3 und A.3:** Die Aussage „Das Lehrbuch lässt offen …" lässt sich für die Renditeformel jetzt am Original belegen (S. 816). Die Rendite bei mehreren Einlagen oder Entnahmen sollte in Berichten als eigene Erweiterung bezeichnet werden, nicht als Lehrbuch-VOFI-Rendite.
3. **Spezifikation Kapitel 3, „Lehrbuchkennzahlen":** Eigenkapitalrendite und Vergleich über das Endvermögen sind am Original belegt; als Quelle die neue Kennung ergänzen. Gesamtkapitalrendite und Amortisationsdauer bleiben bei `MA-028` und `MA-027`.
4. **Bericht A.1:** Tilgungsart „freie Tilgung" (Periodenüberschuss tilgt, Rest am Ende) als Lehrbuchvariante aufnehmen; sie ist im Fallbeispiel die beste (S. 821, 826). Die Zeile A.1 Nr. 1 um den Hinweis ergänzen, dass das Lehrbuch dieselbe Mechanik als einjährige Reinvestition und Zwischenfinanzierung darstellt.
5. **Lehrbuchansicht im Jahresmodus:** Zeilennamen und Blockfolge des Buchs (direkte Zahlungen, indirekte Zahlungen, Saldozeile, Nebenrechnungen) als Darstellungsvariante vormerken, damit sich Lehrbuchfälle Zeile für Zeile vergleichen lassen; dazu ein Glossar der Begriffspaare aus dem Abschnitt „Begriffe".
6. **Bericht, Belastbarkeit (Abschnitt 9) und Notiz 03:** Die Lücke „Immobilien-VOFI-Tabelle nach Schulte nicht im Original gesehen" ist geschlossen; die rekonstruierte Zeilenstruktur in Notiz 03 bleibt als Soll des Projekts gültig, weicht aber in der Darstellung vom Buch ab.
7. **`TASKS.md`:** Der Punkt „Immobilien-VOFI nach Schulte/Ropeter (Zeilenaufbau) … belegen" ist mit dieser Notiz erledigt. Neu: Grob (2015), S. 140 f. und Ropeter (1998), S. 186 ff. beschaffen, wenn `MA-012`, `MA-027` und `MA-028` am Original geklärt werden sollen.

### Modellannahmen

| Kennung | Vorschlag |
|---|---|
| `MA-012` | Status bleibt offen. Grund ergänzen: am Original bestätigt, dass die Lehrbuchformel nur eine Einlage kennt (Notiz 11, S. 816). Klärung durch: Ropeter (1998), S. 186 ff.; fachliche Freigabe durch den Auftraggeber. Quelle: neue Kennung des Kapitels. Voreinstellung unverändert; Zusatz, dass q bei zwei Zinssätzen der Alternative neu zu fassen ist |
| `MA-027` | Status bleibt offen, Voreinstellung unverändert. Bemerkung: Das Kapitel behandelt die Kennzahl nicht |
| `MA-028` | Status bleibt offen, Voreinstellung unverändert. Klärung durch: Grob (2015), S. 140 f. (Fundstelle laut Kapitel, S. 813) |
| `MA-013` | keine Änderung |
| neu | keine neue Annahme nötig: Die zwei Zinssätze der Alternative sind Eingaben, ihr Aufbau ist eine Festlegung |

### Quellenkataster

| Kennung | Titel und Fundstelle | Beleg |
|---|---|---|
| neu: `SCHULTE-IMMOBILIENINVESTITION-2025` | Schulte et al., „Immobilieninvestition", in: Schulte/Bone-Winkel/Schäfers (Hrsg.), Immobilienökonomie, De Gruyter, © 2025, S. 787–838 (Abschnitte 4 bis 6 des Kapitels), DOI 10.1515/9783111704906; Auflage und Bandzählung am PDF nicht erkennbar. Verwendet für: Zeilenaufbau des Immobilien-VOFI, VOFI-Rendite, Unterlassungsalternative, Referenzfälle | original, gelesen am 2026-11-18; vom Auftraggeber bereitgestellt, kostenpflichtig |
| `SCHULTE-IMMOBILIENOEKONOMIE-1` | Als Vorauflage (2016) kennzeichnen und auf die neue Kennung verweisen; die dort genannten Verfasser „Schulte/Allendorf/Ropeter" sind am gelesenen Kapitel nicht zu bestätigen | bleibt ungeprüft |
| `GROB-EINFUEHRUNG` | Das Kapitel zitiert die 5. Auflage mit Jahr 2015, Verlag Franz Vahlen (S. 834); der Katastereintrag nennt 2006. Fundstelle der Gesamtkapitalrentabilität laut Kapitel: S. 140 f. Auflage und Jahr prüfen | bleibt sekundär |
| `ROPETER-1998` | Fundstelle laut Kapitel (S. 836): Dissertation, in: Schulte (Hrsg.), Schriften zur Immobilienökonomie, Band 5, Verlagsgesellschaft Rudolf Müller. Verwendet für: mehrere Eigenkapitaleinsätze und Entnahmen (S. 186 ff.), genaues Steuermodell (S. 245 ff.) | bleibt ungeprüft |
| `SCHULTE-ROPETER-1996` | Im Literaturverzeichnis des Kapitels nicht enthalten; Bemerkung ergänzen, dass der Zeilenaufbau jetzt über die neue Kennung belegt ist | bleibt ungeprüft |

### Neuer Referenzfall (Bericht A.6)

| Fall | Annahmen | Referenzwerte | Toleranz |
|---|---|---|---|
| Schulte, Standardbeispiel (S. 802–820) | wie oben; vier Finanzpläne im Jahresmodus, ungerundet gerechnet | Endvermögen 10.250 / 10.188 / 9.097 / 9.046 GE; Renditen 5,08 / 4,95 / 2,60 / 2,49 %; dazu je Jahr Kreditstand, Reinvestition oder Zwischenfinanzierung und Steuerzahlung | jeder veröffentlichte Wert stimmt nach Rundung auf ganze GE; zusätzlich die eigenen Werte in voller Genauigkeit (10.249,85 / 10.188,28 / 9.096,56 / 9.046,02) auf 0,01 |
| Schulte, Fallbeispiel Bürogebäude (S. 819–830) | wie oben nach den Tabellen; drei Kreditvarianten und Finanzinvestition | Endvermögen 30.179 / 31.400 / 31.567 / 30.445 Tausend Euro; Renditen 3,27 / 3,68 / 3,74 / 3,36 % | Immobilienpläne: jeder Wert stimmt nach Rundung. Finanzinvestition: 1 Tausend Euro je Wert, weil die Quelle in sich um eine Einheit unstimmig ist. Für die freie Tilgung gilt Tab. 11, nicht Tab. 15 |

Der Fall prüft, was die bisherigen Referenzfälle nicht prüfen: getrennte kurzfristige Soll- und Habensätze, die Zwischenfinanzierung mit Zins in der Steuerbemessung, den steuerpflichtigen Verkaufsgewinn über den Buchwert, drei Tilgungsarten und die Unterlassungsalternative mit zwei Zinssätzen. Vor dem Festschreiben ist zu prüfen, ob die Rundungsregeln des Projekts (Bericht A.2 Nr. 10) die gerundeten Buchwerte erhalten. Im Skriptordner fehlt in `LIESMICH.md` noch die Zeile zu `schulte_musterrechnung.py`.

## Nicht gelesen, nicht geklärt

- Die Abschnitte 1 bis 3 des Kapitels und Titelei oder Impressum des Werks liegen nicht vor; Auflage, Bandzählung und Mitverfasser sind deshalb offen.
- Rechenregel der Amortisationsdauer, Abgrenzung der Sollzinsen in der Gesamtkapitalrentabilität und eine Renditeformel für mehrere Einlagen und Entnahmen stehen nicht im Kapitel.
- Unterjährige Zahlungen, Indexierung, Verkaufskosten, Verlustvortrag, Förderdarlehen und Zuschüsse kommen im Kapitel nicht vor.
- Abb. 11 und 12 sind nur als Diagramme vorhanden; ihre Werte sind abgelesen und keine Prüfpunkte.
- Alle Textseiten und Tabellen waren lesbar.
