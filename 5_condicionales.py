# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 23:02:48 2022

@author: MIANCAS
"""
#datos
GRAMO = 1000
ONZA = 35.27
LIBRA = 2.205
TON = 0.001

#funciones
def kilogramo_gramo(cant):
    resultado = cant * GRAMO
    print("KG a Gr: ", resultado)
def kilogramo_onza(cant):
    resultado = cant * ONZA
    print("KG a Oz: ", resultado)
def kilogramo_libra(cant):
    resultado = cant * LIBRA
    print("KG a Lb: ", resultado)
def kilogramo_tonelada(cant):
    resultado = cant * TON
    print("KG a TON: ", resultado)

def opciones():
    cantidad = float(input("Ingrese una cantidad en KG: "))
    opc = int(input("Ingrese una opcion a transformar: \n1. KG a Gr  \n2. KG a Oz \n3.KG a Lb \n4. KG a Ton \n>>:"))
    if opc==1:
        kilogramo_gramo(cantidad)
    elif opc == 2:
        kilogramo_onza(cantidad)
    elif opc == 3:
        kilogramo_libra(cantidad)
    elif opc == 4:
        kilogramo_tonelada(cantidad)
    else:
        print("Opcion incorrecta, ha salido del programa... Gracias por visitarnos")

#ejecucion
opciones()    