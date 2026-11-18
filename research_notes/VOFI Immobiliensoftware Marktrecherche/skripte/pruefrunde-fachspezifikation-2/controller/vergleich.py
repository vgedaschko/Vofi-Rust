import sys; sys.path.insert(0, sys.argv[1])
from decimal import Decimal as D
from dataclasses import replace
import grobkalkulation as g, annahmen as A
from rf_grob import VG, KAT
a = g.rechne_grob(A.ANKAUF, VG, KAT)
st2 = replace(A.ANKAUF.steuer, kst_satz=lambda jahr: D("0.15"))      # Katalogstand ohne Senkung ab 2028
b = g.rechne_grob(replace(A.ANKAUF, steuer=st2), VG, KAT)
v = g.vergleiche(a, b)
print("abweichende Werte:", v["abweichende_werte"])
print("Endwertdifferenz A/B:", [z for z in v["zeilen"] if z[0] == "Endwertdifferenz"])
print("Zahl der Blattgroessen im Vergleich:", len(v["zeilen"]))
st3 = replace(A.ANKAUF.steuer, hebesatz=D("4.40"))
c = g.rechne_grob(replace(A.ANKAUF, steuer=st3), VG, KAT)
print("Hebesatz 440 %: als Herkunft gefuehrt:", g.vergleiche(a, c)["abweichende_werte"])
