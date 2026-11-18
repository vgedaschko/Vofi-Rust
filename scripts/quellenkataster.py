#!/usr/bin/env python3
"""Normen- und Quellenkataster: aus docs/quellenkataster/quellen.toml die lesbare
Übersicht docs/quellenkataster.md erzeugen oder prüfen.

    python3 scripts/quellenkataster.py            # Übersicht neu erzeugen
    python3 scripts/quellenkataster.py --pruefen  # Daten prüfen; Übersicht aktuell?

Felder je Eintrag ([[quelle]]):
    id              eindeutig, stabil, Großbuchstaben/Ziffern/Bindestrich, z. B. "BGB-559"
    gruppe          gesetz | foerderung | norm | methode | literatur | daten
    kurz            Kurzbezeichnung, z. B. "§ 559 BGB"
    titel           amtlicher Titel oder Gegenstand
    herausgeber     wer die Quelle verantwortet
    fundstelle      Adresse oder bibliografische Angabe
    stand           Fassung, Ausgabe oder Stand laut Quelle
    beleg           original (an der amtlichen oder herausgebenden Stelle gelesen)
                    | wortlaut (vollständiger wörtlicher Abdruck bei Fachverlag oder Volltextsammlung gelesen,
                      weil die amtliche Stelle nicht erreichbar war; Stelle in der Fundstelle nennen)
                    | sekundaer (nur Zusammenfassung, Kommentar oder Auszug) | ungeprueft
    gelesen_am      JJJJ-MM-TT, Pflicht bei beleg = original oder wortlaut, sonst ""
    verwendet_fuer  Liste: wofür das Werkzeug die Quelle braucht
    turnus          monatlich | vierteljaehrlich | jaehrlich | bei-neuausgabe
    zugang          frei | kostenpflichtig | lizenz-klaeren
    bemerkung       frei, darf leer sein
"""
import datetime
import re
import sys
import tomllib
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
DATEN = WURZEL / "docs/quellenkataster/quellen.toml"
AUSGABE = WURZEL / "docs/quellenkataster.md"

GRUPPEN = {
    "gesetz": "Gesetze und Verordnungen",
    "foerderung": "Förderrichtlinien, Merkblätter und Produktinformationen",
    "norm": "Normen und Branchenrichtlinien",
    "methode": "Methoden- und Qualitätsstandards",
    "literatur": "Fachliteratur und Rechenbeispiele",
    "daten": "Datenquellen",
}
BELEG = {"original": "am Original gelesen", "wortlaut": "Wortlaut in Verlagswiedergabe gelesen", "sekundaer": "nur Sekundärquelle", "ungeprueft": "nicht geprüft"}
GELESEN = ("original", "wortlaut")
TURNUS = {"monatlich": "monatlich", "vierteljaehrlich": "vierteljährlich", "jaehrlich": "jährlich", "bei-neuausgabe": "bei Neuausgabe"}
ZUGANG = {"frei": "frei", "kostenpflichtig": "kostenpflichtig", "lizenz-klaeren": "Lizenz klären"}
VERWEISENDE = ["docs/spezifikation.md", "docs/fachspezifikation-rechenkern.md", "docs/entwicklungsplan.md", "docs/entscheidungen.md", "CLAUDE.md", "docs/modellannahmen/annahmen.toml"]
VERWEIS = re.compile(r"`([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)`")
PFLICHT = ["id", "gruppe", "kurz", "titel", "herausgeber", "fundstelle", "stand", "beleg", "gelesen_am", "verwendet_fuer", "turnus", "zugang", "bemerkung"]


def laden():
    with DATEN.open("rb") as f:
        return tomllib.load(f).get("quelle", [])


