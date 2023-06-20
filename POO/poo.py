# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:15:22 2022

@author: MIANCAS
"""

class CuentaBancaria:
    #atributos/caracteristicas
    def __init__(self, num_cuenta, nombre_titular, balance):#funcion para inicializar los atributos
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance
        
    #Método/Propiedad o estado del objeto
    def generar_balance(self):
        print(self.balance)
    
    #metodo/que realiza una tarea
    def depositar(self,monto):
        if monto > 0:
            self.balance += monto

mi_cuenta = CuentaBancaria("2207812558", "Miguel Castillo", 50)
print("Saldo:", mi_cuenta.balance)
#mi_cuenta.generar_balance()

mi_cuenta.depositar(int(input("Ingrese un monto a depositar: ")))
print("Saldo Actualizado:", mi_cuenta.balance)