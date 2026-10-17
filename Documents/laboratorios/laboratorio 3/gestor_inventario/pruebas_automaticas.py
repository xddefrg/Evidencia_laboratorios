"""Pruebas obligatorias del reto (sección 16) y comprobación numérica (sección 17).

Ejecutar:  python pruebas_automaticas.py
Termina con código 0 si todo pasa y con 1 si alguna prueba falla.
"""

import sys

from inventario import Inventario
from producto import Producto

resultados = []


def comprobar(descripcion, condicion):
    estado = "OK   " if condicion else "FALLA"
    print(f"[{estado}] {descripcion}")
    resultados.append(bool(condicion))


def producto_rechazado(codigo, nombre, categoria, precio, cantidad):
    """True si Producto lanza ValueError con esos datos."""
    try:
        Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError:
        return True
    return False


def inventario_de_ejemplo():
    inventario = Inventario()
    inventario.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
    inventario.registrar_producto(Producto("P002", "Mouse", "Periféricos", 45000, 0))
    inventario.registrar_producto(Producto("P003", "Tarjeta de video", "Componentes", 700000, 2))
    return inventario


print("--- Inventario vacío ---")
vacio = Inventario()
datos = vacio.resumen()
comprobar("Listado vacío", vacio.listar_productos() == [])
comprobar(
    "Resumen en cero",
    datos["productos"] == 0 and datos["unidades"] == 0
    and datos["valor"] == 0 and datos["categorias"] == set(),
)

print("\n--- Registro ---")
inventario = Inventario()
p001 = Producto("P001", "Teclado", "Periféricos", 85000, 4)
comprobar("Registrar P001: aceptado", inventario.registrar_producto(p001) is True)
comprobar(
    "Registrar nuevamente P001: rechazado",
    inventario.registrar_producto(Producto("P001", "Otro", "Accesorios", 100, 1)) is False,
)
comprobar("El rechazo no agregó nada", len(inventario.listar_productos()) == 1)
comprobar("Código vacío: rechazado", producto_rechazado("", "X", "Accesorios", 100, 1))
comprobar("Código solo espacios: rechazado", producto_rechazado("   ", "X", "Accesorios", 100, 1))
comprobar("Nombre vacío: rechazado", producto_rechazado("P9", "", "Accesorios", 100, 1))
comprobar("Nombre solo espacios: rechazado", producto_rechazado("P9", "  ", "Accesorios", 100, 1))
comprobar("Categoría no permitida: rechazada", producto_rechazado("P9", "X", "Juguetes", 100, 1))
comprobar("Precio cero: rechazado", producto_rechazado("P9", "X", "Accesorios", 0, 1))
comprobar("Precio negativo: rechazado", producto_rechazado("P9", "X", "Accesorios", -5, 1))
comprobar("Cantidad negativa: rechazada", producto_rechazado("P9", "X", "Accesorios", 100, -1))

cero = Producto("P010", "Cable", "Accesorios", 5000, 0)
comprobar("Cantidad cero: producto válido", cero.cantidad == 0)
inventario.registrar_producto(cero)
comprobar("Cantidad cero: aparece sin existencias", "Cable" in inventario.productos_sin_stock())

print("\n--- Búsqueda ---")
antes = len(inventario.listar_productos())
comprobar("Buscar P001: devuelve el objeto", inventario.buscar_por_codigo("P001") is p001)
comprobar("Buscar P999: devuelve None", inventario.buscar_por_codigo("P999") is None)
comprobar("Buscar no altera el inventario", len(inventario.listar_productos()) == antes)

print("\n--- Actualización ---")
comprobar("Actualizar P001 a 10: aceptado", inventario.actualizar_existencias("P001", 10) is True)
comprobar(
    "Solo cambió la cantidad",
    p001.cantidad == 10 and p001.nombre == "Teclado" and p001.precio == 85000
    and p001.categoria == "Periféricos",
)
comprobar("Actualizar a -3: rechazado", inventario.actualizar_existencias("P001", -3) is False)
comprobar("El dato anterior se conserva", p001.cantidad == 10)
comprobar("Actualizar código inexistente: rechazado", inventario.actualizar_existencias("P999", 5) is False)
comprobar("Actualizar a cero: aceptado", inventario.actualizar_existencias("P001", 0) is True)

print("\n--- Eliminación ---")
comprobar("Eliminar existente: aceptado", inventario.eliminar_producto("P010") is True)
comprobar("El registro ya no existe", inventario.buscar_por_codigo("P010") is None)
comprobar("Eliminar inexistente: informa sin fallar", inventario.eliminar_producto("P999") is False)

print("\n--- Encapsulamiento ---")
try:
    p001.codigo = "P999"
    codigo_protegido = False
except AttributeError:
    codigo_protegido = True
comprobar("El código no se puede reasignar", codigo_protegido)

copia = inventario.listar_productos()
copia.clear()
comprobar("Modificar la lista devuelta no altera el inventario", len(inventario.listar_productos()) > 0)

print("\n--- Comprobación numérica (sección 17) ---")
inventario = inventario_de_ejemplo()
datos = inventario.resumen()
comprobar("Productos registrados: 3", datos["productos"] == 3)
comprobar("Unidades disponibles: 6", datos["unidades"] == 6)
comprobar("Valor del inventario: 1740000.0", datos["valor"] == 1740000.0)
comprobar("Categorías utilizadas: 2", len(datos["categorias"]) == 2)
comprobar("Producto sin stock: Mouse", inventario.productos_sin_stock() == ["Mouse"])

inventario.actualizar_existencias("P002", 5)
datos = inventario.resumen()
comprobar("Tras actualizar P002 a 5 -> productos: 3", datos["productos"] == 3)
comprobar("Tras actualizar P002 a 5 -> unidades: 11", datos["unidades"] == 11)
comprobar("Tras actualizar P002 a 5 -> valor: 1965000.0", datos["valor"] == 1965000.0)
comprobar("Ya no hay productos sin stock", inventario.productos_sin_stock() == [])

print("\n--- Independencia entre inventarios ---")
primero = Inventario()
segundo = Inventario()
primero.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
comprobar("Primero tiene 1 producto", len(primero.listar_productos()) == 1)
comprobar("Segundo sigue vacío", len(segundo.listar_productos()) == 0)

total = len(resultados)
superadas = sum(resultados)
print(f"\n{superadas}/{total} pruebas superadas")
sys.exit(0 if superadas == total else 1)
