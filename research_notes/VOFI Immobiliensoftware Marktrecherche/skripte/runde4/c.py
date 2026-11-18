from b import run
import numpy as np
for i in (0.04,0.05,0.06):
  for fak in (14.,18.):
    rs=[(round(l,2),round(run(2.3e6,ltv=l,i=i,fak=fak)[0],4)) for l in np.arange(0.3,1.0,0.05)]
    v=[r for _,r in rs]; d=np.sign(np.diff(v))
    print(i,fak,'Vorzeichenwechsel der Steigung:',int((np.diff(d)!=0).sum()), rs[::2])
