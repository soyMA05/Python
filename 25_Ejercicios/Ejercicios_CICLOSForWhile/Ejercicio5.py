# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:32:55 2022

@author: MIANCAS
"""
import random
# =============================================================================
# EJERCICIO 5: Realizar un juego para adivinar un numero. Para ello genera un numero aleatorio entre 0 - 100,
# y luego ir pidiendo numeros indicando es mayor o es menor segun sea mayor o menor con respecto a N.
#  El proceso termina cuando el usuario acierta y mostrar el numero de intentos.
# =============================================================================

#datos
numero_usuario = int(input("Ingrese un numero entre 0 - 100: "))
numero_aleatorio = random.randint(0, 2)
contador_intentos = 1

while numero_usuario != numero_aleatorio and (numero_usuario>=0 and numero_usuario<=100):
    if numero_usuario > numero_aleatorio:
        print("Es un numero menor")
    if numero_usuario < numero_aleatorio:
        print("Es un numero mayor")
    numero_usuario = int(input("Ingrese un numero entre 0 - 100: "))
    contador_intentos +=1

if numero_usuario<=0 or numero_usuario>=100:
    print("Ha digitado un numero fuera del rango entre 0- 100")
if numero_usuario == numero_aleatorio:
    print(f"Ha encontrado el numero {numero_aleatorio} en {contador_intentos} intentos")