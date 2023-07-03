import funciones_generales as f
from Clases.Venta import Venta
from Clases.Envio import Envio
ventas = []
envios = []


def gestion_envios(sells, sends):
    while True:
        global ventas
        global envios
        ventas = sells
        envios = sends
        mensaje = ">> Gestión de clientes <<\n" + \
            "\n1. Registrar envió nuevo" + \
            "\n2. Buscar envió" + \
            "\n3. Volver al menú principal"

        f.pt(mensaje)
        opcion = f.ingresar_opcion()

        if opcion == 1:
            registrar_envio()
        elif opcion == 2:
            for envio in envios:
                envio.print_envio()
        elif opcion == 3:
            return envios
        else:
            f.pls()
            print(" !!!!!! Opción no válida !!!!!!")


def registrar_envio():
    while True:
        f.pls()
        print(">> Registrar nuevo envio <<")

        if len(ventas) == 0:
            f.pt(" !!!!!! No hay ventas registrados en el sistema !!!!!!")
            print(
                " !!!!!! Por favor registre una venta antes de registrar un envio !!!!!!")
            return

        f.print_lista_ventas(ventas)
        opcion = input(
            "Ingrese el número de la venta asociada al envio (0. Cancelar): ")

        if opcion == "0" or opcion == 0:
            return
        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > len(ventas):
            f.pt(" !!!!!! El número ingresado no es válido !!!!!!")
            opcion = input(
                "Ingrese el número de la venta asociada al envio (0. Cancelar): ")

            if opcion == "0" or opcion == 0:
                return
            opcion = f.checkear_numero(opcion)

        venta = ventas[opcion - 1]

        # ingrese monto del envio
        monto = input("Ingrese el monto del envio: ")
        monto = f.checkear_numero(monto)

        while monto == False:
            f.pt(" !!!!!! El monto ingresado no es válido !!!!!!")
            monto = input("Ingrese el monto del envio: ")
            monto = f.checkear_numero(monto)

        envio = Envio(venta, monto)
        envios.append(envio)
