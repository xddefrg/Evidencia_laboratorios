
productos = ["Teclado", "Mouse"]

nuevo_producto = input("Nombre del producto nuevo: ")

if nuevo_producto == "":
    print("No puede registrarse un producto vacío.")
elif nuevo_producto in productos:
    print("El producto ya está repetido.")
else:
    productos.append(nuevo_producto)
    print("Producto agregado correctamente.")

print("Lista de productos:", productos)