"""Controller, Pruefrunde 2: drei eigene Stichproben allein aus dem Text der Fachspezifikation und Anhang A.
Importiert kein Modul des Referenzrechners."""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP, ROUND_FLOOR
getcontext().prec = 60
C = D("0.01")
def c(x): return D(x).quantize(C, ROUND_HALF_UP)
def r12(x): return D(x).quantize(D("1E-12"), ROUND_HALF_UP)

print("=== Stichprobe 1: RF-12 Neubau frei finanziert (R-11.2, R-11.3, R-5.12, R-5.18, R-5.10) ===")
BK0 = c(D(2600) * 2320 * (1 + D("0.05") + D("0.20")))
raten = {m: c(BK0 / 18 * r12(D("1.03") ** (D(m) / 12))) for m in range(1, 19)}
bk = sum(raten.values())
grund = D(1200000) + c(D(1200000) * D("0.08"))
M = grund + bk
print("BK0", BK0, "Rate 1/2/18", raten[1], raten[2], raten[18], "Baukosten", bk, "M", M)
# Bewirtschaftung: Verwaltung 350 x 30, Instandhaltung 9 Euro (Alter < 22), Betriebskosten 2 Euro; Kostenindex 2 %
def kosten_monat(planjahr):
    idx = D(1)
    for _ in range(planjahr - 1): idx = r12(idx * D("1.02"))
    return c((350 * 30 + 9 * 2000 + 2 * 2000) * idx / 12)
