"""Rahmen der Referenzfaelle (Kapitel 15): Vergleich Ist gegen Soll mit benannter Toleranz."""
from decimal import Decimal as D
from zahlen import NULL, d, de, Rundung
from zeit import Raster
from steuer import Steuerparameter, LEHRBUCH
from finanzplan import PlanEingabe, Verkauf, rechne_plan, rechne_alternative
from proben import pruefe_plan
from kennzahlen import werte_aus, interner_zinsfuss

import json
import os

ERGEBNISSE = []          # (Fall, Name, ok, ist, soll, toleranz)
FESTDATEI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "erwartete_werte.json")
FEST = json.load(open(FESTDATEI, encoding="utf-8")) if os.path.exists(FESTDATEI) else {}
FESTSCHREIBEN = [False]  # nur mit --festschreiben: erwartete Werte der eigenen Faelle neu schreiben
NEU = {}

# Suchbereich des internen Zinsfusses in den Referenzfaellen (H-21, Annahme der Beispiele)
IZF_BEREICH = (D("-0.99"), D("10"), 2000)


def izf(reihe, p=1):
    """Interner Zinsfuss mit dem Suchbereich der Beispiele; Rueckgabe (Loesungen, Wechsel, Status)."""
    return interner_zinsfuss(reihe, *IZF_BEREICH, p=p)


def fall(kennung, titel):
    print(f"\n{kennung}  {titel}")
    return kennung


def pruefe(kennung, name, ist, soll, toleranz="0.01", stellen=2):
    """Bestanden, wenn |Ist - Soll| <= Toleranz. Soll und Toleranz als Zeichenkette oder Decimal."""
    soll_d, tol = d(soll), d(toleranz)
    ok = ist is not None and abs(ist - soll_d) <= tol
    ERGEBNISSE.append((kennung, name, ok, ist, soll_d, tol))
    print(f"  {'ok ' if ok else 'ABW'} {name:<62} Ist {de(ist, stellen) if ist is not None else 'None':>18}  "
          f"Soll {de(soll_d, stellen):>18}  Tol. {tol}")
    return ok


def pruefe_fest(kennung, name, ist, stellen=2, toleranz="0"):
    """Eigener Fall ohne veroeffentlichten Wert: Vergleich mit dem festgeschriebenen Wert aus
    erwartete_werte.json (R-15.2). Geldbetraege im Rundungsmodus Cent stimmen exakt; Kennzahlen werden
    auf 'stellen' Nachkommastellen festgeschrieben und mit halber letzter Stelle verglichen."""
    schluessel = f"{kennung}|{name}"
    if ist is None or isinstance(ist, (str, bool, int, list, dict)):
        wert = ist
    else:
        wert = str(ist.quantize(D(1).scaleb(-stellen)))
    NEU[schluessel] = wert
    if FESTSCHREIBEN[0]:
        ERGEBNISSE.append((kennung, name, True, ist, wert, None))
        print(f"  neu {name:<62} festgeschrieben {wert}")
        return True
    soll = FEST.get(schluessel, "(fehlt)")
    ok = soll == wert
    if not ok and toleranz != "0" and soll not in (None, "(fehlt)") and wert is not None:
        ok = abs(D(str(soll)) - D(str(wert))) <= d(toleranz)
    ERGEBNISSE.append((kennung, name, ok, wert, soll, toleranz))
    print(f"  {'ok ' if ok else 'ABW'} {name:<62} Ist {str(wert):>18}  Soll {str(soll):>18}  (festgeschrieben)")
    return ok


