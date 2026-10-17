# Versión con el error (imprimía None):
#
#     def sumar(a, b):
#         resultado = a + b
#
# La función calculaba la suma pero no la devolvía, así que total valía None.
# Corrección: devolver el resultado con return (sin reemplazarlo por un 30 fijo).

def sumar(a, b):
    resultado = a + b
    return resultado


total = sumar(10, 20)
print(total)
