"""Referenzfaelle RF-08 bis RF-10: Darlehensarten, Regel des Bankdarlehens, Steuer in Kurzform."""
from decimal import Decimal as D
from zahlen import NULL, EINS, d, de, Rundung
from zeit import Raster
from darlehen import Tranche, bankdarlehen
from steuer import (Steuer, KOERPERSCHAFT, GEWERBLICHE_PG, GEPRAEGTE_PG, EINZELUNTERNEHMEN, PRIVAT, BEFREIT)
from proben import pruefe_plan
import annahmen as A
from rf_rahmen import (pruefe_fest, fall, pruefe, pruefe_proz, pruefe_reihe, pruefe_proben, pruefe_gleich, info, jahresplan,
                       lehrbuch_steuer)
from rf_testfall import s1, REINERTRAG

CENT, KEINE = Rundung("cent"), Rundung("keine")


def lauf(tr, perioden, p, rd=CENT, letzte=False):
    zeilen = [tr.periode(0, p, rd)]
    for u in range(1, perioden + 1):
        zeilen.append(tr.periode(u, p, rd, letzte=(letzte and u == perioden)))
    return zeilen


def rf08_darlehen():
    k = fall("RF-08", "Darlehensarten, Rundung je Rate (MA-013), Anschluss nach der Zinsbindung")
    # Prozentannuitaet 700.000 Euro, 4 %, Rate 3.500 Euro monatlich, zehn Jahre (Bericht A.2 Nr. 10)
    for art, soll in (("kaufm", "528208.51"), ("ab", "528207.91"), ("keine", "528208.56")):
        tr = Tranche("D", 700000, "annuitaet_prozent", "0.04", tilgungssatz="0.02", rundung=art)
        lauf(tr, 120, 12)
        pruefe(k, f"Prozentannuitaet, Rundung '{art}': Restschuld nach 120 Raten", tr.rest, soll,
               "0" if art != "keine" else "0.005")
    tr = Tranche("D", 700000, "annuitaet_prozent", "0.04", tilgungssatz="0.02")
    z = lauf(tr, 2, 12)
    pruefe_reihe(k, "Prozentannuitaet: Zins und Tilgung der Raten 1 und 2",
                 [z[1]["zins"], z[1]["tilgung"], z[2]["zins"], z[2]["tilgung"]],
                 ["2333.33", "1166.67", "2329.44", "1170.56"], "0")
    # Ratentilgung
    tr = Tranche("D", 600000, "raten", "0.03", laufzeit=20)
    z = lauf(tr, 5, 1)
    pruefe_reihe(k, "Ratentilgung 600.000, 3 %, 20 Jahre: Zins Jahr 1 bis 3", [x["zins"] for x in z[1:4]],
                 ["18000", "17100", "16200"], "0")
    pruefe(k, "Ratentilgung: Restschuld nach fuenf Jahren", tr.rest, "450000", "0")
    tr = Tranche("D", 100000, "raten", "0.03", laufzeit=7)
    z = lauf(tr, 7, 12)
    pruefe_reihe(k, "Ratentilgung 100.000 in sieben Monatsraten: Rate 1 und Schlussrate",
                 [z[1]["tilgung"], z[7]["tilgung"]], ["14285.71", "14285.74"], "0")
    pruefe(k, "Ratentilgung: Restschuld nach der Schlussrate", tr.rest, "0", "0")
    # endfaellig
    tr = Tranche("D", 500000, "endfaellig", "0.035")
    z = lauf(tr, 60, 12, letzte=True)
    pruefe(k, "endfaellig 500.000, 3,5 %: Monatszins", z[1]["zins"], "1458.33", "0")
    pruefe(k, "endfaellig: Abloesung am Ende", z[60]["abloesung"], "500000", "0")
    # Laufzeitannuitaet und Zins null (Randfall R-14.1)
    tr = Tranche("D", 700000, "annuitaet_laufzeit", 0, laufzeit=20)
    z = lauf(tr, 20, 1)
    pruefe(k, "Laufzeitannuitaet bei Zins null: Rate = gleichmaessige Tilgung", z[1]["tilgung"], "35000", "0")
    pruefe(k, "Laufzeitannuitaet bei Zins null: Restschuld am Ende", tr.rest, "0", "0")
    tr = Tranche("D", 700000, "annuitaet_laufzeit", "0.0001", laufzeit=20)
    z = lauf(tr, 20, 1)
    pruefe(k, "Laufzeitannuitaet bei 0,01 % Zins: Rate (Naeherung K/m x (1 + i x (m + 1) / 2) = 35.036,75)",
           z[1]["zins"] + z[1]["tilgung"], "35036.76", "0")
    pruefe(k, "Laufzeitannuitaet bei 0,01 % Zins: Restschuld am Ende", tr.rest, "0", "0")
    tr = Tranche("D", 700000, "annuitaet_prozent", 0, tilgungssatz="0.02")
    z = lauf(tr, 12, 12)
    pruefe(k, "Prozentannuitaet bei Zins null: Monatsrate", z[1]["tilgung"], "1166.67", "0")
    # Anschluss nach der Zinsbindung (R-5.9): 1.496.000 Euro, 4 % und 2 %, zehn Jahre Bindung, danach 6 %
    # "Restlaufzeit bleibt": rechnerische Restlaufzeit 18,011 Jahre, abgerundet auf 18 Perioden (R-5.9)
    for regel, soll in (("tilgungssatz", "90942"), ("rate", "89760"), ("restlaufzeit", "104989")):
        tr = Tranche("D", 1496000, "annuitaet_prozent", "0.04", tilgungssatz="0.02", bindung=10,
                     anschluss_zins="0.06", anschluss_regel=regel, rundung="keine")
        z = lauf(tr, 11, 1, KEINE)
        pruefe(k, f"Anschluss, Regel '{regel}': Rate ab Jahr 11", z[11]["zins"] + z[11]["tilgung"], soll, "1.5", 0)
    tr = Tranche("D", 1496000, "annuitaet_prozent", "0.04", tilgungssatz="0.02", bindung=10, rundung="keine")
    try:
        lauf(tr, 11, 1, KEINE)
        gemeldet = False
    except ValueError:
        gemeldet = True
    pruefe_gleich(k, "fehlender Anschlusszins wird gemeldet statt still fortgeschrieben", gemeldet, True)
    pruefe(k, "Restlaufzeit einer Prozentannuitaet nach zehn Jahren (reell, vor dem Abrunden)",
           Tranche.restlaufzeit(D("1136777.27"), D(89760), D("0.04")), "18.011", "0.0005", 3)
    # R-5.9, R-14.1: Regel "Restlaufzeit bleibt" ohne Tilgung faellt auf "Tilgungssatz bleibt" zurueck (M-40)
    tr = Tranche("D", 1000000, "annuitaet_prozent", "0.04", tilgungssatz=0, bindung=2, anschluss_zins="0.05",
                 anschluss_regel="restlaufzeit")
    z = lauf(tr, 3, 1)
    pruefe(k, "Restlaufzeit bleibt bei Tilgung null: Rate ab Jahr 3 ist der Zins", z[3]["zins"] + z[3]["tilgung"], "50000", "0")
    pruefe_gleich(k, "... Hinweis M-40", tr.hinweise, ["M-40"])
    # R-5.11: Rate des uebernommenen Darlehens aus dem urspruenglichen Nennbetrag
    tr = Tranche("D", 500000, "annuitaet_prozent", "0.005", tilgungssatz="0.02", rate_betrag=600000)
    z = lauf(tr, 1, 12)
    pruefe(k, "uebernommenes Darlehen, Nennbetrag 600.000, Restschuld 500.000: Monatsrate", z[1]["zins"] + z[1]["tilgung"], "1250.00", "0")
    # R-5.18: Bereitstellungszins auf den nicht ausgezahlten Betrag nach der bereitstellungsfreien Zeit
    tr = Tranche("D", 1200000, "annuitaet_prozent", "0.04", tilgungssatz="0.02", auszahlung={3: 400000, 6: 800000},
                 tilgungsbeginn=7, bereit_satz="0.0025", bereit_frei=2)
    z = lauf(tr, 7, 12)
    pruefe_reihe(k, "Bereitstellungszins Monate 1 bis 7 (0,25 % je Monat, zwei Monate frei)", [x["bereit"] for x in z[1:8]],
                 ["0", "0", "3000", "2000", "2000", "2000", "0"], "0")
    # Foerderdarlehen: zinslos, Entgelt einbehalten, Verwaltungskostenbeitrag, Tilgung ueber 42 Jahre (MA-002, MA-003)
    tr = Tranche("F", 2320000, "raten", 0, laufzeit=42, einbehalt=23200, beitrag_satz="0.005", bindung=35,
                 anschluss_zins="0.05", bank=False, foerder=True)
    z = lauf(tr, 36, 1)
    pruefe(k, "Foerderdarlehen 2,32 Mio.: einbehaltenes Entgelt bei Auszahlung", z[0]["einbehalt"], "23200", "0")
    pruefe(k, "Foerderdarlehen: Verwaltungskostenbeitrag Jahr 1", z[1]["beitrag"], "11600", "0")
    pruefe(k, "Foerderdarlehen: Restschuld nach 35 Jahren (ein Sechstel, Rate 55.238,10)", tr.rest + z[36]["tilgung"], "386666.50", "0")
    pruefe(k, "Foerderdarlehen: Zins im 36. Jahr bei angenommenen 5 %", z[36]["zins"], "19333.33", "0")
    # Disagio, Tilgungszuschuss, Barzuschuss mit Entgelt im Finanzplan: Proben schliessen (Bericht A.4 Nr. 22, 23)
    tr = Tranche("Bankdarlehen", 700000, "annuitaet_prozent", "0.04", tilgungssatz="0.02", einbehalt=21000,
                 tilgungszuschuss={3: 35000})
    zus = [D(100000)] + [NULL] * 5
    plan, alt, kz = jahresplan(5, 1100000, [x.quantize(D("0.01")) for x in REINERTRAG], 400000, [tr], "0.02", "0.08",
                               steuer=lehrbuch_steuer("0.30", verkauf_pflichtig=False), verkauf=1150000, afa=17600,
                               rundung="cent", zuschuss=zus)
    plan.e.zuschuss_einbehalt = None
    pruefe_proben(k, plan, alt, "Disagio 21.000, Tilgungszuschuss 35.000, Zuschuss 100.000: Kontrollsummen")
    pruefe(k, "Tilgungszuschuss mindert die Restschuld ohne Geldfluss (Bestandsprobe, Glied)", plan.zeilen[3]["tilgungszuschuss"], "35000", "0")
    pruefe(k, "Disagio: Auszahlung netto in t0", plan.zeilen[0]["auszahlung"] - plan.zeilen[0]["einbehalt"], "679000", "0")
    # Vorfaelligkeitsentschaedigung (R-5.16): Bindung zehn Jahre, Verkauf nach fuenf, Satz 1 % je Jahr (Annahme)
    tr = Tranche("Bankdarlehen", 700000, "annuitaet_prozent", "0.04", tilgungssatz="0.02", bindung=10, anschluss_zins="0.05")
    r = Raster(1, 5)
    from finanzplan import PlanEingabe, Verkauf, rechne_plan
    re = [NULL] + [x.quantize(D("0.01")) for x in REINERTRAG]
    null = [NULL] * 6
    e = PlanEingabe(raster=r, miete=re, kosten=list(null), erhaltung=list(null), investition=[D(1100000)] + [NULL] * 5,
                    afa=[NULL] + [D(17600)] * 5, tranchen=[tr], steuer=lehrbuch_steuer("0.30", verkauf_pflichtig=False),
                    einlagen=[D(400000)] + [NULL] * 5, entnahmen=list(null), h_kurz=D("0.02"), kk_zins=D("0.08"),
                    verkauf=Verkauf(preis_brutto=D(1150000), buchwert=D(1012000)), vfe_satz=D("0.01"))
    plan = rechne_plan(e)
    pruefe(k, "Vorfaelligkeitsentschaedigung: 624.171,48 x 1 % x 5 Jahre", plan.zeilen[5]["vfe"], "31208.57", "0")
    pruefe(k, "Endwert mit Vorfaelligkeitsentschaedigung (abziehbar, 30 %)", plan.endwert, "562520.28", "0")
    pruefe_gleich(k, "Vorfaelligkeit: Kontrollsummen", len(pruefe_plan(plan)), 0)


