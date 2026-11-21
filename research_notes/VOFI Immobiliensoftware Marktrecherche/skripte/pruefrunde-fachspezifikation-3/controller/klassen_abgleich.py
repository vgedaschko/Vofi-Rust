"""Pruefrunde 3, Controller: Klassen der Vorgaben im Dokument (R-3.4) gegen den Referenzrechner;
Zahl der Blattgroessen im Vergleich (R-11.11, R-11.12)."""
import sys, re, os
from dataclasses import fields
R = "/home/user/vofi-rust/research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner"
sys.path.insert(0, R)
import grobkalkulation as g
fs = open("/home/user/vofi-rust/docs/fachspezifikation-rechenkern.md", encoding="utf-8").read()
doc = {}
for k, klasse in re.findall(r"^\| (H-\d\d) \|[^|]*\|[^|]*\|[^|]*\| ([^|]*) \|$", fs, re.M):
    doc[k] = klasse.strip()
def dk(k):
    c = doc.get(k, "?")
    if c.startswith("Vorgabe"): return "Vorgabe"
    if "Hauswert" in c and "Katalogwert" in c: return "gemischt"
    if c.startswith("fester Hauswert"): return "Hauswert"
    if c.startswith("fester Katalogwert"): return "Katalogwert"
    return c
code = {}
for feld, k in g.KENNUNG_VORGABE.items(): code.setdefault(k, set()).add("Vorgabe")
for feld, k in g.FESTE_HAUSWERTE.items():
    if k.startswith("H-"): code.setdefault(k, set()).add("Hauswert")
for feld, k in g.FESTE_KATALOGWERTE.items(): code.setdefault(k, set()).add("Katalogwert")
code.setdefault("H-38", set()).add("Hauswert")
for feld, k in g.KENNUNG_EINGABE.items(): pass
vg_felder = [f.name for f in fields(g.Vorgaben)]
print("Kennung | Dokument | Referenzrechner")
for k in sorted(doc):
    c = "/".join(sorted(code.get(k, {"-- (kein Feld der Klasse Vorgaben)"})))
    d_ = dk(k)
    flag = "" if (d_ == c or (d_ == "gemischt" and c == "Hauswert/Katalogwert") or d_ == "–") else "   <== ABWEICHUNG"
    print(f"{k} | {d_:<12} | {c}{flag}")
print("\nFelder der Klasse Vorgaben:", len(vg_felder), "davon Lesarten (ma0..):", sum(1 for f in vg_felder if f.startswith('ma0')))
print("Blattgroessen je Spalte:", len(g.BLATTGROESSEN), "; Preisgroessen:", len(g.PREISGROESSEN),
      "; Zeilen bei Basis+Stress+2 Preisen:", 2*len(g.BLATTGROESSEN)+2*len(g.PREISGROESSEN))
