ventas = [
    {"producto": "Teclado", "categoria": "Periféricos", "total": 150000},
    {"producto": "Mouse", "categoria": "Periféricos", "total": 70000},
    {"producto": "Disco SSD", "categoria": "Componentes", "total": 280000},
    {"producto": "Memoria USB", "categoria": "Accesorios", "total": 45000}
]

productos_for = []

for venta in ventas:
    if venta["total"] > 100000:
        productos_for.append(venta["producto"])

print("Con ciclo for:", productos_for)

productos_comprension = [
    venta["producto"]
    for venta in ventas
    if venta["total"] > 100000
]

print("Con comprensión:", productos_comprension)

print("¿Son iguales?:", productos_for == productos_comprension)
categorias = {
    venta["categoria"]
    for venta in ventas
}

print("Categorías diferentes:", categorias)

catalogo_ventas = {
    venta["producto"]: venta["total"]
    for venta in ventas
}

print("Catálogo de ventas:", catalogo_ventas)

valores = [
    venta["total"]
    for venta in ventas
]

total_ventas = sum(valores)

print("Valores de las ventas:", valores)
print("Suma total de ventas:", total_ventas)