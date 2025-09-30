"""
Ejercicio 4:  Dada una lista con valores repetidos: datos: [1, 3, 5, 3, 7, 1, 9, 5, 3]
• Crear una nueva lista sin elementos repetidos. 
• Mostrar el resultado. 
"""
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

cantidad_datos = len(datos)
# Recorremos desde el primer hasta el antiultimo elemento (range va de 0 hasta N-1)
for recorrido in range (cantidad_datos -1):
    for indice_actual in range (cantidad_datos -1 - recorrido):
        if datos[indice_actual] > datos[indice_actual + 1]:
            datos[indice_actual], datos[indice_actual + 1] = datos[indice_actual + 1], datos[indice_actual]
            
print (datos)
datos_sin_repetidos = sorted(set(datos)) #Transforma la lista en un conjunto set, que no permite repeticion
print (datos_sin_repetidos)