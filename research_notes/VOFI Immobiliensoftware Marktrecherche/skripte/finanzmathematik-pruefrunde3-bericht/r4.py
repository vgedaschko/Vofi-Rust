import math, numpy as np
from statistics import NormalDist
N=NormalDist(); p=.05; k=math.sqrt(p*(1-p))/N.pdf(N.inv_cdf(p)); z=N.inv_cdf(.975)
print("k=%.4f k2=%.3f z=%.4f"%(k,k*k,z))
for s in (.02,.03,.05):
    nq=(z*k*s/.0005)**2; nm=(z*s/.0005)**2; nm196=(1.96*s/.0005)**2; nq196=(1.96*k*s/.0005)**2
    print("s=%.0f%%: Quantil %d (1,96: %d)  Mittel %d (1,96: %d)  HB@10k %.2f bp"%(s*100,math.ceil(nq),math.ceil(nq196),math.ceil(nm),math.ceil(nm196),1.96*k*s/100*1e4))
rng=np.random.default_rng(3)
# Nr. 31: Faktor = 1/y, y~N(4.5%,1.5%), 20 Starts je 10.000
m=[np.mean(1/np.random.default_rng(sd).normal(.045,.015,10000)) for sd in range(20)]
print("Nr31 Mittel des Faktors je Start: min %.1f max %.1f median %.1f; Anteil y<0: %.4f"%(min(m),max(m),np.median(m),N.cdf(-3)))
m2=[np.mean(1/np.random.default_rng(100+sd).normal(.045,.015,10000)) for sd in range(200)]
print("   200 Starts: 5%%-95%% der Startmittel %.1f .. %.1f, min %.1f max %.1f"%(np.percentile(m2,5),np.percentile(m2,95),min(m2),max(m2)))
# Nr. 32
T=10; R=200000; mu=.02; sd=.015
def lvl(g): return np.prod(1+g,axis=1)
g=rng.normal(mu,sd,(R,T)); a=lvl(g)
one=rng.normal(mu,sd,(R,1)).repeat(T,1); c=lvl(one)
def ar(phi, marginal):
    e_sd = sd*math.sqrt(1-phi**2) if marginal else sd
    x=np.zeros((R,T)); x[:,0]=rng.normal(0, sd if marginal else sd, R)
    for t in range(1,T): x[:,t]=phi*x[:,t-1]+rng.normal(0,e_sd,R)
    return lvl(mu+x)
b1=ar(.7,True); b2=ar(.7,False)
for n,v in (("unabh",a),("AR .7 stationaer 1,5",b1),("AR .7 Innovation 1,5, Start 1,5",b2),("eine Ziehung",c)):
    print("%-34s sd/mean %.2f%%  sd/1 %.2f%%"%(n,100*v.std()/v.mean(),100*v.std()))
