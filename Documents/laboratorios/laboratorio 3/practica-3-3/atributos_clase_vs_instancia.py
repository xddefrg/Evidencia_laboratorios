# --- Versión con el problema: atributo de clase mutable ---
class RegistroCompartido:
    # Esta lista se crea UNA sola vez, en la clase, y la comparten todas las
    # instancias que no tengan un atributo propio con ese nombre.
    elementos = []


primero = RegistroCompartido()
segundo = RegistroCompartido()

primero.elementos.append("Teclado")
print("Segundo (¡compartida!):", segundo.elementos)  # ['Teclado']


# --- Corrección: atributo de instancia creado en __init__ ---
class Registro:
    def __init__(self):
        # Cada objeto que se crea ejecuta __init__ y recibe SU PROPIA lista.
        self.elementos = []


primero = Registro()
segundo = Registro()

primero.elementos.append("Teclado")

print("Primero:", primero.elementos)  # ['Teclado']
print("Segundo:", segundo.elementos)  # []
