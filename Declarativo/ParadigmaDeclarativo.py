# --- Paradigma Declarativo ---
tareas = ["Cocinar", "Lavar la ropa", "Estudiar"]

# Agregar (nuevo estado)
tareas = [*tareas, "Dormir"]

# Mostrar
[print(f"{i+1}. {t}") for i, t in enumerate(tareas)]

# Actualizar una tarea específica
indice = 0  # índice de la tarea a actualizar
nueva_tarea = "Cocinar pizza"
tareas = [nueva_tarea if i == indice else t for i, t in enumerate(tareas)]

# Eliminar (ej: quitar la segunda tarea)
indice = 1
tareas = [t for i, t in enumerate(tareas) if i != indice]

print("\nDespués de eliminar:")
[print(f"{i+1}. {t}") for i, t in enumerate(tareas)]