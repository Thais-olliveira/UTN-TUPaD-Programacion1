"""
Ejercicio 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y 
devuelva el perímetro del círculo.Solicitar el radio al usuario y llamar ambas funciones 
para mostrar los resultados.
"""
from math import pi

def calcular_area_circulo(radio):
    area_circulo = pi * radio_usuario ** 2
    
    return area_circulo
    
def calcular_perimetro_circulo(radio):
    perimetro_circulo = 2 * pi * radio_usuario
    return perimetro_circulo

radio_usuario = float(input("Ingrese el radio:"))

print(f"El área del círculo es {calcular_area_circulo(radio_usuario)} y el perímetro es {calcular_perimetro_circulo(radio_usuario)}")