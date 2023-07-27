"""
CLASES ABSTRACTAS:
    - No se pueden instanciar directamente.
    - Contienen por lo menos un metodo abstracto.
    - Son la base para crear crear subclases mas especificas.

    Metodos ABSTRACTOS
        - Se deben sobreescribir(polimorfismo) en cada una de las subclases.
"""
from abc import ABC, abstractmethod

class Personaje(ABC):

    #constructor
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.vida = 100
        self.inventario =[] #lista de objetos

    @abstractmethod
    def atacar(self, objetivo):#el personaje puede atacar a otro personaje
        pass

    @abstractmethod
    def getStatus(self): #el personaje obtiene su estado
        print(f"Nombre: {self.nombre} Nivel: {self.nivel}")

    """al no ponerlo como metodo abstracto quiere decir que no lo vamos a 
    sobreescribir, es decir que no lo vamos a extender (al menos que queramos 
    definir una forma diferente para que cada una de las clases suban de nivel)
    en este caso sea mago o guerrero va a tener la misma forma de subir de nivel
    """
    def subirDeNivel(self):
        self.nivel += 1

    def verInventario(self):
        print("Inventario de: %s" % self.nombre)
        for obj in self.inventario:
            print(obj)

#clase secundaria/hija
class Mago(Personaje):

    #constructor
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 120
        self.inteligencia = 95
        self.inventario = ["Pocion de Mana","Grimorio"]

    def getStatus(self):
        print("Clase Mago")
        super().getStatus()
    
    def atacar(self, objetivo):
        objetivo.vida -= self.inteligencia * 0.6
        print(f"Soy {self.nombre}, la Vida actual del objetivo {objetivo.nombre} es {objetivo.vida}")
    
#clase secundaria/hija
class Guerrero(Personaje):
    
    #constructor
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.inventario = ["Pocion de vida", "Escudo", "Espada"]
    
    def getStatus(self):
        print("Clase Guerrero")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza * 0.8
        print(f"Soy {self.nombre}, la Vida actual del objetivo {objetivo.nombre} es {objetivo.vida}")

guerrero = Guerrero("Kaladin")
mago = Mago("Yuno")

guerrero.getStatus()
mago.getStatus()

mago.verInventario()
guerrero.verInventario()

mago.atacar(guerrero)
guerrero.atacar(mago)