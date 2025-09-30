"""
Ejercicio 4: 
Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. 
"""
num_inicial = -1
suma = 0

while True:
    num_inicial = int(input("Por favor, escriba un numero (o 0 se desea salir):"))
    if num_inicial == 0:
        break
    suma += num_inicial

print (f"El valor {suma} es la suma de los numeros")



