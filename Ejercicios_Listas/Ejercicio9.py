# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 00:46:38 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 9: Crear un programa que lea por teclado una tabla de 10 números enteros y
#  la desplace una posición hacia abajo: el primero pasa a ser el segundo, el segunda pasa 
#  a ser el tercero y así sucesivamente. El último pasa a ser el primero.
# =============================================================================

#variables
lista_numeros = []
backup_lista = []
cadena_backup = " "
#llenar lista
for i in range(10):
    lista_numeros.append(int(input(f"{i+1}. Ingrese un numero: ")))

#ordenando lista
j = 0
for i in range(9):
    if i == 0 :
        backup_lista.insert(i,lista_numeros[j+9])
    backup_lista.insert(i+1,lista_numeros[j])
    j += 1

#mostrar lista nueva
for i in range(10):
    cadena_backup += str(backup_lista[i]) + " "

print(cadena_backup)
    