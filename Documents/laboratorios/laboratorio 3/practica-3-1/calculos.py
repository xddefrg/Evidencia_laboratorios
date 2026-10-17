def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


resultado = calcular_subtotal(85000, 3)
print("Subtotal:", resultado)


# --- Comparación: print() frente a return ---
def mostrar_total(precio, cantidad):
    # Su efecto es solo visible: imprime, pero no entrega nada al programa.
    print(precio * cantidad)


def obtener_total(precio, cantidad):
    # Entrega un valor que el programa puede guardar y reutilizar.
    return precio * cantidad


mostrar_total(10000, 3)
total = obtener_total(10000, 3)
print("Resultado reutilizable:", total)