def rf09_bankdarlehen():
    k = fall("RF-09", "Regel des Bankdarlehens R-5.12 (MA-026): drei bindende Grenzen, Null, andere Lesart")
    # kalkulatorischer Zins 4 % und kalkulatorische Tilgung 2 % als Annahme der Beispiele (Werte des Berichts D.4)
    kw = dict(mindestdeckung=D("1.2"), zins_kalk=D("0.04"), tilgung_kalk=D("0.02"), p=1)
    # frei finanzierter Ankauf (Bericht D.4): Reinertrag 107.712
    b = bankdarlehen(D(2600000), D("0.65"), D(107712), mittelbedarf=D(2600000) * D("1.07"), **kw)
    pruefe(k, "Ankauf 2,6 Mio.: Grenze (a) Beleihungsquote", b["a"], "1690000", "0")
    pruefe(k, "Ankauf 2,6 Mio.: Grenze (b) Mindestdeckung", b["b"], "1496000", "0")
    pruefe(k, "Ankauf 2,6 Mio.: Bankdarlehen", b["darlehen"], "1496000", "0")
    pruefe_gleich(k, "Ankauf 2,6 Mio.: bindende Grenze", b["bindend"], ["b"])
    pruefe(k, "Ankauf 2,6 Mio.: Eigenkapital", b["eigenkapital"], "1286000", "0")
    b = bankdarlehen(D(2200000), D("0.65"), D(107712), mittelbedarf=D(2200000) * D("1.07"), **kw)
    pruefe(k, "Ankauf 2,2 Mio.: Bankdarlehen", b["darlehen"], "1430000", "0")
    pruefe_gleich(k, "Ankauf 2,2 Mio.: bindende Grenze", b["bindend"], ["a"])
    pruefe(k, "Knick: Preis, an dem (a) und (b) gleich sind", D(1496000) / D("0.65"), "2301538.46")
    # Ankauf mit uebernommenem Foerderdarlehen (Bericht D.4)
    kw6 = dict(kw)
    b = bankdarlehen(D(2000000), D("0.65"), D(140000), mittelbedarf=D(2200000), uebrige_darlehen=D(1000000),
                     kd_uebrige=D(25000), **kw6)
    pruefe(k, "Ankauf mit uebernommenem Darlehen 1,0 Mio.: Bankdarlehen", b["darlehen"], "300000", "0")
    pruefe_gleich(k, "... bindende Grenze", b["bindend"], ["a"])
    pruefe(k, "... Eigenkapital", b["eigenkapital"], "900000", "0")
    b = bankdarlehen(D(2000000), D("0.65"), D(140000), mittelbedarf=D(2200000), uebrige_darlehen=D(1000000),
                     uebrige_im_beleihungsraum=NULL, kd_uebrige=D(25000), **kw6)
    pruefe(k, "... Rang nach der Bank (Eingabe E-59): Grenze (a)", b["a"], "1300000", "0")
    pruefe(k, "... Rang nach der Bank: Grenze (b) unveraendert ueber alle Darlehen", b["b"], "1527777.74", "0")
    pruefe(k, "... Rang nach der Bank: Bankdarlehen", b["darlehen"], "1200000", "0")
    pruefe_gleich(k, "... Rang nach der Bank: bindende Grenze (Restfinanzierung)", b["bindend"], ["c"])
    pruefe(k, "... Rang nach der Bank: Eigenkapital", b["eigenkapital"], "0", "0")
    # gefoerderter Neubau (Bericht D.4): 10 Mio. Gesamtkosten, 9 Mio. zuwendungsfaehig, Gruppe B
    fd, zs, ekm = D(5400000), D(1800000), D(1800000)
    kd_fd = fd / 42 + fd * D("0.005")
    pruefe(k, "Neubau: Kapitaldienst des Foerderdarlehens im Jahr", kd_fd, "155571.43")
    nb = dict(mittelbedarf=D(10000000), uebrige_darlehen=fd, kd_uebrige=kd_fd, zuschuesse=zs, ek_min=ekm, **kw6)
    b = bankdarlehen(D(10000000), D("0.65"), D(400000), **nb)
    pruefe(k, "Neubau, Quote 65 %: Bankdarlehen", b["darlehen"], "1000000", "0")
    pruefe_gleich(k, "Neubau, Quote 65 %: bindende Grenze (Restfinanzierung)", b["bindend"], ["c"])
    b = bankdarlehen(D(10000000), D("0.60"), D(400000), **nb)
    pruefe(k, "Neubau, Quote 60 %: Bankdarlehen", b["darlehen"], "600000", "0")
    pruefe_gleich(k, "Neubau, Quote 60 %: bindende Grenze (Beleihungsquote)", b["bindend"], ["a"])
    pruefe(k, "Neubau, Quote 60 %: Eigenkapital", b["eigenkapital"], "2200000", "0")
    b = bankdarlehen(D(10000000), D("0.65"), D(200000), **nb)
    pruefe(k, "Neubau, Reinertrag 200.000: Bankdarlehen (geschlossen 184.920,63; Rate gerundet)", b["darlehen"], "184920.58", "0")
    pruefe_gleich(k, "Neubau, Reinertrag 200.000: bindende Grenze (Mindestdeckung)", b["bindend"], ["b"])
    pruefe(k, "Schwelle des Reinertrags, ab der etwas fuer die Bank bleibt", kd_fd * D("1.2"), "186685.71")
    b = bankdarlehen(D(10000000), D("0.65"), D(180000), **nb)
    pruefe(k, "Neubau, Reinertrag 180.000: Bankdarlehen null", b["darlehen"], "0", "0")
    pruefe_gleich(k, "Neubau, Reinertrag 180.000: Meldung M-21", b["meldung"], "M-21")
    pruefe(k, "Neubau, Reinertrag 180.000: Eigenkapital", b["eigenkapital"], "2800000", "0")
    b = bankdarlehen(D(10000000), D("0.60"), D(180000), uebrige_im_beleihungsraum=NULL, **nb)
    pruefe(k, "Neubau, Foerderdarlehen im Nachrang (andere Lesart MA-026): Grenze (a)", b["a"], "6000000", "0")
    pruefe(k, "... Bankdarlehen bleibt null, weil die Deckung immer alle Darlehen rechnet", b["darlehen"], "0", "0")
    pruefe_gleich(k, "... Meldung M-21", b["meldung"], "M-21")
    b = bankdarlehen(D(10000000), D("0.60"), D(400000), uebrige_im_beleihungsraum=NULL, **nb)
    pruefe(k, "Neubau, Foerderdarlehen im Nachrang, Reinertrag 400.000: Bankdarlehen", b["darlehen"], "1000000", "0")
    pruefe_gleich(k, "... bindende Grenze (Restfinanzierung)", b["bindend"], ["c"])
    # R-14.1: kalkulatorischer Zins und Tilgung null: (b) bindet nicht oder sperrt
    kw0 = dict(mindestdeckung=D("1.2"), zins_kalk=NULL, tilgung_kalk=NULL, p=12)
    b = bankdarlehen(D(2400000), D("0.65"), D(100000), mittelbedarf=D(2640000), **kw0)
    pruefe_gleich(k, "Zins und Tilgung null: (b) unbegrenzt, es bindet (a)", (b["b"], b["bindend"], str(b["darlehen"])), (None, ["a"], "1560000.00"))
    b = bankdarlehen(D(2400000), D("0.65"), D(10000), mittelbedarf=D(2640000), uebrige_darlehen=D(500000), kd_uebrige=D(12500), **kw0)
    pruefe_gleich(k, "Zins und Tilgung null, Ertrag deckt die uebrigen Darlehen nicht: null mit M-21", (b["darlehen"] == 0, b["meldung"]), (True, "M-21"))
    # Rundung der Rate auf der sicheren Seite (Monatsraster)
    b = bankdarlehen(D(2600000), D("0.65"), D("107712.37"), D("1.2"), D("0.04"), D("0.02"), D(2782000), p=12)
    pruefe(k, "Monatsraster: Bankdarlehen bei 107.712,37 Euro Reinertrag", b["darlehen"], "1496004.99", "0")
    kd = 12 * CENT.geld(b["darlehen"] * D("0.06") / 12)
    pruefe_gleich(k, "Monatsraster: gerundete Raten halten die Mindestdeckung ein", D("107712.37") / kd >= D("1.2"), True)
    info(f"Monatsraster: Darlehen {de(b['darlehen'])}, Kapitaldienst {de(kd)}, Deckung {de(D('107712.37') / kd, 6)}")


