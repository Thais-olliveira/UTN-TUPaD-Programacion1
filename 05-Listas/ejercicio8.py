"""
Ejercicio 8: Crear una matriz con las notas de 5 estudiantes en 3 materias. 
• Mostrar el promedio de cada estudiante. 
• Mostrar el promedio de cada materia. 
"""
matriz = [
    [7, 8, 9],
    [6, 5, 7],
    [9, 8, 10],
    [4, 6, 5],
    [8, 7, 9]
]

contador = 0
suma_mat = 0
suma_org = 0
suma_prog = 0
#Calcula el promedio por materia
for (matematica, programacion, org_empresarial) in matriz:
    suma_mat += matematica
    suma_prog += programacion
    suma_org += org_empresarial
    contador += 1
    
media_mat = suma_mat / contador
media_prog = suma_prog / contador
media_org = suma_org / contador

print("Médias por matéria:")
print(f"Matemática: {media_mat:.2f}")
print(f"Programación: {media_prog:.2f}")
print(f"Org. Empresarial: {media_org:.2f}")
#Calcula el promedio por alumno
for i, fila in enumerate(matriz, start=1):
    media_aluno = sum(fila) / len(fila)
    print(f"Aluno {i}: notas {fila}, média {media_aluno:.2f}")
