# - Crear un programa que permita el modelamiento de Clientes en una página de compras. 
#       . Se debe utilizar el concepto de Programación Orientada a Objetos y lo aprendido en clase.
#       . Se evaluará el uso correcto de atributos y métodos.

# "La Clase Cliente debe tener mínimo 4 atributos y 2 métodos.
# - Se debe utilizar el método __str__() para darle nombre a los objetos.
#       . Es opcional el uso de herencia."

from clientes import Cliente
from productos import obtener_lista_productos

cliente1 = Cliente()
print(cliente1)

productos = obtener_lista_productos()

print("Productos disponibles:")
for i, producto in enumerate(productos, start=1):
    print(f"{i}. {producto}")

opcion = int(input("Ingrese el número del producto que desea comprar: "))

cliente1.realizar_compra(productos, "Walmart", opcion)
cliente1.enviar_factura()






