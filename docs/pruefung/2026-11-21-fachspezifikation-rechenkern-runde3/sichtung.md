# Sichtung der Prüfrunde 3 – Fachspezifikation des Rechenkerns, Teil 1 (2026-11-21)

Prüfobjekt: `docs/fachspezifikation-rechenkern.md` nach der zweiten Überarbeitung, der Durchsicht an der Wesentlichkeitsschwelle und dem Nachtrag aus den Steuerrichtlinien (eingefroren; 20 Referenzfälle, 1.093 Prüfungen). Auftrag der Runde: Fehler und Reststellen suchen; weitere Sonderfälle nur mit bezifferter Wirkung über der Schwelle.

Noten (Runde 2 → 3): Finanzmathematiker 8 → **9** · Fachexperte 8 → **8** · Praktiker 8 → **8** · Steuerberater 8 → **8** · Bank 8 → **8** · Controller 8 → **8** · Grenzfälle 8 → **8**. Dazu die Blindrechnung ohne Note (Abschnitt am Ende).

Gesamtbild: Die Rechnung trägt. Der Finanzmathematiker hat rund 420 Werte mit eigenem Code nachgebaut und 416 getroffen (die vier Abweichungen sind falsche Zahlen im Text, nicht im Rechner); der Steuerberater trifft alle Stichproben auf den Cent; die Rolle Grenzfälle findet in über 2.300 Läufen keinen Absturz der neuen Regeln. Fast alle Befunde der Runde 2 sind behoben. Dass sechs Rollen bei 8 bleiben, hat einen gemeinsamen Grund: Nach der Durchsicht wurde der Text nicht von vorn bis hinten gegengelesen, und fünf Rollen finden dieselben Reste (entfallene Kennungen, alte Zahlen, H-25 „je Tranchenart“). Dazu kommen ein kritischer Fehler im Rechner (Zielwertsuche), drei Regelfehler und vier Punkte über der Schwelle. Kein Befund verlangt Zuarbeit von außen.

## Nachgeprüft

- **Von mehreren Rollen unabhängig gefunden:** H-25 steht im Text noch je Tranchenart, das Beispiel nennt 826.660,00 statt 964.436,66 Euro, und V-06 („deckungsgleich auf den Cent“) stimmt nur, wenn jede fremde Tranche über den ganzen Bemessungszeitraum fest ist (Fachexperte 3, Bank 3, Praktiker 2, Finanzmathematiker 4, Controller). Verweise auf die entfallene Regel R-6.17 und auf H-36, E-52 (alle sieben Rollen).
- **Mit eigener Rechnung belegt:** Zielwertsuche und Begründungspflicht (Grenzfälle 1, Läufe im Skriptordner); Proben P-03 und P-04 (b) ohne Bereitstellungsprovision (Finanzmathematiker 1); Kürzung eines negativen Grundstücksteils (Steuerberater 1); Zusage im Vorlauf (Bank 1); umgehbare Abweichungsliste (Controller 1).
- **Gelesen in dieser Runde:** BFH III R 1/23 am Original (Steuerberater); Gesetzes- und Richtlinientexte in Verlagswiedergabe, weil `gesetze-im-internet.de` am 21.11. zeitweise nicht erreichbar war. Liste am Ende des Steuerberater-Berichts; neu vorgeschlagen `GEWSTG-14`.
- **Skripte** aller Rollen liegen unter `research_notes/…/skripte/pruefrunde-fachspezifikation-3/`.

## Übernommen (Berichtigung vor der Abnahme)

### A. Fehler im Rechner und in Regeln

