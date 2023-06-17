# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:09:35 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 14: Pedir 10 sueldos. Mostrar su suma y cuantos sueldos hay mayores de $1000
# =============================================================================

#variables
suma_sueldo = 0
contador_sueldo = 0

for i in range(10):
    sueldo_usuario = int(input(f"{i+1}/10. Ingrese un sueldo:"))
    suma_sueldo += sueldo_usuario
    if sueldo_usuario >= 1000:
        contador_sueldo += 1

print("Suma de sueldos: ", suma_sueldo)
print("Sueldos mayores a $1000:", contador_sueldo)
    