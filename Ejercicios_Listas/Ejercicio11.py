# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:00:02 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 11: Leer 5 elementos numéricos que se introducirán ordenados de forma creciente. 
# Estos los guardaremos en una tabla de tamaño 10. Leer un número N, e insertarlo en el lugar 
# adecuado para que la tabla continué ordenado.
# =============================================================================

#variables
lista = []
creciente = False
decreciente = False
n = 0

#entrada
while n == 0: 
    for i in range(5):
        lista.append(int(input(f"{i+1}. Ingrese un numero: ")))   
    
    for i in range(4):
        if lista[i] < lista[i+1]:
            creciente = True
        elif lista[i] > lista[i+1]:
            decreciente = True
        elif creciente == True and decreciente == True:
            break
    
    if creciente == True and decreciente == False:
        n = 1
        #print("Ordenado de forma creciente")
    elif creciente == False and decreciente == True:
        print("Elementos no ordenados de forma creciente")
    elif creciente == True and decreciente == True:
        print("Elementos no ordenados de forma creciente")
    else:
        n = 1
        #print("Iguales")
    creciente = False
    decreciente = False
    
# completar lista de tamaño 10
for i in range(5):
    lista.append(0)

# entrada nuevo numero y encontrar su posicion
numero_usuario = int(input("Ingrese un nuevo número: "))
j = 0
contador_posicion = 0

while lista[j] < numero_usuario and j < len(lista) - 5:  
    contador_posicion += 1
    j += 1

#agregar nuevo numero 
lista[contador_posicion] = numero_usuario

print(lista)