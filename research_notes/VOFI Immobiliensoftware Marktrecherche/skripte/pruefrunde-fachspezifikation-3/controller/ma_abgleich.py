"""Pruefrunde 3, Controller: Abgleich der Modellannahmen zwischen Fachspezifikation und annahmen.toml."""
import tomllib, re, os
ROOT = "/home/user/vofi-rust"
ma = {a["id"]: a for a in tomllib.load(open(f"{ROOT}/docs/modellannahmen/annahmen.toml", "rb"))["annahme"]}
fs = open(f"{ROOT}/docs/fachspezifikation-rechenkern.md", encoding="utf-8").read()
lesarten_haus = {"MA-026", "MA-031", "MA-036", "MA-038"}
print("Kennung status gewicht umschaltbar | in FS? | Gewicht in FS-Tabelle Kap.17")
tab = dict(re.findall(r"^\| `(MA-\d+)` \| [^|]+\| (hoch|mittel|gering) \|", fs, re.M))
for k in sorted(ma):
    a = ma[k]
    in_fs = k in fs
    warn = []
    if a["status"] == "offen" and in_fs:
        if a.get("umschaltbar") and k not in lesarten_haus:
            warn.append("toml umschaltbar=true, FS: kein Schalter")
        if not a.get("umschaltbar") and k in lesarten_haus:
            warn.append("toml umschaltbar=false, FS: Lesart des Hauses")
    if k in tab and tab[k] != a["gewicht"]:
        warn.append(f"Gewicht FS {tab[k]} != toml {a['gewicht']}")
    if a["status"] != "offen" and in_fs:
        warn.append(f"status {a['status']} – in FS verwendet")
    print(f"{k} {a['status']:<10} {a['gewicht']:<7} {str(a.get('umschaltbar')):<5} | {'ja' if in_fs else '- '} | {'; '.join(warn)}")
used = sorted(set(re.findall(r"MA-\d{3}", fs)))
print("\nIn FS verwendet, nicht im Verzeichnis:", [k for k in used if k not in ma])
