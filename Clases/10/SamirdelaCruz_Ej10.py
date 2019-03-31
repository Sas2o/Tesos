import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sum(x)**2

limites=np.zeros((10,2))
limites[:,1]=1
l=np.prod(limites[:,1]-limites[:,0])

def integral(Num_trials=16,N=100):
    Ints=[]
    for i in range(Num_trials):
        fs=[]
        for j in range(N):
            x=np.random.rand(10)
            fs.append(f(x))
        promedio_f=np.mean(fs)
        Ints.append(promedio_f*l)
    promedio_trials=np.mean(Ints)
    return promedio_trials

#Sin for
def integral1(Num_trials=16,N=100):
    return np.mean(np.mean(np.sum(np.random.rand(10,N,Num_trials), axis=0)**2, axis=0))

#1
print(integral())
print(integral1())

#2
Ns=[]
errors=[]
errors1=[]
for p in range(14):
    N=2**p
    Int=integral(N=N)
    Int1=integral1(N=N)
    error=abs(Int-155/6)
    error1=abs(Int1-155/6)
    Ns.append(N)
    errors.append(error)
    errors1.append(error1)
    print("I=",Int,"o",Int1,"Para N=",N)

#Grafica
plt.figure(figsize=(10, 6))
plt.plot(1/np.sqrt(Ns),errors,label="dummies")
plt.plot(1/np.sqrt(Ns),errors1,c='r',label="Forero styles")
plt.legend()
plt.xlabel("$1/\sqrt{N}$")
plt.ylabel("Error")
#plt.axis("equal")
plt.title("Error $vs$ $1/\sqrt{N}$")
plt.savefig("Comparacion_de_distintos_N.png")

#Comentario
print("No se observa comportamiento lineal alguno")

def f(x):
    return np.sin(x)

n_intentos = 10
puntos = np.int_(np.logspace(1,5,n_intentos))
diferencias = np.ones(n_intentos)
for i in range(n_intentos):
    a = 1-np.cos(1)
    b = integral_monte_carlo(N=puntos[i])
    diferencias[i] =  (np.abs((a-b)/a))
plt.plot(puntos, diferencias)
plt.loglog()
plt.xlabel("$N_{puntos}$")
plt.ylabel("|Error|")
plt.savefig("a1.png")

def f(x):
    return np.sin(x)

def dens(x):
    return 2*x

def metropolis_2D(N=100000, sigma_delta=0.5):

    lista_x = [np.random.random()]

    for i in range(1,int(N)):
        propuesta_x  = np.random.random()

        r = min(1, dens(propuesta_x)/dens(lista_x[i-1]))
        alpha = np.random.random()
        if(alpha<r):
            lista_x.append(propuesta_x)
        else:
            lista_x.append(lista_x[i-1])
    return np.array(lista_x)

def integral_analitica():
    return 0.5

def integral_monte_carlo(N=100):
    x =  metropolis_2D(N=N)*(np.pi/2) # esto ya no es una distribucion uniforme!
    return np.sum(f(x))/N

n_intentos = 100
#puntos = np.int_(np.logspace(1,5,n_intentos))
diferencias = np.ones(n_intentos) # aqui guardaremos la diferencia entre la sol. numerica y la analitica
for i in range(n_intentos):
    a = integral_analitica()
    b = integral_monte_carlo(N=puntos[i])
    diferencias[i] =  (np.abs((a-b)/a))
#puntos=np.sort(metropolis_2D(N=1000))
_ = plt.hist(metropolis_2D(N=100))
plt.savefig("b.png")
plt.figure()
plt.plot(diferencias)
plt.loglog()
plt.xlabel("$N_{puntos}$")
plt.ylabel("|Error|")
plt.savefig("a.png")