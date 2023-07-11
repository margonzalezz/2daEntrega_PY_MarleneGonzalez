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






