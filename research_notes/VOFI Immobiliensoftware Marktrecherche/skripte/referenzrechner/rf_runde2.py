"""Referenzfaelle zu den Regeln der zweiten Ueberarbeitung (Pruefrunde 2), eingeordnet in RF-11 bis RF-20.

RF-12 Neubau: Vorlauf, Festpreis, Vorvermietung, Kennwert der Gesamtkosten, nachhaltige Miete, KfW-Darlehen nach dem
Merkblatt, Bemessungszins je Tranche, Ergebnis ohne Bankdarlehen · RF-13 Steuerstatus mit Endwerten · RF-16
Fehlerbilder, die die Rechnung veraendern · RF-17 Zuschuss, Verein und Stiftung, Kuerzung · RF-18 Uebermiete,
Gebietsverordnungen, Leerstandskosten, CO2-Kosten · RF-19 Abweichungen vom Hausstandard, Bemessung, Anschluss ·
RF-20 Raender aus dem Bericht "Grenzfaelle" der Pruefrunde 2 (NG-..), Preissuche, Katalog, Vergleich.
Sollwerte mit benanntem Rechenweg oder aus einer Gegenrechnung der Pruefer stehen im Code; die uebrigen sind in
erwartete_werte.json festgeschrieben.
"""
from decimal import Decimal as D
from dataclasses import replace
from zahlen import NULL, EINS, Rundung, FEHLER
from zeit import Raster
from steuer import (Steuer, KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST, GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN,
                    PRIVAT, BEFREIT)
from darlehen import Tranche, bemessungszins, bemessungskapitaldienst
from kennzahlen import schuldendienstdeckung
import grobkalkulation
from grobkalkulation import (rechne_grob, tragbarer_preis, zielwertsuche, suche_eingabe, haltedauer_tabelle, vergleiche,
                             Meldung, kalkuliere, abweichungsliste, preisgrenze, auftragswerte, vorgaben_im_vorhaben)
import annahmen as A
from rf_rahmen import fall, pruefe, pruefe_fest, pruefe_gleich, info
from rf_bausteine import lauf
from rf_grob import VG, KAT, KATN, GEBUNDEN, GEFOERDERT, MIT_KFW, GRUND, proz_fest, kennungen

CENT = Rundung("cent")
OHNE_STAU = replace(A.ANKAUF, stau_betrag=NULL)
GRUNDTEXT = "Begruendung des Referenzfalls"


def q(x, stellen="0.0001"):
    return None if x is None else str(x.quantize(D(stellen)))


def status(ein, vg=VG, kat=KAT, **kw):
    erg = kalkuliere(ein, vg, kat, **kw)
    return [erg["status"], erg["meldungen"][0]["kennung"] if erg["status"] != "ergebnis" else None]


def mit_fehler(name, f):
    FEHLER.add(name)
    try:
        return f()
    finally:
        FEHLER.discard(name)


def proben_von(bef):
    return sorted({b[0] for b in bef})


