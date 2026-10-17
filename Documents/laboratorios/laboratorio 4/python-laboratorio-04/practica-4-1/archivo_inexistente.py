# Práctica 4.1 - Sección 8: reconocer un archivo inexistente.
from pathlib import Path

ruta = Path("archivo_que_no_existe.txt")

try:
    contenido = ruta.read_text(encoding="utf-8")
    print(contenido)
except FileNotFoundError:
    print("No se encontró el archivo solicitado.")
