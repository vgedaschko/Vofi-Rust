# Sichtung – Prüfung der Steuerungsdokumente (2026-11-18)

Prüfobjekt: Spezifikation, Entwicklungsplan, Entscheidungsprotokoll, `CLAUDE.md`, `TASKS.md`, Übersichten, Befehle, Rollen und Hooks. Rolle: Dokumentation. Berichte: `dokumentation.md` (Note 7) und `dokumentation-nachpruefung.md` (Note 8).

## Erste Prüfung: zehn Befunde, alle am Bestand bestätigt

| Nr. | Befund | Behoben durch |
|---|---|---|
| 1 | Entscheidungsprotokoll: neue Einträge unten | Einträge oben; Ablösevermerke an den alten Einträgen |
| 2 | Offene Punkte doppelt in Spezifikation Kapitel 9 und `TASKS.md` | Kapitel 9 verweist auf `TASKS.md` |
| 3 | Kennungen von Modellannahmen fehlen in der Spezifikation | nachgetragen; Prüfmodus gleicht die Gegenrichtung ab |
| 4 | Quellenkennungen in Texten ungeprüft, `ESTG-35` fehlte | Prüfmodus gleicht Kennungen in Backticks ab; Einträge nachgetragen |
| 5 | Wirkung des Gestaltungs-Hooks zu stark beschrieben | überall: hält den Stopp einmal auf |
| 6 | Feste Zahl der Annahmen im Plan | Zahl entfernt, Verweis auf das Verzeichnis |
| 7 | Werkzeugübersicht veraltet | aktualisiert und geordnet |
| 8 | Auslöser der zeitgesteuerten Prüfungen uneinheitlich | ein Auslöser; Zeile für jährliche Quellen |
| 9 | Rolle Steuerberater prüft je Investorentyp | prüft je Steuerstatus |
| 10 | Kopfzeilen, Verweis auf Gestaltungsreferenzen, Lotse | nachgetragen |

## Nachprüfung: sieben neue Befunde

| Nr. | Befund | Behoben durch |
|---|---|---|
| N1 | Ablösevermerke fehlen an drei Einträgen; ein „Ersetzt“ verweist ins Leere | Vermerke gesetzt; Verweis berichtigt |
| N2 | Plan nennt noch Beschaffung der Lehrbücher und neun Quellnotizen; `CLAUDE.md` den alten Beschaffungsweg | berichtigt |
| N3 | Plan verspricht mehr, als die Skripte prüfen; neue Vorsilben fallen durch | Kennungsprüfung ohne Vorsilbenfilter; Plan nennt die Grenzen (Wirkort in der Zeile und Angaben ohne Backticks prüft die Rolle Dokumentation); Wirkorte im Verzeichnis berichtigt; zwei Kennungen nachgetragen |
| N4 | Protokollzeile und Sichtung fehlen; `TASKS.md` meldet zu viel als behoben | Protokollzeilen, diese Sichtung, Eintrag berichtigt |
| N5 | Ohne git-Arbeitskopie fällt der Abgleich still aus | Skript durchsucht dann das Verzeichnis; erprobt |
| N6 | Skill `steuer-regeln` „je Investorentyp“ | „je Steuerstatus“ |
| N7 | `TASKS.md` ohne Stand und Leser | Kopfzeile ergänzt |

Die Behebung der Befunde N1 bis N7 ist nicht erneut nachgeprüft; die nächste Prüfung der Dokumentation ist am ersten Freigabepunkt fällig (Entwicklungsplan, Prüfplan).
