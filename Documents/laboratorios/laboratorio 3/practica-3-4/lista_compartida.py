# --- Versión con el error: la lista vive en la clase ---
class InventarioCompartido:
    productos = []

    def agregar(self, producto):
        self.productos.append(producto)


primero = InventarioCompartido()
segundo = InventarioCompartido()

primero.agregar("Teclado")
print("Segundo (¡no está vacío!):", segundo.productos)  # ['Teclado']


# --- Corrección: crear la lista dentro de __init__ ---
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)


primero = Inventario()
segundo = Inventario()

primero.agregar("Teclado")
print("Primero:", primero.productos)  # ['Teclado']
print("Segundo:", segundo.productos)  # []
