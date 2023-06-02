
#=========================================================
#   *args

"""
*args =que empaquetará todos los argumentos en una tupla útil 
para que una función pueda aceptar una cantidad variable de argumentos.
"""

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(5,23))

"""NOTA:
se puede poner cualquier nombre por args, lo importante es
poner el asterisco.
"""
def sueldo(*valores):
    total = 0
    valores = list(valores)
    for x in valores:
        total += x
    return total

sueldo_total= sueldo(20,15,30,15,25)
print(sueldo_total)

#=========================================================
#   **kwargs
"""
**kwargs = parametro que empaqueta todos los argumentos en un diccionario
útil para que una función pueda aceptar una cantidad variable de
argumentos de palabras clave.
"""

# funcion con dos palabras claves
def hello (first_name, last_name  ):
    print('Hello ' + first_name + ' ' + last_name)

hello("Miguel", "Castillo")

#funcion con varias palabras claves
def invitation(**kwargs):
    print("Bienvenido "+ kwargs['prof'] + ' ' + kwargs['nombre'] + ' ' + kwargs['apellido'])

invitation(prof="Ing.", nombre="Miguel", apellido="Castillo")

"""NOTA:
se puede poner cualquier nombre por kwargs, lo importante es
poner los asteriscos.
"""
def new_invitation(**datos):
    print('Hola', end=" ")
    for clave, valor in datos.items():
        print(valor, end=" ")

new_invitation(prof="Ing.", nombre="Miguel", apellido="Castillo")

