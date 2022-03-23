# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:00:28 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 11: Diseñar un programa que muestre el producto
# de los 10 primeros numeros impares
# =============================================================================

producto = 1

#FORMA 1
# =============================================================================
# for numero in range (1, 11):
#     if numero % 2  == 1:
#         producto *= numero
#     else:
#         print(numero)
# 
# print("Producto total:", producto)
# =============================================================================

#FORMA 2

contador = 1 

while contador <= 10:
    if contador % 2 == 1:
        producto *= contador
    else:
        print(contador)
    contador += 1
    
print("Producto total:", producto)