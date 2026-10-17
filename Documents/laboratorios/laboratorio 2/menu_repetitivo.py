opcion = ""
while opcion != "0":
    print()
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("0. Salir")
    
    opcion = input("Opcion: ").strip()
    if opcion == "1":
        print("Hola.")
    elif opcion == "2":
        print("El programa sigue ejecutandose")
    elif opcion == "0":
        print("programa terminado.")
    else:
        print("opcion no valida")
        