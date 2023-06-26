"""Se refiere a la posibilidad de que una subclase cuente con métodos
 con el mismo nombre que los de una clase superior pero que definen 
 comportamientos diferentes.

 Sirven para modificar o reemplazar la implementación de un método heredado de una clase padre en una clase hija.
 
 Cuando una clase hereda de otra clase, también hereda los métodos definidos en la clase padre. Sin embargo, a veces es necesario cambiar o extender el comportamiento de 
 un método en la clase hija para adaptarlo a sus necesidades específicas.

La capacidad de sobrescribir métodos
 es fundamental en la herencia y el polimorfismo.  """

class Animal:
    
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This animal is eating a carrot")

rabbit = Rabbit()
rabbit.eat()