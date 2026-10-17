
precios = [10000, 20000, 50000, 80000]

precios_con_impuesto = []

for precio in precios:
    nuevo_precio = precio * 1.19
    precios_con_impuesto.append(nuevo_precio)

print("Con for y append():", precios_con_impuesto)


precios_comprension = [precio * 1.19 for precio in precios]

print("Con comprensión:", precios_comprension)

print("¿Los resultados son iguales?:",
      precios_con_impuesto == precios_comprension)