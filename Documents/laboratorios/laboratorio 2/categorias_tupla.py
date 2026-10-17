categorias = ("Tecnología", "Hogar", "Ropa", "Deportes")
print("Categorías disponibles:")

for i, categoria in enumerate(categorias, start=1):
    print(i, "-", categoria)
categoria_nueva = input("\nEscribe una categoría: ")
categoria_nueva = categoria_nueva.strip()
if categoria_nueva in categorias:
    print("La categoría está permitida.")
else:
    print("La categoría no está disponible.")
print("Cantidad de categorías disponibles:", len(categorias))