# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 23:03:08 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 13: Leer 10 enteros en una tabla. Guardar en otra tabla los 
# elementos pares de la primera, y a continuación los elementos impares.
# =============================================================================
#variables
lista = []
lista_pares = []
lista_impares = []
lista_concatenacion = []
salir = 1

while salir != 0:
    #entrada
    for i in range(10):
        lista.append(int(input(f"{i+1}. Ingrese un número: ")))
    
    #agregar elementos a lista pares e impares
    for i in range(10):
        if lista[i] % 2 == 0:
            lista_pares.append(lista[i])
        if lista[i] % 2 == 1:
            lista_impares.append(lista[i])
            
    #concatenar dos listas
    j = 0
    for i in range(len(lista_pares)):
        lista_concatenacion.append(lista_pares[j])
        if j == (len(lista_pares) - 1):
            break
        j += 1

    j = 0
    for i in range(len(lista_pares) + len(lista_impares)):
        lista_concatenacion.append(lista_impares[j])
        if j == (len(lista_impares) - 1):
            break
        j += 1
    
    #resultados    
    print(f"\nLista Pares:\n {lista_pares}")
    print(f"Lista Impares:\n {lista_impares}")
    print(f"Lista Concatenada:\n {lista_concatenacion}")
    
    #reinicilizar variables
    lista = []
    lista_pares = []
    lista_impares = []
    lista_concatenacion = []
    
    salir = int(input("1. CONTINUAR \t 0. SALIR \n >>Ingrese un número: "))



    