# ------------------------------------------------------------------------------------------------ RF-12
def rf12_runde2():
    k = fall("RF-12", "Neubau, zweite Ueberarbeitung: Vorlauf, Festpreis, Vorvermietung, KfW nach dem Merkblatt")
    n = rechne_grob(A.NEUBAU, VG, KATN)
    # Vorlauf zwischen Grundstueckskauf und Baubeginn (E-23, R-11.2)
    v = rechne_grob(replace(A.NEUBAU, vorlauf_monate=12), VG, KATN)
    z = v.plan.zeilen
    pruefe_fest(k, "Vorlauf 12 Monate: Baukosten, erste und letzte Monatsrate", [str(v.baukosten), str(z[13]["investition"]), str(z[30]["investition"])])
    pruefe(k, "Vorlauf 12 Monate: Rate im Monat 13 = 7.540.000 / 18 x 1,03^(13/12)", z[13]["investition"],
           str(CENT.geld(D(7540000) / 18 * CENT.satz(D("1.03") ** (D(13) / 12)))), "0")
    pruefe_fest(k, "Vorlauf 12 Monate: erster Monat mit Miete, Bankdarlehen, Eigenkapital der Investitionsphase, Endwert, Rendite (%)",
                [min(u for u in range(1, 80) if z[u]["miete"] > 0), str(v.darlehen), str(v.eigenkapital_investitionsphase),
                 str(v.plan.endwert), q(v.kennzahlen["rendite"] * 100, "0.001")])
    pruefe_gleich(k, "Vorlauf 12 Monate: Kontrollsummen", (v.gesperrt, v.befunde), (False, []))
    pruefe_gleich(k, "Vorlauf 12 Monate, Haltedauer 3 Jahre: M-23", status(replace(A.NEUBAU, vorlauf_monate=12, haltedauer=3), VG, KATN), ["eingabe", "M-23"])
    # Festpreis (E-24): keine Baupreissteigerung; steht mit Begruendung in der Liste
    pruefe_gleich(k, "Festpreis ohne Begruendung: Eingabemeldung", status(replace(A.NEUBAU, festpreis=True), VG, KATN), ["eingabe", "M-20"])
    fp = rechne_grob(replace(A.NEUBAU, festpreis=True, begruendungen=GRUND), VG, KATN)
    pruefe(k, "Festpreis: Baukosten = 18 Raten von runde(7.540.000 / 18) = 418.888,89 Euro", fp.baukosten, "7540000.02", "0")
    pruefe_fest(k, "Festpreis: Endwertdifferenz, Wirkung in der Liste der Abweichungen",
                [str(fp.kennzahlen["endwertdifferenz"]), [[a["kennung"], str(a["wirkung_endwertdifferenz"])] for a in fp.abweichungen]])
    # Vorvermietung (E-39): kein Anlaufleerstand
    vv = rechne_grob(replace(A.NEUBAU, vorvermietet=True, begruendungen=GRUND), VG, KATN)
    pruefe_fest(k, "Vorvermietung: erster Monat mit Miete, laufender Nachschussbedarf, Endwertdifferenz",
                [min(u for u in range(1, 60) if vv.plan.zeilen[u]["miete"] > 0), str(vv.nachschuss_laufend), str(vv.kennzahlen["endwertdifferenz"])])
    # Anlaufleerstand getrennt fuer den Neubau (H-34)
    a1 = rechne_grob(A.NEUBAU, replace(VG, anlaufleerstand_neubau=1), KATN)
    pruefe_gleich(k, "Anlaufleerstand im Neubau ein Monat (H-34), im Ankauf weiter drei (H-28): erste Miete im Monat 20",
                  min(u for u in range(1, 60) if a1.plan.zeilen[u]["miete"] > 0), 20)
    # Kennwert als Gesamtkosten der Kostengruppen 200 bis 700 (E-25)
    kg = rechne_grob(replace(A.NEUBAU, kostenkennwert=D(2900), kennwert_gesamt=True), VG, KATN)
    pruefe(k, "Kennwert 2.900 Euro fuer die Kostengruppen 200 bis 700: Baukosten wie 2.320 Euro mit 25 % Zuschlag", kg.baukosten, str(n.baukosten), "0")
    # Betriebskosten leerstehender Flaechen im Anlaufleerstand (H-36, R-6.17)
    lk = rechne_grob(A.NEUBAU, replace(VG, leerstandskosten_je_qm=D(30)), KATN)
    pruefe(k, "Leerstandskosten 30 Euro je m2 und Jahr: Bewirtschaftung im Monat 19 = 2.762,50 + 2.000 x 30 x 1,02 / 12 (Planjahr 2)",
           lk.plan.zeilen[19]["kosten"], "7862.50", "0")
    pruefe(k, "... ab dem ersten Vermietungsmonat 22 keine Leerstandskosten", lk.plan.zeilen[22]["kosten"], str(n.plan.zeilen[22]["kosten"]), "0")
    pruefe_fest(k, "Leerstandskosten im Anlaufleerstand: laufender Nachschussbedarf, Endwertdifferenz", [str(lk.nachschuss_laufend), str(lk.kennzahlen["endwertdifferenz"])])
    # nachhaltige Miete der Bank im Neubau (E-65)
    nm = rechne_grob(replace(A.NEUBAU, nachhaltige_miete=D("15.00")), VG, KATN)
    pruefe(k, "nachhaltige Miete 15,00 Euro: nachhaltiger Reinertrag 85 % von 360.000 Euro", nm.bemessung.ertrag_nachhaltig, "306000.00", "0")
    pruefe(k, "nachhaltige Miete 15,00 Euro: Bankdarlehen 306.000 / 1,2 / 7 %", nm.darlehen, "3642857.14", "0")
    tpn = tragbarer_preis(replace(A.NEUBAU, nachhaltige_miete=D("15.00")), VG, KATN)
    pruefe_fest(k, "nachhaltige Miete 15,00 Euro: tragbarer Grundstueckspreis", tpn["preis"], 0)
    # ---- KfW-Darlehen nach dem Merkblatt (R-5.19)
    kf = rechne_grob(MIT_KFW, VG, KATN)
    zk = kf.plan.zeilen
    tr = [t for t in kf.plan.e.tranchen if t.name == "KfW-Darlehen"][0]
    pruefe(k, "KfW 3 Mio. Euro, 35 Jahre, ein tilgungsfreies Jahr: Annuitaet ueber 408 Monate zu 2,5 % (Gegenrechnung Fachexperte)",
           zk[tr.tilgungsbeginn]["tranchen"]["KfW-Darlehen"]["rate"], "10922.62", "0")
    pruefe_gleich(k, "KfW: erster Abruf, Tilgungsbeginn zwoelf Monate nach dem ersten Abruf (MA-040), Zahl der Tilgungsraten",
                  (min(tr.auszahlung), tr.tilgungsbeginn - min(tr.auszahlung), tr.laufzeit), (min(tr.auszahlung), 13, 408))
    pruefe(k, "KfW: Bemessungszins bei gleicher Zinsbindung wie das Bankdarlehen = Vertragszins", kf.bemessung.bemessungszins["KfW-Darlehen"], "0.025", "0")
    pruefe(k, "KfW: kalkulatorischer Kapitaldienst 3 Mio. x (2,5 % + 2 % Mindesttilgung)", kf.bemessung.kd_uebrige, "135000.00", "0")
    pruefe(k, "KfW: Bankdarlehen (336.600 / 1,2 - 135.000) / 7 %", kf.darlehen, "2078571.42", "0")
    pruefe_fest(k, "KfW: Bereitstellungsprovision (0,15 % je Monat ab dem 13. Monat), Summe und Monate",
                [str(sum(zz["tranchen"]["KfW-Darlehen"]["bereit"] for zz in zk)), [u for u in range(1, 40) if zk[u]["tranchen"]["KfW-Darlehen"]["bereit"] > 0]])
    pruefe_fest(k, "KfW: Deckung im ersten Jahr der Vollvermietung, bei voller Tilgung, kleinste Deckung mit Jahr, Deckung nach Bemessung",
                [q(kf.dscr_vj), q(kf.dscr_vj_voll), q(kf.deckung_min), kf.deckung_min_jahr, q(kf.deckung_bemessung)])
    pruefe_fest(k, "KfW: Deckung im ersten Jahr nach jeder Zinsbindung", {a: [j, q(x)] for a, (j, x) in kf.deckung_nach_bindung.items()})
    pruefe_fest(k, "KfW: kleinste Deckung nach der unguenstigsten Anschlussregel; Darlehen zu Gesamtkosten (%); Restschuld und neue Rate nach der Zinsbindung",
                [q(kf.deckung_min_anschluss[0]), kf.deckung_min_anschluss[1], kf.deckung_min_anschluss[2], q(kf.darlehen_zu_wert * 100, "0.01"),
                 str(zk[120]["tranchen"]["KfW-Darlehen"]["rest"]), str(zk[121]["tranchen"]["KfW-Darlehen"]["rate"])])
    # R-5.16 (KFW-297-298-MERKBLATT): das KfW-Darlehen ist nur gegen Vorfaelligkeitsentschaedigung abloesbar
    k8 = rechne_grob(replace(MIT_KFW, haltedauer=8), VG, KATN, _begruendung=False)
    z8 = k8.plan.zeilen[96]["tranchen"]
    soll8 = [CENT.geld(z8[n_]["abloesung"] * VG.vfe_satz * 24 / 12) for n_ in ("Bankdarlehen", "KfW-Darlehen")]
    pruefe(k, "KfW, Verkauf nach 8 Jahren bei 10 Jahren Zinsbindung: Vorfaelligkeit = 1 % x 2 Jahre auf die abgeloeste Restschuld von Bank- und KfW-Darlehen",
           k8.plan.zeilen[96]["vfe"], str(sum(soll8)), "0")
    pruefe_fest(k, "... Vorfaelligkeit des Bankdarlehens und des KfW-Darlehens", [str(x_) for x_ in soll8])
    f20 = rechne_grob(replace(GEFOERDERT, haltedauer=20), VG, KATN, _begruendung=False)
    pruefe_gleich(k, "Foerderdarlehen der NBank, Verkauf nach 20 Jahren in der zinslosen Zeit: keine Vorfaelligkeit", str(f20.plan.zeilen[240]["vfe"]), "0")
    for lz, tf in ((35, 5), (25, 3), (10, 2)):
        e = rechne_grob(replace(MIT_KFW, kfw_laufzeit=lz, kfw_tilgungsfrei=tf), VG, KATN)
        t = [x for x in e.plan.e.tranchen if x.name == "KfW-Darlehen"][0]
        rate = e.plan.zeilen[t.tilgungsbeginn]["tranchen"]["KfW-Darlehen"]["rate"] if t.tilgungsbeginn <= 180 else None
        pruefe_fest(k, f"KfW-Variante {lz} Jahre mit {tf} tilgungsfreien Jahren: Rate, kalkulatorischer Kapitaldienst, Bankdarlehen, Endwertdifferenz",
                    [str(rate), str(e.bemessung.kd_uebrige), str(e.darlehen), str(e.kennzahlen["endwertdifferenz"])])
    pruefe(k, "KfW-Variante 35 / 5: Annuitaet ueber 360 Monate (Gegenrechnung Fachexperte)",
           CENT.geld(Tranche.annuitaet(D(3000000), D("0.025") / 12, 360)), "11853.63", "0")
    pruefe(k, "KfW-Variante 25 / 3: Annuitaet ueber 264 Monate (Gegenrechnung Fachexperte)",
           CENT.geld(Tranche.annuitaet(D(3000000), D("0.025") / 12, 264)), "14785.20", "0")
    pruefe(k, "KfW-Variante 10 / 2: Annuitaet ueber 96 Monate (Gegenrechnung Fachexperte)",
           CENT.geld(Tranche.annuitaet(D(3000000), D("0.025") / 12, 96)), "34511.53", "0")
    pruefe_gleich(k, "KfW-Variante 35 Jahre mit 6 tilgungsfreien Jahren gibt es nicht: M-20",
                  status(replace(MIT_KFW, kfw_tilgungsfrei=6), VG, KATN), ["eingabe", "M-20"])
    pruefe_gleich(k, "KfW 3.000.001 Euro ohne Qualitaetssiegel: M-20; 4,5 Mio. Euro mit Qualitaetssiegel: gerechnet",
                  [status(replace(MIT_KFW, kfw_betrag=D(3000001)), VG, KATN)[1], status(replace(MIT_KFW, kfw_betrag=D(4500000), kfw_qng=True), VG, KATN)[0]],
                  ["M-20", "ergebnis"])
    pruefe_gleich(k, "KfW-Darlehen ohne Konditionen im Katalog (KAT-15): M-47", status(MIT_KFW, VG, replace(KATN, kfw=None)), ["eingabe", "M-47"])
    ab = rechne_grob(MIT_KFW, replace(VG, ma040_ab_abruf=False), KATN)
    t = [x for x in ab.plan.e.tranchen if x.name == "KfW-Darlehen"][0]
    pruefe_fest(k, "KfW, andere Lesart MA-040 (tilgungsfreie Jahre ab der Bezugsfertigkeit): Tilgungsbeginn, Deckung im ersten Jahr, bei voller Tilgung, Endwertdifferenz",
                [t.tilgungsbeginn, q(ab.dscr_vj), q(ab.dscr_vj_voll), str(ab.kennzahlen["endwertdifferenz"])])
    tpa = tragbarer_preis(MIT_KFW, replace(VG, ma040_ab_abruf=False), KATN)
    tpk = tragbarer_preis(MIT_KFW, VG, KATN)
    pruefe_fest(k, "MA-040 in beide Richtungen: tragbarer Grundstueckspreis ab dem ersten Abruf (Voreinstellung) und ab der Bezugsfertigkeit",
                [tpk["preis"], tpa["preis"]])
    pruefe_gleich(k, "MA-040: die Voreinstellung zeigt die niedrigere Deckung im ersten Jahr (Massstab der Bank), aber nicht den niedrigeren Preis (Ausnahme)",
                  (kf.dscr_vj < ab.dscr_vj, tpk["preis"] <= tpa["preis"]), (True, False))
    kz3 = rechne_grob(replace(MIT_KFW, kfw_zins=D("0.03"), voreinstellungen={"kfw_zins": (D("0.025"), "KAT-15")}), VG, KATN)
    pruefe_fest(k, "KfW-Zins 3 % als Eingabe statt 2,5 % aus dem Katalog: Liste der Abweichungen, kalkulatorischer Kapitaldienst",
                [[[a["kennung"], str(a["wirkung_endwertdifferenz"])] for a in kz3.abweichungen], str(kz3.bemessung.kd_uebrige)])
    pruefe_gleich(k, "KfW: letzter Abruf nach der Abruffrist von zwoelf Monaten: Hinweis M-49", "M-49" in kennungen(kf), True)
    # Bemessungszins je Tranche (R-5.12): Bemessungszeitraum laenger als die Zinsbindung des KfW-Darlehens
    b15 = rechne_grob(MIT_KFW, replace(VG, bemessungszeitraum=15), KATN)
    pruefe(k, "Bemessungszeitraum 15 Jahre (H-32): Bemessungszins (2,5 % x 120 + 5 % x 60) / 180", b15.bemessung.bemessungszins["KfW-Darlehen"],
           "0.033333333333", "0")
    pruefe_fest(k, "Bemessungszeitraum 15 Jahre: kalkulatorischer Kapitaldienst der KfW-Tranche, Bankdarlehen", [str(b15.bemessung.kd_uebrige), str(b15.darlehen)])
    f5 = rechne_grob(MIT_KFW, replace(VG, kalk_zins_kfw=D("0.06"), bemessungszeitraum=15), KATN)
    pruefe(k, "... mit festem kalkulatorischem Zins 6 % fuer das KfW-Darlehen (H-25): (2,5 % x 120 + 6 % x 60) / 180",
           f5.bemessung.bemessungszins["KfW-Darlehen"], "0.036666666667", "0")
    k4 = rechne_grob(MIT_KFW, replace(VG, ma026_fremde_kalkulatorisch=True), KATN)
    pruefe(k, "KfW, Lesart 4 von MA-026 (uebrige Tranchen durchgehend kalkulatorisch): Kapitaldienst 3 Mio. x 7 %, Bankdarlehen wie nach Pruefrunde 1",
           k4.darlehen, "1007142.85", "0")
    tp4 = tragbarer_preis(MIT_KFW, replace(VG, ma026_fremde_kalkulatorisch=True), KATN)
    pruefe_fest(k, "KfW, Lesart 4 von MA-026: tragbarer Grundstueckspreis (strengere Lesart; nach Pruefrunde 1 voreingestellt: 924.244)", tp4["preis"], 0)
    g4 = rechne_grob(GEBUNDEN, replace(VG, ma026_fremde_kalkulatorisch=True), KAT)
    pruefe_fest(k, "gebundener Bestand, Lesart 4 von MA-026: kalkulatorischer Kapitaldienst 600.000 x (3 % + 2 %), Bankdarlehen",
                [str(g4.bemessung.kd_uebrige), str(g4.darlehen)])
    # Ergebnis ohne Bankdarlehen (R-11.15) und Foerderdarlehen in der Bemessung
    f = rechne_grob(GEFOERDERT, VG, KATN)
    fs0 = rechne_grob(GEFOERDERT, VG, KATN, stress=True)
    pruefe(k, "Foerderdarlehen: Bemessungszins null (zinslos ueber den Bemessungszeitraum)", f.bemessung.bemessungszins["Foerderdarlehen"], "0", "0")
    pruefe(k, "Foerderdarlehen: kalkulatorischer Kapitaldienst 12 x runde(5.231.491,40 / 500) + 12 x runde(5.231.491,40 x 0,5 % / 12)",
           f.bemessung.kd_uebrige, "151713.24", "0")
    # ---- Foerderrichtlinie (NBANK-RL-MIETWOHNRAUM-2026 Nr. 4.1, 5.3.5, 5.3.6, 5.5.3): Teilraten, Tilgungsbeginn, Mindesttilgung
    zf = f.plan.zeilen
    fm = f.bemessung.foerderdarlehen + f.bemessung.zuschuss
    kum, stand = [], NULL
    for m_ in range(0, 23):
        stand += zf[m_]["zuschuss"] + zf[m_]["tranchen"]["Foerderdarlehen"]["auszahlung"]
        kum.append(stand)
    pruefe_gleich(k, "Teilraten: bis Monat 9 hoechstens 30 %, bis Monat 14 hoechstens 60 %, bis Monat 21 hoechstens 90 %, im Monat 22 alles",
           [str(kum[9]), str(kum[14]), str(kum[21]), str(kum[22])],
           [str(CENT.geld(fm * D("0.3"))), str(CENT.geld(fm * D("0.6"))), str(CENT.geld(fm * D("0.9"))), str(fm)])
    pruefe_gleich(k, "Teilraten: vor dem Baubeginn fliesst nichts; Darlehen und Zuschuss im gleichen Verhaeltnis (Monat 10)",
                  [str(kum[0]), str(CENT.geld((zf[10]["zuschuss"] + zf[10]["tranchen"]["Foerderdarlehen"]["auszahlung"]) * f.bemessung.foerderdarlehen / fm))],
                  ["0", str(zf[10]["tranchen"]["Foerderdarlehen"]["auszahlung"])])
    pruefe_fest(k, "Zwischenfinanzierung der Teilraten: hoechster Stand, Kontokorrent Ende Monat 9, 14 und 21, nach der letzten Teilrate, Zinsen",
                [str(f.zwischenfinanzierung), str(zf[9]["kk"]), str(zf[14]["kk"]), str(zf[21]["kk"]), str(zf[22]["kk"]), str(sum(x_["kkzins"] for x_ in zf))])
    pruefe_gleich(k, "Teilraten bereit ab Monat 1, 10, 15, 22; im Stressfall (Bauzeit 21 Monate) ab Monat 1, 12, 17, 25",
                  [[m_ for m_, _ in grobkalkulation._foerder_termine(GEFOERDERT, VG, 0, bz, bz)[0]] for bz in (18, 21)], [[1, 10, 15, 22], [1, 12, 17, 25]])
    pruefe_gleich(k, "Zwischenfinanzierung: das Eigenkapital der Investitionsphase bleibt der Ausgleichsposten zuzueglich der Nachschuesse; keine Entnahme",
                  [str(sum(f.plan.e.einlagen)), str(sum(f.plan.entnahmen_netto))], [str(f.ek_soll), "0"])
    tf = [t_ for t_ in f.plan.e.tranchen if t_.name == "Foerderdarlehen"][0]
    tfs = [t_ for t_ in fs0.plan.e.tranchen if t_.name == "Foerderdarlehen"][0]
    pruefe_gleich(k, "Foerderdarlehen: Tilgung ab dem Monat nach der letzten Teilrate (23), 500 Raten bis 42 Jahre nach Bezugsfertigkeit, zinslos bis Monat 438; "
              "Stressfall: spaetestens 24 Monate nach dem Monat nach der Foerderentscheidung (25), 501 Raten",
           [tf.tilgungsbeginn, tf.laufzeit, tf.bindung, str(zf[23]["tranchen"]["Foerderdarlehen"]["rate"]), tfs.tilgungsbeginn, tfs.laufzeit],
           [23, 500, 438, "10462.98", 25, 501])
    auf = rechne_grob(replace(GEFOERDERT, foerder_aufschub_monate=60), VG, KATN)
    ta = [t_ for t_ in auf.plan.e.tranchen if t_.name == "Foerderdarlehen"][0]
    pruefe_fest(k, "Aufschub der Tilgung um 60 Monate (E-68): Tilgungsbeginn, Zahl der Raten, Rate, Rendite (%)",
                [ta.tilgungsbeginn, ta.laufzeit, str(auf.plan.zeilen[83]["tranchen"]["Foerderdarlehen"]["rate"]), q(auf.kennzahlen["rendite"] * 100, "0.001")])
    pruefe_gleich(k, "Aufschub ueber dem Hoechstwert des Katalogs; Tilgungssatz des Bankdarlehens unter der Mindesttilgung der Richtlinie: M-20",
                  [status(replace(GEFOERDERT, foerder_aufschub_monate=61), VG, KATN), status(replace(GEFOERDERT, tilgungssatz=D("0.005")), replace(VG, mindesttilgung=D("0.005")), KATN)],
                  [["eingabe", "M-20"], ["eingabe", "M-20"]])
    pruefe_gleich(k, "Mindesttilgung des Hauses 0,5 %: gefoerdert bemisst die Bank mit 1 % (KAT-10), frei finanziert mit 0,5 %",
                  [str(rechne_grob(GEFOERDERT, replace(VG, mindesttilgung=D("0.005")), KATN).bemessung.tilgung_kalk),
                   str(rechne_grob(replace(A.NEUBAU, begruendungen=GRUND), replace(VG, mindesttilgung=D("0.005")), KATN).bemessung.tilgung_kalk)], ["0.01", "0.005"])
    h37 = rechne_grob(GEFOERDERT, replace(VG, bauabschnitt_rohbau=D("0.4"), bauabschnitt_innenputz=D("0.7")), KATN)
    pruefe_fest(k, "Bauabschnitte 40 % und 70 % der Bauzeit (H-37): hoechster Stand der Zwischenfinanzierung, Endwertdifferenz",
                [str(h37.zwischenfinanzierung), str(h37.kennzahlen["endwertdifferenz"])])
    pruefe_gleich(k, "H-37: Innenputz vor dem Rohbau ist keine zulaessige Vorgabe (M-20)",
                  status(GEFOERDERT, replace(VG, bauabschnitt_rohbau=D("0.8"), bauabschnitt_innenputz=D("0.7")), KATN), ["eingabe", "M-20"])
    knapp = rechne_grob(replace(GEFOERDERT, foerderung=replace(A.FOERDERUNG_B, eingangsmiete=D("7.60"))), VG, KATN)
    pruefe_fest(k, "Eingangsmiete 7,60 Euro: M-50 (Miete deckt Finanzierung und Bewirtschaftung nicht auf Dauer) mit Deckung nach Bemessung und kleinster Deckung; ohne die Aenderung keine M-50",
                [[m_["kennung"] for m_ in knapp.meldungen if m_["kennung"] == "M-50"], q(knapp.deckung_bemessung), q(knapp.deckung_min),
                 [m_["kennung"] for m_ in f.meldungen if m_["kennung"] == "M-50"]])
    o = f.ohne_bankdarlehen
    pruefe_fest(k, "ohne Bankdarlehen: Mindestdeckung, bei der die Restfinanzierung moeglich waere; freier Beleihungsraum; Planjahr, in dem die Mindestdeckung erreicht ist",
                [q(o["mindestdeckung_moeglich"]), str(o["freier_beleihungsraum"].quantize(D("0.01"))), o["planjahr_mindestdeckung"]])
    pruefe_gleich(k, "ohne Bankdarlehen bei gebundener Miete: die noetige Miete entfaellt", o["miete_noetig"], None)
    fs = fs0
    pruefe_fest(k, "ohne Bankdarlehen im Stressfall: Planjahr, in dem die Mindestdeckung erreicht ist", fs.ohne_bankdarlehen["planjahr_mindestdeckung"])
    pruefe_fest(k, "Grobfoerderung: Deckung im ersten Jahr nach dem Ende der zinslosen Zeit (R-10.14)",
                {a: [j, q(x)] for a, (j, x) in f.deckung_nach_bindung.items()})
    pruefe_fest(k, "Grobfoerderung: Kapitaldienstreserve laut Finanzplan und Reserve nach Bemessung", [str(f.kapitaldienstreserve), str(f.reserve_bemessung)])
    erg = kalkuliere(replace(GEFOERDERT, kfw_betrag=D(3000000), kfw_laufzeit=35, kfw_tilgungsfrei=1), VG, KATN)
    pruefe_fest(k, "KfW 3 Mio. Euro neben der Grobfoerderung: M-22 mit dem hoechsten KfW-Betrag, der passt",
                [erg["meldungen"][0]["kennung"], str(erg["meldungen"][0].get("kfw_hoechstens"))])
    # Zielrendite fuer gefoerderte Vorhaben (H-01)
    tp5 = tragbarer_preis(GEFOERDERT, VG, KATN)
    tp3 = tragbarer_preis(GEFOERDERT, replace(VG, zielrendite_gefoerdert=D("0.03")), KATN)
    pruefe_fest(k, "gefoerdert, Zielrendite 5 % und eigene Zielrendite 3 % (H-01): tragbarer Grundstueckspreis, Meldung",
                [[tp5["preis"], tp5["meldung"]], [tp3["preis"], tp3["meldung"]]])
    pruefe_gleich(k, "eigene Zielrendite fuer gefoerderte Vorhaben wirkt nicht auf den frei finanzierten Neubau",
                  rechne_grob(A.NEUBAU, replace(VG, zielrendite_gefoerdert=D("0.03")), KATN).kennzahlen["endwertueberschuss"] == n.kennzahlen["endwertueberschuss"], True)


