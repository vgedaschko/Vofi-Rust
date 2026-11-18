# Unabhaengiger Nachbau RF-11 (Grobkalkulation Ankauf, Koerperschaft, Monatsraster) aus dem Text
from decimal import Decimal as D, getcontext, ROUND_HALF_UP, ROUND_FLOOR, ROUND_DOWN
getcontext().prec = 60
def r(x): return x.quantize(D("0.01"), ROUND_HALF_UP)
def r12(x): return x.quantize(D("1e-12"), ROUND_HALF_UP)
def floorc(x): return x.quantize(D("0.01"), ROUND_DOWN)
def konf(x,p): return x if p==1 else r12((1+x)**(D(1)/D(p))-1)
def kst(y): return {2027:D("0.15"),2028:D("0.14"),2029:D("0.13"),2030:D("0.12"),2031:D("0.11")}.get(y, D("0.15") if y<2027 else D("0.10"))
SOLI=D("0.055"); MZ=D("0.035"); HS=D(4)

BASE=dict(P=D(2400000), enk=D("0.10"), boden=D("0.25"), WF=D(1320), E=20, ist=D("8.50"), markt=D("9.20"), d=4,
  ms=D("0.02"), ks=D("0.02"), bs=D("0.03"), kap=D("0.15"), ausfall=D("0.02"), verw=D(350), inst=D(14), bk=D(2),
  co2=D("0.60"), co2s=D("0.05"), stau=D(120000), staujahr=2, zins=D("0.04"), tilg=D("0.02"), bind=10, aufschlag=D("0.01"),
  beta=D("0.65"), mu=D("1.2"), h=D("0.02"), kk=D("0.08"), n=12, faktor=D(18), vk=D("0.015"), afa=D("0.02"), start=2027,
  stress=None, Lfix=None)

def index(s, j):
    x=D(1)
    for _ in range(j-1): x=r12(x*(1+s))
    return x

def mietpfad(c, n):
    m={}
    for j in range(1,n+2):
        mk=c["markt"]*index(c["ms"],j)
        pf = mk if c["d"]==0 else c["ist"]+(mk-c["ist"])*min(D(1),D(j-1)/D(c["d"]))
        basis = m[j-3] if j>3 else c["ist"]
        m[j]=min(pf, basis*(1+c["kap"]))
    return m

