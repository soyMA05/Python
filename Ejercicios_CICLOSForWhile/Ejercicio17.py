# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:01:56 2022

@author: MIANCAS
"""

# =============================================================================
# EJERCICIO 17: Una empresa que se dedica a la venta de desinfectantes necesita
# un programa para gestionar las facturas. En cada factura figura: el código del artículo, 
# la cantidad vendida en litros y el precio por litro. Se pide de 5 facturas introducidas: 
# Facturación total, cantidad en litros vendidos del articulo 1, y cuántas facturas se emitieron 
# de más de $600.
# =============================================================================

#variables 
CODIGOFACTURA = 1000
CODCLORO = "CLOR001"
CODPEROXIDO = "PERXID001"
CODALCOHOL = "AlCHL001"
PRECIOLTCLORO = 2.10
PRECIOLTPEROXIDO = 4
PRECIOALCOHOL = 1.75

facturacion_total = 0
cantidad_litrosArt1 = 0
facturas_mayorvalor600 = 0

print("*****TIENDA DE DESINFECTANTES******")

for i in range(5):
    #generar codigo factura
    codigo_factura = str(CODIGOFACTURA) + str(i+1)
    
    #ingreso producto
    producto = int(input(f"######\n\t\t\t#{i+1} PRODUCTOS# \n1. Cloro = $2 Lt  2. Peroxido = $2.30 Lt  3. Alcohol = $ 1.75 Lt\n Ingrese una opcion de producto >>:"))
    while producto > 4 or producto < 0 :
        producto = int(input("RECOMENDACION>>Ingrese un producto entre 1 - 3 \n\t\t\t#{i+1} PRODUCTOS# \n1. Cloro = $2 Lt  2. Peroxido = $2.30 Lt  3. Alcohol = $ 1.75 Lt\n>>Ingrese una opcion de producto:"))
    
    #calculo segun producto
    if producto == 1:
        codigo_articulo = CODCLORO
        cantidad_litros = int(input(">>Ingrese litros a vender: "))
        precio_litro = PRECIOLTCLORO
        valor_pagarfactura = cantidad_litros * PRECIOLTCLORO
        cantidad_litrosArt1 += cantidad_litros
        
    if producto == 2:
        codigo_articulo = CODPEROXIDO
        cantidad_litros = int(input(">>Ingrese litros a vender: "))
        precio_litro = PRECIOLTPEROXIDO
        valor_pagarfactura = cantidad_litros * PRECIOLTPEROXIDO
        
    if producto == 3:
        codigo_articulo = CODALCOHOL
        cantidad_litros = int(input(">>Ingrese litros a vender: "))
        precio_litro = PRECIOALCOHOL
        valor_pagarfactura = cantidad_litros * PRECIOALCOHOL
    
    #facturacion total y conteo de facturas mayores a $600
    facturacion_total += valor_pagarfactura
    if valor_pagarfactura >= 600:
        facturas_mayorvalor600 += 1
    
    #imprimir factura
    print(f"Imprimiendo...\n Nro FACTURA |\tCOD PRODUCTO |\tCANTIDAD |\tPRECIO \n\t{codigo_factura}\t\t{codigo_articulo}\t\t\t{cantidad_litros}\t\t\t{precio_litro}\t\t\t\t\t\t\t\n Total: ${valor_pagarfactura}\n######")
        
#imprimir resumen
print(f"\n\nFacturación total: ${facturacion_total} \nCant Litros Producto 1: {cantidad_litrosArt1} \nFacturas mayor $600 : {facturas_mayorvalor600}")