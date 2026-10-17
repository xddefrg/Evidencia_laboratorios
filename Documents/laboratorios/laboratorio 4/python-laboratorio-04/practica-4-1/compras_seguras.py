# Práctica 4.1 - Reto: registro de compras con validaciones.
# Termina cuando el usuario escribe 0. Un error no borra el acumulado
# ni termina el ciclo.
import math

compras_aceptadas = 0
total = 0.0

print("Registra importes de compra. Escribe 0 para terminar.")

while True:
    texto = input("Importe: ")

    try:
        importe = float(texto)
    except ValueError:
        print("Debes escribir un número.")
        continue

    if not math.isfinite(importe):
        print("El importe debe ser un número finito.")
        continue

    if importe == 0:
        break

    if importe < 0:
        print("El importe no puede ser negativo.")
        continue

    compras_aceptadas += 1
    total += importe
    print(f"Compra aceptada. Acumulado: {total}")

print(f"Compras aceptadas: {compras_aceptadas}")
print(f"Suma acumulada: {total}")
