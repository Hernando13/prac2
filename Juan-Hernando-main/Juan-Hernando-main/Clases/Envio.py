import funciones_generales as f


class Envio:
    def __init__(self, venta, costo):
        self.venta = venta
        self.costo = costo

    def print_envio(self):
        self.venta.print_venta()
        print("Costo: " + str(self.costo))
