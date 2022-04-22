# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:30:20 2022

@author: MIANCAS
"""
#------------------------------------------------------------------------------

class Animal:
    ESPECIE = "Mamifero"
    PROPIETARIO = "RCUA"
    def __init__(self, nombre, edad, peso, raza):
        self.nombreAnimal = nombre
        self.edadAnimal = edad
        self.pesoAnimal = peso
        self.fechaNacimiento = ""
        self.razaAnimal = raza
        self.enfermedad = ""
        self.tratamiento = ""
    
    def mugir(self):
        print("Muu-mee")
    
    def comer(self, alimento):
        print('Esta comiendo', alimento)
    
    def dormir(self, lugar):
        return 'Esta durmiendo en: ', lugar
    

#------------------------------------------------------------------------------

class Vaca(Animal):
    def __init__(self, nombre, edad, peso, raza, estado, tetas, partos, observacion):
        self.estadoProduccion = estado
        self.listaCantidad_produccion = []
        self.numero_tetas = tetas
        self.listaAlimentos_vaca = []
        self.listaFechaPartos= []
        self.numero_partos = partos
        #cuando la vaca recien se reincorpora al grupo debera copiar los datos
        self.listaPreniez_toros = []
        self.listaPreniez_fechas = []
        self.nombrarTerneros = {}#encapsulamiento
        self.listaTerneros = []
        self.observacion = observacion
        super().__init__(nombre, edad, peso, raza)
    
            
    #aplicar encapsulamiento
    def agregarTernero(self, nombreTernero, nombrePadreToro):
        if nombrePadreToro == 'desconocido':
            nombreTernero = {"Nombre: ":nombreTernero, "Padre: ":"Toro de Rancho"}
            self.listaTerneros.append(nombreTernero)
        
        else:
            nombreTernero = {"Nombre: ":nombreTernero, "Padre: ": nombrePadreToro}
            self.listaTerneros.append(nombreTernero)
                
        
    #mostrar Lista Terneros
    def listarHijosTerneros(self):
        
        for i in self.listaTerneros:
            print( i["Nombre: "],'-',i['Padre: '])
    
    
    def ordeñar(self, litros):
        self.listaCantidad_produccion.append(litros)
    
    def ordeñarparaTernero(self, motivo):
        if motivo == self.enfermedad:
            print( 'Vaca con "', self.enfermedad, '"leche destinada a terneros')
        elif motivo == self.observacion:
            print( 'Vaca con "', self.observacion, '"leche destinada a terneros')
        else:
            print( 'Motivo no coincide con enfermedad u observacion')
    
    #cuando la vaca se encuentre en plena produccion
    def preñezVaca(self, toroPajilla, fecha):
        if toroPajilla == 'desconocido':
            self.listaPreniez_toros.append('Toro de Rancho')
            self.listaPreniez_fechas.append(fecha)
        else:
            self.listaPreniez_toros.append(toroPajilla)
            self.listaPreniez_fechas.append(fecha)
        
    def agregarAlimento(self, nuevo_alimento):
        self.listaAlimentos_vaca.append(nuevo_alimento)
        print('Alimento agregado')
    
    def eliminarAlimento(self, alimento_eliminar):
        if alimento_eliminar in self.listaAlimentos_vaca:
            self.listaAlimentos_vaca.remove(alimento_eliminar)
            print('El alimento "',alimento_eliminar,'" se ha borrado de la lista de alimentos',self.listaAlimentos_vaca)
        else:
            print( alimento_eliminar, 'no existe en la lista de alimentos')
    def consultarAlimentos(self):
        return self.listaAlimentos_vaca
     


class Ternero(Animal):
    def __init__(self, nombre, edad, peso, raza, nombrePadre, nombreMadre, observacion):
        self.listaConsumo_leche = []
        self.listaAlimentos_ternero = []
        self.nombrePadre = nombrePadre
        self.nombreMadre = nombreMadre
        self.listaHermanos_ternero = []
        self.observacionTernero = observacion
        super().__init__(nombre, edad, peso, raza)
    
    @property
    def nombrePadre(self):
        return self._nombrePadre
    
    @nombrePadre.setter
    def nombrePadre(self, nombrePadre):
        if nombrePadre == 'desconocido':
            self._nombrePadre = 'Torete de Rancho'
        else:
            self._nombrePadre = nombrePadre
    
    def tomarLeche(self, cantidadLeche):
        if cantidadLeche >= 4:
            print( self.nombreAnimal + ' debe tomar '+ str(cantidadLeche) +' hasta los  2 meses')
        if cantidadLeche >= 3:
            print( self.nombreAnimal + ' debe tomar '+ str(cantidadLeche) +' hasta los  4 meses')
        if cantidadLeche >= 2:
            print( self.nombreAnimal + ' debe tomar '+ str(cantidadLeche) +' hasta los  6 meses')
        if cantidadLeche >= 1:
            print( self.nombreAnimal + ' debe tomar '+ str(cantidadLeche) +' hasta los  8 meses')
        self.listaConsumo_leche.append(cantidadLeche)
        
    def agregarAlimento(self, nuevo_alimento):
        self.listaAlimentos_ternero.append(nuevo_alimento)
    
    def eliminarAlimento(self, alimento_eliminar):
        if alimento_eliminar in self.listaAlimentos_ternero:
            self.listaAlimentos_ternero.remove(alimento_eliminar)
            return 'El alimento ', alimento_eliminar, 'se ha borrado de la lista de alimentos',self.listaAlimentos_ternero
        else:
            return alimento_eliminar, 'no existe en la lista de alimentos'
    
    def consultarAlimentos(self):
        return self.listaAlimentos_ternero
        
    



#INSTANCIAS DE CLASE VACA
vaca1 = Vaca('Pulga', 2, 850, 'Brown Swiss', 'produccion', 4, 2, 'ninguna')
vaca1.fechaNacimiento = "05-11-2016"
vaca1.enfermedad = 'mastitis'
vaca1.observacion = "vacuna contra mastitis"
vaca1.listaAlimentos_vaca.append("melasa")
vaca1.agregarAlimento("yerba")
print(vaca1.consultarAlimentos())
vaca1.eliminarAlimento("melasa")
vaca1.ordeñar(15)
vaca1.ordeñar(16)
vaca1.ordeñarparaTernero('vacuna contra mastitis')
print(vaca1.listaCantidad_produccion)
vaca1.listaFechaPartos.append('20-11-2022')
print(vaca1.listaFechaPartos)
vaca1.preñezVaca("DESCONOCIDO".lower(), "20-01-2022")
print(vaca1.listaPreniez_toros)

#BDD
import sqlite3 
conexion = sqlite3.connect(r"C:\Users\Usuario\OneDrive\Documents\JupyerNotebook\ejemplo.db")
cursor= conexion.cursor()
#cursor.execute('CREATE TABLE Vaca (nombreAnimal varchar(30), edadAnimal int, pesoAnimal float, fechaNacimiento date, razaAnimal varchar(30), enfermedad varchar(50), tratamiento varchar(50), estadoProduccion varchar(30), listaCantidad_produccion int, numero_tetas int, listaAlimentos_vaca text, listaFechaPartos text, numero_partos int, listaPreniez_toros text,  listaPreniez_fechas text, listaTerneros text, observacion text)')
#cursor.execute(f'INSERT INTO Vaca VALUES ("Pulga", 2, 850,{vaca1.fechaNacimiento},"Brown Swiss", {vaca1.enfermedad}, {vaca1.tratamiento}  )')
#conexion.commit()

#INSTANCIAS DE CLASE TERNERO
ternero1 = Ternero("Malo", 1, 250, "Gir", 'desconocido', 'Estrella', 'Chivo adoptado por la Estrella')
ternero1.enfermedad = "ninguna"
ternero1.fechaNacimiento = "23-08-2021"
ternero1.listaAlimentos_ternero.extend(['leche','pasto picado','platano'])
ternero1.agregarAlimento('galleta')
print(ternero1.consultarAlimentos())
print(ternero1.eliminarAlimento('leche'))
ternero1.tomarLeche(1)

vaca1.agregarTernero(ternero1, "desconocido")
vaca1.listarHijosTerneros()

"""
FALTA:
    1. Guardar datos de las instancias en la BDD.
    2. Usar Numpy para sumar la cantidad de litros de produccion de una vaca.
    3. Usar Numpy para sumar la cantidad de litros de consumo de un ternero.
"""