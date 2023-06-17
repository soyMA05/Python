# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:22:37 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 7: Leer por teclado una serie de 10 números enteros. La aplicación debe indicarnos si 
# los números están ordenados de forma creciente, decreciente, o si están desordenados.  
# =============================================================================

#variables
lista = []
creciente = False
decreciente = False

#llenar lista
for i in range(10):
    lista.append(int(input(f"{i+1}. Ingrese un elemento: ")))

for i in range(9):
    if lista[i] < lista[i+1]:
        creciente = True
    if lista[i] > lista[i+1]:
        decreciente = True
    if decreciente == True and creciente == True:
        break

if creciente == True and decreciente == False:
    print("La lista esta ordenado de forma CRECIENTE")
elif decreciente == True and creciente == False:
    print("La lista esta ordenado de forma DECRECIENTE")
elif decreciente == True and creciente == True:
    print("La lista esta DESORDENADO")
elif decreciente == False and creciente == False:
    print("Lista con elementos IGUALES")