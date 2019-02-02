# Solucion Primera Parte del Ejercicio 3
#Exercise 1.1

"""Compute how many times, on average, do you have to throw a die (with only six faces) in order to reach reach a minimum of 100 points. In this game you start with 0 points, you throw the die and add the number you get to the total account. Use the results of random.random() to implement the die throw."""

import random

n=1000
n_veces=0

for j in range(n):
    suma=0
    cont=0
    while suma<100:
        a=int(random.random()*6)+1
        suma+=a
        cont+=1
    n_veces+=cont

promedio=n_veces/n

#print(promedio)

# Exercise 2.1

"""Define a function `distance` that takes as arguments two lists `a,b` and computes
the Euclidean distance between the two:

$$
\sqrt{\sum_{i=0}^{N-1} (a_i - b_i)^2}
$$

Check your function with these three values
```python
distance([0,0], [1,1])
1.4142135623730951
```

```python
distance([1,5], [2,2])
3.1622776601683795
```

```python
distance([0,1,2], [2,3,4])
3.4641016151377544
```"""

import math

def distance(a,b):
    suma=0
    for i in range(len(a)):
        suma+=(a[i]-b[i])**2
    return math.sqrt(suma)

print(distance([0,0], [1,1]))

print(distance([1,5], [2,2]))

print(distance([0,1,2], [2,3,4]))

### Exercise 3.1

"""Redefine the class `Circle` to include a new method called `perimeter` that returns the value of the circle's perimeter."""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius #all attributes must be preceded by "self."
    def perimeter(self):
        return math.pi * self.radius
    
### Exercise 3.2

"""Define the class `Vector3D` to represent vectors in 3D.
The class must have

* Three attributes: `x`, `y`, and `z`, to store the coordinates.

* A method called `dot` that computes the dot product

    $$\vec{v} \cdot \vec{w} = v_{x}w_{x} + v_{y}w_{y} + v_{z}w_{z}$$

  The method could then be used as follows
  
```python
v = Vector3D(2, 0, 1)
w = Vector3D(1, -1, 3)
```
    
```python
v.dot(w)
5
```"""

class Vector3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def dot(self,v):
        p=self.x*v.x+self.y*v.y+self.z*v.z
        return p

v = Vector3D(2, 0, 1)
w = Vector3D(1, -1, 3)

v.dot(w)

### Exercise 4.1

"""Import the module `random` and use the function `shuffle` to shuffle the contents of a list that has the integers from 0 to 9. Print the list before and after shuffling. Use `random.shuffle?` to read the documentation string for that function."""

import random

lista=[]

for i in range(10):
    lista.append(i)
    
print(lista)

random.shuffle(lista)

print(lista)

# Solucion Segunda Parte del Ejercicio 3

class Contador:
    def __init__(self,f):
        self.archivo=f
    def cuenta_lineas(self):
        a=open(self.archivo,"r")
        lineas=a.readlines()
        n=len(lineas)
        return n
    def cuenta_caracteres(self,c):
        a=open(self.archivo,"r")
        lineas=a.readlines()
        k=0
        for i in lineas:
            k+=i.count(c)
        return k
