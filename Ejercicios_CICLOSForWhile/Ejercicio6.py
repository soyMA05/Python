# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:07:50 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 6: Pedir numeros hasta que se teclee un 0, mostrar la
# suma de todos los numeros introducidos
# =============================================================================

#datos
numero = int(input("Ingrese un numero: "))
suma_numeros = 0
contador = 0

while numero!=0:
    contador +=1
    suma_numeros += numero
    numero = int(input("Ingrese un numero: "))
    
print(f"Suma total: {suma_numeros} en {contador} intentos")
    