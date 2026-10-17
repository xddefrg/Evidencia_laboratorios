# Práctica 4.4 - Reto: sistema de notificaciones.
#
# Beneficio de una operación común (enviar):
#   El código que usa las notificaciones recorre la colección y llama a
#   enviar(mensaje) sin preguntar de qué tipo es cada objeto. Para agregar
#   un canal nuevo (por ejemplo SMS) basta con crear otra clase con enviar();
#   el ciclo que las usa no cambia (abierto a extensión, cerrado a cambios).
#
# Responsabilidades que deben quedar FUERA de cada notificación:
#   - decidir a quién y cuándo se avisa (lógica de negocio);
#   - construir el contenido del mensaje (formato y plantillas);
#   - validar destinatarios, reintentos y registro de fallos;
#   - guardar el historial de envíos (almacenamiento).
#   Cada clase solo sabe cómo ENTREGAR un mensaje por su canal.
class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError("Cada canal debe implementar enviar().")


class NotificacionCorreo(Notificacion):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    def enviar(self, mensaje):
        return f"[Correo a {self.destinatario}] {mensaje}"


class NotificacionConsola(Notificacion):
    def enviar(self, mensaje):
        return f"[Consola] {mensaje}"


canales = [
    NotificacionCorreo("aprendiz@example.com"),
    NotificacionConsola(),
]

for canal in canales:
    print(canal.enviar("El inventario fue guardado."))
