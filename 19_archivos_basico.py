# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:14:47 2022

@author: MIANCAS
"""
# En FaztCode

#LECTURA (r o sin la r) de archivo 
with open("frases.txt", "r") as archivo:
    for linea in archivo:
        print(linea)

#Para ESCRIBIR(w) contenido al archivo si este está vacío 
with open("frases.txt", "w") as archivo:
    for linea in range(3):
        frase = input("Ingrese la frase: ")
        archivo.write(frase + " \n")

#Para AGREGAR (a) contenido al archivo si este archivo ya tienen un contenido
with open("frases.txt", "a") as archivo:
    for linea in range(1):
        frase = input("Ingrese la frase: ")
        archivo.write(frase + " \n")

#BORRAR TODO EL CONTENIDO  DEL ARCHIVO(r+)
with open("frases.txt", "r+") as archivo:
    archivo.truncate(0)


    
#USO DE DICCIONARIOS

clientes = {"Josh": 23,
            "Cesas": 23,
            "Xavier": 23
            }

with open("frases.txt","a") as archivo:
    for nombre, edad in clientes.items():
        archivo.write(nombre +" - " + str(edad) +" \n")
        