# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:36:31 2022

@author: MIANCAS
"""

# =============================================================================
# EJERCICIO 2: Leer un numero e indicar si es positivo o negativo.
# El proceso se repetira hasta que se introduzca un 0
# =============================================================================
#entrada
numero = int(input("Ingrese un numero: "))
while numero != 0:
    if numero > 0:
        print(f"El {numero} es postivo")
    else:
        print(f"El {numero} es negativo")
    #entrada
    numero = int(input("Ingrese un numero: "))
        

print("\nHa salido....Ud ha pulsado el 0")