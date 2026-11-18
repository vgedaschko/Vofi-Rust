"""Referenzfaelle RF-05 bis RF-07: Testfall S1 mit Varianten, Kennzahlen, mehrere Einlagen und Entnahmen.

Eingaben des Testfalls: Bericht Anhang A.6 (Quellnotiz 03, Testfall S1). Die Werte sind in drei frueheren,
voneinander unabhaengigen Gegenrechnungen bestaetigt (skripte/finanzmathematik-pruefung, runde4, runde5).
"""
from decimal import Decimal as D
from zahlen import NULL, EINS, d, de, Rundung, kaufm, wurzel_rendite
from zeit import Raster
from darlehen import Tranche
from finanzplan import PlanEingabe, Verkauf, rechne_plan, rechne_alternative, verdichte
from kennzahlen import (werte_aus, vofi_rendite, schuldendienstdeckung, interner_zinsfuss, kapitalwert,
                        gesamtkapitalrendite, sollzinsen_nach_steuern, amortisationsdauer, endwertueberschuss,
                        zaehler_nenner)
from proben import pruefe_plan
from rf_rahmen import (pruefe_fest, fall, pruefe, pruefe_proz, pruefe_reihe, pruefe_proben, pruefe_gleich, info, jahresplan,
                       lehrbuch_steuer)

REINERTRAG = [D(55000) * D("1.02") ** t for t in range(5)]


def s1(ek=400000, einlagen=None, entnahmen=None, rundung="keine", reinertrag=None, h="0.02", kk="0.08",
       zins="0.04", a_lang=None, steuer=None, verkauf=1150000, darlehen=700000):
    tr = Tranche("Bankdarlehen", darlehen, "annuitaet_prozent", zins, tilgungssatz="0.02", rundung="kaufm")
    re = reinertrag or REINERTRAG
    if rundung == "cent":
        re = [kaufm(x) for x in re]
    plan, alt, kz = jahresplan(5, 1100000, re, ek, [tr], h, kk,
                               steuer=steuer or lehrbuch_steuer("0.30", verkauf_pflichtig=False),
                               verkauf=verkauf, afa=17600, einlagen=einlagen, entnahmen=entnahmen,
                               rundung=rundung, a_lang=a_lang)
    return plan, alt, kz


def s1_monat(h_eff, kk_eff, rundung):
    """Testfall im Monatsraster: Miete, Rate, Zinsen monatlich; Steuer am Ende jedes Planjahres (R-2.7)."""
    r = Raster(p=12, n=5)
    N = r.N
    rd = Rundung(rundung)
    miete = [NULL] + [rd.geld(REINERTRAG[r.planjahr(u) - 1] / 12) for u in range(1, N + 1)]
    null = [NULL] * (N + 1)
    afa = [NULL] + [rd.geld(D(17600) / 12)] * N
    tr = Tranche("Bankdarlehen", 700000, "annuitaet_prozent", "0.04", tilgungssatz="0.02",
                 rundung="kaufm" if rundung == "cent" else "keine")
    e = PlanEingabe(raster=r, miete=miete, kosten=list(null), erhaltung=list(null),
                    investition=[D(1100000)] + [NULL] * N, afa=afa, tranchen=[tr],
                    steuer=lehrbuch_steuer("0.30", verkauf_pflichtig=False),
                    einlagen=[D(400000)] + [NULL] * N, entnahmen=list(null), h_kurz=h_eff, kk_zins=kk_eff,
                    verkauf=Verkauf(preis_brutto=D(1150000), buchwert=D(1100000) - 5 * 17600), rundung=rd)
    plan = rechne_plan(e)
    alt = rechne_alternative(e, plan.einlagen_netto, plan.entnahmen_netto)
    return plan, alt, werte_aus(plan, alt)


class VerkaufNachSchulden(Verkauf):
    """Fehlerbild fuer P-05: Erloes nach Schulden angesetzt, obwohl die Restschuld abgeloest wird."""
    restschuld = NULL

    @property
    def erloes(self):
        return self.preis_brutto - self.kosten - self.stau_abzug - self.restschuld


