def duplicar(numero):
    resultado = numero * 2
    return resultado


doble = duplicar(8)
print(doble)

# resultado es una variable LOCAL de duplicar(): no existe fuera de la función.
# Se captura el error para mostrarlo sin detener el programa.
try:
    print(resultado)
except NameError as error:
    print("Error:", error)

# Fuera de la función se usa el valor devuelto, guardado en doble.
print("Valor devuelto, guardado en doble:", doble)
