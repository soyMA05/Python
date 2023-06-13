# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:40:07 2022

@author: MIANCAS
"""

# =============================================================================
# #MODULOS: Permiten crear aplicaciones reales. La razón de su uso es evitar tareas repetitivas.
#Existen 3 tipos de módulos
#1. Módulo propio
#2. Módulo de Internet o de Terceros (Pip)
#3. Módulos de las propias bibliotecas de python
# =============================================================================

#FORMA 1 para importar
#import datetime

#devuelve la fecha actual
#print(datetime.date.today())

#devuelve la cantidad de horas y minutos
#print(datetime.timedelta(minutes=70))



#FORMA 2 para importar
# se lee: desde la biblioteca datetime importa timedelta
from datetime import timedelta

#devuelve la cantidad de horas y minutos
print(timedelta(minutes=110))


# IMPORTO MODULO PROPIO modmath
from modulomath import sumar, restar
sumar(23, 5)
restar(23, 5)
