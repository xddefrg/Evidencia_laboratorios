
curso = {
    "nombre": "Programación en Python",
    "codigo": "PY101",
    "temas": ["Variables", "Listas", "Diccionarios"],
    "instructor": {
        "nombre": "Laura Gómez",
        "especialidad": "Desarrollo de software"
    }
}


print("Nombre del curso:", curso["nombre"])


print("Segundo tema:", curso["temas"][1])

print("Nombre del instructor:", curso["instructor"]["nombre"])
print("Cantidad de temas:", len(curso["temas"]))