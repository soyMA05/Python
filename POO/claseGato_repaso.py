# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 21:19:14 2022

@author: MIANCAS
"""

class Gato:
    ESPECIE = "mamifero"
    
    def __init__(self, nombre, edad, alimento):
        self.nombre = nombre
        self.edad = edad
        self.alimentos = alimento
    
    def etapa_vida(self):
        if self.edad > 1:
            print(self.nombre, "es adulto")
        else:
            print(self.nombre, "es cachorro")
    
    def alimento_favorito(self, alimento_u):
        if alimento_u == self.alimentos:
            return True
        else:
            return False

#pregunto que especie son los gatos
print("Los gatos es una especie:", str(Gato.ESPECIE).upper())

#instancia un gato
gato1 = Gato("Michu", 1, "leche")
print( gato1.nombre, "\n", gato1.edad, "\n", gato1.alimentos )

#etapa de vida
gato1.etapa_vida()

#es su alimento favorito
consulta_alimento = gato1.alimento_favorito(input("Ingrese un alimento de gatos: ").lower())
if consulta_alimento == True:
    print("El " + gato1.alimentos + " es su alimento favorito".upper())
else:
    print("El " + gato1.alimentos + " no es su alimento favorito".upper())

#agrego atributo
gato1.genero = "Macho".lower()
print(gato1.genero)

#cambio valores del constructor
nombre_antiguo = gato1.nombre
gato1.nombre = "Kiko"
print("El gato "+ nombre_antiguo + " ahora se llama " + gato1.nombre )

print(dir(gato1))
