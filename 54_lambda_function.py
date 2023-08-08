""" 
Función lambda: función escrita en una línea utilizando la palabra clave lambda acepta cualquier número de argumentos,
pero sólo tiene una expresión.

Piense en ella como un atajo. Son útiles para: 
1. un solo uso(algo simple que se necesite sin hacer tanto codigo) 
 ó
2. si se necesita durante un corto período de tiempo y luego se puede desechar.

ESTRUCTURA DE LA FUNCION LAMBDA:
variable = lambda parametro : expresion
"""

#EJEMPLO 
#antecendente
def double(x):#obtener el doble de un numero, se declara el parametro x
    return x * 2#expresion
print(double(5))

#Ahora con Lambda 
#es la misma funcion anterior, solo que la sobreescribimos
double = lambda x:x*2
print("Funcion Lambda: ",double(5))

#multiplicar
multiply = lambda x,y: x*y
print(multiply(5,6))

#sumar
add = lambda x, y, z : x + y + z
print(add(5,6,7))

#nombres completos
full_name = lambda first_name, last_name : first_name + " " + last_name
print(full_name("soy","MA"))

#comprobar edad
age_check = lambda age: True if age >= 18 else False
print(age_check(17))


#experimento lambda + walrus
edad =18
if (age_check := lambda edad: True if edad >= 18 else False) != False: #compara edad, se le asigna True o False a age_check, devuelve ese valor y compara con False
    print("Mayor de edad")


"""
RESUMEN:
Las funciones lambda simplifican la escritura de codigo y son utilices para tareas cortas o para no escribir una funcion que despues
no se la utilizara. Esta funcion esta bien utilizada SI SOLO TIENE UNA EXPRESION. Si contiene mas de una expresion puede que nos estemos
complicando y es mejor escribir una funcion normal. Es decir, si se le agrega una expresion con un control de flujo muy largo y estamos
teniendo problemas para hacerla funcionar es mejor no hacerla. Es importante recordar que el NRO DE PARAMETROS NO IMPORTA.
"""