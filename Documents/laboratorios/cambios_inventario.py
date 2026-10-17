productos = ["Teclado", "Mouse", "Monitor"]
nuevos = ["Impresora", "Cámara"]

productos[1] = "Mouse inalámbrico"
print("1. Reemplazo:", productos)

productos.insert(0, "Parlantes")
print("2. Inserción:", productos)


productos.extend(nuevos)
print("3. Extensión:", productos)

productos.remove("Monitor")
print("4. Eliminación:", productos)

extraido = productos.pop()
print("5. Elemento extraído:", extraido)
print("Lista final:", productos)