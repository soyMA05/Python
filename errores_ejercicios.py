# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:41:51 2022

@author: MIANCAS
"""
#variables
resultado = 0
#funcion division
def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print(e, " No se puede dividir entre 0")
        return 123
    
#entrada
n1 = int(input("Digite un numero: "))
n2 = int(input("Digite otro numero: "))
rspt = division(n1, n2)

while rspt == 123:
    n1 = int(input("Digite un numero: "))
    n2 = int(input("Digite otro numero: "))
    rspt = division(n1, n2)

print("Rpta",rspt)
    
