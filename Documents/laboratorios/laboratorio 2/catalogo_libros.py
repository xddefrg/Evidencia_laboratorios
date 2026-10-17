
libros = [
    {
        "codigo": "L001",
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "anio": 1967
    },
    {
        "codigo": "L002",
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "anio": 1943
    },
    {
        "codigo": "L003",
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "anio": 1605
    }
]
codigo_buscado = input("Ingresa el código del libro que buscas: ")

encontrado = False

for libro in libros:
    if libro["codigo"] == codigo_buscado:
        print("\nLibro encontrado:")
        for clave, valor in libro.items():
            print(clave, ":", valor)

        encontrado = True
        break

if not encontrado:
    print("El libro no fue localizado.")

print("\n--- Registrar un nuevo libro ---")

nuevo_codigo = input("Código: ")
codigo_repetido = False

for libro in libros:
    if libro["codigo"] == nuevo_codigo:
        codigo_repetido = True
        break

if codigo_repetido:
    print("Error: ya existe un libro con ese código.")
else:
    nuevo_titulo = input("Título: ")
    nuevo_autor = input("Autor: ")
    nuevo_anio = int(input("Año: "))

    nuevo_libro = {
        "codigo": nuevo_codigo,
        "titulo": nuevo_titulo,
        "autor": nuevo_autor,
        "anio": nuevo_anio
    }

    libros.append(nuevo_libro)
    print("Libro agregado correctamente.")
print("\n--- Catálogo de libros ---")

for libro in libros:
    print("-------------------------")
    for clave, valor in libro.items():
        print(clave, ":", valor)