# Práctica 4.1 - Sección 6: diferenciar ValueError y TypeError.

# ValueError: el tipo es correcto (str) pero el contenido no representa un entero.
try:
    cantidad = int("abc")
except ValueError:
    print("El contenido no representa un entero.")

# TypeError: el tipo (None) no admite la conversión.
try:
    cantidad = int(None)
except TypeError:
    print("El tipo recibido no permite esa conversión.")