def rf05_testfall():
    k = fall("RF-05", "Testfall S1 (Bericht A.6): Ankauf, fuenf Jahre, Jahresmodus")
    plan, alt, kz = s1()
    z = plan.zeilen
    pruefe(k, "Endwert", plan.endwert, "584366.28")
    pruefe(k, "Endwert der Unterlassensalternative", alt.endwert, "428795.05")
    pruefe(k, "Endwertdifferenz", kz["endwertdifferenz"], "155571.23")
    pruefe_proz(k, "VOFI-Eigenkapitalrendite", kz["rendite"], "7.876")
    pruefe_proz(k, "Vergleichsrendite der Unterlassensalternative", kz["vergleichsrendite"], "1.400")
    pruefe(k, "Abloesung der Restschuld in t5", z[5]["abloesung"], "624171.48")
    pruefe_reihe(k, "Steuer t1..t5", plan.reihe("steuer")[1:], ["2820.00", "3379.08", "3955.95", "4551.12", "5165.12"], "0.005")
    pruefe_reihe(k, "Guthaben t1..t4", plan.reihe("guthaben")[1:5], ["10180.00", "21104.52", "32792.66", "45263.84"], "0.005")
    pruefe(k, "Summe der Sollzinsen", sum(plan.reihe("zins")), "134171.48")
    pruefe_proben(k, plan, alt)
    dscr = [schuldendienstdeckung(plan, j)[0] for j in range(1, 6)]
    pruefe_reihe(k, "Schuldendienstdeckung t1..t5 (ohne Abloesung)", dscr, ["1.3095", "1.3357", "1.3624", "1.3897", "1.4175"], "0.00005")
    mit_abl = REINERTRAG[4] / (z[5]["zins"] + z[5]["tilgung"] + z[5]["abloesung"])
    pruefe(k, "zum Vergleich: Deckung t5 mit Abloesung im Nenner (falsch)", mit_abl, "0.09", "0.005")
    # Restwertanteil (R-10.16): Beitrag des Verkaufs nach Abloesung zum Endwert
    anteil = (z[5]["verkauf"] - z[5]["abloesung"]) / plan.endwert
    pruefe(k, "Restwertanteil am Endwert (%)", anteil * 100, "89.98", "0.005")
    # Gesamtkapitalrendite und Referenzzinsfuss (R-10.11, MA-028)
    zs = sollzinsen_nach_steuern(plan)
    g = gesamtkapitalrendite(kz["zaehler"], kz["nenner"], zs, D(1100000), 5)
    kref = gesamtkapitalrendite(kz["zaehler_alternative"], kz["nenner"], zs, D(1100000), 5)
    pruefe_proz(k, "VOFI-Gesamtkapitalrendite", g, "4.61", 2)
    pruefe_proz(k, "Referenzzinsfuss der Gesamtkapitalrendite", kref, "2.14", 2)
    # Amortisationsdauer (R-10.12, MA-027); Wertpfad der Nachrechnung: linear 1,00 -> 1,15 Mio. Euro
    verm = [None] + [z[t]["guthaben"] - z[t]["kk"] + D(1000000) + D(150000) * t / 5
                     - (z[t]["restschuld"] if t < 5 else z[5]["abloesung"]) for t in range(1, 6)]
    verm[5] = plan.endwert
    vergl = [None] + [alt.bestand(t) for t in range(1, 6)]
    pruefe_gleich(k, "Amortisationsdauer, Voreinstellung (Alternative dauerhaft erreicht)", amortisationsdauer(verm, vergl), 3)
    pruefe_gleich(k, "Amortisationsdauer, andere Lesart (Eigenkapital gedeckt)",
                  amortisationsdauer(verm, vergl, "eigenkapital", D(400000)), 2)
    # interner Zinsfuss der Eigenkapitalreihe
    izf, wechsel = interner_zinsfuss([D(-400000), 0, 0, 0, 0, plan.endwert])
    pruefe_proz(k, "interner Zinsfuss der Eigenkapitalreihe (= VOFI-Rendite bei einer Einlage)", izf[0], "7.876")
    # Plausibilitaetstest Hebelwirkung (R-15.5): Objektrendite ueber dem Kreditzins -> Rendite faellt mit dem Eigenkapital
    hebel = [s1(ek=ek, darlehen=1100000 - ek)[2]["rendite"] for ek in (300000, 400000, 500000, 600000)]
    pruefe_gleich(k, "Hebelwirkung positiv: VOFI-Rendite faellt mit dem Eigenkapital (300.000 bis 600.000)",
                  all(b_ < a_ for a_, b_ in zip(hebel, hebel[1:])), True)
    pruefe_fest(k, "Hebelwirkung: Renditen bei 300.000 / 400.000 / 500.000 / 600.000 Eigenkapital (%)",
                [str((x * 100).quantize(D("0.001"))) for x in hebel])
    # Cent-Rundung nach Kapitel 12
    plan_c, alt_c, kz_c = s1(rundung="cent")
    pruefe(k, "Endwert mit Rundung je Zahlung (Festschreibung)", plan_c.endwert, "584366.28", "0")
    pruefe(k, "Guthaben t4 mit Rundung je Zahlung", plan_c.zeilen[4]["guthaben"], "45263.83", "0")
    pruefe_fest(k, "Endwertdifferenz mit Rundung je Zahlung", kz_c["endwertdifferenz"])
    pruefe_proben(k, plan_c, alt_c, "Kontrollsummen (Rundungsmodus Cent, exakt null)")
    # P-05: Restschuld doppelt gezaehlt
    falsch = VerkaufNachSchulden(preis_brutto=D(1150000), buchwert=D(1012000))
    falsch.restschuld = z[5]["abloesung"]
    plan_f, _, _ = s1()
    e = plan_f.e
    e.verkauf = falsch
    e.tranchen = [Tranche("Bankdarlehen", 700000, "annuitaet_prozent", "0.04", tilgungssatz="0.02")]
    plan_f = rechne_plan(e)
    pruefe(k, "Fehlerbild Restschuld doppelt: Endwert", plan_f.endwert, "-39805.20")
    bef = [b for b in pruefe_plan(plan_f) if b[0] == "P-05"]
    pruefe(k, "Fehlerbild Restschuld doppelt: Restwertprobe P-05 meldet", bef[0][2] if bef else None, "-624171.48")


