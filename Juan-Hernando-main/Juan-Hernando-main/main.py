# importar librerías externas ---------------------------------------------------------
import json
import requests

# importar funciones propias ----------------------------------------------------------
# f para no tener que escribir funciones_generales cada vez que llamas una funcion de este modulo
import funciones_generales as f
from Modulos.gestion_productos import gestion_productos
from Modulos.gestion_ventas import gestion_ventas
from Modulos.gestion_clientes import gestion_clientes
from Modulos.gestion_pagos import gestion_pagos
from Modulos.gestion_envios import gestion_envios

# clases propias -------------------------------------------------------------
from Clases.Producto import Producto
from Clases.Cliente import Cliente
from Clases.Pago import Pago

# variables globales ---------------------------------------------------------
productos = []  # Lista para almacenar los productos
clientes = []  # Lista para almacenar los clientes
ventas = []  # Lista para almacenar las ventas
pagos = []  # Lista para almacenar los pagos
envios = []  # Lista para almacenar los envios


def main():
    global productos
    global clientes
    api = False
    txt = False
    mensaje_carga = ">> Menu de Carga <<\n" + \
        "\n1. Cargar productos de API." + \
        "\n2. Cargar productos y clientes de TXT." + \
        "\n3. Continuar. \n4. Salir"
    f.pt("Bienvenido a la tienda de Toto...")
    while True:
        if api is True:
            mensaje_carga = "2. Cargar productos de TXT. \n3. Continuar. \n4. Salir"
        if txt is True:
            mensaje_carga = "1. Cargar productos de API. \n3. Continuar. \n4. Salir"
        if api is True and txt is True:
            mensaje_carga = "3. Continuar. \n4. Salir"
        f.pt(mensaje_carga)
        opcion = f.ingresar_opcion()

        if opcion == 1 and api is False:
            # Cargar productos desde la API y agregarlos a la lista global de productos
            productos_temp = cargar_productos()
            productos = productos + productos_temp
            api = True
        elif opcion == 2 and txt is False:
            # Cargar productos desde el archivo de texto y agregarlos a la lista global de productos
            productos_temp = cargar_productos_txt()
            productos = productos + productos_temp
            # Cargar clientes desde el archivo de texto y agregarlos a la lista global de clientes
            clientes_temp = cargar_clientes_txt()
            clientes = clientes + clientes_temp
            txt = True
        elif opcion == 3:
            menu()
        elif opcion == 4:
            SystemExit()
        else:
            f.pls()
            print(" !!!!!! Opción no válida !!!!!!")


def menu():
    global productos
    global clientes
    global ventas
    global pagos
    global envios
    while True:
        mensaje = ">> Menú principal <<\n" + \
            "\n1. Gestión de productos" + \
            "\n2. Gestión de ventas" + \
            "\n3. Gestión de clientes" + \
            "\n4. Gestión de pagos" + \
            "\n5. Gestión de envíos" + \
            "\n6. Indicadores de gestión (estadísticas)" + \
            "\n7. Salir"

        f.pt(mensaje)
        opcion = f.ingresar_opcion()

        if opcion == 1:
            # Llamar a la función de gestión de productos y actualizar la lista global de productos
            productos = gestion_productos(productos)
        elif opcion == 2:
            # Llamar a la función de gestión de ventas y actualizar la lista global de ventas
            ventas = gestion_ventas(ventas, clientes, productos)
        elif opcion == 3:
            # Llamar a la función de gestión de clientes y actualizar la lista global de clientes
            clientes = gestion_clientes(clientes)
        elif opcion == 4:
            f.pls()
            # Llamar a la función de gestión de pagos y actualizar la lista global de pagos
            pagos = gestion_pagos(clientes, ventas)
        elif opcion == 5:
            f.pls()
            envios = gestion_envios(ventas, envios)
        elif opcion == 6:
            f.pls()
            print(">> Indicadores de gestión (estadísticas) no implementado <<")
        elif opcion == 7:
            return
        else:
            f.pls()
            print(" !!!!!! Opción no válida !!!!!!")


def cargar_productos():
    # Carga los productos desde una API a una lista global
    productos_temp = []
    productos = []
    productos_temp = requests.get("https://raw.githubusercontent.com/Algoritmos-y" +
                                  "-Programacion-2223-3/api-proyecto/main/products.json")

    productos_temp = productos_temp.json()

    for producto in productos_temp:
        if "inventory" not in producto:
            # Crea un objeto Producto sin inventario si no se proporciona esa información en la API
            prod_temp = Producto(
                producto["name"],
                producto["description"],
                producto["price"],
                producto["category"]
            )
        else:
            # Crea un objeto Producto con inventario si se proporciona esa información en la API
            prod_temp = Producto(
                producto["name"],
                producto["description"],
                producto["price"],
                producto["category"],
                producto["inventory"]
            )

        productos.append(prod_temp)

    f.pt(" >>> Productos cargados con éxito desde API <<<")
    return productos


def cargar_clientes_txt():
    # Carga los clientes desde un archivo de texto a una lista global
    clientes_temp = []
    clientes = []
    try:
        clientes_temp = open("clientes.txt", "r")
    except FileNotFoundError:
        # Si el archivo no existe, se crea uno nuevo
        clientes_temp = open("clientes.txt", "x")
        clientes_temp = open("clientes.txt", "r")
    with open('clientes.txt') as doc2:
        clientes_temp = json.load(doc2)

    for cliente in clientes_temp:
        # Crea un objeto Cliente
        cliente_temp = Cliente(
            cliente["name"],
            cliente["tipo"],
            cliente["rif"],
            cliente["email"],
            cliente["address"],
            cliente["phone"]
        )

        clientes.append(cliente_temp)

    f.pt(" >>> Clientes cargados con éxito desde TXT <<<")
    return clientes


def cargar_productos_txt():
    # Carga los productos desde un archivo de texto a una lista global
    productos_temp = []
    productos = []
    try:
        productos_temp = open("products.txt", "r")
    except FileNotFoundError:
        # Si el archivo no existe, se crea uno nuevo
        productos_temp = open("products.txt", "x")
        productos_temp = open("products.txt", "r")
    with open('products.txt') as doc:
        productos_temp = json.load(doc)

    for producto in productos_temp:
        if "inventory" not in producto:
            # Crea un objeto Producto sin inventario si no se proporciona esa información en el archivo de texto
            prod_temp = Producto(
                producto["name"],
                producto["description"],
                producto["price"],
                producto["category"]
            )
        else:
            # Crea un objeto Producto con inventario si se proporciona esa información en el archivo de texto
            prod_temp = Producto(
                producto["name"],
                producto["description"],
                producto["price"],
                producto["category"],
                producto["inventory"]
            )

        productos.append(prod_temp)

    f.pt(" >>> Productos cargados con éxito desde TXT <<<")
    return productos


if __name__ == "__main__":
    main()
