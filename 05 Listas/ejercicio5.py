"""
Ejercicio 5:  Crear una lista con los nombres de 8 estudiantes presentes en clase. 
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
• Mostrar la lista final actualizada. 
"""
estudiantes = ["Ana", "Guilherme", "Aparecida", "Pedro", "Margarida", "Carlos", "Miguel", "Fernando" ]

print("Lista inicial de estudiantes:")
print(estudiantes)

opcion = int (input("Desea agregar (1) o eliminar (2) un estudiante? "))

if opcion == 1:
    nuevo = (input("Ingrese el nombre del nuevo estudiante: "))
    estudiantes.append(nuevo)

elif opcion == 2:
    borrar = input("Ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("Ese estudiante no está en la lista.")
else:
    print("Operación invalida.")

print("Lista final de estudiantes:")
print(estudiantes)