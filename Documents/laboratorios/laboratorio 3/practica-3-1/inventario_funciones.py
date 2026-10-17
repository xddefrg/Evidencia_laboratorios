def mostrar_productos(productos):
    for producto in productos:
        print(
            f"{producto['codigo']} - {producto['nombre']} - "
            f"${producto['precio']} - {producto['cantidad']} unidades"
        )


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def valor_inventario(productos):
    total = 0

    for producto in productos:
        total += producto["precio"] * producto["cantidad"]

    return total


def productos_sin_stock(productos):
    return [
        producto["nombre"]
        for producto in productos
        if producto["cantidad"] == 0
    ]


def main():
    productos = [
        {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
        {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 0},
        {"codigo": "P003", "nombre": "Monitor", "precio": 700000, "cantidad": 2},
    ]

    print("Productos:")
    mostrar_productos(productos)

    print()
    encontrado = buscar_producto(productos, "P003")
    print("Búsqueda de P003:", encontrado)
    print("Búsqueda de P999:", buscar_producto(productos, "P999"))

    print()
    print("Valor del inventario:", valor_inventario(productos))
    print("Sin stock:", productos_sin_stock(productos))


if __name__ == "__main__":
    main()
