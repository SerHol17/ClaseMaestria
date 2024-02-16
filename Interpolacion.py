#Interpolación Usando Numpy

import numpy as np

def interNumpy(x,y,x0):
  return np.interp(x0, x, y)


#Cargamos Vectores
x=np.array([20, 40, 60, 80, 100, 120, 140, 160, 180]) #Angulos
xL2=np.array([0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181])
L3L2=np.array([3.963,3.925,3.850,3.738,3.588,3.438,3.250,3.025,2.800])
L1L2= np.array([2.975,2.950,2.9,2.825,2.725,2.625,2.500,2.350,2.200])

#Angulos a interpolar
a=30
b=55
print("El valor interpolado para",a,"grados en x/L2 es:",interNumpy(x,xL2,a))
print("El valor interpolado para",a,"grados en L3/L2 es:",interNumpy(x,L3L2,a))
print("El valor interpolado para",a,"grados en L1/L2 es:",interNumpy(x,L3L2,a))

print("El valor interpolado para",b,"grados en x/L2 es:",interNumpy(x,xL2,b))
print("El valor interpolado para",b,"grados en L3/L2 es:",interNumpy(x,L3L2,b))
print("El valor interpolado para",b,"grados en L1/L2 es:",interNumpy(x,L3L2,b))