def pruefen(quellen):
    fehler, gesehen = [], set()
    for nr, q in enumerate(quellen, 1):
        wo = q.get("id", f"Eintrag {nr}")
        for feld in PFLICHT:
            if feld not in q:
                fehler.append(f"{wo}: Feld '{feld}' fehlt")
        if not re.fullmatch(r"[A-Z0-9][A-Z0-9-]*", str(q.get("id", ""))):
            fehler.append(f"{wo}: id nur aus Großbuchstaben, Ziffern, Bindestrich")
        if q.get("id") in gesehen:
            fehler.append(f"{wo}: id doppelt")
        gesehen.add(q.get("id"))
        for feld, erlaubt in (("gruppe", GRUPPEN), ("beleg", BELEG), ("turnus", TURNUS), ("zugang", ZUGANG)):
            if q.get(feld) not in erlaubt:
                fehler.append(f"{wo}: {feld} = {q.get(feld)!r} ist nicht erlaubt ({', '.join(erlaubt)})")
        datum = q.get("gelesen_am", "")
        if datum:
            try:
                if datetime.date.fromisoformat(datum) > datetime.date.today():
                    fehler.append(f"{wo}: gelesen_am liegt in der Zukunft")
            except (ValueError, TypeError):
                fehler.append(f"{wo}: gelesen_am ist kein Datum JJJJ-MM-TT")
        if q.get("beleg") in GELESEN and not datum:
            fehler.append(f"{wo}: beleg = original oder wortlaut verlangt gelesen_am")
        if q.get("beleg") not in GELESEN and datum:
            fehler.append(f"{wo}: gelesen_am nur bei beleg = original oder wortlaut")
        if not isinstance(q.get("verwendet_fuer"), list) or not q.get("verwendet_fuer"):
            fehler.append(f"{wo}: verwendet_fuer muss eine nicht leere Liste sein")
        for feld in ("kurz", "titel", "herausgeber", "fundstelle", "stand"):
            if not str(q.get(feld, "")).strip():
                fehler.append(f"{wo}: {feld} ist leer")
        for feld in ("id", "kurz", "titel", "herausgeber", "fundstelle", "stand", "gelesen_am", "bemerkung"):
            if feld in q and not isinstance(q[feld], str):
                fehler.append(f"{wo}: {feld} muss Text sein")
        if str(q.get("fundstelle", "")).startswith("http") and " " in str(q.get("fundstelle", "")).strip():
            fehler.append(f"{wo}: fundstelle mit Adresse darf keinen weiteren Text enthalten (Text gehört in bemerkung)")
    fehler.extend(verweise_pruefen(gesehen))
    return fehler


def verweise_pruefen(bekannt):
    """Quellenkennungen, die Steuerungsdokumente in Backticks nennen, müssen im Kataster stehen.

    Geprüft wird jede Kennung in Backticks nach dem Muster GROSS-TEIL (zum Beispiel `ESTG-35`),
    ausgenommen Modellannahmen (MA-000). Angaben ohne Backticks und Stellen, an denen eine
    Kennung ganz fehlt, findet diese Prüfung nicht. Code und Tests kommen hinzu, sobald es sie gibt.
    """
    fehler = []
    for name in VERWEISENDE:
        pfad = WURZEL / name
        if not pfad.is_file():
            continue
        for k in sorted(set(VERWEIS.findall(pfad.read_text(encoding="utf-8")))):
            if k not in bekannt and not re.fullmatch(r"MA-\d{3}", k):
                fehler.append(f"{name}: nennt die Quelle {k}, die nicht im Kataster steht")
    return fehler



def zelle(text):
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def quelle_md(q):
    f = q["fundstelle"]
    name = f"[{zelle(q['kurz'])}]({f})" if f.startswith("http") else zelle(q["kurz"])
    zusatz = "" if f.startswith("http") else f" · {zelle(f)}"
    return f"{name} – {zelle(q['titel'])}{zusatz}"