1. **Zielwertsuche und Haltedauertabelle (kritisch; Grenzfälle 1).** Die Begründungspflicht wird einmal am Ausgangsauftrag geprüft (R-11.1, R-11.9), nicht an jedem Gitterwert; die Haltedauertabelle prüft sie wie jeder andere Lauf. Rechner berichtigen, Fall als Sollwert aufnehmen.
2. **Scheinlösungen der Zielwertsuche (Grenzfälle 2).** Der Übergang von einem unzulässigen zu einem zulässigen Wert ist keine Lösung; R-11.10 ändern, eigene Meldung „Rand des zulässigen Bereichs“.
3. **Bereichsprüfung für Katalogwerte (Grenzfälle 3).** R-3.7 gilt auch für Katalog- und feste Werte: jeder Wert mit zulässigem Bereich; Rückzahlungsfrist und Bindungsdauer größer null. Die Fälle mit negativer Rate und der Absturz bei Bindung null enden mit M-47.
4. **Abweichungsliste nicht umgehbar (Controller 1).** Der Kern löst Voreinstellungen, Hauswerte und Katalogwerte selbst auf; der Auftrag trägt nur Eingaben und Abweichungen. Fehlt ein Wert, den der Lauf braucht, endet er mit M-47 – nie mit einem stillen Ersatzwert. R-3.2, R-3.4 und R-3.7 widerspruchsfrei fassen.
5. **Erweiterte Kürzung nur bei positivem Grundstücksteil (Steuerberater 1).** Die Kürzung gibt es auf Antrag je Jahr; in Verlustjahren wird sie nicht beantragt, der Verlust bleibt vortragsfähig. Wirkung +0,03 bis +0,11 Prozentpunkte; kostet kein Feld. Sollwerte der Fälle mit Kennzeichen ändern sich.
6. **Zeitpunkt der Kreditzusage im Neubau mit Vorlauf (Bank 1).** Zusage im Monat vor dem ersten Abruf des jeweiligen Darlehens, beim KfW-Darlehen im Monat vor Baubeginn – stimmig mit NF-65. Bereitstellungszins, Abruffristen und Zinsbindung laufen nicht mehr ab dem Grundstückskauf. Wirkung im Fall mit zwölf Monaten Vorlauf 1,30 % der Gesamtkosten und 0,129 Prozentpunkte, also über der Schwelle.
7. **Proben P-03 und P-04 (b)** um die Bereitstellungsprovision ergänzen (Finanzmathematiker 1).
8. **Rechner und Text angleichen (Grenzfälle, Controller 5):** H-35 einheitlich; E-69 ohne E-41 wird abgelehnt; Änderung von H-38 oder der Lesart `MA-036` im Vorhaben endet mit M-20; Obergrenze unter Untergrenze der Preissuche endet mit M-31.

### B. Über der Schwelle – ohne oder mit einem freiwilligen Feld

9. **Mietpfad im Neubau (Fachexperte 1).** Die Vergleichsmiete im Neubau ist E-65 mal Mietindex (bisher stillschweigend die Erstvermietungsmiete). E-65 heißt künftig „Vergleichsmiete und nachhaltige Miete bei Bezug“ und dient der Bank wie dem Mietpfad; voreingestellt bleibt E-16, die Sollwerte der Basisfälle ändern sich nicht. Die Voreinstellung „Neubaumiete liegt auf Vergleichsmietenniveau“ wird Modellannahme `MA-042` (Gewicht hoch; Wirkung bei 5 % Abstand rund 7 % der Gesamtkosten). Keine neue Eingabe.
10. **Instandhaltung modernisierter Bestände (Praktiker 1).** Neues freiwilliges Feld „Jahr der durchgreifenden Modernisierung“: bestimmt nur die Stufe der Instandhaltung, nicht die Abschreibung; erscheint in der Abweichungsliste. Wirkung +2,7 % Preis, +0,34 Prozentpunkte – besteht die Schwelle. Dazu ein Satz, was die Staffel H-17 umfasst (Fachexperte 7).
11. **Zwischenfinanzierung der Teilraten als Modellannahme (Bank 2).** `MA-043`: Die Lücke bis zur nächsten Teilrate lässt sich über das Kontokorrent finanzieren, auch wenn die Bank kein Darlehen gibt; andere Lesart: Eigenkapital überbrückt. Frage 6 an die Hausbank ergänzen; die Frage liegt auch beim Auftraggeber.
12. **E-69 um die Einstellung des Betriebs erweitern (Steuerberater 2).** Wird die gewerblich geprägte Gesellschaft mit dem Verkauf eingestellt, endet der Erhebungszeitraum mit dem Verkauf, und die Kürzung bleibt. Begründete Einschätzung, nicht am Text belegt: E-69 und M-51 nennen den Fall, Frage 3 an den Steuerberater wird ergänzt. Kein neues Feld.
13. **Stressfall beim eingegebenen Preis (Praktiker 3, erster Teil).** Ist ein Preis eingegeben, zeigt das Blatt Rendite, Endwertdifferenz und kleinste Deckung des Stressfalls bei diesem Preis. Kostet keine Eingabe.
14. **Stand von Hauswerten und Katalog auf dem Blatt (Controller 4).** Fassung und Datum beider Kataloge stehen im Ergebnis; ebenso, welche Lesarten des Hauses gelten.

