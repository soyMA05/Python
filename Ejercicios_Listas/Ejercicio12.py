# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:17:39 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 12: Leer por teclado una tabla de 10 elementos numéricos enteros y una 
# posición (entre 0 y 9). Eliminar el elemento situado en la posición dada sin dejar huecos.
# =============================================================================

#variables
lista = []

#entrada datos numericos y posicion
for i in range(10):
    lista.append(int(input(f"{i+1}. Ingrese un número: ")))

posicion = int(input("Ingrese una posición entre 0 - 9 para eliminar un elemento: "))
while posicion < 0 or posicion > 10:
    posicion = int(input("Ingrese una posición entre 0 - 9 para eliminar un elemento: "))

lista.pop(posicion)#al eliminar un elemento se reduce la longitud de la lista
print(lista)
