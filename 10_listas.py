# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 16:35:38 2022

@author: MIANCAS
"""
datos=["Miguel", 23, True, [5,11,98]]
colores=["amarillo", "azul", "rojo", "rojo", "caqui"]


#CONSTRUCTOR O FUNCION PARA CREAR LISTAS list()
#crear lista con tupla se usa cuando queremos solo tener el mismo tipo de dato
mylist=list((5,23,8))
print(sum(list(range(0,101,2))))
#print(type(mylist))
print(type("azul" in colores))

#RANGE toma dos parametros de donde a donde va tomar determinado elemento
r=list (range(1,100)) #imprime del 1 al 9
print(r)

r2=list(range(4)) #lista de 4 elementos del 0 al 3
print(r2)


#numero de elementos en lista o longitud de lista
print(len(colores)) #propiedad

#BUSCAR
print(colores[1])#imprime valor en esa posicion
#SABER SI un elemento esta en la lista 
print("green" in colores) #propiedad

#encontrar la posicion de un elemento
print(colores.index("rojo")) #metodo

#contar cuantas veces se encuentra el mismo elemento en la lista
print(colores.count("rojo"))  #metodo

#CAMBIAR VALORES EN LISTA
print(colores)
colores[1]="verde"
print(colores)




#AGREGAR
#AGREGAR NUEVO ELEMENTO A LA LISTA
colores.append("celeste")#agrego un solo elemento, (lista o tupla)
print(colores)

#AGREGAR MAS DE UN ELEMENTO A LA LISTA
colores.extend(['cafe','rosado'])
print(colores)

#INSERTAR UN ELEMENTO EN UNA POSICION DADA
colores.insert(1, "marrow")

#colores.insert(-1, "marrow") #inserta un elemento en la penultima posicion

#insertar un elemento en la ultima posicion de la lista
colores.insert(len(colores), "morado")
print(colores)



#QUITAR UN ELEMENTO DE LA LISTA
colores.pop() #POP quita elementos por indices o quita el ultimo la lista si no tiene un indice. si se ejecuta 2 veces seguidas quita a los 2 ultimos
print(colores)

#quitar un elemento por indice 
colores.pop(1)
print(colores)

#colores.remove('amarillo')#elimino un elemento por nombre o valor
print(colores)

#VACIAR TODA LA LISTA
colores.clear()
print(colores)




#ORDENAR LISTAS

#sort para ordenar de A-Z o de forma creciente en numeros para no estar usando bloques de codigo con while o for para ordenar de forma manual
colores.sort()
print(colores)

#ordena de manera Z-A o de forma decreciente en numeros
colores.sort(reverse=True)
print(colores)

#ordenar de manera inversa los ultimos son primeros y los primeros son ultimos
colores.reverse() 
print(colores)




#CONCATENACION DE LISTAS
lista_concatenada = colores + datos
print(lista_concatenada)

#ACTUALIZACION DE DATOS USANDO SLICING [:]
lista_concatenada[:2]=['negro','blanco']
print('Lista actualizada: ',lista_concatenada)

# 2D = LISTA DE LISTAS
# Ejemplo 1:
fila1=[1,2,3]
fila2=[4,5,6]
fila3=[7,8,9]
matriz=[fila1,fila2,fila3]
print(matriz[1][1:]) #sin pandas

# Ejemplo 2
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]
foods = [drinks, dinner, dessert]
print(foods[2][0])


import pandas as pd
matriz_pd = pd.DataFrame(matriz,
                         columns = ["Columna 1","Columna 2","Columna 3"])
print(matriz_pd)

print(matriz_pd[1:2])
#seleccionar fila con pandas
print(matriz_pd.iloc[1][1:])#con pandas



"""
#EJERCICIO: Dadas dos listas, se debe generar una tercera lista con todos los elementos que se repiten entre ellas
pero no se debe repetir ningun elemento en la nueva lista. 
"""
lista1 = ['M','i', 'a','m','i','g','o', 'E','l','o','n']
lista2 = ['T','u', 'a','m','i','g','u','i','t','o']
lista3 = []

for letra in lista1:
    if letra in lista2 and letra not in lista3:
        lista3.append(letra)
print(lista3)