### C. Klassen der festen Werte

15. **„Feste Katalogwerte“ ohne Rechtsquelle (Controller 3, Fachexperte 8).** Katalogwert heißt nur, was aus einer Quelle des Katasters stammt. Die übrigen (unter anderem H-10, H-23, H-27, H-37, bereitstellungsfreie Zeit) werden **feste Modellwerte**: eine Tabelle mit Wert, Begründung und gemessener Wirkung; die Geschäftsführung gibt die Liste als Ganzes mit dem Freigabeblatt frei, nicht jeden Wert einzeln. Verantwortlich für die Pflege ist die Katalogverantwortung.

### D. Zahlen, Reststellen, Nachweise

16. **Falsche Zahlen im Text:** R-10.9 (Endwertüberschuss im Stress −716.938,74 Euro), R-11.11 (Differenz −10.735.928,53 Euro), R-11.12 („35 Größen“, „Begründungen“), R-5.12 und Anhang A.4 (964.436,66 Euro; H-25 als ein Wert), Anhang A.3 (Hebesatz), Zählregel in R-3.6.
17. **V-06 ehrlich fassen:** deckungsgleich nur bei durchgehend festen fremden Tranchen; sonst bis rund 0,6 % Preis. **V-12** mit der gemessenen Zahl (−0,83 % / −0,103 Prozentpunkte für die weiteren Vermieterkosten, nur bei Heizungen im Sinn von § 5a). **V-17** mit dem Sonderfall Verkauf vor Bindungsende. **V-03, V-14, V-17:** Begründung „kein typischer Fall“ in die Liste. Neubauzeilen der Liste zusätzlich als Anteil am Grundstücksgebot. Neu **V-23** (einfache Kürzung um die Grundsteuer) und ein Satz zu § 8 Abs. 10 KStG bei Verein und Stiftung.
18. **Vollständiges Gegenlesen** des Dokuments und Abgleich aller Kennungen (E, H, KAT, M, P, V, NF, MA, R) zwischen Definition und Verwendung mit den Skripten des Controllers: R-6.17, H-36, E-52, NF-07, NF-15, „Lesart (1)/(2)“, „drei Lesarten“, R-7.11, R-11.9, Liste „Was Teil 2 regelt“, Kataster-Verweis `CO2KOSTAUFG-5A`, M-34 am Beispiel E-65, NF-65 (Begründung gegen die Richtlinie).
19. **Verzeichnis der Modellannahmen:** `MA-026`, `MA-031`, `MA-032`, `MA-034`, `MA-036` auf den Stand der Durchsicht; `umschaltbar` nur noch dort, wo es eine Lesart des Hauses gibt.
20. **Nachweise:** Ursachen der Sollwertänderungen je Wert statt je Gruppe (Controller 2); Zahlen im Text ohne Sollwert wieder festschreiben (Finanzmathematiker 6); `beispielwerte.py` ohne fest eingetragene Altzahlen; Vergleich zweier Fassungen um die fehlenden Teile des Blatts ergänzen.
21. **Schwelle im Neubau** (1 % der Gesamtkosten) in der Spezifikation selbst festhalten, nicht nur in der Durchsicht (Finanzmathematiker 7); Zeile „Vollständigkeit je Vorhabensart“ der Spezifikation unter den Vorbehalt der Wesentlichkeit stellen (Fachexperte 2).

## Nicht übernommen oder verschoben

