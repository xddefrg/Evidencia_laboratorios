from operaciones import calcular_subtotal, calcular_descuento

# Aquí se importan los nombres directamente, así que se llaman sin el prefijo.
subtotal = calcular_subtotal(40000, 2)
descuento = calcular_descuento(subtotal, 5)

print(subtotal - descuento)
