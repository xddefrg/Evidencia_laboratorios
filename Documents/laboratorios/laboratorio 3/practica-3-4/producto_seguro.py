class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        # Atributos "internos" por convención (guion bajo inicial).
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def calcular_valor(self):
        return self._precio * self._cantidad

    # --- Propiedades de solo consulta: se leen sin paréntesis ---
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    # --- Modificación controlada de existencias ---
    def actualizar_existencias(self, nueva_cantidad):
        if nueva_cantidad < 0:
            return False

        self._cantidad = nueva_cantidad
        return True

    # --- Propiedad con setter que valida ---
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._precio = nuevo_precio


producto = Producto("P001", "Teclado", 85000, 4)
print("Valor:", producto.calcular_valor())  # 340000

print(producto.codigo)
print(producto.nombre)
print(producto.cantidad)

# El código no tiene setter: no se puede reasignar.
try:
    producto.codigo = "P999"
except AttributeError as error:
    print("No se puede cambiar el código:", error)

print()
print(producto.actualizar_existencias(10))  # True
print(producto.cantidad)  # 10

print(producto.actualizar_existencias(-5))  # False
print(producto.cantidad)  # sigue en 10

print()
producto.precio = 90000
print(producto.precio)  # 90000

try:
    producto.precio = -5000
except ValueError as error:
    print("ValueError:", error)

print(producto.precio)  # sigue en 90000

# Observación: el constructor de este ejemplo NO valida, así que un producto
# puede nacer inválido. Se corrige en el reto integrador (gestor_inventario).
nacio_mal = Producto("P002", "Mouse", -100, -3)
print()
print("Producto creado con datos inválidos:", nacio_mal.precio, nacio_mal.cantidad)
