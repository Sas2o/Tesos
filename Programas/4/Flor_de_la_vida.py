import numpy as np
import matplotlib.pyplot as plt

def circulo(r=1,N=100):
    tetha=np.linspace(0,2*np.pi,N)
    x=r*np.cos(tetha)
    y=r*np.sin(tetha)
    return [x,y]

def dib_fig1(r=1,n=100):
    pi6=np.pi/6
    t=np.linspace(-pi6,pi6,n)
    x1,y1=r*(np.cos(t)-np.cos(pi6)),r*np.sin(t) # parte derecha de un petalo
    x2,y2=-x1,-y1 # parte izquierda del petalo
    x,y=np.concatenate([x1,x2]),np.concatenate([y1,y2])
    return [x,y]

def rotar(ls,theta):
    x,y=(ls[0]*np.cos(theta)+ls[1]*np.sin(theta)),(ls[1]*np.cos(theta)-ls[0]*np.sin(theta))
    return [x,y]

def desplazar(ls,pos):
    x,y=ls[0]+pos[0],ls[1]+pos[1]
    return [x,y]

def dib_flor(z=3,rc=1,):  
    plt.figure(figsize=(10,10))
    plt.title('Flor de la vida')
    plt.axis("off")
    plt.axis("equal")
    r=[z,z+0.2]
    for p in r:
        d1=circulo(r=p*rc)
        plt.plot(d1[0],d1[1],color="k",lw=p/2)
    d=dib_fig1(r=rc)
    pi3=np.pi/3
    a=rc*np.cos(pi3/2)
    for i in range(3):
        ag=i*pi3
        for o in range(z*2+1):
            j=o-z
            for k in range(z*2-abs(j)):
                x,y=a*j,rc*(k-z+1/2+1/2*abs(j))
                df=desplazar(d,[x,y])
                dfg=rotar(df,ag)
                plt.plot(dfg[0],dfg[1],color="k",lw=1.1)

dib_flor(z=3,rc=5)
plt.savefig("Flor de la vida.png")
