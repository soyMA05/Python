# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:03:54 2022

@author: miancastillo
"""

""" PARTE 1: MANERAS DE CREAR CLASES """

""" 1. Con variables """
print(type(5)) #este es una clase de tipo int
Item = "Telefono"#variable Item de tipo string
Item_precio = 200 #variable de tipo int
Item_cantidad = 2
print(type(Item))#se visualiza la clase de tipo str o string
print(type(Item_precio))#se visualiza la clase de tipo int
print(type(Item_cantidad))#se visualiza la clase de tipo int


""" 2. Usando la palabra clave class """
class Item1:
    pass #permite crear clases minimas. Tambien le indica al programa que ignore cierta condicion y continue con el resto.
    
item1 = Item1() #instancia de clase Item1

""" Atributos de la clase Item1 """
item1.name = "Telefono"
item1.precio = 200
item1.cantidad = 2

print(type(item1.name))#obtenemos el mismo resultado que el anterior.


""" 3. Crear clase con metodo basico. """

class Item2:
    def calcular_total_precio(self, x, y):
        return x * y
    

#instancias
item_1 = Item2()
item_1.precio = 30
item_1.cantidad = 4

item_2 = Item2()
item_2.precio = 500
item_2.cantidad = 5

#invocacion de metodo y visualizacion de precios
print(item_1.calcular_total_precio(item_1.precio, item_1.cantidad))
print(item_2.calcular_total_precio(item_2.precio, item_2.cantidad))