def rf06_varianten():
    k = fall("RF-06", "Varianten des Testfalls (Bericht A.6)")
    basis, alt0, kz0 = s1()
    # Entnahmen
    ent = {t: 5000 for t in range(1, 6)}
    plan, alt, kz = s1(entnahmen=ent)
    pruefe(k, "Entnahmen 5.000 je Jahr: Endwert", plan.endwert, "558656.41")
    pruefe(k, "Entnahmen: Endwertdifferenz unveraendert", kz["endwertdifferenz"], "155571.23")
    pruefe_proz(k, "Entnahmen: Rendite unveraendert", kz["rendite"], "7.876")
    pruefe(k, "Entnahmen ohne Spiegelung (falsch): Endwertdifferenz", plan.endwert - alt0.endwert, "129861.36")
    pruefe_proz(k, "Entnahmen ohne Spiegelung (falsch): Rendite", wurzel_rendite(plan.endwert / 400000, 5), "6.91", 2)
    pruefe_proben(k, plan, alt, "Entnahmen: Kontrollsummen")
    # Kontokorrent
    plan, alt, kz = s1(ek=380000)
    pruefe(k, "Kontokorrent (Eigenkapital 380.000): Endwert", plan.endwert, "561526.16")
    pruefe_reihe(k, "Kontokorrent: Stand t0..t3", plan.reihe("kk")[:4], ["20000", "10940", "770.64", "0"], "0.005")
    pruefe_proz(k, "Kontokorrent: Rendite", kz["rendite"], "8.123")
    plan, alt, kz = s1(ek=380000, entnahmen=ent)
    pruefe_proz(k, "Kontokorrent mit Entnahmen: Rendite", kz["rendite"], "8.089")
    pruefe_proben(k, plan, alt, "Kontokorrent mit Entnahmen: Kontrollsummen")
    # Nachschuss
    plan, alt, kz = s1(einlagen={2: 50000})
    pruefe(k, "Nachschuss 50.000 in t2: Endwert", plan.endwert, "636495.82")
    pruefe(k, "Nachschuss: Endwertdifferenz unveraendert", kz["endwertdifferenz"], "155571.23")
    pruefe_proz(k, "Nachschuss: Rendite nach R-10.5", kz["rendite"], "7.246")
    q = D("1.014")
    pruefe_proz(k, "Nachschuss, andere Lesart: Summe der Einlagen als Nenner", wurzel_rendite(plan.endwert / 450000, 5), "7.18", 2)
    izf, _ = interner_zinsfuss([D(-400000), 0, D(-50000), 0, 0, plan.endwert])
    pruefe_proz(k, "Nachschuss, andere Lesart: interner Zins der Eigenkapitalreihe", izf[0], "7.50", 2)
    pruefe_proz(k, "Nachschuss, andere Lesart: wie negative Entnahme aufgezinst",
                wurzel_rendite((plan.endwert - 50000 * q ** 3) / 400000, 5), "7.88", 2)
    plan_c, _, _ = s1(einlagen={2: 50000}, rundung="cent")
    pruefe(k, "Nachschuss mit Rundung je Zahlung (Festschreibung)", plan_c.endwert, "636495.81", "0")
    # Nachschuss und Entnahme
    plan, alt, kz = s1(einlagen={2: 50000}, entnahmen={2: 50000})
    pruefe(k, "Nachschuss und Entnahme in t2: Endwert wie Testfall", plan.endwert, "584366.28")
    pruefe_proz(k, "Nachschuss und Entnahme in t2: Rendite (saldiert)", kz["rendite"], "7.876")
    w = kz["w"]
    unsaldiert = vofi_rendite(plan.endwert, [D(400000), 0, D(50000), 0, 0, 0], [0, 0, D(50000), 0, 0, 0], w, 5)[0]
    pruefe_proz(k, "dasselbe unsaldiert (falsch)", unsaldiert, "7.246")
    plan, alt, kz = s1(einlagen={2: 50000}, entnahmen={3: 50000})
    pruefe(k, "Nachschuss t2, Entnahme t3: Endwert", plan.endwert, "585086.02")
    pruefe(k, "Nachschuss t2, Entnahme t3: Endwertdifferenz unveraendert", kz["endwertdifferenz"], "155571.23")
    pruefe_proz(k, "Nachschuss t2, Entnahme t3: Rendite", kz["rendite"], "7.246")
    pruefe_proben(k, plan, alt, "Nachschuss t2, Entnahme t3: Kontrollsummen")
    # Miete als Vorjahreswert
    plan, alt, kz = s1(reinertrag=[D(55000) * D("1.02") ** t for t in range(1, 6)])
    pruefe(k, "Miete als Vorjahreswert gelesen: Endwert", plan.endwert, "588484.91")
    pruefe_proz(k, "Miete als Vorjahreswert gelesen: Rendite", kz["rendite"], "8.028")
    # Monatsraster
    nominal = lambda i: (EINS + d(i) / 12) ** 12 - EINS
    plan, alt, kz = s1_monat(nominal("0.02"), nominal("0.08"), "keine")
    pruefe(k, "Monatsraster, Kontenzins nominal/12 wie im Bericht: Endwert", plan.endwert, "585937.57")
    pruefe(k, "Monatsraster wie im Bericht: Abloesung", plan.zeilen[60]["abloesung"], "622651.19")
    pruefe_proz(k, "Monatsraster wie im Bericht: Vergleichsrendite (effektiv)", kz["vergleichsrendite"], "1.413")
    plan, alt, kz = s1_monat(D("0.02"), D("0.08"), "cent")
    pruefe_fest(k, "Monatsraster nach Kapitel 2 (Kontenzins effektiv, Rundung je Zahlung): Endwert", plan.endwert)
    pruefe_fest(k, "Monatsraster nach Kapitel 2: Endwert der Unterlassensalternative", alt.endwert)
    pruefe_fest(k, "Monatsraster nach Kapitel 2: Abloesung", plan.zeilen[60]["abloesung"])
    pruefe_fest(k, "Monatsraster nach Kapitel 2: Rendite (%)", kz["rendite"] * 100, 3)
    pruefe_proz(k, "Monatsraster nach Kapitel 2: Vergleichsrendite", kz["vergleichsrendite"], "1.400")
    pruefe_proben(k, plan, alt, "Monatsraster: Kontrollsummen")
    jahre = verdichte(plan)
    pruefe(k, "Verdichtung: Jahressumme der Mieten Jahr 1", jahre[1]["miete"], "54999.96", "0")
    # einheitlicher Zins: Kapitalwertprobe P-13
    plan, alt, kz = s1(h="0.04", kk="0.04", steuer=lehrbuch_steuer("0.30", verkauf_pflichtig=False))
    qs = EINS + D("0.04") * D("0.7")
    reihe = [D(-1100000)] + [REINERTRAG[t] - D("0.3") * (REINERTRAG[t] - 17600) for t in range(5)]
    reihe[5] += 1150000
    kw = kapitalwert(reihe, qs - 1)
    pruefe(k, "einheitlicher Zins 4 %: Kapitalwert nach Steuern", kw, "110371.99")
    pruefe(k, "einheitlicher Zins 4 %: abgezinste Endwertdifferenz", kz["endwertdifferenz"] / qs ** 5, "110371.99")
    pruefe(k, "einheitlicher Zins 4 %: Probe P-13 (Differenz)", kz["endwertdifferenz"] / qs ** 5 - kw, "0", "0.000001", 6)
    q14 = D("1.014")
    reihe14 = [D(-1100000)] + [REINERTRAG[t] - D("0.3") * (REINERTRAG[t] - 17600) for t in range(5)]
    reihe14[5] += 1150000
    pruefe(k, "Testfall mit getrennten Saetzen: Kapitalwert", kapitalwert(reihe14, q14 - 1), "190202.20")
    pruefe(k, "Testfall mit getrennten Saetzen: abgezinste Endwertdifferenz", kz0["endwertdifferenz"] / q14 ** 5, "145124.09")


