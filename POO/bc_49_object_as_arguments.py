class Tranport:
    pass

class Car(Tranport):
    color = None

class Motorcycle(Tranport): 
    color = None

#funcion utilizada para pasar objetos como argumentos (no es necesario = como parametro)
def change_color(mean_transportation=object, color=str):
    mean_transportation.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()
bike_2 = Motorcycle()

change_color(car_1, "blue")
change_color(car_2, "black")
change_color(car_3, "white")

change_color(bike_1, "green")
change_color(bike_2, "black")


print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
print(bike_2.color)
