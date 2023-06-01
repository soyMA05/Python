"""
Loop Control Statements = change a loops execution from its a normal sequence.

break = used to terminate the loop entirely. 
continue = skips to the next iteration of the loop.
pass = does nothing, acts as a placeholder.

Declaraciones de control de bucle: cambia la ejecucion de un bucle de su secuencia normal.

romper = usado para terminar el bucle por completo.
continuar = salta a la siguiente iteracion del bucle.
pasar = no hace nada, actua como un marcador de posicion.
"""


#break
while True:
    name = str(input('What is your name?'))
    if name != "":
        print('Hi %s' %name)
        break
    else:
        print('Ingrese correctamente su nombre')


#continue
"""en este ejercicio solo quiero obtener los numeros y no caracteres especiales"""
phone_number = "02-2715-565"
for i in phone_number:
    if i == "-":
        continue #aqui puedo hacer un punto de control para tomar un valor especifico
    print(i, end="")

#pass
for i in range(1,21):
    if i == 13:
        pass #aqui puedo evitar que se considere un valor para que continue el programa
    print(i, end=" ")