# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:22:50 2022

@author: MIANCAS
"""

class Gato:
    #atributos de clase o estaticos
    ESPECIE = "mamífero"
    SONIDO = " miau"
    
    #atributos de instancia / metodo constructor
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.alimentos = []#ingreso de alimentos
    
    #etapa de vida de gato
    def etapa_vida(self):
        if self.edad > 1 :
            print(self.nombre, " es adulto".upper())
        else:
            print(self.nombre, " es cachorro".upper())
    
    #consulta alimento favorito
    def alimento_favorito(self, alimento_u):
        return alimento_u in self.alimentos #devuelve T o F
    
    #animo instancia Gato
    def estado_animico(self, cant_maullidos):
        if cant_maullidos == 1:
            print(self.nombre + " quiere jugar")
        if cant_maullidos == 0:
            print(self.nombre + " esta dormido")
        if cant_maullidos >= 2:
            i = 0
            maullidos = ""
            while i < cant_maullidos:
                maullidos += self.SONIDO
                i += 1
            print(self.nombre + " dice "+ maullidos +" porque tiene hambre")
    
    def jugar(self, jugar_u):
        if jugar_u == True:
            estado_jugar = "contento"
            return estado_jugar
        else:
            estado_jugar = "te va aruñar si no juegas"
            return estado_jugar

#informacion basica de los gatos
print("los gatos son " +Gato.ESPECIE + " y dicen " + Gato.SONIDO)

#INSTANCIA 1: gato1        
gato1 = Gato("Michu", 2, "Macho")
gato1.alimentos.extend(['leche','pescado', 'galleta', 'croqueta'])
gato1.etapa_vida()
consulta_alimento = gato1.alimento_favorito(input(f"Ingrese un alimento que le podria gustar a {gato1.nombre}: ").lower())
if consulta_alimento == True:
    print("SI, sus comidas favoritas son: " + str(gato1.alimentos))
else:
    print("NO, sus comidas favoritas son: " + str(gato1.alimentos))

numero_maullidoGato1 = int(input(f"Ingrese un numero de maullidos mayor o igual a 0 para {gato1.nombre}: "))
while numero_maullidoGato1 < -1:
    numero_maullido = int(input(f"Ingrese correctamente un numero de maullidos mayor o igual a 0 para {gato1.nombre}: "))
    
gato1.estado_animico(numero_maullidoGato1)

#pregunto al usuario si quiere jugar con gato1
if numero_maullidoGato1 == 1:
    usuario_jugar = int(input(f"¿Quieres jugar con {gato1.nombre}? \t1. SI \t2. NO: "))
    while usuario_jugar < -1 or usuario_jugar > 2:
        usuario_jugar = int(input(f"Decida bien..¿Quieres jugar con {gato1.nombre}? \t1. SI \t2. NO: "))
    jugar_gato1 = gato1.jugar(usuario_jugar)
    print(gato1.nombre + " " + jugar_gato1)

#============================================
#INSTANCIA 2: gato2
gato2 = Gato("Polo", 1, "Macho")
gato2.alimentos.extend(['leche','pescado'])
numero_maullidoGato2 = int(input(f"Ingrese un numero de maullidos mayor o igual a 0 para {gato2.nombre}: "))
while numero_maullidoGato2 < -1:
    numero_maullidoGato2 = int(input(f"Ingrese correctamente un numero de maullidos mayor o igual a 0 para {gato2.nombre}: "))
    
gato2.estado_animico(numero_maullidoGato2)
#pregunto al usuario si quiere jugar con gato1
if numero_maullidoGato2 == 1:
    usuario_jugar = int(input(f"¿Quieres jugar con {gato1.nombre}? \t1. SI \t2. NO: "))
    while usuario_jugar < -1 or usuario_jugar > 2:
        usuario_jugar = int(input(f"Decida bien..¿Quieres jugar con {gato1.nombre}? \t1. SI \t2. NO: "))
    jugar_gato2 = gato2.jugar(usuario_jugar)
    print(gato1.nombre + " "+ jugar_gato1 + " y " + gato2.nombre + " "+ jugar_gato2)
else:  
    print(gato1.nombre + " y " + gato2.nombre + "estan dormidos o se fueron a cazar")