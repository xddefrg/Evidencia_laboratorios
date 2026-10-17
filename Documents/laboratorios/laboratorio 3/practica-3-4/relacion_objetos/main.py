from producto import Producto
from inventario import Inventario


def texto(aceptado):
    return "aceptado" if aceptado else "rechazado"


inventario = Inventario()

inventario.agregar(Producto("P001", "Teclado"))
inventario.agregar(Producto("P002", "Mouse"))

for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

print()
encontrado = inventario.buscar_por_codigo("P002")

if encontrado is not None:
    print("Encontrado:", encontrado.nombre)
else:
    print("Producto no registrado.")

# --- Reto: inventario con reglas ---
print()
print("Registrar P003 (válido):    ", texto(inventario.agregar(Producto("P003", "Monitor"))))
print("Registrar P001 (repetido):  ", texto(inventario.agregar(Producto("P001", "Otro"))))
print("Eliminar P002 (existe):     ", texto(inventario.eliminar("P002")))
print("Eliminar P999 (no existe):  ", texto(inventario.eliminar("P999")))

print()
print("Inventario final:")
for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)
