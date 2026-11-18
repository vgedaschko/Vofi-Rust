---
description: Arbeitsergebnis von mehreren Prüfern (Fachexperte, Finanzmathematiker, Praktiker, Kunde, Controller, Investor …) gegenlesen lassen und Befunde einarbeiten
---

Führe eine Prüfrunde durch. Prüfobjekt: $ARGUMENTS
(Ohne Angabe: das jüngste Arbeitsergebnis, das laut `docs/pruefung/protokoll.md` noch nicht geprüft wurde.)

1. **Prüfer auswählen.** Nimm nur Rollen, die zum Prüfobjekt etwas beitragen können – meist drei bis sechs, nie alle aus Prinzip. Die Rollen stehen in `.claude/agents/pruefer-*.md`.

   | Prüfobjekt | Üblicherweise |
   |---|---|
   | Recherche, Bericht, Dokumentation | fachexperte, finanzmathematiker (wenn Zahlen), investor, slop |
   | Fachkonzept, Rechenmodell | fachexperte, finanzmathematiker, steuerberater, jurist, foerdermittel, controller, grenzfaelle |
   | Architektur, Datenmodell | architekt, revision, controller |
   | Oberfläche, Eingabemasken | praktiker, endnutzer, slop, controller |
   | Kundenbericht, Export | endnutzer, investor, bank, jurist, slop |
   | Rechencode | finanzmathematiker, grenzfaelle, architekt |
   | Anmeldung, Rechte, Kundenzugang | revision, architekt, jurist |

   Auf Zuruf und an Meilensteinen zusätzlich: **lotse** – der Blick von der Brücke. Er hält eine Rede statt einer Befundliste; verwertbar ist sein Schlusssatz.

   Fehlt für eine spezielle Frage eine passende Rolle, lege einen neuen Prüfer nach dem Muster der vorhandenen an.

2. **Parallel starten.** Modell: das neueste Opus (in den Rollendateien voreingestellt); Fable nur, wenn das Prüfobjekt komplex oder folgenreich ist (Rechenkern, Steuer- und Rechtslogik, Sicherheitsarchitektur). Jeder Prüfer bekommt den Pfad des Prüfobjekts und, falls nötig, die konkrete Frage – nicht deine eigene Einschätzung, sonst bestätigt er sie nur. Sind die Agententypen nicht registriert, starte einen allgemeinen Agenten mit dem Auftrag, zuerst die jeweilige Datei `.claude/agents/pruefer-<rolle>.md` zu lesen und in dieser Rolle zu prüfen.

3. **Befunde sichten – nicht ungeprüft übernehmen.** Doppelte zusammenführen. Jeden Befund mit Schweregrad „kritisch" oder „wichtig" selbst an der Fundstelle nachprüfen: Prüfer irren sich auch. Dann entscheiden: übernehmen · ablehnen (mit Grund) · Rückfrage an den Auftraggeber (nur fachlich/betriebswirtschaftlich).

4. **Einarbeiten.** Übernommene Befunde direkt im Prüfobjekt beheben; was nicht sofort geht, als Aufgabe in `TASKS.md`. Berührt ein Befund eine Festlegung, zuerst `docs/spezifikation.md` anpassen und die Änderung in `docs/entscheidungen.md` eintragen.

5. **Protokollieren** in `docs/pruefung/protokoll.md`: Datum, Prüfobjekt, eingesetzte Rollen, Note je Rolle, Zahl der Befunde je Schweregrad, was übernommen und was mit welchem Grund abgelehnt wurde. Widersprechen sich zwei Rollen, den Zielkonflikt benennen statt ihn stillschweigend zu entscheiden.

6. **Wiederholen bis 9 von 10.** Nach dem Einarbeiten prüfen die Rollen erneut, die unter 9 lagen; in der letzten Runde liest zusätzlich der Einheitsbrei-Prüfer, ob die Korrekturen den Text verschlechtert haben. Jeder Prüfer bekommt in der Folgerunde seinen eigenen vorigen Bericht und die Sichtung, damit er prüft, ob seine Befunde behoben sind, statt von vorn zu beginnen – und er sucht trotzdem nach Neuem.

   Die Schleife endet, wenn
   - alle beteiligten Rollen mindestens 9 geben, oder
   - die niedrigste Note in zwei aufeinanderfolgenden Runden nicht steigt, oder
   - die verbleibenden Befunde außerhalb des Prüfobjekts liegen (fehlende Angaben des Auftraggebers, Auskünfte Dritter, Entscheidungen einer späteren Phase), oder
   - fünf Runden erreicht sind.

   In den letzten drei Fällen dem Auftraggeber berichten: erreichte Noten, was zur 9 fehlt und wer es liefern kann. Eine 9 wird nicht herbeigeredet – weder durch weichere Prüfaufträge noch durch Streichen unbequemer Befunde.

7. **Prüfauftrag sauber fassen.** Jeder Prüfer erfährt, was das Prüfobjekt leisten soll und was ausdrücklich nicht (zum Beispiel: Recherchebericht, keine Wirtschaftlichkeitsrechnung). Bewertet wird gegen diesen Zweck; dass ein anderes Dokument fehlt, ist ein Hinweis an den Auftraggeber, kein Abzug am Prüfobjekt.
