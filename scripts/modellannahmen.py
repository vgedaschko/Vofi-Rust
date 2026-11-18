#!/usr/bin/env python3
"""Verzeichnis der Modellannahmen: aus docs/modellannahmen/annahmen.toml die lesbare
Übersicht docs/modellannahmen.md erzeugen oder prüfen. Die Konvention selbst steht in
docs/spezifikation.md, Kapitel „Modellannahmen".

    python3 scripts/modellannahmen.py            # Übersicht neu erzeugen
    python3 scripts/modellannahmen.py --pruefen  # Daten, Verweise und Aktualität prüfen

Felder je Eintrag ([[annahme]]):
    id             "MA-" und drei Ziffern, fortlaufend, wird nie neu vergeben
    titel          worum es geht, wenige Wörter
    annahme        was das Modell annimmt, ein genauer Satz
    grund          warum sich das vor dem Bau nicht klären lässt
    alternative    die andere denkbare Lesart
    grundlage      worauf sich die Annahme stützt (Text)
    quellen        Liste von Kennungen aus dem Quellenkataster, darf leer sein
    gewicht        hoch | mittel | gering  – Wirkung auf Ergebnisse
    wirkung        welche Ergebnisse betroffen sind und, soweit bekannt, wie stark
    sichtbar       kunde | anwender | intern
                   kunde: steht im Annahmenblatt von Kundenberichten, wenn angewandt
                   anwender: in der Anwendung am betroffenen Ergebnis und in internen Berichten
                   intern: nur in Entwicklungsunterlagen
    umschaltbar    true, wenn die Alternative als Einstellung wählbar ist oder sein soll
    klaerung       wer klären kann (NBank, Anwalt, Steuerberater, Auftraggeber, Fachliteratur …)
    wiedervorlage  wann die Annahme wieder geprüft wird (Datum oder Anlass)
    status         offen | bestaetigt | widerlegt | entfallen
    gesetzt_am     JJJJ-MM-TT
    erledigt_am    JJJJ-MM-TT, Pflicht außer bei status = offen, sonst ""
    verwendet_in   Liste: Stellen in Spezifikation, Katalog, Code, Tests
    bemerkung      frei; bei bestaetigt/widerlegt: wodurch
"""
import datetime
import re
import subprocess
import sys
import tomllib
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
DATEN = WURZEL / "docs/modellannahmen/annahmen.toml"
AUSGABE = WURZEL / "docs/modellannahmen.md"
QUELLEN = WURZEL / "docs/quellenkataster/quellen.toml"

GEWICHT = {"hoch": "hoch", "mittel": "mittel", "gering": "gering"}
SICHTBAR = {"kunde": "Kundenbericht", "anwender": "Anwendung", "intern": "nur intern"}
STATUS = {"offen": "offen", "bestaetigt": "bestätigt", "widerlegt": "widerlegt", "entfallen": "entfallen"}
TEXT = ["id", "titel", "annahme", "grund", "alternative", "grundlage", "wirkung", "klaerung", "wiedervorlage", "gesetzt_am", "erledigt_am", "bemerkung"]
PFLICHT = TEXT + ["quellen", "gewicht", "sichtbar", "umschaltbar", "status", "verwendet_in"]
KENNUNG = re.compile(r"\bMA-\d{3}\b")


def laden():
    with DATEN.open("rb") as f:
        return tomllib.load(f).get("annahme", [])


def quellen_kennungen():
    if not QUELLEN.exists():
        return None
    with QUELLEN.open("rb") as f:
        return {q["id"] for q in tomllib.load(f).get("quelle", [])}


def verweise():
    """Alle im Repository genannten MA-Kennungen außerhalb des Verzeichnisses selbst."""
    try:
        dateien = subprocess.run(["git", "-C", str(WURZEL), "ls-files", "-co", "--exclude-standard"], capture_output=True, text=True, check=True).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError):
        return {}
    fund = {}
    for name in dateien:
        if name.startswith(("docs/modellannahmen", "scripts/modellannahmen.py", "docs/pruefung/", "research_notes/", "reports/")):
            continue
        pfad = WURZEL / name
        if pfad.suffix not in {".md", ".rs", ".toml", ".ts", ".tsx", ".sql", ".py", ".sh"} or not pfad.is_file():
            continue
        try:
            for k in set(KENNUNG.findall(pfad.read_text(encoding="utf-8", errors="ignore"))):
                if k != "MA-000":  # steht in Texten für das Muster der Kennung
                    fund.setdefault(k, []).append(name)
        except OSError:
            pass
    return fund


