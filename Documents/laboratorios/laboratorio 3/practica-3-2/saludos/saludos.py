def saludar(nombre):
    return f"Hola, {nombre}"


# Este bloque solo corre cuando se ejecuta saludos.py directamente.
# Al importar el módulo, __name__ vale "saludos" y el bloque se omite.
if __name__ == "__main__":
    print(saludar("Prueba"))
