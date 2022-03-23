# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:39:28 2022

@author: MIANCAS
"""

# =============================================================================
# EJERCICIO 10: Pedir 10 numeros y escribir la suma 
# total
# =============================================================================

#variables/datos
suma_numeros = 0

#FORMA 1
# =============================================================================
# for i in range(10):
#     numero_usuario = int(input(f"{i+1}.Ingrese un numero: "))
#     suma_numeros += numero_usuario
# 
# print("Suma total: ",suma_numeros)
# =============================================================================

contador = 1
while contador <=10:
    numero_usuario = int(input(f"{contador}.Ingrese un numero: "))
    suma_numeros += numero_usuario
    contador+=1

print(suma_numeros)
