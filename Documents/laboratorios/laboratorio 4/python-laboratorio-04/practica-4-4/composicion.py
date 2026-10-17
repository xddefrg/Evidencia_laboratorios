# Práctica 4.4 - Sección 5: composición. Un objeto utiliza otros objetos.
#
# Un Inventario CONTIENE productos (no es un tipo de producto), por eso
# no tendría sentido "class Inventario(Producto)".
#
# Este ejemplo solo imprime un mensaje: NO escribe un archivo. Sirve para
# ver que un objeto puede delegar una responsabilidad en otro.
class Almacenamiento:
    def guardar(self, datos):
        print("Guardando", len(datos), "registros")


class ServicioInventario:
    def __init__(self, almacenamiento):
        self.almacenamiento = almacenamiento

    def guardar_inventario(self, productos):
        self.almacenamiento.guardar(productos)


servicio = ServicioInventario(Almacenamiento())
servicio.guardar_inventario(["Teclado", "Mouse"])