# Rohertrag erstes Jahr der Vollvermietung: Monate 22..33, 2000 m2 x 16,50
roh = 12 * c(D(2000) * D("16.50"))
bew = sum(kosten_monat((m - 1) // 12 + 1) for m in range(22, 34))
ausfall = roh - 12 * c(c(D(2000) * D("16.50")) * (1 - D("0.015") - D("0.005")))
abzug = max(bew + ausfall, c(D("0.15") * roh))
RE_n = roh - abzug
print("Rohertrag", roh, "Bewirtschaftung VJ", bew, "Ausfall", ausfall, "Abzug", abzug, "RE_n", RE_n)
B = ((RE_n / D("1.2")) / D("0.07")).quantize(C, ROUND_FLOOR)
while D("1.2") * 12 * c(B * D("0.07") / 12) > RE_n: B -= C
A = D("0.65") * M
L = min(A, B, M).quantize(C, ROUND_FLOOR)
EK = M - L
print("A", c(A), "B", B, "L", L, "EK Ausgleichsposten", EK)
# Mittelabruf: Eigenkapital zuerst, dann Bank; Bauzeitzinsen und Bereitstellungszins 0,25 %/Monat nach 6 freien Monaten
ek_rest = EK - grund
aus = {}
rest = D(0); ausgezahlt = D(0); zins_sum = D(0); bereit_sum = D(0); nachschuss = D(0)
for m in range(1, 19):
    zins = c(rest * D("0.04") / 12)
    bereit = c((L - ausgezahlt) * D("0.0025") * 12 / 12) if (m > 6 and ausgezahlt < L) else D(0)
    zins_sum += zins; bereit_sum += bereit
    bedarf = raten[m]
    aus_ek = min(ek_rest, bedarf); ek_rest -= aus_ek; bedarf -= aus_ek
    aus[m] = bedarf; rest += bedarf; ausgezahlt += bedarf
    nachschuss += zins + bereit
    if m in (9, 10):
        print(f"Monat {m}: Eigenkapital {aus_ek}, Bank {aus[m]}, Zins {zins}, Bereitstellungszins {bereit}")
print("Bauzeitzinsen", zins_sum, "Bereitstellungszinsen", bereit_sum, "zusammen", zins_sum + bereit_sum,
      "Eigenkapital der Investitionsphase", EK + nachschuss, "Restschuld Ende Bauzeit", rest)
rate = c(L * D("0.06") / 12)
print("Monat 19: Rate", rate, "Zins", c(rest * D("0.04") / 12), "Tilgung", rate - c(rest * D("0.04") / 12))

print("\n=== Stichprobe 2: RF-12 mit Grobfoerderung (R-11.14, R-5.11, R-5.12, R-11.15) ===")
zf = min(bk, D(5460) * 2000) + min(grund, D(400) * 2500)
FD = c(D("0.6") * zf); ZS = c(D("0.2") * zf); MEK = c(D("0.2") * zf)
ent = c(FD * D("0.01")) + c(ZS * D("0.0075"))
Mf = M + ent
print("zuwendungsfaehig", zf, "FD", FD, "Zuschuss", ZS, "Mindest-EK", MEK, "Entgelte", ent, "M", Mf)
rohf = 12 * c(D(2000) * D("8.20"))
ausf = rohf - 12 * c(c(D(2000) * D("8.20")) * D("0.98"))
REnf = rohf - max(bew + ausf, c(D("0.15") * rohf))
tilg = c(FD / 504)
kd = D(0); r = FD
for k in range(12):
    kd += tilg + c(r * D("0.005") / 12); r -= tilg
Bf = (REnf / D("1.2") - kd) / D("0.07")
Af = D("0.65") * M - FD
Cf = Mf - FD - ZS - MEK
print("Rohertrag", rohf, "RE_n", REnf, "KD Foerderdarlehen", kd, "A", c(Af), "B", c(Bf), "C", Cf)
print("Deckung uebrige Darlehen", (REnf / kd).quantize(D("0.0001")), "Reserve RE_n - 1,2 KD", c(REnf - D("1.2") * kd),
      "EK Ausgleichsposten", Mf - FD - ZS)
noetig = D("1.2") * (kd + 12 * c(Cf * D("0.07") / 12))
print("noetiger Reinertrag fuer die Restfinanzierung", noetig)

print("\n=== Stichprobe 3: RF-11 Ankauf, Mietpfad MA-037 vorsichtig und Bankensicht (R-6.3, R-10.20 bis R-10.22, R-11.7) ===")
idx = [None, D(1)]
for j in range(2, 15): idx.append(r12(idx[-1] * D("1.02")))
miete = {}; lauf = D("8.50"); letzte = 0; erh = []
for m in range(1, 145):
    j = (m - 1) // 12 + 1
    ziel = D("8.50") + (D("9.20") * idx[j] - D("8.50")) * min(D(1), D(j - 1) / 4)
    bezug = miete[m - 36] if m - 36 >= 1 else D("8.50") / D("1.15")   # MA-037 vorsichtig: kein Spielraum gegen Mieten vor dem Stichtag
    if m >= 13 and m - 1 >= letzte + 15:
        neu = min(ziel, bezug * D("1.15"))
        if neu > lauf:
            lauf, letzte = neu, m - 1; erh.append((m, neu.quantize(D("0.0001"))))
    miete[m] = lauf
print("Erhoehungen", erh)
L11 = D("1226609.99")
rate = c(L11 * D("0.06") / 12)
rest = L11; zins1 = D(0)
for u in range(1, 13):
    z = c(rest * D("0.04") / 12); zins1 += z; rest -= rate - z
kd1 = 12 * rate
re1 = D("103035.24")
print("Kapitaldienst Jahr 1", kd1, "Zins Jahr 1", zins1, "Zinsdeckung", (re1 / zins1).quantize(D("0.0001")),
      "Deckung", (re1 / kd1).quantize(D("0.0001")), "Reserve", re1 - D("1.2") * kd1)
P = D(2317235); EKp = P + c(P * D("0.1")) - L11
print("bei P* 2.317.235: Eigenkapital", EKp, "Faktor", (P / D("132620.40")).quantize(D("0.01")),
      "je m2", c(P / 1320), "Abstand zum Angebot", D(2600000) - P)
