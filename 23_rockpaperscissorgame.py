import random

while True:

    opciones = ["piedra", "papel", "tijera"]
    maquina = random.choice(opciones)
    jugador = None
    salir = ["si", "no"]
    jugar_nuevamente = None 
    

    while jugador not in opciones:
        jugador  = input("Piedra, Papel o Tijera ?: ").lower()

    if jugador == maquina:
        print("Computadora: ", maquina)
        print("Jugador: ", jugador) 
        print("EMPATE!")

    elif jugador == "piedra":
        if maquina == "papel":
            print("Computadora: ", maquina)
            print("Jugador: ", jugador) 
            print("PERDISTE!")
        else:
            print("Computadora: ", maquina)
            print("Jugador: ", jugador) 
            print("GANASTE!")

    elif jugador == "papel":
        if maquina == "tijera":
            print("Computadora: ", maquina)
            print("Jugador: ", jugador) 
            print("PERDISTE!")
        else:
            print("Computadora: ", maquina)
            print("Jugador: ", jugador) 
            print("GANASTE!")

    elif jugador == "tijera":
        if maquina == "piedra":
            print("Computadora: ", maquina)
            print("Jugador: ", jugador) 
            print("PERDISTE!")
        else:
            print("Computadora: ", maquina)
            print("Jugador: ", jugador) 
            print("GANASTE!")
    
    while jugar_nuevamente not in salir:
        jugar_nuevamente = input("Seguir jugando? (si/no): ").lower()
    
    if jugar_nuevamente != "si":
        break

print("\nSaliste!!")