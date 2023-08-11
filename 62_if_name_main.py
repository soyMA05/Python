"""
if __name__ == '__main__'

El intérprete de python establece "variables especiales", una de las cuales es __name__. 
Python asignará a la variable __name__ un valor de '__main__' si es el módulo inicial que se está ejecutando. 

RAZONES DE USO:
1. El módulo puede ejecutarse como un programa independiente.

2. 2. El módulo puede ser importado y utilizado por otros módulos.
"""

print(__name__) # imprime __main__

#ejemplo 1

#saludar
def hola():
    print("Hello!")

#ejecutar la funcion saludar
if __name__ == '__main__':
    hola()

#ejemplo 2
import saludar #revisar el archivo saludar
saludar.gritar()


"""
RESUMEN:

Con el condicional if __name__ == '__main__': se pueden crear librerias, modulos, etc, independientes y que a su vez 
facilitan su invocacion en otros programas para extender funcionalidad en los nuevos programas a desarrollar.

RECORDAR que los nombres de los modulos no deben empezar con numeros, si es posible hacerlo sin numeros, sino solo letras.
"""