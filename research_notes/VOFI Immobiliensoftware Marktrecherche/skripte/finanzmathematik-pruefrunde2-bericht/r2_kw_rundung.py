from fractions import Fraction as F
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_DOWN, ROUND_HALF_EVEN, getcontext
from r1_modell import modell
getcontext().prec = 40
# Kapitalwert-Probe Nr. 24
for zins in (F(4,100),):
    EW = modell(h=zins, kk=zins, i=zins); qq = 1+zins*F(7,10)
    dEW = EW - 400000*qq**5
    kw = -1100000 + sum((F(55000)*F(102,100)**(t-1)*F(7,10) + F(3,10)*17600)/qq**t for t in range(1,6)) + F(1150000)/qq**5
    print("einheitlich 4%%: dEW/q^5 %.2f  KW %.2f  Diff %.6f" % (dEW/qq**5, kw, dEW/qq**5-kw))
EW = modell(); qq = 1+F(2,100)*F(7,10); dEW = EW-400000*qq**5
kw14 = -1100000 + sum((F(55000)*F(102,100)**(t-1)*F(7,10) + F(3,10)*17600)/qq**t for t in range(1,6)) + F(1150000)/qq**5
print("Testfall: dEW/q^5 %.2f KW(1,4%%) %.2f Diff %.2f" % (dEW/qq**5, kw14, kw14-dEW/qq**5))
# Rundung Nr. 10
def plan(mode):
    K = D(700000); m = D(4)/D(1200)
    for _ in range(120):
        z = K*m
        if mode: z = z.quantize(D("0.01"), mode)
        K -= D(3500) - z
    return K
for name, mode in (("voll", None), ("kaufm.", ROUND_HALF_UP), ("abgeschn.", ROUND_DOWN), ("Banker", ROUND_HALF_EVEN)):
    print("Restschuld %-9s %s" % (name, plan(mode)))
# Testfall unter den Rundungsregeln von Nr. 10
def rz(x):  # Zins auf Cent kaufmännisch
    return F(D(x.numerator)/D(x.denominator)).limit_denominator(10**12) if False else F(str((D(x.numerator)/D(x.denominator)).quantize(D("0.01"), ROUND_HALF_UP)))
def rst_cent(x): return rz(x)
def rst_euro(x):  # Steuer auf volle Euro abgerundet (Muster § 32a EStG / Abrundung)
    d = (D(x.numerator)/D(x.denominator)); return F(str(d.quantize(D("1"), ROUND_DOWN)))
base = modell()
r_a = modell(rnd={'zins': rz, 'steuer': lambda x: x})
r_b = modell(rnd={'zins': rz, 'steuer': rst_cent})
r_c = modell(rnd={'zins': rz, 'steuer': rst_euro})
print("Testfall EW ungerundet %.4f" % base)
print("  Zinsen auf Cent: %.2f (Diff %.4f)" % (r_a, r_a-base))
print("  + Steuer auf Cent: %.2f (Diff %.4f)" % (r_b, r_b-base))
print("  + Steuer auf volle Euro abgerundet: %.2f (Diff %.4f)" % (r_c, r_c-base))
