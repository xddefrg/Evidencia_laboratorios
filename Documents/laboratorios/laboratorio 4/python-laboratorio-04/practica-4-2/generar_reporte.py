# Práctica 4.2 - Ejercicio: Carpetas de reportes.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CARPETA = BASE_DIR / "reportes"

# 1. Crear la carpeta si no existe.
CARPETA.mkdir(parents=True, exist_ok=True)

# 2. Escribir resumen.txt con tres líneas.
ruta = CARPETA / "resumen.txt"
lineas = [
    "Resumen del periodo",
    "Pruebas ejecutadas: 12",
    "Estado general: sin incidentes críticos",
]
ruta.write_text("\n".join(lineas) + "\n", encoding="utf-8")

# 3. Volver a leerlo y mostrarlo.
print("Contenido del reporte:")
print(ruta.read_text(encoding="utf-8"))

# 4. Indicar dónde quedó guardado.
print("Guardado en:", ruta)
