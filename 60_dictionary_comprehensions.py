""" 
dictionary comprehensions / comprension de diccionarios: crear diccionarios usando una expresion,
puede sustituir a los bucles for y a determinadas funciones lambda.

ESTRUCTURA:
a. dictionary = {key: expression for (key,value) in iterable} (en la expresion se opera con los values y sera el nuevo valor de "value")
b. dictionary = {key: expression for (key,value) in iterable if conditional}
c. dictionary = {key: if/else for(key, value) in iterable}
d. dictionary = {key: function for(key, value) in iterable}
"""

#a.

#declarar dicc 
cities_in_F = {'New York':32, 'Boston':75, 'Los Angeles': 100, 'Chicago': 50}
#hacer operaciones sobre el valor de cada clave
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)
#modificar las claves del diccionario original y asignar nuevos valores a cada clave modificada
cities_in_T = {key+"a": round((value)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_T)


#b.

weather = {"New York": "sunny", "Dallas": "sunny", "Boston": "sunny", "Chicago": "cloudy", "Chicago": "cloudy"}
#obtener las ciudades con un tiempo soleado
sunny_weather = { key: value for(key, value) in weather.items() if value=="sunny"}
print(sunny_weather)

#c. 
cities = {'New York': 32, 'Boston':75, 'Los Angeles':53 , 'Chicago': 20}
description_cities = { key : ("WARM" if value >=40 else "COLD") for (key,value) in cities.items()}
print(description_cities)


#d.

#determinar tiempos
def check_temp(data):
    if data >= 70:
        return "HOT"
    elif 69 >= data <=40:
        return "WARM"
    else:
        return "COLD"
    
cities = {'New York': 32, 'Boston':75, 'Los Angeles':53 , 'Chicago': 20}
#crear un dicc con las ciudades con un tiempo calientisimo, soleado y frio
description_cities = { key : check_temp(value) for (key,value) in cities.items()}
print(description_cities)


""" 
RESUMEN:
- La comprension de diccionarios es una forma simplificada de crear nuevos diccionarios, manejan una estructura similar a la comprension de listas.
- En la expresion se pueden asignar nuevos valores a las claves de un diccionario.
- Existe 4 estructuras para crear diccionarios. La ultima de ellas es que se puede asignar una funcion que retorne un valor y sea el nuevo value. Esto tambien puede
ser aplicado en la comprension de listas.
"""