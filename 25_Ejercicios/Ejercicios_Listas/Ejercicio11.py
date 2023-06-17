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

#entrada
while creciente == False: 
    for i in range(5):
        lista.append(int(input(f"{i+1}. Ingrese un numero: ")))  
    
    creciente = True
    for i in range(4):
        if lista[i] < lista[i+1]:
            creciente = True
        if lista[i] > lista[i+1]:
            creciente = False
            break
    
    if creciente == False:
        print("Lista no Ordenada de forma creciente")
        lista.clear()
        
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
    
#desplazar posiciones
j = 4
while j >= contador_posicion:
    lista[j+1] = lista[j]
    j -= 1

#agregar nuevo numero 
lista[contador_posicion] = numero_usuario

print(lista)