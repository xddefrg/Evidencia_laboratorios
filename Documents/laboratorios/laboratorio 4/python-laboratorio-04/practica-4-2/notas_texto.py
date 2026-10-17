# Práctica 4.2 - Sección 4: with open(...) cierra el archivo automáticamente.
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera observación\n")
    archivo.write("Segunda observación\n")

with open("notas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)
