"""
walrus operator := nuevo en Python 3.8

Es una Expression de asignacion (operador morsa)

Este operador asigna valores a variables como parte de una expresion larga.

:= asigna y devuelve(retorna el valor que es asignado)
"""
#antecedente
happy = True #asignamos un valor
print(happy) #devuelve su valor

print(happy2:=True) #asigna y devuelve
print(type(happy2)) #devuelve un tipo booleano especificamente TRUE

#antecendete

foods = list() # almacenar comidas
while True: #siempre V
    food = input("Ingrese una comida: ") #asignar valor comida
    if food == "salir": #comprar, si es igual sale del bucle
        break
    foods.append(food) #guardamos el valor de food (comida)

print(foods)


# EJEMPLO con Operador :=
foods2 = list()
#asigna un valor, devuelve ese valor y compara con "salir"
while (food := input("Ingrese una comida: ")) != "salir": # si es verdadero ingresa, si es False sale del Bucle
    foods2.append(food)#guarda el valor asignado
print(foods2)


#EJEMPLO 1

#crear lista con 20 veces el nro 1
a = 20*[1]
#asignar a n la longitud de la lista a, verifica/comparar que ese valor de a sea mayor a 10 
if (n := len(a)) > 10:
    print(f"La lista tiene {n} elementos (>10)") #devuelve valor asignado