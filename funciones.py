# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 21:23:57 2022

@author: MIANCAS
"""

# =============================================================================
# DEFINCION Funciones: Bloque de código reutilizable que realiza una sola tarea especficia. 
# Las funciones sirven para evitar tareas repetitivas, y a su vez reduce la cantidad de código.
# =============================================================================

# =============================================================================
# #FORMA 1
# def hola():
#      print("Hola ")
# hola()
# =============================================================================


# =============================================================================
# #FORMA 2 con paso de parametros
# persona1 = "Miguel"
# persona2 = "Paula"
# def hola(nombre):
#     print("Hola " + nombre )
# 
# hola(persona1)
# hola(persona2)
# =============================================================================

# =============================================================================
# #FORMA 3: en el caso de que queramos hacer pruebas rapidas para medir su funcionalidad
# def hola(nombre="Miguel"):
#     print("Hola",nombre)
# 
# hola()
# =============================================================================

# FORMA 4: uso de return

def suma(numero1, numero2):
    total = numero1 + numero2
    return total
    #return numero1 + numero2

#print(suma(2, 5))
sumando = suma(2, 5) 
print(sumando)



