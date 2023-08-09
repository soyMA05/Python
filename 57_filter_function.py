""" 
filter(): crea una colección de elementos a partir de un iterable para el que devuelve una función.

ESTRUCTURA:
filter(function, iterable )
"""

#EJEMPLO

#lista de personas con edad para beber
friends = [("Samuel", 20),("Xavier",21),("Ana",17),("Robert",18),("Claudia", 19), ("Joe",16)]

#funcion para filtrar los datos
age = lambda data : data[1] >= 18

#obtener los mayores de edad, cuyos datos de personas mayores se guarda en una lista
mayores_edad = list(filter(age,friends))
print(type(mayores_edad))
for p in mayores_edad:
    print(p)

"""
RESUMEN:
La funcion filter() permite obtener ciertos que cumplan ciertos requisitos. Esos requisitos se hacen de acuerdo a funcion que uno
mismo debe escribir segun el criterio personal. SI NO HAY FUNCION NO HAY FILTRO.

Recordar que en Python cada funcion se maneja como un objeto, por lo que en este caso, se requeria de una lista para guardar 
los datos filtrados y asi poder mostrarlos. Aunque si no se ponia la lista igualmente aplicando directamente filter() en
el bucle se podia iterar cada elemento filtrado. """