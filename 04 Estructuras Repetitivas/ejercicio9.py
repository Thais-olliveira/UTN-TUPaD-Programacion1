"""
Ejercicio 9: 
Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).  
"""
#Importa la biblioteca media in statistics
from statistics import mean

cuantidad = 5
num = [] #Lista vacia para almacenar los numeros

for i in range (cuantidad):
    num_entero = int(input("Ingrese el numero: "))
    num.append(num_entero) #Almacena el numero en la lista
#Calcula la media de los numeros almacenados
media =  mean (num)
print (f"La media de los valores es {media}")