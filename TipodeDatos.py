# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:04:38 2022

@author: MIANCAS
"""

#Strings
print("Hola Mundo")
print('Hola Mundo')
print('''Hola Mundo''')
print("""Hola Mundo""")

#para ver el tipo de dato que es
print(type("Hola Mundo"))

#concatenar cadenas
print("Hola " + "Miguel")

#Integer o Entero
print(5+23)

#Float o Decimal
print(23.5)

#Boolean o Booleanos
False
True
print(type(False))

#List o Listas: se puede colocar cualquier tipo de dato. Se usan cuando queremos cambiar el valor de los elementos a lo largo del uso de la app..
[10,20,30, False, "Miguel", 23.3, 5+3]
[]#lista vacia
print(type([10,20,30]))
print([10,20,30, False, "Miguel", 23.3, 5+3])


#Tuples o Tuplas: se usan en datos que no cambian. En si es una lista que no puede cambiar una vez ya definida.
(10,20,30)
()#tupla vacia
print(type((10, 20, 30, False)))
print(20,15,False)


#Dictionary o Diccionarios: es una colecccion que sirve para agrupar diferentes tipos de datos, usando clave(nombre campo) y valor. En NoSQL un documento esta compuesto de colecciones que son cada uno de los datos que pertenece a un usuario u otro objeto..
{"nombre": "Miguel",
 "apellido":"Castillo",
 "edad":23}
print(type({"nombre": "Miguel", "apellido":"Castillo",
 "edad":23}))
print({"nombre": "Miguel", "apellido":"Castillo", "edad":23})

#None o ninguno
None
print(None)
print(type(None))





