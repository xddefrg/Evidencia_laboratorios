def calcular_unidades(productos):
    total = 0

    for producto in productos:
        total += producto["cantidad"]

    return total


inventario = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 7}
]

print(calcular_unidades(inventario))  # 11


# --- Una función que MODIFICA la lista recibida ---
def agregar(nombre, nombres):
    nombres.append(nombre)


productos = ["Teclado"]
agregar("Mouse", productos)
# La lista original cambia: ambas referencias apuntan al mismo objeto.
print(productos)


# --- Una función que devuelve una lista NUEVA ---
def agregar_en_copia(nombre, nombres):
    copia = nombres.copy()
    copia.append(nombre)
    return copia


original = ["Teclado"]
nueva = agregar_en_copia("Mouse", original)

print("Original:", original)
print("Nueva:", nueva)


# --- Ejercicio: consultas de inventario ---
def agotados(productos):
    """Versión con for y append()."""
    nombres = []

    for producto in productos:
        if producto["cantidad"] == 0:
            nombres.append(producto["nombre"])

    return nombres


def agotados_comprension(productos):
    """Misma consulta con una comprensión de lista."""
    return [
        producto["nombre"]
        for producto in productos
        if producto["cantidad"] == 0
    ]


existencias = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 0},
    {"nombre": "Monitor", "cantidad": 0},
]

print("Agotados (for):", agotados(existencias))
print("Agotados (comprensión):", agotados_comprension(existencias))
