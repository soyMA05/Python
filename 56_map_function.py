"""
map(): aplica una función a cada elemento de un iterable ( puede ser lista, tupla, etc).

ESTRUCTURA:
map(function, iterable)
"""
# EJEMPLO

#lista de ropa y sus precios(dolares) por cada prenda. #Se pretende cambiar a euros conservando el orden de los productos
store = [("shirt", 20.00),("jacket",50.00),("pants",25.00),("socks",5.00),("hat",36.00)]

#funcion que se va a aplicar a cada elemento la lista
to_euros = lambda data : (data[0],data[1]*0.91)#esto retorna una tupla (nombre_producto, precio convertido a euro)

#mapear cada item de la lista con la funcion creada y lo que nos devuelve lo guardamos en una lista
store_euros = list(map(to_euros,store))

#mostrar los productos con sus precios convertidos a euros.
for p in store_euros:
    print(p)
