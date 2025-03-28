# -*- coding: utf-8 -*-
"""Ejercicio2_Tarea3.3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ah43ExOAlrSlczD2YGaHclX86F5O7luO
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir el sistema de ecuaciones del ejemplo
A = np.array([[8, 2, -1, 0, 0, 0],
              [3, 15, -2, 1, 0, 0],
              [0, -2, 12, 2, -1, 0],
              [0, 1, -1, 9, -2, 1],
              [0, 0, -2, 3, 14, 1],
              [0, 0, 0, 1, -2, 10]])

b = np.array([10, 24, -18, 16, -9, 22])

# Solución exacta del sistema
sol_exacta = np.linalg.solve(A, b)

# Parámetros de convergencia
tolerancia = 1e-6
max_iter = 100

# Implementación del método iterativo de Jacobi
def jacobi(A, b, tol, max_iter):
    n = len(A)
    x = np.zeros(n)  # Vector de aproximación inicial
    errores_abs = []
    errores_rel = []
    errores_cuad = []

    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            suma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - suma) / A[i, i]

        # Cálculo de errores
        error_abs = np.linalg.norm(x_new - sol_exacta, ord=1)
        error_rel = np.linalg.norm(x_new - sol_exacta, ord=1) / np.linalg.norm(sol_exacta, ord=1)
        error_cuad = np.linalg.norm(x_new - sol_exacta, ord=2)

        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cuad.append(error_cuad)

        print(f"Iteración {k+1}: Error absoluto = {error_abs:.6f}, Error relativo = {error_rel:.6f}, Error cuadrático = {error_cuad:.6f}")

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break

        x = x_new

    return x, errores_abs, errores_rel, errores_cuad, k+1

sol_aprox, errores_abs, errores_rel, errores_cuad, iteraciones = jacobi(A, b, tolerancia, max_iter)

# Graficar los errores con nuevos colores
plt.figure(figsize=(8,6))
plt.plot(range(1, iteraciones+1), errores_abs, label="Error absoluto", marker='o', color='purple')
plt.plot(range(1, iteraciones+1), errores_rel, label="Error relativo", marker='s', color='orange')
plt.plot(range(1, iteraciones+1), errores_cuad, label="Error cuadrático", marker='d', color='cyan')
plt.xlabel("Iteraciones")
plt.ylabel("Error")
plt.yscale("log")
plt.title("Convergencia de los errores en el método de Jacobi")
plt.legend()
plt.grid()
plt.savefig("errores_jacobi_colores_nuevos.png")
plt.show()

# Mostrar la solución obtenida
print(f"Solución aproximada: {sol_aprox}")
print(f"Solución exacta: {sol_exacta}")