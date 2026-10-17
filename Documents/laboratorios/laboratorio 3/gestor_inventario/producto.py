"""Clase Producto: representa un artículo y controla sus valores.

No usa input() ni imprime nada: solo guarda datos, valida y calcula.
"""

import math

# Única copia de las categorías autorizadas; otros módulos la importan de aquí.
CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        # Las validaciones se aplican desde la creación: un producto no puede
        # "nacer" con datos inválidos. Si algo falla se lanza ValueError y el
        # objeto no llega a crearse.
        self._codigo = self._validar_texto(codigo, "El código")
        self._nombre = self._validar_texto(nombre, "El nombre")
        self._categoria = self._validar_categoria(categoria)
        self._precio = self._validar_precio(precio)

        if not self._cantidad_es_valida(cantidad):
            raise ValueError("La cantidad debe ser un entero mayor o igual que cero.")
        self._cantidad = cantidad

    # --- Validaciones individuales ---
    @staticmethod
    def _validar_texto(valor, etiqueta):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError(f"{etiqueta} no puede estar vacío.")
        return valor.strip()

    @staticmethod
    def _validar_categoria(categoria):
        if categoria not in CATEGORIAS:
            permitidas = ", ".join(CATEGORIAS)
            raise ValueError(f"La categoría debe ser una de: {permitidas}.")
        return categoria

    @staticmethod
    def _validar_precio(precio):
        es_numero = isinstance(precio, (int, float)) and not isinstance(precio, bool)

        if not es_numero or not math.isfinite(precio) or precio <= 0:
            raise ValueError("El precio debe ser un número mayor que cero.")
        return precio

    @staticmethod
    def _cantidad_es_valida(cantidad):
        es_entero = isinstance(cantidad, int) and not isinstance(cantidad, bool)
        return es_entero and cantidad >= 0

    # --- Propiedades de consulta (sin setters: el código no se cambia libremente) ---
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    # --- Operaciones ---
    def actualizar_existencias(self, nueva_cantidad):
        """Cambia solo las existencias. Devuelve False si el valor no es válido."""
        if not self._cantidad_es_valida(nueva_cantidad):
            return False

        self._cantidad = nueva_cantidad
        return True

    def calcular_valor(self):
        """Valor de las existencias: precio unitario por cantidad."""
        return self._precio * self._cantidad
