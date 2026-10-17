precio = float(input("Introduce el precio del producto: "))

costo_envio1 = "Gratis"
costo_envio2 = 10.000
costo_envio3 = 18.000

if precio >= 200.000:
    costo_envio = costo_envio1
elif precio >= 100.000:
    costo_envio = costo_envio2
else:
    costo_envio = costo_envio3

print(f"Costo del producto: ${precio:,.0f}")
print(f"Costo de envío: {costo_envio if isinstance(costo_envio, str) else f'${costo_envio:,.0f}'}")

if isinstance(costo_envio, (int, float)):
    total = precio + costo_envio
else:
    total = precio

print(f"Total de la compra: ${total:,.0f}")

