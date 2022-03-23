# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:50:14 2022

@author: MIANCAS
"""

# =============================================================================
# EJERCICIO 4: Pedir numeros hasta que se teclee uno negativo, y mostrar
# cuantos numeros se han introducido
# =============================================================================

#dato entrada
numero = int(input("Ingrese un numero: "))
contador = 0

while numero >= 0:
    contador +=1
    #dato entrada
    numero = int(input("Ingrese un numero: "))

print("Total de numero positivos: ", contador)    