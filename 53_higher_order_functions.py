"""
Funciones de Orden Superior: son funciones que...
1. Aceptan como argumento otra funcion.
        ó
2. Retornan una funcion.

Nota: en python las funciones son tratadas como objetos.
"""

#gritar o hablar en voz alta
def laud(text):
    return text.upper()

#decir en voz baja
def quiet(text):
    return text.lower()

#para decir hola, hay dos funciones que se pueden utilizar, decir hola en voz alta o en voz baja
def hello(function):
    text = function("Hola")#retorna una valor de una de las funciones a utilizar y se asigna a text
    print(text)#devuelve o muestra text

#invocamos las funciones, sobre todo la funcion de orden superior que recibe como argumento otra funcion
hello(laud) #se pasa como argumento la variable(de funcion a variable) laud
hello(quiet)



#OTRO EJEMPLO

""" 
dividendo  / divisor  = cociente
10 / 2 = 5
"""
#recibe como parametro un numero que es el divisor
def divisor(x):
    #recibe el dividendo
    def dividendo(y):
        #retorna el cociente, valor que devuelve la funcion dividendo
        return y / x
    #retorna resultado de la funcion dividendo (funcion a variables)
    return dividendo

#invoco la funcion divisor y le paso como argumento un nro, pero esta funcion retorna otra funcion llamada dividendo que a su vez tambien admite un nro como argumento,
dividir = divisor(2)#entonces la nueva variable que es dividir, se le asigna la funcion dividendo
print(dividir(10)) #divisor retorna la funcion dividendo, la funcion dividendo retorna el resultado de la operacion

"""
Resumen: 
Las funciones de orden superior se caracterizan por al menos uno de los dos aspectos; primero, aceptan como argumento otra funcion O segundo, retornan siempre
otra funcion. Para el primer ejemplo, se pasas como argumento una funcion, en el segundo ejemplo se hace retornar una funcion, esa funcion esta asignada 
en una nueva variable, la variable retorna un valor de la funcion por la cual fue igualada.
"""

