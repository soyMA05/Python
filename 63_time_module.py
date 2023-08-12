""" 
epoch/época: fecha y hora a partir de la cual un ordenador mide el tiempo del sistema.
"""

import time

print(time.ctime(0)) #convertir un tiempo expresado en segundos desde la época a una cadena legible.
#                       epoch = cuando su ordenador cree que empezó el tiempo (punto de referencia)
#imprime> Wed Dec 31 19:00:00 1969   #aqui como le pase 0 segundos, el computador piensa que empezo en el año 1969

print(time.time()) # retorna los segundos transcurridos desde la epoch/epoca
#imprime> 1691800439.7776663 #son todo los segundos que tengo a dia de hoy

print(time.ctime(time.time())) # le hago pasar los segundos que tengo a dia de hoy
#imprime > Fri Aug 11 19:36:41 2023  # es la fecha en la que estoy escribiendo esto


#objeto de tiempo
time_object = time.localtime()
print(time_object) 
#imprime> time.struct_time(tm_year=2023, tm_mon=8, tm_mday=11, tm_hour=19, tm_min=39, tm_sec=51, tm_wday=4, tm_yday=223, tm_isdst=0)
# el ultimo argumento, esta relacionado con la estacion del tiempo (verano, invierno, etc, toca revisar)

#cambiar formato de salida del tiempo en mes y numeros
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) #https://strftime.org/
print(local_time)
# a partir de time.struct_time(tm_year=2023, tm_mon=8, tm_mday=11, tm_hour=19, tm_min=39, tm_sec=51, tm_wday=4, tm_yday=223, tm_isdst=0)
# puedo cambiar los campos que quiero, y en este caso el resultado de local_time es:
# August 11 2023 19:44:18


#de formato string a struct_time
time_string = "11 August 2023"
#convertir
time_objecto = time.strptime(time_string, "%d %B %Y")
print(time_objecto)
#imprime > time.struct_time(tm_year=2023, tm_mon=8, tm_mday=11, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=223, tm_isdst=-1)
