#Título Programa: PRACTICA 2---Problema de las 8 Reinas.
#Fecha: 21-octubre-2022
#Autor: Renteria Arriaga Josue

# Exportación de las librerías a utilizar. 
import random # Esta librería nos ayuda a generar números aleatorios.
import numpy as np # Esta librería nos ayudara a utilizar arrays (para sacar el promedio).
from tkinter import * # Para crear el tablero grafico.

# Funcion Recursiva que saca la Heuristica de los pares Hn = (n-1) + Hn-1
def heuristica_pares(numero):
    if numero == 0:
        return 0 # Para el Caso Base.
    else:
        return ((numero - 1) + heuristica_pares(numero -1)) #Caso de Estudio.

# Funcion que saca la Heuristica de nuestro tablero de forma horizontal.
def conteo_horizontal(array):
    heuristica = 0
    for i in range(8):
        contador = 0

        for j in range(8):
            if array[i,j] == 1:
                contador += 1

        # Mandamos a llamar al contador.
        heuristica += heuristica_pares(contador)
    
    return heuristica

# Funcion que saca la Heuristica de nuestro tablero de forma Diagonal.
def conteo_diagonal3(array):
    heuristica = 0
    lista1 = []
    lista2 = []
    for i in range(8):
        for j in range(8):
            contador1 = 0
            contador2 = 0

            # Hace la Busqueda de Derecha a Abajo (Eje. (2,3)-(3,4)). 
            if array[i,j] == 1 and (lista1.count((i,j)) == 0):
                x = i
                y = j
                while (x < 8 and y < 8):
                    if array[x,y] == 1:
                        lista1.append((x,y)) # Agregamos la dupla a una lista (Para no repetir elementos).
                        contador1 += 1
                    x = x + 1
                    y = y + 1
            
            # Hace la Busqueda de Abajo a Izquierda (Eje. (2,3)-(1,4)). 
            if array[i,j] == 1 and (lista2.count((i,j)) == 0):
                x = i
                y = j
                while (x < 8  and y > -1):
                    if array[x,y] == 1:
                        lista2.append((x,y)) # Agregamos la dupla a una lista (Para no repetir elementos).
                        contador2 += 1
                    x = x + 1
                    y = y - 1

            # Mandamos a llamar a los contadores y le agregamos su heuristica.
            heuristica += heuristica_pares(contador1)
            heuristica += heuristica_pares(contador2)
    return heuristica


# Funcion que saca la Heuristica de nuestro tablero de forma Diagonal (Empezando por la izquierda).
def conteo_diagonal(array):
    heuristica = 0
    lista = []
    for i in range(8):
        for j in range(8):
            contador = 0
            if array[i,j] == 1 and (lista.count((i,j)) == 0):
                x = i
                y = j
                while (x < 8 and y < 8):
                    if array[x,y] == 1:
                        lista.append((x,y))
                        contador += 1
                    x = x + 1
                    y = y + 1
            # Mandamos a llamar al contador.
            heuristica += heuristica_pares(contador)
    print(lista)
    return heuristica

# Funcion que saca la Heuristica de nuestro tablero de forma Diagonal (Empezando por la derecha).
def conteo_diagonal2(array):
    heuristica = 0
    lista = []
    for i in range(8):
        for j in range(8):
            contador = 0
            if array[i,j] == 1 and (lista.count((i,j)) == 0):
                x = i
                y = j
                while (x < 8  and y > -1):
                    if array[x,y] == 1:
                        lista.append((x,y))
                        contador += 1
                    x = x + 1
                    y = y - 1
            # Mandamos a llamar al contador.
            heuristica += heuristica_pares(contador)
    print(lista)
    return heuristica


# Creacion del Arreglo BiDimencional de 8x8.
tablero_inicial = np.zeros((8, 8), dtype=np.int64) # Arreglo BiDimencional 8x8.

# For que rellena el Arreglo BiDimencional de 8x8 con 1.
for i in range(8):
    movimiento = random.randint(0,7)
    tablero_inicial[movimiento, i] = 1

# Observar el Arreglo Final (utilizar para sacar la heuristica)
print(tablero_inicial)

# Sacar la heuristica (Horizontalmente).
heuristica_horizontal = conteo_horizontal(tablero_inicial)
print("\n\n")
print(f"La Hueristica Horizontal es de: {heuristica_horizontal}")

# Sacar la heuristica (Horizontalmente).
# heuristica_diagonal = conteo_diagonal(tablero_inicial)
# print(heuristica_diagonal)

# Sacar la heuristica (Horizontalmente).
# heuristica_diagona2 = conteo_diagonal2(tablero_inicial)
# print(heuristica_diagona2)

# Sacar la heuristica (Horizontalmente).
heuristica_diagonal3 = conteo_diagonal3(tablero_inicial)
print(f"La Hueristica Diagonal es de: {heuristica_diagonal3}")

heuristica_total = heuristica_horizontal + heuristica_diagonal3
print(f"La Hueristica Total es de: {heuristica_total}")

#Create & Configure root 
root = Tk()
Grid.rowconfigure(root, 0, weight=10)
Grid.columnconfigure(root, 0, weight=10)
root.geometry("500x500")

#Create & Configure frame 
frame = Frame(root)
frame.grid(row = 0, column = 0, sticky = N+S+E+W)
indice = 0
#Create a 8x8 (rows x columns) grid of buttons inside the frame
for row_index in range(8):
    Grid.rowconfigure(frame, row_index, weight = 10)
    for col_index in range(8):
        Grid.columnconfigure(frame, col_index, weight = 10)
        if tablero_inicial[row_index, col_index] == 1:
            btn = Button(frame, bg = "blue") #create a button inside frame
        else:
            btn = Button(frame) #create a button inside frame 
        btn.grid(row = row_index, column = col_index, sticky = N+S+E+W)  

root.mainloop()