def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    # El porcentaje 10 representa 10 %.
    return subtotal * porcentaje / 100


def calcular_impuesto(base, porcentaje):
    # El impuesto se calcula sobre la base recibida.
    return base * porcentaje / 100


precio = 100000
cantidad = 2
porcentaje_descuento = 10
porcentaje_impuesto = 19

# Cada resultado se guarda en una variable antes de imprimirlo.
subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, porcentaje_descuento)
base = subtotal - descuento
impuesto = calcular_impuesto(base, porcentaje_impuesto)
total = base + impuesto

# Se formatea sin decimales porque en este ejemplo todos los valores son enteros.
print(f"Subtotal: {subtotal:.0f}")
print(f"Descuento: {descuento:.0f}")
print(f"Base después del descuento: {base:.0f}")
print(f"Impuesto: {impuesto:.0f}")
print(f"Total: {total:.0f}")
