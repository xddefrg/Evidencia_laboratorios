# Práctica 4.3 - Depuración: archivo JSON mal formado.
import json

# ORIGINAL (inválido): falta la coma entre los dos objetos.
mal_formado = """
[
  {"codigo": "P001", "nombre": "Teclado"}
  {"codigo": "P002", "nombre": "Mouse"}
]
"""

try:
    json.loads(mal_formado)
except json.JSONDecodeError as error:
    print("Error esperado:", error)
    print("Motivo: en una lista JSON los elementos se separan con comas.")

# CORRECCIÓN: agregar la coma que falta.
corregido = """
[
  {"codigo": "P001", "nombre": "Teclado"},
  {"codigo": "P002", "nombre": "Mouse"}
]
"""

datos = json.loads(corregido)
print("Corregido, registros leídos:", len(datos))
