import validaciones

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

# Por ahora se supone que los datos numéricos pueden convertirse.
nombre = input("Nombre: ")
categoria = input("Categoría: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

if (
    validaciones.nombre_valido(nombre)
    and validaciones.categoria_valida(categoria, CATEGORIAS)
    and validaciones.precio_valido(precio)
    and validaciones.cantidad_valida(cantidad)
):
    print("Datos aceptados.")
else:
    print("Revisa los datos.")
