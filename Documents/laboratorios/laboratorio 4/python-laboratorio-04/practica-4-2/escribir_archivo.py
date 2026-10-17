# Práctica 4.2 - Sección 1: guardar texto.
# write_text() crea el archivo o REEMPLAZA todo su contenido si ya existe.
from pathlib import Path

ruta = Path("mensaje.txt")
ruta.write_text("Primer archivo de Python.\n", encoding="utf-8")

print("Archivo guardado:", ruta)
