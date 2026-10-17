CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

productos = []
opcion = ""

while opcion != "0":
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")

    opcion = input("Opción: ").strip()
    if opcion == "1":
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()

        if codigo == "" or nombre == "" or categoria == "":
            print("Error: los campos de texto no pueden estar vacíos.")

        elif categoria not in CATEGORIAS:
            print("Error: categoría no permitida.")
            print("Categorías válidas:", CATEGORIAS)

        else:
     
            repetido = False

            for producto in productos:
                if producto["codigo"] == codigo:
                    repetido = True
                    break

            if repetido:
                print("Error: el código ya existe.")

            else:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))

                if precio <= 0:
                    print("Error: el precio debe ser mayor que cero.")

                elif cantidad < 0:
                    print("Error: la cantidad no puede ser negativa.")

                else:
                    nuevo_producto = {
                        "codigo": codigo,
                        "nombre": nombre,
                        "categoria": categoria,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    productos.append(nuevo_producto)
                    print("Producto registrado.")

    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados.")

        else:
            print("\n--- LISTA DE PRODUCTOS ---")

            for producto in productos:
                print(
                    producto["codigo"], "-",
                    producto["nombre"], "-",
                    producto["categoria"], "- $",
                    producto["precio"], "-",
                    producto["cantidad"], "unidades"
                )

    elif opcion == "3":
        codigo_buscado = input("Código que deseas buscar: ").strip()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is not None:
            print("\nProducto encontrado:")

            for clave, valor in encontrado.items():
                print(clave, ":", valor)

        else:
            print("El producto no existe.")

    elif opcion == "4":
        codigo_buscado = input("Código del producto: ").strip()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("El producto no existe.")

        else:
            nueva_cantidad = int(input("Nueva cantidad: "))

            if nueva_cantidad < 0:
                print("Error: la cantidad no puede ser negativa.")

            else:
                encontrado["cantidad"] = nueva_cantidad
                print("Existencias actualizadas.")

    elif opcion == "5":
        codigo_buscado = input("Código del producto que deseas eliminar: ").strip()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("El producto no existe.")

        else:
            productos.remove(encontrado)
            print("Producto eliminado correctamente.")


    elif opcion == "6":
        agotados = [
            producto["nombre"]
            for producto in productos
            if producto["cantidad"] == 0
        ]

        if len(agotados) == 0:
            print("No hay productos sin stock.")

        else:
            print("Sin existencias:")

            for nombre in agotados:
                print("-", nombre)
    elif opcion == "7":
        cantidad_productos = len(productos)

        unidades = sum(
            producto["cantidad"]
            for producto in productos
        )

        valor_total = sum(
            producto["precio"] * producto["cantidad"]
            for producto in productos
        )

        categorias_utilizadas = {
            producto["categoria"]
            for producto in productos
        }

        print("\n--- RESUMEN DEL INVENTARIO ---")
        print("Productos:", cantidad_productos)
        print("Unidades:", unidades)
        print("Valor del inventario: $" + str(valor_total))

        print("Categorías utilizadas:")

        if len(categorias_utilizadas) == 0:
            print("Ninguna")

        else:
            for categoria in sorted(categorias_utilizadas):
                print("-", categoria)

    elif opcion == "0":
        print("Programa finalizado.")

    # Opción desconocida
    else:
        print("Opción no válida.")