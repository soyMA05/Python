""" 
daemon thread/hilo demonio (subproceso) = un hilo demonio se ejecuta en segundo plano, no es importante para que el programa se ejecute, su programa no esperará a que los subprocesos
 demonio se completen antes de salir los subprocesos no demonio normalmente no pueden ser eliminados, permanecen vivos hasta que la tarea se complete.

 Ej. tareas en segundo plano, recolección de basura, espera de entrada, procesos de larga duración.
"""
import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1 
        print("logged in for: ", count , " seconds")
        print()

#proceso demonio 
x = threading.Thread(target=timer, daemon=True  )
x.start()

print(x.isDaemon())#consultar si es un proceso demonio True/False

#proceso principal
answer = input("Do you whish to exit?")
print(answer) 


"""
RESUMEN:
- Los hilos demonios conocidos como subprocesos permiten realizar otras tareas bajo el programa principal, es decir se ejecutan en segundo plano.
- Estos subprocesos por lo general se terminan cuando el programa principal termina de ejecutar su flujo de instrucciones.
- Puede ser util para aplicar un contador, cuando un usuario inicia sesion en una aplicacion. Al usar los servicios de la aplicacion se ejecutaria en un primer plano
 y el contador funcionaria como un subproceso o proceso demonio.
"""