edad = int(input("Introduce tu edad: "))
inscripcion = input("¿Estás inscrito? (si/no): ").lower()
documentos = int(input("¿Cuántos documentos has entregado?: "))

if edad >= 16 and inscripcion == "si" and documentos >= 3:
    print("Solicitud aprobada.")
else:
    print("Solicitud rechazada.")