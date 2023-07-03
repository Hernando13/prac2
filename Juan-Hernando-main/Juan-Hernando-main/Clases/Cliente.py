import funciones_generales as f


class Cliente:
    def __init__(self, name, tipo, cedula_rif, email, address, phone):
        self.name = name
        self.type = tipo
        self.i_d = cedula_rif
        self.email = email
        self.address = address
        self.phone = phone

    def print_cliente(self, id_cliente=None):
        f.pls()
        mensaje = ""
        if id_cliente != None:
            mensaje += str(id_cliente + 1) + ". >> "
        else:
            mensaje += ">> "

        mensaje += self.name + " <<"

        if self.type == 1:
            mensaje += "\nTipo: Persona Natural"
        elif self.type == 2:
            mensaje += "\nTipo: Persona Jurídica"

        mensaje += "\nCédula/RIF: " + str(self.i_d) + \
            "\nCorreo Electrónico: " + str(self.email) + \
            "\nDirección: " + str(self.address) + \
            "\nTeléfono: " + str(self.phone)

        print(mensaje)

    def modificar(self, name=None, i_d=None, email=None, address=None, phone=None):
        if name != None:
            self.name = name
        if i_d != None:
            self.i_d = i_d
        if email != None:
            self.email = email
        if address != None:
            self.address = address
        if self.phone != None:
            self.phone = phone
