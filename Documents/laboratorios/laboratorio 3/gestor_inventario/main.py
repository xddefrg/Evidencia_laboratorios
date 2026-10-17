# Planificación (escrita antes de programar)
#
# Producto:
#   representa un artículo y controla sus valores
#
# Inventario:
#   conserva varios objetos Producto
#   registra, busca, actualiza, elimina y consulta
#
# main:
#   solicita datos
#   muestra menú
#   informa los resultados
#
# Preguntas previas:
#   ¿Qué clase debe evitar los códigos repetidos?          -> Inventario
#   ¿Qué clase debe comprobar que la cantidad sea válida?  -> Producto
#   ¿Qué clase calcula el valor de un producto?            -> Producto
#   ¿Dónde debe utilizarse input()?                        -> solo en main.py
#   ¿Quién decide qué mensaje se muestra tras una operación? -> main.py

import math

from producto import Producto
from inventario import Inventario


def mostrar_menu():
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")


# --- Lectura de datos ---
def leer_texto(mensaje):
    return input(mensaje).strip()


def leer_cantidad(mensaje="Cantidad: "):
    while True:
        try:
            cantidad = int(input(mensaje))
        except ValueError:
            print("Debes escribir un número entero.")
            continue

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue

        return cantidad


def leer_precio(mensaje="Precio: "):
    while True:
        try:
            precio = float(input(mensaje))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if not math.isfinite(precio) or precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue

        return precio


# --- Presentación ---
def formatear_producto(producto):
    return (
        f"{producto.codigo} - {producto.nombre} - {producto.categoria} - "
        f"${producto.precio} - {producto.cantidad} unidades"
    )


# --- Una función por opción del menú ---
def registrar_producto(inventario):
    codigo = leer_texto("Código: ")
    nombre = leer_texto("Nombre: ")
    categoria = leer_texto("Categoría: ")
    precio = leer_precio()
    cantidad = leer_cantidad()

    # Producto valida todo al crearse; si algo falla no se guarda nada.
    try:
        producto = Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError as error:
        print(f"Producto no registrado: {error}")
        return

    if inventario.registrar_producto(producto):
        print("Producto registrado.")
    else:
        print(f"Producto no registrado: ya existe el código {producto.codigo}.")


def listar_productos(inventario):
    productos = inventario.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print(formatear_producto(producto))


def buscar_producto(inventario):
    codigo = leer_texto("Código: ")
    producto = inventario.buscar_por_codigo(codigo)

    if producto is None:
        print("No existe un producto con ese código.")
    else:
        print(formatear_producto(producto))


def actualizar_existencias(inventario):
    codigo = leer_texto("Código: ")
    producto = inventario.buscar_por_codigo(codigo)

    if producto is None:
        print("No existe un producto con ese código.")
        return

    nueva_cantidad = leer_cantidad("Nueva cantidad: ")

    if inventario.actualizar_existencias(codigo, nueva_cantidad):
        print(f"Existencias actualizadas: {producto.nombre} ahora tiene {nueva_cantidad} unidades.")
    else:
        print("No se pudo actualizar las existencias.")


def eliminar_producto(inventario):
    codigo = leer_texto("Código: ")

    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("No existe un producto con ese código.")


def consultar_sin_stock(inventario):
    agotados = inventario.productos_sin_stock()

    if not agotados:
        print("No hay productos sin existencias.")
        return

    print("Sin existencias:")
    for nombre in agotados:
        print(f"- {nombre}")


def mostrar_resumen(inventario):
    datos = inventario.resumen()
    categorias = sorted(datos["categorias"])
    detalle = f" ({', '.join(categorias)})" if categorias else ""

    print(f"Productos registrados: {datos['productos']}")
    print(f"Unidades disponibles: {datos['unidades']}")
    print(f"Valor del inventario: ${datos['valor']}")
    print(f"Categorías utilizadas: {len(categorias)}{detalle}")


def main():
    inventario = Inventario()
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            listar_productos(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            actualizar_existencias(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            consultar_sin_stock(inventario)
        elif opcion == "7":
            mostrar_resumen(inventario)
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        # Fin de la entrada (Ctrl+D / Ctrl+Z) o Ctrl+C: salida limpia, sin traza.
        print("\nPrograma interrumpido.")
