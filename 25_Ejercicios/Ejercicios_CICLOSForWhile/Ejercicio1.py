# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:31:04 2022

@author: MIANCAS
"""

# =============================================================================
# Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proceso
# hasta que se introduzca un numero negativo
# =============================================================================


numero = int(input("Ingrese un numero: "))
while numero >=0:
    numero= numero**2
    print(numero)
    numero = int(input("Ingrese un numero: "))
    
print("Ha pulsado un numero negativo...")