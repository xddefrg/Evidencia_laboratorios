productos = [
    {"codigo": 101, "nombre": "Teclado", "precio": 75000, "cantidad": 10},
    {"codigo": 102, "nombre": "Mouse", "precio": 35000, "cantidad": 15},
    {"codigo": 103, "nombre": "Monitor", "precio": 650000, "cantidad": 5}
]

codigo = int(input("Código del producto: "))
nombre = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad disponible: "))

nuevo_producto = {
    "codigo": codigo,
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
}

productos.append(nuevo_producto)


print("\nLista de productos:")

for producto in productos:
    print("--------------------")
    for clave, valor in producto.items():
        print(clave, ":", valor)