#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

'''
Ejemplo de resolución de sistema de ecuaciones lineal
'''
A = np.array([[1, 1, 2], [2, 4, -3], [3, 6, -5]])
b = np.array([9, 1, 0])
AB = np.array([[1, 1, 2, 9], [2, 4, -3, 1], [3, 6, -5, 0]])

print(np.linalg.matrix_rank(A) == np.linalg.matrix_rank(AB))
print(np.linalg.matrix_rank(A) == 3)

x = np.linalg.solve(A, b)
print(x)

# Comprovamos que la solución es correcta obteniendo el vector de terminos
# independientes
print(A.dot(x))

'''
Ejemplo de resolución de sistema de ecuaciones lineal utilizando la libreria
sympy
'''
from sympy import symbols, Matrix
from sympy.solvers.solveset import linsolve

x, y, z = symbols('x,y,z')
x1, x2, x3 = symbols('x1,x2,x3')
sol = linsolve([2*x1 + 2*x2 -1, -x1 + x2 -2], (x1, x2))
print(sol)

# Lo mismo pero introduciendo la matriz ampliada
sol = linsolve(Matrix(([2, 2, 1], [-1, 1, 2])), (x1, x2))
print(sol)

# Opcion 2 de esto último

AB = Matrix(([2, 2, 1], [-1, 1, 2]))
A = AB[:, :-1] # Todas las filas de todas las columnas menos la última
b = AB[:, -1] # Todas las filas de la última columna
system = A, b
sol = linsolve(system, x1, x2)
print(sol)
