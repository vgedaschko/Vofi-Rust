# Skripte aus Recherche und Prüfung

Aus der Sitzung gesichert, damit die Rechnungen nachvollziehbar bleiben. Kein Produktcode.

- `finanzmathematik-pruefung/` – unabhängige Gegenrechnung des Testfalls S1 und der Varianten aus Notiz 09 (Python).
- `monte-carlo-benchmark/` – Messprogramm aus Notiz 05: Durchsatz nativ gegenüber WebAssembly und Ergebnisgleichheit (Rust).
- `runde4/`, `runde5/` – Gegenrechnungen der Prüfrunden 4 und 5 und Belege für die Zahlen der Überarbeitungen (Python).
- `bewirtschaftungskosten_index.py` – Fortschreibung der Bewirtschaftungskosten nach Anlage 3 ImmoWertV aus dem Verbraucherpreisindex (Notiz 10).
- `schulte_musterrechnung.py` – Nachbau der beiden Musterrechnungen aus dem Lehrbuchkapitel (Notiz 11); vergleicht mit den Buchwerten und endet mit Rückgabewert 1, solange die drei bekannten Abweichungen um je eine Einheit bestehen.
- `referenzrechner/` – Referenzrechner zur Fachspezifikation des Rechenkerns (`docs/fachspezifikation-rechenkern.md`): setzt deren Regeln um und rechnet alle Referenzfälle (`python3 referenzfaelle.py`, rund 75 Sekunden); eigene `LIESMICH.md` im Ordner.
- `pruefrunde-fachspezifikation-1/` – Gegenrechnungen der Prüfer aus der ersten Prüfrunde zur Fachspezifikation.
