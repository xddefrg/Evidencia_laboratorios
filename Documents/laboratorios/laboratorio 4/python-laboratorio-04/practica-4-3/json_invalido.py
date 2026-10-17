# Práctica 4.3 - Sección 7: un JSON puede ser inválido.
# Para probarlo, trabaja sobre una COPIA de productos.json y elimina una
# coma o una comilla.
import json
from pathlib import Path

ruta = Path("productos.json")

try:
    with ruta.open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)
except json.JSONDecodeError:
    print("El archivo no contiene JSON válido.")
except FileNotFoundError:
    print("El archivo no existe (error distinto de un JSON dañado).")
else:
    print("JSON válido:", len(productos), "productos.")
