# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:16:55 2022

@author: MIANCAS
"""

class Carrera:
    def __init__(self, nombre):
        self.nombreCarrera = nombre
        self.materias = {}
        #self.materias = [] #lista

    def agregarMaterias(self, codigo, materia):
        self.materias[codigo]= materia
        
class Materia:
    def __init__(self, nombre, profesor):
        self.nombreMateria = nombre
        self.nombreProfesor = profesor
        
ingenieria = Carrera("Ingenieria")
algebra = Materia("Algebra", "Miguel Castillo")
fisica = Materia("Fisica", "Blanca Vargas")
quimica = Materia("Quimica", "Esperanza Enriquez")
print(algebra.nombreProfesor)

"""
ingenieria.materias.append((235, algebra)) #lista
ingenieria.materias.append((236, fisica))
ingenieria.materias.append((237, quimica))
print(len(ingenieria.materias))
print(ingenieria.materias)
print(algebra.nombreMateria)
"""
ingenieria.agregarMaterias(123, algebra)
print(ingenieria.materias)