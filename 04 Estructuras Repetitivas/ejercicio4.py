"""
Ejercicio 4: 
Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. 
"""
num_inicial = -1
suma = 0

#Mientras no se ingrese el 0 el numero va se sumando
while num_inicial != 0:
    num_inicial = int(input("Por favor, escriba un numero (o 0 se desea salir):"))
#Se o numero ingresado es distindo a cero, suma al acumulador
    num = num_inicial + suma
    suma += num

print (f"El valor {suma} es la suma de los numeros")



