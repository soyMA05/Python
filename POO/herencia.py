# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:21:55 2022

@author: MIANCAS
"""
#CLASE EMPLEADO (SuperClase)
class Empleado:
    NACIONALIDAD = "Ecuatoriana"
    
    def __init__(self, nombre, edad, legajo, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.legajo = legajo
        self.sueldo = sueldo
    
    def calcularSueldo(self, descuentos, bonos):
        return self.sueldo - descuentos + bonos

    def etapa_vida(self):
        if self.edad >= 18 and self.edad <= 30:
            print("El sr(a)." + f"{self.nombre}".upper() + " es Adulto Joven")
        if self.edad >= 31 and self.edad <= 50:
            print("El sr(a). " + f"{self.nombre}".upper()+ " es Adulto ")
        if self.edad >= 51 and self.edad <= 60:
            print("El sr(a)." + f"{self.nombre}".upper()+ " es Super Adulto ")
        
#CLASE AGENTE VENTAS (Subclase)
class AgenteVentas(Empleado):#llamada a clase padre

    def __init__(self, nombre, edad, legajo, sueldo, codigoMostrador): #parametros de clase padre y luego clase hija 
        self.numeroMostrador = codigoMostrador
        super().__init__(nombre, edad, legajo, sueldo)#inicializo atributos de clase padre

#CLASE TRIPULANTE (Subclase)
class Tripulante(Empleado):
    NIVEL = "Bachiller"
    def renovarLicencia(self):
        if self.edad < 50:
            print("Debe renovar su licencia de conducir cada año")
        else:
            print("Debe renovar su licencia de conducir cada 6 meses")

#INSTANCIA 1: Agente ventas : agente1
agente1 = AgenteVentas("Miguel", 23, "MA05", 1400, 230001)#se debe pasar parametros de clase padre, luego clase hija
sueldo = agente1.calcularSueldo(100, 2000)
agente1.etapa_vida()
print(sueldo)

#Instancia 1: Tripulante: tripulante1
tripulante1 = Tripulante("lucas", 24, "LUC23", 1500)#se debe pasar parametros de clase padre, porque clase hija no tiene metodo constructor
tripulante1.renovarLicencia()
print(tripulante1.NIVEL)