"""Gestor de inventario persistente (Laboratorio 4).

main.py concentra la interacción con el usuario: muestra el menú, lee las
entradas, coordina las operaciones y presenta los mensajes. La lógica de
negocio vive en Producto/Inventario; los archivos, en almacenamiento.py y
reportes.py.
"""
from almacenamiento import ErrorAlmacenamiento, RUTA_JSON, cargar_inventario, guardar_inventario
from inventario import Inventario
from producto import CATEGORIAS, Producto
from reportes import exportar_csv

MENU = """
================================
       GESTOR DE INVENTARIO
================================
1. Registrar producto
2. Listar productos
3. Buscar por código
4. Actualizar existencias
5. Eliminar producto
6. Consultar productos sin stock
7. Resumen del inventario
8. Guardar inventario
9. Exportar reporte CSV
0. Salir"""

MENSAJE_BLOQUEO = (
    "Operación bloqueada: el archivo de datos está dañado y no se modificará "
    "automáticamente. Corrígelo o restaura una copia válida y reinicia el programa."
)


class Estado:
    """Datos de la sesión: el inventario activo y las banderas de seguridad."""

    def __init__(self, inventario, solo_lectura=False):
        self.inventario = inventario
        self.solo_lectura = solo_lectura  # True si el JSON existente no pudo cargarse
        self.pendiente_guardar = False  # True si hay cambios que no llegaron al disco


# ----------------------------------------------------------------------
# Lectura de entradas
# ----------------------------------------------------------------------
def leer_texto(mensaje):
    return input(mensaje).strip()


def leer_decimal(mensaje):
    """Repite la pregunta hasta que el texto pueda convertirse a número."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debes escribir un número.")


def leer_entero(mensaje):
    """Repite la pregunta hasta que el texto pueda convertirse a entero."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes escribir un número entero.")


def leer_categoria():
    texto = leer_texto(f"Categoría ({'/'.join(CATEGORIAS)}): ")
    # Comodidad de entrada: ignora mayúsculas. La validación real sigue en Producto.
    for categoria in CATEGORIAS:
        if texto.casefold() == categoria.casefold():
            return categoria
    return texto


# ----------------------------------------------------------------------
# Guardado
# ----------------------------------------------------------------------
def intentar_guardar(estado):
    """Guarda y avisa. Solo anuncia éxito si la escritura se confirmó."""
    try:
        guardar_inventario(estado.inventario)
    except ErrorAlmacenamiento as error:
        estado.pendiente_guardar = True
        print(f"ADVERTENCIA: no se confirmó el guardado. {error}")
        print("Los cambios podrían existir solamente en memoria.")
        return False

    estado.pendiente_guardar = False
    print("Inventario guardado.")
    return True


def bloqueado(estado):
    if estado.solo_lectura:
        print(MENSAJE_BLOQUEO)
        return True
    return False


def avisar_si_solo_lectura(estado):
    """En las consultas, aclara que un resultado vacío no significa 'sin datos'."""
    if estado.solo_lectura:
        print("(Aviso: el archivo de datos está dañado; esta consulta no refleja lo guardado.)")


# ----------------------------------------------------------------------
# Operaciones del menú
# ----------------------------------------------------------------------
def registrar_producto(estado):
    if bloqueado(estado):
        return

    codigo = leer_texto("Código: ")
    nombre = leer_texto("Nombre: ")
    categoria = leer_categoria()
    precio = leer_decimal("Precio: ")
    cantidad = leer_entero("Cantidad: ")

    try:
        producto = Producto(codigo, nombre, categoria, precio, cantidad)
        estado.inventario.registrar(producto)
    except ValueError as error:
        print("Producto rechazado:", error)
        return  # operación rechazada: no se guarda

    print("Producto registrado.")
    intentar_guardar(estado)


def listar_productos(estado):
    avisar_si_solo_lectura(estado)
    productos = estado.inventario.listar()
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        print(producto)


def buscar_producto(estado):
    avisar_si_solo_lectura(estado)
    codigo = leer_texto("Código a buscar: ")
    producto = estado.inventario.buscar(codigo)
    if producto is None:
        print("No existe un producto con ese código.")
    else:
        print(producto)


