from fractions import Fraction as F
from s1_gegenrechnung import *
rows = vofi(n, Z, reinertrag, afa, ek, K0, i, ANN, h, kkz, s)
def f(x, nd=2): return fmt(x, nd)
print("| t | Originäre Zahlung | davon Reinertrag (steuerpfl.) | Eigenkapital | Kreditaufnahme | Sollzins | Tilgung | Ablösung | Habenzins | AfA | steuerl. BMG | Steuer | Geldanlage (− Anlage) | Finanzierungssaldo | Guthaben | Kontokorrent | Restschuld | Bestandssaldo |")
print("|" + "---|" * 18)
for r in rows:
    t = r["t"]
    cells = [str(t), f(r["Z"]), f(reinertrag[t]), f(r["ek"]), f(r["aufn"]), f(-r["sollz"]), f(-r["tilg"]), f(-r["abl"]), f(r["habenz"]),
             f(r["afa"]), f(r["bmg"]), f(-r["steuer"]), f(-r["anlage"]), f(r["fin"]), f(r["guth"]), f(r["kk"]), f(r["rs"]), f(r["bestand"])]
    print("| " + " | ".join(cells) + " |")
print()
print("4 Nachkommastellen:")
for r in rows:
    t = r["t"]
    print(t, f(reinertrag[t],4), f(r["sollz"],4), f(r["tilg"],4), f(r["abl"],4), f(r["habenz"],4), f(r["bmg"],4), f(r["steuer"],4), f(r["anlage"],4), f(r["guth"],4), f(r["rs"],4), f(r["bestand"],4))
print("Zeilensummen-Probe:", [f(r["Z"]+r["ek"]+r["aufn"]-r["sollz"]-r["tilg"]-r["abl"]+r["habenz"]-r["steuer"]-r["anlage"]) for r in rows])
for r in rows[1:]:
    t=r["t"]; print("DSCR", t, f(reinertrag[t]/(r["sollz"]+r["tilg"]),4), "ICR", f(reinertrag[t]/r["sollz"],4), "LTV-Ersatz Restschuld/1.1Mio", f(r["rs"]/F(1100000),4))
