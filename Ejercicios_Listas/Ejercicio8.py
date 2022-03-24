# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:10:06 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 8: Diseñar una aplicación que declare una tabla de 10 elementos enteros.
# Leer mediante el teclado 8 números. Después pedir un número y una posición, 
# insertarlo en la posición indicada, desplazando los que estén detrás. Completado
# =============================================================================

#variables
lista_numeros = []
backup_listaNumeros = []
cadena_listaNum = " "

#llenar tabla
for i in range(8):
    lista_numeros.append(int(input(f"{i}. Ingrese un numero: ")))

#nuevo datos del usurio
numero_usuario = int(input("Ingrese un nuevo numero: "))
posicion_usuario = int(input("Ingrese una posicion para el nuevo numero: "))

#crear backup 
# =============================================================================
# contador_posicion = posicion_usuario
# j = 0
# longitud_backup = len(lista_numeros)-posicion_usuario
# while j < (longitud_backup):
#     backup_listaNumeros.append(lista_numeros[contador_posicion])
#     contador_posicion +=1
#     j+=1
# 
# #mostrar backup
# for i in range(longitud_backup):
#     print(backup_listaNumeros[i])
# =============================================================================

#insertar elemento nuevo en la lista (cada vez que se ingresa un nuevo elemento la lista aumenta de tamanio)
lista_numeros.insert(posicion_usuario, numero_usuario)

#mostrar lista con nuevo elemento
for i in range(len(lista_numeros)): #longitud es 9
    cadena_listaNum += str(lista_numeros[i]) + " "
print(f"****LISTA COMPLETA **** \n {cadena_listaNum}")
