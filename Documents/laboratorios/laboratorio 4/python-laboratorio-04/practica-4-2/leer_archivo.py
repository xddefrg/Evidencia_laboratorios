# Práctica 4.2 - Sección 2: leer texto.
# Atendemos FileNotFoundError como se aprendió en la práctica 4.1.
from pathlib import Path

ruta = Path("mensaje.txt")

try:
    contenido = ruta.read_text(encoding="utf-8")
except FileNotFoundError:
    print("No existe mensaje.txt. Ejecuta primero escribir_archivo.py.")
else:
    print("Contenido:")
    print(contenido)
