# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:22:51 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 13: Pedir 10 numeros. Mostrar la media
# de los numeros positivos, la media de los numeros negativos
# y la cantidad de ceros
# =============================================================================

#variables
suma_positivos = 0
suma_negativos = 0
media_positivos = 0
media_negativos = 0
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0

# =============================================================================
# #FORMA 1
# #ingreso y clasificacion de numeros
# for i in range (10):
#     numero = int(input(f"{i+1}. Ingrese un numero: "))
#     if numero > 0:
#         suma_positivos += numero
#         contador_positivos += 1
#     elif numero < 0:
#         suma_negativos += numero
#         contador_negativos += 1
#     else:
#         contador_ceros += 1
# =============================================================================

#FORMA 2
contador = 0
#ingreso y clasificacion de numeros
while contador < 10:
    numero = int(input(f"{contador+1}. Ingrese un numero: "))
    if numero > 0:
        suma_positivos += numero
        contador_positivos += 1
    elif numero < 0:
        suma_negativos += numero
        contador_negativos += 1
    else:
        contador_ceros += 1
    contador +=1


#calculo de la media
if contador_positivos == 0:
    print("\nNo ha ingresado numeros positivos y por lo tanto no se puede dividir para cero")
else:
    media_positivos = suma_positivos / contador_positivos
    print("\nMedia positivos: ", media_positivos)

if contador_negativos == 0:
    print("No ha ingresado numeros negativos y por lo tanto no se puede dividir para cero")
else:
    media_negativos = suma_negativos / contador_negativos
    print("Media negativos: ", media_negativos)

#mostrar resultado
print("Cantidad de ceros: ", contador_ceros)
