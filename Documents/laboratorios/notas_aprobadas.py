
notas = [2.5, 3.0, 4.8, 1.9, 3.7, 5.0]
aprobadas = [nota for nota in notas if nota >= 3.0]
reprobadas = [nota for nota in notas if nota < 3.0]
notas_dobles = [nota * 2 for nota in notas]
print("Notas aprobadas:", aprobadas)
print("Notas inferiores a 3.0:", reprobadas)
print("Notas multiplicadas por 2:", notas_dobles)