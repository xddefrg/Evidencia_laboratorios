# Práctica 4.3 - Secciones 4, 5 y 6: los objetos propios no se guardan
# directamente en JSON; hay que convertirlos a diccionarios y reconstruirlos.
import json


class Producto:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["codigo"],
            datos["nombre"]
        )


producto = Producto("P001", "Teclado")

# Sección 4: json.dumps(producto) falla porque no sabe serializar la clase.
try:
    json.dumps(producto)
except TypeError as error:
    print("TypeError esperado:", error)

# Sección 5: convertir a diccionario primero.
print(json.dumps(producto.a_diccionario(), ensure_ascii=False))

# Sección 6: reconstruir un objeto a partir de un diccionario.
datos = {"codigo": "P002", "nombre": "Mouse"}

nuevo = Producto.desde_diccionario(datos)

print(type(nuevo))
print(nuevo.nombre)
