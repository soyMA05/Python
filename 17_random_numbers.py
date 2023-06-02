import random

# obtener un numero entero del 1 - 6
x = random.randint(1,6)
print(x)

#obtengo un numero cualquiera
y = random.random()
print(y)

#seleccionar un elemento de una lista
favorite_foods = ['hamburger', 'pizza', 'papitas', 'naturisimo', 'helado']
z = random.choice(favorite_foods)
print(z)

#mezclar o barajar elementos de una lista
cartas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A "]
random.shuffle(cartas)
print(cartas)