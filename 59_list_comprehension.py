""" 
comprensión de lista: 
- 1. es una forma de crear una nueva lista con menos sintaxis.
- 2. puede imitar a las funciones lambda 
- 3. Son fácil de leer.

ESTRUCTURA:
a. list= [(expression) for (item/element) in (iterable)]
b. list= [(expression) for (item/element) in (iterable) if (conditional)]
c. list= [(expression) (if/else) for (item/element) in (iterable)]

una expresion es la combinacion entre constantes, variables, funciones, operadores y operaciones, etc que son interpretadas para obtener algo.
"""

#ANTECEDENTE

#lista para almacenar el cuadrado de numero
squares = []

for i in range(1,11):
    squares.append(i*i)

print(squares)

#1. CON LIST COMPREHENSION
squares = [ i*i for i in range(1,11) ]
print(squares)


#2. 
# lista de notas, ver cuantos estudiantes tienen un puntaje mayor a 70
notas = [100, 60, 80, 90, 85, 71, 69, 50, 40, 20, 43]

#forma 1
estudiantes_pasados = list(filter((lambda nota: nota>=70),notas))
print(estudiantes_pasados)

#forma 2 con estructura b
estudiantes_pasados = [nota for nota in notas if nota >= 70]
print(estudiantes_pasados)

#forma 2 con estructura c
estudiantes_pasados = [nota if nota >= 70 else "REPETIR" for nota in notas]
print(estudiantes_pasados) # resultado = [100, 'REPETIR', 80, 90, 85, 71, 'REPETIR', 'REPETIR', 'REPETIR', 'REPETIR', 'REPETIR']

"""
RESUMEN:
La comprension de listas simplifican la manera de crear listas usando una sintaxis simple.
Manejan 3 tipos de estructuras. Tambien una manera de simular una lista comprendida es mediante list(funcion_a_operar())
"""