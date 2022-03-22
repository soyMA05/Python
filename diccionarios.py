# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:37:38 2022

@author: MIANCAS
"""

#DICCIONARIOS>> sirven para definir y entender mucho mejor los datos de un objeto real o persona, usando clave y valor
#La ventaja de usar diccionarios es que se pueden extender mucho mas que las listas.

product={
    "name":"book",
    "quantity":3,
    "price":4.99
    }

person={
        "first_name":"Miguel",
        "last_name":"Castillo"
        }

#print(dir(person))

#OBTENER SOLO CLAVES DE UN DICCIONARIO
print(person.keys())

#OBTENER ITEMS (elementos con clave-valor) DE UN DICCIONARIO
print(person.items())


#VACIAR DICCIONARIO
person.clear()

#LISTA CON DICCIONARIOS
productos=[{"name":"book", "price":3.99, "stock":30, "author":"Miguel A."},
           {"name":"laptop", "price":805.99, "stock":20, "author":"Miguel A."}]


print(productos)














