# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:00:39 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 7: Pedir numeros hasta que se introduzca uno negativo,
#  y calcular la media.
# =============================================================================
#datos
numero_usuario = int(input("Ingrese un numero: "))
suma_numeros = 0
media = 0
contador = 0
  
#suma de numeros 
while numero_usuario >=0:
    contador +=1
    suma_numeros += numero_usuario
    numero_usuario = int(input("Ingrese un numero: "))

if contador == 0:
    print("Debe ingresar un numero positivo porque no se puede dividir para cero")
else:
    #media
    media = suma_numeros/ contador
    print("Cantidad de Nros ingresados:", contador)
    print("Suma total:", suma_numeros)
    print("Media:",media)