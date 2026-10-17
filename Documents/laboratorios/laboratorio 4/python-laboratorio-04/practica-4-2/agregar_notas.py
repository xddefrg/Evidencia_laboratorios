# Práctica 4.2 - Sección 5: agregar sin reemplazar (modo "a").
# Si lo ejecutas dos veces, la línea adicional aparece dos veces:
# el modo "a" siempre agrega al final y conserva lo anterior.
with open("notas.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Una observación adicional\n")
