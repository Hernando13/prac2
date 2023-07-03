import funciones_generales as f


class Producto:
    def __init__(self, name, description, price, category, inventory=0):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.inventory = inventory

    def print_producto(self, id_prod=None):
        f.pls()
        mensaje = ""
        if id_prod != None:
            mensaje += str(id_prod + 1) + ". >> "
        else:
            mensaje = ">> "

        mensaje += self.name + " <<" + \
            "\nDescripción: " + str(self.description) + \
            "\nPrecio: " + str(self.price) + \
            "\nCategoría: " + str(self.category) + \
            "\nInventario: " + \
            str(self.inventory)

        print(mensaje)

    def modificar(self, name=None, description=None, price=None, category=None, inventory=None):
        if name != None:
            self.name = name
        if description != None:
            self.description = description
        if price != None:
            self.price = price
        if category != None:
            self.category = category
        if self.inventory != None:
            self.inventory = inventory
