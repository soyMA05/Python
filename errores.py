# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 16:16:58 2022

@author: MIANCAS
"""
"""
#Tipos
1. Syntax Error: significa que hay error por no seguir las reglas de escritura.
2. EXCEPCION: Error detectado durante la ejecución de un programa.
3. RecursionError: es porque nunca se llega al caso base y el proceso de ejecucion va al infinito.

"""
#SINTAXIS: Formas de alternativas de uso:

# =============================================================================
# #Forma 1. Manejo de excepciones de forma generalizada (no es muy sugerible)
# try:
#     #Intenta ejecutar este codigo
# except:
#     #Si ocurre una excepcion, detente inmediatamente y ejecuta este código.
# =============================================================================


# =============================================================================
# #FORMA 2. Manejo de excepciones explícitas o específicas (recomendable)
# try:
#     #Intenta ejecutar este codigo
# except ZeroDivisionError:
#     #Si ocurre una excepcion, detente inmediatamente y ejecuta este código.
# =============================================================================

# =============================================================================
# #FORMA 3: Manejar multiples excepciones
# try:
#     #Intenta ejecutar este codigo
# except ZeroDivisionError:
# except BaseException:
#     #Si ocurre una excepcion, detente inmediatamente y ejecuta este código.
# =============================================================================

# =============================================================================
# #FORMA 4: Asignar a la excepción una variable, para obtener más información de lo que ocurrió osea el tipo de excepcion que ocurrio.
# n1 = 8
# n2 = 0
# try:
#     #Intenta ejecutar este codigo
#     resultado = n1/n2
#     print(resultado)
# except ZeroDivisionError as e:
#     #Si ocurre una excepcion, detente inmediatamente y ejecuta este código.
#     print (e)
# =============================================================================

# =============================================================================
# FORMA 5: Uso de la claúsula "Else"
# n1 = 8
# n2 = 0
# try:
#     #Intenta ejecutar este codigo
#     resultado = n1/n2 (aqui puede ocurrir una exepcion)
#     print(resultado)
# except ZeroDivisionError as e:
#     #Si ocurre una excepcion, detente inmediatamente y ejecuta este código.
#     print (e)
# else:
#     #Si no ocurrio una excepcion en 'try' ejecuta este codigo (se salta la clausula except para venir aqui).
      #Si se ejecuta expceto ya no se ejecuta else.  
#     print("Else")
# =============================================================================

# =============================================================================
# # FORMA 6: Se puede combinar todas las clausulas siempre y cuando sea valido
# try:
#     
# except:
#     
# else:
#     
# finally:
# =============================================================================
    



