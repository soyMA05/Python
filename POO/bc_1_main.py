from bc_1_car import Car

cars = []
car_1 = Car("Chrevrolet", "Corvette", 2020, "blue")
car_2 = Car("Ford", "Ranger", 2025, "black")


#CAR 1
#imprimir atributos de clase
print(car_1.make)
print(car_1.wheels)
#imprimir acciones o metodo de clase
car_1.drive()

#CAR 2
print(car_2.make)
print(car_2.wheels)
car_2.drive()


"""extra"""
cars.append(car_1)
cars.append(car_2)

#imprimir caracteristicas de todos los carros
for c in cars:
    print("****Caracteristicas de carro: "+ str(cars.index(c)+1))
    print(c.make)
    print(c.model)
    print(c.year)
    print(c.color)
    c.drive()
    c.stop()


#llamando atributos de clase
Car.wheels=6
#creando objeto
car_3 = Car("Ford", "Bronco 6x6", "2021","black")
#invocando atributos de instancia
print(car_3.make)
print(car_3.wheels)