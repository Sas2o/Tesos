import matplotlib.pyplot as plt
import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#1

random.seed(None)

num_pasos=100
x,y=0,0

plt.figure()
plt.axis("equal")
for i in range(num_pasos):
    dx= (random.random() -0.5)*2
    dy= (random.random() -0.5)*2
    L=np.sqrt(dx**2+dy**2)
    dx,dy=dx/L,dy/L
    plt.plot([x,x+dx],[y,y+dy])
    x+= dx
    y+= dy
plt.savefig("Punto 1")

#Defs

def caminatas(n=100,mostrar_fig=False,d=2):
    K=int(np.sqrt(n))
    l=[]
    for i in range(K):
        l.append(cam(n=n,mostrar_fig=mostrar_fig,d=d))
        plt.savefig("Punto N"+ str(i))
    suma_R2=0
    for i in l:
        suma_R2+=l[0][1]
    espR2=suma_R2/K
    return [l,espR2]
        
def cam(n=1000,mostrar_fig=True,normalizar=True,d=2):
    random.seed(random.random()*10)
    
    Tt=[]
    Dt=[]
    Suma_dt=[]
    L2=0
    
    for j in range(d):
        Tt.append([0])
        Dt.append([])
        Dt[j].append((random.random() -0.5)*2)
        Suma_dt.append(Dt[j][0])
        L2+=Dt[j][0]**2
    
    for i in range(n):
        L=1
        if normalizar:
            L=np.sqrt(L2)
        L2=0
        for j in range(d):
            Dt[j][i]=Dt[j][i]/L
            Suma_dt[j]+=Dt[j][i]
            Tt[j].append(Tt[j][-1]+Dt[j][i])
            Dt[j].append((random.random() -0.5)*2)
            L2+=Dt[j][-1]**2
    
    R2=0
    for j in Suma_dt:
        R2+=j**2
    
        
    if mostrar_fig:
        if d==2:
            plt.figure()
            plt.axis("equal")
            plt.axis("off")
            plt.plot(Tt[0],Tt[1])
            
        elif d==3:
            fig = plt.figure()
            
            ax = plt.axes(projection='3d')
            ax.plot(Tt[0], Tt[1], Tt[2], '-b')
            ax.axis("equal")
            #ax.axis("off")
    
    return [Tt, R2]

#N=100
#l=caminatas(n=10,mostrar_fig=True,d=3)
#l2=cam(n=3,mostrar_fig=True,normalizar=False,d=2)
#'No muestran ninguna correracion entre los pasos, justo como se esperaria de una caminata aleatorea'

#2
for i in range(10):
    cam()
    plt.savefig("Punto 2"+ str(i))
print('No se nota ninguna correlacion, justo como se esperaria de una caminata aleatorea')

#3
walks=caminatas(n=200,mostrar_fig=True)
plt.savefig("Punto 3"+ str(i))

#4
print(walks[1])

#5
for i in range(3):
    cam(n=20,d=3)
    plt.savefig("Punto 5"+ str(i))
caminatas(n=20,mostrar_fig=True,d=3)[1]
plt.savefig("Punto 52")
print('No se nota ninguna correlacion, justo como se esperaria de una caminata aleatorea')

#6
walk=walks[0][0][0]
DTt=[]
for i in walk:
    DTt.append([])
    for j in range(len(i)-1):
        DTt[-1].append(i[j+1]-i[j])
suma1=0
suma2=0
for j in range(len(DTt[0])):
    for i in range(len(DTt[1])):
        if i!=j:
            suma1+=DTt[0][i]*DTt[1][j]
            suma2+=DTt[0][j]*DTt[1][i]
suma1/=len(DTt[0])
suma2/=len(DTt[1])
r1=suma1/walks[0][0][1]
r2=suma2/walks[0][0][1]
print(r1,r2)

#7
x,y=[],[]
for i in range(1,2000,10):
    y.append(caminatas(n=i)[1])
    x.append(np.sqrt(i))
plt.figure()
plt.plot(x,y)
plt.savefig("Punto 7")