platos_carta = ["Ternera","Pizza","Champiniones con Pollo","Camarones reventados","Lechon hornado"]
lista_pedidos = []
rpta_sino = ["si", "no"]
opciones_confirmacion = ["a", "b"]

#presentar platos disponibles en la lista
def presentar_platos(_platos_carta):
    contador_plato = 1
    print("\n\t\t** MENU DEL DIA **")
    for plato in _platos_carta:
        print("{}. {}".format(contador_plato, plato))
        contador_plato += 1

    #llamada para seleccionar los platos presentados
    seleccionar_plato(_platos_carta)

#escoger un plato de la lista
def seleccionar_plato(platos_carta):
    buscar_plato = None
    seleccion_plato = None#
    #controlar que los platos si se encuentra en la lista de platos
    while buscar_plato not in platos_carta:
        try :
            seleccion_plato = int(input("\nSeleccione el numero del plato: "))
            buscar_plato = platos_carta[seleccion_plato-1]
            
            #imprimo el plato seleccionado y lo agrego a la lista de pedidos
            print("Plato seleccionado: ", buscar_plato)
            lista_pedidos.append(buscar_plato)
        
        #manejo de excepciones
        except ValueError as ev:
            print(ev, '\nDato ingresado incorrectamente, intente nuevamente...')

        except IndexError as e:
            print(e,"\nEse plato no existe, intente nuevamente...")

    #pregunto al cliente si desea hacer otro pedido
    opcion_nuevospedidos()

#mostrar los platos que ha pedido el cliente
def platos_pedidos():
    contador_pedidos = 1
    print("\n\t## Pedidos realizados ## \nTotal= {} platos".format(len(lista_pedidos)))
    for plato in lista_pedidos:
        print("{}. {}".format(contador_pedidos, plato))
        contador_pedidos +=1

#opcion para hacer otro pedido o no
def opcion_nuevospedidos():
    otro_pedido = None
    eliminar_pedido = None

    while otro_pedido not in rpta_sino:
        otro_pedido = input("Desea realizar otro pedido? (Escriba 'si' o 'no'): ").lower()

    if otro_pedido == 'si':
        seleccionar_plato(platos_carta)
    else:
        #mostrar platos pedidos si el cliente no quiere hacer otros pedidos
        platos_pedidos()

    while eliminar_pedido not in opciones_confirmacion:
        eliminar_pedido = input("\nEstimado cliente seleccione una opcion: \na. Confirmar pedido \nb. Eliminar o cambiar un pedido \n>>: ").lower()

    if eliminar_pedido == 'b':
        #entrar a eliminar un pedido
        quitar_platopedidos()
        
    elif eliminar_pedido == 'a':
        print("Su pedido ha sido confirmado, espere nuestros platos\nGracias por preferirnos :)")
        exit()

    #eliminar_pedido = None

def quitar_platopedidos():
    quitar_pedido = None
    buscar_plato = None
    indice_plato = None

    """corregir este bucle"""
    while buscar_plato not in lista_pedidos:
        try :
            quitar_pedido = int(input("\nSeleccione el numero del pedido a quitar: "))
            buscar_plato = lista_pedidos[quitar_pedido-1]
            
        #manejo de excepciones
        except ValueError as ev:
            print(ev, '\nDato ingresado incorrectamente, intente nuevamente...')

    if type(buscar_plato) is str:
        indice_plato = lista_pedidos.index(buscar_plato)
        lista_pedidos.pop(indice_plato)
    

    #mostrar actualizacion de datos pedidos
    platos_pedidos()

    #el cliente puede realizar otro pedido por el cual elimino o de una vez sale de app
    opcion_nuevospedidos()

#empezar
presentar_platos(platos_carta)


#finalizar
print("\n\nHa salido de la aplicacion...")