"""Stichprobe der Messungen aus docs/pruefung/2026-11-21-wesentlichkeit/durchsicht.md mit eigenem Nachbau."""
import ank, nb
from decimal import Decimal as D
def pst(mod, par, lo, hi, **kw):
    ok = lambda P: mod.rechne(par, P=P, **kw)["EU"] >= 0
    assert ok(lo) and not ok(hi), (lo, hi)
    while hi - lo > 1:
        m = (lo + hi) // 2
        lo, hi = (m, hi) if ok(m) else (lo, m)
    return lo
def an(name, base, var, st=None, lo=1500000, hi=3000000):
    p0 = pst(ank, base, lo, hi, stress=st); p1 = pst(ank, var, lo, hi, stress=st)
    r0 = ank.rechne(base, stress=st)["r"]; r1 = ank.rechne(var, stress=st)["r"]
    print(f"AN {name:42s} Preis {float((p1-p0)/D(p0))*100:+.2f} % ({p0} -> {p1})  Rendite {float(r1-r0)*100:+.3f} PP")
B = ank.BASIS
an("V-22 Stress Instandhaltung +10 % (8 -> 9 Groessen)", B, B, st=True)  # Basiswert
p8 = pst(ank, B, 1500000, 3000000, stress=True); p9 = pst(ank, B, 1500000, 3000000, stress="neun")
r8 = ank.rechne(B, stress=True)["r"]; r9 = ank.rechne(B, stress="neun")["r"]
print(f"   Stress ohne/mit Instandhaltung: {p8} / {p9}: {float((p8-p9)/D(p9))*100:+.2f} %, Rendite {float(r8-r9)*100:+.3f} PP")
an("H-16 Verkaufskosten 1,5 -> 2,5 %", B, dict(B, vk=D("0.025")))
an("H-17 Verwaltung 350 -> 420", B, dict(B, verw=D(420)))
an("H-08 Habenzins 2 -> 1 %", B, dict(B, h=D("0.01")))
E = dict(B, ez=D(12000), ez_st=D("0.02"))
an("E-63 Erbbauzins-Steigerung 2 -> 3 % (EZ 12.000)", E, dict(E, ez_st=D("0.03")), lo=1000000)
def nbm(name, var, lo=300000, hi=1100000, base=nb.BASIS):
    p0 = pst(nb, base, lo, hi); p1 = pst(nb, var, lo, hi)
    gk = nb.rechne(base, P=p0)["GK"]
    r0 = nb.rechne(base)["r"]; r1 = nb.rechne(var)["r"]
    print(f"NB {name:42s} Preis {float((p1-p0)/gk)*100:+.2f} % GK (Grundstueck {float((p1-p0)/D(p0))*100:+.2f} %; {p0} -> {p1}, GK {gk})  Rendite {float(r1-r0)*100:+.3f} PP")
nbm("H-16 Verkaufskosten 1,5 -> 2,5 %", dict(nb.BASIS, vk=D("0.025")))
nbm("H-08 Habenzins 2 -> 1 %", dict(nb.BASIS, h=D("0.01")))
nbm("H-17 Verwaltung 350 -> 420", dict(nb.BASIS, verw=D(420)))
