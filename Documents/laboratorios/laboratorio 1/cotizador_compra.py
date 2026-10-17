
cliente = input("Ingrese el nombre del cliente: ")
producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad a comprar: "))
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento : "))
porcentaje_impuesto = int(input("Ingrese el porcentaje de impuesto: "))

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * (porcentaje_descuento / 100)
base_despues_descuento = subtotal - valor_descuento
valor_impuesto = base_despues_descuento * (porcentaje_impuesto / 100)
total_final = base_despues_descuento + valor_impuesto

print("\n")
print(f"RESUMEN DE LA COTIZACIÓN")
print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad} | Precio Unitario: ${precio_unitario}")

print(f"Subtotal:                      ${subtotal}")
print(f"Valor del Descuento ({porcentaje_descuento}%):       ${valor_descuento}")
print(f"Base después del Descuento:    ${base_despues_descuento}")
print(f"Valor del Impuesto ({porcentaje_impuesto}%):         ${valor_impuesto}")

print(f"TOTAL FINAL:                   ${total_final}")
