#Interpolación usando Nunmpy

#Fuerza

#20/L2

#30
import numpy as np

# Vectores dados
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181])

# Valor a interpolar
x_interpolar = 30

# Realizar la interpolación
f_interpolar = np.interp(x_interpolar, xi, fi)

print(f"El valor interpolado para xi=30 es: {f_interpolar}")


# Vectores dados

#55
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181])

# Valor a interpolar
x_interpolar = 55

# Realizar la interpolación
f_interpolar = np.interp(x_interpolar, xi, fi)

print(f"El valor interpolado para xi=30 es: {f_interpolar}")


#L3/L2

#30

xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([3.963,3.925,3.850,3.738,3.588,3.438,3.250,3.025,2.800])

# Valor a interpolar
x_interpolar = 30

# Realizar la interpolación
f_interpolar = np.interp(x_interpolar, xi, fi)

print(f"El valor interpolado para xi=30 es: {f_interpolar}")

#55

# Vectores dados
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([3.963,3.925,3.850,3.738,3.588,3.438,3.250,3.025,2.800])

# Valor a interpolar
x_interpolar = 55

# Realizar la interpolación
f_interpolar = np.interp(x_interpolar, xi, fi)

print(f"El valor interpolado para xi=30 es: {f_interpolar}")

