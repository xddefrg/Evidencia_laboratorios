# --- Versión con el error: el método no declara self ---
class SaludoConError:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar():
        print("Hola")


saludo_malo = SaludoConError("Ana")

try:
    saludo_malo.mostrar()
except TypeError as error:
    # Python pasa el objeto como primer argumento, pero mostrar() no recibe ninguno.
    print("Error:", error)


# --- Corrección: self como primer parámetro, y uso del nombre ---
class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Hola, {self.nombre}")


saludo = Saludo("Ana")
saludo.mostrar()
