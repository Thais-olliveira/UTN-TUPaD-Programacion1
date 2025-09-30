"""
Ejercicio 1: Crear una lista con las notas de 10 estudiantes.
(Mostrar la lista completa; Calcular y mostrar el promedio;Indicar la nota más alta y la más baja)
"""

notas = [5, 8, 5, 9, 7, 9, 6, 3, 0, 10, 10]

print (f"Las notas son:{notas}")
cantidad_notas = len(notas)
for recorrido in range (cantidad_notas -1):
    for indice_actual in range (cantidad_notas -1 - recorrido):
        if notas[indice_actual] > notas[indice_actual + 1]:
            notas[indice_actual], notas[indice_actual + 1] = notas[indice_actual + 1], notas[indice_actual]
            
suma = sum(notas)

promedio = suma / cantidad_notas

print("Notas ordenadas de menor a mayor")
print(notas)
print ("La menor nota es")
print (notas[0])
print ("La mayor nota es")
print (notas[-1])
print(f"El promedio de las notas es {promedio: .2f}")