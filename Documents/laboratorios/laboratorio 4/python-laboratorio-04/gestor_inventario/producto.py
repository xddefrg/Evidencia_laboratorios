"""Producto: representa un artículo del inventario y protege sus reglas.

Este módulo no lee del teclado ni conoce el sistema de archivos. Solo valida
datos, expone consultas y sabe convertirse a/desde un diccionario.
"""
import math

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

CAMPOS = ("codigo", "nombre", "categoria", "precio", "cantidad")


class Producto:
    """Un producto con código único, nombre, categoría, precio y existencias."""

    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        # Cada validación lanza ValueError antes de asignar, de modo que un
        # producto inválido nunca llega a existir.
        self._codigo = self._validar_codigo(codigo)
        self._nombre = self._validar_nombre(nombre)
        self._categoria = self._validar_categoria(categoria)
        self._precio = self._validar_precio(precio)
        self._cantidad = self._validar_cantidad(cantidad)

    # ------------------------------------------------------------------
    # Validaciones (devuelven el valor normalizado o lanzan ValueError)
    # ------------------------------------------------------------------
    @staticmethod
    def _validar_codigo(codigo):
        if not isinstance(codigo, str) or codigo.strip() == "":
            raise ValueError("El código es obligatorio.")
        return codigo.strip()

    @staticmethod
    def _validar_nombre(nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre es obligatorio.")
        return nombre.strip()

    @staticmethod
    def _validar_categoria(categoria):
        if categoria not in CATEGORIAS:
            permitidas = ", ".join(CATEGORIAS)
            raise ValueError(f"Categoría desconocida. Permitidas: {permitidas}.")
        return categoria

    @staticmethod
    def _validar_precio(precio):
        # bool es subclase de int: se rechaza explícitamente.
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser un número.")

        try:
            valor = float(precio)
        except OverflowError:
            raise ValueError("El precio debe ser un número finito.") from None

        if not math.isfinite(valor):
            raise ValueError("El precio debe ser un número finito.")
        if valor <= 0:
            raise ValueError("El precio debe ser positivo.")
        return valor

    @staticmethod
    def _validar_cantidad(cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        return cantidad

    # ------------------------------------------------------------------
    # Consultas
    # ------------------------------------------------------------------
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

    @property
    def sin_stock(self):
        return self._cantidad == 0

    @property
    def valor_inventario(self):
        """Valor de las existencias: precio unitario por cantidad."""
        return self._precio * self._cantidad

    # ------------------------------------------------------------------
    # Operación que modifica el estado
    # ------------------------------------------------------------------
    def actualizar_cantidad(self, nueva_cantidad):
        """Cambia las existencias. Valida PRIMERO; si falla, nada cambia."""
        nueva_cantidad = self._validar_cantidad(nueva_cantidad)
        self._cantidad = nueva_cantidad

    # ------------------------------------------------------------------
    # Serialización
    # ------------------------------------------------------------------
    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Reconstruye un Producto pasando por el constructor (con validaciones)."""
        if not isinstance(datos, dict):
            raise ValueError("Cada producto debe ser un objeto con sus cinco campos.")

        faltantes = [campo for campo in CAMPOS if campo not in datos]
        if faltantes:
            raise ValueError("Faltan campos: " + ", ".join(faltantes) + ".")

        sobrantes = [campo for campo in datos if campo not in CAMPOS]
        if sobrantes:
            raise ValueError("Campos no reconocidos: " + ", ".join(sobrantes) + ".")

        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"],
        )

    def __str__(self):
        return (
            f"{self.codigo} | {self.nombre} | {self.categoria} | "
            f"${self.precio} | {self.cantidad} uds."
        )

    def __repr__(self):
        return (
            f"Producto(codigo={self.codigo!r}, nombre={self.nombre!r}, "
            f"categoria={self.categoria!r}, precio={self.precio!r}, "
            f"cantidad={self.cantidad!r})"
        )
