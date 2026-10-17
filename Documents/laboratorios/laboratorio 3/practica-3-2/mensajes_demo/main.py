from mensajes import despedir

# Predicción:
#   python main.py      -> "Hasta luego"   (el bloque __main__ de mensajes.py no corre)
#   python mensajes.py  -> "Prueba directa" (se ejecuta directamente; despedir() no se llama)
print(despedir())
