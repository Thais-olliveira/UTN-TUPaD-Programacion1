"""
Ejercicio 7: 
Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario. 
"""

num = int(input("Ingrese un numero positivo:"))
total = 0

for i in range (num):
    total += i 

print (f"La suma de los numero compreendidos entre 0 y {num} es {total}.")
