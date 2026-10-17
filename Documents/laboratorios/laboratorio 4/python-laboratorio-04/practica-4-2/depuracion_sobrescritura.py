# Práctica 4.2 - Depuración: sobrescritura accidental.
#
# ORIGINAL (con el error):
#
#   ruta.write_text("Registro 1\n", encoding="utf-8")
#   ruta.write_text("Registro 2\n", encoding="utf-8")
#
# ¿Por qué solo queda el segundo registro? Porque write_text() usa el modo
# "w": cada llamada reemplaza TODO el contenido anterior.
#
# CORRECCIÓN (opción A): abrir en modo "a" para agregar al final.
from pathlib import Path

ruta = Path("historial.txt")
ruta.write_text("", encoding="utf-8")  # empezar limpio para la demostración

with open(ruta, "a", encoding="utf-8") as archivo:
    archivo.write("Registro 1\n")
with open(ruta, "a", encoding="utf-8") as archivo:
    archivo.write("Registro 2\n")

print("Opción A (modo 'a'):")
print(ruta.read_text(encoding="utf-8"))

# CORRECCIÓN (opción B): escribir ambas líneas en una sola operación.
ruta.write_text("Registro 1\nRegistro 2\n", encoding="utf-8")

print("Opción B (una sola escritura):")
print(ruta.read_text(encoding="utf-8"))
