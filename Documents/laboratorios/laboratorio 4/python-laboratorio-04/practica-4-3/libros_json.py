# Práctica 4.3 - Ejercicio: Catálogo de libros.
# Guarda tres libros en libros.json y luego los lee y los muestra.
#
# Para la parte "modifica uno de los registros del archivo": abre libros.json
# con un editor, cambia por ejemplo el año de un libro, guarda y vuelve a
# ejecutar este script. Se mostrará el valor modificado, porque el archivo es
# la fuente de datos. Si introduces un error de sintaxis (una coma de más o
# de menos), json.load() lanzará JSONDecodeError, que aquí se informa.
import json
from pathlib import Path

RUTA = Path(__file__).resolve().parent / "libros.json"

libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "El coronel no tiene quien le escriba", "autor": "Gabriel García Márquez", "anio": 1961},
    {"codigo": "L003", "titulo": "Rayuela", "autor": "Julio Cortázar", "anio": 1963},
]


def guardar(libros):
    with RUTA.open("w", encoding="utf-8") as archivo:
        json.dump(libros, archivo, ensure_ascii=False, indent=4)


def cargar():
    with RUTA.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def mostrar(libros):
    for libro in libros:
        print(f'{libro["codigo"]} - {libro["titulo"]} ({libro["autor"]}, {libro["anio"]})')


if __name__ == "__main__":
    # Solo se crea el archivo la primera vez, para no pisar tus modificaciones manuales.
    if not RUTA.exists():
        guardar(libros)
        print("libros.json creado.")

    try:
        mostrar(cargar())
    except json.JSONDecodeError as error:
        print("libros.json no contiene JSON válido:", error)
