"""Inventario: administra una colección de objetos Producto (composición).

No usa input() ni conoce archivos. Las operaciones que reciben datos
inválidos lanzan ValueError sin dejar el inventario a medio modificar.
"""
from producto import Producto


class Inventario:
    def __init__(self):
        # Diccionario código -> Producto: búsqueda directa y orden de registro.
        self._productos = {}

    def __len__(self):
        return len(self._productos)

    # ------------------------------------------------------------------
    # Operaciones principales
    # ------------------------------------------------------------------
    def registrar(self, producto):
        if not isinstance(producto, Producto):
            raise ValueError("Solo se pueden registrar objetos Producto.")
        if producto.codigo in self._productos:
            raise ValueError(f"Ya existe un producto con el código {producto.codigo}.")
        self._productos[producto.codigo] = producto

    def buscar(self, codigo):
        """Devuelve el Producto o None si no existe."""
        return self._productos.get(str(codigo).strip())

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con el código {str(codigo).strip()}.")
        # actualizar_cantidad valida antes de modificar.
        producto.actualizar_cantidad(nueva_cantidad)
        return producto

    def eliminar(self, codigo):
        producto = self.buscar(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con el código {str(codigo).strip()}.")
        del self._productos[producto.codigo]
        return producto

    # ------------------------------------------------------------------
    # Consultas (no modifican el inventario)
    # ------------------------------------------------------------------
    def listar(self):
        """Lista nueva con los productos; la colección interna no se expone."""
        return list(self._productos.values())

    def sin_stock(self):
        return [p for p in self._productos.values() if p.sin_stock]

    def resumen(self):
        productos = self.listar()
        sin_existencias = [p.nombre for p in productos if p.sin_stock]
        return {
            "productos": len(productos),
            "unidades": sum(p.cantidad for p in productos),
            "valor_total": sum(p.valor_inventario for p in productos),
            "sin_existencias": sin_existencias,
            "categorias_utilizadas": len({p.categoria for p in productos}),
        }

    # ------------------------------------------------------------------
    # Exportar / importar el estado
    # ------------------------------------------------------------------
    def exportar_datos(self):
        """Lista de diccionarios con todos los productos (copias de los datos)."""
        return [p.a_diccionario() for p in self._productos.values()]

    @classmethod
    def desde_datos(cls, registros):
        """Construye un inventario NUEVO a partir de una lista de diccionarios.

        Se arma primero un inventario temporal. Si cualquier registro es
        inválido o repite un código, se lanza ValueError y no se devuelve
        nada: no existe la carga parcial.
        """
        if not isinstance(registros, list):
            raise ValueError("Se esperaba una lista de productos.")

        temporal = cls()
        for indice, registro in enumerate(registros, start=1):
            try:
                temporal.registrar(Producto.desde_diccionario(registro))
            except ValueError as error:
                raise ValueError(f"Registro {indice}: {error}") from error
        return temporal
