"""Pruefrunde 3, Controller: Abgleich aller Kennungen der Fachspezifikation zwischen Definition und Verwendung.
Definition: Tabellenzeile, die mit der Kennung beginnt, oder fett gesetzte Regelueberschrift (**R-x.y).
Ausgabe: verwendet ohne Definition; definiert ohne Verwendung; Verwendungen entfallener Kennungen mit Zeile."""
import re, sys
FS = "/home/user/vofi-rust/docs/fachspezifikation-rechenkern.md"
zeilen = open(FS, encoding="utf-8").read().split("\n")
MUSTER = r"\b(E-\d{2}|H-\d{2}|KAT-\d{2}|M-\d{2}|P-\d{2}|V-\d{2}|NF-\d{2}|RF-\d{2}|R-\d{1,2}\.\d{1,2}|Z-[A-Z]\d{0,2})\b"
defn, verw = {}, {}
for nr, z in enumerate(zeilen, 1):
    m = re.match(r"^\| (E-\d{2}|H-\d{2}|KAT-\d{2}|M-\d{2}|P-\d{2}|V-\d{2}|NF-\d{2}|RF-\d{2}|Z-[A-Z]\d{0,2}) \|", z)
    if m and nr < 1645:  # Anhang A ist keine Definition
        defn.setdefault(m.group(1), nr)
    m = re.match(r"^\*\*(R-\d{1,2}\.\d{1,2}) ", z)
    if m:
        defn.setdefault(m.group(1), nr)
    for k in re.findall(MUSTER, z):
        verw.setdefault(k, []).append(nr)
# Kennungen, die als Bereich verwendet werden (E-56 bis E-58), gelten als verwendet
entfallen = {}
for nr, z in enumerate(zeilen, 1):
    m = re.match(r"^\| (H-\d{2}|KAT-\d{2}) \| entfällt", z)
    if m: entfallen[m.group(1)] = nr
for k in ["E-44","E-52","E-53","E-54","E-55","E-61","E-63","E-66","E-67","E-68"]: entfallen[k] = "R-3.3"
entfallen["R-6.17"] = "R-6.17"
def sortkey(k):
    p, n = k.split("-", 1)
    return (p, [int(x) if x.isdigit() else x for x in re.split(r"[.]", n)] if p != "Z" else n)
print("== verwendet, aber nirgends definiert")
for k in sorted(set(verw) - set(defn), key=sortkey):
    if k.startswith("Z-") or k in entfallen: continue
    print(f"  {k}: Zeilen {verw[k][:8]}")
print("== definiert, aber nur an der Definition genannt")
for k in sorted(defn, key=sortkey):
    if [n for n in verw.get(k, []) if n != defn[k]] == []:
        print(f"  {k} (Zeile {defn[k]})")
print("== entfallene Kennungen und ihre Nennungen (Zeile)")
for k in sorted(entfallen, key=sortkey):
    print(f"  {k}: {verw.get(k, [])}")
# Lücken in der Nummernfolge
for p in ["E","H","KAT","M","P","V","NF"]:
    ns = sorted(int(k.split('-')[1]) for k in defn if k.split('-')[0] == p)
    if ns:
        luecken = [i for i in range(ns[0], ns[-1]+1) if i not in ns]
        print(f"{p}: {len(ns)} definiert ({ns[0]}..{ns[-1]}), Luecken {luecken}")
