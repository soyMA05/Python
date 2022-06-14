# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:03:22 2022

@author: miancastillo
"""
#importar librerias import pandas as pd

#crear clase perro
class Perro:
    #atributos
    tipo = "canino"
    def __init__(self, _nombre, _edad, _raza):
        self.nombre = _nombre
        self.edad = _edad
        self.raza = _raza
        self.trucos = []
    
    def agregarTrucos(self, _trucosPerro):
        self.trucos.append(_trucosPerro)
        return self.trucos
    
    def mostrarDatos(self):
        datos = str("\t"+self.nombre +" \t" +str(self.edad) +" \t" + self.raza)
        return datos
    
    def mostrarDatos_trucos(self): #F
        lista_trucos = str(lambda truco : len(self.trucos))
        datos_trucos = str(self.nombre +" \t" + lista_trucos)
        return datos_trucos

#variables
lista_perros = []

#digitar el numero de registros de perros a ingresar
numero_perros = int(input("Ingrese el numero de perros a ingresar: "))

#bucle para ingresar los datos 
for i in range(numero_perros):
    print(f"****REGISTRO DEL PERRO {i+1}****")
    nombre = str(input("Digite el nombre del perro: "))
    edad = int(input("Ingrese la edad del perro: "))
    raza = str(input("Ingrese la raza del perro: "))
    
    #creacion de objeto y asignacion de valores 
    perro = Perro(nombre, edad, raza)
    num_trucos = int(input("Desea ingresar los trucos que puede hacer este perro ? 1.SI  2.NO"))
    if (num_trucos == 1):
        truco = str(input("Ingrese el truco que puede hacer el perro: "))
        perro.agregarTrucos(truco)
    #agregar objeto perro a un diccionario
    dicc_perro = {i:perro}
    
    #agregar diccionario a una lista
    lista_perros.append(dicc_perro)

#mostrar lista de perros agregados 
print("----------LISTA DE PERROS--------------\n\tNombre \tEdad \tRaza")
j=0
for i in lista_perros:
    print(i[j].mostrarDatos())
    j+=1

#mostrar lista de perros que pueden hacer trucos
print("----------LISTA DE PERROS CON TRUCOS--------------\n\tNombre \tHabilidad")
#F
j=0
for i in lista_perros:
    print(i[j].mostrarDatos_trucos())
    j+=1


#NOTA: falta mostrar el contenido de la lista de los trucos que puede hacer un perro