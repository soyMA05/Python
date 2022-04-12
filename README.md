#  **Introduccion a  Python**

# Indice
1. [**Tipos de datos en Python (Resumen)**](#tipos_datos_resumen)
2. [**Variables**](#variables) 
3. [**Condicionales**](#condicionales)
4. [**Bucles: For & While**](#for_and_while)
5. [**Funciones**](#funciones)
    
    5.1. [**Funciones Lambda**](#funciones_lambda)
    
    5.2. [**Funciones Recursivas**](#funciones_recursivas)
6. [**Módulos**](#modulos)
7. [**Archivos**](#archivos)
8. [**Errores: manejo de excepciones**](#errores_excepciones)
9. [**Programacion Orientada a Objetos - POO**](#poo)

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

# <a id="funciones_recursivas"> </a>
## 5.2 Funciones recursivas
La recursion es definir algo en términos de sí mismo. Es decir, una función recursiva es aquella que se llama así misma.

Elementos de las funciones recursivas
* **Caso base**: permite que el proceso se detenga, el proceso de que la función se llame así una y otra vez. En sí no debe automallarse.
* **Caso recursivo**: permite descomponer el problema en una versión más pequeña de ese mismo problema, hasta llegar al caso base que detiene ese proceso.

```python
def fibonacci(n):
    #caso base
    if n== 0 or n ==1:
        return n
    #caso recursivo
    if n !=0 and n !=1:
        return fibonacci(n-1) + fibonacci(n-2)     
print(fibonacci(3))
```
**Nota:**  Otro ejemplo de recursividad aplicado a factorial se encuentra en el archivo "Python\recursividad.py".

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

# <a id="archivos"> </a>
# 7. Archivos
Unicamente se tratan archivos de texto(txt). Para trabajar con archivos en python es recomendable usar la setencia **with**.
* **Sentencia "with"**: permite abrir un archivo y luego lo cierra automaticamente.
* Modos de apertura:
    * "r" LECTURA
    * "w" ESCRITURA y reemplaza todo el contenido del archivo.
    * "a" AGREGAR contenido archivo.
    * Agregar un + incluye leer. Por ejemplo r+ o w+.

```python
with open("nombreArchivo.txt"," r,w,a") as nombreVariable:
    for linea in nombreVariable
    print(linea)
```

**Nota:**  Revisar el archivo "Python\archivos.py" donde se encuentran los ejemplos de los tres modos para leer, escribir, agregar y se usa r+ para eliminar con el metodo truncate.

# <a id="errores_excepciones"> </a>
# 8. Errores: manejo de excepciones

Manual de manejo de principales tipos de excepciones:
https://aprendeconalf.es/docencia/python/manual/excepciones/

Apuntes Python: https://docs.hektorprofe.net/python/errores-y-excepciones/excepciones-multiples/
```python
    n1 = 8
    n2 = 0
    try:
        #Intenta ejecutar este codigo
    except ZeroDivisionError:
    else:
    finally:
    
    #Ejercicio
    
    #variables
    resultado = 0
    #funcion division
    def division(num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError as e:
            print(e, " No se puede dividir entre 0")
            return 123
        
    #entrada
    n1 = int(input("Digite un numero: "))
    n2 = int(input("Digite otro numero: "))
    rspt = division(n1, n2)

    while rspt == 123:
        n1 = int(input("Digite un numero: "))
        n2 = int(input("Digite otro numero: "))
        rspt = division(n1, n2)

    print("Rpta",rspt)
```
**Nota:**  Revisar el archivo "Python\errores.py" donde se encuentran las 6 formas de usar las excepciones. El ejercicio se encuentra en "Python\errores_ejercicios.py"

# <a id="poo"> </a>
# 9. Programacion Orientada a Objetos - POO
Para crear un objeto especifico, se debe crear un plano. Desde un plano se pueden crear varios objetos del mismo tipo, porque tienen el mismo plano. Un plano de casa, puede crear varias casas.
* **self**: esta relacionado con el concepto de instancia. En el ejemplo que se ve, self está relacionado con cada una de las cuentas bancarias.

```python
#SINTAXIS
class NombreClase:
    #Metodo Constructor para definir Atributos/Caracteristicas 
    def __init__(self, parametros_ValorAtributo):
        self.nombre_atributo = parametros_ValorAtributo
    
    def metodo_valorObjeto(self):
        print (self.nombre_atributo)#para mostrar los valores actuales del objeto
    
    def metodo_operacion(self, parametros_ValorAtributo):
        if self.nombre_atributo >= 0: #para operar con  valores en los metodos 
            

#EJEMPLO
class CuentaBancaria:
    #Metodo Constructor para definir Atributos/Caracteristicas
    def __init__(self, num_cuenta, nombre_titular, balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance

    #Método/Propiedad o estado del objeto
    def generar_balance(self): # viene a ser como Get 
        print(self.balance)
    
    #metodo/que realiza una tarea
    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
    
mi_cuenta = CuentaBancaria("2207812558", "Miguel Castillo", 50)
print("Saldo:", mi_cuenta.balance)
#mi_cuenta.generar_balance()

mi_cuenta.depositar(int(input("Ingrese un monto a depositar: ")))
print("Saldo Actualizado:", mi_cuenta.balance)
```
## 9.1 POO - conceptos
* **Objeto** es algo que se quiere representar, es una Entidad. Posee atributos y métodos.
    * **Atributos** son las características o estados que definen al objeto. Se pueden crear de forma dinámica, es decir, después de su ejecución.
        1. **Atributo de clase o estático**: para todos las instancias de esa clase van a tener el mismo valor, es atributo estatico.
        2. **Atributo instancia**: para cada uno de los objetos van a tener sus propios atributos.
    * **Métodos** son las acciones que puede realizar el objeto.
        1. **Metodo constructor (privado)** que inicializa los valores de los atributos de instancia.
        2. **Metodo de accion** son las operaciones para obtener el estado del objeto o manejar determinados datos de ese objeto para realizar cambios y mostrarlos.
        3. **Metodo estático o de clase** son aquellos que se pueden utilizar sin la necesidad de una instancia.
* **Clase** es el plano o molde para definir la estructura y poder crear objetos.
* **Instancia** es obtener un objeto (crear objeto) a partir de una clase.
* **Metodo constructor** sirve para inicializar los atributos de un objeto.
    * **self** hace referencia al objeto que se está creando (dentro de la clase) y no se debe tomar en cuenta cuando se quiere instanciar un objeto (solo los parametros que son).
    ```python
    class Clase:
        #Atributo de clase
        atributo_estatico = "valor"

        #metodo constructor / Atributo de instancia
        def __init__(self, parametro)
            self.atributo = parametro
    ```

* **UML (Language Unified Modeling - Lenguaje Unificado de Modelado)**
En la POO se utiliza el *diagrama de clases* para visualizar rápidamente un sistema que ha utilizado POO. Ver explicacion: https://www.youtube.com/watch?v=iliKayKaGtc
* **Patrones de Diseño**: son reglas o formas que nos permiten diseñar un modelo de forma correcta y que nos ayudan a que nuestro modelo funciona de la manera que se espera.
## 9.2 Fundamentos de POO
* **HERENCIA** [**aqui**](https://www.youtube.com/watch?v=iliKayKaGtc)
    * Relación de generalización (clase hija (subclase) hereda de la clase padre (súperclase))
    * La subclase hereda los métodos de la superclase, a menos que la subclase los reimplemente o sea los puede reescribir y se utiliza el método de la clase hija y ya no de la clase padre.
    * Se pueden usar clases abstractas pero estas no se pueden instanciar, si no que se instancian a partir de las clases hijas.



**NOTA** aqui me quedo https://www.youtube.com/watch?v=iliKayKaGtc

# Referencias
FatzCode(2019) "Python para principiantes" https://www.youtube.com/watch?v=chPhlsHoEPo

freeCodeCamp Español (2021) "Introducción a Programación en Python" https://www.youtube.com/watch?v=DLikpfc64cA&t=13924s



**Lectura**

Hector Docs(2018) "Apuntes de Python" https://docs.hektorprofe.net/python/errores-y-excepciones/excepciones-multiples/

# Crear un Portafolio Exitoso
1. Comprar un dominio. 
    * Esto tiene un valor de 10 a 20 $.
    * Utiliza el dominio nombreapellido.com
2. Idioma.
    * Dependiendo del pais en donde quiero conseguir el trabajo debo poner la página en esos idiomas (minimo 2, español-ingles, español-frances, etc).
3. Servicios que ofreces.
    * Lo que quiero vender debe estar claro en mi página.
4. Area de proyectos.
    * Parte vital porque demuestro mi experiencia.
    * Demuestro en qué proyectos he trabajado, pueden ser los más destacados o todos, pero...
    * Debo asegurar una buena experiencia de usuario.
    * Por cada proyecto que coloque debo hacer:
        - Colocar una imagen, debajo el nombre del proyecto, luego debajo colocar un resumen de 2 a 3 líneas sobre lo que trata el proyecto.
        - Debajo del resumen, usar iconos para poner el link del proyecto. Otro ícono para poner la URL del código del proyecto.
5. Experiencia laboral
    * Poner en qué empresas he trabajado o realizado pasantías.
    * Poner fecha, titulo de ocupacion.
    * Breve descripción si es posible.
6. Educacion.
    * Si hice cursos o certificaciones.
    * Resaltar qué tecnologías uno sabe, por ejemplo:.
        * Seccion de Frontend Development.
            - Lenguajes:
                * HTML5
                * CSS
                * JavaSript
            - Frameworks and Librerías
                * Bootstrap
                * Angular
                * React
                * Vue.js
                * Materialize Css
                * Webpack
                * Flexbox
                * Pug
                * EJS
        * Seccion de Backend Development.
            - Lenguajes y Frameworks
                * Python
                * JavaScript
                * Java
                * Django
                * Node.js
                * Express.js
            - Databases
                * MySQL
                * HeidiSQL
                * MongoDB
            - Others
                * Postman
                * Heroku
                * Firebase
                * Docker
                * Salesforce
                * Grafana
        * Sección Machine Learning y otras cosas
            - ML Libraries
                * Tensorflow
                * Pytorch
            - Others
                * Git
                * Github
                * Photoshop
                * EcmaScript
                * TypeScript
                * NPM
                * Scrum
                * Jira
            - Sistemas Operativos
                * Windows
                * Linux
7. Informacion de contacto
    * Redes sociales