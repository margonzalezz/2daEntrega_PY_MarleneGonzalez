class Cliente:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.correo = input("Ingrese su correo electrónico: ")
        self.direccion = input("Ingrese su dirección: ")
        self.telefono = input("Ingrese su número de teléfono: ")

    def __str__(self):
        return f"Nombre: {self.nombre}\nCorreo electrónico: {self.correo}\nDirección: {self.direccion}\nTeléfono: {self.telefono}"

    def realizar_compra(self, productos, tienda, opcion):
        if opcion < 1 or opcion > len(productos):
            print("Opción inválida. No se realizó ninguna compra.")
        else:
            producto_elegido = productos[opcion - 1]
            print(f"El cliente {self.nombre} ha comprado {producto_elegido} en la tienda {tienda}")

    def enviar_factura(self):
        print(f"Se le ha enviado un correo con la factura de compra a {self.correo}")
