# Práctica 4.1 - Depuración: capturar lo que no corresponde.
#
# ORIGINAL (con el error):
#
#   try:
#       numero = int("hola")
#   except ZeroDivisionError:
#       print("No se pudo convertir.")
#
# ¿Por qué no se atiende? int("hola") lanza ValueError, y el bloque solo
# captura ZeroDivisionError. Como los tipos no coinciden, la excepción
# se propaga y el programa se interrumpe.
#
# CORRECCIÓN: capturar el tipo de excepción que realmente ocurre.
try:
    numero = int("hola")
except ValueError:
    print("No se pudo convertir.")
