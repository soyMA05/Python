""" 
1. Una funcion puede convertirse en una variable si se le quita el ().
2. Se puede asignar a una NUEVA VARIABLE el valor de una funcion o la actividad que hace esa funcion
"""
#funcion para decir hola
def hellow():
    print("Hola")

print(hellow)#obtiene la ubicacion en memoria (formato hexadecimal) de esa funcion
hellow()#imprime realmente el valor que devuelve esa funcion, es decir, Hola

#de funcion a variable, porque le hemos quitado el () y automaticamente es una variable que esta igualada o tiene un valor de "Hola"
toma_el_valor = hellow #entonces el valor de la variable hellow se le asigna a la variable toma_el_valor
toma_el_valor()#imprimos el valor anteriormente asignado


#OTRO EJEMPLO
#print es una funcion que recibe un argumento para mostrar algo
say = print #print se convierte en una variable cuya funcion(mostrar algo) se le asigna a otra variable llamada say
say("Hola que tal") #say puede hacer lo que hace print
