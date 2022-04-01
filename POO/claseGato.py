# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:25:57 2022

@author: MIANCAS
"""

class Gato:
    #Atributo de clase (otorga el mismo valor a cada instancia de la clase)
    especie = "Mamifero"
    
    #metodo constructor
    #Atributos de instancia (para cada uno de los objetos de tipo gato que se 
    #instancie va a tener diferentes valores, es decir cada gato con sus respectivos valores)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.alimentos = []
    
    #etapa de vida
    def etapa_vida(self):
        if self.edad > 1:
            print(self.nombre, "es adulto")
        else:
            print(self.nombre, "es cachorro")
            
    def esAlimento_Favorito(self, alimento):
        return alimento in self.alimentos
        
    
gato = Gato("Michu", 1)
gato.etapa_vida()

"""
for i in range(3):
    gato.alimentos.append(input(f"{i+1} Ingrese un alimento de gato: "))

comida = gato.esAlimento_Favorito("galleta")
print("Es su comida favorita: ",comida)
print(gato.alimentos)
"""
# =============================================================================
# AGREGAR UN NUEVO ATRIBUTO
# gato.raza = "Siames"
# print(gato.raza)
# =============================================================================

#USO DE ATRIBUTO CLASE
#instanciando un objeto
print(gato.especie)

#llamando a la clase directamente
print(Gato.especie)