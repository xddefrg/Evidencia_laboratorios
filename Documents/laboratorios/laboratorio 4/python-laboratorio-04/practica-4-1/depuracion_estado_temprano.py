# Práctica 4.1 - Depuración: se modificó el estado demasiado pronto.
#
# ORIGINAL (con el error):
#
#   producto._cantidad = nueva_cantidad
#
#   if nueva_cantidad < 0:
#       print("Cantidad inválida.")
#
# ¿Por qué llega tarde la comprobación? Porque el atributo ya se cambió
# antes de validar: aunque se imprima "Cantidad inválida.", el producto
# queda con una cantidad negativa.
#
# CORRECCIÓN: validar primero y modificar solo si el dato es aceptable.


class Producto:
    def __init__(self, nombre, cantidad):
        self._nombre = nombre
        self._cantidad = cantidad

    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:  # 1) validar
            raise ValueError("Cantidad inválida.")
        self._cantidad = nueva_cantidad  # 2) modificar solo si es válido

    @property
    def cantidad(self):
        return self._cantidad


producto = Producto("Teclado", 4)

try:
    producto.actualizar_cantidad(-3)
except ValueError as error:
    print("Rechazado:", error)

print("Cantidad actual (sin cambios):", producto.cantidad)  # sigue en 4

producto.actualizar_cantidad(10)
print("Cantidad actual tras entrada válida:", producto.cantidad)  # 10