def schreibe_fest(basis_datei, ursachen_datei, bericht_datei, im_code=()):
    """R-15.2: schreibt die erwarteten Werte nur zusammen mit einem Differenzbericht.

    basis_datei     Stand, gegen den verglichen wird (Voreinstellung: die bisherige erwartete_werte.json)
    ursachen_datei  JSON mit "ursachen": Liste von [Muster, Ursache] (das erste Muster, das als regulaerer
                    Ausdruck auf den Schluessel passt, liefert die Ursache) und "umbenannt": Liste von
                    [Muster, Ersatz] fuer Werte, deren Name sich geaendert hat. Hat ein geaenderter, neuer oder
                    entfallener Wert keine Ursache, wird nichts geschrieben.
    bericht_datei   Markdown-Datei mit alt, neu und Ursache je Wert
    im_code         Liste (Name, alt, neu, Ursache) fuer Sollwerte, die im Code der Referenzfaelle stehen
    """
    import re
    alt = json.load(open(basis_datei, encoding="utf-8")) if basis_datei and os.path.exists(basis_datei) else {}
    angaben = json.load(open(ursachen_datei, encoding="utf-8"))
    ursachen = angaben["ursachen"]
    umbenannt = {}
    for k in list(alt):
        for muster, ersatz in angaben.get("umbenannt", []):
            neu_k = re.sub(muster, ersatz, k)
            if neu_k != k and neu_k in NEU and neu_k not in alt:
                alt[neu_k] = alt.pop(k)
                umbenannt[neu_k] = k
                break

    def ursache(schluessel):
        for muster, text in ursachen:
            if re.search(muster, schluessel):
                return text
        return None

    zeilen, ohne = [], []
    for k in sorted(set(alt) | set(NEU)):
        a, n = alt.get(k, "(neu)"), NEU.get(k, "(entfallen)")
        if a == n:
            continue
        u = ursache(k)
        if u is None:
            ohne.append(k)
        zeilen.append((k, a, n, u))
    if ohne:
        print(f"\nNICHT festgeschrieben: {len(ohne)} geaenderte Werte ohne Ursache in {os.path.basename(ursachen_datei)}:")
        for k in ohne[:40]:
            print("   ", k)
        return False

    def zelle(x):
        return str(x).replace("|", "/")
    gleich = len([k for k in NEU if alt.get(k) == NEU[k]])
    kopf = ["# Differenzbericht zur Festschreibung der Sollwerte", "",
            f"Basis: `{os.path.basename(basis_datei)}` ({len(alt)} Werte). Neu: `{os.path.basename(FESTDATEI)}` "
            f"({len(NEU)} Werte). Unveraendert: {gleich}. Geaendert, neu oder entfallen: {len(zeilen)}.", "",
            "## Festgeschriebene Werte", "", "| Fall | Wert | alt | neu | Ursache |", "|---|---|---|---|---|"]
    for k, a, n, u in zeilen:
        fall_, name = k.split("|", 1)
        if k in umbenannt:
            name += f" (bisher: {umbenannt[k].split('|', 1)[1]})"
        kopf.append(f"| {fall_} | {zelle(name)} | {zelle(a)} | {zelle(n)} | {u} |")
    if im_code:
        kopf += ["", "## Sollwerte im Code der Referenzfaelle", "", "| Wert | alt | neu | Ursache |", "|---|---|---|---|"]
        kopf += [f"| {zelle(a)} | {zelle(b)} | {zelle(c)} | {u} |" for a, b, c, u in im_code]
    open(bericht_datei, "w", encoding="utf-8").write("\n".join(kopf) + "\n")
    json.dump(NEU, open(FESTDATEI, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    print(f"\n{len(NEU)} erwartete Werte nach {os.path.basename(FESTDATEI)} geschrieben; "
          f"{len(zeilen)} Aenderungen im Differenzbericht {os.path.basename(bericht_datei)}.")
    return True


def pruefe_proz(kennung, name, ist, soll_prozent, stellen=3):
    """Rendite in Prozent auf die ausgewiesenen Nachkommastellen."""
    tol = D(1).scaleb(-stellen) / 2
    return pruefe(kennung, name + " (%)", None if ist is None else ist * 100, soll_prozent, tol, stellen)


def pruefe_gleich(kennung, name, ist, soll):
    ok = ist == soll
    ERGEBNISSE.append((kennung, name, ok, ist, soll, None))
    print(f"  {'ok ' if ok else 'ABW'} {name:<62} Ist {str(ist):>18}  Soll {str(soll):>18}")
    return ok


def pruefe_reihe(kennung, name, ist, soll, toleranz="0.5"):
    """Reihe veroeffentlichter (gerundeter) Werte; Toleranz je Wert."""
    tol = d(toleranz)
    abw = [(t + 1, de(a, 2), s) for t, (a, s) in enumerate(zip(ist, soll)) if abs(a - d(s)) > tol]
    ok = not abw and len(ist) == len(soll)
    ERGEBNISSE.append((kennung, name, ok, None, None, tol))
    print(f"  {'ok ' if ok else 'ABW'} {name:<62} {len(soll)} Werte, Tol. {tol}" + ("" if ok else f"  abweichend: {abw}"))
    return ok


def pruefe_proben(kennung, plan, alt=None, name="Kontrollsummen des Finanzplans (P-01 bis P-03, P-05, P-08 bis P-11, P-15 bis P-17, P-19)"):
    bef = pruefe_plan(plan, alt)
    return pruefe_gleich(kennung, name, len(bef), 0) or print("     ", bef[:5])


def info(text):
    print("      " + text)


def lehrbuch_steuer(satz, verlust="sofort", verkauf_pflichtig=True, zins_satz=None):
    return Steuerparameter(status=LEHRBUCH, satz=d(satz), verlust=verlust,
                           verkaufsgewinn_pflichtig=verkauf_pflichtig,
                           zins_satz=None if zins_satz is None else d(zins_satz))


def jahresplan(n, a0, ueberschuss, ek, tranchen, h, kk, steuer=None, verkauf=None, afa=0, buchwert=None,
               a_lang=None, einlagen=None, entnahmen=None, rundung="keine", kk_linie=None, p=1,
               zuschuss=None, afa_grundlage=None):
    """Baut einen Finanzplan im Jahresmodus aus Lehrbuchgroessen.

    ueberschuss: Zahl oder Liste (t = 1..n) der Einnahmenueberschuesse; a0 Investitionsausgabe in t = 0;
    verkauf: Erloes in t = n (nach Verkaufskosten); afa: Jahresabschreibung; buchwert: Restbuchwert in t = n.
    """
    r = Raster(p=p, n=n)
    N = r.N
    ue = [d(x) for x in ueberschuss] if isinstance(ueberschuss, (list, tuple)) else [d(ueberschuss)] * n
    miete = [NULL] + ue
    null = [NULL] * (N + 1)
    ein = [NULL] * (N + 1)
    ein[0] = d(ek)
    for t, v in (einlagen or {}).items():
        ein[t] += d(v)
    ent = [NULL] * (N + 1)
    for t, v in (entnahmen or {}).items():
        ent[t] += d(v)
    afa_reihe = [NULL] + [d(afa)] * n
    vk = None
    anschaffung = None
    if verkauf is not None:
        bw = d(buchwert) if buchwert is not None else d(a0) - d(afa) * n
        vk = Verkauf(preis_brutto=d(verkauf), buchwert=bw)
        if buchwert is None and zuschuss is None:        # Anschaffungskosten bekannt: P-08 und P-15 laufen mit
            anschaffung = d(a0)
    e = PlanEingabe(raster=r, miete=miete, kosten=list(null), erhaltung=list(null),
                    investition=[d(a0)] + [NULL] * N, afa=afa_reihe, tranchen=tranchen,
                    steuer=steuer or lehrbuch_steuer(0), einlagen=ein, entnahmen=ent, h_kurz=d(h), kk_zins=d(kk),
                    a_lang=None if a_lang is None else d(a_lang), kk_linie=kk_linie, verkauf=vk,
                    zuschuss=zuschuss, rundung=Rundung(rundung), anschaffung=anschaffung,
                    afa_grundlage=afa_grundlage)
    plan = rechne_plan(e)
    alt = rechne_alternative(e, plan.einlagen_netto, plan.entnahmen_netto)
    return plan, alt, werte_aus(plan, alt)


def zusammenfassung():
    gesamt = len(ERGEBNISSE)
    abw = [x for x in ERGEBNISSE if not x[2]]
    faelle = sorted({x[0] for x in ERGEBNISSE})
    schlecht = sorted({x[0] for x in abw})
    print(f"\nReferenzfaelle: {len(faelle)} Faelle mit {gesamt} Pruefungen; "
          f"{gesamt - len(abw)} bestanden, {len(abw)} abweichend.")
    for k, name, ok, ist, soll, tol in abw:
        print(f"  ABWEICHUNG {k} {name}: Ist {ist}, Soll {soll}, Toleranz {tol}")
    if schlecht:
        print("  Faelle mit Abweichung:", ", ".join(schlecht))
    return 0 if not abw else 1
