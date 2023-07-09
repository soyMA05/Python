"""
walrus operator := nuevo en Python 3.8

Es una Expression de asignacion (operador morsa)

Este operador asigna valores a variables como parte de una expresion larga.
"""
#antecedente
happy = True
print(happy)

print(happy2:=True)


foods = list()
while True:
    food = input("Ingrese una comida: ")
    if food == "salir":
        break
    foods.append(food)

print(foods)


#con Operador :=
foods2 = list()
while food := input("Ingrese una comida: ") != "salir": # si es verdadero ingresa si es False sale del Bucle, mientras se cumpla esa condicion food sera igual a True
    foods2.append(food)

print(foods2)
