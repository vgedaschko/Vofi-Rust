"""Referenzfaelle RF-11 bis RF-14: Grobkalkulation 1a (Ankauf, Neubau, Steuerstatus) und Randfaelle.

Eigene Faelle ohne veroeffentlichte Werte: Die Sollwerte sind in erwartete_werte.json festgeschrieben (R-15.2);
der Basisfall des Ankaufs ist zusaetzlich in gegenrechnung.py unabhaengig nachgebaut.
"""
from decimal import Decimal as D
from dataclasses import replace
from zahlen import NULL, EINS, d, de, proz, Rundung
from steuer import KOERPERSCHAFT, GEWERBLICHE_PG, EINZELUNTERNEHMEN, PRIVAT, BEFREIT
from kennzahlen import interner_zinsfuss, schuldendienstdeckung
from grobkalkulation import (rechne_grob, tragbarer_preis, zielwertsuche, suche_eingabe, haltedauer_tabelle,
                             vergleiche, Meldung)
from finanzplan import verdichte
import annahmen as A
from rf_rahmen import (fall, pruefe, pruefe_fest, pruefe_proz, pruefe_reihe, pruefe_gleich, info, jahresplan,
                       lehrbuch_steuer)
from rf_testfall import s1


def blatt(k, name, e, kurz=False):
    """Schreibt die Groessen des verkuerzten Kennzahlenblatts fest (R-11.12)."""
    kz = e.kennzahlen
    pruefe_gleich(k, f"{name}: alle Kontrollsummen bestanden", len(e.befunde), 0)
    pruefe_fest(k, f"{name}: Bankdarlehen", e.darlehen)
    pruefe_fest(k, f"{name}: bindende Grenze des Darlehens", e.bemessung.bank["bindend"])
    pruefe_fest(k, f"{name}: Eigenkapital der Investitionsphase", e.eigenkapital_investitionsphase)
    pruefe_fest(k, f"{name}: Endwert", e.plan.endwert)
    pruefe_fest(k, f"{name}: Endwert der Unterlassensalternative", e.alt.endwert)
    pruefe_fest(k, f"{name}: Endwertdifferenz", kz["endwertdifferenz"])
    pruefe_fest(k, f"{name}: VOFI-Rendite (%)", None if kz["rendite"] is None else kz["rendite"] * 100, 3)
    if kurz:
        return
    pruefe_fest(k, f"{name}: Vergleichsrendite (%)", kz["vergleichsrendite"] * 100, 3)
    pruefe_fest(k, f"{name}: Abstand zur Zielrendite (Prozentpunkte)", kz["abstand_zielrendite"] * 100, 3)
    pruefe_fest(k, f"{name}: Endwertueberschuss", kz["endwertueberschuss"])
    pruefe_fest(k, f"{name}: Nachschussbedarf nach der Investitionsphase", e.nachschuss_spaeter)
    pruefe_fest(k, f"{name}: Schuldendienstdeckung im ersten Jahr der Vollvermietung", e.dscr_vj, 4)
    pruefe_fest(k, f"{name}: Beleihungsauslauf (%)", e.beleihungsauslauf * 100, 2)
    pruefe_fest(k, f"{name}: Einstiegsfaktor", e.einstiegsfaktor, 2)
    pruefe_fest(k, f"{name}: Ausstiegsfaktor", e.ausstiegsfaktor, 2)
    pruefe_fest(k, f"{name}: Nettoanfangsrendite (%)", e.nettoanfangsrendite * 100, 2)
    pruefe_fest(k, f"{name}: Restwertanteil am Endwert (%)", None if e.restwertanteil is None else e.restwertanteil * 100, 2)
    pruefe_fest(k, f"{name}: Verkaufspreis brutto", e.verkauf.preis_brutto)


