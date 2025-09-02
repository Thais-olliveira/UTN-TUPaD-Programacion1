"""
Ejercicio 2: 
Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”. 
"""
# Solicita al usuario que ingrese su nota;
nota_usuario = int(input("Por favor ingrese su nota: "))
nota_minima = 6
    # Se la nota ingresada es mayor o igual que 6
if nota_usuario >= nota_minima:
    print("Aprobado")
        # Se la nota ingresada es menor que 6
else:
        print("Desaprobado")