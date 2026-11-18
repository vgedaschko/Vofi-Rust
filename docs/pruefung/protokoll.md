# Prüfprotokoll

Eine Zeile je Prüfrunde; Details darunter. Stand: Datum der letzten Zeile. Leser: Entwicklung vor jeder Prüfrunde. Maßstab und Format der Prüfer stehen in [`regeln.md`](regeln.md), Berichte und Sichtung je Runde im Ordner der Runde.

| Datum | Prüfobjekt | Rollen | Befunde (kritisch / wichtig / Hinweis) | Ergebnis |
|---|---|---|---|---|
| 2026-11-17 | Recherchebericht, erste Fassung | Fachexperte, Finanzmathematiker, Praktiker, Investor, Jurist, Einheitsbrei-Prüfer; Lotse ohne Note | 9 / 39 / 10 | Noten 5 bis 7; erste Überarbeitung · [Runde 1](2026-11-17-recherchebericht/sichtung.md) |
| 2026-11-18 | Recherchebericht, nach erster Überarbeitung | dieselben sechs | 2 / 29 / 25 | Noten 7 bis 8; zweite Überarbeitung · [Runde 2](2026-11-18-recherchebericht-runde2/sichtung.md) |
| 2026-11-18 | Recherchebericht, nach zweiter Überarbeitung | dieselben sechs | 1 / 17 / 33 | Noten 8 bis 9; dritte Überarbeitung · [Runde 3](2026-11-18-recherchebericht-runde3/sichtung.md) |
| 2026-11-18 | Recherchebericht, nach dritter Überarbeitung | vier Rollen voll; Finanzmathematiker und Jurist nur die Änderungen | 0 / 16 / 30 | Noten 8 bis 9; vierte Überarbeitung, danach gezielte Nachprüfung · [Runde 4](2026-11-18-recherchebericht-runde4/sichtung.md) |
| 2026-11-18 | Recherchebericht, nach vierter Überarbeitung | alle sechs, nur die geänderten Stellen | 0 / 12 / 28 | Noten 8 bis 9 (fünfmal 9); abgenommen nach Schlussredaktion ohne weitere Runde · [Runde 5](2026-11-18-recherchebericht-runde5/sichtung.md) |
| 2026-11-18 | Steuerungsdokumente (Spezifikation, Plan, Entscheidungsprotokoll, Arbeitsregeln, Hooks, Rollen) | Dokumentation | 0 / 7 / 3 | Note 7; Befunde behoben · [Sichtung](2026-11-18-steuerungsdokumente/sichtung.md) |
| 2026-11-18 | Steuerungsdokumente, Nachprüfung | Dokumentation | 0 / 4 / 3 | Note 8; Befunde behoben, nicht erneut nachgeprüft · [Sichtung](2026-11-18-steuerungsdokumente/sichtung.md) |
| 2026-11-18 | Fachspezifikation des Rechenkerns, Teil 1, Entwurf mit Referenzrechner | Finanzmathematiker, Fachexperte, Praktiker, Steuerberater, Bank, Controller, Grenzfälle | 7 / 43 / 20 | Noten 7 bis 8; erste Überarbeitung · [Runde 1](2026-11-18-fachspezifikation-rechenkern/sichtung.md) |

## Noten je Rolle (Recherchebericht)

| Rolle | Runde 1 | Runde 2 | Runde 3 | Runde 4 | Runde 5 |
|---|---|---|---|---|---|
| Finanzmathematiker | 7 | 8 | 9 | 9 | 9 |
| Jurist | 6 | 7 | 9 | 9 | 9 |
| Fachexperte | 6 | 8 | 8 | 8 | 9 |
| Einheitsbrei-Prüfer | 7 | 8 | 8 | 8 | 9 |
| Investor | 5 | 7 | 8 | 8 | 8 |
| Praktiker | 5 | 7 | 8 | 8 | 9 |

## Was die Runden verändert haben

- **Runde 1:** Rechts- und Förderstand am Original nachgezogen (NBank-Richtlinie 2026, Mietrecht, Steuerrecht); Wirtschaftlichkeit des Eigenbaus als offene Frage mit Vorstudie statt als Annahme; Zuschnitt in Stufen mit Freigabepunkten.
- **Runde 2:** Vorprüfung als erster Freigabepunkt; Grobkalkulation als eigener erster Teilschritt; Rechenkonventionen mit nachgerechneten Referenzfällen.
- **Runde 3:** Grobkalkulation mit Steuer in Kurzform und Finanzierungsgrenze; vier Teilschritte; Restwertregel ohne Doppelzählung; Verzeichnis der Modellannahmen auf 25 Einträge.
- **Runde 4:** Regel für den höchsten tragbaren Preis neu gefasst (die Bank begrenzt das Darlehen, nicht den Preis); geförderter Neubau als Restfinanzierung; Zinsbindung und Anschlusszins in der Grobkalkulation; Bedarfsschwelle zweigeteilt; offene Aufträge nur noch in `TASKS.md`.
- **Runde 5:** Restfinanzierung für alle Fälle, Bezug von Beleihungsquote und Mindestdeckung, Freibetrag der Gewerbesteuer, Schutz der Finanzierungsvorgaben gegen Schönrechnen, vier Maßstäbe der Vorprüfung; Gesamtkapitalrendite und Amortisationsdauer geklärt oder als Annahme gefasst.

## Wiederkehrendes Muster

In jeder Runde lagen die neuen Befunde an den Nahtstellen der vorigen Überarbeitung: Eine Regel wurde an einer Stelle geändert und an zwei anderen nicht, oder ein neuer Baustein bekam im ersten Teilschritt keine Rechengrundlage. Für die Fachspezifikation folgt daraus: jede Regel an einem Ort, Verweise statt Wiederholung, und nach jeder Änderung eine Suche nach dem alten Wortlaut.
