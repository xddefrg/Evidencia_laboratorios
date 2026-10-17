'''
Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad de frutos recolectados y la cantidad de frutos producidos en total.
Fórmula:Índice de cosecha = (cantidad de frutos recolectados / cantida cantidad de frutos producidos) * 100%
'''
'''
Un alumno desea saber cuál será su calificación final en la materia de Matemáticas. Dicha siguiente calificación se compone de los porcentajes: 55% del promedio de sus tres calificaciones parciales (se debe leer cada calificación parcial). 30% de la calificación del examen final. 15% de la calificación de un trabajo final.
'''
'''
Recibir una frase y transformarla a mayúscula sostenida e invirtiendo su contenido.
'''

print("bienvenido al sistema de notas, digite su nombre, necesito que digite 5 notas, las primeras 3 valen el 55%, la 4 vale el 30% del la calificacion del examen, y la 5 vale el 15% de un trabajo final")
nombre = input("Digite su nombre \n")
calificacion1 = int(input("Digite la primera nota \n"))
calificacion2 = int(input("Digite la segunda nota \n"))
calificacion3 = int(input("Digite la tercera nota \n"))
calificacion4 = int(input("Digite la cuarta nota \n"))
calificacion5 = int(input("Digite la quinta nota \n"))

calificacion_parciales = (calificacion1 + calificacion2 + calificacion3)/3 * (55/100)
calificacion_examen = calificacion4 * (30/100)
calificacion_trabajo = calificacion5 * (15/100)

calificacion_final = (calificacion_parciales +  calificacion_examen + calificacion_trabajo) 

print("Su calificacion final es:" + str(calificacion_final))