def rf11_ankauf():
    k = fall("RF-11", "Grobkalkulation Ankauf (Monatsraster, Koerperschaft; Vorgaben und Katalog als Annahme)")
    e = rechne_grob(A.ANKAUF, A.VORGABEN)
    blatt(k, "Basisfall", e)
    pruefe_fest(k, "Basisfall: Reinertrag im ersten Jahr", e.bemessung.reinertrag_vj)
    pruefe_fest(k, "Basisfall: Miete je m2 und Monat, Jahre 1 bis 6", [str(x.quantize(D("0.0001"))) for x in e.miete_je_qm[1:7]])
    j = verdichte(e.plan)
    pruefe_fest(k, "Basisfall: Jahresmiete Jahr 1 (Einzahlung nach Mietausfall)", j[1]["miete"])
    pruefe_fest(k, "Basisfall: Bewirtschaftung Jahr 1", j[1]["kosten"])
    pruefe_fest(k, "Basisfall: Investitionsstau, Zahlung in Jahr 2 (Preisstand 1,03^2)", j[2]["erhaltung"])
    pruefe_fest(k, "Basisfall: Steuer Jahre 1 bis 4", [str(x["steuer"]) for x in j[1:5]])
    pruefe_fest(k, "Basisfall: Rate ab Jahr 11 nach Anschlusszins (Jahressumme)", j[11]["zins"] + j[11]["tilgung"])
    pruefe_fest(k, "Basisfall: Steuer auf den Verkaufsgewinn", e.steuer_verkaufsgewinn)
    info(f"Endwert {de(e.plan.endwert)}, Endwertdifferenz {de(e.kennzahlen['endwertdifferenz'])}, "
         f"Rendite {proz(e.kennzahlen['rendite'])}, Darlehen {de(e.darlehen)} {e.bemessung.bank['bindend']}")
    # kombinierter Stressfall: Darlehen aus dem Basisfall (R-11.8)
    es = rechne_grob(A.ANKAUF, A.VORGABEN, stress=True)
    blatt(k, "kombinierter Stressfall", es)
    pruefe_gleich(k, "Stressfall: Bankdarlehen unveraendert aus dem Basisfall", es.darlehen == e.darlehen, True)
    # hoechster tragbarer Preis
    tp = tragbarer_preis(A.ANKAUF, A.VORGABEN)
    pruefe_fest(k, "hoechster tragbarer Kaufpreis (Basisfall)", tp["preis"], 0)
    pruefe_gleich(k, "tragbarer Preis: bindende Grenze", tp["bindend"], "Rendite")
    pruefe_fest(k, "tragbarer Preis: Grenze, die das Darlehen bestimmt", tp["ergebnis"].bemessung.bank["bindend"])
    pruefe_fest(k, "tragbarer Preis: noetiges Eigenkapital", tp["ergebnis"].eigenkapital_investitionsphase)
    ob = rechne_grob(A.ANKAUF, A.VORGABEN, preis=tp["preis"] + 1, mit_blatt=False)
    pruefe_gleich(k, "Probe P-14: Rendite beim tragbaren Preis >= Ziel und einen Euro darueber < Ziel",
                  tp["ergebnis"].kennzahlen["rendite"] >= A.VORGABEN.zielrendite > ob.kennzahlen["rendite"], True)
    pruefe_gleich(k, "tragbarer Preis: genau eine Loesung im Suchbereich", tp["suche"]["status"], "eine Loesung")
    tps = tragbarer_preis(A.ANKAUF, A.VORGABEN, stress=True)
    pruefe_fest(k, "hoechster tragbarer Kaufpreis im kombinierten Stressfall", tps["preis"], 0)
    pruefe_fest(k, "... Grenze, die das Darlehen bestimmt", tps["ergebnis"].bemessung.bank["bindend"])
    pruefe_fest(k, "... Schuldendienstdeckung im Stressfall", tps["ergebnis"].dscr_vj, 4)
    tpe = tragbarer_preis(replace(A.ANKAUF, verfuegbares_ek=D(900000)), A.VORGABEN)
    pruefe_fest(k, "tragbarer Preis bei 900.000 Euro verfuegbarem Eigenkapital", tpe["preis"], 0)
    pruefe_gleich(k, "... bindende Grenze", tpe["bindend"], "Eigenkapital")
    # Monotonie am Knick zwischen Beleihungsquote und Mindestdeckung (R-11.5)
    knick = int(e.bemessung.bank["b"] / A.VORGABEN.beleihungsquote)
    r = [rechne_grob(A.ANKAUF, A.VORGABEN, preis=knick + dx, mit_blatt=False).kennzahlen["rendite"]
         for dx in (-20000, -10000, 0, 10000, 20000)]
    pruefe_gleich(k, f"Rendite faellt beiderseits des Knicks bei {knick} streng", all(b < a for a, b in zip(r, r[1:])), True)
    info("Rendite um den Knick (je 10.000 Euro): " + " / ".join(proz(x, 4) for x in r))
    info(f"Steigung links {de((r[2] - r[1]) * 10000, 4)}, rechts {de((r[3] - r[2]) * 10000, 4)} Basispunkte je 10.000 Euro")
    preise = range(1500000, 3600001, 100000)
    rs = [rechne_grob(A.ANKAUF, A.VORGABEN, preis=x, mit_blatt=False).kennzahlen["rendite"] for x in preise]
    pruefe_gleich(k, "Rendite faellt von 1,5 bis 3,6 Mio. Euro streng mit dem Preis", all(b < a for a, b in zip(rs, rs[1:])), True)
    # Zielwertsuche auf gekennzeichnete Eingaben (R-11.9, R-11.10)
    teuer = replace(A.ANKAUF, kaufpreis=D(2600000))
    s = suche_eingabe(teuer, A.VORGABEN, "markt_miete", D("6.00"), D("20.00"), D("0.01"))
    pruefe_gleich(k, "Zielwertsuche Marktmiete bei 2,6 Mio. Euro: Status", s["status"], "eine Loesung")
    pruefe_fest(k, "Zielwertsuche: noetige Marktmiete", s["loesungen"][0]["wert"])
    s = suche_eingabe(A.ANKAUF, A.VORGABEN, "stau_betrag", D(0), D(1000000), D(100))
    pruefe_fest(k, "Zielwertsuche: tragbarer Investitionsstau beim Kaufpreis 2,4 Mio. Euro", s["loesungen"][0]["wert"])
    s = suche_eingabe(A.ANKAUF, A.VORGABEN, "verkaufsfaktor", D(8), D(40), D("0.01"))
    pruefe_fest(k, "Zielwertsuche: kritischer Verkaufsfaktor", s["loesungen"][0]["wert"])
    s = suche_eingabe(teuer, A.VORGABEN, "markt_miete", D("6.00"), D("9.00"), D("0.01"))
    pruefe_gleich(k, "Zielwertsuche ohne Loesung im Bereich", s["status"], "keine Loesung: Ziel im ganzen Bereich verfehlt")
    s = zielwertsuche(lambda x: (x - 3) * (x - 7), 0, 10, D("0.01"))
    pruefe_gleich(k, "Zielwertsuche auf eine nicht monotone Funktion: beide Loesungen gemeldet",
                  (s["status"], [str(l["wert"]) for l in s["loesungen"]]), ("2 Loesungen", ["3.00", "7.00"]))
    try:
        suche_eingabe(A.ANKAUF, A.VORGABEN, "haltedauer", 1, 30, 1)
        m = None
    except Meldung as x:
        m = x.kennung
    pruefe_gleich(k, "Zielwertsuche auf die Haltedauer ist nicht zugelassen", m, "M-30")
    # Varianten des Darlehens: gelockerte Tilgung, andere Lesart, uebernommenes Darlehen, Wertansatz
    gebunden = replace(A.ANKAUF, gebunden_anteil=D("0.4"), bindung_jahre=6, gebundene_miete=D("6.80"),
                       geb_steigerung=D("0.0615"),
                       uebernommen=dict(restschuld=D(500000), zins=D("0.005"), tilgungssatz=D("0.02"),
                                        bindung_jahre=8, anschluss_zins=D("0.03")))
    eg = rechne_grob(gebunden, A.VORGABEN)
    blatt(k, "Ankauf gebundener Bestand mit uebernommenem Darlehen", eg, kurz=True)
    pruefe_fest(k, "gebundener Bestand: Miete je m2, Jahre 1 bis 10", [str(x.quantize(D("0.0001"))) for x in eg.miete_je_qm[1:11]])
    pruefe_fest(k, "gebundener Bestand: Kapitaldienst des uebernommenen Darlehens im ersten Jahr", eg.bemessung.kd_uebrige)
    eg2 = rechne_grob(gebunden, replace(A.VORGABEN, nur_eigenes_darlehen=True))
    pruefe_fest(k, "gebundener Bestand, andere Lesart MA-026: Bankdarlehen", eg2.darlehen)
    pruefe_gleich(k, "andere Lesart MA-026 ergibt das hoehere Darlehen", eg2.darlehen > eg.darlehen, True)
    # Vergleich zweier Fassungen (R-11.11): frei und gebunden
    v = vergleiche(e, eg)
    pruefe_fest(k, "Vergleich zweier Fassungen: Differenz der Endwertdifferenz (gebunden - frei)", v[1][3])
    # Haltedauertabelle (R-11.13)
    tab = haltedauer_tabelle(A.ANKAUF, A.VORGABEN, 8, 13)
    pruefe_fest(k, "Haltedauertabelle 8 bis 13 Jahre: VOFI-Rendite (%)", [str((x[3] * 100).quantize(D("0.001"))) for x in tab])


