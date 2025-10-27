"""
Ejercicio 7: Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""

parcial1 = {5, 8, 10, 10, 9}
parcial2 = {6, 7, 5, 10, 10}

print('Estudiantes que aprobaron ambos parciales:', parcial1.intersection(parcial2))
print('Estudiantes que aprobaron solo en uno de los dos:', parcial1.symmetric_difference(parcial2))
print('Estudiantes que aprobaron al menos un parcial:', parcial1.union(parcial2))