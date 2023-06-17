# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 23:44:14 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 14: Leer dos series de 10 números enteros, que estarán ordenados crecientemente.
# Copiar (fusionar) las dos tablas en una tercera, de forma que sigan ordenados. 
# =============================================================================

#variables
lista1 = []
lista2 = []
lista_fusionada = []
creciente = False

#entrada datos serie 1
while creciente == False:
    print("****A****")
    for i in range(10):
        lista1.append(int(input(f"{i+1}. Ingrese un número: ")))
    
    #verificar si es creiciente a pesar
    creciente = True
    for i in range(9):
        if lista1[i] < lista1[i+1]:
            creciente = True
        if lista1[i] > lista1[i+1]:
            creciente = False
            break
        
    if creciente == False:
        print("Lista no Ordenada de forma creciente, ingrese de nuevo...")
        lista1.clear()
    
#entrada datos serie 2
creciente = False
while creciente == False:
    print("\n****B****")
    for i in range(10):
        lista2.append(int(input(f"{i+1}. Ingrese un número: ")))
    
    #verificar si es creiciente a pesar
    creciente = True
    for i in range(9):
        if lista2[i] < lista2[i+1]:
            creciente = True
        if lista2[i] > lista2[i+1]:
            creciente = False
            break
        
    if creciente == False:
        print("Lista no Ordenada de forma creciente, ingrese de nuevo...")
        lista2.clear()
    
print("Lista 1 >>>",lista1)
print("Lista 2 >>>",lista2)

#fusionar lista1 y lista2 en lista_fusionada
j = 0
for i in range(10):
    lista_fusionada.append(lista1[j])
    j += 1
j = 0
for i in range(10):
    lista_fusionada.append(lista2[j])
    j += 1

#ordenamiento creciente
lista_fusionada.sort()        
        
print("Lista F >>>",lista_fusionada)
