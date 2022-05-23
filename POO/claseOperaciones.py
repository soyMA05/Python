# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:52:19 2022

@author: miancastillo
"""

class Operaciones(object):#segun yo es opcional poner object ya que da lo mismo
    resultado=0    

    #no tiene constructor puesto que no se quiere inializar

    def sumar(self, numx, numy):
        resutado = numx + numy
        return resutado
    
    def restar(self, numx, numy):
        return numx-numy
    
    def multiplicar(self, numx, numy):
        return numx*numy
    
    def dividir(self, numx, numy):
        if numx == 0 and numy==0:
            return "No se puede dividir para 0."
        if numy == 0:
            return "No se puede dividir para 0"
        else:
            resultado = numx/numy
            return round(resultado,2)
    

o = Operaciones()
print(o.sumar(5,6))
print(o.restar(5, 2))
print(o.multiplicar(5, 3))
print(o.dividir(5, 3))

