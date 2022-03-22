# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:52:09 2022

@author: MIANCAS
"""

def notas_puntaje(opc):
    notas = {
        1:"Insuficiente",
        2:"Insuficiente",
        3:"Insuficiente",
        4:"Insuficiente",
        5:"Insuficiente",
        5:"Insuficiente",
        7:"Suficiente",
        8:"Bien",
        9:"Notable",
        10:"Sobresaliente",
        }
    return notas.get(opc, "Nota inválida")

#entrada
opcion=int(input("Ingrese una calificacion: "))
print(notas_puntaje(opcion))