- **Wirkung jeder einzelnen Stressgröße auf den tragbaren Preis** (Praktiker 3, zweiter Teil): acht zusätzliche Preissuchen je Lauf; steht für die Vollkalkulation in der Liste „Was Teil 2 regelt“.
- **Haltedauer im geförderten Bau** am Tiefpunkt der Rendite (Praktiker): bleibt Frage an den Auftraggeber.
- **Ladenmiete unter „sonstige Erträge“** (Praktiker): Feldhilfe, wird mit der Maske umgesetzt (Vormerkung).
- **Rollen und Rechte** für Vorgaben, Hauswerte und Lesarten (Controller, Runde 2 Nr. 2): Spezifikation Kapitel 5 mit dem Architekturentwurf.
- **Katalogwerte KAT-01 und KAT-08 für Bremen, Hamburg, Schleswig-Holstein und Nordrhein-Westfalen:** aus Quellnotiz 14 mit Belegstufe in den Katalog übernehmen – in derselben Berichtigung, weil die Abnahme von 1a daran hängt.
- **Zielrendite für geförderte Vorhaben:** Freigabeblatt.

## Blindrechnung

Ein zweiter Bearbeiter hat die Regeln allein aus dem Text nachgebaut (ohne Referenzrechner, Sollwertdatei und Prüfberichte): **951 Sollwerte nachgerechnet, 946 getroffen, 5 abweichend.** Urteil: Nach dem heutigen Text lässt sich ohne Rückfrage programmieren; an keiner ergebniswirksamen Stelle musste der Sollwert die Lesart entscheiden. Die sieben Lücken der Runde 2 sind geschlossen. Zwei der fünf Abweichungen decken sich mit dem Finanzmathematiker (R-10.9 und R-11.11: zwei unabhängige Rechnungen ergeben −716.938,74 und −10.735.928,53 Euro); der Text ist falsch, nicht die Rechnung.

Übernommen:

22. **Die fünf Abweichungen berichtigen:** R-10.9; R-11.11 (am Referenzrechner mit den drei Werten der Blindrechnung für „frei, 38 Jahre“ klären: Endwert 25.525.695,66, Alternative 9.133.557,41, Endwertdifferenz 16.392.138,25 Euro); R-5.12 Rohertrag des gebundenen Bestands (123.868,80 Euro); R-11.5 Steigung aus ungerundeten Renditen; R-5.19 Schreibweise.
23. **R-10.14 Nr. 4:** Endet eine Zinsbindung mitten im Planjahr, zählt das erste **volle** Planjahr danach (vorsichtiger; im geförderten Neubau 1,6943 statt 1,8848). Sollwert ändern.
24. **R-11.8 mit R-5.8:** Ein nicht überschriebener Anschlusszins eines übernommenen Darlehens ist eine Voreinstellung und steigt im Stressfall wie der des Bankdarlehens; ein eingegebener bleibt. Sollwert für den gebundenen Bestand aufnehmen.
25. **Formulierungen:** R-10.16 („Steuer ohne Verkaufsgewinn“ mit Kennzeichen E-41), R-5.12 (Abrundungsrichtung bei negativem B), RF-09 (ungerundeter Kapitaldienst), R-12.7 („Jahresmieten“ sind Mieteinzahlungen), R-12.4 (`runde12` am Dezimalwert); alte neben neuer Formulierung in R-12.5 und R-6.10/R-6.16.
26. **Reste entfallener Kennungen** aus der Tabelle des Berichts – geht in Punkt 18 auf.

Der Code der Blindrechnung liegt unter `research_notes/…/skripte/blindrechnung-fachspezifikation/` (`python3 blindwerte.py`, rund 20 Sekunden) und bleibt als zweite Umsetzung im Projekt.

## Wie es weitergeht

Berichtigung durch den Bearbeiter der Überarbeitung (kein neuer Regelumfang über die Punkte oben hinaus), Lauf der Referenzfälle, danach Nachprüfung durch die Rollen mit offenen Punkten. Abnahme bei mindestens 9 in jeder Rolle oder wenn feststeht, warum eine Rolle sie nicht erreicht.
