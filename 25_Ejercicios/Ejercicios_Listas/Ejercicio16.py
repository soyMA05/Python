  # -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:39:30 2022

@author: MIANCAS
"""
# =============================================================================
# EJERCICIO 16: Queremos desarrollar una aplicación que nos ayude a gestionar las
#  notas de un centro educativo. Cada grupo (o clase) está compuesto por 5 alumnos.
#  Se pide leer las notas del primer, segundo y tercer trimestre de un grupo. 
#  Debemos mostrar al final: la nota media del grupo en cada trimestre, y la 
#  media del alumno que se encuentra en la posición N (N se lee por teclado). 
# =============================================================================
notas_parcial1 = []
notas_parcial2 = []
notas_parcial3 = []

#ingreso de notas 
print("***PARCIAL 1***")
for i in range(5):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: ")) 
    while nota < 0 or nota > 20:
        nota = float(input(f"Ingrese correctamente la nota del estudiante {i+1}: ")) 
    notas_parcial1.append(nota)

print("***PARCIAL 2***")
for i in range(5):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: ")) 
    while nota < 0 or nota > 20:
        nota = float(input(f"Ingrese correctamente la nota del estudiante {i+1}: ")) 
    notas_parcial2.append(nota)

print("***PARCIAL 3***")
for i in range(5):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: ")) 
    while nota < 0 or nota > 20:
        nota = float(input(f"Ingrese correctamente la nota del estudiante {i+1}: ")) 
    notas_parcial3.append(nota)

#registrar notas
print("Nro. Estudiante \tParcial 1 |\tParcial 2 |\tParcial 3 ")
k= 1
for parcial1, parcial2, parcial3 in zip(notas_parcial1, notas_parcial2, notas_parcial3):
    print(f"\t{k} \t\t\t\t\t{parcial1} \t\t{parcial2} \t\t{parcial3} ")
    k += 1

#media de cada parcial y trimestral
suma_notasParcial1 = 0
suma_notasParcial2 = 0
suma_notasParcial3 = 0
for i in range(5):
    suma_notasParcial1 += notas_parcial1[i]
    suma_notasParcial2 += notas_parcial2[i]
    suma_notasParcial3 += notas_parcial3[i]

media_parcial1 = suma_notasParcial1 / 5
media_parcial2 = suma_notasParcial2 / 5
media_parcial3 = suma_notasParcial3 / 5

media_trimestre = (media_parcial1 + media_parcial2 + media_parcial3) / 3 

print(f"Promedio parcial 1: {media_parcial1}")
print(f"Promedio parcial 2: {media_parcial2}")
print(f"Promedio parcial 3: {media_parcial3}")
print(f"Promedio trimestral: {media_trimestre}")

#promedio de estudiante  N
salir = 1
while salir != 0:
    numero_estudiante = int(input("Ingrese el numero de lista (1 - 5) del estudiante: "))
    while numero_estudiante < 1 or numero_estudiante >5:
        numero_estudiante = int(input("Ingrese el numero de lista (1 - 5) del estudiante: "))
    estudiante_lista = numero_estudiante - 1
    
    j = estudiante_lista
    while j == estudiante_lista:
        estudiante_notas = notas_parcial1[j]
        estudiante_notas += notas_parcial2[j]
        estudiante_notas += notas_parcial3[j]
        j +=1
    
    promedio_estudiante = estudiante_notas / 3
        
    print(f"\nPromedio estudiante Nro. {numero_estudiante}: {promedio_estudiante}")
    
    salir = int(input("¿Desea revisar otros promedios?: \n1. SI: 0. NO \n>>>>: "))
    
    