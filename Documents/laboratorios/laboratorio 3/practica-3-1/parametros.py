def saludar(nombre):
    print(f"Hola, {nombre}")


# nombre es el parámetro; "Laura" y "Andrés" son argumentos de llamadas distintas.
saludar("Laura")
saludar("Andrés")


def mostrar_producto(nombre, cantidad):
    print(f"Producto: {nombre}")
    print(f"Existencias: {cantidad}")


mostrar_producto("Teclado", 4)
mostrar_producto("Mouse", 7)


# --- Antes de ejecutar: Predice ---
def presentar(nombre, ciudad):
    print(f"{nombre} vive en {ciudad}")


presentar("Ana", "Bogotá")

# Predicción: la segunda llamada NO produce un error, sino una frase extraña,
# porque los argumentos posicionales se asignan en orden:
#     presentar("Cali", "Luis")  ->  "Cali vive en Luis"
#
# Corrección: respetar el orden (nombre, ciudad).
presentar("Luis", "Cali")
