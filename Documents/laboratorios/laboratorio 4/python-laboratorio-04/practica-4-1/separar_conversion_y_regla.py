# Práctica 4.1 - Sección 3: separar la conversión de la regla de negocio.
#
# Predicción antes de ejecutar:
#   abc -> "No es un número entero."
#   -3  -> "No se aceptan existencias negativas."
#   0   -> "Cantidad aceptada: 0"
#   7   -> "Cantidad aceptada: 7"
try:
    cantidad = int(input("Cantidad: "))
except ValueError:
    print("No es un número entero.")
else:
    if cantidad < 0:
        print("No se aceptan existencias negativas.")
    else:
        print("Cantidad aceptada:", cantidad)
