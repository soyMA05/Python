#Lectura de archivos
try:
    with open ('text.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("Archivo no encontrado")


#Escritura de archivos
texto = "Hoooola\nEs un gusto conocerte\nBienvenido"
with open('texto2.txt','w') as file:
    file.write(texto())

#Agregar mas contenido o sobreescritura de archivos

texto2="Agregando mas informacion"
with open('texto.txt','a'):
    file.write(texto2)