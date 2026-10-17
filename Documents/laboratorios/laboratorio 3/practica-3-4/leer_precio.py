try:
    precio = float(input("Precio: "))
    print("Precio ingresado:", precio)
except ValueError:
    # Solo se atiende el error concreto de conversión, no cualquier error.
    print("Debes escribir un número válido.")
