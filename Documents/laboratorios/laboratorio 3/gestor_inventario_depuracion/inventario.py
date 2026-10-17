"""Clase Inventario: colección de objetos Producto, operaciones y reportes.

No usa input() ni imprime nada: devuelve resultados para que main.py decida
qué mostrar.
"""

from producto import Producto


class Inventario:
    def __init__(self):
        # La lista se crea aquí, al instanciar, para que cada inventario tenga
        # la suya. Si estuviera en el cuerpo de la clase se compartiría.
        self._productos = []

    def registrar_producto(self, producto):
        """Registra el producto. Devuelve False si no es un Producto o su código ya existe."""
        if not isinstance(producto, Producto):
            return False

        if self.buscar_por_codigo(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def listar_productos(self):
        """Devuelve una copia de la lista: modificarla no altera el inventario."""
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        """Devuelve el Producto con ese código o None. No modifica nada."""
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        """Cambia las existencias respetando las reglas de Producto."""
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        return producto.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        """Quita el producto si existe. Devuelve True si lo eliminó."""
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        """Nombres de los productos cuya cantidad es cero."""
        return [
            producto.nombre
            for producto in self._productos
            if producto.cantidad == 0
        ]

    def resumen(self):
        """Totales del inventario: productos, unidades, valor y categorías usadas."""
        categorias = {producto.categoria for producto in self._productos}

        return {
            "productos": len(self._productos),
            "unidades": sum(producto.cantidad for producto in self._productos),
            # El valor inicial 0.0 hace que el total sea siempre un número decimal.
            "valor": sum(
                (producto.calcular_valor() for producto in self._productos), 0.0
            ),
            "categorias": categorias,
        }
