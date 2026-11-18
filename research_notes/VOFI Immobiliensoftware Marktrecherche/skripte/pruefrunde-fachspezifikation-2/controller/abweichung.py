import sys; sys.path.insert(0, sys.argv[1])
from decimal import Decimal as D
from dataclasses import replace
import grobkalkulation as g, annahmen as A
from rf_grob import VG, KAT
b = g.rechne_grob(A.ANKAUF, VG, KAT)
print("Haus: Bankdarlehen", b.darlehen, "dEW", b.kennzahlen["endwertdifferenz"], "a_lang", VG.a_lang, "kalk_zins", VG.kalk_zins)
for feld, wert in (("kalk_zins", D("0.01")), ("a_lang", D("0.005"))):
    ein = replace(A.ANKAUF, abweichungen={feld: (wert, "")})
    try:
        e = g.rechne_grob(ein, VG, KAT)
        print(feld, wert, "ohne Begruendung gerechnet; Liste:", e.abweichungen, "Bankdarlehen", e.darlehen,
              "dEW", e.kennzahlen["endwertdifferenz"])
        tp = g.tragbarer_preis(ein, VG, KAT)
        print("   tragbarer Preis", tp["preis"], "statt 2317235")
    except g.Meldung as m:
        print(feld, wert, "Meldung", m.kennung, m.text)
for feld, wert in (("instandhaltung_staffel", [(0, D(9))]),):
    try:
        e = g.rechne_grob(replace(A.ANKAUF, abweichungen={feld: (wert, "Gutachten")}), VG, KAT)
        print(feld, "gerechnet", e.abweichungen)
    except g.Meldung as m:
        print(feld, "Meldung", m.kennung, m.text)
try:
    e = g.rechne_grob(replace(A.ANKAUF, abweichungen={"stress": (VG.stress, "")}), VG, KAT)
except g.Meldung as m:
    print("stress", "Meldung", m.kennung, m.text)
# Voreinstellungen H-23/H-24: Abweichung der Eingabe steht in der Liste?
e = g.rechne_grob(replace(A.ANKAUF, anpassungsdauer=1, zinsbindung_jahre=5), VG, KAT)
print("Anpassungsdauer 1 statt H-23 4 J., Zinsbindung 5 statt H-24 10 J.: Liste", e.abweichungen,
      "dEW", e.kennzahlen["endwertdifferenz"])
# Erwerbsnebenkosten unter KAT-01
e = g.rechne_grob(replace(A.ANKAUF, enk_satz=D("0.03")), VG, KAT)
print("E-11 3 % statt KAT-01 10 %: Liste", e.abweichungen, "Meldungen", [m["kennung"] for m in e.meldungen])
tp = g.tragbarer_preis(replace(A.ANKAUF, enk_satz=D("0.03")), VG, KAT); print("   tragbarer Preis", tp["preis"])