def rf12_neubau():
    k = fall("RF-12", "Grobkalkulation Neubau in Grobform (frei finanziert und mit Grobfoerderung)")
    n = rechne_grob(A.NEUBAU, A.VORGABEN_NEUBAU)
    blatt(k, "Neubau frei finanziert", n)
    z = n.plan.zeilen
    pruefe_fest(k, "Neubau: Baukosten", n.bemessung.baukosten)
    pruefe_fest(k, "Neubau: Mittelbedarf ohne Bauzeitzinsen", n.bemessung.mittelbedarf)
    pruefe_fest(k, "Neubau: Bauzeitzinsen (Summe der Zinsen in der Bauzeit)", sum(x["zins"] for x in z[1:19]))
    pruefe_fest(k, "Neubau: Monat der ersten Auszahlung des Bankdarlehens", min(u for u in range(19) if z[u]["auszahlung"] > 0))
    pruefe_fest(k, "Neubau: Abschreibung im Planjahr 2 (sechs Monate)", z[24]["afa"])
    tp = tragbarer_preis(A.NEUBAU, A.VORGABEN_NEUBAU)
    pruefe_fest(k, "Neubau: hoechster tragbarer Grundstueckspreis", tp["preis"], 0)
    pruefe_fest(k, "Neubau: Meldung der Preissuche", tp["meldung"])
    ns = rechne_grob(A.NEUBAU, A.VORGABEN_NEUBAU, stress=True)
    blatt(k, "Neubau kombinierter Stressfall", ns, kurz=True)
    pruefe_gleich(k, "Neubau Stressfall: Mehrkosten traegt das Eigenkapital",
                  ns.eigenkapital_investitionsphase > n.eigenkapital_investitionsphase and ns.darlehen == n.darlehen, True)
    gef = replace(A.NEUBAU, foerderung=A.FOERDERUNG_B, haltedauer=20)
    f = rechne_grob(gef, A.VORGABEN_NEUBAU)
    blatt(k, "Neubau mit Grobfoerderung, Verkauf nach 20 Jahren", f)
    bm = f.bemessung
    pruefe_fest(k, "Grobfoerderung: Foerderdarlehen", bm.foerderdarlehen)
    pruefe_fest(k, "Grobfoerderung: Zuschuss", bm.zuschuss)
    pruefe_fest(k, "Grobfoerderung: Mindesteigenkapital", bm.ek_min)
    pruefe_fest(k, "Grobfoerderung: einbehaltene Entgelte", bm.einbehalt_darlehen + bm.einbehalt_zuschuss)
    pruefe_fest(k, "Grobfoerderung: Kapitaldienst des Foerderdarlehens im Jahr", bm.kd_uebrige)
    pruefe_gleich(k, "Grobfoerderung: Meldung M-21 (Reinertrag deckt den Kapitaldienst des Foerderdarlehens nicht)", bm.bank["meldung"], "M-21")
    pruefe_fest(k, "Grobfoerderung: Rueckzahlung des Zuschusses beim Verkauf (MA-017)", f.verkauf.foerder_rueckzahlung)
    pruefe_fest(k, "Grobfoerderung: Abloesung des Foerderdarlehens beim Verkauf", f.plan.zeilen[240]["tranchen"]["Foerderdarlehen"]["abloesung"])
    pruefe_fest(k, "Grobfoerderung: Miete je m2, Vermietungsjahre 1 bis 8", [str(x.quantize(D("0.0001"))) for x in f.miete_je_qm[1:9]])
    f2 = rechne_grob(gef, replace(A.VORGABEN_NEUBAU, nur_eigenes_darlehen=True))
    pruefe_fest(k, "Grobfoerderung, andere Lesart MA-026: Bankdarlehen", f2.darlehen)
    pruefe_gleich(k, "... bindende Grenze ist die Restfinanzierung", f2.bemessung.bank["bindend"], ["c"])
    pruefe_gleich(k, "... Kontrollsummen", len(f2.befunde), 0)
    v = vergleiche(rechne_grob(replace(A.NEUBAU, haltedauer=20), A.VORGABEN_NEUBAU), f)
    pruefe_fest(k, "Vergleich frei gegen gefoerdert (20 Jahre): Differenz der Endwertdifferenz", v[1][3])


