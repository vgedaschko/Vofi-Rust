"""Pruefrunde 3, Controller: Zeilen des Beispiels in R-3.2, die nicht als Sollwert festgeschrieben sind, nachgerechnet."""
import sys, io, contextlib
from dataclasses import replace
from decimal import Decimal as D
R = "/home/user/vofi-rust/research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner"
sys.path.insert(0, R)
with contextlib.redirect_stdout(io.StringIO()):
    from rf_grob import VG, KAT, A
    import grobkalkulation as g
basis = g.rechne_grob(A.ANKAUF, VG, KAT); pb = g.tragbarer_preis(A.ANKAUF, VG, KAT)["preis"]
z5 = replace(A.ANKAUF, zinsbindung_jahre=5)
e5 = g.rechne_grob(z5, VG, KAT); p5 = g.tragbarer_preis(z5, VG, KAT)["preis"]
k = lambda e: e.kennzahlen
print("Zinsbindung 5 statt 10: EWD", k(e5)["endwertdifferenz"] - k(basis)["endwertdifferenz"], "(Text -44.943,46); Preis", D(p5) - D(pb), "(Text -26.475);",
      "Abstand", (k(e5)["abstand_zielrendite"] - k(basis)["abstand_zielrendite"]) * 100, "PP (Text -0,16)")
m = replace(VG, mietsteigerung=D("0.025"))
em = g.rechne_grob(A.ANKAUF, m, KAT); pm = g.tragbarer_preis(A.ANKAUF, m, KAT)["preis"]
print("Mietsteigerung 2,5 %: EWD", k(em)["endwertdifferenz"] - k(basis)["endwertdifferenz"], "(Text +165.880,04); Preis", D(pm) - D(pb), "(Text +97.715); Abstand",
      (k(em)["abstand_zielrendite"] - k(basis)["abstand_zielrendite"]) * 100, "PP (Text +0,56)")
