# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:28:29 2022

@author: MIANCAS
"""
#Existen dos tipos de datos numericos. Integer y Float. Tambien existen numeros imaginarios para aplicaciones cientificas

#OPERACIONES
#suma y resta
#print(2+3-1)

#elevar al cubo
#print(2**3)

#operador de modulo que devuelve el cociente con flotante
#print(3/2)

#operador de modulo que devuelve el cociente con parte entera
#print(3//2)

#operador de modulo que devuelve residuo 
#print(4%2)


#EJERCICIOS CON OPERADORES
#1
#edad = input("Ingrese su edad: ") #toda entrada es un dato de tipo string
#nueva_edad= int(edad)+1 #se debe convertir a entero o float para hacer operaciones
#print( "Su edad es: ")
#print(nueva_edad)

#2
#IVA = 0.12

#nombre_Producto= input("Ingrese el nombre del producto: ")
#precio, cantidad = input("Ingrese el precio del producto " + nombre_Producto.upper() +": "),input("Cantidad: ")

#subtotal=float(precio)* int(cantidad) #subtotal es float
#total= (subtotal*IVA)+subtotal #total es float
#print(precio)
#print(type(subtotal))
#print(type(total))
#print("Total a pagar: ")
#print(total)



#3
nota_P1,nota_P2,nota_P3=input("Ingrese la nota del primer parcial: "),input("Ingrese la nota del segundo parcial: "),input("Ingrese la nota del tercer parcial: ")

promedio=(float(nota_P1)+float(nota_P2)+ float(nota_P3))/3
print(type(promedio))

print("Promedio es: ")
print(promedio)

