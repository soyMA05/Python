# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 22:24:21 2022

@author: MIANCAS
"""

# =============================================================================
# EJERCICIO 15: Dadas las edades y alturas de 5 alumnos, mostrar la edad y la estatura media,
# la cantidad de alumnos mayores de 18 años, y la cantidad de alumnos que miden más de 1.75.
# =============================================================================

#variables
MAYOREDAD = 18
ESTATURAM = 1.75
suma_edad = 0
suma_estatura = 0
contador_alumnosMayor18 = 0
contador_alumnosEstatura175 = 0


#ingreso de datos
for i in range(5):
    edad = int(input(f" Ingrese la edad del alumno {i+1}: "))
    estatura = float(input(f" Ingrese la estatura del alumno {i+1}: "))
    suma_edad += edad
    suma_estatura += estatura
    if edad >= MAYOREDAD:
        contador_alumnosMayor18 += 1
    if estatura >= ESTATURAM:
        contador_alumnosEstatura175 += 1

#medias
suma_edad = suma_edad/ 5
suma_estatura = suma_estatura / 5
print("Edad media: ", suma_edad)
print("Estatura media: ", suma_estatura)
print("Estudiantes mayores de 18 años: ",contador_alumnosMayor18)
print("Cantidad alumnos mayores a 1.75: ", contador_alumnosEstatura175)