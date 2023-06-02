# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:24:47 2022

@author: MIANCAS
"""

#SET: es una coleccion que es desordenada y no tiene indice.
#Se usa cuando no queremos ordenar los datos y agregarlo con libertad

colores={"amarillo","azul","rojo"}
#print(type(colores))
print(colores)
 
#BUSCAR ELEMENTO
print("rojo" in colores)

#AGREGAR
colores.add("violeta") #en tupla es append()

#ELIMINAR ELEMENTO
colores.remove("rojo")

#VACIAR SET
colores.clear()
print(colores)

#ELIMINAR variable de tipo de dato SET
del colores

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}
utensils.add("napkin")
dishes.update(utensils)
dinner_table =utensils.union(dishes)

for i in dinner_table:
    print(i)
