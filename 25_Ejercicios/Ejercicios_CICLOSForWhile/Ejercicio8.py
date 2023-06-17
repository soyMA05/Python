# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:22:05 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 8: Pedir un numero N, y mostrar todos los numeros
# del 1 al N
# =============================================================================

#datos 
numero_usuario = int(input("Ingrese un numero: "))

# =============================================================================
# #FORMA 1
# for numero in range( 1, numero_usuario+1):
#     print(numero)
#     
# =============================================================================

#FORMA 2
contador = 1
while contador <= numero_usuario:
    print(contador)
    contador += 1
    