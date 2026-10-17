"""Reportes: construye y exporta el reporte CSV del inventario.

El CSV es una EXPORTACIÓN: se genera cuando el usuario lo pide y no se
mantiene sincronizado con el JSON. Este módulo no modifica existencias.
"""
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"

CAMPOS = ["codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario"]


def construir_filas(inventario):
    """Una fila por producto; valor_inventario = precio * cantidad."""
    filas = []
    for producto in inventario.listar():
        fila = producto.a_diccionario()
        fila["valor_inventario"] = producto.valor_inventario
        filas.append(fila)
    return filas


def exportar_csv(inventario, ruta=RUTA_CSV):
    """Escribe el CSV con encabezados y devuelve la ruta generada."""
    ruta = Path(ruta)
    filas = construir_filas(inventario)

    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(filas)

    return ruta
