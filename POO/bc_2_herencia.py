#clase padre o superclase
class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")

#clases hijas o subclases
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


#crear instancias de clase
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#imprimir atributos y metodos de clase padre
print("Atributos y metodos de clase padre")
print(rabbit.alive)
fish.eat()
hawk.slumber()

print("\nMetodos clase hija")
#imprimir metodos de clase hijas
rabbit.run()
fish.swim()
hawk.fly()