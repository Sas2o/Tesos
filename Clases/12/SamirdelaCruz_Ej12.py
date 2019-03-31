import numpy as np
import matplotlib.pyplot as plt

def f1(E):
    return np.sqrt(10-E)*np.tan(np.sqrt(10-E))-np.sqrt(E)

xmin=0
xmax=10
E_B=np.linspace(xmin,xmax,1000)
eps=1e-15

plt.figure()
plt.plot(E_B[abs(np.tan(np.sqrt(10-E_B)))<20],f1(E_B[abs(np.tan(np.sqrt(10-E_B)))<20]))
E_0=E_B[abs(f1(E_B))<0.05]
plt.scatter(E_0,f1(E_0))
plt.savefig("grafica1.png")

def Bisection(f,xmin,xplus,imax=100):
    for it in range(imax):
        x=(xmin+xplus)/2
        if f(xplus)*f(x)>0:
            xplus=x
        else :
            xmin=x
        if abs(f(x))<1e-12:
            break
    return x

print(Bisection(f1,0,2))
print(Bisection(f1,8,10))

def f2(E):
    return np.sqrt(E)*(np.tan(np.sqrt(10-E))**(-1))-np.sqrt(10-E)

plt.figure()
E2_B=E_B[abs(np.tan(np.sqrt(10-E_B)))>0.1]
plt.plot(E2_B,f2(E2_B))
E2_0=E2_B[abs(f2(E2_B))<0.05]
plt.scatter(E2_0,f2(E2_0))
plt.savefig("grafica2.png")
print(Bisection(f2,8,9))

def NewtonR(f,x,dx,it=100):
    for i in range(it+1):
        F=f(x)
        if (abs(F)<=eps or x+dx/2>10 or x-dx/2<0):
            break
        df=(f(x+dx/2)-f(x-dx/2))/dx
        dx=-F/df
        x+=dx
    return x

print(NewtonR(f2,6,0.003))
