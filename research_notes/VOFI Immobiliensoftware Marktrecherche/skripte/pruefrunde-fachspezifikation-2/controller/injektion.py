"""Controller, Pruefrunde 2: Fehlerinjektion in die Rechenlogik (nicht in die Ausgabe) und Sperre an einzelnen
Stuetzstellen. Aufruf: python3 injektion.py <Pfad zum Referenzrechner>"""
import sys
sys.path.insert(0, sys.argv[1])
from decimal import Decimal as D
from dataclasses import replace
import grobkalkulation as g
import steuer as st
import finanzplan as fp
import darlehen as dl
import annahmen as A
from rf_grob import VG, KAT
from proben import pruefe_plan

NULL = D(0)


def proben(e):
    return sorted({b[0] for b in e.befunde}) if e.befunde else []


basis = g.rechne_grob(A.ANKAUF, VG, KAT)
print("Basis: gesperrt", basis.gesperrt, "Endwert", basis.plan.endwert, "Rendite", basis.kennzahlen["rendite"])
tp0 = g.tragbarer_preis(A.ANKAUF, VG, KAT)
print("Basis tragbarer Preis", tp0["preis"])

# --- 1. Sperre nur an einer Stuetzstelle der Preissuche (nahe P*), nur im Bisektionsbereich
def stoer_nahe(lokal):
    if lokal["bm"].preis is not None and 2317200 <= lokal["bm"].preis <= 2317240 and not lokal["stress"]:
        lokal["einl"][0] += D(1)
g.STOERUNG[0] = stoer_nahe
tp = g.tragbarer_preis(A.ANKAUF, VG, KAT)
print("1 Stoerung nur bei 2.317.200-2.317.240 (1 Euro Einlage): Preis", tp["preis"], "Meldung", tp["meldung"])
# nur im Stressfall
def stoer_stress(lokal):
    if lokal["stress"]:
        lokal["einl"][0] += D(1)
g.STOERUNG[0] = stoer_stress
e = g.rechne_grob(A.ANKAUF, VG, KAT)
es = g.rechne_grob(A.ANKAUF, VG, KAT, stress=True)
print("1b Stoerung nur im Stressfall: Basis gesperrt", e.gesperrt, "Stress gesperrt", es.gesperrt, proben(es))
tps = g.tragbarer_preis(A.ANKAUF, VG, KAT, stress=True)
print("   tragbarer Preis im Stress:", tps["preis"], tps["meldung"])
# Zielwertsuche: Stoerung nur bei Verkaufsfaktor 19,06 (kritischer Wert)
def stoer_faktor(lokal):
    if lokal["ein"].verkaufsfaktor == D("19.06"):
        lokal["einl"][0] += D(1)
g.STOERUNG[0] = stoer_faktor
try:
    s = g.suche_eingabe(A.ANKAUF, VG, KAT, "verkaufsfaktor", D(8), D(40), D("0.01"))
    print("1c Zielwertsuche mit Stoerung nur bei 19,06:", s["status"], [x["wert"] for x in s["loesungen"]])
except g.Meldung as m:
    print("1c Zielwertsuche mit Stoerung nur bei 19,06: Meldung", m.kennung)
g.STOERUNG[0] = None

# --- 2. Steuer: Verlustvortrag wird nie verbraucht (Programmfehler), Protokoll in sich stimmig
orig_nv = st.Steuer._nach_vortrag
def nv_ohne_verbrauch(self, ergebnis, topf, teile):
    vv = getattr(self, topf)
    zugang = max(-ergebnis, NULL)
    setattr(self, topf, vv + zugang)
    teile[topf + "_anfang"], teile[topf + "_zugang"], teile[topf + "_genutzt"] = vv, zugang, NULL
    return max(ergebnis, NULL)
st.Steuer._nach_vortrag = nv_ohne_verbrauch
e = g.rechne_grob(A.ANKAUF, VG, KAT)
print("2a Vortrag nie verbraucht: gesperrt", e.gesperrt, proben(e), "Endwert", e.plan.endwert,
      "Delta", e.plan.endwert - basis.plan.endwert)
# 2b: Vortrag als verbraucht protokolliert, aber nicht von der Bemessung abgezogen
def nv_nicht_abgezogen(self, ergebnis, topf, teile):
    orig_nv(self, ergebnis, topf, teile)
    return max(ergebnis, NULL)
st.Steuer._nach_vortrag = nv_nicht_abgezogen
e = g.rechne_grob(A.ANKAUF, VG, KAT)
print("2b Vortrag protokolliert, aber nicht abgezogen: gesperrt", e.gesperrt, proben(e), "Delta Endwert",
      e.plan.endwert - basis.plan.endwert)
st.Steuer._nach_vortrag = orig_nv
# 2c: Verlust geht doppelt in den Vortrag (Zugang doppelt gezaehlt, Protokoll Zugang einfach)
def nv_doppelt(self, ergebnis, topf, teile):
    r = orig_nv(self, ergebnis, topf, teile)
    setattr(self, topf, getattr(self, topf) + max(-ergebnis, NULL))
    return r
