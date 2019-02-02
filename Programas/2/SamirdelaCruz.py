
#Exercise 1.1

#Compute the number of seconds since the day you were born

segundos_nacimiento= (int(22*365.25)+ 30*2+ 31*5+ 1)*24*60*60
#print(segundos_nacimiento)

# Exercise 1.2

#Compute the value for the golden ratio number $(1+\sqrt{5})/2$
numero_aureo= (1+ math.sqrt(5))/2
#print(numero_aureo)

# Exercise 2.01

#* Define a list with the integers from 1 to 10 and use slicing print the second half of the list.

enteros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_lista=enteros[int(len(enteros))//2:]
print(new_lista)

# Exercise 2.02

#* Build a list with 100 repetitions of the sequence `1`, `-1` (i.e. `[1,-1,1,-1,1,-1,...]`)
lista_secuencia=[1, -1]
lista_completa=100*lista_secuencia
#print(lista_completa)

# Exercise 2.03

#* Build a list that contains a `1` surrounded by 15 zeroes on the left and the right.
ista_0= [0]
lista_1= [1]
lista_resultado= 15*lista_0+ lista_1+ 15*lista_0
#print(lista_resultado)

# Exercise 2.04

#* Compute the median of the following list

#`a = [21, 48, 79, 60, 77, 
#    15, 43, 90,  5,  49, 
#    15, 52, 20, 70, 55,  
#    4, 86, 49, 87, 59]`

a = [21, 48, 79, 60, 77, 15, 43, 90,  5,  49, 15, 52, 20, 70, 55,  4, 86, 49, 87, 59]
a_ordenada = sorted(a)
i= len(a_ordenada)//2
mediana= a_ordenada[i-1]+ a_ordenada[i]/2
#print(mediana)

# Exercise 3.01

#Create a dictionary with the integers `0` to `4` as keys and the vowels (a, e, i, o u) as values.

diccionario= {0: 'a', 1:'e', 2: 'i', 3: 'o', 4:'u'}
#print(diccionario)

# Exercise 3.02

#Use the following dictionary of dictionaries to create a new dictionary that has the same keys and the values correspond to the total number of hours used in all activities.

activities = {
    'Monday': {'study':4, 'sleep':8, 'party':0},
    'Tuesday': {'study':8, 'sleep':4, 'party':0},
    'Wednesday': {'study':8, 'sleep':4, 'party':0},
    'Thursday': {'study':4, 'sleep':4, 'party':4},
    'Friday': {'study':1, 'sleep':4, 'party':8},
}

total_dias= {}
for i in activities.keys():
    suma= 0
    for k in activities[i].values():
        suma+= k
    total_dias[i]= suma
#print(total_dias)

# Exercise 4.01
#Write a `for` cycle that prints the sequence: 5, 4, 3, 2, 1, 0.

for i in range(6):
    print(5-i)
    
# Exercise 4.02

#The following can be used to generate a random number between 0 and 1:

#```python
#import random
#a = random.random()
#```
#Use `random.random()` and a `for` cycle to compute the sum of 100 random numbers.

import random
suma=0
for a in range(100):
    suma+=random.random()
#print(suma)

# Exercise 4.03

#Use the results from the previous exercise to compute the standard deviation of 
#a list of `1000` numbers where each number is itself the sum of `N=100` random numbers. 
#What is the answer if `N=200`? `N=300`? 

lista_numeros_aleatoreos= []
N= 100 
total= 0
for i in range(1000):
    a=0
    for k in range(N):
        a+= random.random()
    total+= a
    print(a)
    lista_numeros_aleatoreos.append(a)
n= len(lista_numeros_aleatoreos)
promedio= total/n
suma= 0
for i in lista_numeros_aleatoreos:
    suma+= (i- promedio)**2

desviacion_estandar= math.sqrt(1/(n- 1)*suma)
#print(desviacion_estandar)
#Probando otros valores para N, como lo son 200 y 300 se observa que a medida que el numero N aumenta la desviasion estandar aumenta


#Segunda parte Ejercicio #2:

#Escriba el código necesario en python para leer el archivo definitivas.dat (el archivo se encuentra dentro del repositorio en ejercicios/2/) e imprimir por separado el promedio y la desviación estándar de las notas definitivas de Hombres (H) y de Mujeres (M). El archivo columnas_definitivas.txt tiene la descripción del significado de las columnas del archivo definitivas.dat.

f= open("definitivas.dat","r")
lineas= f.readlines()
for i in range(len(lineas)):
    lineas[i]=lineas[i].split()
#print(lineas)
notas_H= []
notas_M= []
total_H=0
total_M=0
for i in range(len(lineas)):
    a=float(lineas[i][-1])
    if lineas[i][0]=='H':
        notas_H.append(a)
        total_H+=a
    else:
        notas_M.append(a)
        total_M+=a
#print (notas_M,notas_H)

n_H= len(notas_H)
promedio_H= total_H/n_H
suma_H= 0
for i in notas_H:
    suma_H+= (i- promedio_H)**2
import math
desviacion_estandar_H= math.sqrt(1/(n_H- 1)*suma_H)
print(promedio_H,desviacion_estandar_H)

n_M= len(notas_M)
promedio_M= total_M/n_M
suma_M= 0
for i in notas_M:
    suma_M+= (i- promedio_M)**2
import math
desviacion_estandar_M= math.sqrt(1/(n_M- 1)*suma_M)
print(promedio_M, desviacion_estandar_M)