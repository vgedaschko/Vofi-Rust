"""Pruefrunde 3, Controller: Quellenkennungen der Fachspezifikation gegen das Kataster; 'verwendet_fuer' mit
Regeln, die entfallen sind (R-6.17) oder entfallene Kennungen nennen."""
import tomllib, re
ROOT = "/home/user/vofi-rust"
q = {x["id"]: x for x in tomllib.load(open(f"{ROOT}/docs/quellenkataster/quellen.toml", "rb"))["quelle"]}
fs = open(f"{ROOT}/docs/fachspezifikation-rechenkern.md", encoding="utf-8").read()
ids = sorted(set(re.findall(r"`([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+)`", fs)) - {k for k in re.findall(r"`(MA-\d+)`", fs)})
print("in FS, nicht im Kataster:", [i for i in ids if i not in q and not i.startswith("MA-")])
print("Kataster-Felder:", sorted(next(iter(q.values())).keys()))
alt = re.compile(r"E-44|E-5[2-5]|E-61|E-63|E-6[6-8]|H-07|H-36|R-6\.17|KAT-02|MA-035")
for k, x in q.items():
    for v in x.get("verwendet_fuer", []):
        if alt.search(v):
            print(f"  {k}: {v[:160]}")