st.Steuer._nach_vortrag = nv_doppelt
e = g.rechne_grob(A.ANKAUF, VG, KAT)
print("2c Zugang doppelt im Bestand: gesperrt", e.gesperrt, proben(e))
st.Steuer._nach_vortrag = orig_nv
# 2d: Koerperschaftsteuer mit Satz des Vorjahres (Kalenderjahr um eins verschoben)
orig_kj = None
import zeit
orig_kj = zeit.Raster.kalenderjahr
zeit.Raster.kalenderjahr = lambda self, j: orig_kj(self, j) - 1
e = g.rechne_grob(A.ANKAUF, VG, KAT)
print("2d Steuersatz des falschen Kalenderjahres: gesperrt", e.gesperrt, proben(e), "Delta Endwert",
      e.plan.endwert - basis.plan.endwert)
zeit.Raster.kalenderjahr = orig_kj

# --- 3. Unterlassensalternative
orig_alt = fp.rechne_alternative
src_ok = True
def alt_falscher_satz(pe, einl, entn):
    pe2 = pe
    saved = pe.a_lang
    pe.a_lang = (pe.h_kurz if pe.a_lang is None else pe.a_lang) + D("0.005")   # langfristiger Satz 0,5 Pp. zu hoch
    try:
        return orig_alt(pe, einl, entn)
    finally:
        pe.a_lang = saved
g.rechne_alternative = alt_falscher_satz
e = g.rechne_grob(A.ANKAUF, VG, KAT)
print("3a Alternative mit falschem Anlagezins: gesperrt", e.gesperrt, proben(e), "EW_U", e.alt.endwert,
      "statt", basis.alt.endwert)
def alt_ohne_steuer(pe, einl, entn):
    a = orig_alt(pe, einl, entn)
    return a
# Steuer der Alternative mit falschem Status: Koerperschaft ohne Gewerbesteuer
def alt_falscher_status(pe, einl, entn):
    saved = pe.steuer
    pe.steuer = replace(saved, status=st.KOERPERSCHAFT_OHNE_GEWST)
    try:
        return orig_alt(pe, einl, entn)
    finally:
        pe.steuer = saved
g.rechne_alternative = alt_falscher_status
try:
    e = g.rechne_grob(A.ANKAUF, VG, KAT)
    print("3b Alternative ohne Gewerbesteuer besteuert: gesperrt", e.gesperrt, proben(e), "EW_U", e.alt.endwert,
          "statt", basis.alt.endwert)
except Exception as x:
    print("3b nicht ausfuehrbar:", type(x).__name__, x)
g.rechne_alternative = orig_alt

# --- 4. Zinsen
orig_zp = dl.Tranche.zins_der_periode
def zins_fortgeschrieben(self, u):            # heutiger Zins still fortgeschrieben (R-5.8 verboten)
    return self.zins
dl.Tranche.zins_der_periode = zins_fortgeschrieben
e = g.rechne_grob(A.ANKAUF, VG, KAT)
print("4a Anschlusszins nicht angewandt (Zins fortgeschrieben): gesperrt", e.gesperrt, proben(e))
dl.Tranche.zins_der_periode = orig_zp
# 4b: Tranche schon falsch aufgebaut: Anschlusszins ohne Aufschlag H-05
orig_init = dl.Tranche.__init__
def init_ohne_aufschlag(self, *a, **kw):
    orig_init(self, *a, **kw)
    if self.anschluss_zins is not None and self.name == "Bankdarlehen":
        self.anschluss_zins = self.zins
dl.Tranche.__init__ = init_ohne_aufschlag
e = g.rechne_grob(A.ANKAUF, VG, KAT)
print("4b Anschlusszins beim Aufbau der Tranche ohne Aufschlag: gesperrt", e.gesperrt, proben(e), "Delta Endwert",
      e.plan.endwert - basis.plan.endwert)
es = g.rechne_grob(A.ANKAUF, VG, KAT, stress=True)
es0 = None
dl.Tranche.__init__ = orig_init
es0 = g.rechne_grob(A.ANKAUF, VG, KAT, stress=True)
print("   im Stressfall: Delta Endwert", es.plan.endwert - es0.plan.endwert, "gesperrt", es.gesperrt)
# 4c: Habenzins mit nominalem statt konformem Satz
import zahlen
orig_pk = fp.periodensatz_konform if hasattr(fp, "periodensatz_konform") else None
if orig_pk:
    fp.periodensatz_konform = lambda x, p, rd: rd.satz(x / p)
    e = g.rechne_grob(A.ANKAUF, VG, KAT)
    print("4c Habenzins nominal/12 statt konform: gesperrt", e.gesperrt, proben(e))
    fp.periodensatz_konform = orig_pk
