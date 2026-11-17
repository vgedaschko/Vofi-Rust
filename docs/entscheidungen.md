# VOFI-Projekt – festgelegte Rahmenbedingungen

Stand 2026-11-17, aus dem Fragenkatalog mit dem Auftraggeber.

| Thema | Entscheidung |
|---|---|
| Nutzerkreis | Internes Werkzeug **und** Beratung für Kunden (Berichte, ggf. Lesezugang) – kein SaaS-Verkauf |
| Vorhabensarten | Ankauf Bestand · Neubau zur Vermietung · Sanierung im Bestand · Entwicklung mit Verkauf |
| Nutzungsarten | Frei finanziertes Wohnen · geförderter Wohnungsbau · Gewerbe/Mixed-Use · Sonderimmobilien |
| Steuersichten | Kapitalgesellschaft · Privatperson/Personengesellschaft · steuerbefreit/kommunal |
| Mehrbenutzer | Echte Co-Editierung (gleichzeitiges Bearbeiten, Präsenz), Projektzuweisung an Mitarbeiter |
| Technik | Rust für Rechenkern und Server; Oberfläche in TypeScript, Rechenkern zusätzlich als WebAssembly im Browser |
| Fachliche Referenz | Keine eigene Excel-Vorlage; Lehrbuch-Standard (Grob, Schulte/Ropeter) und Branchenrichtlinien (gif) |
| Fördermodule | KfW, NBank und weitere – als konfigurierbare Daten, nicht fest verdrahtet |
| Repository | `vgedaschko/Vofi-Rust`; die älteren Repos `VoFi` und `NBank` sind überholt und werden nicht herangezogen |
| Zusammenarbeit | Auftraggeber ist Betriebswirt, kein Programmierer: technische Entscheidungen trifft Claude und begründet sie in Geschäftssprache (Kosten, Risiko, Nutzen); Rückfragen nur zu fachlichen und betriebswirtschaftlichen Themen |
