
def iniciar_juego():
    pronosticos = []
    num_pregunta = 1
    puntaje = 0

    #variables para control de entrada
    opciones_validas = ["A", "B", "C", "D"]
    respuesta_usuario = None
    rpta_sino = ["si", "no"]
    rpta_jugardnuevo = None

    print("-------***Empezamos***--------\n")
    #bucle para mostrar pregunta
    for k in preguntas.keys():
        print("\n",k) #imprimo pregunta

        #bucle para respuesta por pregunta
        for op in opciones[num_pregunta-1]:
            print(op) #mostrar cada una de las opciones
        
        #bucle para controlar entradas del usuario
        while respuesta_usuario not in opciones_validas:
            respuesta_usuario = input("Seleccione la respuesta correcta (A, B, C, D): ").upper()
        pronosticos.append(respuesta_usuario)

        #si rpta es correcta, suma 1
        puntaje += comprobar_respuestas(preguntas.get(k), respuesta_usuario)
        #igual nuevamente a None para anular asignaciones
        respuesta_usuario = None

        num_pregunta += 1

    mostrar_puntaje(puntaje, pronosticos)

    #bucle para validar la continuidad del juego
    while rpta_jugardnuevo not in rpta_sino:
        rpta_jugardnuevo = input("Quieres seguir jugando? (si/no):").lower()
    jugar_de_nuevo(rpta_jugardnuevo)

def comprobar_respuestas(rpta_original, rpta_usuaurio):
    if rpta_original == rpta_usuaurio:
        print("Correcto!")
        return 1
    else:
        print("X Incorrecto ")
        return 0

def mostrar_puntaje(_puntaje, _pronosticos):
    puntuacion = int((_puntaje/len(preguntas))*100)
    print("\nPuntaje obtenido: " + str(puntuacion)+"/100")
    print("Respondido \tSolucion")
    for rpta_us, rpta_correcta in zip(_pronosticos, preguntas):
        print(rpta_us +"\t\t"+preguntas.get(rpta_correcta))

def jugar_de_nuevo(_rptacontinuar):
    if _rptacontinuar == "si":
        iniciar_juego()
    elif _rptacontinuar == "no":
        print("-------------Fin de juego--------------")


preguntas = {
    "Quien creo Python?: " :"A",
    "En que anio fue creado Python?: " : "B",
    "Es facil aprender Python?: " : "D",
    "En que area se aprovecha mas Python?: " : "D"
}

opciones = [
    ["A. Guido Van Roussum", "B. Mark  Zuckenburg", "C. Bill Gates", "D. Brendan Eich"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 1995"],
    ["A. No", "B. Complejo", "C. No lo he intentado", "D. Si, muy divertido!"],
    ["A. Aplicaciones moviles", "B. Videojuegos", "C. Aplicaciones de Desktop", "D. Inteligencia Artificial"]
]
iniciar_juego()