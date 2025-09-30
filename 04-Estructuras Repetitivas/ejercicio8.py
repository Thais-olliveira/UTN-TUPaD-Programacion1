"""
Ejercicio 8: 
Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
"""

cuantidad = 100
negativo = 0
positivo = 0
par = 0
impar = 0

for i in range (cuantidad):
    num_entero = int(input("Ingrese el numero: "))
    if num_entero % 2 == 0:
        par += 1
    else:
        impar +=1
    if num_entero < 0:
        negativo +=1
    else:
        positivo +=1
print (f"De estos numeros {negativo} son negativos, {positivo} positivos, y tenemos {par} pares y {impar} impares") 