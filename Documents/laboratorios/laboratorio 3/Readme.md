<!-- 
Respuestas del Laboratorio 03

Predicciones, explicaciones de depuración y respuestas a los apartados de *Comprobación*. Todas las predicciones se verificaron ejecutando el código.

#Práctica 3.1 — Funciones

**Predice: `presentar("Cali", "Luis")`.** No produce error: Python asigna los argumentos por posición, así que `nombre="Cali"` y `ciudad="Luis"`, y se imprime `Cali vive en Luis`. Se corrige respetando el orden: `presentar("Luis", "Cali")`.

**Predice: `calcular_total`.** Salidas: `100000.0` (sin descuento se usa el valor predeterminado 0), `90000.0` y `80000.0`.

**Depuración: faltó devolver el dato.** `sumar()` calculaba `resultado` pero nunca lo devolvía; sin `return` una función entrega `None`. Se corrige con `return resultado`.

**Comprobación**
- **`print()` frente a `return`:** `print()` muestra un texto en pantalla (efecto visible) pero no entrega nada al programa; `return` entrega un valor que se puede guardar, comparar o reutilizar, y termina la función.
- **Parámetro y argumento:** el parámetro es el nombre que aparece en la definición (`def saludar(nombre)`); el argumento es el valor concreto que se envía en cada llamada (`saludar("Laura")`).
- **Modificar la lista recibida o devolver una nueva:** si la función hace `append()` sobre la lista recibida, cambia el objeto original porque ambas referencias apuntan al mismo objeto. Si hace `copy()` y devuelve la copia modificada, el original queda intacto.

## Práctica 3.2 — Módulos

**Predice (`mensajes.py` y `main.py`).** `python main.py` imprime `Hasta luego` (el bloque `if __name__ == "__main__"` no corre al importar). `python mensajes.py` imprime `Prueba directa` (se ejecuta directamente y `__name__` vale `"__main__"`).

**Depuración: importación incorrecta.** `import operaciones` solo crea el nombre `operaciones` en `main.py`; `calcular_subtotal` existe dentro del módulo, no en el espacio de nombres de `main.py`, y por eso aparece `NameError`. Se corrige con `operaciones.calcular_subtotal(...)` o con `from operaciones import calcular_subtotal`.

**Comprobación**
- **Qué archivo se ejecuta:** el que se pasa a `python` (normalmente `main.py`); los demás solo se ejecutan si alguien los importa.
- **Qué significa importar:** Python ejecuta el código de nivel superior del módulo (una vez por proceso) y deja disponibles sus nombres.
- **`import modulo` o `from modulo import funcion`:** `import modulo` deja claro de dónde viene cada nombre (`modulo.funcion`) y evita choques; `from modulo import funcion` acorta las llamadas cuando se usan pocas funciones. Se evita `import *`.
- **`if __name__ == "__main__"`:** separa lo que se ejecuta al correr el archivo directamente (pruebas, demostraciones) de lo que ocurre al importarlo, para que un módulo importable no lance programas ni lea el teclado.

## Práctica 3.3 — Clases y objetos

**Atributo de clase compartido.** `elementos = []` en el cuerpo de la clase se crea una sola vez y todas las instancias que no tengan un atributo propio con ese nombre acceden a la misma lista; por eso `Teclado` aparece en `segundo`.

**Depuración: falta `self`.** Python pasa el objeto como primer argumento al llamar al método; `def mostrar():` no declara parámetros y falla con `TypeError`. Se corrige a `def mostrar(self):` y se usa `self.nombre`.

**Depuración: atributo inexistente.** El atributo creado en `__init__` es `nombre`; `nombree` nunca existió y da `AttributeError`.

**Comprobación**
- **`self`:** representa el objeto concreto que ejecuta el método; permite acceder a sus propios atributos.
- **`__init__`:** inicializa los atributos de un objeto recién creado.
- **`self.elementos = []`:** `__init__` se ejecuta por cada objeto que se crea, así que cada uno recibe su propia lista; no hay una lista única a nivel de clase.

## Práctica 3.4 — Encapsulamiento

**Comprobación**
- **Por qué `Inventario` conserva una colección de objetos:** el inventario gestiona la colección (registrar, buscar, eliminar) y cada `Producto` conoce y protege sus propios datos; cada clase tiene una sola responsabilidad.
- **Por qué `_productos` es interno:** el guion bajo indica por convención que es parte de la implementación; el resto del programa debe usar los métodos de la clase y no tocar la lista directamente.
- **Asignar libremente o usar un método con reglas:** una asignación directa (`producto.cantidad = -10`) acepta cualquier valor; un método (`actualizar_existencias`) o un setter puede rechazar los valores inválidos y mantener consistente el estado del objeto.

## Práctica 3.5 — Preguntas previas al reto

| Pregunta | Respuesta |
|---|---|
| ¿Qué clase debe evitar los códigos repetidos? | `Inventario`: es la que conoce todos los productos |
| ¿Qué clase debe comprobar que la cantidad sea válida? | `Producto`: controla sus propios valores |
| ¿Qué clase calcula el valor de un producto? | `Producto` (`calcular_valor()`) |
| ¿Dónde debe utilizarse `input()`? | Solo en `main.py` |
| ¿Quién decide qué mensaje se muestra tras una operación? | `main.py`, a partir de los valores devueltos por las clases |

La depuración de la sección 20 está en `gestor_inventario_depuracion/depuracion_errores.py`.
-->

