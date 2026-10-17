class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        # self.nombre es el atributo del objeto; nombre es el parámetro recibido.
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalle(self):
        print("Código:", self.codigo)
        print("Producto:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad:", self.cantidad)

    def calcular_valor(self):
        return self.precio * self.cantidad


# No se escribe self al crear el objeto: Python lo proporciona solo.
teclado = Producto("P001", "Teclado", 85000, 4)

teclado.mostrar_detalle()
print("Valor:", teclado.calcular_valor())  # 340000

print()
print("--- Dos objetos de la misma clase ---")
mouse = Producto("P002", "Mouse", 45000, 7)

print("Valor del teclado:", teclado.calcular_valor())  # 340000
print("Valor del mouse:", mouse.calcular_valor())  # 315000

mouse.cantidad = 2

print("Cantidad del teclado (no cambió):", teclado.cantidad)  # 4
print("Cantidad del mouse:", mouse.cantidad)  # 2
print("Nuevo valor del mouse:", mouse.calcular_valor())  # 90000
