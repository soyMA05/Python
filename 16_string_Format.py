""" 
str.format()= metodo opcional que brinda a los usuarios mas control cuando
se quiere mostrar salida/resultados.
"""

animal = "cow"
item = "moon"

print("The "+ animal + " jumped over the " + item)
#utilizando .format()
print("The {} jumped over the {} ".format(animal, item))
print("The {1} jumped over the {0} ".format(animal, item)) #posicion de argumento

print("The {animal} jumped over the {item} ".format(animal="vaca", item="moon"))


# ESPACIOS CON TEXTO
name = "Miguel"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name)) #recorro 10 espacios a partir de la variable invocada
#recorro 10 espacios a la derecha a partir de la variable invocada (lo mismo que arriba)
print("Hello, my name is {:<10}. Nice to meet you".format(name)) 
#recorro 10 espacios a la izq a partir de la variable invocada (lo mismo que arriba)
print("Hello, my name is {:>10}. Nice to meet you".format(name)) 
#con 10 espacios centro el texto de la variable invocada (lo mismo que arriba)
print("Hello, my name is {:^10}. Nice to meet you".format(name)) 


# VISUALIZAR NUMEROS
number = 3.14159
#mostrar dos numeros de la porcion decimal 
print("The number pi is {:.2f}".format(number))

num= 1000
#agrego una coma en el primer digito
print("The number pi is {:,}".format(num))
#mostrar el numero en formato binario
print("The number pi is {:b}".format(num))
#mostrar el numero en formato octal
print("The number pi is {:o}".format(num))
#mostrar el numero en formato hexadecimal x/X
print("The number pi is {:X}".format(num))

#mostrar el numero en notacion cientifica e/E
print("The number pi is {:E}".format(num))