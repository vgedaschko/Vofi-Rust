import math, random, statistics as st
from statistics import NormalDist
N01 = NormalDist()
for s in (0.02,0.03,0.05):
    n = (1.96*s/0.0005)**2; print("Mittelwert sigma %.0f%%: N=%.2f -> %d" % (s*100, n, math.ceil(n)))
print("1000 Laeufe sigma 3%%: Halbbreite %.2f bp, SE %.2f bp" % (1.96*0.03/math.sqrt(1000)*1e4, 0.03/math.sqrt(1000)*1e4))
p=0.05; zp=N01.inv_cdf(p); k=math.sqrt(p*(1-p))/N01.pdf(zp)
print("Quantil-Faktor k = sqrt(p(1-p))/phi(z_p) = %.4f (SE = k*sigma/sqrt(N)); Varianzverhaeltnis zum Mittelwert %.2f" % (k, k*k))
for s in (0.02,0.03,0.05):
    n = (1.96*k*s/0.0005)**2
    print("5%%-Quantil sigma %.0f%%: N fuer 5 bp Halbbreite = %d; Halbbreite bei 10.000 = %.1f bp" % (s*100, math.ceil(n), 1.96*k*s/100*1e4))
# Simulationsprobe
random.seed(7); s=0.03; reps=400; N=10000; qs=[]
for _ in range(reps):
    x=sorted(random.gauss(0,s) for _ in range(N)); qs.append(x[int(0.05*N)-1])
print("Simulation: SE 5%%-Quantil bei N=10.000, sigma 3%%: %.2f bp (Formel %.2f bp)" % (st.pstdev(qs)*1e4, k*s/100*1e4))
