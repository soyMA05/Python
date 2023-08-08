"""
1. sort() method = used with lists / usando con listas
2. sorted() function = used with iterables / usado con iterables, cualquier tipo de datos que se pueda iterar.

"""

"""NIVEL DE DIFICULTAD 1"""
#1. METODO sort() de la list----------------------------
students = ["Squiward", "Sandy", "Patrick", "Spong", " Mr.Krabs\n"]
#mostrar estudiantes en orden alfabetico
students.sort()
for estudiante in students:
    print(estudiante)

#ordenar estudiantes de atras hacia adelante por orden alfabetico
students.sort(reverse=True)
for estudiante in students:
    print( estudiante, end=" ")



#2. FUNCION sorted(), dado el caso que no tengamos una lista(si no una tupla o lo que sea),entonces no vamos a poder ordenar nuestros datos
#tupla de estudiantes----------------------------------------
students = ("Aquiward", "Sandy", "Patrick", "Spong", "Mr.Krabs")
sorted_students = sorted(students)#ordenamos los datos de esa tupla, por defecto se ordena alfabeticamente
for s in sorted_students:#mostramos los datos ordenados
    print(s)

sorted_students = sorted(students, reverse=True)#ordenar al reves segun el orden alfabeticamente
for s in sorted_students:
    print("%i. %s" % (sorted_students.index(s)+1, s))





"""NIVEL DE DIFICULTAD 2"""
#1. METODO sort()---------------------------------------------

#lista con tuplas de datos de cada uno de los estudiantes (nombre, calificacion, edad)
students = [("Squiward", "F", 60), ("Sandy","A",33), ("Patrick","D",36), ("Spong","B",20), ("Mr.Krabs","C",65)]

#a. ordenar por calificacion

#calificaciones es una lista y selecciona el valor del indice 1
calificacion = lambda calificaciones : calificaciones[1] #1 esa la columna de la mitad porque el indice empieza en 0
#print(calificacion([1,2,3])) el valor seria el 2

#en key, Si se da una función clave(la funcion calificacion es creada con lambda), la aplica una vez a cada elemento de la lista 
# en este caso, cada tupla es tratada como una lista, extrae cada valor del indice 1 de cada uno de los elementos,
#  y al final con todos los datos extraidos los ordena, ascendente o descendentemente, según sus valores.
students.sort(key=calificacion)#ordena ascedentemente
for s in students:
    print("{}. {}".format(students.index(s)+1, s))

students.sort(key=calificacion, reverse=True)#ordena descendentemente
for s in students:
    print("{}. {}".format(students.index(s)+1, s))

#b. ordenar por edad
edad = lambda edades : edades[2]
students.sort(key=edad)#ordena ascendentemente
for s in students:
    print("{}. {}".format(students.index(s)+1, s))




#2. FUNCION sorted()--------------------------------------------------------
#tupla con tuplas 
students = (("Squiward", "F", 60), ("Sandy","A",33), ("Patrick","D",36), ("Spong","B",20), ("Mr.Krabs","C",65))
#ordenamos con clave, donde edad es la misma funcion lambda anterior, practicamente key de sorted() 
# maneja el mismo concepto de key de sort(), solo que aqui students no es una lista
sorted_students = sorted(students,key=edad)
for s in sorted_students:
    print("{}. {}".format(sorted_students.index(s)+1, s))


"""
RESUMEN:
1. el metodo sort() funciona unicamente para listas
2. la funcion sorted() funciona para tipos de datos que NO SON LISTAS como las tuplas
3. key se iguala a una funcion, esta funcion se la debe crear aparte (en este caso con lambda) y toma automaticamente los valores 
que van a ser ordenados ya sea por sort() o sorted().
4. Si tenemos una lista con tuplas o una tupla de tuplas, cada de elemento es tratado automaticamente como una lista y extraera 
    todos los datos de cada indice.
"""