"""Almacenamiento: lee y escribe el inventario en JSON.

Es uno de los dos módulos que conocen el sistema de archivos (el otro es
reportes.py). No pregunta nada al usuario: informa mediante valores de
retorno o mediante ErrorAlmacenamiento.
"""
import json
from pathlib import Path

from inventario import Inventario

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


class ErrorAlmacenamiento(Exception):
    """El archivo no se pudo leer o escribir, o su contenido no es válido."""


def cargar_inventario(ruta=RUTA_JSON):
    """Devuelve el Inventario guardado.

    - Archivo inexistente  -> inventario vacío (primera ejecución).
    - Archivo válido       -> inventario con todos sus productos.
    - Archivo dañado o con registros inválidos -> ErrorAlmacenamiento.
      Este módulo NUNCA escribe en el archivo al cargar.
    """
    ruta = Path(ruta)

    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        return Inventario()
    except json.JSONDecodeError as error:
        raise ErrorAlmacenamiento(
            f"{ruta.name} no es JSON válido "
            f"(línea {error.lineno}, columna {error.colno}: {error.msg})."
        ) from error
    except UnicodeDecodeError as error:
        raise ErrorAlmacenamiento(f"{ruta.name} no está codificado en UTF-8.") from error
    except OSError as error:
        raise ErrorAlmacenamiento(f"No se pudo leer {ruta.name}: {error}") from error

    try:
        return Inventario.desde_datos(datos)
    except ValueError as error:
        raise ErrorAlmacenamiento(f"Datos inválidos en {ruta.name}. {error}") from error


def guardar_inventario(inventario, ruta=RUTA_JSON):
    """Escribe el inventario en JSON (UTF-8, indentado) y devuelve la ruta.

    Escribe primero en un archivo temporal y lo reemplaza al terminar, así
    un fallo a mitad de escritura no deja el original truncado.
    Lanza ErrorAlmacenamiento si no se pudo confirmar el guardado.
    """
    ruta = Path(ruta)
    datos = inventario.exportar_datos()
    temporal = ruta.with_name(ruta.name + ".tmp")

    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with temporal.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4, allow_nan=False)
        temporal.replace(ruta)
    except (OSError, ValueError) as error:
        try:
            temporal.unlink(missing_ok=True)
        except OSError:
            pass
        raise ErrorAlmacenamiento(f"No se pudo guardar en {ruta}: {error}") from error

    return ruta
