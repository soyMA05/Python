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
        self.materias[codigo]= materia #aqui está el ENCAPSULAMIENTO porque agrego al diccionario materias de la clase Materia... 
        #que posteriormente su estructura no podrá ser modificado ya que se supone que tiene todos los atributos y métodos necesarios
        
class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombreMateria = nombre
        self.nombreProfesor = profesor
        #OCULTAMIENTO (Forma 1) de aqui para abajo
        #nuevo atributo que no puede ser anterior a 2006
        self.fechaInicioDictadoMateria = fecha # primero pasa por una validacion (los metodos de abajo) y luego se asigna
        
    @property # PROPERTY enmascara o envuelve un atributo dentro de una propiedad
    def fechaInicioDictadoMateria(self):
        #print("prueba que primero pasa por aqui para luego asignar")
        return self._fechaInicioDictadoMateria #atributo privado, es decir que esta protegido o que esta oculto
    
    #SETTER permite modificar o hacer la validación para luego confirmar la asignacion
    @fechaInicioDictadoMateria.setter
    def fechaInicioDictadoMateria(self, fecha):
        if fecha < 2006:
            self._fechaInicioDictadoMateria = 2006
        else:
            self._fechaInicioDictadoMateria = fecha
        
ingenieria = Carrera("Ingenieria")
algebra = Materia("Algebra", "Miguel Castillo", 2005)
fisica = Materia("Fisica", "Blanca Vargas",2022)
quimica = Materia("Quimica", "Esperanza Enriquez",2022)
print(algebra.nombreProfesor)

"""
ingenieria.materias.append((235, algebra)) #lista
ingenieria.materias.append((236, fisica))
ingenieria.materias.append((237, quimica))
print(len(ingenieria.materias))
print(ingenieria.materias)
print(algebra.nombreMateria)
"""
#ENCAPUSALAMIENTO
ingenieria.agregarMaterias(123, algebra)
print(ingenieria.materias)

# OCULTAMIENTO
print(algebra.fechaInicioDictadoMateria)