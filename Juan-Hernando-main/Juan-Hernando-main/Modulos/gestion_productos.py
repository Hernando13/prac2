import funciones_generales as f
from Clases.Producto import Producto
productos = []


def gestion_productos(prods):
    global productos
    productos = prods
    while True:
        mensaje = ">> Gestión de productos <<\n" + \
            "\n1. Agregar nuevo producto" + \
            "\n2. Buscar productos" + \
            "\n3. Modificar información de productos" + \
            "\n4. Eliminar productos" + \
            "\n5. Volver al menú principal"

        f.pt(mensaje)
        opcion = f.ingresar_opcion()

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            buscar_producto()
        elif opcion == 3:
            modificar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            return productos
        else:
            f.pls()
            print(" !!!!!! Opción no válida !!!!!!")


def agregar_producto():
    while True:
        f.pls()
        print(">> Agregar nuevo producto <<\n")

        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        precio = input("Ingrese el precio del producto: ")
        precio = f.checkear_numero(precio)
        categoria = input("Ingrese la categoría del producto: ")
        inventario = input("Ingrese el inventario disponible del producto: ")
        inventario = f.checkear_numero(inventario)

        if precio == False or inventario == False:
            f.pt(" !!!!!! El input de precio o de inventario no son numeros válidos !!!!!!")
        else:
            producto = Producto(nombre, descripcion,
                                precio, categoria, inventario)
            productos.append(producto)
            f.pt(">>> Producto agregado con éxito <<<")
            return


def buscar_producto():
    while True:
        resultado = []
        mensaje = ">> Buscar productos <<\n" + \
            "\n1. Buscar por categoría" + \
            "\n2. Buscar por precio" + \
            "\n3. Buscar por nombre" + \
            "\n4. Buscar por disponibilidad en inventario" + \
            "\n5. Imprimir todos los productos" + \
            "\n6. Volver al menú de gestión de productos"

        f.pt(mensaje)
        opcion = f.ingresar_opcion()

        if opcion == 1:
            resultado = buscar_por_categoria()
        elif opcion == 2:
            resultado = buscar_por_precio()
        elif opcion == 3:
            resultado = buscar_por_nombre()
        elif opcion == 4:
            resultado = buscar_por_disponibilidad()
        elif opcion == 5:
            resultado = productos
        elif opcion == 6:
            return
        else:
            f.pls()
            print(" !!!!!! Opción no válida !!!!!!")

        f.print_lista_productos(resultado)


def buscar_por_categoria():
    resultado = []
    f.pt(">> Buscar por categoría <<")
    categoria = input("Ingrese la categoría: ")
    f.pli()

    for producto in productos:
        if producto.category == categoria:
            resultado.append(producto)

    return resultado


def buscar_por_precio():
    resultado = []
    f.pt(">> Buscar por precio <<")
    precio = input("Ingrese el precio: ")
    f.pli()

    precio = f.checkear_numero(precio)

    if precio == False:
        f.pls()
        print(" !!!!!! El precio no es un número válido !!!!!!")
        buscar_por_precio()

    for producto in productos:
        if producto.price == precio:
            resultado.append(producto)

    return resultado


def buscar_por_nombre():
    resultado = []
    f.pt(">> Buscar por nombre <<")
    nombre = input("Ingrese el nombre: ")
    f.pli()

    for producto in productos:
        if producto.name == nombre:
            resultado.append(producto)

    return resultado


def buscar_por_disponibilidad():
    resultado = []
    f.pt(">> Buscar por disponibilidad de inventario <<")
    disponibilidad = input("Ingrese el numero de inventario: ")
    f.pli()

    disponibilidad = f.checkear_numero(disponibilidad)

    if disponibilidad == False:
        f.pls()
        print(" !!!!!! El inventario no es un número válido !!!!!!")
        buscar_por_disponibilidad()

    for producto in productos:
        if producto.inventory == disponibilidad:
            resultado.append(producto)

    return resultado


def modificar_producto():
    while True:
        producto_a_modificar = {}
        f.print_lista_productos(productos)
        f.pls()
        print(">> Modificar productos <<\n")
        opcion = input(
            "Ingrese el número del producto que desea modificar (0. Cancelar): ")

        if opcion == "0" or opcion == 0:
            return

        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > len(productos):
            f.pt(" !!!!!! El número ingresado no es válido !!!!!!")
            opcion = input(
                "Ingrese el número del producto que desea modificar (0. Cancelar): ")
            if opcion == "0":
                return
            opcion = f.checkear_numero(opcion)

        producto_a_modificar = productos[opcion - 1]
        producto_a_modificar.print_producto()
        f.pt("¿Quieres modificar este producto? (1. Si / 2. No)")

        opcion = input("Ingrese una opción: ")
        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > 2:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            opcion = input("Ingrese una opción: ")
            opcion = f.checkear_numero(opcion)

        if opcion == 2:
            continue

        f.pt("¿Qué campo quieres modificar? (1. Nombre / 2. Descripción / 3. Precio / 4. Categoría / 5. Inventario / 6.Cancelar)")
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
            producto_a_modificar.modificar(name=nombre)
        elif opcion == 2:
            descripcion = input("Ingrese la nueva descripción: ")
            producto_a_modificar.modificar(description=descripcion)
        elif opcion == 3:
            precio = input("Ingrese el nuevo precio: ")
            precio = f.checkear_numero(precio)
            if precio == False:
                f.pt(" !!!!!! El precio ingresado no es válido !!!!!!")
                continue
            producto_a_modificar.modificar(price=precio)
        elif opcion == 4:
            categoria = input("Ingrese la nueva categoría: ")
            producto_a_modificar.modificar(category=categoria)
        elif opcion == 5:
            inventario = input("Ingrese el nuevo inventario: ")
            inventario = f.checkear_numero(inventario)
            if inventario == False:
                f.pt(" !!!!!! El inventario ingresado no es válido !!!!!!")
                continue
            producto_a_modificar.modificar(inventory=inventario)

        f.pt(">>> Producto modificado con éxito <<<")


def eliminar_producto():
    while True:
        producto_a_eliminar = {}
        numero_producto = 0
        f.print_lista_productos(productos)
        f.pls()
        print(">> Eliminar productos <<\n")
        opcion = input(
            "Ingrese el número del producto que desea eliminar (0. Cancelar): ")

        if opcion == "0":
            return

        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > len(productos):
            f.pt(" !!!!!! El número ingresado no es válido !!!!!!")
            opcion = input(
                "Ingrese el número del producto que desea eliminar (0. Cancelar): ")
            if opcion == "0":
                return
            opcion = f.checkear_numero(opcion)

        numero_producto = opcion - 1
        producto_a_eliminar = productos[numero_producto]
        producto_a_eliminar.print_producto()

        f.pt("¿Quieres eliminar este producto? (1. Si / 2. No)")

        opcion = input("Ingrese una opción: ")
        opcion = f.checkear_numero(opcion)

        while opcion == False or opcion > 2:
            f.pt(" !!!!!! Opción no válida !!!!!!")
            opcion = input("Ingrese una opción: ")
            opcion = f.checkear_numero(opcion)

        if opcion == 2:
            continue

        productos.pop(numero_producto)
        f.pt(">>> Producto eliminado con éxito <<<")
