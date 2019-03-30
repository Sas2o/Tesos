import numpy as np
import matplotlib.pyplot as plt

"""Punto 1"""

#CENTRAL DIFFERENCE (ALGORITHM)
    #Tomado de Landau, R. H., Páez, M. J., & Bordeianu, C. C. (2018). A Survey of Computational Physics. A Survey of Computational Physics, 0. https://doi.org/10.2307/j.ctv7h0rx7
def Central_D(f, x, h):
    return (f(x+h/2)-f(x-h/2))/h

#EXTRAPOLATED DIFFERENCE (METHOD)
    #Tomado de Landau, R. H., Páez, M. J., & Bordeianu, C. C. (2018). A Survey of Computational Physics. A Survey of Computational Physics, 0. https://doi.org/10.2307/j.ctv7h0rx7
def Extrapolated_D(f, x, h=1E-7):
    return (4*Central_D(f, x, h/2)-Central_D(f, x, h))/3.0

#Newton  raphson
def newton_raphson(f,D,x_0,N=2,l=0):
    x=[x_0]
    for n in range(N):
        x_n1=x[n]-f(x[n])/D(f,x[n])
        x.append(x_n1)
    if l==1:
        return x
    else :
        return x[-1]
    
def equilibrio(m,q,l,g):
    #conversion
    m=m*1e-3 #kg
    q=q*1e-9 #C
    #Fuerza de Coulomb
    def Fc(q1,q2,r):
        return q1*q2/(4*2.7816251401340457e-11*r**2)
    
    #Tension, sale de la hacer la sumatoria de fuerzas en y =0
    def T(m,g,t):
        return m*g/np.cos(t)

    #Sumatoria de Fuerzas en x
    def sum_F(t):
        r=2*l*np.sin(t)
        return Fc(q,q,r)-T(m,g,t)*np.sin(t)
    r1=0.44 #primera raiz
    raiz=newton_raphson(sum_F,Extrapolated_D,r1,N=100)
    return raiz
    
"""
#prueba
    #datos m=15 , q=2800, l=1.20 , g=9.8
m=15 #g
q=2800 #nC
l=1.20 #m
g=9.8 #m/s^2

print(equilibrio(m,q,l,g))
"""



"""Punto 2"""

def matrix_polynomial(filename, poly_degree=2):
    N=poly_degree+1
    datos=np.loadtxt(filename,dtype=np.float64)
    x=datos[:,0]
    y=datos[:,1]
    
    #generar S
    S=np.zeros((len(x),N))
    for i in range(len(x)):
        for j in range(N):
            S[i][j]=x[i]**(j)
    
    S1=S.T.dot(S)
    y1=S.T.dot(y)
    return elim_gaussiana(S1,y1)

    #soluciona sistema de ecuaciones usando el metodo de eliminacion gaussiana
        #pre* la matriz S recibida debe ser invertible
def elim_gaussiana(A,x):
    for i in range(A.shape[1]):
        n=A[i,i]
        A[i]=A[i]/n
        x[i]=x[i]/n
        for j in range(A.shape[0]):
            if j!=i:
                p1=A[j,i]
                A[j]=A[j]-A[i]*p1
                x[j]=x[j]-x[i]*p1
    return x

"""
#Prueba
    #datos
datos=np.array([[1,2,1],[2,5,1],[3,10,1]])
np.savetxt("prueba.txt",datos)

def fit_polynomial(cs,x):
    y=[]
    for j in range(len(x)):
        suma =0
        for i in range(len(cs)):
            suma+=cs[i]*(x[j]**(i))
        y.append(suma)
    return y

x=np.linspace(0,4,20)

cs=matrix_polynomial("prueba.txt",poly_degree=2)
cs1=matrix_polynomial("prueba.txt",poly_degree=1)

y=fit_polynomial(cs,x)
y1=fit_polynomial(cs1,x)
datos=np.loadtxt("prueba.txt")

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.scatter(datos[:,0],datos[:,1],c="black")
plt.plot(x,y1)
plt.title("Ajuste polinomial de primer grado")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.ylim(0,16)

plt.subplot(1,2,2)
plt.scatter(datos[:,0],datos[:,1],c="black")
plt.plot(x,y,c='r')
plt.title("Ajuste polinomial de segundo grado")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.ylim(0,16)

plt.savefig("Punto 2.png")
"""



"""Punto 3"""

def F_polinominal(cs,x):
    suma=0
    for i in range(cs.shape[0]):
        suma+=cs[i]*x**i
    return suma

def MCMC_polynomial(filename,poly_degree=2,n_steps=50000):
    datos=np.loadtxt(filename,dtype=np.float64)
    x=datos[:,0]
    y=datos[:,1]
    s=datos[:,2]
    #Es mas facil usar el logaritmo
    def logSuma_error(cs):
        return -0.5 * np.sum(((y -  F_polinominal(cs,x))/s)**2)
    
    def logP_anterior(cs):
        p = -np.inf
        a=True
        for i in cs:
            if 10<i or i<-10:
                a=False
        if a: 
            p = 0.0
        return p
    
    N=poly_degree+1
    Cs = np.zeros((n_steps,N))
    Cs[0]=np.random.rand(N)
    ds = 0.2

    for i in range(n_steps-1):
        pro=[]
        for n in range(N):
            pro.append(Cs[i,n] + np.random.normal(loc=0.0, scale=ds))
        cs=np.array(pro)
        logpropuesta_A = logSuma_error(Cs[i]) + logP_anterior(Cs[i])
        logpropuesta_N = logSuma_error(cs) + logP_anterior(cs)
        r = min(1,np.exp((logpropuesta_N-logpropuesta_A)/5))
        r1 = np.random.random()
        if(r1<r):
            Cs[i+1]=cs
        else:
            Cs[i+1]=Cs[i]

    return Cs.sum(axis=0)/n_steps

"""
#Prueba
cs=MCMC_polynomial("prueba.txt",poly_degree=2,n_steps=50000)

x=np.linspace(0,4,20)
y=fit_polynomial(cs,x)
datos=np.loadtxt("prueba.txt")

plt.figure(figsize=(10,10))
plt.scatter(datos[:,0],datos[:,1],c="black")
plt.plot(x,y)
plt.title("MCMC")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.ylim(0,16)

plt.savefig("Punto 3")
"""