# ------------------------------------------------------------------------------------------------ RF-13
def rf13_runde2():
    k = fall("RF-13", "Steuerstatus, zweite Ueberarbeitung: Endwert der Unterlassensalternative je Auspraegung")
    faelle = (("Koerperschaft", A.steuer(KOERPERSCHAFT)),
              ("Koerperschaft mit erweiterter Kuerzung", A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True)),
              ("Koerperschaft ohne Gewerbesteuer (Verein, Stiftung)", A.steuer(KOERPERSCHAFT_OHNE_GEWST)),
              ("originaer gewerbliche Personengesellschaft, Hebesatz 440 %", A.steuer(GEWERBLICHE_PG, hebesatz=D("4.40"))),
              ("Einzelunternehmen mit Betriebsvermoegen, Hebesatz 440 %", A.steuer(EINZELUNTERNEHMEN, hebesatz=D("4.40"))),
              ("Privatperson", A.steuer(PRIVAT)), ("befreite Koerperschaft", A.steuer(BEFREIT)))
    for name, st in faelle:
        e = rechne_grob(replace(A.ANKAUF, steuer=st, begruendungen=GRUND), VG, KAT)
        pruefe_fest(k, f"{name}: Endwert der Unterlassensalternative", e.alt.endwert)
    e = rechne_grob(replace(A.ANKAUF, steuer=A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True, uebergang_jahresende=True),
                            begruendungen=GRUND), VG, KAT)
    mk = rechne_grob(replace(A.ANKAUF, steuer=A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True)), VG, KAT)
    pruefe(k, "Koerperschaft mit Kuerzung, Voreinstellung (BFH-III-R-1-23: im Verkaufsjahr entfaellt die Kuerzung ganz): Endwert (Wert der bisherigen dritten Lesart)",
           mk.plan.endwert, "2562727.38", "0")
    pruefe(k, "... Uebergang zum Jahresende (E-69): Endwert (Wert der bisherigen Voreinstellung)", e.plan.endwert, "2570679.38", "0")
    pruefe_fest(k, "Koerperschaft mit Kuerzung, Uebergang zum Jahresende (E-69; laufender Ertrag gekuerzt, Verkaufsgewinn gewerbesteuerpflichtig): Endwert, Rendite (%), Abstand zur Voreinstellung",
                [str(e.plan.endwert), q(e.kennzahlen["rendite"] * 100, "0.001"), str(e.plan.endwert - mk.plan.endwert)])
    for jahre in (10, 11):
        e = rechne_grob(replace(A.ANKAUF, steuer=A.steuer(KOERPERSCHAFT_OHNE_GEWST), haltedauer=jahre), VG, KAT)
        pruefe_fest(k, f"Verein oder Stiftung, Verkauf nach {jahre} Jahren: Steuer auf den Verkaufsgewinn, Rendite (%)",
                    [str(e.steuer_verkaufsgewinn), q(e.kennzahlen["rendite"] * 100, "0.001")])


