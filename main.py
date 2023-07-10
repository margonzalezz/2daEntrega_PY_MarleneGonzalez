# - Crear un programa que permita el modelamiento de Clientes en una página de compras. 
#       . Se debe utilizar el concepto de Programación Orientada a Objetos y lo aprendido en clase.
#       . Se evaluará el uso correcto de atributos y métodos.

# "La Clase Cliente debe tener mínimo 4 atributos y 2 métodos.
# - Se debe utilizar el método __str__() para darle nombre a los objetos.
#       . Es opcional el uso de herencia."

class Cliente:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.correo = input("Ingrese su correo electrónico: ")
        self.direccion = input("Ingrese su dirección para poder enviarle su producto: ")
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


# Ejemplo de uso
cliente1 = Cliente()
print(cliente1)

productos = [
    "Laptop",
    "Teléfono",
    "Tablet",
    "Smartwatch",
    "Cámara",
    "TV",
    "Auriculares",
    "Altavoces",
    "Consola de videojuegos"
]

print("Productos disponibles:")
for i, producto in enumerate(productos, start=1):
    print(f"{i}. {producto}")

opcion = int(input("Ingrese el número del producto que desea comprar: "))

cliente1.realizar_compra(productos, "Walmart", opcion)
cliente1.enviar_factura()





