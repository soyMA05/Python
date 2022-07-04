# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 17:56:38 2022

@author: miancastillo
"""

#Crear clase animal
class Animal:
    #atributos de clase
    predio='Rancho Casi un Angel'
    totalanimales= []
    
    #crear metodo constructor
    def __init__(self, nombre:str, peso:float, raza:str, edad=0):
        #ejecutar validaciones a los argumentos de entrada
        assert peso >= 0 ,f"El peso ingresado es {peso} y debe ser mayor a cero"
        assert edad >= 0 , f"La edad ingresada es {edad} y debe ser mayor o igual a cero"
        
        #asignar los valores de atributos de clase
        self.nombre= nombre
        self.peso = peso
        self.raza = raza
        self.edad = edad
        
        #agregar cada instancia a una lista
        Animal.totalanimales.append(self)
        
    #devolver objetos creados
    def __repr__(self):
        return f"Animal({self.nombre}, {self.peso}, {self.raza}, {self.edad})"
    

#crear instancias
animal1= Animal("Pulga", 430.3, "Browswiss", 5)
animal2= Animal("Pepita", 230.3, "Jersey", 5)
animal3= Animal("Blanca", 523.3, "Hosltein", 5)

#imprimir todos los objetos
print(Animal.totalanimales)

#imprimir solo nombres de los objetos
for i in Animal.totalanimales:
    print(i.nombre)

"""PENDIENTES: guardar animales en un diccionario y visualizar el archivo json con todos los animales creados."""