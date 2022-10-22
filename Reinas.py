#Título Programa: PRACTICA 2---Problema de las 8 Reinas.
#Fecha: 21-octubre-2022
#Autor: Renteria Arriaga Josue

# Exportación de las librerías a utilizar. 
import random # Esta librería nos ayuda a generar números aleatorios.
import numpy as np # Esta librería nos ayudara a utilizar arrays (para sacar el promedio).

def heuristica_pares(n):
    if n == 0:
        return 0
    else:
        n = (n-1)+heuristica_pares(int(n-1))

hola = heuristica_pares(4)
print(hola)
# Valores de Heuristica por pares (ej. Euristica de 3 pares (h3) = 6 posibilidades).
h1, h2, h3, h4, h5, h6, h7 = 0, 2, 6, 10, 15, 21, 28 # Nota: Podria hacerse una funcion recursiva

# Creacion del Arreglo BiDimencional de 8x8.
tablero_inicial = np.zeros((8, 8), dtype=np.int64) # Arreglo BiDimencional 8x8.
print(tablero_inicial)

# For que rellena el Arreglo BiDimencional de 8x8 con 1.
for i in range(8):
    movimiento = random.randint(0,7)
    tablero_inicial[movimiento, i] = 1

# Sacar la heuristica (Horizontalmente).

# Observar el Arreglo Final (utilizar para sacar la heuristica)
print("\n\n")
print(tablero_inicial)
