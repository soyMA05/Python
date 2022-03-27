#  **Introduccion a  Python**

# Indice
1. [**Tipos de datos en Python (Resumen)**](#tipos_datos_resumen)
2. [**Variables**](#variables) 
3. [**Condicionales**](#condicionales)
4. [**Bucles: For & While**](#for_and_while)
5. [**Funciones**](#funciones)
    
    5.1. [**Funciones Lambda**](#funciones_lambda)
6. [**Módulos**](#modulos)

# <a id="tipos_datos_resumen"></a> 
# 1. Tipos de datos en Python (Resumen)
Ver qué tipo de dato se está usando o tomando de una variable
 `print(type("Hola Mundo")) `.

Ver informacion sobre una variable `print(dir(nombre_variable))`. En los resultados, la primera parte corresponderá las propiedades y la segunda parte del resultado serán los métodos.

Un breve resumen de los tipos de datos revisar el archivo "Python\TipodeDatos.py".
* **Strings**: 

    ```python
        cadena = "Hola"
        print(cadena + "Mundo")
    ```
    **Nota:** Para ver más de informacion sobre el tipo de dato *string*, revisar el archivo "Python\strings.py".


* **Numeros**: 

    En Python existen dos tipos de datos numéricos (existen números imaginarios para apps cientiíficas, aquí no se abarcó):
    * **Integer**
        ```python
        print(5+3)
        ```

    * **Float (Decimal)**
        ```python
        print(23.5)
        ```
    **Nota:** Para ver más de informacion sobre el tipo de dato *Integer o entero*, revisar el archivo "Python\numeros.py".


* **Boolean** 

    Solo existen dos valores, True y False

* **List o Listas**

    En las listas se puede colocar cualquier tipo de dato. Se usan cuando queremos cambiar el valor de los elementos después del tiempo de ejecución, es decir, a lo largo del uso de la aplicación.
    
    ```python
    [] #lista vacia
    [10,20,30, False, "Miguel", 23.3, 5+3]
    print([10,20,30, False, "Miguel", 23.3, 5+3])

    notas_parcial1 = [] # es forma de usar una lista dinámica.
    for i in range(5):
        nota = float(input(f"Ingrese la nota del estudiante {i+1}: ")) 
        while nota < 0 or nota > 20:
            nota = float(input(f"Ingrese correctamente la nota del estudiante {i+1}: ")) 
        notas_parcial1.append(nota)
    
    print(notas_parcial1)

    ``` 
    
    **Nota:** Para ver un poco más de informacion sobre el manejo *Listas*, revisar el archivo "Python\listas.py". En la carpeta "Python\Ejercicios_Listas" se encuentra el archivo "EJERCICIOS_BLOQUE_LISTAS.txt" donde se encuentran la descripcion de los ejercicios que se han realizado para conocer el manejo de las listas.


    **RESUMEN DE TRABAJAR CON LISTAS:**
    ```python
    print(len(colores))#numero de elementos en lista o longitud de lista
    colores[1]="verde"#cambiar el valor en esa posicion de la lista

    #BUSCAR
    print("green" in colores) #saber si existe un elemento en la lista
    print(colores.index("rojo")) #encontrar la posicion de un elemento

    #AGREGAR
    colores.append("celeste") #AGREGAR nuevo elemento en la lista y  crece automaticamente en el caso de que no se use un for o while.
    colores.insert(1, "marrow")# INSERTAR un elemento dado un indice y un valor.
    colores.extend(['cafe','rosado']) #para AGREGAR VARIOS ELEMENTOS a la lista.
    
    #ELIMINAR O QUITAR ELEMENTOS
    colores.pop() #ELIMINAR el ultimo elemento de la lista
    colores.pop(1) #ELIMINAR el elemento con que se encuentra en la posicion 1 y reduce el tamanio de la lista
    colores.clear()# vaciar toda la lista
    colores.remove('amarillo')#elimino un elemento por nombre o valor

    #ORDENAR LISTAS
    colores.sort()#ORDENAR de A-Z o de forma creciente
    colores.sort(reverse=True)#ordena de manera Z-A o de forma decreciente en numeros
    colores.reverse()#rdenar de manera inversa los ultimos son primeros y los primeros son ultimos
    ```


* **Tuples o Tuplas**

    Se usan en datos que no cambian. En si es una lista que no puede cambiar una vez ya definida en la aplicacion.
    ```python
    (10,20,30)
    ()#tupla vacia
    print(type((10, 20, 30, False)))
    ```
    **Nota:** Para ver más de informacion sobre *Tuplas*, revisar el archivo "Python\tuplas.py".


* **Dictionary o Diccionarios**: 

    Es una colecccion que sirve para agrupar diferentes tipos de datos, usando clave(nombre campo) y valor. En NoSQL un documento esta compuesto de colecciones que son cada uno de los datos que pertenece a un usuario u otro objeto.
    ```python
    {"nombre": "Miguel",
    "apellido":"Castillo",
    "edad":23}
    print(type({"nombre": "Miguel", "apellido":"Castillo",
    "edad":23}))
    print({"nombre": "Miguel", "apellido":"Castillo", "edad":23})
    ```
    **Nota:** Para ver más de informacion sobre *Diccionarios*, revisar el archivo "Python\diccionarios.py".


* **Set**

     Es un tipo de dato que no tiene indice. Se usa cuando no se quiere ordenar datos.
    ```python
    colores={"amarillo","azul","rojo"}
    print(type(colores))
    print(colores)
    ```
    **Nota:** Para ver más de informacion sobre *Set*, revisar el archivo "Python\tipodato_set.py".


* **None o ninguno**: 

    No presenta ningun tipo de dato.
    ```python
    None
    print(None)
    print(type(None))
    ```
# <a id="variables"></a> 
## Variables 
Sirven para almacenar un valor de un tipo de dato en una palabra clave.

Reglas para nombrar variables en Python:
* nombre_variable (Snake Case)
* _nombre1_variable
* nombreVariable (Camel Case)
* NombreVariable (Pascal Case)
* ESTATICA (Ej: PI = 3.1416)

**Nota**: No está permitido iniciar con un número para nombrar una variable. Sólo puede contener caracteres alfanuméricos (A-Z, a-z, 0-9, _ ). En tal caso revisar "Python\Variables.py".

# <a id="condicionales"></a> 
# 3. Condicionales
Se usa if, elif (en Java es *else if*) y else.
```python
    #DEMO
    numero = int(input("Escriba un numero entre 0-1: "))
    if numero ==0:
        print("Escribio el numero 0")
    elif numero == 1:
        print("Escribio el numero 0")
    else:
        print("Escribio un numero fuera de rango")
```
**Nota:**  En python no existe el swtich case como en Java, revisar el archivo "Python\condicional_switch.py". Otra DEMO se puede revisar en el archivo "Python\condicionales.py"

# <a id="for_and_while"></a> 
# 4. Bucles: For & While

Revisar el archivo "Python\for.py" donde se encuentran 3 ejercicios basicos del uso del bucle FOR.

El archivo "Python\while.py" es una demostracion sencilla del bucle WHILE.

# <a id="funciones"></a>
# 5. Funciones
Son un bloque de código reutilizable que realiza una sola tarea especifica. En el caso de la función len() y otras es una función precontruida que otorga python.

Las funciones sirven para evitar tareas repetitivas(reduce cantidad de código).
El principio **DRY (Don't Repeat Yourself)** se aplica en no repetir código si no es necesario.

Ventajas:
* Reusable
* Conciso: no se escribe cientos de líneas varias veces.
* Leíble: para otros desarrolladores y para nosotros mismo.
* Mantenible: cambios en ese bloque de código.
* Comprobable: código fácil de comprobar que funciona correctamente.

```python
#Ejemplo 1
def hola(nombre="Miguel"):
     print("Hola",nombre)
 
hola()

#Ejemplo 2
def suma(numero1, numero2):
    #return numero1 + numero2
    total = numero1 + numero2
    return total

#print(suma(2, 5))
sumando = suma(2, 5) 
print(sumando)
```

**Nota:**  Revisar la DEMO en el archivo "Python\funciones.py"

# <a id="funciones_lambda"> </a>
## 5.1 Funciones Lambda
Son funciones anónimas que toman un numero de argumentos pero que estas solo pueden ser escritas utilizando  una sola expresion. Se esriben en una sola línea.

Se usan idealmente cuando necesitamos hacer algo simple y estamos más interesados en hacer el trabajo rápidamente en lugar de nombrar formalmente la función.
```python
suma = lambda numero1, numero2: numero1 + numero2
print(suma(5, 18))
```

**Nota:** Este mismo ejemplo se encuentra en el archivo "Python\funciones_lambda.py"

# <a id="modulos"> </a>     
# 6. Módulos
Los módulos permiten crear aplicaciones reales, ya que no es necesario escribir codigo desde cero, porque ya existe codigo escrito, mejorado y/o testeado. Cuentan con funcionalidades de avanzadas que optimizan las tareas y dan mayor funcionalidad a la aplicación.

Existen 3 tipos de módulos
1. Módulo de Internet o de Terceros (Pip)
2. Módulos de las propias bibliotecas de python (preconstruidos)
3. Módulo propio

## 6.1 Módulos precontruidos de Python
Revisar funcionalidad
https://www.w3schools.com/python/python_modules.asp

Revisar lista de módulos de Python https://pymotw.com/3/py-modindex.html

```python
import datetime #importa toda la biblioteca
from datetime import timedelta #importa una funcionalidad de la biblioteca
```

## 6.2 Módulo de Internet o de Terceros
Estos módulos son creados por empresas o por la comunidad.
https://pypi.org/

Para instalar módulos de tercero se usa el comando pip. A veces la consola de Windows no presenta la misma facilidad como en la de otros S.O. 

* Django es un framework para crear aplicaciones.
* Tkinter es un biblioteca que permite diseñar interfaces gráficas de usuario o de escritorio.

## 6.3 Modulos propio
Se escribe codigo en un archivo.py y para usarlo, debemos importarlo desde otro archivo.


# Referencias
https://www.youtube.com/watch?v=chPhlsHoEPo
