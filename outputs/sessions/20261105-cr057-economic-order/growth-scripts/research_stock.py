import numpy as np
yrs=np.arange(1870,1930); i29=59; i13=43
def path(pts):
    ks=sorted(pts); return np.interp(yrs,ks,[pts[k] for k in ks])
def stock(s,g,d=0.15):
    K=s[0]/(g+d); out=[]
    for si in s:
        K=K*(1-d)/(1+g)+si; out.append(K)
    return np.array(out)
for label,pac in [("author 0.6/1.5/2.5/3.0",{1870:0.003,1880:0.006,1900:0.015,1913:0.025,1929:0.03}),
                  ("alt 0.6/1.2/1.8/2.0",{1870:0.003,1880:0.006,1900:0.012,1913:0.018,1929:0.02})]:
  for ulabel,uni in [("Union 0.1/0.2/0.3/0.5",{1870:0.0005,1880:0.001,1900:0.002,1913:0.003,1929:0.005}),
                     ("Union 0.05/0.1/0.15/0.25",{1870:0.0003,1880:0.0005,1900:0.001,1913:0.0015,1929:0.0025})]:
    Kp=stock(path(pac),0.06); Ku=stock(path(uni),0.04)
    # foreign (Europe) stock per unit of *Union-size* output, absorbed: world floor W = 0.5% intensity-equivalent stock
    W=stock(path({1870:0.002,1880:0.002,1900:0.003,1913:0.004,1929:0.005}),0.025)
    for absorb in (0, 1):
        # absorption a = own_stock/(own_stock+0.05) (absorptive capacity); 0 = no world floor
        if absorb:
            aP=Kp/(Kp+0.05); aU=Ku/(Ku+0.05)
            rP=Kp+0.25*Ku*0.3*0 + aP*W*1.0; rU=Ku+aU*W*1.0+0.25*Kp*0.3
        else:
            rP=Kp; rU=Ku+0.25*Kp*0.3
        r=rP/rU
        print(f"{label} | {ulabel} | world+absorb {absorb}: ratio1913 {r[i13]:.1f} 1929 {r[i29]:.1f} ; x1929 g=.08/.10/.12/.15:",[round(r[i29]**g,3) for g in (.08,.10,.12,.15)])
