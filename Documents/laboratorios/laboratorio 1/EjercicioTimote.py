print("Bienvenido a la plataforma de cursos del sena, actualmente contamos con 3 cusos:")
print("python: 250000")
print("Java: 200000")
print("PHP: 150000")
descuento = 0
valor_curso = 0
nombre = input("Digite su nombre \n")
curso = input("Digite el curso que quiere tomar \n")
if curso == "python":
    valor_curso = 250_000
elif curso == "Java":
    valor_curso = 200_000
elif curso == "PHP":
    valor_curso = 150_000
else:
    print("Dato no valido, vuelvalo a intentar")
estudiante = input("Digite si es estudiante del sena S/N \n")
if estudiante == "S":
    descuento = valor_curso * (30/100)
    print("Descuento aplicado")
elif estudiante == "N":
    print("Bien, descuento no aplicado")
else: 
    print("Dato ingresado no valido, vuelvalo a intentar")
estudiante_adso = input("Es estudiante de ADSO? S/N \n")
if estudiante_adso == "S":
    descuento = valor_curso * (25/100)
elif estudiante_adso == "N":
    print("Bien, descuento no aplicado")
else:
    print("Dato ingresado no valido, vuelvalo a intentar")
edad = int(input("Digite su edad \n"))
if edad < 15 and edad > 25:
    print("No tiene ningun descuento aplicable")
elif edad >= 15 and edad < 20:
    descuento = valor_curso * (15/100)
elif edad >= 20 and edad <= 25:
    descuento = valor_curso * (10/100)
else:
    print("Dato digitado no valido")
precio_final = valor_curso - descuento
print (f"Descuento: ${descuento}")
print (f"total a pagar: ${precio_final}")