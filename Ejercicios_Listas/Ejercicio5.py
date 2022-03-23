# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:17:17 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 5: Leer por teclado dos tablas de 10 números enteros y mezclarlas 
# en una tercera de la forma: el 1° de A, el 1° de B, el 2° de A, el 2° de B.
# =============================================================================

#variables
lista_a = []
lista_b = []
lista_ab = []
cadena_listaAB = ""
#llenar lista a y b
for i in range(10):
    lista_a.append(int(input(f"**A** \n{i}. Ingrese un numero: ")))

for i in range(10):
    lista_b.append(int(input(f"**B** \n{i}. Ingrese un numero: ")))

print("Longitud de lista_a")
print(len(lista_a))

#combinar listas
j=0
k=0
for i in range(0,19,2):
    lista_ab.insert(i, lista_a[j])
    lista_ab.insert(i+1, lista_b[k])
    j+=1
    k+=1

#mostrar elementos combinados
print("***Elementos Combinados***")
for i in range(20):
    cadena_listaAB += str(lista_ab[i]) + " "
    #print(lista_ab[i])
    
print(cadena_listaAB)