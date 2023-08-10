"""
reduce(): aplica una función a un iterable y lo reduce a un único valor acumulativo.

    Realiza la función en los dos primeros elementos y repite el proceso hasta que queda 1 valor.
ESTRUCTURA 
reduce(funcion, iterable)
"""


#lista de letras
letters = ["H","E","L","L","O"]


#trabajr con funciones de orden superior (en otros lenguajes puede ser recursividad) practicamente llama nuevamente a la misma funcion
import functools
word = functools.reduce((lambda x,y: x + y), letters)

print(word)


""" 
RESUMEN
Esta funcion reduce a un unico valor los elementos que se almacenan sobre un iterable (lista, tupla, etc).
Toma los dos primeros elementos, los suma, luego, toma la suma mas el tercer elemento original de la lista y los suma, luego
la suma de los tres primeros elementos y lo suma más el cuarto elemento y asi hasta llegar al último elemento y quedar
con unico valor.

OJO dependiendo del contexto, tambien se lo puede hacer con un bucle.
"""