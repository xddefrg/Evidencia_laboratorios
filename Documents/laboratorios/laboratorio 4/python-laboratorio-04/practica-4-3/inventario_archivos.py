# Práctica 4.3 - Reto: inventario sencillo con JSON y CSV (sin clases propias).
#
# Operaciones:
#   - guardar productos en inventario.json
#   - recuperarlos al ejecutar de nuevo
#   - exportarlos a inventario.csv
#
# Si inventario.json existe pero está dañado, se informa y NO se reemplaza
# por una lista vacía: el guardado queda bloqueado.
import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "inventario.json"
RUTA_CSV = BASE_DIR / "inventario.csv"


def guardar_productos(productos):
    with RUTA_JSON.open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)


def recuperar_productos():
    """Devuelve (productos, guardado_permitido)."""
    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        return [], True
    except json.JSONDecodeError as error:
        print(f"inventario.json tiene un error de formato: {error}")
        print("No se sobrescribirá. Revísalo o restaura una copia válida.")
        return [], False

    if not isinstance(datos, list):
        print("inventario.json tiene una estructura inesperada.")
        return [], False

    return datos, True


def exportar_csv(productos):
    campos = ["codigo", "nombre", "precio", "cantidad"]
    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(productos)


def main():
    productos, guardado_permitido = recuperar_productos()

    if not guardado_permitido:
        return

    print(f"Productos recuperados: {len(productos)}")

    if not productos:
        productos = [
            {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
            {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 0},
        ]
        print("Inventario inicial creado.")

    guardar_productos(productos)
    print("Guardado en", RUTA_JSON.name)

    exportar_csv(productos)
    print("Exportado en", RUTA_CSV.name)


if __name__ == "__main__":
    main()
