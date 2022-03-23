# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 21:02:12 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 6: Leer los datos correspondientes a dos tablas de 12 elementos numéricos,
#  y mezclarlos en una tercera de la forma: 3 de la tabla A, 3 de la B, otros 3 de A, 
#  otros 3 de la B, etc. Completado
# =============================================================================

#variables
lista_a = []
lista_b = []
lista_ab = []
cadena_listaAB = " "

#llenar lista A y B
for i in range (12):
    lista_a.append(int(input(f"***A***\n {i+1}. Ingrese un numero: ")))

for i in range (12):
    lista_b.append(int(input(f"***B***\n {i+1}. Ingrese un numero: ")))

#longitud de la lista
#print(len(lista_a))

#Combinar listas
j = 0
for i in range (0,24,6):
    # A en lista_ab
    lista_ab.insert(i, lista_a[j])
    lista_ab.insert(i+1, lista_a[j+1])
    lista_ab.insert(i+2, lista_a[j+2])
    #B en lista_ab
    lista_ab.insert(i+3, lista_b[j])
    lista_ab.insert(i+4, lista_b[j+1])
    lista_ab.insert(i+5, lista_b[j+2])
    j += 3

# =============================================================================
#     #B en lista_ab
# j = 0
# for i in range (3,24,6):
#     lista_ab.insert(i, lista_b[j])
#     lista_ab.insert(i+1, lista_b[j+1])
#     lista_ab.insert(i+2, lista_b[j+2])
#     j += 3
# =============================================================================
    
#longitud de la lista
#print(len(lista_ab))

for i in range (24):
    #print(lista_ab[i])
    cadena_listaAB += str(lista_ab[i]) + " "

print(f"Lista Combinada: \n {cadena_listaAB}")