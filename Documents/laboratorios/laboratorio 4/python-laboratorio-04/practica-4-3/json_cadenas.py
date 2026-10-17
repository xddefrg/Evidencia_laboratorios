# Práctica 4.3 - Sección 3: dumps / loads trabajan con cadenas de texto.
import json

producto = {"nombre": "Cámara", "precio": 120000}

texto = json.dumps(producto, ensure_ascii=False)
recuperado = json.loads(texto)

print(texto)
print(recuperado["nombre"])
