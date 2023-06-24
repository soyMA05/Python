"""metodo de encadenamiento = es usado para llamar a varios métodos secuencialmente,
cada llamada realiza una acción en el mismo objeto y se devuelve a sí mismo.
"""

class Car:
    
    #metodo para encender el carro
    def turn_on(self):
        print("You start the engine")
        return self
    
    #metodo para conducir
    def drive(self):
        print("You drive the car")
        return self
    
    #metodo para frenar
    def brake(self):
        print("You step on the brakes")
        return self
    
    #metodo para apagar el carro
    def turn_off(self):
        print("You turn off the engine")
        return self
    
car = Car()

car.turn_on().drive().brake().turn_off()