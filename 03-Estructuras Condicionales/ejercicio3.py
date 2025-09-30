"""
Ejercicio 3: 
Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
operador de módulo (%) en Python para evaluar si un número es par o impar.
"""
# Solicita al usuario que ingrese un numero;
num_usuario = int(input("Por favor ingrese un número par: "))
# Comprueba si el número ingresado es par (si el resto de la división por 2 es igual a 0)
if num_usuario % 2 == 0:
    print ("Ha ingresado un número par")
else: 
    print ("Por favor, ingrese un numero par")