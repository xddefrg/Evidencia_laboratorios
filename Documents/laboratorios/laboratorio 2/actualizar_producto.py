producto = {
    "codigo": 101,
    "nombre": "Teclado",
    "precio": 75000,
    "cantidad": 10
}

nuevo_precio = float(input("Ingresa el nuevo precio: "))

if nuevo_precio > 0:
    producto["precio"] = nuevo_precio
    print("Precio actualizado correctamente.")
else:
    print("Error: el precio debe ser mayor que cero.")

print("\nDatos del producto:")

for clave, valor in producto.items():
    print(clave, ":", valor)