def datum(wert):
    try:
        return datetime.date.fromisoformat(wert) <= datetime.date.today()
    except (ValueError, TypeError):
        return False


def pruefen(annahmen):
    fehler, gesehen = [], set()
    bekannt = quellen_kennungen()
    for nr, a in enumerate(annahmen, 1):
        wo = a.get("id", f"Eintrag {nr}")
        for feld in PFLICHT:
            if feld not in a:
                fehler.append(f"{wo}: Feld '{feld}' fehlt")
        for feld in TEXT:
            if feld in a and not isinstance(a[feld], str):
                fehler.append(f"{wo}: {feld} muss Text sein")
        if not re.fullmatch(r"MA-\d{3}", str(a.get("id", ""))) or a.get("id") == "MA-000":
            fehler.append(f"{wo}: id muss die Form MA-001 bis MA-999 haben")
        if a.get("id") in gesehen:
            fehler.append(f"{wo}: id doppelt")
        gesehen.add(a.get("id"))
        for feld, erlaubt in (("gewicht", GEWICHT), ("sichtbar", SICHTBAR), ("status", STATUS)):
            if a.get(feld) not in erlaubt:
                fehler.append(f"{wo}: {feld} = {a.get(feld)!r} ist nicht erlaubt ({', '.join(erlaubt)})")
        if not isinstance(a.get("umschaltbar"), bool):
            fehler.append(f"{wo}: umschaltbar muss true oder false sein")
        for feld in ("titel", "annahme", "grund", "alternative", "grundlage", "wirkung", "klaerung", "wiedervorlage"):
            if not str(a.get(feld, "")).strip():
                fehler.append(f"{wo}: {feld} ist leer")
        if not datum(a.get("gesetzt_am", "")):
            fehler.append(f"{wo}: gesetzt_am ist kein gültiges Datum JJJJ-MM-TT")
        if a.get("status") == "offen" and a.get("erledigt_am"):
            fehler.append(f"{wo}: erledigt_am nur, wenn die Annahme nicht mehr offen ist")
        if a.get("status") in ("bestaetigt", "widerlegt", "entfallen"):
            if not datum(a.get("erledigt_am", "")):
                fehler.append(f"{wo}: status {a['status']} verlangt erledigt_am")
            if not str(a.get("bemerkung", "")).strip():
                fehler.append(f"{wo}: status {a['status']} verlangt in bemerkung, wodurch")
        if a.get("status") == "bestaetigt" and not a.get("quellen"):
            fehler.append(f"{wo}: bestätigt nur mit Quelle aus dem Quellenkataster")
        if a.get("gewicht") == "hoch" and a.get("sichtbar") == "intern":
            fehler.append(f"{wo}: Annahme mit hohem Gewicht darf nicht nur intern sichtbar sein")
        if not isinstance(a.get("quellen"), list) or not isinstance(a.get("verwendet_in"), list):
            fehler.append(f"{wo}: quellen und verwendet_in müssen Listen sein")
        elif bekannt is not None:
            for k in a["quellen"]:
                if k not in bekannt:
                    fehler.append(f"{wo}: Quelle {k} steht nicht im Quellenkataster")
    for k, dateien in sorted(verweise().items()):
        if k not in gesehen:
            fehler.append(f"{k}: wird genannt in {', '.join(sorted(dateien)[:3])}, steht aber nicht im Verzeichnis")
    return fehler


