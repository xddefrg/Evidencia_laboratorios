# Gestor de inventario persistente

Versión del Laboratorio 4 del gestor de inventario. Conserva las operaciones de
la versión orientada a objetos del Laboratorio 3 (`Producto` e `Inventario`) y
agrega **persistencia en JSON**, **exportación a CSV** y **manejo de errores de
entrada y de archivos**. Solo usa módulos de la biblioteca estándar
(`json`, `csv`, `pathlib`).

> Nota: este proyecto se construyó a partir de la especificación del
> laboratorio. Si ya tienes tu propio `producto.py` / `inventario.py` del
> Laboratorio 3, compáralos con estos y adapta lo que necesites; los métodos
> nuevos son `a_diccionario`, `desde_diccionario`, `exportar_datos` y
> `desde_datos`.

## Cómo ejecutarlo

Desde esta carpeta:

```bash
python main.py        # también: py main.py / python3 main.py
```

La ruta de los datos se calcula a partir de la ubicación de los módulos, así que
funciona aunque lo lances desde otra carpeta (`python ruta/a/main.py`).

Pruebas automáticas (usan carpetas temporales; no tocan tus datos):

```bash
python -m unittest -v
```

## Estructura

| Archivo | Responsabilidad | ¿Conoce el sistema de archivos? |
|---|---|---|
| `producto.py` | Representa un producto, valida sus datos y lo convierte a/desde diccionario | No |
| `inventario.py` | Administra objetos `Producto` (registrar, buscar, actualizar, eliminar, consultar) | No |
| `almacenamiento.py` | Lee y escribe `datos/productos.json` | Sí |
| `reportes.py` | Construye y exporta `reportes/inventario.csv` | Sí |
| `main.py` | Menú, lectura de entradas, coordinación y mensajes | No (solo llama a los módulos anteriores) |
| `test_gestor.py` | Pruebas automáticas | Solo carpetas temporales |

`datos/productos.json` y `reportes/inventario.csv` se generan al usar el
programa; no hay que crearlos a mano. Solo `main.py` usa `input()`.

## Reglas de los productos

- Código único, no vacío.
- Nombre no vacío.
- Categoría en `("Periféricos", "Componentes", "Accesorios")`.
- Precio numérico, **finito** y mayor que cero (se rechazan `nan`, `inf`, `0` y negativos).
- Cantidad entera mayor o igual que cero (`0` se acepta: producto sin existencias).

`Producto.desde_diccionario()` reconstruye pasando por el constructor, así que
los datos leídos del JSON se validan igual que los escritos por el usuario.

## Decisiones de diseño

- **Composición, no herencia:** `Inventario` contiene objetos `Producto`.
- **Una operación rechazada no cambia nada:** se valida antes de modificar y no se guarda.
- **Carga todo o nada:** `Inventario.desde_datos()` arma primero un inventario
  temporal; si algún registro es inválido o repite un código, no se devuelve nada.
- **Tres estados del archivo** (`almacenamiento.cargar_inventario`):

  | Situación | Comportamiento |
  |---|---|
  | `productos.json` no existe | Inventario vacío |
  | Existe y es válido | Se recuperan los productos |
  | Existe pero está dañado o tiene datos inválidos | Se informa, **no se sobrescribe** y el programa entra en modo de solo consulta (se bloquean registrar, actualizar, eliminar, guardar y exportar) |

- **Guardado seguro:** se escribe en `productos.json.tmp` y se reemplaza el original
  al terminar (así un fallo a mitad de escritura no deja el JSON truncado).
  Solo se anuncia «Inventario guardado.» cuando la escritura se confirmó; si falla,
  se advierte que los cambios están solo en memoria y se reintenta al salir.
- **CSV = exportación:** `valor_inventario = precio * cantidad` (calculado en
  `Producto.valor_inventario`). Se genera al pedirlo; no se mantiene sincronizado.

## Pruebas realizadas

Resultados de ejecutar el programa y `python -m unittest` (33 pruebas, todas OK).

| Situación (tabla 16) | Resultado |
|---|---|
| Primera ejecución, JSON inexistente | Inventario vacío sin error |
| Guardar dos productos | JSON con ambos registros |
| Cerrar y reiniciar | Se recuperan los productos |
| Código duplicado | Se rechaza; el JSON no se duplica |
| Categoría desconocida | Se rechaza |
| Precio negativo | Se rechaza |
| `nan` / `inf` como precio | Se rechaza |
| Cantidad negativa | Se rechaza |
| Cantidad cero | Se acepta |
| Actualizar una cantidad | Se conserva tras reiniciar |
| Eliminar un producto | Sigue eliminado tras reiniciar |
| Texto no numérico en precio/cantidad | Mensaje y nueva oportunidad |
| JSON con sintaxis incorrecta | Se informa; archivo intacto (verificado byte a byte) |
| JSON con estructura inesperada | Se rechaza la carga; archivo intacto |
| JSON con código repetido | No se acepta carga parcial; archivo intacto |
| Error de escritura | Se advierte que no se confirmó el guardado; el JSON en disco no cambia |
| Exportar CSV | Encabezados y valores correctos |
| Resumen | Totales correctos |
| Opción `0` | Salida controlada |

### Prueba numérica (sección 17)

| Paso | Productos | Unidades | Valor | Sin existencias | Categorías |
|---|---:|---:|---:|---|---:|
| Registrar P001, P002, P003 | 3 | 6 | $1740000.0 | Mouse | 2 |
| Reiniciar | 3 | 6 | $1740000.0 | Mouse | 2 |
| Mouse a 5, guardar y reiniciar | 3 | 11 | $1965000.0 | Ninguno | 2 |

CSV tras el cambio:

```text
codigo,nombre,categoria,precio,cantidad,valor_inventario
P001,Teclado,Periféricos,85000.0,4,340000.0
P002,Mouse,Periféricos,45000.0,5,225000.0
P003,Monitor,Componentes,700000.0,2,1400000.0
```

### Prueba de archivo dañado (sección 18)

1. Se guardó un inventario válido y se hizo una copia de `productos.json`.
2. Se eliminó una coma del JSON (`Expecting ',' delimiter`, línea 9, columna 5).
3. Al ejecutar, el programa detectó el error y entró en modo de solo consulta.
4. Los intentos de registrar, actualizar, eliminar, guardar y exportar fueron bloqueados.
5. El archivo dañado quedó **idéntico** (no se reemplazó por `[]`).
6. Se restauró la copia válida y al reiniciar volvieron a cargarse los productos.

## Limitaciones

- No hay confirmación antes de eliminar un producto.
- Con el archivo dañado, la corrección es manual: editar el JSON o restaurar una
  copia y reiniciar. No incluye herramienta de reparación.
- No se hace copia de seguridad del JSON antes de cada guardado.
