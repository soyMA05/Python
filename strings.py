# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:41:16 2022

@author: MIANCAS
"""

myStr= "Hola Mundo"

#CONCATENACION
print("La pelicula se llama "+ myStr)
print(f"La pelicula se llama {myStr}")#version de python > 3.6 
print("La nueva pelicula es : {0}".format(myStr)) 

#para obtener _propiedades  y metodos para hacer modificaciones con los datos
#print(dir(myStr)) 

#transformar texto a mayusculas, tipo oracion y otro metodos se pueden visualizar en el anterior
print(myStr.upper())
#transformar texto a tipo oracion
print(myStr.capitalize())
#transformar texto a minuscula
print(myStr.lower())

#reemplazar texto
print(myStr.replace("Hola", "Bienvenido"))

#metodo dentro de otro (conocido como metodos encadenados )
print(myStr.replace("Hola", "Bienvenido").lower())

#contar el numero de veces que se repite una letra o caracteres vacios
print(myStr.count('o'))
print(myStr.count(' '))

#para encontrar si el valor de una cadena empieza con una determinada palabra, arrojando un valor true o false
print(myStr.startswith('Hola'))
#para ver si terminar 
print(myStr.endswith('do'))

#SEPARAR el texto en listas
#separacion por espacios en blanco
print(myStr.split())

#separacion por coma
myStr2= "Hola,Mundo"
print(myStr2.split(','))

#separacion por letra
myStr2= "Hola,Mundo"
print(myStr2.split('o'))

#BUSCAR
# en que posicion se encuentra una letra
print(myStr.find('o'))

#con el indice que palabra se encuentra en esa posicion
print(myStr[5])
print(myStr[-1]) #de atras hacia adelante

#conocer la longitud de la variable de tipo string 
print(len(myStr))

#para conocer el indice de una letra (similar al metodo find() )
print(myStr.index('o'))

#DETECTAR
#para saber si variable es numerica o no
print(myStr.isnumeric())
#para saber si variable es Alfanumerica o no
print(myStr.isalpha())



#SLICING DE CADENAS
#posiciones      012345
#posiciones reversa -6-5-4-3-2-1       

#
cadena_reversa = "leugiM"
print(cadena_reversa[::-1])

texto='Hola Mundo'
print(texto[:4])

texto2= 'cadena'
print(texto2[-6::2])