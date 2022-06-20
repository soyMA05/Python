# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 22:45:34 2022

@author: miancastillo
"""

""" PARTE1: INICIALIZACION DEL CONSTRUCTOR SOLO CON INSTANCIAR UNA CLASE """

""" Creacion de clase Item """
class Item:
    
    #constructor
    def __init__(self):
        print("He sido creado")
        
""" Solo con instanciar la clase se ejecuta el metodo constructor, ya que inicializa al objeto """
item = Item()


""" PARTE 2: CREAR CLASES CON SUS ATRIBUTOS E INSTANCIARLAS Y EJECUTAR METODO """

class Item1:
    
    #constructor
    def __init__(self, nombre:str, precio:float, cantidad=0): 
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
       
    #metodo (porque esta dentro de la clase. Si esta fuera de la clase se llama funcion)
    def calcular_total_precio(self):
        return self.cantidad * self.precio

""" Instancia de clase Item1 """
item = Item1("Laptop", 5, "1")
print(item.calcular_total_precio())# invocacion de metodo desde el objeto creado a partir de la instancia de clase Item1



""" NOTAS:
    1. Para validar un campo de tipo entero no es necesario poner cantidad: int, porque python reconocer por defecto los 
        numeros enteros. Tambien, se puede usar una valor predeterminado, ejemplo: cantidad=0. Este valor se usara cuando
        no se pase algun valor y si se pasa un valor tomara el primero y no el que esta por defecto.
    
    
"""