
productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]
disponibles = [
    producto["nombre"]
    for producto in productos
    if producto["cantidad"] > 0
]
print("Productos disponibles:", disponibles)

valores = [
    producto["precio"] * producto["cantidad"]
    for producto in productos
]
print("Valor total:", sum(valores))
sin_existencias = [
    producto["nombre"]
    for producto in productos
    if producto["cantidad"] == 0
]
print("Sin existencias:", sin_existencias)
precios_altos = [
    producto["nombre"]
    for producto in productos
    if producto["precio"] > 100000
]
print("Precio superior a $100.000:", precios_altos)

cantidades = {
    producto["cantidad"]
    for producto in productos
}
print("Cantidades diferentes:", cantidades)

catalogo_precios = {
    producto["nombre"]: producto["precio"]
    for producto in productos
}
print("Catálogo de precios:", catalogo_precios)