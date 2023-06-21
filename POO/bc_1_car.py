class Car:
    # variables de clases
    wheels = 4 

    #metodo para iniciar las variables de instancia
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print("This car "+self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")