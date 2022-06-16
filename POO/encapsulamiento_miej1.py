# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:03:22 2022

@author: miancastillo
"""
#importar librerias import pandas as pd

#clase perro
class Perro:
    
    #atributos de clase
    TIPO = "canino"
    numero_de_perros = 0
    
    #constructor y atributos de objeto
    def __init__(self, _nombre, _edad, _raza):
        self.nombre = _nombre
        self.edad = _edad
        self.raza = _raza
        self.habilidades = []
        Perro.numero_de_perros +=1 # suma los objetos creados
    
    # agregar habilidades para cada objeto
    def agregarhabilidades(self, _habilidadesPerro):
        self.habilidades.append(_habilidadesPerro)
        return self.habilidades
    
    # mostrar datos del objeto 
    def mostrarDatos(self):
        datos = str("\t"+self.nombre +" \t" +str(self.edad) +" \t" + self.raza)
        return datos
    
    # listar habilidades del perro
    def mostrarHabilidades(self):
        datos_habilidades = ""
        for i in self.habilidades:
            datos_habilidades += "-" + i +"\n\t\t"
        lista_habilidades = str(self.nombre +" \t" + datos_habilidades)
        return lista_habilidades

#VARIABLES
lista_perros = [] #registro de perros a ingresar

#digitar el numero de registros de perros a ingresar
numero_perros = int(input("Ingrese el numero de perros a ingresar: "))

#ingresar datos del objeto 
for i in range(numero_perros):
    print(f"****REGISTRO DEL PERRO {i+1}****")
    nombre = str(input("Digite su nombre: "))
    edad = int(input("Ingrese su edad: "))
    raza = str(input("Ingrese su raza: "))
    
    #instancia de clase con los valores digitados 
    perro = Perro(nombre, edad, raza)
    
    #preguntar si el perro tiene habilidades
    select_habilidad = int(input(f"Desea ingresar las habilidades de {nombre}? 1.SI  2.NO: "))
    while(select_habilidad <1 or select_habilidad >2 ):
        select_habilidad = int(input(f"Desea ingresar las habilidades de {nombre}? 1.SI  2.NO: "))
    
    #ingreso de habilidades del perro
    while(select_habilidad == 1):
        habilidad = str(input(f"Ingrese la habilidad de {nombre}: "))
        perro.agregarhabilidades(habilidad)
        select_habilidad = int(input(f"Desea ingresar otra habilidad de {nombre}? 1.SI  2.NO: "))
        
    #agregar objeto perro a un diccionario
    dicc_perro = {i:perro}
    
    #agregar diccionario a una lista de registro de perro
    lista_perros.append(dicc_perro)

#mostrar lista de perros agregados 
print(f"----------LISTA DE PERROS--------------\nNro de Perros:{perro.numero_de_perros} \n\n\tNombre \tEdad \tRaza")
j=0#para acceder a cada objeto por medio de la clave que se ha agregado a la lista de perros.
for i in lista_perros:
    print( i[j].mostrarDatos())
    j+=1

#mostrar lista de perros que pueden hacer habilidades
print("\n\n----------HABILIDADES DE LOS PERROS--------------\n\tNombre \tHabilidad")
#F
j=0
for i in lista_perros:
    print(i[j].mostrarHabilidades())
    j+=1

