#!/usr/bin/env python3
"""Zusatzrechnungen des Pruefers: Monatsmodus S1, Bauzeitzinsen, Randfaelle, Monte-Carlo-Aussagen."""
import math
import numpy as np

# ------------------------------------------------------------ S1 im Monatsraster
def s1_monat(vorschuessig=False, steuer_monatlich=False):
    n_j = 5
    K = 700_000.0; i = 0.04; rate = 42_000 / 12
    h = 0.02; s = 0.30; afa = 17_600.0
    guth = 0.0; rs = K
    if vorschuessig:
        guth += 55_000 / 12           # Januarmiete faellt zum Zeitpunkt 0 an
    for j in range(1, n_j + 1):
        re_j = 55_000 * 1.02 ** (j - 1)
        bmg = -afa
        for m in range(1, 13):
            sollz = rs * i / 12
            habenz = guth * h / 12
            tilg = rate - sollz
            miete = re_j / 12
            if vorschuessig:
                # Miete des Folgemonats geht am Monatsende ein (= Beginn Folgemonat)
                last = (j == n_j and m == 12)
                nxt = 0.0 if last else (55_000 * 1.02 ** (j - 1 + (1 if m == 12 else 0))) / 12
                zufluss = nxt
            else:
                zufluss = miete
            bmg += miete - sollz + habenz
            guth += zufluss - rate + habenz
            rs -= tilg
            if steuer_monatlich:
                guth -= s * (miete - sollz + habenz - afa / 12)
        if not steuer_monatlich:
            guth -= s * bmg
    guth += 1_150_000 - rs
    return guth, rs

print("--- S1 im Monatsraster (ANNAHMEN Pruefer: Miete/12, Rate 3.500, Zins i/12, Habenzins h/12, Steuer am Jahresende) ---")
ew_j = 584_366.2816
for lab, kw in (("nachschuessig, Steuer jaehrlich", {}), ("Miete vorschuessig, Steuer jaehrlich", dict(vorschuessig=True)),
                ("nachschuessig, Steuer monatlich", dict(steuer_monatlich=True))):
    ew, rs = s1_monat(**kw)
    print(f"{lab}: EW = {ew:,.2f}  Abloesung = {rs:,.2f}  Differenz zum Jahresmodus = {ew - ew_j:,.2f}  r_EK = {((ew / 400000) ** 0.2 - 1) * 100:.4f} %")
q = 1 + 0.04 / 12
print("Restschuld Monat 60 geschlossen:", f"{700000 * q ** 60 - 3500 * (q ** 60 - 1) / (0.04 / 12):,.2f}", " (Jahresmodus 624.171,48)")
print("Habenzins effektiv bei monatlicher Gutschrift:", f"{((1 + 0.02 / 12) ** 12 - 1) * 100:.4f} %")
print("Opportunitaet 400.000, 5 J.: jaehrlich n.St.", f"{400000 * 1.014 ** 5:,.2f}",
      " monatlich h/12 mit jaehrlicher Steuer:", f"{400000 * (1 + ((1 + 0.02 / 12) ** 12 - 1) * 0.7) ** 5:,.2f}")

# ------------------------------------------------------------ Bauzeitzinsen
print("\n--- Bauzeitzinsen: 10 Mio. Kosten, 24 Monate, 5 % p.a., Zinsen kapitalisiert ---")
C = 10_000_000.0; T = 24; i = 0.05

def abfluss(form):
    if form == "linear":
        F = lambda x: x
    else:
        F = lambda x: 3 * x ** 2 - 2 * x ** 3
    return [C * (F(t / T) - F((t - 1) / T)) for t in range(1, T + 1)]

def bauzins(costs, ek_gesamt):
    """Equity first: erst EK bis ek_gesamt, danach Kredit; Zinsen werden kapitalisiert."""
    ek_rest = ek_gesamt; kredit = 0.0; zinsen = 0.0
    for c in costs:
        z = kredit * i / 12
        zinsen += z; kredit += z
        aus_ek = min(ek_rest, c); ek_rest -= aus_ek
        kredit += c - aus_ek
    return zinsen, kredit

for form in ("linear", "kubisch"):
    z, k = bauzins(abfluss(form), 0.0)
    print(f"{form}, 100 % Kredit: Bauzeitzinsen = {z:,.0f}  (Faustformel K*i*T*0,5 = {C * i * 2 * 0.5:,.0f})")
