nombre_producto = "mouse"
cantidad = 45
precio = 50000
porcentaje_descuento = 5
subtotal = precio * cantidad
monto_descuento = subtotal * (porcentaje_descuento / 100)
total_a_pagar = subtotal - monto_descuento

print("\n--- FACTURA SIMPLIFICADA ---")
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento ({porcentaje_descuento}%): -${monto_descuento:.2f}")
print(f"Total a pagar: ${total_a_pagar}")
