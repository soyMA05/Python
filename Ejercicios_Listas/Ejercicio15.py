# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:16:07 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 15: Leer 10 enteros ordenados crecientemente. Leer N y buscarlo en 
# la tabla. Se debe mostrar la posición en que se encuentra. Si no está, indicarlo 
# con un mensaje. 
# =============================================================================

#variables 
lista = []
creciente = False

#entrada datos serie 1
while creciente == False:
    print("****A****")
    for i in range(10):
        lista.append(int(input(f"{i+1}. Ingrese un número: ")))
    
    #verificar si es creiciente a pesar
    creciente = True
    for i in range(9):
        if lista[i] < lista[i+1]:
            creciente = True
        if lista[i] > lista[i+1]:
            creciente = False
            break
        
    if creciente == False:
        print("Lista no Ordenada de forma creciente, ingrese de nuevo...")
        lista.clear()

#buscar numero y posicion
n = 1
while n != 0:
    numero_usuario  = int(input("Ingrese un número a buscar: "))
    buscar_numero = numero_usuario in lista
    if buscar_numero == True:    
        posicion = lista.index(numero_usuario)
        print(f"El elemento {numero_usuario} se encuentra en la posicion {posicion}")
    else:
        print(f"El elemento {numero_usuario} no se encuentra en la lista ")
    print(lista)
    
    n = int(input("Digite: \n1. CONTINUAR: 0. SALIR \n>>>>"))