def erzeugen(quellen):
    z = []
    z += ["# Normen- und Quellenkataster", ""]
    z += ["Zentrales Verzeichnis aller Gesetze, Förderrichtlinien, Normen, Standards, Fachliteratur und Datenquellen, auf die sich Spezifikation, Regel- und Förderkatalog und später die Anwendung stützen. Leser: Entwicklung, Katalogverantwortliche, Prüfer.", ""]
    z += ["**Diese Datei wird erzeugt.** Gepflegt wird `docs/quellenkataster/quellen.toml`; danach `python3 scripts/quellenkataster.py` ausführen. Jede Rechts-, Förder- oder Normangabe im Projekt verweist auf eine Kennung aus diesem Kataster.", ""]
    gelesen = [q["gelesen_am"] for q in quellen if q["gelesen_am"]]
    z += [f"**Stand:** {len(quellen)} Quellen" + (f" · zuletzt gelesen: {max(gelesen)}" if gelesen else ""), ""]
    z += ["Belegstufen: „am Original gelesen“ heißt an der amtlichen oder herausgebenden Stelle; „Wortlaut in Verlagswiedergabe gelesen“ heißt vollständiger wörtlicher Abdruck bei einem Fachverlag oder in einer Volltextsammlung, weil die amtliche Stelle nicht erreichbar war; „nur Sekundärquelle“ heißt Zusammenfassung, Kommentar oder Auszug.", ""]
    z += ["## Überblick", "", "| Gruppe | Quellen | am Original gelesen | Wortlaut in Verlagswiedergabe | nur Sekundärquelle | nicht geprüft |", "|---|---|---|---|---|---|"]
    for g, titel in GRUPPEN.items():
        teil = [q for q in quellen if q["gruppe"] == g]
        if teil:
            n = lambda b: sum(1 for q in teil if q["beleg"] == b)
            z.append(f"| {titel} | {len(teil)} | {n('original')} | {n('wortlaut')} | {n('sekundaer')} | {n('ungeprueft')} |")
    n = lambda b: sum(1 for q in quellen if q["beleg"] == b)
    z += [f"| **Gesamt** | **{len(quellen)}** | **{n('original')}** | **{n('wortlaut')}** | **{n('sekundaer')}** | **{n('ungeprueft')}** |", ""]
    offen = [q for q in quellen if q["beleg"] != "original" or q["zugang"] == "lizenz-klaeren"]
    if offen:
        z += ["## Handlungsbedarf", "", "Quellen, die noch nicht an der amtlichen Stelle gelesen sind oder deren Nutzungsrecht zu klären ist.", "", "| Kennung | Quelle | Was fehlt |", "|---|---|---|"]
        folge = list(GRUPPEN)
        for q in sorted(offen, key=lambda q: (folge.index(q["gruppe"]), q["id"])):
            was = []
            if q["beleg"] != "original":
                was.append(BELEG[q["beleg"]])
            if q["zugang"] == "lizenz-klaeren":
                was.append("Lizenz klären")
            z.append(f"| `{q['id']}` | {zelle(q['kurz'])} | {'; '.join(was)} |")
        z.append("")
    for g, titel in GRUPPEN.items():
        teil = sorted((q for q in quellen if q["gruppe"] == g), key=lambda q: q["id"])
        if not teil:
            continue
        z += [f"## {titel}", "", "| Kennung | Quelle | Stand | Beleg | Verwendet für | Prüfturnus | Zugang |", "|---|---|---|---|---|---|---|"]
        for q in teil:
            beleg = BELEG[q["beleg"]] + (f" ({q['gelesen_am']})" if q["gelesen_am"] else "")
            z.append(f"| `{q['id']}` | {quelle_md(q)} | {zelle(q['stand'])} | {beleg} | {zelle('; '.join(q['verwendet_fuer']))} | {TURNUS[q['turnus']]} | {ZUGANG[q['zugang']]} |")
        z.append("")
        hinweise = [q for q in teil if q["bemerkung"].strip()]
        if hinweise:
            z += ["Bemerkungen:", ""] + [f"- `{q['id']}`: {q['bemerkung'].strip()}" for q in hinweise] + [""]
    return "\n".join(z).rstrip() + "\n"


def main():
    quellen = laden()
    fehler = pruefen(quellen)
    if fehler:
        print("Quellenkataster: Fehler\n  " + "\n  ".join(fehler), file=sys.stderr)
        return 1
    text = erzeugen(quellen)
    if "--pruefen" in sys.argv:
        if not AUSGABE.exists() or AUSGABE.read_text(encoding="utf-8") != text:
            print("Quellenkataster: docs/quellenkataster.md ist nicht aktuell – python3 scripts/quellenkataster.py ausführen", file=sys.stderr)
            return 1
        print(f"Quellenkataster in Ordnung: {len(quellen)} Quellen")
        return 0
    AUSGABE.write_text(text, encoding="utf-8")
    print(f"{AUSGABE.relative_to(WURZEL)} erzeugt: {len(quellen)} Quellen")
    return 0


if __name__ == "__main__":
    sys.exit(main())
