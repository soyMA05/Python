# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:43:39 2022

@author: MIANCAS
"""

# =============================================================================
# EJERCICIO 3: Leer numeros hasta que se introduzca un cero. Para cada
# uno indicar si es par o impar
# =============================================================================

#dato entrada
numero = int(input("Ingrese un numero: "))

while numero !=0:
    if numero % 2 ==0:
        print(f"El numero {numero} es PAR")
    else:
        print(f"El numero {numero} es IMPAR")
        
    #dato entrada
    numero = int(input("Ingrese un numero: "))

print("\n Ha salido....")