class Inventario:
    def __init__(self):
        # Lista propia de cada inventario, creada al instanciar (no en la clase).
        self._productos = []

    def agregar(self, producto):
        # No se permiten códigos duplicados.
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def listar(self):
        # Devuelve una copia de la lista: quien la reciba no altera la interna.
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def eliminar(self, codigo):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True
