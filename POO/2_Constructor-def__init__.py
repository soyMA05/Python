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
    #Atributo de clase
    tasa_de_pago = 0.8 #aplicar descuento del 20%
    all = []
    
    #constructor
    def __init__(self, nombre:str, precio:float, cantidad=0): 
        #Run validations to the received arguments(Ejecutar validaciones a los argumentos recibidos)
        assert precio > 0, f"El precio {precio} no es mayor a 0"
        assert cantidad >=0, f"La cantidad {cantidad} no es mayor a 0"
        
        # asignar a un objeto propio el valor de los atributos
        self.nombre = nombre
        self.precio = precio 
        self.cantidad = cantidad
        
        #atributo de clase para agregar objetos
        Item1.all.append(self) #self es la instancia que se crea y se va agregando a lista
       
    #metodo (porque esta dentro de la clase. Si esta fuera de la clase se llama funcion)
    def calcular_total_precio(self):
        return self.cantidad * self.precio
    
    #metodo para hacer descuento
    def aplicar_descuento(self):
        return self.precio * Item1.tasa_de_pago #forma correcta de hacer uso de atributos de clase
    
    #parte3.1: metodo responsable de representar objeto creado> [Clase(atributo1, atributo2), ...]
    def __repr__(self):
        return f"Item1({self.nombre}, {self.precio}, {self.cantidad})"
    

""" Instancia de clase Item1 """
item = Item1("Laptop", 5, 11)
print(item.calcular_total_precio())# invocacion de metodo desde el objeto creado a partir de la instancia de clase Item1

""" Formas de acceder atributos de clase """
print(Item1.tasa_de_pago)# a nivel de clase
print(item.tasa_de_pago) # a nivel de instancia
print(item.aplicar_descuento())


""" PARTE 3: SOLUCION AL PROBLEMA DE CREAR VARIOS TIPOS DE ARTICULOS/ITEMS """
item1 = Item1("TV", 200, 1)
item2 = Item1("PC", 700, 1)
item3 = Item1("Laptop", 1200, 1)
item4 = Item1("Mouse", 20, 1)
item5 = Item1("Keyboard", 20, 1)

print(Item1.all)#imprimo todos los objetos creados que estan en la lista usando el metodo __repr__


#es util si solo queremos filtrar informacion de todos los objetos creados
for i in Item1.all:
    print(i.nombre)

""" NOTAS:
    1. Para validar un campo de tipo entero no es necesario poner cantidad: int, porque python reconocer por defecto los 
        numeros enteros. Tambien, se puede usar una valor predeterminado, ejemplo: cantidad=0. Este valor se usara cuando
        no se pase algun valor y si se pasa un valor tomara el primero y no el que esta por defecto.
    
    2. assert permite validar los argumentos que se recibe y tambien permite recuperar los errores antes de que se ejecute
        el resto del programa.
        
"""