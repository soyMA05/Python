""" 
multiprocessing/multiprocesamiento = ejecución de tareas en paralelo en distintos núcleos de la CPU, sin tener en cuenta
                                    el GIL(Global interpreter Lock) utilizado para los subprocesos.

                * Se pueden crear procesos y cada proceso ejecutarse en paralelo (lo que multithreading no se podia hacer porque el GIL se turnaba para cada proceso)

- multiprocesamiento = mejor para tareas ligadas a la CPU (uso intensivo de la CPU)
- multithreading = mejor para tareas ligadas a io (espera)
"""

from multiprocessing import Process, cpu_count
import time

#contar numeros desde 0
def counter(num):
    count = 0 
    while count < num:
        count += 1


def main():
    print(cpu_count()) #ver cpus de nuestro ordenador
    #> 8 (por ver)
    
    #creamos dos procesos
    a  = Process(target= counter, args=(1000000000,))#ejecutar proceso de 0 a mil millones
    b  = Process(target= counter, args=(1000000000,))#ejecutar proceso de 0 a mil millones
    
    #ejecutamos los dos procesos que van hacer la misma tarea de forma paralela
    a.start()
    b.start()

    #sincronizamos procesos con el hilo principal
    a.join()
    b.join()

    #el programa principal terminara cuando los procesos se hayan terminado
    print("finished in: ", time.perf_counter(), " seconds")

    #> 43.6927644  # segundos que ha demorado mi pc solo con el proceso a
    #> 46.4976691   # segundos que ha demorado mi pc con procesos a y b


if __name__ == "__main__":
    main()


"""
RESUMEN:
- El multiprocesamiento permite ejecutar varios procesos de forma paralela/simultanea, es decir, no hay esperas
para poder continuar con otras tareas dentro de nuestro programa.
- Es viable manejar el numero de procesos segun las cpus de nuestro ordenador, es decir si tiene 4  procesadores logicos
 crear 4 procesos seria bien, aunque en algunos casos es valido duplicarlos, tripicarlos, etc, pero ya depende de los 
 recursos de la pc y el contexto en que se desee aplicar.
"""