# --- Versión con el error: nombre de atributo mal escrito ---
class PersonaConError:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(self.nombree)


try:
    PersonaConError("Ana").mostrar()
except AttributeError as error:
    # El atributo creado en __init__ es "nombre"; "nombree" nunca existió.
    print("Error:", error)


# --- Corrección: solo cambia el nombre del atributo ---
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(self.nombre)


Persona("Ana").mostrar()
