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
        break
    else:
        print('Hi %s' %name)