def rechne(c, p=12, verbose=False):
    n=c["n"]; N=p*n; P=c["P"]
    st=c["stress"] or {}
    ausfall=c["ausfall"]+st.get("ausfall",0); 
    c2=dict(c); c2["ms"]=c["ms"]-st.get("ms",0)
    miete=mietpfad(c2,n)
    inst=c["inst"]*(1+st.get("inst",0))
    def planjahr(u): return (u-1)//p+1
    def soll(u): return r(c["WF"]*miete[planjahr(u)]*12/p)
    def ein(u): return r(soll(u)*(1-ausfall))
    def bew(u, inst_=inst):
        j=planjahr(u); jb=(c["verw"]*c["E"]+inst_*c["WF"]+c["bk"]*c["WF"])*index(c["ks"],j)
        return r(jb/p)
    def co2(u): return r(c["co2"]*c["WF"]*index(c["co2s"],planjahr(u))/p)
    # Bemessung (Basisannahmen fuer das Darlehen, R-11.8)
    def re1(ausf, inst_):
        cc=dict(c); m=mietpfad(c,n)
        s=D(0)
        for u in range(1,p+1):
            so=r(c["WF"]*m[1]*12/p); s+= r(so*(1-ausf)) - bew(u,inst_) - co2(u)
        return s
    RE=re1(c["ausfall"], c["inst"])
    enk=r(P*c["enk"]); M=P+enk
    W=P
    A=c["beta"]*W
    Bc=(RE/c["mu"])/(c["zins"]+c["tilg"]); B=floorc(Bc)
    while c["mu"]*p*r(B*(c["zins"]+c["tilg"])/p) > RE: B-=D("0.01")
    Cc=M
    L=max(D(0), floorc(min(A,B,Cc)))
    if c["Lfix"] is not None: L=c["Lfix"]
    bind=min(A,B,Cc); grenze=[k for k,v in (("a",A),("b",B),("c",Cc)) if v==bind]
    EK=M-L
    # AfA
    bodenw=(P+enk)*c["boden"]; grund=(P+enk)-bodenw
    afa_j=r(grund*c["afa"])
    # Verkauf
    fak=c["faktor"]*(1-st.get("faktor",0))
    sollf=sum(soll(u) for u in range(N+1,N+p+1))
    vp=r(fak*sollf); vkst=r(vp*c["vk"]); erl=vp-vkst
    # Finanzplan
    hp=konf(c["h"],p); kp=konf(c["kk"],p)
    rate=r(L*(c["zins"]+c["tilg"])/p); RS=L; i=c["zins"]
    G=D(0); KK=D(0); einl={0:EK}; nach={}
    vv_k=D(0); vv_g=D(0); eop=D(0); zh=D(0); sum_afa=D(0)
    kd1=D(0); re_j={}; kd_j={}
    for u in range(1,N+1):
        j=planjahr(u); jahr=c["start"]+j-1
        if u==c["bind"]*p+1:
            i=c["zins"]+c["aufschlag"]+st.get("anschluss",0); rate=r(RS*(i+c["tilg"])/p)
        zi=r(RS*i/p); ti=min(RS,max(D(0),rate-zi)); RS-=ti
        orig=ein(u)-bew(u)-co2(u)
        re_j[j]=re_j.get(j,D(0))+orig; kd_j[j]=kd_j.get(j,D(0))+zi+ti
        erh=D(0)
        if c["staujahr"]>=1 and u==c["staujahr"]*p and c["staujahr"]<=n:
            erh=r(c["stau"]*(1+c["bs"])**c["staujahr"])
        abl=D(0); vk=D(0)
        if u==N: abl=RS; RS=D(0); vk=erl
        hz=r(G*hp); kz=r(KK*kp)
        eop+= orig-erh-zi-kz; zh+=hz
        tax=D(0)
        if u%p==0:
            a=min(afa_j, grund-sum_afa); sum_afa+=a
            gv = (erl-(bodenw+grund-sum_afa)) if u==N else D(0)
            e=eop-a+zh+gv
            # KSt
            if e<0: vv_k-=e; bk=D(0)
            else: nu=min(vv_k,e); vv_k-=nu; bk=e-nu
            ks=r(kst(jahr)*(1+SOLI)*bk)
            if e<0: vv_g-=e; bg=D(0)
            else: nu=min(vv_g,e); vv_g-=nu; bg=e-nu
            ge=(bg/100).to_integral_value(ROUND_FLOOR)*100
            gw=r(r(ge*MZ)*HS)
            tax=ks+gw
            if verbose: print(j, "e",e,"tax",tax,"G",G)
            eop=D(0); zh=D(0)
        sal=orig-erh+vk-zi-ti-abl+hz-kz-tax
        net=G-KK+sal
        if net>=0: G,KK=net,D(0)
        else:
            G=D(0); KK=D(0); nach[u]=-net   # Linie 0 -> Nachschuss
    EW=G-KK
    # UA (Koerperschaft): langfristig + Wiederanlage, gleiche Steuer, eigener VV
    ein_ser=dict(einl); 
    for u,v in nach.items(): ein_ser[u]=ein_ser.get(u,D(0))+v
    Lg=ein_ser[0]; Wa=D(0); KU=D(0); vk_=D(0); vg_=D(0); zs=D(0)
    for u in range(1,N+1):
        j=planjahr(u); jahr=c["start"]+j-1
        z=r(Lg*hp)+r(Wa*hp); zk=r(KU*kp); zs+=z-zk; tax=D(0)
        if u%p==0:
            e=zs
            if e<0: vk_-=e; bk=D(0)
            else: nu=min(vk_,e); vk_-=nu; bk=e-nu
            ks=r(kst(jahr)*(1+SOLI)*bk)
            if e<0: vg_-=e; bg=D(0)
            else: nu=min(vg_,e); vg_-=nu; bg=e-nu
            gw=r(r((bg/100).to_integral_value(ROUND_FLOOR)*100*MZ)*HS)
            tax=ks+gw; zs=D(0)
        e_=ein_ser.get(u,D(0)); back=min(KU,e_); KU-=back; Lg+=e_-back
        x=Wa-KU+z-zk-tax
        if x>=0: Wa,KU=x,D(0)
        else:
            need=-x; Wa=D(0); KU=D(0); tk=min(Lg,need); Lg-=tk; KU=need-tk
    EWU=Lg+Wa-KU
    # Vergleichsfaktor
    f={}
    for u in range(1,N+1):
        jahr=c["start"]+planjahr(u)-1; sz=kst(jahr)*(1+SOLI)+MZ*HS
        f[u]=r12((1+c["h"]*(1-sz))**(D(1)/D(p)))
    def w(t):
        x=D(1)
        for v in range(t+1,N+1): x*=f[v]
        return x
    Dn=sum(v*w(u) for u,v in ein_ser.items())/w(0)
    Z=EW
    rr=(Z/Dn)**(D(1)/D(n))-1 if Z>0 else D(-1)
    ZU=EWU; rU=(ZU/Dn)**(D(1)/D(n))-1
    return dict(RE=RE,A=A,B=B,C=Cc,L=L,grenze=grenze,EK=EK,nach=nach,EW=EW,EWU=EWU,dEW=EW-EWU,r=rr,rU=rU,
                w0=w(0),w24=w(24),vp=vp,abl=None,D=Dn,deck1=re_j[1]/kd_j[1], EUe=Z-Dn*D("1.05")**n, kd=kd_j, re=re_j)

if __name__=="__main__":
    x=rechne(BASE, verbose=True)
    for k in ("RE","A","B","C","L","grenze","EK","nach","EW","EWU","dEW","r","rU","w0","w24","vp","deck1","EUe"): print(k, x[k])
