"""
Ejercicio 7:  Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
semana. 
• Calcular el promedio de las mínimas y el de las máximas. 
• Mostrar en qué día se registró la mayor amplitud térmica. 
"""
matriz = [
  [10, 18],
  [11, 20],
  [9, 17],
  [12, 21],
  [8, 16],
  [10, 19],
  [11, 22]
]

suma_min = 0
suma_max = 0
contador = 0

maximo = matriz[0][1]   
dia_max = 1             
#Percorre la matriz y con el enumerate pone los numeros de los dias
for dia, (temp_min, temp_max) in enumerate(matriz, start=1):
    suma_min += temp_min
    suma_max += temp_max
    contador += 1

  
    if temp_max > maximo:
        maximo = temp_max
        dia_max = dia
#Calcula el promedio maximo y minimo
media_minima = suma_min / contador
media_maxima = suma_max / contador

print(f"El promedio de la mínima es de: {media_minima:.2f}°C")
print(f"El promedio de la máxima es de: {media_maxima:.2f}°C")
print(f"La mayor amplitud térmica fue de {maximo}°C, en el día {dia_max}")