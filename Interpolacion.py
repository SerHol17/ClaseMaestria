#Librerias

from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


#Interpolación Usando Numpy


def interNumpy(x,y,x0):
  return np.interp(x0, x, y)

print("Interpolación usando Numpy")
#Cargamos Vectores Fuerza
x=np.array([20, 40, 60, 80, 100, 120, 140, 160, 180]) #Angulos
xL2=np.array([0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181])
L3L2=np.array([3.963,3.925,3.850,3.738,3.588,3.438,3.250,3.025,2.800])
L1L2= np.array([2.975,2.950,2.9,2.825,2.725,2.625,2.500,2.350,2.200])

#Angulos a interpolar
a=30
b=55


data = {'Grados': [30,55],
        'L1': [interNumpy(x,L1L2,a)*(20/interNumpy(x,xL2,a)),interNumpy(x,L1L2,b)*(20/interNumpy(x,xL2,b))],
        'L2': [20/interNumpy(x,xL2,a),20/interNumpy(x,xL2,b)],
        'L3': [ interNumpy(x,L3L2,a)*(20/interNumpy(x,xL2,a)), interNumpy(x,L3L2,b)*(20/interNumpy(x,xL2,b))],
        'x/L2': [ interNumpy(x,xL2,a), interNumpy(x,xL2,b)],
        'L1/L2': [interNumpy(x,L1L2,a), interNumpy(x,L3L2,b)],
        'L3/L2': [ interNumpy(x,L3L2,a), interNumpy(x,L1L2,b)]}
df = pd.DataFrame(data)
print("Fuerza")
print(df)

#Cargamos Vectores velocidad

xL2=np.array([0.480, 0.950, 1.411, 1.845, 2.237, 2.600, 2.932,3.232,3.456])
L3L2=np.array([2.613, 2.575, 2.538, 2.463, 2.350, 2.238, 2.125,2.013,1.863])
L1L2= np.array([1.045, 1.124, 1.178, 1.229, 1.275, 1.319, 1.347,1.361,1.374])


data = {'Grados': [30,55],
        'L1': [interNumpy(x,L1L2,a)*(20/interNumpy(x,xL2,a)),interNumpy(x,L1L2,b)*(20/interNumpy(x,xL2,b))],
        'L2': [20/interNumpy(x,xL2,a),20/interNumpy(x,xL2,b)],
        'L3': [ interNumpy(x,L3L2,a)*(20/interNumpy(x,xL2,a)), interNumpy(x,L3L2,b)*(20/interNumpy(x,xL2,b))],
        'x/L2': [ interNumpy(x,xL2,a), interNumpy(x,xL2,b)],
        'L1/L2': [interNumpy(x,L1L2,a), interNumpy(x,L3L2,b)],
        'L3/L2': [ interNumpy(x,L3L2,a), interNumpy(x,L1L2,b)]}
df = pd.DataFrame(data)
print("Velocidad")
print(df)


#Interpolación y graficas con Lagrange

def interLagrange(x,y,a):
  plt.figure('1')
  plt.plot(x,y,'x', mew=2, label='Datos')
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.legend()
  
  
  p = lagrange(x,y)
  
  
  x1 = np.linspace(20,180,100)
  y1 = p(x1)
  
  plt.figure('2')
  plt.plot(x1, y1, label='interpolacion')
  plt.plot(x, y, 'x', mew=2, label='Datos')
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.legend()
  plt.show()
  return p(a)


xL2=np.array([0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181])
L3L2=np.array([3.963,3.925,3.850,3.738,3.588,3.438,3.250,3.025,2.800])
L1L2= np.array([2.975,2.950,2.9,2.825,2.725,2.625,2.500,2.350,2.200])

data = {'Grados': [30,55],
        'L1': [interLagrange(x,L1L2,a)*(20/interLagrange(x,xL2,a)),interLagrange(x,L1L2,b)*(20/interLagrange(x,xL2,b))],
        'L2': [20/interLagrange(x,xL2,a),20/interLagrange(x,xL2,b)],
        'L3': [ interLagrange(x,L3L2,a)*(20/interLagrange(x,xL2,a)), interLagrange(x,L3L2,b)*(20/interLagrange(x,xL2,b))],
        'x/L2': [ interLagrange(x,xL2,a), interLagrange(x,xL2,b)],
        'L1/L2': [interLagrange(x,L1L2,a), interLagrange(x,L3L2,b)],
        'L3/L2': [ interLagrange(x,L3L2,a), interLagrange(x,L1L2,b)]}
df = pd.DataFrame(data)
print("Fuerza")
print(df)


xL2=np.array([0.480, 0.950, 1.411, 1.845, 2.237, 2.600, 2.932,3.232,3.456])
L3L2=np.array([2.613, 2.575, 2.538, 2.463, 2.350, 2.238, 2.125,2.013,1.863])
L1L2= np.array([1.045, 1.124, 1.178, 1.229, 1.275, 1.319, 1.347,1.361,1.374])

data = {'Grados': [30,55],
        'L1': [interLagrange(x,L1L2,a)*(20/interLagrange(x,xL2,a)),interLagrange(x,L1L2,b)*(20/interLagrange(x,xL2,b))],
        'L2': [20/interLagrange(x,xL2,a),20/interLagrange(x,xL2,b)],
        'L3': [ interLagrange(x,L3L2,a)*(20/interLagrange(x,xL2,a)), interLagrange(x,L3L2,b)*(20/interLagrange(x,xL2,b))],
        'x/L2': [ interLagrange(x,xL2,a), interLagrange(x,xL2,b)],
        'L1/L2': [interLagrange(x,L1L2,a), interLagrange(x,L3L2,b)],
        'L3/L2': [ interLagrange(x,L3L2,a), interLagrange(x,L1L2,b)]}
df = pd.DataFrame(data)
print("Velocidad")
print(df)



''''
Conclusión:

La función Numpy muestra valores más precisos que la función de interpolación de lagrange.
''''
