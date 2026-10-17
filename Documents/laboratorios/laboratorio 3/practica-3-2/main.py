import operaciones

# El punto indica que la función pertenece al módulo operaciones.
subtotal = operaciones.calcular_subtotal(85000, 3)
descuento = operaciones.calcular_descuento(subtotal, 10)

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total:", subtotal - descuento)
