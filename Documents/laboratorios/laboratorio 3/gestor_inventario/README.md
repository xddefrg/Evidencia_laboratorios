# Gestor de inventario orientado a objetos

Aplicación de consola en Python 3 que registra, lista, busca, actualiza y elimina productos, y genera informes del inventario (productos sin stock y resumen). Cada producto es una instancia de `Producto` y su administración corresponde a una instancia de `Inventario`. No requiere instalar paquetes externos.

## Estructura de archivos

```
gestor_inventario/
├── main.py                    # menú, lectura de datos y presentación de resultados
├── producto.py                # clase Producto
├── inventario.py              # clase Inventario
├── pruebas_independencia.py   # dos inventarios no comparten datos
├── pruebas_automaticas.py     # batería de pruebas obligatorias (40 comprobaciones)
└── README.md
```

## Ejecución

Desde la carpeta `gestor_inventario`:

```
python main.py
```

Según el equipo, el comando puede ser `py main.py` o `python3 main.py`. Para las pruebas:

```
python pruebas_automaticas.py
python pruebas_independencia.py
```

## Responsabilidad de cada clase

| Elemento | Responsabilidad |
|---|---|
| `Producto` | Representa un artículo y controla sus valores. Valida código y nombre (no vacíos, ni solo espacios), categoría autorizada, precio mayor que cero y cantidad entera no negativa **desde la creación** (lanza `ValueError`). Ofrece propiedades de solo consulta (el código no se puede reasignar), `actualizar_existencias()` y `calcular_valor()`. |
| `Inventario` | Conserva una lista propia de objetos `Producto` (`self._productos`, creada en `__init__`). Registra (sin códigos repetidos), lista (devuelve una copia), busca (objeto o `None`), actualiza existencias, elimina, consulta productos sin stock (comprensión de lista) y calcula el resumen (comprensión de conjunto para las categorías). Las operaciones que modifican devuelven `True` o `False`. |
| `main.py` | Único lugar con `input()` y `print()`: muestra el menú, lee y valida entradas numéricas (repite la pregunta ante un valor inválido), captura `ValueError` al crear productos y decide qué mensaje mostrar. |

`Producto` e `Inventario` no usan `input()` ni imprimen: devuelven resultados y `main.py` los presenta. Las categorías (`CATEGORIAS`) se declaran una sola vez en `producto.py`.

## Pruebas realizadas y resultados observados

Todas se ejecutaron con `pruebas_automaticas.py` (**40/40 superadas**, código de salida 0) y, para el menú, con sesiones de entrada simuladas.

| Caso | Resultado observado |
|---|---|
| Iniciar inventario vacío | Listado vacío ("No hay productos registrados.") y resumen en cero |
| Registrar P001 | Registro aceptado |
| Registrar nuevamente P001 | Rechazado: "ya existe el código P001"; no se agrega nada |
| Código o nombre vacío (o solo espacios) | Rechazado: "El código no puede estar vacío." |
| Categoría no permitida | Rechazada, y el mensaje lista las categorías válidas |
| Precio cero o negativo | Rechazado |
| Cantidad negativa | Rechazada |
| Cantidad cero | Producto válido; aparece en "sin existencias" |
| Buscar P001 | Muestra su información |
| Buscar P999 | "No existe un producto con ese código." |
| Actualizar a 10 unidades | Cambia solo la cantidad (nombre, precio y categoría intactos) |
| Actualizar a -3 unidades | Rechazado; se conserva el dato anterior |
| Eliminar producto existente | Registro eliminado |
| Eliminar código inexistente | Informa sin fallar |
| Texto en un campo numérico | Mensaje ("Debes escribir un número entero.") y nueva oportunidad |
| Consultar resumen | Totales coherentes con los productos registrados |
| Salir (opción 0) | Termina el ciclo con "Programa finalizado." |

### Comprobación numérica

Con P001 (85000 × 4, Periféricos), P002 (45000 × 0, Periféricos) y P003 (700000 × 2, Componentes):

- Productos registrados: 3
- Unidades disponibles: 6
- Valor del inventario: $1740000.0
- Categorías utilizadas: 2
- Producto sin stock: Mouse

Después de actualizar P002 a cinco unidades: 3 productos, 11 unidades y valor $1965000.0.

### Prueba de independencia

`pruebas_independencia.py` imprime `Primero: 1` y `Segundo: 0`: registrar en un inventario no afecta al otro. También se comprobó que actualizar o eliminar en uno no modifica al otro.

### Notas sobre la salida

- La línea del resumen muestra la cantidad y los nombres de las categorías, por ejemplo `Categorías utilizadas: 2 (Componentes, Periféricos)`. Así cubre tanto el ejemplo de ejecución (nombres) como la comprobación numérica (cantidad).
- Los precios se leen con `float()`, por eso se muestran como `$85000.0`, igual que en el ejemplo de ejecución del enunciado.
- Si la entrada termina de forma inesperada (Ctrl+D o Ctrl+C) el programa se cierra con el mensaje "Programa interrumpido." en lugar de mostrar una traza de error.
