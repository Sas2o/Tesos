import numpy as np
import matplotlib.pyplot as plt

#7.1

def f(x):
    y = 0.5 * np.sin(x)
    if(np.isscalar(x)):# esto va a funcionar si entra un numero
        if (x>np.pi) | (x<0):
            y = 0
    else: #esto va a funcionar si entra un array
        ii = (x>np.pi) | (x<0)
        y[ii] = 0.0
    return y


N = 100000
lista = [np.random.random()*np.pi]
sigma_delta = 0.001

for i in range(1,N):
    propuesta  = lista[i-1] + np.random.normal(loc=0.0, scale=sigma_delta)
    r = min(1,f(propuesta)/f(lista[i-1]))
    alpha = np.random.random()
    if(alpha<r):
        lista.append(propuesta)
    else:
        lista.append(lista[i-1])

plt.figure()
x = np.linspace(0, np.pi)
plt.plot(x, f(x))
_ = plt.hist(lista, density=True, bins=x)

lista = [np.random.random()*np.pi]
sigma_delta = 1000.0
plt.savefig("Delta_Sigma_0001.png")

for i in range(1,N):
    propuesta  = lista[i-1] + np.random.normal(loc=0.0, scale=sigma_delta)
    r = min(1,f(propuesta)/f(lista[i-1]))
    alpha = np.random.random()
    if(alpha<r):
        lista.append(propuesta)
    else:
        lista.append(lista[i-1])

plt.figure()
plt.plot(x, f(x))
_ = plt.hist(lista, density=True, bins=x)
plt.savefig("Delta_Sigma_1000.png")

#7.2

def dens(x, y):
    return np.exp(-0.5*(x**2 + (y/3)**2 -x*y/12))


# Genera lista de puntos
N = 100000
Xx = [np.random.random()*10-5]
Yy = [np.random.random()*10-5]
sigma_delta_x = 1.0
sigma_delta_y = 1.0

for i in range(N):
    x_i = Xx[i]
    y_i = Yy[i]
    x_i1  = x_i + np.random.normal(loc=0.0, scale=sigma_delta_x)
    y_i1  = y_i + np.random.normal(loc=0.0, scale=sigma_delta_y)
    r = min(1,dens(x_i1,y_i1)/dens(x_i,y_i))
    alpha = np.random.random()
    if(alpha<r):
        Xx.append(x_i1)
        Yy.append(y_i1)
    else:
        Xx.append(x_i)
        Yy.append(y_i)
        
# Genera puntos sobre una grid        
Xx_line = np.linspace(-5,5,100)
Yy_line = np.linspace(-5,5,100)
Xx_grid,Yy_grid=np.meshgrid(Xx_line,Yy_line)
Zz_grid=dens(Xx_grid,Yy_grid)

fig, (ax0, ax1) = plt.subplots(1,2)

# grafica los puntos de la grid
im = ax0.pcolormesh(Xx_grid, Yy_grid, Zz_grid)

# grafica el histograma bidimensional a partir de la lista de puntos
_ = plt.hist2d(Xx, Yy, bins=50)
plt.title("Distribucion de puntos segun la densidad")
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.savefig("Puntos_con_Densidad_de_Probabilidad.png")

x_obs = np.array([-2.0,1.3,0.4,5.0,0.1, -4.7, 3.0, -3.5,-1.1])
y_obs = np.array([ -1.931,   2.38,   1.88,  -24.22,   3.31, -21.9,  -5.18, -12.23,   0.822])
sigma_y_obs = ([ 2.63,  6.23, -1.461, 1.376, -4.72,  1.313, -4.886, -1.091,  0.8054])
#plt.errorbar(x_obs, y_obs, yerr=sigma_y_obs, fmt='o')

def model(x,a,b,c):
    return a*x**2 +b*x+ c

# Numericamente es mas estable trabajar con el logaritmo
def loglikelihood(x_obs, y_obs, sigma_y_obs, a, b ,c ):
    d = y_obs -  model(x_obs, a, b, c)
    d = d/sigma_y_obs
    d = -0.5 * np.sum(d**2)
    return d

# Numericamente es mas estable trabajar con el logaritmo
def logprior(a, b, c):
    p = -np.inf
    if a < 10 and a >-10 and b >-10 and b<10 and c >-10 and c<10:
        p = 0.0
    return p

N = 50000
lista_a = [np.random.random()]
lista_b = [np.random.random()]
lista_c = [np.random.random()]
logposterior = [loglikelihood(x_obs, y_obs, sigma_y_obs, lista_a[0], lista_b[0], lista_c[0]) + logprior(lista_a[0], lista_b[0], lista_c[0])]

sigma_delta_a = 0.2
sigma_delta_b = 0.2
sigma_delta_c = 0.2

for i in range(N):
    propuesta_a  = lista_a[i] + np.random.normal(loc=0.0, scale=sigma_delta_a)
    propuesta_b  = lista_b[i] + np.random.normal(loc=0.0, scale=sigma_delta_b)
    propuesta_c  = lista_c[i] + np.random.normal(loc=0.0, scale=sigma_delta_c)

    logposterior_viejo = loglikelihood(x_obs, y_obs, sigma_y_obs, lista_a[i], lista_b[i], lista_c[i]) + logprior(lista_a[i], lista_b[i], lista_c[i])
    logposterior_nuevo = loglikelihood(x_obs, y_obs, sigma_y_obs, propuesta_a, propuesta_b, propuesta_c) + logprior(propuesta_a, propuesta_b, propuesta_c)

    r = min(1,np.exp(logposterior_nuevo-logposterior_viejo))
    alpha = np.random.random()
    if(alpha<r):
        lista_a.append(propuesta_a)
        lista_b.append(propuesta_b)
        lista_c.append(propuesta_c)
        logposterior.append(logposterior_nuevo)
    else:
        lista_a.append(lista_a[i])
        lista_b.append(lista_b[i])
        lista_c.append(lista_c[i])
        logposterior.append(logposterior_viejo)
lista_a = np.array(lista_a)
lista_b = np.array(lista_b)
lista_c = np.array(lista_c)
logposterior = np.array(logposterior)

plt.figure(figsize=(10,10))
plt.title("Título") 
plt.subplot(2,2,2)
_=plt.hist(lista_a, bins=40, density=True)
plt.xlabel('a')
plt.ylabel('P(a|datos)')

plt.subplot(2,2,3)
_=plt.hist(lista_b, bins=40, density=True)
plt.xlabel('b')
plt.ylabel('P(b|datos)')

plt.subplot(2,2,4)
_=plt.hist(lista_c, bins=40, density=True)
plt.xlabel('c')
plt.ylabel('P(c|datos)')


plt.subplot(2,2,1)
x_model=np.linspace(min(x_obs),max(x_obs))
y_model = model(x_model,np.mean(lista_a),np.mean(lista_b),np.mean(lista_c))
plt.errorbar(x_obs,y_obs, yerr=sigma_y_obs, fmt='o')
plt.plot(x_model, y_model)
plt.savefig("Ajuste_polinominal.png")