def zelle(text):
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def erzeugen(annahmen):
    offen = [a for a in annahmen if a["status"] == "offen"]
    erledigt = [a for a in annahmen if a["status"] != "offen"]
    rang = {"hoch": 0, "mittel": 1, "gering": 2}
    z = ["# Modellannahmen", ""]
    z += ["Verzeichnis der Annahmen über Recht, Förderpraxis und Methode, die sich vor dem Bau nicht klären lassen und auf denen das Modell trotzdem rechnet. Leser: Auftraggeber, Entwicklung, Prüfer. Die Regeln dazu stehen in `docs/spezifikation.md`, Kapitel „Modellannahmen“.", ""]
    z += ["**Diese Datei wird erzeugt.** Gepflegt wird `docs/modellannahmen/annahmen.toml`; danach `python3 scripts/modellannahmen.py` ausführen.", ""]
    z += [f"**Stand:** {len(offen)} offene Annahmen, davon {sum(1 for a in offen if a['gewicht'] == 'hoch')} mit hohem Gewicht · {len(erledigt)} erledigt", ""]
    if offen:
        z += ["## Offene Annahmen", "", "| Kennung | Thema | Gewicht | Sichtbar | Umschaltbar | Klärung durch | Wiedervorlage |", "|---|---|---|---|---|---|---|"]
        for a in sorted(offen, key=lambda a: (rang[a["gewicht"]], a["id"])):
            z.append(f"| `{a['id']}` | {zelle(a['titel'])} | {GEWICHT[a['gewicht']]} | {SICHTBAR[a['sichtbar']]} | {'ja' if a['umschaltbar'] else 'nein'} | {zelle(a['klaerung'])} | {zelle(a['wiedervorlage'])} |")
        z.append("")
        klaerer = {}
        for a in offen:
            klaerer.setdefault(a["klaerung"], []).append(a["id"])
        z += ["Nach Klärungsweg:", ""] + [f"- **{zelle(k)}:** " + ", ".join(f"`{i}`" for i in sorted(v)) for k, v in sorted(klaerer.items())] + [""]
    z += ["## Einzelheiten", ""]
    for a in sorted(annahmen, key=lambda a: a["id"]):
        z += [f"### {a['id']} · {zelle(a['titel'])}", ""]
        z += [f"- **Annahme:** {a['annahme'].strip()}", f"- **Warum offen:** {a['grund'].strip()}", f"- **Andere Lesart:** {a['alternative'].strip()}"]
        grundlage = a["grundlage"].strip() + (" Quellen: " + ", ".join(f"`{k}`" for k in a["quellen"]) + "." if a["quellen"] else "")
        z += [f"- **Grundlage:** {grundlage}", f"- **Wirkung ({GEWICHT[a['gewicht']]}):** {a['wirkung'].strip()}"]
        z += [f"- **Sichtbar:** {SICHTBAR[a['sichtbar']]} · **Umschaltbar:** {'ja' if a['umschaltbar'] else 'nein'} · **Klärung durch:** {zelle(a['klaerung'])} · **Wiedervorlage:** {zelle(a['wiedervorlage'])}"]
        stand = f"{STATUS[a['status']]}, gesetzt am {a['gesetzt_am']}" + (f", erledigt am {a['erledigt_am']}" if a["erledigt_am"] else "")
        z += [f"- **Status:** {stand}"]
        if a["verwendet_in"]:
            z += ["- **Verwendet in:** " + "; ".join(zelle(v) for v in a["verwendet_in"])]
        if a["bemerkung"].strip():
            z += [f"- **Bemerkung:** {a['bemerkung'].strip()}"]
        z.append("")
    return "\n".join(z).rstrip() + "\n"


def main():
    annahmen = laden()
    fehler = pruefen(annahmen)
    if fehler:
        print("Modellannahmen: Fehler\n  " + "\n  ".join(fehler), file=sys.stderr)
        return 1
    text = erzeugen(annahmen)
    if "--pruefen" in sys.argv:
        if not AUSGABE.exists() or AUSGABE.read_text(encoding="utf-8") != text:
            print("Modellannahmen: docs/modellannahmen.md ist nicht aktuell – python3 scripts/modellannahmen.py ausführen", file=sys.stderr)
            return 1
        offen = sum(1 for a in annahmen if a["status"] == "offen")
        print(f"Modellannahmen in Ordnung: {len(annahmen)} Einträge, {offen} offen")
        return 0
    AUSGABE.write_text(text, encoding="utf-8")
    print(f"{AUSGABE.relative_to(WURZEL)} erzeugt: {len(annahmen)} Einträge")
    return 0


if __name__ == "__main__":
    sys.exit(main())
