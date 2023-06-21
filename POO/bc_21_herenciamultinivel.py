#herencia multinivel: es cuando una clase derivada (hijo) hereda otra clase derivada (hijo)

#clase padre
class Organism:
    alive=True


#clase hija
class Animal(Organism):
    def eat(self):
        print("This animal is eating")

#clase hija de hija
class Dog(Animal):
    def bark(self):
        print("This dog is barking")


#instanciar clase/crear objeto
dog = Dog()

#imprimir atributo de clase padre Organismo
print(dog.alive)

#imprimir metodo de clase padre Animal
dog.eat()

#imprimir metodo de clase
dog.bark()

