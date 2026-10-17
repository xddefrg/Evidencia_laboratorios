class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print("Nombre:", self.nombre)
        print("Ficha:", self.ficha)
        print("Promedio:", self.promedio)

    def aprobo(self):
        return self.promedio >= 3.0


primero = Estudiante("Laura", "2901234", 2.8)
segundo = Estudiante("Andrés", "2901235", 4.1)

primero.mostrar_perfil()
print("¿Aprobó?", primero.aprobo())  # False

print()
segundo.mostrar_perfil()
print("¿Aprobó?", segundo.aprobo())  # True
