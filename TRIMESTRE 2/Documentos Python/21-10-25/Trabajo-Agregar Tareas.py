
tareas = []  

def agregar_tarea():
    
    tarea = input("Escribe la nueva tarea: ")
    tareas.append({"tarea": tarea, "completada": False})
    print(f"Tarea '{tarea}' agregada exitosamente ✅")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    print("\n--- LISTA DE TAREAS ---")
    for i, t in enumerate(tareas, start=1):
        estado = "〰️" if t["completada"] else "✅"
        print(f"{i}. {t['tarea']} - {estado}")

def completar_tarea():
    mostrar_tareas()
    try:
        num = int(input("Ingrese el número de la tarea a completar: "))
        if 1 <= num <= len(tareas):
            tareas[num - 1]["completada"] = True
            print(f"Tarea '{tareas[num - 1]['tarea']}' marcada como completada.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def eliminar_tarea():
    mostrar_tareas()
    try:
        num = int(input("Ingrese el número de la tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            tarea_eliminada = tareas.pop(num - 1)
            print(f"Tarea '{tarea_eliminada['tarea']}' eliminada.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del gestor de tareas")
            break
        else:
            print("Ingrese una opcion Valida")

# Ejecutar programa
menu()


