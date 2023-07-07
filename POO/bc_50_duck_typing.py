"""
tipificación de variables
Concepto en el que la clase de un objeto es menos importante que los métodos/atributos el tipo de clase no se comprueba si están presentes los métodos/atributos mínimos 
"Si camina como un pato, y grazna como un pato, entonces debe ser un pato"

El término correcto es "duck typing" (tipado de pato), y se utiliza en lenguajes de programación que admiten tipificación dinámica,
como Python. En estos lenguajes, el duck typing se basa en el principio de "si parece un pato y suena como un pato, entonces debe ser un pato".

En el duck typing, la idoneidad de un objeto para un determinado uso se determina por su comportamiento en lugar de su tipo explícito.
Esto significa que no importa el tipo específico de un objeto, siempre y cuando el objeto posea los métodos y atributos requeridos
para realizar una operación específica.

El duck typing se utiliza en situaciones donde el énfasis está en el comportamiento y las capacidades del objeto en lugar
de su tipo concreto. Esto permite una mayor flexibilidad y reutilización de código, ya que los objetos no necesitan heredar
de una clase específica o implementar una interfaz definida para ser utilizados en un contexto dado.


En conclusion, el tipo de clase no se comprobará si están presentes los métodos o atributos mínimos, ya que 
se enfoca en el comportamiento del objeto en lugar de su tipo explícito.
"""

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:
    def talk(self):
        print("This chicken is walking")

    def walk(self):
        print("This duck is clucking")

class Person:#lo veo mas para videojuevos
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")
        

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)