
unidades_disponibles = 12
unidades_solicitadas = 8

hay_suficientes = unidades_disponibles >= unidades_solicitadas
son_iguales = unidades_disponibles == unidades_solicitadas
solicitadas_mayor = unidades_solicitadas > unidades_disponibles

print(f"¿Hay suficientes unidades?: {hay_suficientes}")
print(f"¿Las cantidades son iguales?: {son_iguales}")
print(f"¿Se solicitaron más unidades de las disponibles?: {solicitadas_mayor}")