def rf07_einlagen_entnahmen():
    k = fall("RF-07", "Mehrere Einlagen und Entnahmen: Eigenschaften der Renditeformel (MA-012)")
    # Alternative mit zwei Zinssaetzen: langfristig 3 %, kurzfristig 2 %
    for name, kw in (("eine Einlage", {}), ("Nachschuss t2", dict(einlagen={2: 50000})),
                     ("Entnahmen 5.000 je Jahr", dict(entnahmen={t: 5000 for t in range(1, 6)})),
                     ("Nachschuss t2 und Entnahme t3", dict(einlagen={2: 50000}, entnahmen={3: 50000}))):
        plan, alt, kz = s1(a_lang="0.03", **kw)
        info(f"{name}: Endwert {de(plan.endwert)}, Alternative {de(alt.endwert)}, Differenz {de(kz['endwertdifferenz'])}, "
             f"Rendite {de(kz['rendite'] * 100, 3)} %, Vergleichsrendite {de(kz['vergleichsrendite'] * 100, 3)} %")
        pruefe_gleich(k, f"zwei Saetze, {name}: Rendite > Vergleichsrendite genau wenn Differenz > 0",
                      (kz["rendite"] > kz["vergleichsrendite"]) == (kz["endwertdifferenz"] > 0), True)
    plan, alt, kz = s1(a_lang="0.03")
    pruefe(k, "zwei Saetze, eine Einlage: Endwert der Alternative", alt.endwert, "443192.58")
    pruefe_proz(k, "zwei Saetze, eine Einlage: Vergleichsrendite", kz["vergleichsrendite"], "2.072")
    pruefe(k, "zwei Saetze, eine Einlage: Endwertdifferenz", kz["endwertdifferenz"], "141173.70")
    plan, alt, kz = s1(a_lang="0.03", entnahmen={t: 5000 for t in range(1, 6)})
    pruefe_proz(k, "zwei Saetze, Entnahmen aus dem Wiederanlagekonto: Rendite unveraendert", kz["rendite"], "7.876")
    pruefe(k, "zwei Saetze, Entnahmen: Endwertdifferenz unveraendert", kz["endwertdifferenz"], "141173.70")
    basis_diff = kz["endwertdifferenz"]
    plan, alt, kz = s1(a_lang="0.03", entnahmen={4: 40000})
    info(f"Entnahme 40.000 in t4 uebersteigt das Wiederanlagekonto der Alternative ({de(alt.zeilen[3]['kurz'])} in t3): "
         f"Endwertdifferenz {de(kz['endwertdifferenz'])}, Rendite {de(kz['rendite'] * 100, 3)} %")
    pruefe_fest(k, "zwei Saetze, Entnahme groesser als das Wiederanlagekonto: Endwertdifferenz", kz["endwertdifferenz"])
    pruefe_gleich(k, "... die Endwertdifferenz steigt, weil die Alternative langfristige Anlage aufloest",
                  kz["endwertdifferenz"] > basis_diff, True)
    # verlustbringender Fall: Rendite unter Vergleichsrendite
    plan, alt, kz = s1(verkauf=950000, einlagen={2: 50000})
    pruefe_gleich(k, "Verkauf 950.000 mit Nachschuss: Differenz negativ und Rendite unter Vergleichsrendite",
                  kz["endwertdifferenz"] < 0 and kz["rendite"] < kz["vergleichsrendite"], True)
    info(f"Verkauf 950.000: Endwertdifferenz {de(kz['endwertdifferenz'])}, Rendite {de(kz['rendite'] * 100, 3)} %, "
         f"Vergleichsrendite {de(kz['vergleichsrendite'] * 100, 3)} %")
    # Endwertueberschuss ueber die Zielrendite (R-10.9), Zielrendite 5 % als Annahme
    ziel = D("0.05")
    plan, alt, kz = s1()
    eu0 = endwertueberschuss(kz["zaehler"], kz["nenner"], ziel, 5)
    pruefe(k, "Endwertueberschuss Testfall bei Zielrendite 5 % (Annahme)", eu0, "73853.66")
    plan, alt, kz = s1(einlagen={2: 50000}, entnahmen={3: 50000})
    eu1 = endwertueberschuss(kz["zaehler"], kz["nenner"], ziel, 5)
    pruefe(k, "Endwertueberschuss, Nachschuss t2 und Entnahme t3", eu1, "63919.08")
    pruefe_gleich(k, "Vorzeichen von Endwertueberschuss und Abstand zur Zielrendite stimmen ueberein",
                  (eu1 > 0) == (kz["rendite"] > ziel), True)
    w = kz["w"]
    Z = kz["zaehler"]
    eu2 = Z - (400000 * (1 + ziel) ** 5 + 50000 * (1 + ziel) ** 3)
    eu3 = plan.endwert + 50000 * (1 + ziel) ** 2 - (400000 * (1 + ziel) ** 5 + 50000 * (1 + ziel) ** 3)
    info(f"andere Lesarten: Einlagen einzeln mit der Zielrendite aufgezinst {de(eu2)}; "
         f"Einlagen und Entnahmen mit der Zielrendite aufgezinst {de(eu3)}; Testfall ohne beide Zahlungen {de(eu0)}")
    pruefe(k, "andere Lesart: Einlagen einzeln mit der Zielrendite aufgezinst", eu2, "68101.94")
    pruefe(k, "andere Lesart: Einlagen und Entnahmen mit der Zielrendite aufgezinst", eu3, "71817.14")
    # andere Lesart "Rueckfuehrungen gegen fruehere Einlagen verrechnen": Nenner = Barwert der Netto-Eigenkapitalreihe
    # (Werte der Gegenrechnung des Finanzmathematikers, Pruefrunde 3, Befund 1)
    q = D("1.014")
    netto = wurzel_rendite(plan.endwert / (400000 + 50000 / q ** 2 - 50000 / q ** 3), 5)
    pruefe_proz(k, "andere Lesart Barwert der Nettoreihe: Nachschuss t2, Entnahme t3", netto, "7.866")
    p5, _, _ = s1(entnahmen={t: 5000 for t in range(1, 6)})
    netto5 = wurzel_rendite(p5.endwert / (400000 - sum(5000 / q ** t for t in range(1, 6))), 5)
    pruefe_proz(k, "andere Lesart Barwert der Nettoreihe: Entnahmen 5.000 je Jahr (Rendite steigt)", netto5, "8.240")
    # Randfall des Zaehlers (R-10.7): Endwert -10.000, aufgezinste Entnahmen 50.000, Eigenkapital 400.000
    r, Zx, Dx, status = vofi_rendite(D(-10000), [D(400000), 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, D(50000)], [EINS] * 6, 5)
    pruefe_proz(k, "Zaehler 40.000 bei Eigenkapital 400.000 ueber fuenf Jahre", r, "-36.9", 1)
    # Monatsraster: Entnahme aus dem Guthaben aendert die Rendite nur in der fuenften Nachkommastelle
    plan, alt, kz = s1_monat(D("0.02"), D("0.08"), "cent")
    e = plan.e
    e.entnahmen = [NULL] * 61
    e.entnahmen[30] = D(10000)
    e.tranchen = [Tranche("Bankdarlehen", 700000, "annuitaet_prozent", "0.04", tilgungssatz="0.02")]
    plan2 = rechne_plan(e)
    alt2 = rechne_alternative(e, plan2.einlagen_netto, plan2.entnahmen_netto)
    kz2 = werte_aus(plan2, alt2)
    info(f"Monatsraster, Entnahme 10.000 in Monat 30: Rendite {de(kz2['rendite'] * 100, 4)} % statt "
         f"{de(kz['rendite'] * 100, 4)} %; Endwertdifferenz {de(kz2['endwertdifferenz'])} statt {de(kz['endwertdifferenz'])}")
    pruefe(k, "Monatsraster, Entnahme aus dem Guthaben: Aenderung der Rendite (Prozentpunkte)",
           (kz2["rendite"] - kz["rendite"]) * 100, "0", "0.001", 4)
    pruefe(k, "Monatsraster, Entnahme aus dem Guthaben: Aenderung der Endwertdifferenz",
           kz2["endwertdifferenz"] - kz["endwertdifferenz"], "0", "1.00")
    # Monatsverschiebung: Nachschuss und Entnahme im selben Monat gegen einen Monat Abstand (R-10.6)
    werte = []
    for monat_entnahme in (13, 14, 24):
        e.einlagen = [D(400000)] + [NULL] * 60
        e.einlagen[13] = D(50000)
        e.entnahmen = [NULL] * 61
        e.entnahmen[monat_entnahme] = D(50000)
        e.tranchen = [Tranche("Bankdarlehen", 700000, "annuitaet_prozent", "0.04", tilgungssatz="0.02")]
        px = rechne_plan(e)
        ax = rechne_alternative(e, px.einlagen_netto, px.entnahmen_netto)
        kx = werte_aus(px, ax)
        werte.append((kx["rendite"], kx["endwertdifferenz"]))
    pruefe(k, "Monatsraster: Nachschuss und Entnahme im selben Monat aendern die Rendite nicht (Prozentpunkte)",
           (werte[0][0] - kz["rendite"]) * 100, "0", "0.0000001", 7)
    pruefe_fest(k, "Monatsraster: Rendite, Entnahme einen Monat nach dem Nachschuss (%)", werte[1][0] * 100, 3)
    pruefe_fest(k, "Monatsraster: Rendite, Entnahme elf Monate nach dem Nachschuss (%)", werte[2][0] * 100, 3)
    pruefe(k, "Monatsraster: Endwertdifferenz bleibt bei Verschiebung um einen Monat (Euro)",
           werte[1][1] - werte[0][1], "0", "0.50")
    info(f"Monatsverschiebung: Rendite {de(werte[0][0] * 100, 3)} % (selber Monat), {de(werte[1][0] * 100, 3)} % (ein Monat spaeter), "
         f"{de(werte[2][0] * 100, 3)} % (elf Monate spaeter); Endwertdifferenz {de(werte[0][1])} / {de(werte[1][1])} / {de(werte[2][1])}")


def alle():
    rf05_testfall()
    rf06_varianten()
    rf07_einlagen_entnahmen()
