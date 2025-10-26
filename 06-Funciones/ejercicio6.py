"""
Ejercicio 6: Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""

def tabla_multiplicar (numero):
    tabla = ""
    for i in range (1, 11):
        tabla += f"{numero} x {i} = {numero * i}\n" 
    return tabla
    
numero = int(input("Ingrese un número:"))

print(tabla_multiplicar(numero))
