import numpy as np

def f(x):
    return np.exp(-x)-x

def error(x1,x2):
    return abs(x2-x1)/x1

def Central_D(f, x, h):
    return (f(x+h/2)-f(x-h/2))/h

def Extrapolated_D(f, x, h=1E-7):
    return (4*Central_D(f, x, h/2)-Central_D(f, x, h))/3.0

#Newton  raphson
def newton_raphson(f,x_0,N=20):
    x=[x_0]
    for n in range(N-1):
        x_n1=x[n]-f(x[n])/Extrapolated_D(f,x[n])
        x.append(x_n1)
    return x

print(newton_raphson(f,1,N=100))

def Bisection(f,xmin,xplus,imax=100):
    x=[]
    for it in range(imax):
        x0=(xmin+xplus)/2
        x.append(x0)
        if f(xplus)*f(x0)>0:
            xplus=x0
        else :
            xmin=x0
        #if abs(f(x0))<1e-12:
            #break
    return x

print(Bisection(f,0,2))

def secante(f,x0,x1,N=100):
    x=[]
    for i in range(N):
        x.append(x0)
        x2=x1-f(x1)*(x0-x1)/(f(x0)-f(x1))
        x0=x1
        x1=x2
    return x

print(secante(f,1,0.5))