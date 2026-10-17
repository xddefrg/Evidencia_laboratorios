# Práctica 4.4 - Secciones 3 y 4: sobrescritura de métodos y polimorfismo.
#
# Predicción de las tres líneas:
#   Enviando notificación general
#   Enviando correo electrónico
#   Enviando mensaje de texto
class Notificacion:
    def enviar(self):
        return "Enviando notificación general"


class Correo(Notificacion):
    def enviar(self):
        return "Enviando correo electrónico"


class MensajeTexto(Notificacion):
    def enviar(self):
        return "Enviando mensaje de texto"


notificaciones = [Notificacion(), Correo(), MensajeTexto()]

for notificacion in notificaciones:
    print(notificacion.enviar())
