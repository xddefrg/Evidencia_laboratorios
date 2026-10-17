# Práctica 4.3 - Ejercicio: Exportación de ventas.
# Se exportan cuatro ventas a CSV, se leen de nuevo y se suma el total
# convirtiendo la columna "total" (que llega como texto) a número.
import csv
from pathlib import Path

RUTA = Path(__file__).resolve().parent / "ventas.csv"
CAMPOS = ["codigo", "producto", "cantidad", "total"]

ventas = [
    {"codigo": "V001", "producto": "Teclado", "cantidad": 2, "total": 170000},
    {"codigo": "V002", "producto": "Mouse", "cantidad": 3, "total": 135000},
    {"codigo": "V003", "producto": "Monitor", "cantidad": 1, "total": 700000},
    {"codigo": "V004", "producto": "Cámara", "cantidad": 2, "total": 240000},
]

with RUTA.open("w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
    escritor.writeheader()
    escritor.writerows(ventas)

print("Ventas exportadas:", RUTA.name)

total_vendido = 0.0
with RUTA.open("r", newline="", encoding="utf-8") as archivo:
    for fila in csv.DictReader(archivo):
        print(fila["codigo"], fila["producto"], fila["cantidad"], fila["total"])
        total_vendido += float(fila["total"])  # el CSV entrega texto

print("Total vendido:", total_vendido)
