"""
Ejercicio 7: Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara
"""

def operaciones_basicas (a,b):
    suma = a + b
    resta = a - b
    multiplicación = a * b
    división = a / b
    resultados = [suma, resta, multiplicación, división]
    return resultados
    
a = int(input("Ingrese el primer número:"))
b = int(input("Ingrese el segundo número:"))

resultados = []
resultados = operaciones_basicas(a,b)

print("Los resultados son:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")