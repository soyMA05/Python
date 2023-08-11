""" 
zip(*iterables)
- agrega elementos de dos o más iterables(list,tuples, sets, etc.)
- crea un objeto zip con elementos emparejados almacenados en tuplas para cada elemento.
"""

usernames= ["Dude", "Bro", "Mister", "Mik"]
password = ["1235@", "+89*/", "abc321", "guest_admin"]
login_date = ["1/1/2021", "3/2/2021", "12/11/2020", "13/10/2022"]
users = list(zip(usernames, password))
for i in users:
    print(i) 
    #('Dude', '1235@')
    #('Bro', '+89*/')
    #('Mister', 'abc321')
    #('Mik', 'guest_admin')



users = dict(zip(usernames, password))
for key,value in users.items():
    print(key + " : " + value)
    #Dude : 1235@
    #Bro : +89*/
    #Mister : abc321
    #Mik : guest_admin

users = zip(usernames, password, login_date)
for i in users:
    print(i)
    #('Dude', '1235@', '1/1/2021')
    #('Bro', '+89*/', '3/2/2021')
    #('Mister', 'abc321', '12/11/2020')
    #('Mik', 'guest_admin', '13/10/2022')

""" 
RESUMEN
- Las funciones zip permiten emparejar datos de dos o mas iterables, siempre y cuando tengan la misma longitud de indices.
- El emparejamiento de datos lo hace mediante tuplas, de ahi depende en que tipo de datos queremos guardar esas tuplas. Cada tupla es un indice. 
"""