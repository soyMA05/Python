""" 
thread(hilo) = es un flujo de ejecucion.
                cada hilo puede llevar a cabo su propia orden separado de instrucciones.

                Sin embargo, cada hilo se ejecuta por turnos para lograr la concurrencia ( concurrencia = varios a la vez y no uno a uno). Es decir, los hilos
                se pueden ejecutar en diferentes partes de un programa, en diferentes momentos, pero NO 
                VERDADERAMENTE en paralelo (multithreading mas adelante) si no que cada hilo toma un turno.

                Existe una caracteristicas en python que se llama:
                GIL = (bloqueo global del intérprete), permite que sólo un hilo mantenga el control del intérprete de Python en un momento dado. Es decir,
                solamente un hilo puede funcionar en ese instante de tiempo, pero todos los demas pueden tomar un turno para ejecutarse.

Los programas y tareas pueden dividirse en dos categorias diferentes: cpu bound y io bound.

    cpu bound = es decir, un programa o una tarea que pasa la mayor parte de su tiempo esperando eventos internos (CPU intensiva).
                * cuando una tarea requiere uso intensivo de la cpu es mejor usar multiprocessing(multiprocesamiento). 
                * SINCRONICO

    io bound (input/output) =  programa/tarea pasará la mayor parte de su tiempo esperando eventos externoss (aplicaciones como sistemas de procesamiento de textos, aplicaciones web (login, entradas de texto), copia de archivos y descarga de archivos.).
                * aqui es mejor usar multithread(multihilo) porque podemos tener múltiples hilos ejecutándose concurrentemente(que en realidad realizaran su tarea unicamente cuando ocurra ese evento esperado),
                pero NO realmente en paralelo como hacemos con el multiprocesamiento. 
                * ASINCRONO
"""

import threading
import time
#Introduccion

#contar el número de hilos que se están ejecutando actualmente (o sea que estan activos) en segundo plano
#print(threading.active_count())
#>  1 

#listar todos los hilos que se estan ejecutando
#print(threading.enumerate())
#> [<_MainThread(MainThread, started 15288)>] # El hilo de ejecutar este programa se llama MainThread



#EJEMPLO para probar los hilos
#a algunos les gusta estudiar antes de ir al colegio, pero toca ir comiendo el desayuno y tomar cafe
def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finish studying")

#A. SIN MULTI-HILOS (aqui demora aprox 12seg>=)

#ejecutar esas tres funciones en nuestro hilo principal, cada actividad se va ejecutar cuando finaliza la anterior
#por lo tanto, estas actividades en realidad no las hacemos secuencialmente sino que concurrentemente
#ya que demorariamos mas tiempo en hacerlo uno a uno, es decir, mientras comemos el desayuno, paramos
#un ratito y bebemos cafe, de lo contrario nos atoramos, y luego paramos otro ratito
# y miramos nuestro libro para ir recordando o estudiando.
#eat_breakfast()
#drink_coffee()
#study()
#print(threading.active_count()) #por lo tanto hay 1 solo hilo que esta a cargo de estas tres funciones separadas
#print(threading.enumerate())




#B. SOLUCION - MULTIHILOS (aqui demora aprox 5 seg)
#crear tres hilos y cada una de ellas va a ejecutar una actividad y luego tendremos nuestro hilo principal ejecutándose en segundo plano que completará el resto del programa 

#si la funcion tiene parametros, debemos pasar esos argumentos, pero como no tiene lo dejo vacio(aunque lo puedo quitar)
x = threading.Thread(target=eat_breakfast, args=()) 
x.start()#empezar ejecucion
y = threading.Thread(target=drink_coffee, args=()) 
y.start()#empezar ejecucion
z = threading.Thread(target=study, args=()) 
z.start()#empezar ejecucion

print(threading.active_count())
#>  4   # el hilo principal de este programa se mantiene y se ejecuta en 2doplano, se agregan 3 hilos que ejecutan de manera independiente cada actividad
print(threading.enumerate()) 
#>  [<_MainThread(MainThread, started 18204)>, <Thread(Thread-1, started 8452)>, <Thread(Thread-2, started 14504)>, <Thread(Thread-3, started 12836)>]

#print(time.perf_counter())#ver cuanto tiempo demora en ejecutarse las instrucciones del hilo principal
#> 0.0394712 # estos segundos demoro en mostrar todas las instrucciones del hilo principal



#C. SINCRONIZACION DE HILOS

# el hilo principal debe esperar a que todos los demas hilos terminen sus procesos para que pueda continuar con sus intrucciones del programa, ya sea mostrar
# finalizar o invocar otras funciones, metodos, etc.

x.join()
y.join()
z.join()
print(time.perf_counter())
#>  5.0514011  tiempo en segundos que el hilo principal termina de ejecutarse por la sincronizacion de los hilos adicionales.



""" 
RESUMEN:

Practico
- Podemos tener diferentes hilos que ejecuten diferentes partes de nuestro programa.
- Al tener más de un hilo ejecutándose concurrentemente, realmente NO se ejecutan en paralelo sino que los hilos se turnarán mientras
mientras uno de ellos está inactivo.

- La razon porque la solucion demora en ejecutarse 5 segundos es porque trabaja de forma concurrente. Es decir, la primera actividad se muestra a los 3, la otra a los 4 segundos y la otra a los 5 segundos. Eso
es concurrente, todos a la vez respetando sus tiempos. Por lo cual, todo el programa se terminar de ejecutar a los 5 segundos.
Al demorar 12 segundos trabaja en un hilo(hilo principal) de forma manera secuencial. a los tres segundos se ejecuta una actividad, a los 7 seg la otra y a los 12 seg la ultima actividad.
Si le quitara los tiempos demoraria menos o igual a un 1 segundo.

- Una vez termine de ejecutarse cada activdad en cada hilo, ya no se podran visualizar los hilos activos, es por eso que se puso el tiempo para revisar los hilos activos.
Por ejemplo, si la actividad de un hilo se ejecuta a los 3 seg,  el hilo principal mostrara/ejecutara alguna actividad que este bajo su control,
es decir, el HILO PRINCIPAL NO VA A ESPERAR a que estos tres hilos se completen y continuara con sus instrucciones que le han encomendado.

- El hilo principal se ejecuta en segundo plano, mientras los otros hilos agregados se ejecutan en primer plano segun sus instrucciones.



Teorico:
- un hilo es un flujo de ejecucion donde un programa cualquiera tendra al menos un hilo ejecutandose inicialmente y que se denomina hilo principal. 
- Se pueden crear multiples hilos ejecutandose concurremente y no en parelelo como los es como muli-processing.
- Multi hilo es I/O bound (EVENTOS EXTERNOS), es decir, el usuario debe indicar para que comience la actividad.
- Multi procesamiento esta relacionado con procesos que se ejecutan en un ordenador para hacer calculos de forma interna, ya que reciben eventos internos
y por lo tanto necesitan de CPU (ver en 66_multiprocessing.py).
"""