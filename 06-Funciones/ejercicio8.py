"""
Ejercicio 8: Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para 
mostrar el resultado con dos decimales.
"""

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso (ej: 80.5):"))
altura = float(input("Ingrese su altura (ej: 1.66):"))

resultado = calcular_imc(peso,altura)
print (f"Tiene {peso}kg y {altura}cm, el IMC es de {resultado:.2f}")

