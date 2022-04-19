# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 23:09:49 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 10: Crear un programa que lea por teclado una tabla de 10 números enteros 
# y desplace N posiciones en el arreglo (N es digitado por el usuario). 
# =============================================================================

#variables
lista = []
lista_backup = []
#entrada 
for i in range (10):
    lista.append(int(input(f"{i+1}. Ingrese un numero: ")))

"""
#Forma 1
numero_posicion = int(input("Ingrese una posición a desplazar entre 1 - 9: "))
while numero_posicion < 0 or numero_posicion >9 :
    numero_posicion = int(input("Ingrese una posición a desplazar correcta entre 1 - 9: "))
"""

#Forma2
while (True):
    numero_posicion = int(input("Ingrese una posición a desplazar entre 1 - 9: "))
    if numero_posicion > 0 and numero_posicion <9:
        break

# dezplazar n posiciones
j = 0
for i in range(10):
    if i + numero_posicion < 10:
        nueva_posicion = i + numero_posicion
        lista_backup.insert(nueva_posicion, lista[j])
    if i + numero_posicion > 9:
        nueva_posicion = abs((i + numero_posicion) - len(lista) )
        lista_backup.insert(nueva_posicion, lista[j])
        
    j += 1

#print(len(lista_backup))   
print(lista_backup)