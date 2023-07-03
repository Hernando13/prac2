import funciones_generales as f


class Pago:
    def __init__(self, cliente, monto, moneda, tipo, fecha):
        self.cliente = cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo = tipo
        self.fecha = fecha

    def print_pago(self, id_pago=None):
        f.pls()
        moneda = ""
        if self.moneda == 1:
            moneda = "Dolar"
        elif self.moneda == 2:
            moneda = "Bolivar"
        elif self.moneda == 3:
            moneda = "Euro"

        tipo = ""
        if self.tipo == 1:
            tipo = "PdV"
        elif self.tipo == 2:
            tipo = "PM"
        elif self.tipo == 3:
            tipo = "Zelle"
        elif self.tipo == 4:
            tipo = "Cash"

        mensaje = ""
        if id_pago != None:
            mensaje += str(id_pago + 1) + ". >> "
        else:
            mensaje += ">> "

        mensaje += self.cliente.name + " <<"

        mensaje += "\nMonto: " + str(self.monto) + \
            "\nMoneda: " + str(moneda) + \
            "\nTipo: " + str(tipo) + \
            "\nFecha: " + str(self.fecha)

        print(mensaje)

    def modificar(self, cliente=None, monto=None, moneda=None, tipo=None, fecha=None):
        if cliente != None:
            self.cliente = cliente
        if monto != None:
            self.monto = monto
        if moneda != None:
            self.moneda = moneda
        if tipo != None:
            self.tipo = tipo
        if self.fecha != None:
            self.fecha = fecha
