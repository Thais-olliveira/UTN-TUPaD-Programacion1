"""
Ejercicio 1: 
Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""
# Solicita al usuario que ingrese su edad;
edad = int(input("Por favor ingrese su edad: "))
# Si el número es mayor o igual que 18
if edad >= 18:
# Se cumpre, muestra la mensaje por pantalla
    print("Es mayor de edad")
else: 
    print("No es mayor de edad")
