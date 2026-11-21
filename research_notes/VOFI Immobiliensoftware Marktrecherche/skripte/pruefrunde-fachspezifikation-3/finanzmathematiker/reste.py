"""Sucht in der Fachspezifikation alte Sollwerte (Spalte 'alt' der Differenzberichte), die nicht mehr gelten."""
import re, json
REF = "../../referenzrechner/"
doc = open("/home/user/vofi-rust/docs/fachspezifikation-rechenkern.md").read()
txt = open(REF + "aenderungen-runde2.md").read()
teil = txt[txt.index("## Durchsicht und Nachtrag 2"):]
ev = json.load(open(REF + "erwartete_werte.json"))
werte_neu = set()
for v in ev.values():
    for x in re.findall(r"-?\d+\.\d+|-?\d{4,}", json.dumps(v)):
        werte_neu.add(x.lstrip("-"))
def de(s):
    s = s.lstrip("-")
    if "." in s:
        a, b = s.split(".")
    else:
        a, b = s, None
    a = f"{int(a):,}".replace(",", ".")
    return a + ("," + b if b else "")
gefunden = []
for zeile in teil.splitlines():
    if not zeile.startswith("| RF"): continue
    sp = [c.strip() for c in zeile.split("|")[1:-1]]
    if len(sp) < 5: continue
    fall, name, alt, neu = sp[0], sp[1], sp[2], sp[3]
    for x in re.findall(r"-?\d+\.\d+|-?\d{5,}", alt):
        if x in neu or x.lstrip("-") in werte_neu: continue
        for form in {de(x), x.lstrip("-")}:
            if len(form) >= 6 and form in doc:
                for m in re.finditer(re.escape(form), doc):
                    ln = doc[:m.start()].count("\n") + 1
                    gefunden.append((ln, form, fall, name[:70], neu[:40]))
for g in sorted(set(gefunden)): print(g)
