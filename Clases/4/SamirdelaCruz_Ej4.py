import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use('Agg')

# Solucion Primera Parte del Ejercicio 4

### Exercise 1.1

"""Create an bidimensional array of random numbers with shape (4,8).

First, set the last column to `-1` and then set the second row to `2`"""

#import numpy as np 

b=np.random.rand(4,8) 


b[:,-1]=-1
b[1,:]=2

#print (b)

### Exercise 1.2

"""Using `a=np.random.normal(size=1000)` generate an array of 1000 thousand random numbers generated from a normal (i.e. gaussian) distribution with mean zero and standard deviation of one.

Print the number of elements with values larger than `2.0`. Is this number close to what you expected from the properties of a gaussian distribution?"""

a=np.random.normal(size=1000)
print(a[a>2.0])

#Si, corresponde al numero de elementos que se esperaria para una distribucion gaussiana

### Exercise 1.3

"""Using `a=np.random.normal(size=1000)` generate an array of 1000 thousand random numbers generated from a normal (i.e. gaussian) distribution with mean zero and standard deviation of one.

Then using only `ufuncs` on `a` generate a new array `b` that is `-1` wherever `a` is negative and `1` wherever `a` is positive."""

a=np.random.normal(size=1000)

a[np.less(a,0)]=-1
a[np.greater(a,0)]=1

#print(a)

### Exercise 4.1

"""Make a plot of the Lissajous curve corresponding to $a=5$, $b=4$.
See https://en.wikipedia.org/wiki/Lissajous_curve"""

#import numpy as np
#import matplotlib.pyplot as plt

t=np.linspace(0,2*np.pi,1000)

plt.figure(figsize=(5,5))
plt.plot(np.cos(5*t+np.pi/2),np.sin(4*t))
plt.axis("equal")
plt.axis("off")
plt.show()

### Exercise 4.2

"""**The solution to this exercise must ufuncs only, i.e. `for`, `while`, `if` statements cannot be used.**

Write a function to generate `N` points homogeneously distributed over a circle of radius `1` centered
on the origin of the coordinate system. The function must take as a in input `N` and return two arrays
`x` and `y` with the cartesian coodinates of the points. Use the function and generate `1000` points to 
make a plot and confirm that indeed the points are homogeneously distributed.

Write a similar function to distribute `N` points over the surface of the 3D sphere of radius `1`.

Read the documentation https://pythonprogramming.net/matplotlib-3d-scatterplot-tutorial/ to see how to 
make a 3D plot."""

def circulo(N):
    tetha=np.linspace(0,2*np.pi,N)
    x=np.cos(tetha)
    y=np.sin(tetha)
    return x,y
x1,y1=circulo(1000)
plt.figure()
plt.plot(x1,y1,)
plt.axis("equal")
plt.axis("off")
plt.show()


# Solucion Segunda Parte del Ejercicio 4

plt.figure()
plt.axis("equal")
plt.axis("off")
x,y=circulo(1000)
plt.plot(x*3,y*3)
plt.plot(x,y)
tt=np.pi/3
for i in range(1,3):
    x1=i
    y1=0
    x2=(x1*np.cos(tt)+y1*np.sin(tt))
    y2=(y1*np.cos(tt)-x1*np.sin(tt))
    plt.plot(x-x1,y)
    plt.plot(x+x1,y)
    plt.plot(x+x2,y+y2)
    plt.plot(x-x2,y-y2)
    plt.plot(x-x2,y+y2)
    plt.plot(x+x2,y-y2)
plt.title("Flor de la vida") 
plt.savefig("F.png")
    