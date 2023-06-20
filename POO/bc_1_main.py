from bc_1_car import Car

cars = []
car_1 = Car("Chrevrolet", "Corvette", 2020, "blue")
car_2 = Car("Ford", "Ranger", 2025, "black")


#CAR 1
#imprimir atributos de clase
print(car_1.make)
#imprimir acciones o metodo de clase
car_1.drive()

#CAR 2
print(car_2.make)
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