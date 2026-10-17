# Práctica 4.3 - Sección 2: recuperar los datos desde JSON.
import json
from pathlib import Path

ruta = Path("productos.json")

with ruta.open("r", encoding="utf-8") as archivo:
    productos = json.load(archivo)

for producto in productos:
    print(producto["codigo"], "-", producto["nombre"])
