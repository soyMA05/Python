from datetime import date
from collections import deque

#herencia multiple {
class Persona:
    def __init__(self,nombres, apellidos, cedula=str,fecha_nacimiento=date, nacionalidad=str) -> None:
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad

class Cliente(Persona):
    def __init__(self,nombres, apellidos, cedula,fecha_nacimiento, nacionalidad) -> None:
        super().__init__(nombres, apellidos, cedula, fecha_nacimiento, nacionalidad)

    def quien_soy(self):
        print("Soy cliente")

class Administrador(Persona):
    usuario = "admin"
    passw = "admin123"

    def __init__(self,nombres, apellidos, cedula, fecha_nacimiento, nacionalidad) -> None:
        super().__init__(nombres,apellidos, cedula, fecha_nacimiento, nacionalidad)
    
    def quien_soy(self):
        print("Soy administrador")
#}

class Banco:
    institucion = "BP"
    
    #constructor
    def __init__(self) -> None:
        self.clientes = deque()
    
    #metodo crear cuenta
    def crear_cuenta(self,monto_inicial=float, cliente=object):
        self.cuenta_cliente ={}
        if monto_inicial >= 5:
            nro_cuenta = self.generar_nro_cuenta()
            #en un solo paso agrego todos los datos necesarios para crear cuenta
            self.cuenta_cliente.update({"numero_cuenta":nro_cuenta, "cliente":cliente, "capital":monto_inicial})
            self.clientes.appendleft(self.cuenta_cliente)#agrego la cuenta creada a la cola de clientes
            print("Estimado cliente {} {} su cuenta numero {} ha sido creada exitosamente\nEs importante que guarde su nro de cuenta"
                  .format(cliente.nombres, cliente.apellidos, nro_cuenta))
        else:
            print("Fallo: El monto inicial para crear la cuenta no es el adecuado")
    
    #generar numero de cuenta
    def generar_nro_cuenta(self):
        longitud_clientes = len(self.clientes)
        return longitud_clientes + 1
    
    #metodo para depositar dinero
    def depositar(self, nro_cuenta=int, monto=float):
        if nro_cuenta in self.clientes:
            print(True,monto)
        else:
            print(False)


cliente1 = Cliente("Miguel Angel", "Castillo Camacho", "2300203557",date(1998,11,5), "ecuatoriana")
cliente1.quien_soy()
cuenta_cliente1 = Banco()
cuenta_cliente1.crear_cuenta(5, cliente1)
cuenta_cliente1.depositar(1, 500)