def actualizar_existencias(estado):
    if bloqueado(estado):
        return

    codigo = leer_texto("Código: ")
    if estado.inventario.buscar(codigo) is None:
        print("No existe un producto con ese código.")
        return

    nueva_cantidad = leer_entero("Nueva cantidad: ")

    try:
        producto = estado.inventario.actualizar_existencias(codigo, nueva_cantidad)
    except ValueError as error:
        print("Actualización rechazada:", error)
        return

    print(f"Existencias actualizadas: {producto.nombre} ahora tiene {producto.cantidad} unidades.")
    intentar_guardar(estado)


def eliminar_producto(estado):
    if bloqueado(estado):
        return

    codigo = leer_texto("Código a eliminar: ")
    try:
        producto = estado.inventario.eliminar(codigo)
    except ValueError as error:
        print("No se eliminó nada:", error)
        return

    print(f"Producto eliminado: {producto.nombre}.")
    intentar_guardar(estado)


def consultar_sin_stock(estado):
    avisar_si_solo_lectura(estado)
    agotados = estado.inventario.sin_stock()
    if not agotados:
        print("No hay productos sin existencias.")
        return
    for producto in agotados:
        print(producto)


def mostrar_resumen(estado):
    avisar_si_solo_lectura(estado)
    datos = estado.inventario.resumen()
    sin_existencias = ", ".join(datos["sin_existencias"]) or "Ninguno"
    print(f"Productos registrados: {datos['productos']}")
    print(f"Unidades disponibles: {datos['unidades']}")
    print(f"Valor total: ${datos['valor_total']}")
    print(f"Sin existencias: {sin_existencias}")
    print(f"Categorías utilizadas: {datos['categorias_utilizadas']}")


def guardar_manual(estado):
    if bloqueado(estado):
        return
    intentar_guardar(estado)


def exportar_reporte(estado):
    if bloqueado(estado):
        return
    try:
        ruta = exportar_csv(estado.inventario)
    except OSError as error:
        print(f"No se pudo exportar el reporte: {error}")
        return
    print("Reporte exportado:", ruta)


OPERACIONES = {
    "1": registrar_producto,
    "2": listar_productos,
    "3": buscar_producto,
    "4": actualizar_existencias,
    "5": eliminar_producto,
    "6": consultar_sin_stock,
    "7": mostrar_resumen,
    "8": guardar_manual,
    "9": exportar_reporte,
}


# ----------------------------------------------------------------------
# Arranque y cierre
# ----------------------------------------------------------------------
def iniciar_estado():
    try:
        inventario = cargar_inventario()
    except ErrorAlmacenamiento as error:
        print("No se pudo cargar el inventario guardado.")
        print(error)
        print(f"El archivo {RUTA_JSON} NO se modificará.")
        print("Modo de solo consulta: se bloquean las operaciones que modifican datos.")
        return Estado(Inventario(), solo_lectura=True)

    if len(inventario) > 0:
        print(f"Inventario cargado: {len(inventario)} productos.")
    else:
        print("No hay datos guardados: se inicia un inventario vacío.")
    return Estado(inventario)


def cerrar(estado):
    if estado.pendiente_guardar and not estado.solo_lectura:
        print("Hay cambios sin guardar: se intenta guardarlos antes de salir.")
        if not intentar_guardar(estado):
            print("Los cambios pendientes NO se guardaron.")
    print("Programa finalizado.")


def main():
    estado = iniciar_estado()

    try:
        while True:
            print(MENU)
            try:
                opcion = input("\nOpción: ").strip()
            except EOFError:  # entrada cerrada (por ejemplo, en pruebas con tuberías)
                print()
                break

            if opcion == "0":
                break

            operacion = OPERACIONES.get(opcion)
            if operacion is None:
                print("Opción no válida. Elige un número del menú.")
                continue

            try:
                operacion(estado)
            except EOFError:
                print()
                break
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario.")

    cerrar(estado)


if __name__ == "__main__":
    main()
