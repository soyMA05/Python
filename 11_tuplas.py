# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:53:32 2022

@author: MIANCAS
"""
#Tuplas es un conjunto de elementos que se usan para definir un solo tipo de datos que no van a cambiar, es decir, que son inmutables.

t=(1) #NO es una tupla
t2=(1,) #tupla de un solo elemento
x=(10,20,30,40,50)#tupla de varios elementos
#print((x))


#CONSTRUCTOR O FUNCION PARA CREAR UNA TUPLA
tupla=tuple((1,2,3,4))
#print(tupla)


#ACCEDER A ELEMENTOS DE LA TUPLA
#print(x[0])

#BUSCAR ELEMENTO
#print(10 in x)

#ELIMINAR UNA TUPLA 
#del x
#print(x)



#DICIONARIO 

#creacion de diccionario de localizacion con aplicacion de tupla
locations={ #un diccionario no puede tener elementos con las mismas claves
    (35.12312, 39.000):"Tokio",
    (36.12312, 45.000):"Quito"
    }
