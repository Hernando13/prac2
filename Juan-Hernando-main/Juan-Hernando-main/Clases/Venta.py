import funciones_generales as f


class Venta:
    def __init__(self, cliente, productos, fecha, metodo_pago, metodo_entrega, subtotal, iva, descuento, igtf, total, plazo=1):
        self.cliente = cliente
        self.productos = productos
        self.fecha = fecha
        self.metodo_pago = metodo_pago
        self.metodo_entrega = metodo_entrega
        self.subtotal = subtotal
        self.iva = iva
        self.descuento = descuento
        self.igtf = igtf
        self.total = total
        self.plazo = plazo
        self.pago_dia = total/plazo

    def print_venta(self, id_venta=None):
        f.pls()
        mensaje = ""
        if id_venta != None:
            mensaje += str(id_venta + 1) + ". >> "
        else:
            mensaje += ">> "

        mensaje += self.cliente.name + " <<"

        mensaje += "\nProductos: "
        for prod in self.productos:
            mensaje += "\n\t" + prod[0].name
            mensaje += "\n\t\tCantidad: " + str(prod[1])

        if self.metodo_pago == 1:
            pago = "PdV"
        elif self.metodo_pago == 2:
            pago = "PM"
        elif self.metodo_pago == 3:
            pago = "Zelle"

        if self.metodo_entrega == 1:
            envio = "MRW"
        elif self.metodo_entrega == 2:
            envio = "Zoom"
        elif self.metodo_entrega == 3:
            envio = "Delivery"

        mensaje += "\nFecha: " + str(self.fecha) + \
            "\nMétodo de pago: " + str(pago) + \
            "\nMétodo de entrega: " + str(envio) + \
            "\nSubtotal: " + str(self.subtotal) + \
            "\nIVA: " + str(self.iva) + \
            "\nDescuento: " + str(self.descuento) + \
            "\nIGTF: " + str(self.igtf) + \
            "\nTotal: " + str(self.total)

        if self.plazo != 1:
            mensaje += "\nPlazo: " + str(self.plazo) + " días" + \
                "\nPago diario: " + str(self.pago_dia)

        print(mensaje)

    def modificar(self, cliente=None, productos=None, fecha=None, metodo_pago=None, metodo_entrega=None, subtotal=None, iva=None, descuento=None, igtf=None, total=None):
        if cliente != None:
            self.cliente = cliente
        if productos != None:
            self.productos = productos
        if fecha != None:
            self.fecha = fecha
        if metodo_pago != None:
            self.metodo_pago = metodo_pago
        if metodo_entrega != None:
            self.metodo_entrega = metodo_entrega
        if subtotal != None:
            self.subtotal = subtotal
        if iva != None:
            self.iva = iva
        if descuento != None:
            self.descuento = descuento
        if igtf != None:
            self.igtf = igtf
        if total != None:
            self.total = total
