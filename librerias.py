# -*- coding: utf-8 -*-
"""librerias.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xbWcIWknoqxd3xqc2MLVqhMfLtZka563
"""

#MATPLOTLIB
import matplotlib.pyplot as plt
# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar puntos
ax.scatter(x = [1, 2, 3], y = [3, 2, 1])
# Guardar el gráfico en formato png
plt.savefig('diagrama-dispersion.png')
# Mostrar el gráfico
plt.show()

#Producto de dos matrices
# a.dot(b) 
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 1], [2, 2], [3, 3]])
print(a @ b)
print(a.dot(b))

#1, Cree un objeto ndarray unidimensional con una longitud de 10 y todos 0, y luego haga que el quinto elemento sea igual a 1.
import numpy as np
a = np.zeros((1,10))
print(a)
a[0,4] =1
print(a)

#2, Crea un objeto ndarray con elementos del 10 al 49.
import numpy as np
a = np.arange (10,50)
print(a)

#Determinante de una matriz 
#.linalg.det()
import numpy as np
a = np.array([[1, 2], [3, 4]])
print(np.linalg.det(a))

#Matriz inversa
#.linalg.inv()
import numpy as np
a = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(a))

#Solución de un sistema de ecuaciones
#solve (a,b)
import numpy as np
# Sistema de dos ecuaciones y dos incógnitas
# x + 2y = 1
# 3x + 5y = 2 
a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
print(np.linalg.solve(a, b))