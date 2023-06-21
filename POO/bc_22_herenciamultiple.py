#herencia múltiple: cuando una clase secundaria se deriva de más de una clase principal

#clase presa
class Prey:

    #metodo huir
    def flee(self):
        print("This animal flees")

#clase depredador
class Predator:

    #metodo cazar
    def hunt(self):
        print("This animal is hunting")

#clase Conejo que hereda de clase Presa
class Rabbit(Prey):
    pass

#clase Halcon que hereda de Depredador
class Hawk(Predator):
    pass

#clase Pescado que hereda de Presa y Depredor(un pez grande puede comerse a un pez pequenio)
class Fish(Prey, Predator):
    pass


#instanciar clases
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

#invocar metodos de clase
rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()



