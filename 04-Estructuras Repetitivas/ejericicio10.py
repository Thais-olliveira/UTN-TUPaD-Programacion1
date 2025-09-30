"""
Ejercicio 10: 
Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
num_inverso = ""
num = input("Ingrese un numero:")

for i in num:
    num_inverso = i + num_inverso

print (f"El numero invertido es {num_inverso}")