def rf13_steuerstatus():
    k = fall("RF-13", "Grobkalkulation Ankauf je Steuerstatus (derselbe Fall, angenommener Katalogstand)")
    faelle = (("Koerperschaft", A.steuer(KOERPERSCHAFT)),
              ("Koerperschaft mit erweiterter Kuerzung", A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True)),
              ("Koerperschaft, Verluste sofort verrechnet", A.steuer(KOERPERSCHAFT, verlust="sofort")),
              ("gewerbliche Personengesellschaft, Hebesatz 400 %", A.steuer(GEWERBLICHE_PG)),
              ("gewerbliche Personengesellschaft, Hebesatz 440 %", A.steuer(GEWERBLICHE_PG, hebesatz=D("4.40"))),
              ("gewerbliche Personengesellschaft, 440 %, natuerliche Personen 60 %",
               A.steuer(GEWERBLICHE_PG, hebesatz=D("4.40"), anteil_natuerliche=D("0.6"))),
              ("gewerbliche Personengesellschaft, 440 %, mit Kuerzung",
               A.steuer(GEWERBLICHE_PG, hebesatz=D("4.40"), erweiterte_kuerzung=True)),
              ("Einzelunternehmen mit Betriebsvermoegen, Hebesatz 440 %", A.steuer(EINZELUNTERNEHMEN, hebesatz=D("4.40"))),
              ("Privatperson, Verkauf nach 12 Jahren", A.steuer(PRIVAT)),
              ("befreite Koerperschaft", A.steuer(BEFREIT)))
    for name, st in faelle:
        e = rechne_grob(replace(A.ANKAUF, steuer=st), A.VORGABEN)
        kz = e.kennzahlen
        pruefe_gleich(k, f"{name}: Kontrollsummen", len(e.befunde), 0)
        pruefe_fest(k, f"{name}: Endwert", e.plan.endwert)
        pruefe_fest(k, f"{name}: Endwertdifferenz", kz["endwertdifferenz"])
        pruefe_fest(k, f"{name}: VOFI-Rendite (%)", kz["rendite"] * 100, 3)
        pruefe_fest(k, f"{name}: Vergleichsrendite (%)", kz["vergleichsrendite"] * 100, 3)
        pruefe_fest(k, f"{name}: Summe der Steuerzahlungen", sum(e.plan.reihe("steuer")))
    p10 = rechne_grob(replace(A.ANKAUF, steuer=A.steuer(PRIVAT), haltedauer=10), A.VORGABEN)
    p11 = rechne_grob(replace(A.ANKAUF, steuer=A.steuer(PRIVAT), haltedauer=11), A.VORGABEN)
    pruefe_fest(k, "Privatperson, Verkauf nach 10 Jahren: Steuer auf den Verkaufsgewinn", p10.steuer_verkaufsgewinn)
    pruefe(k, "Privatperson, Verkauf nach 11 Jahren: Steuer auf den Verkaufsgewinn", p11.steuer_verkaufsgewinn, "0", "0")
    tab = haltedauer_tabelle(replace(A.ANKAUF, steuer=A.steuer(PRIVAT)), A.VORGABEN, 9, 12)
    pruefe_fest(k, "Privatperson, Haltedauertabelle 9 bis 12 Jahre: Rendite (%)", [str((x[3] * 100).quantize(D("0.001"))) for x in tab])


