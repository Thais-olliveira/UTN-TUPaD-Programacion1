"""
Ejercicio 6: 
Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
"""
#Importa funciones estatiscticas como mode, median y mean del paquete statistics de python
from statistics import mode, median, mean
#Import random para generar números aleatórios
import random
#Crea una lista con 50 números entre 1 y 100
numeros_aleatorios = [random.randint(1,100) for i in range (50)]
#Realiza los calculos de moda, mediana y media para los numeros
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean (numeros_aleatorios)
#Mostra en la pantalla los numeros aleatorios generados
print ("Numeros (1 a 50):", numeros_aleatorios)
print ("Moda:", moda)
print ("Mediana", mediana)
print ("Media", media)
#Media es mayor que la mediana y la mediana es mayor que la moda
if media > mediana and mediana > moda:
    print ("Sesgo positivo o a la derecha")
#Media es menor que la mediana y la mediana es menor que la moda
elif media < mediana and mediana < moda:
    print ("Sesgo negativo o a la izquierda")
else:
    #Media, mediana y moda son iguales
    print ("Sin sesgo")
