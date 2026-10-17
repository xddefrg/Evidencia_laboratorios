import calculos
import validaciones


def leer_dato(mensaje, convertir, validar, mensaje_error):
    """Repite la pregunta hasta recibir un dato convertible y válido."""
    while True:
        try:
            valor = convertir(input(mensaje))
        except ValueError:
            print("Debes escribir un número válido.")
            continue

        if validar(valor):
            return valor

        print(mensaje_error)


def main():
    precio = leer_dato(
        "Precio unitario: ", float,
        validaciones.precio_valido, "El precio debe ser mayor que cero."
    )
    cantidad = leer_dato(
        "Cantidad: ", int,
        validaciones.cantidad_valida, "La cantidad debe ser mayor que cero."
    )
    porcentaje_descuento = leer_dato(
        "Descuento (%): ", float,
        validaciones.porcentaje_valido, "El porcentaje debe estar entre 0 y 100."
    )
    porcentaje_impuesto = leer_dato(
        "Impuesto (%): ", float,
        validaciones.porcentaje_valido, "El porcentaje debe estar entre 0 y 100."
    )

    subtotal = calculos.calcular_subtotal(precio, cantidad)
    descuento = calculos.calcular_descuento(subtotal, porcentaje_descuento)
    base = subtotal - descuento
    impuesto = calculos.calcular_impuesto(base, porcentaje_impuesto)
    total = base + impuesto

    print()
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Descuento: {descuento:.2f}")
    print(f"Base después del descuento: {base:.2f}")
    print(f"Impuesto: {impuesto:.2f}")
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
