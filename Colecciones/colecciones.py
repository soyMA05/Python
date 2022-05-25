# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:13:10 2022

@author: miancastillo
"""

#COLLECTIONS: counter, namedtuple,OrderedDict, defaultdict, deque

"""
1. Counter: es un contenedor que almacena los elementos como claves de diccionario y sus
cuentas(numero de veces que se repite el elemento) como valores de diccionario.

from collections import Counter
a = "aabccddd"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())#tuplas con su clave valor
print(my_counter.most_common(2))#elementos de diccionario que mas se repite
print(my_counter.most_common(1)[0])#elemento la lista del diccionario que mas se repite
#llevar a una lista los elementos(claves) del diccionario
print(list(my_counter.elements()))
"""

"""
2. Namedtuple (tupla nombrada) son un tipo de objeto ligero y facil de crear similar a una estructura, permite 
crear subclases de tuplas donde el primer campo es la clase que se instancia y el segundo campo son los valores. 

from collections import namedtuple

Point = namedtuple('Point', ['x','y'])
punto = Point(4, 5)
print(punto) #imprime la clase Point, mostrando coordenadas asi x=4  y y=5.
print(punto.x, punto.y) #imprime unicamente los valores de las variables x y y.
"""

"""
3. OrderedDict (dictado ordenado): es como un diccionario normal que recuerda el orden en que se insertaron los 
elementos. 
Nota: ya no es muy usado porque desde la clase diccionario integrada en python >=3.7 se puede hacer eso.

from collections import OrderedDict
diccionario_ordenado = OrderedDict()
clave=" "#nombre
valor=""#edad
for i in range(3):
    clave = str(input("Ingrese su nombre: "))
    valor = int(input("Ingrese su edad: "))
    diccionario_ordenado[clave]=valor

print(diccionario_ordenado.items())#muestra el orden en que ingrese los elementos a diferencia de muestre por orden A-Z

"""

"""
4. DefaultDict (diccionario predeterminado): tendrá un valor predeterminado si la clave aun no se ha configurado.
Permite crear un diccionario poniendo valores como si fuera un lista. 
NOTA: UTIL PARA CREAR DICCIONARIOS DINAMICOS
"""
from collections import defaultdict

dic = defaultdict(int)#defino tipo de dato para el valor
dic['a']=1
dic['b']=2
dic['c']=3
print(dic)


"""
5. Deque(): permite agregar elementos en una lista ya sea desde la derecha o desde la izquierda, osea inicio o final.
"""

from collections import deque

listaD = deque()
listaD.append(1)
listaD.append(2)
listaD.append(3)
listaD.append(4)
listaD.appendleft(5)#agrega a la izquierda
print(listaD)


