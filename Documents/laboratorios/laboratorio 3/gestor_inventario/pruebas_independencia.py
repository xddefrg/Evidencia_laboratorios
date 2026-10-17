from inventario import Inventario
from producto import Producto

primero = Inventario()
segundo = Inventario()

primero.registrar_producto(
    Producto("P001", "Teclado", "Periféricos", 85000, 4)
)

print("Primero:", len(primero.listar_productos()))  # 1
print("Segundo:", len(segundo.listar_productos()))  # 0

# Comprobación extra: modificar o eliminar en uno no afecta al otro.
segundo.registrar_producto(
    Producto("P001", "Teclado", "Periféricos", 85000, 4)
)
segundo.actualizar_existencias("P001", 0)
primero.eliminar_producto("P001")

print("Tras actualizar el segundo y eliminar en el primero:")
print("Primero:", len(primero.listar_productos()))  # 0
print("Segundo:", len(segundo.listar_productos()))  # 1
print("Cantidad en el segundo:", segundo.buscar_por_codigo("P001").cantidad)  # 0
