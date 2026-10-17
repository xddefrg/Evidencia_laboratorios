# Práctica 4.2 - Reto: historial persistente de operaciones.
# Cada registro es una línea de texto "concepto | valor" en operaciones.txt.
# Sin JSON: el objetivo es entender archivos de texto y rutas.
import math
from pathlib import Path

RUTA = Path(__file__).resolve().parent / "operaciones.txt"
SEPARADOR = " | "


def registrar_operacion():
    concepto = input("Concepto: ").strip()
    if concepto == "":
        print("El concepto es obligatorio.")
        return

    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("El valor debe ser un número.")
        return

    if not math.isfinite(valor):
        print("El valor debe ser un número finito.")
        return

    # Los saltos de línea romperían el formato "una línea por registro".
    concepto = concepto.replace("\n", " ").replace(SEPARADOR.strip(), "/")

    try:
        with open(RUTA, "a", encoding="utf-8") as archivo:
            archivo.write(f"{concepto}{SEPARADOR}{valor}\n")
    except OSError as error:
        print("No se pudo guardar la operación:", error)
        return

    print("Operación registrada.")


def mostrar_historial():
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print("Todavía no hay historial: registra una operación primero.")
        return

    if not lineas:
        print("El historial está vacío.")
        return

    print("--- Historial ---")
    for numero, linea in enumerate(lineas, start=1):
        print(numero, "-", linea)


def main():
    while True:
        print("\n1. Registrar operación")
        print("2. Mostrar historial")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_operacion()
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
