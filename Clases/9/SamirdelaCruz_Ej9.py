import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial as P

#Deifine el integrando
def f(t):
    return np.sin(t)

#Grafica
a=0
b=np.pi
t=np.linspace(a,b)
#plt.plot(t,y_t,c="r")


#Metodo del Trapecio
def trapInt(N, a, b):
    Int=0
    h=(b-a)/(N-1)
    for i in range(1,N):
        x_i=a+(i-1)*h
        x_i1=a+(i)*h
        Int+= (f(x_i)+f(x_i1))*h/2
        plt.plot([x_i,x_i1],[f(x_i),f(x_i1)])
    return Int
Int=trapInt(4, a, b)
print(Int)


#Metodo de Simpson
def SimpsInt(N, a, b):
    if N%2==0:
        N+=1
    Int=0
    h=(b-a)/(N-1)
    for i in range(1,N,2):
        x_1i=a+(i-1)*h
        x_i=a+(i)*h
        x_i1=a+(i+1)*h
        Int+= (f(x_1i)+4*f(x_i)+f(x_i1))*h/3
        cc,bb,aa=P.polynomial.polyfit([x_1i,x_i,x_i1], [f(x_1i),f(x_i),f(x_i1)], deg=2)
        t=np.linspace(x_1i,x_i1,int(100/N))
        plt.plot(t,aa*t**2+bb*t+cc)
    return Int
Int=SimpsInt(4, 0, np.pi)
print(Int)


#Clase
a=0
b=1
N=1000
def f(u,z):
    return (-np.log(u))**(z-1)
def gauss_legendre(N,z=1):
    x,w=np.polynomial.legendre.leggauss(N+1)
    Int=sum(f((b-a)*x/2+(b+a)/2,z)*w)
    return (b-a)*Int/2
print(gauss_legendre(N,z=6))