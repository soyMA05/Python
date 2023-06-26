"""
Se utiliza principalmente para modelar, diseñar entidades complejas del mundo real 
separando los datos de las instancias/objetos de manera que no se pueda 
alterar su comportamiento o caracteristicas relevantes.

-Impide que un usuario cree un objeto de esa clase.

-Obliga al usuario a sobrescribir métodos abstractos en una clase hija.

Diferencia entre:
1. Clase abstracta: una clase que contiene uno o más métodos abstractos.

2. Método abstracto: un método que tiene una declaración pero no tiene una implementación.
"""

#importar modulo de ABC (abstract based class)
from abc import ABC, abstractmethod

#clase padre que hereda de la clase ABC
class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

#clase hija Carro
class Car(Vehicle):
    
    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

#clase hija Moto
class Motocycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This Motocycle is stopped")




#crear objetos
#vehicle = Vehicle() no se pueden instanciar y por lo tanto no se puede interactuar directamente
car = Car()
motocycle = Motocycle()

#invocar metodos de clases
#vehicle.go() #no se puede implementar (anteriormente no se puede instanciar)
car.go()
motocycle.go()

car.stop()
motocycle.stop()