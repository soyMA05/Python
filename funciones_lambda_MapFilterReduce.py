# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 21:23:56 2022

@author: MIANCAS
"""

# =============================================================================
# FUNCIONES LAMBDA
# Son funciones anónimas que toman un numero de argumentos pero que estas solo
# pueden ser escritas utilizando  una sola expresion.
# =============================================================================

suma = lambda numero1, numero2: numero1 + numero2
print(suma(5, 18)) 

doble = lambda numx: numx**2
print(doble(5))

####FILTER(): obtiene elementos que cumplen condiciones escritas
#Ejercicio > quiero obtener los numeros que multiplicados por dos sean mayores a 10 
data = [1,2,3,4,5,6,7,8,9,10]

filtro_data = list(filter(lambda n: n*2>10, data))
print(filtro_data)


###MAP(): itera sobre todo los elementos de una lista
#Ejercicio > quiero obtener el cuadrado de todos los elementos de la lista data
cuadrado_data = list(map(lambda n: n**2, data))
print(cuadrado_data)


###REDUCE(): reduce una lista con las operaciones que se escriban
#Ejercicio > reducir la lista data en una sola suma de cada elemento restado - 2
import functools as ft
data_reduce = ft.reduce(lambda x, y: x +(y-1), len(data))#x es la variable que almacena, y itera pero no considera el ultimo elemento
print(data_reduce)

