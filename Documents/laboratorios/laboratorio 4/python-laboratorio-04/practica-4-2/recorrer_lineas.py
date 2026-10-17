# Práctica 4.2 - Sección 6: leer por líneas.
# strip() limpia solo la cadena mostrada; no cambia el archivo.
from pathlib import Path

RUTA = Path(__file__).resolve().parent / "pruebas.txt"

try:
    with open(RUTA, "r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, start=1):
            print(numero, "-", linea.strip())
except FileNotFoundError:
    print("Todavía no hay registros. Ejecuta bitacora.py primero.")
