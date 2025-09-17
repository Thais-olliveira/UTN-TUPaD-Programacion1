"""
Ejercicio 10: 
Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

num = (input("Ingrese un numero:"))

num_inverso = "".join(reversed(num)) #Inverte el numero ingresado con el iterador reversed y converte los caracteres en string

print (f"{num_inverso} es {num} invertido")