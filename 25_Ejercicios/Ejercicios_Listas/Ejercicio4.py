# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:41:51 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 4: Leer 10 números enteros, guardarlos en un arreglo.
# Debemos mostrarlos en el siguiente orden: el primero, el último, 
# el segundo, el penúltimo, el tercero. 
# =============================================================================
#variables
lista = []
cadena_lista = " "

#llenar lista
for i in range(10):
    lista.append(int(input(f"{i}. Ingrese un numero:")))

#mostrar lista
i_contador=0
j_contador=9
for i in range(5):
    cadena_lista += str(lista[i]) + " " +str(lista[j_contador]) + " " 
    j_contador -=1

print(cadena_lista)