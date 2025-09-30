"""
Ejercicio 2: 
Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. 
"""

num_entero = (input("Ingrese un numero entero:"))
tamaño = 0

for i in num_entero:
    if i == "-": #Caso el numero ingresado sea negativo
        pass    
    else:
        tamaño += 1
print (input(f"Su numero tiene {tamaño} digitos"))