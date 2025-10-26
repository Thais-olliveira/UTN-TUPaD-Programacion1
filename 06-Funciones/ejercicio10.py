"""
Ejercicio 10: Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""

def calcular_promedio(a,b,c):
    promedio = (a + b + c)/3
    return promedio

a = int(input("Ingrese el primer numero:"))
b = int(input("Ingrese el segundo numero:"))
c = int(input("Ingrese el tercer numero:"))

resultado = calcular_promedio(a,b,c)

print (f"El promedio de los numeros {a},{b},{c} es de {resultado}")

