"""
Ejercicio 8: 
Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas. 
"""
nombre = (input("Por favor ingrese su nombre: "))
opcion = (input("Elija una opción para mostrar tu nombre.\n 1.Si quiere su nombre en mayúscula.\n 2.Si quiere su nombre en minúscula.\n 3.Si quiere su nombre con la primera letra mayúscula.\n Opción deseada: "))

if opcion == "1":
#La funcíón .upper retorna todo en mayúscula
    print (nombre.upper()) 
elif opcion == "2":
#La funcíón .lower retorna todo en minúscula
    print (nombre.lower())
else:
#La funcíón .titlle retorna la primera en mayúscula
    print (nombre.title())