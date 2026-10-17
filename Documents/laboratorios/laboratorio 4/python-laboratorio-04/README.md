Laboratorio 4 — Excepciones, archivos, persistencia y POO en Python

| Carpeta | Contenido |
|---|---|
| `practica-4-1/` | Excepciones, validaciones y recuperación de errores |
| `practica-4-2/` | Archivos de texto, rutas y `pathlib` |
| `practica-4-3/` | Persistencia con JSON y exportación a CSV |
| `practica-4-4/` | Herencia, sobrescritura, polimorfismo y composición |
| `gestor_inventario/` | Reto integrador: gestor de inventario persistente (ver su `README.md`) |

Cada script se ejecuta de forma independiente desde su carpeta:

```bash
cd practica-4-1
python leer_edad.py        # también: py / python3
```

Los scripts que escriben archivos (`escribir_archivo.py`, `primer_json.py`, etc.)
los crean en la carpeta desde donde se ejecutan o junto al script, según se
indica en cada uno.

Los archivos `depuracion_*.py` muestran el código con error en un comentario,
la explicación y la corrección.

Proyecto final:

```bash
cd gestor_inventario
python main.py
python -m unittest -v      # pruebas automáticas
```
