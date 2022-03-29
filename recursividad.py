# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:46:16 2022

@author: MIANCAS
"""

"""
def fibonacci(n):
    #caso base
    if n== 0 or n ==1:
        return n
    #caso recursivo
    if n !=0 and n !=1:
        return fibonacci(n-1) + fibonacci(n-2)     
print(fibonacci(3))
"""

"""
def factorial_recursivo(n):
    #caso base
    if n == 0 or n == 1:
        return n
    #case recursivo
    if n != 0 and n != 1:
        return n * factorial_recursivo(n - 1)

print(factorial_recursivo(5))
"""

"""
#EJERCICIO 1: Calcular la potencia de un numero
def potencia(b=3, e=3):
    if e == 0:
        print("CB1",b)
        return 1
    if b == 1 or b == 0:
        print("CB2",b)
        return b
    if e == 1:
        print("CB3",b)
        return b
    if e != 1:
        print("R",b)
        return b * potencia(b,e-1)
print("RPTA",potencia())
"""

"""
#EJERCICIO 2: SUmar los digitos de un numero entero
def suma_digitos(numero=23):
    #suma = 0
    #numero_str = str(numero)
    #for i in range(len(numero_str)):
    #    suma += int (numero_str[i])
    #return suma
    if numero == 0:
        return 0
    else:
        print(numero%10, numero//10)
        return numero % 10 + suma_digitos(numero//10)
    #if numero !=
print(suma_digitos())
"""

"""
#EJERCICIO 3: crear una funcion recursiva que permita sumar los elementos de una lista.
def suma_lista(lista):
    if len(lista)==0:
        return 0
    if len(lista)==1:
        return lista[0]
    if len(lista)>1:
        return lista[0]+ suma_lista(lista[1:])
lista = [1,2,3]
print(suma_lista(lista))
"""

"""
# EJERCICIO 4: crear una funcion recursiva que permita sumar los elementos de una lista mixta
#lista Mixta [13,4,[12],[[1]][]]

def suma_lista_mixta(lista):
    suma = 0
    for i in lista:
        if type(i) == type([]):
            suma += suma_lista_mixta(i)
        else:
            suma += i
    return suma

lista = [13,4,[12],[[1]],[]]
print(suma_lista_mixta(lista))
"""

nums = [1,-2,3,-4,-2,5,10]
def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num=num 
    return max_num    

print(find_max(nums))
    
