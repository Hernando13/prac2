import funciones_generales as f
from Clases.Cliente import Cliente
clientes = []


def gestion_clientes(clients):
    while True:
        global clientes
        clientes = clients
        mensaje = ">> Gestión de clientes <<\n" + \
            "\n1. Registrar cliente nuevo" + \
            "\n2. Modificar información de cliente" + \
            "\n3. Eliminar Cliente" + \
            "\n4. Buscar Cliente" + \
            "\n5. Volver al menú principal"

        f.pt(mensaje)
        opcion = f.ingresar_opcion()

        if opcion == 1:
            registrar_cliente()
        elif opcion == 2:
            modificar_cliente()
        elif opcion == 3:
            eliminar_cliente()
        elif opcion == 4:
            buscar_cliente()
        elif opcion == 5:
            f.print_lista_clientes(clientes)
            return clientes
        else:
            f.pls()
            print(" !!!!!! Opción no válida !!!!!!")


def registrar_cliente():
    while True:
        f.pls()
        print(">> Registrar nuevo cliente <<")

        f.pt("¿Cliente Natural o Jurídico? (1. Natural / 2. Jurídico)")

        opcion = input("Ingrese una opción: ")
        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > 2:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            opcion = input("Ingrese una opción: ")
            opcion = f.checkear_numero(opcion)

        if opcion == 1:
            nombre = input("Ingrese el nombre completo de la persona: ")
            cedula = input("Ingrese la cédula de la persona: ")
            correo = input("Ingrese el correo de la persona: ")
            direccion = input("Ingrese la dirección de envió de la persona: ")
            telefono = input("Ingrese el teléfono de la persona: ")

            cliente_temp = Cliente(
                nombre, opcion, cedula, correo, direccion, telefono)
            clientes.append(cliente_temp)
            return

        elif opcion == 2:
            nombre = input("Ingrese el nombre de la empresa: ")
            rif = input("Ingrese el RIF de la empresa: ")
            correo = input("Ingrese el correo de la empresa: ")
            direccion = input("Ingrese la dirección de envió de la empresa: ")
            telefono = input("Ingrese el teléfono de la empresa: ")

            cliente_temp = Cliente(nombre, opcion, rif,
                                   correo, direccion, telefono)
            clientes.append(cliente_temp)
            return


def modificar_cliente():
    while True:
        cliente_a_modificar = {}
        f.print_lista_clientes(clientes)
        f.pls()
        print(">> Modificar clientes <<\n")
        opcion = input(
            "Ingrese el número del cliente que desea modificar (0. Cancelar): ")

        if opcion == "0" or opcion == 0:
            return

        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > len(clientes):
            f.pt(" !!!!!! El número ingresado no es válido !!!!!!")
            opcion = input(
                "Ingrese el número del cliente que desea modificar (0. Cancelar): ")
            if opcion == "0":
                return
            opcion = f.checkear_numero(opcion)

        cliente_a_modificar = clientes[opcion - 1]
        cliente_a_modificar.print_cliente()
        f.pt("¿Quieres modificar este cliente? (1. Si / 2. No)")

        opcion = input("Ingrese una opción: ")
        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > 2:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            opcion = input("Ingrese una opción: ")
            opcion = f.checkear_numero(opcion)

        if opcion == 2:
            continue

        f.pt("¿Qué campo quieres modificar? (1. Nombre / 2. Cédula/RIF / 3. Correo / 4. Dirección / 5. Teléfono / 6.Cancelar)")
        opcion = input("Ingrese una opción: ")
        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > 6:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            opcion = input("Ingrese una opción: ")
            opcion = f.checkear_numero(opcion)

        if opcion == 6:
            continue

        f.pls()
        if opcion == 1:
            nombre = input("Ingrese el nuevo nombre: ")
            cliente_a_modificar.modificar(name=nombre)
        elif opcion == 2:
            i_d = input("Ingrese la nueva cédula/RIF: ")
            cliente_a_modificar.modificar(i_d=i_d)
        elif opcion == 3:
            correo = input("Ingrese el nuevo correo: ")
            cliente_a_modificar.modificar(email=correo)
        elif opcion == 4:
            direccion = input("Ingrese la nueva dirección: ")
            cliente_a_modificar.modificar(address=direccion)
        elif opcion == 5:
            telefono = input("Ingrese el nuevo teléfono: ")
            cliente_a_modificar.modificar(phone=telefono)

        f.pt(">>> Cliente modificado con éxito <<<")


def eliminar_cliente():
    while True:
        cliente_a_eliminar = {}
        numero_cliente = 0
        f.print_lista_clientes(clientes)
        f.pls()
        print(">> Eliminar clientes <<\n")
        opcion = input(
            "Ingrese el número del cliente que desea eliminar (0. Cancelar): ")

        if opcion == "0":
            return

        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > len(clientes):
            f.pt(" !!!!!! El número ingresado no es válido !!!!!!")
            opcion = input(
                "Ingrese el número del cliente que desea eliminar (0. Cancelar): ")
            if opcion == "0":
                return
            opcion = f.checkear_numero(opcion)

        numero_cliente = opcion - 1
        cliente_a_eliminar = clientes[numero_cliente]
        cliente_a_eliminar.print_cliente()

        f.pt("¿Quieres eliminar este cliente? (1. Si / 2. No)")

        opcion = input("Ingrese una opción: ")
        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > 2:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            opcion = input("Ingrese una opción: ")
            opcion = f.checkear_numero(opcion)

        if opcion == 2:
            continue

        clientes.pop(numero_cliente)
        f.pt(">>> Cliente eliminado con éxito <<<")


def buscar_cliente():
    while True:
        resultado = []
        mensaje = ">> Buscar clientes <<\n" + \
            "\n1. Buscar por nombre" + \
            "\n2. Buscar por cédula/RIF" + \
            "\n3. Buscar por correo" + \
            "\n4. Buscar por dirección" + \
            "\n5. Buscar por teléfono" + \
            "\n6. Imprimir todos los clientes" + \
            "\n7. Volver al menú de gestión de clientes"

        f.pt(mensaje)
        opcion = f.ingresar_opcion()

        if opcion == 1:
            resultado = []
            f.pt(">> Buscar por nombre <<")
            nombre = input("Ingrese el nombre: ")
            f.pli()

            for cliente in clientes:
                if cliente.name == nombre:
                    resultado.append(cliente)
        elif opcion == 2:
            resultado = []
            f.pt(">> Buscar por cédula/RIF <<")
            i_d = input("Ingrese el cédula/RIF: ")
            f.pli()

            for cliente in clientes:
                if cliente.i_d == i_d:
                    resultado.append(cliente)
        elif opcion == 3:
            resultado = []
            f.pt(">> Buscar por correo <<")
            correo = input("Ingrese el correo: ")
            f.pli()

            for cliente in clientes:
                if cliente.email == correo:
                    resultado.append(cliente)
        elif opcion == 4:
            resultado = []
            f.pt(">> Buscar por dirección <<")
            direccion = input("Ingrese el dirección: ")
            f.pli()

            for cliente in clientes:
                if cliente.name == direccion:
                    resultado.append(cliente)
        elif opcion == 5:
            resultado = []
            f.pt(">> Buscar por teléfono <<")
            telefono = input("Ingrese el teléfono: ")
            f.pli()

            for cliente in clientes:
                if cliente.name == telefono:
                    resultado.append(cliente)
        elif opcion == 6:
            resultado = clientes
        elif opcion == 7:
            return
        else:
            f.pls()
            print(" !!!!!! Opción no válida !!!!!!")

        f.print_lista_clientes(resultado)
