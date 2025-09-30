"""
Ejercicio 6: 
Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. 
"""
#Contagem en orden decreciente del 100 hasta 0 (incluye el 0)
for i in range (100,-1, -1):
    if i % 2 == 0: #Si el resto de la division es 0 el numero es par
        print (i)