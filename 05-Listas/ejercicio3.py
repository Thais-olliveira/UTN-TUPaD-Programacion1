"""
Ejercicio 3: Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista
"""
#importa random pra crear un numero aleatorio
import random


pares = []
impares = []

for i in range(15):  # 15 números aleatórios
    num_aleatorio = random.randint(1, 100) #Numeros entre 1 y 100

    if num_aleatorio % 2 == 0:
        pares.append(num_aleatorio)
    else:
        impares.append(num_aleatorio)
    #Ordenanado los numeros en orden cresciente
pares_ordenados = sorted (pares)
impares_ordenados = sorted (impares)
#Verificando la cantidad de numeros en cada lista
tamaño_par = (len(pares_ordenados))
tamaño_impar = (len(impares_ordenados))



print(f"Tenemos {tamaño_par} numeros pares y los números son:", pares_ordenados)
print(f"Tenemos {tamaño_impar} numeros impares y los números son:", impares_ordenados)