notas = [4.0, 3.5, 2.8, 4.5, 3.5, 5.0, 3.0]
print("Tres primeras:", notas[:3])
print("Dos últimas:", notas[-2:])
print("Cantidad total:", len(notas))
print("Notas ordenadas:", sorted(notas))
nota_buscada = 3.5
print("La nota", nota_buscada, "aparece", notas.count(nota_buscada), "veces")

print("Lista original:", notas)