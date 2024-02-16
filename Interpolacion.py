#Interpolación Usando Numpy

import numpy as np

def interNumpy(x,y,x0):
  return np.interp(x0, x, y)


#Cargamos Vectores Fuerza
x=np.array([20, 40, 60, 80, 100, 120, 140, 160, 180]) #Angulos
xL2=np.array([0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181])
L3L2=np.array([3.963,3.925,3.850,3.738,3.588,3.438,3.250,3.025,2.800])
L1L2= np.array([2.975,2.950,2.9,2.825,2.725,2.625,2.500,2.350,2.200])

#Angulos a interpolar
a=30
b=55

#Valores 30°

print("El valor interpolado para L1",a,"en fuerza es:", L1L2*(20/interNumpy(x,L1L2,a)))
print("El valor interpolado para L2",a,"en fuerza es:", 20/interNumpy(x,L3L2,a))
print("El valor interpolado para L3",a,"en fuerza es:", L3L2/(20/interNumpy(x,L3L2,a)))

print("El valor interpolado para",a,"grados en x/L2 en fuerza es:",interNumpy(x,xL2,a))
print("El valor interpolado para",a,"grados en L3/L2 en fuerza es:",interNumpy(x,L3L2,a))
print("El valor interpolado para",a,"grados en L1/L2 en fuerza es:",interNumpy(x,L1L2,a))

#Valores 55°

print("El valor interpolado para L1",b,"en fuerza es:", L1L2*(20/interNumpy(x,L1L2,b)))
print("El valor interpolado para L2",b,"en fuerza es:", 20/interNumpy(x,L3L2,b))
print("El valor interpolado para L3",b,"en fuerza es:", L3L2/(20/interNumpy(x,L3L2,b)))

print("El valor interpolado para",b,"grados en x/L2 en fuerza es:",interNumpy(x,xL2,b))
print("El valor interpolado para",b,"grados en L3/L2 en fuerza es:",interNumpy(x,L3L2,b))
print("El valor interpolado para",b,"grados en L1/L2 en fuerza es:",interNumpy(x,L1L2,b))


#Cargamos Vectores velocidad

xL2=np.array([0.480, 0.950, 1.411, 1.845, 2.237, 2.600, 2.932,3.232,3.456])
L3L2=np.array([2.613, 2.575, 2.538, 2.463, 2.350, 2.238, 2.125,2.013,1.863])
L1L2= np.array([1.045, 1.124, 1.178, 1.229, 1.275, 1.319, 1.347,1.361,1.374])

print("El valor interpolado para",a,"grados en x/L2 en velocidad es:",interNumpy(x,xL2,a))
print("El valor interpolado para",a,"grados en L3/L2 en velocidad es:",interNumpy(x,L3L2,a))
print("El valor interpolado para",a,"grados en L1/L2 en velocidad es:",interNumpy(x,L3L2,a))

print("El valor interpolado para",b,"grados en x/L2 en velocidad es:",interNumpy(x,xL2,b))
print("El valor interpolado para",b,"grados en L3/L2 en velocidad es:",interNumpy(x,L3L2,b))
print("El valor interpolado para",b,"grados en L1/L2 en velocidad es:",interNumpy(x,L3L2,b))
