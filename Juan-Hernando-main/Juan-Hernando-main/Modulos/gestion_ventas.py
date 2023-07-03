import funciones_generales as f
import Clases.Cliente as Cliente
import Clases.Venta as Venta
ventas = []
clientes = []
productos = []
comprados = []


def gestion_ventas(vents, clients, products):
    while True:
        global ventas
        global clientes
        global productos
        ventas = vents
        clientes = clients
        productos = products
        mensaje = ">> Gestión de ventas <<\n" + \
            "\n1. Registrar venta" + \
            "\n2. Buscar factura" + \
            "\n4. Volver al menú principal"

        f.pt(mensaje)
        opcion = f.ingresar_opcion()

        if opcion == 1:
            registrar_venta()
        elif opcion == 2:
            buscar_venta()
        elif opcion == 3:
            return ventas
        else:
            f.pls()
            print(" !!!!!! Opción no válida !!!!!!")


def agregar_producto():
    if len(productos) == 0:
        f.pt(" !!!!!! No hay productos registrados en el sistema !!!!!!")
        print(
            " !!!!!! Por favor registre un producto antes de registrar una venta !!!!!!")
        return None

    f.print_lista_productos(productos)
    opcion = input(
        "Ingrese el número del producto a comprar (0. Cancelar): ")

    if opcion == "0" or opcion == 0:
        return None
    opcion = f.checkear_numero(opcion)

    while opcion == False or opcion > len(productos):
        f.pt(" !!!!!! El número ingresado no es válido !!!!!!")
        opcion = input(
            "Ingrese el número del producto a comprar (0. Cancelar): ")

        if opcion == "0" or opcion == 0:
            return None
        opcion = f.checkear_numero(opcion)

    if productos[opcion - 1].inventory == 0:
        f.pt(" !!!!!! El producto seleccionado no tiene inventario disponible !!!!!!")
        return None

    producto = productos[opcion - 1]

    f.pls()
    cantidad = input("Ingrese la cantidad a comprar: ")
    cantidad = f.checkear_numero(cantidad)

    while cantidad == False or cantidad > producto.inventory:
        f.pt(" !!!!!! La cantidad ingresada no es válida !!!!!!")
        cantidad = input("Ingrese la cantidad a comprar: ")
        cantidad = f.checkear_numero(cantidad)

    producto.inventory -= cantidad

    comprado = [producto, cantidad]
    return comprado


def registrar_venta():
    while True:
        global comprados
        f.pls()
        print(">> Registrar venta <<")

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

        f.pls()
        print(">> Agregar productos a la venta <<\n")

        comprado = agregar_producto()
        if comprado == None:
            return
        elif comprado != None:
            comprados.append(comprado)

        while True:
            f.pls()
            opcion = input(
                "¿Desea agregar otro producto a la venta? (1. Sí, 2. No): ")
            f.pli()

            opcion = f.checkear_numero(opcion)

            if opcion == 1:
                comprado = agregar_producto()
                if comprado == None:
                    return
                elif comprado != None:
                    comprados.append(comprado)

            elif opcion == 2:
                break

        f.pt("¿Tipo de pago? (1. PdV / 2. PM / 3. Zelle / 4. Cash)")
        tipo = input("Ingrese una opción: ")
        tipo = f.checkear_numero(tipo)

        while tipo == False or tipo > 4:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            tipo = input("Ingrese una opción: ")
            tipo = f.checkear_numero(tipo)

        f.pt("¿Tipo de envío? (1. MRW / 2. Zoom / 3. Delivery)")
        envio = input("Ingrese una opción: ")
        envio = f.checkear_numero(envio)

        while envio == False or envio > 3:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            envio = input("Ingrese una opción: ")
            envio = f.checkear_numero(envio)

        subtotal = 0
        for n in comprados:
            subtotal += n[0].price * n[1]

        descuento = 0
        if cliente.type == 2:
            descuento += subtotal * 0.05

        iva = subtotal * 0.16

        igtf = 0
        if tipo == 3:
            igtf += subtotal * 0.03

        total = subtotal + iva + igtf - descuento

        f.pls()
        fecha = input("Ingrese la fecha del pago(dd/mm/aaaa): ")
        fecha = f.checkear_fecha(fecha)

        while fecha == False:
            f.pt(" !!!!!! La fecha ingresada no es válida !!!!!!")
            fecha = input("Ingrese la fecha(dd/mm/aaaa): ")
            fecha = f.checkear_fecha(fecha)

        if cliente.type == 2:
            f.pt("¿Plazo de pago? (1. 30 días / 2. 15 días")
            plazo = input("Ingrese una opción: ")
            plazo = f.checkear_numero(plazo)

            while plazo == False or plazo > 2:
                f.pt(" !!!!!! Opción no válida !!!!!!")
                plazo = input("Ingrese una opción: ")
                plazo = f.checkear_numero(plazo)

            if plazo == 1:
                plazo = 30
            elif plazo == 2:
                plazo = 15

            venta = Venta.Venta(cliente, comprados, fecha, tipo,
                                envio, subtotal, iva, descuento, igtf, total, plazo)

        venta = Venta.Venta(cliente, comprados, fecha, tipo,
                            envio, subtotal, iva, descuento, igtf, total)

        ventas.append(venta)
        venta.print_venta()
        f.pt(">>> Venta registrada con éxito <<<")


def buscar_venta():
    while True:
        f.pls()
        print(">> Buscar venta <<")
        f.pt("¿Qué desea hacer?\n" +
             "1. Buscar por cliente\n" +
             "2. Buscar por fecha\n" +
             "3. Buscar por monto total\n" +
             "4. Volver al menú principal")

        opcion = input("Ingrese una opción: ")
        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > 4:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            opcion = input("Ingrese una opción: ")
            opcion = f.checkear_numero(opcion)

        if opcion == 1:
            resultado = buscar_venta_cliente()
        elif opcion == 2:
            resultado = buscar_venta_fecha()
        elif opcion == 3:
            resultado = buscar_venta_monto()
        elif opcion == 4:
            return

        if len(resultado) == 0:
            f.pt(" !!!!!! No se encontraron ventas con los criterios ingresados !!!!!!")
            return

        f.print_lista_ventas(resultado)


def buscar_venta_cliente():
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

    for venta in ventas:
        if venta.cliente == cliente:
            resultado.append(venta)

    return resultado


def buscar_venta_fecha():
    resultado = []

    f.pt(">> Buscar por fecha <<")
    fecha = input("Ingrese la fecha(dd/mm/aaaa): ")
    fecha = f.checkear_fecha(fecha)

    while fecha == False:
        f.pt(" !!!!!! La fecha ingresada no es válida !!!!!!")
        fecha = input("Ingrese la fecha(dd/mm/aaaa): ")
        fecha = f.checkear_fecha(fecha)

    for venta in ventas:
        if venta.fecha == fecha:
            resultado.append(venta)

    return resultado


def buscar_venta_monto():
    resultado = []

    f.pt(">> Buscar por monto total (montos mayores al número ingresado) <<")
    monto = input("Ingrese el monto total: ")
    monto = f.checkear_numero(monto)

    while monto == False:
        f.pt(" !!!!!! El monto ingresado no es válido !!!!!!")
        monto = input("Ingrese el monto total: ")
        monto = f.checkear_numero(monto)

    for venta in ventas:
        if venta.total >= monto:
            resultado.append(venta)

    return resultado
