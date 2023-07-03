# Este módulo permitirá a los usuarios administrar los pagos realizados por los clientes en la tienda en línea. Para ello, se deberá desarrollar lo siguiente:
import funciones_generales as f
from Clases.Cliente import Cliente
from Clases.Pago import Pago
clientes = []
pagos = []


def gestion_pagos(clients, pays):
    while True:
        global clientes
        global pagos
        clientes = clients
        pagos = pays
        mensaje = ">> Gestión de pagos <<\n" + \
            "\n1. Registrar pago" + \
            "\n2. Buscar pagos" + \
            "\n3. Volver al menú principal"

        f.pt(mensaje)
        opcion = f.ingresar_opcion()

        if opcion == 1:
            registrar_pago()
        elif opcion == 2:
            buscar_pago()
        elif opcion == 3:
            return pagos
        else:
            f.pls()
            print(" !!!!!! Opción no válida !!!!!!")


def registrar_pago():
    while True:
        f.pls()
        print(">> Registrar nuevo pago <<")

        if len(clientes) == 0:
            f.pt(" !!!!!! No hay clientes registrados en el sistema !!!!!!")
            print(
                " !!!!!! Por favor registre un cliente antes de registrar un pago !!!!!!")
            return

        f.print_lista_clientes(clientes)
        opcion = input(
            "Ingrese el número del cliente asociado al pago (0. Cancelar): ")

        if opcion == "0" or opcion == 0:
            return
        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > len(clientes):
            f.pt(" !!!!!! El número ingresado no es válido !!!!!!")
            opcion = input(
                "Ingrese el número del cliente asociado al pago (0. Cancelar): ")

            if opcion == "0" or opcion == 0:
                return
            opcion = f.checkear_numero(opcion)

        cliente = clientes[opcion - 1]

        monto = input("Ingrese el monto del pago: ")
        monto = f.checkear_numero(monto)

        while monto == False:
            f.pt(" !!!!!! El monto no es un número válido !!!!!!")
            monto = input("Ingrese el monto del pago: ")
            monto = f.checkear_numero(monto)

        f.pt("¿Moneda? (1. Dolar / 2. Bolivar / 3. Euro)")
        moneda = input("Ingrese una opción: ")
        moneda = f.checkear_numero(moneda)

        while moneda == False or moneda > 3:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            moneda = input("Ingrese una opción: ")
            moneda = f.checkear_numero(moneda)

        f.pt("¿Tipo de pago? (1. PdV / 2. PM / 3. Zelle / 4. Cash)")
        tipo = input("Ingrese una opción: ")
        tipo = f.checkear_numero(tipo)

        while tipo == False or tipo > 4:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            tipo = input("Ingrese una opción: ")
            tipo = f.checkear_numero(tipo)

        fecha = input("Ingrese la fecha del pago(dd/mm/aaaa): ")
        fecha = f.checkear_fecha(fecha)

        while fecha == False:
            f.pt(" !!!!!! La fecha ingresada no es válida !!!!!!")
            fecha = input("Ingrese la fecha(dd/mm/aaaa): ")
            fecha = f.checkear_fecha(fecha)

        pago_temp = Pago(cliente, monto, moneda, tipo, fecha)
        pagos.append(pago_temp)
        f.pt(">>> Pago registrado con éxito <<<")
        return


def buscar_pago():
    while True:
        resultado = []
        mensaje = ">> Buscar pagos <<\n" + \
            "\n1. Buscar por cliente" + \
            "\n2. Buscar por fecha" + \
            "\n3. Buscar por tipo de pago" + \
            "\n4. Buscar por moneda de pago" + \
            "\n5. Imprimir todos los pagos" + \
            "\n6. Volver al menú de gestión de pagos"

        f.pt(mensaje)
        opcion = f.ingresar_opcion()

        if opcion == 1:
            resultado = buscar_por_cliente()
        elif opcion == 2:
            resultado = buscar_por_fecha()
        elif opcion == 3:
            resultado = buscar_por_tipo()
        elif opcion == 4:
            resultado = buscar_por_moneda()
        elif opcion == 5:
            resultado = pagos
        elif opcion == 6:
            return
        else:
            f.pls()
            print(" !!!!!! Opción no válida !!!!!!")

        f.print_lista_pagos(resultado)


def buscar_por_cliente():
    resultado = []

    if len(clientes) == 0:
        f.pt(" !!!!!! No hay clientes registrados en el sistema !!!!!!")
        return resultado

    f.pt(">> Buscar por cliente <<")
    f.print_lista_clientes(clientes)
    opcion = input("Ingrese el número del cliente: ")
    opcion = f.checkear_numero(opcion)

    while opcion == False or opcion > len(clientes):
        f.pt(" !!!!!! El número ingresado no es válido !!!!!!")
        opcion = input("Ingrese el número del cliente: ")
        opcion = f.checkear_numero(opcion)

    cliente = clientes[opcion - 1]

    for pago in pagos:
        if pago.cliente == cliente:
            resultado.append(pago)

    return resultado


def buscar_por_fecha():
    resultado = []
    f.pt(">> Buscar por fecha <<")
    fecha = input("Ingrese la fecha(dd/mm/aaaa): ")
    fecha = f.checkear_fecha(fecha)

    while fecha == False:
        f.pt(" !!!!!! La fecha ingresada no es válida !!!!!!")
        fecha = input("Ingrese la fecha(dd/mm/aaaa): ")
        fecha = f.checkear_fecha(fecha)

    for pago in pagos:
        if pago.fecha == fecha:
            resultado.append(pago)

    return resultado


def buscar_por_tipo():
    resultado = []
    f.pt(">> Buscar por tipo de pago <<")
    f.pt("¿Tipo de pago? (1. PdV / 2. PM / 3. Zelle / 4. Cash)")
    tipo = input("Ingrese una opción: ")
    tipo = f.checkear_numero(tipo)

    while tipo == False or tipo > 4:
        f.pt(" !!!!!! Opción no válida !!!!!!")
        tipo = input("Ingrese una opción: ")
        tipo = f.checkear_numero(tipo)

    for pago in pagos:
        if pago.tipo == tipo:
            resultado.append(pago)

    return resultado


def buscar_por_moneda():
    resultado = []
    f.pt(">> Buscar por moneda de pago <<")
    f.pt("¿Moneda? (1. Dolar / 2. Bolivar / 3. Euro)")
    moneda = input("Ingrese una opción: ")
    moneda = f.checkear_numero(moneda)

    while moneda == False or moneda > 3:
        f.pt(" !!!!!! Opción no válida !!!!!!")
        moneda = input("Ingrese una opción: ")
        moneda = f.checkear_numero(moneda)

    for pago in pagos:
        if pago.moneda == moneda:
            resultado.append(pago)

    return resultado