def rf10_steuer():
    k = fall("RF-10", "Steuer in Kurzform je Steuerstatus (angenommener Katalogstand, annahmen.py)")
    r = Raster(1, 12, startjahr=2027)

    def st(status, **kw):
        return Steuer(A.steuer(status, **kw), r, CENT)

    # Koerperschaft
    s = st(KOERPERSCHAFT, verlust="sofort")
    pruefe(k, "Koerperschaft 2027, 100.000 Ergebnis, ohne Kuerzung", s.jahr(1, D(100000), NULL), "29825", "0")
    pruefe(k, "Koerperschaft 2032, 100.000 Ergebnis, ohne Kuerzung", s.jahr(6, D(100000), NULL), "24550", "0")
    s = st(KOERPERSCHAFT, erweiterte_kuerzung=True)
    pruefe(k, "Koerperschaft 2027, mit erweiterter Kuerzung", s.jahr(1, D(100000), NULL), "15825", "0")
    s = st(KOERPERSCHAFT)
    pruefe(k, "Koerperschaft, Verlustvortrag: Jahr 1 mit -50.000", s.jahr(1, D(-50000), NULL), "0", "0")
    pruefe(k, "Koerperschaft, Verlustvortrag: Jahr 2 mit +80.049 (Satz 2028, Abrundung auf 100)", s.jahr(2, D(80049), NULL), "8638.24", "0")
    info(f"Teile Jahr 2: {s.protokoll[-1]['koerperschaftsteuer']} Koerperschaftsteuer, {s.protokoll[-1]['gewerbesteuer']} Gewerbesteuer")
    s = st(KOERPERSCHAFT, verlust="sofort")
    pruefe(k, "Koerperschaft, sofortige Verrechnung (andere Lesart MA-016): -50.000", s.jahr(1, D(-50000), NULL), "-14912.50", "0")
    # gewerbliche Personengesellschaft: Bericht B.3 (Messbetrag 2.642,50)
    for hebesatz, gew, anr, summe in (("4.00", "10570", "10570", "42000"), ("2.80", "7399", "7399", "42000"),
                                      ("4.80", "12684", "10570", "44114")):
        s = st(GEWERBLICHE_PG, hebesatz=D(hebesatz))
        steuer = s.jahr(1, D(100000), NULL)
        p = s.protokoll[-1]
        pruefe(k, f"Personengesellschaft, Hebesatz {hebesatz}: Gewerbesteuer", p["gewerbesteuer"], gew, "0")
        pruefe(k, f"Personengesellschaft, Hebesatz {hebesatz}: Anrechnung", p["anrechnung"], anr, "0")
        pruefe(k, f"Personengesellschaft, Hebesatz {hebesatz}: Steuer gesamt", steuer, summe, "0")
    pruefe(k, "Personengesellschaft: Messbetrag bei 100.000 Gewerbeertrag", p["messbetrag"], "2642.50", "0")
    s = st(GEWERBLICHE_PG, anteil_natuerliche=D("0.5"))
    pruefe(k, "Personengesellschaft, Anteil natuerlicher Personen 50 %: Steuer", s.jahr(1, D(100000), NULL), "47285", "0")
    s = st(GEWERBLICHE_PG, est_satz=D("0.08"))
    s.jahr(1, D(100000), NULL)
    pruefe(k, "Personengesellschaft, Einkommensteuer 8.000 begrenzt die Anrechnung", s.protokoll[-1]["anrechnung"], "8000", "0")
    s = st(GEPRAEGTE_PG, erweiterte_kuerzung=True)
    pruefe(k, "gewerblich gepraegte Personengesellschaft mit erweiterter Kuerzung, ohne Zinsen: nur Einkommensteuer", s.jahr(1, D(100000), NULL), "42000", "0")
    s = st(GEWERBLICHE_PG)
    s.jahr(1, D(20000), NULL)
    pruefe(k, "Personengesellschaft, Gewinn 20.000 unter dem Freibetrag: Gewerbesteuer", s.protokoll[-1]["gewerbesteuer"], "0", "0")
    s = st(EINZELUNTERNEHMEN, anteil_natuerliche=D("0.5"))
    pruefe(k, "Einzelunternehmen: Anteil ist stets 100 %", s.jahr(1, D(100000), NULL), "42000", "0")
    # Privatperson
    s = st(PRIVAT, haltedauer=10)
    pruefe(k, "Privat: 30.000 Vermietung, 1.000 Zinsen", s.jahr(1, D(30000), D(1000)), "12863.75", "0")
    pruefe(k, "Privat: Verkauf nach zehn Jahren, Gewinn 200.000 steuerpflichtig", s.jahr(10, NULL, NULL, D(200000)), "84000", "0")
    s = st(PRIVAT, haltedauer=11)
    pruefe(k, "Privat: Verkauf nach elf Jahren steuerfrei", s.jahr(11, NULL, NULL, D(200000)), "0", "0")
    s = st(PRIVAT, haltedauer=11)
    s.jahr(1, D(-10000), D(500))
    pruefe(k, "Privat: Vermietungsverlust mindert die Steuer auf Zinsen nicht", s.protokoll[-1]["steuer"], "131.88", "0")
    pruefe(k, "Befreite Koerperschaft: Steuer null", st(BEFREIT).jahr(1, D(100000), D(1000), D(500000)), "0", "0")
    # Verlustverrechnung im Finanzplan (MA-016): Testfall mit Anlaufverlust, Reinertrag 20.000 und 30.000
    re = [D(20000), D(30000)] + REINERTRAG[2:]
    p_s, a_s, k_s = s1(reinertrag=re, rundung="cent", steuer=lehrbuch_steuer("0.30", "sofort", False))
    p_v, a_v, k_v = s1(reinertrag=re, rundung="cent", steuer=lehrbuch_steuer("0.30", "vortrag", False))
    pruefe_fest(k, "Anlaufverlust, Vortrag im Vorhaben (Voreinstellung MA-016): Endwert", p_v.endwert)
    pruefe_fest(k, "Anlaufverlust, sofortige Verrechnung (andere Lesart): Endwert", p_s.endwert)
    pruefe_fest(k, "Vortrag: Steuer t1..t5", [str(x) for x in p_v.reihe("steuer")[1:]])
    pruefe_fest(k, "Vortrag: Verlustvortrag am Ende", p_v.steuer.vv)
    pruefe_fest(k, "sofort: Steuer t1..t5", [str(x) for x in p_s.reihe("steuer")[1:]])
    pruefe_proben(k, p_v, a_v, "Anlaufverlust: Kontrollsummen")
    # steuerpflichtiger Verkaufsgewinn ueber den Buchwert
    p_g, a_g, k_g = s1(steuer=lehrbuch_steuer("0.30", "sofort", True))
    pruefe(k, "Testfall mit steuerpflichtigem Verkaufsgewinn 138.000: Endwert", p_g.endwert, "542966.28")
    pruefe(k, "... Steuer auf den Verkaufsgewinn", p_g.zeilen[5]["g_v"] * D("0.3"), "41400", "0")


def alle():
    rf08_darlehen()
    rf09_bankdarlehen()
    rf10_steuer()
