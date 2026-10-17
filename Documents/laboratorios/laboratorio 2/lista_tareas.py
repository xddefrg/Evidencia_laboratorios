tareas = []

while True:
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Consultar cantidad")
    print("0. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nueva_tarea = input("Escribe la nueva tarea: ")

        if nueva_tarea == "":
            print("No puedes agregar una tarea vacía.")
        else:
            tareas.append(nueva_tarea)
            print("Tarea agregada correctamente.")

    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas registradas.")
        else:
            print("\nLista de tareas:")
            for i in range(len(tareas)):
                print(i + 1, "-", tareas[i])

    elif opcion == "3":
        print("Cantidad de tareas:", len(tareas))

    elif opcion == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción desconocida. Intenta de nuevo.")
        