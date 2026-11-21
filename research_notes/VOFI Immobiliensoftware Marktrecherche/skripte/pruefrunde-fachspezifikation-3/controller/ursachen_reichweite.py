"""Pruefrunde 3, Controller: Reichweite der Ursachenmuster (R-15.2).
Zaehlt je Muster, wie viele festgeschriebene Werte es trifft (in wie vielen Faellen),
und wie viele davon in der Durchsicht tatsaechlich geaendert wurden (laut aenderungen-runde2.md)."""
import json, re, sys, os
R = os.path.join(os.path.dirname(__file__), "..", "..", "referenzrechner")
werte = json.load(open(os.path.join(R, "erwartete_werte.json"), encoding="utf-8"))
for datei in sys.argv[1:] or ["ursachen-durchsicht.json", "ursachen-runde2-nachtrag2.json", "ursachen-runde2.json"]:
    u = json.load(open(os.path.join(R, datei), encoding="utf-8"))["ursachen"]
    print(f"\n== {datei}: {len(u)} Muster, {len(werte)} Sollwerte")
    breit = []
    for muster, text in u:
        treffer = [k for k in werte if re.search(muster, k)]
        faelle = sorted({k.split('|')[0] for k in treffer})
        voll = muster in werte  # voller Name?
        breit.append((len(treffer), muster, faelle, voll))
    breit.sort(reverse=True)
    vollnamen = sum(1 for b in breit if b[3])
    print(f"   davon voller Wertname: {vollnamen}; Muster mit >= 5 Treffern: {sum(1 for b in breit if b[0]>=5)}")
    for n, m, f, v in breit[:12]:
        print(f"   {n:4d} Werte in {len(f)} Faellen  {m[:90]}")
