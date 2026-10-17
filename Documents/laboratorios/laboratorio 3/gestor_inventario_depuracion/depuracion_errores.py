"""Depuración del gestor de inventario (sección 20 del reto).

Trabaja sobre una COPIA del proyecto (producto.py e inventario.py son copias de
gestor_inventario/): el proyecto original no se toca. Cada caso provoca uno de
los seis errores, muestra el síntoma, explica la causa y presenta la corrección.

Ejecutar:  python depuracion_errores.py
"""

from producto import Producto
from inventario import Inventario


def titulo(texto):
    print()
    print("=" * 60)
    print(texto)
    print("=" * 60)


teclado = Producto("P001", "Teclado", "Periféricos", 85000, 4)

# ---------------------------------------------------------------------------
titulo("1. _productos como lista compartida a nivel de clase")


class InventarioCompartido:
    _productos = []  # ERROR: la lista vive en la clase, no en cada objeto

    def registrar_producto(self, producto):
        self._productos.append(producto)
        return True

    def listar_productos(self):
        return self._productos.copy()


uno = InventarioCompartido()
dos = InventarioCompartido()
uno.registrar_producto(teclado)
print("Productos en el segundo inventario (debería ser 0):", len(dos.listar_productos()))

# Causa: una lista mutable en el cuerpo de la clase se crea una sola vez y todas
# las instancias la comparten.
# Corrección: crearla en __init__ con self._productos = [] (como hace Inventario).
uno = Inventario()
dos = Inventario()
uno.registrar_producto(teclado)
print("Con la corrección, el segundo inventario tiene:", len(dos.listar_productos()))

# ---------------------------------------------------------------------------
titulo("2. Consultar una propiedad que no existe")

try:
    print(teclado.stock)  # ERROR: la propiedad se llama "cantidad"
except AttributeError as error:
    print("AttributeError:", error)

# Causa: Producto no define ninguna propiedad llamada "stock".
# Corrección: usar el nombre correcto de la propiedad.
print("Con la corrección, teclado.cantidad =", teclado.cantidad)

# ---------------------------------------------------------------------------
titulo("3. Omitir self en un método de instancia")


class InventarioSinSelf:
    def __init__(self):
        self._productos = []

    def contar():  # ERROR: falta self
        return 0


try:
    InventarioSinSelf().contar()
except TypeError as error:
    print("TypeError:", error)

# Causa: Python pasa el objeto como primer argumento al llamar al método, pero
# contar() no declara ningún parámetro para recibirlo.
# Corrección: declarar self y usar el estado del objeto.


class InventarioConSelf:
    def __init__(self):
        self._productos = []

    def contar(self):
        return len(self._productos)


print("Con la corrección, contar() =", InventarioConSelf().contar())

# ---------------------------------------------------------------------------
titulo("4. Dejar crear un producto con cantidad negativa")


class ProductoSinValidar:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad  # ERROR: se acepta sin validar

    @property
    def cantidad(self):
        return self._cantidad


malo = ProductoSinValidar("P002", "Mouse", "Periféricos", 45000, -10)
print("Producto creado con cantidad:", malo.cantidad)

# Causa: el constructor asigna los valores sin comprobarlos, así que el objeto
# "nace" inválido y rompe los totales del inventario.
# Corrección: validar en __init__ y lanzar ValueError (como hace Producto).
try:
    Producto("P002", "Mouse", "Periféricos", 45000, -10)
except ValueError as error:
    print("Con la corrección, ValueError:", error)

# ---------------------------------------------------------------------------
titulo("5. Eliminar una instrucción de importación")

# Se simula ejecutando código en un espacio de nombres vacío, para no editar
# ningún archivo del proyecto.
sin_importacion = "inventario = Inventario()"
try:
    exec(sin_importacion, {})
except NameError as error:
    print("NameError:", error)

# Causa: main.py usa Inventario, pero ese nombre solo existe si se importa.
# Corrección: restaurar la línea  from inventario import Inventario
con_importacion = "from inventario import Inventario\ninventario = Inventario()"
exec(con_importacion, {})
print("Con la importación restaurada, el código se ejecuta sin errores.")

# ---------------------------------------------------------------------------
titulo("6. Sumar precios sin multiplicar por cantidades")

productos = [
    Producto("P001", "Teclado", "Periféricos", 85000, 4),
    Producto("P002", "Mouse", "Periféricos", 45000, 0),
    Producto("P003", "Tarjeta de video", "Componentes", 700000, 2),
]

valor_erroneo = sum(producto.precio for producto in productos)  # ERROR
print("Valor calculado con el error:", valor_erroneo)

# Causa: se suman los precios unitarios y se ignora cuántas unidades hay de cada
# producto (y que el Mouse no tiene existencias).
# Corrección: sumar precio * cantidad de cada producto, con calcular_valor().
valor_correcto = sum(producto.calcular_valor() for producto in productos)
print("Valor correcto (esperado 1740000):", valor_correcto)
