def calcular_total(precio, cantidad, descuento=0):
    subtotal = precio * cantidad
    return subtotal - subtotal * descuento / 100


# Predicción:
#   1ª -> 100000.0  (sin descuento: se usa 0)
#   2ª ->  90000.0  (10 % de descuento)
#   3ª ->  80000.0  (20 % de descuento, con argumentos con nombre)
print(calcular_total(50000, 2))
print(calcular_total(50000, 2, 10))
print(calcular_total(precio=50000, cantidad=2, descuento=20))


# --- Ejercicio: costos de envío ---
def calcular_cobro(valor_compra, envio=10000):
    return valor_compra + envio


print("Cobro con envío predeterminado:", calcular_cobro(80000))
print("Cobro con envío gratuito:", calcular_cobro(80000, envio=0))
