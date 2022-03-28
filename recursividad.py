# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:46:16 2022

@author: MIANCAS
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
def factorial_recursivo(n):
    #caso base
    if n == 0 or n == 1:
        return n
    #case recursivo
    if n != 0 and n != 1:
        return n * factorial_recursivo(n - 1)

print(factorial_recursivo(5))
"""