costs = abfluss("linear")
z1, k1 = bauzins(costs, 0.30 * C)
print(f"Equity first, EK = 30 % der Baukosten (ein Durchlauf): Zinsen = {z1:,.0f}, Kredit Ende = {k1:,.0f}, "
      f"LTC = {k1 / (C + z1) * 100:.2f} %  (Faustformel auf 7 Mio.: {7e6 * i * 2 * 0.5:,.0f})")
ek = 0.30 * C
for it in range(1, 30):
    z, k = bauzins(costs, ek)
    ek_neu = 0.30 * (C + z)
    if abs(ek_neu - ek) < 0.005:
        break
    ek = ek_neu
print(f"Fixpunkt EK = 30 % der Gesamtkosten inkl. Bauzeitzinsen: EK = {ek:,.2f}, Zinsen = {z:,.2f}, Kredit = {k:,.2f}, "
      f"LTC = {k / (C + z) * 100:.2f} %, Iterationen = {it}")

# logistische S-Kurve ohne Normierung
k_, t0 = 10.0, 0.5
F = lambda x: 1 / (1 + math.exp(-k_ * (x - t0)))
print(f"Logistische Kurve k=10, tau0=0,5 unnormiert: F(0) = {F(0):.4f}, F(1) = {F(1):.4f} -> verteilt nur {(F(1) - F(0)) * 100:.2f} % der Kosten")

# ------------------------------------------------------------ Annuitaet bei Zins 0
print("\n--- Annuitaetenformel bei i = 0 ---")
try:
    i0 = 0.0; N = 20; K0 = 700_000
    A = K0 * i0 * (1 + i0) ** N / ((1 + i0) ** N - 1)
except ZeroDivisionError as e:
    print("A = K0*i*q^N/(q^N-1) mit i=0 ->", repr(e), "; Grenzwert K0/N =", 700_000 / 20)
for ii in (1e-9, 1e-12, 1e-15):
    N = 20
    print(f"i = {ii:g}: A = {700_000 * ii * (1 + ii) ** N / ((1 + ii) ** N - 1):,.4f}")

# ------------------------------------------------------------ Monte-Carlo: Stichprobenumfang
print("\n--- Erforderliche Laeufe fuer Halbbreite 95-%-KI von E[r_EK] < 5 Basispunkte ---")
for sig in (0.01, 0.02, 0.03, 0.05):
    N = (1.96 * sig / 0.0005) ** 2
    print(f"sigma(r_EK) = {sig * 100:.0f} Pp.: N >= {N:,.0f};  Halbbreite bei N=1.000: {1.96 * sig / math.sqrt(1000) * 1e4:.1f} Bp, bei N=5.000: {1.96 * sig / math.sqrt(5000) * 1e4:.1f} Bp")
phi = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
z05 = -1.6448536
for N in (1000, 10000):
    se = math.sqrt(0.05 * 0.95 / N) / phi(z05)
    print(f"Standardfehler des 5-%-Quantils (normalverteilte Zielgroesse) bei N={N}: {se:.4f} sigma")

# ------------------------------------------------------------ Normalverteilte Exit-Rendite
print("\n--- Exit-Rendite normalverteilt: Verkaufsfaktor 1/y ---")
for mu, sig in ((0.045, 0.010), (0.045, 0.015)):
    p = 0.5 * math.erfc((mu - 0.005) / sig / math.sqrt(2))
    means = []; maxs = []; neg = 0
    for seed in range(20):
        rng = np.random.default_rng(seed)
        y = rng.normal(mu, sig, 10_000)
        f = 1 / y
        means.append(f.mean()); maxs.append(np.abs(f).max()); neg += (y <= 0).sum()
    print(f"mu={mu * 100:.1f} %, sigma={sig * 100:.1f} %: P(y<0,5 %) = {p:.5f}; Mittel des Faktors ueber 20 Seeds a 10.000: "
          f"min {min(means):.2f} / max {max(means):.2f} (deterministisch {1 / mu:.2f}); groesster |Faktor| {max(maxs):,.0f}; negative Renditen gesamt {neg}")
