# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:11:08 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 12: Pedir un numero y calcular su factorial
# =============================================================================

#Datos/variables
numero_usuario = int(input("Ingrese un numero: "))
factorial = 1

# =============================================================================
# #FORMA 1
# for contador in range(1,numero_usuario+1):
#     factorial *= contador
# 
# print(factorial)
# =============================================================================

#FORMA 2

i_contador = 1
while i_contador <= numero_usuario:
    factorial *= i_contador
    i_contador += 1

print(factorial)