"""
Ejercicio 5: 
Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
"""
#importa random pra crear un numero aleatorio entre 0 y 9
import random
num_aleatorio = random.randint(0,9)


print ("Juego de la adivinanza: Debes adivinar el numero entre 0 y 9")
#Solicita el numero al usuario y ya arranca el contador con este primero intento
num = int(input("Por favor, ingrese un numero:"))
cont = 1
#Enquanto o numero ingresado es distinto do numero que foi gerado aleatorio ele acrescenta 1 al contador
while num != num_aleatorio:
    print ("No es correcto, ingrese el numero nuevamente")
    num = int (input("Por favor, ingrese un numero:"))
    cont += 1
#Caso el numero ingresado es el mismo, en la pantalla apunta los intentos y cual fue el numero correcto
else:
    print (f"Felicitaciones!! Después de {cont} intentos, adivinastes que {num} es el numero correcto")