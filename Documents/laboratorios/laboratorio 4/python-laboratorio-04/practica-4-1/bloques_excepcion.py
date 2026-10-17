# Práctica 4.1 - Sección 7: try / except / else / finally.
# Con "10": entra a else y luego a finally.
# Con "hola": entra a except y luego a finally.
try:
    numero = int(input("Número: "))
except ValueError:
    print("Entrada no numérica.")
else:
    print("Número aceptado:", numero)
finally:
    print("Finalizó el intento de lectura.")
