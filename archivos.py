# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:14:47 2022

@author: MIANCAS
"""

"""
#Lectura (r o sin la r) de archivo 
with open("frases.txt", "r") as archivo:
    for linea in archivo:
        print(linea)

"""

#Para escribir(w) contenido al archivo si este está vacío 
with open("frases.txt", "w") as archivo:
    for linea in range(3):
        frase = input("Ingrese la frase: ")
        archivo.write(frase + " \n")


#Para AGREGAR (a) contenido al archivo si este archivo ya tienen un contenido
with open("frases.txt", "a") as archivo:
    for linea in range(1):
        frase = input("Ingrese la frase: ")
        archivo.write(frase + " \n")

with open("frases.txt", "r") as archivo:
    for linea in archivo:
        print(linea)

"""
#BORRAR TODO CONTENIDO (r+)
with open("frases.txt", "r+") as archivo:
    archivo.truncate(0)
"""    
    
    
    