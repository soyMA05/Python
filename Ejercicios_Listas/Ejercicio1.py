# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:27:25 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 1: Ingresar e imprimir una lista
# =============================================================================
#variables
lista = []

#llenar lista
for i in range(10):
    #lista.append(int(input("Ingrese un numero: ")))
    #lista.append(str(input("Ingrese un nombre: ")))
    lista.append(input("Ingrese un elemento:"))
  
#imprimir elementos de la lista
print()
for i in range(10):
    print(lista[i])
    