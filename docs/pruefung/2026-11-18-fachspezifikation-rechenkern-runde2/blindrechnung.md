# Blindrechnung zur Fachspezifikation Rechenkern (Prüfrunde 2)

**Stand:** 2026-11-18 · in Arbeit, wird fortlaufend ergänzt
**Quelle:** allein `docs/fachspezifikation-rechenkern.md`; der Referenzrechner, `erwartete_werte.json` und die Prüfberichte wurden nicht gelesen.
**Code:** eigener Nachbau in Python (`decimal`, nur Standardbibliothek), abgelegt im Scratchpad `fs2-blind/` (`kern.py` und je Fall ein Skript).

## Zwischenstand

- RF-11 Ankauf Basisfall, Stressfall, Haltedauertabelle, höchster tragbarer Preis (Rendite- und Eigenkapitalgrenze, Basis und Stress): alle geprüften Sollwerte auf den Cent getroffen.
- RF-12 Neubau frei finanziert (Basis und Stress) und gefördert (38, 20, 36 bis 39 Jahre): alle geprüften Sollwerte getroffen; mehrere Stellen brauchten eine geratene Lesart (siehe Schlussfassung).
- offen: KfW-Tranche, Preissuche Neubau, RF-13, gebundener Bestand, RF-06.
