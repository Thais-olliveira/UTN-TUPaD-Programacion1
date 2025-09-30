"""
Ejercicio 9: 
Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).  
"""
cuantidad = 100
suma = 0 

for i in range (cuantidad):
    num_entero = int(input("Ingrese el numero: "))
    suma += num_entero
media = suma / cuantidad
print (f"La media de los valores es {media}")