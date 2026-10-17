# Práctica 4.1 - Ejercicio: División segura.
# Diferencia: entrada no numérica, divisor cero y división válida.
# Pruebas: 10 / 2, 10 / 0 y una entrada "abc".
try:
    dividendo = float(input("Dividendo: "))
    divisor = float(input("Divisor: "))
    resultado = dividendo / divisor
except ValueError:
    print("Entrada no válida: debes escribir números.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
else:
    print(f"{dividendo} / {divisor} = {resultado}")
