import sys, traceback; sys.path.insert(0,"rr")
from decimal import Decimal as D
from dataclasses import replace
import annahmen as A
from grobkalkulation import rechne_grob, tragbarer_preis, Meldung
from finanzplan import rechne_plan
from grobkalkulation import _kopie
from proben import pruefe_plan, pruefe_mittel
from zahlen import de, proz
NULL=D(0); ANK=replace(A.ANKAUF, stau_betrag=NULL); VG=A.VORGABEN
arg=sys.argv[1]
if arg=="19b":
    ue=dict(restschuld=D(2000000), zins=D("0.06"), tilgungssatz=D("0.02"), bindung_jahre=20, anschluss_zins=D("0.07"))
    e=replace(ANK, uebernommen=ue, verkaufsfaktor=D(4))
    try:
        t=tragbarer_preis(e, VG)
        print("Ergebnis", t["preis"], t["meldung"], t["suche"]["status"], [str(l["wert"]) for l in t["suche"]["loesungen"]])
    except Exception as x:
        print("ABSTURZ", type(x).__name__, x)
    for P in (1818181, 1818182, 1900000, 2400000):
        try:
            g=rechne_grob(e, VG, preis=D(P), mit_blatt=False)
            print(P, "EW", de(g.plan.endwert), "r", proz(g.kennzahlen["rendite"]), g.kennzahlen["rendite_status"], "EK", de(g.eigenkapital_investitionsphase))
        except Meldung as m: print(P, m.kennung)
if arg=="44":
    e=replace(ANK, enk_satz=NULL, ist_miete=D("20"), markt_miete=D("20"), verkaufsfaktor=D(5))
    vg=replace(VG, beleihungsquote=D(1), mindestdeckung=D(1))
    for P in (1000000, 3000000, 3826767, 3826768, 4500000):
        g=rechne_grob(e, vg, preis=D(P), mit_blatt=False)
        k=g.kennzahlen
        print(P, "L", de(g.darlehen), "EK0", de(g.eigenkapital_investitionsphase), "Nachschuss", de(g.nachschuss_spaeter), "EW", de(g.plan.endwert), "D", de(k["nenner"]), "r", proz(k["rendite"]))
if arg=="leer":
    for q in ("0.02","0.3","0.5","1"):
        g=rechne_grob(ANK, replace(VG, mietausfall=D(q)), mit_blatt=False)
        # Gegenrechnung: Verkaufspreis auf die Mieteinzahlung des Folgejahres (nach Ausfall)
        vk=g.verkauf.preis_brutto; vk_ist=(vk*(1-D(q))).quantize(D("0.01"))
        print(q, "VK", de(vk), "VK auf Ist-Miete", de(vk_ist), "EW", de(g.plan.endwert), "dEW", de(g.kennzahlen["endwertdifferenz"]), "r", proz(g.kennzahlen["rendite"]))
if arg=="p04":
    g=rechne_grob(A.ANKAUF, VG)
    pe=g.plan.e
    einl=list(pe.einlagen); einl[0]+=D(100000)
    pe2=replace(pe, einlagen=einl, tranchen=_kopie(pe.tranchen))
    p=rechne_plan(pe2)
    ph=p.zeilen[:1]
    herkunft=dict(ek=sum(p.einlagen_netto[:1]), bank=sum(z["tranchen"]["Bankdarlehen"]["auszahlung"] for z in ph))
    verw=dict(inv=sum(z["investition"] for z in ph), erh=sum(z["erhaltung"] for z in ph),
              einb=sum(z["einbehalt"]+z["zuschuss_einbehalt"] for z in ph),
              fin=sum(z["zins"]+z["beitrag"]+z["kkzins"]-z["habenzins"] for z in ph),
              lauf=sum(z["kosten"]-z["miete"]+z["steuer"]+z["tilgung"] for z in ph),
              guth=ph[-1]["guthaben"]-ph[-1]["kk"])
    print("Einlage t0", de(p.einlagen_netto[0]), "statt", de(g.eigenkapital_investitionsphase), "| EK nach R-5.12", de(g.bemessung.bank["eigenkapital"]))
    print("P-01..P-11:", pruefe_plan(p), "| P-04:", pruefe_mittel(herkunft, verw), "| EW", de(p.endwert), "statt", de(g.plan.endwert))
if arg=="irr":
    from kennzahlen import interner_zinsfuss
    print(interner_zinsfuss([D(-400000)]+[D(0)]*11+[D(1)], p=12))
    print(interner_zinsfuss([D(-100)]+[D(1200)], p=1))
if arg=="leer2":
    for q,f in (("0.3","12.6"),("0.5","9"),("0.02","17.64")):
        g=rechne_grob(replace(ANK, verkaufsfaktor=D(f)), replace(VG, mietausfall=D(q)), mit_blatt=False)
        print(q, "Faktor", f, "VK", de(g.verkauf.preis_brutto), "dEW", de(g.kennzahlen["endwertdifferenz"]), "r", proz(g.kennzahlen["rendite"]))
