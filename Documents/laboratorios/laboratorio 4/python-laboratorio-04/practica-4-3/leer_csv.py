# Práctica 4.3 - Sección 10: leer un CSV con encabezados.
# Todos los valores llegan como texto; hay que convertirlos para operar.
import csv
from pathlib import Path

ruta = Path("reporte.csv")

with ruta.open("r", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for producto in lector:
        print(producto["codigo"], producto["nombre"], producto["precio"])
