# FUNCIONES GENERALES -----------------------------------------------------------------------------------------------
from datetime import datetime


def pt(string):  # imprimir titulo
    pls()
    print(string)
    pls()


def pli():  # imprimir linea inferior
    print("\n-------------------------------------------------")


def pls():  # imprimir linea superior
    print("\n-------------------------------------------------\n")


def checkear_numero(numero):  # checkear si el input es un numero
    try:
        numero = int(numero)
        if numero < 0:
            return False
        return numero
    except ValueError:
        return False


def ingresar_opcion():  # ingresar opcion de menu
    opcion = input("Ingrese una opción: ")
    opcion = checkear_numero(opcion)
    pli()

    if opcion == False:
        return 0

    return opcion


def print_lista_productos(productos):  # imprimir lista completa de productos
    if len(productos) == 0:
        pls()
        print(" !!!! No se encontraron productos !!!!")
        return

    mensaje = " >> Productos encontrados <<\n(subir para ver lista completa)"
    for i, producto in enumerate(productos):
        producto.print_producto(i)

    pt(mensaje)


def print_lista_clientes(clientes):  # imprimir lista completa de clientes
    if len(clientes) == 0:
        pls()
        print(" !!!! No se encontraron clientes !!!!")
        return

    mensaje = " >> Clientes encontrados <<\n(subir para ver lista completa)"
    for i, cliente in enumerate(clientes):
        cliente.print_cliente(i)

    pt(mensaje)


def print_lista_pagos(pagos):  # imprimir lista completa de pagos
    if len(pagos) == 0:
        pls()
        print(" !!!! No se encontraron pagos !!!!")
        return

    mensaje = " >> Pagos encontrados <<\n(subir para ver lista completa)"
    for i, pago in enumerate(pagos):
        pago.print_pago(i)

    pt(mensaje)


def print_lista_ventas(ventas):  # imprimir lista completa de ventas
    if len(ventas) == 0:
        pls()
        print(" !!!! No se encontraron ventas !!!!")
        return

    mensaje = " >> Ventas encontradas <<\n(subir para ver lista completa)"
    for i, venta in enumerate(ventas):
        venta.print_venta(i)

    pt(mensaje)


def checkear_fecha(fecha):  # checkear si el input es una fecha valida
    try:
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        return fecha
    except ValueError:
        return False
