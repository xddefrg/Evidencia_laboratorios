# Práctica 4.2 - Ejercicio: Bitácora de pruebas.
# Cada ejecución agrega una línea a pruebas.txt sin perder las anteriores.
from pathlib import Path

RUTA = Path(__file__).resolve().parent / "pruebas.txt"

nombre = input("Nombre de la prueba: ").strip()

while True:
    resultado = input("Resultado (aprobada/fallida): ").strip().lower()
    if resultado in ("aprobada", "fallida"):
        break
    print("Escribe 'aprobada' o 'fallida'.")

observacion = input("Observación breve: ").strip()

# Se evita que un salto de línea dentro de un dato rompa el formato
# de "una línea por prueba".
linea = " | ".join(parte.replace("\n", " ") for parte in (nombre, resultado, observacion))

with open(RUTA, "a", encoding="utf-8") as archivo:
    archivo.write(linea + "\n")

print("Registro agregado a", RUTA.name)
