"""
Ejercicio 7: 
Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla. 
"""
# Pedimos al usuario que ingrese una frase o palabra
frase_usuario = (input("Por favor ingrese una palavra o frase: "))
#Buscando la ultima posicion de la palabra o frase, el indice -1 siempre significa el ultimo elemento
ultima_letra = frase_usuario[-1]
#Verificar se el valor está dentro de una coleção (aeiou) y .lower() considera las mayusculas también
if ultima_letra.lower() in "aeiou":
#Se si añadir un signo de exclamación
    print(f"{frase_usuario}!")
else:
    #En otro caso, imprimir la frase
    print (frase_usuario)
