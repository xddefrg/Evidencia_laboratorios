# Práctica 4.2 - Sección 8: ruta relativa vs. ruta del proyecto.
# BASE_DIR se calcula desde la ubicación de ESTE archivo, no desde la
# carpeta en la que se lanzó Python. Así funciona igual desde cualquier lugar.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_DATOS = BASE_DIR / "datos" / "inventario.txt"

RUTA_DATOS.parent.mkdir(parents=True, exist_ok=True)
RUTA_DATOS.write_text("Datos del proyecto\n", encoding="utf-8")

print(RUTA_DATOS)
