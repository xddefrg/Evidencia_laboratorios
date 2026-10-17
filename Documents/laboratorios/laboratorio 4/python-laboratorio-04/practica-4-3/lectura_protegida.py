# Práctica 4.3 - Ejercicio: respetar un archivo dañado.
#
# Tres escenarios (tabla de la sección 8):
#   1. El archivo no existe        -> empezar con lista vacía.
#   2. Existe y es válido          -> recuperar los productos.
#   3. Existe pero está dañado     -> informar, NO sobrescribir y permitir
#                                     revisar su contenido.
import json
from pathlib import Path

RUTA = Path(__file__).resolve().parent / "productos.json"


def cargar_protegido():
    """Devuelve (productos, ok). Si ok es False, no se debe guardar encima."""
    try:
        with RUTA.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print("El archivo no existe: se inicia una lista vacía.")
        return [], True
    except json.JSONDecodeError as error:
        print(f"Formato JSON incorrecto (línea {error.lineno}, columna {error.colno}): {error.msg}")
        return [], False

    if not isinstance(datos, list):
        print("Estructura inesperada: se esperaba una lista de productos.")
        return [], False

    print(f"Archivo válido: {len(datos)} productos recuperados.")
    return datos, True


def guardar(productos):
    with RUTA.open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)


def mostrar_contenido_crudo():
    print("--- Contenido actual del archivo ---")
    print(RUTA.read_text(encoding="utf-8"))
    print("------------------------------------")


if __name__ == "__main__":
    productos, ok = cargar_protegido()

    if not ok:
        print("Guardado BLOQUEADO para no destruir un archivo recuperable.")
        if input("¿Ver el contenido del archivo? (s/n): ").strip().lower() == "s":
            mostrar_contenido_crudo()
    else:
        productos.append({"codigo": f"P{len(productos) + 1:03d}", "nombre": "Nuevo", "precio": 1000, "cantidad": 1})
        guardar(productos)
        print("Producto agregado y guardado.")
