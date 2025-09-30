"""
Ejercicio 3: 
Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.
"""


print("Suma de los numeros compreendidos entre dos valores")
num_inicial = int(input("Ingrese el primero numero:"))
num_final = int(input("Ingrese el segundo numero:"))

suma = 0
#Percore todo los numero entre el primero numero y el segundo
for i in range (num_inicial + 1 , num_final):
    suma += i #En cada repeticion suma 1 al contador

print(f"La suma es:{suma}")
