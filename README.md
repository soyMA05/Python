#  Introduccion a  Python

## Tipos de datos en Python (Resumen)
Ver qué tipo de dato se está usando o tomando de una variable
 `print(type("Hola Mundo")) `.

Ver informacion sobre una variable `print(dir(nombre_variable))`. En los resultados, la primera parte corresponderá las propiedades y la segunda parte del resultado serán los métodos.
* [**Strings**](#strings): 
    ```python
        cadena = "Hola"
        print(cadena + "Mundo")
    ```
* **Integer**:
    ```python
    print(5+3)
    ```
* **Float (Decimal)**:
    ```python
    print(23.5)
    ```
* **Boolean**: True o False
* **List o Listas**:se puede colocar cualquier tipo de dato. Se usan cuando queremos cambiar el valor de los elementos después del tiempo de ejecución a lo largo del uso de la aplicación.
    ```python
    [] #lista vacia
    [10,20,30, False, "Miguel", 23.3, 5+3]
    print([10,20,30, False, "Miguel", 23.3, 5+3])
    ```
* **Tuples o Tuplas**: Se usan en datos que no cambian. En si es una lista que no puede cambiar una vez ya definida en la aplicacion.
    ```python
    (10,20,30)
    ()#tupla vacia
    print(type((10, 20, 30, False)))
    ```
* **Dictionary o Diccionarios**: Es una colecccion que sirve para agrupar diferentes tipos de datos, usando clave(nombre campo) y valor. En NoSQL un documento esta compuesto de colecciones que son cada uno de los datos que pertenece a un usuario u otro objeto.
    ```python
    {"nombre": "Miguel",
    "apellido":"Castillo",
    "edad":23}
    print(type({"nombre": "Miguel", "apellido":"Castillo",
    "edad":23}))
    print({"nombre": "Miguel", "apellido":"Castillo", "edad":23})
    ```
* **Set**: Es un tipo de dato que no tiene indice. Se usa cuando no se quiere ordenar datos.
    ```python
    colores={"amarillo","azul","rojo"}
    print(type(colores))
    print(colores)
    ```
* **None o ninguno**: no presenta ningun tipo de dato.
    ```python
    None
    print(None)
    print(type(None))
    ```

## Variables 
Sirven para almacenar un valor de un tipo de dato en una palabra clave.

Reglas para nombrar variables en Python:
* nombre_variable (Snake Case)
* _nombre1_variable
* nombreVariable (Camel Case)
* NombreVariable (Pascal Case)
* ESTATICA (Ej: PI = 3.1416)

*Nota*: No está permitido iniciar con un número para nombrar una variable. Sólo puede contener caracteres alfanuméricos (A-Z, a-z, 0-9, _ ).

## Conociendo los tipos de datos

### <a id="strings" />Strings

### Numeros en Python

### Listas

### Tuplas 

### Sets

### Diccionarios


## Condicionales

## Bucles: For & While

## Funciones

## Modulos

