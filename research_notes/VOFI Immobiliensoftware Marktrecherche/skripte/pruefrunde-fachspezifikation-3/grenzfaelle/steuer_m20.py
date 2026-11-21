"""GF3-E E-69 im ersten Jahr und am Bindungsende; GF3-F E-70 an der Mindestdauer; GF3-G Auftraege, die feste Werte aendern (M-20)."""
from h import *
import sys

GR = {"steuer.kuerzung_bleibt_verkaufsjahr": "Sachverhalt geprueft", "zuschuss_verteilung": "Antrag gestellt"}


def gew(e):
    pr = e.plan.steuer.protokoll if hasattr(e.plan.steuer, "protokoll") else None
    n = e.plan.e.raster.n
    z = e.plan.zeilen
    st = [e.plan.jahressumme("steuer", j) for j in range(1, n + 1)]
    return f"Steuer je Jahr {[de(x) for x in st[-2:]]}"


w = sys.argv[1:] or ["E", "F", "G"]
if "E" in w:
    print("== GF3-E E-41/E-69: Verkauf im ersten Jahr, am Ende der Zinsbindung, am Bindungsende der Foerderung")
    for n in (1, 2, 10, 11, 12):
        for e69 in (False, True):
            s = A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True, kuerzung_bleibt_verkaufsjahr=e69)
            print(f"  Ankauf n {n} E-69 {e69}:", zeig(replace(ANK, steuer=s, haltedauer=n, begruendungen=GR), extra=gew))
    for n in (36, 37, 38):
        for e69 in (False, True):
            s = A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True, kuerzung_bleibt_verkaufsjahr=e69)
            print(f"  gefoerdert n {n} E-69 {e69}:", zeig(replace(GEF, steuer=s, haltedauer=n, begruendungen=GR), kat=KATN,
                  extra=lambda e: gew(e) + f" Rueckzahlung {de(e.verkauf.foerder_rueckzahlung)}"))
    s = A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=False, kuerzung_bleibt_verkaufsjahr=True)
    print("  E-69 ja ohne E-41:", zeig(replace(ANK, steuer=s, begruendungen=GR)))
    s = A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=False, kuerzung_bleibt_verkaufsjahr=True)
    print("  E-69 ja ohne E-41, ohne Begruendung:", zeig(replace(ANK, steuer=s)))
    s = A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True, kuerzung_bleibt_verkaufsjahr=True)
    print("  E-69 ja ohne Begruendung:", zeig(replace(ANK, steuer=s)))
    s = A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True, kuerzung_bleibt_verkaufsjahr=True)
    print("  E-69 ja ohne Begruendung, Preissuche:", tp(replace(ANK, steuer=s)))
    s = A.steuer(PRIVAT, kuerzung_bleibt_verkaufsjahr=True)
    print("  E-69 ja bei Privatperson:", zeig(replace(ANK, steuer=s, begruendungen=GR)))
    s = A.steuer(GEPRAEGTE_PG, erweiterte_kuerzung=True, kuerzung_bleibt_verkaufsjahr=True)
    print("  E-69 geprägte PG n 1:", zeig(replace(ANK, steuer=s, haltedauer=1, begruendungen=GR), extra=gew))
if "F" in w:
    print("== GF3-F E-70 und Bindungsdauer")
    priv = replace(GEF, steuer=A.steuer(PRIVAT))
    for bj in (5, 6, 35):
        for n in (5, 6, 7, 38):
            print(f"  Privat, Bindung {bj}, n {n}, E-70:", zeig(replace(priv, zuschuss_verteilung=True, haltedauer=n, begruendungen=GR,
                  foerderung=replace(A.FOERDERUNG_B, bindung_jahre=bj)), kat=KATN, extra=lambda e: f"Lesart {e.zuschuss_lesart} Rueck {de(e.verkauf.foerder_rueckzahlung)}"))
    print("  Privat, E-70 ohne Begruendung:", zeig(replace(priv, zuschuss_verteilung=True), kat=KATN))
    print("  Privat, E-70 im Ankauf:", zeig(replace(ANK, steuer=A.steuer(PRIVAT), zuschuss_verteilung=True)))
    print("  Privat, E-70 im Neubau ohne Foerderung:", zeig(replace(NB, steuer=A.steuer(PRIVAT), zuschuss_verteilung=True), kat=KATN))
    print("  Koerperschaft, E-70:", zeig(replace(GEF, zuschuss_verteilung=True, begruendungen=GR), kat=KATN))
    print("  KAT-19 fehlt, Privat, E-70:", zeig(replace(priv, zuschuss_verteilung=True, begruendungen=GR), kat=replace(KATN, vorauszahlung_jahre=None)))
if "G" in w:
    print("== GF3-G feste Werte im Vorhaben (M-20)")
    for feld, wert in (("a_lang", D("0.005")), ("kk_zins", D("0.07")), ("kk_linie", D(100000)), ("vfe_satz", D("0.02")),
                       ("ma031_zuschuss", "sofort"), ("ma026_ertrag_vorhaben", True), ("ma038_rueckfuehrung", False),
                       ("anpassungsdauer", 2), ("forderungsausfall", D("0.01")), ("bodenanteil", D("0.3")),
                       ("suchraster", 10), ("bauabschnitt_rohbau", D("0.6")), ("bereit_frei", 3), ("bereit_satz", D("0.001")),
                       ("vorlauf", 6), ("zielrendite", D("0.04")), ("leerstand", D("0.03")), ("instandhaltung_staffel", [(0, D(5))]),
                       ("foo", 1)):
        ab = {feld: (wert, "Test")}
        print(f"  Vorhaben setzt {feld}={wert}:", zeig(replace(ANK, abweichungen=ab)))
    # H-38 und MA-036 stehen in den Steuerparametern der Eingabe
    s = A.steuer(KOERPERSCHAFT, verlust="sofort")
    e = replace(ANK, steuer=s, stau_betrag=D(400000), stau_jahr=1)
    print("  Eingabe setzt steuer.verlust=sofort:", zeig(e, extra=lambda g: str([(a['kennung'], a['begruendung']) for a in g.abweichungen])))
    s = A.steuer(GEWERBLICHE_PG, aufgabegewinn=True)
    print("  Eingabe setzt steuer.aufgabegewinn=True:", zeig(replace(ANK, steuer=s), extra=lambda g: str([(a['kennung'], a['begruendung']) for a in g.abweichungen])))
    s = replace(A.steuer(KOERPERSCHAFT), hebesatz=D("2.0"))
    print("  Eingabe setzt steuer.hebesatz=200 % (Katalogwert):", zeig(replace(ANK, steuer=s), extra=lambda g: str([(a['kennung'], a['begruendung']) for a in g.abweichungen])))
    print("  E-05 im Neubau gesetzt:", zeig(replace(NB, im_bremsgebiet=False, im_kappungsgebiet=False), kat=KATN))
    print("  E-12 bei Koerperschaft gesetzt (0,9):", zeig(replace(ANK, bodenanteil=D("0.9"))))
