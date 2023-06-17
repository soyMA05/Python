# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 23:24:51 2022

@author: MIANCAS
"""

# =============================================================================
# EJERCICIO 16: Ingresar un numero entre 0 - 10 y que muestre la tabla de multiplicar de dicho numero.
# =============================================================================

#variables
resultado = 0

numero_usuario = int(input("Ingrese un numero: "))

while numero_usuario >= 0 and numero_usuario <= 10:
    for i in range(11):
        resultado = numero_usuario * i
        print(f"{numero_usuario} x {i} = {resultado}")
    numero_usuario = int(input("Ingrese un numero: "))

print("Saliste....")