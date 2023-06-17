# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:19:34 2022

@author: MIANCAS
"""

# =============================================================================
# EJERCICIO 2: Ingresar elementos a una lista e imprimir la lista de atras hacia adelante
# =============================================================================

#variables
lista = []

#llenar lista
for i in range (10):
    lista.append(input("Ingrese un elemento: "))
    
#imprimir lista 
for i in range (9,-1,-1):
    print(lista[i])