# ------------------------------------------------------------------------------------------------ RF-16
def rf16_runde2():
    k = fall("RF-16", "Fehlerbilder, die die Rechnung veraendern: jede Probe meldet ihren Fehler (R-13.4)")
    gut = rechne_grob(A.ANKAUF, VG, KAT)
    bank = replace(OHNE_STAU, zins=D("0.03"), ist_miete=D("8.50"), vergleichsmiete=D("8.50"))
    neubau = replace(A.NEUBAU, bauzeit_monate=24, zinsbindung_jahre=2)
    bilder = (
        ("bemessung_ohne_deckung", "Mindestdeckung in der Bemessung vergessen", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-12"]),
        ("rate_ohne_anschluss", "Rate nach dem Ende der Zinsbindung mit dem alten Zins gebildet (Neubau, Stressfall)",
         lambda: rechne_grob(neubau, VG, KATN, stress=True), ["P-20"]),
        ("zins_ohne_anschluss", "Zins nach der Zinsbindung still fortgeschrieben", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-17", "P-20"]),
        ("tranche_ohne_aufschlag", "Bankdarlehen ohne den Anschlussaufschlag H-05 aufgebaut", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-21"]),
        ("vortrag_nicht_verbraucht", "Verlustvortrag wird nie verbraucht", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-15"]),
        ("steuerjahr_falsch", "Steuersatz des falschen Kalenderjahres", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-15", "P-16"]),
        ("afa_doppelt", "Abschreibung im Ergebnis zweimal abgezogen", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-15"]),
        ("alternative_zins", "Unterlassensalternative mit falschem Anlagezins", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-16"]),
        ("alternative_ohne_gewerbesteuer", "Unterlassensalternative ohne Gewerbesteuer besteuert", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-16"]),
        ("alternative_ohne_steuerabzug", "Steuer der Unterlassensalternative gerechnet, aber nicht gebucht", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-16"]),
        ("verdichtung_bestand", "Jahresdarstellung mit dem Bestand der vorletzten Periode", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-09"]),
        ("index_potenz", "Index als Potenz ohne Rundung je Schritt", lambda: rechne_grob(A.ANKAUF, VG, KAT), ["P-18"]),
    )
    for name, text, f, soll in bilder:
        e = mit_fehler(name, f)
        pruefe_gleich(k, f"Fehlerbild {text}: gesperrt, meldende Proben", (e.gesperrt, proben_von(e.befunde)), (True, soll))
    pruefe_gleich(k, "ohne Fehlerbild: derselbe Lauf ist nicht gesperrt", (rechne_grob(A.ANKAUF, VG, KAT).gesperrt, len(FEHLER)), (False, 0))
    e = mit_fehler("vortrag_nicht_verbraucht", lambda: rechne_grob(A.ANKAUF, VG, KAT))
    pruefe(k, "Fehlerbild Verlustvortrag nie verbraucht: Wirkung auf den Endwert (Injektion der Rolle Controller)",
           e.plan.endwert - gut.plan.endwert, "-32243.29", "0")
    e = mit_fehler("alternative_ohne_gewerbesteuer", lambda: rechne_grob(A.ANKAUF, VG, KAT))
    pruefe(k, "Fehlerbild Alternative ohne Gewerbesteuer: Endwert der Alternative (Injektion der Rolle Controller)", e.alt.endwert, "1829535.74", "0")
    e = mit_fehler("bemessung_ohne_deckung", lambda: rechne_grob(A.ANKAUF, VG, KAT))
    pruefe(k, "Fehlerbild Mindestdeckung vergessen: Bankdarlehen (Bericht Grenzfaelle NG-36: 1.471.932,00 ohne Investitionsstau)", e.darlehen, "1471932.00", "0")
    tp = mit_fehler("vortrag_nicht_verbraucht", lambda: tragbarer_preis(A.ANKAUF, VG, KAT))
    pruefe_gleich(k, "Fehlerbild in der Preissuche: M-10 und kein Preis", (tp["preis"], tp["meldung"]), (None, "M-10"))
    # Rundungsmodus "keine": Toleranz der Proben (R-13.2)
    ej = rechne_grob(A.ANKAUF, VG, KAT, p=1, rundung="keine")
    pruefe_gleich(k, "Ankauf im Jahresmodus ohne Rundung: keine Probe meldet (Toleranz 1E-12 Euro)", (ej.gesperrt, ej.befunde), (False, []))
    pruefe_gleich(k, "Neubau ohne Rundung (nur im Monatsraster rechenbar): M-20 statt Sperre", status(A.NEUBAU, VG, KATN, rundung="keine"), ["eingabe", "M-20"])
    pruefe_gleich(k, "Ankauf im Monatsraster ohne Rundung: M-20", status(A.ANKAUF, VG, KAT, rundung="keine"), ["eingabe", "M-20"])


# ------------------------------------------------------------------------------------------------ RF-17
def rf17_runde2():
    k = fall("RF-17", "Steuer, zweite Ueberarbeitung: Zuschuss, Verein und Stiftung, Kuerzung, Entgelte")
    r = Raster(1, 12, startjahr=2027)

    def st(status_, alternative=False, **kw):
        return Steuer(A.steuer(status_, **kw), r, CENT, alternative=alternative)

    # R-7.8 in gesetzlicher Reihenfolge: Kuerzung vor dem Verlustvortrag (GEWSTG-9, GEWSTG-10A); Jahr 2 ist das
    # Verkaufsjahr mit Uebergang zum Jahresende (E-69)
    s = st(KOERPERSCHAFT, erweiterte_kuerzung=True, uebergang_jahresende=True, haltedauer=2)
    pruefe(k, "Kennzeichen, Anlaufverlust 50.000: keine Steuer", s.jahr(1, D(-50000), NULL), "0", "0")
    pruefe(k, "... der gekuerzte Verlust bildet keinen gewerbesteuerlichen Vortrag", s.vv_gew, "0", "0")
    pruefe(k, "... Folgejahr 2028 mit 100.000 Ergebnis, 10.000 Zinsen, 500.000 Verkaufsgewinn: 14,77 % von 560.000 + 14 % von 510.000",
           s.jahr(2, D(100000), D(10000), D(500000)), "154112.00", "0")
    # R-7.8 (BFH-III-R-1-23): im Verkaufsjahr entfaellt die Kuerzung ganz, ausser bei Uebergang zum Jahresende (E-69)
    pruefe(k, "Verkaufsjahr mit Kennzeichen, Voreinstellung: 15,825 % und 14 % von 610.000",
           st(KOERPERSCHAFT, erweiterte_kuerzung=True, haltedauer=1).jahr(1, D(100000), D(10000), D(500000)), "181932.50", "0")
    pruefe(k, "... die Lesart 'Verkaufsgewinn gekuerzt' (MA-030) wirkt ohne Uebergang zum Jahresende nicht",
           st(KOERPERSCHAFT, erweiterte_kuerzung=True, kuerzung_verkauf=True, haltedauer=1).jahr(1, D(100000), D(10000), D(500000)), "181932.50", "0")
    pruefe(k, "... in einem Jahr vor dem Verkauf bleibt die Kuerzung: 17.407,50 + 14 % von 10.000",
           st(KOERPERSCHAFT, erweiterte_kuerzung=True, haltedauer=2).jahr(1, D(100000), D(10000)), "18807.50", "0")
    pg = dict(hebesatz=D("4.00"), anteil_natuerliche=D("0.6"))
    pruefe(k, "gepraegte Personengesellschaft, 400 %, 60 %, Verkaufsgewinn 500.000: laufender Gewinn (Gegenrechnung Steuerberater)",
           st(GEPRAEGTE_PG, **pg).jahr(1, NULL, NULL, D(500000)), "236628.00", "0")
    pruefe(k, "... als Aufgabegewinn (Gegenrechnung Steuerberater)", st(GEPRAEGTE_PG, aufgabegewinn=True, **pg).jahr(1, NULL, NULL, D(500000)), "219828.00", "0")
    # R-7.17 Verein und Stiftung: Verkauf wie bei der Privatperson, Satz der Koerperschaft
    pruefe(k, "Verein, Verkauf nach 10 Jahren, Verlust 20.000, Gewinn 200.000, Vorfaelligkeit 30.000: 10,55 % von 150.000 (Jahr 2036)",
           st(KOERPERSCHAFT_OHNE_GEWST, haltedauer=10).jahr(10, D(-20000), NULL, D(200000), NULL, NULL, D(30000)), "15825.00", "0")
    s = st(KOERPERSCHAFT_OHNE_GEWST, haltedauer=11)
    pruefe(k, "Verein, Verkauf nach 11 Jahren: Gewinn steuerfrei; 5.000 Zinsen gegen 20.000 Vermietungsverlust: keine Steuer",
           s.jahr(11, D(-20000), D(5000), D(200000), NULL, NULL, D(30000)), "0", "0")
    pruefe(k, "... Verlustvortrag (Vermietung und Zinsen in einem Einkommen)", s.vv, "15000", "0")
    # R-7.6: Einzelunternehmen bei sofortiger Verrechnung: Anrechnung ohne Begrenzung auf die Einkommensteuer
    s = st(EINZELUNTERNEHMEN, verlust="sofort", hebesatz=D("4.80"))
    pruefe(k, "Einzelunternehmen, sofort, Hebesatz 480 %, Verlust 50.000: -21.000 - 8.400 + 7.000", s.jahr(1, D(-50000), NULL), "-22400.00", "0")
    # R-7.19 Zuschuss: Voreinstellung nach Kennzeichen; Rueckzahlung im laufenden Ergebnis (Lesart "sofort")
    gek = replace(GEFOERDERT, steuer=A.steuer(KOERPERSCHAFT, erweiterte_kuerzung=True))
    e = rechne_grob(gek, VG, KATN)
    pruefe_gleich(k, "Voreinstellung mit Kennzeichen E-41: 'minderung'", e.zuschuss_lesart, "minderung")
    werte = {}
    for lesart in ("verteilt", "minderung", "sofort"):
        for jahre in (38, 20):
            x = rechne_grob(replace(gek, haltedauer=jahre), replace(VG, ma031_zuschuss=lesart), KATN)
            werte[(lesart, jahre)] = x.kennzahlen["endwertdifferenz"]
            pruefe_fest(k, f"mit Kennzeichen, Zuschuss '{lesart}', {jahre} Jahre: Endwertdifferenz, Rendite (%), Summe der Steuern",
                        [str(x.kennzahlen["endwertdifferenz"]), q(x.kennzahlen["rendite"] * 100, "0.001"), str(sum(x.plan.reihe("steuer")))])
            pruefe_gleich(k, f"mit Kennzeichen, Zuschuss '{lesart}', {jahre} Jahre: Kontrollsummen", (x.gesperrt, x.befunde), (False, []))
    pruefe_fest(k, "mit Kennzeichen: 'minderung' gegen 'verteilt', Endwertdifferenz 38 und 20 Jahre (Rechnung in beide Richtungen)",
                [str(werte[("minderung", j)] - werte[("verteilt", j)]) for j in (38, 20)])
    for name, stx in (("Privatperson", A.steuer(PRIVAT)), ("Koerperschaft", A.steuer(KOERPERSCHAFT))):
        x = rechne_grob(replace(GEFOERDERT, haltedauer=20, steuer=stx), replace(VG, ma031_zuschuss="sofort"), KATN)
        t = x.plan.steuer.protokoll[-1]
        pruefe_fest(k, f"{name}, Zuschuss 'sofort', Verkauf nach 20 Jahren: Rueckzahlung, operatives Ergebnis und Verkaufsgewinn des Verkaufsjahres, Steuer, Rendite (%)",
                    [str(x.verkauf.foerder_rueckzahlung), str(t["e_op"]), str(t["g_v"]), str(t["steuer"]), q(x.kennzahlen["rendite"] * 100, "0.001")])
        pruefe_gleich(k, f"{name}, Zuschuss 'sofort', 20 Jahre: Kontrollsummen (Bruecke P-15)", (x.gesperrt, x.befunde), (False, []))
    for lesart in ("sofort", "verteilt"):
        x = rechne_grob(replace(GEFOERDERT, haltedauer=20, steuer=A.steuer(PRIVAT, verlust="sofort"), begruendungen=GRUND),
                        replace(VG, ma031_zuschuss=lesart), KATN)
        pruefe_fest(k, f"Privatperson mit sofortiger Verlustverrechnung, Zuschuss '{lesart}', 20 Jahre: Steuer des Verkaufsjahres, Summe der Steuern, Rendite (%)",
                    [str(x.plan.steuer.protokoll[-1]["steuer"]), str(sum(x.plan.reihe("steuer"))), q(x.kennzahlen["rendite"] * 100, "0.001")])
    pv = rechne_grob(replace(GEFOERDERT, steuer=A.steuer(PRIVAT)), VG, KATN)
    pruefe_fest(k, "Privatperson, gefoerdert: Entgelt des Darlehens verteilt (ESTG-11), Planjahre 1 bis 3; Lesart des Zuschusses",
                [[str(pv.plan.jahressumme("einbehalt_steuer", j)) for j in (1, 2, 3)], pv.zuschuss_lesart])
    mi = rechne_grob(GEFOERDERT, replace(VG, ma031_zuschuss="minderung"), KATN)
    pruefe(k, "Lesart 'Minderung': das Entgelt auf den Zuschuss kuerzt ihn; Abschreibungsgrundlage = Baukosten - Gebaeudeanteil + Entgeltanteil",
           mi.plan.e.afa_grundlage, str(mi.baukosten - mi.bemessung.zuschuss_gebaeude
                                        + CENT.geld(mi.bemessung.einbehalt_zuschuss * mi.bemessung.zuschuss_gebaeude / mi.bemessung.zuschuss)), "0")
    so = rechne_grob(GEFOERDERT, replace(VG, ma031_zuschuss="sofort"), KATN)
    pruefe(k, "Lesart 'sofort': das Entgelt auf den Zuschuss ist im Jahr der Zahlung Aufwand", sum(so.plan.jahressumme("zuschuss_entgelt_steuer", j) for j in (1, 2)),
           str(so.bemessung.einbehalt_zuschuss), "0")
    pruefe_gleich(k, "das Entgelt auf den Zuschuss zaehlt nicht zu den Entgelten fuer Schulden (GEWSTG-8)",
                  sum(z["entgelte"] for z in so.plan.zeilen) == sum(z["zins"] + z["kkzins"] + z["beitrag"] + z["bereit"] + z["einbehalt_steuer"] + z["vfe"] for z in so.plan.zeilen), True)
    e = rechne_grob(replace(A.ANKAUF, steuer=A.steuer(BEFREIT)), VG, KAT)
    pruefe_gleich(k, "befreite Koerperschaft: M-44, aber kein M-37", ("M-44" in kennungen(e), "M-37" in kennungen(e)), (True, False))


# ------------------------------------------------------------------------------------------------ RF-18
def rf18_runde2():
    k = fall("RF-18", "Miete, zweite Ueberarbeitung: Uebermiete, Gebietsverordnungen, Leerstandskosten, CO2-Kosten")
    jahre = lambda e, n=7: [q(e.miete_je_qm[(j - 1) * 12 + 1]) for j in range(1, n + 1)]
    ue = replace(A.ANKAUF, ist_miete=D("11.00"))
    a = rechne_grob(ue, VG, KAT)
    b = rechne_grob(ue, replace(VG, ma038_rueckfuehrung=False), KAT)
    pruefe_fest(k, "Ist-Miete 11,00 Euro, andere Lesart MA-038 (bleibt stehen): Miete zu Beginn der Jahre 1 bis 7", jahre(b))
    pruefe_fest(k, "Uebermiete: Endwertdifferenz mit Rueckfuehrung und ohne; die Voreinstellung ist die niedrigere",
                [str(a.kennzahlen["endwertdifferenz"]), str(b.kennzahlen["endwertdifferenz"]), a.kennzahlen["endwertdifferenz"] < b.kennzahlen["endwertdifferenz"]])
    pruefe_fest(k, "Uebermiete: tragbarer Kaufpreis mit Rueckfuehrung und ohne (Rangfolge der Vorsicht)",
                [tragbarer_preis(ue, VG, KAT)["preis"], tragbarer_preis(ue, replace(VG, ma038_rueckfuehrung=False), KAT)["preis"]])
    pruefe_gleich(k, "Uebermiete: MA-038 steht unter den Annahmen, die gewirkt haben; ohne Uebermiete nicht",
                  ("MA-038" in a.modellannahmen, "MA-038" in rechne_grob(A.ANKAUF, VG, KAT).modellannahmen), (True, False))
    # Gebietsverordnungen (KAT-08, MA-039, E-05)
    basis = rechne_grob(A.ANKAUF, VG, KAT)
    ende = rechne_grob(A.ANKAUF, replace(VG, ma039_fortgeltung=False), KAT)
    wechsel = lambda e: [m for m in range(2, 157) if e.miete_je_qm[m] != e.miete_je_qm[m - 1]]
    pruefe_fest(k, "andere Lesart MA-039 (Verordnung endet 2029, danach 20 %): Monate der Erhoehungen und Mieten",
                [wechsel(ende), [q(ende.miete_je_qm[m]) for m in wechsel(ende)]])
    pruefe_fest(k, "MA-039: Endwertdifferenz mit Fortgeltung und ohne; die Voreinstellung ist die niedrigere",
                [str(basis.kennzahlen["endwertdifferenz"]), str(ende.kennzahlen["endwertdifferenz"]),
                 basis.kennzahlen["endwertdifferenz"] <= ende.kennzahlen["endwertdifferenz"]])
    pruefe_fest(k, "MA-039: tragbarer Kaufpreis ohne Fortgeltung (mit Fortgeltung 2.317.235 Euro)",
                tragbarer_preis(A.ANKAUF, replace(VG, ma039_fortgeltung=False), KAT)["preis"], 0)
    ausser = rechne_grob(replace(A.ANKAUF, im_kappungsgebiet=False, voreinstellungen={"im_kappungsgebiet": (True, "KAT-08")},
                                 begruendungen={"im_kappungsgebiet": "Teilgebiet ausserhalb der Verordnung"}), VG, KAT)
    pruefe_fest(k, "Vorhaben ausserhalb des Gebiets der abgesenkten Kappungsgrenze (E-05): Monate der Erhoehungen, Mieten, Liste der Abweichungen",
                [wechsel(ausser), [q(ausser.miete_je_qm[m]) for m in wechsel(ausser)], [[x["kennung"], str(x["wirkung_endwertdifferenz"])] for x in ausser.abweichungen]])
    leer = replace(A.ANKAUF, leere_flaeche=D(200))
    mb = rechne_grob(leer, VG, KAT)
    ob = rechne_grob(replace(leer, im_bremsgebiet=False, voreinstellungen={"im_bremsgebiet": (True, "KAT-08")},
                             begruendungen={"im_bremsgebiet": "Teilgebiet ausserhalb der Verordnung"}), VG, KAT)
    pruefe_gleich(k, "200 m2 leer, Vorhaben ausserhalb des Gebiets der Mietpreisbremse (E-05): Sollmiete im Monat 4 mit 10,50 statt 10,12 Euro",
                  [str(mb.ertrag.soll(4)), str(ob.ertrag.soll(4))], ["11544.00", "11620.00"])
    # Betriebskosten leerstehender Flaechen (H-36, R-6.17)
    lk = rechne_grob(leer, replace(VG, leerstandskosten_je_qm=D(30)), KAT)
    pruefe(k, "200 m2 leer, 30 Euro je m2 und Jahr: Bewirtschaftung im Monat 1 hoeher um 200 x 30 / 12",
           lk.plan.zeilen[1]["kosten"] - mb.plan.zeilen[1]["kosten"], "500.00", "0")
    pruefe(k, "... ab dem Monat 4 (vermietet) keine Leerstandskosten", lk.plan.zeilen[4]["kosten"] - mb.plan.zeilen[4]["kosten"], "0", "0")
    pruefe_fest(k, "... Reinertrag im ersten Jahr und Bankdarlehen ohne und mit Leerstandskosten",
                [str(mb.bemessung.reinertrag_vj), str(lk.bemessung.reinertrag_vj), str(mb.darlehen), str(lk.darlehen)])
    # CO2-Kosten: haelftige Teilung nach CO2KOSTAUFG-5A ab dem Katalogjahr (E-66), weitere Kosten des Vermieters (E-67)
    h = rechne_grob(replace(A.ANKAUF, heizung_5a=True), VG, KAT)
    pruefe(k, "Heizung nach CO2KOSTAUFG-5A: 2027 Stufenanteil 40 %: 66,00 Euro CO2-Kosten im Monat 1", h.plan.zeilen[1]["kosten"] - D("2343.33"), "66.00", "0")
    pruefe(k, "... 2028 haelftig: 30 x 1.320 x 50 % x 52,50 / 1.000 / 12", h.plan.zeilen[13]["kosten"] - CENT.geld(D(28120) * D("1.02") / 12), "86.63", "0")
    pruefe_fest(k, "Heizung nach CO2KOSTAUFG-5A: Endwertdifferenz gegen den Basisfall", str(h.kennzahlen["endwertdifferenz"] - basis.kennzahlen["endwertdifferenz"]))
    pruefe_gleich(k, "Heizung nach CO2KOSTAUFG-5A ohne Katalogwert: M-47", status(replace(A.ANKAUF, heizung_5a=True), VG, replace(KAT, co2_5a_anteil=None)), ["eingabe", "M-47"])


# ------------------------------------------------------------------------------------------------ RF-19
def rf19_runde2():
    k = fall("RF-19", "Bankensicht, zweite Ueberarbeitung: Abweichungen vom Hausstandard, Bemessungszins, Anschluss, Rate")
    basis = rechne_grob(A.ANKAUF, VG, KAT)
    # ---- R-3.2: Abweichungen in beide Richtungen mit ihrer Wirkung; Begruendung, wenn die Abweichung am Fall erhoeht
    ab = {"mietsteigerung": (D("0.015"), None), "beleihungsquote": (D("0.60"), None)}
    e = rechne_grob(replace(A.ANKAUF, abweichungen=ab), VG, KAT)
    pruefe_fest(k, "Mietsteigerung 1,5 % und Beleihungsquote 60 % ohne Begruendung: gerechnet; Liste (Kennung, Art, Wirkung auf die Endwertdifferenz), Meldungen",
                [[a["kennung"], a["art"], str(a["wirkung_endwertdifferenz"])] for a in e.abweichungen] + kennungen(e))
    liste = abweichungsliste(replace(A.ANKAUF, abweichungen=ab), VG, KAT)
    pruefe_fest(k, "... Wirkung auf den tragbaren Preis je Abweichung", [[a["kennung"], str(a["wirkung_preis"])] for a in liste])
    ohne = lambda feld, wert: status(replace(A.ANKAUF, abweichungen={feld: (wert, None)}))
    pruefe_gleich(k, "Mietsteigerung 2,5 % ohne Begruendung: M-20", ohne("mietsteigerung", D("0.025")), ["eingabe", "M-20"])
    e = rechne_grob(replace(A.ANKAUF, abweichungen={"mietsteigerung": (D("0.025"), "Mietspiegel 2026, Fortschreibung")}), VG, KAT)
    pruefe_fest(k, "Mietsteigerung 2,5 % mit Begruendung: Liste und Meldungen",
                [[a["kennung"], a["art"], a["begruendung"], str(a["wirkung_endwertdifferenz"])] for a in e.abweichungen] + kennungen(e))
    # Vorgaben, die als Regel gefasst sind (Bericht Controller 1): verglichen wird mit dem aufgeloesten Wert des Hauses
    pruefe_gleich(k, "fester kalkulatorischer Zins 1 % statt 'Anschlusszins' (H-25) ohne Begruendung: M-20", ohne("kalk_zins", D("0.01")), ["eingabe", "M-20"])
    liste = abweichungsliste(replace(A.ANKAUF, abweichungen={"kalk_zins": (D("0.01"), GRUNDTEXT)}), VG, KAT)
    pruefe(k, "... mit Begruendung: Wirkung auf den tragbaren Preis (Gegenrechnung Controller: 2.359.366 - 2.317.235)", liste[0]["wirkung_preis"], "42131", "0")
    pruefe(k, "... Wirkung auf die Endwertdifferenz (wie Lesart 2 von MA-026: die Bank rechnet dann mit dem Vertragszins)", liste[0]["wirkung_endwertdifferenz"], "-38496.31", "0")
    pruefe_gleich(k, "langfristiger Anlagezins 0,5 % statt gleich dem Habenzins (H-09) ohne Begruendung: M-20", ohne("a_lang", D("0.005")), ["eingabe", "M-20"])
    e = rechne_grob(replace(A.ANKAUF, abweichungen={"a_lang": (D("0.005"), GRUNDTEXT)}), VG, KAT)
    pruefe(k, "... mit Begruendung: Endwertdifferenz (Gegenrechnung Controller)", e.kennzahlen["endwertdifferenz"], "966697.17", "0")
    # Richtung haengt am Fall (Finanzmathematiker 2): hoehere Mindestdeckung hebt den tragbaren Preis bei negativem Hebel
    z2 = replace(VG, zielrendite=D("0.02"))
    pruefe_gleich(k, "Zielrendite 2 %: Mindestdeckung 1,3 statt 1,2 ohne Begruendung: M-20 (sie erhoeht den tragbaren Preis)",
                  status(replace(A.ANKAUF, abweichungen={"mindestdeckung": (D("1.3"), None)}), z2), ["eingabe", "M-20"])
    liste = abweichungsliste(replace(A.ANKAUF, abweichungen={"mindestdeckung": (D("1.3"), GRUNDTEXT)}), z2, KAT)
    pruefe(k, "... Wirkung auf den tragbaren Preis (Gegenrechnung Finanzmathematiker: 2.983.619 - 2.973.391)", liste[0]["wirkung_preis"], "10228", "0")
    pruefe_gleich(k, "Zielrendite 5 %: Mindestdeckung 1,3 ohne Begruendung: M-20 (sie erhoeht die Endwertdifferenz, weil das Darlehen mehr kostet als die Anlage bringt)",
                  status(replace(A.ANKAUF, abweichungen={"mindestdeckung": (D("1.3"), None)})), ["eingabe", "M-20"])
    liste = abweichungsliste(replace(A.ANKAUF, abweichungen={"mindestdeckung": (D("1.3"), GRUNDTEXT)}), VG, KAT)
    pruefe_fest(k, "... Wirkung auf Endwertdifferenz und tragbaren Preis bei Zielrendite 5 %", [str(liste[0]["wirkung_endwertdifferenz"]), str(liste[0]["wirkung_preis"])])
    for regel in ("restlaufzeit", "rate"):
        pruefe_gleich(k, f"Anschlussregel '{regel}' statt 'tilgungssatz' (H-07) ohne Begruendung: M-20 (hoehere Endwertdifferenz)",
                      ohne("anschluss_regel", regel), ["eingabe", "M-20"])
    pruefe_gleich(k, "feste Vorgabe (H-21 Rasterzahl) im Vorhaben geaendert: M-20", ohne("suchraster", 80), ["eingabe", "M-20"])
    # Voreinstellungen aus Vorgabe und Katalog (Bericht Controller 2)
    vor = {"enk_satz": (D("0.10"), "KAT-01"), "anpassungsdauer": (4, "H-23"), "zinsbindung_jahre": (10, "H-24")}
    pruefe_gleich(k, "Erwerbsnebenkosten 3 % statt 10 % aus dem Katalog ohne Begruendung: M-20",
                  status(replace(A.ANKAUF, enk_satz=D("0.03"), voreinstellungen=vor)), ["eingabe", "M-20"])
    liste = abweichungsliste(replace(A.ANKAUF, enk_satz=D("0.03"), voreinstellungen=vor, begruendungen={"enk_satz": GRUNDTEXT}), VG, KAT)
    pruefe(k, "... mit Begruendung: Wirkung auf den tragbaren Preis (Gegenrechnung Controller: 2.474.717 - 2.317.235)", liste[0]["wirkung_preis"], "157482", "0")
    e = rechne_grob(replace(A.ANKAUF, anpassungsdauer=1, zinsbindung_jahre=5, voreinstellungen=vor, begruendungen={"anpassungsdauer": GRUNDTEXT}), VG, KAT)
    pruefe_fest(k, "Anpassungsdauer 1 statt 4 Jahre (H-23) und Zinsbindung 5 statt 10 Jahre (H-24): Liste mit Wirkung auf die Endwertdifferenz",
                [[a["kennung"], str(a["haus"]), str(a["vorhaben"]), str(a["wirkung_endwertdifferenz"])] for a in e.abweichungen])
    pruefe(k, "... Aenderung der Endwertdifferenz gegen den Basisfall (Gegenrechnung Controller)", e.kennzahlen["endwertdifferenz"] - basis.kennzahlen["endwertdifferenz"],
           "-39643", "0.5")
    # Lesart einer Modellannahme im Vorhaben und als Lesart des Hauses
    pruefe_gleich(k, "Lesart 2 von MA-026 im Vorhaben ohne Begruendung: M-20", ohne("ma026_vertragszins", True), ["eingabe", "M-20"])
    e = rechne_grob(replace(A.ANKAUF, abweichungen={"ma026_vertragszins": (True, GRUNDTEXT)}), VG, KAT)
    h = rechne_grob(A.ANKAUF, replace(VG, ma026_vertragszins=True), KAT)
    pruefe_fest(k, "Lesart 2 von MA-026 im Vorhaben mit Begruendung und als Lesart des Hauses: Liste (Kennung, Art, Begruendung, Wirkung)",
                [[[a["kennung"], a["art"], a["begruendung"], str(a["wirkung_endwertdifferenz"])] for a in x.abweichungen] for x in (e, h)])
    # ---- R-5.12: Bemessungszins je Tranche am uebernommenen Darlehen
    g = rechne_grob(GEBUNDEN, VG, KAT)
    pruefe(k, "gebundener Bestand: Bemessungszins (0,5 % x 96 + 3 % x 24) / 120", g.bemessung.bemessungszins["Uebernommenes Darlehen"], "0.01", "0")
    pruefe(k, "... kalkulatorischer Kapitaldienst 600.000 x (1 % + 2 %), bezogen auf den Nennbetrag", g.bemessung.kd_uebrige, "18000.00", "0")
    pruefe_fest(k, "... Endwert der Unterlassensalternative, Rendite (%), Vergleichsrendite (%)",
                [str(g.alt.endwert), q(g.kennzahlen["rendite"] * 100, "0.001"), q(g.kennzahlen["vergleichsrendite"] * 100, "0.001")])
    reihe = {}
    for bindung in (8, 9, 10, 12):
        x = rechne_grob(replace(GEBUNDEN, uebernommen=dict(GEBUNDEN.uebernommen, bindung_jahre=bindung)), VG, KAT)
        reihe[str(bindung)] = [str(x.bemessung.bemessungszins["Uebernommenes Darlehen"]), str(x.bemessung.kd_uebrige), str(x.darlehen)]
    pruefe_fest(k, "Zinsbindung des uebernommenen Darlehens 8, 9, 10, 12 Jahre: Bemessungszins, Kapitaldienst, Bankdarlehen (keine Klippe)", reihe)
    pruefe(k, "Zinsbindung 12 Jahre: Kapitaldienst 15.000, Bankdarlehen (Gegenrechnung Bank)", D(reihe["12"][2]), "886660.00", "0")
    ohne_k = rechne_grob(replace(GEBUNDEN, uebernommen=dict(GEBUNDEN.uebernommen, foerderdarlehen=None)), VG, KAT)
    mit_k = rechne_grob(GEBUNDEN, VG, KAT)
    pruefe_gleich(k, "Kennzeichen Foerderdarlehen nicht angegeben: wie 'nein'; das Kennzeichen aendert die Bemessung nicht mehr",
                  (ohne_k.darlehen == mit_k.darlehen, [a["kennung"] for a in ohne_k.abweichungen], [a["kennung"] for a in mit_k.abweichungen]),
                  (True, [], ["E-59"]))
    fuenf = replace(GEBUNDEN, haltedauer=5, uebernommen=dict(GEBUNDEN.uebernommen, bindung_jahre=20))
    pruefe_gleich(k, "Kennzeichen Foerderdarlehen 'ja' ohne Begruendung, wenn es die Vorfaelligkeit erspart: M-20",
                  status(replace(fuenf, begruendungen=None)), ["eingabe", "M-20"])
    pruefe_fest(k, "... Vorfaelligkeit nach 5 Jahren mit und ohne Kennzeichen (Zinsbindung 20 Jahre)",
                [str(rechne_grob(replace(fuenf, uebernommen=dict(fuenf.uebernommen, foerderdarlehen=x)), VG, KAT).plan.zeilen[60]["vfe"]) for x in (True, False)])
    # Lesart 2 von MA-026 und H-25 je Tranchenart
    pruefe_fest(k, "gebundener Bestand: Bankdarlehen nach Lesart 2 von MA-026 und mit festem kalkulatorischem Zins 4 % fuer uebernommene Darlehen (H-25)",
                [str(rechne_grob(GEBUNDEN, replace(VG, ma026_vertragszins=True), KAT).darlehen),
                 str(rechne_grob(GEBUNDEN, replace(VG, kalk_zins_uebernommen=D("0.04")), KAT).darlehen)])
    pruefe(k, "Mindestansatz der Bewirtschaftung als Vorgabe H-33 (10 % statt 15 % aus dem Katalog): Neubau, Reinertrag des Vorhabens bindet",
           rechne_grob(A.NEUBAU, replace(VG, bewirtschaftung_mindest=D("0.10")), KATN).bemessung.ertrag_nachhaltig, "354432.75", "0")
    # ---- R-10.24, R-10.14: Kennzahlen nach Bemessungskonditionen, Anschlussregel mit der niedrigsten Deckung
    pruefe_fest(k, "Ankauf: Deckung nach Bemessung, Reserve nach Bemessung, Kapitaldienstreserve laut Finanzplan",
                [q(basis.deckung_bemessung, "0.000001"), str(basis.reserve_bemessung), str(basis.kapitaldienstreserve)])
    pruefe(k, "Ankauf: Kapitaldienst zu Bemessungskonditionen 12 x 7.155,22", basis.kd_bemessung, "85862.64", "0")
    w26 = rechne_grob(replace(A.ANKAUF, wertansatz_bank=D(2600000), wertansatz_begruendung="Gutachten vom Stichtag"), VG, KAT)
    pruefe_fest(k, "Wertansatz 2,6 Mio. Euro: Darlehen zu Kaufpreis und Darlehen zu Wertansatz (%)",
                [q(w26.darlehen_zu_wert * 100, "0.01"), q(w26.darlehen_zu_wertansatz * 100, "0.01")])
    pruefe_fest(k, "tragbarer Kaufpreis je Anschlussregel 'rate' und 'restlaufzeit' (Gegenrechnung Finanzmathematiker: 2.317.477 und 2.317.632)",
                [tragbarer_preis(A.ANKAUF, replace(VG, anschluss_regel=r_), KAT)["preis"] for r_ in ("rate", "restlaufzeit")])
    pruefe_fest(k, "Ankauf: kleinste Deckung nach der unguenstigsten Anschlussregel (Deckung, Jahr, Regel)",
                [q(basis.deckung_min_anschluss[0]), basis.deckung_min_anschluss[1], basis.deckung_min_anschluss[2]])
    bank = replace(OHNE_STAU, zins=D("0.03"), ist_miete=D("8.50"), vergleichsmiete=D("8.50"))
    vgb = replace(VG, mietsteigerung=D("0.005"))
    tab = {}
    for name, vg_, stress in (("kalkulatorisch, Stress", vgb, True), ("Vertragskonditionen, Basis", replace(vgb, ma026_vertragszins=True), False),
                              ("Vertragskonditionen, Stress", replace(vgb, ma026_vertragszins=True), True)):
        x = rechne_grob(bank, vg_, KAT, stress=stress)
        tab[name] = [q(x.deckung_min), q(x.deckung_min_anschluss[0]), x.deckung_min_anschluss[2], [m for m in kennungen(x) if m in ("M-38", "M-39")]]
    pruefe_fest(k, "Bankfall (Zins 3 %, Mietsteigerung 0,5 %): kleinste Deckung, nach der unguenstigsten Anschlussregel, Regel, Meldung", tab)
    pruefe(k, "... Vertragskonditionen, Basis: 'Restlaufzeit bleibt' ergibt 1,1975 und M-38 (Gegenrechnung Bank)", D(tab["Vertragskonditionen, Basis"][1]), "1.1975", "0.00005")
    pruefe(k, "... Vertragskonditionen, Stress: 0,8966 und M-39 (Gegenrechnung Bank)", D(tab["Vertragskonditionen, Stress"][1]), "0.8966", "0.00005")
    # ---- R-11.8: Stressfall mit neu bemessenem Darlehen
    es = rechne_grob(A.ANKAUF, VG, KAT, stress=True)
    pruefe(k, "Stressfall: Mehrbedarf an Eigenkapital durch den Zinsanstieg bis zur Zusage (Gegenrechnung Bank, Finanzmathematiker)",
           es.eigenkapital_investitionsphase - basis.eigenkapital_investitionsphase, "81774.00", "0")
    pruefe(k, "Stressfall: Anschlusszins des Bankdarlehens 4 % + 0,5 + 1 + 1 Prozentpunkte", es.plan.zeilen[121]["tranchen"]["Bankdarlehen"]["satz"], "0.065", "0")
    # ---- R-5.10: Zinsbindung endet vor dem Tilgungsbeginn (Bericht Grenzfaelle NG-22, NG-14)
    n1 = rechne_grob(replace(A.NEUBAU, zinsbindung_jahre=1), VG, KATN)
    pruefe(k, "Neubau, Zinsbindung 1 Jahr, Tilgung ab Monat 19: Rate mit dem Anschlusszins L x (5 % + 2 %) / 12", n1.plan.zeilen[19]["tranchen"]["Bankdarlehen"]["rate"],
           str(CENT.geld(n1.darlehen * D("0.07") / 12)), "0")
    pruefe(k, "... Bankdarlehen 4.007.142,85: Rate 23.375,00 (Bericht Grenzfaelle)", n1.plan.zeilen[19]["tranchen"]["Bankdarlehen"]["rate"], "23375.00", "0")
    n2 = replace(A.NEUBAU, bauzeit_monate=24, zinsbindung_jahre=2)
    b2, s2 = rechne_grob(n2, VG, KATN), rechne_grob(n2, VG, KATN, stress=True)
    pruefe_fest(k, "Neubau, Bauzeit 24, Zinsbindung 2 Jahre: Tilgung im ersten Tilgungsmonat und Deckung im ersten Jahr, Basis und Stress",
                [[str(x.plan.zeilen[u]["tranchen"]["Bankdarlehen"]["tilgung"]), q(x.dscr_vj)] for x, u in ((b2, 25), (s2, 28))])
    pruefe_gleich(k, "... im Stressfall wird getilgt, und die Deckung ist nicht besser als im Basisfall",
                  (s2.plan.zeilen[28]["tranchen"]["Bankdarlehen"]["tilgung"] > 0, s2.dscr_vj < b2.dscr_vj), (True, True))
    tr = Tranche("KfW", 3000000, "annuitaet_laufzeit", "0.025", laufzeit=276, tilgungsbeginn=145, bindung=120, anschluss_zins="0.05", bank=False)
    z = lauf(tr, 160, 12)
    pruefe(k, "Laufzeitannuitaet, zwoelf tilgungsfreie Jahre bei zehn Jahren Zinsbindung: Rate zum Anschlusszins ueber 276 Monate",
           z[145]["zins"] + z[145]["tilgung"], str(CENT.geld(Tranche.annuitaet(D(3000000), D("0.05") / 12, 276))), "0")
    pruefe_gleich(k, "... sie tilgt", z[145]["tilgung"] > 0, True)
    # ---- R-5.16 im Jahresmodus: Kuendigungstermin auf ganze Perioden aufgerundet (Bericht Grenzfaelle NG-16)
    v15 = replace(OHNE_STAU, zinsbindung_jahre=15, haltedauer=10)
    pruefe_fest(k, "Zinsbindung 15 Jahre, Verkauf nach 10: Vorfaelligkeit im Monatsraster (6 Monate) und im Jahresmodus (1 Jahr)",
                [str(rechne_grob(v15, VG, KAT).plan.zeilen[120]["vfe"]), str(rechne_grob(v15, VG, KAT, p=1).plan.zeilen[10]["vfe"])])


# ------------------------------------------------------------------------------------------------ RF-20
def rf20_runde2():
    k = fall("RF-20", "Raender, zweite Ueberarbeitung: Eingabepruefung, Katalog, Suchen, Warnschwellen, Vergleich")
    # ---- Eingabepruefung (Bericht Grenzfaelle NG-09, NG-34, NG-35)
    for name, ein in (("gebundene Miete 0", replace(GEBUNDEN, gebundene_miete=NULL)), ("gebundene Miete -1", replace(GEBUNDEN, gebundene_miete=D(-1))),
                      ("uebernommenes Darlehen, Anschlusszins -5 %", replace(GEBUNDEN, uebernommen=dict(GEBUNDEN.uebernommen, anschluss_zins=D("-0.05")))),
                      ("uebernommenes Darlehen, Beitrag -1 %", replace(GEBUNDEN, uebernommen=dict(GEBUNDEN.uebernommen, beitrag_satz=D("-0.01")))),
                      ("uebernommenes Darlehen, Zinsbindung 0 Jahre", replace(GEBUNDEN, uebernommen=dict(GEBUNDEN.uebernommen, bindung_jahre=0))),
                      ("Investitionsstau ohne Jahr der Ausfuehrung", replace(A.ANKAUF, stau_jahr=None))):
        pruefe_gleich(k, f"{name}: M-20", status(ein), ["eingabe", "M-20"])
    for name, vg_ in (("H-18 Vorfaelligkeitssatz -1 %", replace(VG, vfe_satz=D("-0.01"))), ("H-11 Linie -100.000", replace(VG, kk_linie=D(-100000))),
                      ("H-09 Anlagezins -50 %", replace(VG, a_lang=D("-0.5"))), ("H-29 CO2-Preis -500", replace(VG, co2_preis=D(-500))),
                      ("H-17 Verwaltung -2.000", replace(VG, verwaltung_je_einheit=D(-2000))),
                      ("H-06 Stress Leerstand -50 Punkte", replace(VG, stress=replace(VG.stress, leerstand_pp=D("-0.5")))),
                      ("H-17 Staffel leer", replace(VG, instandhaltung_staffel=[])), ("H-21 Rasterzahl 0", replace(VG, suchraster=0)),
                      ("H-25 kalkulatorischer Zins -1 %", replace(VG, kalk_zins=D("-0.01"))), ("H-33 Mindestansatz 150 %", replace(VG, bewirtschaftung_mindest=D("1.5")))):
        pruefe_gleich(k, f"Vorgabe ausserhalb ihres Bereichs, {name}: M-20", status(A.ANKAUF, vg_), ["eingabe", "M-20"])
    tp = tragbarer_preis(A.ANKAUF, replace(VG, suchraster=0), KAT)
    pruefe_gleich(k, "H-21 Rasterzahl 0 in der Preissuche: M-20, kein Absturz", (tp["preis"], tp["meldung"]), (None, "M-20"))
    # ---- Katalog (NG-31): fehlender Wert und fremdes Land enden mit M-47
    for name, ein, kat in (("Land Bayern mit dem Katalog fuer Niedersachsen", replace(A.ANKAUF, land="Bayern"), KAT),
                           ("andere Gemeinde", replace(A.ANKAUF, gemeinde="03241001"), KAT),
                           ("Kappungsgrenze fehlt", A.ANKAUF, replace(KAT, kappung=None)), ("Wartefrist fehlt", A.ANKAUF, replace(KAT, wartefrist=None)),
                           ("Hebesatz fehlt", replace(A.ANKAUF, steuer=A.steuer(KOERPERSCHAFT, hebesatz=None)), KAT),
                           ("Koerperschaftsteuersatz fehlt", replace(A.ANKAUF, steuer=A.steuer(KOERPERSCHAFT, kst_satz=None)), KAT),
                           ("Abschreibungssatz fehlt", A.ANKAUF, replace(KAT, afa_satz=None))):
        pruefe_gleich(k, f"Katalog, {name}: M-47, keine Rechnung", status(ein, VG, kat), ["eingabe", "M-47"])
    tp = tragbarer_preis(replace(A.ANKAUF, land="Bayern"), VG, KAT)
    pruefe_gleich(k, "Katalogwert fehlt in der Preissuche: M-47", (tp["preis"], tp["meldung"]), (None, "M-47"))
    # ---- M-24 in Suchen und Tabelle (NG-33)
    ohne_zins = replace(GEFOERDERT, foerderung=replace(A.FOERDERUNG_B, zins_danach=None))
    tp = tragbarer_preis(ohne_zins, VG, KATN)
    pruefe_gleich(k, "Grobfoerderung ohne Zins nach der zinslosen Zeit: Preissuche endet mit M-24", (tp["preis"], tp["meldung"]), (None, "M-24"))
    s = suche_eingabe(ohne_zins, VG, KATN, "verkaufsfaktor", D(10), D(30), D("0.01"), raster=4)
    pruefe_gleich(k, "... Zielwertsuche: jeder Gitterwert endet mit M-24", s["status"], "keine Suche: jeder Gitterwert endet mit M-24")
    pruefe_gleich(k, "... Haltedauertabelle 37 und 38 Jahre: M-24 je Zeile", [x[3] for x in haltedauer_tabelle(ohne_zins, VG, KATN, 37, 38)], ["M-24", "M-24"])
    # ---- ohne eingesetztes Eigenkapital (NG-25, NG-37)
    voll = replace(OHNE_STAU, enk_satz=NULL, verkaufsfaktor=D(5))
    vgv = replace(VG, beleihungsquote=EINS, mindestdeckung=EINS, ma026_vertragszins=True)
    tp = tragbarer_preis(replace(voll, verfuegbares_ek=NULL), vgv, KAT)
    pruefe_fest(k, "Vollfinanzierung, verfuegbares Eigenkapital 0: kein tragbarer Preis (M-41), bindende Grenze, Nebenangabe",
                [tp["preis"], tp["meldung"], tp["bindend"], tp.get("nebenangabe")])
    s = suche_eingabe(replace(voll, kaufpreis=D(1500000)), vgv, KAT, "verkaufsfaktor", D(4), D(8), D("0.01"), raster=8)
    pruefe_fest(k, "Zielwertsuche ohne eingesetztes Eigenkapital: Status, Meldungen, Zahl der Gitterwerte ohne Eigenkapital",
                [s["status"], s["meldungen"], len(s["ohne_eigenkapital"]) > 0])
    # ---- M-34 nur aus der bindenden Grenze (NG-24)
    z = replace(VG, zielrendite=D("0.05000253"))
    tpr = tragbarer_preis(A.ANKAUF, z, KAT)
    tpe = tragbarer_preis(replace(A.ANKAUF, verfuegbares_ek=D(1200000)), z, KAT)
    pruefe_gleich(k, "Zielrendite 5,000253 %: M-34 aus der Renditegrenze; bindet das Eigenkapital, kein M-34",
                  [(tpr["bindend"], tpr["meldung"]), (tpe["bindend"], tpe["meldung"])], [("Rendite", "M-34"), ("Eigenkapital", None)])
    # ---- Sprungstelle der 15-%-Regel in der Preissuche (NG-32)
    sprung = replace(A.ANKAUF, stau_betrag=D(336000), stau_jahr=1)
    tp = tragbarer_preis(sprung, replace(VG, zielrendite=D("0.0371259")), KAT)
    pruefe_gleich(k, "Erhaltung 336.000 Euro im Jahr 1, Zielrendite 3,71259 %: Preis nach der Definition R-11.4 mit M-34 (Bericht Grenzfaelle: 2.350.070)",
                  (tp["preis"], tp["meldung"]), (2350070, "M-34"))
    e1, e2 = (rechne_grob(sprung, VG, KAT, preis=x, mit_blatt=False) for x in (2350089, 2350090))
    pruefe_gleich(k, "... Schwellenpreis: bis 2.350.089 Euro aktiviert (M-36), ab 2.350.090 Euro sofort abziehbar",
                  ("M-36" in kennungen(e1), "M-36" in kennungen(e2)), (True, False))
    # ---- Nachsuche: das Ergebnis selbst erfuellt das Ziel (Bericht Praktiker 3); Stuetzstellen ganzzahlig
    f = lambda x: D(1) if (x <= 1000 or x in (1003, 1004)) else D(-1)
    pruefe_gleich(k, "Preisgrenze einer Pruefunktion (erreicht bis 1.000, verfehlt 1.001 und 1.002, erreicht 1.003 und 1.004): 1.000 mit Mehrfachwechsel",
                  preisgrenze(f, 1, 5000, 40, 20), (1000, "eine", True))
    g = lambda x: D(1) if x <= 3000 else D(-1)
    pruefe_gleich(k, "Preisgrenze ohne Mehrfachwechsel: 3.000", preisgrenze(g, 1, 5000, 40, 20), (3000, "eine", False))
    s = zielwertsuche(lambda x: 1 - x, 1, 18, 1, 5)
    pruefe_gleich(k, "Stuetzstellen: Bereich 1 bis 18, fuenf Rasterschritte: Indizes (i x 17) div 5", s["punkte"], [0, 3, 6, 10, 13, 17])
    pruefe_gleich(k, "Zielwertsuche: bei steigendem Wechsel der erste Gitterwert, an dem das Ziel erreicht ist",
                  [(str(l["wert"]), l["richtung"]) for l in zielwertsuche(lambda x: x - D("2.5"), 0, 10, 1, 5)["loesungen"]], [("3", "steigend")])
    # ---- Warnschwellen (H-20, M-48)
    e = rechne_grob(replace(OHNE_STAU, haltedauer=1), VG, KAT)
    pruefe_fest(k, "Verkauf nach einem Jahr: Warnschwelle Restwertanteil 95 % ueberschritten (Kennzahl, Wert in %)",
                [[w[0], q(w[1] * 100, "0.01")] for w in e.warnungen])
    e = rechne_grob(replace(A.ANKAUF, verkaufsfaktor=D(20)), VG, KAT)
    pruefe_fest(k, "Verkaufsfaktor 20 bei Einstiegsfaktor 18,10: Warnschwelle fuer den Abstand der Faktoren (1,0) ueberschritten",
                [[w[0], q(w[1], "0.01")] for w in e.warnungen] + [m for m in kennungen(e) if m == "M-48"])
    pruefe_gleich(k, "Referenzobjekt Ankauf: keine Warnschwelle ueberschritten", "M-48" in kennungen(rechne_grob(A.ANKAUF, VG, KAT)), False)
    # ---- Vergleich ueber das ganze Blatt, mit anderem Katalogstand (Bericht Controller 4); Herkunft je Wert
    a = dict(basis=rechne_grob(A.ANKAUF, VG, KAT), stress=rechne_grob(A.ANKAUF, VG, KAT, stress=True),
             preis=tragbarer_preis(A.ANKAUF, VG, KAT), preis_stress=tragbarer_preis(A.ANKAUF, VG, KAT, stress=True))
    b_ein = replace(A.ANKAUF, steuer=A.steuer(KOERPERSCHAFT, kst_satz=lambda jahr: D("0.15")))
    b = dict(basis=rechne_grob(b_ein, VG, KAT), stress=rechne_grob(b_ein, VG, KAT, stress=True),
             preis=tragbarer_preis(b_ein, VG, KAT), preis_stress=tragbarer_preis(b_ein, VG, KAT, stress=True))
    v = vergleiche(a, b)
    zeilen = {z_[0]: z_ for z_ in v["zeilen"]}
    pruefe_fest(k, "Vergleich gleicher Eingaben mit anderem Katalogstand (Koerperschaftsteuer 15 % in allen Jahren): Zahl der Zeilen, abweichende Werte (Herkunft, Name)",
                [len(v["zeilen"]), [[x[0], x[1]] for x in v["abweichende_werte"]]])
    pruefe(k, "... Differenz der Endwertdifferenz (Gegenrechnung Controller)", zeilen["Endwertdifferenz"][3], "-56063.35", "0")
    pruefe_fest(k, "... Differenz des tragbaren Preises im Basis- und im Stressfall",
                [str(zeilen["tragbarer Preis: preis"][3]), str(zeilen["tragbarer Preis im Stressfall: preis"][3])])
    hebe = replace(A.ANKAUF, steuer=A.steuer(KOERPERSCHAFT, hebesatz=D("4.40")))
    v2 = vergleiche(a["basis"], rechne_grob(hebe, VG, KAT))
    pruefe_gleich(k, "Hebesatz 440 % statt 400 %: Herkunft Katalog", [[x[0], x[1]] for x in v2["abweichende_werte"]], [["KAT", "steuer.hebesatz"]])
    w = auftragswerte(a["basis"])
    pruefe_fest(k, "Herkunft je Wert des Auftrags: Zahl der Werte je Herkunft (E, H, KAT, MA)",
                {h: sum(1 for x in w if x[0] == h) for h in ("E", "H", "KAT", "MA")})


def alle():
    rf12_runde2()
    rf13_runde2()
    rf16_runde2()
    rf17_runde2()
    rf18_runde2()
    rf19_runde2()
    rf20_runde2()
