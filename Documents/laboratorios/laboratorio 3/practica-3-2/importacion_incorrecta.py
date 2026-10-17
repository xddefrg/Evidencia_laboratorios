import operaciones

# Versión con el error:
#
#     import operaciones
#     print(calcular_subtotal(10000, 3))     # NameError
#
# "import operaciones" solo crea en este archivo el nombre "operaciones".
# La función calcular_subtotal existe DENTRO del módulo, no en este archivo,
# por eso hay que llamarla con el prefijo del módulo.
try:
    print(calcular_subtotal(10000, 3))
except NameError as error:
    print("Error:", error)

# Corrección 1: usar el prefijo del módulo.
print(operaciones.calcular_subtotal(10000, 3))

# Corrección 2 (alternativa): importar el nombre de la función.
from operaciones import calcular_subtotal

print(calcular_subtotal(10000, 3))
