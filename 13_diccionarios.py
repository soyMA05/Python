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

print(dir(person))

#OBTENER SOLO CLAVES DE UN DICCIONARIO
print(person.keys())

#OBTENER ITEMS (elementos con clave-valor) DE UN DICCIONARIO
print(person.items())


#VACIAR DICCIONARIO
person.clear()

#UPDATE 
capitals = {'USA':"Washigton DC",
            'India':'New Dehli',
            'China': 'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})#actualizo diccionario
print(capitals.get('Germany')) #obtengo valor a partir de clave

capitals.pop('China')#elimino un elemento del dicc a partir de la clave
print(capitals.items())

#LISTA CON DICCIONARIOS
productos=[{"name":"book", "price":3.99, "stock":30, "author":"Miguel A."},
           {"name":"laptop", "price":805.99, "stock":20, "author":"Miguel A."}]

print(productos)


# ASIGNO VALOR EN UNA CLAVE O ACTUALIZO VALOR
#declaro diccionario vacio
computadoras = {}
"""nombreDiccionario[clave] = valor"""
computadoras[123]="DELL"#Esta forma se utiliza para asignar un valor a una clave de diccionario o para actualizar su valor
print(computadoras)



#EJERCICIO: Agregar diccionarios a una Lista

registro_clientes = {}
lista_clientes = []
clv_nombre = "Nombre"
clv_edad = "Edad"

num_clientes = int(input("Ingrese la cantidad de clientes a registrar: "))

for i in range(num_clientes):
    nombre = input(f'Ingrese el nombre del cliente {i+1}: ')
    edad = int(input(f'Ingrese la edad del cliente {i+1}: '))
    registro_clientes={clv_nombre:nombre, clv_edad:edad}
    #registro_clientes[clv_nombre]= nombre #Al utilizar asi se actualizan los valores (Nota: Revisar encapsulamiento_y_ocultamiento.py)
    print(registro_clientes.items())#muestra valores por cada diccionario
    lista_clientes.append(registro_clientes)
    
print("Clientes registrados: ")
for i in lista_clientes:
    print(i["Nombre"],'-',i['Edad'])
    