def rf14_randfaelle():
    k = fall("RF-14", "Randfaelle mit definiertem Ergebnis (Kapitel 14)")
    # R-14.1 Zinssaetze null
    plan, alt, kz = s1(h="0", kk="0", zins="0")
    pruefe(k, "alle Zinssaetze null: Endwert der Unterlassensalternative = Eigenkapital", alt.endwert, "400000", "0")
    pruefe_proz(k, "alle Zinssaetze null: Vergleichsrendite", kz["vergleichsrendite"], "0.000")
    pruefe_fest(k, "alle Zinssaetze null: Endwert", plan.endwert)
    # R-14.2 Eigenkapital null
    plan, alt, kz = s1(ek=0)
    pruefe_gleich(k, "Eigenkapital null: Rendite nicht definiert", kz["rendite"], None)
    pruefe_gleich(k, "Eigenkapital null: Status", kz["rendite_status"], "nicht definiert (kein Eigenkapital)")
    pruefe_fest(k, "Eigenkapital null: Endwert = Endwertdifferenz", plan.endwert)
    pruefe(k, "Eigenkapital null: Endwert der Unterlassensalternative", alt.endwert, "0", "0")
    # R-14.3 negativer Endwert
    plan, alt, kz = s1(verkauf=500000)
    pruefe_gleich(k, "negativer Endwert: Rendite -100 %", kz["rendite"], D(-1))
    pruefe_fest(k, "negativer Endwert: Endwert", plan.endwert)
    pruefe_gleich(k, "negativer Endwert: Kontrollsummen bestehen", len(__import__("proben").pruefe_plan(plan, alt)), 0)
    # R-14.4 Haltedauer endet vor der Vollvermietung
    try:
        rechne_grob(replace(A.NEUBAU, haltedauer=2), A.VORGABEN_NEUBAU)
        m = None
    except Meldung as x:
        m = x.kennung
    pruefe_gleich(k, "Neubau, Haltedauer 2 Jahre bei 18 Monaten Bauzeit: Meldung", m, "M-23")
    n3 = rechne_grob(replace(A.NEUBAU, haltedauer=3), A.VORGABEN_NEUBAU)
    pruefe_fest(k, "Neubau, Haltedauer 3 Jahre: Endwert", n3.plan.endwert)
    pruefe_gleich(k, "Neubau, Haltedauer 3 Jahre: Kontrollsummen", len(n3.befunde), 0)
    # R-14.5 Verkauf im ersten Jahr
    e1 = rechne_grob(replace(A.ANKAUF, haltedauer=1, stau_betrag=NULL), A.VORGABEN)
    pruefe_fest(k, "Ankauf, Verkauf nach einem Jahr: Endwert", e1.plan.endwert)
    pruefe_fest(k, "Ankauf, Verkauf nach einem Jahr: Rendite (%)", e1.kennzahlen["rendite"] * 100, 3)
    pruefe_fest(k, "Ankauf, Verkauf nach einem Jahr: Vorfaelligkeitsentschaedigung (neun Jahre Restbindung)", e1.plan.zeilen[12]["vfe"])
    pruefe_gleich(k, "Ankauf, Verkauf nach einem Jahr: Kontrollsummen", len(e1.befunde), 0)
    # R-14.6 Investitionsstau nach dem Verkauf: Abzug vom Verkaufserloes zum Preisstand des Stichtags
    spaet = rechne_grob(replace(A.ANKAUF, haltedauer=10, stau_betrag=D(100000), stau_jahr=12), A.VORGABEN)
    pruefe(k, "Stau 100.000 geplant fuer Jahr 12, Verkauf in Jahr 10: Abzug", spaet.verkauf.stau_abzug, "134391.64", "0.01")
    pruefe_gleich(k, "... Kontrollsummen einschliesslich P-05 und P-06", len(spaet.befunde), 0)
    # R-14.7 Ueberfinanzierung
    try:
        rechne_grob(replace(A.ANKAUF, uebernommen=dict(restschuld=D(3000000), zins=D("0.01"), tilgungssatz=D("0.02"))), A.VORGABEN)
        m = None
    except Meldung as x:
        m = x.kennung
    pruefe_gleich(k, "uebernommenes Darlehen ueber dem Mittelbedarf: Meldung", m, "M-22")
    # R-14.8 Mietausfall 100 %: kein Ertrag, Bankdarlehen null
    leer = rechne_grob(A.ANKAUF, replace(A.VORGABEN, mietausfall=D(1)))
    pruefe(k, "Mietausfall 100 %: Bankdarlehen", leer.darlehen, "0", "0")
    pruefe_gleich(k, "Mietausfall 100 %: Schuldendienstdeckung nicht definiert (kein Kapitaldienst)", leer.dscr_vj, None)
    pruefe_gleich(k, "Mietausfall 100 %: Kontrollsummen", len(leer.befunde), 0)
    pruefe_fest(k, "Mietausfall 100 %: Nachschussbedarf", leer.nachschuss_spaeter)
    # R-14.9 kein tragbarer Preis / Preis ueber dem Suchbereich
    tp = tragbarer_preis(replace(A.ANKAUF, stau_betrag=D(6000000), stau_jahr=0), A.VORGABEN)
    pruefe_gleich(k, "Stau 6 Mio. Euro zum Stichtag: kein tragbarer Preis", (tp["preis"], tp["meldung"]), (None, "M-32"))
    tp = tragbarer_preis(A.ANKAUF, replace(A.VORGABEN, zielrendite=D("-0.5")))
    pruefe_gleich(k, "Zielrendite -50 %: Ziel im ganzen Suchbereich erreicht", (tp["preis"], tp["meldung"]), (None, "M-33"))
    # R-14.10 interner Zinsfuss mehrdeutig und ohne Loesung
    loes, wechsel = interner_zinsfuss([D(-1000), D(5000), D(-6000)])
    pruefe_gleich(k, "interner Zinsfuss -1.000 / +5.000 / -6.000: zwei Vorzeichenwechsel", wechsel, 2)
    pruefe_reihe(k, "... beide Loesungen 100 % und 200 %", loes, ["1", "2"], "0.000001")
    loes, wechsel = interner_zinsfuss([D(-1000), D(-50), D(-20)])
    pruefe_gleich(k, "interner Zinsfuss ohne Vorzeichenwechsel: keine Loesung", (loes, wechsel), ([], 0))
    # R-14.11 langer Zeitraum: 42 Jahre im Monatsraster, Abschreibung aufgebraucht, Zins ab dem 36. Jahr
    lang = rechne_grob(replace(A.NEUBAU, foerderung=A.FOERDERUNG_B, haltedauer=42), A.VORGABEN_NEUBAU)
    pruefe_gleich(k, "42 Jahre, 504 Perioden: Kontrollsummen", len(lang.befunde), 0)
    pruefe_fest(k, "42 Jahre: Endwert", lang.plan.endwert)
    pruefe_fest(k, "42 Jahre: Endwertdifferenz", lang.kennzahlen["endwertdifferenz"])
    pruefe_fest(k, "42 Jahre: VOFI-Rendite (%)", lang.kennzahlen["rendite"] * 100, 3)
    afa = [lang.plan.zeilen[j * 12]["afa"] for j in range(1, 43)]
    pruefe_fest(k, "42 Jahre: letztes Jahr mit Abschreibung", max(j + 1 for j, x in enumerate(afa) if x > 0))
    pruefe(k, "42 Jahre: Rueckzahlung des Zuschusses nach Bindungsende", lang.verkauf.foerder_rueckzahlung, "0", "0")
    zj = [lang.plan.jahressumme("zins", j) for j in range(1, 43)]
    pruefe_fest(k, "42 Jahre: erstes Planjahr mit Zins auf das Foerderdarlehen", min(j + 1 for j, x in enumerate(zj) if x > 0))
    pruefe_fest(k, "42 Jahre: Abloesung des Foerderdarlehens am Ende", lang.plan.zeilen[504]["tranchen"]["Foerderdarlehen"]["abloesung"])
    # R-14.12 Jahresmodus und Monatsraster desselben Ankaufs
    ej = rechne_grob(A.ANKAUF, A.VORGABEN, p=1)
    pruefe_fest(k, "Ankauf im Jahresmodus: Endwert", ej.plan.endwert)
    pruefe_gleich(k, "Ankauf im Jahresmodus: Kontrollsummen", len(ej.befunde), 0)
    em = rechne_grob(A.ANKAUF, A.VORGABEN)
    info(f"Ankauf: Endwert Jahresmodus {de(ej.plan.endwert)}, Monatsraster {de(em.plan.endwert)}; "
         f"Rendite {proz(ej.kennzahlen['rendite'])} gegen {proz(em.kennzahlen['rendite'])}")


def alle():
    rf11_ankauf()
    rf12_neubau()
    rf13_steuerstatus()
    rf14_randfaelle()
