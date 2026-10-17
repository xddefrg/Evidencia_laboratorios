cantidad = int(input("Cantidad de notas: "))

while cantidad <= 0:
    print("La cantidad debe ser mayor que cero.")
    cantidad = int(input("Cantidad de notas: "))

suma = 0

for i in range(1, cantidad + 1):
    nota = float(input(f"Nota {i}: "))
    suma += nota

promedio = suma / cantidad

print(f"\nPromedio: {promedio}")