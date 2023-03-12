# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:51:09 2022

@author: MIANCAS
"""
#FORMA 1 declarar variables
name="Miguel"
x =100
_1numero= 10 #no colocar primero un numero si no usar un _ para poder usar el numero para asignar nombre a las variables
lista=["Castillo", True, None]
tupla=("Libro Rino")
diccionario= {"nombre":"Miguel", "valor":10000}

print( "Nombre: " + name +  " Lista: " + tupla) #si la tupla tiene otro un dato que no sea string no deja imprimir

#case sensitive
book="Libro Free"
Book="Libro Free"


#FORMA 2 declarar variables
autor, edad= "Denzel Washigton", 55
print(autor, edad)

#Convenciones> se llaman convenciones porque los programadores eligen una forma de definir sus variables

book_name="I Robot" #Snake Case
bookName=" Rino" #Camel Case
BookName=" Tarzan" #Pascal Case

#constantes
PI = 3.1416 #con mayuscula se entiende que este valor es estatico, nunca cambia
NOMBRE = "Miguel"

#tipado dinamico (en java no se puede hacer esto)
nombre_estudiante="Miguel"
nombre_estudiante=23 
