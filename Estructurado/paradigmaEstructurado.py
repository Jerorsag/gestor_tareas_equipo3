tareas = []

def agregar_tarea(tarea):
    tareas.append(tarea)

def mostrar_tareas():
    for i, t in enumerate(tareas, 1):
        print(f"{i}. {t}")

def actualizar_tarea(indice, nueva_tarea):
    if 0 <= indice < len(tareas):
        tarea_anterior = tareas[indice]
        tareas[indice] = nueva_tarea
        print(f"Tarea actualizada: '{tarea_anterior}' -> '{nueva_tarea}'")
    else:
        print("Índice de tarea no válido.")

def eliminar_tarea(indice):
    if 0 <= indice < len(tareas):
        tareas.pop(indice)

# Uso:
agregar_tarea("Estudiar para el examen")
agregar_tarea("Hacer ejercicio")
print("\n=== Tareas iniciales ===")
mostrar_tareas()

# Ejemplo de actualización
print("\n=== Actualizando tarea ===")
actualizar_tarea(0, "Estudiar Git y GitHub para el examen")
mostrar_tareas()

print("\n=== Eliminando tarea ===")
eliminar_tarea(0)
mostrar_tareas()