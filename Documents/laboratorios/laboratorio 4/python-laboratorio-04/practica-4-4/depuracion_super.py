# Práctica 4.4 - Depuración: no se inicializó la clase base.
#
# ORIGINAL (con el error):
#
#   class Aprendiz(Persona):
#       def __init__(self, nombre, ficha):
#           self.ficha = ficha          # <- nunca llama a Persona.__init__
#
#   aprendiz = Aprendiz("Carlos", "123456")
#   print(aprendiz.nombre)              # AttributeError
#
# ¿Por qué falla? Al definir __init__ en la clase hija, Python deja de ejecutar
# automáticamente el __init__ de la clase base. Por eso "nombre" nunca se asigna.
#
# CORRECCIÓN: llamar a super().__init__(nombre).
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Aprendiz(Persona):
    def __init__(self, nombre, ficha):
        super().__init__(nombre)
        self.ficha = ficha


aprendiz = Aprendiz("Carlos", "123456")
print(aprendiz.nombre)
print(aprendiz.ficha)
