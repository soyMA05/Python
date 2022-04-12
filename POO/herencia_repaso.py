# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 22:25:23 2022

@author: MIANCAS
"""

#clase animal
class Animal:
    #atributos de clase
    PROPIEDAD = "RCUA"
    ESPECIE = "Mamifero"
    
    #metodo constructor
    def __init__(self, nombre, edad, peso):
        self.nombreAnimal = nombre
        self.edadAnimal = edad
        self.pesoAnimal = peso
        self.alimentosAnimal = []
    
    #metodos operativos
    def alimentos_animal(self, alimento):
        if alimento in self.alimentosAnimal == True:
            rpta = f"{alimento} Es uno de los alimentos preferidos"
            return rpta
        else:
            rpta = "No, sus alimentos favoritos son: "
            return rpta + str(self.alimentosAnimal)
    
    def dormir_animal(self):
        if self.edadAnimal > 1 :
            print("Duerme minimo 4 horas")
        if self.edadAnimal <= 1:
            print("Duerme minimo 10 horas")

#clase vaca 
class Vaca(Animal):
    SONIDO_HABLAR = "Mugir"
    
    def __init__(self, nombre, edad, peso, raza, estado, cantidad_produccion, etapa_preñez):
        self.razaVaca = raza
        self.estadoVaca = estado
        self.cantidadProduccion = cantidad_produccion 
        self.preñez = etapa_preñez
        super().__init__(nombre, edad, peso)
    
    def pastar(self):
        if self.cantidadProduccion > 10:
            print("Pasto Especial")
        else:
            print("Pasto Comun")
    
#clase perro
class Perro(Animal):
    SONIDO_HABLAR = "ladrar"
    
    def __init__(self, nombre, edad, peso, raza, altura):
        self.razaPerro = raza
        self.alturaPerro = altura
        super().__init__(nombre, edad, peso)
    
    def arrear(self):
        if self.razaPerro == "Chihuhua" or self.razaPerro == "Pastor":
            print("Perro arreador")
        else:
            print("Perro seguidor")
            

#Instancia 1: Vaca : vaca1
vaca1 = Vaca("Pulga", 4, 940, "Brown Swiss", "produccion", 15, 2)
print(type(vaca1))
print(vaca1.SONIDO_HABLAR)
vaca1.alimentosAnimal.extend(["Hierba","Taralla Maiz","Maiz","Caña dulce", "Platano","Sal mineral", "Melasa"])
consulta_alimento = vaca1.alimentos_animal("yuca")
print(consulta_alimento)
vaca1.dormir_animal()
vaca1.pastar()

#Instancia 1: Perro : perro1
perro1 = Perro("Dana", 1, 15, "chihuhua".capitalize(), 0.25)
print(type(perro1))
print(perro1.SONIDO_HABLAR)
perro1.alimentosAnimal.extend(["leche","balanceado","caldo"])
consulta_alimentoPerro = perro1.alimentos_animal("pan")
print(consulta_alimentoPerro)
perro1.dormir_animal()
perro1.arrear()