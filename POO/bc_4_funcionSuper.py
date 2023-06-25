"""funcion super():
función utilizada para dar acceso a los métodos (constructor y funcionalidad) de una clase padre. 
Devuelve un objeto temporal de una clase principal cuando se usa y asi,
podemos inicilizar variables de una clase hija a partir de las variables de 
la clase padre, incluso se puede reutilizar metodos de funcionalidad de la clase padre
para agregar mas funcionalidad en la clase hija.

super(): asegura que el comportamiento de la clase padre se mantenga intacto, 
incluso cuando se realiza una sobrescritura en la clase hija.

"""

class Rectangle:
    
    #inicializar variables de instancias
    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width
    
    #metodo saludar
    def saludar(self):
        return "Soy una figura Geometrica"

class Square(Rectangle):

    #inicializar variables de instancias
    def __init__(self, _length, _width):
        super().__init__(_length, _width)

    #metodo para calcular el area del cuadrado
    def area(self):
        return self.length * self.width
    
    #reutilizar metodo saludar de clase padre
    def saludar(self):
        return print(super().saludar(),"=> Cuadrado")

class Cube(Rectangle):
    
    #inicializar variables de instancias
    def __init__(self, _length, _width, _height):
        super().__init__(_length, _width)
        self.height = _height

    #metodo para calcular el volumen del cubo
    def volume(self):
        return self.width * self.length * self.height

    #reutilizar metodo saludar de clase padre
    def saludar(self):
        return print(super().saludar(),"=> Cubo")    

#crear objetos
square = Square(4,4)
cube = Cube(4, 4, 4)

#invocar metodos de clases donde se reutilizan el metodo constructor
print(square.area())
print(cube.volume())

#invocar metodo saludar() de clase Padre en hijas
square.saludar()
cube.saludar()
