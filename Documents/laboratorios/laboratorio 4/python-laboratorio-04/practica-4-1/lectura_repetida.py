# Práctica 4.1 - Sección 4: reintentar hasta recibir un dato correcto.
#
# float() acepta "nan" e "inf". Aquí añadimos math.isfinite() para rechazarlos,
# tal como pide la advertencia del laboratorio (el precio debe ser finito).
import math

while True:
    try:
        precio = float(input("Precio: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if not math.isfinite(precio):
        print("El precio debe ser un número finito.")
        continue

    if precio <= 0:
        print("El precio debe ser positivo.")
        continue

    print("Precio aceptado:", precio)
    break