rng = np.random.default_rng(1)
a, m, b = 0.035, 0.045, 0.065
al = 1 + 4 * (m - a) / (b - a); be = 1 + 4 * (b - m) / (b - a)
y = a + (b - a) * rng.beta(al, be, 1_000_000)
print(f"PERT(3,5/4,5/6,5 %): E[y] = {y.mean() * 100:.4f} % (Formel {(a + 4 * m + b) / 6 * 100:.4f} %), E[1/y] = {(1 / y).mean():.3f}, 1/E[y] = {1 / y.mean():.3f}, 1/Modus = {1 / m:.3f}")
tri = rng.triangular(a, m, b, 1_000_000)
print(f"Dreieck: E = {tri.mean() * 100:.4f} % (Formel {(a + m + b) / 3 * 100:.4f} %); Std Dreieck {tri.std() * 100:.4f} %, Std PERT {y.std() * 100:.4f} %")

# ------------------------------------------------------------ Serielle Korrelation Mietwachstum
print("\n--- Mietniveau nach 10 Jahren, g ~ N(2 %, 1,5 %) ---")
rng = np.random.default_rng(7)
N = 200_000; Tn = 10; mu, sig = 0.02, 0.015
g_iid = rng.normal(mu, sig, (N, Tn))
g_one = np.repeat(rng.normal(mu, sig, (N, 1)), Tn, axis=1)
phi_ = 0.7
eps = rng.normal(0, sig * math.sqrt(1 - phi_ ** 2), (N, Tn))
g_ar = np.empty((N, Tn)); g_ar[:, 0] = rng.normal(mu, sig, N)
for t in range(1, Tn):
    g_ar[:, t] = mu + phi_ * (g_ar[:, t - 1] - mu) + eps[:, t]
for lab, g in (("unabhaengig je Jahr", g_iid), ("AR(1), phi=0,7", g_ar), ("eine Ziehung fuer alle Jahre", g_one)):
    lvl = np.prod(1 + g, axis=1)
    print(f"{lab}: Std des Niveaus {lvl.std() * 100:.2f} %, P5 {np.quantile(lvl, 0.05):.4f}, P95 {np.quantile(lvl, 0.95):.4f}, Std des Durchschnittswachstums {g.mean(axis=1).std() * 100:.3f} Pp.")

# ------------------------------------------------------------ Copula: Korrelationsmass
print("\n--- Gauss-Copula: latente Korrelation vs. Spearman vs. Pearson der Raender ---")
for rho in (0.5, 0.8, -0.5):
    print(f"latent rho = {rho}: Spearman = {6 / math.pi * math.asin(rho / 2):.4f}; fuer Spearman = {rho} noetig: rho = {2 * math.sin(math.pi * rho / 6):.4f}; "
          f"Pearson zweier Lognormal(sigma=1)-Raender = {(math.exp(rho) - 1) / (math.e - 1):.4f}")

# ------------------------------------------------------------ LHS: sigma/sqrt(N) gilt nicht
print("\n--- Latin Hypercube: tatsaechlicher Fehler des Mittelwerts vs. sigma/sqrt(N) ---")
def lhs(rng, n, d):
    u = (rng.random((n, d)) + np.arange(n)[:, None]) / n
    for j in range(d):
        u[:, j] = u[rng.permutation(n), j]
    return u
def ziel(u):  # glatte, ueberwiegend additive Zielgroesse aus 5 Inputs
    return 0.05 + 0.04 * (u[:, 0] - 0.5) + 0.03 * (u[:, 1] - 0.5) ** 2 + 0.02 * u[:, 2] * u[:, 3] - 0.03 * (u[:, 4] - 0.5)
n = 1000; d = 5
rng = np.random.default_rng(3)
m_iid = [ziel(rng.random((n, d))).mean() for _ in range(400)]
m_lhs = [ziel(lhs(rng, n, d)).mean() for _ in range(400)]
sig_naiv = ziel(rng.random((200_000, d))).std() / math.sqrt(n)
print(f"N=1.000: naive Formel sigma/sqrt(N) = {sig_naiv * 1e4:.3f} Bp; beobachtet einfache Zufallsstichprobe {np.std(m_iid) * 1e4:.3f} Bp; LHS {np.std(m_lhs) * 1e4:.3f} Bp")

# ------------------------------------------------------------ Summationsreihenfolge
x = np.random.default_rng(5).normal(0.07, 0.03, 100_000)
s1 = float(np.sum(x)); s2 = sum(float(v) for v in x); s3 = sum(float(v) for v in x[::-1])
print("\n--- Gleitkomma: Summe derselben 100.000 Werte in drei Reihenfolgen ---")
print(repr(s1 / 1e5), repr(s2 / 1e5), repr(s3 / 1e5), " identisch:", s1 == s2 == s3)
