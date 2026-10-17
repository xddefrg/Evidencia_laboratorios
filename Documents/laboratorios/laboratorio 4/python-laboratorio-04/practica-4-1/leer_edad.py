# Práctica 4.1 - Ejercicio: Edad válida.
# Mensajes distintos para error de conversión y para valores fuera de rango.
# Pruebas: veinte, -1, 121, 20.

EDAD_MAXIMA = 120

try:
    edad = int(input("Edad: "))
except ValueError:
    print("Error de conversión: debes escribir un número entero.")
else:
    if edad < 0:
        print("Fuera de rango: la edad no puede ser negativa.")
    elif edad > EDAD_MAXIMA:
        print(f"Fuera de rango: la edad no puede ser superior a {EDAD_MAXIMA}.")
    else:
        print("Edad aceptada:", edad)
